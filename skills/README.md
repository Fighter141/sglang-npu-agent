# Skills 能力目录

所有可安装 Skill 均位于 `.agents/skills/<skill-name>/SKILL.md`，安装器自动扫描目录。新增 Skill 无需修改安装器。

## 项目原生 Skills

| Skill | 能力 |
|---|---|
| sglang-npu-project | 项目入口、架构导航和开发规范 |
| sglang-model-bringup | SGLang 模型适配与验证 |
| sglang-serving-config | SGLang Ascend 服务配置 |
| sglang-performance-optimization | 端到端性能优化闭环 |
| sglang-benchmark | 服务级 Benchmark |
| ascend-profiling | Profiling 采集与分析流程 |
| sglang-incident-triage | SGLang NPU 故障诊断 |
| sglang-code-review | SGLang / Ascend 代码审查 |
| sglang-moe-optimization | MoE / EP 优化 |
| sglang-graph-mtp-optimization | Graph / FIA / MTP 优化 |
| ascend-operator-development | 算子开发总入口 |

## 从 Ascend/agent-skills 迁入的 Skills

来源仓库：<https://github.com/Ascend/agent-skills>
固定源 Commit：`155ac37bd169ddb89479af528297cfb2237400aa`
原仓库许可证：Mulan Permissive Software License 2.0。迁入文件保留来源标记；发布前需完成许可证与第三方依赖审查。

### Profiling / 设备 / 通信

- `ascend-profiling-anomaly`：Profiling 异常发现、模型结构分析。
- `npu-smi`：NPU 设备查询与管理命令参考。
- `hccl-test`：HCCL 集合通信与多机预检。

### AscendC 算子开发

- `ascendc-operator-dev`
- `ascendc-operator-design`
- `ascendc-operator-code-gen`
- `ascendc-operator-compile-debug`
- `ascendc-operator-code-review`
- `ascendc-operator-project-init`
- `ascendc-operator-testcase-gen`
- `ascendc-operator-precision-eval`
- `ascendc-operator-precision-debug`
- `ascendc-operator-performance-eval`
- `ascendc-operator-performance-optim`
- `ascendc-operator-mssanitizer`
- `ascendc-operator-doc-gen`

### Triton-Ascend 算子开发

- `triton-operator-dev`
- `triton-operator-design`
- `triton-operator-code-gen`
- `triton-operator-code-review`
- `triton-operator-env-config`
- `triton-operator-performance-eval`
- `triton-operator-performance-optim`
- `triton-operator-precision-eval`
- `triton-operator-doc-gen`

## 安装

```bash
python3 scripts/install.py list
python3 scripts/install.py install
python3 scripts/install.py install --all
python3 scripts/install.py install --all --global
```

## 迁入状态说明

当前已迁入上述 Skill 的入口文件；部分 Skill 的 references / scripts / templates 已同步。尚未完整同步的依赖资源、路径适配和真机验证会继续补齐。**Skill 出现在安装列表不等于其所有自动化脚本已通过验证。**

安装前应先阅读对应 Skill 的来源标记和限制；尤其不要直接执行会安装驱动、修改固件、创建 privileged 容器或运行多机通信测试的脚本。
