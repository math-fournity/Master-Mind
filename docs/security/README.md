# Security

Security facts and boundaries:

- `.env`, local secrets, virtualenvs, caches, temp files, OS metadata, and tool-private local state are not
  committed.
- `.env.example` is a tracked template. During sixth-generation reconstruction its credential-like non-placeholder
  password value was replaced by an explicit placeholder. The pre-reconstruction tag and Git history still contain
  the historical value and must be treated as sensitive; do not display it.
- The 416 proxy/network document is preserved in original form by user ruling and contains credential-like
  material. Reports must not quote or display the sensitive value.
- Do not push, write databases, start external solver systems, or operate external services without explicit
  current user authorization.
- Do not fabricate hidden reasoning or leak answer routes into experiments that require role separation.

Relevant evidence:

- `rulings.md`
- `dev-docs/governance-alignment-baseline-2026-08-24.md`
- `dev-docs/governance-alignment-manifests/excluded-local-secret-cache-temp.tsv`
