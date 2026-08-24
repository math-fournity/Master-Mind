# Governance Alignment Baseline - 2026-08-24

This file records the pre-alignment baseline for `~/master-mind-glm5.2-worktree`.
It exists so later governance work can prove what was present, what was restored, what was committed,
what was excluded as local state, and what was moved out as large problem data.

## Snapshot

- Repository branch at snapshot: `glm5.2`
- Original HEAD before alignment work: `08ad266e9e3506d4d57fba372cef91516070459b`
- `git rev-list --count --all`: 1,397 commits
- Snapshot date: 2026-08-24
- Tag planned after baseline commits: `pre-governance-alignment-2026-08-24`
- Governance branch planned after tag: `codex/governance-alignment-2026-08-24`

## Restored Historical Files

- `AGENTS.md` was restored from HEAD before baseline commit. The restored content matches the prior root
  project instructions and keeps the old AI work-routing rules recoverable.
- `dev-docs/416-v0-2026-08-18-HuggingFace模型下载网络诊断与Clash代理配置经验.md` was restored from HEAD.
  This document is intentionally preserved in original form by user ruling. It contains credential-like
  material, so reports must mention the risk without displaying the sensitive value.
- `dev-docs/governance-alignment-manifests/pre_restore_git_status.txt` and
  `dev-docs/governance-alignment-manifests/pre_restore_diff_name_status.tsv` preserve the deleted-state
  evidence from immediately before restoration.

## Machine Evidence

The baseline machine manifests are under `dev-docs/governance-alignment-manifests/`:

- `baseline-summary.json`: machine-readable summary of branch, HEAD, counts, and policy counts.
- `current-file-manifest.tsv`: all filesystem paths excluding any `.git` metadata directory, with Git state,
  ignore state, include/offload/exclude policy, size, mtime, and SHA-256 where appropriate.
- `include-policy-paths.tsv`: paths intended for Git inclusion, separated from local/cache exclusions and
  large problem-data offload.
- `excluded-local-secret-cache-temp.tsv`: local secrets, virtualenv, caches, bytecode, OS files, and temporary
  files that are intentionally not submitted.
- `offload-large-problem-data.tsv`: large problem-bank paths that must be moved to D disk rather than added
  to this repository as new Git blobs.
- `problem-banks-pre-offload-sha256.tsv`: SHA-256 inventory for `knowledge/problem_banks/**` before D disk
  offload.
- `problem-banks-pre-offload-summary.json`: count and byte summary for the problem-bank offload source.
- `git-history-path-index.tsv`: path-level index derived from the full Git history.

## Inclusion Policy

The baseline separates assets into four classes:

1. Existing tracked project files remain recoverable through Git history and current HEAD.
2. Non-ignored project assets are submitted with explicit pathspec staging.
3. Ignored but project-relevant evidence such as run outputs, subagent working directories, and AGENTS backup
   evidence may be force-added with explicit pathspec staging when it is not a local secret/cache/temp file.
4. Large problem data under `knowledge/problem_banks/**` is not submitted as new Git blobs. It is registered
   for D disk offload and must be represented in the repository by manifests and pointer documents.

## Explicit Exclusions

The following classes are registered but not committed as content:

- `.env`
- `.venv/`
- `.ruff_cache/`
- `.aider*`
- `.DS_Store`
- `tmp/`
- `__pycache__/`
- `*.pyc`
- `*.pyo`
- `.pytest_cache/`
- local app or runtime private state such as `.devin/config.local.json`

## Updated User Rulings Captured By This Baseline

- The 416 document remains preserved in original form; do not quote the sensitive value in reports.
- Large problem data discovered during governance alignment must be moved to D disk storage, not newly added
  to this repository as Git blobs.
- Project-local governance innovations may be placed under this repository's `.codex/` directory when this
  super repo needs extensions beyond the global standard. Such innovations must explain why they differ from
  the global pattern and preserve verification experience for later possible upstreaming into the global
  governance framework.

## Audit Meaning

This baseline is not the final governance state. It is the frozen pre-alignment evidence layer. The final
governance branch must connect root entrypoints, feature state, memory, rulings, lineage, and offloaded
problem-data pointers back to these manifests so future AI sessions can build a fast, complete, evidence
traceable cognitive closure before answering or changing the project.
