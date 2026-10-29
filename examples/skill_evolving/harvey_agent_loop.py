"""Trainable VERL multi-turn rollout against an isolated Harvey LAB task.

The model is VERL's rollout server. Harvey supplies the task, prompt, tool
definitions, skill manuals and sandbox. One coroutine owns one ToolExecutor;
the immutable skill snapshot is pinned by the trainer's group configuration.
"""

from __future__ import annotations

import asyncio
import json
import tempfile
import weakref
from pathlib import Path
from typing import Any

from pydantic import ConfigDict

from lab_core.harness.tools import ToolExecutor, get_all_tool_definitions

from verl.experimental.agent_loop.agent_loop import AgentLoopOutput, ToolListWrap
from verl.experimental.agent_loop.tool_agent_loop import AgentState, ToolAgentLoop
from verl.tools.function_tool import FunctionTool
from verl.tools.schemas import (
    OpenAIFunctionParametersSchema,
    OpenAIFunctionPropertySchema,
    OpenAIFunctionSchema,
    OpenAIFunctionToolSchema,
    ToolResponse,
)

from examples.skill_evolving.skill_store import SkillSnapshot, find_token_span
from examples.skill_evolving.harvey_episode import HarveyEpisode
from examples.skill_evolving.harvey_reward import score_episode


_SANDBOX_SLOTS: weakref.WeakKeyDictionary = weakref.WeakKeyDictionary()


class _HarveyProperty(OpenAIFunctionPropertySchema):
    model_config = ConfigDict(extra="allow")


class _HarveyParameters(OpenAIFunctionParametersSchema):
    properties: dict[str, _HarveyProperty]


class _HarveyFunction(OpenAIFunctionSchema):
    parameters: _HarveyParameters


class _HarveyToolSchema(OpenAIFunctionToolSchema):
    function: _HarveyFunction


def harvey_tool_carriers() -> ToolListWrap:
    """Give VERL's parser Harvey's official schemas; dispatch stays local."""

    def never_called(**_kwargs):
        raise RuntimeError("Harvey tool dispatch must use the per-trajectory executor")

    tools = []
    for definition in get_all_tool_definitions(enable_finish=True):
        schema = _HarveyToolSchema.model_validate({"type": "function", "function": definition})
        tools.append(FunctionTool(name=definition["name"], fn=never_called, tool_schema=schema))
    return ToolListWrap(tools)


