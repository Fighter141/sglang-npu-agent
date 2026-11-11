# 总体架构与模块边界

## 架构决策

采用 **CANNBot 的 Plugin / Agent / Skill 作为任务组织模型**，但不直接复制其面向 CANN 通用开发的全部实现。知识治理参考 CANNBot Knowledge；实验闭环参考 xLLM Workflow；多仓与远程开发工作区参考 VAWS；远程执行、资源协调和观测工具的职责拆分参考 MindIE Agent。

核心原则：**Agent 负责理解与决策，Skill 负责流程与判断，Service 负责确定性执行，Knowledge 负责可追溯经验。**

## 六个逻辑层

| 层 | 职责 | 不负责 |
|---|---|---|
| Plugin / Workflow | 用户任务入口、路由、编排、阶段门禁 | SSH、设备锁、Profiler 底层解析 |
| Agent | 专业角色分工、任务委派、结果审阅 | 维护隐式基础设施状态 |
| Skill | 操作规程、决策树、工具组合、失败分支 | 长时间进程监管、资源锁 |
| Service | 远程执行、资源租约、Serving、Benchmark、Profiler、实验存储 | 自然语言任务理解 |
| Knowledge | 领域事实、SOP、Workflow、故障与优化经验 | 无证据结论 |
| Reference / Schema | 稳定接口、实验清单、产物格式和机器契约 | 临时实验观察 |

Agent 层不是第一阶段的硬性依赖。先用单 Agent + Workflow + Skills + Services 跑通闭环，再根据任务并行度和独立审查需求引入多 Agent。

## 核心任务工作流

### 模型适配 / Bring-up
模型结构与配置检查 → SGLang 支持缺口分析 → 权重与 Tokenizer 检查 → 后端算子 / Attention / MoE 适配 → 精度验证 → NPU 服务 Smoke Test → 适配报告。

### 推理服务配置
硬件拓扑探测 → 版本兼容检查 → TP / DP / EP / PP 等并行策略 → Attention Backend / Graph / FIA → KV Cache 与显存预算 → MTP / Speculative Decoding 兼容性 → 生效配置采集 → 服务验证。

### 性能优化
固定 SLA 与 Workload → 预热 Baseline → 分析 TTFT / TPOT / 吞吐 / HBM / 通信 → Profiler 定位 → 候选收益与风险排序 → 单变量修改 → 正确性验证 → 非 Profiling A/B → 消融 → 记录结论。

### 故障诊断
稳定复现 → 收集版本、日志和拓扑 → 分类为模型 / 算子 / Runtime / Graph / HCCL / 内存 / 调度 → 最小化定位 → 修复 → 正确性与性能回归 → 形成知识卡。

### PR 与版本回归
上游变更追踪 → 影响模块识别 → 兼容性检查 → 目标硬件构建 → 正确性测试 → 性能回归 → 变更与证据报告。

## 基础服务边界

- `remote-dev`：SSH、远端文件读写、代码同步、容器命令、后台任务和日志读取。迁移参考：MindIE Agent `remote-dev`、VAWS 远程工具。
- `npu-coordinator`：机器 / 容器台账、设备拓扑、NPU 与端口租约。迁移参考：MindIE Agent `coordinator`。
- `serving-manager`：服务启动、健康检查、Smoke Test、停止与清理。迁移参考：VAWS Serving Skill，需改为 SGLang。
- `benchmark`：Workload、预热、重复测量、指标归一化和结果保存。迁移参考：VAWS Benchmark、xLLM Workflow Benchmark。
- `profiler`：msprof / torch profiler 采集、解析、关联和跨轮次对比。迁移参考：VAWS Profiling、MindIE Agent Profiler。
- `experiment-store`：Run Manifest、Attempt Ledger、配置快照、产物索引和经验晋升。迁移参考：xLLM Workflow Lifecycle。
- `git-ci`：Worktree、上游同步、PR 检查和回归门禁。迁移参考：VAWS Workspace。

以上是目标接口边界，不代表服务当前已经实现。优先封装成熟 CLI / SDK，不为每个工具重新造轮子。

## 知识体系

参考 CANNBot Knowledge 的 OKF v0.2 文件化 Knowledge Bundle：Markdown + YAML Frontmatter、目录和 `index.md` 渐进导航、Git 版本审计。正式落地前必须核对其 Schema、Profile、Contract 和安装脚本；当前仓库尚未宣称通过 OKF 一致性检查。

建议知识分为硬件 / 软件约束、API / 算子 / 框架接口、模型适配 / 部署 / 排障 SOP、经验证的代码变换和优化经验。证据等级与知识类别分离。

## 实验与性能证据

采用 xLLM Workflow 的 Run / Attempt / Checkpoint / Finalize 思路，但将执行器适配为 SGLang。每次实验有唯一 Run ID；每个候选修改是独立 Attempt；保留环境快照、原始日志、Benchmark、正确性和 Profiler 产物。性能验收使用非 Profiling 数据。

## 部署策略

第一阶段以本地 CLI / Coding Agent + SSH 远程执行为主。服务接口保持传输层无关，后续需要时再提供 MCP 或 Web UI。不要在单 Agent 工作流和确定性服务尚未跑通前，先开发复杂多 Agent Runtime、任务调度平台或 Web 控制台。

详细来源与迁移路径见 [迁移来源映射表](source-migration-map.md)。
