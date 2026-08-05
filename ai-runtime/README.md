# MOIRA AI Work Runtime

This directory contains the runtime contract that lets Devin CLI support MOIRA without flattening the project into a linear coding backlog.

MOIRA has a nonlinear research loop. Each Worker absorbs an experience package, extracts formal dimensions, updates system maturity, evaluates computability and may generate new tasks. The runtime therefore has to re-inject current state every time an agent starts, receives a prompt or tries to stop.

The current implementation has four pieces.

1. `.devin/config.json` fixes project-level Devin import and permission policy.
2. `.devin/hooks.v1.json` injects a capsule on `SessionStart` and `UserPromptSubmit`, and blocks `Stop` when the runtime still sees queued, leased, busy or protocol-drift work.
3. `.devin/skills/` defines role skills for runtime, master, worker and auditor modes.
4. `tools/moira_runtime.py` renders the capsule and audits protocol anchors.

The provider adapter is `tools/agent_launcher.py`. Existing opencode support remains available. Devin support is activated by setting `MOIRA_AGENT_PROVIDER=devin` or passing `--provider devin` to `worker.sh`.
