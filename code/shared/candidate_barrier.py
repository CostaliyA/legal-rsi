"""Trainer-side staging and conflict graph for concurrent Writer proposals."""

from __future__ import annotations

import json
from pathlib import Path

from examples.skill_evolving.skill_store import SkillSnapshot, _content_hash, _tokens


def stage_candidates(parent: SkillSnapshot, rows: list[dict], staging_dir: Path) -> dict:
    """Stage each distinct valid action against one frozen parent; never overwrite."""
    staging_dir.mkdir(parents=True, exist_ok=True)
    candidates: list[dict] = []
    duplicates: list[dict] = []
    seen: dict[tuple, str] = {}
    for row in rows:
        if row.get("status") != "valid" or row.get("action") == "NO_CHANGE":
            continue
        action = json.loads(Path(row["candidate_path"]).read_text(encoding="utf-8"))
        if action.get("parent_snapshot_id") != parent.snapshot_id:
            raise ValueError("Stale Writer action cannot enter the batch barrier")
        candidate_id = action.get("candidate_id")
        payload = {key: action[key] for key in ("action", "parent_snapshot_id", "target_skill_ids", "skill")}
        if not isinstance(candidate_id, str) or candidate_id != _content_hash(payload)[:20]:
            raise ValueError("Writer action content hash mismatch")
        semantic_key = (action["action"], tuple(sorted(action["target_skill_ids"])),
                        _content_hash(action.get("skill")))
        if semantic_key in seen:
            duplicates.append({"candidate_id": candidate_id, "same_as": seen[semantic_key]})
            continue
        seen[semantic_key] = candidate_id
        target = staging_dir / f"{candidate_id}.json"
        canonical = json.dumps(action, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if target.exists():
            if target.read_text(encoding="utf-8") != canonical:
                raise ValueError("Staged action ID already has different content")
        else:
            with target.open("x", encoding="utf-8") as stream:
                stream.write(canonical)
            target.chmod(0o444)
        candidates.append({"candidate_id": candidate_id, "action": action,
                           "staged_path": str(target), "source_path": row["candidate_path"]})
    edges: list[dict] = []
    for i, left in enumerate(candidates):
        for right in candidates[i + 1:]:
            why = _conflict(left["action"], right["action"])
            if why:
                edges.append({"left": left["candidate_id"], "right": right["candidate_id"],
                              "reason": why})
    return {"parent_snapshot_id": parent.snapshot_id, "candidates": candidates,
            "duplicates": duplicates, "conflicts": edges}


def _conflict(left: dict, right: dict) -> str | None:
    left_targets, right_targets = set(left["target_skill_ids"]), set(right["target_skill_ids"])
    if left_targets & right_targets:
        return "shared_target"
    left_skill, right_skill = left.get("skill") or {}, right.get("skill") or {}
    if left_skill.get("id") and left_skill.get("id") == right_skill.get("id"):
        return "same_output_id"
    if (right_skill.get("id") in left_skill.get("incompatible_skill_ids", [])
            or left_skill.get("id") in right_skill.get("incompatible_skill_ids", [])):
        return "declared_incompatibility"
    if left_skill and right_skill:
        scope = ("level", "subtype", "operation_pattern", "legal_domain")
        if all(left_skill.get(key) == right_skill.get(key) for key in scope):
            left_text = " ".join((left_skill.get("summary", ""), *left_skill.get("instructions", [])))
            right_text = " ".join((right_skill.get("summary", ""), *right_skill.get("instructions", [])))
            left_tokens, right_tokens = _tokens(left_text), _tokens(right_text)
            if left_tokens and right_tokens and len(left_tokens & right_tokens) / len(left_tokens | right_tokens) >= 0.9:
                return "near_duplicate_scope_and_steps"
    return None


def resolve_evaluated(barrier: dict, evaluations: dict[str, dict]) -> str | None:
    """Pick one confirmed non-regressive branch; no last-writer-wins rule."""
    valid = []
    for candidate in barrier["candidates"]:
        candidate_id = candidate["candidate_id"]
        result = evaluations.get(candidate_id)
        if not result:
            continue
        deltas = result.get("per_task_deltas", [])
        if (result.get("parent_snapshot_id") == barrier["parent_snapshot_id"]
                and len(deltas) >= 2 and min(deltas) >= 0
                and sum(deltas) / len(deltas) > 0):
            valid.append((sum(deltas) / len(deltas), candidate_id))
    return max(valid, default=(0.0, None))[1]
