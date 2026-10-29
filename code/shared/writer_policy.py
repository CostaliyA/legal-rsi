"""Pure Skill Writer action parsing and token-level reward attribution."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from examples.skill_evolving.skill_store import Skill, SkillSnapshot, _content_hash


ACTIONS = {"ADD", "REVISE", "MERGE", "RETIRE", "NO_CHANGE"}
SUPPORTED_PATTERNS = {"analyze", "assess", "compare", "draft", "extract", "identify", "review"}


def parse_writer_action(text: str, parent: SkillSnapshot) -> dict[str, Any]:
    """Parse only JSON actions; invalid proposals remain penalizable actions."""
    body = text.strip()
    if body.startswith("```"):
        body = re.sub(r"^```(?:json)?\s*|\s*```$", "", body)
    raw = json.loads(body)
    if not isinstance(raw, dict) or raw.get("action") not in ACTIONS:
        raise ValueError("Writer must return a JSON action")
    action = raw["action"]
    target_ids = raw.get("target_skill_ids", [])
    if not isinstance(target_ids, list) or not all(isinstance(item, str) for item in target_ids):
        raise ValueError("target_skill_ids must be a list of strings")
    existing = {item.skill_id for item in parent.skills}
    if action == "NO_CHANGE":
        if raw.get("skill") is not None or target_ids:
            raise ValueError("NO_CHANGE cannot include a skill or targets")
        skill = None
    elif action == "RETIRE":
        if len(target_ids) != 1 or target_ids[0] not in existing or raw.get("skill") is not None:
            raise ValueError("RETIRE needs one existing target and no new skill")
        skill = None
    else:
        skill = Skill.from_dict(raw["skill"])
        if skill.operation_pattern and skill.operation_pattern not in SUPPORTED_PATTERNS:
            raise ValueError("operation_pattern is not a supported Harvey task prefix")
        if action == "ADD" and (target_ids or skill.skill_id in existing):
            raise ValueError("ADD needs a new skill ID and no target")
        if action == "REVISE" and (len(target_ids) != 1 or target_ids[0] not in existing):
            raise ValueError("REVISE needs one existing target")
        if action == "REVISE" and skill.skill_id != target_ids[0]:
            raise ValueError("REVISE must keep the target skill ID")
        if action == "MERGE" and (len(set(target_ids)) < 2 or not set(target_ids) <= existing):
            raise ValueError("MERGE needs at least two existing targets")
        if action == "MERGE" and skill.skill_id in existing - set(target_ids):
            raise ValueError("MERGE output ID conflicts with an unrelated skill")
    proposal = {
        "action": action,
        "parent_snapshot_id": parent.snapshot_id,
        "target_skill_ids": target_ids,
        "skill": skill.to_dict() if skill else None,
    }
    proposal["candidate_id"] = _content_hash(proposal)[:20]
    return proposal


def writer_reward(
    *,
    ref_old: list[float], ref_new: list[float],
    cur_old: list[float], cur_new: list[float],
    alpha: float = 0.7, cost: float = 0.0, negative_transfer: float = 0.0,
) -> dict[str, float]:
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must be in [0, 1]")
    lengths = {len(ref_old), len(ref_new), len(cur_old), len(cur_new)}
    if lengths != {len(ref_old)} or not ref_old:
        raise ValueError("Four score vectors must be nonempty and equally long")
    delta_ref = sum(new - old for old, new in zip(ref_old, ref_new)) / len(ref_old)
    delta_cur = sum(new - old for old, new in zip(cur_old, cur_new)) / len(cur_old)
    raw = alpha * delta_ref + (1 - alpha) * delta_cur
    return {
        "delta_ref": delta_ref,
        "delta_cur": delta_cur,
        "raw_paired_gain": raw,
        "cost": cost,
        "negative_transfer": negative_transfer,
        "reward_writer": raw - cost - negative_transfer,
    }


def reward_on_author_tokens(author_mask: list[int], reward: float) -> list[float]:
    """Place outcome reward at the final generated writer-action token."""
    if not author_mask or not all(value in (0, 1) for value in author_mask):
        raise ValueError("author_mask must be binary and nonempty")
    positions = [i for i, value in enumerate(author_mask) if value]
    if not positions:
        raise ValueError("No author token in the trajectory")
    scores = [0.0] * len(author_mask)
    scores[positions[-1]] = float(reward)
    return scores


def stage_action_snapshot(parent: SkillSnapshot, action: dict[str, Any], path: Path) -> SkillSnapshot:
    """Materialize one candidate branch without mutating the parent snapshot."""
    if action["parent_snapshot_id"] != parent.snapshot_id:
        raise ValueError("Candidate parent snapshot mismatch")
    old = [item.to_dict() for item in parent.skills]
    targets = set(action["target_skill_ids"])
    kind = action["action"]
    if kind == "NO_CHANGE":
        new = old
    elif kind == "ADD":
        new = old + [action["skill"]]
    elif kind == "REVISE":
        replacement = dict(action["skill"])
        replacement["id"] = next(iter(targets))
        new = [replacement if item["id"] in targets else item for item in old]
    elif kind == "MERGE":
        new = [item for item in old if item["id"] not in targets] + [action["skill"]]
    elif kind == "RETIRE":
        new = [item for item in old if item["id"] not in targets]
    else:
        raise ValueError("Unknown writer action")
    if len({item["id"] for item in new}) != len(new):
        raise ValueError("Candidate branch has duplicate skill IDs")
    payload = {
        "version": f"{parent.version}-trial-{action['candidate_id'][:12]}",
        "parent_snapshot_id": parent.snapshot_id,
        "candidate_id": action["candidate_id"],
        "skills": new,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
    return SkillSnapshot.load(path)
