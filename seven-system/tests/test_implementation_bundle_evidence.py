"""Side-effect-free ImplementationCompletionBundle assembler tests."""

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
sys.path.insert(0, str(Path(__file__).resolve().parent))

from seven_system.hashing import canonical_json_bytes
from seven_system.operations.implementation_bundle_evidence import (
    ImplementationBundleEvidenceError,
    ZERO_IMPLEMENTATION_BUNDLE_SIDE_EFFECT_COUNTS,
    build_side_effect_free_implementation_completion_bundle,
)
from seven_system.operations.work_package_plan_builder import build_side_effect_free_work_package_plan
from seven_system.operations.work_package_state import WorkPackageStateService
from support import write_signed_normative_review_fixture  # noqa: E402


DAG_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
INDEX_PATH = SYSTEM_ROOT / "docs" / "implementation" / "normative-requirement-index.v1.json"
SCHEMA_PATH = SYSTEM_ROOT / "docs" / "implementation" / "implementation-completion-bundle.v1.schema.json"
COMMIT = "a" * 40
TREE = "b" * 40
BASELINE = {"commit": "0" * 40, "tree": "1" * 40}


def _ref(name: str, fill: str = "1") -> dict[str, str]:
    return {"ref": name, "sha256": fill * 64}


def _plan_hash(plan: dict) -> str:
    candidate = copy.deepcopy(plan)
    candidate["plan_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _write_json(path: Path, payload: dict) -> str:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _make_plan(wp_id: str = "WP-GV0", execution_mode: str = "SIDE_EFFECT_FREE") -> dict:
    dag_sha = hashlib.sha256(DAG_PATH.read_bytes()).hexdigest()
    plan = {
        "schema_id": "seven/work-package-plan",
        "schema_version": 1,
        "wp_id": wp_id,
        "implementation_attempt_id": f"{wp_id.lower()}-attempt-001",
        "plan_timing": "PREREGISTERED",
        "execution_mode": execution_mode,
        "protocol_deviations": [],
        "baseline": dict(BASELINE),
        "canonical_dag": {"ref": str(DAG_PATH), "sha256": dag_sha},
        "development_dependency_bundles": [_ref("evidence/wp-doc0/bootstrap.json", "2")],
        "inherited_audit_debt": ["WP-DOC0 bootstrap evidence still requires independent audit"],
        "activation_dependencies": ["WP-DOC0"],
        "normative_index_ref_and_hash": _ref("normative-requirement-index.v1.json", "3"),
        "normative_review_record_ref_and_hash": _ref("normative-review.json", "4"),
        "requirement_ids": ["AUTH-001", "DATA-005"],
        "normative_clause_ids": ["NORM-unit-001", "NORM-unit-002"],
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
        "test_plan_ids": ["test_implementation_bundle_evidence"],
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
                "code_refs": ["src/seven_system/operations/implementation_bundle_evidence.py"],
                "schema_refs": ["implementation-completion-bundle.v1.schema.json"],
                "test_receipts": [test_ref],
                "runtime_evidence_refs": [],
                "status": "COVERED",
            },
            {
                "requirement_id": "DATA-005",
                "normative_clause_ids": ["NORM-unit-002"],
                "code_refs": ["src/seven_system/operations/implementation_bundle_evidence.py"],
                "schema_refs": ["implementation-completion-bundle.v1.schema.json"],
                "test_receipts": [test_ref],
                "runtime_evidence_refs": [],
                "status": "COVERED",
            },
        ],
        "modified_files": ["src/seven_system/operations/implementation_bundle_evidence.py"],
        "schema_ids_and_hashes": [_ref("implementation-completion-bundle.v1.schema.json", "8")],
        "code_entrypoints": ["seven_system.operations.implementation_bundle_evidence"],
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
        "audit_replay_commands": [[sys.executable, "-m", "unittest", "seven-system/tests/test_implementation_bundle_evidence.py"]],
        "created_at": "2026-08-14T20:45:00Z",
        "creator": "unit-test",
    }


