---
name: sglang-performance-optimization
description: 对 SGLang Ascend NPU 推理服务开展证据驱动的端到端性能优化。适用于吞吐、TTFT、TPOT、显存、通信或并发不达标，需要定位瓶颈和验证优化收益的任务。
---

# SGLang NPU 性能优化闭环

## 强制原则

没有可复现 Baseline，不开始性能改动。Profiler 用于解释瓶颈；非 Profiling Benchmark 用于确认收益。不得将单次测量、不同 Workload 或不同环境的数据直接比较。

## 输入

目标 SLA、模型与 Revision、SGLang / Ascend 后端 Commit、硬件拓扑、软件栈、Workload / Trace、当前启动配置和已有测量数据。

## 流程

1. **定义目标**：明确优化的是 TTFT、TPOT、吞吐、并发、显存还是成本；固定验收条件。
2. **审计 Baseline**：确认模型、Tokenizer、dtype、量化、输入输出长度、请求分布、并发、采样参数、软件版本和设备一致。
3. **重复测量**：完成预热和多轮非 Profiling 测试，保存原始数据、统计口径和异常请求。
4. **识别瓶颈层级**：架构 / 并行策略、服务流水线、通信、算子、内存访问；先判断端到端瓶颈，再决定是否进入 kernel 级。
5. **采集诊断证据**：根据假设采集 msprof / torch profiler、HBM、通信、Host / Device 时间线；Profiler 结果不替代性能数据。
6. **提出候选**：每个候选写明根因假设、预期影响指标、风险、依赖条件和验证方法。
7. **单变量实验**：一次只改变一个主要因素；组合优化需做消融，识别冲突和收益归属。
8. **正确性门禁**：检查输出一致性、精度、稳定性和长时间运行。
9. **非 Profiling A/B**：相同 Workload 下比较 Baseline 与 Candidate，报告分布、波动和回退。
10. **沉淀经验**：保留失败尝试、适用条件、软件版本和硬件证据；经 Review 后才晋升为知识卡。

## 优化方向检查清单

- 并行策略与负载均衡：TP / DP / EP / PP / DCP；
- MoE Dispatch / Combine、通信后端与专家负载；
- Attention Backend、FIA、KV Cache；
- Graph 捕获、Replay 和执行开销；
- MTP / Speculative Decoding 的接受率与验证开销；
- PD 分离、KV 传输与 Prefill / Decode 干扰；
- HBM 带宽、显存容量、算子融合和数据布局。

不得默认某项优化一定有效；必须按当前 SGLang Ascend 版本和目标硬件确认支持情况。

## 输出

Baseline 报告、瓶颈证据、候选实验矩阵、代码差异、正确性结果、非 Profiling A/B、消融报告、回退建议和知识候选卡。

## 来源

- SGLang Ascend 参数调优：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx
- SGLang Ascend Profiling：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/profiling.mdx
- CANNBot Skills：昇腾推理优化流程参考：https://gitcode.com/cann/cannbot-skills
- CANN / HCCL 官方文档及目标版本实现：以实际使用版本为准。

## 不允许

不允许仅凭 profiler 截图宣称加速；不允许混用不同模型 / Trace / 软件栈；不允许删除负面实验记录。
