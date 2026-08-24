"""POC-VMS-40 deterministic multi-view truth regression tests."""

from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from system.solve_vein_analysis.semantic_truth import (
    EvaluationVerdict,
    SemanticAcceptableSet,
    SemanticCandidate,
    SemanticValidationError,
    evaluate_candidate,
    evaluate_candidate_value,
)


HERE = Path(__file__).resolve().parent
FIXTURE_PATH = HERE / "multiview_fixtures" / "vms40_cases.json"
PROTOCOL_PATH = (
    HERE.parents[2]
    / "docs/history/sixth-generation/rnd"
    / "366-v0-2026-08-14-POC-VMS-40-多视图脉络真值与acceptable-set确定性协议.md"
)


def load_pack() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text())


def case_by_id(case_id: str) -> dict[str, object]:
    return next(case for case in load_pack()["cases"] if case["case_id"] == case_id)


class FrozenFixtureMatrixTests(unittest.TestCase):
    def test_protocol_hash_is_frozen_before_implementation(self) -> None:
        pack = load_pack()
        actual = hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest()
        self.assertEqual(
            actual,
            "8d045365b5cd14d8d98d617ddec7c6607d96aeb1e2a871216fa1c631ca1b6857",
        )
        self.assertEqual(pack["protocol_sha256"], actual)

    def test_mv1_through_mv6_are_present_exactly_once(self) -> None:
        case_ids = [case["case_id"] for case in load_pack()["cases"]]
        self.assertEqual(case_ids, ["MV1", "MV2", "MV3", "MV4", "MV5", "MV6"])
        self.assertEqual(len(case_ids), len(set(case_ids)))

    def test_all_preregistered_candidate_verdicts_match(self) -> None:
        observed = 0
        for case in load_pack()["cases"]:
            acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
            for spec in case["candidates"]:
                with self.subTest(case=case["case_id"], candidate=spec["label"]):
                    evaluation = evaluate_candidate_value(spec["candidate"], acceptable)
                    self.assertEqual(
                        evaluation.overall_verdict.value,
                        spec["expected_verdict"],
                    )
                    observed += 1
        self.assertEqual(observed, 26)

    def test_every_pass_is_recomputable_from_empty_error_set(self) -> None:
        for case in load_pack()["cases"]:
            acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
            for spec in case["candidates"]:
                evaluation = evaluate_candidate_value(spec["candidate"], acceptable)
                if evaluation.overall_verdict is EvaluationVerdict.PASS:
                    self.assertEqual(evaluation.errors, ())
                    result = evaluation.to_dict()
                    statuses = [
                        result["occurrence_verdict"]["status"],
                        result["required_relation_verdict"]["status"],
                        result["forbidden_relation_verdict"]["status"],
                        result["unmatched_relation_verdict"]["status"],
                    ]
                    statuses.extend(
                        item["status"] for item in result["relation_clause_verdicts"]
                    )
                    statuses.extend(
                        item["status"] for item in result["state_constraint_verdicts"]
                    )
                    statuses.extend(
                        item["status"] for item in result["legacy_status_verdicts"]
                    )
                    statuses.extend(
                        item["status"]
                        for item in result["structural_constraint_verdicts"]
                    )
                    self.assertTrue(all(status == "PASS" for status in statuses))
                else:
                    self.assertTrue(evaluation.errors)


class AcceptableSetSemanticsTests(unittest.TestCase):
    def test_two_complete_mv3_projections_pass(self) -> None:
        case = case_by_id("MV3")
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        evaluations = {
            spec["label"]: evaluate_candidate_value(spec["candidate"], acceptable)
            for spec in case["candidates"]
        }
        self.assertEqual(evaluations["projection-a-pass"].overall_verdict.value, "PASS")
        self.assertEqual(evaluations["projection-b-pass"].overall_verdict.value, "PASS")

    def test_mixed_partial_and_double_mv3_projections_fail(self) -> None:
        case = case_by_id("MV3")
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        for label in (
            "mixed-alternatives-fail",
            "both-alternatives-fail",
            "half-alternative-fail",
        ):
            spec = next(item for item in case["candidates"] if item["label"] == label)
            evaluation = evaluate_candidate_value(spec["candidate"], acceptable)
            self.assertEqual(evaluation.overall_verdict.value, "FAIL")
            self.assertIn(
                "RELATION_CLAUSE_UNSATISFIED",
                {item["code"] for item in evaluation.errors},
            )

    def test_true_merge_counts_distinct_parent_occurrences(self) -> None:
        case = case_by_id("MV4")
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        passing = next(
            item for item in case["candidates"] if item["label"] == "two-parent-merge-pass"
        )
        evaluation = evaluate_candidate_value(passing["candidate"], acceptable)
        structural = evaluation.structural_constraint_verdicts[0]
        self.assertEqual(structural["distinct_parent_ids"], ["a", "b"])
        self.assertEqual(structural["status"], "PASS")

    def test_optional_relation_is_observed_but_not_required(self) -> None:
        case = case_by_id("MV5")
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        required_only = next(
            item for item in case["candidates"] if item["label"] == "required-only-pass"
        )
        with_optional = next(
            item for item in case["candidates"] if item["label"] == "optional-present-pass"
        )
        first = evaluate_candidate_value(required_only["candidate"], acceptable)
        second = evaluate_candidate_value(with_optional["candidate"], acceptable)
        self.assertEqual(first.overall_verdict.value, "PASS")
        self.assertEqual(second.overall_verdict.value, "PASS")
        self.assertFalse(first.optional_relation_observations[0]["observed"])
        self.assertTrue(second.optional_relation_observations[0]["observed"])

    def test_per_view_coverage_keeps_relation_views_separate(self) -> None:
        case = case_by_id("MV3")
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        spec = next(
            item for item in case["candidates"] if item["label"] == "projection-a-pass"
        )
        evaluation = evaluate_candidate_value(spec["candidate"], acceptable)
        self.assertEqual(
            evaluation.per_view_coverage["CONTROL_FLOW"]["matched_required_count"],
            1,
        )
        self.assertEqual(
            evaluation.per_view_coverage["STATE_IDENTITY"][
                "matched_required_count"
            ],
            1,
        )


