# Sixth-Generation Current Repo Reconstruction Guide - 2026-08-24

## Purpose

This guide is the working constitution for the next reconstruction phase. Its goal is to let future Codex
sessions continue after context compression and still know exactly how to turn this repository into a
sixth-generation current-state repo.

This is not the same as the completed governance-alignment work. The previous phase made the historical super
repo auditable and traceable. This phase narrows the active worktree so it looks like a repo that was created
from day one for the sixth-generation system under the governance framework.

## Current Baseline

- Repo: `~/master-mind-glm5.2-worktree`
- Current branch at guide creation: `codex/governance-alignment-2026-08-24`
- Current HEAD at guide creation: `9f7c9fe`
- Safety tag already available: `pre-governance-alignment-2026-08-24`
- Governance alignment commits:
  - `c1b934a`: pre-governance baseline assets
  - `e52927f`: large external data offloaded to D disk
  - `9f7c9fe`: root governance skeleton, lineage, closure, validation

Do not push, rewrite history, write DBs, start solver batches, operate external systems, or use subagents unless
the user explicitly authorizes that action for the current task.

## Required First Move

Before broad migration or deletion, create a new safety tag and branch:

```bash
git tag -a pre-sixth-gen-current-repo-2026-08-24 -m "Baseline before narrowing repo to sixth-generation current system"
git switch -c codex/sixth-gen-current-repo-2026-08-24
```

If those names already exist, inspect them before choosing replacements. Do not overwrite tags or branches
without explicit user approval.

## Target State

The final active worktree should contain only the sixth-generation current system and the governance/evidence
needed to work on it:

```text
AGENTS.md
README.md
feature-list.md
MEMORY.md
rulings.md
system/
docs/
prompts/
evidence/
knowledge/
dev-docs/
认知闭包/
```

`system/` should initially keep the current package name and implementation layout. Do not rename it to a new
Python package until imports, tests, docs, and callers have been closed and verified.

## Non-Goals

- Do not canonicalize every historical generation.
- Do not keep Seven, Eight, analysis, astrology, first-five, or primitive-system directories as active root
  content unless a specific file is extracted into sixth-generation current truth.
- Do not rewrite Git history to make the old repo look clean.
- Do not preserve old directory names merely because a human or AI once used them as entry points.
- Do not delete anything silently. Git is recoverability; migration maps are current auditability.

## Source Inventory

Create these files before migration:

```text
dev-docs/sixth-gen-current-repo/source-inventory.tsv
dev-docs/sixth-gen-current-repo/concept-extraction.tsv
dev-docs/sixth-gen-current-repo/path-migration-map.tsv
```

Recommended columns:

```text
source-inventory.tsv:
path	status	size	commit_hint	system_hint	notes

concept-extraction.tsv:
concept	source_path	source_commit	claim	current_status	canonical_target	confidence	reason

path-migration-map.tsv:
old_path	new_path	action	reason	recoverability	evidence
```

Use explicit pathspecs when staging generated manifests. Do not use `git add -A`, `git add .`, or `git add -u`.

## Path Classification

Every existing path must end in exactly one class:

| Class | Meaning |
|---|---|
| `keep-current` | The path is part of the sixth-generation current repo and remains or moves to a canonical location. |
| `extract-current-knowledge` | The original path is historical, but one or more current sixth-generation facts are extracted into canonical docs. |
| `history-only` | The path is not current sixth-generation truth; it is recoverable through Git/tag/history maps. |
| `external-data` | The path is large data or large run evidence that belongs on D disk with repo pointers. |
| `exclude-local` | The path is local secret/cache/venv/temp/tool-private state and must not be committed. |
| `unknown` | Temporary investigation state only. Completion requires zero `unknown`. |

Completion requires `unknown=0`.

## Sixth-Generation Truth Priority

When sources conflict, decide current sixth-generation truth in this order:

