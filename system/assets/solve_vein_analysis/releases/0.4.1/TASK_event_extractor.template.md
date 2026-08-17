# Frozen VMS-41R1 Event Extractor Task

Attempt ID: `{{ATTEMPT_ID}}`
Case ID: `{{CASE_ID}}`
Trajectory ID: `{{TRAJECTORY_ID}}`
Problem ID: `{{PROBLEM_ID}}`

Use this exact source identity in the output:

```json
{
  "carrier": "fixture",
  "source_artifact_ref": "raw_solver_trajectory.txt",
  "source_artifact_sha256": "{{SOURCE_SHA256}}"
}
```

Read `problem.md`, `raw_solver_trajectory.txt`,
`reasoning-trajectory-candidate-v2.md` and `input-manifest.json`. Produce
`reasoning-trajectory-candidate-v2.json` and the exact one-line `DONE.md` marker
specified by `AGENTS.md`. Do not create any other file.

The hidden acceptable set, reference candidates, thresholds, negative checks and
blind review rubric are not in this workspace. If you see them, stop without
writing a candidate output.
