# SGLang NPU Knowledge Base

本目录不是空的文档占位区，而是项目可持续积累的工程知识库。知识按主题组织，所有条目必须保留来源、适用版本、证据等级和验证状态。

## 知识导航

| 分类 | 内容 | 入口 |
|---|---|---|
| 硬件 | 910C、A3、Die / Rank / HCCS / HBM 等拓扑与约束 | [hardware/index.md](hardware/index.md) |
| 软件栈 | CANN、Driver、Firmware、PyTorch、torch_npu、SGLang 版本关系 | [software/index.md](software/index.md) |
| SGLang | Ascend 后端架构、模型接入、Serving、MoE、Graph / MTP | [sglang/index.md](sglang/index.md) |
| Profiling | msprof、MindIE Profiler、msit、msmonitor 的职责与工作流 | [profiling/index.md](profiling/index.md) |
| 精度诊断 | msprobe、逐层对比、算子误差定位 | [accuracy/index.md](accuracy/index.md) |
| 算子 | AscendC、Triton-Ascend、算子开发与测试 | [operators/index.md](operators/index.md) |
| 工作流 | Bring-up、部署、Benchmark、排障 SOP | [workflows/index.md](workflows/index.md) |
| 来源登记 | Source 仓库、版本、迁移状态与许可证核查 | [sources/index.md](sources/index.md) |

## 证据等级

- `upstream_documented`：上游文档或源码明确说明。
- `hardware_spec`：官方硬件规格。
- `reproduced_empirical`：记录了环境和 Workload 的复现实验。
- `single_observation`：单次观测，不能泛化。
- `hypothesis`：待验证假设。

## 知识卡规范

每张知识卡需写明：适用范围、结论、操作 / 判断流程、来源链接、来源版本或核验日期、证据等级、验证状态、限制和后续待核实项。没有证据时不得把经验包装成事实。

## 更新规则

新资料先登记为候选知识，再经过来源核查、版本标注和 Review。性能数据必须同时保留原始数据、配置、源码 Commit 和测试环境。不得把规划中的能力写成已实现。
