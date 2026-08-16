"""Deterministic regressions for the VMS-41R1 occurrence/projection contract."""

from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import unittest

from system.solve_vein_analysis.event_extraction_projection import (
    CandidateTrajectoryV2,
    EventExtractionAcceptableSetV2,
    MechanicalVerdict,
    ProjectionOverallStatus,
    ProjectionValidationError,
    evaluate_candidate_json_v2,
    resolve_candidate_occurrences,
    _enumerate_paths,
)
from system.solve_vein_analysis.models import EdgeRelation


SOURCE = (
    "ROOT: inspect the invariant.\n"
    "EXTRA: rewrite the local condition.\n"
    "LEFT: derive the modular lemma.\n"
    "RIGHT: build an independent bound.\n"
    "MERGE: combine the lemma and bound.\n"
    "END: conclude the target.\n"
).encode("utf-8")


def source_identity() -> dict[str, str]:
    return {
        "carrier": "fixture",
        "source_artifact_ref": "fixture://vms41r1/calibration-merge",
        "source_artifact_sha256": hashlib.sha256(SOURCE).hexdigest(),
    }


def span(witness: str) -> dict[str, int]:
    encoded = witness.encode("utf-8")
    start = SOURCE.index(encoded)
    return {"start": start, "end": start + len(encoded)}


def path_pattern(
    pattern_id: str,
    relations: list[str],
    *,
    minimum: int = 1,
    maximum: int = 1,
    max_hops: int = 1,
) -> dict[str, object]:
    return {
        "pattern_id": pattern_id,
        "atoms": [
            {
                "allowed_relations": relations,
                "min_repeat": minimum,
                "max_repeat": maximum,
            }
        ],
        "max_hops": max_hops,
    }


