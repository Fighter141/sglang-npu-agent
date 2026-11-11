#!/usr/bin/env python3
"""SGLang NPU Agent Skill installer. Python standard library only."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills"
GLOBAL_TARGET = Path.home() / ".agents" / "skills"


def available_skills() -> list[Path]:
    if not SOURCE.exists():
        return []
    return sorted(p.parent for p in SOURCE.glob("*/SKILL.md"))


def installed_skills(target: Path) -> list[Path]:
    if not target.exists():
        return []
    return sorted(p.parent for p in target.glob("*/SKILL.md"))


def choose_interactively(skills: list[Path]) -> list[Path]:
    if not skills:
        print("当前没有可安装的 Skill。")
        return []
    print("可安装的 SGLang NPU Skills：")
    for i, skill in enumerate(skills, 1):
        print(f"  {i}. {skill.name}")
    raw = input("输入序号（多个用逗号分隔，输入 all 全选，直接回车取消）：").strip()
    if not raw:
        return []
    if raw.lower() == "all":
        return skills
    selected = []
    for token in raw.split(","):
        try:
            idx = int(token.strip()) - 1
            if 0 <= idx < len(skills):
                selected.append(skills[idx])
            else:
                print(f"忽略无效序号：{token}")
        except ValueError:
            print(f"忽略无效输入：{token}")
    return list(dict.fromkeys(selected))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从本地 SGLang NPU Agent 仓库选择并安装 Codex Skills（无需 npm）。"
    )
    parser.add_argument("command", nargs="?", choices=["list", "install", "uninstall", "status", "doctor"], default="install")
    parser.add_argument("skills", nargs="*", help="Skill 名称；install/uninstall 支持 --all")
    parser.add_argument("--global", dest="global_install", action="store_true", help="安装到 ~/.agents/skills/")
    parser.add_argument("--target", default=".", help="项目级安装目标目录，默认为当前目录")
    parser.add_argument("--all", action="store_true", help="安装或卸载全部已存在的 Skill")
    parser.add_argument("--force", action="store_true", help="覆盖已存在的同名 Skill")
    args = parser.parse_args()

    available = available_skills()
    target = GLOBAL_TARGET if args.global_install else Path(args.target).expanduser().resolve() / ".agents" / "skills"

    if args.command == "list":
        if not available:
            print("当前没有可安装的 Skill。")
        for skill in available:
            print(skill.name)
        return 0

    if args.command == "doctor":
        print(f"Python：{sys.version.split()[0]}")
        print(f"Skill 源目录：{'存在' if SOURCE.is_dir() else '缺失'} ({SOURCE})")
        print(f"安装目标：{target}")
        print(f"可安装 Skill 数：{len(available)}")
        return 0 if SOURCE.is_dir() else 1

    if args.command == "status":
        installed = installed_skills(target)
        print(f"安装位置：{target}")
        if installed:
            for skill in installed:
                print(f"  ✓ {skill.name}")
        else:
            print("当前未安装任何 Skill。")
        return 0

    if args.command == "install":
        requested = available if args.all else [SOURCE / name for name in args.skills]
        if not args.all and not args.skills:
            requested = choose_interactively(available)
        for src in requested:
            if not (src / "SKILL.md").is_file():
                print(f"跳过：{src.name} 不是有效 Skill 目录。", file=sys.stderr)
                continue
            dst = target / src.name
            if dst.exists() and not args.force:
                print(f"已存在，跳过（覆盖请加 --force）：{dst}")
                continue
            if dst.exists():
                shutil.rmtree(dst)
            target.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst)
            print(f"已安装：{dst}")
        return 0

    if args.command == "uninstall":
        installed = installed_skills(target)
        requested_names = {p.name for p in installed} if args.all else set(args.skills)
        if not requested_names:
            print("请指定 Skill 名称或使用 --all。")
            return 2
        for name in requested_names:
            dst = target / name
            if dst.exists() and (dst / "SKILL.md").is_file():
                shutil.rmtree(dst)
                print(f"已卸载：{name}")
            else:
                print(f"未找到已安装 Skill：{name}")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
