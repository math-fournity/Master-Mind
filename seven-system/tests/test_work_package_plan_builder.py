"""Side-effect-free WorkPackagePlan builder tests."""

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
from seven_system.operations.work_package_plan_builder import (
    ZERO_PLAN_SIDE_EFFECT_BUDGET,
    WorkPackagePlanBuilderError,
    build_side_effect_free_work_package_plan,
)
from seven_system.contracts.work_package_plan import verify_work_package_plan_file
from support import write_signed_normative_review_fixture  # noqa: E402


DAG_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
INDEX_PATH = SYSTEM_ROOT / "docs" / "implementation" / "normative-requirement-index.v1.json"
SCHEMA_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-plan.v1.schema.json"
BASELINE = {"commit": "0" * 40, "tree": "1" * 40}


def _ref(name: str, fill: str = "1") -> dict[str, str]:
    return {"ref": name, "sha256": fill * 64}


def _write_json(path: Path, payload: dict) -> str:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _plan_input(wp_id: str = "WP-DB1L") -> dict:
    return {
        "wp_id": wp_id,
        "implementation_attempt_id": f"{wp_id.lower()}-plan-attempt-001",
        "baseline": dict(BASELINE),
        "normative_review_record_ref_and_hash": _ref("reviews/normative-review.json", "2"),
        "development_dependency_bundles": [_ref("evidence/wp-gv0/bundle.json", "3")],
        "inherited_audit_debt": ["upstream READY_FOR_AUDIT is not AUDITED_PASS"],
        "goals": ["derive a schema-valid side-effect-free plan"],
        "non_goals": ["do not authorize live work"],
        "allowed_path_rules": ["derive DAG and normative-index fields mechanically"],
        "forbidden_boundaries": ["no DB writes", "no model calls", "no Solver launch"],
        "input_object_types_and_hashes": [_ref("inputs/db1l-precheck-input.json", "4")],
        "output_object_types": ["WorkPackagePlan"],
        "interfaces_and_schema_ids": ["seven/work-package-plan/v1"],
        "state_machines_and_registries": ["ImplementationCapabilityRegistry"],
        "security_and_view_contracts": ["SIDE_EFFECT_FREE only"],
        "idempotency_fence_recovery_rules": ["rebuild from the same input and frozen index"],
        "test_plan_ids": ["test_work_package_plan_builder"],
        "pass_criteria": ["plan validates against canonical schema"],
        "stop_conditions": ["any requested external side effect"],
        "explicit_nonclaims": ["not an ImplementationCompletionBundle"],
    }


def _write_plan_input_with_review(
    tmp: Path,
    *,
    plan_input: dict | None = None,
    mutate_review: object | None = None,
) -> tuple[Path, Path, str, bytes]:
    payload = plan_input or _plan_input()
    record_path = tmp / "normative-review.json"
    record_sha, public_key_bytes, _ = write_signed_normative_review_fixture(
        record_path,
        index_path=INDEX_PATH,
        mutate=mutate_review,
    )
    if "normative_review_record_ref_and_hash" in payload:
        payload["normative_review_record_ref_and_hash"] = {"ref": str(record_path), "sha256": record_sha}
    input_path = tmp / "plan-input.json"
    _write_json(input_path, payload)
    return input_path, record_path, record_sha, public_key_bytes


def _build(
    plan_input: dict | None = None,
    *,
    mutate_review: object | None = None,
    review_hash_override: str | None = None,
    public_key_override: bytes | None = None,
) -> dict:
    payload = plan_input or _plan_input()
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        record_path = tmp / "normative-review.json"
        record_sha, public_key_bytes, _ = write_signed_normative_review_fixture(
            record_path,
            index_path=INDEX_PATH,
            mutate=mutate_review,
        )
        if "normative_review_record_ref_and_hash" in payload:
            payload["normative_review_record_ref_and_hash"] = {
                "ref": str(record_path),
                "sha256": review_hash_override or record_sha,
            }
        return build_side_effect_free_work_package_plan(
            plan_input=payload,
            dag_path=DAG_PATH,
            normative_index_path=INDEX_PATH,
            normative_review_record_path=record_path,
            normative_review_public_key_bytes=public_key_override or public_key_bytes,
        )


