# 建设路线图

状态：规划中。只有完成实现并在声明的软硬件环境验证后，才能将任务标记为完成。

## P0：可信的工程执行与证据闭环

- [ ] SGLang / Ascend 后端 / CANN / Driver / Firmware / PyTorch / torch_npu 版本探测。
- [ ] 远程主机 / 容器清单与安全命令执行（参考 MindIE Agent remote-dev）。
- [ ] NPU 拓扑探测、设备占用检查和资源租约（参考 MindIE Agent coordinator）。
- [ ] SGLang 服务启动、健康检查、Smoke Test、停止和清理。
- [ ] SGLang Benchmark Workload、预热、重复测量和结果归档。
- [ ] 正确性 Smoke Test 与结果归档。
- [ ] msprof 采集、解析和跨轮次对比（参考 MindIE Agent Profiler、CANN 官方工具）。
- [ ] Baseline / Candidate 公平性检查、实验记录和性能回归。
- [ ] Skill 路由、知识 Schema、脚本和工作流测试。

## P1：SGLang NPU 专项能力

- [ ] 模型 Bring-up、支持缺口分析和适配报告。
- [ ] 服务配置生成、参数校验和生效配置快照。
- [ ] TP / DP / EP / PP / DCP 等并行策略分析。
- [ ] MoE 通信后端、FuseEP / DeepEP 等模式对比。
- [ ] Attention Backend、Graph / FIA 兼容性检查。
- [ ] MTP / Speculative Decoding 收益与负优化判定。
- [ ] PD 分离、Prefill / Decode 性能分析。
- [ ] HBM、KV Cache、容量与并发规划。
- [ ] AscendC / Triton-Ascend 算子开发、正确性和性能验证。

## P2：知识治理与持续回归

- [ ] 核查并引入 CANNBot Knowledge 的 Schema / Profile / Lint / Query / Ingest。
- [ ] 建立 SGLang 专属知识检索回归集。
- [ ] 实验记录到候选经验卡的提炼与人工审核。
- [ ] SGLang / Ascend 后端 PR 影响分析与兼容性矩阵。
- [ ] 跨版本、跨芯片正确性和性能回归。
- [ ] 有预算、有边界的配置候选生成与自动调优。

## 验收原则

每个工作流必须定义输入、输出、前置条件、失败分支、资源清理、安全门禁和验证证据。性能优化必须包含固定环境的 Baseline、候选版本、正确性结果、非 Profiling 性能测量和原始产物。知识卡必须标明来源、适用条件和证据等级。未经真机复现的内容不得标记为已验证。
