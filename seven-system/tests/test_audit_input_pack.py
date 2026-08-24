"""Mechanical audit input-pack verifier tests.

These tests cover only the handoff precheck.  They deliberately do not create
AuditAssignment, AuditRecord, HumanGate decisions, or any AUDITED_* state.
"""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import jsonschema


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.audit.audit_input_pack import (  # noqa: E402
    audit_input_pack_hash,
    audit_readiness_report_hash,
    build_audit_input_pack_from_refs,
    build_audit_readiness_report,
    load_and_validate_audit_input_pack,
)
from seven_system.hashing import canonical_json_bytes  # noqa: E402
from seven_system.operations.doc0_bootstrap_evidence import (  # noqa: E402
    build_doc0_bootstrap_completion_record,
)
from seven_system.operations.implementation_bundle_evidence import (  # noqa: E402
    build_side_effect_free_implementation_completion_bundle,
)


DAG_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
SCHEMA_PATH = SYSTEM_ROOT / "docs" / "implementation" / "audit-input-pack.v1.schema.json"
READINESS_SCHEMA_PATH = SYSTEM_ROOT / "docs" / "implementation" / "audit-readiness-report.v1.schema.json"
COMMIT = "a" * 40
TREE = "b" * 40
BASELINE = {"commit": "0" * 40, "tree": "1" * 40}


def _ref(name: str, fill: str = "1") -> dict[str, str]:
    return {"ref": name, "sha256": fill * 64}


