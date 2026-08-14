from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from seven_system.config import ConfigError, SevenConfig, load_config  # noqa: E402
from seven_system.preflight import capability_subject_hashes, run_preflight  # noqa: E402
from support import build_site, patched_site, write_pass_capability  # noqa: E402


class PreflightTests(unittest.TestCase):
    def test_dry_run_passes_without_db_or_live_capabilities(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, _ = build_site(Path(directory))
            payload = json.loads(config_path.read_text(encoding="utf-8"))
            with patched_site(payload), patch.dict(os.environ, {}, clear=True):
                report = run_preflight(load_config(config_path))
            self.assertEqual(report["overall_verdict"], "PASS")
            self.assertEqual(report["side_effects"], "NONE")
            self.assertEqual(report["allowed_phases"], ["P0", "P1"])

    def test_data_root_inside_repo_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path, payload = build_site(root)
            bad_root = Path(payload["repository_root"]) / "runtime"
            bad_root.mkdir()
            payload["storage"]["data_root"] = str(bad_root)
            payload["answers"]["vault_root"] = str(bad_root / "vault")
            config_path.write_text(json.dumps(payload), encoding="utf-8")
            with patched_site(payload):
                report = run_preflight(load_config(config_path))
            self.assertEqual(report["overall_verdict"], "BLOCKED")
            self.assertIn("data_root_boundary", report["blockers"])

    def test_math_queue_namespace_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            payload["control"]["redis_namespace"] = "math:"
            config_path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaises(ConfigError):
                load_config(config_path)
            with patched_site(payload):
                report = run_preflight(SevenConfig.from_mapping(payload))
            self.assertIn("queue_namespace", report["blockers"])

    def test_live_mode_remains_blocked_even_with_capability_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path, payload = build_site(root, mode="golden_slice")
            capability_paths = []
            for section, key, name in (
                ("database", "capability_report", "database"),
                ("solver", "safe_launch_capability_report", "safe_launch"),
                ("solver", "no_tool_capability_report", "no_tool"),
                ("answers", "capability_report", "answer_isolation"),
            ):
                report_path = root / f"{name}.json"
                payload[section][key] = str(report_path)
                capability_paths.append((report_path, name))
            payload["solver"]["allow_live_dispatch"] = True
            config_path.write_text(json.dumps(payload), encoding="utf-8")
            with patched_site(payload):
                subjects = capability_subject_hashes(load_config(config_path))
            for report_path, name in capability_paths:
                write_pass_capability(
                    report_path, name, subject_hash=subjects[name]
                )
            with patched_site(payload), patch.dict(
                os.environ, {"ARANGO_DB": "xishujuzhen_math_glm52"}, clear=True
            ):
                report = run_preflight(load_config(config_path))
            self.assertEqual(report["overall_verdict"], "BLOCKED")
            self.assertIn("database_capability", report["blockers"])
            self.assertIn("live_execution_implementation", report["blockers"])

    def test_capability_top_level_pass_cannot_hide_failed_check(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path, payload = build_site(root, mode="golden_slice")
            report_path = root / "no_tool.json"
            payload["solver"]["no_tool_capability_report"] = str(report_path)
            config_path.write_text(json.dumps(payload), encoding="utf-8")
            with patched_site(payload):
                subject = capability_subject_hashes(load_config(config_path))["no_tool"]
            write_pass_capability(report_path, "no_tool", subject_hash=subject)
            capability = json.loads(report_path.read_text(encoding="utf-8"))
            capability["checks"][0]["verdict"] = "FAIL"
            report_path.write_text(json.dumps(capability), encoding="utf-8")
            config_path.write_text(json.dumps(payload), encoding="utf-8")

            with patched_site(payload):
                report = run_preflight(load_config(config_path))
            self.assertIn("no_tool_capability", report["blockers"])

    def test_incomplete_capability_claims_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path, payload = build_site(root, mode="golden_slice")
            report_path = root / "no_tool.json"
            payload["solver"]["no_tool_capability_report"] = str(report_path)
            config_path.write_text(json.dumps(payload), encoding="utf-8")
            with patched_site(payload):
                subject = capability_subject_hashes(load_config(config_path))["no_tool"]
            write_pass_capability(report_path, "no_tool", subject_hash=subject)
            capability = json.loads(report_path.read_text(encoding="utf-8"))
            del capability["claims"]["missing_observation_fails_closed"]
            report_path.write_text(json.dumps(capability), encoding="utf-8")
            config_path.write_text(json.dumps(payload), encoding="utf-8")

            with patched_site(payload):
                report = run_preflight(load_config(config_path))
            self.assertIn("no_tool_capability", report["blockers"])

    def test_capability_subject_must_match_current_site(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path, payload = build_site(root, mode="golden_slice")
            report_path = root / "no_tool.json"
            write_pass_capability(report_path, "no_tool", subject_hash="0" * 64)
            payload["solver"]["no_tool_capability_report"] = str(report_path)
            config_path.write_text(json.dumps(payload), encoding="utf-8")

            with patched_site(payload):
                report = run_preflight(load_config(config_path))
            self.assertIn("no_tool_capability", report["blockers"])

    def test_wrong_database_environment_value_is_never_logged(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory), mode="golden_slice")
            secret_wrong_value = "wrong-db-with-secret-token"
            with patched_site(payload), patch.dict(
                os.environ,
                {"ARANGO_DB": secret_wrong_value},
                clear=True,
            ):
                report = run_preflight(load_config(config_path))
            self.assertIn("expected_database", report["blockers"])
            self.assertNotIn(secret_wrong_value, json.dumps(report))


if __name__ == "__main__":
    unittest.main()
