"""Versioned, deterministic Router skill for Harvey rollout retrieval.

The Router is kept outside task snapshots. Its structured choice is cached per
task/snapshot/index/config, so repeated samples cannot see different skills.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field

from examples.skill_evolving.skill_store import RetrievedSkill, SkillSnapshot


ROUTER_VERSION = "router-rule-v1"
ROUTER_INSTRUCTIONS = (
    "Choose at most three applicable task skills after hard operation/domain/exclusion filters; "
    "avoid declared incompatible pairs and repeated guidance; obey the context budget."
)


def _token_cost(item: RetrievedSkill) -> int:
    text = " ".join((item.skill.title, item.skill.summary, *item.skill.instructions))
    return max(1, len(text.encode("utf-8")) // 4)


@dataclass
class SkillRouter:
    top_k: int = 8
    top_n: int = 3
    token_budget: int = 1500
    model_checkpoint: str = "fixed-api-model"
    _cache: dict[str, tuple[tuple[RetrievedSkill, ...], dict]] = field(default_factory=dict)

    def choose(self, snapshot: SkillSnapshot, task_id: str, query: str,
               operation_pattern: str, legal_domain: str) -> tuple[tuple[RetrievedSkill, ...], dict]:
        key_payload = (task_id, hashlib.sha256(query.encode()).hexdigest(), self.model_checkpoint,
                       snapshot.snapshot_id, ROUTER_VERSION, snapshot.index_version,
                       self.top_k, self.top_n, self.token_budget)
        key = hashlib.sha256(json.dumps(key_payload).encode()).hexdigest()
        if key in self._cache:
            selected, record = self._cache[key]
            return selected, {**record, "cache_hit": True}
        candidates = snapshot.retrieve_hybrid(query, self.top_k, operation_pattern=operation_pattern,
                                              legal_domain=legal_domain)
        selected: list[RetrievedSkill] = []
        rejected: list[dict] = []
        spent = 0
        for item in candidates:
            skill = item.skill
            cost = _token_cost(item)
            conflict = next((prior.skill.skill_id for prior in selected
                             if skill.skill_id in prior.skill.incompatible_skill_ids
                             or prior.skill.skill_id in skill.incompatible_skill_ids), None)
            if len(selected) >= self.top_n:
                reason = "top_n"
            elif conflict:
                reason = f"incompatible_with:{conflict}"
            elif spent + cost > self.token_budget:
                reason = "token_budget"
            else:
                selected.append(item)
                spent += cost
                continue
            rejected.append({"id": skill.skill_id, "reason": reason})
        record = {
            "router_version": ROUTER_VERSION,
            "router_instructions": ROUTER_INSTRUCTIONS,
            "index_version": snapshot.index_version,
            "selection_key": key,
            "candidate_ids": [item.skill.skill_id for item in candidates],
            "candidate_hashes": [item.skill.content_hash for item in candidates],
            "candidate_scores": [item.score for item in candidates],
            "selected_ids": [item.skill.skill_id for item in selected],
            "selected_hashes": [item.skill.content_hash for item in selected],
            "selected_reasons": {item.skill.skill_id: "highest compatible hybrid rank" for item in selected},
            "rejected": rejected,
            "estimated_token_cost": spent,
            "token_budget": self.token_budget,
            "fallback": False,
            "cache_hit": False,
        }
        result = tuple(selected)
        self._cache[key] = (result, record)
        return result, record
