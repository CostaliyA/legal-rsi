from __future__ import annotations

import json
from pathlib import Path

import pytest

from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.commit_trial import commit
from examples.skill_evolving.harvey_reward import reward_from_counts
from examples.skill_evolving.distill_initial_skills import _read_run
from examples.skill_evolving.writer_policy import (
    parse_writer_action,
    reward_on_author_tokens,
    stage_action_snapshot,
    writer_reward,
)


EMPTY = Path(__file__).resolve().parent / "library" / "snapshot_harvey_empty.json"


def _action() -> dict:
    return {
        "action": "ADD",
        "target_skill_ids": [],
        "skill": {
            "id": "cross-document-check",
            "title": "Check cross-document facts",
            "summary": "Verify facts against their sources",
            "instructions": ["Locate each source", "Reconcile conflicting names and dates"],
            "triggers": ["documents"],
            "exclusions": [],
            "level": "general",
        },
    }


def test_writer_candidate_is_staged_and_old_snapshot_is_immutable(tmp_path):
    old = SkillSnapshot.load(EMPTY)
    action = parse_writer_action(json.dumps(_action()), old)
    new = stage_action_snapshot(old, action, tmp_path / "trial.json")
    assert len(old.skills) == 0
    assert [item.skill_id for item in new.skills] == ["cross-document-check"]
    assert new.snapshot_id != old.snapshot_id


def test_writer_rejects_unreachable_operation_pattern():
    parent = SkillSnapshot.load(EMPTY)
    raw = _action()
    raw["skill"].update(level="specific", subtype="pattern", operation_pattern="assemble")
    with pytest.raises(ValueError, match="operation_pattern is not a supported Harvey task prefix"):
        parse_writer_action(json.dumps(raw), parent)


def test_writer_accepts_draft_operation_pattern():
    parent = SkillSnapshot.load(EMPTY)
    raw = _action()
    raw["skill"].update(level="specific", subtype="pattern", operation_pattern="draft")
    assert parse_writer_action(json.dumps(raw), parent)["skill"]["operation_pattern"] == "draft"


def test_reward_lands_on_final_writer_token_only():
    breakdown = writer_reward(
        ref_old=[0.4, 0.6], ref_new=[0.6, 0.8],
        cur_old=[0.5, 0.7], cur_new=[0.7, 0.9], alpha=0.7,
    )
    assert breakdown["reward_writer"] == pytest.approx(0.2)
    assert reward_on_author_tokens([0, 1, 1, 0], breakdown["reward_writer"]) == [0.0, 0.0, 0.2, 0.0]


def test_harvey_dense_reward_uses_criterion_counts():
    assert reward_from_counts(33, 35) == (False, 33 / 35, pytest.approx(0.2 * 33 / 35))
    assert reward_from_counts(35, 35) == (True, 1.0, 1.2)


def test_source_trace_keeps_unicode_line_separator_inside_json_record(tmp_path):
    (tmp_path / "rollout_metadata.json").write_text(json.dumps(
        {"task_id": "domain/extract-case", "skill_snapshot_id": "empty"}))
    (tmp_path / "transcript.jsonl").write_text(json.dumps(
        {"role": "assistant", "turn": 1, "text": "before\u2028after", "tool_calls": []},
        ensure_ascii=False) + "\n")
    task_id, snapshot_id, actions = _read_run(tmp_path)
    assert (task_id, snapshot_id) == ("domain/extract-case", "empty")
    assert json.loads(actions)[0]["plan"] == "before\u2028after"


def test_specific_skill_filters_by_pattern_and_domain(tmp_path):
    raw = {
        "version": "filter-test",
        "skills": [
            {**_action()["skill"], "id": "extract-terms", "level": "specific",
             "subtype": "pattern", "operation_pattern": "extract", "legal_domain": None},
        ],
    }
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(raw))
    snapshot = SkillSnapshot.load(path)
    assert snapshot.retrieve("extract documents", operation_pattern="extract", legal_domain="real-estate")
    assert not snapshot.retrieve("extract documents", operation_pattern="identify", legal_domain="real-estate")


def test_commit_checks_underlying_pair_scores(tmp_path):
    parent = SkillSnapshot.load(EMPTY)
    action = parse_writer_action(json.dumps(_action()), parent)
    trial_path = tmp_path / "trial.json"
    trial = stage_action_snapshot(parent, action, trial_path)
    pairs = []
    for index in range(5):
        task_id = f"domain/task-{index}"
        pair = {"task_id": task_id, "old_snapshot_id": parent.snapshot_id,
                "new_snapshot_id": trial.snapshot_id, "delta_api": 0.1}
        for side, snapshot_id, reward in (("old", parent.snapshot_id, 0.3),
                                          ("new", trial.snapshot_id, 0.4)):
            run_dir = tmp_path / f"{index}-{side}"
            run_dir.mkdir()
            (run_dir / "scores.json").write_text(json.dumps(
                {"task_id": task_id, "n_grading_errors": 0, "reward_task": reward}))
            (run_dir / "rollout_metadata.json").write_text(json.dumps(
                {"task_id": task_id, "skill_snapshot_id": snapshot_id}))
            (run_dir / "transcript.jsonl").write_text("{}\n")
            pair[f"{side}_run_dir"] = str(run_dir)
            pair[f"{side}_reward_task"] = reward
        pairs.append(pair)
    summary_path = tmp_path / "paired_summary.json"
    summary = {"mode": "api_protocol_and_frozen_model_reward",
               "old_snapshot_id": parent.snapshot_id, "new_snapshot_id": trial.snapshot_id,
               "mean_delta_api": 0.1, "pairs": pairs}
    summary_path.write_text(json.dumps(summary))
    assert commit(EMPTY, trial_path, summary_path, tmp_path / "published.json")["mean_delta"] == pytest.approx(0.1)
    assert (tmp_path / "published.json").stat().st_ino != trial_path.stat().st_ino
    summary["pairs"][0]["delta_api"] = 0.5
    summary_path.write_text(json.dumps(summary))
    with pytest.raises(ValueError, match="delta differs"):
        commit(EMPTY, trial_path, summary_path, tmp_path / "tampered.json")
    summary["pairs"] = pairs[:2]
    summary["pairs"][0]["delta_api"] = 0.1
    summary_path.write_text(json.dumps(summary))
    assert commit(EMPTY, trial_path, summary_path, tmp_path / "published_two.json",
                  expected_pairs=2)["mean_delta"] == pytest.approx(0.1)
