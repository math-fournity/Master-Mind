# VMS-41R1 Blind Review Rubric

The reviewer sees only the public raw trajectory, a candidate occurrence DAG,
source spans and this rubric.  Do not request or inspect acceptable-sets.json,
reference-candidates.json, mechanical error summaries or aggregate results.

Judgment fields:

- source_fidelity: ACCEPT | REJECT | AMBIGUOUS
- occurrence_granularity: ACCEPT | REJECT | AMBIGUOUS
- temporal_status: ACCEPT | REJECT | AMBIGUOUS
- branch_and_merge_semantics: ACCEPT | REJECT | AMBIGUOUS
- high_severity_failure: true | false
- notes

A candidate may include source-backed extra occurrences.  Reject only when an
extra occurrence is duplicated, rhetorical-only, unsupported by the source or
used to fabricate a merge/frontier that did not occur.
