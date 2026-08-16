from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from system.tests.solve_vein_analysis import vms41r1_manual_judgment_contract as contract


def valid_judgment() -> dict[str, object]:
    attempt_map = contract.expected_attempt_map()
    case_id = sorted(attempt_map)[0]
    return {
        "schema_version": contract.SCHEMA_VERSION,
        "review_id": "vms41r1-manual-review-fixture-001",
        "case_id": case_id,
        "attempt_id": attempt_map[case_id],
        "blinded_package_sha256": "a" * 64,
        "reviewer_blinding_attestation": {
            "reviewer_view_only": True,
            "hidden_acceptable_set_seen": False,
            "reference_candidate_seen": False,
            "mechanical_grader_result_seen": False,
        },
        "axis_verdicts": {axis: "PASS" for axis in contract.REQUIRED_AXES},
        "final_manual_verdict": "MANUAL_PASS",
        "reviewer_notes": "Synthetic contract fixture; not a real manual review.",
        "sealed_status": "SEALED_MANUAL_JUDGMENT",
        "explicit_nonclaims": sorted(contract.REQUIRED_NONCLAIMS),
    }


class VMS41R1ManualJudgmentContractTests(unittest.TestCase):
    def test_valid_synthetic_judgment_passes(self) -> None:
        self.assertEqual(contract.validate_manual_judgment(valid_judgment()), [])

    def test_contract_summary_has_zero_side_effects(self) -> None:
        summary = contract.build_contract_summary()
        self.assertEqual(summary["case_count"], 6)
        self.assertTrue(all(value == 0 for value in summary["side_effects"].values()))
        self.assertIn("does_not_perform_manual_review", summary["explicit_nonclaims"])

    def test_rejects_attempt_mismatch(self) -> None:
        value = valid_judgment()
        value["attempt_id"] = "wrong-attempt"
        self.assertIn("attempt_id_mismatch", contract.validate_manual_judgment(value))

    def test_rejects_hidden_exposure(self) -> None:
        value = valid_judgment()
        value["reviewer_blinding_attestation"] = {
            "reviewer_view_only": True,
            "hidden_acceptable_set_seen": True,
            "reference_candidate_seen": False,
            "mechanical_grader_result_seen": False,
        }
        self.assertIn(
            "reviewer_blinding_attestation_invalid",
            contract.validate_manual_judgment(value),
        )

    def test_rejects_manual_pass_with_failed_axis(self) -> None:
        value = valid_judgment()
        value["axis_verdicts"]["merge_contribution_fidelity"] = "FAIL"  # type: ignore[index]
        self.assertIn(
            "manual_pass_requires_all_axes_pass",
            contract.validate_manual_judgment(value),
        )

    def test_rejects_missing_axis_and_unknown_key(self) -> None:
        value = valid_judgment()
        del value["axis_verdicts"]["file_boundary_cleanliness"]  # type: ignore[index]
        value["axis_verdicts"]["unknown_axis"] = "PASS"  # type: ignore[index]
        errors = contract.validate_manual_judgment(value)
        self.assertTrue(any(error.startswith("axis_keys_mismatch") for error in errors))

    def test_cli_validate_pass_and_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            good = Path(tmp) / "good.json"
            bad = Path(tmp) / "bad.json"
            good.write_text(json.dumps(valid_judgment(), sort_keys=True))
            bad_value = valid_judgment()
            bad_value["blinded_package_sha256"] = "not-a-sha"
            bad.write_text(json.dumps(bad_value, sort_keys=True))
            good_run = subprocess.run(
                [
                    sys.executable,
                    "system/tests/solve_vein_analysis/vms41r1_manual_judgment_contract.py",
                    "--validate",
                    str(good),
                ],
                cwd=contract.REPO_ROOT,
                text=True,
                capture_output=True,
                check=True,
            )
            bad_run = subprocess.run(
                [
                    sys.executable,
                    "system/tests/solve_vein_analysis/vms41r1_manual_judgment_contract.py",
                    "--validate",
                    str(bad),
                ],
                cwd=contract.REPO_ROOT,
                text=True,
                capture_output=True,
            )
        self.assertIn('"verdict": "PASS"', good_run.stdout)
        self.assertEqual(bad_run.returncode, 2)
        self.assertIn("blinded_package_sha256_invalid", bad_run.stderr)


if __name__ == "__main__":
    unittest.main()
