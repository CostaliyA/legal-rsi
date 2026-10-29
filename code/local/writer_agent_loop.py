"""VERL policy episode that authors one staged skill-maintenance action."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from verl.experimental.agent_loop.agent_loop import AgentLoopOutput
from verl.experimental.agent_loop.single_turn_agent_loop import SingleTurnAgentLoop

from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.writer_policy import parse_writer_action
from examples.skill_evolving.writer_prompt import build_writer_messages


class HarveySkillWriterAgentLoop(SingleTurnAgentLoop):
    def __init__(self, *args, skill_library_path: str, expected_snapshot_id: str, candidate_root: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.snapshot = SkillSnapshot.load(skill_library_path)
        if self.snapshot.snapshot_id != expected_snapshot_id:
            raise ValueError("Writer snapshot does not match the pinned group")
        self.candidate_root = Path(candidate_root).expanduser().resolve()

    async def run(self, sampling_params: dict[str, Any], priority: int = 0, **kwargs) -> AgentLoopOutput:
        extra_info = kwargs.get("extra_info") or {}
        sources = extra_info.get("source_run_dirs")
        if not isinstance(sources, list):
            raise ValueError("Writer sample needs extra_info.source_run_dirs")
        child_kwargs = dict(kwargs)
        child_kwargs["raw_prompt"] = build_writer_messages(self.snapshot, sources)
        output = await super().run(sampling_params, priority=priority, **child_kwargs)
        text = self.tokenizer.decode(output.response_ids, skip_special_tokens=True)
        author_mask = list(output.response_mask)
        try:
            proposal = parse_writer_action(text, self.snapshot)
            error = None
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            proposal = None
            error = str(exc)
        phase = extra_info.get("phase", "train")
        if proposal is not None and phase == "train":
            self.candidate_root.mkdir(parents=True, exist_ok=True)
            path = self.candidate_root / f"{proposal['candidate_id']}.json"
            try:
                with path.open("x", encoding="utf-8") as stream:
                    json.dump({**proposal, "source_runs": sources}, stream, ensure_ascii=False, indent=2)
            except FileExistsError:
                existing = json.loads(path.read_text(encoding="utf-8"))
                if existing["candidate_id"] != proposal["candidate_id"]:
                    raise
        output.extra_fields.update(
            {
                "skill_snapshot_id": self.snapshot.snapshot_id,
                "candidate_id": proposal["candidate_id"] if proposal else None,
                "candidate_action": proposal["action"] if proposal else None,
                "candidate_valid": proposal is not None,
                "candidate_error": error,
                "candidate_parent_snapshot_id": self.snapshot.snapshot_id,
                "skill_author_mask": author_mask,
                "skill_author_token_count": sum(author_mask),
                "source_run_dirs": sources,
                "phase": phase,
                "raw_writer_action": text,
                "writer_trace_root": str(self.candidate_root / "reward_traces"),
            }
        )
        return output
