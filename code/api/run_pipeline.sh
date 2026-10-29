#!/usr/bin/env bash
# Thirty scored cold-start sources -> one 1x2 hybrid-Router VERL/API epoch.
set -euo pipefail

: "${HARVEY_ROOT:?Set HARVEY_ROOT to the Harvey LAB checkout}"
: "${DEEPSEEK_API_KEY_FILE:?Set DEEPSEEK_API_KEY_FILE to a private key file}"
: "${OUTPUT_ROOT:?Set OUTPUT_ROOT to the one-epoch artifact directory}"
: "${SEED_SNAPSHOT:?Set SEED_SNAPSHOT to a seed snapshot file}"

VERL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
EXAMPLE_ROOT="${VERL_ROOT}/examples/skill_evolving"
source "${EXAMPLE_ROOT}/cache_env.sh"
export PYTHONPATH="${VERL_ROOT}:${HARVEY_ROOT}${PYTHONPATH:+:${PYTHONPATH}}"
export PATH="${EXAMPLE_ROOT}/podman_compat:/data0/zyr/agent/bin:${PATH}"
IFS= read -r DEEPSEEK_API_KEY < "${DEEPSEEK_API_KEY_FILE}" || true
export DEEPSEEK_API_KEY
export OPENAI_API_KEY="${DEEPSEEK_API_KEY}"
export OPENAI_BASE_URL="https://api.deepseek.com"

VERL_PY="${VERL_ROOT}/.venv/bin/python"
HARVEY_PY="${HARVEY_ROOT}/.venv/bin/python"
MANIFEST="${EXAMPLE_ROOT}/harvey_one_epoch_1x2_manifest.json"
SEED="${SEED_SNAPSHOT}"
TRIAL="${OUTPUT_ROOT}/trial_snapshot.json"
PARENT="${OUTPUT_ROOT}/parent_snapshot.json"
MODEL="${MODEL:-deepseek-flash}"
JUDGE_MODEL="${JUDGE_MODEL:-deepseek-flash}"
ROLLOUT_TEMPERATURE="${ROLLOUT_TEMPERATURE:-0.7}"
CONCURRENCY="${CONCURRENCY:-4}"
JUDGE_CONCURRENCY="${JUDGE_CONCURRENCY:-4}"

mkdir -p "${OUTPUT_ROOT}"
test -f "${SEED}"
if [[ ! -f "${PARENT}" ]]; then
  cp "${SEED}" "${PARENT}"
fi

"${VERL_PY}" -m examples.skill_evolving.run_api_verl_4x \
  --manifest "${MANIFEST}" --split train --snapshot "${PARENT}" \
  --output-root "${OUTPUT_ROOT}/train" --model "${MODEL}" \
  --temperature "${ROLLOUT_TEMPERATURE}" --concurrency "${CONCURRENCY}" \
  --protocol 1x2 --retrieval-mode hybrid_router
"${HARVEY_PY}" -m examples.skill_evolving.score_existing_rollouts \
  --summary "${OUTPUT_ROOT}/train/summary.json" --output "${OUTPUT_ROOT}/train_rewards.json" \
  --model "${JUDGE_MODEL}" --concurrency "${JUDGE_CONCURRENCY}"

if [[ ! -f "${OUTPUT_ROOT}/candidate.json" ]]; then
  selected=0
  for attempt in 1 2 3; do
    writer_dir="${OUTPUT_ROOT}/writer_attempt_${attempt}"
    if [[ ! -f "${writer_dir}/writer_summary.json" ]]; then
      if [[ -e "${writer_dir}" ]]; then
        mv "${writer_dir}" "${writer_dir}.incomplete.$(date +%s)"
      fi
      "${HARVEY_PY}" -m examples.skill_evolving.api_writer \
        --source-summary "${OUTPUT_ROOT}/train/summary.json" --snapshot "${PARENT}" \
        --output-root "${writer_dir}" --model "${MODEL}" --n 8 \
        --min-sources 4 --concurrency 4
    fi
    selection=("${HARVEY_PY}" -m examples.skill_evolving.select_writer_candidate \
      --writer-summary "${writer_dir}/writer_summary.json" \
      --output "${OUTPUT_ROOT}/candidate.json" --snapshot "${PARENT}" \
      --source-summary "${OUTPUT_ROOT}/train/summary.json" \
      --retrieval-mode hybrid_router)
    if "${selection[@]}"; then
      selected=1
      break
    fi
  done
  if [[ "${selected}" != 1 ]]; then
    echo "No Writer candidate changed source-task hybrid Router retrieval" >&2
    exit 1
  fi
fi

if [[ ! -f "${TRIAL}" ]]; then
  "${HARVEY_PY}" -m examples.skill_evolving.commit_trial \
    --parent "${PARENT}" --candidate "${OUTPUT_ROOT}/candidate.json" --trial "${TRIAL}"
fi

for side in old new; do
  snapshot="${PARENT}"
  if [[ "${side}" == new ]]; then snapshot="${TRIAL}"; fi
  "${VERL_PY}" -m examples.skill_evolving.run_api_verl_4x \
    --manifest "${MANIFEST}" --split test --snapshot "${snapshot}" \
    --output-root "${OUTPUT_ROOT}/test_${side}" --model "${MODEL}" \
    --temperature "${ROLLOUT_TEMPERATURE}" --concurrency "${CONCURRENCY}" \
    --protocol 1x2 --retrieval-mode hybrid_router
  "${HARVEY_PY}" -m examples.skill_evolving.score_existing_rollouts \
    --summary "${OUTPUT_ROOT}/test_${side}/summary.json" \
    --output "${OUTPUT_ROOT}/test_${side}_rewards.json" \
    --model "${JUDGE_MODEL}" --concurrency "${JUDGE_CONCURRENCY}"
done

"${HARVEY_PY}" -m examples.skill_evolving.summarize_one_epoch_4x \
  --manifest "${MANIFEST}" --parent "${PARENT}" --trial "${TRIAL}" \
  --train-summary "${OUTPUT_ROOT}/train/summary.json" \
  --old-summary "${OUTPUT_ROOT}/test_old/summary.json" \
  --new-summary "${OUTPUT_ROOT}/test_new/summary.json" \
  --temperature "${ROLLOUT_TEMPERATURE}" \
  --model "${MODEL}" --judge-model "${JUDGE_MODEL}" \
  --protocol 1x2 --retrieval-mode hybrid_router \
  --candidate-barrier "${OUTPUT_ROOT}/candidate_barrier.json" \
  --published "${OUTPUT_ROOT}/published_snapshot.json" \
  --output "${OUTPUT_ROOT}/one_epoch_summary.json"