class HarveySkillAgentLoop(ToolAgentLoop):
    def __init__(
        self,
        *args,
        skill_library_path: str,
        expected_snapshot_id: str,
        artifact_root: str,
        top_k: int = 3,
        shell_timeout: int = 60,
        judge_model: str = "",
        judge_parallel: int = 2,
        max_concurrent_sandboxes: int = 4,
        harvey_max_turns: int = 200,
        max_harvey_tool_chars: int = 65536,
        retrieval_mode: str = "lexical",
        router_model_checkpoint: str = "native-actor",
        **kwargs,
    ):
        # The worker's shared tools are replaced by Harvey's seven schemas.
        kwargs["tools"] = harvey_tool_carriers()
        super().__init__(*args, **kwargs)
        source = Path(skill_library_path)
        if not source.is_absolute():
            source = Path(__file__).resolve().parent / source
        self.snapshot = SkillSnapshot.load(source)
        if self.snapshot.snapshot_id != expected_snapshot_id:
            raise ValueError("Configured Harvey skill snapshot ID does not match the file")
        self.top_k = int(top_k)
        self.retrieval_mode = retrieval_mode
        self.router_model_checkpoint = router_model_checkpoint
        self.artifact_root = Path(artifact_root).expanduser().resolve()
        self.shell_timeout = int(shell_timeout)
        self.judge_model = judge_model
        self.judge_parallel = int(judge_parallel)
        self.max_concurrent_sandboxes = int(max_concurrent_sandboxes)
        if self.max_concurrent_sandboxes < 1:
            raise ValueError("max_concurrent_sandboxes must be positive")
        self.max_assistant_turns = int(harvey_max_turns)
        self.max_tool_response_length = int(max_harvey_tool_chars)
        self.executor: ToolExecutor | None = None
        self.episode: HarveyEpisode | None = None
        self._tool_lock = asyncio.Lock()
        self.trace: list[dict[str, Any]] = []
        # Accept every tool call in a model turn; the lock serializes access to
        # Harvey's mutable cwd and filesystem inside this trajectory.
        self.max_parallel_calls = 16

    async def run(self, sampling_params: dict[str, Any], priority: int = 0, **kwargs) -> AgentLoopOutput:
        extra_info = kwargs.get("extra_info") or {}
        task_id = extra_info.get("harvey_task_id")
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("Each Harvey sample needs extra_info.harvey_task_id")
        self.artifact_root.mkdir(parents=True, exist_ok=True)
        requested_dir = kwargs.get("harvey_run_dir")
        if requested_dir is None:
            run_dir = Path(tempfile.mkdtemp(prefix="harvey-", dir=self.artifact_root))
        else:
            run_dir = Path(requested_dir).resolve()
            if not run_dir.is_relative_to(self.artifact_root) or run_dir == self.artifact_root:
                raise ValueError("Harvey run directory must be inside artifact_root")
            run_dir.mkdir(parents=True, exist_ok=False)
        episode = HarveyEpisode(task_id, self.snapshot, run_dir, top_k=self.top_k,
                                shell_timeout=self.shell_timeout,
                                max_tool_response_chars=self.max_tool_response_length,
                                retrieval_mode=self.retrieval_mode,
                                router_model_checkpoint=getattr(self, "model", self.router_model_checkpoint))
        self.episode = episode
        event_loop = asyncio.get_running_loop()
        slots = _SANDBOX_SLOTS.get(event_loop)
        if slots is None:
            slots = asyncio.Semaphore(self.max_concurrent_sandboxes)
            _SANDBOX_SLOTS[event_loop] = slots
        await slots.acquire()
        try:
            await asyncio.to_thread(episode.start)
            self.executor = episode.executor
            self.trace = []
            child_kwargs = dict(kwargs)
            child_kwargs["raw_prompt"] = episode.messages
            output = await super().run(sampling_params, priority=priority, **child_kwargs)
            output.extra_fields.update(
                {
                    "harvey_task_id": task_id,
                    "harvey_run_dir": str(run_dir),
                    "harvey_finished": self.executor.finished,
                    "harvey_finish_summary": self.executor.finish_summary,
                    "skill_snapshot_id": self.snapshot.snapshot_id,
                    "retrieved_skill_ids": episode.metadata()["retrieved_skill_ids"],
                    "retrieved_skill_hashes": episode.metadata()["retrieved_skill_hashes"],
                    "retrieval_mode": episode.metadata()["retrieval_mode"],
                    "router_record": episode.metadata()["router_record"],
                    "injected_skill_token_span": (
                        find_token_span(self.tokenizer, output.prompt_ids, episode.skill_context)
                        if episode.skill_context else None
                    ),
                }
            )
            episode.write_metadata()
            with (run_dir / "transcript.jsonl").open("w", encoding="utf-8") as stream:
                for row in self.trace:
                    stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            if self.judge_model:
                scores = await asyncio.to_thread(score_episode, episode.task, run_dir, self.judge_model, self.judge_parallel)
                output.reward_score = scores["reward_task"]
                output.extra_fields["harvey_score"] = scores["score"]
                output.extra_fields["harvey_max_score"] = scores["max_score"]
            return output
        finally:
            try:
                await asyncio.to_thread(episode.close)
                self.executor = None
                self.episode = None
            finally:
                slots.release()

    async def _call_tool(self, tool_call, tools_kwargs, agent_data):
        if self.episode is None or self.executor is None:
            raise RuntimeError("Harvey sandbox is not active")
        if tool_call.name not in self.tools:
            return ToolResponse(text=f"Unknown Harvey tool: {tool_call.name}"), 0.0, {}
        try:
            arguments = json.loads(tool_call.arguments)
            if not isinstance(arguments, dict):
                raise ValueError("arguments must be an object")
        except (ValueError, TypeError) as exc:
            return ToolResponse(text=f"Invalid Harvey tool arguments: {exc}"), 0.0, {}
        async with self._tool_lock:
            result = await asyncio.to_thread(self.episode.execute, tool_call.name, arguments)
        return ToolResponse(text=result), 0.0, {}

    async def _handle_generating_state(self, agent_data, sampling_params, ignore_termination=False):
        previous_count = len(agent_data.messages)
        state = await super()._handle_generating_state(agent_data, sampling_params, ignore_termination)
        if len(agent_data.messages) > previous_count:
            message = agent_data.messages[-1]
            self.trace.append(
                {
                    "turn": agent_data.assistant_turns,
                    "role": "assistant",
                    "text": message.get("content", ""),
                    "tool_calls": message.get("tool_calls", []),
                }
            )
        return state

    async def _handle_processing_tools_state(self, agent_data):
        previous_count = len(agent_data.messages)
        next_state = await super()._handle_processing_tools_state(agent_data)
        for message in agent_data.messages[previous_count:]:
            self.trace.append(
                {"turn": agent_data.assistant_turns, "role": "tool", "result": message.get("content", "")}
            )
        if self.executor is not None and self.executor.finished:
            return AgentState.TERMINATED
        return next_state
