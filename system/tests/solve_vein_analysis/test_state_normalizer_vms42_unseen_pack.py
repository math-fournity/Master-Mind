"""Regression tests for the VMS-42 unseen qualification extension pack."""

from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest

from system.tests.solve_vein_analysis import build_vms42_state_normalizer_unseen_pack as unseen_pack


REPO_ROOT = Path(__file__).resolve().parents[3]


class VMS42UnseenQualificationExtensionTests(unittest.TestCase):
    def test_unseen_extension_pack_passes_but_does_not_qualify_profile(self) -> None:
        result = unseen_pack.build_vms42_unseen_qualification_extension()
        self.assertEqual(result["schema_version"], unseen_pack.UNSEEN_EXTENSION_SCHEMA_VERSION)
        self.assertEqual(result["overall_verdict"], "PASS")
        self.assertEqual(
            result["profile_qualification_verdict"],
            "DEVELOPMENT_UNSEEN_EXTENSION_PACK_PASS_NOT_LIVE_QUALIFIED",
        )
        self.assertEqual(result["case_count"], 2)
        self.assertEqual(result["reference_candidate_count"], 2)
        self.assertEqual(result["negative_candidate_count"], 2)
        self.assertEqual(set(result["base_case_ids"]) & set(result["unseen_case_ids"]), set())

    def test_same_fixture_as_base_is_rejected_as_case_overlap(self) -> None:
        with self.assertRaises(unseen_pack.VMS42UnseenPackError) as caught:
            unseen_pack.build_vms42_unseen_qualification_extension(
                base_fixture=unseen_pack.UNSEEN_FIXTURE,
                unseen_fixture=unseen_pack.UNSEEN_FIXTURE,
            )
        self.assertEqual(caught.exception.code, "CASE_ID_OVERLAP_WITH_BASE_FIXTURE")

    def test_candidate_id_overlap_with_base_is_rejected(self) -> None:
        source = json.loads(unseen_pack.UNSEEN_FIXTURE.read_text())
        source["cases"][0]["candidates"][0]["input"]["candidate_id"] = "v42-multiaxis-separated-pass"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "overlap.json"
            path.write_text(json.dumps(source, ensure_ascii=False), encoding="utf-8")
            with self.assertRaises(unseen_pack.VMS42UnseenPackError) as caught:
                unseen_pack.build_vms42_unseen_qualification_extension(unseen_fixture=path)
        self.assertEqual(caught.exception.code, "CANDIDATE_ID_OVERLAP_WITH_BASE_FIXTURE")

    def test_expected_verdict_drift_is_rejected_before_extension_pass(self) -> None:
        source = json.loads(unseen_pack.UNSEEN_FIXTURE.read_text())
        source["cases"][0]["candidates"][0]["expected_verdict"] = "FAIL"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "drift.json"
            path.write_text(json.dumps(source, ensure_ascii=False), encoding="utf-8")
            with self.assertRaises(Exception):
                unseen_pack.build_vms42_unseen_qualification_extension(unseen_fixture=path)

    def test_public_manifest_keeps_hidden_dictionary_and_acceptables_out(self) -> None:
        result = unseen_pack.build_vms42_unseen_qualification_extension()
        public_keys = _walk_keys(result["public_manifest"])
        self.assertNotIn("dictionary", public_keys)
        self.assertNotIn("acceptable_set", public_keys)
        self.assertNotIn("expected_verdict", public_keys)
        self.assertNotIn("raw_axis_claims", public_keys)

    def test_public_and_hidden_manifest_hashes_are_bound_to_unseen_pack_id(self) -> None:
        result = unseen_pack.build_vms42_unseen_qualification_extension()
        self.assertEqual(result["public_manifest"]["pack_id"], unseen_pack.UNSEEN_PACK_ID)
        self.assertEqual(result["hidden_manifest"]["pack_id"], unseen_pack.UNSEEN_PACK_ID)
        tampered = deepcopy(result)
        tampered["public_manifest"]["pack_id"] = "wrong-pack"
        with self.assertRaises(unseen_pack.VMS42UnseenPackError) as caught:
            unseen_pack._verify_extension_summary(tampered)
        self.assertEqual(caught.exception.code, "PUBLIC_PACK_ID_MISMATCH")

    def test_cli_outputs_pass_receipt(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/build_vms42_state_normalizer_unseen_pack.py",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(receipt["side_effects"]["model_calls"], 0)

    def test_unseen_pack_builder_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        roots = unseen_pack.assert_no_forbidden_imports(Path(unseen_pack.__file__))
        self.assertNotIn("arango", roots)
        self.assertNotIn("socket", roots)
        self.assertNotIn("subprocess", roots)

def _walk_keys(value: object) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(_walk_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(_walk_keys(child))
    return keys


if __name__ == "__main__":
    unittest.main()
