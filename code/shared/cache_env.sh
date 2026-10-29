#!/usr/bin/env bash
# Keep this experiment's package, model and temporary files under /data0.
TASK_DATA_ROOT="${TASK_DATA_ROOT:-/data0/zyr/agent}"
export UV_CACHE_DIR="${TASK_DATA_ROOT}/uv_cache"
export UV_PYTHON_INSTALL_DIR="${TASK_DATA_ROOT}/uv_python"
export XDG_CACHE_HOME="${TASK_DATA_ROOT}/cache/xdg"
export PIP_CACHE_DIR="${TASK_DATA_ROOT}/cache/pip"
export HF_HOME="${TASK_DATA_ROOT}/cache/huggingface"
export HF_HUB_CACHE="${HF_HOME}/hub"
export HF_DATASETS_CACHE="${HF_HOME}/datasets"
export TORCH_HOME="${TASK_DATA_ROOT}/cache/torch"
export TORCHINDUCTOR_CACHE_DIR="${TASK_DATA_ROOT}/cache/torch_inductor"
export TRITON_CACHE_DIR="${TASK_DATA_ROOT}/cache/triton"
export VLLM_CACHE_ROOT="${TASK_DATA_ROOT}/cache/vllm"
export CUDA_CACHE_PATH="${TASK_DATA_ROOT}/cache/cuda"
export MPLCONFIGDIR="${TASK_DATA_ROOT}/cache/matplotlib"
export WANDB_DIR="${TASK_DATA_ROOT}/cache/wandb"
export TMPDIR="${TASK_DATA_ROOT}/tmp"
export RAY_TMPDIR="${TASK_DATA_ROOT}/tmp/ray"
mkdir -p "${UV_CACHE_DIR}" "${UV_PYTHON_INSTALL_DIR}" "${XDG_CACHE_HOME}" "${PIP_CACHE_DIR}" \
  "${HF_HUB_CACHE}" "${HF_DATASETS_CACHE}" "${TORCH_HOME}" "${TORCHINDUCTOR_CACHE_DIR}" \
  "${TRITON_CACHE_DIR}" "${VLLM_CACHE_ROOT}" "${CUDA_CACHE_PATH}" \
  "${MPLCONFIGDIR}" "${WANDB_DIR}" "${TMPDIR}" "${RAY_TMPDIR}"
