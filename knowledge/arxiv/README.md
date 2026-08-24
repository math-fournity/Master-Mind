# arXiv Corpus Pointer

The arXiv fulltext corpus previously present under `knowledge/arxiv/` was moved out of the active Git working
tree during governance alignment because it is high-volume external reference data.

- Old repo path: `knowledge/arxiv/`
- Local storage path: `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/knowledge/arxiv/`
- Pre-alignment tag: `pre-governance-alignment-2026-08-24`
- Migration verification:
  - `dev-docs/governance-alignment-manifests/external-large-data-pre-offload-sha256.tsv`
  - `dev-docs/governance-alignment-manifests/external-large-data-post-copy-verification.json`

Future AI sessions should use this file as the route to the corpus. The repository keeps the pointer and
checksums, not the corpus body.
