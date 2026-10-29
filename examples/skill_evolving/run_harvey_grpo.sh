#!/usr/bin/env bash
# Run one fixed-snapshot Harvey/VERL GRPO group. Run from the VERL checkout.
set -euo pipefail

: "${MODEL_PATH:?Set MODEL_PATH to a local tool-capable model}"
: "${TRAIN_FILE:?Set TRAIN_FILE to prepared Harvey Parquet}"
: "${VAL_FILE:?Set VAL_FILE to separate Harvey validation Parquet}"
: "${AGENT_CONFIG:?Set AGENT_CONFIG to a generated, pinned group config}"
: "${HARVEY_ROOT:?Set HARVEY_ROOT to the Harvey LAB checkout}"
source "${PWD}/examples/skill_evolving/cache_env.sh"

export PYTHONPATH="${PWD}:${HARVEY_ROOT}${PYTHONPATH:+:${PYTHONPATH}}"
export PATH="${PWD}/examples/skill_evolving/podman_compat:${PATH}"

ROLLOUT_BACKEND=${ROLLOUT_BACKEND:-vllm}
case "${ROLLOUT_BACKEND}" in
  vllm|sglang) ;;
  *) echo "ROLLOUT_BACKEND must be vllm or sglang" >&2; exit 2 ;;
esac
AGENT_NUM_WORKERS=${AGENT_NUM_WORKERS:-2}
ROLLOUT_N=${ROLLOUT_N:-2}
TRAIN_BATCH_SIZE=${TRAIN_BATCH_SIZE:-4}
NGPUS_PER_NODE=${NGPUS_PER_NODE:-8}
PROMPT_LENGTH=${PROMPT_LENGTH:-8192}
RESPONSE_LENGTH=${RESPONSE_LENGTH:-32768}
ROLLOUT_TP=${ROLLOUT_TP:-2}

uv run --frozen --no-sync --all-packages --extra "${ROLLOUT_BACKEND}" --extra fsdp python3 -m verl.trainer.main_ppo \
  algorithm.adv_estimator=grpo \
  data.train_files="${TRAIN_FILE}" \
  data.val_files="${VAL_FILE}" \
  data.train_batch_size="${TRAIN_BATCH_SIZE}" \
  data.max_prompt_length="${PROMPT_LENGTH}" \
  data.max_response_length="${RESPONSE_LENGTH}" \
  actor_rollout_ref.model.path="${MODEL_PATH}" \
  actor_rollout_ref.model.use_remove_padding=True \
  actor_rollout_ref.model.enable_gradient_checkpointing=True \
  actor_rollout_ref.actor.ppo_mini_batch_size="${TRAIN_BATCH_SIZE}" \
  actor_rollout_ref.actor.use_dynamic_bsz=True \
  actor_rollout_ref.rollout.name="${ROLLOUT_BACKEND}" \
  actor_rollout_ref.rollout.tensor_model_parallel_size="${ROLLOUT_TP}" \
  actor_rollout_ref.rollout.prompt_length="${PROMPT_LENGTH}" \
  actor_rollout_ref.rollout.response_length="${RESPONSE_LENGTH}" \
  actor_rollout_ref.rollout.n="${ROLLOUT_N}" \
  actor_rollout_ref.rollout.multi_turn.enable=True \
  actor_rollout_ref.rollout.multi_turn.format=hermes \
  actor_rollout_ref.rollout.agent.agent_loop_config_path="${AGENT_CONFIG}" \
  actor_rollout_ref.rollout.agent.default_agent_loop=harvey_skill_agent \
  actor_rollout_ref.rollout.agent.num_workers="${AGENT_NUM_WORKERS}" \
  trainer.n_gpus_per_node="${NGPUS_PER_NODE}" \
  trainer.nnodes=1 \
  trainer.logger='["console"]' \
  trainer.total_epochs=1 \
  ray_kwargs.ray_init.runtime_env.py_executable="uv -v run --frozen --no-sync --all-packages --extra ${ROLLOUT_BACKEND} --extra fsdp" \
  "$@"
