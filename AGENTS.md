# AGENTS.md - Math Master Manufacturing

This file is the project constitution for `~/master-mind-glm5.2-worktree`.
It is intentionally short. Current maps live in `README.md`; current requirements live in
`feature-list.md`; current state lives in `MEMORY.md`; original user rulings live in `rulings.md`.

## First Rule: Cognitive Closure First

Before answering, designing, editing, running, or verifying anything non-trivial in this repository, build the
smallest sufficient, evidence-traceable cognitive closure for the specific task.

Minimum route:

1. Read this `AGENTS.md`.
2. Read root `README.md` to identify the relevant system island and source assets.
3. Read `feature-list.md`, `MEMORY.md`, and `rulings.md` when the task depends on current requirements,
   current state, or user decisions.
4. Read the relevant topic entry under `docs/` and then the underlying code, config, tests, run evidence, or
   historical Git facts that prove the claim.
5. State unknowns honestly. "Not found" requires scoped search evidence; it does not mean "does not exist."

The purpose of every governance file in this repo is to help future AI establish this cognitive closure quickly
and correctly.

## Repository Boundary

- Active repo path: `~/master-mind-glm5.2-worktree`
- Governance branch for this alignment: `codex/governance-alignment-2026-08-24`
- Pre-alignment tag: `pre-governance-alignment-2026-08-24`
- No push is authorized by default.
- Do not rewrite Git history.
- Use explicit pathspec staging. Do not use `git add -A`, `git add .`, or `git add -u`.
- Before editing, moving, or deleting an existing file, run
  `~/codex/tools/check_file_baseline.sh <path>...`.

The old `RepoInfo.md` rule "only work on `glm5.2`" is superseded only for the user-authorized governance
alignment branch. For ordinary future work, check `rulings.md` and `MEMORY.md` before changing branch policy.

## Current Reconstruction Constitution

The next authorized direction is to turn this worktree into a sixth-generation current-state repository, not to
canonicalize every historical system. Before starting that work, read and follow:

`dev-docs/sixth-gen-current-repo/action-guide-2026-08-24.md`

That guide is binding for the reconstruction until it is superseded by an explicit user ruling. In short:

- open a new tag and branch before any broad migration;
- preserve this governance-alignment branch as the safety baseline;
- keep only sixth-generation current code, docs, prompts, evidence, and governance in the active worktree;
- extract still-current sixth-generation knowledge from older systems before removing their visible directories;
- classify every old path as current, extracted, history-only, D-disk external data, local excluded, or unknown;
- do not allow `unknown` at completion;
- do not rewrite Git history, push, write DBs, start solver batches, or run external systems without explicit
  current authorization.

## System Islands

This is a super repo, not one clean application. Treat each island as a bounded historical or active system:

- root governance and historical maps;
- astrology / star-system inheritance material;
- first five Math Master generations;
- Grove / VMS / first-principles system design;
- sixth-generation implementation under `system/`;
- Tell taxonomy and non-specialization research under `Tell分类学研究过程文档/`;
- analysis / Devin failure system remnants under `analysis-devin-failure-system/`;
- Seven evidence factory under `seven-system/`;
- Eight non-specialization refinement under `eight-system/`;
- external solver repos outside this repo.

Do not collapse these islands into one current architecture. Use `README.md` and `docs/history/` to find the
right lineage before making claims.

## Data, Secrets, and External Systems

- Large corpora and problem-bank bodies are stored on D disk, not as active Git content. See
  `knowledge/README.md` and `dev-docs/external-large-data-offload-2026-08-24.md`.
- Do not commit `.env`, virtualenvs, caches, temp files, OS metadata, local app state, or tool-private state.
- The 416 proxy/network document is preserved by user ruling and contains credential-like material. Do not
  quote or display the sensitive value.
- Do not run commands that write ArangoDB, start solver batches, push to remotes, or operate external systems
  unless the user explicitly authorizes that action for the current task.

## AI and Subagent Policy

- Do not use subagents unless the user explicitly approves the strategy first.
- For AI-system semantics, prompts, roles, trajectories, evals, judges, leakage, or tool permissions, load the
  applicable governance skills and `docs/ai/README.md`.
- Preserve public run evidence and explicit artifacts; do not fabricate or request hidden chain-of-thought.

## File Roles

- `README.md`: system registry and routing map.
- `feature-list.md`: current requirements and acceptance criteria.
- `MEMORY.md`: current state, verified facts, active directions, and open issues.
- `rulings.md`: user decisions and authority boundaries.
- `docs/`: stable knowledge by topic.
- `dev-docs/`: investigations, transition notes, manifests, and unsettled work.
- `认知闭包/`: auditable cognitive-closure records.
- Code, config, tests, run outputs, database observations, and Git history are evidence; summary files only route
  to that evidence.
