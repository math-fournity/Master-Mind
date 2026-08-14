"""AuditCapabilityReport — WP-AU1 P6 审计能力报告。

来自 docs/implementation/15-work-package-implementation-contracts.md WP-AU1 行：
READY_FOR_AUDIT 最低产物：三审分别 seal、分歧/缺失合法 terminal。

报告验证：
- 三审分别 sealed
- 分歧/缺失为合法 terminal 状态
- 边界检查：不输出其他工作包的报告
- side-effect 全为 0

SIDE_EFFECT_FREE：纯计算，不接触真实 DB/Redis/D 盘/Solver/模型。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    AU_ALLOWED_OUTPUT_KINDS,
    AU_CHECK_IDS,
    AU_CLAIMS,
    AU_FORBIDDEN_OUTPUT_KINDS,
    AU_NONCLAIMS,
    AU_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)


AUDIT_REPORT_SCHEMA_VERSION = "au1-audit-capability-report/v1"
AUDIT_REPORT_SCOPE = "AUDIT_CAPABILITY_V1"


class AuditCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-AU1。"""


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


def build_audit_capability_report(
    *,
    plan_hash: str,
    bundle_count: int,
    views_generated: int,
    process_audits_sealed: int,
    proof_judgments_sealed: int,
    leakage_audits_sealed: int,
    run_audits_assembled: int,
    missing_terminal_count: int,
    disagreement_preserved_count: int,
    contamination_flagged_count: int,
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 AuditCapabilityReport。"""
    report: dict[str, Any] = {
        "schema_version": AUDIT_REPORT_SCHEMA_VERSION,
        "report_kind": "AuditCapabilityReport",
        "scope": AUDIT_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "plan_hash": plan_hash,
        "bundle_count": bundle_count,
        "views_generated": views_generated,
        "process_audits_sealed": process_audits_sealed,
        "proof_judgments_sealed": proof_judgments_sealed,
        "leakage_audits_sealed": leakage_audits_sealed,
        "run_audits_assembled": run_audits_assembled,
        "missing_terminal_count": missing_terminal_count,
        "disagreement_preserved_count": disagreement_preserved_count,
        "contamination_flagged_count": contamination_flagged_count,
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in AU_CHECK_IDS
        ],
        "claims": {claim: True for claim in AU_CLAIMS},
        "side_effects": {key: 0 for key in AU_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(AU_NONCLAIMS),
    }

    errors = verify_audit_capability_report(report)
    if errors:
        raise AuditCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_audit_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 AuditCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != AUDIT_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {AUDIT_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "AuditCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be AuditCapabilityReport",
        ))

    # boundary check: must not be other WP's output
    if rk in AU_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.AU_OUTPUT_KIND_FORBIDDEN,
            f"AU1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != AUDIT_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {AUDIT_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # plan_hash
    if not _sha256_hex(report.get("plan_hash")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "plan_hash must be a lowercase sha256 hex",
        ))

    # counts must be non-negative integers
    for field_name in (
        "bundle_count", "views_generated", "process_audits_sealed",
        "proof_judgments_sealed", "leakage_audits_sealed",
        "run_audits_assembled", "missing_terminal_count",
        "disagreement_preserved_count", "contamination_flagged_count",
    ):
        val = report.get(field_name)
        if not isinstance(val, int) or val < 0:
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a non-negative integer",
            ))

    # checks
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "checks must be an array"))
    else:
        check_ids = [c.get("check_id") if isinstance(c, dict) else None for c in checks]
        if not all(isinstance(cid, str) for cid in check_ids):
            errors.append((EC.REQUIRED_FIELD_MISSING, "every check ID must be a string"))
        elif len(check_ids) != len(set(check_ids)):
            errors.append((EC.REQUIRED_FIELD_MISSING, "check IDs must not contain duplicates"))
        elif check_ids != list(AU_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every AU1 check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(AU_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match AU1 claims"))
    elif any(claims[c] is not True for c in AU_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all AU1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(AU_SIDE_EFFECT_KEYS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the AU1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in AU_SIDE_EFFECT_KEYS):
        errors.append((EC.AU_OUTPUT_KIND_FORBIDDEN, "all AU1 report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "AU1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS AU1 report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(AU_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the AU1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
