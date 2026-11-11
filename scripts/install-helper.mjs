#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SOURCE = path.join(ROOT, ".agents", "skills");
const args = process.argv.slice(2);
const command = args[0] || "help";
const value = (flag, fallback) => {
  const i = args.indexOf(flag);
  return i >= 0 && args[i + 1] ? args[i + 1] : fallback;
};
const has = flag => args.includes(flag);
const level = value("--level", "project");
const target = value("--target", process.cwd());
const destRoot = level === "global"
  ? path.join(os.homedir(), ".agents", "skills")
  : path.join(path.resolve(target), ".agents", "skills");

function skills() {
  if (!fs.existsSync(SOURCE)) return [];
  return fs.readdirSync(SOURCE, { withFileTypes: true })
    .filter(d => d.isDirectory() && fs.existsSync(path.join(SOURCE, d.name, "SKILL.md")))
    .map(d => d.name).sort();
}
function copyDir(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const from = path.join(src, entry.name);
    const to = path.join(dst, entry.name);
    if (entry.isDirectory()) copyDir(from, to);
    else if (entry.isFile()) fs.copyFileSync(from, to);
  }
}
function removeDir(dir) {
  if (fs.existsSync(dir)) fs.rmSync(dir, { recursive: true, force: true });
}
function usage() {
  console.log(`SGLang NPU Agent 安装工具

用法：
  sglang-npu list
  sglang-npu install <skill-name|--all> [--level project|global] [--target PATH]
  sglang-npu uninstall <skill-name|--all> [--level project|global] [--target PATH]
  sglang-npu status [--level project|global] [--target PATH]
  sglang-npu doctor [--level project|global] [--target PATH]

说明：
  project：安装到目标项目的 .agents/skills/
  global ：安装到 ~/.agents/skills/
  --target：指定项目根目录，仅对 project 级安装有效

当前仅安装本仓库中实际存在 SKILL.md 的技能，不会安装路线图中的规划能力。`);
}
function installed() {
  if (!fs.existsSync(destRoot)) return [];
  return fs.readdirSync(destRoot, { withFileTypes: true })
    .filter(d => d.isDirectory() && fs.existsSync(path.join(destRoot, d.name, "SKILL.md")))
    .map(d => d.name).sort();
}

if (command === "help" || command === "--help" || command === "-h") usage();
else if (command === "list") {
  const names = skills();
  console.log("可安装的 SGLang NPU Skills：");
  if (!names.length) console.log("  当前没有可发布的专项 Skill。");
  for (const name of names) console.log(`  - ${name}`);
} else if (command === "install") {
  const requested = args[1] === "--all" ? skills() : [args[1]].filter(Boolean);
  if (!requested.length) {
    console.error("没有可安装的 Skill。请先查看 list；不会创建空 Skill。");
    process.exitCode = 2;
  } else {
    for (const name of requested) {
      const src = path.join(SOURCE, name);
      if (!fs.existsSync(path.join(src, "SKILL.md"))) {
        console.error(`跳过 ${name}：源 Skill 不存在。`);
        process.exitCode = 2;
        continue;
      }
      const dst = path.join(destRoot, name);
      if (fs.existsSync(dst) && !has("--force")) {
        console.log(`已存在，跳过（如需覆盖加 --force）：${dst}`);
        continue;
      }
      removeDir(dst);
      copyDir(src, dst);
      console.log(`已安装：${dst}`);
    }
  }
} else if (command === "uninstall") {
  const requested = args[1] === "--all" ? installed() : [args[1]].filter(Boolean);
  for (const name of requested) {
    const dst = path.join(destRoot, name);
    if (!fs.existsSync(dst)) console.log(`未安装：${name}`);
    else {
      removeDir(dst);
      console.log(`已卸载：${name}`);
    }
  }
} else if (command === "status") {
  console.log(`安装位置：${destRoot}`);
  const names = installed();
  console.log(names.length ? names.map(n => `  ✓ ${n}`).join("\n") : "当前未安装任何 Skill。");
} else if (command === "doctor") {
  console.log(`Node.js：${process.version}`);
  console.log(`Skill 源目录：${fs.existsSync(SOURCE) ? "存在" : "缺失"} (${SOURCE})`);
  console.log(`目标目录：${destRoot}`);
  console.log(`目标目录可写：${(() => { try { fs.mkdirSync(destRoot, {recursive:true}); fs.accessSync(destRoot, fs.constants.W_OK); return "是"; } catch { return "否"; } })()}`);
  console.log(`可安装 Skill 数：${skills().length}`);
} else {
  console.error(`未知命令：${command}`);
  usage();
  process.exitCode = 2;
}
