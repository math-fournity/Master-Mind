# MEMORY.md — 当前态与续做记录

> 职责边界：本文件只记录当前状态、已确认新知、开放问题和下一步。完整要求见 `feature-list.md`；
> 原始裁定见 `rulings.md`；调查资产见 `dev-docs/git-history-reconstruction/`。

## Current State

- 更新时间：2026-08-24
- 当前任务：从 `glm5.2` 完整 Git 历史倒序重建数学大师制造系统认知。
- 任务身份：这是一个“整理项目”的特殊治理项目，不是产品代码开发；同样必须以认知闭包为先导。
- 当前分支：`glm5.2`
- 当前 HEAD：`f7dc625ced176dcc04a6151092fdb0861dc66fdc`
- 当前 `glm5.2` 可达 commit 数：1399
- 最近提交：`docs: make Git history reconstruction the project constitution`
- 已确认新裁定：历史重建必须从粗到细、广度优先，先建立系统群、代码群、POC 群和研究线群的大图，再深入局部。
- 第一轮调查状态：已完成全量 metadata/stat 总账，已建立组群级大图初稿；尚未开始逐 commit diff-review。

## Progress

- 已读取并确认项目 `AGENTS.md`。
- 已记录用户裁定 `R-2026-08-24-001`。
- 已归一当前要求 `GHR-001`。
- 已初始化 `dev-docs/git-history-reconstruction/` 调查入口和注册表骨架。
- 已生成 `commit-ledger.tsv`：1399 / 1399 commits，1399 个唯一 commit，全部 `stat-reviewed`。
- 已写入 `system-architecture.md` 的 first-pass 大图：7 个时间阶段、8 个系统群、11 个代码/资产群、7 个 POC 群、10 条研究线候选。
- 已写入 `poc-registry.tsv`、`implementation-registry.tsv`、`research-registry.tsv` 的 first-pass 候选注册表。
- 已验证：`commit-ledger.tsv` 为 1399 行数据、1399 个唯一 commit、全部 `stat-reviewed`；TSV 结构检查通过；目标文件尾随空白检查通过；`git diff --check` 通过。
- 尚未开始逐 commit diff-review。

## Next Handoff

下一次继续时：

1. 完整读取 `AGENTS.md`，确认仍在 `glm5.2`。
2. 读取本文件和 `dev-docs/git-history-reconstruction/README.md`。
3. 若 HEAD 或 commit count 与记录不同，先审计闭包是否失效。
4. 从 `dev-docs/git-history-reconstruction/README.md` 记录的 next phase 继续：优先按 first-pass 大图选择第二轮 diff-review 的高价值转折 commit。
5. 第二轮仍需 newest-to-oldest；可按系统群/POC 群分批，但必须在 `commit-ledger.tsv` 中保留每个 commit 的覆盖状态和剩余项。

## Open Questions

- 组群分类仍是 first-pass 候选，可能被后续 diff-review 修正。
- 当前实际架构、已实现代码、全部 POC、current research 和 historical research 都尚未达到完成门。
