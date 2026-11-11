# Skills 能力目录

Skill 是可复用的操作规程和决策流程。每个 Skill 应包含简洁的 `SKILL.md`，并按需提供 `references/`、`scripts/` 和测试。

| Skill | 目标 | 主要迁移参考 | 状态 |
|---|---|---|---|
| `sglang-model-bringup` | 模型结构、权重、算子和精度适配 | CANNBot Skills 模型迁移类；SGLang 官方模型接入文档；VAWS 工作流组织 | 规划中 |
| `sglang-serving-config` | 配置生成、参数校验和生效配置采集 | VAWS Serving；MindIE Agent remote-dev / coordinator；SGLang Ascend 文档 | 规划中 |
| `sglang-performance-optimization` | 多轮端到端性能优化闭环 | xLLM Workflow SOTA Loop；CANNBot Skills 推理优化类 | 规划中 |
| `sglang-benchmark` | Workload、预热、重复测量、公平性与报告 | xLLM Workflow Benchmark / Eval Runner；VAWS Benchmark | 规划中 |
| `ascend-profiling` | msprof 采集、解析和瓶颈归因 | MindIE Agent Profiler；VAWS Profiling Collection / Analysis | 规划中 |
| `sglang-incident-triage` | Runtime、HCCL、Graph、OOM、精度故障定位 | MindIE Agent Debugger；xLLM Incident Triage；CANNBot Sentry | 规划中 |
| `sglang-code-review` | 适配正确性、兼容性和性能回归审查 | CANNBot Skills Review 类；xLLM NPU Code Review | 规划中 |
| `sglang-moe-optimization` | EP、通信后端、负载均衡和融合优化 | SGLang Ascend 实现；CANNBot 推理优化知识；本项目实测 | 规划中 |
| `sglang-graph-mtp-optimization` | Graph、FIA、MTP 组合和收益评估 | SGLang Ascend 文档 / 源码；CANNBot 知识；本项目实测 | 规划中 |

不要为了填满目录而创建空 Skill。只有明确输入输出、适用范围、执行步骤和验证方式后才新增。
