# 源码与实验来源

- VERL 基线 commit：`2ab35292039a51175a4b3d3b3b2d76e951a0d3e4`。
- Harvey LAB 基线 commit：`794557ac1f40458dca87cf80ad538425a2d6942f`。
- `code/verl_core.patch` 修改四个 VERL 核心文件；`code/install_manifest.json` 列出 40 个示例源码、配置和测试文件的目标路径及 SHA-256。
- `code/install_into_verl.py` 将阅读用的分组目录安装回 `examples.skill_evolving.*`，保留既有 import 路径。
- `LICENSE` 复制自上述 VERL checkout，保留原有许可文本；本次整理不更改 Harvey 任务材料和随附第三方文件的原有许可。
- `data/01_gain_epoch1` 保存正向发布的一轮及独立后续加载证据；`data/02_no_gain_latest` 保存最新 20 条轨迹和未发布决策。
- `showcase_data.json` 从两组原始工件汇总，证据路径相对仓库根目录；原始工件内历史绝对路径保持不变。
- 当前 API 验证未执行 actor 梯度更新；本地模型训练入口及原生集成边界见 README。
