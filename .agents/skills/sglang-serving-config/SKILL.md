---
name: sglang-serving-config
description: 为 SGLang Ascend NPU 服务生成、审查和验证启动配置。适用于 A3/910C 部署、TP/DP/EP 配置、Attention/Graph/FIA、KV Cache、MTP 和启动故障排查。
---

# SGLang Ascend Serving 配置

## 原则

配置必须由目标 SGLang 版本的参数定义、Ascend 后端实现和对应模型部署文档共同确认。不得把其他框架的参数名、默认值或调优建议迁入。

## 输入

模型与 Revision、设备型号及拓扑、软件版本、目标输入输出长度、并发 / SLA、dtype / 量化、部署形态（单机、多机、PD）。

## 执行流程

1. 探测设备：采集 `npu-smi info`、卡 / Die 数、可见设备、拓扑和资源占用。
2. 固定软件栈：记录 SGLang / Ascend 后端 Commit、CANN、Driver、Firmware、torch_npu、PyTorch 和镜像。
3. 核对模型：确认 Ascend 支持清单、模型专属部署指南、Attention / MoE / 量化限制。
4. 核对参数：从当前版本 CLI help、参数定义和文档确认参数名称、类型、默认值、取值范围和弃用状态。
5. 检查并行布局：依据模型结构、卡数、Die / Rank 拓扑和显存容量分析 TP / DP / EP / PP / DCP 等组合；不得只凭经验给固定值。
6. 检查功能组合：Attention Backend、Graph、FIA、MTP、Prefix Cache、KV Cache、量化和 PD 相关选项逐项核对兼容性。
7. 生成配置：输出启动命令、配置文件和逐项理由；将默认值与显式设置分开标注。
8. 启动验证：检查进程、端口、日志、设备占用、健康接口、模型加载和短请求。
9. 保存生效配置：从进程参数、服务日志或运行时接口核实实际配置，不能只保存计划配置。

## 故障定位

按环境 / 驱动 / 权限 → 模型加载 → 参数解析 → 设备初始化 → 通信初始化 → Graph / Kernel 初始化 → 请求执行的顺序定位。每次只改变少量变量，并保存前后配置。

## 验收

服务健康、目标模型输出正确、目标 Workload 可运行、资源清理明确、生效配置已归档。性能结论必须转入 Benchmark Skill，不以服务启动成功代替性能验证。

## 来源

- SGLang Ascend Quick Start：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx
- SGLang Ascend 参数调优与兼容性：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx
- SGLang Ascend 部署教程目录：https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus/model-deployment
- SGLang Ascend FAQ：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/faq.mdx

## 输出

配置文件、参数解释、兼容性检查表、生效配置快照、启动日志和限制说明。
