---
name: sglang-graph-mtp-optimization
description: 分析 SGLang Ascend NPU 上 Graph、FIA、MTP / Speculative Decoding 等功能的兼容性与性能收益。适用于图捕获失败、功能冲突、Decode 性能优化和投机解码负优化分析。
---

# SGLang Ascend Graph / FIA / MTP 优化

## 原则

功能是否支持、是否互斥、默认值和适用模型必须以当前 SGLang Ascend 版本源码与文档为准。不得根据 GPU 行为推断 NPU 行为，也不得假设多个优化开关可直接叠加。

## 输入

模型 / Draft 模型及 Revision、SGLang / Ascend 后端 Commit、设备拓扑、CANN / torch_npu 版本、Graph / FIA / MTP / Prefix Cache 配置、Workload 和 Baseline。

## 流程

1. 明确目标是 Graph 稳定性、Attention 性能、Decode 吞吐、TPOT、MTP 接受率还是端到端 SLA。
2. 从当前版本 CLI 参数、Ascend 文档和源码确认 Graph、FIA、MTP、Prefix Cache 的实现入口、支持条件和限制。
3. 建立功能兼容矩阵：模型、dtype、并行策略、Attention Backend、Graph 模式、Prefix Cache、Speculative 算法。
4. 先建立不启用待测功能的正确性与性能 Baseline。
5. 每次仅启用一个功能，验证启动、Graph capture / replay、请求正确性和稳定性。
6. 对 MTP 记录 Draft / Target 模型配套关系、Draft 加载开销、接受率、验证开销、额外显存和端到端收益。
7. 检查 Prefix Cache、Chunked Prefill、并发、长输入等真实 Workload 下是否发生冲突或负优化。
8. 对 Graph / FIA 组合分别采集诊断 Trace，但使用非 Profiling 数据确认最终收益。
9. 对每个候选做消融和回退测试，记录不兼容条件和失败日志。
10. 输出按 Workload 分场景的配置建议，不给出脱离条件的“万能参数”。

## 重点判据

- Graph：捕获成功率、Replay 稳定性、图外回退和实际端到端收益。
- FIA / Attention：支持模型与输入形状、KV Cache 行为、精度和延迟。
- MTP：接受率、Draft 额外成本、Target 验证成本、显存和端到端吞吐 / TPOT。
- Prefix Cache：命中率、缓存占用、请求前缀分布和与其他功能的兼容性。

## 来源

- SGLang Ascend 参数与功能兼容性：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx
- SGLang Ascend FAQ：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/faq.mdx
- SGLang Ascend Attention 后端实现：https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/hardware_backend/npu/attention
- SGLang Speculative Decoding 文档与实现：https://github.com/sgl-project/sglang/tree/main/docs

## 输出

功能兼容矩阵、逐项配置、正确性结果、接受率与性能数据、消融报告和回退建议。
