---
id: profiling-resource-monitoring-correlation
title: 资源监控与 Profiling Trace 关联
category: profiling
evidence: upstream_documented
status: design_reference
last_verified: 2026-11-11
sources:
  - https://github.com/Ascend/msmonitor
  - https://github.com/Ascend/msit
  - https://github.com/Ascend/msprof
---

# 资源监控与 Profiling Trace 关联

## 目标

将设备资源状态与 SGLang 请求 / Profiling 时间线放到同一实验上下文中，辅助解释 HBM、利用率、功耗、温度和通信表现。

## 需要采集的资源指标

以目标 msmonitor / 驱动版本实际支持为准，候选包括：
- NPU 利用率与显存 / HBM 占用；
- 功耗、温度、频率和设备健康；
- 设备级和进程级资源占用；
- 采样时间戳、设备 ID 和 Rank 映射。

## 时间关联

1. 所有采集器使用统一时钟基准，记录时区和时间精度。
2. 每个 Run 保存开始 / 结束时间和节点时钟信息。
3. 按节点、设备、Rank、PID 和时间窗关联资源指标与 Trace。
4. 记录采样周期；低频监控数据不得解释为微秒级算子行为。
5. 对齐失败、时钟偏差或缺失指标必须显式标注。

## 重要边界

HBM 峰值、带宽和瞬时占用是不同指标；不得用监控采样值替代 msprof 硬件计数器。通信归因必须结合 HCCL / NPU 时间线，不能只看设备利用率。
