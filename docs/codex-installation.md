# Codex 安装与使用（无 npm 依赖）

本项目不发布 npm 包，也不要求用户安装 Node.js 或第三方 CLI。安装器要求 Python 3.9+，仅使用 Python 标准库。

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

交互式选择并安装到另一个项目：

```bash
python3 scripts/install.py install --target /path/to/target-project
```

安装指定 Skill：

```bash
python3 scripts/install.py install sglang-npu-project --target /path/to/target-project
```

安装全部 11 个 Skill：

```bash
python3 scripts/install.py install --all --target /path/to/target-project
```

省略 `--target` 时目标是当前工作目录。源码仓库自身已经包含 Skills，不需要重复安装；普通安装会保留原目录，`--force` 自覆盖及卸载源码都会被拒绝。非交互环境必须指定 Skill 名称或 `--all`；交互时回车可取消。

安装到 Codex 全局目录：

```bash
python3 scripts/install.py install sglang-npu-project --global
```

## 管理 Skill

```bash
python3 scripts/install.py list
python3 scripts/install.py status --target /path/to/target-project
python3 scripts/install.py doctor --target /path/to/target-project
python3 scripts/install.py uninstall sglang-npu-project --target /path/to/target-project
python3 scripts/install.py uninstall --all --target /path/to/target-project
```

覆盖已安装版本可增加 `--force`。它会替换该 Skill 的本地修改，请先保存需要保留的内容。安装器先在目标目录内准备完整副本，再替换旧版本；复制失败保留旧版本，替换失败尝试恢复。恢复本身失败时，错误信息会给出旧版本备份路径。一次安装多个 Skill 按 Skill 依次完成，不提供整批事务或并发安装保证。

安装成功会在 Skill 目录内写入 `.sglang-npu-agent-install.json` 来源记录。`status` 区分本安装器管理和未托管目录；`uninstall --all` 仅删除有匹配来源记录的安装，保留其他项目及旧版未标记的 Skills。指定名称卸载也要求来源匹配。

旧版安装没有来源记录。如需升级并交由本安装器管理，先备份该 Skill 的本地修改，再执行：

```bash
python3 scripts/install.py install sglang-npu-project --force --target /path/to/target-project
```

Skill 名称不接受绝对路径或 `../`；源文件、`.agents`、`skills` 或目标 Skill 中用于越界的符号链接会被拒绝。`--global` 与 `--target` 不能同时使用。

## 安装路径

- 项目级：`<目标项目>/.agents/skills/<skill-name>/`
- 全局：`~/.agents/skills/<skill-name>/`

## 当前可安装内容

当前有 11 个 Skill，覆盖项目入口、模型适配、Serving 配置、性能优化、Benchmark、Profiling、排障、代码审查、MoE、Graph / MTP 和算子开发。完整清单见 [Skills 能力目录](../skills/README.md)，实际安装清单以 `list` 输出为准。

入口 Skill 的配套资料位于安装目录下的 `sglang-npu-project/references/project/`，保留原文档的相对目录结构，包含规范、知识库、实验模板及许可证。不会把本项目的 `AGENTS.md` 写到目标工作区根目录。其他专项 Skill 当前自包含工作流指南及公开来源链接。

## 检查与测试

`doctor` 检查源 Skill、配套资料、安装目录边界和已托管入口 Skill 的资料完整性。它不检查 Codex 是否实际发现 Skill、NPU 软件栈或执行服务，也不代表真机验证通过。

```bash
python3 -m unittest discover -s tests -v
```

测试使用隔离临时目录，包括全局安装路径的替身，不修改真实全局 Skills、不访问网络、不启动 NPU。覆盖安装、卸载、来源判定、资料独立性、路径边界、复制失败与恢复。GitHub Actions 使用 Python 3.9 和 3.12 执行同一套测试。

退出码：`0` 表示命令成功（包括保留已有安装或用户取消），`1` 表示文件检查或执行失败，`2` 表示命令行参数错误。未知 Skill 不再静默成功。

## 注意

- 安装 Skill 只安装工作流指引，不会自动安装远程执行、NPU 管理、Benchmark 或 Profiler 服务。
- 安装后如 Codex 未立即发现 Skill，重新打开项目或启动新会话。
- 安装器不访问网络、不下载依赖、不使用 npm。
