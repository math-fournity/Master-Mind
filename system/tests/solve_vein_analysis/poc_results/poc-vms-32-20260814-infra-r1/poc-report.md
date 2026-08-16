# POC-VMS-32 result

- Overall verdict: **INCONCLUSIVE_PROTOCOL**
- Carrier: `devin_cli`
- Model: `glm-5-2`
- Normalized effort: `high`
- Scientific attempts per role: `1`
- Database connections: `0`
- Solver launches: `0`

## Components

### reasoning_event_extractor

- Component verdict: `INCONCLUSIVE_PROTOCOL`
- Scientific verdict: `FAIL`
- Protocol OK: `False`
- Metrics: `{"false_merge_count": 0, "occurrence_recall": 0.0, "revisit_occurrence_identity": false, "source_artifact_sha256_exact": false, "source_spans_byte_exact": false, "strict_schema_valid": false, "true_merge_two_parent_recall": 0.0, "typed_edge_recall": 0.0}`

### mathematical_state_normalizer

- Component verdict: `INCONCLUSIVE_PROTOCOL`
- Scientific verdict: `FAIL`
- Protocol OK: `False`
- Metrics: `{"immutable_event_history_preserved": false, "invented_event_or_edge_count": null, "preregistered_corrections_recall": 0.0, "strict_schema_valid": false, "unrelated_field_mutation_count": null}`

### process_trace_auditor

- Component verdict: `INCONCLUSIVE_PROTOCOL`
- Scientific verdict: `FAIL`
- Protocol OK: `False`
- Metrics: `{"fake_merge_rejected": false, "invalid_trace_rejection": 0.0, "overall_verdict_exact": false, "top_level_contract_valid": false, "valid_trace_acceptance": 0.0}`

## Boundary

This is one calibration case per component. It does not establish production,
streaming, cross-domain, Solver-integration, Tell/Hint-effect, or Codex capability.
