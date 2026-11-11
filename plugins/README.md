# Plugin / Workflow 目录

Plugin / Workflow 是面向用户任务的入口，负责识别意图、调用 Skills / Services、执行阶段门禁并组织最终产物。

建议先建设以下端到端工作流：
- `model-bringup`：模型适配与正确性验证。
- `serving-deployment`：配置检查、服务启动和 Smoke Test。
- `performance-optimization`：基线、诊断、候选优化、验证和实验归档。
- `incident-debugging`：故障复现、日志采集、定位、修复和回归。
- `release-regression`：上游同步、兼容性和性能回归。

**迁移来源：** Plugin / Agent / Skill 的组织模型参考 [CANNBot](https://gitcode.com/cann/cannbot) 和 [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)；实验阶段和证据闭环参考 [xLLM Workflow](https://github.com/xLLM-AI/xllm-workflow)。以上均为设计参考，尚未迁移实现。
