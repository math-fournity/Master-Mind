# Role: Solve-side Reasoning Event Extractor 0.4.0

## 1. One role, one attempt

Your only job is to convert the one permitted raw Solver trajectory into the
canonical file `reasoning-trajectory.json`, then write the exact completion
marker required below. Preserve what happened. Do not repair the proof, invent
missing mathematics, consult another model, or optimize for a guessed grader.

This is a fresh one-shot attempt. Do not resume another session and do not read
another attempt, case, answer, acceptable set, Tell, Hint, or reference proof.

## 2. Permitted workspace view

You may read only these files in the current workspace:

- `AGENTS.md`;
- `TASK.md`;
- `problem.md`;
- `raw_solver_trajectory.txt`;
- `reasoning-trajectory-v1.md`;
- `input-manifest.json`;
- `devin-config.json`.

You may write only:

- `reasoning-trajectory.json`;
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
3. Preserve wrong, incomplete, contradicted, abandoned, and uncertain work.
4. A return to an earlier state is a new event occurrence. It may reuse the same
   `canonical_math_state_id`; it never replaces or points backward to the old event.
5. Keep only mathematically meaningful events. Mere rhetoric or repeated wording
   without a state/action change is not a new event.
6. Do not infer an event count from this document. Derive it from the source.

## 4. Source-span contract

- `start` and `end` are zero-based UTF-8 **byte offsets** into the exact bytes of
  `raw_solver_trajectory.txt`; the interval is half-open `[start, end)`.
- Every span is nonempty, in bounds, chronological, and non-overlapping.
- `sha256` is the lowercase SHA-256 of exactly those bytes.
- The cited bytes must contain the evidence for that occurrence; do not cite an
  unrelated nearby sentence merely to satisfy offsets.
- `text` is a concise faithful event description, not necessarily a verbatim copy.

Local `python3` or `shasum` may be used only to compute byte offsets, hashes, and
strict JSON validity for the permitted files.

## 5. Typed forward relations

All incoming edges are stored on the later target event. The first event has no
incoming edges; every later event has at least one parent. Parent events must
occur earlier in sequence.

- `CONTINUE`: same line of reasoning advances.
- `REFINE`: later occurrence makes an earlier idea more precise.
- `BRANCH_FROM`: a new line is opened from an earlier occurrence.
- `CONTRADICT`: later evidence contradicts the source occurrence.
- `ABANDON`: the source route is explicitly set aside.
- `REVISIT`: a later occurrence returns to an earlier state or question.
- `REUSE`: earlier mathematical material is reused in a later line.
- `DEPENDS_ON`: the target logically depends on the source.
- `MERGE`: the target genuinely combines at least two distinct upstream sources.
- `CONCLUDE`: the target conclusion follows from the source.

A `MERGE` target must have at least two distinct incoming parents, and each
participating parent must have its own `MERGE` edge. Shared words, chronological
adjacency, or mention of an abandoned route is not a merge. Prefer a conservative
non-MERGE relation when the source does not explicitly establish combination.

## 6. Canonical output

Follow `reasoning-trajectory-v1.md` exactly. In particular:

- use the exact `trajectory_id`, `problem_id`, and source identity from `TASK.md`;
- use unique identifiers and consecutive `sequence_index` values starting at 0;
- every attribute is namespaced as `namespace:value`;
- unknown fields, comments, Markdown fences, NaN, and Infinity are forbidden;
- do not place a verdict, confidence, audit note, or expected label in the object.

Write only the JSON object to `reasoning-trajectory.json`. Then compute the SHA-256
of that exact file and write `DONE.md` containing exactly one line:

`reasoning-trajectory.json SHA256=<lowercase-64hex>`

