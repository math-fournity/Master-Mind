# Evidence

This is the canonical routing entry for sixth-generation verification and run evidence. It contains pointers,
not copied large run bodies.

Current in-repo evidence:

- offline tests and frozen fixtures: `system/tests/solve_vein_analysis/`;
- absorb-side historical POC assets: `system/tests/vein_analysis/` when present;
- evidence and qualification interpretation: `docs/quality/sixth-generation-evidence-and-qualification.md`;
- reconstruction manifests: `dev-docs/sixth-gen-current-repo/`.
- Tell/non-specialization research and POC history: `evidence/history/tell-research/`.

External/local evidence:

- solve-side POC bundles: `/data/master-mind-solve-vein-data/`;
- offloaded large knowledge/problem data:
  `/data/master-mind-glm5.2-worktree-external-data/2026-08-24/`.

Every claim must identify its evidence layer: static code, offline test, development canary, manual audit, hidden
join, live qualification, or observed runtime. A PASS at one layer does not imply the next. Sealed attempts and
negative evidence are append-only and must not be overwritten.
