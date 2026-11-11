# SGLang NPU Agent

面向昇腾 NPU 上 SGLang 开发、部署、性能调优与故障诊断的智能研发工作区。

> 项目状态：架构与安装器骨架阶段。当前实际可安装的 Skill 只有项目入口 Skill；其他专项能力仍在规划中。

## 项目目标

- 工程化 SGLang + Ascend 的模型适配、服务部署、性能优化和故障定位。
- 将 Agent 决策与 SSH、设备分配、服务管理、Benchmark、Profiler 等确定性执行能力分离。
- 为每次实验保存可追溯的源码、软硬件环境、模型、Workload、配置、日志和性能证据。
- 复用 SGLang、CANN、昇腾及社区项目的公开知识和工具，并记录来源、版本、许可证与适用边界。

## 能力范围

本项目筛选建设九类 SGLang NPU 研发能力：Agent 架构与任务编排、知识库与经验管理、开发环境与远程机器管理、模型适配与部署、推理性能优化、Benchmark 与实验管理、Profiling 与故障诊断、算子开发与优化、代码审查与持续回归。

明确排除 vLLM / vLLM-Ascend / xLLM 专属的模型适配、Serving、Benchmark、工作流、脚本、接口和配置。详细范围及来源见 [已筛选能力与迁移来源](docs/selected-scope-and-sources.md)。

## Codex 安装

本项目采用类似 CANNBot Skills 的安装方式：通过安装器将选定 Skill 安装到 Codex 项目级或全局目录。

```bash
git clone https://github.com/Fighter141/sglang-npu-agent.git
cd sglang-npu-agent

# 查看可安装 Skill
node scripts/install-helper.mjs list

# 安装项目入口 Skill 到当前仓库
node scripts/install-helper.mjs install sglang-npu-project

# 安装到 Codex 全局
node scripts/install-helper.mjs install sglang-npu-project --level global
```

详细说明见 [Codex 安装指南](docs/codex-installation.md)。当前安装器尚未发布 npm 包；专项 Skill 会在真正实现并验证后逐步加入，不发布空壳能力。

## 总体架构

采用 Plugin / Workflow → Agent → Skill 组织任务入口和专业能力；将确定性执行能力建设为独立服务；以可追溯知识库和实验数据作为持续迭代基础。

```text
用户 / Coding Agent
  ├── Plugin / Workflow：任务入口、路由、流程编排、阶段门禁
  ├── Agent：模型与正确性、性能与 Profiling、Runtime 故障、代码审查
  ├── Skill：模型适配、Serving 配置、MoE / EP、Graph / FIA / MTP、Benchmark / Debug
  ├── 基础服务：Remote Dev、NPU Coordinator、Serving、Benchmark、Profiler、Experiment Store
  └── Knowledge：硬件软件约束、API / 算子、SOP、故障案例、模型与优化经验
```

## 主要技术来源

- [CANNBot](https://gitcode.com/cann/cannbot) / [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：Agent、Plugin、Skill 组织方式和安装器设计参考。
- [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge)：知识格式、Schema、Ingest / Query / Lint 和治理。
- [MindIE Agent](https://github.com/mindie-agent/mindie-agent)：远程执行、资源协调、Profiler、Debugger 等基础设施职责边界。
- [CANNBot DSL](https://gitcode.com/cann/cannbot-dsl) / [CANN Bench](https://gitcode.com/cann/cann-bench) / [CANNBot Sentry](https://gitcode.com/cann/cannbot-sentry)：算子开发、测试和质量保障候选参考。
- [SGLang](https://github.com/sgl-project/sglang)：目标推理框架及 Ascend NPU 后端的实际代码与文档。

所有来源均为候选参考，不代表代码已迁移。迁移前必须检查具体文件、固定版本、许可证、依赖和适用范围。
