# 迁移来源映射与复用计划

本文是本项目的来源登记表。**Source 表示参考或候选迁移来源，不代表代码已经复制、接口已经兼容或功能已经实现。** 每次真正迁移时，必须补充源文件路径、固定 Commit / Tag、许可证、改动说明、测试证据和本项目对应路径。

## 1. 总体架构与 Agent 组织

| 本项目模块 | 迁移来源 | 重点研究 / 迁移内容 | 迁移方式与边界 |
|---|---|---|---|
| Plugin / Workflow | [CANNBot](https://gitcode.com/cann/cannbot)、[CANNBot Skills](https://gitcode.com/cann/cannbot-skills) | Plugin-Agent-Skill 组织、任务入口、领域工作流、技能发现与编排 | 借鉴职责边界和流程组织；针对 SGLang 重写入口与路由，不复制 CANN 专属实现 |
| Skill 目录与规范 | [CANNBot Skills](https://gitcode.com/cann/cannbot-skills) | Skill 分类、输入输出、执行步骤、工具调用和验证门禁 | 逐项选择 SGLang 适用 Skill；固定源版本并检查许可证 |
| Agent 角色 | [CANNBot](https://gitcode.com/cann/cannbot)、[MindIE Agent](https://github.com/mindie-agent/mindie-agent) | 专业角色、任务委派、上下文边界、工具访问边界 | 初期单 Agent；出现独立并行调查或独立审查需求后再引入多 Agent |
| 跨客户端规则 | [VAWS](https://github.com/mindie-agent/vllm-ascend-workspace) | AGENTS.md、客户端规则入口、工作区初始化 | 迁移通用规则；不把 vLLM 专用规则直接用于 SGLang |

## 2. 知识系统

| 本项目模块 | 迁移来源 | 重点研究 / 迁移内容 | 迁移方式与边界 |
|---|---|---|---|
| 知识 Bundle 与卡片 | [cannbot-knowledge](https://gitcode.com/cann/cannbot-knowledge) | OKF v0.2、Knowledge Bundle、Markdown + YAML Frontmatter、Concept ID、index.md 渐进导航 | 优先按上游 Schema / Profile 实现；不要自行宣称兼容，需通过其检查 |
| Schema / 治理 | 同上：`governance/schemas/`、`governance/specs/`、`governance/contracts/` | 字段、受控词表、路径规则、来源与生命周期校验 | 优先复用规范与契约；代码复制前审许可证 |
| Ingest / Query / Lint | 同上：`.agents/skills/` 中的 `knowledge-ingest`、`knowledge-query`、`knowledge-lint` | 来源登记、候选卡生成、检索、Lint、审计 receipt | 先复用只读 Query / Lint；Ingest 以候选卡方式写入，合并需 Review |
| 知识评测 | 同上：`evals/`、`check.sh` | 检索回归、导航检查、治理检查、安装回归 | 建立 SGLang 专属检索样例和回归集 |
| 模型 / PR 经验 | [xLLM Workflow](https://github.com/xLLM-AI/xllm-workflow) 的 model / PR history 思路 | 历史变更、失败尝试、模型适配风险和优化经验 | 设计 SGLang 模型 Dossier；每条经验绑定 commit、环境和证据 |

## 3. 远程开发与基础设施

| 本项目模块 | 迁移来源 | 重点研究 / 迁移内容 | 迁移方式与边界 |
|---|---|---|---|
| 多仓工作区 / Worktree | [vllm-ascend-workspace](https://github.com/mindie-agent/vllm-ascend-workspace) | `repo_init.py`、`workspace.py`、Git submodule、Fork / upstream、任务 Worktree 隔离 | 将 vLLM + vLLM-Ascend 双仓关系改成 SGLang + Ascend 后端实际仓库关系；先核对当前 SGLang 后端代码归属 |
| 远程执行 | [MindIE Agent remote-dev](https://github.com/mindie-agent/remote-dev)；VAWS 远程工具脚本 | SSH、远端文件读写、容器命令、后台作业、日志增量读取 | 优先封装已有 SSH / CLI；定义超时、取消、重连、幂等和凭据边界 |
| NPU 资源协调 | [MindIE Agent coordinator](https://github.com/mindie-agent/coordinator) | 机器 / 容器台账、设备拓扑、NPU 与端口租约、并发任务冲突 | 先做只读探测，再实现显式租约；适配 A3 双 Die / 910C 拓扑前需真机验证 |
| Serving 生命周期 | VAWS 的 `vllm-ascend-serving`；MindIE Agent remote-dev / coordinator | 启动、健康检查、Smoke Test、停止、清理、服务身份记录 | 重写 SGLang 启动参数与后端检查；保留可追踪 launch ID |
| 安全与任务恢复 | MindIE Agent remote-dev / coordinator | 任务状态、资源归属、取消与清理 | 不盲目重放未知状态的远端命令；先查询任务状态再恢复 |

## 4. Benchmark、Profiler、Debug 与实验管理

| 本项目模块 | 迁移来源 | 重点研究 / 迁移内容 | 迁移方式与边界 |
|---|---|---|---|
| Benchmark Runner | VAWS `vllm-ascend-benchmark`；xLLM Workflow `xllm-npu-benchmark`、`xllm-npu-eval-runner` | 预热、重复测量、并发矩阵、结果聚合、公平性检查 | 替换为 SGLang 可用的 serving benchmark；统一 TTFT / TPOT / 吞吐和原始结果格式 |
| 实验生命周期 | [xLLM Workflow](https://github.com/xLLM-AI/xllm-workflow) 的 `xllm-experiment-lifecycle`、`scripts/xllm_flow.py` | Run / Attempt / Checkpoint / Finalize、证据校验、归档 | 迁移其证据模型与生命周期思想；运行器和配置适配 SGLang |
| Profiler 采集 | VAWS `ascend-profiling-collection`；MindIE Agent [profiler](https://github.com/mindie-agent/profiler) | msprof / torch profiler 采集、任务身份、原始文件管理 | 优先封装官方工具，固定采集配置和环境 |
| Profiler 分析 | VAWS `ascend-profiling-analysis`；MindIE Agent profiler | Host-Device 关联、算子耗时、通信、显存、跨轮次比较 | 先明确 SGLang trace 格式和分析指标，再移植解析器 |
| 故障与精度诊断 | MindIE Agent [debugger](https://github.com/mindie-agent/debugger)；xLLM Workflow `xllm-npu-incident-triage`、`xllm-npu-accuracy-debug`；[CANNBot Sentry](https://gitcode.com/cann/cannbot-sentry) | 日志分诊、复现、精度定位、HCCL / Graph / OOM 故障路径 | 迁移通用诊断流程；SGLang 特有栈、错误码和定位逻辑需重新验证 |
| 性能优化闭环 | xLLM Workflow `xllm-npu-sota-loop`；CANNBot Skills 推理优化类 Skill | 候选排序、单变量实验、消融、证据门禁、经验沉淀 | 迁移方法论和实验产物契约，不照搬 xLLM 专属命令 |
| 算子开发 / DSL | [CANNBot DSL](https://gitcode.com/cann/cannbot-dsl)、[CANNBot Skills](https://gitcode.com/cann/cannbot-skills) | AscendC / PyPTO / TileLang / Triton 等开发流程与模板 | 只引入 SGLang NPU 确实调用的算子路径；DSL / 编译器适配单独验证 |
| 算子测试基准 | [CANN Bench](https://gitcode.com/cann/cann-bench) | 算子正确性、性能测试与基准管理 | 研究测试契约和数据组织；与 SGLang 端到端 Benchmark 分层，不混用指标 |

## 5. SGLang 专属适配来源

| 本项目模块 | 权威来源 | 需要抽取的内容 |
|---|---|---|
| SGLang 主框架行为 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | Model Registry、Scheduler、Runtime、Backend 接口、启动参数、测试规范 |
| Ascend 后端 | SGLang 仓库中的 Ascend NPU 文档与实际后端代码；对应 Ascend 维护仓库 / PR | NPU 算子、Attention、Graph、通信、平台检测、版本约束 |
| MoE / EP | SGLang Ascend 对应实现、CANN / HCCL 文档、上游 PR | FuseEP / DeepEP 等后端适配、模式选择、负载均衡和兼容性 |
| MTP / Speculative Decoding | SGLang 对应实现、模型官方配置、Ascend 后端测试 | Draft / Target 兼容性、Graph、Prefix Cache 交互、接受率和端到端收益 |
| PD 分离 | SGLang PD 实现、KV Transfer / Mooncake 等官方集成文档 | Prefill / Decode 调度、KV 传输、网络与服务指标 |

SGLang 专属模块不能仅从 vLLM 迁移。vLLM-Ascend 的 Skill 可以提供流程参考，但模型注册、调度器、后端接口、算子调用点和服务参数必须以 SGLang 实际代码为准。

## 6. 迁移状态与准入规则

当前状态统一使用：
- `候选来源`：已识别项目，尚未逐文件核查。
- `已核查`：已检查指定版本、路径和许可证。
- `已迁移`：代码 / Schema / 文档已进入本仓，并注明来源。
- `已验证`：本仓测试通过；硬件相关能力还需注明真机型号与软件版本。

当前本表所列均为**候选来源**，不应误读为已完成迁移。

每次迁移必须补充以下记录：
1. 上游仓库 URL、源文件路径、Commit / Tag、核验日期；
2. 许可证与署名要求；
3. 迁移类型：直接复用 / 适配改写 / 仅借鉴设计；
4. 本仓落点和改动差异；
5. 单元测试、集成测试及真机验证结果；
6. 尚未覆盖的芯片、版本和边界条件。

不得将不同项目的脚本直接拼接成一个未经验证的工具链。先复用接口与数据契约，再逐个迁移实现。
