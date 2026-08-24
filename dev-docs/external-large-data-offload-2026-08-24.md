# External Large Data Offload - 2026-08-24

This note records the governance-branch migration of large external data out of the active Git working tree.
The purpose is cognitive closure: future AI sessions should see where the data is, why it is outside Git, and
which checks prove that the move did not lose files.

## Scope

Moved out of the active working tree:

- `knowledge/arxiv/`
- `knowledge/problem_banks/`

Destination:

`/data/master-mind-glm5.2-worktree-external-data/2026-08-24/knowledge/`

## Why This Differs From Ordinary Repo Storage

The global governance skeleton assumes that long-lived project knowledge has stable in-repo entrypoints. This
super repo contains high-volume external corpora and problem-bank data. Storing the corpus bodies as active Git
content slows future cognition, makes ordinary review noisy, and does not improve task-relative cognitive
closure. The governance-aligned form is therefore:

- keep small curated notes in Git;
- keep large corpus bodies on D disk;
- keep repo pointers, checksums, and migration maps in Git;
- preserve the pre-offload Git state through `pre-governance-alignment-2026-08-24`;
- make the move auditable by old path, new path, size, SHA-256, and tracked/untracked status.

## Verification Evidence

- Pre-offload full physical manifest:
  `dev-docs/governance-alignment-manifests/external-large-data-pre-offload-sha256.tsv`
- Post-copy verification:
  `dev-docs/governance-alignment-manifests/external-large-data-post-copy-verification.json`
- Migration map:
  `dev-docs/governance-alignment-manifests/external-large-data-migration-map.tsv`
- Migration summary:
  `dev-docs/governance-alignment-manifests/external-large-data-migration-summary.json`

Verification result: PASS. The post-copy verification checked 12,284 files with zero missing files and zero
hash mismatches.

## Repo Pointers

- `knowledge/README.md`
- `knowledge/arxiv/README.md`
- `knowledge/problem_banks/README.md`

These files are intentionally committed even though `knowledge/` is ignored. They are the in-repo cognitive
route to the external data.

## Deletion/Migration Interpretation

The Git diff deletes historical tracked corpus files from the active branch. This is not a content-loss claim:

- Old content remains recoverable at `pre-governance-alignment-2026-08-24`.
- The full local corpus body exists on D disk at the destination path above.
- Every moved physical file has a row in the migration map.
- Future active work should treat the D disk location as the local data root.
