"""Regression tests for the VMS-41R1 zero-model preexecution freeze."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from system.solve_vein_analysis.models import canonical_json_bytes
from system.tests.solve_vein_analysis.build_vms41r1_qualification_pack import (
    ATTEMPT_IDS,
    CASE_ORDER,
    FIXTURE_ROOT,
)
from system.tests.solve_vein_analysis.freeze_vms41r1_event_extractor_preexecution import (
    EXPLICIT_NONCLAIMS,
    FREEZE_TARGET,
    SCHEMA_VERSION,
    VMS41R1FreezeError,
    build_freeze_payload,
    write_or_verify_freeze,
)


class VMS41R1PreexecutionFreezeTests(unittest.TestCase):
    def test_default_freeze_matches_current_deterministic_payload(self) -> None:
        payload = build_freeze_payload()
        frozen = json.loads(FREEZE_TARGET.read_text())
        self.assertEqual(frozen, payload)
        self.assertEqual(frozen["schema_version"], SCHEMA_VERSION)
        self.assertEqual(frozen["qualification_pack"]["case_count"], 6)
        self.assertEqual(
            frozen["qualification_pack"]["manifest_sha256"],
            hashlib.sha256((FIXTURE_ROOT / "pack-manifest.json").read_bytes()).hexdigest(),
        )
        self.assertEqual(tuple(frozen["case_order"]), CASE_ORDER)
        self.assertEqual(frozen["attempt_ids"], ATTEMPT_IDS)
        self.assertEqual(frozen["planned_live_attempts"], 6)
        self.assertEqual(frozen["explicit_nonclaims"], list(EXPLICIT_NONCLAIMS))

    def test_default_freeze_reverification_is_append_once(self) -> None:
        before = FREEZE_TARGET.read_bytes()
        result = write_or_verify_freeze()
        self.assertEqual(result["operation"], "ALREADY_FROZEN")
        self.assertEqual(FREEZE_TARGET.read_bytes(), before)
        self.assertEqual(result["model_calls_authorized"], 0)
        self.assertEqual(result["devin_sessions_authorized"], 0)
        self.assertEqual(result["solver_calls_authorized"], 0)
        self.assertEqual(result["database_connections_authorized"], 0)

    def test_temp_output_creation_and_drift_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "freeze.json"
            result = write_or_verify_freeze(target)
            self.assertEqual(result["operation"], "FROZEN")
            self.assertEqual(json.loads(target.read_text()), build_freeze_payload())
            self.assertEqual(target.read_bytes(), canonical_json_bytes(build_freeze_payload()))

            target.write_text("{}\n")
            with self.assertRaises(VMS41R1FreezeError) as caught:
                write_or_verify_freeze(target)
            self.assertEqual(caught.exception.code, "FREEZE_TARGET_DRIFT")

    def test_side_effect_authorization_is_zero_and_live_requires_new_authorization(self) -> None:
        payload = build_freeze_payload()
        auth = payload["side_effect_authorization"]
        self.assertEqual(auth["model_calls_authorized"], 0)
        self.assertEqual(auth["devin_sessions_authorized"], 0)
        self.assertEqual(auth["solver_calls_authorized"], 0)
        self.assertEqual(auth["database_connections_authorized"], 0)
        self.assertEqual(auth["redis_connections_authorized"], 0)
        self.assertEqual(auth["network_calls_authorized"], 0)
        self.assertTrue(auth["future_live_attempts_require_new_explicit_authorization"])
        self.assertEqual(payload["runtime_profile_request"]["effective_model_probe"], "NOT_RUN_IN_THIS_PREFREEZE")
        self.assertEqual(payload["blind_review"]["status"], "NOT_STARTED")


class VMS41R1PreexecutionFreezeSurfaceTests(unittest.TestCase):
    def test_freeze_builder_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        path = Path(
            "system/tests/solve_vein_analysis/freeze_vms41r1_event_extractor_preexecution.py"
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
