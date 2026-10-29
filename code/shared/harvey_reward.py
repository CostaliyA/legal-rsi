"""Harvey rubric reward shared by API verification and VERL policy rollouts."""

from __future__ import annotations

import json
import os
import hashlib
from pathlib import Path
from typing import Any


def reward_from_counts(n_passed: int, n_criteria: int, beta: float = 0.2) -> tuple[bool, float, float]:
    if n_criteria <= 0 or not 0 <= n_passed <= n_criteria:
        raise ValueError("Invalid Harvey criterion counts")
    all_pass = n_passed == n_criteria
    fraction = n_passed / n_criteria
    return all_pass, fraction, float(all_pass) + beta * fraction


def score_episode(
    task: dict[str, Any], run_dir: Path, judge_model: str, parallel: int = 2, beta: float = 0.2
) -> dict:
    from lab_core.evaluation.run_eval import Judge
    from lab_core.evaluation.scoring import score_rubric

    if judge_model.startswith("deepseek"):
        from openai import OpenAI

        class DeepSeekJudge(Judge):
            def __init__(self, model: str):
                self.model = model
                self.provider = "openai"
                self.client = OpenAI(
                    api_key=os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY"),
                    base_url="https://api.deepseek.com",
                )

        judge = DeepSeekJudge(judge_model)
    else:
        judge = Judge(model=judge_model)
    result = score_rubric(
        criteria=task["config"]["criteria"],
        run_dir=run_dir,
        judge=judge,
        task_desc=task["config"]["title"],
        parallel=parallel,
    )
    if result.n_grading_errors or result.max_score <= 0:
        raise RuntimeError(f"Harvey rubric grading failed: {result.n_grading_errors} errors")
    n_criteria = len(result.criteria_results)
    n_passed = sum(item["verdict"] == "pass" for item in result.criteria_results)
    all_pass, criterion_fraction, reward_task = reward_from_counts(n_passed, n_criteria, beta)
    # Keep the judge's criterion-level evidence for later, training-only
    # experience analysis. Do not put it in scores.json, which is consumed by
    # rollout summaries and validation comparisons.
    feedback = {
        "task_id": task["name"],
        "judge_model": judge_model,
        "criteria_results": result.criteria_results,
    }
    feedback_bytes = json.dumps(feedback, ensure_ascii=False, indent=2).encode("utf-8")
    feedback_path = run_dir / "rubric_feedback.json"
    fd = os.open(feedback_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(feedback_bytes)
    feedback_path.chmod(0o600)
    scores = {
        "task_id": task["name"],
        "judge_model": judge_model,
        "score": result.score,
        "max_score": result.max_score,
        "all_pass": all_pass,
        "n_passed": n_passed,
        "n_criteria": n_criteria,
        "n_grading_errors": result.n_grading_errors,
        "criterion_fraction": criterion_fraction,
        "beta": beta,
        "reward_task": reward_task,
        "rubric_feedback_file": feedback_path.name,
        "rubric_feedback_sha256": hashlib.sha256(feedback_bytes).hexdigest(),
    }
    (run_dir / "scores.json").write_text(json.dumps(scores, indent=2), encoding="utf-8")
    return scores
