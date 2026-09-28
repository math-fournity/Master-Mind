# MEMORY.md — 当前态与续做记录

> 职责边界：本文件只记录当前状态、已确认新知、开放问题和下一步。完整要求见 `feature-list.md`；
> 原始裁定见 `rulings.md`；调查资产见 `dev-docs/git-history-reconstruction/`。

## Current Execution Queue

| 优先级 | lifecycle | 当前工作 | 完成条件 | 下一动作 |
|---|---|---|---|---|
| P0 | `ACTIVE_WORK` | 对immutable snapshot的1,399 commits执行second-pass exact diff review并闭合五方向registries | reconstruction validator `--require-pass`、tip reconciliation和unknown completion全部PASS | 用Devin E010 harness启动，从ordinal 1 / `f7dc625...`开始首个可提交批次 |
| P1 | `CURRENT_REQUIREMENT` | 保持current/history、documented/implemented/verified/live与migration授权分离 | 每批ledger/registries/MEMORY/commit可恢复，历史不污染当前调度 | 遵守`devin-execution-contract.md` |

Structure migration 当前不是 `ACTIVE_WORK`。它只有 reconstruction PASS 且用户另行授权具体阶段/wave
后才获得调度权。

## Current State

- 更新时间：2026-09-28（repo群梳理批次；上一状态2026-08-25）
- 当前任务：从 `glm5.2` 完整 Git 历史倒序重建数学大师制造系统认知。
- 任务身份：这是一个“整理项目”的特殊治理项目，不是产品代码开发；同样必须以认知闭包为先导。
- 当前分支：`glm5.2`
- immutable snapshot：tag `legacy-reconstruction-snapshot-2026-08-24` ->
  `f7dc625ced176dcc04a6151092fdb0861dc66fdc`，1399 commits。
- 当前branch tip已包含snapshot之后的治理/coverage commits；它们不追涨snapshot denominator。
- 已确认新裁定：历史重建必须从粗到细、广度优先，先建立系统群、代码群、POC 群和研究线群的大图，再深入局部。
- 第一轮调查状态：已完成全量 metadata/stat 总账，已建立组群级大图初稿；尚未开始逐 commit diff-review。
- Devin E010准备状态：根AGENTS已适配单文件预算；旧项目Rules/Skills/Hooks已转legacy；200k执行合同、
  path-group sidecar和harness使用说明已建立。

## Progress

- 已读取并确认项目 `AGENTS.md`。
- 已记录用户裁定 `R-2026-08-24-001`。
- 已归一当前要求 `GHR-001`。
- 已初始化 `dev-docs/git-history-reconstruction/` 调查入口和注册表骨架。
- 已生成 `commit-ledger.tsv`：1399 / 1399 commits，1399 个唯一 commit，全部 `stat-reviewed`。
- 已写入 `system-architecture.md` 的 first-pass 大图：7 个时间阶段、8 个系统群、11 个代码/资产群、7 个 POC 群、10 条研究线候选。
- 已写入 `poc-registry.tsv`、`implementation-registry.tsv`、`research-registry.tsv` 的 first-pass 候选注册表。
- 已验证：`commit-ledger.tsv` 为 1399 行数据、1399 个唯一 commit、全部 `stat-reviewed`；TSV 结构检查通过；目标文件尾随空白检查通过；`git diff --check` 通过。
- ordinal 1 (`f7dc625`) exact diff-review 完成：governance constitution commit，AGENTS.md M +331/-50，将旧 short-form AGENTS 替换为10节重建宪法；meta/governance 变更，五方向 impact 均为 none；ledger 已升级为 diff-reviewed。
- ordinal 2 (`c1b934a`) path-group 计划已建立：14 个 coherent top-level groups 写入 `commit-path-group-coverage.tsv`，全部 pending；2207 paths 覆盖完整。
- 尚未开始 ordinal 2 path-group 逐组 diff-review。
- 旧项目`.devin/rules`、`.devin/skills`与Arango cognition Hook保留在
  `.devin/legacy/pre-e010-project-governance/`，默认无当前调度权。
- 2026-09-28 repo群梳理批次（用户新任务，只关注多代系统线）：完成ORIGIN/GROVE/HOME/FEITEHUA/
  SUPERVISOR及排除项/负结论/相邻项登记与拓扑三问；ORIGIN脏区三批封存（19ca14d/56508a7/36d5e85，
  Phase7+183/184+arango备份）、GROVE脏区五批封存（5e0fea7/09c2f9d/f86e13f/2979464/460ce36，
  文档/删除/题库manifest/runs）、FEITEHUA初始保全（84ff468），三仓工作区均clean；GitHub目标
  Master-Mind（public空仓）与既有已上传生态对位完成；上传硬约束（敏感token绝不出现在上传内容）、
  敏感内容量化扫描与Gate清单落盘于`dev-docs/repo-group-mapping/`（真实路径在gitignored附录）。
- 2026-09-28补做：后续工作方案落地为文件级checklist（`dev-docs/repo-group-mapping/followup-plan.md`，
  W1内容对账/W2 Gate执行准备/W3上传wave化/待裁定项），配套三类清单资产（37独有commits清单、
  独有内容HOME存在性矩阵、敏感内容逐文件inventory）；fork点复核修正：GROVE↔HOME真实fork
  commit为`2596dcf`（08-08 07:53），first-pass曾误读为`2e33663`（实为共享段早期commit）。

## Next Handoff

下一次继续时：

1. 使用Devin E010 harness启动，完整读取根AGENTS、README、本文件、Feature/rulings、investigation
   README与`devin-execution-contract.md`。
2. 确认仍在`glm5.2`，核对current HEAD/status和immutable snapshot tag/set/count；current branch新增
   governance commit不改变1399 denominator。
3. 运行coverage validator，不全文读取ledger；查询状态统计和next incomplete row。
4. 从ordinal 2 / `c1b934a...`开始 path-group diff-review；按`commit-path-group-coverage.tsv`中14个
   coherent top-level groups逐组审阅，每组terminal后更新sidecar，全部group terminal且remainder=0后
   才升级整commit为diff-reviewed。
5. 每批更新coverage/registries/current queue并精确commit；PostCompaction或新Session从已提交next
   item恢复。

## Open Questions

- 组群分类仍是 first-pass 候选，可能被后续 diff-review 修正。
- 当前实际架构、已实现代码、全部 POC、current research 和 historical research 都尚未达到完成门。
- 新增45项Layer2后的真实router选择与目标repo fresh全文注入需在第一次harness运行保留私有证据；
  static/mechanical通过不能冒充长期行为证明。
- repo群开放项：GROVE 37个独有commits与HOME的内容级对账、ORIGIN 146/147封存版本drift核对、
  worker分支/tag上传保全决策、上传wave化方案——见`dev-docs/repo-group-mapping/topology-findings.md`§7。

## Open Incidents

当前无已确认`OPEN_INCIDENT`。

## Closed Incident Registry

当前无项目治理事故记录。空表不编造关闭事项；未来记录必须包含`CLOSED_INCIDENT`、closed_at、
closure evidence、still-valid lesson、reopen_if和current route。
