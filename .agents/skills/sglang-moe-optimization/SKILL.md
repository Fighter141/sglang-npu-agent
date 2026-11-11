---
name: sglang-moe-optimization
description: 分析和优化 SGLang Ascend NPU 上的 MoE 推理路径，包括 EP、Dispatch/Combine、通信后端、专家负载均衡和融合。适用于 MoE 性能低、Rank 偏斜或通信瓶颈。
---

# SGLang Ascend MoE / EP 优化

## 目标

针对 SGLang 实际 MoE 路径分析端到端瓶颈，选择并验证通信和计算优化。不得把 vLLM / xLLM 的 MoE Runner、配置或工作流迁入。

## 输入

模型 MoE 结构（专家数、Top-K、Shared Experts、隐藏维度）、硬件拓扑、卡 / Die / Rank 数、dtype / 量化、SGLang / Ascend 后端 Commit、Workload、当前 MoE 配置和基线。

## 流程

1. 读取模型配置和实际 MoE 层实现，确认 Router、Top-K、专家布局、Shared Expert 和权重格式。
2. 从 SGLang Ascend 代码追踪 Dispatch → Expert GEMM / FFN → Combine 的真实调用链。
3. 记录 EP / TP / DP 等并行关系、Rank 映射、通信域、Buffer 和同步语义。
4. 建立 Baseline：记录吞吐、TTFT / TPOT、各 Rank token 分布、Dispatch / Combine 时间、显存和通信指标。
5. 判断瓶颈是通信量、通信启动、专家负载偏斜、GEMM 效率、同步、Buffer 或 Host 调度。
6. 列出当前版本真实可用的后端和模式；对 FuseEP、DeepEP、MegaMoE、EPLB 等候选逐项核对 SGLang Ascend 支持和互斥条件，不假设都能同时启用。
7. 设计小规模对照实验：固定模型、Workload、卡数和软件栈，每次只改变一个后端 / 模式 / 均衡策略。
8. 验证多 Rank 正确性、无死锁、负载分布、端到端收益和显存变化。
9. 对组合优化做消融；若端到端收益不稳定或回退，保留负面结果。
10. 将可复现配置、兼容边界和测量证据沉淀为知识卡。

## 重点观测

- 每层 / 每 Rank token 数、专家命中分布和最大 / 平均负载；
- Dispatch / Combine 通信时间与字节数；
- Expert GEMM 时间、算子形状和利用率；
- Rank 间等待、尾部延迟和负载偏斜；
- HBM 峰值、Buffer 使用和端到端 TTFT / TPOT / 吞吐。

## 来源

- SGLang 主仓 MoE 实现：https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/layers/moe
- SGLang Ascend 后端代码与文档：https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus
- CANN / HCCL 官方文档：https://www.hiascend.com/document
- CANNBot Skills：昇腾推理优化流程参考：https://gitcode.com/cann/cannbot-skills

## 验收

必须有相同 Workload 的非 Profiling Baseline / Candidate 数据、正确性结果、通信和负载证据、配置快照及软件版本。只提升 kernel 时间但端到端无收益，不算优化成功。
