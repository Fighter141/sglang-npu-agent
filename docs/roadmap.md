# 建设路线图

状态：规划中。只有完成代码实现并在声明的软硬件环境验证后，才能将任务标记为完成。

## P0：先跑通可信的工程闭环

- [ ] 版本与仓库探测：SGLang、Ascend 后端、CANN、Driver、Firmware、PyTorch、torch_npu。
- [ ] 远程主机 / 容器清单与安全命令执行（参考 MindIE Agent remote-dev、VAWS）。
- [ ] NPU 拓扑探测、设备占用检查和资源租约（参考 MindIE Agent coordinator）。
- [ ] SGLang 服务生命周期：启动、健康检查、Smoke Test、停止、清理（参考 VAWS Serving）。
- [ ] Benchmark Workload / Run Manifest / Attempt Ledger（参考 xLLM Workflow）。
- [ ] 正确性 Smoke Test 与结果归档。
- [ ] msprof 采集、解析、跨轮次对比接口（参考 VAWS、MindIE Agent Profiler）。
- [ ] Baseline / Candidate 公平性检查与性能回归报告。
- [ ] Skill 路由、Schema、脚本和工作流测试。

## P1：SGLang NPU 专项能力

- [ ] 模型 Bring-up、模型支持缺口和适配报告（参考 CANNBot 模型迁移 Skill，按 SGLang 重写）。
- [ ] 服务配置生成、参数校验、生效配置快照。
- [ ] TP / DP / EP / PP / DCP 等并行策略分析。
- [ ] MoE 通信后端、FuseEP / DeepEP 等模式对比。
- [ ] Attention Backend、Graph / FIA 兼容性检查。
- [ ] MTP / Speculative Decoding 收益与负优化判定。
- [ ] PD 分离、Prefill / Decode 性能分析。
- [ ] HBM、KV Cache、容量与并发规划。

## P2：自动化与知识飞轮

- [ ] 迁移 CANNBot Knowledge 的 Schema / Profile / Lint / Query / Ingest，并建立 SGLang 检索回归集。
- [ ] 实验记录到候选经验卡的自动提炼与人工审核。
- [ ] 多任务 Git Worktree 隔离（参考 VAWS）。
- [ ] 有预算、有边界的参数候选生成与自动调优（参考 xLLM Workflow 优化闭环）。
- [ ] 跨版本、跨芯片回归追踪。
- [ ] 在确有收益时引入多 Agent 并行调查。

## 里程碑验收原则

每个工作流必须定义输入、输出、前置条件、失败分支、资源清理、安全门禁和验证证据。不能只以“Agent 能生成命令”作为完成标准。

性能优化必须包含固定环境的 Baseline、候选版本、正确性结果、非 Profiling 性能测量和原始产物。知识卡必须经过 Schema / Lint 检查并标明来源、适用条件和证据等级。未经真机复现的内容不得标记为已验证。