def acceptable_value(*, reuse_mode: bool = False) -> dict[str, object]:
    left_to_merge = "REUSE" if reuse_mode else "MERGE"
    right_to_merge = "DEPENDS_ON" if reuse_mode else "MERGE"
    return {
        "schema_version": "solve-vein/event-extraction-acceptable-set/v2",
        "acceptable_set_id": "acceptable-v41r1-calibration",
        "case_id": "V41R1-CAL-MERGE",
        "problem_id": "problem-v41r1-calibration",
        "trajectory_id": "trajectory-v41r1-calibration",
        "source": source_identity(),
        "anchors": [
            {
                "anchor_id": "A-ROOT",
                "unique_witness_text": "ROOT: inspect the invariant.",
                "allowed_event_kinds": ["STATE"],
                "allowed_status_at_occurrence": ["ACTIVE"],
                "allowed_later_resolutions": ["STILL_ACTIVE"],
            },
            {
                "anchor_id": "A-LEFT",
                "unique_witness_text": "LEFT: derive the modular lemma.",
                "allowed_event_kinds": ["DECISION"],
                "allowed_status_at_occurrence": ["TENTATIVE"],
                "allowed_later_resolutions": ["SOLVED"],
            },
            {
                "anchor_id": "A-RIGHT",
                "unique_witness_text": "RIGHT: build an independent bound.",
                "allowed_event_kinds": ["DECISION"],
                "allowed_status_at_occurrence": ["ESTABLISHED"],
                "allowed_later_resolutions": ["SOLVED"],
            },
            {
                "anchor_id": "A-MERGE",
                "unique_witness_text": "MERGE: combine the lemma and bound.",
                "allowed_event_kinds": ["SYNTHESIS"],
                "allowed_status_at_occurrence": ["ESTABLISHED"],
                "allowed_later_resolutions": ["SOLVED"],
            },
            {
                "anchor_id": "A-END",
                "unique_witness_text": "END: conclude the target.",
                "allowed_event_kinds": ["CONCLUSION"],
                "allowed_status_at_occurrence": ["SOLVED"],
                "allowed_later_resolutions": ["SOLVED"],
            },
        ],
        "typed_path_clauses": [
            {
                "clause_id": "P-ROOT-LEFT",
                "source_anchor_id": "A-ROOT",
                "target_anchor_id": "A-LEFT",
                "required": True,
                "patterns": [
                    path_pattern(
                        "PAT-ROOT-LEFT",
                        ["CONTINUE", "REFINE"],
                        maximum=3,
                        max_hops=3,
                    )
                ],
            },
            {
                "clause_id": "P-ROOT-RIGHT",
                "source_anchor_id": "A-ROOT",
                "target_anchor_id": "A-RIGHT",
                "required": True,
                "patterns": [
                    path_pattern("PAT-ROOT-RIGHT", ["BRANCH_FROM"])
                ],
            },
            {
                "clause_id": "P-LEFT-MERGE",
                "source_anchor_id": "A-LEFT",
                "target_anchor_id": "A-MERGE",
                "required": True,
                "patterns": [
                    path_pattern("PAT-LEFT-MERGE", [left_to_merge])
                ],
            },
            {
                "clause_id": "P-RIGHT-MERGE",
                "source_anchor_id": "A-RIGHT",
                "target_anchor_id": "A-MERGE",
                "required": True,
                "patterns": [
                    path_pattern("PAT-RIGHT-MERGE", [right_to_merge])
                ],
            },
            {
                "clause_id": "P-MERGE-END",
                "source_anchor_id": "A-MERGE",
                "target_anchor_id": "A-END",
                "required": True,
                "patterns": [path_pattern("PAT-MERGE-END", ["CONCLUDE"])],
            },
        ],
        "forbidden_path_clauses": [
            {
                "clause_id": "F-ROOT-END-CONTRADICT",
                "source_anchor_id": "A-ROOT",
                "target_anchor_id": "A-END",
                "patterns": [
                    path_pattern(
                        "PAT-FORBIDDEN-CONTRADICT",
                        ["CONTRADICT"],
                        maximum=6,
                        max_hops=6,
                    )
                ],
            }
        ],
        "forbidden_relations": ["ABANDON"] + (["MERGE"] if reuse_mode else []),
        "merge_constraints": []
        if reuse_mode
        else [
            {
                "constraint_id": "M-INDEPENDENT-FRONTIER",
                "target_anchor_id": "A-MERGE",
                "required_origin_anchor_ids": ["A-LEFT", "A-RIGHT"],
                "minimum_distinct_contributions": 2,
                "contribution_path_patterns": [
                    path_pattern(
                        "PAT-CONTRIBUTION",
                        ["CONTINUE", "REFINE", "REUSE", "DEPENDS_ON"],
                        maximum=3,
                        max_hops=3,
                    )
                ],
                "require_pairwise_incomparable": True,
            }
        ],
        "extra_event_policy": {
            "allow_unanchored_events": True,
            "maximum_extra_events": 2,
            "require_unique_semantic_signature": True,
            "require_nondecreasing_source_start": True,
        },
    }


def edge(source_id: str, relation: str, target_witness: str) -> dict[str, object]:
    return {
        "source_event_id": source_id,
        "relation": relation,
        "evidence": f"source-backed {source_id} relation",
        "evidence_span": span(target_witness),
    }


def contribution(
    parent_id: str, role: str, parent_witness: str
) -> dict[str, object]:
    return {
        "parent_event_id": parent_id,
        "contribution_role": role,
        "contribution_claim": f"contribution from {parent_id}",
        "evidence_span": span(parent_witness),
        "use_in_target": f"use {parent_id} in the synthesis",
    }


