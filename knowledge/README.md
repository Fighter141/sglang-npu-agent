# 工程知识库

本目录用于保存可追溯、可检索、带适用条件和验证状态的 SGLang NPU 工程知识。

## 设计参考

优先研究并迁移 [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge) 的 OKF v0.2 文件化知识 Bundle、YAML Frontmatter、渐进式 `index.md` 导航、来源治理、Schema / Contract、Ingest / Query / Lint 和检索评测机制。

**当前目录尚未宣称通过 CANNBot Knowledge 的 Schema 或 OKF 一致性检查。** 正式引入前，先固定上游版本，核查许可证、Profile、Schema、Contract、Skill 和测试，再决定直接依赖、复制适配或独立实现。

## 建议分类

- `hardware/`：设备拓扑、显存、片上存储、通信与硬件约束。
- `software/`：CANN、Driver、Firmware、PyTorch、torch_npu、Triton-Ascend 版本与兼容性。
- `sglang/`：SGLang 架构、Ascend 后端、参数、Attention、Graph、调度和 KV Cache。
- `operators/`：算子 API、DSL、实现、精度、性能与限制。
- `models/`：模型适配、权重、Tokenizer、量化与服务配置。
- `workflows/`：Bring-up、部署、Benchmark、Profiling 和排障 SOP。
- `lessons/`：经过验证的优化经验、负面结果和失效边界。

## 知识卡最低元数据

每张卡至少声明唯一 ID、标题、知识类别、适用芯片、软件版本、框架 / 模型范围、来源、证据等级、验证状态、失效边界和最后核验日期。具体字段以迁移并验证后的 Schema 为准。

## 证据等级

- `upstream_documented`：上游文档或代码明确说明。
- `hardware_spec`：可追溯的硬件规格。
- `reproduced_empirical`：在记录的环境和 Workload 下复现。
- `single_observation`：单次观测，不能直接泛化。
- `hypothesis`：待验证假设。

## 治理流程

来源登记 → Ingest 生成候选卡 → Schema / Lint → 人工 Review → 检索与引用检查 → 合并 → 定期复核。实验自动提炼的知识只能作为候选，不能绕过审核直接成为已验证结论。
