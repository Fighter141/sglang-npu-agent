---
id: mindie-profiler-integration
title: MindIE Agent Profiler 集成评估
category: profiling
evidence: upstream_documented
status: candidate_integration
last_verified: 2026-11-11
sources:
  - https://github.com/mindie-agent/profiler
  - https://github.com/mindie-agent/mindie-agent
---

# MindIE Agent Profiler 集成评估

## 评估目标

判断 MindIE Agent Profiler 哪些模块能作为独立解析 / 分析组件复用，避免重复开发 Trace 解析器和性能报告逻辑。

## 核查清单

1. 仓库的包结构、入口命令、公开 API 和服务依赖。
2. 输入格式：msprof 原始目录、数据库、CSV、JSON 或其他产物。
3. 输出格式：算子表、时间线、通信分析、内存指标和报告。
4. 是否依赖 MindIE Agent 专属任务对象、数据库或 MCP Runtime。
5. 是否支持多 Rank / 多机和不同 CANN 版本。
6. 许可证、依赖和版本发布策略。
7. 能否以 Python 库 / CLI 独立调用。

## 推荐策略

- 若解析器可独立运行：优先作为外部工具依赖或薄适配器调用。
- 若与 MindIE Runtime 强耦合：只借鉴数据模型和分析算法，独立实现 SGLang 适配层。
- 若其功能与 msit / msprof 重复：指定唯一主实现，其他仅保留兼容入口。

## 状态

候选集成。尚未逐文件核查其 API / CLI、许可证和依赖，因此不宣称已完成集成。
