from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import unittest

from system.solve_vein_analysis import state_normalization as sn


HERE = Path(__file__).resolve().parent
FIXTURE_PATH = HERE / "state_normalizer_fixtures" / "vms42_cases.json"


def load_pack() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text())


def first_case() -> dict[str, object]:
    return load_pack()["cases"][0]  # type: ignore[index]


class VMS42StateNormalizerTests(unittest.TestCase):
    def test_fixture_pack_expected_verdicts_match(self) -> None:
        receipt = sn.evaluate_state_normalization_pack(load_pack())
        self.assertEqual(receipt["schema_version"], "solve-vein/state-normalization-pack-evaluation/v1")
        self.assertEqual(receipt["case_count"], 2)
        self.assertEqual(receipt["candidate_count"], 4)
        self.assertEqual(receipt["mismatch_count"], 0)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))

    def test_multiaxis_revisit_preserves_problem_projection_but_splits_other_axes(self) -> None:
        case = first_case()
        candidate = case["candidates"][0]["input"]  # type: ignore[index]
        bundle = sn.normalize_state_claims(candidate, case["dictionary"])  # type: ignore[index]
        projection = bundle.legacy_projection()
        self.assertEqual(projection["e0"], "prove-main")
        self.assertEqual(projection["e1"], "prove-main")
        binding_map = bundle.binding_map()
        self.assertNotEqual(
            binding_map[("e0", sn.StateAxis.STRATEGY_METHOD)],
            binding_map[("e1", sn.StateAxis.STRATEGY_METHOD)],
        )
        self.assertNotEqual(
            binding_map[("e0", sn.StateAxis.REPRESENTATION)],
            binding_map[("e1", sn.StateAxis.REPRESENTATION)],
        )

    def test_collapsing_strategy_axis_fails_cannot_link(self) -> None:
        case = first_case()
        candidate = case["candidates"][1]["input"]  # type: ignore[index]
        acceptable = sn.StateNormalizationAcceptableSet.from_dict(case["acceptable_set"])  # type: ignore[index]
        bundle = sn.normalize_state_claims(candidate, case["dictionary"])  # type: ignore[index]
        evaluation = sn.evaluate_normalized_bundle(bundle, acceptable)
        self.assertEqual(evaluation["overall_verdict"], "FAIL")
        self.assertIn("STATE_CONSTRAINT_UNSATISFIED", {error["code"] for error in evaluation["errors"]})

    def test_unknown_alias_is_invalid_not_fail(self) -> None:
        case = load_pack()["cases"][1]  # type: ignore[index]
        candidate = case["candidates"][1]["input"]  # type: ignore[index]
        evaluation = sn.evaluate_state_normalization_value(
            candidate, case["dictionary"], case["acceptable_set"]  # type: ignore[arg-type]
        )
        self.assertEqual(evaluation["overall_verdict"], "INVALID")
        self.assertEqual(evaluation["errors"][0]["code"], "DICTIONARY_ALIAS_UNKNOWN")

    def test_duplicate_axis_claim_fails_closed(self) -> None:
        case = first_case()
        candidate = deepcopy(case["candidates"][0]["input"])  # type: ignore[index]
        candidate["raw_axis_claims"].append(deepcopy(candidate["raw_axis_claims"][0]))  # type: ignore[index]
        evaluation = sn.evaluate_state_normalization_value(
            candidate, case["dictionary"], case["acceptable_set"]  # type: ignore[arg-type]
        )
        self.assertEqual(evaluation["overall_verdict"], "INVALID")
        self.assertEqual(evaluation["errors"][0]["code"], "RAW_AXIS_CLAIM_DUPLICATE")

    def test_missing_required_axis_fails_coverage(self) -> None:
        case = first_case()
        candidate = deepcopy(case["candidates"][0]["input"])  # type: ignore[index]
        candidate["raw_axis_claims"] = [  # type: ignore[index]
            item for item in candidate["raw_axis_claims"] if not (item["occurrence_id"] == "e1" and item["axis"] == "KNOWLEDGE_STATE")
        ]
        evaluation = sn.evaluate_state_normalization_value(
            candidate, case["dictionary"], case["acceptable_set"]  # type: ignore[arg-type]
        )
        self.assertEqual(evaluation["overall_verdict"], "FAIL")
        self.assertEqual(evaluation["axis_coverage_verdict"]["status"], "FAIL")

    def test_candidate_order_is_canonical(self) -> None:
        case = first_case()
        candidate = deepcopy(case["candidates"][0]["input"])  # type: ignore[index]
        reordered = deepcopy(candidate)
        reordered["occurrence_ids"].reverse()
        reordered["raw_axis_claims"].reverse()
        first = sn.StateNormalizationInput.from_dict(candidate)
        second = sn.StateNormalizationInput.from_dict(reordered)
        self.assertEqual(first.canonical_sha256, second.canonical_sha256)
        self.assertEqual(first.to_dict(), second.to_dict())

    def test_cli_evaluates_fixture_pack_without_side_effects(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/solve_vein_analysis/state_normalization.py",
                "--pack",
                str(FIXTURE_PATH),
            ],
            cwd=HERE.parents[2],
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["candidate_count"], 4)
        self.assertEqual(receipt["mismatch_count"], 0)
        self.assertEqual(receipt["side_effects"]["model_calls"], 0)


if __name__ == "__main__":
    unittest.main()
