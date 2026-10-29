"""Concurrent API verification of the same HarveyEpisode used by VERL.

API responses validate environment, retrieval and tool state, but provide no
native policy token IDs or old log probabilities and are never training data.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import traceback
from pathlib import Path

from lab_core.harness.adapters.openai import OpenAIAdapter

from examples.skill_evolving.harvey_episode import HarveyEpisode
from examples.skill_evolving.harvey_reward import score_episode
from examples.skill_evolving.skill_store import SkillSnapshot


def run_one(
    task_id: str,
    snapshot: SkillSnapshot,
    run_dir: Path,
    *,
    model: str,
    judge_model: str,
    max_turns: int,
    top_k: int,
) -> dict:
    episode = HarveyEpisode(task_id, snapshot, run_dir, top_k=top_k)
    adapter = OpenAIAdapter(model=model, temperature=0.0, openai_hosted=False)
    messages = [
        adapter.make_system_message(episode.messages[0]["content"]),
        adapter.make_user_message(episode.messages[1]["content"]),
    ]
    trace = []
    usage = {"input_tokens": 0, "output_tokens": 0}
    finish_reason = "max_turns"
    try:
        episode.start()
        for turn in range(1, max_turns + 1):
            response = adapter.chat(messages, episode.tools)
            usage["input_tokens"] += response.input_tokens
            usage["output_tokens"] += response.output_tokens
            tool_calls = [
                {"id": call.id, "name": call.name, "arguments": call.arguments}
                for call in response.tool_calls
            ]
            trace.append(
                {
                    "turn": turn,
                    "role": "assistant",
                    "text": response.text,
                    "tool_calls": tool_calls,
                    "input_tokens": response.input_tokens,
                    "output_tokens": response.output_tokens,
                    "finish_reason": response.finish_reason,
                }
            )
            messages.append(response.message)
            if not response.tool_calls:
                finish_reason = "no_tool_calls"
                break
            results = []
            for call in response.tool_calls:
                result = episode.execute(call.name, call.arguments)
                results.append((call.id, result))
                trace.append(
                    {
                        "turn": turn,
                        "role": "tool",
                        "tool_call_id": call.id,
                        "tool_name": call.name,
                        "arguments": call.arguments,
                        "result": result,
                    }
                )
            messages.extend(adapter.make_tool_result_messages(results))
            if episode.finished:
                finish_reason = "finish_tool"
                break
        with (run_dir / "transcript.jsonl").open("w", encoding="utf-8") as stream:
            for row in trace:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        metadata = episode.metadata()
        metadata.update(
            {
                "model": model,
                "api_test_only": True,
                "native_policy_token_ids_available": False,
                "turn_count": sum(row["role"] == "assistant" for row in trace),
                "finish_reason": finish_reason,
                "usage": usage,
            }
        )
        (run_dir / "rollout_metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2))
        if judge_model:
            scores = score_episode(episode.task, run_dir, judge_model)
            metadata["reward_task"] = scores["reward_task"]
            metadata["all_pass"] = scores["all_pass"]
        return {"status": "complete", "task_id": task_id, "run_dir": str(run_dir), **metadata}
    finally:
        episode.close()


def completed_result(task_id: str, snapshot: SkillSnapshot, run_dir: Path,
                     model: str, judge_model: str) -> dict | None:
    metadata_path = run_dir / "rollout_metadata.json"
    transcript_path = run_dir / "transcript.jsonl"
    if not (metadata_path.exists() and transcript_path.exists()):
        return None
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if transcript_path.stat().st_size == 0:
        return None
    if (metadata.get("task_id") != task_id
            or metadata.get("skill_snapshot_id") != snapshot.snapshot_id
            or metadata.get("model") != model):
        raise ValueError(f"Existing rollout has a different task, snapshot, or model: {run_dir}")
    if judge_model:
        score_path = run_dir / "scores.json"
        if score_path.exists():
            scores = json.loads(score_path.read_text(encoding="utf-8"))
            if scores.get("task_id") != task_id or scores.get("judge_model") != judge_model:
                raise ValueError(f"Existing score has a different task or judge: {score_path}")
            if scores.get("n_grading_errors") != 0:
                raise ValueError(f"Existing score has grading errors: {score_path}")
        else:
            from lab_core.harness.run import load_task

            scores = score_episode(load_task(task_id), run_dir, judge_model)
        metadata["reward_task"] = scores["reward_task"]
        metadata["all_pass"] = scores["all_pass"]
    return {"status": "complete", "task_id": task_id, "run_dir": str(run_dir), **metadata}


async def run_many(args: argparse.Namespace) -> list[dict]:
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Set DEEPSEEK_API_KEY or OPENAI_API_KEY for API validation")
    os.environ["OPENAI_API_KEY"] = key
    os.environ["OPENAI_BASE_URL"] = args.base_url
    if args.concurrency < 1:
        raise ValueError("concurrency must be positive")
    snapshot = SkillSnapshot.load(args.snapshot)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    tasks = manifest[args.split]
    if not tasks or len(tasks) != len(set(tasks)):
        raise ValueError("Task list must be nonempty and unique")
    args.output_root.mkdir(parents=True, exist_ok=True)
    slots = asyncio.Semaphore(args.concurrency)

    async def bounded(index: int, task_id: str) -> dict:
        run_dir = args.output_root / f"{index:02d}-{task_id.replace('/', '__')}"
        async with slots:
            try:
                if run_dir.exists():
                    previous = await asyncio.to_thread(
                        completed_result, task_id, snapshot, run_dir, args.model, args.judge_model
                    )
                    if previous is not None:
                        return previous
                    for archive_index in range(1, 1000):
                        archived = run_dir.with_name(f"{run_dir.name}.incomplete.{archive_index:03d}")
                        if not archived.exists():
                            run_dir.rename(archived)
                            break
                    else:
                        raise RuntimeError(f"Too many incomplete runs for {run_dir}")
                run_dir.mkdir()
                return await asyncio.to_thread(
                    run_one, task_id, snapshot, run_dir,
                    model=args.model, judge_model=args.judge_model,
                    max_turns=args.max_turns, top_k=args.top_k,
                )
            except Exception as exc:
                row = {"status": "error", "task_id": task_id, "run_dir": str(run_dir), "error": str(exc),
                       "traceback": traceback.format_exc()}
                if run_dir.exists():
                    (run_dir / "error.json").write_text(json.dumps(row, ensure_ascii=False, indent=2))
                return row

    results = await asyncio.gather(*(bounded(index, task) for index, task in enumerate(tasks, start=1)))
    (args.output_root / "summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=2))
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--split", choices=["initial", "final"], required=True)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--model", default="deepseek-flash")
    parser.add_argument("--base-url", default="https://api.deepseek.com")
    parser.add_argument("--judge-model", default="")
    parser.add_argument("--max-turns", type=int, default=200)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--concurrency", type=int, default=5)
    args = parser.parse_args()
    results = asyncio.run(run_many(args))
    print(json.dumps({"completed": sum(item["status"] == "complete" for item in results),
                      "errors": sum(item["status"] == "error" for item in results),
                      "summary": str(args.output_root / "summary.json")}, indent=2))


if __name__ == "__main__":
    main()
