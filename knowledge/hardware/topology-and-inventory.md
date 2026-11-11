---
id: hardware-topology-inventory
title: 昇腾 NPU 拓扑与实验环境盘点
category: hardware
evidence: upstream_documented
status: initial_reference
last_verified: 2026-11-11
sources:
  - https://www.hiascend.com/document
  - https://github.com/Ascend/pytorch
---

# 昇腾 NPU 拓扑与实验环境盘点

## 目的

在 SGLang NPU 部署、Benchmark 和 Profiling 前固定设备与软件环境，避免因卡数、Die / Rank 映射或版本不同导致实验不可比。

## 必须采集

- 产品型号和设备标识：910C / A3，准确 SKU 以设备信息为准。
- 物理卡数、每卡 Die 数、可见 NPU 数和 Rank 映射。
- 互联拓扑、HCCS / RoCE / 网络接口及链路状态（按实际平台采集）。
- 每设备 HBM 总量、运行时可用量、任务前后峰值。
- Driver、Firmware、CANN、torch_npu、PyTorch、Python 版本。
- 容器镜像 Digest、环境变量、可见设备配置。
- SGLang 与 Ascend 后端 Git Commit。

## 采集建议

在目标机器上通过官方设备管理命令和 torch_npu 运行时接口采集。常见入口包括 `npu-smi info`、`torch.npu.device_count()`、设备属性查询和 HCCL 拓扑配置。具体命令参数需按安装版本的帮助信息确认。

## 重要约束

1. 不用“机器有几张卡”替代逻辑 NPU / Die / Rank 数量。
2. 多机实验需记录每节点设备映射、网卡和通信拓扑。
3. 测量前后记录设备健康、温度、功耗和其他进程占用（若平台提供）。
4. 未采集的规格字段写 `unknown`，不得根据型号名称猜测。

## 验证状态

这是环境盘点规范，不包含特定机器的实测数据；当前不构成 910C / A3 的规格结论。
