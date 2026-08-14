from __future__ import annotations

import copy
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from seven_system.database.capability import (  # noqa: E402
    STRICT_DATABASE_CONTRACT_CHECK_IDS,
)
from seven_system.database.contract_report import (  # noqa: E402
    build_strict_db_contract_report,
    strict_db_implementation_tree_files,
    strict_db_implementation_tree_hash,
    verify_strict_db_contract_report,
)
from seven_system.config import ConfigError  # noqa: E402
from seven_system.cli import _wp1_db_contract_report  # noqa: E402
from seven_system.storage import ContentConflictError  # noqa: E402
from support import build_site, patched_site  # noqa: E402


def _report() -> dict[str, object]:
    return build_strict_db_contract_report(system_root=SYSTEM_ROOT)


class StrictDbContractReportTests(unittest.TestCase):
    def test_current_tree_builds_and_verifies_a_contract_only_pass(self) -> None:
        report = _report()
        self.assertEqual(
            verify_strict_db_contract_report(
                report,
                system_root=SYSTEM_ROOT,
            ),
            (),
        )
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["scope"], "OFFLINE_STATIC_AND_FAKE_ADAPTER")
        self.assertNotIn("DatabaseSiteCapabilityReport", repr(report))

    def test_implementation_hash_binds_sources_tests_schema_and_validator(self) -> None:
        paths = {
            path.relative_to(SYSTEM_ROOT).as_posix()
            for path in strict_db_implementation_tree_files(SYSTEM_ROOT)
        }
        for required in (
            "src/seven_system/database/contract_report.py",
            "tests/test_database_contract_report.py",
            "tests/strict_db_contract_runner.py",
            "schemas/wp1-strict-db-contract-report.schema.json",
            "schemas/runtime-config.schema.json",
            "scripts/seven.py",
            "src/seven_system/__main__.py",
            "src/seven_system/schema_validation.py",
        ):
            self.assertIn(required, paths)
        self.assertIsNotNone(
            re.fullmatch(
                r"[0-9a-f]{64}",
                strict_db_implementation_tree_hash(SYSTEM_ROOT),
            )
        )

    def test_caller_cannot_inject_pass_evidence_or_suite_hash(self) -> None:
        with self.assertRaises(TypeError):
            build_strict_db_contract_report(
                check_evidence={  # type: ignore[call-arg]
                    check_id: ("caller says pass",)
                    for check_id in STRICT_DATABASE_CONTRACT_CHECK_IDS
                },
                test_suite_hash="0" * 64,
                system_root=SYSTEM_ROOT,
            )

    def test_duplicate_checks_and_fabricated_receipt_are_rejected(self) -> None:
        report = _report()
        checks = report["checks"]
        assert isinstance(checks, list)
        checks.append(copy.deepcopy(checks[0]))
        evidence = checks[0]["evidence"]
        assert isinstance(evidence, list)
        evidence[-1] = "test_execution_receipt_sha256=" + "0" * 64
        errors = verify_strict_db_contract_report(
            report,
            system_root=SYSTEM_ROOT,
        )
        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("controlled test receipt" in error for error in errors))

    def test_claim_side_effect_and_subject_tampering_are_rejected(self) -> None:
        report = _report()
        claims = report["claims"]
        side_effects = report["side_effects"]
        assert isinstance(claims, dict)
        assert isinstance(side_effects, dict)
        claims["reads_have_no_schema_side_effects"] = False
        side_effects["database_connections"] = 1
        report["subject_hash"] = "0" * 64
        errors = verify_strict_db_contract_report(
            report,
            system_root=SYSTEM_ROOT,
        )
        self.assertTrue(any("claims" in error for error in errors))
        self.assertTrue(any("side effects" in error for error in errors))
        self.assertTrue(any("subject hash" in error for error in errors))

    def test_nonclaims_cannot_be_removed_to_imply_site_capability(self) -> None:
        report = _report()
        nonclaims = report["explicit_nonclaims"]
        assert isinstance(nonclaims, list)
        nonclaims.pop()
        errors = verify_strict_db_contract_report(
            report,
            system_root=SYSTEM_ROOT,
        )
        self.assertTrue(any("nonclaims" in error for error in errors))

    def test_schema_invalid_json_is_rejected_without_verifier_exception(self) -> None:
        malformed_check = _report()
        checks = malformed_check["checks"]
        assert isinstance(checks, list)
        assert isinstance(checks[0], dict)
        checks[0]["check_id"] = []
        self.assertNotEqual(
            verify_strict_db_contract_report(
                malformed_check,
                system_root=SYSTEM_ROOT,
            ),
            (),
        )

        malformed_nonclaim = _report()
        nonclaims = malformed_nonclaim["explicit_nonclaims"]
        assert isinstance(nonclaims, list)
        nonclaims[0] = {}
        self.assertNotEqual(
            verify_strict_db_contract_report(
                malformed_nonclaim,
                system_root=SYSTEM_ROOT,
            ),
            (),
        )

    def test_controlled_runner_ignores_caller_pythonpath_sitecustomize(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            attack_root = Path(directory)
            marker = attack_root / "sitecustomize-loaded"
            (attack_root / "sitecustomize.py").write_text(
                "from pathlib import Path\n"
                f"Path({str(marker)!r}).write_text('loaded', encoding='utf-8')\n",
                encoding="utf-8",
            )
            with patch.dict(os.environ, {"PYTHONPATH": str(attack_root)}):
                report = _report()
            self.assertFalse(marker.exists())
            self.assertEqual(
                verify_strict_db_contract_report(report, system_root=SYSTEM_ROOT),
                (),
            )

    def test_caller_cannot_inject_generated_at(self) -> None:
        with self.assertRaises(TypeError):
            build_strict_db_contract_report(
                generated_at="fake-time",
                system_root=SYSTEM_ROOT,
            )

    def test_cli_commits_once_under_the_approved_data_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            config_path, payload = build_site(Path(directory))
            with patched_site(payload):
                first = _wp1_db_contract_report(config_path, "contract-001")
                second = _wp1_db_contract_report(config_path, "contract-001")
            self.assertEqual(first["status"], "COMMITTED")
            self.assertEqual(second["status"], "ALREADY_COMMITTED")
            report_path = Path(first["path"])
            self.assertTrue(report_path.is_file())
            self.assertTrue(
                report_path.resolve().is_relative_to(
                    Path(payload["storage"]["data_root"]).resolve()
                )
            )

    def test_cli_rejects_noncanonical_database_config_without_writing(self) -> None:
        for key, value in (
            ("expected_database", "wrong_database"),
            ("adapter_contract", "caller-contract/v999"),
        ):
            with self.subTest(key=key), tempfile.TemporaryDirectory() as directory:
                config_path, payload = build_site(Path(directory))
                payload["database"][key] = value
                config_path.write_text(json.dumps(payload), encoding="utf-8")
                with patched_site(payload), self.assertRaises(ConfigError):
                    _wp1_db_contract_report(config_path, "contract-001")
                self.assertFalse(
                    (
                        Path(payload["storage"]["data_root"])
                        / "capabilities"
                    ).exists()
                )

    def test_cli_rejects_existing_report_behind_ancestor_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path, payload = build_site(root)
            external = root / "outside-approved-volume"
            report_root = external / "strict-db-contract"
            report_root.mkdir(parents=True)
            (report_root / "contract-001.json").write_text(
                json.dumps(_report()),
                encoding="utf-8",
            )
            data_root = Path(payload["storage"]["data_root"])
            (data_root / "capabilities").symlink_to(
                external,
                target_is_directory=True,
            )
            with patched_site(payload), self.assertRaises(ContentConflictError):
                _wp1_db_contract_report(config_path, "contract-001")


if __name__ == "__main__":
    unittest.main()
