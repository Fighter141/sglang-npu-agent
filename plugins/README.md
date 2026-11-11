# Plugin / Workflow 目录

Plugin / Workflow 是面向用户任务的入口，负责识别意图、调用 Skills / Services、执行阶段门禁并组织最终产物。

首批规划的端到端工作流：
- model-bringup：模型适配与正确性验证。
- serving-deployment：配置检查、服务启动和 Smoke Test。
- performance-optimization：基线、诊断、候选优化、验证和实验归档。
- incident-debugging：故障复现、日志采集、定位、修复和回归。
- release-regression：上游同步、兼容性和性能回归。

**迁移来源：** Plugin / Agent / Skill 的组织模型参考 CANNBot 与 CANNBot Skills；知识工作流参考 CANNBot Knowledge。所有流程将围绕 SGLang NPU 重新定义，不迁移其他推理框架专属 Plugin 或 Workflow。
