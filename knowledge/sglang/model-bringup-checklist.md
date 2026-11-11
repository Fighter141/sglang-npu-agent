---
id: sglang-model-bringup-checklist
title: SGLang Ascend 模型 Bring-up 检查清单
category: workflow
evidence: upstream_documented
status: initial_reference
last_verified: 2026-11-11
sources:
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/development/support_new_models.mdx
  - https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus/model-deployment
---

# SGLang Ascend 模型 Bring-up 检查清单

## 阶段 1：模型结构与权重

- 记录模型仓库、Revision、config、architectures、Tokenizer 和权重格式。
- 检查 Dense / MoE、Attention 类型、MLA、多模态组件、量化格式。
- 确认权重 shard、键名、scale / zero-point 等元数据。

## 阶段 2：SGLang 支持情况

- 检查目标 SGLang Commit 的模型注册和已有模型实现。
- 检查 Ascend 支持模型清单和模型部署教程。
- 检查相关测试、已知限制和未合入 PR。
- 明确是模型代码缺失，还是底层算子 / Runtime 不支持。

## 阶段 3：Ascend 执行路径

- 沿模型 forward 追踪 Attention、MoE、Norm、RoPE、量化和采样调用。
- 对每个关键算子确认 NPU 实现、dtype、shape、layout 和边界条件。
- 不以 CUDA kernel 存在推断 NPU 后端可用。

## 阶段 4：正确性

- 建立最小输入和参考实现。
- 比较 logits / token、关键中间 Tensor 和误差统计。
- 对 MoE 路由、量化 scale、RoPE、KV Cache 等结构性风险单独检查。
- 必要时使用 msprobe 进行数据采集和精度比对。

## 阶段 5：服务与性能

- 启动服务并执行健康检查和短请求。
- 验证目标 dtype / 量化 / 并行方式。
- 固定真实 Workload 后建立非 Profiling Baseline。
- Profiling 仅用于定位，不能替代性能验收。

## 交付

模型支持差距、适配 Commit、测试命令、精度结果、部署配置、性能数据、限制和回滚方式。
