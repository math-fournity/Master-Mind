"""VerdictCapabilityReport — P9 verdict 能力报告。

来自 docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

READY_FOR_AUDIT最低产物: factory/scientific/scale分轴Verdict、
completion-contract remainder=0、全链remainder=0

关键约束（blocker）：
- factory/scientific/scale 分轴 Verdict
- completion-contract remainder=0
- full chain remainder=0
- SIDE_EFFECT_FREE：所有 side-effect 键为 0

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    VR_CHECK_IDS,
    VR_CLAIMS,
    VR_FORBIDDEN_OUTPUT_KINDS,
    VR_NONCLAIMS,
    VR_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)


VERDICT_REPORT_SCHEMA_VERSION = "vr1-verdict-capability-report/v1"
VERDICT_REPORT_SCOPE = "VERDICT_CAPABILITY_V1"


class VerdictCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-VR1。"""


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


def build_verdict_capability_report(
    *,
    dag_hash: str,
    verdict_hash: str,
    gate_verdict_hash: str,
    evidence_index_hash: str,
    replay_hash: str,
    completion_remainder_hash: str,
    full_chain_remainder_hash: str,
    cost_coverage_delta_hash: str,
    summary_hash: str,
    checkpoint_hash: str,
    registry_hash: str,
    factory_axis_independent: bool,
    scientific_axis_independent: bool,
    scale_axis_independent: bool,
    no_pass_averaged_fail: bool,
    not_tested_not_pass: bool,
    six_gates_independent: bool,
    evidence_index_in_p9_only: bool,
    evidence_retraceable: bool,
    checkpoint_hash_bound: bool,
    all_objects_placed: bool,
    no_orphans: bool,
    no_duplicates: bool,
    no_missing: bool,
    completion_contract_remainder_zero: bool,
    full_chain_remainder_zero: bool,
    verdict_rule_registry_fail_closed: bool,
    cost_delta_complete: bool,
    coverage_delta_complete: bool,
    summary_valid: bool,
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 VerdictCapabilityReport。

    READY_FOR_AUDIT 最低产物：factory/scientific/scale 分轴 Verdict、
    completion-contract remainder=0、全链 remainder=0。
    """
    report: dict[str, Any] = {
        "schema_version": VERDICT_REPORT_SCHEMA_VERSION,
        "report_kind": "VerdictCapabilityReport",
        "scope": VERDICT_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "dag_hash": dag_hash,
        "verdict_hash": verdict_hash,
        "gate_verdict_hash": gate_verdict_hash,
        "evidence_index_hash": evidence_index_hash,
        "replay_hash": replay_hash,
        "completion_remainder_hash": completion_remainder_hash,
        "full_chain_remainder_hash": full_chain_remainder_hash,
        "cost_coverage_delta_hash": cost_coverage_delta_hash,
        "summary_hash": summary_hash,
        "checkpoint_hash": checkpoint_hash,
        "registry_hash": registry_hash,
        "factory_axis_independent": factory_axis_independent,
        "scientific_axis_independent": scientific_axis_independent,
        "scale_axis_independent": scale_axis_independent,
        "no_pass_averaged_fail": no_pass_averaged_fail,
        "not_tested_not_pass": not_tested_not_pass,
        "six_gates_independent": six_gates_independent,
        "evidence_index_in_p9_only": evidence_index_in_p9_only,
        "evidence_retraceable": evidence_retraceable,
        "checkpoint_hash_bound": checkpoint_hash_bound,
        "all_objects_placed": all_objects_placed,
        "no_orphans": no_orphans,
        "no_duplicates": no_duplicates,
        "no_missing": no_missing,
        "completion_contract_remainder_zero": completion_contract_remainder_zero,
        "full_chain_remainder_zero": full_chain_remainder_zero,
        "verdict_rule_registry_fail_closed": verdict_rule_registry_fail_closed,
        "cost_delta_complete": cost_delta_complete,
        "coverage_delta_complete": coverage_delta_complete,
        "summary_valid": summary_valid,
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in VR_CHECK_IDS
        ],
        "claims": {claim: True for claim in VR_CLAIMS},
        "side_effects": {key: 0 for key in VR_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(VR_NONCLAIMS),
    }

    errors = verify_verdict_capability_report(report)
    if errors:
        raise VerdictCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_verdict_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 VerdictCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != VERDICT_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {VERDICT_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "VerdictCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be VerdictCapabilityReport",
        ))

    # boundary check
    if rk in VR_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.VR_OUTPUT_KIND_FORBIDDEN,
            f"VR1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != VERDICT_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {VERDICT_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # hashes
    for field_name in (
        "dag_hash", "verdict_hash", "gate_verdict_hash",
        "evidence_index_hash", "replay_hash",
        "completion_remainder_hash", "full_chain_remainder_hash",
        "cost_coverage_delta_hash", "summary_hash",
        "checkpoint_hash", "registry_hash",
    ):
        val = report.get(field_name)
        if not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex",
            ))

    # constraint flags
    flag_map = {
        "factory_axis_independent": EC.VR_AXIS_NOT_INDEPENDENT,
        "scientific_axis_independent": EC.VR_AXIS_NOT_INDEPENDENT,
        "scale_axis_independent": EC.VR_AXIS_NOT_INDEPENDENT,
        "no_pass_averaged_fail": EC.VR_PASS_AVERAGED_FAIL,
        "not_tested_not_pass": EC.VR_NOT_TESTED_AS_PASS,
        "six_gates_independent": EC.VR_GATE_NOT_INDEPENDENT,
        "evidence_index_in_p9_only": EC.VR_EVIDENCE_INDEX_BEFORE_P9,
        "evidence_retraceable": EC.VR_NON_RETRACEABLE,
        "checkpoint_hash_bound": EC.VR_CHECKPOINT_HASH_MISMATCH,
        "all_objects_placed": EC.VR_REPLAY_INCOMPLETE,
        "no_orphans": EC.VR_ORPHAN_OBJECT,
        "no_duplicates": EC.VR_DUPLICATE_OBJECT,
        "no_missing": EC.VR_MISSING_OBJECT,
        "completion_contract_remainder_zero": (
            EC.VR_COMPLETION_CONTRACT_REMAINDER_NONZERO
        ),
        "full_chain_remainder_zero": EC.VR_FULL_CHAIN_REMAINDER_NONZERO,
        "verdict_rule_registry_fail_closed": (
            EC.VR_VERDICT_RULE_UNKNOWN_NOT_FAIL_CLOSED
        ),
        "cost_delta_complete": EC.VR_COST_DELTA_INCOMPLETE,
        "coverage_delta_complete": EC.VR_COVERAGE_DELTA_INCOMPLETE,
        "summary_valid": EC.VR_SUMMARY_INVALID,
    }
    for flag_name, code in flag_map.items():
        if report.get(flag_name) is not True:
            errors.append((code, f"{flag_name} must be True"))

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
        elif check_ids != list(VR_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every VR1 check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(VR_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match VR1 claims"))
    elif any(claims[c] is not True for c in VR_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all VR1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(VR_SIDE_EFFECT_KEYS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the VR1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in VR_SIDE_EFFECT_KEYS):
        errors.append((EC.VR_OUTPUT_KIND_FORBIDDEN, "all VR1 report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "VR1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS VR1 report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(VR_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the VR1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
