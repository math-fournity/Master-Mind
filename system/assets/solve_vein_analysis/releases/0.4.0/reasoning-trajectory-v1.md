# `solve-vein/reasoning-trajectory/v1` strict shape

The root has exactly these fields:

```json
{
  "schema_version": "solve-vein/reasoning-trajectory/v1",
  "trajectory_id": "identifier",
  "problem_id": "identifier",
  "source": {
    "carrier": "imported",
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
  "status": "ACTIVE",
  "source_span": {
    "start": 0,
    "end": 1,
    "sha256": "lowercase-64hex"
  },
  "incoming_edges": []
}
```

Every incoming edge has exactly:

```json
{
  "source_event_id": "earlier-event-id",
  "relation": "CONTINUE",
  "evidence": "nonempty source-grounded explanation"
}
```

Allowed event kinds:

`STATE, DECISION, FAILURE, RETURN, SYNTHESIS, CONCLUSION`

Allowed statuses:

`ACTIVE, ABANDONED, CONTRADICTED, SOLVED, UNKNOWN`

Allowed relations:

`CONTINUE, REFINE, BRANCH_FROM, CONTRADICT, ABANDON, REVISIT, REUSE,
DEPENDS_ON, MERGE, CONCLUDE`

Identifiers match `[A-Za-z0-9][A-Za-z0-9_.:-]*`. Events are listed in exact
occurrence order; `sequence_index` is exactly `0..n-1`; event 0 has no incoming
edge and every later event has at least one edge from an earlier event.

