"""Regression tests for the frozen VMS-41R1 qualification pack."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from system.tests.solve_vein_analysis.build_vms41r1_qualification_pack import (
    CASE_ORDER,
    EXPECTED_NONCLAIMS,
    FIXTURE_ROOT,
    OLD_VMS41_SOURCE_IDS,
    PACK_ID,
    VMS41R1PackError,
    evaluate_reference_cases,
    load_vms41r1_qualification_pack,
)


class VMS41R1QualificationPackTests(unittest.TestCase):
    def test_frozen_pack_loads_and_replays_reference_self_check(self) -> None:
        result = load_vms41r1_qualification_pack()
        self.assertEqual(result["pack_id"], PACK_ID)
        self.assertEqual(result["case_count"], 6)
        self.assertEqual(result["reference_candidate_count"], 6)
        self.assertEqual(result["negative_check_count"], 4)
        self.assertEqual(result["summary"]["verdict"], "PASS")
        self.assertEqual(result["model_calls_authorized"], 0)
        self.assertEqual(result["database_calls_authorized"], 0)
        self.assertEqual(result["solver_calls_authorized"], 0)

    def test_manifest_case_order_nonclaims_and_attempts_are_exact(self) -> None:
        manifest = self._json(FIXTURE_ROOT / "pack-manifest.json")
        self.assertEqual(tuple(manifest["case_order"]), CASE_ORDER)
        self.assertEqual(manifest["explicit_nonclaims"], list(EXPECTED_NONCLAIMS))
        self.assertEqual(sorted(manifest["attempt_ids"]), sorted(CASE_ORDER))
        self.assertTrue(
            all(value.startswith("poc-vms-41r1-") for value in manifest["attempt_ids"].values())
        )
        self.assertEqual(manifest["model_calls_authorized"], 0)
        self.assertEqual(manifest["database_calls_authorized"], 0)
        self.assertEqual(manifest["solver_calls_authorized"], 0)

    def test_public_case_manifests_do_not_expose_hidden_gold(self) -> None:
        hidden_names = {
            "acceptable-sets.json",
            "reference-candidates.json",
            "negative-checks.json",
        }
        for case_id in CASE_ORDER:
            public_manifest = self._json(FIXTURE_ROOT / case_id / "input-manifest.json")
            self.assertEqual(public_manifest["case_id"], case_id)
            self.assertEqual(
                public_manifest["public_files"],
                ["problem.md", "raw_solver_trajectory.txt", "input-manifest.json"],
            )
            self.assertTrue(hidden_names.issubset(public_manifest["hidden_files_forbidden"]))
            for hidden_name in hidden_names:
                self.assertFalse((FIXTURE_ROOT / case_id / hidden_name).exists())

    def test_real_source_receipt_is_self_contained_and_not_vms41_source(self) -> None:
        receipt = self._json(
            FIXTURE_ROOT / "V41R1-REAL-GF2-PAGODA" / "source-receipt.json"
        )
        self.assertEqual(receipt["source_id"], "p48cc0b3636be4b9990a9")
        self.assertNotIn(receipt["source_id"], OLD_VMS41_SOURCE_IDS)
        self.assertEqual(set(receipt["excluded_vms41_source_ids"]), OLD_VMS41_SOURCE_IDS)
        raw = (
            FIXTURE_ROOT
            / "V41R1-REAL-GF2-PAGODA"
            / "raw_solver_trajectory.txt"
        ).read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), receipt["selected_sha256"])
        self.assertEqual(receipt["source_mutations"], 0)

    def test_negative_checks_are_replayed_not_trusted(self) -> None:
        acceptable_pack = self._json(FIXTURE_ROOT / "acceptable-sets.json")
        reference_candidates = self._json(FIXTURE_ROOT / "reference-candidates.json")
        checks = self._json(FIXTURE_ROOT / "negative-checks.json")
        sources = {
            case_id: (FIXTURE_ROOT / case_id / "raw_solver_trajectory.txt").read_text()
            for case_id in CASE_ORDER
        }
        summary = evaluate_reference_cases(
            acceptable_pack, reference_candidates, sources, checks
        )
        self.assertEqual(summary, self._json(FIXTURE_ROOT / "reference-self-check-summary.json"))
        self.assertTrue(all(row["matched"] for row in summary["negative_check_rows"]))

    @staticmethod
    def _json(path: Path) -> dict[str, object]:
        value = json.loads(path.read_text())
        assert isinstance(value, dict)
        return value


class VMS41R1QualificationPackIntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "vms41r1"
        shutil.copytree(FIXTURE_ROOT, self.root)

    def test_member_tamper_is_rejected(self) -> None:
        path = self.root / "thresholds.json"
        value = json.loads(path.read_text())
        value["case_count"] = 7
        path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")
        with self.assertRaises(VMS41R1PackError) as caught:
            load_vms41r1_qualification_pack(self.root)
        self.assertIn(
            caught.exception.code,
            {"MANIFEST_MEMBER_SIZE_MISMATCH", "MANIFEST_MEMBER_HASH_MISMATCH"},
        )

    def test_extra_file_is_rejected(self) -> None:
        (self.root / "extra.txt").write_text("not in manifest")
        with self.assertRaises(VMS41R1PackError) as caught:
            load_vms41r1_qualification_pack(self.root)
        self.assertEqual(caught.exception.code, "PACK_FILE_SET_INVALID")

    def test_symlink_member_is_rejected(self) -> None:
        outside = Path(self.temporary.name) / "outside.txt"
        outside.write_text("outside")
        (self.root / "link").symlink_to(outside)
        with self.assertRaises(VMS41R1PackError) as caught:
            load_vms41r1_qualification_pack(self.root)
        self.assertEqual(caught.exception.code, "PACK_SYMLINK_MEMBER")


class VMS41R1BuilderSurfaceTests(unittest.TestCase):
    def test_builder_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        builder = Path(
            "system/tests/solve_vein_analysis/build_vms41r1_qualification_pack.py"
        )
        tree = ast.parse(builder.read_text())
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
