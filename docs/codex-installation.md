# Codex 安装与使用（无 npm 依赖）

本项目不发布 npm 包，也不要求用户安装 Node.js 或第三方 CLI。安装器仅使用 Python 标准库。

## 方式一：直接把本仓库作为 Codex 工作区

```bash
git clone https://github.com/Fighter141/sglang-npu-agent.git
cd sglang-npu-agent
codex
```

Codex 在打开项目时读取根目录 `AGENTS.md`，并从 `.agents/skills/` 发现项目内 Skill。无需额外安装步骤。

## 方式二：从本仓库选择 Skill，安装到另一个项目

先克隆本仓库：

```bash
git clone https://github.com/Fighter141/sglang-npu-agent.git
cd sglang-npu-agent
```

交互式选择并安装到当前项目：

```bash
python3 scripts/install.py install
```

安装指定 Skill：

```bash
python3 scripts/install.py install sglang-npu-project --target /path/to/target-project
```

安装到 Codex 全局目录：

```bash
python3 scripts/install.py install sglang-npu-project --global
```

## 管理 Skill

```bash
python3 scripts/install.py list
python3 scripts/install.py status --target /path/to/target-project
python3 scripts/install.py doctor
python3 scripts/install.py uninstall sglang-npu-project --target /path/to/target-project
```

覆盖已安装版本可增加 `--force`。

## 安装路径

- 项目级：`<目标项目>/.agents/skills/<skill-name>/`
- 全局：`~/.agents/skills/<skill-name>/`

## 当前可安装内容

目前只有 `sglang-npu-project` 项目入口 Skill。其他专项 Skill 会在内容、输入输出、失败分支和验证方式完成后逐个加入，不创建空壳 Skill。

## 注意

- 安装 Skill 只安装工作流指引，不会自动安装远程执行、NPU 管理、Benchmark 或 Profiler 服务。
- 安装后如 Codex 未立即发现 Skill，重新打开项目或启动新会话。
- 安装器不访问网络、不下载依赖、不使用 npm。
