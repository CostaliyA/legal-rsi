"""Shared Harvey task/skill/sandbox contract for VERL and API verification.

Only model generation differs between the two frontends.  In particular, an
API run exercises this project's prompt, retrieval, tools and finish logic;
it does not delegate the episode to Harvey LAB's agent_loop.run_agent.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from lab_core.harness import run as harvey
from lab_core.harness.tools import ToolExecutor, get_all_tool_definitions
from lab_core.sandbox.sandbox import Sandbox

from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.skill_router import SkillRouter


_ROUTERS: dict[tuple[int, int, int, str], SkillRouter] = {}


class HarveyEpisode:
    def __init__(
        self,
        task_id: str,
        snapshot: SkillSnapshot,
        run_dir: Path,
        *,
        top_k: int = 3,
        shell_timeout: int = 60,
        max_tool_response_chars: int = 65536,
        retrieval_mode: str = "lexical",
        router_model_checkpoint: str = "fixed-api-model",
    ) -> None:
        self.task = harvey.load_task(task_id)
        self.snapshot = snapshot
        self.run_dir = Path(run_dir)
        self.shell_timeout = shell_timeout
        self.max_tool_response_chars = int(max_tool_response_chars)
        if self.max_tool_response_chars < 1:
            raise ValueError("max_tool_response_chars must be positive")
        self.operation_pattern = task_id.split("/", 1)[1].split("-", 1)[0]
        self.legal_domain = task_id.split("/", 1)[0]
        self.retrieval_mode = retrieval_mode
        self.router_record: dict[str, Any] | None = None
        if retrieval_mode == "hybrid_router":
            key = (8, top_k, 1500, router_model_checkpoint)
            router = _ROUTERS.setdefault(key, SkillRouter(top_k=8, top_n=top_k,
                                                          token_budget=1500,
                                                          model_checkpoint=router_model_checkpoint))
            self.retrieved, self.router_record = router.choose(
                snapshot, task_id, self.task["instructions"], self.operation_pattern, self.legal_domain,
            )
        elif retrieval_mode == "lexical":
            self.retrieved = snapshot.retrieve(
                self.task["instructions"], top_k=top_k,
                operation_pattern=self.operation_pattern, legal_domain=self.legal_domain,
            )
        else:
            raise ValueError(f"Unknown retrieval mode: {retrieval_mode}")
        self.skill_context = snapshot.render(self.retrieved) if self.retrieved else ""
        base_system = harvey.build_system_preamble(True) + harvey.load_skills(list(harvey.DEFAULT_SKILLS))
        self.messages = [
            {"role": "system", "content": base_system + ("\n\n" + self.skill_context if self.skill_context else "")},
            {"role": "user", "content": self.task["instructions"]},
        ]
        self.tools = get_all_tool_definitions(enable_finish=True)
        self.sandbox: Sandbox | None = None
        self.executor: ToolExecutor | None = None

    def start(self) -> None:
        output_dir = self.run_dir / "output"
        workspace_dir = self.run_dir / "workspace"
        output_dir.mkdir(parents=True, exist_ok=False)
        workspace_dir.mkdir(parents=True, exist_ok=False)
        sandbox = Sandbox(
            documents_dir=Path(self.task["docs_dir"]),
            output_dir=output_dir,
            workspace_dir=workspace_dir,
            default_timeout=self.shell_timeout,
        )
        self.sandbox = sandbox
        try:
            sandbox.start()
            harvey.setup_skill_scripts(list(harvey.DEFAULT_SKILLS), workspace_dir)
            self.executor = ToolExecutor(sandbox=sandbox, shell_timeout=self.shell_timeout, enable_finish=True)
        except BaseException:
            sandbox.stop()
            raise

    def execute(self, name: str, arguments: dict[str, Any] | str) -> str:
        if self.executor is None:
            raise RuntimeError("Harvey episode has not started")
        result = self.executor.execute(name, arguments)
        if len(result) > self.max_tool_response_chars:
            return result[: self.max_tool_response_chars] + "...(truncated)"
        return result

    @property
    def finished(self) -> bool:
        return bool(self.executor and self.executor.finished)

    def close(self) -> None:
        if self.sandbox is not None:
            self.sandbox.stop()

    def metadata(self) -> dict[str, Any]:
        return {
            "task_id": self.task["name"],
            "operation_pattern": self.operation_pattern,
            "legal_domain": self.legal_domain,
            "skill_snapshot_id": self.snapshot.snapshot_id,
            "retrieved_skill_ids": [item.skill.skill_id for item in self.retrieved],
            "retrieved_skill_hashes": [item.skill.content_hash for item in self.retrieved],
            "retrieval_scores": [item.score for item in self.retrieved],
            "retrieval_mode": self.retrieval_mode,
            "router_record": self.router_record,
            "max_tool_response_chars": self.max_tool_response_chars,
            "finished": self.finished,
        }

    def write_metadata(self) -> None:
        (self.run_dir / "rollout_metadata.json").write_text(
            json.dumps(self.metadata(), ensure_ascii=False, indent=2), encoding="utf-8"
        )
