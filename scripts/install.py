#!/usr/bin/env python3
"""Install local SGLang NPU Agent Skills using only the Python standard library."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills"
GLOBAL_TARGET = Path.home() / ".agents" / "skills"
PROJECT_SKILL = "sglang-npu-project"
OWNER = "Fighter141/sglang-npu-agent"
MARKER = ".sglang-npu-agent-install.json"
BUNDLE_PATHS = (
    "AGENTS.md", "LICENSE", "README.md", "CONTRIBUTING.md",
    "docs", "knowledge", "reference", "skills", "plugins", "services",
)


def valid_name(name: str) -> bool:
    return len(name) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None


def available_skills() -> list[Path]:
    return sorted(p.parent for p in SOURCE.glob("*/SKILL.md"))


def installed_skills(target: Path) -> list[Path]:
    return sorted(p.parent for p in target.glob("*/SKILL.md"))


def is_managed(skill: Path) -> bool:
    marker = skill / MARKER
    if skill.is_symlink() or marker.is_symlink():
        return False
    try:
        return json.loads(marker.read_text(encoding="utf-8")) == {
            "schema_version": 1, "repository": OWNER, "skill": skill.name,
        }
    except (OSError, ValueError):
        return False


def check_tree(path: Path) -> None:
    """Do not follow symlinks into files outside a distributable source tree."""
    if not path.exists():
        raise ValueError(f"缺少源文件或目录：{path}")
    if path.is_symlink() or (path.is_dir() and any(p.is_symlink() for p in path.rglob("*"))):
        raise ValueError(f"源文件包含符号链接，拒绝复制：{path}")


def check_target(target: Path) -> None:
    for path in (target.parent, target):
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise ValueError(f"安装目录必须是普通目录：{path}")


def check_destination(dst: Path) -> None:
    if dst.is_symlink() or (dst.exists() and not dst.is_dir()):
        raise ValueError(f"Skill 目标必须是普通目录：{dst}")


def check_sources(skills: list[Path]) -> None:
    if not skills:
        raise ValueError("没有可安装的 Skill，请检查源目录。")
    check_tree(SOURCE)
    check_tree(ROOT / "LICENSE")
    for skill in skills:
        if not valid_name(skill.name) or not (skill / "SKILL.md").is_file():
            raise ValueError(f"无效 Skill：{skill.name}")
        if skill.name == PROJECT_SKILL:
            for name in BUNDLE_PATHS:
                check_tree(ROOT / name)


def choose_interactively(skills: list[Path]) -> list[Path]:
    if not sys.stdin.isatty():
        raise ValueError("非交互环境请指定 Skill 名称或 --all。")
    for i, skill in enumerate(skills, 1):
        print(f"  {i}. {skill.name}")
    try:
        raw = input("输入序号（逗号分隔，all 全选，回车取消）：").strip()
    except EOFError as exc:
        raise ValueError("未收到选择；请指定 Skill 名称或 --all。") from exc
    if not raw:
        return []
    if raw.lower() == "all":
        return skills
    selected = []
    for token in raw.split(","):
        if not token.strip().isdigit() or not 1 <= int(token) <= len(skills):
            raise ValueError(f"无效序号：{token}")
        selected.append(skills[int(token) - 1])
    return list(dict.fromkeys(selected))


def install_one(src: Path, dst: Path) -> None:
    """Stage a complete skill before replacing an existing installation."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".sglang-install-", dir=dst.parent))
    prepared, backup = stage / "prepared", stage / "previous"
    try:
        shutil.copytree(src, prepared)
        shutil.copy2(ROOT / "LICENSE", prepared / "LICENSE")
        if src.name == PROJECT_SKILL:
            bundle = prepared / "references" / "project"
            bundle.mkdir(parents=True)
            for name in BUNDLE_PATHS:
                source = ROOT / name
                if source.is_dir():
                    shutil.copytree(source, bundle / name)
                else:
                    shutil.copy2(source, bundle / name)
        (prepared / MARKER).write_text(json.dumps({
            "schema_version": 1, "repository": OWNER, "skill": src.name,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if dst.exists():
            dst.rename(backup)
        try:
            prepared.rename(dst)
        except BaseException:
            if backup.exists():
                backup.rename(dst)
            raise
    finally:
        # If rollback itself fails, preserve the backup for manual recovery.
        if backup.exists() and not dst.exists():
            print(f"旧版本保留在：{backup}", file=sys.stderr)
        else:
            shutil.rmtree(stage)


def main() -> int:
    parser = argparse.ArgumentParser(description="安装本地 SGLang NPU Agent Skills（Python 3.9+，无需 npm）。")
    parser.add_argument("command", nargs="?", choices=["list", "install", "uninstall", "status", "doctor"], default="install")
    parser.add_argument("skills", nargs="*", help="Skill 名称（不接受路径）")
    location = parser.add_mutually_exclusive_group()
    location.add_argument("--global", dest="global_install", action="store_true", help="使用 ~/.agents/skills/")
    location.add_argument("--target", help="项目目录，默认为当前目录")
    parser.add_argument("--all", action="store_true", help="安装全部源 Skill，或仅卸载本安装器管理的 Skill")
    parser.add_argument("--force", action="store_true", help="覆盖同名安装；不允许覆盖源目录")
    args = parser.parse_args()
    if args.all and args.skills:
        parser.error("Skill 名称与 --all 不能同时指定。")
    if args.force and args.command != "install":
        parser.error("--force 仅用于 install。")
    if (args.skills or args.all) and args.command not in {"install", "uninstall"}:
        parser.error("此命令不接受 Skill 名称或 --all。")
    if any(not valid_name(name) for name in args.skills):
        parser.error("Skill 名称只能包含小写字母、数字和单个连字符，不接受路径。")

    target = GLOBAL_TARGET if args.global_install else Path(args.target or ".").expanduser().resolve() / ".agents" / "skills"
    available = available_skills()
    try:
        check_target(target)
        if args.command == "list":
            check_sources(available)
            for skill in available:
                print(skill.name)
            return 0

        if args.command == "doctor":
            print(f"Python：{sys.version.split()[0]}")
            print(f"Skill 源目录：{SOURCE}")
            print(f"安装目标：{target}")
            check_sources(available)
            print(f"可安装 Skill 数：{len(available)}")
            entry = target / PROJECT_SKILL
            if is_managed(entry):
                for name in BUNDLE_PATHS:
                    source = ROOT / name
                    bundle = entry / "references" / "project"
                    check_tree(bundle / name)
                    if source.is_dir():
                        for path in source.rglob("*"):
                            check_tree(bundle / path.relative_to(ROOT))
            print("安装文件检查通过；未检查 Codex 发现、NPU 环境或执行服务。")
            return 0

        if args.command == "status":
            print(f"安装位置：{target}")
            for skill in installed_skills(target):
                label = "本安装器管理" if is_managed(skill) else "未托管（批量卸载保留）"
                print(f"  {skill.name}: {label}")
            return 0

        if args.command == "install":
            known = {p.name: p for p in available}
            unknown = set(args.skills) - known.keys()
            if unknown:
                raise ValueError(f"未知 Skill：{', '.join(sorted(unknown))}")
            check_sources(available)
            requested = available if args.all else [known[name] for name in dict.fromkeys(args.skills)]
            if not args.all and not args.skills:
                requested = choose_interactively(available)
            # Validate the whole selection before making any changes.
            for src in requested:
                dst = target / src.name
                check_destination(dst)
                if dst.resolve() == src.resolve():
                    if args.force:
                        raise ValueError("不能覆盖 Skill 源目录；仓库内可直接使用，或指定其他 --target。")
                elif src.resolve() in dst.resolve().parents or dst.resolve() in src.resolve().parents:
                    raise ValueError("源目录与目标目录不能互相包含。")
            for src in requested:
                dst = target / src.name
                if dst.exists() and not args.force:
                    print(f"已存在，保留：{dst}")
                    continue
                install_one(src, dst)
                print(f"已安装：{dst}")
            return 0

        if args.command == "uninstall":
            if target.resolve() == SOURCE.resolve():
                raise ValueError("不能卸载仓库中的 Skill 源目录；请指定安装目标。")
            if not args.all and not args.skills:
                parser.error("请指定 Skill 名称或 --all。")
            requested = ([p for p in installed_skills(target) if is_managed(p)] if args.all
                         else [target / name for name in dict.fromkeys(args.skills)])
            for dst in requested:
                check_destination(dst)
                if (dst.resolve() == SOURCE.resolve() or SOURCE.resolve() in dst.resolve().parents
                        or dst.resolve() in SOURCE.resolve().parents):
                    raise ValueError("不能卸载 Skill 源目录。")
                if dst.exists() and not is_managed(dst):
                    raise ValueError(f"未托管 Skill，保留：{dst.name}；旧版安装可先用 install --force 显式升级。")
            for dst in requested:
                if dst.exists():
                    shutil.rmtree(dst)
                    print(f"已卸载：{dst.name}")
                else:
                    print(f"未找到已安装 Skill：{dst.name}")
            return 0
    except (OSError, ValueError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
