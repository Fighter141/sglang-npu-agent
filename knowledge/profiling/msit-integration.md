---
id: msit-profiling-integration
title: msit Profile 组件集成评估
category: profiling
evidence: upstream_documented
status: candidate_integration
last_verified: 2026-11-11
sources:
  - https://github.com/Ascend/msit
  - https://github.com/Ascend/msit/tree/master/msit/components/profile
---

# msit Profile 组件集成评估

## 定位

msit 是昇腾工具集，不等同于单一 Profiler。项目应只接入与 SGLang NPU 相关的 Profile / 预检能力，不把整个工具集作为运行时依赖。

## 已确认的代码导航入口

- `msit/components/profile/`：Profile 组件。
- `msit/components/profile/msit_prof/`：Profile CLI / 采集流程相关实现。
- `msit/components/profile/msit_prof/msprof/`：msprof 参数适配与处理逻辑。

上述路径来自已检索的公开仓库文件；使用前应固定 Commit 并再次确认。

## 集成评估

- 是否可直接调用 msit Profile CLI？
- 是否只是对 msprof 的参数封装，还是提供额外解析能力？
- 与 SGLang 服务进程、容器和多 Rank 的关系如何处理？
- 失败退出码和产物目录如何统一？
- 是否与 MindIE Profiler 已有解析功能重复？

## 推荐策略

先以官方 CLI 作为采集入口，保留其原始输出；仅在 msit 提供额外价值时接入对应解析能力。不要同时维护两个采集主入口。
