# Solve-side cognitive-role assets 0.3.0

This is the file-producing Devin cognitive-role profile selected after
POC-VMS-36/37 exposed self-denial of the role workspace.

- Devin CLI runs without sandbox and with `dangerous`/bypass approval mode.
- Each role's frozen `AGENTS.md` limits authority to the current workspace and
  names the only permitted outputs and local utilities.
- The dedicated CLI config does not deny a whole host volume that may contain the
  role's own workspace.
- Network access, git, nested AI/agent launch and destructive commands remain
  forbidden; sealed tool events are audited for compliance.

This profile does not claim sandbox-strength isolation. It does not qualify any
role until a newly preregistered live POC completes. Release `0.2.0` remains a
paused response-only alternative and is not silently merged into this profile.
