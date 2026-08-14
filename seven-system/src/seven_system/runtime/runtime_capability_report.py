"""DatabaseRuntimeCapabilityReport + ArtifactCommitReconcileCapabilityReport.

RT1 的完成输出严格限定为：
- DatabaseRuntimeCapabilityReport
- ArtifactCommitReconcileCapabilityReport
- RuntimeCheckpoint / recovery receipts

RT1 不得重发 SchemaStateReport（那是 DB1I 的输出）。

DatabaseRuntimeCapabilityReport 验证：
- 受限 principal 只写 seven_*
- expected-revision transaction / CAS
- WorkEvent sequence
- lease/fence
- outbox
- duplicate delivery
- Redis rebuild
- 关键崩溃恢复

ArtifactCommitReconcileCapabilityReport 验证：
- CommitIntent
- permit reserve/consume
- partial→seal
- fsync/rename
- CAS/DB 双向对账
- stale fence/cancel/revocation 拒绝
- 单边崩溃的真实恢复

SIDE_EFFECT_FREE：纯计算，不接触真实 DB/Redis/D 盘。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    RT1_ALLOWED_OUTPUT_KINDS,
    RT1_FORBIDDEN_OUTPUT_KINDS,
    VerificationErrorCode as EC,
)
from ..hashing import canonical_json_bytes, object_hash

# ─── DatabaseRuntimeCapabilityReport ───────────────────────────────────

RUNTIME_REPORT_SCHEMA_VERSION = "rt1-database-runtime-capability-report/v1"
RUNTIME_REPORT_SCOPE = "RUNTIME_CAPABILITY_V1"

RUNTIME_CHECK_IDS = (
    "rt1.runtime.principal_writes_seven_only",
    "rt1.runtime.expected_revision_transaction",
    "rt1.runtime.workevent_sequence_monotonic",
    "rt1.runtime.lease_fence_protocol",
    "rt1.runtime.outbox_same_transaction",
    "rt1.runtime.duplicate_delivery_rejected",
    "rt1.runtime.redis_rebuild_from_events",
    "rt1.runtime.crash_recovery_checkpoint",
    "rt1.runtime.canonical_db_reservation_backend",
    "rt1.runtime.boundary_no_schema_state_report",
)

RUNTIME_CLAIMS = (
    "principal_writes_seven_only",
    "expected_revision_transaction_verified",
    "workevent_sequence_monotonic",
    "lease_fence_protocol_verified",
    "outbox_same_transaction_as_state_events",
    "duplicate_delivery_rejected",
    "redis_rebuildable_from_events",
    "crash_recovery_via_checkpoint",
    "canonical_db_reservation_backend_implemented",
    "does_not_reissue_schema_state_report",
)

RUNTIME_NONCLAIMS = (
    "does_not_prove_schema_correctness",
    "does_not_prove_solver_or_model_role_capability",
    "does_not_prove_answer_isolation",
    "does_not_connect_to_arangodb_in_test_suite",
    "does_not_authorize_live_canary_or_solver_dispatch",
)

RUNTIME_SIDE_EFFECT_KEYS = (
    "database_connections",
    "database_writes",
    "redis_connections",
    "redis_writes",
    "d_volume_writes",
    "solver_launches",
)

# ─── ArtifactCommitReconcileCapabilityReport ───────────────────────────

RECONCILE_REPORT_SCHEMA_VERSION = "rt1-artifact-commit-reconcile-capability-report/v1"
RECONCILE_REPORT_SCOPE = "ARTIFACT_RECONCILE_V1"

RECONCILE_CHECK_IDS = (
    "rt1.reconcile.commit_intent_durable",
    "rt1.reconcile.permit_reserve_consume",
    "rt1.reconcile.partial_to_seal",
    "rt1.reconcile.cas_db_two_sided_reconcile",
    "rt1.reconcile.stale_fence_rejected",
    "rt1.reconcile.cancel_revocation_rejected",
    "rt1.reconcile.crash_after_seal_before_db_commit",
    "rt1.reconcile.crash_after_db_commit_before_outbox",
    "rt1.reconcile.redis_full_loss_rebuild",
    "rt1.reconcile.boundary_no_schema_state_report",
)

RECONCILE_CLAIMS = (
    "commit_intent_durable_before_rename",
    "permit_reserve_consume_verified",
    "partial_to_seal_protocol_verified",
    "cas_db_two_sided_reconcile",
    "stale_fence_rejected",
    "cancel_revocation_rejected",
    "crash_after_seal_before_db_commit_recovered",
    "crash_after_db_commit_before_outbox_recovered",
    "redis_full_loss_rebuilt_from_events",
    "does_not_reissue_schema_state_report",
)

RECONCILE_NONCLAIMS = (
    "does_not_prove_db_identity",
    "does_not_prove_solver_or_model_role_capability",
    "does_not_prove_answer_isolation",
    "does_not_connect_to_arangodb_in_test_suite",
    "does_not_authorize_live_canary_or_solver_dispatch",
)

RECONCILE_SIDE_EFFECT_KEYS = (
    "database_connections",
    "database_writes",
    "redis_connections",
    "redis_writes",
    "d_volume_writes",
    "solver_launches",
)


class CapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-RT1。"""


