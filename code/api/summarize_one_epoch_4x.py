"""Verify and summarize one 4x4 VERL/API skill-evolution epoch."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import stat
import uuid
from pathlib import Path

from examples.skill_evolving.harvey_reward import reward_from_counts
from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.candidate_barrier import resolve_evaluated
from examples.skill_evolving.skill_router import ROUTER_VERSION


def _read_side(summary_path: Path, snapshot: SkillSnapshot, tasks: list[str],
               temperature: float, model: str, judge_model: str,
               retrieval_mode: str = "lexical") -> dict[tuple[str, int], dict]:
    rows = json.loads(summary_path.read_text(encoding="utf-8"))
    expected = {(task, sample) for task in tasks for sample in range(1, 5)}
    keys = {(row["task_id"], row["sample_index"]) for row in rows}
    if len(rows) != len(expected) or keys != expected:
        raise ValueError(f"Expected {len(tasks)} tasks x 4 samples: {summary_path}")
    checked = {}
    for row in rows:
        if row["status"] != "complete":
            raise ValueError(f"Incomplete rollout: {row['run_dir']}")
        run_dir = Path(row["run_dir"])
        metadata = json.loads((run_dir / "rollout_metadata.json").read_text(encoding="utf-8"))
        scores = json.loads((run_dir / "scores.json").read_text(encoding="utf-8"))
        feedback_path = run_dir / scores["rubric_feedback_file"]
        all_pass, fraction, reward = reward_from_counts(
            scores["n_passed"], scores["n_criteria"], scores.get("beta", 0.2)
        )
        if (metadata["task_id"] != row["task_id"] or scores["task_id"] != row["task_id"]
                or metadata["skill_snapshot_id"] != snapshot.snapshot_id
                or metadata.get("temperature") != temperature
                or metadata.get("model") != model or scores.get("judge_model") != judge_model
                or metadata.get("sample_index") != row["sample_index"]
                or metadata.get("verl_state_machine") != "ToolAgentLoop.run"
                or not metadata.get("finished")
                or metadata.get("retrieval_mode", "lexical") != retrieval_mode
                or not metadata.get("api_test_only")
                or scores["n_grading_errors"] or not (run_dir / "transcript.jsonl").exists()
                or scores["all_pass"] != all_pass
                or not math.isclose(scores["criterion_fraction"], fraction, abs_tol=1e-9)
                or not math.isclose(scores["reward_task"], reward, abs_tol=1e-9)
                or stat.S_IMODE(feedback_path.stat().st_mode) != 0o600
                or hashlib.sha256(feedback_path.read_bytes()).hexdigest() != scores["rubric_feedback_sha256"]):
            raise ValueError(f"Invalid rollout evidence: {run_dir}")
        if retrieval_mode == "hybrid_router":
            router = metadata.get("router_record") or {}
            if (router.get("router_version") != ROUTER_VERSION
                    or router.get("index_version") != snapshot.index_version
                    or router.get("selected_ids") != metadata["retrieved_skill_ids"]
                    or router.get("selected_hashes") != metadata["retrieved_skill_hashes"]
                    or len(router.get("candidate_ids", [])) > 8
                    or len(router.get("selected_ids", [])) > 3):
                raise ValueError(f"Invalid Router evidence: {run_dir}")
        checked[(row["task_id"], row["sample_index"])] = {
            "run_dir": str(run_dir), "reward": float(scores["reward_task"]),
            "all_pass": bool(scores["all_pass"]), "turns": int(metadata["turn_count"]),
            "retrieved_skill_ids": metadata["retrieved_skill_ids"],
            "retrieved_skill_hashes": metadata["retrieved_skill_hashes"],
            "router_record": metadata.get("router_record"),
        }
    return checked


def _publish(trial_path: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    trial = SkillSnapshot.load(trial_path)
    if output_path.exists():
        if SkillSnapshot.load(output_path).snapshot_id != trial.snapshot_id:
            raise ValueError("Published snapshot differs from this trial")
        return
    temporary = output_path.with_name(f".{output_path.name}.{uuid.uuid4().hex}.tmp")
    try:
        with temporary.open("xb") as stream:
            stream.write(trial_path.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
        if SkillSnapshot.load(temporary).snapshot_id != trial.snapshot_id:
            raise ValueError("Trial changed during publication")
        temporary.chmod(0o444)
        os.link(temporary, output_path)
    finally:
        temporary.unlink(missing_ok=True)


def summarize(args: argparse.Namespace) -> dict:
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    train_tasks, test_tasks = manifest["train"], manifest["test"]
    protocol = getattr(args, "protocol", "4x4")
    retrieval_mode = getattr(args, "retrieval_mode", "lexical")
    train_count, test_count = (1, 2) if protocol == "1x2" else (4, 4)
    if (len(train_tasks) != train_count or len(test_tasks) != test_count
            or len(set(train_tasks)) != train_count or len(set(test_tasks)) != test_count
            or set(train_tasks) & set(test_tasks)):
        raise ValueError("Train/test task counts or disjointness invalid")
    parent, trial = SkillSnapshot.load(args.parent), SkillSnapshot.load(args.trial)
    trial_payload = json.loads(args.trial.read_text(encoding="utf-8"))
    if trial_payload.get("parent_snapshot_id") != parent.snapshot_id:
        raise ValueError("Trial does not derive from parent")
    train = _read_side(args.train_summary, parent, train_tasks, args.temperature,
                       args.model, args.judge_model, retrieval_mode)
    old = _read_side(args.old_summary, parent, test_tasks, args.temperature,
                     args.model, args.judge_model, retrieval_mode)
    new = _read_side(args.new_summary, trial, test_tasks, args.temperature,
                     args.model, args.judge_model, retrieval_mode)
    if retrieval_mode == "hybrid_router":
        for side in (train, old, new):
            for task in {key[0] for key in side}:
                records = [side[(task, sample)]["router_record"] for sample in range(1, 5)]
                if any(record is None for record in records):
                    raise ValueError("Missing Router provenance")
                if len({tuple(record["selected_ids"]) for record in records}) != 1:
                    raise ValueError("Same-task samples did not share Router choice")
                if len({record["selection_key"] for record in records}) != 1:
                    raise ValueError("Same-task samples used different Router cache keys")
    paired = []
    per_task = []
    for task in test_tasks:
        items = []
        for sample in range(1, 5):
            left, right = old[(task, sample)], new[(task, sample)]
            item = {"task_id": task, "sample_index": sample,
                    "old_run_dir": left["run_dir"], "new_run_dir": right["run_dir"],
                    "old_reward": left["reward"], "new_reward": right["reward"],
                    "delta": right["reward"] - left["reward"],
                    "retrieval_changed": (
                        list(zip(left["retrieved_skill_ids"], left["retrieved_skill_hashes"]))
                        != list(zip(right["retrieved_skill_ids"], right["retrieved_skill_hashes"]))
                    )}
            paired.append(item)
            items.append(item)
        per_task.append({"task_id": task,
                         "old_mean": sum(item["old_reward"] for item in items) / 4,
                         "new_mean": sum(item["new_reward"] for item in items) / 4,
                         "delta_mean": sum(item["delta"] for item in items) / 4,
                         "retrieval_changed_samples": sum(item["retrieval_changed"] for item in items)})
    mean_delta = sum(item["delta"] for item in paired) / len(paired)
    old_mean = sum(item["old_reward"] for item in paired) / len(paired)
    new_mean = sum(item["new_reward"] for item in paired) / len(paired)
    if not math.isclose(new_mean - old_mean, mean_delta, abs_tol=1e-9):
        raise ValueError("Paired mean arithmetic mismatch")
    promoted = mean_delta > 0 and min(item["delta_mean"] for item in per_task) >= 0
    barrier_path = getattr(args, "candidate_barrier", None)
    if barrier_path:
        barrier = json.loads(barrier_path.read_text(encoding="utf-8"))
        winner = resolve_evaluated(barrier, {
            trial_payload["candidate_id"]: {
                "parent_snapshot_id": parent.snapshot_id,
                "per_task_deltas": [item["delta_mean"] for item in per_task],
            }
        })
        promoted = promoted and winner == trial_payload["candidate_id"]
    if promoted:
        _publish(args.trial, args.published)
    result = {
        "epoch": 1,
        "train_tasks": train_tasks, "test_tasks": test_tasks,
        "train_samples": len(train), "test_samples_per_snapshot": len(old),
        "temperature": args.temperature,
        "retrieval_mode": retrieval_mode,
        "parent_snapshot_id": parent.snapshot_id,
        "trial_snapshot_id": trial.snapshot_id,
        "candidate_id": trial_payload["candidate_id"],
        "old_test_mean": old_mean, "new_test_mean": new_mean,
        "writer_reward_frozen_api": mean_delta,
        "task_results": per_task,
        "pairs": paired,
        "promotion_gate": "positive overall mean and no negative per-task mean",
        "candidate_barrier_path": str(barrier_path) if barrier_path else None,
        "promoted": promoted,
        "published_snapshot_path": str(args.published.resolve()) if promoted else None,
        "next_snapshot_id": trial.snapshot_id if promoted else parent.snapshot_id,
        "rollout_engine": "VERL ToolAgentLoop state machine with structured API generation",
        "sampling_note": "Old/new API draws are independent; sample index aligns artifacts, not random seeds. Interpret task means rather than individual slot deltas.",
        "native_policy_update_performed": False,
        "policy_token_ids_available": False,
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--trial", type=Path, required=True)
    parser.add_argument("--train-summary", type=Path, required=True)
    parser.add_argument("--old-summary", type=Path, required=True)
    parser.add_argument("--new-summary", type=Path, required=True)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--model", default="deepseek-flash")
    parser.add_argument("--judge-model", default="deepseek-flash")
    parser.add_argument("--protocol", choices=["4x4", "1x2"], default="4x4")
    parser.add_argument("--retrieval-mode", choices=["lexical", "hybrid_router"], default="lexical")
    parser.add_argument("--candidate-barrier", type=Path)
    parser.add_argument("--published", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    row = summarize(args)
    print(json.dumps({key: row[key] for key in ("epoch", "train_samples", "test_samples_per_snapshot",
                                                   "old_test_mean", "new_test_mean", "writer_reward_frozen_api",
                                                   "promoted", "next_snapshot_id")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
