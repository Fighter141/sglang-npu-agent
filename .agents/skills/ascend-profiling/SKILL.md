---
name: ascend-profiling
description: 为 SGLang Ascend NPU 推理服务规划、采集和分析 msprof / PyTorch Profiler 数据。适用于定位算子、通信、Host/Device、HBM 和流水线瓶颈。
---

# Ascend Profiling 采集与分析

## 原则

先提出明确瓶颈假设，再选择采集范围和指标。Profiling 可能改变执行开销，采集结果用于诊断，不作为非 Profiling 性能验收值。

## 输入

目标服务、模型、Workload、设备拓扑、SGLang / CANN / torch_npu 版本、待验证瓶颈假设和可用磁盘空间。

## 采集流程

1. 记录源码 Commit、环境版本、设备拓扑、模型与 Workload。
2. 确认服务稳定并记录无 Profiling 的性能参考值。
3. 根据目标选择 PyTorch Profiler 或 msprof，明确采集范围、持续时间和采样策略。
4. 检查采集开销、输出目录、磁盘容量和数据完整性。
5. 采集后保留原始文件，不覆盖已有 Trace；记录采集命令和工具版本。
6. 分析 Host / Device 时间线、算子耗时、通信活动、同步等待、HBM / 显存和关键阶段。
7. 将 Trace 中的事件与服务日志、请求阶段和硬件信息关联。
8. 对比不同轮次时固定分析口径，避免把采集配置差异误判为性能变化。
9. 根据证据提出根因假设，再通过独立实验验证。

## 分析报告必须回答

- 最耗时的阶段和事件是什么？
- 是计算、访存、通信、同步还是 Host 开销？
- 该事件是否位于关键路径？
- 是否与端到端指标一致？
- 哪些结论是 Trace 直接观察，哪些仍是推断？
- 下一步如何通过独立实验验证？

## 来源

- SGLang Ascend Profiling 指南：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/profiling.mdx
- MindIE Agent Profiler：https://github.com/mindie-agent/profiler
- CANN / msprof 官方工具文档：https://www.hiascend.com/document

## 输出

采集配置、工具版本、原始 Trace 路径、分析摘要、关键事件表、瓶颈假设和后续验证方案。
