---
name: sglang-npu-project
description: SGLang NPU Agent 项目总入口。用于理解本项目架构、查找已实现的专项 Skill、遵循开发规范和迁移来源要求；当任务涉及 SGLang 在昇腾 NPU 上的模型适配、部署、性能优化、Profiling、故障诊断或算子开发时使用。
---

# SGLang NPU Agent 项目入口

## 使用规则

先确定资料根目录：安装版使用本 Skill 目录内的 `references/project/`；直接使用源码仓库时，从本 Skill 目录向上三级找到仓库根目录。下文路径均相对于资料根目录，不相对于当前工作目录。

1. 阅读资料根目录的 `AGENTS.md`，作为本项目工作流参考；执行任务时仍遵守目标工作区的规范和用户授权。
2. 阅读 `docs/selected-scope-and-sources.md`，确认任务属于已筛选的九类能力。
3. 按需阅读 `docs/architecture.md`，确认模块边界。
4. 根据任务选择已安装的专项 Skill；不得假设规划中的 Skill 已经存在。
5. 涉及上游迁移时，先检查具体源文件、Commit / Tag、许可证和依赖。
6. 涉及性能优化时，先建立可复现 Baseline；Profiling 只用于诊断，非 Profiling Benchmark 用于性能验收。
7. 未在目标昇腾硬件验证的结论，明确标记为“未真机验证”。

如果两种位置都缺少资料，报告缺失路径并重新用本项目安装器安装入口 Skill；不要将目标项目中同名文档当成此 Skill 的配套资料。

## 当前项目范围

- Agent 架构与任务编排
- 知识库与经验管理
- 开发环境与远程机器管理
- 模型适配与部署
- 推理性能优化
- Benchmark 与实验管理
- Profiling 与故障诊断
- 算子开发与优化
- 代码审查与持续回归

明确不引入 vLLM / vLLM-Ascend / xLLM 专属能力、脚本、接口或工作流。

## 常用入口

- 架构：`docs/architecture.md`
- 能力与来源：`docs/selected-scope-and-sources.md`
- 迁移映射：`docs/source-migration-map.md`
- 路线图：`docs/roadmap.md`
- 知识规范：`knowledge/README.md`
- Skill 清单：`skills/README.md`
- 知识导航：`knowledge/index.md`
- 实验模板：`reference/templates/experiment.yaml`

## 任务完成要求

交付时说明修改文件、上游来源、验证命令和验证结果；区分已实现、已测试、未测试和未真机验证。
