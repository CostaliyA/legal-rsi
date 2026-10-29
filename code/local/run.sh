#!/usr/bin/env bash
# Prepare a pinned native Solver group and launch VERL with vLLM or SGLang.
set -euo pipefail
DELIVERY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
: "${VERL_ROOT:?Set VERL_ROOT to the target VERL checkout}"
: "${HARVEY_ROOT:?Set HARVEY_ROOT to Harvey LAB}"
: "${MODEL_PATH:?Set MODEL_PATH to a local tool-capable checkpoint}"
ROLLOUT_BACKEND="${1:-${ROLLOUT_BACKEND:-vllm}}"
case "${ROLLOUT_BACKEND}" in vllm|sglang) ;; *) echo 'Use vllm or sglang' >&2; exit 2;; esac
if [[ $# -gt 0 ]]; then shift; fi
export VERL_ROOT HARVEY_ROOT MODEL_PATH ROLLOUT_BACKEND
OUTPUT_ROOT="${OUTPUT_ROOT:-${DELIVERY_ROOT}/runs/local_${ROLLOUT_BACKEND}_$(date +%Y%m%d_%H%M%S)}"
SEED_SNAPSHOT="${SEED_SNAPSHOT:-${DELIVERY_ROOT}/data/02_no_gain_latest/parent_snapshot.json}"
VERL_ROOT="$(cd "${VERL_ROOT}" && pwd)"
HARVEY_ROOT="$(cd "${HARVEY_ROOT}" && pwd)"
VERL_PYTHON="${VERL_PYTHON:-${VERL_ROOT}/.venv/bin/python}"
python3 "${DELIVERY_ROOT}/code/install_into_verl.py" --verl-root "${VERL_ROOT}" --apply
mkdir -p "${OUTPUT_ROOT}"
OUTPUT_ROOT="$(cd "${OUTPUT_ROOT}" && pwd)"
export PYTHONPATH="${VERL_ROOT}:${HARVEY_ROOT}${PYTHONPATH:+:${PYTHONPATH}}"
if [[ -n "${JUDGE_API_KEY_FILE:-}" ]]; then
  IFS= read -r OPENAI_API_KEY < "${JUDGE_API_KEY_FILE}" || true
  export OPENAI_API_KEY
fi
: "${OPENAI_API_KEY:?Set JUDGE_API_KEY_FILE or OPENAI_API_KEY for Harvey judge}"
export OPENAI_BASE_URL="${JUDGE_BASE_URL:-https://api.deepseek.com}"
cd "${VERL_ROOT}"
source examples/skill_evolving/cache_env.sh
"${VERL_PYTHON}" - "${DELIVERY_ROOT}" "${OUTPUT_ROOT}" "${SEED_SNAPSHOT}" "${MODEL_CHECKPOINT_ID:-${MODEL_PATH}}" "${JUDGE_MODEL:-deepseek-flash}" <<'PY'
import json,sys
from pathlib import Path
from examples.skill_evolving.prepare_harvey_data import prepare
from examples.skill_evolving.make_group_config import make_config
release,out,seed,checkpoint,judge=sys.argv[1:]
r=Path(out);m=json.loads((Path(release)/'code/shared/harvey_one_epoch_1x2_manifest.json').read_text())
prepare(m['train'],r/'train.parquet');prepare(m['test'],r/'validation.parquet')
make_config(Path(seed),r/'group.json',r/'rollouts',judge,'hybrid_router',checkpoint)
PY
export TRAIN_FILE="${OUTPUT_ROOT}/train.parquet"
export VAL_FILE="${OUTPUT_ROOT}/validation.parquet"
export AGENT_CONFIG="${OUTPUT_ROOT}/group.json"
export ROLLOUT_N="${ROLLOUT_N:-4}" TRAIN_BATCH_SIZE="${TRAIN_BATCH_SIZE:-1}"
exec bash examples/skill_evolving/run_harvey_grpo.sh \
  actor_rollout_ref.rollout.temperature="${ROLLOUT_TEMPERATURE:-0.7}" \
  actor_rollout_ref.rollout.val_kwargs.n=4 \
  actor_rollout_ref.rollout.val_kwargs.temperature="${ROLLOUT_TEMPERATURE:-0.7}" \
  "$@"
