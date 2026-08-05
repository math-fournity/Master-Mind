---
name: moira-runtime
description: Read MOIRA's nonlinear runtime capsule and protocol anchors before acting.
allowed-tools:
  - read
  - grep
  - glob
  - exec
triggers:
  - user
  - model
---

Run `python3 tools/moira_runtime.py capsule --role master --format text` before making a project-control decision.

Treat the capsule as the fresh control context. It is stronger than memory and terminal impressions. If the capsule says `CONTINUE_REQUIRED`, do not stop. If it says `REVIEW_REQUIRED`, repair protocol drift or inspect failed evidence before dispatching more work.

Use `python3 tools/moira_runtime.py protocol-audit --format text` when rules, docs, skills or hooks have changed.
