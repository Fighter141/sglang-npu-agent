---
name: sglang-benchmark
description: 对 SGLang Ascend NPU 服务执行可复现性能测试、并发扫描、A/B 对比和回归验证。适用于建立 Baseline、评估优化收益或生成测试报告。
---

# SGLang NPU Benchmark

## 目标

建立可复现、可审计的服务级性能测量流程。Benchmark 负责测量和报告，不负责凭空推断优化根因。

## 输入契约

- 模型与权重 Revision、Tokenizer、dtype / 量化；
- SGLang 与 Ascend 后端 Commit、软件栈和硬件拓扑；
- 服务启动命令及生效配置；
- Workload / Trace、输入输出长度、请求速率、并发；
- Warmup 数、测量请求数、重复轮数；
- 指标定义、SLA 和超时策略。

## 执行步骤

1. 检查环境、设备空闲状态、服务健康和版本信息。
2. 固定 Workload 文件及其校验和；记录请求长度分布，而不只记录平均值。
3. 启动服务并执行正确性 Smoke Test。
4. 预热到稳定状态；预热请求不纳入正式统计。
5. 按预先声明的并发 / 请求速率矩阵执行测量；每个点重复多轮。
6. 记录 TTFT、TPOT、吞吐、请求成功率、超时、显存峰值和资源利用率；说明分位数与聚合口径。
7. 保存原始逐请求结果、服务日志、启动参数、环境快照和结果摘要。
8. A/B 比较时确保模型、Workload、硬件、软件环境和 SLA 一致；不同版本允许独立调参，但需记录差异。
9. 做回归判定时使用预先定义的阈值和波动容忍度，不事后挑选有利指标。
10. 生成机器可读结果和人类可读报告。

## 质量门禁

- Workload 和配置可追溯；
- Warmup 与测量阶段分离；
- 有重复测量及方差 / 分位数；
- 失败、超时和错误请求没有被静默丢弃；
- Profiling 数据不混入正式性能验收；
- A/B 比较的环境和口径明确。

## 来源

- SGLang 官方 Benchmark 工具与文档：https://github.com/sgl-project/sglang/tree/main/benchmark
- SGLang Ascend 部署与性能文档：https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus
- CANN Bench：算子测试和基准管理参考：https://gitcode.com/cann/cann-bench

## 输出

Benchmark Manifest、逐请求原始数据、汇总指标、A/B 对比、回归判定和复现实验命令。
