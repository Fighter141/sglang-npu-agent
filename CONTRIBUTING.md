# 贡献指南

## 开始之前

1. 阅读 [README](README.md)、[架构设计](docs/architecture.md) 和 [迁移来源映射表](docs/source-migration-map.md)。
2. 明确本次改动属于 Plugin、Agent、Skill、Service、Knowledge 还是 Reference。
3. 如果复用上游内容，记录源仓库、源文件路径、Commit / Tag、许可证和本仓落点。
4. 不提交凭据、私有主机信息、内网 IP、私有模型路径或未脱敏日志。

## 贡献要求

- Skill 必须有明确适用场景、输入、输出、执行步骤、失败分支和验证标准。
- Service 必须定义参数、返回值、退出状态、超时、取消和安全边界。
- Knowledge 必须有来源、适用条件、证据等级、验证状态和失效边界。
- Schema / Script / Workflow 的行为变化必须增加测试。
- 性能优化必须提供可比较的 Baseline、Candidate、正确性结果和非 Profiling 性能数据。
- 未在真实昇腾设备验证的内容必须标注“未真机验证”。

## 上游迁移记录

每个迁移 PR 应更新 `docs/source-migration-map.md`，并说明：
- 直接复用、适配改写还是仅借鉴设计；
- 上游固定版本和具体文件路径；
- 许可证与署名；
- 本仓修改点；
- 自动化测试和真机验证情况。

## 提交前检查

至少检查 Markdown 链接、YAML 格式、敏感信息和新增脚本语法。新增功能应提供对应测试。
