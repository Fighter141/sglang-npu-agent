---
name: sglang-model-bringup
description: 在昇腾 NPU 上为 SGLang 分析、适配和验证新模型。适用于模型尚未支持、加载失败、算子或 Attention 后端不兼容、精度异常及模型接入评审。
---

# SGLang NPU 模型适配与 Bring-up

## 目标

以 SGLang 上游模型接入机制和 Ascend 后端实际实现为准，完成模型支持缺口分析、最小适配、正确性验证和可复现交付。不得照搬其他推理框架的模型适配实现。

## 输入

- 模型仓库、Revision、配置文件和权重格式；
- 目标设备型号、卡数及拓扑；
- SGLang / Ascend 后端 Commit；
- CANN、Driver、Firmware、PyTorch、torch_npu 版本；
- 目标 Workload、dtype、量化方式和服务参数。

## 工作流程

1. **盘点环境**：记录代码 Commit、软件栈、设备拓扑、容器镜像和模型 Revision。缺失信息明确列为待确认项。
2. **确认模型结构**：读取 config、architectures、hidden size、层数、Attention 类型、MoE / MLA / 多模态结构、Tokenizer 和权重索引。
3. **检查 SGLang 支持**：检索 SGLang Models Directory、Model Registry、加载器、对应单元测试和 Ascend NPU 模型支持清单；先判断是否已支持，不重复造轮子。
4. **定位最小缺口**：区分模型定义、权重映射、算子、Attention、MoE、量化、Tokenizer、Runtime 和 Ascend 后端问题。给出具体源文件与调用链。
5. **设计适配方案**：优先复用 SGLang 已有接口；明确需要修改的文件、风险、兼容版本和回退方案。
6. **实现与静态检查**：遵循 SGLang 代码风格、注册机制和测试规范；不引入无关框架抽象。
7. **正确性验证**：先跑 CPU / NPU 可用的最小测试，再跑目标 NPU；与可信参考输出比较 logits / token、数值误差和生成行为。
8. **服务验证**：完成权重加载、启动、健康检查、短请求和目标 Workload Smoke Test。
9. **交付**：记录支持范围、限制、修改文件、测试命令、环境、原始日志和未验证项。

## 失败分支

- 权重加载失败：先核对 shard 索引、键名映射、dtype、量化元数据和加载器路径。
- 算子缺失：确认实际调用点及 Ascend kernel 是否存在，不以 CUDA 实现存在推断 NPU 可用。
- 精度异常：构造最小输入，逐层比较中间结果，区分权重、算子、dtype 和并行归约误差。
- 服务可启动但输出异常：检查 tokenizer、chat template、sampling、模型配置和后端路径。

## 验收标准

- 模型与软件版本可追溯；
- 最小正确性测试通过；
- 目标 NPU 服务 Smoke Test 通过；
- 适用硬件、dtype、量化和限制明确；
- 未完成真机验证的部分明确标记。

## 来源

- SGLang 模型接入指南：https://github.com/sgl-project/sglang/blob/main/docs/docs/supported-models/support_new_models.mdx
- SGLang Ascend 模型适配指南：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/development/support_new_models.mdx
- Ascend 支持模型清单：https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/reference/support_models.mdx
- CANNBot Skills：模型迁移类流程参考（具体 Skill 需逐项核查）：https://gitcode.com/cann/cannbot-skills

## 输出产物

模型支持差距报告、适配计划、代码变更清单、正确性结果、服务 Smoke Test 记录和知识候选卡。