def event(
    event_id: str,
    sequence_index: int,
    kind: str,
    witness: str,
    state: str,
    status: str,
    resolution: str,
    incoming: list[dict[str, object]],
    contributions: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    return {
        "event_id": event_id,
        "sequence_index": sequence_index,
        "event_kind": kind,
        "text": witness,
        "canonical_math_state_id": state,
        "attributes": ["fixture:calibration"],
        "status_at_occurrence": status,
        "later_resolution": resolution,
        "source_span": span(witness),
        "incoming_edges": incoming,
        "merge_contributions": contributions or [],
    }


def candidate_value(*, include_extra: bool = True, reuse_mode: bool = False) -> dict[str, object]:
    rows: list[dict[str, object]] = [
        event(
            "E-ROOT",
            0,
            "STATE",
            "ROOT: inspect the invariant.",
            "state-root",
            "ACTIVE",
            "STILL_ACTIVE",
            [],
        )
    ]
    if include_extra:
        rows.append(
            event(
                "E-EXTRA",
                1,
                "STATE",
                "EXTRA: rewrite the local condition.",
                "state-extra-rewrite",
                "ACTIVE",
                "STILL_ACTIVE",
                [edge("E-ROOT", "CONTINUE", "EXTRA: rewrite the local condition.")],
            )
        )
        left_parent = "E-EXTRA"
        left_relation = "REFINE"
    else:
        left_parent = "E-ROOT"
        left_relation = "REFINE"
    rows.append(
        event(
            "E-LEFT",
            len(rows),
            "DECISION",
            "LEFT: derive the modular lemma.",
            "state-left-lemma",
            "TENTATIVE",
            "SOLVED",
            [edge(left_parent, left_relation, "LEFT: derive the modular lemma.")],
        )
    )
    rows.append(
        event(
            "E-RIGHT",
            len(rows),
            "DECISION",
            "RIGHT: build an independent bound.",
            "state-right-bound",
            "ESTABLISHED",
            "SOLVED",
            [edge("E-ROOT", "BRANCH_FROM", "RIGHT: build an independent bound.")],
        )
    )
    if reuse_mode:
        merge_edges = [
            edge("E-LEFT", "REUSE", "MERGE: combine the lemma and bound."),
            edge("E-RIGHT", "DEPENDS_ON", "MERGE: combine the lemma and bound."),
        ]
        contributions: list[dict[str, object]] = []
    else:
        merge_edges = [
            edge("E-LEFT", "MERGE", "MERGE: combine the lemma and bound."),
            edge("E-RIGHT", "MERGE", "MERGE: combine the lemma and bound."),
        ]
        contributions = [
            contribution("E-LEFT", "LEMMA", "LEFT: derive the modular lemma."),
            contribution("E-RIGHT", "BOUND", "RIGHT: build an independent bound."),
        ]
    rows.append(
        event(
            "E-MERGE",
            len(rows),
            "SYNTHESIS",
            "MERGE: combine the lemma and bound.",
            "state-merged-certificate",
            "ESTABLISHED",
            "SOLVED",
            merge_edges,
            contributions,
        )
    )
    rows.append(
        event(
            "E-END",
            len(rows),
            "CONCLUSION",
            "END: conclude the target.",
            "state-conclusion",
            "SOLVED",
            "SOLVED",
            [edge("E-MERGE", "CONCLUDE", "END: conclude the target.")],
        )
    )
    return {
        "schema_version": "solve-vein/reasoning-trajectory-candidate/v2",
        "trajectory_id": "trajectory-v41r1-calibration",
        "problem_id": "problem-v41r1-calibration",
        "source": source_identity(),
        "events": rows,
    }


def evaluation(
    candidate: dict[str, object], acceptable: dict[str, object] | None = None
):
    parsed = EventExtractionAcceptableSetV2.from_dict(
        acceptable or acceptable_value()
    )
    return evaluate_candidate_json_v2(
        json.dumps(candidate, ensure_ascii=False), parsed, SOURCE
    )


def codes(result: object) -> set[str]:
    return {item["code"] for item in result.errors}


class OccurrenceProjectionTests(unittest.TestCase):
    def test_fine_grained_history_projects_to_coarse_anchors(self) -> None:
        result = evaluation(candidate_value(include_extra=True))
        self.assertEqual(result.mechanical_scientific_verdict, MechanicalVerdict.PASS)
        self.assertEqual(result.metrics["observed_event_count"], 6)
        self.assertEqual(result.metrics["expected_anchor_count"], 5)
        self.assertEqual(result.metrics["extra_event_count"], 1)
        root_left = next(
            row for row in result.typed_path_verdicts if row["clause_id"] == "P-ROOT-LEFT"
        )
        self.assertEqual(root_left["status"], "PASS")
        self.assertEqual(root_left["collapsed_event_ids"], ["E-EXTRA"])

    def test_direct_history_projects_to_same_coarse_anchors(self) -> None:
        result = evaluation(candidate_value(include_extra=False))
        self.assertEqual(result.mechanical_scientific_verdict, MechanicalVerdict.PASS)
        self.assertEqual(result.metrics["observed_event_count"], 5)
        self.assertEqual(result.metrics["extra_event_count"], 0)

    def test_arbitrary_reachability_does_not_satisfy_typed_path(self) -> None:
        candidate = candidate_value()
        candidate["events"][2]["incoming_edges"][0]["relation"] = "DEPENDS_ON"
        result = evaluation(candidate)
        self.assertEqual(result.typed_path_verdict, MechanicalVerdict.FAIL)
        self.assertIn("REQUIRED_TYPED_PATH_MISSING", codes(result))

    def test_forbidden_relation_is_independently_detected(self) -> None:
        candidate = candidate_value()
        candidate["events"][1]["incoming_edges"][0]["relation"] = "ABANDON"
        result = evaluation(candidate)
        self.assertEqual(result.forbidden_semantics_verdict, MechanicalVerdict.FAIL)
        self.assertIn("FORBIDDEN_RELATION_OBSERVED", codes(result))

    def test_status_at_occurrence_cannot_be_backfilled_from_later_success(self) -> None:
        candidate = candidate_value()
        candidate["events"][2]["status_at_occurrence"] = "SOLVED"
        result = evaluation(candidate)
        self.assertEqual(result.temporal_status_verdict, MechanicalVerdict.FAIL)
        self.assertIn("STATUS_AT_OCCURRENCE_UNACCEPTABLE", codes(result))
        left = next(row for row in result.anchor_verdicts if row["anchor_id"] == "A-LEFT")
        self.assertEqual(left["later_resolution"], "SOLVED")

    def test_true_merge_has_injective_incomparable_contributions(self) -> None:
        result = evaluation(candidate_value())
        self.assertEqual(result.merge_contribution_verdict, MechanicalVerdict.PASS)
        row = result.merge_constraint_verdicts[0]
        self.assertEqual(row["status"], "PASS")
        self.assertTrue(row["pairwise_incomparable"])
        self.assertEqual(set(row["origin_parent_assignment"].values()), {"E-LEFT", "E-RIGHT"})

    def test_ancestor_chain_cannot_masquerade_as_independent_frontier(self) -> None:
        candidate = candidate_value()
        candidate["events"][3]["incoming_edges"] = [
            edge("E-LEFT", "REUSE", "RIGHT: build an independent bound.")
        ]
        result = evaluation(candidate)
        self.assertEqual(result.merge_contribution_verdict, MechanicalVerdict.FAIL)
        self.assertFalse(result.merge_constraint_verdicts[0]["pairwise_incomparable"])

    def test_merge_contribution_parent_set_mismatch_is_invalid(self) -> None:
        candidate = candidate_value()
        candidate["events"][4]["merge_contributions"].pop()
        result = evaluation(candidate)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("MERGE_CONTRIBUTION_PARENT_SET_MISMATCH", codes(result))

    def test_reuse_without_merge_is_representable(self) -> None:
        result = evaluation(
            candidate_value(reuse_mode=True), acceptable_value(reuse_mode=True)
        )
        self.assertEqual(result.mechanical_scientific_verdict, MechanicalVerdict.PASS)
        self.assertEqual(result.metrics["merge_constraint_count"], 0)

    def test_false_merge_without_hidden_constraint_fails(self) -> None:
        result = evaluation(candidate_value(), acceptable_value(reuse_mode=True))
        self.assertEqual(result.merge_contribution_verdict, MechanicalVerdict.FAIL)
        self.assertIn("UNCONSTRAINED_MERGE", codes(result))
        self.assertIn("FORBIDDEN_RELATION_OBSERVED", codes(result))

    def test_mechanical_pass_remains_pending_blind_manual_audit(self) -> None:
        result = evaluation(candidate_value())
        self.assertEqual(
            result.overall_status,
            ProjectionOverallStatus.PENDING_BLIND_MANUAL_AUDIT,
        )
        self.assertEqual(result.manual_semantic_audit, "PENDING")
        self.assertFalse(result.metrics["manual_semantic_audit_complete"])


class ProvenanceAndFailClosedTests(unittest.TestCase):
    def test_candidate_event_count_has_a_hard_resource_limit(self) -> None:
        candidate = candidate_value()
        candidate["events"] = [deepcopy(candidate["events"][0]) for _ in range(257)]
        result = evaluation(candidate)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("EVENT_COUNT_LIMIT_EXCEEDED", codes(result))

    def test_candidate_json_size_has_a_hard_resource_limit(self) -> None:
        acceptable = EventExtractionAcceptableSetV2.from_dict(acceptable_value())
        result = evaluate_candidate_json_v2(" " * (4 * 1024 * 1024 + 1), acceptable, SOURCE)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("CANDIDATE_JSON_SIZE_LIMIT_EXCEEDED", codes(result))

    def test_candidate_edge_count_has_a_hard_resource_limit(self) -> None:
        candidate = candidate_value()
        root = deepcopy(candidate["events"][0])
        root["event_id"] = "E-0"
        events = [root]
        edge_template = candidate["events"][1]["incoming_edges"][0]
        event_template = candidate["events"][1]
        for index in range(1, 256):
            item = deepcopy(event_template)
            item["event_id"] = f"E-{index}"
            item["sequence_index"] = index
            item["incoming_edges"] = []
            for source_index in range(max(0, index - 9), index):
                incoming = deepcopy(edge_template)
                incoming["source_event_id"] = f"E-{source_index}"
                item["incoming_edges"].append(incoming)
            events.append(item)
        candidate["events"] = events
        result = evaluation(candidate)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("EDGE_COUNT_LIMIT_EXCEEDED", codes(result))

    def test_path_search_and_enumeration_budgets_fail_closed(self) -> None:
        adjacency = {
            "A": (("B", EdgeRelation.CONTINUE), ("C", EdgeRelation.CONTINUE)),
            "B": (("D", EdgeRelation.CONTINUE),),
            "C": (("D", EdgeRelation.CONTINUE),),
            "D": (),
        }
        with self.assertRaises(ProjectionValidationError) as states:
            _enumerate_paths(
                "A", "missing", adjacency, max_hops=4, max_search_states=2
            )
        self.assertEqual(states.exception.code, "PATH_SEARCH_BUDGET_EXCEEDED")
        with self.assertRaises(ProjectionValidationError) as paths:
            _enumerate_paths(
                "A", "D", adjacency, max_hops=4, max_enumerated_paths=1
            )
        self.assertEqual(paths.exception.code, "PATH_ENUMERATION_LIMIT_EXCEEDED")

    def test_candidate_has_no_span_hash_and_runner_derives_it(self) -> None:
        candidate = candidate_value()
        self.assertNotIn("sha256", candidate["events"][0]["source_span"])
        parsed = CandidateTrajectoryV2.from_dict(candidate)
        resolved = resolve_candidate_occurrences(parsed, SOURCE)
        resolved_span = resolved["events"][0]["source_span"]
        expected = SOURCE[resolved_span["start"] : resolved_span["end"]]
        self.assertEqual(resolved_span["sha256"], hashlib.sha256(expected).hexdigest())

    def test_one_event_cannot_swallow_two_anchors(self) -> None:
        candidate = candidate_value()
        candidate["events"][0]["source_span"]["end"] = span(
            "LEFT: derive the modular lemma."
        )["end"]
        result = evaluation(candidate)
        self.assertIn("EVENT_SWALLOWS_MULTIPLE_ANCHORS", codes(result))

    def test_extra_event_limit_is_enforced_without_exact_event_count(self) -> None:
        acceptable = acceptable_value()
        acceptable["extra_event_policy"]["maximum_extra_events"] = 0
        result = evaluation(candidate_value(), acceptable)
        self.assertIn("EXTRA_EVENT_LIMIT_EXCEEDED", codes(result))

    def test_duplicate_semantic_signature_is_invalid(self) -> None:
        candidate = candidate_value()
        duplicate = deepcopy(candidate["events"][0])
        duplicate["event_id"] = "E-DUPLICATE"
        duplicate["sequence_index"] = 1
        duplicate["incoming_edges"] = [
            edge("E-ROOT", "CONTINUE", "ROOT: inspect the invariant.")
        ]
        candidate["events"].insert(1, duplicate)
        for index, item in enumerate(candidate["events"]):
            item["sequence_index"] = index
        result = evaluation(candidate)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("EVENT_SEMANTIC_SIGNATURE_DUPLICATE", codes(result))

    def test_unknown_field_is_invalid(self) -> None:
        candidate = candidate_value()
        candidate["self_verdict"] = "PASS"
        result = evaluation(candidate)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("OBJECT_KEYS_INVALID", codes(result))

    def test_bool_cannot_be_sequence_index(self) -> None:
        candidate = candidate_value()
        candidate["events"][0]["sequence_index"] = True
        result = evaluation(candidate)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("TYPE_INTEGER_REQUIRED", codes(result))

    def test_nonfinite_json_is_invalid(self) -> None:
        acceptable = EventExtractionAcceptableSetV2.from_dict(acceptable_value())
        text = json.dumps(candidate_value()).replace('"sequence_index": 0', '"sequence_index": NaN', 1)
        result = evaluate_candidate_json_v2(text, acceptable, SOURCE)
        self.assertEqual(result.overall_status, ProjectionOverallStatus.INVALID)
        self.assertIn("JSON_NONFINITE_NUMBER", codes(result))

    def test_source_identity_mismatch_fails_artifact_axis(self) -> None:
        candidate = candidate_value()
        candidate["source"]["source_artifact_ref"] = "fixture://wrong-source"
        result = evaluation(candidate)
        self.assertEqual(result.artifact_verdict, MechanicalVerdict.FAIL)
        self.assertIn("SOURCE_IDENTITY_MISMATCH", codes(result))

    def test_out_of_bounds_span_fails_artifact_axis(self) -> None:
        candidate = candidate_value()
        candidate["events"][-1]["source_span"]["end"] = len(SOURCE) + 1
        result = evaluation(candidate)
        self.assertEqual(result.artifact_verdict, MechanicalVerdict.FAIL)
        self.assertIn("SOURCE_SPAN_OUT_OF_BOUNDS", codes(result))

    def test_unconstrained_merge_is_never_silently_accepted(self) -> None:
        acceptable = acceptable_value()
        acceptable["merge_constraints"] = []
        acceptable["forbidden_relations"] = []
        result = evaluation(candidate_value(), acceptable)
        self.assertEqual(result.merge_contribution_verdict, MechanicalVerdict.FAIL)
        self.assertIn("UNCONSTRAINED_MERGE", codes(result))

    def test_weak_extra_event_policy_is_rejected(self) -> None:
        acceptable = acceptable_value()
        acceptable["extra_event_policy"]["require_unique_semantic_signature"] = False
        with self.assertRaises(ProjectionValidationError) as caught:
            EventExtractionAcceptableSetV2.from_dict(acceptable)
        self.assertEqual(caught.exception.code, "EXTRA_EVENT_POLICY_WEAKENS_V2_INVARIANT")


if __name__ == "__main__":
    unittest.main()
