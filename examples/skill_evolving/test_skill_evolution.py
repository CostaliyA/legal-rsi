from __future__ import annotations

import json
from pathlib import Path

import pytest

from examples.skill_evolving.skill_evolution import publish, stage_shadow, verify_paired_scores
from examples.skill_evolving.skill_store import SkillSnapshot


EXAMPLE = Path(__file__).resolve().parent
EMPTY = EXAMPLE / "library" / "snapshot_harvey_empty.json"


def _candidate(tmp_path: Path) -> Path:
    parent = SkillSnapshot.load(EMPTY)
    path = tmp_path / "candidate.json"
    path.write_text(
        json.dumps(
            {
                "parent_snapshot_id": parent.snapshot_id,
                "source_runs": ["run-1", "run-2"],
                "skill": {
                    "id": "source-check",
                    "title": "Check sources",
                    "summary": "Verify source support before drafting",
                    "instructions": ["Read primary material", "Check quoted facts against it"],
                    "triggers": ["document"],
                    "exclusions": [],
                },
            }
        ),
        encoding="utf-8",
    )
    return path


def test_bootstrap_publishes_one_immutable_snapshot(tmp_path):
    candidate = _candidate(tmp_path)
    output = tmp_path / "snapshot-v1.json"
    shadow = stage_shadow(EMPTY, candidate, tmp_path / "shadow-v1.json", "v1")
    result = publish(EMPTY, candidate, output, version="v1", bootstrap=True)
    assert shadow["snapshot_id"] == result["snapshot_id"]
    assert result["snapshot_id"] == SkillSnapshot.load(output).snapshot_id
    with pytest.raises(FileExistsError):
        publish(EMPTY, candidate, output, version="v1", bootstrap=True)


def test_evolution_rejects_regression(tmp_path):
    manifest = tmp_path / "pairs.json"
    manifest.write_text(
        json.dumps(
            {
                "pairs": [
                    {"task_id": "a", "seed": 1, "parent_score": 7, "parent_max_score": 10,
                     "candidate_score": 8, "candidate_max_score": 10},
                    {"task_id": "b", "seed": 1, "parent_score": 8, "parent_max_score": 10,
                     "candidate_score": 7, "candidate_max_score": 10},
                ]
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="utility gate"):
        verify_paired_scores(manifest)


def test_paired_gate_checks_snapshot_and_artifacts(tmp_path):
    candidate = _candidate(tmp_path)
    parent_id = SkillSnapshot.load(EMPTY).snapshot_id
    shadow_id = stage_shadow(EMPTY, candidate, tmp_path / "shadow.json", "v1")["snapshot_id"]
    pairs = []
    for task_id in ("heldout-a", "heldout-b"):
        pair = {"task_id": task_id, "seed": 1}
        for side, score, snapshot_id in (("parent", 5, parent_id), ("candidate", 6, shadow_id)):
            run_dir = tmp_path / f"{task_id}-{side}"
            run_dir.mkdir()
            score_path = run_dir / "scores.json"
            score_path.write_text(json.dumps({"task_id": task_id, "score": score,
                                               "max_score": 10, "n_grading_errors": 0}))
            (run_dir / "rollout_metadata.json").write_text(json.dumps({"skill_snapshot_id": snapshot_id}))
            pair.update({f"{side}_score": score, f"{side}_max_score": 10,
                         f"{side}_scores_path": str(score_path)})
        pairs.append(pair)
    manifest = tmp_path / "pairs.json"
    manifest.write_text(json.dumps({"parent_snapshot_id": parent_id,
                                    "candidate_skill_id": "source-check",
                                    "candidate_snapshot_id": shadow_id, "pairs": pairs}))
    output = tmp_path / "published.json"
    assert publish(EMPTY, candidate, output, version="v1", paired_scores=manifest)["snapshot_id"] == shadow_id
