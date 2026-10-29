"""API verification through VERL's ToolAgentLoop state machine.

This bridge keeps VERL's PENDING/GENERATING/PROCESSING_TOOLS transitions and
HarveySkillAgentLoop's per-trajectory sandbox dispatch. The provider returns
structured calls but no policy token IDs or old log probabilities, so the
output carries only non-trainable placeholder IDs and is never fed to PPO.
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from types import SimpleNamespace

from lab_core.harness.adapters.openai import OpenAIAdapter

from verl.experimental.agent_loop.tool_agent_loop import AgentState
from verl.experimental.agent_loop.tool_parser import FunctionCall

from examples.skill_evolving.harvey_agent_loop import HarveySkillAgentLoop, harvey_tool_carriers
from examples.skill_evolving.skill_store import SkillSnapshot


class _NoPolicyTokenizer:
    def encode(self, text: str, **_kwargs) -> list[int]:
        return list(text.encode("utf-8"))


class ApiHarveySkillAgentLoop(HarveySkillAgentLoop):
    """Execute the real VERL tool state machine with an API generation step."""

    def __init__(self, *, snapshot: SkillSnapshot, artifact_root: Path, model: str,
                 temperature: float, max_turns: int = 200, top_k: int = 3,
                 max_concurrent_sandboxes: int = 4, retrieval_mode: str = "lexical"):
        # The normal constructor requires a local actor and rollout server.
        # Set only fields consumed by ToolAgentLoop.run and Harvey's hooks.
        self.snapshot = snapshot
        self.artifact_root = Path(artifact_root).resolve()
        self.top_k = top_k
        self.retrieval_mode = retrieval_mode
        self.router_model_checkpoint = model
        self.shell_timeout = 60
        self.judge_model = ""
        self.judge_parallel = 2
        self.max_concurrent_sandboxes = max_concurrent_sandboxes
        self.max_assistant_turns = max_turns
        self.max_user_turns = None
        self.max_parallel_calls = 64
        self.max_tool_response_length = 65536
        self.response_length = 20000
        self.rollout_config = SimpleNamespace(full_determinism=False)
        self.processor = None
        self.mm_processor_kwargs = {}
        self.tokenizer = _NoPolicyTokenizer()
        self.tools = {tool.name: tool for tool in harvey_tool_carriers().tools}
        self.tool_schemas = [tool.tool_schema.model_dump(exclude_unset=True, exclude_none=True)
                             for tool in self.tools.values()]
        self.executor = None
        self.episode = None
        self._tool_lock = asyncio.Lock()
        self.trace = []
        self.model = model
        self.temperature = temperature
        self.adapter: OpenAIAdapter | None = None
        self.usage = {"input_tokens": 0, "output_tokens": 0}

    async def run(self, sampling_params: dict, priority: int = 0, **kwargs):
        self.adapter = OpenAIAdapter(model=self.model, temperature=self.temperature, openai_hosted=False)
        output = await super().run(sampling_params, priority=priority, **kwargs)
        output.extra_fields.update({
            "api_test_only": True,
            "native_policy_token_ids_available": False,
            "native_old_log_probs_available": False,
            "model": self.model,
            "temperature": self.temperature,
            "usage": self.usage,
        })
        metadata_path = Path(output.extra_fields["harvey_run_dir"]) / "rollout_metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata.update({
            "api_test_only": True,
            "native_policy_token_ids_available": False,
            "native_old_log_probs_available": False,
            "verl_state_machine": "ToolAgentLoop.run",
            "model": self.model,
            "temperature": self.temperature,
            "usage": self.usage,
            "turn_count": sum(row["role"] == "assistant" for row in self.trace),
            "finished": output.extra_fields["harvey_finished"],
        })
        metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        return output

    async def _handle_pending_state(self, agent_data, sampling_params):
        # A sentinel is only a state-machine placeholder; it is not a model ID.
        agent_data.prompt_ids = [0]
        return AgentState.GENERATING

    async def _handle_generating_state(self, agent_data, sampling_params, ignore_termination=False):
        assert self.adapter is not None and self.episode is not None
        if agent_data.assistant_turns == 0:
            self.adapter.make_system_message(self.episode.messages[0]["content"])
        response = await asyncio.to_thread(self.adapter.chat, agent_data.messages, self.episode.tools)
        self.usage["input_tokens"] += response.input_tokens
        self.usage["output_tokens"] += response.output_tokens
        agent_data.assistant_turns += 1
        agent_data.prompt_ids.append(0)
        agent_data.response_mask.append(0)
        agent_data.response_ids = [0]
        agent_data.tool_calls = [FunctionCall(name=call.name, arguments=call.arguments,
                                              tool_call_id=call.id) for call in response.tool_calls]
        if len(agent_data.tool_calls) > self.max_parallel_calls:
            raise ValueError("API returned more tool calls than the VERL rollout can execute")
        agent_data.messages.append(self._build_assistant_message(response.text, agent_data))
        self.trace.append({
            "turn": agent_data.assistant_turns,
            "role": "assistant",
            "text": response.text,
            "tool_calls": [{"id": call.id, "name": call.name, "arguments": call.arguments}
                           for call in response.tool_calls],
            "input_tokens": response.input_tokens,
            "output_tokens": response.output_tokens,
            "finish_reason": response.finish_reason,
        })
        if agent_data.assistant_turns >= self.max_assistant_turns:
            return AgentState.TERMINATED
        return AgentState.PROCESSING_TOOLS if agent_data.tool_calls else AgentState.TERMINATED

    async def ct_merge_context_msg(self, previous_messages, updated_messages, runtime_token_ids,
                                   response_mask, response_logprobs=None, tools=None):
        # ToolAgentLoop's tool processing owns message construction and transition.
        # IDs are explicit placeholders because the API supplies no actor tokens.
        added = len(updated_messages) - len(previous_messages)
        ids = runtime_token_ids + [0] * added
        return SimpleNamespace(token_ids=ids), response_mask + [0] * added, None

    async def _handle_processing_tools_state(self, agent_data):
        before = len(agent_data.messages)
        state = await super()._handle_processing_tools_state(agent_data)
        assert self.adapter is not None
        replies = [(msg["tool_call_id"], msg["content"])
                   for msg in agent_data.messages[before:] if msg.get("role") == "tool"]
        for row, call in zip(self.trace[-len(replies):], agent_data.tool_calls):
            row.update({"tool_call_id": call.tool_call_id, "tool_name": call.name,
                        "arguments": call.arguments})
        self.adapter.make_tool_result_messages(replies)
        return state
