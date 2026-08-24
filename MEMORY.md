# MEMORY.md - Current State

This file records current state for future sessions. It is a handoff surface, not a substitute for evidence.

## Current Branch And Baseline

- Current branch: `codex/governance-alignment-2026-08-24`
- Pre-alignment tag: `pre-governance-alignment-2026-08-24`
- Original HEAD before alignment work: `08ad266e9e3506d4d57fba372cef91516070459b`
- Baseline commit: `c1b934ab56d6f0554c7a7e9d89bb8b5d66b6baaa`
- Large-data offload commit: `e52927f19fcd1cbee04b245ca498eecec1f25c6d`
- No push has been performed.

## Active Goal

Use the completed governance alignment as the safety baseline for a new sixth-generation current-state repo
reconstruction. The binding working guide is
`dev-docs/sixth-gen-current-repo/action-guide-2026-08-24.md`.

## Verified Facts

- The repo had 1,397 commits across all refs before governance baseline commits.
- `AGENTS.md` and the 416 proxy/network document were restored from HEAD before baseline sealing.
- The 416 document is preserved by user ruling and contains credential-like material that must not be displayed.
- Baseline manifests are stored under `dev-docs/governance-alignment-manifests/`.
- Large data was copied to `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/` and verified by
  SHA-256 over 12,284 files with zero missing files and zero mismatches.
- The active repo stores `knowledge/` pointer README files for the offloaded data.

## Active Work

| Direction | Status | Next step | Requirement |
|---|---|---|---|
| Governance skeleton | verified | Keep root and topic docs updated as facts change | GOV-001 to GOV-006 |
| History lineage | verified | Update lineage when new system islands or migrations happen | GOV-004, GOV-005 |
| Audit closure | verified | Use the closure file as the entry for auditing this alignment | GOV-001, GOV-003 |
| Seven verification | verified | Re-run when Seven code/contracts change | GOV-003 |
| Sixth-generation current repo reconstruction | planned | Create `pre-sixth-gen-current-repo-2026-08-24` and `codex/sixth-gen-current-repo-2026-08-24`, then follow the action guide | GOV-010 |

## Open Questions

- Whether the project-local `.codex/` large-data pointerization pattern should later be promoted to the global
  governance framework. Do not promote it until this repo's final governance result has been reviewed.
- Which historical research lines should be considered active after this governance alignment. Current docs
  preserve traceability but do not make old lines active by default.

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
