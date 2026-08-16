"""Regression tests for VMS-42 final reviewer + hidden-join receipt."""

from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import unittest

from system.tests.solve_vein_analysis import vms42_state_normalizer_final_join_receipt as final_join
from system.tests.solve_vein_analysis import vms42_state_normalizer_hidden_join as hidden_join
from system.tests.solve_vein_analysis import vms42_state_normalizer_manual_judgment_contract as manual


REPO_ROOT = Path(__file__).resolve().parents[3]


class VMS42FinalJoinReceiptTests(unittest.TestCase):
    def test_synthetic_reference_final_join_passes_but_not_live_qualified(self) -> None:
        receipt = final_join.build_synthetic_final_join_receipt()
        self.assertEqual(receipt["schema_version"], final_join.FINAL_JOIN_SCHEMA_VERSION)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(
            receipt["profile_qualification_verdict"],
            "DEVELOPMENT_SYNTHETIC_FINAL_JOIN_PASS_NOT_LIVE_QUALIFIED",
        )
        self.assertEqual(receipt["candidate_count"], 2)
        self.assertEqual(receipt["hidden_fail_count"], 0)

    def test_hidden_fail_preserved_as_final_fail(self) -> None:
        bundle = hidden_join.build_negative_candidate_bundle()
        reviewer = manual.build_synthetic_reviewer_judgment(bundle)
        hidden = hidden_join.hidden_join_state_normalizer_candidates(bundle)
        receipt = final_join.final_join_reviewer_and_hidden_receipts(
            candidate_bundle=bundle,
            reviewer_judgment=reviewer,
            hidden_join_receipt=hidden,
        )
        self.assertEqual(receipt["overall_verdict"], "FAIL")
        self.assertEqual(receipt["hidden_fail_count"], 2)
        self.assertEqual(receipt["profile_qualification_verdict"], "FINAL_JOIN_FAIL_NOT_QUALIFIED")

    def test_manual_fail_preserved_as_final_fail_even_when_hidden_passes(self) -> None:
        inputs = final_join.build_synthetic_final_join_inputs()
        reviewer = deepcopy(inputs["reviewer_judgment"])
        reviewer["axis_verdicts"]["public_manifest_alignment"] = "FAIL"
        reviewer["final_manual_verdict"] = "MANUAL_FAIL"
        receipt = final_join.final_join_reviewer_and_hidden_receipts(
            candidate_bundle=inputs["candidate_bundle"],
            reviewer_judgment=reviewer,
            hidden_join_receipt=inputs["hidden_join_receipt"],
        )
        self.assertEqual(receipt["manual_verdict"], "MANUAL_FAIL")
        self.assertEqual(receipt["hidden_join_verdict"], "PASS")
        self.assertEqual(receipt["overall_verdict"], "FAIL")

    def test_candidate_bundle_hash_mismatch_is_rejected(self) -> None:
        inputs = final_join.build_synthetic_final_join_inputs()
        hidden = deepcopy(inputs["hidden_join_receipt"])
        hidden["candidate_bundle_sha256"] = "0" * 64
        with self.assertRaises(final_join.VMS42FinalJoinError) as caught:
            final_join.final_join_reviewer_and_hidden_receipts(
                candidate_bundle=inputs["candidate_bundle"],
                reviewer_judgment=inputs["reviewer_judgment"],
                hidden_join_receipt=hidden,
            )
        self.assertEqual(caught.exception.code, "CANDIDATE_BUNDLE_HASH_MISMATCH")

    def test_invalid_reviewer_judgment_is_rejected_before_join(self) -> None:
        inputs = final_join.build_synthetic_final_join_inputs()
        reviewer = deepcopy(inputs["reviewer_judgment"])
        reviewer["reviewer_blinding_attestation"]["hidden_join_result_seen"] = True
        with self.assertRaises(final_join.VMS42FinalJoinError) as caught:
            final_join.final_join_reviewer_and_hidden_receipts(
                candidate_bundle=inputs["candidate_bundle"],
                reviewer_judgment=reviewer,
                hidden_join_receipt=inputs["hidden_join_receipt"],
            )
        self.assertEqual(caught.exception.code, "REVIEWER_JUDGMENT_INVALID")

    def test_public_manifest_hash_mismatch_is_rejected(self) -> None:
        inputs = final_join.build_synthetic_final_join_inputs()
        hidden = deepcopy(inputs["hidden_join_receipt"])
        hidden["public_manifest_sha256"] = "0" * 64
        with self.assertRaises(final_join.VMS42FinalJoinError) as caught:
            final_join.final_join_reviewer_and_hidden_receipts(
                candidate_bundle=inputs["candidate_bundle"],
                reviewer_judgment=inputs["reviewer_judgment"],
                hidden_join_receipt=hidden,
            )
        self.assertEqual(caught.exception.code, "PUBLIC_MANIFEST_HASH_MISMATCH")

    def test_cli_outputs_reference_and_negative_receipts(self) -> None:
        positive = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/vms42_state_normalizer_final_join_receipt.py",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        negative = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/vms42_state_normalizer_final_join_receipt.py",
                "--negative",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertEqual(json.loads(positive.stdout)["overall_verdict"], "PASS")
        self.assertEqual(json.loads(negative.stdout)["overall_verdict"], "FAIL")

    def test_final_join_surface_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        roots = final_join.assert_no_forbidden_imports(Path(final_join.__file__))
        self.assertNotIn("arango", roots)
        self.assertNotIn("subprocess", roots)


if __name__ == "__main__":
    unittest.main()
