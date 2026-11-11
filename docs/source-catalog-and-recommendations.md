# 上游 Source 总表与补充调研

本文统一登记当前项目已采用和建议进一步研究的 Source。Source 分为四种角色：架构参考、可迁移工具 / Skill、技术事实来源、候选补充来源。**列入 Source 不代表需要整仓迁移。** 每项能力只抽取与 SGLang NPU 研发直接相关的文件、Schema、脚本或流程。

## A. 当前已纳入的主要 Source

### A1. CANNBot 生态（GitCode）

| 仓库 | 角色 | 当前用途 | 建议导入范围 |
|---|---|---|---|
| [cannbot](https://gitcode.com/cann/cannbot) | Agent / Plugin 总体架构 | Plugin、Agent、任务编排的设计参考 | 只借鉴架构和必要入口，不整仓迁移 |
| [cannbot-skills](https://gitcode.com/cann/cannbot-skills) | Skills 集合与安装分发 | Skill 结构、安装器、领域工作流 | 筛选模型迁移、推理优化、算子开发、Review 等通用且适用的 Skill |
| [cannbot-knowledge](https://gitcode.com/cann/cannbot-knowledge) | 知识系统 | OKF / Knowledge Bundle、Schema、Profile、Contract、Ingest、Query、Lint | 优先研究知识格式、Schema、Lint、Query；逐项确认许可证和可复用边界 |
| [cannbot-dsl](https://gitcode.com/cann/cannbot-dsl) | DSL / 算子研发 | 算子设计、DSL 和 Kernel 开发流程参考 | 只选择 SGLang NPU 实际使用的 DSL / 算子路径 |
| [cann-bench](https://gitcode.com/cann/cann-bench) | 算子基准测试 | 算子正确性、性能测量和报告思路 | 复用测试契约、用例组织和可独立工具；不代替服务级 Benchmark |
| [cannbot-sentry](https://gitcode.com/cann/cannbot-sentry) | 质量与诊断 | 问题监测、质量保障流程参考 | 先核查实际功能，避免与 msProbe / MindIE Debugger 重复 |

说明：以上 GitCode 仓库的具体默认分支、Commit、许可证和目录尚需逐个核查；本表不是代码迁移完成声明。

### A2. MindIE Agent 生态（GitHub）

| 仓库 | 角色 | 当前用途 | 建议导入范围 |
|---|---|---|---|
| [mindie-agent](https://github.com/mindie-agent/mindie-agent) | 系统架构 | 组件拆分、宿主插件和基础设施边界 | 只参考架构，不把整套 Agent 产品引入本项目 |
| [remote-dev](https://github.com/mindie-agent/remote-dev) | 远程开发 | SSH、文件读写、远程命令、后台任务 | 优先研究远程执行、安全边界和任务恢复 |
| [coordinator](https://github.com/mindie-agent/coordinator) | NPU 资源协调 | 机器 / 容器台账、设备拓扑、NPU 与端口租约 | 优先研究拓扑探测和资源租约，适配本项目硬件 |
| [profiler](https://github.com/mindie-agent/profiler) | Profiling | 昇腾性能数据采集、解析、关联和对比 | 优先研究可独立复用的解析器与指标模型 |
| [debugger](https://github.com/mindie-agent/debugger) | 故障诊断 | NPU 故障分诊、精度 / 内存问题定位 | 选择通用诊断工具，重写 SGLang 调用链规则 |

### A3. SGLang 官方（GitHub）

| 仓库 / 路径 | 角色 | 当前用途 | 建议导入范围 |
|---|---|---|---|
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 唯一框架事实基线 | 模型、Runtime、Scheduler、Ascend 后端、CLI、测试、CI | 直接以源码和文档为事实来源；只迁移适合本项目的上游 Agent Skills |
| [Ascend NPU 文档](https://github.com/sgl-project/sglang/tree/main/docs/docs/hardware-platforms/ascend-npus) | 部署与调优指南 | 安装、模型支持、参数兼容、Profiling、FAQ | 建立本地索引和版本化知识卡 |
| SGLang 上游源码 / 文档 / CI | 技术事实来源 | 模型、Runtime、Ascend 后端、参数、测试和 CI 行为 | Codex 在 SGLang 源码工作区可直接读取上游文件；本项目不重复导入上游 Skills，避免重复维护 |

## B. 新发现、值得补充的 Source

### B1. Ascend 官方 Agent Skills

[Ascend/agent-skills](https://github.com/Ascend/agent-skills)

这是目前最值得补充的来源之一。它提供面向昇腾的真实专项 Skills，而不只是文档。已检查到的具体内容包括：

- `ascendc-operator-dev`：七阶段算子开发编排。
- `ascendc-operator-compile-debug`：编译、安装和测试排障。
- `ascendc-operator-precision-eval`：算子精度评估。
- Catlass 算子设计、代码生成和测试流程。
- 其他模型迁移、SSH、工具链等 Skill。

**建议导入：**
1. AscendC 算子设计 / 编译 / 精度评估中通用的阶段门禁和检查表；
2. 适合当前 SGLang 算子路径的算子开发子流程；
3. 远程 SSH Skill 中与具体工具无关的安全与会话经验。

**不建议整组照搬：** 其中部分 Skill 面向 Driving SDK、Megatron、VeRL、Catlass 或其他框架 / 工程；必须按本项目范围筛选。对算子开发尤其要确认 SGLang 依赖的真实 DSL、CANN 版本和目标芯片。

### B2. Ascend/msprobe

[Ascend/msprobe](https://github.com/Ascend/msprobe)

这是精度诊断的重要官方工具来源。已确认存在大模型推理精度定位指南，涉及模型结构、参数配置、算子计算偏差，以及推理数据采集和比对。

**建议补充：**
- 推理精度问题分类与定位 SOP；
- Tensor / 算子级数据采集和逐层比对方法；
- NaN / Inf、异常输出和数值误差诊断；
- SGLang 服务场景下的采集接入方式（需单独验证）。

不建议复制 msprobe 本身；优先作为工具依赖 / 外部 CLI，并让 Skill 编排其调用和结果分析。注意其部分功能覆盖训练场景，本项目不引入训练专属流程。

### B3. Ascend/msit

[Ascend/msit](https://github.com/Ascend/msit)

这是昇腾工具集入口，覆盖性能、精度、预检、模型压缩等多类工具。已检查到 Profile 组件及工具导航。

**建议补充：**
- msprof 数据采集和处理接口；
- 推理部署前环境 / 连通性预检；
- 性能数据分析工具的调用方式；
- 与 msProbe、msMonitor 等工具的职责边界。

不建议把整个 msit 作为本项目依赖；应按需调用独立工具，并优先使用官方维护的工具链。

### B4. Ascend/pytorch（torch_npu）

[Ascend/pytorch](https://github.com/Ascend/pytorch)

这是 SGLang Ascend 运行时行为的重要技术事实来源。

**建议补充：**
- torch_npu API 和环境变量知识；
- NPU Runtime、Graph、Stream、通信和算子行为；
- 兼容性、精度和性能相关限制；
- SGLang Ascend 后端实际依赖的 torch_npu 调用链。

不需要迁移 torch_npu 源码；将相关文档和源码入口纳入知识库，并按版本建立索引。

### B5. Ascend/msprof、msmonitor、msmodelslim

- [Ascend/msprof](https://github.com/Ascend/msprof)：性能数据采集底座，优先研究采集配置和数据格式。
- [Ascend/msmonitor](https://github.com/Ascend/msmonitor)：设备监控与指标采集，适合资源观测和任务前后状态记录。
- [Ascend/msmodelslim](https://github.com/Ascend/msmodelslim)：模型量化 / 压缩工具。建议只引入与 SGLang 支持格式直接相关的量化知识、模型格式转换和校验流程，不把模型压缩平台本身纳入 Agent 核心。

### B6. CANN 官方文档与工具链

[CANN 官方文档](https://www.hiascend.com/document)

作为底层技术事实来源，建议按任务索引：
- CANN / Driver / Firmware 版本兼容；
- AscendC、Triton-Ascend、编译器和算子 API；
- HCCL 通信；
- ACL / Runtime / Graph；
- msprof 采集与分析；
- NPU 设备管理和故障码。

不将文档站整站复制到仓库；保留来源 URL、版本和相关章节索引。

## C. 需要避免的重复建设

| 能力 | 主参考 / 工具来源 | 避免重复 |
|---|---|---|
| Agent / Skill 组织 | CANNBot、CANNBot Skills | 不再另造一套 Agent 框架 |
| 知识 Schema / Lint | CANNBot Knowledge | 不同时维护多个互不兼容知识格式 |
| SSH / 远程任务 | MindIE remote-dev | 不在 Skill 脚本中重复造 SSH 客户端 |
| NPU 资源协调 | MindIE coordinator | 不让多个 Skill 各自管理卡锁 |
| Profiling 采集 / 分析 | msprof、MindIE profiler | 区分官方采集工具和本项目分析编排 |
| 精度调试 | msprobe | 不重复实现 Tensor 对比和精度诊断底层工具 |
| 算子开发流程 | Ascend Agent Skills、CANNBot DSL | 只保留 SGLang 真正用到的开发链 |
| SGLang 测试 / CI | SGLang 内置 Skills、上游 CI | 不复制其他框架 CI 工作流 |

## D. 建议的下一轮导入优先级

| 优先级 | Source | 建议动作 | 原因 |
|---|---|---|---|
| P0 | CANNBot Knowledge | 导入知识 Schema、Bundle、索引、Lint / Query / Ingest | 解决知识库结构和治理能力缺失 |
| P0 | Ascend/agent-skills | 筛选 AscendC 设计、编译、精度评估子 Skill | 当前算子开发 Skill 还缺少可复用的阶段化流程 |
| P0 | Ascend/msprobe | 引入推理精度诊断 SOP 与工具调用知识 | 模型适配和算子优化必须有可靠精度定位 |
| P0 | msprof + MindIE Profiler + msit | 统一采集入口、Trace 解析、Host / Device 时间线和指标模型 | 形成性能分析工具链，保留各自职责边界 |

| P1 | Ascend/pytorch | 建立 torch_npu 版本化知识索引 | SGLang NPU 问题常涉及运行时行为 |
| P2 | Ascend/msmonitor | 资源观测、任务前后状态和历史指标 | 远程任务与性能实验需要资源上下文 |
| P2 | Ascend/msmodelslim | 量化格式和模型转换知识 | 只在实际模型适配需要时引入 |

## E. 导入准则

1. 先确定要解决的 SGLang NPU 任务，再选 Source；不以 Source 仓库数量作为项目完整度指标。
2. 先复用官方 CLI / SDK / Schema，再考虑复制代码。
3. 每个迁移项固定源 Commit / Tag、文件路径、许可证和依赖。
4. 对框架耦合内容只以 SGLang 实际调用链为准。
5. 不引入 vLLM、vLLM-Ascend、xLLM 的专属代码、配置、工作流和接口。
6. 同一职责只指定一个主实现来源；其他项目作为补充知识，不形成重复工具。
7. 每个导入项必须有本仓落点、测试和适用边界。


## F. 用户确认的导入边界（2026-11-11）

- CANNBot 生态：引入与 Agent / Skill / Knowledge / DSL / Benchmark / Sentry 相关且经筛选的内容。
- SGLang 官方：不复制其内置 Skills；Codex 在 SGLang 原仓库工作区可直接读取原始 Skill 和源码。本项目只维护 SGLang NPU 特有的知识卡、适配工作流和技术索引。
- Ascend 官方生态：选择性引入 Ascend Agent Skills、msprobe、msprof、msit、msmonitor、torch_npu 相关能力。
- Profiling 工具链作为明确建设项：统一采集入口、Trace 解析与跨轮次比较、Host / Device 时间线、HBM / 通信 / 算子归因、资源监控关联。底层采集优先调用 msprof；评估 MindIE Profiler 可独立复用的解析分析能力；按需集成 msit Profile / 预检组件；msmonitor 提供资源监控数据。
- 上述统一工具链当前处于知识设计和 Source 评估阶段，尚未实现统一 CLI / Parser / UI。
