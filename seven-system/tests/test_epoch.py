from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from seven_system.config import load_config  # noqa: E402
from seven_system.epoch import (  # noqa: E402
    EpochError,
    INITIAL_SEALED_FILES,
    P1_SEALED_FILES,
    _integrity_index,
    dry_run_epoch,
    init_epoch,
    validate_epoch,
)
from support import build_site, patched_site  # noqa: E402


class EpochTests(unittest.TestCase):
    def test_new_epoch_is_validated_before_success_is_returned(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            forced_failure = {
                "verdict": "FAIL",
                "current_runtime_compatibility": "PASS",
                "errors": ["injected final validation failure"],
                "compatibility_errors": [],
            }
            with patched_site(payload), patch(
                "seven_system.epoch.validate_epoch", return_value=forced_failure
            ), self.assertRaises(EpochError):
                init_epoch(config, "final-check-001")

    def test_init_and_dry_run_are_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                first = init_epoch(config, "dryrun-001")
                second = init_epoch(config, "dryrun-001")
            self.assertEqual(first["status"], "INITIALIZED")
            self.assertEqual(second["status"], "ALREADY_INITIALIZED")
            self.assertEqual(first["manifest_hash"], second["manifest_hash"])

            with patched_site(payload):
                report = dry_run_epoch(config, "dryrun-001")
            self.assertEqual(report["verdict"], "PASS")
            self.assertEqual(report["side_effects"]["solver_launches"], 0)
            self.assertEqual(report["side_effects"]["database_connections"], 0)

            epoch_root = Path(payload["storage"]["data_root"]) / "epochs" / "dryrun-001"
            self.assertEqual(validate_epoch(epoch_root)["verdict"], "PASS")
            with patched_site(payload):
                self.assertEqual(
                    dry_run_epoch(config, "dryrun-001")["verdict"], "PASS"
                )

    def test_manifest_tampering_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                init_epoch(config, "tamper-001")
            epoch_root = Path(payload["storage"]["data_root"]) / "epochs" / "tamper-001"
            manifest_path = epoch_root / "runtime-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["mode"] = "continuous"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            result = validate_epoch(epoch_root)
            self.assertEqual(result["verdict"], "FAIL")
            self.assertIn("runtime-manifest hash mismatch", result["errors"])

    def test_incomplete_existing_epoch_is_not_reported_as_initialized(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                init_epoch(config, "partial-001")
            epoch_root = Path(payload["storage"]["data_root"]) / "epochs" / "partial-001"
            (epoch_root / "phase-plan.json").unlink()

            with patched_site(payload), self.assertRaises(EpochError):
                init_epoch(config, "partial-001")

    def test_tampered_dry_run_report_is_rejected_on_reentry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                dry_run_epoch(config, "report-tamper-001")
            epoch_root = (
                Path(payload["storage"]["data_root"])
                / "epochs"
                / "report-tamper-001"
            )
            report_path = epoch_root / "dry-run-report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["side_effects"]["solver_launches"] = 1
            report_path.write_text(json.dumps(report), encoding="utf-8")

            with patched_site(payload), self.assertRaises(EpochError):
                dry_run_epoch(config, "report-tamper-001")

    def test_non_object_manifest_and_tampered_verdict_fail_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                init_epoch(config, "shape-001")
            epoch_root = Path(payload["storage"]["data_root"]) / "epochs" / "shape-001"

            manifest_path = epoch_root / "runtime-manifest.json"
            original_manifest = manifest_path.read_text(encoding="utf-8")
            manifest_path.write_text("[]\n", encoding="utf-8")
            self.assertEqual(validate_epoch(epoch_root)["verdict"], "FAIL")
            manifest_path.write_text(original_manifest, encoding="utf-8")

            verdict_path = epoch_root / "verdict.json"
            verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
            verdict["overall_verdict"] = "FULL_PASS"
            verdict_path.write_text(json.dumps(verdict), encoding="utf-8")
            result = validate_epoch(epoch_root)
            self.assertEqual(result["verdict"], "FAIL")
            self.assertTrue(
                any("verdict.json" in error for error in result["errors"])
            )

    def test_epoch_symlink_escape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path, payload = build_site(root)
            config = load_config(config_path)
            data_root = Path(payload["storage"]["data_root"])
            epochs_root = data_root / "epochs"
            epochs_root.mkdir()
            outside = root / "outside"
            outside.mkdir()
            (epochs_root / "escape-001").symlink_to(outside, target_is_directory=True)

            with patched_site(payload), self.assertRaises(EpochError):
                init_epoch(config, "escape-001")
            self.assertFalse((outside / "runtime-manifest.json").exists())

    def test_existing_epoch_rechecks_preflight(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                init_epoch(config, "recheck-001")
            (Path(payload["storage"]["volume_root"]) / "README.md").unlink()

            with patched_site(payload), self.assertRaises(EpochError):
                init_epoch(config, "recheck-001")

    def test_source_tree_drift_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                init_epoch(config, "source-drift-001")
            asset = (
                Path(payload["repository_root"]) / "assets" / "solver" / "AGENTS.md"
            )
            asset.write_text(
                asset.read_text(encoding="utf-8") + "drift\n", encoding="utf-8"
            )
            epoch_root = (
                Path(payload["storage"]["data_root"])
                / "epochs"
                / "source-drift-001"
            )
            result = validate_epoch(epoch_root)
            self.assertEqual(result["artifact_integrity"], "PASS")
            self.assertEqual(result["current_runtime_compatibility"], "BLOCKED")
            self.assertIn(
                "evidence factory source tree drift",
                result["compatibility_errors"],
            )
            from seven_system.cli import main

            for command in ("validate-epoch", "status"):
                with self.subTest(command=command), redirect_stdout(io.StringIO()):
                    self.assertEqual(
                        main([command, "--epoch-root", str(epoch_root)]), 3
                    )

    def test_recomputed_index_cannot_authorize_scientific_overclaim(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                dry_run_epoch(config, "overclaim-001")
            epoch_root = (
                Path(payload["storage"]["data_root"])
                / "epochs"
                / "overclaim-001"
            )
            report_path = epoch_root / "dry-run-report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["scientific_claim"] = "TELL_PROVEN"
            report_path.write_text(json.dumps(report), encoding="utf-8")

            verdict_path = epoch_root / "p1-verdict.json"
            verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
            verdict["factory_pipeline"] = "PASS"
            verdict["scientific_analyzability"] = "PASS"
            verdict["tell_evidence"] = "SUPPORTS"
            verdict["overall_verdict"] = "FULL_SCIENTIFIC_PASS"
            verdict_path.write_text(json.dumps(verdict), encoding="utf-8")

            manifest = json.loads(
                (epoch_root / "runtime-manifest.json").read_text(encoding="utf-8")
            )
            initial_index = json.loads(
                (epoch_root / "integrity-index.json").read_text(encoding="utf-8")
            )
            rebuilt = _integrity_index(
                epoch_root,
                epoch_id="overclaim-001",
                manifest_hash=manifest["manifest_hash"],
                paths=P1_SEALED_FILES,
                index_kind="P1_DRY_RUN",
                previous_index_hash=initial_index["index_hash"],
            )
            (epoch_root / "p1-integrity-index.json").write_text(
                json.dumps(rebuilt), encoding="utf-8"
            )

            result = validate_epoch(epoch_root)
            self.assertEqual(result["verdict"], "FAIL")
            self.assertTrue(
                any("scientific" in error.lower() for error in result["errors"])
            )

    def test_external_receipt_rejects_recomputed_initial_index(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            with patched_site(payload):
                init_epoch(config, "receipt-001")
            epoch_root = (
                Path(payload["storage"]["data_root"])
                / "epochs"
                / "receipt-001"
            )
            summary_path = epoch_root / "summary.md"
            summary_path.write_text("rewritten\n", encoding="utf-8")
            manifest = json.loads(
                (epoch_root / "runtime-manifest.json").read_text(encoding="utf-8")
            )
            rebuilt = _integrity_index(
                epoch_root,
                epoch_id="receipt-001",
                manifest_hash=manifest["manifest_hash"],
                paths=INITIAL_SEALED_FILES,
                index_kind="INITIAL_SCAFFOLD",
            )
            (epoch_root / "integrity-index.json").write_text(
                json.dumps(rebuilt), encoding="utf-8"
            )
            result = validate_epoch(epoch_root)
            self.assertEqual(result["verdict"], "FAIL")
            self.assertTrue(
                any("receipt index_hash" in error for error in result["errors"])
            )

    def test_consistent_failed_gate_is_valid_replayable_artifact(self) -> None:
        from seven_system import epoch as epoch_module

        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            config = load_config(config_path)
            real_commit = epoch_module.commit_json_once

            def simulate_failed_conflict_probe(path, body, **kwargs):
                if path.name == "idempotency-probe.json" and body.get("value") == "conflict":
                    return "ALREADY_COMMITTED"
                return real_commit(path, body, **kwargs)

            with patched_site(payload), patch(
                "seven_system.epoch.commit_json_once",
                side_effect=simulate_failed_conflict_probe,
            ):
                report = dry_run_epoch(config, "valid-fail-001")
            self.assertEqual(report["verdict"], "FAIL")
            epoch_root = (
                Path(payload["storage"]["data_root"])
                / "epochs"
                / "valid-fail-001"
            )
            validation = validate_epoch(epoch_root)
            self.assertEqual(validation["artifact_integrity"], "PASS")
            self.assertEqual(
                json.loads(
                    (epoch_root / "gate-decisions" / "P1.json").read_text(
                        encoding="utf-8"
                    )
                )["verdict"],
                "FAIL",
            )


if __name__ == "__main__":
    unittest.main()
