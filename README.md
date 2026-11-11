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

## Codex 使用与 Skill 安装（无需 npm）

### 直接作为研发工作区

```bash
git clone https://github.com/Fighter141/sglang-npu-agent.git
cd sglang-npu-agent
codex
```

Codex 会读取根目录 `AGENTS.md`，并发现 `.agents/skills/` 下的项目级 Skill。

### 安装到其他项目

克隆本仓库后，在仓库目录运行 Python 安装器：

```bash
git clone https://github.com/Fighter141/sglang-npu-agent.git
cd sglang-npu-agent

# 交互式选择 Skill，安装到当前目录对应的项目
python3 scripts/install.py install

# 安装指定 Skill 到另一个项目
python3 scripts/install.py install sglang-npu-project --target /path/to/target-project

# 安装到 Codex 全局
python3 scripts/install.py install sglang-npu-project --global
```

安装器只使用 Python 标准库，不需要 npm、Node.js 或第三方 CLI。完整命令见 [Codex 安装指南](docs/codex-installation.md)。

## 总体架构

采用 Plugin / Workflow → Agent → Skill 组织任务入口和专业能力；将确定性执行能力建设为独立服务；以可追溯知识库和实验数据作为持续迭代基础。

## 主要技术来源

- [CANNBot](https://gitcode.com/cann/cannbot) / [CANNBot Skills](https://gitcode.com/cann/cannbot-skills)：Agent、Plugin、Skill 组织方式。
- [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge)：知识格式、Schema、Ingest / Query / Lint 和治理。
- [MindIE Agent](https://github.com/mindie-agent/mindie-agent)：远程执行、资源协调、Profiler、Debugger 等基础设施职责边界。
- [CANNBot DSL](https://gitcode.com/cann/cannbot-dsl) / [CANN Bench](https://gitcode.com/cann/cann-bench) / [CANNBot Sentry](https://gitcode.com/cann/cannbot-sentry)：算子开发、测试和质量保障候选参考。
- [SGLang](https://github.com/sgl-project/sglang)：目标推理框架及 Ascend NPU 后端的实际代码与文档。

所有来源均为候选参考，不代表代码已迁移。迁移前必须检查具体文件、固定版本、许可证、依赖和适用范围。
