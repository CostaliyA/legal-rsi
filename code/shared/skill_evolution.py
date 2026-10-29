"""Stage skill proposals and publish snapshots only at a rollout-group barrier."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

from examples.skill_evolving.skill_store import Skill, SkillSnapshot, _content_hash


ID_RE = re.compile(r"^[a-z][a-z0-9-]{2,63}$")


def validate_candidate(raw: dict, parent: SkillSnapshot, *, bootstrap: bool = False) -> dict:
    if raw.get("parent_snapshot_id") != parent.snapshot_id:
        raise ValueError("Candidate parent does not match the pinned snapshot")
    sources = raw.get("source_runs")
    if not isinstance(sources, list) or len(set(sources)) < 2:
        raise ValueError("A candidate needs at least two distinct source rollouts")
    if not all(isinstance(item, str) and item for item in sources):
        raise ValueError("Invalid source run")
    candidate = raw.get("skill")
    if not isinstance(candidate, dict):
        raise ValueError("Candidate skill must be an object")
    skill = Skill.from_dict(candidate)
    if not ID_RE.fullmatch(skill.skill_id):
        raise ValueError("Skill ID must be a stable lowercase slug")
    if len(skill.instructions) < 2 or len(skill.instructions) > 8:
        raise ValueError("Skill must have two to eight concrete steps")
    if any(len(step) > 500 or not step.strip() for step in skill.instructions):
        raise ValueError("Skill instructions are empty or too long")
    if any(item.skill_id == skill.skill_id for item in parent.skills):
        raise ValueError("Skill ID already exists in the parent snapshot")
    return skill.to_dict()


def verify_paired_scores(
    path: Path,
    *,
    min_pairs: int = 2,
    max_regression: float = 0.0,
    expected_parent: str | None = None,
    expected_skill_id: str | None = None,
    expected_candidate_snapshot: str | None = None,
    source_runs: list[str] | None = None,
) -> dict:
    """Evaluate a candidate on paired, held-out task/seed runs before publish."""
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if expected_parent is not None and manifest.get("parent_snapshot_id") != expected_parent:
        raise ValueError("Paired scores use a different parent snapshot")
    if expected_skill_id is not None and manifest.get("candidate_skill_id") != expected_skill_id:
        raise ValueError("Paired scores use a different candidate")
    if expected_candidate_snapshot is not None and manifest.get("candidate_snapshot_id") != expected_candidate_snapshot:
        raise ValueError("Paired scores use a different candidate snapshot")
    pairs = manifest.get("pairs")
    if not isinstance(pairs, list) or len(pairs) < min_pairs:
        raise ValueError("Need at least two held-out paired rollouts")
    keys = set()
    source_paths = {str(Path(item).resolve()) for item in source_runs or []}
    for pair in pairs:
        key = (pair.get("task_id"), pair.get("seed"))
        if not key[0] or key in keys:
            raise ValueError("Paired rollout task/seed keys must be unique")
        keys.add(key)
        if expected_parent is not None:
            for side in ("parent", "candidate"):
                score_path = Path(pair[f"{side}_scores_path"]).resolve()
                if str(score_path.parent) in source_paths:
                    raise ValueError("Held-out evaluation overlaps candidate source runs")
                scored = json.loads(score_path.read_text(encoding="utf-8"))
                scored_task = scored.get("task_id", scored.get("task"))
                if scored_task != pair["task_id"] or scored.get("n_grading_errors"):
                    raise ValueError("Paired score artifact has wrong task or grading errors")
                metadata_path = score_path.parent / "rollout_metadata.json"
                if not metadata_path.exists():
                    metadata_path = score_path.parent / "skill_provenance.json"
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                expected_snapshot = expected_parent if side == "parent" else expected_candidate_snapshot
                if metadata.get("skill_snapshot_id") != expected_snapshot:
                    raise ValueError("Paired rollout used the wrong skill snapshot")
                if (scored["score"], scored["max_score"]) != (
                    pair[f"{side}_score"], pair[f"{side}_max_score"]
                ):
                    raise ValueError("Paired score values differ from the score artifact")
        for side in ("parent", "candidate"):
            score = pair.get(f"{side}_score")
            count = pair.get(f"{side}_max_score")
            if not isinstance(score, (int, float)) or not isinstance(count, (int, float)):
                raise ValueError("Paired scores must be numeric")
            if count <= 0 or score < 0 or score > count:
                raise ValueError("Paired scores out of range")
    parent_rates = [p["parent_score"] / p["parent_max_score"] for p in pairs]
    candidate_rates = [p["candidate_score"] / p["candidate_max_score"] for p in pairs]
    deltas = [new - old for new, old in zip(candidate_rates, parent_rates)]
    if min(deltas) < -max_regression or sum(deltas) <= 0:
        raise ValueError("Candidate failed held-out paired utility gate")
    return {"pairs": len(pairs), "mean_delta": sum(deltas) / len(deltas), "min_delta": min(deltas)}


def _next_payload(parent: SkillSnapshot, skill: dict, version: str) -> tuple[dict, str]:
    payload = {
        "version": version,
        "skills": [old.to_dict() for old in parent.skills] + [skill],
    }
    snapshot_payload = {
        "version": version,
        "skills": [{"id": item["id"], "hash": Skill.from_dict(item).content_hash} for item in payload["skills"]],
    }
    return payload, f"{version}-{_content_hash(snapshot_payload)[:12]}"


def stage_shadow(parent_path: Path, candidate_path: Path, output_path: Path, version: str) -> dict:
    """Materialize a candidate snapshot for read-only held-out evaluation."""
    parent = SkillSnapshot.load(parent_path)
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
    skill = validate_candidate(candidate, parent)
    payload, snapshot_id = _next_payload(parent, skill, version)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
    return {"shadow_path": str(output_path.resolve()), "snapshot_id": snapshot_id}


def publish(
    parent_path: Path,
    candidate_path: Path,
    output_path: Path,
    *,
    version: str,
    paired_scores: Path | None = None,
    bootstrap: bool = False,
) -> dict:
    parent = SkillSnapshot.load(parent_path)
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
    skill = validate_candidate(candidate, parent, bootstrap=bootstrap)
    payload, candidate_snapshot_id = _next_payload(parent, skill, version)
    if bootstrap:
        if parent.skills:
            raise ValueError("Bootstrap requires an empty parent snapshot")
    else:
        if paired_scores is None:
            raise ValueError("Evolution requires held-out paired scores")
        verify_paired_scores(
            paired_scores,
            expected_parent=parent.snapshot_id,
            expected_skill_id=skill["id"],
            expected_candidate_snapshot=candidate_snapshot_id,
            source_runs=candidate["source_runs"],
        )
    if output_path.exists() or output_path.resolve() == parent_path.resolve():
        raise FileExistsError("Snapshots are immutable; choose a new output path")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive create is the coordinator barrier: two writers cannot publish
    # the same version, and no rollout ever observes a partly written file.
    temporary = output_path.with_name(output_path.name + f".{os.getpid()}.tmp")
    with temporary.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
        stream.flush()
        os.fsync(stream.fileno())
    try:
        os.link(temporary, output_path)
    finally:
        temporary.unlink(missing_ok=True)
    snapshot = SkillSnapshot.load(output_path)
    if snapshot.snapshot_id != candidate_snapshot_id:
        raise AssertionError("Published snapshot ID differs from the evaluated snapshot")
    return {
        "snapshot_path": str(output_path.resolve()),
        "snapshot_id": snapshot.snapshot_id,
        "parent_snapshot_id": parent.snapshot_id,
        "candidate_source_runs": candidate["source_runs"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--paired-scores", type=Path)
    parser.add_argument("--bootstrap", action="store_true")
    parser.add_argument("--shadow", action="store_true", help="Write an evaluation-only candidate snapshot")
    args = parser.parse_args()
    if args.shadow:
        result = stage_shadow(args.parent, args.candidate, args.output, args.version)
    else:
        result = publish(args.parent, args.candidate, args.output, version=args.version,
                         paired_scores=args.paired_scores, bootstrap=args.bootstrap)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
