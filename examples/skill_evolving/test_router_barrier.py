from __future__ import annotations

import json
from pathlib import Path

import pytest

from examples.skill_evolving.candidate_barrier import resolve_evaluated, stage_candidates
from examples.skill_evolving.skill_router import SkillRouter
from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.writer_policy import parse_writer_action


def _snapshot(tmp_path: Path) -> SkillSnapshot:
    path = tmp_path / "parent.json"
    path.write_text(json.dumps({"version": "test", "skills": [
        {"id": "one", "title": "Draft source document", "summary": "Check source text",
         "instructions": ["Check source text"], "triggers": ["draft"], "exclusions": [],
         "incompatible_skill_ids": ["two"]},
        {"id": "two", "title": "Draft target document", "summary": "Check target text",
         "instructions": ["Check target text"], "triggers": ["draft"], "exclusions": []},
        {"id": "wrong", "title": "Employment review", "summary": "Review employment",
         "instructions": ["Review employment"], "triggers": ["review"], "exclusions": [],
         "level": "specific", "subtype": "legal_domain", "legal_domain": "employment-labor"},
    ]}))
    return SkillSnapshot.load(path)


def test_router_cache_filters_and_conflicts(tmp_path):
    snapshot = _snapshot(tmp_path)
    router = SkillRouter(top_k=8, top_n=3, token_budget=1000)
    first, record = router.choose(snapshot, "real-estate/draft-case", "Draft source target text",
                                  "draft", "real-estate")
    second, cached = router.choose(snapshot, "real-estate/draft-case", "Draft source target text",
                                   "draft", "real-estate")
    assert first == second and cached["cache_hit"]
    assert "wrong" not in record["candidate_ids"]
    assert len(first) == 1
    assert any(item["reason"].startswith("incompatible_with") for item in record["rejected"])


def test_batch_barrier_deduplicates_conflicts_and_rejects_stale(tmp_path):
    parent = _snapshot(tmp_path)
    rows = []
    for title in ("Change A", "Change B", "Change A"):
        action = parse_writer_action(json.dumps({
            "action": "REVISE", "target_skill_ids": ["one"],
            "skill": {"id": "one", "title": title, "summary": "Draft check",
                      "instructions": ["Check source"], "triggers": ["draft"], "exclusions": []},
        }), parent)
        path = tmp_path / f"input-{len(rows)}.json"
        path.write_text(json.dumps(action))
        rows.append({"status": "valid", "action": "REVISE", "candidate_path": str(path)})
    barrier = stage_candidates(parent, rows, tmp_path / "staging")
    assert len(barrier["candidates"]) == 2
    assert len(barrier["duplicates"]) == 1
    assert len(barrier["conflicts"]) == 1
    ids = [item["candidate_id"] for item in barrier["candidates"]]
    evaluations = {ids[0]: {"parent_snapshot_id": parent.snapshot_id,
                            "per_task_deltas": [0.1, 0.0]},
                   ids[1]: {"parent_snapshot_id": parent.snapshot_id,
                            "per_task_deltas": [0.2, -0.01]}}
    assert resolve_evaluated(barrier, evaluations) == ids[0]
    stale = json.loads(Path(rows[0]["candidate_path"]).read_text())
    stale["parent_snapshot_id"] = "old"
    Path(rows[0]["candidate_path"]).write_text(json.dumps(stale))
    with pytest.raises(ValueError, match="Stale"):
        stage_candidates(parent, rows, tmp_path / "other")
