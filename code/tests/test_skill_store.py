from __future__ import annotations

import json
from pathlib import Path

from examples.skill_evolving.skill_store import SkillSnapshot, inject_context


LIBRARY = Path(__file__).resolve().parent / "library" / "snapshot_v0001.json"


def test_retrieval_is_deterministic_and_relevant():
    snapshot = SkillSnapshot.load(LIBRARY)
    first = snapshot.retrieve("How should skill retrieval work for GRPO rollout?", top_k=3)
    second = snapshot.retrieve("How should skill retrieval work for GRPO rollout?", top_k=3)
    assert [(item.skill.skill_id, item.score) for item in first] == [
        (item.skill.skill_id, item.score) for item in second
    ]
    assert {item.skill.skill_id for item in first} >= {
        "hybrid-skill-retrieval",
        "immutable-rollout-snapshot",
    }


def test_loaded_snapshot_does_not_observe_same_group_file_changes(tmp_path):
    target = tmp_path / "snapshot.json"
    target.write_text(LIBRARY.read_text(encoding="utf-8"), encoding="utf-8")
    pinned = SkillSnapshot.load(target)
    raw = json.loads(target.read_text(encoding="utf-8"))
    raw["version"] = "v0002"
    raw["skills"] = []
    target.write_text(json.dumps(raw), encoding="utf-8")
    assert pinned.version == "v0001"
    assert len(pinned.skills) == 3
    assert SkillSnapshot.load(target).snapshot_id != pinned.snapshot_id


def test_context_injection_does_not_mutate_dataset_prompt():
    messages = [{"role": "user", "content": "original"}]
    augmented = inject_context(messages, "<skill_context>demo</skill_context>")
    assert messages[0]["content"] == "original"
    assert augmented[0]["content"].endswith("</skill_context>")