class TestWorkPackagePlanBuilder(unittest.TestCase):
    def test_builds_schema_valid_plan(self) -> None:
        plan = _build()
        schema = json.loads(SCHEMA_PATH.read_text())
        errors = list(jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(plan))
        self.assertEqual(errors, [])
        self.assertEqual(plan["wp_id"], "WP-DB1L")
        self.assertEqual(plan["execution_mode"], "SIDE_EFFECT_FREE")
        self.assertEqual(plan["side_effect_budget"], ZERO_PLAN_SIDE_EFFECT_BUDGET)
        self.assertIsNone(plan["external_execution_authorization_ref"])
        self.assertIsNone(plan["live_run_permit_ref"])
        self.assertIsNone(plan["authorization_consumption_reservation_ref"])
        self.assertEqual(plan["activation_dependencies"], ["WP-GV0", "WP-HG0"])
        self.assertIn("DB-001", plan["requirement_ids"])
        self.assertTrue(plan["normative_clause_ids"])
        self.assertTrue(plan["normative_spec_refs_and_hashes"])

        expected = copy.deepcopy(plan)
        expected["plan_hash"] = None
        self.assertEqual(plan["plan_hash"], hashlib.sha256(canonical_json_bytes(expected)).hexdigest())

    def test_generated_plan_passes_canonical_plan_verifier(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            plan_path = Path(tmpdir) / "plan.json"
            plan = _build()
            plan_sha = _write_json(plan_path, plan)
            result = verify_work_package_plan_file(
                plan_path=plan_path,
                dag_path=DAG_PATH,
                expected_wp_id="WP-DB1L",
                expected_file_sha256=plan_sha,
            )
            self.assertTrue(result.passed, result.details)

    def test_rejects_doc0_and_ga1(self) -> None:
        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "WP-DOC0"):
            _build(_plan_input("WP-DOC0"))
        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "WP-GA1"):
            _build(_plan_input("WP-GA1"))

    def test_rejects_unknown_input_field(self) -> None:
        payload = _plan_input()
        payload["live_run_permit_ref"] = _ref("permit.json", "5")
        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "unknown plan_input fields"):
            _build(payload)

    def test_rejects_missing_normative_review_record(self) -> None:
        payload = _plan_input()
        del payload["normative_review_record_ref_and_hash"]
        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "missing plan_input fields"):
            _build(payload)

    def test_rejects_review_record_hash_mismatch(self) -> None:
        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "RECORD_HASH_MISMATCH"):
            _build(review_hash_override="f" * 64)

    def test_rejects_wrong_review_public_key(self) -> None:
        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "SIGNED_OBJECT_INVALID"):
            _build(public_key_override=b"\x00" * 32)

    def test_rejects_review_record_not_assigning_package(self) -> None:
        def mutate(record: dict) -> None:
            for decision in record["decisions"]:
                decision["consumer_wp_ids"] = ["WP-DOC0"]

        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "no normative review decisions assigned"):
            _build(mutate_review=mutate)

    def test_rejects_non_ref_dependency_bundle(self) -> None:
        payload = _plan_input()
        payload["development_dependency_bundles"] = [{"ref": "missing-sha"}]
        with self.assertRaisesRegex(WorkPackagePlanBuilderError, "development_dependency_bundles"):
            _build(payload)


class TestWorkPackagePlanToolAndCli(unittest.TestCase):
    def test_tool_prints_schema_valid_plan(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path, review_path, _, public_key_bytes = _write_plan_input_with_review(Path(tmpdir))
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "docs" / "implementation" / "tools" / "build_work_package_plan.py"),
                    "--plan-input",
                    str(input_path),
                    "--dag",
                    str(DAG_PATH),
                    "--normative-index",
                    str(INDEX_PATH),
                    "--normative-review-record",
                    str(review_path),
                    "--normative-review-public-key-hex",
                    public_key_bytes.hex(),
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            plan = json.loads(result.stdout)
            self.assertEqual(plan["schema_id"], "seven/work-package-plan")

    def test_cli_prints_schema_valid_plan(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path, review_path, _, public_key_bytes = _write_plan_input_with_review(Path(tmpdir))
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "build-work-package-plan",
                    "--plan-input",
                    str(input_path),
                    "--dag",
                    str(DAG_PATH),
                    "--normative-index",
                    str(INDEX_PATH),
                    "--normative-review-record",
                    str(review_path),
                    "--normative-review-public-key-hex",
                    public_key_bytes.hex(),
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            plan = json.loads(result.stdout)
            self.assertEqual(plan["wp_id"], "WP-DB1L")
            self.assertEqual(plan["side_effect_budget"], ZERO_PLAN_SIDE_EFFECT_BUDGET)

    def test_cli_boundary_case_returns_3_without_stdout(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            payload = _plan_input("WP-GA1")
            input_path, review_path, _, public_key_bytes = _write_plan_input_with_review(Path(tmpdir), plan_input=payload)
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "build-work-package-plan",
                    "--plan-input",
                    str(input_path),
                    "--dag",
                    str(DAG_PATH),
                    "--normative-index",
                    str(INDEX_PATH),
                    "--normative-review-record",
                    str(review_path),
                    "--normative-review-public-key-hex",
                    public_key_bytes.hex(),
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 3)
            self.assertEqual(result.stdout, "")
            self.assertIn("WP-GA1", result.stderr)

    def test_cli_rejects_wrong_review_public_key(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path, review_path, _, _ = _write_plan_input_with_review(Path(tmpdir))
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "build-work-package-plan",
                    "--plan-input",
                    str(input_path),
                    "--dag",
                    str(DAG_PATH),
                    "--normative-index",
                    str(INDEX_PATH),
                    "--normative-review-record",
                    str(review_path),
                    "--normative-review-public-key-hex",
                    "00" * 32,
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 3)
            self.assertEqual(result.stdout, "")
            self.assertIn("SIGNED_OBJECT_INVALID", result.stderr)


if __name__ == "__main__":
    unittest.main()
