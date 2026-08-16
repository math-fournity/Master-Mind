"""Regression tests for VMS-42 sealed reviewer judgment contract."""

from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest

from system.tests.solve_vein_analysis import vms42_state_normalizer_hidden_join as hidden_join
from system.tests.solve_vein_analysis import vms42_state_normalizer_manual_judgment_contract as contract


REPO_ROOT = Path(__file__).resolve().parents[3]


def reference_bundle() -> dict[str, object]:
    return hidden_join.build_reference_candidate_bundle()


def valid_judgment() -> dict[str, object]:
    return contract.build_synthetic_reviewer_judgment(reference_bundle())


class VMS42ManualJudgmentContractTests(unittest.TestCase):
    def test_valid_synthetic_judgment_passes_with_candidate_bundle(self) -> None:
        bundle = reference_bundle()
        judgment = contract.build_synthetic_reviewer_judgment(bundle)
        self.assertEqual(contract.validate_manual_judgment(judgment, candidate_bundle=bundle), [])

    def test_contract_summary_has_zero_side_effects_and_no_hidden_join(self) -> None:
        summary = contract.build_contract_summary()
        self.assertEqual(summary["schema_version"], contract.CONTRACT_SUMMARY_SCHEMA_VERSION)
        self.assertTrue(all(value == 0 for value in summary["side_effects"].values()))
        self.assertIn("does_not_run_hidden_join", summary["explicit_nonclaims"])

    def test_rejects_hidden_material_exposure_attestation(self) -> None:
        value = valid_judgment()
        value["reviewer_blinding_attestation"] = {
            "reviewer_view_only": True,
            "dictionary_seen": True,
            "acceptable_set_seen": False,
            "reference_candidates_seen": False,
            "hidden_join_result_seen": False,
        }
        self.assertIn("reviewer_blinding_attestation_invalid", contract.validate_manual_judgment(value))

    def test_rejects_candidate_bundle_hash_mismatch(self) -> None:
        bundle = reference_bundle()
        value = contract.build_synthetic_reviewer_judgment(bundle)
        value["candidate_bundle_sha256"] = "0" * 64
        self.assertIn(
            "candidate_bundle_sha256_mismatch",
            contract.validate_manual_judgment(value, candidate_bundle=bundle),
        )

    def test_rejects_reviewed_candidate_drift(self) -> None:
        bundle = reference_bundle()
        value = contract.build_synthetic_reviewer_judgment(bundle)
        value["reviewed_candidates"][0]["candidate_id"] = "wrong-candidate"  # type: ignore[index]
        self.assertIn(
            "reviewed_candidates_mismatch",
            contract.validate_manual_judgment(value, candidate_bundle=bundle),
        )

    def test_rejects_manual_pass_with_failed_axis(self) -> None:
        value = valid_judgment()
        value["axis_verdicts"]["raw_axis_claim_source_fidelity"] = "FAIL"  # type: ignore[index]
        self.assertIn("manual_pass_requires_all_axes_pass", contract.validate_manual_judgment(value))

    def test_rejects_duplicate_reviewed_candidate(self) -> None:
        value = valid_judgment()
        value["reviewed_candidates"].append(deepcopy(value["reviewed_candidates"][0]))  # type: ignore[index]
        errors = contract.validate_manual_judgment(value)
        self.assertTrue(any(error.startswith("reviewed_candidate_duplicate") for error in errors))

    def test_rejects_missing_nonclaim(self) -> None:
        value = valid_judgment()
        value["explicit_nonclaims"] = ["does_not_run_hidden_join"]
        self.assertIn("explicit_nonclaims_missing", contract.validate_manual_judgment(value))

    def test_cli_validate_pass_and_fail_with_candidate_bundle(self) -> None:
        bundle = reference_bundle()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle_path = root / "bundle.json"
            good_path = root / "good.json"
            bad_path = root / "bad.json"
            bundle_path.write_text(json.dumps(bundle, ensure_ascii=False, sort_keys=True))
            good_path.write_text(json.dumps(contract.build_synthetic_reviewer_judgment(bundle), sort_keys=True))
            bad = contract.build_synthetic_reviewer_judgment(bundle)
            bad["public_manifest_sha256"] = "0" * 64
            bad_path.write_text(json.dumps(bad, sort_keys=True))
            good_run = subprocess.run(
                [
                    sys.executable,
                    "system/tests/solve_vein_analysis/vms42_state_normalizer_manual_judgment_contract.py",
                    "--validate",
                    str(good_path),
                    "--candidate-bundle",
                    str(bundle_path),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=True,
            )
            bad_run = subprocess.run(
                [
                    sys.executable,
                    "system/tests/solve_vein_analysis/vms42_state_normalizer_manual_judgment_contract.py",
                    "--validate",
                    str(bad_path),
                    "--candidate-bundle",
                    str(bundle_path),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )
        self.assertIn('"verdict": "PASS"', good_run.stdout)
        self.assertEqual(bad_run.returncode, 2)
        self.assertIn("public_manifest_sha256_mismatch", bad_run.stderr)

    def test_contract_surface_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        roots = contract.assert_no_forbidden_imports(Path(contract.__file__))
        self.assertNotIn("arango", roots)
        self.assertNotIn("subprocess", roots)


if __name__ == "__main__":
    unittest.main()