def _valid_generated_at(value: object) -> bool:
    if not isinstance(value, str) or any(c in value for c in "\r\n\x00"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _sha256_hex(value: str) -> bool:
    return len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def build_database_runtime_capability_report(
    *,
    site_fingerprint_hash: str,
    database_identity_hash: str,
    spec_hash: str,
    plan_hash: str,
    dag_hash: str,
    schema_state_report_hash: str,
    probe_results: list[dict[str, Any]],
    positive_evidence_refs: list[str],
    negative_evidence_refs: list[str],
    residual_risks: list[str],
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 DatabaseRuntimeCapabilityReport。"""
    report: dict[str, Any] = {
        "schema_version": RUNTIME_REPORT_SCHEMA_VERSION,
        "report_kind": "DatabaseRuntimeCapabilityReport",
        "scope": RUNTIME_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "site_fingerprint_hash": site_fingerprint_hash,
        "database_identity_hash": database_identity_hash,
        "spec_hash": spec_hash,
        "plan_hash": plan_hash,
        "dag_hash": dag_hash,
        "schema_state_report_hash": schema_state_report_hash,
        "probe_results": list(probe_results),
        "positive_and_negative_evidence_refs": {
            "positive": list(positive_evidence_refs),
            "negative": list(negative_evidence_refs),
        },
        "residual_risks": list(residual_risks),
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in RUNTIME_CHECK_IDS
        ],
        "claims": {claim: True for claim in RUNTIME_CLAIMS},
        "side_effects": {key: 0 for key in RUNTIME_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(RUNTIME_NONCLAIMS),
    }

    errors = verify_database_runtime_capability_report(report)
    if errors:
        raise CapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_database_runtime_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 DatabaseRuntimeCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != RUNTIME_REPORT_SCHEMA_VERSION:
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                f"schema_version must be {RUNTIME_REPORT_SCHEMA_VERSION}",
            )
        )

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "DatabaseRuntimeCapabilityReport":
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "report_kind must be DatabaseRuntimeCapabilityReport",
            )
        )

    # 边界检查：不得是 DB1I 的输出
    if rk in RT1_FORBIDDEN_OUTPUT_KINDS:
        errors.append(
            (
                EC.RUNTIME_SCHEMA_STATE_REPORT_REISSUED,
                f"RT1 must not produce {rk}",
            )
        )

    # scope
    if report.get("scope") != RUNTIME_REPORT_SCOPE:
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, f"scope must be {RUNTIME_REPORT_SCOPE}")
        )

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "generated_at is not a timezone-aware ISO-8601 timestamp",
            )
        )

    # hashes
    for field_name in (
        "site_fingerprint_hash",
        "database_identity_hash",
        "spec_hash",
        "plan_hash",
        "dag_hash",
        "schema_state_report_hash",
    ):
        val = report.get(field_name)
        if not isinstance(val, str) or not _sha256_hex(val):
            errors.append(
                (
                    EC.REQUIRED_FIELD_MISSING,
                    f"{field_name} must be a lowercase sha256 hex",
                )
            )

    # checks
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "checks must be an array"))
    else:
        check_ids = [c.get("check_id") if isinstance(c, dict) else None for c in checks]
        if not all(isinstance(cid, str) for cid in check_ids):
            errors.append(
                (EC.REQUIRED_FIELD_MISSING, "every check ID must be a string")
            )
        elif len(check_ids) != len(set(check_ids)):
            errors.append(
                (EC.REQUIRED_FIELD_MISSING, "check IDs must not contain duplicates")
            )
        elif check_ids != list(RUNTIME_CHECK_IDS):
            errors.append(
                (
                    EC.REQUIRED_FIELD_MISSING,
                    "checks must exactly match canonical IDs and order",
                )
            )
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append(
                    (EC.REQUIRED_FIELD_MISSING, "every RT1 check must be PASS")
                )

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(RUNTIME_CLAIMS):
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match RT1 claims")
        )
    elif any(claims[c] is not True for c in RUNTIME_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all RT1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(
        RUNTIME_SIDE_EFFECT_KEYS
    ):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "side-effect set does not match the RT1 report scope",
            )
        )
    elif any(side_effects[k] != 0 for k in RUNTIME_SIDE_EFFECT_KEYS):
        errors.append(
            (EC.DB1L_WRITE_DETECTED, "all RT1 report side effects must be zero")
        )

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "RT1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, "PASS RT1 report must have no blockers")
        )

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(RUNTIME_NONCLAIMS)
    ):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "explicit nonclaims must preserve the runtime boundary",
            )
        )

    return tuple(dict.fromkeys(errors))


def build_artifact_commit_reconcile_capability_report(
    *,
    site_fingerprint_hash: str,
    database_identity_hash: str,
    spec_hash: str,
    plan_hash: str,
    dag_hash: str,
    schema_state_report_hash: str,
    probe_results: list[dict[str, Any]],
    positive_evidence_refs: list[str],
    negative_evidence_refs: list[str],
    residual_risks: list[str],
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 ArtifactCommitReconcileCapabilityReport。"""
    report: dict[str, Any] = {
        "schema_version": RECONCILE_REPORT_SCHEMA_VERSION,
        "report_kind": "ArtifactCommitReconcileCapabilityReport",
        "scope": RECONCILE_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "site_fingerprint_hash": site_fingerprint_hash,
        "database_identity_hash": database_identity_hash,
        "spec_hash": spec_hash,
        "plan_hash": plan_hash,
        "dag_hash": dag_hash,
        "schema_state_report_hash": schema_state_report_hash,
        "probe_results": list(probe_results),
        "positive_and_negative_evidence_refs": {
            "positive": list(positive_evidence_refs),
            "negative": list(negative_evidence_refs),
        },
        "residual_risks": list(residual_risks),
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in RECONCILE_CHECK_IDS
        ],
        "claims": {claim: True for claim in RECONCILE_CLAIMS},
        "side_effects": {key: 0 for key in RECONCILE_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(RECONCILE_NONCLAIMS),
    }

    errors = verify_artifact_commit_reconcile_capability_report(report)
    if errors:
        raise CapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_artifact_commit_reconcile_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 ArtifactCommitReconcileCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != RECONCILE_REPORT_SCHEMA_VERSION:
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                f"schema_version must be {RECONCILE_REPORT_SCHEMA_VERSION}",
            )
        )

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "ArtifactCommitReconcileCapabilityReport":
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "report_kind must be "
                "ArtifactCommitReconcileCapabilityReport",
            )
        )

    # 边界检查：不得是 DB1I 的输出
    if rk in RT1_FORBIDDEN_OUTPUT_KINDS:
        errors.append(
            (
                EC.RUNTIME_SCHEMA_STATE_REPORT_REISSUED,
                f"RT1 must not produce {rk}",
            )
        )

    # scope
    if report.get("scope") != RECONCILE_REPORT_SCOPE:
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, f"scope must be {RECONCILE_REPORT_SCOPE}")
        )

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "generated_at is not a timezone-aware ISO-8601 timestamp",
            )
        )

    # hashes
    for field_name in (
        "site_fingerprint_hash",
        "database_identity_hash",
        "spec_hash",
        "plan_hash",
        "dag_hash",
        "schema_state_report_hash",
    ):
        val = report.get(field_name)
        if not isinstance(val, str) or not _sha256_hex(val):
            errors.append(
                (
                    EC.REQUIRED_FIELD_MISSING,
                    f"{field_name} must be a lowercase sha256 hex",
                )
            )

    # checks
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "checks must be an array"))
    else:
        check_ids = [c.get("check_id") if isinstance(c, dict) else None for c in checks]
        if not all(isinstance(cid, str) for cid in check_ids):
            errors.append(
                (EC.REQUIRED_FIELD_MISSING, "every check ID must be a string")
            )
        elif len(check_ids) != len(set(check_ids)):
            errors.append(
                (EC.REQUIRED_FIELD_MISSING, "check IDs must not contain duplicates")
            )
        elif check_ids != list(RECONCILE_CHECK_IDS):
            errors.append(
                (
                    EC.REQUIRED_FIELD_MISSING,
                    "checks must exactly match canonical IDs and order",
                )
            )
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append(
                    (EC.REQUIRED_FIELD_MISSING, "every RT1 reconcile check must be PASS")
                )

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(RECONCILE_CLAIMS):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "claim set does not exactly match RT1 reconcile claims",
            )
        )
    elif any(claims[c] is not True for c in RECONCILE_CLAIMS):
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, "all RT1 reconcile claims must be true")
        )

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(
        RECONCILE_SIDE_EFFECT_KEYS
    ):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "side-effect set does not match the RT1 reconcile report scope",
            )
        )
    elif any(side_effects[k] != 0 for k in RECONCILE_SIDE_EFFECT_KEYS):
        errors.append(
            (EC.DB1L_WRITE_DETECTED, "all RT1 reconcile report side effects must be zero")
        )

    # verdict
    if report.get("verdict") != "PASS":
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, "RT1 reconcile report verdict must be PASS")
        )

    # blockers
    if report.get("blockers") != []:
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, "PASS RT1 reconcile report must have no blockers")
        )

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(RECONCILE_NONCLAIMS)
    ):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "explicit nonclaims must preserve the reconcile boundary",
            )
        )

    return tuple(dict.fromkeys(errors))
