---
id: unified-profiling-workflow
title: SGLang NPU 统一 Profiling 采集与分析工作流
category: profiling
evidence: upstream_documented
status: design_reference
last_verified: 2026-11-11
sources:
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/profiling.mdx
  - https://github.com/Ascend/msit
  - https://github.com/Ascend/msprof
  - https://github.com/mindie-agent/profiler
  - https://github.com/Ascend/msmonitor
---

# SGLang NPU 统一 Profiling 采集与分析工作流

## 目标

统一不同工具的入口和结果模型，但不重写 msprof、msit 或 MindIE Profiler 已有能力。

## 工作流

1. 创建 Profiling Run，分配唯一 Run ID。
2. 记录 SGLang / Ascend 后端 Commit、CANN / Driver / Firmware / torch_npu、设备拓扑、模型和 Workload。
3. 记录非 Profiling Benchmark 基线，作为端到端性能参考。
4. 依据诊断目标选择 msprof 采集配置；通过统一入口调用官方工具。
5. 保存原始输出、采集命令、工具版本、采集范围和失败状态。
6. 运行解析器，将工具原始数据转换为统一事件 / 指标 Schema；原始字段必须可追溯。
7. 生成 Host / Device 时间线，关联 SGLang 请求阶段、Rank、Stream、算子和通信事件。
8. 归因 HBM / 内存、算子、通信、同步等待、Host 调度等候选瓶颈。
9. 关联 msmonitor 资源指标和 Benchmark Run ID；没有可靠时间戳 / Rank 对齐时不得强行关联。
10. 对比多次 Profiling Run，输出差异和证据；最终优化收益仍用非 Profiling Benchmark 复测。

## 建议统一数据模型

- `run_id`：实验唯一标识。
- `source_commit`：SGLang 与后端 Commit。
- `environment`：CANN、Driver、Firmware、PyTorch、torch_npu、工具版本。
- `topology`：节点、设备、Die、Rank、互联信息。
- `workload_id`：输入输出长度、请求速率、并发和 Trace 校验和。
- `collection`：采集工具、参数、开始 / 结束时间、原始目录。
- `events`：Host / Device 时间戳、Rank、Stream、事件类别、算子名、耗时和源文件引用。
- `metrics`：HBM、通信字节数、算子耗时、利用率等及其单位 / 采样口径。
- `analysis`：瓶颈假设、证据、置信度和待验证事项。

## 当前实现状态

这是统一工作流设计，不表示仓库已实现统一采集器、Trace Parser 或可视化时间线。下一步需分别核查 msprof CLI、MindIE Profiler API / CLI、msit Profile 子命令和 msmonitor 输出 Schema，再定义 Adapter。
