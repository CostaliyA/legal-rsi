"""Deterministic read-only skill snapshots and retrieval.

The rollout-facing store intentionally has no commit method.  Evolution writes
must be staged elsewhere and become visible only after a trainer-side barrier
creates a new immutable snapshot.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


_WORD_RE = re.compile(r"[a-z0-9_+.-]+|[\u4e00-\u9fff]", re.IGNORECASE)


def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _content_hash(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _tokens(text: str) -> set[str]:
    return {token.lower() for token in _WORD_RE.findall(text)}


def _hashed_features(text: str, dimensions: int = 512) -> dict[int, float]:
    normalized = text.lower()
    words = _WORD_RE.findall(normalized)
    features = ["w:" + word for word in words]
    features += ["c:" + normalized[i:i + 3] for i in range(max(0, len(normalized) - 2))
                 if not normalized[i:i + 3].isspace()]
    vector: dict[int, float] = {}
    for feature in features:
        slot = int.from_bytes(hashlib.sha256(feature.encode()).digest()[:4], "big") % dimensions
        vector[slot] = vector.get(slot, 0.0) + 1.0
    norm = math.sqrt(sum(value * value for value in vector.values()))
    return {slot: value / norm for slot, value in vector.items()} if norm else {}


def _cosine(left: dict[int, float], right: dict[int, float]) -> float:
    return sum(value * right.get(slot, 0.0) for slot, value in left.items())


@dataclass(frozen=True)
class Skill:
    skill_id: str
    title: str
    summary: str
    instructions: tuple[str, ...]
    triggers: tuple[str, ...]
    exclusions: tuple[str, ...]
    content_hash: str
    level: str = "general"
    subtype: str | None = None
    operation_pattern: str | None = None
    legal_domain: str | None = None
    incompatible_skill_ids: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Skill":
        required = {"id", "title", "summary", "instructions"}
        missing = sorted(required - raw.keys())
        if missing:
            raise ValueError(f"skill is missing required fields: {missing}")
        incompatible = raw.get("incompatible_skill_ids", [])
        if (not isinstance(incompatible, list)
                or not all(isinstance(item, str) for item in incompatible)
                or str(raw["id"]) in incompatible):
            raise ValueError("incompatible_skill_ids must be a list of other skill IDs")
        semantic = {
            "id": str(raw["id"]),
            "title": str(raw["title"]),
            "summary": str(raw["summary"]),
            "instructions": [str(item) for item in raw["instructions"]],
            "triggers": [str(item) for item in raw.get("triggers", [])],
            "exclusions": [str(item) for item in raw.get("exclusions", [])],
        }
        if "incompatible_skill_ids" in raw:
            semantic["incompatible_skill_ids"] = incompatible
        level = str(raw.get("level", "general"))
        subtype = raw.get("subtype")
        operation_pattern = raw.get("operation_pattern")
        legal_domain = raw.get("legal_domain")
        if level not in {"general", "specific"}:
            raise ValueError("skill level must be general or specific")
        if level == "general" and (subtype or operation_pattern or legal_domain):
            raise ValueError("general skill cannot have a specific subtype or task tag")
        if level == "specific":
            if subtype not in {"pattern", "legal_domain", "composite"}:
                raise ValueError("specific skill needs a pattern, legal_domain or composite subtype")
            if subtype in {"pattern", "composite"} and not operation_pattern:
                raise ValueError("pattern/composite skill needs operation_pattern")
            if subtype in {"legal_domain", "composite"} and not legal_domain:
                raise ValueError("legal_domain/composite skill needs legal_domain")
        for key, value in (
            ("level", level),
            ("subtype", subtype),
            ("operation_pattern", operation_pattern),
            ("legal_domain", legal_domain),
        ):
            if key in raw:
                semantic[key] = value
        return cls(
            skill_id=semantic["id"],
            title=semantic["title"],
            summary=semantic["summary"],
            instructions=tuple(semantic["instructions"]),
            triggers=tuple(semantic["triggers"]),
            exclusions=tuple(semantic["exclusions"]),
            content_hash=_content_hash(semantic),
            level=level,
            subtype=subtype,
            operation_pattern=operation_pattern,
            legal_domain=legal_domain,
            incompatible_skill_ids=tuple(semantic.get("incompatible_skill_ids", [])),
        )

    @property
    def searchable_text(self) -> str:
        return " ".join(
            part for part in (
                self.title, self.summary, self.operation_pattern or "", self.legal_domain or "",
                *self.triggers, *self.instructions
            ) if part
        )

    def to_dict(self) -> dict[str, Any]:
        raw: dict[str, Any] = {
            "id": self.skill_id,
            "title": self.title,
            "summary": self.summary,
            "instructions": list(self.instructions),
            "triggers": list(self.triggers),
            "exclusions": list(self.exclusions),
        }
        if self.incompatible_skill_ids:
            raw["incompatible_skill_ids"] = list(self.incompatible_skill_ids)
        if self.level != "general" or self.subtype or self.operation_pattern or self.legal_domain:
            raw.update(
                level=self.level,
                subtype=self.subtype,
                operation_pattern=self.operation_pattern,
                legal_domain=self.legal_domain,
            )
        return raw


@dataclass(frozen=True)
class RetrievedSkill:
    skill: Skill
    score: float


@dataclass(frozen=True)
class SkillSnapshot:
    version: str
    snapshot_id: str
    skills: tuple[Skill, ...]
    source_path: str

    @classmethod
    def load(cls, path: str | Path) -> "SkillSnapshot":
        source = Path(path).expanduser().resolve()
        raw = json.loads(source.read_text(encoding="utf-8"))
        version = str(raw["version"])
        skills = tuple(Skill.from_dict(item) for item in raw["skills"])
        ids = [skill.skill_id for skill in skills]
        if len(ids) != len(set(ids)):
            raise ValueError("skill IDs must be unique within one snapshot")
        snapshot_payload = {
            "version": version,
            "skills": [{"id": skill.skill_id, "hash": skill.content_hash} for skill in skills],
        }
        snapshot_id = f"{version}-{_content_hash(snapshot_payload)[:12]}"
        return cls(version=version, snapshot_id=snapshot_id, skills=skills, source_path=str(source))

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
        *,
        operation_pattern: str | None = None,
        legal_domain: str | None = None,
    ) -> tuple[RetrievedSkill, ...]:
        """Return deterministic lexical candidates with explicit exclusions.

        This is deliberately a dependency-free baseline.  It combines token
        overlap with exact trigger matches and keeps stable ID tie-breaking so
        identical snapshot/query pairs reproduce retrieval order.
        """

        if top_k < 1:
            return ()
        query_lower = query.lower()
        query_tokens = _tokens(query)
        ranked: list[RetrievedSkill] = []
        for skill in self.skills:
            if skill.operation_pattern and skill.operation_pattern != operation_pattern:
                continue
            if skill.legal_domain and skill.legal_domain != legal_domain:
                continue
            if any(exclusion.lower() in query_lower for exclusion in skill.exclusions):
                continue
            skill_tokens = _tokens(skill.searchable_text)
            overlap = len(query_tokens & skill_tokens)
            union = max(len(query_tokens | skill_tokens), 1)
            lexical = overlap / union
            trigger_hits = sum(trigger.lower() in query_lower for trigger in skill.triggers)
            score = lexical + math.log1p(trigger_hits)
            if score > 0:
                ranked.append(RetrievedSkill(skill=skill, score=score))
        ranked.sort(key=lambda item: (-item.score, item.skill.skill_id))
        return tuple(ranked[:top_k])

    def retrieve_hybrid(
        self, query: str, top_k: int = 8, *,
        operation_pattern: str | None = None, legal_domain: str | None = None,
    ) -> tuple[RetrievedSkill, ...]:
        """Stable cosine on hashed word/character features plus lexical score.

        The feature hash is a local embedding so the index is reproducible and
        needs no remote embedding service. It is not a learned semantic model.
        """
        if top_k < 1:
            return ()
        query_lower = query.lower()
        query_tokens = _tokens(query)
        query_vec = _hashed_features(query)
        ranked: list[RetrievedSkill] = []
        for skill in self.skills:
            if skill.operation_pattern and skill.operation_pattern != operation_pattern:
                continue
            if skill.legal_domain and skill.legal_domain != legal_domain:
                continue
            if any(exclusion.lower() in query_lower for exclusion in skill.exclusions):
                continue
            skill_tokens = _tokens(skill.searchable_text)
            overlap = len(query_tokens & skill_tokens)
            union = max(len(query_tokens | skill_tokens), 1)
            trigger_hits = sum(trigger.lower() in query_lower for trigger in skill.triggers)
            lexical = min(1.0, overlap / union + math.log1p(trigger_hits) / 2)
            cosine = _cosine(query_vec, _hashed_features(skill.searchable_text))
            score = 0.7 * cosine + 0.3 * lexical
            if score > 0:
                ranked.append(RetrievedSkill(skill=skill, score=score))
        ranked.sort(key=lambda item: (-item.score, item.skill.skill_id))
        return tuple(ranked[:top_k])

    @property
    def index_version(self) -> str:
        return "hash-words-char3-v1-" + _content_hash(
            [(skill.skill_id, skill.content_hash) for skill in self.skills]
        )[:12]

    def render(self, retrieved: tuple[RetrievedSkill, ...]) -> str:
        lines = [f'<skill_context snapshot="{self.snapshot_id}">']
        lines.append("Use only applicable guidance; do not invent missing preconditions.")
        for item in retrieved:
            lines.append(f"\n[{item.skill.skill_id}] {item.skill.title}")
            lines.append(item.skill.summary)
            lines.extend(f"- {step}" for step in item.skill.instructions)
        lines.append("</skill_context>")
        return "\n".join(lines)


def extract_query(messages: list[dict[str, Any]]) -> str:
    parts: list[str] = []
    for message in messages:
        content = message.get("content", "")
        if isinstance(content, str):
            parts.append(content)
        elif isinstance(content, list):
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    parts.append(str(item.get("text", "")))
    return "\n".join(parts)


def inject_context(messages: list[dict[str, Any]], context: str) -> list[dict[str, Any]]:
    """Append an isolated context block without mutating the dataset sample."""

    copied = [dict(message) for message in messages]
    for index in range(len(copied) - 1, -1, -1):
        content = copied[index].get("content")
        if copied[index].get("role") == "user" and isinstance(content, str):
            copied[index]["content"] = f"{content}\n\n{context}"
            return copied
    copied.append({"role": "user", "content": context})
    return copied


def find_token_span(tokenizer: Any, prompt_ids: list[int], text: str) -> list[int] | None:
    """Locate the exact context content tokens inside the rendered prompt."""

    needle = tokenizer.encode(text, add_special_tokens=False)
    if not needle:
        return None
    limit = len(prompt_ids) - len(needle) + 1
    for start in range(max(limit, 0)):
        if prompt_ids[start : start + len(needle)] == needle:
            return [start, start + len(needle)]
    return None

