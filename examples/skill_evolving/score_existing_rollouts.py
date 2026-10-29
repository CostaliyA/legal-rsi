"""Grade completed Harvey rollout artifacts without rerunning the solver."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from lab_core.harness.run import load_task

from examples.skill_evolving.harvey_reward import reward_from_counts, score_episode


async def score_summary(summary_path: Path, output_path: Path, model: str, concurrency: int) -> list[dict]:
    rows = json.loads(summary_path.read_text(encoding="utf-8"))
    if not rows or any(row["status"] != "complete" for row in rows):
        raise ValueError("Every rollout must be complete before grading")
    slots = asyncio.Semaphore(concurrency)

    async def one(row: dict) -> dict:
        async with slots:
            run_dir = Path(row["run_dir"])
            score_path = run_dir / "scores.json"
            if score_path.exists():
                scores = json.loads(score_path.read_text(encoding="utf-8"))
                if scores.get("n_grading_errors") != 0 or scores.get("n_criteria", 0) <= 0:
                    raise ValueError(f"Invalid existing grading result: {score_path}")
                all_pass, fraction, reward = reward_from_counts(
                    scores["n_passed"], scores["n_criteria"], scores.get("beta", 0.2)
                )
                if scores["all_pass"] != all_pass:
                    raise ValueError(f"Inconsistent all-pass result: {score_path}")
                if scores.get("criterion_fraction") != fraction or scores.get("reward_task") != reward:
                    scores["criterion_fraction"] = fraction
                    scores["reward_task"] = reward
                    score_path.write_text(json.dumps(scores, ensure_ascii=False, indent=2), encoding="utf-8")
            else:
                task = await asyncio.to_thread(load_task, row["task_id"])
                scores = await asyncio.to_thread(score_episode, task, run_dir, model)
            return {"task_id": row["task_id"], "run_dir": str(run_dir),
                    "snapshot_id": row["skill_snapshot_id"], "reward_task": scores["reward_task"],
                    "all_pass": scores["all_pass"], "score": scores["score"],
                    "max_score": scores["max_score"], "scores_path": str(score_path)}

    results = await asyncio.gather(*(one(row) for row in rows))
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="deepseek-flash")
    parser.add_argument("--concurrency", type=int, default=5)
    args = parser.parse_args()
    results = asyncio.run(score_summary(args.summary, args.output, args.model, args.concurrency))
    print(json.dumps({"graded": len(results), "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
