# Git History Reconstruction — Investigation Entry

> 职责边界：本目录保存 `glm5.2` 完整 Git 历史认知重建的调查阶段资产。这里的结论在完成门通过前
> 仍是调查结论；稳定结论以后再按治理框架沉淀到 README、Feature、MEMORY、rulings 或 docs。

## Frozen Snapshot

- 快照日期：2026-08-24
- 工作分支：`glm5.2`
- immutable ref：annotated tag `legacy-reconstruction-snapshot-2026-08-24`
- snapshot HEAD：`f7dc625ced176dcc04a6151092fdb0861dc66fdc`
- `git rev-list --count legacy-reconstruction-snapshot-2026-08-24`：1399
- `git status --short --branch --untracked-files=all`：`## glm5.2`
- 最新提交：`f7dc625ced176dcc04a6151092fdb0861dc66fdc` / `docs: make Git history reconstruction the project constitution`

Snapshot之后的治理/coverage commits不追涨1399分母。恢复时仍核对current branch HEAD/status；只有
snapshot tag/set本身变化或用户明确要求纳入新产品历史时才建立新snapshot版本，不静默扩范围。

## Objective

从 `glm5.2` 可达的完整 Git 历史倒序重建五个认知方向：

1. 系统架构；
2. 过往的所有 POC；
3. 已经实现的代码；
4. 正在进行的研究；
5. 过往进行的研究。

本任务是一个“整理项目”的特殊治理项目，不是产品代码开发；仍必须使用 Codex 治理架构，并以认知
闭包为先导。

## 2026-08-24 User Ruling

用户裁定本任务必须从粗到细、广度优先。系统有系统群，代码有代码群，POC 往往成组连续出现并有
组内次序逻辑；调查必须先看到大的 Picture，并让这个大的 Picture 成为当前项目治理框架的一部分。
未来深入某个系统、代码目录或 POC 组时，必须先经由 `AGENTS.md` 和相关 Skill 建立认知闭包，再做
具体细节梳理。

权威来源：`rulings.md` 的 `R-2026-08-24-001`；归一要求：`feature-list.md` 的 `GHR-001`。

## Method

1. 第一遍覆盖全部 commits 的 metadata、message、changed paths 和 stat，建立一行不漏的
   `commit-ledger.tsv`。
2. 第一遍同时抽取系统群、代码群、POC 群和研究线群的大图，先建立组群和代际关系。
3. 第二遍仍按 newest-to-oldest 做逐 commit diff-review；大型提交可以按组件分批，但必须记录覆盖范围。
4. 深入单个系统、代码目录或 POC 组前，必须先能说明该局部在大图中的位置。
5. 所有历史、实现和验证主张最终回到 exact commit/diff、当前代码、测试、run artifact 或 receipt。

## Assets

| 资产 | 职责 |
|---|---|
| `commit-ledger.tsv` | `glm5.2` 可达 commits 的一行不漏总账和 review 状态 |
| `commit-path-group-coverage.tsv` | 超大commit内部path-group coverage；全部group terminal后才能升级整commit |
| `devin-execution-contract.md` | Devin E010 / 200k context的批次、恢复、证据、生命周期与迁移Gate |
| `system-architecture.md` | 代际、系统群、组件、当前目标/实际架构和证据入口 |
| `poc-registry.tsv` | 显式/隐式 POC、实验群、组内次序、verdict、失败和替代关系 |
| `implementation-registry.tsv` | 代码群、模块、引入/变更 commit、当前状态、消费者和验证证据 |
| `research-registry.tsv` | current 与 historical 研究线、起止、状态、影响和后继 |
| `unresolved-conflicts.md` | 来源冲突、unknown、已查范围和阻塞影响 |

## Progress

- snapshot：done
- commit ledger rows：1399 / 1399
- unique commits in ledger：1399 / 1399
- stat-reviewed：1398 / 1399
- diff-reviewed：1 / 1399
- blocked：0
- last completed phase：ordinal 1 exact diff-review (f7dc625, governance constitution commit)
- next phase：second-pass exact diff-review of ordinal 2 (c1b934a, large baseline seal) via path groups
- next commit for strict newest-to-oldest diff ledger：`c1b934ab56d6f0554c7a7e9d89bb8b5d66b6baaa` (ordinal 2, 2207 paths, 14 path groups pending in `commit-path-group-coverage.tsv`)
- next large-commit mechanism：`c1b934ab...`按`commit-path-group-coverage.tsv`拆 14 coherent top-level path groups; all groups terminal + remainder=0 后才升级整 commit

## First-Pass Findings

Evidence strength: metadata, subject, changed paths and numstat only. These findings identify investigation
groups and priorities; they do not yet prove semantic behavior, implementation status, verdict correctness, or
current research finality.

- Time map: 1399 commits split cleanly into 7 first-pass epochs: 2026-07-07..07-10 legacy astro/qizheng start
  (139 commits), 2026-08-02..08-05 xishujuzhen and early POC turn (176), 2026-08-06..08-08 Grove/tell-hint and
  VMS formalization surge (345), 2026-08-09..08-12 sixth-gen consolidation (354), 2026-08-13..08-17
  seven/eight and solve_vein evidence factory work (230), 2026-08-18..08-22 continuation/solver split/POC-2.5c
  work (153), 2026-08-24 governance history reconstruction bootstrap (2).
- High-touch roots by commit count: `AGENTS.md` 414, `dev-docs` 407, `xishujuzhen` 189, `subagents-dirs` 142,
  `Tell分类学研究过程文档` 124, `.devin` 85, `analysis-devin-failure-system` 80, `第六代系统研发过程文档` 68,
  `seven-system` 67, `system` 50, `任务追踪` 50.
- Candidate system groups are recorded in `system-architecture.md`; candidate code/asset groups are recorded in
  `implementation-registry.tsv`.
- Candidate POC groups include early xishujuzhen POC-2..8, POC-VMS-0..10, sixth-gen VMS/solve_vein POC work,
  POC-2.5/2.6/2.7 continuation runs, POC-1 re-review with POC-2.5c, seven/eight non-specialized evidence
  factory runs, and canary/qualification/baseline assets.
- Candidate research lines include Grove/tell-hint core cognition, primitive/facet formalization, sixth-gen
  solve_vein, continuation analysis, CAT non-specialized research, seven/eight evidence factory, solver
  externalization, AGENTS slimming/governance, and legacy astro/qizheng lineage.

## Validation

Executed during first-pass write-back:

- Parsed `commit-ledger.tsv`: 1399 data rows, 1399 unique commits, all `review_status=stat-reviewed`.
- Parsed first-pass registries: `poc-registry.tsv` has 7 rows / 16 columns, `implementation-registry.tsv` has
  12 rows / 12 columns, `research-registry.tsv` has 11 rows / 13 columns.
- Checked target files for trailing whitespace with `rg -n "[ \t]+$" ...`: no hits.
- Ran `git diff --check`: passed.
- Checked for accidental hidden temporary files under this directory: none.

## Current Unknowns

- 系统群、代码群、POC 群和研究线群已建立 first-pass 候选；仍需 diff-review 校准。
- 五个认知方向尚未闭合。
- 尚不能声称全部 POC 已梳理、当前研究已确定、历史研究无遗漏或可以安全退役路径。
