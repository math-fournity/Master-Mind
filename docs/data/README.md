# Data

## Current Sixth-Generation Data Boundary

Read `sixth-generation-data-boundaries.md` for the exact distinction between Python types, DB adapter code,
unverified live ArangoDB, structured trajectory files, fixtures, D-disk bodies, secrets, and local state.

Data in this super repo is split into active Git knowledge, offloaded local data, ignored local state, and
external runtime/database state.

## Active Git Data

Small curated knowledge notes and evidence pointers may live in Git.

## D Disk Data

Large corpora and problem-bank bodies live at:

`/data/master-mind-glm5.2-worktree-external-data/2026-08-24/`

Evidence:

- `knowledge/README.md`
- `dev-docs/external-large-data-offload-2026-08-24.md`
- `dev-docs/governance-alignment-manifests/external-large-data-migration-map.tsv`
- `dev-docs/governance-alignment-manifests/external-large-data-post-copy-verification.json`

## Excluded Local State

Do not commit `.env`, `.venv/`, caches, temp files, OS metadata, local tool state, DB files, or bytecode.
Baseline exclusions are listed in
`dev-docs/governance-alignment-manifests/excluded-local-secret-cache-temp.tsv`.

## Databases

ArangoDB use is not authorized by default. If a future task requires DB reads or writes, first read
`RepoInfo.md`, current rulings, and the relevant island docs, then obtain the needed user authorization for any
write or external runtime action.
