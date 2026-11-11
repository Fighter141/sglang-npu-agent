---
id: ascend-inference-accuracy-debugging
title: 昇腾大模型推理精度定位流程
category: accuracy
evidence: upstream_documented
status: source_index
last_verified: 2026-11-11
sources:
  - https://github.com/Ascend/msprobe/blob/master/docs/zh/best_practices/infer_debug_guide.md
  - https://github.com/Ascend/msprobe
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/development/support_new_models.mdx
---

# 昇腾大模型推理精度定位流程

## 问题分类

- 模型结构 / 权重问题：权重映射、配置、Tokenizer、模型实现不一致。
- 参数配置问题：dtype、量化参数、并行布局、采样配置不一致。
- 算子数值问题：计算精度、累加顺序、近似实现或边界行为。
- Runtime / 通信问题：多 Rank 数据、同步、缓存或执行路径异常。

## 定位流程

1. 固定模型 Revision、权重、Tokenizer、dtype、量化方式和输入样例。
2. 建立可重复的异常请求，保存输入和完整输出。
3. 与可信参考实现对比；先做端到端判断，再缩小到模块和算子。
4. 根据 msprobe 目标版本文档选择推理数据采集 / Tensor 对比能力。
5. 比较关键层输入输出、算子输出、NaN / Inf、最大绝对误差、相对误差和误差分布。
6. 沿第一个出现显著偏差的位置向上游定位。
7. 对量化、MoE 路由、RoPE、Norm、Attention、KV Cache 等高风险路径分别检查。
8. 修复后运行最小复现、模型正确性测试和目标服务回归。

## 解释结果时注意

- GPU 与 NPU 浮点计算存在合理数值差异，不能要求逐 bit 一致。
- 必须根据模型、dtype 和任务选择合理容差 / 评估指标。
- 第一个出现偏差的中间 Tensor 通常比最终文本差异更有定位价值。
- 训练场景的 msprobe 流程不自动适用于推理服务；本卡只覆盖推理诊断。

## 来源说明

msprobe 官方指南是流程依据；具体 CLI 参数、采集能力和支持的 SGLang 版本应以目标安装版本文档为准。
