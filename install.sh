#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/Fighter141/sglang-npu-agent.git"
DEST="${1:-$HOME/.local/share/sglang-npu-agent}"

if ! command -v git >/dev/null 2>&1; then
  echo "错误：需要先安装 Git。" >&2
  exit 1
fi
if [[ -e "$DEST" ]]; then
  echo "目标目录已存在：$DEST" >&2
  echo "请指定其他目录，或自行更新现有检出。" >&2
  exit 1
fi

mkdir -p "$(dirname "$DEST")"
git clone "$REPO_URL" "$DEST"
cd "$DEST"

echo
echo "SGLang NPU Agent 已检出到：$DEST"
echo "Codex 项目级 Skill 可通过以下命令安装："
echo "  node scripts/install-helper.mjs list"
echo "  node scripts/install-helper.mjs install sglang-npu-project --target /path/to/your/project"
echo
echo "注意：当前安装器尚未发布到 npm；此脚本只负责获取仓库，不会自动安装未实现的专项能力。"
