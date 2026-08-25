# System Architecture Reconstruction

> 调查状态：first-pass-stat-reviewed。本文从 `glm5.2` 的 1399 个 commits 的 metadata、subject、
> changed paths 和 numstat 建立大图。所有结论都是候选路由，必须经后续 exact diff/current code/test/run
> evidence 校准后才能成为稳定架构事实。

## Snapshot

- 目标分支：`glm5.2`
- HEAD：`f7dc625ced176dcc04a6151092fdb0861dc66fdc`
- commit ledger：1399 / 1399 rows，1399 unique commits
- review level：first-pass `stat-reviewed`
- diff-reviewed：0 / 1399

## Time Epochs

| Epoch | 日期 | commits | First-pass meaning | Evidence boundary |
|---|---:|---:|---|---|
| E0 | 2026-07-07..2026-07-10 | 139 | legacy astro/qizheng/moira 起点、工作自动化和审计方法早期形态 | 主要来自 subject/path；当前数学系统继承关系待 diff 校准 |
| E1 | 2026-08-02..2026-08-05 | 176 | 转入 xishujuzhen/数学大师制造，早期 POC 与 ArangoDB/题目基座/安全边界开始出现 | POC verdict 和数据边界待逐 commit 查证 |
| E2 | 2026-08-06..2026-08-08 | 345 | Grove、tell/hint、原语/面相/criteria、POC-VMS 0..10 和第五/第六代思想成形 | 高密度设计与实验混合，需避免把文档主张当实现 |
| E3 | 2026-08-09..2026-08-12 | 354 | 第六代系统、`system/`、`six/` 合并、solve_vein/VMS 系列和提示词资产集中发展 | `six/` 到 `system/` lineage 待 diff-review |
| E4 | 2026-08-13..2026-08-17 | 230 | `seven-system`、`eight-system`、solve_vein evidence/canary/qualification 和 selfrun 运行资产 | live/qualification 上限待 run artifact 校准 |
| E5 | 2026-08-18..2026-08-22 | 153 | continuation/analysis system、AGENTS 瘦身、solver/pipe 外迁、POC-2.7/2.5c 与 CAT 非特化线收束 | current research 与 externalized 边界待查 |
| E6 | 2026-08-24 | 2 | pre-governance baseline 封存和本历史重建宪法建立 | 当前治理入口事实已由本轮写回补充 |

## System Groups

| Group | Candidate identity | Primary roots | First-pass status | Next diff target |
|---|---|---|---|---|
| SG-00 | governance/work-system layer | `AGENTS.md`, `README.md`, `dev-docs`, `任务追踪`, `CurrentTaskAwareness.md` | current governance/route layer, heavily rewritten over time | `f7dc625`, `c1b934a`, AGENTS slimming commits 2026-08-19 |
| SG-01 | legacy astro/qizheng/moira island | `qizheng`, `moira`, `swisseph`, `moira_extra_files`, `base`, `build` | historical/removed-at-tip candidate; likely methodological ancestor | `de5212a`, cleanup commits around 2026-08-05 |
| SG-02 | early xishujuzhen math master and data foundation | `xishujuzhen`, `knowledge`, `DataFoundation.md`, `ProblemProfileWork.md` | mixed implementation/research/data island; later partly externalized | 2026-08-03..08-06 POC and DB commits; 2026-08-20 split commits |
| SG-03 | Grove/tell-hint/core cognition and formalization | `GroveCoreCognition.md`, `000-*`, `primitives`, `concepts`, `facets`, `criteria`, `原语化AI数学工程系统设计` | design/research backbone candidate | 2026-08-06..08-08 formalization commits |
| SG-04 | sixth-generation solve_vein/current system | `system`, `第六代系统技术说明书`, `第六代系统研发过程文档`, `第六代系统提示词积累目录` | current implementation/design candidate, not yet verified | `system/` introduction, `six/` merge, VMS-31..43 commits |
| SG-05 | continuation and Devin failure analysis system | `analysis-devin-failure-system`, `AnalysisSystem*.md`, `MonitorPipe.md`, `POC-2.7`, `trajectory-schema.md` | continuation system candidate; likely split/external repo boundary | 2026-08-18..08-19 monitor/session/continuation commits |
| SG-06 | seven/eight non-specialized evidence factory | `seven-system`, `eight-system`, `seven-system非特化证据工厂研发过程文档` | experimental/evidence-factory island candidate | 2026-08-13..08-17 scaffold/audit/MH commits |
| SG-07 | solver/pipe/external execution boundary | `solver-harness`, `SolverPipeSystem.md`, `SolverOpsSOP.md`, `scripts`, `tools`, externalization subjects | current repo boundary changed by external split | 2026-08-20 split and cleanup commits |
| SG-08 | runtime/evidence asset layer | `runs`, `subagents-dirs`, `subagent-docs`, `knowledge`, `Tell分类学研究过程文档` | evidence/workspace/history assets; not automatically current truth | `c1b934a` baseline and POC-specific earlier commits |

## Code And Asset Groups

The first-pass code map is normalized in `implementation-registry.tsv`. Current high-touch roots suggest code and
asset groups should be investigated in this order: `system`, `analysis-devin-failure-system`, `seven-system`,
`xishujuzhen`, `scripts/tools`, `primitives/concepts/facets/criteria`, runtime/evidence roots, then legacy removed
roots. `AGENTS.md` and `dev-docs` are governance/research carriers, not implementation proof by themselves.

## POC Groups

The first-pass POC map is normalized in `poc-registry.tsv`. The largest groups are:

1. early xishujuzhen POC-2..8 and POC-3/4/5/6/7 result chain;
2. POC-VMS-0..10 on 2026-08-08, including A/B, baseline and tell/hint validation;
3. sixth-gen VMS/solve_vein POC/canary/qualification work around VMS-24, VMS-27, VMS-28 and VMS-31..43;
4. continuation POC-2.5/2.6/2.7/2.7.5/2.7.6 and proof/HANDOVER assets;
5. POC-1 re-review and POC-2.5c CAT non-specialized research;
6. seven/eight MH/evidence-factory experiments.

## Research Lines

The first-pass research map is normalized in `research-registry.tsv`. Current/candidate status remains uncertain
until newer commits, user rulings and actual code/run assets are reconciled by diff-review.

## Evidence Boundary

- `commit-ledger.tsv` proves coverage of commit metadata/stat for the frozen snapshot.
- It does not prove that any POC verdict is correct, any code path is callable, or any research line is active.
- The next phase must read exact diffs, starting from newest-to-oldest or from high-value group pivots while keeping
  the ledger as the one coverage authority.
