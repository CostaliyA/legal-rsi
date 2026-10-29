"""Exercise the VERL Writer prompt/action parser with an API model."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from lab_core.harness.adapters.openai import OpenAIAdapter

from examples.skill_evolving.skill_store import SkillSnapshot
from examples.skill_evolving.writer_prompt import build_writer_messages
from examples.skill_evolving.writer_policy import parse_writer_action


def propose_one(index: int, snapshot: SkillSnapshot, sources: list[str], model: str, output_root: Path) -> dict:
    prompt = build_writer_messages(snapshot, sources)
    adapter = OpenAIAdapter(model=model, temperature=0.7, openai_hosted=False)
    response = adapter.chat(
        [adapter.make_system_message(prompt[0]["content"]), adapter.make_user_message(prompt[1]["content"])], []
    )
    raw = response.text
    try:
        proposal = parse_writer_action(raw, snapshot)
        proposal["source_runs"] = sources
        path = output_root / f"candidate-{index:02d}-{proposal['candidate_id']}.json"
        path.write_text(json.dumps(proposal, ensure_ascii=False, indent=2))
        return {"index": index, "status": "valid", "candidate_path": str(path),
                "candidate_id": proposal["candidate_id"], "action": proposal["action"]}
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        path = output_root / f"candidate-{index:02d}-invalid.json"
        path.write_text(json.dumps({"raw_response": raw, "error": str(exc)}, ensure_ascii=False, indent=2))
        return {"index": index, "status": "invalid", "error": str(exc), "path": str(path)}


async def run(args: argparse.Namespace) -> list[dict]:
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Set an API key for Writer API validation")
    os.environ["OPENAI_API_KEY"] = key
    os.environ["OPENAI_BASE_URL"] = args.base_url
    snapshot = SkillSnapshot.load(args.snapshot)
    rows = json.loads(args.source_summary.read_text(encoding="utf-8"))
    sources = [row["run_dir"] for row in rows if row["status"] == "complete"]
    if len(sources) < args.min_sources:
        raise ValueError(f"Writer validation needs {args.min_sources} completed source runs")
    args.output_root.mkdir(parents=True, exist_ok=False)
    slots = asyncio.Semaphore(args.concurrency)

    async def bounded(index: int) -> dict:
        async with slots:
            return await asyncio.to_thread(propose_one, index, snapshot, sources, args.model, args.output_root)

    results = await asyncio.gather(*(bounded(i) for i in range(1, args.n + 1)))
    (args.output_root / "writer_summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=2))
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-summary", required=True, type=Path)
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--model", default="deepseek-flash")
    parser.add_argument("--base-url", default="https://api.deepseek.com")
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--min-sources", type=int, default=10)
    parser.add_argument("--concurrency", type=int, default=5)
    args = parser.parse_args()
    results = asyncio.run(run(args))
    print(json.dumps({"valid": sum(row["status"] == "valid" for row in results),
                      "summary": str(args.output_root / "writer_summary.json")}, indent=2))


if __name__ == "__main__":
    main()
