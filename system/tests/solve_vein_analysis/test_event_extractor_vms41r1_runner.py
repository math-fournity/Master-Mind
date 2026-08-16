"""Regression tests for the VMS-41R1 zero-model runner shell."""

from __future__ import annotations

import ast
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

from system.tests.solve_vein_analysis.freeze_vms41r1_event_extractor_preexecution import (
    FREEZE_TARGET,
)
from system.tests.solve_vein_analysis.run_vms41r1_event_extractor_qualification import (
    EXPECTED_VISIBLE_FILES,
    EXPECTED_WRITABLE_FILES,
    HIDDEN_FORBIDDEN_FILES,
    VMS41R1RunnerError,
    build_preflight_receipt,
    load_and_validate_freeze,
    main,
)


class VMS41R1RunnerShellTests(unittest.TestCase):
    def test_preflight_receipt_is_zero_model_and_ready_for_authorization(self) -> None:
        receipt = build_preflight_receipt()
        self.assertEqual(receipt["schema_version"], "solve-vein/vms41r1-runner-preflight/v1")
        self.assertEqual(receipt["poc_id"], "POC-VMS-41R1")
        self.assertEqual(receipt["case_count"], 6)
        self.assertEqual(receipt["attempt_count"], 6)
        self.assertEqual(receipt["workspace_plan_verdict"], "PASS")
        self.assertEqual(receipt["hidden_public_split_verdict"], "PASS")
        self.assertEqual(receipt["live_authorization_status"], "NOT_AUTHORIZED")
        self.assertEqual(receipt["overall_status"], "READY_FOR_AUTHORIZATION")
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))

    def test_attempt_plan_has_exact_workspace_visible_and_writable_sets(self) -> None:
        receipt = build_preflight_receipt()
        observed_ids = set()
        for row in receipt["attempt_plan"]:
            observed_ids.add(row["attempt_id"])
            self.assertEqual(row["candidate_visible_files"], list(EXPECTED_VISIBLE_FILES))
            self.assertEqual(row["candidate_writable_files"], list(EXPECTED_WRITABLE_FILES))
            self.assertEqual(row["hidden_files_forbidden"], list(HIDDEN_FORBIDDEN_FILES))
            self.assertEqual(row["workspace_materialization_status"], "PLANNED_NOT_WRITTEN")
        self.assertEqual(len(observed_ids), 6)

    def test_freeze_validation_rejects_side_effect_authorization_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "freeze.json"
            value = json.loads(FREEZE_TARGET.read_text())
            value["side_effect_authorization"]["devin_sessions_authorized"] = 1
            target.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")
            with self.assertRaises(VMS41R1RunnerError) as caught:
                load_and_validate_freeze(target)
            self.assertEqual(caught.exception.code, "SIDE_EFFECT_NOT_ZERO")

    def test_freeze_validation_rejects_attempt_map_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "freeze.json"
            value = json.loads(FREEZE_TARGET.read_text())
            value["attempt_ids"].pop("V41R1-SYN-TRUE-MERGE")
            target.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")
            with self.assertRaises(VMS41R1RunnerError) as caught:
                load_and_validate_freeze(target)
            self.assertEqual(caught.exception.code, "ATTEMPT_MAP_INVALID")

    def test_execute_flag_fails_closed_without_live_permit(self) -> None:
        with mock.patch.object(sys, "argv", ["runner", "--execute"]):
            with self.assertRaises(VMS41R1RunnerError) as caught:
                main()
        self.assertEqual(caught.exception.code, "LIVE_NOT_AUTHORIZED")


class VMS41R1RunnerShellSurfaceTests(unittest.TestCase):
    def test_runner_shell_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        path = Path(
            "system/tests/solve_vein_analysis/run_vms41r1_event_extractor_qualification.py"
        )
        tree = ast.parse(path.read_text())
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
