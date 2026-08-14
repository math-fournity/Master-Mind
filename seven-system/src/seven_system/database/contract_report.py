"""G-WP1-C 的离线 StrictDbContract 报告生成与机器验证。

报告不能接受调用者自报的 PASS/evidence/hash。生成与验证都会在清空 Arango
凭据的子进程中重跑固定测试模块，并把确定性测试收据绑定到当前实现树。
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..hashing import file_sha256, object_hash
from ..schema_validation import validate_schema
from .capability import (
    STRICT_DATABASE_CONTRACT_CHECK_IDS,
    StrictDatabaseContractSubject,
)
from .environment import EXPECTED_DATABASE
from .port import DATABASE_PORT_CONTRACT_VERSION


REPORT_SCHEMA_VERSION = "wp1-strict-db-contract-report/v1"
REPORT_SCHEMA_NAME = "wp1-strict-db-contract-report.schema.json"
REPORT_SCOPE = "OFFLINE_STATIC_AND_FAKE_ADAPTER"
TEST_SUITE_EVIDENCE_PREFIX = "test_execution_receipt_sha256="

STRICT_DB_CONTRACT_CLAIMS = (
    "expected_database_fail_closed",
    "no_default_database",
    "reads_have_no_schema_side_effects",
    "migration_is_explicit",
    "collection_names_are_seven_prefixed",
    "unique_index_plan_is_frozen",
    "ledger_sequence_unique_index_spec_frozen",
    "outbox_unique_index_spec_frozen",
    "no_raw_client_escape_hatch",
)

STRICT_DB_REPORT_SIDE_EFFECT_KEYS = (
    "database_connections",
    "database_writes",
    "migrations_applied",
    "container_restarts",
    "solver_launches",
    "redis_writes",
)

STRICT_DB_REPORT_NONCLAIMS = (
    "does_not_prove_database_site_capability",
    "does_not_verify_physical_database_storage",
    "does_not_connect_to_arangodb_or_apply_migrations",
    "does_not_provide_durable_migration_ledger_fence_or_resume",
    "does_not_prove_runtime_append_only_cas_or_outbox_delivery_semantics",
    "does_not_authenticate_wall_clock_or_file_immutability",
)

_BOUND_TEST_PATHS = (
    "tests/strict_db_contract_runner.py",
    "tests/test_database_contract_report.py",
    "tests/test_database_environment.py",
    "tests/test_database_migration.py",
    "tests/test_database_spec.py",
)
_BOUND_DEPENDENCY_PATHS = (
    f"schemas/{REPORT_SCHEMA_NAME}",
    "schemas/runtime-config.schema.json",
    "scripts/seven.py",
    "src/seven_system/cli.py",
    "src/seven_system/__main__.py",
    "src/seven_system/config.py",
    "src/seven_system/hashing.py",
    "src/seven_system/preflight.py",
    "src/seven_system/schema_validation.py",
    "src/seven_system/storage/__init__.py",
    "src/seven_system/storage/_legacy.py",
    "src/seven_system/storage/artifact_store.py",
    "src/seven_system/contracts/__init__.py",
    "src/seven_system/contracts/errors.py",
    "src/seven_system/contracts/completion_contract.py",
    "src/seven_system/contracts/security_contract.py",
    "src/seven_system/contracts/reservation.py",
    "src/seven_system/contracts/capability_report.py",
)
_CORE_TEST_MODULES = (
    "tests.test_database_environment",
    "tests.test_database_migration",
    "tests.test_database_spec",
)
_CONTROLLED_RUNNER_PATH = "tests/strict_db_contract_runner.py"
_CHECK_TEST_METHODS: dict[str, tuple[str, ...]] = {
    "strict_db.environment.required_before_client": (
        "test_missing_environment_constructs_zero_clients",
    ),
    "strict_db.identity.expected_before_client": (
        "test_wrong_database_constructs_zero_clients_and_hides_actual_value",
    ),
    "strict_db.identity.current_database_verified": (
        "test_current_database_mismatch_is_rejected_after_connection",
    ),
    "strict_db.collections.fixed_allowlist": (
        "test_unknown_and_unicode_collections_never_reach_driver",
        "test_collection_allowlist_is_exact_and_versioned",
    ),
    "strict_db.secrets.redacted": (
        "test_environment_has_no_defaults_and_redacts_password",
        "test_driver_failure_does_not_leak_password_or_cause",
    ),
    "strict_db.raw_client.no_public_bypass": (
        "test_raw_driver_constructor_is_not_a_public_bypass",
    ),
    "strict_db.planner.read_only": (
        "test_plan_is_deterministic_and_has_zero_write_side_effects",
    ),
    "strict_db.migration.no_runtime_apply_primitive": (
        "test_no_runtime_apply_or_ddl_primitive_is_exposed",
    ),
    "strict_db.spec.canonical_hash": (
        "test_migration_spec_is_json_serializable_and_hash_stable",
        "test_index_semantics_are_explicit_unique_and_auditable",
    ),
    "strict_db.schema.extra_indexes_rejected": (
        "test_extra_persistent_index_is_schema_drift",
        "test_nonpersistent_user_index_is_not_hidden_from_planner",
    ),
    "strict_db.capability.site_separation": (
        "test_offline_contract_and_site_capability_subjects_are_separate",
    ),
}


class StrictDbContractReportError(ValueError):
    """报告输入、绑定文件或受控测试不满足 G-WP1-C。"""


def _system_root(system_root: Path | None) -> Path:
    return (
        Path(__file__).resolve().parents[3]
        if system_root is None
        else Path(system_root).resolve()
    )


def strict_db_implementation_tree_files(
    system_root: Path | None = None,
) -> tuple[Path, ...]:
    """返回 StrictDbContract subject 必须绑定的完整、稳定文件集合。"""

    root = _system_root(system_root)
    database_sources = tuple(
        sorted((root / "src" / "seven_system" / "database").glob("*.py"))
    )
    if not database_sources:
        raise StrictDbContractReportError("database source tree is missing")
    paths = (
        *database_sources,
        *(root / relative for relative in _BOUND_TEST_PATHS),
        *(root / relative for relative in _BOUND_DEPENDENCY_PATHS),
    )
    if len(paths) != len(set(paths)):
        raise StrictDbContractReportError("implementation tree contains duplicate paths")
    for path in paths:
        try:
            path.relative_to(root)
        except ValueError:
            raise StrictDbContractReportError(
                "implementation tree path escapes Seven System root"
            ) from None
        if path.is_symlink() or not path.is_file():
            raise StrictDbContractReportError(
                "bound implementation file is missing or a symlink"
            )
    return tuple(paths)


def strict_db_implementation_tree_hash(system_root: Path | None = None) -> str:
    root = _system_root(system_root)
    entries = [
        {"path": path.relative_to(root).as_posix(), "sha256": file_sha256(path)}
        for path in strict_db_implementation_tree_files(root)
    ]
    entries.sort(key=lambda item: item["path"])
    return object_hash(
        "StrictDbImplementationTree", "strict-db-implementation-tree/v1", entries
    )


def _load_report_schema(system_root: Path) -> dict[str, Any]:
    try:
        payload = json.loads(
            (system_root / "schemas" / REPORT_SCHEMA_NAME).read_text(encoding="utf-8")
        )
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StrictDbContractReportError(
            "cannot load the StrictDbContract report schema"
        ) from exc
    if not isinstance(payload, dict):
        raise StrictDbContractReportError("report schema root must be an object")
    return payload


def _valid_generated_at(value: object) -> bool:
    if not isinstance(value, str) or any(character in value for character in "\r\n\x00"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _run_controlled_tests(
    system_root: Path,
) -> tuple[str, dict[str, tuple[str, ...]]]:
    """重跑固定测试集合；不接受调用者传入的 verdict 或 evidence。"""

    if set(_CHECK_TEST_METHODS) != set(STRICT_DATABASE_CONTRACT_CHECK_IDS):
        raise StrictDbContractReportError(
            "controlled test map does not match canonical check IDs"
        )
    environment = {
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONIOENCODING": "utf-8",
    }
    command = [
        sys.executable,
        "-I",
        "-S",
        "-B",
        str(system_root / _CONTROLLED_RUNNER_PATH),
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=system_root,
            env=environment,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise StrictDbContractReportError(
            "controlled Strict DB test execution failed"
        ) from exc
    if completed.returncode != 0:
        raise StrictDbContractReportError(
            "controlled Strict DB test suite did not PASS"
        )
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise StrictDbContractReportError(
            "controlled Strict DB runner did not return machine JSON"
        ) from exc
    if not isinstance(result, dict):
        raise StrictDbContractReportError(
            "controlled Strict DB runner result must be an object"
        )
    test_ids = result.get("test_ids")
    tests_run = result.get("tests_run")
    clean_result = (
        result.get("schema_version") == "strict-db-controlled-test-result/v1"
        and result.get("test_modules") == list(_CORE_TEST_MODULES)
        and isinstance(test_ids, list)
        and bool(test_ids)
        and all(isinstance(test_id, str) for test_id in test_ids)
        and len(test_ids) == len(set(test_ids))
        and isinstance(tests_run, int)
        and not isinstance(tests_run, bool)
        and tests_run == len(test_ids)
        and result.get("successful") is True
        and all(
            result.get(key) == 0
            for key in (
                "failures",
                "errors",
                "skipped",
                "expected_failures",
                "unexpected_successes",
            )
        )
    )
    if not clean_result:
        raise StrictDbContractReportError(
            "controlled Strict DB runner returned an incomplete result"
        )
    evidence: dict[str, tuple[str, ...]] = {}
    ordered_methods: list[str] = []
    for check_id in STRICT_DATABASE_CONTRACT_CHECK_IDS:
        methods = _CHECK_TEST_METHODS[check_id]
        for method in methods:
            matches = [
                test_id
                for test_id in test_ids
                if test_id.rsplit(".", 1)[-1] == method
            ]
            if len(matches) != 1:
                raise StrictDbContractReportError(
                    "controlled test result lacks a unique required method"
                )
            ordered_methods.append(method)
        evidence[check_id] = tuple(f"unittest={method}" for method in methods)
    receipt_hash = object_hash(
        "StrictDbTestExecutionReceipt",
        "strict-db-test-execution-receipt/v1",
        {
            "implementation_sha256": strict_db_implementation_tree_hash(system_root),
            "test_modules": list(_CORE_TEST_MODULES),
            "passed_test_methods": ordered_methods,
            "complete_test_ids": test_ids,
            "tests_run": tests_run,
            "database_environment_removed": True,
            "database_connections": 0,
        },
    )
    marker = TEST_SUITE_EVIDENCE_PREFIX + receipt_hash
    return receipt_hash, {
        check_id: (*items, marker) for check_id, items in evidence.items()
    }


def _subject_hash(system_root: Path) -> str:
    return StrictDatabaseContractSubject(
        implementation_sha256=strict_db_implementation_tree_hash(system_root)
    ).subject_hash


def build_strict_db_contract_report(
    *, system_root: Path | None = None
) -> dict[str, Any]:
    """受控重跑固定测试后构造报告；调用者不能注入PASS/evidence/hash。"""

    root = _system_root(system_root)
    _, evidence = _run_controlled_tests(root)
    generated_at = datetime.now(timezone.utc).isoformat()
    report: dict[str, Any] = {
        "schema_version": REPORT_SCHEMA_VERSION,
        "report_kind": "StrictDbContractReport",
        "contract": DATABASE_PORT_CONTRACT_VERSION,
        "scope": REPORT_SCOPE,
        "generated_at": generated_at,
        "subject_hash": _subject_hash(root),
        "verdict": "PASS",
        "checks": [
            {"check_id": check_id, "verdict": "PASS", "evidence": list(evidence[check_id])}
            for check_id in STRICT_DATABASE_CONTRACT_CHECK_IDS
        ],
        "claims": {claim: True for claim in STRICT_DB_CONTRACT_CLAIMS},
        "migration_policy": {
            "mode": "PLAN_AND_VERIFY_ONLY",
            "expected_database": EXPECTED_DATABASE,
            "collection_prefix": "seven_",
            "shared_production_apply_allowed": False,
        },
        "side_effects": {key: 0 for key in STRICT_DB_REPORT_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(STRICT_DB_REPORT_NONCLAIMS),
    }
    errors = verify_strict_db_contract_report(report, system_root=root)
    if errors:
        raise StrictDbContractReportError(
            "generated report failed verification: " + "; ".join(errors)
        )
    return report


def verify_strict_db_contract_report(
    report: object, *, system_root: Path | None = None
) -> tuple[str, ...]:
    """Schema+语义验证，并独立重跑固定测试；空tuple才是有效PASS。"""

    errors: list[str] = []
    root = _system_root(system_root)
    try:
        schema = _load_report_schema(root)
    except StrictDbContractReportError as exc:
        return (str(exc),)
    errors.extend(validate_schema(report, schema))
    if not isinstance(report, dict):
        return tuple(errors or ["report root must be an object"])

    try:
        receipt_hash, expected_evidence = _run_controlled_tests(root)
    except StrictDbContractReportError as exc:
        errors.append(str(exc))
        receipt_hash, expected_evidence = "", {}

    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append("checks must be an array")
    else:
        check_ids = [item.get("check_id") if isinstance(item, dict) else None for item in checks]
        check_ids_are_strings = all(isinstance(check_id, str) for check_id in check_ids)
        if not check_ids_are_strings:
            errors.append("every check ID must be a string")
        elif len(check_ids) != len(set(check_ids)):
            errors.append("check IDs must not contain duplicates")
        if not check_ids_are_strings or check_ids != list(
            STRICT_DATABASE_CONTRACT_CHECK_IDS
        ):
            errors.append("checks must exactly match canonical IDs and order")
        marker = TEST_SUITE_EVIDENCE_PREFIX + receipt_hash
        for item in checks:
            if not isinstance(item, dict):
                continue
            check_id = item.get("check_id")
            if item.get("verdict") != "PASS":
                errors.append("every StrictDbContract check must be PASS")
            evidence = item.get("evidence")
            if not isinstance(check_id, str):
                errors.append("check evidence has a non-string check ID")
                continue
            if (
                check_id not in expected_evidence
                or not isinstance(evidence, list)
                or evidence != list(expected_evidence[check_id])
                or marker not in evidence
            ):
                errors.append("check evidence does not match the controlled test receipt")

    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(STRICT_DB_CONTRACT_CLAIMS):
        errors.append("claim set does not exactly match StrictDbContract")
    elif any(claims[claim] is not True for claim in STRICT_DB_CONTRACT_CLAIMS):
        errors.append("all nine StrictDbContract claims must be true")

    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(
        STRICT_DB_REPORT_SIDE_EFFECT_KEYS
    ):
        errors.append("side-effect set does not match the offline report scope")
    elif any(side_effects[key] != 0 for key in STRICT_DB_REPORT_SIDE_EFFECT_KEYS):
        errors.append("all offline report side effects must be zero")
    if report.get("verdict") != "PASS":
        errors.append("StrictDbContract report verdict must be PASS")
    if report.get("blockers") != []:
        errors.append("PASS StrictDbContract report must have no blockers")
    if not _valid_generated_at(report.get("generated_at")):
        errors.append("generated_at is not a timezone-aware ISO-8601 timestamp")
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(STRICT_DB_REPORT_NONCLAIMS)
    ):
        errors.append("explicit nonclaims must preserve the offline/site boundary")
    try:
        expected_subject_hash = _subject_hash(root)
    except StrictDbContractReportError as exc:
        errors.append(str(exc))
    else:
        if report.get("subject_hash") != expected_subject_hash:
            errors.append("subject hash does not match the current implementation/spec")
    return tuple(dict.fromkeys(errors))
