# Profiling 与性能工具知识

本分类明确区分工具职责，避免重复实现和把采集工具、解析器、Agent 工作流混为一谈。

## 工具职责

| 工具 / 项目 | 主要职责 | 在本项目中的定位 |
|---|---|---|
| msprof | 昇腾性能数据采集 | 采集底座，保留原始输出 |
| MindIE Agent Profiler | 采集任务组织、Trace 处理 / 分析工作流（以实际仓库能力为准） | 可复用组件候选，需核查依赖与格式 |
| msit | 昇腾工具集入口，包含 Profile 等组件 | 作为工具入口和集成参考，不整体复制 |
| msmonitor | 设备 / 系统监控 | 采集任务前后资源状态 |
| SGLang Ascend Profiling 文档 | SGLang 场景下的采集和分析说明 | 框架侧场景指南 |

## 知识条目

- [统一 Profiling 工作流](unified-profiling-workflow.md)
- [msprof 采集职责](msprof-collection.md)
- [MindIE Profiler 集成评估](mindie-profiler-integration.md)
- [msit 工具集成评估](msit-integration.md)
- [资源监控与 Trace 关联](resource-monitoring-correlation.md)

## 统一数据链

任务 / Run ID → 环境与拓扑快照 → msprof 采集 → 原始 Trace → 解析与规范化 → Host / Device 时间线 → 算子 / 通信 / HBM 归因 → 与服务日志和 Benchmark 关联 → 跨轮次比较。

采集与分析必须保留原始文件；分析结果不能替代原始 Trace。
