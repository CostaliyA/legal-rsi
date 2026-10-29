"""Create one VERL prompt group whose rollout.n samples Writer actions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from examples.skill_evolving.skill_store import SkillSnapshot


def prepare(
    source_summary: Path, manifest_path: Path, snapshot_path: Path,
    output_path: Path, artifact_root: Path, reference_model: str,
    judge_model: str, current_model: str = "",
) -> dict:
    snapshot = SkillSnapshot.load(snapshot_path)
    source_rows = json.loads(source_summary.read_text(encoding="utf-8"))
    sources = [row["run_dir"] for row in source_rows if row["status"] == "complete"]
    source_tasks = [row["task_id"] for row in source_rows if row["status"] == "complete"]
    if len(sources) < 10:
        raise ValueError("Need ten completed source rollouts")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    probes = manifest["credit_probe"]
    if len(probes) < 2 or set(probes) & (set(source_tasks) | set(manifest["final"])):
        raise ValueError("Credit probes must be separate from source and final tasks")
    row = {
        "data_source": "harvey_skill_writer",
        "prompt": [{"role": "user", "content": "Propose one reusable skill action from the provided trajectories."}],
        "agent_name": "harvey_skill_writer",
        "extra_info": {"index": 0, "source_run_dirs": sources,
                       "source_task_ids": source_tasks, "phase": "train"},
        "reward_model": {
            "ground_truth": {
                "snapshot_path": str(snapshot_path.resolve()),
                "snapshot_id": snapshot.snapshot_id,
                "probe_tasks": probes,
                "artifact_root": str(artifact_root.resolve()),
                "reference_model": reference_model,
                "current_model": current_model or None,
                "judge_model": judge_model,
                "alpha": 0.7,
            }
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([row]).to_parquet(output_path, index=False)
    return {"writer_data": str(output_path.resolve()), "snapshot_id": snapshot.snapshot_id,
            "source_trajectories": len(sources), "credit_probes": probes}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-summary", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--reference-model", default="deepseek-flash")
    parser.add_argument("--current-model", default="")
    parser.add_argument("--judge-model", default="deepseek-flash")
    args = parser.parse_args()
    print(json.dumps(prepare(args.source_summary, args.manifest, args.snapshot, args.output,
                             args.artifact_root, args.reference_model, args.judge_model,
                             args.current_model), indent=2))


if __name__ == "__main__":
    main()
