"""Fail-closed verification for frozen ``WorkPackagePlan`` files.

The state service must never treat a caller supplied path/hash pair as proof
that a plan exists.  This module reads the referenced file, executes the
canonical JSON Schema, recomputes both the file digest and the plan self-hash,
and binds the plan to the exact canonical DAG used by the state service.

The verifier is deliberately side-effect free.  A verified plan is an
immutable snapshot of what was read; callers still re-run verification before
every state-changing start operation so post-registration drift is rejected.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..hashing import canonical_json_bytes, file_sha256
from .errors import VerificationErrorCode as EC


@dataclass(frozen=True)
class VerifiedWorkPackagePlan:
    wp_id: str
    plan_path: Path
    file_sha256: str
    plan_hash: str
    canonical_dag_sha256: str
    plan: dict[str, Any]


@dataclass(frozen=True)
class WorkPackagePlanVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    verified_plan: VerifiedWorkPackagePlan | None = None

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS" and self.verified_plan is not None


def _canonical_plan_hash(plan: dict[str, Any]) -> str:
    candidate = copy.deepcopy(plan)
    candidate["plan_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def verify_work_package_plan_file(
    *,
    plan_path: Path,
    dag_path: Path,
    expected_wp_id: str,
    expected_file_sha256: str | None = None,
) -> WorkPackagePlanVerificationResult:
    """Verify one on-disk plan against the canonical Schema and DAG.

    ``expected_file_sha256`` is optional only so a caller may discover the
    digest during a controlled import.  State-changing consumers should pass
    it and then retain the returned immutable snapshot.
    """

    errors: list[EC] = []
    details: list[str] = []
    plan_path = Path(plan_path)
    dag_path = Path(dag_path)

    if plan_path.is_symlink():
        return WorkPackagePlanVerificationResult(
            verdict="FAIL",
            error_codes=[EC.SCHEMA_VALIDATION_FAILED],
            details=[f"plan path must not be a symlink: {plan_path}"],
        )
    if not plan_path.is_file():
        return WorkPackagePlanVerificationResult(
            verdict="FAIL",
            error_codes=[EC.SCHEMA_FILE_NOT_FOUND],
            details=[f"plan file does not exist: {plan_path}"],
        )
    if not dag_path.is_file():
        return WorkPackagePlanVerificationResult(
            verdict="FAIL",
            error_codes=[EC.DAG_LOAD_FAILED],
            details=[f"canonical DAG does not exist: {dag_path}"],
        )

    try:
        raw = plan_path.read_bytes()
        plan = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        return WorkPackagePlanVerificationResult(
            verdict="FAIL",
            error_codes=[EC.SCHEMA_VALIDATION_FAILED],
            details=[f"cannot read plan JSON: {exc}"],
        )
    if not isinstance(plan, dict):
        return WorkPackagePlanVerificationResult(
            verdict="FAIL",
            error_codes=[EC.SCHEMA_VALIDATION_FAILED],
            details=["WorkPackagePlan must be a JSON object"],
        )

    actual_file_sha256 = hashlib.sha256(raw).hexdigest()
    if expected_file_sha256 is not None and actual_file_sha256 != expected_file_sha256:
        errors.append(EC.SUBJECT_HASH_MISMATCH)
        details.append(
            "plan file hash mismatch: "
            f"expected {expected_file_sha256}, got {actual_file_sha256}"
        )

    schema_path = dag_path.parent / "work-package-plan.v1.schema.json"
    try:
        from jsonschema import Draft202012Validator, FormatChecker

        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        schema_errors = sorted(
            validator.iter_errors(plan), key=lambda item: list(item.absolute_path)
        )
        if schema_errors:
            errors.append(EC.SCHEMA_VALIDATION_FAILED)
            details.extend(
                "plan schema error at "
                f"{'.'.join(map(str, item.absolute_path)) or '(root)'}: {item.message}"
                for item in schema_errors[:20]
            )
    except Exception as exc:  # missing Schema/validator is a hard failure
        errors.append(EC.SCHEMA_FILE_LOAD_FAILED)
        details.append(f"cannot execute canonical plan Schema {schema_path}: {exc}")

    if plan.get("wp_id") != expected_wp_id:
        errors.append(EC.WP_ID_MISMATCH)
        details.append(
            f"plan wp_id mismatch: expected {expected_wp_id}, got {plan.get('wp_id')!r}"
        )

    expected_plan_hash = _canonical_plan_hash(plan)
    if plan.get("plan_hash") != expected_plan_hash:
        errors.append(EC.SELF_HASH_MISMATCH)
        details.append(
            "plan_hash mismatch: "
            f"expected {expected_plan_hash}, got {plan.get('plan_hash')!r}"
        )

    dag_sha256 = file_sha256(dag_path)
    dag_binding = plan.get("canonical_dag")
    if not isinstance(dag_binding, dict) or dag_binding.get("sha256") != dag_sha256:
        errors.append(EC.DAG_HASH_MISMATCH)
        details.append(
            "plan canonical_dag hash mismatch: "
            f"expected {dag_sha256}, got "
            f"{dag_binding.get('sha256') if isinstance(dag_binding, dict) else None!r}"
        )

    if errors:
        return WorkPackagePlanVerificationResult(
            verdict="FAIL", error_codes=errors, details=details
        )

    return WorkPackagePlanVerificationResult(
        verdict="PASS",
        verified_plan=VerifiedWorkPackagePlan(
            wp_id=expected_wp_id,
            plan_path=plan_path.resolve(),
            file_sha256=actual_file_sha256,
            plan_hash=str(plan["plan_hash"]),
            canonical_dag_sha256=dag_sha256,
            plan=copy.deepcopy(plan),
        ),
    )


__all__ = [
    "VerifiedWorkPackagePlan",
    "WorkPackagePlanVerificationResult",
    "verify_work_package_plan_file",
]
