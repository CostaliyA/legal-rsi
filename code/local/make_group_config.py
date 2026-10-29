"""Write an immutable VERL agent-loop config pinned to one skill snapshot."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from examples.skill_evolving.skill_store import SkillSnapshot


def make_config(snapshot_path: Path, output_path: Path, artifact_root: Path, judge_model: str = "",
                retrieval_mode: str = "lexical", router_model_checkpoint: str = "native-actor") -> dict:
    if retrieval_mode not in {"lexical", "hybrid_router"}:
        raise ValueError("Unknown retrieval mode")
    if retrieval_mode == "hybrid_router" and router_model_checkpoint == "native-actor":
        raise ValueError("Hybrid Router config needs an explicit actor checkpoint ID")
    snapshot = SkillSnapshot.load(snapshot_path)
    config = [
        {
            "name": "harvey_skill_agent",
            "_target_": "examples.skill_evolving.harvey_agent_loop.HarveySkillAgentLoop",
            "skill_library_path": str(snapshot_path.resolve()),
            "expected_snapshot_id": snapshot.snapshot_id,
            "artifact_root": str(artifact_root.resolve()),
            "judge_model": judge_model,
            "judge_parallel": 2,
            "max_concurrent_sandboxes": 4,
            "harvey_max_turns": 200,
            "max_harvey_tool_chars": 65536,
            "top_k": 3,
            "retrieval_mode": retrieval_mode,
            "router_model_checkpoint": router_model_checkpoint,
            "shell_timeout": 60,
        },
        {
            "name": "harvey_skill_writer",
            "_target_": "examples.skill_evolving.writer_agent_loop.HarveySkillWriterAgentLoop",
            "skill_library_path": str(snapshot_path.resolve()),
            "expected_snapshot_id": snapshot.snapshot_id,
            "candidate_root": str((artifact_root / "candidates").resolve()),
        },
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("x", encoding="utf-8") as stream:
        json.dump(config, stream, ensure_ascii=False, indent=2)
    return {"config_path": str(output_path.resolve()), "snapshot_id": snapshot.snapshot_id}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--judge-model", default="")
    parser.add_argument("--retrieval-mode", choices=["lexical", "hybrid_router"], default="lexical")
    parser.add_argument("--router-model-checkpoint", default="native-actor")
    args = parser.parse_args()
    print(json.dumps(make_config(args.snapshot, args.output, args.artifact_root, args.judge_model,
                                 args.retrieval_mode, args.router_model_checkpoint), indent=2))


if __name__ == "__main__":
    main()