def _write_json(path: Path, payload: dict) -> str:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _plan_hash(plan: dict) -> str:
    candidate = copy.deepcopy(plan)
    candidate["plan_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _make_plan(wp_id: str = "WP-GV0") -> dict:
    dag_sha = hashlib.sha256(DAG_PATH.read_bytes()).hexdigest()
    plan = {
        "schema_id": "seven/work-package-plan",
        "schema_version": 1,
        "wp_id": wp_id,
        "implementation_attempt_id": f"{wp_id.lower()}-attempt-001",
        "plan_timing": "PREREGISTERED",
        "execution_mode": "SIDE_EFFECT_FREE",
        "protocol_deviations": [],
        "baseline": dict(BASELINE),
        "canonical_dag": {"ref": str(DAG_PATH), "sha256": dag_sha},
        "development_dependency_bundles": [_ref("evidence/wp-doc0/bootstrap.json", "2")],
        "inherited_audit_debt": ["WP-DOC0 bootstrap evidence still requires independent audit"],
        "activation_dependencies": ["WP-DOC0"],
        "normative_index_ref_and_hash": _ref("normative-requirement-index.v1.json", "3"),
        "normative_review_record_ref_and_hash": _ref("normative-review.json", "4"),
        "requirement_ids": ["AUTH-001"],
        "normative_clause_ids": ["NORM-unit-001"],
        "normative_clause_scope": "unit-test fixture",
        "normative_spec_refs_and_hashes": [_ref("implementation/12-completion-evidence-bundle.md", "5")],
        "goals": ["build a side-effect-free bundle fixture"],
        "non_goals": ["do not run live systems"],
        "allowed_path_rules": ["stdout-only assembly"],
        "forbidden_boundaries": ["no DB/model/Solver side effects"],
        "input_object_types_and_hashes": [_ref("input.json", "6")],
        "output_object_types": ["ImplementationCompletionBundle"],
        "interfaces_and_schema_ids": ["seven/implementation-completion-bundle/v1"],
        "state_machines_and_registries": ["WorkPackageStateService"],
        "security_and_view_contracts": ["no live side effects"],
        "idempotency_fence_recovery_rules": ["deterministic bundle hash"],
        "test_plan_ids": ["test_audit_input_pack"],
        "external_execution_authorization_ref": None,
        "live_run_permit_ref": None,
        "authorization_consumption_reservation_ref": None,
        "side_effect_budget": {
            "db_connections": 0,
            "db_writes": 0,
            "redis_connections": 0,
            "remote_model_calls": 0,
            "target_solver_launches": 0,
            "d_volume_writes": 0,
        },
        "pass_criteria": ["bundle validates"],
        "stop_conditions": ["any side effect requested"],
        "explicit_nonclaims": ["not audited"],
        "plan_hash_algorithm": "sha256(canonical-json-with-plan_hash-null)",
        "plan_hash": None,
    }
    plan["plan_hash"] = _plan_hash(plan)
    return plan


def _bundle_input(wp_id: str = "WP-GV0") -> dict:
    test_ref = _ref("evidence/unit-tests.json", "7")
    return {
        "bundle_id": f"{wp_id.lower()}-bundle-001",
        "wp_id": wp_id,
        "implementation_attempt_id": f"{wp_id.lower()}-attempt-001",
        "implementation_subject": {"commit": COMMIT, "tree": TREE},
        "requirement_coverage": [
            {
                "requirement_id": "AUTH-001",
                "normative_clause_ids": ["NORM-unit-001"],
                "code_refs": ["src/seven_system/audit/audit_input_pack.py"],
                "schema_refs": ["audit-input-pack.v1.schema.json"],
                "test_receipts": [test_ref],
                "runtime_evidence_refs": [],
                "status": "COVERED",
            }
        ],
        "modified_files": ["src/seven_system/audit/audit_input_pack.py"],
        "schema_ids_and_hashes": [_ref("audit-input-pack.v1.schema.json", "8")],
        "code_entrypoints": ["seven_system.audit.audit_input_pack"],
        "state_transitions_implemented": ["none"],
        "test_receipts": [test_ref],
        "fault_injection_receipts": [],
        "capability_reports": [],
        "artifact_refs": [],
        "claims": ["Side-effect-free candidate bundle assembled."],
        "nonclaims": ["Not independently audited."],
        "known_limitations": ["Unit-test fixture only."],
        "protocol_deviations": [],
        "unresolved_findings": [],
        "inherited_audit_debt": [_ref("evidence/wp-doc0/bootstrap.json", "2")],
        "recovery_notes": ["Rebuild from frozen plan and receipts."],
        "audit_replay_commands": [[sys.executable, "-m", "unittest", "seven-system/tests/test_audit_input_pack.py"]],
        "created_at": "2026-08-14T20:45:00Z",
        "creator": "unit-test",
    }


def _doc0_receipts() -> tuple[dict, dict]:
    subject = {
        "commit": COMMIT,
        "tree": TREE,
        "working_tree_clean": True,
        "source_relation": "COMMITTED_TREE",
    }
    plan_ref = _ref("wp-doc0-plan.v1.json", "9")
    index_ref = _ref("normative-requirement-index.v1.json", "a")
    doc_contract = {
        "schema_id": "seven/docs/doc-contract-verification-receipt",
        "verdict": "PASS",
        "errors": [],
        "implementation_subject": subject,
        "work_package_plan_ref_and_hash": plan_ref,
        "normative_index_ref_and_hash": index_ref,
    }
    test_receipt = {
        "schema_id": "seven/docs/doc0-test-execution-receipt",
        "wp_id": "WP-DOC0",
        "aggregate_verdict": "PASS",
        "side_effect_counts": {
            "db_connections": 0,
            "db_writes": 0,
            "redis_connections": 0,
            "remote_model_calls": 0,
            "target_solver_launches": 0,
            "d_volume_writes": 0,
        },
        "implementation_subject": {
            "commit": COMMIT,
            "tree": TREE,
            "working_tree_clean_before_tests": True,
            "source_relation": "COMMITTED_TREE",
        },
        "work_package_plan_ref_and_hash": plan_ref,
        "normative_index_ref_and_hash": index_ref,
    }
    return doc_contract, test_receipt


def _make_audit_pack(doc0_ref: dict, gv0_ref: dict) -> dict:
    pack = {
        "schema_id": "seven/audit-input-pack",
        "schema_version": 1,
        "pack_id": "ga1-input-pack-unit-001",
        "purpose": "GA1_MECHANICAL_INPUT_CANDIDATE",
        "canonical_dag_ref_and_hash": {"ref": str(DAG_PATH), "sha256": hashlib.sha256(DAG_PATH.read_bytes()).hexdigest()},
        "target_work_package_ids": ["WP-DOC0", "WP-GV0"],
        "completion_objects": [
            {
                "wp_id": "WP-DOC0",
                "completion_contract": "DOC_BOOTSTRAP_RECORD",
                "object_ref_and_hash": doc0_ref,
                "implementation_subject": {"commit": COMMIT, "tree": TREE},
                "expected_state_after_consume": "READY_FOR_AUDIT",
            },
            {
                "wp_id": "WP-GV0",
                "completion_contract": "IMPLEMENTATION_BUNDLE",
                "object_ref_and_hash": gv0_ref,
                "implementation_subject": {"commit": COMMIT, "tree": TREE},
                "expected_state_after_consume": "READY_FOR_AUDIT",
            },
        ],
        "audit_assignment_status": "NOT_REQUESTED",
        "audit_record_status": "NOT_CREATED",
        "state_effect": "NONE",
        "claims": ["This pack mechanically references candidate completion objects for future GA1 review."],
        "nonclaims": [
            "This pack is not an AuditAssignment.",
            "This pack is not an AuditRecord.",
            "This pack does not change any work-package state.",
            "This pack does not claim AUDITED_PASS.",
        ],
        "created_at": "2026-08-14T21:05:00Z",
        "creator": "unit-test",
        "input_pack_hash_algorithm": "sha256(canonical-json-with-input_pack_hash-null)",
        "input_pack_hash": None,
    }
    pack["input_pack_hash"] = audit_input_pack_hash(pack)
    return pack


class TestAuditInputPack(unittest.TestCase):
    def _fixture(self, tmp: Path) -> tuple[Path, dict]:
        doc_contract, test_receipt = _doc0_receipts()
        doc0_record = build_doc0_bootstrap_completion_record(
            record_id="doc0-record-001",
            doc_contract_receipt=doc_contract,
            doc_contract_receipt_ref_and_hash=_ref("doc-contract.json", "b"),
            doc0_test_receipt=test_receipt,
            doc0_test_receipt_ref_and_hash=_ref("doc0-tests.json", "c"),
            created_at="2026-08-14T21:00:00Z",
            creator="unit-test",
        )
        plan_path = tmp / "gv0-plan.json"
        plan_sha = _write_json(plan_path, _make_plan())
        gv0_bundle = build_side_effect_free_implementation_completion_bundle(
            bundle_input=_bundle_input(),
            plan_path=plan_path,
            expected_plan_sha256=plan_sha,
            dag_path=DAG_PATH,
        )
        doc0_path = tmp / "doc0-record.json"
        gv0_path = tmp / "gv0-bundle.json"
        doc0_sha = _write_json(doc0_path, doc0_record)
        gv0_sha = _write_json(gv0_path, gv0_bundle)
        pack = _make_audit_pack(
            {"ref": doc0_path.name, "sha256": doc0_sha},
            {"ref": gv0_path.name, "sha256": gv0_sha},
        )
        pack_path = tmp / "audit-input-pack.json"
        _write_json(pack_path, pack)
        return pack_path, pack

    def test_valid_pack_is_schema_valid_and_mechanically_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            pack_path, pack = self._fixture(Path(tmpdir))
            schema = json.loads(SCHEMA_PATH.read_text())
            errors = list(jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(pack))
            self.assertEqual(errors, [])

            result = load_and_validate_audit_input_pack(
                pack_path=pack_path,
                schema_path=SCHEMA_PATH,
                dag_path=DAG_PATH,
            )
            self.assertTrue(result.passed, result.errors)
            self.assertEqual(result.independent_audit_verdict, "NOT_STARTED")
            self.assertEqual(result.state_effect, "NONE")
            self.assertEqual(result.checked_work_package_ids, ["WP-DOC0", "WP-GV0"])

    def test_rejects_ga1_as_completion_object(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, pack = self._fixture(tmp)
            pack["target_work_package_ids"].append("WP-GA1")
            pack["completion_objects"].append(
                {
                    "wp_id": "WP-GA1",
                    "completion_contract": "IMPLEMENTATION_BUNDLE",
                    "object_ref_and_hash": pack["completion_objects"][1]["object_ref_and_hash"],
                    "implementation_subject": {"commit": COMMIT, "tree": TREE},
                    "expected_state_after_consume": "READY_FOR_AUDIT",
                }
            )
            pack["input_pack_hash"] = audit_input_pack_hash(pack)
            _write_json(pack_path, pack)
            result = load_and_validate_audit_input_pack(pack_path=pack_path, schema_path=SCHEMA_PATH, dag_path=DAG_PATH)
            self.assertFalse(result.passed)
            self.assertTrue(any("WP-GA1" in item for item in result.errors))

    def test_rejects_object_hash_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, pack = self._fixture(tmp)
            gv0_path = tmp / "gv0-bundle.json"
            bundle = json.loads(gv0_path.read_text())
            bundle["claims"] = ["Changed after pack sealing."]
            _write_json(gv0_path, bundle)
            result = load_and_validate_audit_input_pack(pack_path=pack_path, schema_path=SCHEMA_PATH, dag_path=DAG_PATH)
            self.assertFalse(result.passed)
            self.assertTrue(any("hash mismatch" in item for item in result.errors))

    def test_rejects_audit_verdict_overclaim_in_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, pack = self._fixture(tmp)
            gv0_path = tmp / "gv0-bundle.json"
            bundle = json.loads(gv0_path.read_text())
            bundle["claims"] = ["AUDITED_PASS already achieved"]
            bundle["bundle_hash"] = None
            bundle["bundle_hash"] = hashlib.sha256(canonical_json_bytes(bundle)).hexdigest()
            new_sha = _write_json(gv0_path, bundle)
            pack["completion_objects"][1]["object_ref_and_hash"]["sha256"] = new_sha
            pack["input_pack_hash"] = audit_input_pack_hash(pack)
            _write_json(pack_path, pack)
            result = load_and_validate_audit_input_pack(pack_path=pack_path, schema_path=SCHEMA_PATH, dag_path=DAG_PATH)
            self.assertFalse(result.passed)
            self.assertTrue(any("audit verdict" in item for item in result.errors))

    def test_cli_returns_nonzero_for_negative_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, pack = self._fixture(tmp)
            pack["input_pack_hash"] = "0" * 64
            _write_json(pack_path, pack)
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "validate-audit-input-pack",
                    "--pack",
                    str(pack_path),
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 3)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["verdict"], "FAIL")
            self.assertTrue(any("input_pack_hash mismatch" in item for item in payload["errors"]))

    def test_builder_derives_pack_from_completion_refs(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, pack = self._fixture(tmp)
            pack_input = {
                "pack_id": "ga1-input-pack-built-001",
                "completion_object_refs": [
                    pack["completion_objects"][0]["object_ref_and_hash"],
                    pack["completion_objects"][1]["object_ref_and_hash"],
                ],
                "created_at": "2026-08-14T21:15:00Z",
                "creator": "unit-test",
            }
            built = build_audit_input_pack_from_refs(
                pack_input=pack_input,
                pack_base_dir=tmp,
                schema_path=SCHEMA_PATH,
                dag_path=DAG_PATH,
            )
            self.assertEqual(built["target_work_package_ids"], ["WP-DOC0", "WP-GV0"])
            self.assertEqual(built["audit_assignment_status"], "NOT_REQUESTED")
            self.assertEqual(built["audit_record_status"], "NOT_CREATED")
            self.assertEqual(built["state_effect"], "NONE")
            self.assertNotEqual(built["input_pack_hash"], pack["input_pack_hash"])
            built_path = tmp / "built-audit-input-pack.json"
            _write_json(built_path, built)
            result = load_and_validate_audit_input_pack(pack_path=built_path, schema_path=SCHEMA_PATH, dag_path=DAG_PATH)
            self.assertTrue(result.passed, result.errors)

    def test_builder_rejects_completion_ref_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            _, pack = self._fixture(tmp)
            ref = dict(pack["completion_objects"][0]["object_ref_and_hash"])
            ref["sha256"] = "0" * 64
            with self.assertRaisesRegex(Exception, "hash mismatch"):
                build_audit_input_pack_from_refs(
                    pack_input={
                        "pack_id": "ga1-input-pack-built-002",
                        "completion_object_refs": [ref],
                        "created_at": "2026-08-14T21:16:00Z",
                        "creator": "unit-test",
                    },
                    pack_base_dir=tmp,
                    schema_path=SCHEMA_PATH,
                    dag_path=DAG_PATH,
                )

    def test_cli_builds_pack_to_stdout(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            _, pack = self._fixture(tmp)
            input_path = tmp / "pack-input.json"
            _write_json(
                input_path,
                {
                    "pack_id": "ga1-input-pack-cli-001",
                    "completion_object_refs": [
                        pack["completion_objects"][0]["object_ref_and_hash"],
                        pack["completion_objects"][1]["object_ref_and_hash"],
                    ],
                    "created_at": "2026-08-14T21:17:00Z",
                    "creator": "unit-test",
                },
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "build-audit-input-pack",
                    "--pack-input",
                    str(input_path),
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["schema_id"], "seven/audit-input-pack")
            self.assertEqual(payload["target_work_package_ids"], ["WP-DOC0", "WP-GV0"])

    def test_readiness_report_complete_for_pack_targets_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, _ = self._fixture(tmp)
            report = build_audit_readiness_report(
                report_id="ga1-readiness-unit-001",
                pack_path=pack_path,
                input_pack_schema_path=SCHEMA_PATH,
                dag_path=DAG_PATH,
                expected_scope="PACK_TARGETS_ONLY",
                created_at="2026-08-14T21:20:00Z",
                creator="unit-test",
            )
            schema = json.loads(READINESS_SCHEMA_PATH.read_text())
            errors = list(jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(report))
            self.assertEqual(errors, [])
            self.assertEqual(report["mechanical_handoff_status"], "COMPLETE")
            self.assertEqual(report["independent_audit_verdict"], "NOT_STARTED")
            self.assertEqual(report["state_effect"], "NONE")
            expected = copy.deepcopy(report)
            expected["report_hash"] = None
            self.assertEqual(report["report_hash"], hashlib.sha256(canonical_json_bytes(expected)).hexdigest())
            self.assertEqual(report["report_hash"], audit_readiness_report_hash(report))

    def test_readiness_report_incomplete_for_ga1_development_closure(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, _ = self._fixture(tmp)
            report = build_audit_readiness_report(
                report_id="ga1-readiness-unit-002",
                pack_path=pack_path,
                input_pack_schema_path=SCHEMA_PATH,
                dag_path=DAG_PATH,
                expected_scope="GA1_DEVELOPMENT_CLOSURE",
                created_at="2026-08-14T21:21:00Z",
                creator="unit-test",
            )
            self.assertEqual(report["mechanical_handoff_status"], "INCOMPLETE")
            self.assertIn("WP-VR1", report["missing_work_package_ids"])
            self.assertEqual(report["unexpected_work_package_ids"], [])

    def test_cli_readiness_report_returns_nonzero_when_incomplete(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            pack_path, _ = self._fixture(tmp)
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "audit-input-pack-report",
                    "--pack",
                    str(pack_path),
                    "--report-id",
                    "ga1-readiness-cli-001",
                    "--expected-scope",
                    "GA1_DEVELOPMENT_CLOSURE",
                    "--created-at",
                    "2026-08-14T21:22:00Z",
                    "--creator",
                    "unit-test",
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 3)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["mechanical_handoff_status"], "INCOMPLETE")
            self.assertIn("WP-VR1", payload["missing_work_package_ids"])


if __name__ == "__main__":
    unittest.main()
