# 基础服务目录

Services 提供可独立测试的确定性执行能力。Skill 可以调用 Service，但不得用提示词替代资源锁、后台作业状态、Benchmark 或 Profiler 解析。

| 服务 | 责任 | 主要来源 |
|---|---|---|
| remote-dev | SSH、远端文件、容器命令、后台任务 | MindIE Agent remote-dev |
| npu-coordinator | 设备探测、拓扑、卡与端口租约 | MindIE Agent coordinator |
| serving-manager | SGLang 服务启动、健康检查、停止和清理 | SGLang 官方启动接口；本项目适配实现 |
| benchmark | Workload、预热、重复测量、结果归档 | SGLang 官方测试工具；CANN Bench 测试方法参考 |
| profiler | msprof 采集、解析和跨轮次分析 | MindIE Agent Profiler；CANN 官方工具 |
| experiment-store | 实验清单、候选记录、检查点和结果归档 | 本项目独立定义；参考通用实验管理方法 |

当前均为规划接口。实施前先核查上游具体实现、依赖和许可证，并定义本仓服务契约。明确不迁移 vLLM / xLLM 专属 Serving、Benchmark 或实验管理实现。
