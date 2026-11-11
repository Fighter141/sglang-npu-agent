---
id: sglang-ascend-version-inventory
title: SGLang Ascend 软件栈版本盘点
category: software
evidence: upstream_documented
status: initial_reference
last_verified: 2026-11-11
sources:
  - https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus
  - https://github.com/Ascend/pytorch
  - https://www.hiascend.com/document
---

# SGLang Ascend 软件栈版本盘点

## 目的

建立一份针对每次部署和实验的版本快照，避免将不同分支、不同 CANN / torch_npu 组合的结果混为一谈。

## 必须记录的组件

| 组件 | 记录内容 |
|---|---|
| SGLang | Git URL、Commit、分支、未提交 Patch |
| Ascend 后端 | 集成仓库 / 子模块 / Patch 来源及 Commit；以当前实际代码布局为准 |
| CANN | Toolkit 版本、安装路径、社区版 / 商用版 |
| Driver / Firmware | 完整版本和设备型号 |
| PyTorch | 版本、构建来源 |
| torch_npu | 版本、Commit 或 wheel 版本 |
| Python | 主次版本及虚拟环境 |
| 算子 / DSL | Triton-Ascend、AscendC 工具链和相关库版本 |
| 容器 | 镜像标签和 Digest |

## 版本核验流程

1. 在目标环境读取包元数据和官方版本信息。
2. 读取 SGLang 当前分支的 Ascend 安装文档和依赖约束。
3. 核对 CANN / Driver / Firmware 与 torch_npu 的官方兼容矩阵。
4. 确认模型部署指南所要求的最低版本和已知限制。
5. 保存版本输出、安装命令和容器 Digest。
6. 升级任一关键组件后，重新运行正确性 Smoke Test 和代表性 Benchmark。

## 不应推断

- 不要仅因某个 SGLang Commit 可以安装，就推断其与任意 CANN 版本兼容。
- 不要用 CUDA 环境的 PyTorch 版本推断 torch_npu wheel 兼容性。
- 不要把不同发布日期的文档默认值拼接成一套配置。

## 当前状态

本条目提供版本核查流程，不提供未经逐项核对的固定兼容矩阵。实际矩阵应从官方发布文档提取并注明版本区间。
