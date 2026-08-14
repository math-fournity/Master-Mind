"""OperationsCapabilityReport — OP1 能力报告。

来自 WP-OP1：

READY_FOR_AUDIT最低产物: soak、Redis重建、create→seal→next Epoch、
跨Epoch remainder=0

关键约束（blocker）：
- 未审即 live → OP_UNAUDITED_LIVE
- real scaling FORBIDDEN without GA1 AUDITED_PASS
- SIDE_EFFECT_FREE：所有 side-effect 键为 0

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    OP_CHECK_IDS,
    OP_CLAIMS,
    OP_FORBIDDEN_OUTPUT_KINDS,
    OP_NONCLAIMS,
    OP_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)


OPERATIONS_REPORT_SCHEMA_VERSION = "op1-operations-capability-report/v1"
OPERATIONS_REPORT_SCOPE = "OPERATIONS_CAPABILITY_V1"


class OperationsCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-OP1。"""


def _valid_generated_at(value: object) -> bool:
    if not isinstance(value, str) or any(c in value for c in "\r\n\x00"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _sha256_hex(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(c in "0123456789abcdef" for c in value)
    )


def build_operations_capability_report(
    *,
    dag_hash: str,
    schedule_hash: str,
    redis_rebuild_hash: str,
    epoch_seal_hash: str,
    coverage_tensor_hash: str,
    selection_record_hash: str,
    soak_report_hash: str,
    budget_ledger_hash: str,
    release_pointer_hash: str,
    duplicate_assessment_hash: str,
    longitudinal_verdict_hash: str,
    multi_worker_no_starvation: bool,
    worker_queue_no_loss: bool,
    redis_rebuildable: bool,
    redis_rebuild_hash_match: bool,
    epoch_create_seal_next: bool,
    epoch_sealed_before_next: bool,
    cross_epoch_remainder_zero: bool,
    coverage_tensor_valid: bool,
    selection_record_valid: bool,
    soak_crash_recovered: bool,
    soak_continuous_execution: bool,
    budget_conserved: bool,
    holdout_no_reuse: bool,
    release_mid_epoch_no_change: bool,
    release_activation_gated: bool,
    no_cross_epoch_duplicate: bool,
    longitudinal_verdict_valid: bool,
    real_scaling_blocked_without_ga1: bool,
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 OperationsCapabilityReport。

    READY_FOR_AUDIT 最低产物：soak、Redis 重建、create→seal→next Epoch、
    跨 Epoch remainder=0。
    """
    report: dict[str, Any] = {
        "schema_version": OPERATIONS_REPORT_SCHEMA_VERSION,
        "report_kind": "OperationsCapabilityReport",
        "scope": OPERATIONS_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "dag_hash": dag_hash,
        "schedule_hash": schedule_hash,
        "redis_rebuild_hash": redis_rebuild_hash,
        "epoch_seal_hash": epoch_seal_hash,
        "coverage_tensor_hash": coverage_tensor_hash,
        "selection_record_hash": selection_record_hash,
        "soak_report_hash": soak_report_hash,
        "budget_ledger_hash": budget_ledger_hash,
        "release_pointer_hash": release_pointer_hash,
        "duplicate_assessment_hash": duplicate_assessment_hash,
        "longitudinal_verdict_hash": longitudinal_verdict_hash,
        "multi_worker_no_starvation": multi_worker_no_starvation,
        "worker_queue_no_loss": worker_queue_no_loss,
        "redis_rebuildable": redis_rebuildable,
        "redis_rebuild_hash_match": redis_rebuild_hash_match,
        "epoch_create_seal_next": epoch_create_seal_next,
        "epoch_sealed_before_next": epoch_sealed_before_next,
        "cross_epoch_remainder_zero": cross_epoch_remainder_zero,
        "coverage_tensor_valid": coverage_tensor_valid,
        "selection_record_valid": selection_record_valid,
        "soak_crash_recovered": soak_crash_recovered,
        "soak_continuous_execution": soak_continuous_execution,
        "budget_conserved": budget_conserved,
        "holdout_no_reuse": holdout_no_reuse,
        "release_mid_epoch_no_change": release_mid_epoch_no_change,
        "release_activation_gated": release_activation_gated,
        "no_cross_epoch_duplicate": no_cross_epoch_duplicate,
        "longitudinal_verdict_valid": longitudinal_verdict_valid,
        "real_scaling_blocked_without_ga1": real_scaling_blocked_without_ga1,
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in OP_CHECK_IDS
        ],
        "claims": {claim: True for claim in OP_CLAIMS},
        "side_effects": {key: 0 for key in OP_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(OP_NONCLAIMS),
    }

    errors = verify_operations_capability_report(report)
    if errors:
        raise OperationsCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_operations_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 OperationsCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != OPERATIONS_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {OPERATIONS_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "OperationsCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be OperationsCapabilityReport",
        ))

    # boundary check
    if rk in OP_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.OP_OUTPUT_KIND_FORBIDDEN,
            f"OP1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != OPERATIONS_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {OPERATIONS_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # hashes
    for field_name in (
        "dag_hash", "schedule_hash", "redis_rebuild_hash",
        "epoch_seal_hash", "coverage_tensor_hash",
        "selection_record_hash", "soak_report_hash",
        "budget_ledger_hash", "release_pointer_hash",
        "duplicate_assessment_hash", "longitudinal_verdict_hash",
    ):
        val = report.get(field_name)
        if not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex",
            ))

    # constraint flags
    flag_map = {
        "multi_worker_no_starvation": EC.OP_WORKER_STARVATION,
        "worker_queue_no_loss": EC.OP_QUEUE_LOSS,
        "redis_rebuildable": EC.OP_REDIS_NOT_REBUILDABLE,
        "redis_rebuild_hash_match": EC.OP_REDIS_NOT_REBUILDABLE,
        "epoch_create_seal_next": EC.OP_EPOCH_NOT_SEALED,
        "epoch_sealed_before_next": EC.OP_EPOCH_NOT_SEALED,
        "cross_epoch_remainder_zero": EC.OP_CROSS_EPOCH_REMAINDER_NONZERO,
        "coverage_tensor_valid": EC.OP_COVERAGE_TENSOR_INVALID,
        "selection_record_valid": EC.OP_SELECTION_RECORD_INVALID,
        "soak_crash_recovered": EC.OP_SOAK_CRASH_NOT_RECOVERED,
        "soak_continuous_execution": EC.OP_SOAK_STATE_INVALID,
        "budget_conserved": EC.OP_BUDGET_NOT_CONSERVED,
        "holdout_no_reuse": EC.OP_HOLDOUT_REUSE_ACROSS_EPOCHS,
        "release_mid_epoch_no_change": EC.OP_MID_EPOCH_VERSION_CHANGE,
        "release_activation_gated": EC.OP_ACTIVE_RELEASE_NOT_GATED,
        "no_cross_epoch_duplicate": EC.OP_CROSS_EPOCH_DUPLICATE,
        "longitudinal_verdict_valid": EC.OP_LONGITUDINAL_VERDICT_INVALID,
        "real_scaling_blocked_without_ga1": EC.OP_UNAUDITED_LIVE,
    }
    for flag_name, code in flag_map.items():
        if report.get(flag_name) is not True:
            errors.append((code, f"{flag_name} must be True"))

    # checks
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "checks must be an array"))
    else:
        check_ids = [
            c.get("check_id") if isinstance(c, dict) else None for c in checks
        ]
        if not all(isinstance(cid, str) for cid in check_ids):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "every check ID must be a string",
            ))
        elif len(check_ids) != len(set(check_ids)):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "check IDs must not contain duplicates",
            ))
        elif check_ids != list(OP_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((
                    EC.REQUIRED_FIELD_MISSING,
                    "every OP1 check must be PASS",
                ))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(OP_CLAIMS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "claim set does not exactly match OP1 claims",
        ))
    elif any(claims[c] is not True for c in OP_CLAIMS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "all OP1 claims must be true",
        ))

    # side_effects
    side_effects = report.get("side_effects")
    if (
        not isinstance(side_effects, dict)
        or set(side_effects) != set(OP_SIDE_EFFECT_KEYS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the OP1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in OP_SIDE_EFFECT_KEYS):
        errors.append((
            EC.OP_OUTPUT_KIND_FORBIDDEN,
            "all OP1 report side effects must be zero",
        ))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "OP1 report verdict must be PASS",
        ))

    # blockers
    if report.get("blockers") != []:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "PASS OP1 report must have no blockers",
        ))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(OP_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the OP1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
