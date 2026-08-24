# feature-list.md - Current Requirements

This file records what the project should do now. It is not an implementation proof; implementation and
verification claims must cite code, tests, run evidence, manifests, or Git history.

## Status Semantics

- Ruling: proposed / adopted / superseded / retired.
- Delivery: not started / partial / implemented-unverified / verified.

## Governance Alignment Requirements

| ID | Type | Current requirement | Source | Ruling | Delivery | Evidence |
|---|---|---|---|---|---|---|
| GOV-001 | Cognitive closure | Future AI must be able to build task-relative, minimal sufficient, evidence-traceable cognitive closure before answering or acting. | User, 2026-08-24 | adopted | verified | `AGENTS.md`, `README.md`, `docs/README.md`, `认知闭包/2026-08-24-governance-alignment-认知闭包.md` |
| GOV-002 | Root skeleton | The repo must have the full governance skeleton: `AGENTS.md`, `README.md`, `feature-list.md`, `MEMORY.md`, `rulings.md`, `docs/*/README.md`, and `dev-docs/README.md`. | User plan, 2026-08-24 | adopted | verified | `final-validation-results.json`; governance validator PASS |
| GOV-003 | File auditability | No original file may become unknown: each path must be tracked, newly tracked, excluded as local/secret/cache, or mapped to offloaded/history evidence. | User plan, 2026-08-24 | adopted | verified | `final-file-reconciliation-summary.json`; 0 unknown |
| GOV-004 | No silent deletion | Historical content must not be deleted without old path, new path or history pointer, commit, and reason. | User plan, 2026-08-24 | adopted | verified | `dev-docs/external-large-data-offload-2026-08-24.md`, `docs/history/legacy-assets.md`, `external-large-data-migration-map.tsv` |
| GOV-005 | Historical traceability | Important concepts from every historical system generation must be reachable from root governance and Git history. | User plan, 2026-08-24 | adopted | verified | `docs/history/system-lineage.md`, `docs/history/git-log-lineage.tsv`, `history-lineage-spot-checks.tsv` |
| GOV-006 | Branch and tag discipline | Seal pre-alignment state with annotated tag, then work on `codex/governance-alignment-2026-08-24`; do not push unless authorized. | User plan, 2026-08-24 | adopted | verified | tag `pre-governance-alignment-2026-08-24`; branch `codex/governance-alignment-2026-08-24` |
| GOV-007 | Large data offload | Large problem data and high-volume external corpora must live on D disk, with repo pointers and verification manifests instead of active Git corpus bodies. | User update, 2026-08-24 | adopted | verified | `e52927f`, `knowledge/README.md`, `external-large-data-post-copy-verification.json` |
| GOV-008 | Project-local governance innovation | This repo may keep local `.codex/` governance extensions when the super-repo shape needs practices not yet promoted globally. | User update, 2026-08-24 | adopted | verified | `.codex/governance/project-local-extensions.md` |
| GOV-009 | Sensitive content handling | Preserve the 416 document in original form, but never quote or display its credential-like value in reports. | User ruling, 2026-08-24 | adopted | verified | `rulings.md`, `docs/security/README.md` |
| GOV-010 | Sixth-generation current repo reconstruction | Future work should narrow this worktree into a sixth-generation current-state repo, with the action guide treated as the binding working constitution until superseded. | User ruling, 2026-08-24 | adopted | implemented-unverified | `AGENTS.md`, `dev-docs/sixth-gen-current-repo/action-guide-2026-08-24.md`, `rulings.md` R-008 |

## System Requirements Ledger

The historical project contains many candidate systems and research lines. Current governance does not declare
all of them active. For each work request, use `README.md` and `docs/history/system-lineage.md` to identify the
right island, then verify current implementation from that island's code/docs/tests.
