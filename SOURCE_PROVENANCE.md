# 源码与实验来源

- VERL 基线 commit：`2ab35292039a51175a4b3d3b3b2d76e951a0d3e4`。
- Harvey LAB 基线 commit：`794557ac1f40458dca87cf80ad538425a2d6942f`。
- `code/verl_core.patch` 修改四个 VERL 核心文件；`code/install_manifest.json` 列出 40 个示例源码、配置和测试文件的目标路径及 SHA-256。
- `code/install_into_verl.py` 将阅读用的分组目录安装回 `examples.skill_evolving.*`，保留既有 import 路径。
- `LICENSE` 复制自上述 VERL checkout，保留原有许可文本；本次整理不更改 Harvey 任务材料和随附第三方文件的原有许可。
- `data/01_gain_epoch1` 保存正向发布的一轮及独立后续加载证据；`data/02_no_gain_latest` 保存最新 20 条轨迹和未发布决策。
- `showcase_data.json` 从两组原始工件汇总，证据路径相对仓库根目录；原始工件内历史绝对路径保持不变。
- 当前 API 验证未执行 actor 梯度更新；本地模型训练入口及原生集成边界见 README。

## 随包 VERL 源码

- `verl/` 包含原工作目录的完整 VERL Python 库，四个已修改核心文件均保留最终实现。
- 根目录包含源码构建/依赖文件及上游 scripts、tests、examples 和 docs；原上游 README 保存在 `README.verl.md`。
- `examples/skill_evolving/` 已按 manifest 安装全部 40 个实验扩展文件，`code/` 保留按职责分组的阅读入口与可审查补丁。
- API 与本地模型启动器默认 `VERL_ROOT` 为本仓库根目录，仍支持显式覆盖。
- 不复制原 `.git` 历史、虚拟环境、缓存、上游 CI/agent 配置；未展开的 `recipe` 子模块不在包内，本实验入口不依赖它。
