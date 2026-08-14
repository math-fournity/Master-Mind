"""SolverCapabilityReport — SV1 能力报告（WP-SV1）。

SolverCapabilityReport 报告四种能力 kind（来自 CapabilityKindRegistry）：
- TARGET_SOLVER_HARNESS
- TARGET_SOLVER_NO_TOOL
- TARGET_SOLVER_SAFE_LAUNCH
- TARGET_SOLVER_ANSWER_ISOLATION

SV1 的完成输出严格限定为：
- SolverHarnessCapabilityReport
- SolverNoToolCapabilityReport
- SolverSafeLaunchReport
- SolverAnswerIsolationReport
- SolverLaunchReceipt

SV1 不得输出其他工作包的报告类型。

SIDE_EFFECT_FREE：纯计算，不接触真实 CLI / DB / D-volume。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ...contracts.errors import (
    SV_ALLOWED_OUTPUT_KINDS,
    SV_CAPABILITY_KINDS,
    SV_FORBIDDEN_OUTPUT_KINDS,
    VerificationErrorCode as EC,
)
from ...hashing import canonical_json_bytes, object_hash


SOLVER_REPORT_SCHEMA_VERSION = "sv1-solver-capability-report/v1"
SOLVER_REPORT_SCOPE = "TARGET_SOLVER_CAPABILITY_V1"

SOLVER_CHECK_IDS = (
    "sv1.solver.harness_adapter_isolated",
    "sv1.solver.notool_policy_enforced",
    "sv1.solver.safe_launch_verified",
    "sv1.solver.answer_isolation_verified",
    "sv1.solver.boundary_no_other_wp_reports",
)

SOLVER_CLAIMS = (
    "harness_adapter_is_only_solver_harness_caller",
    "notool_policy_enforced_no_tool_events",
    "safe_launch_verified_no_bypass_no_tool_events_trajectory_present",
    "answer_isolation_verified_answer_separate_from_trajectory",
    "does_not_produce_other_wp_reports",
)

SOLVER_NONCLAIMS = (
    "does_not_prove_live_solver_capability",
    "does_not_prove_model_role_capability",
    "does_not_prove_database_or_runtime_capability",
    "does_not_authorize_live_canary_or_solver_dispatch",
    "does_not_prove_harness_profile_qualified_for_production",
)

SOLVER_SIDE_EFFECT_KEYS = (
    "solver_launches",
    "database_writes",
    "redis_writes",
    "d_volume_writes",
    "model_live_calls",
    "subprocess_calls",
)


class SolverCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-SV1。"""


def _valid_generated_at(value: object) -> bool:
    if not isinstance(value, str) or any(c in value for c in "\r\n\x00"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _sha256_hex(value: str) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(c in "0123456789abcdef" for c in value)
    )


class SolverCapabilityReport:
    """SolverCapabilityReport — SV1 能力报告（dict-based，与 RT1 风格一致）。"""

    schema_id: str = "seven/sv1-solver-capability-report"
    schema_version: str = SOLVER_REPORT_SCHEMA_VERSION

    def __init__(self, report_dict: dict[str, Any]) -> None:
        self._dict = report_dict

    def to_dict(self) -> dict[str, Any]:
        return dict(self._dict)

    @property
    def report_kind(self) -> str:
        return self._dict.get("report_kind", "")

    @property
    def verdict(self) -> str:
        return self._dict.get("verdict", "")


def build_solver_capability_report(
    *,
    harness_profile_hash: str,
    notool_policy_hash: str,
    safe_launch_report_hash: str,
    answer_isolation_report_hash: str,
    dag_hash: str,
    probe_results: list[dict[str, Any]],
    positive_evidence_refs: list[str],
    negative_evidence_refs: list[str],
    residual_risks: list[str],
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 SolverCapabilityReport。"""
    report: dict[str, Any] = {
        "schema_version": SOLVER_REPORT_SCHEMA_VERSION,
        "report_kind": "SolverCapabilityReport",
        "scope": SOLVER_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "harness_profile_hash": harness_profile_hash,
        "notool_policy_hash": notool_policy_hash,
        "safe_launch_report_hash": safe_launch_report_hash,
        "answer_isolation_report_hash": answer_isolation_report_hash,
        "dag_hash": dag_hash,
        "capability_kinds": sorted(SV_CAPABILITY_KINDS),
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
            for cid in SOLVER_CHECK_IDS
        ],
        "claims": {claim: True for claim in SOLVER_CLAIMS},
        "side_effects": {key: 0 for key in SOLVER_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(SOLVER_NONCLAIMS),
    }

    errors = verify_solver_capability_report(report)
    if errors:
        raise SolverCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_solver_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 SolverCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != SOLVER_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {SOLVER_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "SolverCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be SolverCapabilityReport",
        ))

    # boundary check: must not be other WP's output
    if rk in SV_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.SV_OUTPUT_KIND_FORBIDDEN,
            f"SV1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != SOLVER_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {SOLVER_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # hashes
    for field_name in (
        "harness_profile_hash",
        "notool_policy_hash",
        "safe_launch_report_hash",
        "answer_isolation_report_hash",
        "dag_hash",
    ):
        val = report.get(field_name)
        if not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex",
            ))

    # capability_kinds
    cap_kinds = report.get("capability_kinds", [])
    if not isinstance(cap_kinds, list):
        errors.append((EC.SV_CAPABILITY_KIND_INVALID, "capability_kinds must be a list"))
    elif set(cap_kinds) != set(SV_CAPABILITY_KINDS):
        errors.append((
            EC.SV_CAPABILITY_KIND_INVALID,
            f"capability_kinds must exactly match SV_CAPABILITY_KINDS, "
            f"got {sorted(cap_kinds)}",
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
        elif check_ids != list(SOLVER_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every SV1 check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(SOLVER_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match SV1 claims"))
    elif any(claims[c] is not True for c in SOLVER_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all SV1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(SOLVER_SIDE_EFFECT_KEYS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the SV1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in SOLVER_SIDE_EFFECT_KEYS):
        errors.append((EC.SV_DIRECT_DEVIN_BYPASS, "all SV1 report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "SV1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS SV1 report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(SOLVER_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the SV1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
