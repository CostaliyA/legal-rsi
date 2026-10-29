"""Run four independent API samples per Harvey task via VERL's tool state machine."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import traceback
from pathlib import Path

from examples.skill_evolving.api_harvey_rollout import completed_result
from examples.skill_evolving.api_verl_harvey_loop import ApiHarveySkillAgentLoop
from examples.skill_evolving.skill_store import SkillSnapshot


async def run_many(args: argparse.Namespace) -> list[dict]:
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Set DEEPSEEK_API_KEY or OPENAI_API_KEY")
    os.environ["OPENAI_API_KEY"] = key
    os.environ["OPENAI_BASE_URL"] = args.base_url
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    tasks = manifest[args.split]
    expected_tasks = 1 if args.split == "train" and args.protocol == "1x2" else 2 if args.protocol == "1x2" else 4
    if len(tasks) != expected_tasks or len(set(tasks)) != expected_tasks:
        raise ValueError(f"This protocol needs {expected_tasks} distinct tasks in {args.split}")
    if args.samples != 4:
        raise ValueError("This protocol needs exactly four independent samples per task")
    if not 0 < args.temperature <= 2:
        raise ValueError("temperature must be in (0,2]")
    if args.concurrency < 1:
        raise ValueError("concurrency must be positive")
    snapshot = SkillSnapshot.load(args.snapshot)
    args.output_root.mkdir(parents=True, exist_ok=True)
    slots = asyncio.Semaphore(args.concurrency)

    async def one(index: int, task_id: str, sample: int) -> dict:
        run_dir = args.output_root / f"{index:02d}-{task_id.replace('/', '__')}" / f"sample-{sample:02d}"
        async with slots:
            try:
                if run_dir.exists():
                    prior = await asyncio.to_thread(
                        completed_result, task_id, snapshot, run_dir, args.model, ""
                    )
                    if prior:
                        if prior.get("temperature") != args.temperature or prior.get("sample_index") != sample:
                            raise ValueError(f"Existing run has different sampling parameters: {run_dir}")
                        return {**prior, "sample_index": sample}
                    for archive_index in range(1, 1000):
                        archived = run_dir.with_name(f"{run_dir.name}.incomplete.{archive_index:03d}")
                        if not archived.exists():
                            run_dir.rename(archived)
                            break
                    else:
                        raise RuntimeError(f"Too many incomplete runs for {run_dir}")
                loop = ApiHarveySkillAgentLoop(
                    snapshot=snapshot, artifact_root=args.output_root, model=args.model,
                    temperature=args.temperature, max_turns=args.max_turns, top_k=args.top_k,
                    max_concurrent_sandboxes=args.concurrency,
                    retrieval_mode=args.retrieval_mode,
                )
                output = await loop.run(
                    {"temperature": args.temperature},
                    raw_prompt=[],
                    extra_info={"harvey_task_id": task_id},
                    harvey_run_dir=run_dir,
                )
                metadata = json.loads((run_dir / "rollout_metadata.json").read_text(encoding="utf-8"))
                if len(output.response_mask) == 0 or any(output.response_mask):
                    raise RuntimeError("API bridge must produce non-trainable placeholder mask")
                metadata.update({"sample_index": sample, "split": args.split})
                (run_dir / "rollout_metadata.json").write_text(
                    json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                return {"status": "complete", "task_id": task_id, "sample_index": sample,
                        "run_dir": str(run_dir), **metadata}
            except Exception as exc:
                error = {"status": "error", "task_id": task_id, "sample_index": sample,
                         "run_dir": str(run_dir), "error": str(exc), "traceback": traceback.format_exc()}
                run_dir.mkdir(parents=True, exist_ok=True)
                (run_dir / "error.json").write_text(json.dumps(error, ensure_ascii=False, indent=2))
                return error

    rows = await asyncio.gather(*(one(index, task_id, sample)
                                  for index, task_id in enumerate(tasks, 1)
                                  for sample in range(1, args.samples + 1)))
    (args.output_root / "summary.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--split", choices=["train", "test"], required=True)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--model", default="deepseek-flash")
    parser.add_argument("--base-url", default="https://api.deepseek.com")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--samples", type=int, default=4)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--max-turns", type=int, default=200)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--protocol", choices=["4x4", "1x2"], default="4x4")
    parser.add_argument("--retrieval-mode", choices=["lexical", "hybrid_router"], default="lexical")
    args = parser.parse_args()
    rows = asyncio.run(run_many(args))
    print(json.dumps({"completed": sum(row["status"] == "complete" for row in rows),
                      "errors": sum(row["status"] == "error" for row in rows),
                      "summary": str(args.output_root / "summary.json")}, indent=2))


if __name__ == "__main__":
    main()
