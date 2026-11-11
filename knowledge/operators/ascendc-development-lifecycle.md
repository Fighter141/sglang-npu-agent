---
id: ascendc-operator-development-lifecycle
title: AscendC 算子七阶段研发流程
category: operators
evidence: upstream_documented
status: source_index
last_verified: 2026-11-11
sources:
  - https://github.com/Ascend/agent-skills/blob/master/skills/ascendc-operator-dev/SKILL.md
  - https://github.com/Ascend/agent-skills
  - https://gitcode.com/cann/cannbot-dsl
---

# AscendC 算子七阶段研发流程

Ascend 官方 Agent Skills 中的 `ascendc-operator-dev` 采用阶段化算子开发编排。对本项目建议保留通用门禁，并根据 SGLang 实际算子路径适配。

## 阶段

1. 需求与环境确认：算子语义、Shape、dtype、目标芯片、CANN 和编译工具链。
2. 算子设计：数学定义、数据布局、Tiling、片上 Buffer 和并行策略。
3. 测试用例：常规 Shape、边界 Shape、dtype、异常值和参考实现。
4. 代码实现与编译：AscendC / Triton-Ascend 或实际选定 DSL。
5. 接口与框架集成：注册、构建、PyTorch / torch_npu 调用和 SGLang 接入点。
6. 精度评估：全量用例、误差分析和失败样例定位。
7. 性能评测：预热、重复测量、Profiling 诊断和端到端影响。

## 阶段门禁

上一阶段产物经检查后才进入下一阶段。设计文档和测试用例应先于 Kernel 编码；精度通过后再做性能验收。

## 适用边界

Ascend Agent Skills 中部分流程面向 Catlass 或特定 ascend-kernel 工程。不得原样照搬其目录、构建命令和依赖；本项目只借鉴阶段划分、检查点和通用测试方法。
