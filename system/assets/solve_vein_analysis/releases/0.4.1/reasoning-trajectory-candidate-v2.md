# `solve-vein/reasoning-trajectory-candidate/v2` strict shape

The root has exactly these fields:

```json
{
  "schema_version": "solve-vein/reasoning-trajectory-candidate/v2",
  "trajectory_id": "identifier",
  "problem_id": "identifier",
  "source": {
    "carrier": "fixture",
    "source_artifact_ref": "raw_solver_trajectory.txt",
    "source_artifact_sha256": "lowercase-64hex"
  },
  "events": []
}
```

Every event has exactly:

```json
{
  "event_id": "unique-identifier",
  "sequence_index": 0,
  "event_kind": "STATE",
  "text": "nonempty faithful description",
  "canonical_math_state_id": "identifier",
  "attributes": ["namespace:value"],
  "status_at_occurrence": "ACTIVE",
  "later_resolution": "STILL_ACTIVE",
  "source_span": {
    "start": 0,
    "end": 1
  },
  "incoming_edges": [],
  "merge_contributions": []
}
```

Every incoming edge has exactly:

```json
{
  "source_event_id": "earlier-event-id",
  "relation": "CONTINUE",
  "evidence": "nonempty source-grounded explanation",
  "evidence_span": {
    "start": 0,
    "end": 1
  }
}
```

Every merge contribution has exactly:

```json
{
  "parent_event_id": "earlier-event-id",
  "contribution_role": "LEMMA",
  "contribution_claim": "nonempty claim",
  "evidence_span": {
    "start": 0,
    "end": 1
  },
  "use_in_target": "nonempty explanation of how the target uses this parent"
}
```

Allowed event kinds:

`STATE, DECISION, FAILURE, RETURN, SYNTHESIS, CONCLUSION`

Allowed `status_at_occurrence` values:

`ACTIVE, TENTATIVE, ESTABLISHED, SOLVED, UNKNOWN`

Allowed `later_resolution` values:

`STILL_ACTIVE, ABANDONED, CONTRADICTED, SOLVED, SUPERSEDED, UNKNOWN`

Allowed relations:

`CONTINUE, REFINE, BRANCH_FROM, CONTRADICT, ABANDON, REVISIT, REUSE,
DEPENDS_ON, MERGE, CONCLUDE`

Allowed contribution roles:

`LEMMA, CONSTRUCTION, CERTIFICATE, COUNTEREXAMPLE, BOUND, REPRESENTATION, OTHER`

Identifiers match `[A-Za-z0-9][A-Za-z0-9_.:-]*`. Events are listed in exact
occurrence order; `sequence_index` is exactly `0..n-1`; event 0 has no incoming
edge and every later event has at least one edge from an earlier event. A `MERGE`
target requires at least two `MERGE` incoming edges and matching contribution
objects for those parents.
