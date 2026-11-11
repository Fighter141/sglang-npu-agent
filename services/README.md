# 基础服务目录

Services 提供可独立测试的确定性执行能力。Skill 可以调用 Service，但不得用提示词替代资源锁、后台作业状态、Benchmark 或 Profiler 解析。

| 服务 | 责任 | 主要迁移来源 |
|---|---|---|
| remote-dev | SSH、远端文件、容器命令、后台任务 | MindIE Agent remote-dev；VAWS 远程工具 |
| npu-coordinator | 设备探测、拓扑、卡与端口租约 | MindIE Agent coordinator |
| serving-manager | SGLang 服务启动、健康检查、停止和清理 | VAWS vLLM-Ascend Serving，需改写为 SGLang |
| benchmark | Workload、预热、重复测量、结果归档 | VAWS Benchmark；xLLM Workflow Benchmark |
| profiler | msprof 采集、解析和跨轮次分析 | MindIE Agent Profiler；VAWS Profiling |
| experiment-store | Run / Attempt / Checkpoint / Finalize | xLLM Workflow Experiment Lifecycle |

当前均为规划接口。实施前先核查上游具体实现、依赖和许可证，并定义本仓服务契约。