1. Current user rulings and this guide.
2. `system/` code, `.ref`, `.ai-check`, tests, and direct run/evidence artifacts.
3. `system/docs/` that still matches the implementation.
4. `docs/history/sixth-generation/rnd/` conclusions that were confirmed by later evidence.
5. `docs/history/sixth-generation/legacy-spec/` statements that were not superseded or falsified.
6. Fifth-generation, primitive, Tell, Grove, VMS, or other legacy material only after proving it is inherited by
   the sixth-generation current system.
7. Purely historical ideas, failed routes, and superseded plans never become current truth by location alone.

Documentation alone does not prove implementation. Code existence does not prove verification. Tests prove only
their assertions and environment.

## Concept Ledger

At minimum, inspect and classify these concept families:

- sixth-generation identity and scope;
- Grove loop;
- VMS;
- Trace;
- Tell;
- Hint;
- Trace/Tell/Hint chain;
- FCA/RCA and lattice language;
- pipe architecture;
- prompt assets and AI role contracts;
- `system/vein_analysis.py`;
- `system/solve_vein_analysis/`;
- Devin/tmux development-only contracts;
- qualification packs and live-run permits;
- State Normalizer;
- Trace Auditor;
- data, DB, D-disk, and large-run boundaries;
- tests, POCs, audit receipts, and failure evidence.

Each concept must have a current canonical target or an explicit history-only decision.

## Execution Phases

1. **Branch And Baseline**
   Create the new tag and branch. Re-run `git status --short --branch --untracked-files=all`.

2. **Inventory**
   Generate source inventory for current tracked and relevant ignored paths. Exclude local secrets, venvs, caches,
   temp files, `.DS_Store`, `__pycache__`, `*.pyc`, and tool-private local state from content commits.

3. **Concept Extraction**
   Fill `concept-extraction.tsv`. Use Git log/diff and actual files for claims. Do not treat old docs as current
   truth without evidence.

4. **Target Structure**
   Draft the canonical root README, Feature rows, MEMORY direction, docs topic map, prompt/evidence/data
   boundaries, and historical replacement model.

5. **Migration**
   Move or remove paths only after `path-migration-map.tsv` has a planned row. For existing files, run
   `~/codex/tools/check_file_baseline.sh <path>...` before mutation. Prefer `git mv` for tracked
   path moves and explicit pathspec staging.

6. **Canonicalization**
   Rewrite current sixth-generation docs so future AI can start from governance entry points, then reach code,
   contracts, prompts, tests, and evidence without reading old generation folders.

7. **Reconciliation**
   Generate a final path reconciliation table. Every baseline path must be tracked/current, migrated, history-only,
   external-data, or excluded-local. `unknown` must be zero.

8. **Verification**
   Run governance validation, `git diff --check`, safe Python compile checks, safe `system` tests, link/path
   checks, and representative concept spot checks. Do not run DB-writing or external runtime commands.

9. **Commit**
   Commit in reviewable batches: baseline/plan, inventory, canonical docs, path migration, verification. Use
   explicit pathspec staging. Do not push.

## Completion Criteria

- Future AI reads `AGENTS.md`, `README.md`, `feature-list.md`, `MEMORY.md`, and can identify the repo as a
  sixth-generation current-state repo.
- Non-sixth-generation systems are no longer active root content.
- Current sixth-generation requirements, design, implementation, prompts, evidence, data, operations, AI contracts,
  and history routes are all reachable through the governance skeleton.
- Valid current facts formerly scattered through older systems are extracted into canonical sixth-generation docs.
- Superseded or historical content has replacement/history pointers.
- Final reconciliation has zero unknown paths.
- No local secrets, venvs, caches, temp files, or large data bodies are committed.
- Validation evidence is recorded in `docs/quality/`, `MEMORY.md`, and the final manifests.

## Stop Conditions

Stop and report instead of continuing if:

- a target deletion lacks recoverable Git history or migration mapping;
- a source contains sensitive material that cannot be safely summarized;
- a code move would require unverified import/package changes;
- a DB/external runtime action would be needed to prove a claim without current authorization;
- concept extraction shows the sixth-generation current truth cannot be distinguished from historical proposals.
