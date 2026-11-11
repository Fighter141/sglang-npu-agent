# Skills 能力目录

Skill 是可复用的操作规程和决策流程。每个 Skill 应包含简洁的 SKILL.md，并按需提供 references、scripts 和测试。

| Skill | 目标 | 主要来源 | 状态 |
|---|---|---|---|
| sglang-model-bringup | 模型结构、权重、算子和精度适配 | SGLang 官方模型接入代码 / 文档；CANNBot Skills 模型迁移类 | 规划中 |
| sglang-serving-config | SGLang 服务配置、参数校验和生效配置采集 | SGLang Ascend 文档 / 源码；CANNBot Skills | 规划中 |
| sglang-performance-optimization | 多轮端到端性能优化 | SGLang Ascend 实现；CANNBot Skills 推理优化类 | 规划中 |
| sglang-benchmark | Workload、预热、重复测量、公平性与报告 | SGLang 官方测试工具；CANN Bench 的测试方法参考 | 规划中 |
| ascend-profiling | msprof 采集、解析和瓶颈归因 | MindIE Agent Profiler；CANN 官方工具 | 规划中 |
| sglang-incident-triage | Runtime、HCCL、Graph、OOM、精度故障定位 | MindIE Agent Debugger；CANNBot Sentry | 规划中 |
| sglang-code-review | 适配正确性、兼容性和性能回归审查 | SGLang 官方贡献与 CI 规范；CANNBot Skills Review 类 | 规划中 |
| sglang-moe-optimization | EP、通信后端、负载均衡和融合优化 | SGLang Ascend 源码 / PR；CANN / HCCL 文档 | 规划中 |
| sglang-graph-mtp-optimization | Graph、FIA、MTP 组合和收益评估 | SGLang Ascend 源码 / 文档；目标硬件实测 | 规划中 |
| ascend-operator-development | AscendC / Triton-Ascend 算子开发与优化 | CANNBot DSL / Skills；CANN 官方文档 | 规划中 |

明确不建设 vLLM、vLLM-Ascend 或 xLLM 专属 Skill。
