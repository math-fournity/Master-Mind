"""Fail-closed replay tests for the immutable VMS-41R1 calibration pack."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from system.tests.solve_vein_analysis.run_event_extractor_calibration import (
    CalibrationError,
    DEFAULT_FIXTURE_ROOT,
    EXPECTED_NONCLAIMS,
    apply_frozen_mutations,
    load_calibration_pack,
    run_calibration_pack,
)


class CalibrationReplayTests(unittest.TestCase):
    def test_frozen_pack_replays_all_axes_without_mismatch(self) -> None:
        result = run_calibration_pack()
        self.assertEqual(result["verdict"], "PASS")
        self.assertTrue(result["all_expected_verdicts_matched"])
        self.assertEqual(result["candidate_scenario_count"], 13)
        self.assertEqual(result["file_effect_scenario_count"], 6)
        self.assertEqual(result["mismatches"], [])
        self.assertTrue(all(row["matched"] for row in result["candidate_results"]))
        self.assertTrue(all(row["matched"] for row in result["file_effect_results"]))

    def test_pack_is_development_only_and_preserves_nonclaims(self) -> None:
        result = run_calibration_pack()
        self.assertEqual(result["evidence_lane"], "DEVELOPMENT_ONLY")
        self.assertEqual(tuple(result["explicit_nonclaims"]), EXPECTED_NONCLAIMS)
        self.assertIn("DOES_NOT_QUALIFY_ANY_MODEL_PROFILE", result["explicit_nonclaims"])
        self.assertIn("DOES_NOT_AUTHORIZE_LIVE_EXECUTION", result["explicit_nonclaims"])

    def test_fine_and_direct_histories_both_pass_but_are_distinct_inputs(self) -> None:
        rows = {
            row["scenario_id"]: row
            for row in run_calibration_pack()["candidate_results"]
        }
        self.assertTrue(rows["C01"]["matched"])
        self.assertTrue(rows["C02"]["matched"])
        self.assertEqual(rows["C01"]["observed"], rows["C02"]["observed"])
        self.assertNotEqual(
            rows["C01"]["materialized_candidate_sha256"],
            rows["C02"]["materialized_candidate_sha256"],
        )

    def test_scenario_identity_sets_are_exact(self) -> None:
        pack = load_calibration_pack()
        candidate_ids = [
            row["scenario_id"] for row in pack["matrix"]["candidate_scenarios"]
        ]
        file_ids = [
            row["scenario_id"] for row in pack["matrix"]["file_effect_scenarios"]
        ]
        self.assertEqual(candidate_ids, [f"C{value:02d}" for value in range(1, 14)])
        self.assertEqual(file_ids, [f"F{value:02d}" for value in range(1, 7)])


class CalibrationPackIntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "pack"
        shutil.copytree(DEFAULT_FIXTURE_ROOT, self.root)

    def test_member_tamper_is_rejected(self) -> None:
        path = self.root / "source.txt"
        path.write_bytes(path.read_bytes() + b"tamper")
        with self.assertRaises(CalibrationError) as caught:
            load_calibration_pack(self.root)
        self.assertIn(
            caught.exception.code,
            {"MANIFEST_MEMBER_SIZE_MISMATCH", "MANIFEST_MEMBER_HASH_MISMATCH"},
        )

    def test_extra_member_is_rejected(self) -> None:
        (self.root / "unlisted.txt").write_text("not part of the frozen pack")
        with self.assertRaises(CalibrationError) as caught:
            load_calibration_pack(self.root)
        self.assertEqual(caught.exception.code, "FIXTURE_FILE_SET_INVALID")

    def test_symlink_member_is_rejected(self) -> None:
        target = Path(self.temporary.name) / "outside.txt"
        target.write_text("outside")
        (self.root / "extra-link").symlink_to(target)
        with self.assertRaises(CalibrationError) as caught:
            load_calibration_pack(self.root)
        self.assertEqual(caught.exception.code, "FIXTURE_NONREGULAR_MEMBER")

    def test_expected_verdict_tamper_is_detected_not_learned(self) -> None:
        matrix_path = self.root / "scenario-matrix.json"
        matrix = json.loads(matrix_path.read_text())
        matrix["candidate_scenarios"][0]["expected"]["protocol_verdict"] = "FAIL"
        self._rewrite_member_and_manifest("scenario-matrix.json", matrix)
        result = run_calibration_pack(self.root)
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual([row["scenario_id"] for row in result["mismatches"]], ["C01"])
        self.assertEqual(
            result["candidate_results"][0]["observed"]["protocol_verdict"], "PASS"
        )

    def _rewrite_member_and_manifest(self, member: str, value: object) -> None:
        path = self.root / member
        payload = (
            json.dumps(
                value,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
            + "\n"
        ).encode()
        path.write_bytes(payload)
        manifest_path = self.root / "pack-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        row = next(item for item in manifest["files"] if item["path"] == member)
        row["bytes"] = len(payload)
        row["sha256"] = hashlib.sha256(payload).hexdigest()
        manifest_path.write_text(
            json.dumps(
                manifest,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
            + "\n"
        )


class FrozenMutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.value = {"events": [{"value": 1}, {"value": 2}]}

    def assert_mutation_code(self, mutation: object, code: str) -> None:
        with self.assertRaises(CalibrationError) as caught:
            apply_frozen_mutations(self.value, [mutation])
        self.assertEqual(caught.exception.code, code)

    def test_only_replace_and_remove_are_supported(self) -> None:
        self.assert_mutation_code(
            {"op": "add", "path": "/events/0/value", "value": 3},
            "MUTATION_OPERATION_INVALID",
        )

    def test_replace_target_must_exist(self) -> None:
        self.assert_mutation_code(
            {"op": "replace", "path": "/events/0/missing", "value": 3},
            "MUTATION_TARGET_MISSING",
        )

    def test_pointer_must_be_canonical_and_cannot_append(self) -> None:
        self.assert_mutation_code(
            {"op": "remove", "path": "/events/01"},
            "JSON_POINTER_ARRAY_INDEX_INVALID",
        )
        self.assert_mutation_code(
            {"op": "remove", "path": "/events/-"},
            "JSON_POINTER_SEGMENT_INVALID",
        )
        self.assert_mutation_code(
            {"op": "remove", "path": "/"},
            "JSON_POINTER_INVALID",
        )


class RunnerSurfaceTests(unittest.TestCase):
    def test_runner_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        runner = Path(
            "system/tests/solve_vein_analysis/run_event_extractor_calibration.py"
        )
        tree = ast.parse(runner.read_text())
        roots: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                roots.add(node.module.split(".")[0])
        self.assertTrue(
            roots.isdisjoint(
                {
                    "arango",
                    "http",
                    "requests",
                    "socket",
                    "subprocess",
                    "urllib",
                }
            )
        )


if __name__ == "__main__":
    unittest.main()
