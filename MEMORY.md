# MEMORY.md - Current State

This file records current state for future sessions. It is a handoff surface, not a substitute for evidence.

## Current Branch And Baseline

- Current branch: `codex/sixth-gen-current-repo-2026-08-24`
- Pre-alignment tag: `pre-governance-alignment-2026-08-24`
- Reconstruction safety tag: `pre-sixth-gen-current-repo-2026-08-24`
- Original HEAD before alignment work: `08ad266e9e3506d4d57fba372cef91516070459b`
- Baseline commit: `c1b934ab56d6f0554c7a7e9d89bb8b5d66b6baaa`
- Large-data offload commit: `e52927f19fcd1cbee04b245ca498eecec1f25c6d`
- No push has been performed.

## Active Goal

Use the completed governance alignment as the safety baseline for the active sixth-generation current-state
repo reconstruction. The binding working guide is
`dev-docs/sixth-gen-current-repo/action-guide-2026-08-24.md`.

## Verified Facts

- The repo had 1,397 commits across all refs before governance baseline commits.
- `AGENTS.md` and the 416 proxy/network document were restored from HEAD before baseline sealing.
- The 416 document is preserved by user ruling and contains credential-like material that must not be displayed.
- Baseline manifests are stored under `dev-docs/governance-alignment-manifests/`.
- Large data was copied to `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/` and verified by
  SHA-256 over 12,284 files with zero missing files and zero mismatches.
- The active repo stores `knowledge/` pointer README files for the offloaded data.
- The reconstruction branch was created from the clean governance state and is protected by
  `pre-sixth-gen-current-repo-2026-08-24`.
- First reverse investigation commit: `d84ee11`.
- The first current-tree inventory covers 19,286 paths: 6,184 tracked, 13,100 ignored, and the 2 inventory
  files generated during collection. The generated inventory paths are now committed investigation assets, not
  pre-existing untracked project content. The initial 69 `unknown` paths have now been classified as 43
  `keep-current`, 7 `extract-current-knowledge`, 18 `history-only`, and 1 `exclude-local`; literal unknown is zero.
- `.env.example` is a tracked safe template and is `keep-current`; only `.env` and actual local secret state are excluded.
- Path comparison for the manifests must use `LC_ALL=C`; the default macOS locale can treat distinct Chinese
  filenames as collation-equivalent and produce false matches or false duplicate reports.
- The initial path maps contain 5,795 pending candidate actions. Unknown zero does not mean migration complete.
- `dev-docs/sixth-gen-current-repo/reverse-git-log.tsv` contains one row for each of the 1,401 commits visible
  from all refs, in newest-to-oldest order.
- Canonical sixth-generation scope, concepts, architecture, detailed contracts, AI, data, quality, operations,
  and history routes now exist under `docs/`; `prompts/` and `evidence/` provide non-duplicating asset entries.
- `PYTHONPATH=. python3 -m pytest system/tests/solve_vein_analysis` collected and passed 294 tests in 13.29s
  on Python 3.14.6/pytest 9.1.1/darwin. One test-return warning remains.
- Current code proves the complete Grove/four-Pipe system is not implemented: entry loaders, Solver exploration,
  solve-mode vein analysis, Trace/Tell matching, Tell deposit, Hint extraction, Guide expansion, and tree persistence
  remain stubs or explicit `NotImplementedError` paths.
- `.env.example` contained a non-placeholder credential-like password value. The current branch now uses an
  explicit placeholder; the safety tag and Git history remain sensitive and the historical value must not be shown.

## Active Work

| Direction | Status | Next step | Requirement |
|---|---|---|---|
| Governance skeleton | verified | Keep root and topic docs updated as facts change | GOV-001 to GOV-006 |
| History lineage | verified | Update lineage when new system islands or migrations happen | GOV-004, GOV-005 |
| Audit closure | verified | Use the closure file as the entry for auditing this alignment | GOV-001, GOV-003 |
| Seven verification | verified | Re-run when Seven code/contracts change | GOV-003 |
| Sixth-generation current repo reconstruction | in progress | Reconcile stale `system/docs` status/counts against canonical docs, then close 5,795 pending path actions before migration | GOV-010 |

## Open Questions

- Whether the project-local `.codex/` large-data pointerization pattern should later be promoted to the global
  governance framework. Do not promote it until this repo's final governance result has been reviewed.
- Which historical research lines should be considered active after this governance alignment. Current docs
  preserve traceability but do not make old lines active by default.
- Which specific facts from Grove, VMS, Tell/Hint, Seven, Eight, and analysis-system materials remain current
  sixth-generation truth after code/test/diff reconciliation.

## Log

### 2026-08-24 - Baseline Sealed

Created `c1b934a` on `glm5.2`, then annotated `pre-governance-alignment-2026-08-24` and switched to
`codex/governance-alignment-2026-08-24`.

### 2026-08-24 - Large Data Offloaded

Moved high-volume `knowledge/arxiv/` and `knowledge/problem_banks/` bodies to D disk, committed repo pointers
and verification evidence in `e52927f`.

### 2026-08-24 - Governance Alignment Verified

Validation evidence is in `dev-docs/governance-alignment-manifests/final-validation-results.json`: governance
layout PASS, `git diff --check` PASS, POC-2.5c scripts `py_compile` PASS, Seven tests `2385 passed`, D disk
offload verification PASS, and baseline file reconciliation PASS with 0 unknown paths.

### 2026-08-24 - Sixth-Generation Reconstruction Guide Added

The user narrowed the next objective from full historical canonicalization to a sixth-generation current-state
repo reconstruction. The working constitution is now rooted in `AGENTS.md` and detailed in
`dev-docs/sixth-gen-current-repo/action-guide-2026-08-24.md`.

### 2026-08-24 - Sixth-Generation Reverse Investigation Started

Created `pre-sixth-gen-current-repo-2026-08-24`, switched to
`codex/sixth-gen-current-repo-2026-08-24`, and committed the first investigation assets in `d84ee11`:
the full current-tree source inventory, path migration map, 1,401-commit reverse index, 19-concept ledger,
and the first investigation report. No content migration had started at this commit.

### 2026-08-24 - Initial Unknown Paths Classified

Resolved all 69 initial unknown paths without moving content. The byte-exact manifests contain 19,286 unique
paths with matching path sets and zero literal unknown. The remaining 5,795 candidate actions still require
concept-level code/test/history evidence before they can become keep, extract, or history-only decisions.

### 2026-08-24 - Canonical Sixth-Generation Cognition Established

Created a breadth-first current cognition layer across product, domain, system design, detailed contracts, AI,
data, quality, operations, and history, plus Prompt/evidence root routes. Direct code inspection established the
partial implementation boundary, and 294 solve-side offline tests passed with one warning. No DB, Devin, tmux,
Solver, network, or live qualification action was performed. Sanitized `.env.example` without displaying its
historical credential-like value.