def _generated_plan_input(wp_id: str = "WP-DB1L") -> dict:
    return {
        "wp_id": wp_id,
        "implementation_attempt_id": f"{wp_id.lower()}-generated-plan-attempt-001",
        "baseline": dict(BASELINE),
        "normative_review_record_ref_and_hash": _ref("reviews/normative-review.json", "a"),
        "development_dependency_bundles": [_ref("evidence/wp-gv0/bundle.json", "b")],
        "inherited_audit_debt": ["upstream READY_FOR_AUDIT is not AUDITED_PASS"],
        "goals": ["exercise WorkPackagePlan to ImplementationCompletionBundle composition"],
        "non_goals": ["do not authorize live side effects"],
        "allowed_path_rules": ["stdout-only composition in test fixture"],
        "forbidden_boundaries": ["no DB writes", "no model calls", "no Solver launch"],
        "input_object_types_and_hashes": [_ref("inputs/generated-plan-input.json", "c")],
        "output_object_types": ["WorkPackagePlan", "ImplementationCompletionBundle"],
        "interfaces_and_schema_ids": [
            "seven/work-package-plan/v1",
            "seven/implementation-completion-bundle/v1",
        ],
        "state_machines_and_registries": ["WorkPackageStateService"],
        "security_and_view_contracts": ["SIDE_EFFECT_FREE only"],
        "idempotency_fence_recovery_rules": ["rebuild from the same frozen plan and bundle input"],
        "test_plan_ids": ["test_plan_builder_output_can_feed_bundle_builder"],
        "pass_criteria": ["generated bundle validates"],
        "stop_conditions": ["any requested external side effect"],
        "explicit_nonclaims": ["not an audited completion"],
    }


def _coverage_for_generated_plan(plan: dict) -> list[dict]:
    index = json.loads(INDEX_PATH.read_text())
    plan_clause_ids = set(plan["normative_clause_ids"])
    clauses_by_requirement: dict[str, set[str]] = {requirement_id: set() for requirement_id in plan["requirement_ids"]}
    for clause in index["clauses"]:
        clause_id = clause.get("clause_id")
        if clause_id not in plan_clause_ids:
            continue
        for requirement_id in clause.get("requirement_ids", []):
            if requirement_id in clauses_by_requirement:
                clauses_by_requirement[requirement_id].add(clause_id)

    test_ref = _ref("evidence/generated-plan-bundle-test.json", "d")
    coverage = []
    for requirement_id in plan["requirement_ids"]:
        coverage.append(
            {
                "requirement_id": requirement_id,
                "normative_clause_ids": sorted(clauses_by_requirement[requirement_id]),
                "code_refs": ["src/seven_system/operations/implementation_bundle_evidence.py"],
                "schema_refs": ["implementation-completion-bundle.v1.schema.json"],
                "test_receipts": [test_ref],
                "runtime_evidence_refs": [],
                "status": "COVERED",
            }
        )
    return coverage


def _bundle_input_for_generated_plan(plan: dict) -> dict:
    payload = _bundle_input(plan["wp_id"])
    payload["bundle_id"] = f"{plan['wp_id'].lower()}-generated-bundle-001"
    payload["implementation_attempt_id"] = plan["implementation_attempt_id"]
    payload["requirement_coverage"] = _coverage_for_generated_plan(plan)
    payload["claims"] = ["A bundle can be assembled from the generated WorkPackagePlan."]
    payload["nonclaims"] = ["This is a side-effect-free composition test, not independent audit."]
    return payload


def _build_with_temp_files(plan: dict | None = None, bundle_input: dict | None = None) -> dict:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        plan_path = tmp / "plan.json"
        plan_sha = _write_json(plan_path, plan or _make_plan())
        return build_side_effect_free_implementation_completion_bundle(
            bundle_input=bundle_input or _bundle_input(),
            plan_path=plan_path,
            expected_plan_sha256=plan_sha,
            dag_path=DAG_PATH,
        )


def _generated_plan_from_builder() -> dict:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        record_path = tmp / "normative-review.json"
        record_sha, public_key_bytes, _ = write_signed_normative_review_fixture(
            record_path,
            index_path=INDEX_PATH,
        )
        plan_input = _generated_plan_input()
        plan_input["normative_review_record_ref_and_hash"] = {"ref": str(record_path), "sha256": record_sha}
        return build_side_effect_free_work_package_plan(
            plan_input=plan_input,
            dag_path=DAG_PATH,
            normative_index_path=INDEX_PATH,
            normative_review_record_path=record_path,
            normative_review_public_key_bytes=public_key_bytes,
        )


