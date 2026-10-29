from __future__ import annotations

import hashlib
import json
from argparse import Namespace
from pathlib import Path

from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.summarize_one_epoch_4x import summarize
from examples.skill_evolving.writer_policy import parse_writer_action, stage_action_snapshot
from examples.skill_evolving.candidate_barrier import stage_candidates


EMPTY = Path(__file__).resolve().parent / "library" / "snapshot_harvey_empty.json"


def _write_side(root: Path, tasks: list[str], snapshot: SkillSnapshot, reward_by_task: dict[str, float],
                label: str) -> Path:
    rows = []
    for task in tasks:
        for sample in range(1, 5):
            run_dir = root / label / task.replace("/", "__") / f"sample-{sample:02d}"
            run_dir.mkdir(parents=True)
            metadata = {"task_id": task, "skill_snapshot_id": snapshot.snapshot_id,
                        "temperature": 0.7, "sample_index": sample, "model": "mock",
                        "verl_state_machine": "ToolAgentLoop.run", "api_test_only": True,
                        "finished": True,
                        "turn_count": 1, "retrieved_skill_ids": [], "retrieved_skill_hashes": []}
            feedback = b"{}"
            (run_dir / "rubric_feedback.json").write_bytes(feedback)
            (run_dir / "rubric_feedback.json").chmod(0o600)
            reward = reward_by_task[task]
            scores = {"task_id": task, "judge_model": "mock", "n_passed": int(reward * 10),
                      "n_criteria": 20, "all_pass": False, "criterion_fraction": reward / 2,
                      "beta": 0.2, "reward_task": reward / 10,
                      "n_grading_errors": 0, "rubric_feedback_file": "rubric_feedback.json",
                      "rubric_feedback_sha256": hashlib.sha256(feedback).hexdigest()}
            # n_passed/20 * beta equals reward/10.
            (run_dir / "rollout_metadata.json").write_text(json.dumps(metadata))
            (run_dir / "scores.json").write_text(json.dumps(scores))
            (run_dir / "transcript.jsonl").write_text('{"role":"assistant"}\n')
            rows.append({"status": "complete", "task_id": task, "sample_index": sample,
                         "run_dir": str(run_dir)})
    summary = root / f"{label}_summary.json"
    summary.write_text(json.dumps(rows))
    return summary


def test_one_epoch_publishes_only_without_per_task_regression(tmp_path):
    parent = SkillSnapshot.load(EMPTY)
    action = parse_writer_action(json.dumps({
        "action": "ADD", "target_skill_ids": [],
        "skill": {"id": "draft-check", "title": "Draft check", "summary": "Check drafts",
                  "instructions": ["Review the source", "Check the output"], "triggers": ["draft"],
                  "exclusions": [], "level": "specific", "subtype": "pattern",
                  "operation_pattern": "draft", "legal_domain": None},
    }), parent)
    trial_path = tmp_path / "trial.json"
    trial = stage_action_snapshot(parent, action, trial_path)
    train_tasks = [f"train/task-{i}" for i in range(4)]
    test_tasks = [f"test/task-{i}" for i in range(4)]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"train": train_tasks, "test": test_tasks}))
    train_summary = _write_side(tmp_path, train_tasks, parent, dict.fromkeys(train_tasks, 1.0), "train")
    old_summary = _write_side(tmp_path, test_tasks, parent, dict.fromkeys(test_tasks, 1.0), "old")
    new_summary = _write_side(tmp_path, test_tasks, trial, dict.fromkeys(test_tasks, 1.5), "new")
    args = Namespace(manifest=manifest, parent=EMPTY, trial=trial_path,
                     train_summary=train_summary, old_summary=old_summary, new_summary=new_summary,
                     temperature=0.7, model="mock", judge_model="mock",
                     published=tmp_path / "published.json", output=tmp_path / "result.json")
    result = summarize(args)
    assert result["promoted"] and args.published.exists()
    assert result["train_samples"] == 16 and result["test_samples_per_snapshot"] == 16
    assert result["writer_reward_frozen_api"] > 0
    args.published.unlink()
    for sample in range(1, 5):
        score_path = tmp_path / "new" / "test__task-0" / f"sample-{sample:02d}" / "scores.json"
        scores = json.loads(score_path.read_text())
        scores.update(n_passed=5, criterion_fraction=0.25, reward_task=0.05)
        score_path.write_text(json.dumps(scores))
    result = summarize(args)
    assert result["writer_reward_frozen_api"] > 0
    assert not result["promoted"] and not args.published.exists()


def test_one_by_two_protocol_uses_barrier_and_four_samples_per_task(tmp_path):
    parent = SkillSnapshot.load(EMPTY)
    action = parse_writer_action(json.dumps({
        "action": "ADD", "target_skill_ids": [],
        "skill": {"id": "new", "title": "New", "summary": "Draft source",
                  "instructions": ["Check the source"], "triggers": ["draft"], "exclusions": []},
    }), parent)
    candidate = tmp_path / "candidate.json"
    candidate.write_text(json.dumps(action))
    barrier_path = tmp_path / "barrier.json"
    barrier_path.write_text(json.dumps(stage_candidates(parent, [
        {"status": "valid", "action": "ADD", "candidate_path": str(candidate)}
    ], tmp_path / "staging")))
    trial_path = tmp_path / "trial.json"
    trial = stage_action_snapshot(parent, action, trial_path)
    tasks = ["test/one", "test/two"]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"train": ["train/one"], "test": tasks}))
    args = Namespace(manifest=manifest, parent=EMPTY, trial=trial_path,
                     train_summary=_write_side(tmp_path, ["train/one"], parent,
                                               {"train/one": 1.0}, "train"),
                     old_summary=_write_side(tmp_path, tasks, parent,
                                             dict.fromkeys(tasks, 1.0), "old"),
                     new_summary=_write_side(tmp_path, tasks, trial,
                                             dict.fromkeys(tasks, 1.5), "new"),
                     temperature=0.7, model="mock", judge_model="mock",
                     protocol="1x2", retrieval_mode="lexical", candidate_barrier=barrier_path,
                     published=tmp_path / "published.json", output=tmp_path / "result.json")
    result = summarize(args)
    assert result["train_samples"] == 4
    assert result["test_samples_per_snapshot"] == 8
    assert result["promoted"] and args.published.exists()
