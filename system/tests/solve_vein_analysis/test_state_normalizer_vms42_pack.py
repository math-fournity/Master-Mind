"""Regression tests for the zero-model VMS-42 state-normalizer pack."""

from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest

from system.tests.solve_vein_analysis import build_vms42_state_normalizer_pack as pack


REPO_ROOT = Path(__file__).resolve().parents[3]


class VMS42StateNormalizerPackTests(unittest.TestCase):
    def test_pack_builds_public_hidden_split_and_self_checks(self) -> None:
        result = pack.build_vms42_state_normalizer_pack()
        self.assertEqual(result["schema_version"], pack.PACK_SCHEMA_VERSION)
        self.assertEqual(result["pack_id"], pack.PACK_ID)
        self.assertEqual(result["case_count"], 2)
        self.assertEqual(result["reference_candidate_count"], 2)
        self.assertEqual(result["negative_candidate_count"], 2)
        self.assertEqual(result["overall_verdict"], "PASS")
        self.assertEqual(result["side_effects"]["model_calls"], 0)
        self.assertEqual(result["side_effects"]["files_written"], 0)

    def test_public_manifest_does_not_expose_hidden_gold(self) -> None:
        result = pack.build_vms42_state_normalizer_pack()
        public_keys = pack._walk_keys(result["public_manifest"])  # noqa: SLF001 - intentional leak test
        self.assertTrue(pack.FORBIDDEN_PUBLIC_KEYS.isdisjoint(public_keys))
        for case in result["public_manifest"]["cases"]:
            self.assertIn("expected_occurrence_ids", case)
            self.assertIn("required_axes", case)
            self.assertIn("candidate_output_schema", case)

    def test_reference_and_negative_rows_are_replayed_not_trusted(self) -> None:
        result = pack.build_vms42_state_normalizer_pack()
        self.assertTrue(all(row["expected_verdict"] == "PASS" for row in result["reference_check_rows"]))
        self.assertTrue(all(row["observed_verdict"] == "PASS" for row in result["reference_check_rows"]))
        self.assertEqual(
            [row["expected_verdict"] for row in result["negative_check_rows"]],
            ["FAIL", "INVALID"],
        )
        self.assertEqual(
            [row["observed_verdict"] for row in result["negative_check_rows"]],
            ["FAIL", "INVALID"],
        )

    def test_expected_verdict_tamper_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = json.loads(pack.SOURCE_FIXTURE.read_text())
            source["cases"][0]["candidates"][1]["expected_verdict"] = "PASS"
            path = Path(temporary) / "tampered.json"
            path.write_text(json.dumps(source, ensure_ascii=False, sort_keys=True) + "\n")
            with self.assertRaises(pack.VMS42PackError) as caught:
                pack.build_vms42_state_normalizer_pack(path)
            self.assertIn(
                caught.exception.code,
                {"SOURCE_PACK_SELF_CHECK_FAILED", "EXPECTED_VERDICT_MISMATCH"},
            )

    def test_public_manifest_hash_tamper_is_rejected(self) -> None:
        result = pack.build_vms42_state_normalizer_pack()
        tampered = deepcopy(result)
        tampered["public_manifest"]["cases"][0]["required_axes"].append("LEAKED_AXIS")
        with self.assertRaises(pack.VMS42PackError) as caught:
            pack._verify_pack_summary(tampered)  # noqa: SLF001 - intentional internal contract test
        self.assertEqual(caught.exception.code, "PUBLIC_MANIFEST_HASH_MISMATCH")

    def test_builder_surface_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        roots = pack.assert_no_forbidden_imports(Path(pack.__file__))
        self.assertNotIn("subprocess", roots)
        self.assertNotIn("socket", roots)

    def test_cli_outputs_pack_receipt_without_side_effects(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/build_vms42_state_normalizer_pack.py",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["pack_id"], pack.PACK_ID)
        self.assertEqual(receipt["hidden_manifest_sha256"], pack.sha256_json(receipt["hidden_manifest"]))
        self.assertEqual(receipt["side_effects"]["devin_sessions"], 0)


if __name__ == "__main__":
    unittest.main()
