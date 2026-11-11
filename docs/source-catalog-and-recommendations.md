# 上游 Source 总表与迁移建议

本文件登记本项目选定的 Source。Source 分为架构参考、可迁移 Skill / 工具、技术事实来源和候选补充来源。列入清单不代表整仓迁移。

## 1. CANNBot 生态（按需引入）

| 仓库 | 用途 | 处理策略 |
|---|---|---|
| [cannbot](https://gitcode.com/cann/cannbot) | Plugin / Agent 架构 | 借鉴组织方式 |
| [cannbot-skills](https://gitcode.com/cann/cannbot-skills) | Skills、安装器、专项流程 | 迁移适用的通用 Skill |
| [cannbot-knowledge](https://gitcode.com/cann/cannbot-knowledge) | OKF、Schema、知识治理 | 优先核查 Schema / Profile / Contract / Ingest / Query / Lint |
| [cannbot-dsl](https://gitcode.com/cann/cannbot-dsl) | DSL / 算子开发 | 仅选 SGLang NPU 实际需要的路径 |
| [cann-bench](https://gitcode.com/cann/cann-bench) | 算子基准测试 | 复用测试契约与工具 |
| [cannbot-sentry](https://gitcode.com/cann/cannbot-sentry) | 质量诊断 | 核查后按需引入 |

## 2. Ascend 官方生态（重点引入）

| 仓库 | 用途 | 处理策略 |
|---|---|---|
| [Ascend/agent-skills](https://github.com/Ascend/agent-skills) | AscendC、Triton、Profiling、设备和通信 Skills | 已开始选择性迁入，见下文 |
| [Ascend/msprof](https://github.com/Ascend/msprof) | 性能数据采集 | 主采集底座 |
| [Ascend/msit](https://github.com/Ascend/msit) | Profile、数据处理、环境预检等工具 | 按组件集成 |
| [Ascend/msprobe](https://github.com/Ascend/msprobe) | 推理精度诊断 | 工具调用 + Skill 工作流 |
| [Ascend/msmonitor](https://github.com/Ascend/msmonitor) | NPU 资源监控 | 资源指标采集 |
| [Ascend/pytorch](https://github.com/Ascend/pytorch) | torch_npu / Runtime | 版本化知识索引，不复制源码 |
| [CANN 文档](https://www.hiascend.com/document) | CANN、HCCL、AscendC、Triton-Ascend | 底层技术事实来源 |

### 2.1 已迁入 Ascend/agent-skills 的能力

上游仓库：<https://github.com/Ascend/agent-skills>
源 Commit：`155ac37bd169ddb89479af528297cfb2237400aa`
原仓库许可证：MulanPSL-2.0。迁入文件保留源路径和 Commit 标记。

**Profiling / 设备 / 通信**
- `ascend-profiling-anomaly`：SKILL、分析规则、数据 Schema、数据指南、架构报告模板和 Host gap 脚本。
- `npu-smi`：SKILL、设备查询 / 配置 / 固件 / 虚拟化参考、健康检查脚本。
- `hccl-test`：SKILL、常见问题、预检清单、测试场景和参数参考；已迁入多机测试、预检、快速验证、结果解析等脚本。

**AscendC**
- `ascendc-operator-dev`
- `ascendc-operator-design`
- `ascendc-operator-code-gen`
- `ascendc-operator-compile-debug`
- `ascendc-operator-code-review`
- `ascendc-operator-project-init`
- `ascendc-operator-testcase-gen`
- `ascendc-operator-precision-eval`
- `ascendc-operator-precision-debug`
- `ascendc-operator-performance-eval`
- `ascendc-operator-performance-optim`
- `ascendc-operator-mssanitizer`
- `ascendc-operator-doc-gen`

**Triton-Ascend**
- `triton-operator-dev`
- `triton-operator-design`
- `triton-operator-code-gen`
- `triton-operator-code-review`
- `triton-operator-env-config`
- `triton-operator-performance-eval`
- `triton-operator-performance-optim`
- `triton-operator-precision-eval`
- `triton-operator-doc-gen`

已选择性迁入上述 25 个 Skill 入口及其 150 个文件（SKILL.md、references、scripts、templates、examples），源文件均来自固定 Commit。仅省略空目录占位文件 `.gitkeep`。仍需检查相对路径、子 Skill 调用关系、脚本安全和适用硬件版本；仅省略了空目录占位文件 `.gitkeep`；其余 150 个上游文件均已同步。文件同步完成不等于执行验证完成。

### 2.2 Profiling 工具链边界

- **msprof**：统一采集底座，保留原始 Trace。
- **msit Profile**：按需提供官方 Profile CLI、数据处理和预检能力。
- **ascend-profiling-anomaly**：消费已采集的 Profiling 数据，负责异常发现、Host gap / device bubble 分析和模型结构逆向分析。
- **msmonitor**：设备资源指标采集，与 Run ID / 时间戳 / 设备 / Rank 关联。
- **MindIE Profiler**：不作为本项目必需依赖。只有在逐文件核查后确认存在 msprof / msit 未覆盖、可独立复用的解析器或分析能力时，才考虑选用。

目标链路：Run Manifest → msprof 采集 → 原始 Trace → 统一事件 Schema → Host / Device 时间线 → 算子 / 通信 / HBM 归因 → msmonitor 资源关联 → 跨轮次比较。当前链路仍在建设，不代表统一 Parser 已实现。MindIE Profiler 不作为本项目必需依赖；只有未来核查到 msprof / msit 未覆盖且可独立复用的功能，才单独评估。

## 3. MindIE Agent 组件（可选参考）

| 仓库 | 用途 | 处理策略 |
|---|---|---|
| [mindie-agent](https://github.com/mindie-agent/mindie-agent) | Agent 基础设施架构 | 参考职责边界 |
| [remote-dev](https://github.com/mindie-agent/remote-dev) | 远程 SSH / 文件 / 作业 | 评估是否需要独立复用 |
| [coordinator](https://github.com/mindie-agent/coordinator) | 资源协调 | 评估拓扑和租约机制 |
| [profiler](https://github.com/mindie-agent/profiler) | Trace 分析 | 非必需；仅在有独立增量价值时采用 |
| [debugger](https://github.com/mindie-agent/debugger) | 故障诊断 | 评估通用诊断组件 |

## 4. SGLang 官方

SGLang 主仓及 Ascend 后端是唯一框架技术事实来源。**不复制 SGLang 官方 Skills**，Codex 在 SGLang 源码工作区中可直接检索上游 Skills、源码、测试和文档；本项目只沉淀 SGLang NPU 专项知识与工作流。

## 5. 排除项

不迁移 vLLM / vLLM-Ascend / xLLM 的框架专属代码、Skill、工作流、接口和配置；不整仓复制任何参考项目。

## 6. 迁移准入

每次迁移固定源 Commit、源路径、许可证、依赖、本仓落点、修改说明和测试结果。硬件相关能力必须注明真机型号、CANN / Driver / Firmware 和测试结论。
