# System Lineage

This file summarizes the major historical system islands and how to trace them. It is a route, not a complete
history. For exact commits, use `git-log-lineage.tsv` and Git diffs.

## Lineage Summary

| Period | System / concept family | Evidence route | Notes |
|---|---|---|---|
| 2026-07-07 to 2026-07-10 | Astrology, qizheng, tieban, source-text audit system | early commits such as `de5212a`, `04f301d`, `a2c71b3`; old paths in Git history | This is the inherited star-system layer. It is historical for this repo's current Math Master scope but explains many working disciplines. |
| 2026-08-02 to 2026-08-03 | Study-system turn, xishujuzhen as cognitive graph / work-system brain | commits around `6b4f308`, `c167e3c`, `66377d3`, `d222ee2` | The project moved from ordinary engineering toward cognition accumulation and dependency-graph-assisted AI work. |
| 2026-08-04 to 2026-08-05 | Math Master architecture baseline, exhaustive knowledge absorption, arXiv/data foundation, POC sequence, audit methodology | `108/109` plans in dev-docs, `knowledge/README.md`, `7c25c11`, `a3d4978` | Establishes the early Math Master research loop, POC discipline, and audit-method vocabulary. Large data is now pointerized to D disk. |
| 2026-08-05 to 2026-08-08 | First-principles and first five generations, primitive system, VMS/Grove roots | `第五代系统技术说明书/`, `原语化AI数学工程系统设计/`, `primitives/`, `concepts/`, `criteria/`, `facets/` | Historical design lineage. Use these paths for concept origins, not as proof of current implementation. |
| 2026-08-08 to 2026-08-12 | Sixth-generation implementation and Tell/Hint taxonomy | `system/`, `SixthGenRnD.md`, `第六代系统技术说明书/`, `Tell分类学研究过程文档/` | Main in-repo implementation and research period for Grove loop, solve vein analysis, Tell/Hint, and non-specialization POCs. |
| 2026-08-12 to 2026-08-16 | Solver batch systems, analysis-devin-failure-system, Seven and Eight emergence | `analysis-devin-failure-system/`, `seven-system/`, `eight-system/`, `runs/`, `subagents-dirs/` | Contains runtime evidence, profile extraction, evidence-factory contracts, and overdesign/refinement investigations. |
| 2026-08-17 to 2026-08-22 | Non-specialization POC expansion, continuation/handover, solver-system split, AGENTS slimming | `Tell分类学研究过程文档/396*` to `418*`, `POC-2.7/`, root `RepoInfo.md`, `WorkPrinciples.md` | Active solver code moved to external repos; root AGENTS was slimmed and high-value content moved to route documents. |
| 2026-08-24 | Governance alignment | `pre-governance-alignment-2026-08-24`, `c1b934a`, `e52927f`, current governance files | Establishes cognitive-closure-first repo governance and D disk pointerization for large data. |

## Concept Routes

| Concept | First route to load | Historical evidence route |
|---|---|---|
| Cognitive closure | `AGENTS.md`, `README.md`, `feature-list.md` | Current governance commits and `认知闭包/` |
| Grove loop | `GroveCoreCognition.md`, `system/README.md` | Git grep/log for `Grove`, `VMS`, `引导树`, `解题树` |
| Tell/Hint | `000-v0-2026-08-08-引导树闭环-识别端结构定义.md`, `Tell分类学研究过程文档/` | Git grep/log for `Tell`, `Hint`, `tell/hint` |
| VMS | `MemoryArchive.md`, `任务追踪/`, VMS run dirs | Git grep/log for `VMS`, `虚拟数学系统` |
| First five generations | `第五代系统技术说明书/`, `原语化AI数学工程系统设计/` | Git log for `第五代`, `原语`, `Phase 0` |
| Sixth generation | `system/README.md`, `SixthGenRnD.md` | Git log for `第六代`, `system/`, `solve_vein_analysis` |
| Analysis system | `AnalysisSystemDesign.md`, `AnalysisSystemOps.md`, `analysis-devin-failure-system/` | Git log for `analysis-devin-failure-system`, `错题分析` |
| Seven | `seven-system/AGENTS.md`, `seven-system/README.md` | Git log for `seven-system`, `WP-` |
| Eight | `eight-system/README.md` | Git log for `eight-system`, `过度设计`, `非特化` |
| External solver split | `RepoInfo.md`, external repo `AGENTS.md` files | commits `0f54bf4`, `d80201f`, `e318b58` |
| Large data offload | `knowledge/README.md`, `docs/data/README.md` | commit `e52927f`, migration manifests |

## How To Use This Lineage

1. Locate the island or concept here.
2. Read the current route file.
3. Use `git-log-lineage.tsv` to find commits and paths.
4. Open the underlying file, code, test, run evidence, or diff before making a material claim.
5. If current docs and historical files conflict, current requirements come from `feature-list.md` and user
   rulings; historical files explain origin and evolution.
