# Quality And Verification

Verification must be proportional to the claim.

Current governance-alignment evidence:

- Governance layout validation: `~/codex/tools/validate_governance_repo.sh`.
- Whitespace/path validation: `git diff --check`.
- Baseline file manifest: `dev-docs/governance-alignment-manifests/current-file-manifest.tsv`.
- Final file reconciliation: `dev-docs/governance-alignment-manifests/final-file-reconciliation-summary.json`.
- Historical concept spot checks: `dev-docs/governance-alignment-manifests/history-lineage-spot-checks.tsv`.
- Large-data copy verification: `external-large-data-post-copy-verification.json`.
- History lineage: `docs/history/git-log-lineage.tsv`.
- Auditable cognitive closure: `认知闭包/2026-08-24-governance-alignment-认知闭包.md`.
- Final validation summary: `dev-docs/governance-alignment-manifests/final-validation-results.json`.

Code claims require tests or compile checks from the relevant island. Do not treat documentation edits as
implementation or verification.
