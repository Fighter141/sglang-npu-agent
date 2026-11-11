# AGENTS.md — SGLang NPU Agent 项目级规范

本文件约束在本仓库中工作的 Codex、Claude Code、Cursor 等 Coding Agent。

## 项目定位

本仓库用于建设面向昇腾 NPU 的 SGLang 智能研发工作区。当前处于架构与工程骨架阶段；不得把路线图中的规划能力描述为已经实现。

## 目录职责

- `plugins/`：用户任务入口、路由、端到端流程和阶段门禁。
- `agents/`：可选的专业角色定义、委派边界和交接契约。
- `skills/`：可复用操作规程、判断逻辑和工具组合。
- `services/`：SSH、后台作业、NPU 资源、Serving、Benchmark、Profiler 等确定性执行能力。
- `knowledge/`：有来源、有适用条件、有证据等级的知识卡。
- `reference/`：稳定 Schema、接口契约、Workload 与产物模板。
- `runs/`：本地实验运行记录，默认 Git 忽略。
- `tests/`：目录、Schema、脚本、路由和工作流测试。

不得把远程执行、设备锁、进程监管、Benchmark 或 Profiler 解析仅写成提示词。

## 工程约束

1. 修改前先读目标文件、相关 Skill、架构契约和上游实现。
2. 优先做最小、可验证的修改；不要为单次需求引入不必要抽象。
3. 不提交密码、Token、私有主机名、内网 IP、私有模型路径或未脱敏日志。
4. 不虚构性能数据、兼容性结论、硬件能力或上游行为。
5. 每个外部技术结论记录来源 URL、仓库、Commit / Tag、适用版本及核验日期。
6. 性能优化必须先建立预热后的 Baseline；正确性修复必须先保留稳定复现用例。
7. Profiling 是诊断证据，不能替代非 Profiling 的性能验收数据。
8. 保留失败实验和负面结果，不只保留最优结果。
9. 对进程终止、环境替换、资源释放和昂贵多机任务设置明确授权门槛。
10. 适配代码与知识卡必须遵循各自上游许可证及署名要求。

## 强制优化闭环

调研 → 基线 → 诊断 → 方案 → 修改 → 正确性验证 → 性能评测 → Review → 记录。

性能结论必须有可比的 Baseline 与 Candidate 数据，并固定模型、Tokenizer、数据类型、硬件、软件环境、Workload 和 SLA。每次测量记录预热次数、重复次数、并发、请求数及原始产物。

## 实验证据

每次实验记录 SGLang 与 Ascend 后端 Commit、CANN / Driver / Firmware / PyTorch / torch_npu 版本、设备型号与拓扑、容器镜像 Digest、模型 Revision、Workload、启动命令、生效配置、Warmup、测量次数、TTFT、TPOT、吞吐、显存、正确性结果和原始产物。

## 知识可信度

区分 `upstream_documented`、`hardware_spec`、`reproduced_empirical`、`single_observation`、`hypothesis`。保留适用条件、失效边界、来源和最后核验日期。失败路径也应记录。

## 迁移与交付

迁移前查看 `docs/source-migration-map.md`。该表是来源登记入口，不替代逐文件许可证检查。不得把某项目的目录名或能力描述当成已经获得其实现代码。优先复用标准、Schema 和可独立验证的工具接口；框架耦合逻辑必须针对 SGLang 重写和测试。

新增 Skill 应包含 `SKILL.md`、适用 / 不适用条件、输入输出、失败分支和验证标准；新增 Service 应定义输入输出、超时、取消、退出状态、幂等性和安全边界。任何未在目标昇腾设备验证的能力，必须明确标注“未真机验证”。
