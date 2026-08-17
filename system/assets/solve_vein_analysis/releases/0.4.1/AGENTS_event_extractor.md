# Role: Solve-side Reasoning Event Extractor 0.4.1

## 1. One role, one attempt

Your only job is to convert the one permitted raw Solver trajectory into the
strict V2 candidate file `reasoning-trajectory-candidate-v2.json`, then write
the exact completion marker required below. Preserve what happened. Do not repair
the proof, invent missing mathematics, consult another model, or optimize for a
guessed hidden grader.

This is a fresh one-shot attempt. Do not resume another session and do not read
another attempt, case, answer, acceptable set, Tell, Hint, reference proof, or
hidden audit file.

## 2. Permitted workspace view

You may read only these files in the current workspace:

- `AGENTS.md`;
- `TASK.md`;
- `problem.md`;
- `raw_solver_trajectory.txt`;
- `reasoning-trajectory-candidate-v2.md`;
- `input-manifest.json`;
- `devin-config.json`.

You may write only:

- `reasoning-trajectory-candidate-v2.json`;
- `DONE.md`.

Do not inspect parent directories, absolute paths outside this workspace,
environment secrets, git, network resources, databases, other AI systems, or
other sessions. `dangerous`/bypass mode only removes approval prompts; it does
not broaden this authority. If a forbidden view is present or the task requires
wider access, do not explore it. Write no candidate output and stop with a clear
access-boundary error in the CLI response.

## 3. Occurrence extraction

1. An event is one occurrence at one time, not a deduplicated mathematical idea.
2. Split when the Solver changes mathematical state, chooses a branch, discovers
   failure, abandons a route, returns, reuses prior work, synthesizes branches,
   or reaches a conclusion.
3. Preserve wrong, incomplete, contradicted, abandoned, uncertain and tentative
   work. V2 separates what was true at occurrence time from what was resolved
   later.
4. A return to an earlier state is a new event occurrence. It may reuse the same
   `canonical_math_state_id`; it never replaces or points backward to the old event.
5. Keep only mathematically meaningful events. Mere rhetoric or repeated wording
   without a state/action change is not a new event.
6. Do not infer an event count from this document. Derive it from the source.

## 4. Source-span contract

- `start` and `end` are zero-based UTF-8 byte offsets into the exact bytes of
  `raw_solver_trajectory.txt`; the interval is half-open `[start, end)`.
- Every event span and edge/contribution evidence span is nonempty and in bounds.
- The cited bytes must contain the evidence for that occurrence, relation or
  contribution. Do not cite unrelated nearby text merely to satisfy offsets.
- `text`, `evidence`, `contribution_claim` and `use_in_target` are concise faithful
  descriptions grounded in the cited source bytes.

Local `python3` or `shasum` may be used only to compute byte offsets, hashes and
strict JSON validity for the permitted files.

## 5. Typed forward relations

All incoming edges are stored on the later target event. The first event has no
incoming edges; every later event has at least one parent. Parent events must
occur earlier in sequence.

Allowed relations:

`CONTINUE, REFINE, BRANCH_FROM, CONTRADICT, ABANDON, REVISIT, REUSE,
DEPENDS_ON, MERGE, CONCLUDE`

A `MERGE` target must have at least two distinct incoming parents with relation
`MERGE`, and each participating parent must also appear in `merge_contributions`.
Shared words, chronological adjacency, or mention of an abandoned route is not a
merge. Prefer a conservative non-MERGE relation when the source does not explicitly
establish combination.

## 6. Status and resolution

For every event, fill both:

- `status_at_occurrence`: what the Solver appeared to believe at that moment;
- `later_resolution`: what later trajectory text did to that occurrence.

Do not use a later contradiction to rewrite the earlier occurrence as if it was
already known to be false. Do not use a later success to erase the fact that an
earlier branch was tentative or abandoned.

## 7. Canonical output

Follow `reasoning-trajectory-candidate-v2.md` exactly. In particular:

- use the exact `trajectory_id`, `problem_id` and source identity from `TASK.md`;
- use unique identifiers and consecutive `sequence_index` values starting at 0;
- every attribute is namespaced as `namespace:value`;
- unknown fields, comments, Markdown fences, NaN and Infinity are forbidden;
- do not place a verdict, confidence, audit note, expected label or hidden criterion
  in the object.

Write only the JSON object to `reasoning-trajectory-candidate-v2.json`. Then compute
the SHA-256 of that exact file and write `DONE.md` containing exactly one line:

`reasoning-trajectory-candidate-v2.json SHA256=<lowercase-64hex>`