class CanonicalizationAndFailClosedTests(unittest.TestCase):
    def test_order_insensitive_arrays_have_identical_candidate_hash(self) -> None:
        case = case_by_id("MV2")
        raw = deepcopy(case["candidates"][0]["candidate"])
        reordered = deepcopy(raw)
        reordered["occurrence_ids"].reverse()
        reordered["state_bindings"].reverse()
        first = SemanticCandidate.from_dict(raw)
        second = SemanticCandidate.from_dict(reordered)
        self.assertEqual(first.canonical_sha256, second.canonical_sha256)
        self.assertEqual(first.to_dict(), second.to_dict())

    def test_acceptable_set_array_order_is_canonical(self) -> None:
        case = case_by_id("MV3")
        raw = deepcopy(case["acceptable_set"])
        reordered = deepcopy(raw)
        reordered["expected_occurrence_ids"].reverse()
        reordered["relation_clauses"][0]["alternatives"].reverse()
        for alternative in reordered["relation_clauses"][0]["alternatives"]:
            alternative["complete_relation_set"].reverse()
        first = SemanticAcceptableSet.from_dict(raw)
        second = SemanticAcceptableSet.from_dict(reordered)
        self.assertEqual(first.canonical_sha256, second.canonical_sha256)

    def test_relation_kind_must_belong_to_its_view(self) -> None:
        case = case_by_id("MV6")
        raw = deepcopy(case["candidates"][0]["candidate"])
        raw["relations"][0]["view"] = "SYNTHESIS"
        with self.assertRaises(SemanticValidationError) as caught:
            SemanticCandidate.from_dict(raw)
        self.assertEqual(caught.exception.code, "RELATION_VIEW_KIND_MISMATCH")

    def test_unknown_candidate_field_returns_invalid_evaluation(self) -> None:
        case = case_by_id("MV6")
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        raw = deepcopy(case["candidates"][0]["candidate"])
        raw["verdict"] = "PASS"
        evaluation = evaluate_candidate_value(raw, acceptable)
        self.assertEqual(evaluation.overall_verdict.value, "INVALID")
        self.assertEqual(evaluation.errors[0]["code"], "OBJECT_KEYS_INVALID")

    def test_overlapping_relation_categories_are_invalid_protocol(self) -> None:
        case = case_by_id("MV5")
        raw = deepcopy(case["acceptable_set"])
        raw["optional_relations"] = deepcopy(raw["required_relations"])
        with self.assertRaises(SemanticValidationError) as caught:
            SemanticAcceptableSet.from_dict(raw)
        self.assertEqual(caught.exception.code, "RELATION_CATEGORY_OVERLAP")

    def test_bool_cannot_be_structural_minimum(self) -> None:
        case = case_by_id("MV4")
        raw = deepcopy(case["acceptable_set"])
        raw["structural_constraints"][0]["minimum"] = True
        with self.assertRaises(SemanticValidationError) as caught:
            SemanticAcceptableSet.from_dict(raw)
        self.assertEqual(caught.exception.code, "TYPE_INTEGER_REQUIRED")

    def test_case_mismatch_does_not_fabricate_occurrence_difference(self) -> None:
        case = case_by_id("MV6")
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        spec = next(
            item for item in case["candidates"] if item["label"] == "case-mismatch-fail"
        )
        candidate = SemanticCandidate.from_dict(spec["candidate"])
        evaluation = evaluate_candidate(candidate, acceptable)
        self.assertEqual(evaluation.overall_verdict.value, "FAIL")
        self.assertEqual(evaluation.occurrence_verdict["status"], "PASS")
        self.assertEqual(
            [item["code"] for item in evaluation.errors],
            ["CASE_ID_MISMATCH"],
        )


if __name__ == "__main__":
    unittest.main()
