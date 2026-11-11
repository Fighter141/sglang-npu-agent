# SGLang NPU Agent

面向昇腾 NPU 上 SGLang 开发、部署、性能调优与故障诊断的智能研发工作区。

> 项目状态：架构与工程骨架阶段。路线图中的规划能力不代表已经实现。

## 项目目标

- 工程化 SGLang + Ascend 的模型适配、服务部署、性能优化和故障定位。
- 将 Agent 决策与 SSH、设备分配、服务管理、Benchmark、Profiler 等确定性执行能力分离。
- 为每次实验保存可追溯的源码、软硬件环境、模型、Workload、配置、日志和性能证据。
- 复用 SGLang、CANN、昇腾及社区项目的公开知识和工具，并记录来源、版本、许可证与适用边界。

## 能力范围

本项目只建设经筛选的 SGLang NPU 研发能力：Agent 架构与任务编排、知识库与经验管理、开发环境与远程机器管理、模型适配与部署、推理性能优化、Benchmark 与实验管理、Profiling 与故障诊断、算子开发与优化、代码审查与持续回归。

**明确排除：vLLM / vLLM-Ascend / xLLM 专属的模型适配、Serving、Benchmark、工作流、脚本、接口和配置。** 不将这些项目作为实现依赖。详细范围及来源见 [已筛选能力与迁移来源](docs/selected-scope-and-sources.md)。

## 总体架构

采用 **Plugin / Workflow → Agent → Skill** 组织任务入口和专业能力；将确定性执行能力建设为独立服务；以可追溯知识库和实验数据作为持续迭代基础。

```text
用户 / Coding Agent
  ├── Plugin / Workflow：任务入口、路由、流程编排、阶段门禁
  ├── Agent：模型与正确性、性能与 Profiling、Runtime 故障、代码审查
  ├── Skill：模型适配、Serving 配置、MoE / EP、Graph / FIA / MTP、Benchmark / Debug
  ├── 基础服务：Remote Dev、NPU Coordinator、Serving、Benchmark、Profiler、Experiment Store
  └── Knowledge：硬件软件约束、API / 算子、SOP、故障案例、模型与优化经验
```

## 目录结构

```text
.
├── docs/          # 架构、筛选范围、迁移来源、路线图和工作流
├── plugins/       # 端到端任务入口与工作流
├── agents/        # 可选的专业角色与交接契约
├── skills/        # SKILL.md、references、按需脚本
├── services/      # 远程执行、资源、评测、分析等确定性服务
├── knowledge/     # 来源可追溯的工程知识卡
├── reference/     # Schema、接口契约、Workload 与产物模板
├── runs/          # 本地实验产物，默认不提交 Git
└── tests/         # Schema、路由、脚本和工作流测试
```

## 研发闭环

调研 → 基线 → 诊断 → 方案 → 修改 → 正确性验证 → 性能评测 → Review → 经验沉淀。

性能优化必须先建立可复现基线；Profiler 用于解释瓶颈，非 Profiling 的 Benchmark 用于确认性能结论。

## 主要技术来源

- [CANNBot](https://gitcode.com/cann/cannbot) / [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：Agent、Plugin、Skill 组织方式。
- [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge)：知识格式、Schema、Ingest / Query / Lint 和治理。
- [MindIE Agent](https://github.com/mindie-agent/mindie-agent)：远程执行、资源协调、Profiler、Debugger 等基础设施职责边界。
- [CANNBot DSL](https://gitcode.com/cann/cannbot-dsl) / [CANN Bench](https://gitcode.com/cann/cann-bench) / [CANNBot Sentry](https://gitcode.com/cann/cannbot-sentry)：算子开发、测试和质量保障候选参考。
- [SGLang](https://github.com/sgl-project/sglang)：目标推理框架及 Ascend NPU 后端的实际代码与文档。

所有来源均为候选参考，不代表代码已迁移。迁移前必须检查具体文件、固定版本、许可证、依赖和适用范围。

## 开发原则

1. Skill 负责判断和编排，服务负责确定性执行。
2. 先证据后修改：性能工作先测基线，正确性工作先建立复现。
3. 每个结论必须能追溯到源码版本、环境、模型、Workload 和原始产物。
4. 区分上游文档事实、上游代码事实、真机复现、单次观察和假设。
5. 不静默修改配置；展示最终生效配置及其与默认值的差异。
6. 进程终止、环境替换、资源释放和昂贵多机任务必须有明确安全边界和用户授权。
