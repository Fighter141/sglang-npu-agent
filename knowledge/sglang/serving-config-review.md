---
id: sglang-serving-config-review
title: SGLang Ascend Serving 配置审查
category: workflow
evidence: upstream_documented
status: initial_reference
last_verified: 2026-11-11
sources:
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/getting-started/quick_start.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/ascend-npus/optimization/parameter_tuning.mdx
---

# SGLang Ascend Serving 配置审查

## 配置审查项

1. 模型路径、Revision、Tokenizer 和量化配置。
2. 设备可见性、卡数、Die / Rank 拓扑。
3. TP / DP / EP / PP / DCP 等并行参数与模型结构是否一致。
4. Attention Backend、FIA、Graph、MTP 和 Prefix Cache 的版本支持与功能组合。
5. KV Cache、显存预算、最大并发、输入输出长度。
6. HCCL、网络接口、通信 Buffer 和多机启动环境。
7. 日志、健康检查、端口和服务退出清理。

## 参数确认

每个非默认参数都应记录：
- 目标版本是否存在；
- CLI 名称、类型、默认值和取值范围；
- 代码中读取参数的位置；
- 适用硬件 / 模型条件；
- 与其他参数的冲突；
- 启动后是否确认生效。

不要从旧版博客复制参数默认值。先以当前版本 `--help`、参数定义和 Ascend 文档交叉确认。

## 结果要求

输出启动命令、参数差异表、兼容性风险、实际生效配置和 Smoke Test 结果。服务成功启动不代表配置最优。
