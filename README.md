# Harvey Skill Evolving：一键启动 rollout

本项目提供两种启动方式：**API 完整技能进化验证**，以及**本地 vLLM/SGLang rollout 与 Solver GRPO**。下面的命令均在本 README 所在目录执行，将示例中的路径换成实际绝对路径。

VERL 源码已经放在本仓库中：`verl/` 是完整 Python 库，`examples/skill_evolving/` 是安装好的实验扩展，根目录包含 `pyproject.toml`、`uv.lock`、`setup.py` 和原生训练入口所需配置。四个核心文件已经包含本次修改，`code/verl_core.patch` 保留对应差异。启动器默认使用当前仓库，不必另找 VERL checkout。

## 1. 运行环境

启动前需要准备：

- 本仓库根目录下准备好 `.venv/bin/python`，能导入 VERL 和本流程依赖。VERL 源码基线 commit 为 `2ab35292039a51175a4b3d3b3b2d76e951a0d3e4`；依赖环境使用 `uv` 管理，源码随包提供，虚拟环境不随包复制。
- 一个 Harvey LAB checkout，基线 commit 为 `794557ac1f40458dca87cf80ad538425a2d6942f`；其 `.venv/bin/python` 能执行 Harvey 任务与评分，任务材料已就绪。
- Docker、pandoc，以及可写的缓存目录。当前启动器使用随包的 Docker 兼容 shim。
- 包外的私有 API key 文件，内容为一行 key。API 流程用于模型生成及评分；本地模型流程只用它进行 Harvey 评分。

本地模型路径还需要空闲 GPU、兼容的 CUDA 环境，以及所选 `vllm`/`sglang` 与 `fsdp` 依赖。模型需支持当前 `hermes` 工具调用格式；其他格式需传入匹配配置。

启动器会检查并安装本包源码及四个 VERL 核心文件的补丁，随后准备配置并启动；不会自动安装驱动、下载模型或获取 Harvey 数据。目标文件已相同时直接复用，内容不同时会报错，不会覆盖。

## 2. API：一键运行完整 rollout 与技能进化验证

环境准备好后，执行这一条命令：

```bash
HARVEY_ROOT=/absolute/path/to/harvey-labs \
DEEPSEEK_API_KEY_FILE=/absolute/path/to/private/api_key \
TASK_DATA_ROOT=/absolute/path/to/writable/cache-root \
OUTPUT_ROOT="$PWD/runs/api_demo" \
bash code/api/run.sh
```

脚本直接使用随包的 11 技能父快照，无需重跑冷启动。默认模型与 judge 为 `deepseek-flash`，求解温度 `0.7`，并发 `4`。执行流程：

```text
训练题 1 道 × 4 次 rollout → Harvey 评分
→ Writer 生成 8 个候选 → 校验、冲突 staging、按来源任务选择候选
→ 创建独立 trial 快照
→ 验证题 2 道 × 旧库各 4 次、新库各 4 次 → Harvey 评分
→ 汇总增益与负迁移检查 → 发布新库或保留父库
```

共生成 20 条 Solver 轨迹。验证总体均值提高且每题均值不退步时，才发布试验库。候选选择只读取来源任务，验证题不参与候选选择。

API 生成接入真实 VERL `ToolAgentLoop.run` 状态机，复用 Harvey 工具、沙箱和技能检索；API 占位 token 全部不可训练，此入口不执行 actor 梯度更新。

可在上述命令前设置以下环境变量：

| 变量 | 默认值 | 作用 |
|---|---|---|
| `MODEL` | `deepseek-flash` | 求解与 Writer 模型 |
| `JUDGE_MODEL` | `deepseek-flash` | Harvey 评分模型 |
| `ROLLOUT_TEMPERATURE` | `0.7` | Solver 采样温度 |
| `CONCURRENCY` | `4` | Solver 并发数 |
| `JUDGE_CONCURRENCY` | `4` | 评分并发数 |
| `SEED_SNAPSHOT` | `data/02_no_gain_latest/parent_snapshot.json` | 固定父技能库，实际默认路径由启动器按包目录定位 |
| `OUTPUT_ROOT` | `runs/api_<时间>/` | 本次运行的输出目录 |
| `TASK_DATA_ROOT` | `/data0/zyr/agent` | 包、模型及临时缓存的根目录 |
| `VERL_ROOT` | 本仓库根目录 | 默认使用随包 VERL；需要时可指定其他兼容 checkout |

中断后，以**相同参数和相同 `OUTPUT_ROOT`** 重跑原命令，会复用已完整完成的阶段。更换模型、温度、任务或种子时，使用新的输出目录。

## 3. 本地模型：一键启动 vLLM/SGLang rollout

vLLM 入口：

```bash
HARVEY_ROOT=/absolute/path/to/harvey-labs \
MODEL_PATH=/absolute/path/to/tool-capable-model \
JUDGE_API_KEY_FILE=/absolute/path/to/private/judge_key \
TASK_DATA_ROOT=/absolute/path/to/writable/cache-root \
OUTPUT_ROOT="$PWD/runs/local_vllm_demo" \
bash code/local/run.sh vllm
```

