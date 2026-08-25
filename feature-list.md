# feature-list.md — 当前需求与验收

> 职责边界：本文件记录当前被接受的需求、约束和验收命题，并区分裁定状态与交付状态。原始用户
> 裁定见 `rulings.md`；当前状态和下一步见 `MEMORY.md`。

## Accepted Requirements

| ID | 类型 | 当前要求 | 来源 | 裁定状态 | 交付状态 | 证据锚点 |
|---|---|---|---|---|---|---|
| GHR-001 | governance-reconstruction | `glm5.2` 历史重建必须作为“整理项目”的特殊治理项目执行：先建立任务相对认知闭包，再从粗到细、广度优先建立系统群、代码群、POC 群和研究线群的大图，最后才深入局部细节、路径处置或目录重塑。 | R-2026-08-24-001 | accepted | first-pass-stat-reviewed | `AGENTS.md` 1.1；`dev-docs/git-history-reconstruction/README.md`；`dev-docs/git-history-reconstruction/commit-ledger.tsv` |

## Acceptance Criteria

GHR-001 的验收命题：

1. 历史重建调查入口记录冻结快照、目标分支、commit 总数、当前进度和 next commit。
2. 第一遍必须覆盖 `glm5.2` 全部 commits 的 metadata/message/changed paths/stat，并产出一行不漏的 commit 总账。
3. 在深挖单个系统、代码目录或 POC 前，必须先建立系统群、代码群、POC 群和研究线群的大图。
4. POC 必须按连续实验群记录组内次序逻辑、verdict、失败、nonclaim、替代和后继关系。
5. 任一局部结论必须能说明自己在大图中的位置，并能返回 exact commit/diff、当前代码、测试或运行实物。
6. 五方向未闭合前，不生成最终路径处置表，不批量删除、移动或退役历史内容。

## Delivery Notes

- `first-pass-stat-reviewed` 表示第一轮 metadata/message/changed-path/stat 总账已覆盖冻结快照的全部 1399 个 commits，并已形成组群级大图初稿；它不表示逐 commit diff-review 已完成。
- 后续不得仅因本文件存在而声称已完成大图、已梳理全部 POC 或可以安全做目录退役。
