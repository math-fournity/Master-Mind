# AI Contracts

## Current Sixth-Generation Contract

Read `sixth-generation-runtime-and-prompt-contracts.md` for role visibility, active Prompt versions, runtime
isolation, trajectory/failure semantics, VMS qualification limits, and the live-authorization boundary.

AI work in this repo is governed by cognitive closure, role separation, and evidence discipline.

Current contracts:

- Read `AGENTS.md` and root governance entrypoints before non-trivial repo work.
- Do not use subagents without explicit user approval.
- Do not fabricate or require hidden chain-of-thought.
- Preserve trajectories and public run artifacts as evidence when they exist.
- Do not leak answers into tests or prompts that are meant to evaluate guidance.
- For model/prompt/agent/tool/eval changes, load the relevant AI-system governance skill and verify against the
  affected island's files.

Historical AI concepts such as Grove, Tell/Hint, VMS, Seven, and Eight are routed through
`docs/history/system-lineage.md` and the island docs listed in root `README.md`.
