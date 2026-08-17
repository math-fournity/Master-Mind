# Frozen Event Extractor Task

Attempt ID: `{{ATTEMPT_ID}}`
Case ID: `{{CASE_ID}}`
Trajectory ID: `{{TRAJECTORY_ID}}`
Problem ID: `{{PROBLEM_ID}}`

Use this exact source identity in the output:

```json
{
  "carrier": "imported",
  "source_artifact_ref": "raw_solver_trajectory.txt",
  "source_artifact_sha256": "{{SOURCE_SHA256}}"
}
```

Read `problem.md`, `raw_solver_trajectory.txt`, and
`reasoning-trajectory-v1.md`. Produce `reasoning-trajectory.json` and the exact
one-line `DONE.md` marker specified by `AGENTS.md`. Do not create any other file.

