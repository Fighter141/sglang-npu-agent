# Source 登记与迁移状态

| Source | 用途 | 当前策略 |
|---|---|---|
| CANNBot / CANNBot Skills | Agent、Skill、安装分发 | 选择性迁移通用流程 |
| CANNBot Knowledge | Knowledge Bundle、Schema、Ingest / Query / Lint | 优先核查格式和治理 |
| CANNBot DSL / CANN Bench / Sentry | 算子、测试、质量 | 按需抽取 |
| MindIE remote-dev / coordinator | 远程执行、资源管理 | 评估独立组件 |
| MindIE profiler / debugger | Trace 分析、故障诊断 | 评估独立能力 |
| Ascend Agent Skills | AscendC、精度、编译工作流 | 选择性迁移 |
| Ascend msprobe | 推理精度诊断 | 外部工具 + Skill 编排 |
| Ascend msprof | 性能采集 | 官方采集底座 |
| Ascend msit | Profile、预检及工具入口 | 按组件集成 |
| Ascend msmonitor | 设备资源监控 | 指标适配 |
| Ascend torch_npu | Runtime / API | 版本化知识索引 |
| SGLang | 框架行为与 Ascend 后端 | 直接检索上游，不重复复制其 Skills |

## 迁移状态
- `candidate`：已识别，尚未核对版本 / 文件 / 许可证。
- `source_checked`：已检查源文件、版本、许可证和依赖。
- `adapted`：已适配到本项目并记录差异。
- `validated`：本仓测试通过；硬件相关内容需附真机环境和证据。

每项实际迁移必须登记上游 Commit、文件路径、许可证、目标路径、改动和测试结果。
