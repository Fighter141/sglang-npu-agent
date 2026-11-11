# Codex 安装与使用

本项目采用 CANNBot Skills 类似的“安装器 + Agent Skills 开放标准”模式，但当前仅实现仓库内 Skill 的项目级 / 全局复制安装。

## 1. 获取项目

```bash
git clone https://github.com/Fighter141/sglang-npu-agent.git
cd sglang-npu-agent
```

## 2. 查看可安装 Skill

```bash
node scripts/install-helper.mjs list
```

当前仅包含 `sglang-npu-project` 项目入口 Skill。模型适配、MoE、Profiling 等专项 Skill 尚未实现，不会作为空壳发布。

## 3. 安装到当前项目（推荐）

在目标 SGLang 项目根目录执行：

```bash
node /path/to/sglang-npu-agent/scripts/install-helper.mjs install sglang-npu-project --target .
```

安装位置：`.agents/skills/sglang-npu-project/`。

也可以在本仓库根目录直接执行：

```bash
node scripts/install-helper.mjs install sglang-npu-project
```

## 4. 安装到 Codex 全局

```bash
node scripts/install-helper.mjs install sglang-npu-project --level global
```

安装位置：`~/.agents/skills/sglang-npu-project/`。

## 5. 管理

```bash
node scripts/install-helper.mjs list
node scripts/install-helper.mjs status
node scripts/install-helper.mjs doctor
node scripts/install-helper.mjs uninstall sglang-npu-project
``

覆盖更新可加 `--force`。卸载只删除目标 Skill 目录，不修改其他项目文件。

## 6. 与 npx skills 兼容

每个 Skill 遵循 Agent Skills 格式，后续可使用通用 `skills` CLI 安装单项能力。安装路径与工具选择以该 CLI 当前版本为准。

## 7. 当前限制

- 本仓库尚未发布 npm 包，因此暂不能使用 `npx @...` 形式运行本项目安装器。
- 当前安装器只负责复制 Skill 文件，不安装 MCP Server、远程执行环境或 CANN 依赖。
- Codex 通常需要新开会话或刷新 Skill 列表后识别新安装的 Skill。
- 项目级 Skill 放在目标项目的 `.agents/skills/`；全局 Skill 放在 `~/.agents/skills/`。
