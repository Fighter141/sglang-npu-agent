---
name: sglang-incident-triage
description: 诊断 SGLang Ascend NPU 的启动失败、请求异常、精度错误、Runtime 崩溃、Graph、HCCL、OOM、Hang 和分布式故障。
---

# SGLang Ascend 故障诊断

## 处理原则

先复现和保全证据，再定位和修改。禁止在未保存日志、进程状态和环境信息前直接清理现场。

## 输入

错误现象、发生时间、最小复现、服务日志、设备状态、源码 Commit、镜像和软件栈版本、并行拓扑、最近变更。

## 诊断流程

1. **事件定界**：明确首次失败时间、影响范围、是否稳定复现、单卡 / 多卡 / 单机 / 多机。
2. **证据保全**：保存完整日志、进程状态、设备状态、环境变量（脱敏）、启动命令和最近代码差异。
3. **分类**：环境安装 / 驱动、模型加载、算子、精度、Runtime、Graph、通信 / HCCL、显存 / OOM、调度 / Hang。
4. **最小复现**：缩小模型、输入长度、并发、卡数或功能组合；每次只减少一个维度并记录结果。
5. **源码定位**：从错误栈进入 SGLang 调用路径，沿 Ascend 后端、torch_npu、CANN / HCCL 追踪；确认报错组件与实际执行组件。
6. **形成假设**：每个假设附支持证据、反证、验证实验和回退方案。
7. **修复验证**：先跑最小复现，再跑相关单测、目标模型 Smoke Test 和回归。
8. **清理与恢复**：核对远程任务、进程、端口和 NPU 资源归属后再清理；未知状态先查询，不盲目重启或重放命令。
9. **经验沉淀**：记录触发条件、根因证据、修复版本、验证范围和已知限制。

## 安全边界

进程终止、容器删除、环境重建、NPU 资源释放和多机重启均须确认目标及影响。不得把凭据、内网地址和未脱敏日志写入知识库。

## 来源

- SGLang Ascend FAQ：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/faq.mdx
- MindIE Agent Debugger：https://github.com/mindie-agent/debugger
- CANNBot Sentry：https://gitcode.com/cann/cannbot-sentry
- CANN / HCCL 官方文档：https://www.hiascend.com/document

## 输出

事件摘要、影响范围、环境快照、复现步骤、根因证据、修复差异、验证结果和未解决风险。
