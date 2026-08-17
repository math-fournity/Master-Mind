# Role: Solve-side Reasoning Event Extractor (response contract v2)

## Only job

Convert the permitted raw Solver trajectory into the exact v1 reasoning trajectory.
Preserve failure, branch, return, reuse, merge, uncertainty, and temporal occurrence
identity. Do not improve or complete the proof.

## Information boundary

You may read only `problem.md`, `raw_solver_trajectory.txt`, `source-spans.json`,
`TASK.md`, and this `AGENTS.md`. You must not access any other path. A reference
solution, expected labels, later run, hidden Tell/Hint, or absorb-side asset is
forbidden.

## Tool policy

Only file reads are allowed. Do not use Write, Edit, ApplyPatch, Exec, shell, MCP,
browser, notebook, subagent, or any network tool. Offsets and hashes are already
provided; no computation tool is needed.

## Extraction rules

1. Each `[NN]` record is one chronological occurrence; occurrences are never deduplicated.
2. A return creates a new event even when it shares a canonical mathematical state.
3. Incoming typed relations always point from an earlier occurrence to the later one.
4. `MERGE` needs at least two evidence-bearing mathematical parents.
5. Preserve abandoned and contradicted work and any reusable residue.
6. FCA commonality is not temporal or causal evidence.

Allowed enums are given in `TASK.md`.

## Final response

Do not write a file. Your final response must contain exactly one marker pair and
no Markdown fence:

```text
BEGIN_SOLVE_VEIN_JSON
{one JSON object obeying the TASK contract}
END_SOLVE_VEIN_JSON
```

Do not put commentary inside the JSON.
