"""Select one substantive, valid API Writer action for the protocol run."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.skill_router import SkillRouter
from examples.skill_evolving.writer_policy import stage_action_snapshot
from examples.skill_evolving.candidate_barrier import stage_candidates


def _task_retrieval_changes(candidate: dict, snapshot: SkillSnapshot, task_ids: list[str],
                            retrieval_mode: str = "lexical") -> int:
    from lab_core.harness.run import load_task

    with tempfile.TemporaryDirectory(prefix="writer-reachability-") as temporary:
        trial = stage_action_snapshot(snapshot, candidate, Path(temporary) / "trial.json")
        changed = 0
        for task_id in task_ids:
            query = load_task(task_id)["instructions"]
            domain, task_name = task_id.split("/", 1)
            pattern = task_name.split("-", 1)[0]
            kwargs = {"operation_pattern": pattern, "legal_domain": domain, "top_k": 3}
            if retrieval_mode == "hybrid_router":
                router = SkillRouter(top_k=8, top_n=3)
                old, _ = router.choose(snapshot, task_id, query, pattern, domain)
                new, _ = router.choose(trial, task_id, query, pattern, domain)
            elif retrieval_mode == "lexical":
                old = snapshot.retrieve(query, **kwargs)
                new = trial.retrieve(query, **kwargs)
            else:
                raise ValueError(f"Unknown retrieval mode: {retrieval_mode}")
            signature = lambda items: [(item.skill.skill_id, item.skill.content_hash) for item in items]
            changed += signature(old) != signature(new)
        return changed


def _source_retrieval_changes(candidate: dict, snapshot: SkillSnapshot, source_summary: Path,
                              retrieval_mode: str = "lexical") -> int:
    rows = json.loads(source_summary.read_text(encoding="utf-8"))
    return _task_retrieval_changes(candidate, snapshot, [row["task_id"] for row in rows], retrieval_mode)


def select(summary_path: Path, output_path: Path, snapshot_path: Path | None = None,
           source_summary: Path | None = None, validation_tasks: list[str] | None = None,
           retrieval_mode: str = "lexical") -> dict:
    if (snapshot_path is None) != (source_summary is None):
        raise ValueError("snapshot_path and source_summary must be supplied together")
    snapshot = SkillSnapshot.load(snapshot_path) if snapshot_path else None
    rows = json.loads(summary_path.read_text(encoding="utf-8"))
    if snapshot:
        barrier = stage_candidates(snapshot, rows, output_path.parent / "staging")
        (output_path.parent / "candidate_barrier.json").write_text(
            json.dumps(barrier, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        candidate_rows = [{"status": "valid", "action": item["action"]["action"],
                           "candidate_path": item["staged_path"]} for item in barrier["candidates"]]
    else:
        candidate_rows = rows
    for row in candidate_rows:
        if row["status"] == "valid" and row["action"] != "NO_CHANGE":
            candidate = json.loads(Path(row["candidate_path"]).read_text(encoding="utf-8"))
            changes = _source_retrieval_changes(candidate, snapshot, source_summary, retrieval_mode) if snapshot else None
            if changes == 0:
                continue
            validation_changes = (
                _task_retrieval_changes(candidate, snapshot, validation_tasks, retrieval_mode)
                if snapshot and validation_tasks else None
            )
            if validation_tasks and validation_changes != len(validation_tasks):
                continue
            output_path.write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding="utf-8")
            return {"candidate_id": candidate["candidate_id"], "action": candidate["action"],
                    "source_path": row["candidate_path"], "output_path": str(output_path),
                    "source_retrieval_changes": changes,
                    "validation_retrieval_changes": validation_changes}
    raise ValueError("Writer produced no valid substantive action exposed on the required tasks")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--writer-summary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--source-summary", type=Path)
    parser.add_argument("--validation-task", action="append", default=[])
    parser.add_argument("--allow-validation-exposure", action="store_true")
    parser.add_argument("--retrieval-mode", choices=["lexical", "hybrid_router"], default="lexical")
    args = parser.parse_args()
    if args.validation_task and not args.allow_validation_exposure:
        parser.error("--validation-task requires explicit --allow-validation-exposure; keep final tests untouched")
    print(json.dumps(select(args.writer_summary, args.output, args.snapshot, args.source_summary,
                            args.validation_task, args.retrieval_mode),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
