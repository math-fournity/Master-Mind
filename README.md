# README.md - Math Master Manufacturing System Registry

This branch is the active reconstruction of the sixth-generation Math Master system as a current-state repo.
The working tree still contains historical super-repo source islands while extraction and migration are in
progress; those paths are evidence sources, not current components unless the canonical sixth-generation docs
and implementation say so.

## Start Here

1. Read `AGENTS.md` for the constitution and hard boundaries.
2. Read `feature-list.md` for current requirements.
3. Read `MEMORY.md` for current state and next actions.
4. Read `rulings.md` for user decisions.
5. Use the system registry below to select the relevant island.
6. Use `docs/history/` and Git evidence when a claim depends on evolution, replacement, or deletion.
7. For the active sixth-generation reconstruction, read `dev-docs/sixth-gen-current-repo/` and its report before
   interpreting old-generation documents or moving any path.

## Sixth-Generation Current State

| Concern | Canonical current route |
|---|---|
| Product scope and delivery | `docs/product/sixth-generation-scope.md` |
| Trace/Tell/Hint/Grove/FCA concepts | `docs/domain/sixth-generation-concepts.md` |
| Current and target architecture | `docs/design/system/sixth-generation-architecture.md` |
| Exact current contracts and stubs | `docs/design/detailed/sixth-generation-current-contracts.md` |
| AI roles, Prompt, isolation and qualification | `docs/ai/sixth-generation-runtime-and-prompt-contracts.md` |
| DB, files, D disk and secret boundaries | `docs/data/sixth-generation-data-boundaries.md` |
| Tests, POC verdicts and evidence limits | `docs/quality/sixth-generation-evidence-and-qualification.md` |
| Safe and prohibited runtime actions | `docs/operations/sixth-generation-runtime-boundaries.md` |
| Lineage, supersession and recovery | `docs/history/sixth-generation-route-replacements.md` |
| Prompt asset routing | `prompts/README.md` |
| Evidence routing | `evidence/README.md` |

Current implementation verdict: the complete four-Pipe/Grove loop is not implemented. The verified current
core is the independent solve-side structured-trajectory offline toolchain, which passed 295 tests on
2026-08-24; live model roles remain unqualified and unauthorized.

## Current Governance Entry Points

| Asset | Role |
|---|---|
| `AGENTS.md` | Project constitution, cognitive-closure-first rule, Git/data/external-system boundaries |
| `feature-list.md` | Current requirements and acceptance criteria |
| `MEMORY.md` | Current status, verified facts, active work, open questions |
| `rulings.md` | User rulings, including branch/tag authorization, 416 preservation, and D disk offload |
| `docs/README.md` | Stable knowledge topic index |
| `dev-docs/README.md` | Investigations, baselines, manifests, and transition notes |
| `dev-docs/sixth-gen-current-repo/` | Active reconstruction constitution, reverse-history report, source inventory, concept ledger, and migration map |
| `认知闭包/` | Auditable cognitive-closure records |
| `.codex/governance/` | Project-local governance extensions not yet promoted to the global framework |

## System Islands

| Island | Main paths | Current interpretation |
|---|---|---|
| Root historical cognition | `GroveCoreCognition.md`, `RepoInfo.md`, `WorkPrinciples.md`, `RulePointers.md`, `MemoryArchive.md`, `SystemAssets.md`, `Glossary.md` | Legacy high-value maps. Current governance routes through this README plus `docs/`; old files remain as historical evidence. |
| Astrology / star-system inheritance | historical root docs and Git commits around 2026-07-07 to 2026-07-10 | Historical inheritance layer. Concepts are traceable through `docs/history/system-lineage.md` and Git log. |
| First five Math Master generations | `第五代系统技术说明书/`, `原语化AI数学工程系统设计/`, `primitives/`, `concepts/`, `criteria/`, `facets/` | Historical design and primitive-system lineage. Not the single current implementation. |
| Grove / VMS / first-principles loop | `GroveCoreCognition.md`, `任务追踪/`, VMS-related dev-docs | Core historical concept family: guide tree, solver tree, tell/hint, VMS, Grove loop. |
| Sixth-generation implementation | `system/`, `SixthGenRnD.md`, `第六代系统技术说明书/`, `第六代系统研发过程文档/` | Main in-repo implementation island for sixth-generation code and run assets. Read `system/README.md` before code claims. |
| Sixth-generation current repo reconstruction | `dev-docs/sixth-gen-current-repo/`, branch `codex/sixth-gen-current-repo-2026-08-24` | Active transition lane. It determines which sixth-generation facts become canonical and which old paths become extracted or history-only. |
| Tell taxonomy and non-specialization research | `Tell分类学研究过程文档/`, `POC-2.7/`, `dev-docs/385*`, `dev-docs/394*` to `399*` | Research and POC lineage for Tell/Hint, non-specialization, and overdesign investigations. |
| Analysis / Devin failure system remnants | `analysis-devin-failure-system/`, `AnalysisSystemDesign.md`, `AnalysisSystemOps.md`, `AnalysisSystem开发/` | Historical/residual in this repo. Active solve-side systems are external unless current files prove otherwise. |
| Seven evidence factory | `seven-system/`, `seven-system非特化证据工厂研发过程文档/` | In-repo Seven island with its own `AGENTS.md`, docs, contracts, and tests. Respect its isolation rules. |
| Eight refinement system | `eight-system/` | Non-specialization refinement and overdesign response island, including project runs and scripts. |
| External solver systems | `~/master-mind-normal-solver/`, `~/master-mind-analysis-system/` | Not governed by this repo's root files. Enter those repos and read their `AGENTS.md` before work. |
| External large data | `knowledge/README.md`, `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/` | Large corpus/problem-bank bodies live on D disk. This repo stores pointers, manifests, and migration evidence. |

## Stable Topic Index

Use `docs/README.md` for stable knowledge:

- `docs/product/README.md`: project scope and non-goals.
- `docs/domain/README.md`: terminology and concept families.
- `docs/design/system/README.md`: system boundaries and island topology.
- `docs/design/detailed/README.md`: exact contracts when stable.
- `docs/decisions/README.md`: adopted decisions and ADR-style records.
- `docs/interfaces/README.md`: CLIs, APIs, schemas, and cross-repo interfaces.
- `docs/data/README.md`: data roots, D disk offload, DB boundaries.
- `docs/quality/README.md`: verification and audit evidence.
- `docs/security/README.md`: secrets, sensitive docs, external-system limits.
- `docs/operations/README.md`: runbooks and operational constraints.
- `docs/development/README.md`: development workflow and Git discipline.
- `docs/releases/README.md`: tags, branches, release notes.
- `docs/ai/README.md`: AI roles, prompts, tools, trajectories, leakage controls.
- `docs/history/README.md`: lineage, legacy assets, migrations, and Git-log index.
- `docs/reference/README.md`: reference files and external pointers.

## Historical Lineage

The main history layer is:

- `docs/history/system-lineage.md`
- `docs/history/legacy-assets.md`
- `docs/history/git-log-lineage.tsv`

These files connect old concepts and directories to the Git timeline. They do not replace the old artifacts;
they make the old artifacts findable.

## Large Data

Large external data was moved out of the active working tree during governance alignment:

- D disk root: `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/`
- Offload note: `dev-docs/external-large-data-offload-2026-08-24.md`
- Migration map: `dev-docs/governance-alignment-manifests/external-large-data-migration-map.tsv`
- Verification: `dev-docs/governance-alignment-manifests/external-large-data-post-copy-verification.json`

Future work should add large problem data to D disk and commit only pointers plus verification evidence.
