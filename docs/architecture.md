# 总体架构与模块边界

## 架构决策

采用 **CANNBot 的 Plugin / Agent / Skill 作为任务组织模型**，参考 CANNBot Knowledge 建设知识治理；参考 MindIE Agent 的基础设施职责拆分。所有框架适配、模型调用链和性能优化逻辑以 SGLang 主仓及实际 Ascend 后端为准。

本项目明确不迁移 vLLM / vLLM-Ascend / xLLM 的框架专属能力、脚本、接口、配置和工作流，也不依赖 VAWS 或 xLLM 作为实现底座。

核心原则：**Agent 负责理解与决策，Skill 负责流程与判断，Service 负责确定性执行，Knowledge 负责可追溯经验。**

## 九类能力范围

1. Agent 架构与任务编排：Plugin、Agent、Skill、任务路由和上下文管理。
2. 知识库与经验管理：Schema、知识卡、Ingest、Query、Lint、来源追踪和经验沉淀。
3. 开发环境与远程机器管理：仓库、SSH、容器、环境探测、NPU 拓扑和远程任务。
4. 模型适配与部署：SGLang 模型接入、权重、算子兼容、服务配置和验证。
5. 推理性能优化：MoE / EP、Attention、Graph、FIA、MTP、KV Cache、PD。
6. Benchmark 与实验管理：Workload、预热、重复测量、A/B、消融、实验记录和回归。
7. Profiling 与故障诊断：msprof、HBM、通信、Runtime、Graph、HCCL、OOM 和精度问题。
8. 算子开发与优化：AscendC、Triton-Ascend、实际使用的 DSL、Kernel 生成和验证。
9. 代码审查与持续回归：SGLang / Ascend 后端 PR 影响分析、正确性和性能回归。

具体来源、边界和迁移方式见 [已筛选能力与迁移来源](selected-scope-and-sources.md)。

## 六个逻辑层

| 层 | 职责 | 不负责 |
|---|---|---|
| Plugin / Workflow | 用户任务入口、路由、编排、阶段门禁 | SSH、设备锁、Profiler 底层解析 |
| Agent | 专业角色分工、任务委派、结果审阅 | 维护隐式基础设施状态 |
| Skill | 操作规程、决策树、工具组合、失败分支 | 长时间进程监管、资源锁 |
| Service | 远程执行、资源租约、Serving、Benchmark、Profiler、实验存储 | 自然语言任务理解 |
| Knowledge | 领域事实、SOP、Workflow、故障与优化经验 | 无证据结论 |
| Reference / Schema | 稳定接口、实验清单、产物格式和机器契约 | 临时实验观察 |

Agent 层不是第一阶段的硬性依赖。先用单 Agent + Workflow + Skills + Services 跑通闭环，再根据需要引入多 Agent。

## 基础服务边界与来源

- remote-dev：SSH、远端文件、容器命令和后台任务。参考 MindIE Agent remote-dev。
- npu-coordinator：设备探测、拓扑、NPU 与端口租约。参考 MindIE Agent coordinator。
- serving-manager：SGLang 服务启动、健康检查、Smoke Test、停止和清理。以 SGLang 启动接口实现，不迁移其他框架 Serving。
- benchmark：Workload、预热、重复测量、指标归一化和结果保存。以 SGLang 官方测试接口及本项目 Schema 独立实现。
- profiler：msprof / torch profiler 采集、解析和跨轮次对比。参考 MindIE Agent Profiler 与 CANN 官方工具。
- experiment-store：Run Manifest、Attempt Ledger、配置快照和产物索引。按本项目需求独立实现。
- git-ci：仓库状态、上游同步、PR 检查和回归门禁。以 SGLang 仓库规范为准。

以上是目标接口边界，不代表服务当前已经实现。

## 知识体系

参考 CANNBot Knowledge 的 OKF / Knowledge Bundle 思路：Markdown + YAML Frontmatter、渐进式索引、来源治理和 Schema / Lint。正式落地前核对其 Schema、Profile、Contract 和许可证；当前仓库尚未宣称通过 OKF 一致性检查。

## 性能证据

每次实验记录源码 Commit、CANN / Driver / Firmware / PyTorch / torch_npu 版本、设备拓扑、模型 Revision、Workload、启动命令、生效配置、Warmup、重复次数和原始产物。Profiling 用于瓶颈归因，非 Profiling 数据用于性能验收。

## 实施顺序

先建设远程执行、环境探测、服务管理、Benchmark、正确性验证和实验记录；再建设 SGLang 专项优化 Skill；最后完善知识 Ingest / Query / Lint 和自动经验沉淀。避免先开发复杂多 Agent Runtime 或 Web 控制台。
