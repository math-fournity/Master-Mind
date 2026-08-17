# Solve-side vein analysis runtime assets

This directory belongs only to `system.solve_vein_analysis`. It must not be
copied into, imported by, or used to overwrite `system/assets/vein_analysis/`,
which is the protected absorb-side runtime asset set.

## Roles

| Asset | Role | Input | Required output |
|---|---|---|---|
| `AGENTS_event_extractor.md` | Reasoning Event Extractor | raw Solver trajectory view | `reasoning-trajectory.json` |
| `AGENTS_state_normalizer.md` | Mathematical State Normalizer | extractor output + permitted raw spans | `normalized-reasoning-trajectory.json` |
| `AGENTS_trace_auditor.md` | Process Trace Auditor | sealed DAG/FCA/trace artifacts | `trace-audit.json` |

The deterministic POC-VMS-31 does not invoke any of these roles. Later
POC-VMS-32/33/35/36/37 experiments invoked frozen copies through the independent
solve-side role runtime. POC-VMS-35 recovered direct file writing and parseable
exports for all three roles, but its overall verdict remained
`INCONCLUSIVE_PROTOCOL` and no role reached scientific qualification. VMS-36 and
VMS-37 then proved tmux observability while exposing two self-inflicted path
denials: the workspace was first under the denied repo and then under the denied
`/Volumes/**` tree.

Asset set `0.3.0` applies the user's explicit execution decision: these
file-producing cognitive roles run without Devin sandbox and with
`dangerous`/bypass approval mode. The exact role authority is written into each
workspace `AGENTS.md`; the dedicated config no longer denies an entire filesystem
that may contain the role's own workspace. Network, recursive AI launch, git and
destructive commands remain forbidden, and tool events remain auditable.

Therefore:

- asset integrity can be tested now;
- this asset set still makes no live capability claim by itself;
- Devin file-writing execution is `TESTED_NOT_QUALIFIED` only in separate POC evidence;
- dangerous mode is an approval mechanism, not a strong isolation proof;
- compliance with an AGENTS boundary must be verified from the sealed tool-event record;
- Codex execution, production isolation and streaming remain `NOT_TESTED`;
- prompt existence must never be reported as a capability PASS;
- no role is allowed to inspect a reference solution merely because it is an AI.

`asset-manifest.json` freezes every runtime asset by SHA-256. A live adapter must
bind the exact manifest hash in its invocation receipt before it may use an asset.
The documentation-only `0.1.1` release superseded the stale README hash in
`0.1.0`; its three role prompts were byte-identical to `0.1.0`. Release `0.2.0`
is a paused response-only alternative and is not the active file-producing
profile. Release `0.3.0` is the dangerous-mode workspace-contract candidate used
by the VMS-38 debug evidence. Release `0.4.0` is the historical VMS-41 v1 Event
Extractor candidate. Release `0.4.1` is the VMS-41R1 V2 Event Extractor candidate
bound by `poc_vms_41r1.freeze.json`; it remains `LIVE_NOT_AUTHORIZED` and does
not qualify the role until a newly preregistered live POC and blind audit complete.
