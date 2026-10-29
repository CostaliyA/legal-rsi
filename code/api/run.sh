#!/usr/bin/env bash
# Full API verification epoch: train4 -> Writer -> validation old8/new8 -> gate.
set -euo pipefail
DELIVERY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
: "${VERL_ROOT:?Set VERL_ROOT to the target VERL checkout}"
: "${HARVEY_ROOT:?Set HARVEY_ROOT to Harvey LAB}"
: "${DEEPSEEK_API_KEY_FILE:?Set DEEPSEEK_API_KEY_FILE to a private key file}"
VERL_ROOT="$(cd "${VERL_ROOT}" && pwd)"
HARVEY_ROOT="$(cd "${HARVEY_ROOT}" && pwd)"
python3 "${DELIVERY_ROOT}/code/install_into_verl.py" --verl-root "${VERL_ROOT}" --apply
export HARVEY_ROOT DEEPSEEK_API_KEY_FILE
export OUTPUT_ROOT="${OUTPUT_ROOT:-${DELIVERY_ROOT}/runs/api_$(date +%Y%m%d_%H%M%S)}"
export SEED_SNAPSHOT="${SEED_SNAPSHOT:-${DELIVERY_ROOT}/data/02_no_gain_latest/parent_snapshot.json}"
mkdir -p "${OUTPUT_ROOT}"
export OUTPUT_ROOT="$(cd "${OUTPUT_ROOT}" && pwd)"
cd "${VERL_ROOT}"
exec bash examples/skill_evolving/run_api_one_epoch.sh "$@"
