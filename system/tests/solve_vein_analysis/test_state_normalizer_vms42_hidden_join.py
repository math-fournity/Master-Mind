"""Regression tests for the zero-model VMS-42 state-normalizer hidden join."""

from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import unittest

from system.tests.solve_vein_analysis import vms42_state_normalizer_hidden_join as join


REPO_ROOT = Path(__file__).resolve().parents[3]


class VMS42StateNormalizerHiddenJoinTests(unittest.TestCase):
    def test_reference_candidate_bundle_hidden_join_passes_development_only(self) -> None:
        bundle = join.build_reference_candidate_bundle()
        receipt = join.hidden_join_state_normalizer_candidates(bundle)
        self.assertEqual(receipt["schema_version"], join.HIDDEN_JOIN_SCHEMA_VERSION)
        self.assertEqual(receipt["candidate_count"], 2)
        self.assertEqual(receipt["pass_count"], 2)
        self.assertEqual(receipt["fail_count"], 0)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(
            receipt["profile_qualification_verdict"],
            "DEVELOPMENT_REFERENCE_JOIN_PASS_NOT_LIVE_QUALIFIED",
        )
        self.assertEqual(receipt["side_effects"]["model_calls"], 0)

    def test_negative_candidate_bundle_hidden_join_fails_without_exception(self) -> None:
        bundle = join.build_negative_candidate_bundle()
        receipt = join.hidden_join_state_normalizer_candidates(bundle)
        self.assertEqual(receipt["candidate_count"], 2)
        self.assertEqual(receipt["pass_count"], 0)
        self.assertEqual(receipt["fail_count"], 2)
        self.assertEqual(receipt["overall_verdict"], "FAIL")
        self.assertEqual(receipt["profile_qualification_verdict"], "JOIN_FAIL_NOT_QUALIFIED")

    def test_public_manifest_hash_mismatch_is_rejected_before_hidden_evaluation(self) -> None:
        bundle = join.build_reference_candidate_bundle()
        bundle["public_manifest_sha256"] = "0" * 64
        with self.assertRaises(join.VMS42HiddenJoinError) as caught:
            join.hidden_join_state_normalizer_candidates(bundle)
        self.assertEqual(caught.exception.code, "PUBLIC_MANIFEST_HASH_MISMATCH")

    def test_candidate_input_hash_mismatch_is_rejected(self) -> None:
        bundle = join.build_reference_candidate_bundle()
        bundle["candidates"][0]["candidate_input"]["raw_axis_claims"][0]["raw_value"] = "changed"
        with self.assertRaises(join.VMS42HiddenJoinError) as caught:
            join.hidden_join_state_normalizer_candidates(bundle)
        self.assertEqual(caught.exception.code, "CANDIDATE_INPUT_HASH_MISMATCH")

    def test_candidate_bundle_hidden_key_leak_is_rejected(self) -> None:
        bundle = join.build_reference_candidate_bundle()
        bundle["acceptable_set"] = {"leak": True}
        with self.assertRaises(join.VMS42HiddenJoinError) as caught:
            join.hidden_join_state_normalizer_candidates(bundle)
        self.assertEqual(caught.exception.code, "CANDIDATE_BUNDLE_KEYS_INVALID")

    def test_candidate_nested_hidden_key_leak_is_rejected(self) -> None:
        bundle = join.build_reference_candidate_bundle()
        tampered = deepcopy(bundle)
        tampered["candidates"][0]["candidate_input"]["expected_verdict"] = "PASS"
        tampered["candidates"][0]["candidate_input_sha256"] = join.sha256_json(
            tampered["candidates"][0]["candidate_input"]
        )
        with self.assertRaises(join.VMS42HiddenJoinError) as caught:
            join.hidden_join_state_normalizer_candidates(tampered)
        self.assertEqual(caught.exception.code, "CANDIDATE_BUNDLE_LEAKS_HIDDEN_KEY")

    def test_cli_outputs_zero_side_effect_hidden_join_receipt(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/vms42_state_normalizer_hidden_join.py",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(receipt["candidate_count"], 2)
        self.assertEqual(receipt["side_effects"]["files_written"], 0)

    def test_hidden_join_surface_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        roots = join.assert_no_forbidden_imports(Path(join.__file__))
        self.assertNotIn("arango", roots)
        self.assertNotIn("subprocess", roots)


if __name__ == "__main__":
    unittest.main()
