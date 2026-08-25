# feature-list.md — 当前需求与验收

> 职责边界：本文件记录当前被接受的需求、约束和验收命题，并区分裁定状态与交付状态。原始用户
> 裁定见 `rulings.md`；当前状态和下一步见 `MEMORY.md`。

## Accepted Requirements

| ID | 类型 | 当前要求 | 来源 | 裁定状态 | 交付状态 | 证据锚点 |
|---|---|---|---|---|---|---|
| GHR-001 | governance-reconstruction | `glm5.2` 历史重建必须作为“整理项目”的特殊治理项目执行：先建立任务相对认知闭包，再从粗到细、广度优先建立系统群、代码群、POC 群和研究线群的大图，最后才深入局部细节、路径处置或目录重塑。 | R-2026-08-24-001 | accepted | first-pass-stat-reviewed | `AGENTS.md` 1.1；`dev-docs/git-history-reconstruction/README.md`；`dev-docs/git-history-reconstruction/commit-ledger.tsv` |
| GHR-002 | devin-execution | 使用Devin CLI处理完整历史时，必须通过E010两层治理与repo-local Hook建立闭包，在200k上下文内按可提交批次持续推进；snapshot分母固定，状态落入ledger/registries/MEMORY/Git，不依赖聊天记忆；旧项目Rules/Skills退出当前自动发现但保留legacy血统。 | R-2026-08-25-002 | accepted | implemented-pending-live-verification | 根`AGENTS.md`；`.devin/README.md`；`devin-execution-contract.md`；Devin E010 docs/runtime |
| GHR-003 | structure-migration-gate | 全repo目录/文档/代码重塑只能在reconstruction PASS、完整path manifest、consumer/data/artifact/runtime scan、rollback和用户对具体阶段/wave的明确授权后执行；设计不等于移动授权。 | R-2026-08-25-002 | accepted | documented | 根`AGENTS.md`；`devin-execution-contract.md`；`repo-structure-migration` |

## Acceptance Criteria

GHR-001 的验收命题：

1. 历史重建调查入口记录冻结快照、目标分支、commit 总数、当前进度和 next commit。
2. 第一遍必须覆盖 `glm5.2` 全部 commits 的 metadata/message/changed paths/stat，并产出一行不漏的 commit 总账。
3. 在深挖单个系统、代码目录或 POC 前，必须先建立系统群、代码群、POC 群和研究线群的大图。
4. POC 必须按连续实验群记录组内次序逻辑、verdict、失败、nonclaim、替代和后继关系。
5. 任一局部结论必须能说明自己在大图中的位置，并能返回 exact commit/diff、当前代码、测试或运行实物。
6. 五方向未闭合前，不生成最终路径处置表，不批量删除、移动或退役历史内容。

GHR-002/GHR-003 的补充验收：

1. Devin fresh Session实际只发现精简后的项目AGENTS面与global router，不自动加载旧项目Rules/Skills；
2. Harness能安装/停止且不覆盖并行配置，PostCompaction后从持久coverage恢复；
3. Router对完整重建选择closure+legacy reconstruction+匹配领域，对普通局部问题不误选structure migration；
4. Snapshot tag/set/order/count固定为1399，后续治理commit不造成分母追涨；
5. Reconstruction PASS前structure migration无任务资格；每个真实wave需要单独授权与rollback。

## Delivery Notes

- `first-pass-stat-reviewed` 表示第一轮 metadata/message/changed-path/stat 总账已覆盖冻结快照的全部 1399 个 commits，并已形成组群级大图初稿；它不表示逐 commit diff-review 已完成。
- 后续不得仅因本文件存在而声称已完成大图、已梳理全部 POC 或可以安全做目录退役。
- `implemented-pending-live-verification`只说明E010文件/配置已落地；必须用第一次真实fresh/harness/
  route/trajectory证据后才能把GHR-002升级为verified。
