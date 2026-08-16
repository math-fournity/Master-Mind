"""POC-VMS-41 deterministic acceptable-set and grader regression tests."""

from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from system.solve_vein_analysis.event_extraction_qualification import (
    EventExtractionAcceptableSet,
    EventExtractionAcceptableSetPack,
    MechanicalVerdict,
    OverallQualificationStatus,
    QualificationValidationError,
    evaluate_candidate_json,
)


HERE = Path(__file__).resolve().parent
FIXTURE_ROOT = HERE / "qualification_fixtures" / "vms41"
ACCEPTABLE_SET_PATH = FIXTURE_ROOT / "acceptable-sets.json"
CASE_DIRS = {
    "V41-SYN-FALSE-MERGE": "syn_false_merge",
    "V41-SYN-TRUE-MERGE": "syn_true_merge",
    "V41-REAL-SPIRAL": "real_spiral",
    "V41-REAL-BATTERY": "real_battery",
}


def load_raw_pack() -> dict[str, object]:
    return json.loads(ACCEPTABLE_SET_PATH.read_text())


def load_pack() -> EventExtractionAcceptableSetPack:
    return EventExtractionAcceptableSetPack.from_json_text(
        ACCEPTABLE_SET_PATH.read_text()
    )


def source_for(case_id: str) -> bytes:
    return (
        FIXTURE_ROOT / CASE_DIRS[case_id] / "raw_solver_trajectory.txt"
    ).read_bytes()


def build_passing_candidate(
    acceptable: EventExtractionAcceptableSet,
    source_bytes: bytes,
) -> dict[str, object]:
    witness_spans = acceptable.witness_spans(source_bytes)
    events: list[dict[str, object]] = []
    required_by_target: dict[str, list[object]] = {}
    for clause in acceptable.edge_clauses:
        if clause.required:
            required_by_target.setdefault(clause.target_anchor_id, []).append(clause)
    for index, anchor in enumerate(acceptable.anchors):
        start, end = witness_spans[anchor.anchor_id]
        event_id = f"event-{anchor.anchor_id}"
        incoming: list[dict[str, str]] = []
        for clause in required_by_target.get(anchor.anchor_id, []):
            incoming.append(
                {
                    "source_event_id": f"event-{clause.source_anchor_id}",
                    "relation": clause.allowed_relations[0].value,
                    "evidence": f"frozen clause {clause.clause_id}",
                }
            )
        events.append(
            {
                "event_id": event_id,
                "sequence_index": index,
                "event_kind": anchor.allowed_event_kinds[0].value,
                "text": anchor.unique_witness_text,
                "canonical_math_state_id": f"state-{anchor.anchor_id}",
                "attributes": ["qualification:anchor"],
                "status": anchor.allowed_statuses[0].value,
                "source_span": {
                    "start": start,
                    "end": end,
                    "sha256": hashlib.sha256(source_bytes[start:end]).hexdigest(),
                },
                "incoming_edges": incoming,
            }
        )
    return {
        "schema_version": "solve-vein/reasoning-trajectory/v1",
        "trajectory_id": acceptable.trajectory_id,
        "problem_id": acceptable.problem_id,
        "source": acceptable.source.to_dict(),
        "events": events,
    }


def evaluate_value(
    candidate: dict[str, object],
    acceptable: EventExtractionAcceptableSet,
    source_bytes: bytes,
):
    return evaluate_candidate_json(
        json.dumps(candidate, ensure_ascii=False), acceptable, source_bytes
    )


class FrozenPackTests(unittest.TestCase):
    def test_exact_four_case_pack_and_unique_witnesses(self) -> None:
        pack = load_pack()
        self.assertEqual(
            [case.case_id for case in pack.cases],
            [
                "V41-SYN-FALSE-MERGE",
                "V41-SYN-TRUE-MERGE",
                "V41-REAL-SPIRAL",
                "V41-REAL-BATTERY",
            ],
        )
        for acceptable in pack.cases:
            with self.subTest(case=acceptable.case_id):
                spans = acceptable.witness_spans(source_for(acceptable.case_id))
                self.assertEqual(len(spans), acceptable.expected_event_count)

    def test_reference_candidates_mechanically_pass_all_cases(self) -> None:
        for acceptable in load_pack().cases:
            with self.subTest(case=acceptable.case_id):
                source = source_for(acceptable.case_id)
                evaluation = evaluate_value(
                    build_passing_candidate(acceptable, source), acceptable, source
                )
                self.assertEqual(
                    evaluation.protocol_verdict, MechanicalVerdict.PASS
                )
                self.assertEqual(
                    evaluation.artifact_verdict, MechanicalVerdict.PASS
                )
                self.assertEqual(
                    evaluation.mechanical_scientific_verdict,
                    MechanicalVerdict.PASS,
                )
                self.assertEqual(evaluation.errors, ())

    def test_mechanical_pass_never_self_promotes_to_final_pass(self) -> None:
        acceptable = load_pack().case_by_id("V41-SYN-TRUE-MERGE")
        source = source_for(acceptable.case_id)
        evaluation = evaluate_value(
            build_passing_candidate(acceptable, source), acceptable, source
        )
        self.assertEqual(
            evaluation.overall_status,
            OverallQualificationStatus.PENDING_MANUAL_AUDIT,
        )
        self.assertEqual(evaluation.manual_semantic_audit, "PENDING")

    def test_unknown_acceptable_set_field_is_rejected(self) -> None:
        raw = deepcopy(load_raw_pack()["cases"][0])
        raw["self_verdict"] = "PASS"
        with self.assertRaises(QualificationValidationError) as caught:
            EventExtractionAcceptableSet.from_dict(raw)
        self.assertEqual(caught.exception.code, "OBJECT_KEYS_INVALID")

    def test_bool_cannot_be_event_count(self) -> None:
        raw = deepcopy(load_raw_pack()["cases"][0])
        raw["expected_event_count"] = True
        with self.assertRaises(QualificationValidationError) as caught:
            EventExtractionAcceptableSet.from_dict(raw)
        self.assertEqual(caught.exception.code, "TYPE_INTEGER_REQUIRED")

    def test_duplicate_witness_in_source_is_protocol_invalid(self) -> None:
        raw = deepcopy(load_raw_pack()["cases"][0])
        source = source_for(raw["case_id"])
        witness = raw["anchors"][0]["unique_witness_text"].encode()
        mutated = source + b"\n" + witness + b"\n"
        raw["source"]["source_artifact_sha256"] = hashlib.sha256(mutated).hexdigest()
        acceptable = EventExtractionAcceptableSet.from_dict(raw)
        with self.assertRaises(QualificationValidationError) as caught:
            acceptable.witness_spans(mutated)
        self.assertEqual(caught.exception.code, "ANCHOR_WITNESS_NOT_UNIQUE")


class CandidateFailClosedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pack = load_pack()

    def test_candidate_authored_verdict_field_is_invalid(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-FALSE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        candidate["verdict"] = "PASS"
        evaluation = evaluate_value(candidate, acceptable, source)
        self.assertEqual(evaluation.overall_status, OverallQualificationStatus.INVALID)
        self.assertEqual(evaluation.errors[0]["code"], "OBJECT_KEY_UNKNOWN")

    def test_source_identity_mismatch_fails_artifact_axis(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-FALSE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        candidate["source"]["source_artifact_ref"] = "another-file.txt"
        evaluation = evaluate_value(candidate, acceptable, source)
        self.assertEqual(evaluation.artifact_verdict, MechanicalVerdict.FAIL)
        self.assertIn(
            "SOURCE_IDENTITY_MISMATCH",
            {error["code"] for error in evaluation.errors},
        )

    def test_span_hash_mismatch_fails_artifact_axis(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-FALSE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        candidate["events"][0]["source_span"]["sha256"] = "0" * 64
        evaluation = evaluate_value(candidate, acceptable, source)
        self.assertEqual(evaluation.artifact_verdict, MechanicalVerdict.FAIL)
        self.assertIn(
            "SOURCE_SPAN_HASH_MISMATCH",
            {error["code"] for error in evaluation.errors},
        )

    def test_one_event_cannot_swallow_two_anchors(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-FALSE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        second_end = candidate["events"][1]["source_span"]["end"]
        candidate["events"][0]["source_span"]["end"] = second_end
        candidate["events"][0]["source_span"]["sha256"] = hashlib.sha256(
            source[:second_end]
        ).hexdigest()
        evaluation = evaluate_value(candidate, acceptable, source)
        codes = {error["code"] for error in evaluation.errors}
        self.assertIn("EVENT_ANCHOR_CARDINALITY_INVALID", codes)
        self.assertIn("ANCHOR_EVENT_CARDINALITY_INVALID", codes)

    def test_unacceptable_event_kind_fails(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-FALSE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        candidate["events"][3]["event_kind"] = "FAILURE"
        evaluation = evaluate_value(candidate, acceptable, source)
        self.assertIn(
            "ANCHOR_EVENT_KIND_UNACCEPTABLE",
            {error["code"] for error in evaluation.errors},
        )

    def test_false_merge_is_forbidden(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-FALSE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        candidate["events"][2]["incoming_edges"][0]["relation"] = "MERGE"
        evaluation = evaluate_value(candidate, acceptable, source)
        self.assertEqual(evaluation.metrics["forbidden_edge_count"], 1)
        self.assertIn(
            "FORBIDDEN_EDGE_OBSERVED",
            {error["code"] for error in evaluation.errors},
        )

    def test_true_merge_requires_both_frozen_parents(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-TRUE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        merge_event = candidate["events"][3]
        merge_event["incoming_edges"] = [merge_event["incoming_edges"][1]]
        evaluation = evaluate_value(candidate, acceptable, source)
        codes = {error["code"] for error in evaluation.errors}
        self.assertIn("REQUIRED_EDGE_MISSING", codes)
        self.assertIn("MERGE_CONSTRAINT_UNSATISFIED", codes)

    def test_unmatched_edge_is_not_silently_accepted(self) -> None:
        acceptable = self.pack.case_by_id("V41-SYN-FALSE-MERGE")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        candidate["events"][3]["incoming_edges"].append(
            {
                "source_event_id": "event-F0",
                "relation": "DEPENDS_ON",
                "evidence": "invented extra edge",
            }
        )
        evaluation = evaluate_value(candidate, acceptable, source)
        self.assertEqual(evaluation.metrics["unmatched_edge_count"], 1)
        self.assertIn(
            "UNMATCHED_EDGE", {error["code"] for error in evaluation.errors}
        )

    def test_any_merge_relation_has_automatic_two_parent_guard(self) -> None:
        acceptable = self.pack.case_by_id("V41-REAL-BATTERY")
        source = source_for(acceptable.case_id)
        candidate = build_passing_candidate(acceptable, source)
        target = candidate["events"][8]
        target["incoming_edges"][0]["relation"] = "MERGE"
        evaluation = evaluate_value(candidate, acceptable, source)
        self.assertIn(
            "MERGE_PARENT_CARDINALITY_INVALID",
            {error["code"] for error in evaluation.errors},
        )


if __name__ == "__main__":
    unittest.main()

