"""Commit one evaluated Writer action after the five-task confirmation barrier."""

from __future__ import annotations

import argparse
import json
import math
import os
import uuid
from pathlib import Path

from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.writer_policy import stage_action_snapshot


def create_trial(parent_path: Path, candidate_path: Path, output_path: Path) -> dict:
    parent = SkillSnapshot.load(parent_path)
    action = json.loads(candidate_path.read_text(encoding="utf-8"))
    trial = stage_action_snapshot(parent, action, output_path)
    return {"trial_snapshot_path": str(output_path.resolve()), "trial_snapshot_id": trial.snapshot_id,
            "candidate_id": action["candidate_id"], "parent_snapshot_id": parent.snapshot_id}


def commit(
    parent_path: Path, trial_path: Path, paired_summary_path: Path, output_path: Path,
    *, max_regression: float = 0.0, expected_pairs: int = 5,
) -> dict:
    parent = SkillSnapshot.load(parent_path)
    trial = SkillSnapshot.load(trial_path)
    trial_payload = json.loads(trial_path.read_text(encoding="utf-8"))
    if trial_payload.get("parent_snapshot_id") != parent.snapshot_id or not trial_payload.get("candidate_id"):
        raise ValueError("Trial was not staged from the requested parent")
    summary = json.loads(paired_summary_path.read_text(encoding="utf-8"))
    pairs = summary.get("pairs", [])
    if len(pairs) != expected_pairs or len({pair["task_id"] for pair in pairs}) != expected_pairs:
        raise ValueError(f"Exactly {expected_pairs} distinct confirmation pairs are required")
    if summary.get("old_snapshot_id") != parent.snapshot_id or summary.get("new_snapshot_id") != trial.snapshot_id:
        raise ValueError("Confirmation did not compare the requested snapshots")
    deltas = []
    for pair in pairs:
        if pair.get("old_snapshot_id") != parent.snapshot_id or pair.get("new_snapshot_id") != trial.snapshot_id:
            raise ValueError("Confirmation pair used the wrong snapshot")
        rewards = []
        for side, expected_snapshot in (("old", parent.snapshot_id), ("new", trial.snapshot_id)):
            run_dir = Path(pair[f"{side}_run_dir"])
            scores = json.loads((run_dir / "scores.json").read_text(encoding="utf-8"))
            metadata = json.loads((run_dir / "rollout_metadata.json").read_text(encoding="utf-8"))
            if (scores.get("task_id") != pair["task_id"] or metadata.get("task_id") != pair["task_id"]
                    or metadata.get("skill_snapshot_id") != expected_snapshot
                    or scores.get("n_grading_errors") != 0
                    or not (run_dir / "transcript.jsonl").exists()):
                raise ValueError("Confirmation pair lacks matching complete rollout evidence")
            reward = float(scores["reward_task"])
            if not math.isclose(reward, float(pair[f"{side}_reward_task"]), abs_tol=1e-9):
                raise ValueError("Confirmation reward differs from its score artifact")
            rewards.append(reward)
        delta = rewards[1] - rewards[0]
        if not math.isclose(delta, float(pair["delta_api"]), abs_tol=1e-9):
            raise ValueError("Confirmation delta differs from its score artifacts")
        deltas.append(delta)
    if not math.isclose(sum(deltas) / len(deltas), float(summary["mean_delta_api"]), abs_tol=1e-9):
        raise ValueError("Confirmation mean differs from its pairs")
    if sum(deltas) <= 0 or min(deltas) < -max_regression:
        raise ValueError("Candidate failed positive-gain and non-regression gate")
    if summary.get("mode") != "api_protocol_and_frozen_model_reward":
        raise ValueError("Unrecognized confirmation mode")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Publish a separate immutable inode. Hard-linking the trial itself would
    # let a later edit to staging silently mutate the published snapshot.
    temporary = output_path.with_name(f".{output_path.name}.{uuid.uuid4().hex}.tmp")
    try:
        with temporary.open("xb") as stream:
            stream.write(trial_path.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
        if SkillSnapshot.load(temporary).snapshot_id != trial.snapshot_id:
            raise ValueError("Copied trial snapshot changed during publication")
        temporary.chmod(0o444)
        os.link(temporary, output_path)
    finally:
        temporary.unlink(missing_ok=True)
    record = {
        "parent_snapshot_id": parent.snapshot_id,
        "published_snapshot_id": trial.snapshot_id,
        "candidate_id": trial_payload["candidate_id"],
        "confirmation_summary": str(paired_summary_path.resolve()),
        "mean_delta": sum(deltas) / len(deltas),
        "min_delta": min(deltas),
        "output_path": str(output_path.resolve()),
    }
    (output_path.with_suffix(output_path.suffix + ".commit.json")).write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", required=True, type=Path)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--trial", required=True, type=Path)
    parser.add_argument("--paired-summary", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-regression", type=float, default=0.0)
    parser.add_argument("--expected-pairs", type=int, default=5)
    args = parser.parse_args()
    if args.candidate:
        result = create_trial(args.parent, args.candidate, args.trial)
    else:
        if not args.paired_summary or not args.output:
            parser.error("--paired-summary and --output are required for commit")
        result = commit(args.parent, args.trial, args.paired_summary,
                        args.output, max_regression=args.max_regression, expected_pairs=args.expected_pairs)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
