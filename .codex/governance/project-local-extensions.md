# Project-Local Governance Extensions

This repository is a super repo with multiple historical systems, large external data, and several AI-runtime
evidence layers. It follows the global governance framework, but keeps a small project-local extension area
under `.codex/governance/` for practices that are needed here before they are proven general enough to move
into `~/codex`.

## Current Extensions

### External Large-Data Pointerization

Global rule being preserved: future AI must be able to build a fast, complete, evidence-traceable cognitive
closure before answering or acting.

Project-local extension: large corpus and problem-bank bodies are stored on D disk, while this repo stores
pointers, checksums, migration maps, and lineage notes.

Reason this repo needs the extension:

- The active project tree contained gigabyte-scale external corpora.
- These files are evidence and data, but not the right first-load cognition surface for future AI sessions.
- A future AI needs to know that the data exists and how to verify it; it does not need thousands of corpus
  files in normal Git review.

Current implementation:

- `knowledge/arxiv/README.md`
- `knowledge/problem_banks/README.md`
- `dev-docs/external-large-data-offload-2026-08-24.md`
- `dev-docs/governance-alignment-manifests/external-large-data-*.tsv`
- `dev-docs/governance-alignment-manifests/external-large-data-*.json`

Verification standard:

- old path to D disk path mapping exists;
- SHA-256 copy verification passes;
- active README/docs history points to the external data root;
- no unclassified large data remains in `git status --short --untracked-files=all`.

## Upstreaming Rule

Do not change the global governance framework merely because this repo needed a project-local extension. After
this alignment is complete, compare the extension against actual verification results. Only then decide whether
the idea should be promoted into the global governance repo.
