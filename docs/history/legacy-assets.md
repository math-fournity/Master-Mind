# Legacy Assets

This file records old or historical assets that should remain traceable. "Legacy" does not mean worthless; it
means future AI should not assume the asset is the current authoritative implementation without evidence.

## Root Historical Maps

| Path | Current role | Retention reason |
|---|---|---|
| `GroveCoreCognition.md` | Historical high-value cognition map | Preserves Grove loop, assistant roles, Tell/Hint, VMS and Seven conceptual routes. |
| `RepoInfo.md` | Historical environment and hard-boundary map | Contains DB, branch, external solver split, and old operational rules; some branch facts are superseded by `rulings.md`. |
| `WorkPrinciples.md` | Historical work-principles expansion | Preserves star-system inheritance, no-do list, POC and pipe naming warnings. |
| `RulePointers.md` | Historical rule index | Routes into `.devin/rules/` and POC rule descriptions. |
| `MemoryArchive.md` | Historical cross-session memory | Preserves VMS, fifth-generation and first-principles handoff facts. |
| `SystemAssets.md` | Historical asset index | Routes to primitives, concept files, and generation documentation. |
| `Glossary.md` | Historical glossary | Useful term route; current topic route is `docs/domain/README.md`. |

## System Directories

| Path | Current role | Retention reason |
|---|---|---|
| `system/` | Sixth-generation implementation island | Code and docs are still evidence for sixth-generation claims. |
| `seven-system/` | Seven evidence-factory island | Has its own AGENTS, docs, schemas, code, and tests. |
| `eight-system/` | Non-specialization refinement island | Preserves overdesign investigation and refined POC/system ideas. |
| `analysis-devin-failure-system/` | Analysis-system historical/residual island | Active solve-side systems are external unless current evidence says otherwise. |
| `evidence/history/tell-research/` | Tell/non-specialization research record moved from the old root | Numbered documents and POC assets preserve research chronology without acting as current truth. |
| `docs/history/sixth-generation/legacy-spec/` | Legacy sixth-generation specification moved from the old root | Historical design route; canonical current docs supersede it. |
| `docs/history/sixth-generation/rnd/` | Sixth-generation R&D source moved from the old root | Preserves protocols, results, failures and route replacement history. |
| `第五代系统技术说明书/` | Fifth-generation documentation | Conceptual lineage for prior generations. |
| `原语化AI数学工程系统设计/` | Primitive-system design archive | Preserves primitive and two-tree design ideas. |
| `primitives/`, `concepts/`, `criteria/`, `facets/` | Primitive knowledge structure | Historical design and reference material. |
| `任务追踪/` | Historical task tracking | Useful for old active-state recovery; current state is now root `MEMORY.md`. |
| `runs/`, `palyground/`, `subagents-dirs/` | Runtime and extraction evidence | Baseline-committed evidence. Do not treat all run outputs as current truth. |

## Migrations And Replacements

| Old path | New/current route | Commit / evidence | Reason |
|---|---|---|---|
| `knowledge/arxiv/` corpus body | `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/knowledge/arxiv/` plus `knowledge/arxiv/README.md` | `e52927f`, `external-large-data-migration-map.tsv` | High-volume external corpus pointerized for cognitive-closure efficiency. |
| `knowledge/problem_banks/` corpus body | `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/knowledge/problem_banks/` plus `knowledge/problem_banks/README.md` | `e52927f`, `external-large-data-migration-map.tsv` | Large problem data must not be active Git body content. |
| In-repo solver systems | `~/master-mind-normal-solver/` and `~/master-mind-analysis-system/` | commits `0f54bf4`, `d80201f`, `e318b58`; root `RepoInfo.md` | Active solver work moved to independent repos to avoid AGENTS/running-system interference. |
| Old AGENTS long-form sections | Root route docs such as `GroveCoreCognition.md`, `RepoInfo.md`, `WorkPrinciples.md`, `RulePointers.md` | commits around 2026-08-19 | AGENTS slimming moved details to route documents instead of deleting them. |

## Deletion Rule

Future deletions or migrations must add:

- old path;
- new path or Git/history pointer;
- commit;
- reason;
- verification or recovery evidence.

If any of these is missing, do not claim the content was safely removed.
