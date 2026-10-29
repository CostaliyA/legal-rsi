#!/usr/bin/env bash
# One Writer GRPO group: five policy-authored candidates and paired probe reward.
set -euo pipefail

export TRAIN_BATCH_SIZE=1
export ROLLOUT_N=5

REWARD_FN="${PWD}/examples/skill_evolving/writer_reward_fn.py"
exec bash "${PWD}/examples/skill_evolving/run_harvey_grpo.sh" \
  actor_rollout_ref.rollout.agent.default_agent_loop=harvey_skill_writer \
  reward.custom_reward_function.path="${REWARD_FN}" \
  reward.custom_reward_function.name=compute_score \
  reward.num_workers=2 \
  trainer.test_freq=-1 \
  "$@"
