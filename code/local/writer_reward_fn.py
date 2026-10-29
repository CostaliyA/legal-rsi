"""VERL custom reward function for a policy-authored skill action.

The first runnable mode uses a frozen API model for old/new shadow probes. A
current-model endpoint can be supplied for the full four-cell reward. API
probe trajectories are evaluation only; only the Writer's native VERL token
sequence is updated by the policy optimizer.
"""

from __future__ import annotations

import json
import os
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from examples.skill_evolving.api_harvey_rollout import run_one
from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.writer_policy import parse_writer_action, stage_action_snapshot, writer_reward


def compute_score(data_source: str, solution_str: str, ground_truth: dict, extra_info: dict, **_kwargs) -> dict:
    if data_source != "harvey_skill_writer":
        raise ValueError(f"Unexpected data_source: {data_source}")
    try:
        parent = SkillSnapshot.load(ground_truth["snapshot_path"])
        action = parse_writer_action(solution_str, parent)
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        return {"score": -0.1, "candidate_valid": False, "candidate_error": str(exc)}
    if action["action"] == "NO_CHANGE":
        return {"score": 0.0, "candidate_valid": True, "candidate_action": "NO_CHANGE",
                "candidate_id": action["candidate_id"]}
    tasks = ground_truth["probe_tasks"]
    if len(tasks) < 2 or len(tasks) != len(set(tasks)):
        raise ValueError("Writer reward needs at least two distinct credit-probe tasks")
    source_tasks = set(extra_info.get("source_task_ids", []))
    if source_tasks.intersection(tasks):
        raise ValueError("Credit-probe task overlaps Writer source tasks")
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("API key unavailable to Writer reward worker")
    os.environ["OPENAI_API_KEY"] = key
    os.environ["OPENAI_BASE_URL"] = ground_truth.get("base_url", "https://api.deepseek.com")
    root = Path(ground_truth["artifact_root"])
    root.mkdir(parents=True, exist_ok=True)
    run_root = Path(tempfile.mkdtemp(prefix=f"writer-{action['candidate_id']}-", dir=root))
    trial = stage_action_snapshot(parent, action, run_root / "trial_snapshot.json")
    judge_model = ground_truth["judge_model"]
    ref_model = ground_truth["reference_model"]
    cur_model = ground_truth.get("current_model")
    max_turns = int(ground_truth.get("max_turns", 200))

    def paired(model: str, label: str) -> tuple[list[float], list[float]]:
        def one(task_id: str, index: int, side: str):
            run_dir = run_root / f"{label}-{index}-{side}"
            run_dir.mkdir()
            snapshot = parent if side == "old" else trial
            return run_one(task_id, snapshot, run_dir, model=model, judge_model=judge_model,
                           max_turns=max_turns, top_k=3)

        with ThreadPoolExecutor(max_workers=min(4, len(tasks) * 2)) as pool:
            old_jobs = [pool.submit(one, task_id, index, "old") for index, task_id in enumerate(tasks)]
            new_jobs = [pool.submit(one, task_id, index, "new") for index, task_id in enumerate(tasks)]
            baseline = [float(job.result()["reward_task"]) for job in old_jobs]
            candidate = [float(job.result()["reward_task"]) for job in new_jobs]
        return baseline, candidate

    ref_old, ref_new = paired(ref_model, "ref")
    delta_ref = sum(new - old for old, new in zip(ref_old, ref_new)) / len(tasks)
    if cur_model:
        cur_old, cur_new = paired(cur_model, "cur")
        breakdown = writer_reward(ref_old=ref_old, ref_new=ref_new,
                                  cur_old=cur_old, cur_new=cur_new,
                                  alpha=float(ground_truth.get("alpha", 0.7)))
        mode = "four_cell"
    else:
        breakdown = {"delta_ref": delta_ref, "delta_cur": None,
                     "raw_paired_gain": delta_ref, "cost": 0.0, "negative_transfer": 0.0,
                     "reward_writer": delta_ref}
        mode = "frozen_api_only"
    result = {
        "score": breakdown["reward_writer"],
        "candidate_valid": True,
        "candidate_id": action["candidate_id"],
        "candidate_action": action["action"],
        "reward_mode": mode,
        "paired_probe_tasks": tasks,
        "trial_snapshot_id": trial.snapshot_id,
        "reward_breakdown": breakdown,
        "artifact_root": str(run_root),
    }
    (run_root / "reward.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    return result
