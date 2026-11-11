# Skills 能力目录

本项目所有可安装 Skill 均位于 `.agents/skills/<skill-name>/SKILL.md`，遵循 Agent Skills 开放格式。安装器直接扫描该目录，不维护第二份硬编码技能清单。

## 当前已建立的 Skills

| Skill | 能力 | 主要来源 |
|---|---|---|
| `sglang-npu-project` | 项目入口、架构导航、开发规范和来源约束 | 本项目规范；CANNBot Skills 组织方式 |
| `sglang-model-bringup` | 模型支持分析、适配、精度与服务验证 | SGLang 模型接入文档、SGLang Ascend 开发文档、CANNBot Skills |
| `sglang-serving-config` | SGLang Ascend 配置、参数兼容和部署验证 | SGLang Ascend Quick Start、参数调优文档和源码 |
| `sglang-performance-optimization` | Baseline、瓶颈诊断、候选优化、A/B 和消融 | SGLang Ascend 文档与实现、CANNBot Skills |
| `sglang-benchmark` | Workload、预热、重复测量、公平性和报告 | SGLang Benchmark 工具、CANN Bench 测试方法 |
| `ascend-profiling` | msprof / PyTorch Profiler 采集与分析 | SGLang Ascend Profiling、MindIE Agent Profiler、CANN 官方工具 |
| `sglang-incident-triage` | Runtime、HCCL、Graph、OOM、Hang 和精度诊断 | SGLang Ascend FAQ、MindIE Agent Debugger、CANNBot Sentry |
| `sglang-code-review` | SGLang / Ascend 代码审查与回归风险检查 | SGLang CONTRIBUTING / CI / 测试、CANNBot Skills |
| `sglang-moe-optimization` | MoE、EP、Dispatch / Combine、通信与负载均衡 | SGLang MoE 实现、Ascend 后端、CANN / HCCL |
| `sglang-graph-mtp-optimization` | Graph、FIA、MTP 兼容性与收益评估 | SGLang Ascend 参数文档、Attention 后端和 Speculative Decoding 实现 |
| `ascend-operator-development` | AscendC / Triton-Ascend 算子开发、精度和性能 | CANNBot DSL、CANN Bench、CANN 官方文档、SGLang Ascend 后端 |

## 安装与分发

```bash
# 查看所有可安装 Skill
python3 scripts/install.py list

# 交互式选择并安装到另一个项目
python3 scripts/install.py install --target /path/to/target-project

# 安装全部当前 Skill
python3 scripts/install.py install --all --target /path/to/target-project

# 安装到 Codex 全局目录
python3 scripts/install.py install --all --global
```

安装器自动扫描 `.agents/skills/`，新增符合规范的 Skill 后无需修改安装器。

直接使用本源码仓库无需安装。入口 Skill 安装时附带 `references/project/` 资料；来源记录用于安全卸载。覆盖、旧版升级和检查方法见 [安装指南](../docs/codex-installation.md)。

## 质量要求

每个 Skill 必须定义适用场景、输入、执行步骤、失败分支、验收标准和来源。当前内容属于工作流指南；需要远程执行、自动测试、Profiling 解析等真实执行能力时，仍需对应 Service / Script 实现，不能仅凭 Skill 文档宣称自动化已经完成。
