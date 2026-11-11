---
name: ascend-operator-development
description: 为 SGLang Ascend NPU 开发、迁移、调试和优化 AscendC / Triton-Ascend 算子。适用于识别算子瓶颈、实现新 Kernel、验证精度和测量算子性能。
---

# SGLang Ascend 算子开发与优化

## 范围

只处理 SGLang Ascend 后端实际调用的算子路径。根据目标算子选择 AscendC、Triton-Ascend 或项目实际使用的 DSL；不为引入 DSL 而引入 DSL。

## 输入

算子调用点、输入输出 Shape / Stride / dtype、布局、数值语义、目标芯片、CANN / torch_npu / Triton-Ascend 版本、性能基线和正确性参考。

## 流程

1. 从 SGLang 调用栈定位算子及其上下游，确认是否已有可复用实现。
2. 明确数学定义、输入输出契约、Shape 范围、数据布局、dtype、累加精度和边界行为。
3. 建立独立正确性参考和基线测试；记录算子耗时、调用频率、端到端占比和显存影响。
4. 评估 AscendC / Triton-Ascend / 现有库实现的适用性，核查目标 CANN 与编译器版本支持。
5. 设计 Kernel：数据切分、并行映射、片上 Buffer、访存合并、流水、同步和尾块处理。
6. 先完成最小实现与正确性测试，再逐步优化；每次只调整一个主要因素。
7. 使用目标设备 Profiling 分析访存、计算、同步和资源利用率。
8. 在相同 Shape / dtype / 数据分布下做多轮非 Profiling 性能测量。
9. 评估算子级收益能否传递到 SGLang 端到端指标；必要时做融合或调用路径调整。
10. 补充单测、边界测试、精度容差、性能基准和目标设备限制说明。

## 必查项

- 非连续 Tensor、Stride、对齐和尾块；
- NaN / Inf、极值、空输入和边界 Shape；
- dtype 转换、累加精度和误差传播；
- 多流 / 异步执行及同步语义；
- 临时 Buffer 生命周期和越界风险；
- 编译缓存、动态 Shape 和目标芯片兼容；
- 算子耗时占端到端比例，避免优化非关键路径。

## 来源

- [CANNBot DSL](https://gitcode.com/cann/cannbot-dsl)：DSL / 算子生成与开发流程候选参考。
- [CANN Bench](https://gitcode.com/cann/cann-bench)：算子测试与基准管理参考。
- [CANN 官方文档](https://www.hiascend.com/document)：AscendC、Triton-Ascend、编译器和工具链。
- [SGLang Ascend 后端](https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/hardware_backend/npu)：实际算子调用与适配位置。

## 输出

算子契约、实现路径、正确性与精度报告、性能基准、Profiling 证据、端到端影响和已知限制。
