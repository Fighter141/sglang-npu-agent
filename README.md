# SGLang NPU Agent

面向昇腾 NPU 上 SGLang 开发、部署、性能调优与故障诊断的智能研发工作区。

> 项目处于架构与工程骨架阶段。路线图中的规划能力不代表已经实现。

## 项目目标

- 工程化 SGLang + Ascend 的模型适配、服务部署、性能优化和故障定位。
- 将 Agent 决策与 SSH、设备分配、服务管理、Benchmark、Profiler 等确定性执行能力分离。
- 为每次实验保存可追溯的源码、软硬件环境、模型、Workload、配置、日志和性能证据。
- 复用 SGLang、CANN、昇腾及社区项目的公开知识和工具，并记录来源、版本、许可证与适用边界。

## 总体架构

采用 **Plugin / Workflow → Agent → Skill** 组织任务入口和专业能力；将确定性执行能力建设为独立服务；以可追溯知识库和实验数据作为持续迭代基础。

```text
用户 / Codex / Claude Code / Cursor
  ├── Plugin / Workflow：任务入口、路由、流程编排、阶段门禁
  ├── Agent：模型与正确性、性能与 Profiling、Runtime / 分布式故障、代码审查
  ├── Skill：模型适配、Serving 配置、MoE / EP、Graph / FIA / MTP、Benchmark / Debug
  ├── 基础服务：Remote Dev、NPU Coordinator、Serving、Benchmark、Profiler、Experiment Store
  └── Knowledge：硬件与软件约束、API / 算子、SOP、故障案例、模型与优化经验
```

## 目录结构

```text
.
├── docs/          # 架构、迁移来源、路线图和工作流文档
├── plugins/       # 端到端任务入口与工作流
├── agents/        # 可选的专业角色与交接契约
├── skills/        # SKILL.md、references、按需脚本
├── services/      # 远程执行、资源、评测、分析等确定性服务
├── knowledge/     # 按知识规范组织的来源可追溯知识卡
├── reference/     # Schema、接口契约、Workload 与产物模板
├── runs/          # 本地实验产物，默认不提交 Git
└── tests/         # Schema、路由、脚本和工作流测试
```

## 研发闭环

调研 → 基线 → 诊断 → 方案 → 修改 → 正确性验证 → 性能评测 → Review → 经验沉淀。

性能优化必须先建立可复现基线；Profiler 用于解释瓶颈，非 Profiling 的 Benchmark 用于确认性能结论。

## 上游项目与迁移来源

**每个模块的迁移来源、拟研究路径、迁移方式和状态均登记在 [迁移来源映射表](docs/source-migration-map.md)。** 当前均为候选来源，不代表代码已复制或适配完成。

- [CANNBot](https://gitcode.com/cann/cannbot) / [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：Plugin、Agent、Skill 组织方式。
- [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge)：OKF v0.2、知识卡、Ingest / Query / Lint 和治理。
- [CANNBot DSL](https://gitcode.com/cann/cannbot-dsl) / [CANN Bench](https://gitcode.com/cann/cann-bench) / [CANNBot Sentry](https://gitcode.com/cann/cannbot-sentry)：算子 DSL、测试基准与质量保障候选参考。
- [vLLM-Ascend Workspace](https://github.com/mindie-agent/vllm-ascend-workspace)：多仓工作区、Worktree、远程 NPU 开发与服务测试。
- [xLLM AI Coding Workflow](https://github.com/xLLM-AI/xllm-workflow)：实验生命周期、证据 Schema、Benchmark 公平性与优化闭环。
- [MindIE Agent](https://github.com/mindie-agent/mindie-agent)：Remote Dev、Coordinator、Profiler、Debugger 等基础设施职责边界。
- [SGLang](https://github.com/sgl-project/sglang)：目标推理框架及 Ascend NPU 后端的实际代码与文档。

迁移前必须逐项检查源文件、固定版本、许可证、依赖和适用范围。不得将参考项目的能力描述为本项目已经实现。

## 开发原则

1. Skill 负责判断和编排，服务负责确定性执行。
2. 先证据后修改：性能工作先测基线，正确性工作先建立复现。
3. 每个结论必须能追溯到源码版本、环境、模型、Workload 和原始产物。
4. 区分上游文档事实、上游代码事实、真机复现、单次观察和假设。
5. 不静默修改配置；展示最终生效配置及其与默认值的差异。
6. 进程终止、环境替换、资源释放和昂贵多机任务必须有明确安全边界和用户授权。

项目状态见 [路线图](docs/roadmap.md)。
