# Codex 安装与使用

## 推荐方式：通用 Agent Skills CLI

本项目遵循 Agent Skills 开放格式。可以直接从 GitHub 安装，不需要本项目先发布 npm 包。

前置要求：Node.js 22.20 或更高版本。

### 1. 查看仓库中可安装的 Skill

```bash
npx skills add Fighter141/sglang-npu-agent --list
```

### 2. 安装到当前项目

```bash
npx skills add Fighter141/sglang-npu-agent --skill sglang-npu-project --agent codex
```

默认安装为项目级 Skill，适合与当前项目一起提交和共享。

### 3. 安装到 Codex 全局

```bash
npx skills add Fighter141/sglang-npu-agent --skill sglang-npu-project --agent codex --global
```

全局 Skill 可在多个项目中使用。

### 4. 交互式安装

```bash
npx skills add Fighter141/sglang-npu-agent
```

按提示选择要安装的 Skill 和 Coding Agent。

### 5. 更新与卸载

```bash
npx skills check
npx skills update
npx skills remove sglang-npu-project
```

## 本仓库自带安装脚本

`scripts/install-helper.mjs` 是本地辅助脚本，主要用于调试安装目录和复制行为。当前不作为用户主入口，也未发布 npm 包。

## 当前可安装能力

目前只有 `sglang-npu-project` 项目入口 Skill，提供架构导航、开发规范、迁移来源和任务边界。模型适配、MoE 优化、Profiling 等专项 Skill 尚未实现，因此不会出现在安装列表中。

## 重要说明

- 安装 Skill 不等于安装远程执行、NPU 管理、Benchmark 或 Profiler 服务。
- 新安装后如 Codex 未立即发现 Skill，重新打开项目或启动新会话。
- 只安装本项目实际提供的 Skill；不要把路线图中的规划项当作已发布能力。
- 通用 CLI 的选项和 Node.js 版本要求以其当前文档为准。
