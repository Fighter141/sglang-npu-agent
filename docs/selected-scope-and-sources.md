# 能力类别与迁移来源清单

本项目已按用户确认的范围筛选为以下 9 类。**不迁移 vLLM、vLLM-Ascend 或 xLLM 的框架专属能力、脚本、接口、配置和工作流。** 不以 VAWS 或 xLLM 作为本项目的实现依赖。

来源登记说明：
- “主要来源”是本类别的候选参考，不表示已经复制代码。
- CANNBot 相关仓库需要进一步核查具体目录、Commit、许可证和依赖后，才能决定复用或改写。
- SGLang 相关功能以 SGLang 官方代码和实际 Ascend 后端实现为准；其他框架只能作为背景资料，不能作为实现依据。
- 每次实际迁移必须登记源文件路径、固定版本、许可证、目标路径、改动和测试证据。

## 类别 1：Agent 架构与任务编排

**纳入范围**
- Plugin / Workflow：研发任务入口和端到端流程。
- Agent：专业角色定义、任务委派和交接。
- Skill：任务路由、执行步骤、判断条件、失败分支。
- 上下文与状态管理：项目约定、任务上下文和实验引用。

**主要来源**
- [CANNBot](https://gitcode.com/cann/cannbot)：整体 Agent / Plugin 组织方式。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：Skill 组织和任务流程。

**不纳入**
- 训练框架、其他推理框架专属 Plugin / Agent / Skill。
- 第一阶段不建设复杂的多 Agent Runtime；先跑通单 Agent 工作流。

## 类别 2：知识库与经验管理

**纳入范围**
- Knowledge Schema / Profile / Contract。
- 知识卡、分类目录和渐进式索引。
- Ingest、Query、Lint、来源追踪。
- 知识质量与检索评测。
- 模型 / PR / Issue / 故障 / 优化经验沉淀。

**主要来源**
- [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge)：OKF、Knowledge Bundle、Schema、Profile、Contract、Ingest / Query / Lint 和治理。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：知识调用与任务工作流的衔接方式。
- SGLang 官方文档、源码、PR、Issue：SGLang 技术知识的事实来源。

**迁移边界**
- 优先核查并复用 CANNBot Knowledge 的知识格式和校验机制。
- 不把未经核实的经验直接标记为已验证。
- 不迁移与 SGLang NPU 无关的知识领域。

## 类别 3：开发环境与远程机器管理

**纳入范围**
- SGLang 及 Ascend 后端仓库初始化和版本配套。
- SSH、远程文件、容器命令、后台任务。
- CANN / Driver / Firmware / PyTorch / torch_npu 环境探测。
- NPU 拓扑、设备占用、资源与端口管理。
- 远程代码同步和任务清理。

**主要来源**
- [MindIE Agent](https://github.com/mindie-agent/mindie-agent)：组件职责和远程研发体系。
- [remote-dev](https://github.com/mindie-agent/remote-dev)：SSH、远端文件、命令和后台作业。
- [coordinator](https://github.com/mindie-agent/coordinator)：机器、容器、NPU 拓扑与资源租约。
- [SGLang](https://github.com/sgl-project/sglang)：本项目实际需要管理的仓库和版本关系。

**不纳入**
- VAWS 的 vLLM + vLLM-Ascend 双仓结构和专属初始化脚本。
- vLLM 专属 Worktree、Serving 或模型工作流。若需要通用 Git Worktree 能力，则独立设计，不复制其框架约定。

## 类别 4：模型适配与部署

**纳入范围**
- 模型支持情况分析、模型结构和配置检查。
- SGLang Model Registry / Model Loader 接入。
- 权重、Tokenizer、量化格式和精度检查。
- Ascend 算子、Attention、MoE 等后端适配。
- SGLang 服务配置、启动、健康检查和 Smoke Test。
- 版本兼容性检查。

**主要来源**
- [SGLang 主仓库](https://github.com/sgl-project/sglang)：模型注册、Runtime、Scheduler、启动参数、测试规范。
- [SGLang Ascend NPU 文档](https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus)：昇腾安装、部署和调优文档。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：模型迁移、适配、验证类工作流。
- CANN / torch_npu 官方文档与对应算子实现：底层兼容性依据。

**迁移边界**
- 模型适配必须围绕 SGLang 的接口和调用链实现。
- 不迁移 vLLM Model Adapter、vLLM Serving 或其他框架专属实现。

## 类别 5：推理性能优化

**纳入范围**
- Baseline 和 Workload 分析。
- MoE / EP / 通信后端 / 负载均衡。
- Attention Backend、FIA、KV Cache。
- Graph / CUDA Graph 对应的 NPU 图执行能力。
- MTP / Speculative Decoding。
- PD 分离与 Prefill / Decode。
- 配置搜索、候选排序、消融和收益回退判断。

**主要来源**
- SGLang 主仓库和 Ascend 后端实际实现、文档、PR、Issue。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：昇腾推理优化类 Skill。
- CANN / HCCL / torch_npu 官方资料：底层执行、通信和算子约束。
- 本项目在目标 A3 / 910C 环境上的复现实验：最终优化结论依据。

**不纳入**
- xLLM 专属 SOTA Loop、配置、脚本和实验接口。
- vLLM 专属调优逻辑。
- 未经 SGLang Ascend 验证的其他框架参数组合。

## 类别 6：Benchmark 与实验管理

**纳入范围**
- Workload / Trace 管理和固定。
- 预热、重复测量、并发扫描。
- TTFT、TPOT、吞吐、显存、正确性等指标。
- Baseline / Candidate 对比、公平性检查、A/B 和消融。
- Run / Attempt 记录、日志与产物索引。
- 性能回归和报告生成。

**主要来源**
- [CANN Bench](https://gitcode.com/cann/cann-bench)：昇腾算子 / 性能测试的候选参考。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：测试任务工作流。
- SGLang 官方 Benchmark / Eval 工具及其真实接口：服务级测试执行。
- 本项目独立定义的 Experiment Manifest / Result Schema：避免绑定其他框架。

**不纳入**
- xLLM Workflow 的专属 Experiment Lifecycle、CLI、Schema 和目录结构。
- VAWS 的 vLLM Benchmark 实现。只在确认某个底层测试方法通用且许可证允许时，才单独评估。

## 类别 7：Profiling 与故障诊断

**纳入范围**
- msprof 采集、解析和时间线分析。
- Host / Device、算子、通信、HBM / 显存分析。
- Runtime、Graph、HCCL、OOM、Hang 故障诊断。
- 精度错误和数值异常定位。
- 根因证据、修复验证和回归。

**主要来源**
- [MindIE Agent Profiler](https://github.com/mindie-agent/profiler)：昇腾 Profiling 采集和分析。
- [MindIE Agent Debugger](https://github.com/mindie-agent/debugger)：故障分诊和精度调试。
- [CANNBot Sentry](https://gitcode.com/cann/cannbot-sentry)：监测和质量保障候选参考。
- CANN / msprof / torch_npu 官方工具与 SGLang Ascend 日志、Trace：技术依据。

**迁移边界**
- 复用通用采集 / 解析能力时必须检查依赖和许可证。
- 故障分类、日志规则和调用栈必须针对 SGLang NPU 验证。

## 类别 8：算子开发与优化

**纳入范围**
- SGLang 算子调用链和热点识别。
- AscendC、Triton-Ascend 及实际使用的 DSL / Kernel 开发。
- 算子生成、调优、精度和性能验证。
- 算子接口与不同 NPU 后端的适配。
- 算子级性能回归。

**主要来源**
- [CANNBot DSL](https://gitcode.com/cann/cannbot-dsl)：DSL / 算子开发能力候选参考。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：算子开发与优化流程。
- [CANN Bench](https://gitcode.com/cann/cann-bench)：算子正确性和性能测试。
- SGLang Ascend 实际算子调用点、torch_npu / CANN 官方实现：适配依据。

**迁移边界**
- 只引入 SGLang NPU 实际需要的算子开发路径。
- 不引入无关 DSL、其他芯片或训练专属工作流。

## 类别 9：代码审查与持续回归

**纳入范围**
- SGLang / Ascend 后端 PR 变更影响分析。
- 模型、算子、Runtime 和配置兼容性 Review。
- 正确性回归、性能回归和版本矩阵。
- 上游 Commit / PR 追踪与知识更新。

**主要来源**
- SGLang 官方仓库的 CONTRIBUTING、测试目录、CI 和 PR。
- [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：Review 类任务工作流。
- [CANNBot Sentry](https://gitcode.com/cann/cannbot-sentry)：质量监测候选参考。
- 本项目自己的测试与回归契约。

**不纳入**
- vLLM / xLLM 专属 PR 检查规则、CI 工作流和版本发布脚本。

## 迁移状态

| 状态 | 定义 |
|---|---|
| 候选来源 | 已选定参考项目，尚未核对具体实现 |
| 已核查 | 已检查具体路径、Commit / Tag、许可证和依赖 |
| 已迁移 | 内容或代码已进入本仓，并有来源记录 |
| 已验证 | 本仓自动化测试通过；硬件能力另需标注真机型号、软件版本和结果 |

当前所有来源均为候选来源。后续逐项核查，不进行整仓复制。
