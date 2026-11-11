# 建设路线图

状态：Skills 第一批已建立工作流指南；确定性执行服务、自动化脚本和目标硬件验证仍待建设。

## P0：让 Skill 可安装、可执行、可验证

- [x] Codex Agent Skills 目录与项目入口 Skill。
- [x] Python 标准库安装器自动发现 Skill。
- [x] 第一批专项 Skill：模型适配、Serving、性能优化、Benchmark、Profiling、故障诊断、代码审查、MoE、Graph / MTP、算子开发。
- [ ] 安装器单元测试：项目级 / 全局、覆盖、卸载、空目录和路径边界。
- [ ] 在实际 Codex 环境验证 Skill 发现与调用。
- [ ] 每个专项 Skill 增加来源核查记录、参考资料和适用版本。
- [ ] 版本与仓库探测：SGLang、Ascend 后端、CANN、Driver、Firmware、PyTorch、torch_npu。
- [ ] 远程主机 / 容器安全命令执行与 NPU 拓扑 / 资源管理。
- [ ] SGLang 服务启动、健康检查、Smoke Test、停止和清理。
- [ ] SGLang Benchmark、正确性验证、msprof 采集和实验归档。

## P1：SGLang NPU 专项自动化

- [ ] 模型 Bring-up 自动化检查和支持缺口报告。
- [ ] 服务配置参数解析、兼容性校验和生效配置采集。
- [ ] TP / DP / EP / PP / DCP 并行策略分析。
- [ ] MoE 通信后端、FuseEP / DeepEP 等模式对比。
- [ ] Attention Backend、Graph / FIA 兼容性检查。
- [ ] MTP / Speculative Decoding 收益与负优化判定。
- [ ] PD 分离、Prefill / Decode 性能分析。
- [ ] AscendC / Triton-Ascend 算子测试与性能回归。

## P2：知识治理与持续回归

- [ ] 核查并引入 CANNBot Knowledge 的 Schema / Profile / Lint / Query / Ingest。
- [ ] 建立 SGLang 专属知识检索回归集。
- [ ] 实验记录到候选经验卡的提炼与人工审核。
- [ ] SGLang / Ascend 后端 PR 影响分析与兼容性矩阵。
- [ ] 跨版本、跨芯片正确性和性能回归。
- [ ] 有预算、有边界的配置候选生成与自动调优。

## 验收原则

Skill 文档已建立不等于对应自动化工具已实现。每项能力分别标注文档工作流、脚本实现、集成测试和真机验证状态。性能优化必须包含固定环境 Baseline、正确性结果、非 Profiling 性能测量和原始产物。未经真机复现的内容不得标记为已验证。