使用 SGLang 时，将最后一行改为：

```bash
bash code/local/run.sh sglang
```

其余环境变量与 vLLM 命令相同，并需准备对应的 SGLang 依赖。

启动器自动生成 1 道训练题、2 道验证题的 Parquet 与固定技能快照配置，然后调用 `verl.trainer.main_ppo`。默认使用 GRPO，每道题 rollout 4 次，温度 `0.7`，运行 1 个 epoch。模型生成由选定的本地 rollout 后端执行。

这是固定快照的 Solver GRPO 组入口。原生 Writer 接口也在 `code/local/`，但本地一键脚本尚未串接完整的原生 probe 池与 Trainer 内自动快照发布；完整技能进化流程使用上一节的 API 入口。

本地资源与运行参数：

| 变量 | 默认值 | 作用 |
|---|---|---|
| `NGPUS_PER_NODE` | `8` | GPU 数 |
| `ROLLOUT_TP` | `2` | rollout tensor parallel 大小 |
| `AGENT_NUM_WORKERS` | `2` | AgentLoop worker 数 |
| `ROLLOUT_N` | `4` | 训练题采样次数，验证固定每题 4 次 |
| `MODEL_CHECKPOINT_ID` | `MODEL_PATH` | 固定模型版本标识 |
| `JUDGE_MODEL` | `deepseek-flash` | 评分模型 |
| `JUDGE_BASE_URL` | `https://api.deepseek.com` | 评分服务地址 |

例如，在配置好上述路径变量后调整资源：

```bash
NGPUS_PER_NODE=4 ROLLOUT_TP=1 AGENT_NUM_WORKERS=2 \
bash code/local/run.sh vllm trainer.total_epochs=1
```

本地入口的 `OUTPUT_ROOT` 应使用新的配置目录；已有 `group.json` 不会静默覆盖。

## 4. 输出在哪里

API 流程的结果写入 `OUTPUT_ROOT`：

```text
train/                     来源题 4 条轨迹与交付物
train_rewards.json         来源评分
writer_attempt_*/          Writer 候选、无效动作与生成记录
candidate.json             选中的技能维护动作
candidate_barrier.json     候选去重与冲突记录
parent_snapshot.json       本轮固定父库
trial_snapshot.json        候选对应的试验库
test_old/                  旧库下 8 条验证轨迹
test_new/                  试验库下 8 条验证轨迹
test_old_rewards.json      旧库评分
test_new_rewards.json      试验库评分
one_epoch_summary.json     逐题均值、总体增益与发布决策
published_snapshot.json    仅通过发布门槛时生成
```

单条运行目录包含 `transcript.jsonl`、`rollout_metadata.json`、`scores.json`、`rubric_feedback.json` 和生成的交付物。`one_epoch_summary.json` 的 `promoted` 表示是否发布，`next_snapshot_id` 表示下一组应加载的技能库。

本地流程在 `OUTPUT_ROOT` 生成 `train.parquet`、`validation.parquet`、`group.json` 和 `rollouts/`；训练日志由 VERL 输出到终端。

## 5. 查看已完成实验与展示数据

统一展示入口是 [showcase_data.json](showcase_data.json)，包含两组的逐次评分、逐题与总体 old/new 对比、技能修改前后正文、发布决策及轨迹相对路径。

| 字段 | 内容 |
|---|---|
| `reward_definition` / `reading_notes` | 奖励公式、发布门槛与比较口径 |
| `experiments[].summary` / `protocol` | 总体指标、发布结果及题数、采样次数 |
| `source_task_results` / `validation_task_results` | 逐题分数数组和均值 |
| `snapshots` / `skill_evolution` | 技能库、修改正文、候选与冲突信息 |
| `runs` | 每条轨迹的评分、轮数、用量、加载技能与证据路径 |
| `later_load_evidence` | 正向发布后的后续加载证据，不计入首轮增益 |

除顶层字段外，表中字段均在 `experiments[]` 内；证据路径相对本目录。

- `data/01_gain_epoch1/`：6 条实验轨迹及 1 条后续加载证据，平均增益 `+0.005319148936`，已发布。
- `data/02_no_gain_latest/`：最新 20 条轨迹，平均增益 `-0.000323498965`，未发布。

两组题目与协议不同，不能直接比较算法优劣；old/new API 采样也不共享随机种子。每组 `DATA_INDEX.json` 提供可移动的相对路径索引；原始工件内的历史服务器绝对路径保持原样。设计文档位于 `docs/`。

## 6. 只检查，不启动模型

检查随包源码摘要、数据路径、反馈哈希和 reward 计算：

```bash
python3 check_release.py
```

检查能否安装到目标 VERL，不写入文件：

```bash
python3 code/install_into_verl.py --verl-root "$PWD"
```

添加 `--apply` 才会安装；两个一键启动入口会自动执行安装。安装后模块路径恢复为 `examples.skill_evolving.*`，不要直接运行阅读用分组目录里的 Python 模块。