class TestImplementationBundleEvidenceAssembler(unittest.TestCase):
    def test_builds_schema_valid_bundle(self) -> None:
        bundle = _build_with_temp_files()
        schema = json.loads(SCHEMA_PATH.read_text())
        errors = list(jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(bundle))
        self.assertEqual(errors, [])
        self.assertEqual(bundle["external_side_effect_counts"], ZERO_IMPLEMENTATION_BUNDLE_SIDE_EFFECT_COUNTS)
        self.assertEqual(bundle["status"], "READY_FOR_AUDIT")

        expected = copy.deepcopy(bundle)
        expected["bundle_hash"] = None
        self.assertEqual(bundle["bundle_hash"], hashlib.sha256(canonical_json_bytes(expected)).hexdigest())

    def test_rejects_doc0_and_ga1(self) -> None:
        with self.assertRaisesRegex(ImplementationBundleEvidenceError, "WP-DOC0"):
            _build_with_temp_files(plan=_make_plan("WP-DOC0"), bundle_input=_bundle_input("WP-DOC0"))
        with self.assertRaisesRegex(ImplementationBundleEvidenceError, "WP-GA1"):
            _build_with_temp_files(plan=_make_plan("WP-GA1"), bundle_input=_bundle_input("WP-GA1"))

    def test_rejects_missing_requirement_coverage(self) -> None:
        payload = _bundle_input()
        payload["requirement_coverage"] = payload["requirement_coverage"][:1]
        with self.assertRaisesRegex(ImplementationBundleEvidenceError, "missing requirement coverage"):
            _build_with_temp_files(bundle_input=payload)

    def test_rejects_clause_outside_plan(self) -> None:
        payload = _bundle_input()
        payload["requirement_coverage"][0]["normative_clause_ids"] = ["NORM-outside"]
        with self.assertRaisesRegex(ImplementationBundleEvidenceError, "outside the plan"):
            _build_with_temp_files(bundle_input=payload)

    def test_rejects_live_plan(self) -> None:
        plan = _make_plan(execution_mode="AUTHORIZED_LIVE_CANARY")
        plan["external_execution_authorization_ref"] = _ref("eea.json", "a")
        plan["live_run_permit_ref"] = _ref("permit.json", "b")
        plan["authorization_consumption_reservation_ref"] = _ref("reservation.json", "c")
        plan["side_effect_budget"]["remote_model_calls"] = 1
        plan["plan_hash"] = _plan_hash(plan)
        with self.assertRaisesRegex(ImplementationBundleEvidenceError, "SIDE_EFFECT_FREE"):
            _build_with_temp_files(plan=plan)

    def test_rejects_attempt_id_mismatch_between_plan_and_bundle(self) -> None:
        payload = _bundle_input()
        payload["implementation_attempt_id"] = "different-attempt"
        with self.assertRaisesRegex(ImplementationBundleEvidenceError, "implementation_attempt_id"):
            _build_with_temp_files(bundle_input=payload)

    def test_plan_builder_output_can_feed_bundle_builder(self) -> None:
        plan = _generated_plan_from_builder()
        bundle = _build_with_temp_files(
            plan=plan,
            bundle_input=_bundle_input_for_generated_plan(plan),
        )
        schema = json.loads(SCHEMA_PATH.read_text())
        errors = list(jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(bundle))
        self.assertEqual(errors, [])
        self.assertEqual(bundle["wp_id"], "WP-DB1L")
        self.assertEqual(bundle["implementation_attempt_id"], plan["implementation_attempt_id"])
        self.assertEqual(bundle["external_side_effect_counts"], ZERO_IMPLEMENTATION_BUNDLE_SIDE_EFFECT_COUNTS)


