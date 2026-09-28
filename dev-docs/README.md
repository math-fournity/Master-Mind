# dev-docs/README.md — 未定调查与过程资产入口

> 职责边界：`dev-docs/` 保存调查、方案、POC、过程记录和未稳定沉淀的材料。当前稳定要求放在
> `feature-list.md`，用户裁定放在 `rulings.md`，当前状态放在 `MEMORY.md`。

## Active Investigations

| 路径 | 状态 | 说明 |
|---|---|---|
| `dev-docs/git-history-reconstruction/README.md` | active-second-pass-ready | immutable snapshot的1399个commits metadata/stat总账已完成；E010 Devin执行合同、path-group sidecar和Hook启动面已就绪；下一步是逐commit exact diff-review。 |
| `dev-docs/repo-group-mapping/README.md` | first-pass-complete-2026-09-28 | 多代系统repo群梳理（ORIGIN/GROVE/HOME核心三仓+外围+排除/负结论/相邻）；拓扑三问、2026-09-28未提交内容封存收据（三仓已clean）、GitHub整备（Master-Mind）处置提案与上传前Gate量化清单；`followup-plan.md`为文件级checklist后续工作方案（W1对账/W2 Gate准备/W3上传wave）；含gitignored本地路径附录。不改变重建分母。 |

## Boundary

旧 `dev-docs/` 文件仍作为有日期的历史证据存在。未经 Git diff、当前代码和直接验证证据核对，不能
因为路径或标题把旧过程文档当成当前真值。
