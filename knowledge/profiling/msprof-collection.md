---
id: msprof-collection
title: msprof 采集底座与接入原则
category: profiling
evidence: upstream_documented
status: source_index
last_verified: 2026-11-11
sources:
  - https://github.com/Ascend/msprof
  - https://github.com/Ascend/msit/tree/master/msit/components/profile
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/profiling.mdx
---

# msprof 采集底座与接入原则

## 定位

msprof 是昇腾性能数据采集底座。本项目应通过适配器调用目标环境安装的官方工具，避免自行实现设备级采集。

## 接入时必须核实

- 目标 CANN / msprof 版本和命令行参数。
- 采集应用的启动方式、PID / 进程树关联方式。
- Host、Device、算子、通信、HBM / 系统硬件指标的采集开关。
- 采集开销、采样频率、输出目录和数据格式。
- 多 Rank / 多机采集文件的归属与合并规则。
- 工具退出码、超时、部分失败和磁盘空间处理。

## 统一入口设计

建议封装为 `profile collect` 任务接口，输入 Run Manifest、服务 PID / 启动命令、采集 Profile 和输出目录；输出任务状态、实际命令、工具版本、原始文件清单和校验和。

不得假定所有版本使用同一参数名或相同数据格式。执行前必须从目标机器上的 `msprof --help` 和对应版本文档核验。
