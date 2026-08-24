# rulings.md - User Rulings

This file records user decisions that govern future interpretation. It preserves authority and context; it is
not a place for AI to invent requirements.

## R-001 - 2026-08-24 - Implement Governance Alignment Plan

The user instructed Codex to implement the Math Master Manufacturing repo governance alignment plan. Required
effects include baseline sealing, an explanatory tag, a new branch, root governance skeleton, system lineage,
file auditability, history traceability, and final verification.

## R-002 - 2026-08-24 - Branch Authorization

The user authorized creating `codex/governance-alignment-2026-08-24` after the pre-alignment tag. This overrides
the older general `RepoInfo.md` rule that ordinary work should remain on `glm5.2`, but only for this governance
alignment.

## R-003 - 2026-08-24 - 416 Document Preservation

The user chose to preserve the 416 proxy/network document in original form even though it contains
credential-like material. Future reports may mention that the risk exists, but must not quote or display the
sensitive value.

## R-004 - 2026-08-24 - Large Problem Data Goes To D Disk

The user updated the objective: if large-scale problem data is found, move it to D disk storage instead of
committing it into this repository. This alignment implemented the rule for `knowledge/problem_banks/` and also
applied the same project-local pointerization pattern to high-volume `knowledge/arxiv/` corpus data.

## R-005 - 2026-08-24 - Project-Local Governance Innovation

The user allowed project-local governance adjustments under this repository's `.codex/` directory, provided
they explain why they differ from the global standard and preserve experience for later evaluation. These local
extensions do not automatically change `~/codex`.

## R-006 - 2026-08-24 - Subagent Constraint

The user does not want subagents used unless Codex first explains the strategy and receives explicit approval.
This alignment was implemented without subagents.

## R-007 - 2026-08-24 - No Push Or External Runtime Side Effects

The governance alignment is local. Do not push, write databases, start external solver batches, or run external
systems unless the user separately authorizes that action.

## R-008 - 2026-08-24 - Sixth-Generation Current Repo Working Constitution

The user narrowed the next governance objective: instead of canonicalizing the entire historical super repo,
future work should turn this worktree into a sixth-generation current-state repo. The action guide should be
persisted so future sessions after context compression can find and follow it. The project `AGENTS.md` should
carry the binding short constitution, and the complete guide should live under
`dev-docs/sixth-gen-current-repo/action-guide-2026-08-24.md` until superseded by an explicit user ruling.