class TestImplementationBundleTool(unittest.TestCase):
    def test_tool_prints_schema_valid_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            plan_path = tmp / "plan.json"
            input_path = tmp / "bundle-input.json"
            plan_sha = _write_json(plan_path, _make_plan())
            _write_json(input_path, _bundle_input())

            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "docs" / "implementation" / "tools" / "build_implementation_completion_bundle.py"),
                    "--bundle-input",
                    str(input_path),
                    "--plan",
                    str(plan_path),
                    "--plan-sha256",
                    plan_sha,
                    "--dag",
                    str(DAG_PATH),
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            bundle = json.loads(result.stdout)
            schema = json.loads(SCHEMA_PATH.read_text())
            errors = list(jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(bundle))
            self.assertEqual(errors, [])

    def test_tool_returns_3_for_plan_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            plan_path = tmp / "plan.json"
            input_path = tmp / "bundle-input.json"
            _write_json(plan_path, _make_plan())
            _write_json(input_path, _bundle_input())

            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "docs" / "implementation" / "tools" / "build_implementation_completion_bundle.py"),
                    "--bundle-input",
                    str(input_path),
                    "--plan",
                    str(plan_path),
                    "--plan-sha256",
                    "0" * 64,
                    "--dag",
                    str(DAG_PATH),
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 3)
            self.assertEqual(result.stdout, "")
            self.assertIn("plan file hash mismatch", result.stderr)


class TestImplementationBundleCli(unittest.TestCase):
    def test_cli_prints_schema_valid_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            plan_path = tmp / "plan.json"
            input_path = tmp / "bundle-input.json"
            plan_sha = _write_json(plan_path, _make_plan())
            _write_json(input_path, _bundle_input())

            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "build-implementation-completion-bundle",
                    "--bundle-input",
                    str(input_path),
                    "--plan",
                    str(plan_path),
                    "--plan-sha256",
                    plan_sha,
                    "--dag",
                    str(DAG_PATH),
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            bundle = json.loads(result.stdout)
            self.assertEqual(bundle["schema_id"], "seven/implementation-completion-bundle")
            self.assertEqual(bundle["external_side_effect_counts"], ZERO_IMPLEMENTATION_BUNDLE_SIDE_EFFECT_COUNTS)

    def test_cli_boundary_case_returns_3_without_stdout(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            plan_path = tmp / "plan.json"
            input_path = tmp / "bundle-input.json"
            _write_json(plan_path, _make_plan())
            _write_json(input_path, _bundle_input())

            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "build-implementation-completion-bundle",
                    "--bundle-input",
                    str(input_path),
                    "--plan",
                    str(plan_path),
                    "--plan-sha256",
                    "0" * 64,
                    "--dag",
                    str(DAG_PATH),
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 3)
            self.assertEqual(result.stdout, "")
            self.assertIn("plan file hash mismatch", result.stderr)


class TestImplementationBundleStateServiceBridge(unittest.TestCase):
    def test_generated_bundle_is_consumed_by_state_service_complete(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            plan_path = tmp / "plan.json"
            plan_sha = _write_json(plan_path, _make_plan())
            bundle = build_side_effect_free_implementation_completion_bundle(
                bundle_input=_bundle_input(),
                plan_path=plan_path,
                expected_plan_sha256=plan_sha,
                dag_path=DAG_PATH,
            )
            bundle_path = tmp / "bundle.json"
            bundle_sha = _write_json(bundle_path, bundle)

            service = WorkPackageStateService(dag_path=DAG_PATH)
            ok, errors, details = service.register_plan("WP-GV0", plan_path, plan_sha)
            self.assertTrue(ok, f"plan registration failed: {errors} {details}")
            service.wp_states["WP-DOC0"] = "READY_FOR_AUDIT"
            ok, errors, details = service.start("WP-GV0")
            self.assertTrue(ok, f"start failed: {errors} {details}")

            ok, errors, details = service.complete(
                "WP-GV0",
                completion_path=bundle_path,
                expected_file_sha256=bundle_sha,
                completion_contract="IMPLEMENTATION_BUNDLE",
                expected_subject_commit=COMMIT,
                expected_subject_tree=TREE,
            )
            self.assertTrue(ok, f"complete failed: {errors} {details}")
            self.assertEqual(service.get_state("WP-GV0"), "READY_FOR_AUDIT")
            self.assertEqual(service.wp_completion_objects["WP-GV0"]["sha256"], bundle_sha)


if __name__ == "__main__":
    unittest.main()
