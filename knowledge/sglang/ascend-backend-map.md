---
id: sglang-ascend-backend-map
title: SGLang Ascend 后端研发入口
category: sglang
evidence: upstream_documented
status: source_index
last_verified: 2026-11-11
sources:
  - https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/hardware_backend/npu
  - https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus
---

# SGLang Ascend 后端研发入口

## 定位

本条目是代码导航索引，不复制 SGLang 上游实现。研发时应在目标 SGLang Commit 中检索调用链，并以实际目录为准。

## 建议按问题分层

| 问题 | 优先检查位置 / 入口 |
|---|---|
| 模型是否支持 | Ascend 支持模型清单、模型注册、模型实现和对应测试 |
| 服务启动 | Ascend Quick Start、启动参数定义、Runtime 初始化日志 |
| Attention | NPU Attention Backend、算子实现和模型调用点 |
| MoE | SGLang MoE Runner、NPU MoE routing、token dispatcher、专家计算 |
| Graph | NPU Graph / ACL Graph 相关实现、捕获与回放测试 |
| 通信 | HCCL 初始化、EP Dispatch / Combine、Rank 映射 |
| Profiling | Ascend Profiling 指南、msprof 输出和 SGLang 请求时间线 |
| 精度 | 模型适配指南、参考实现、逐层 / 算子对比 |

## 上游文档入口

- Ascend 平台文档：https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus
- 模型适配指南：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/development/support_new_models.mdx
- 参数调优：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx
- Profiling：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/profiling.mdx

## 约束

不得把上游目录路径永久视为稳定 API；代码迁移或升级时需重新确认目标 Commit 中的路径和职责。
