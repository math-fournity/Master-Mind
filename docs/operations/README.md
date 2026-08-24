# Operations

This repo contains operational docs for several historical systems, but governance alignment does not authorize
running them.

Routes:

- General repo environment and DB warnings: `RepoInfo.md`.
- Sixth-generation operations: `system/README.md` and `system/docs/`.
- Seven operations: `seven-system/docs/operations.md`.
- Analysis operations: `AnalysisSystemOps.md`.
- External solver operations: enter the external solver repo and read its own `AGENTS.md`.

Default boundary: no DB writes, no solver batch launches, no remote push, and no external runtime side effects
without explicit user authorization.
