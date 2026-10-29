"""Build VERL Parquet samples from Harvey's official task instructions."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from lab_core.harness.run import load_task


def prepare(task_ids: list[str], output: Path) -> None:
    if not task_ids:
        raise ValueError("At least one Harvey task is required")
    rows = []
    for index, task_id in enumerate(task_ids):
        task = load_task(task_id)
        rows.append(
            {
                "data_source": "harvey_lab",
                "prompt": [{"role": "user", "content": task["instructions"]}],
                "agent_name": "harvey_skill_agent",
                "extra_info": {"harvey_task_id": task_id, "index": index},
            }
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_parquet(output, index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", action="append", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    prepare(args.task, args.output)


if __name__ == "__main__":
    main()
