# 工程知识库

本目录用于保存可追溯、可检索、带适用条件和验证状态的 SGLang NPU 工程知识。

## 设计来源

主要参考 [CANNBot Knowledge](https://gitcode.com/cann/cannbot-knowledge)，重点核查其 OKF / Knowledge Bundle、YAML Frontmatter、渐进式索引、来源治理、Schema / Profile / Contract、Ingest / Query / Lint 和检索评测。

当前仓库尚未宣称通过 CANNBot Knowledge 的 Schema 或 OKF 一致性检查。正式引入前，固定上游版本，核查许可证、Schema、Profile、Contract、Skill 和测试，再决定直接依赖、适配或独立实现。

## 知识分类

- hardware：设备拓扑、显存、片上存储、通信与硬件约束。
- software：CANN、Driver、Firmware、PyTorch、torch_npu、Triton-Ascend 版本与兼容性。
- sglang：SGLang 架构、Ascend 后端、参数、Attention、Graph、调度和 KV Cache。
- operators：算子 API、DSL、实现、精度、性能与限制。
- models：模型适配、权重、Tokenizer、量化与服务配置。
- workflows：Bring-up、部署、Benchmark、Profiling 和排障 SOP。
- lessons：经过验证的优化经验、负面结果和失效边界。

## 知识可信度

区分 upstream_documented、hardware_spec、reproduced_empirical、single_observation、hypothesis。知识类别描述内容用途，证据等级描述可信度，两者不能混为一谈。

## 治理流程

来源登记 → Ingest 生成候选卡 → Schema / Lint → 人工 Review → 检索与引用检查 → 合并 → 定期复核。实验自动提炼的知识只能作为候选，不能绕过审核直接成为已验证结论。
