---
name: sglang-code-review
description: 审查 SGLang Ascend NPU 相关代码、模型适配、算子和性能优化 PR。用于检查正确性、接口兼容、硬件约束、测试覆盖和性能回归风险。
---

# SGLang NPU 代码审查

## 审查范围

只依据目标分支和实际 SGLang / Ascend 后端代码审查。不得把其他推理框架的目录结构、接口或规则套用到 SGLang。

## 流程

1. 获取 PR diff、基准 Commit、目标 Commit、关联 Issue 和设计说明。
2. 阅读项目 AGENTS / CONTRIBUTING、相邻实现、调用方、测试和相关文档。
3. 判断变更层级：模型注册 / 权重、Runtime、Scheduler、Attention、MoE、通信、Graph、量化、算子或构建。
4. 检查接口契约、dtype / shape / layout、设备分支、异常处理、资源生命周期和多卡行为。
5. 检查 Ascend 特有路径：设备检测、torch_npu / CANN API、算子可用性、Graph 捕获约束、HCCL / Rank 语义。
6. 检查功能组合与回退路径；确认未支持组合有明确报错，而非静默走错分支。
7. 检查测试是否覆盖目标芯片、模型、dtype、输入边界、单卡 / 多卡和失败路径。
8. 对性能 PR 检查 Baseline、Workload、环境一致性、非 Profiling 数据、消融和原始结果。
9. 给出按严重程度排序的 Findings，每项包含文件 / 行、触发条件、影响和建议。
10. 明确未验证范围；没有证据时不得声称通过。

## 审查检查表

- 是否存在未使用或错误的设备分支？
- 是否错误假设 CUDA / CPU 语义等价于 NPU？
- 是否改变数值精度、累加顺序或输出语义？
- 是否可能造成多 Rank 死锁、资源泄漏或重复初始化？
- 是否破坏 Graph capture / replay 或异步执行约束？
- 是否新增参数却没有文档、默认值和兼容性测试？
- 性能结论是否能从原始数据复现？

## 来源

- SGLang 贡献指南：https://github.com/sgl-project/sglang/blob/main/CONTRIBUTING.md
- SGLang Ascend 开发文档：https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus/development
- SGLang CI / 测试代码：https://github.com/sgl-project/sglang/tree/main/test
- CANNBot Skills：代码 Review 流程参考：https://gitcode.com/cann/cannbot-skills

## 输出

PR 摘要、Findings（严重程度 / 文件 / 行 / 依据）、测试缺口、性能风险和最终审查结论。
