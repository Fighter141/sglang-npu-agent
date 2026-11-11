# 第三方内容与许可证声明

本仓库包含本项目原创内容，也包含从第三方开源项目选择性迁入的文件。根目录 LICENSE 不覆盖下列第三方文件；第三方文件继续适用其原始许可证。

## Ascend/agent-skills

- 上游仓库：https://github.com/Ascend/agent-skills
- 迁入时固定 Commit：`155ac37bd169ddb89479af528297cfb2237400aa`
- 上游声明许可证：Mulan Permissive Software License, Version 2.0（MulanPSL-2.0）
- 上游许可证文本：https://github.com/Ascend/agent-skills/blob/master/LICENSE
- 迁入目录：`.agents/skills/ascend-profiling-anomaly/`、`.agents/skills/npu-smi/`、`.agents/skills/hccl-test/`、`.agents/skills/ascendc-operator-*/`、`.agents/skills/triton-operator-*/`
- 迁入方式：选择性复制 Skill 入口文件及部分 references / scripts / templates；各文件顶部保留来源路径、Commit 和许可证标记。

## 使用与再分发注意事项

1. 本仓库根目录的 Apache-2.0 LICENSE 仅适用于本项目原创且未另行声明许可证的内容。
2. 从 Ascend/agent-skills 迁入的文件应按 MulanPSL-2.0 及上游版权声明使用和再分发。
3. 迁入后新增的适配内容应与上游原文区分；不得删除源文件中的版权和许可证声明。
4. 第三方脚本执行前需检查其命令、权限、环境假设和副作用；本仓库尚未对所有迁入脚本完成安全审计或昇腾真机验证。
5. 发布发行包前，应逐文件确认是否存在不同许可证的嵌套依赖、模板或生成代码。

本文件是迁移登记，不构成法律意见。
