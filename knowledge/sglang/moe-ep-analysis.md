---
id: sglang-moe-ep-analysis
title: SGLang Ascend MoE / EP 调用链分析
category: sglang
evidence: upstream_documented
status: source_index
last_verified: 2026-11-11
sources:
  - https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/layers/moe
  - https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/hardware_backend/npu
  - https://www.hiascend.com/document
---

# SGLang Ascend MoE / EP 调用链分析

## 代码导航

当前上游已能检索到以下 Ascend MoE 相关实现入口（路径会随 Commit 变化）：

- `python/sglang/srt/layers/moe/moe_runner/ascend.py`
- `python/sglang/srt/layers/moe/token_dispatcher/ascend_ops.py`
- `python/sglang/srt/hardware_backend/npu/moe/routing.py`
- `python/sglang/srt/hardware_backend/npu/moe/activation.py`
- `python/sglang/srt/hardware_backend/npu/quantization/moe_utils.py`

## 分析步骤

1. 从模型 MoE 层 forward 追踪到 Runner。
2. 确认 Router / Top-K、专家权重布局、Shared Experts 和量化方法。
3. 追踪 Dispatch、Expert GEMM / FFN、Combine。
4. 记录 EP / TP / DP 关系、Rank 映射、通信域和 Buffer。
5. 分别测量通信、专家计算、等待和端到端时延。
6. 对 FuseEP、DeepEP、MegaMoE、EPLB 等候选只在当前 SGLang Ascend 代码明确支持时测试，并检查互斥关系。

## 关键指标

每 Rank token 数、专家负载最大 / 平均比、Dispatch / Combine 时间、通信字节数、专家 GEMM 时间、尾部等待、HBM 峰值、TTFT / TPOT / 吞吐。

## 限制

本卡是源码导航和分析方法，不代表列出的所有通信后端或模式都能在所有设备 / 版本组合中使用。每次实验必须记录实际 Commit 和支持矩阵。
