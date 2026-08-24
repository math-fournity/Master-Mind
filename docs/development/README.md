# Development

## Sixth-Generation Current Contract

Read `sixth-generation-development-contracts.md` for the current `.py/.ref/.ai-check`, Prompt/runtime asset,
evidence, baseline versioning, test, Git, and migration rules. It replaces active dependence on the historical
`.devin/rules/` tree; old rules remain recoverable from the reconstruction safety tag.

Development rules:

- Build cognitive closure before non-trivial work.
- Check file baseline before editing existing files.
- Use explicit pathspec staging; do not use `git add -A`, `git add .`, or `git add -u`.
- Preserve unrelated user changes.
- Keep large problem data and high-volume external corpora on D disk with pointers and manifests.
- Update only the governance truth source that owns the fact.

Project-local governance extensions are under `.codex/governance/`. They are experimental for this repo and do
not automatically change the global framework.
