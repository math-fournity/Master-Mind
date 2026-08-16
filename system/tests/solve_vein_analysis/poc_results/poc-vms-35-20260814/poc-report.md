# POC-VMS-35 result

- Overall verdict: **INCONCLUSIVE_PROTOCOL**
- Carrier: `devin_cli`
- Model: `glm-5-2`
- Normalized effort: `high`
- Sandbox requested: `False`
- Scientific attempts per role: `1`
- Database connections: `0`
- Solver launches: `0`

## Components

### reasoning_event_extractor

- Component verdict: `PARTIAL`
- Scientific verdict: `PARTIAL`
- Protocol OK: `True`
- Metrics: `{"false_merge_count": 0, "occurrence_recall": 1.0, "revisit_occurrence_identity": false, "source_artifact_sha256_exact": true, "source_spans_byte_exact": true, "strict_schema_valid": true, "true_merge_two_parent_recall": 1.0, "typed_edge_recall": 0.6923076923076923}`

### mathematical_state_normalizer

- Component verdict: `INCONCLUSIVE_PROTOCOL`
- Scientific verdict: `FAIL`
- Protocol OK: `False`
- Metrics: `{"immutable_event_history_preserved": false, "invented_event_or_edge_count": 0, "preregistered_corrections_recall": 0.6666666666666666, "strict_schema_valid": true, "unrelated_field_mutation_count": 1}`

### process_trace_auditor

- Component verdict: `PARTIAL`
- Scientific verdict: `PARTIAL`
- Protocol OK: `True`
- Metrics: `{"fake_merge_rejected": true, "invalid_trace_rejection": 1.0, "overall_verdict_exact": false, "top_level_contract_valid": true, "valid_trace_acceptance": 1.0}`

## Boundary

This is one calibration case per component. It does not establish production,
streaming, cross-domain, Solver-integration, Tell/Hint-effect, or Codex capability.
