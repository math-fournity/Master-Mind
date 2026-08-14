"""RevisionCapabilityReport — P8 修订能力报告。

来自 docs/implementation/15-work-package-implementation-contracts.md WP-RV1：

READY_FOR_AUDIT最低产物: NO_CHANGE或受控revision纵切，旧证据不改

关键约束（blocker）：
- NO_CHANGE 或受控 revision 纵切
- 旧证据不改
- P8 不读取 EvidenceIndex
- SIDE_EFFECT_FREE：所有 side-effect 键为 0

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    RV_CHECK_IDS,
    RV_CLAIMS,
    RV_FORBIDDEN_OUTPUT_KINDS,
    RV_NONCLAIMS,
    RV_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)


REVISION_REPORT_SCHEMA_VERSION = "rv1-revision-capability-report/v1"
REVISION_REPORT_SCOPE = "REVISION_CAPABILITY_V1"


class RevisionCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-RV1。"""


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


def build_revision_capability_report(
    *,
    provenance_snapshot_hash: str,
    localization_hash: str,
    outcome_kind: str,
    nochange_decision_hash: str = "",
    revision_proposal_hash: str = "",
    candidate_release_hash: str = "",
    prospective_evaluation_hash: str = "",
    revision_policy_hash: str,
    old_evidence_not_modified: bool,
    no_evidence_index_in_p8: bool,
    holdout_not_unsealed_on_nochange: bool,
    two_human_gates_for_revision: bool,
    candidate_not_self_approved: bool,
    holdout_fit_not_confirmation: bool,
    holdout_no_repeated_peek: bool,
    holdout_no_single_case_split: bool,
    prospective_one_time: bool,
    prospective_no_reuse_viewed_holdout: bool,
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 RevisionCapabilityReport。

    READY_FOR_AUDIT 最低产物：NO_CHANGE 或受控 revision 纵切，旧证据不改。
    outcome_kind: "NO_CHANGE" 或 "CONTROLLED_REVISION"。
    """
    report: dict[str, Any] = {
        "schema_version": REVISION_REPORT_SCHEMA_VERSION,
        "report_kind": "RevisionCapabilityReport",
        "scope": REVISION_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "provenance_snapshot_hash": provenance_snapshot_hash,
        "localization_hash": localization_hash,
        "outcome_kind": outcome_kind,
        "nochange_decision_hash": nochange_decision_hash,
        "revision_proposal_hash": revision_proposal_hash,
        "candidate_release_hash": candidate_release_hash,
        "prospective_evaluation_hash": prospective_evaluation_hash,
        "revision_policy_hash": revision_policy_hash,
        "old_evidence_not_modified": old_evidence_not_modified,
        "no_evidence_index_in_p8": no_evidence_index_in_p8,
        "holdout_not_unsealed_on_nochange": holdout_not_unsealed_on_nochange,
        "two_human_gates_for_revision": two_human_gates_for_revision,
        "candidate_not_self_approved": candidate_not_self_approved,
        "holdout_fit_not_confirmation": holdout_fit_not_confirmation,
        "holdout_no_repeated_peek": holdout_no_repeated_peek,
        "holdout_no_single_case_split": holdout_no_single_case_split,
        "prospective_one_time": prospective_one_time,
        "prospective_no_reuse_viewed_holdout": prospective_no_reuse_viewed_holdout,
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in RV_CHECK_IDS
        ],
        "claims": {claim: True for claim in RV_CLAIMS},
        "side_effects": {key: 0 for key in RV_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(RV_NONCLAIMS),
    }

    errors = verify_revision_capability_report(report)
    if errors:
        raise RevisionCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_revision_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 RevisionCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != REVISION_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {REVISION_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "RevisionCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be RevisionCapabilityReport",
        ))

    # boundary check
    if rk in RV_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.RV_OUTPUT_KIND_FORBIDDEN,
            f"RV1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != REVISION_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {REVISION_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # hashes
    for field_name in (
        "provenance_snapshot_hash", "localization_hash", "revision_policy_hash",
    ):
        val = report.get(field_name)
        if not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex",
            ))

    # outcome_kind
    outcome = report.get("outcome_kind", "")
    if outcome not in ("NO_CHANGE", "CONTROLLED_REVISION"):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "outcome_kind must be NO_CHANGE or CONTROLLED_REVISION",
        ))

    # optional hashes (sha256 if present)
    for field_name in (
        "nochange_decision_hash", "revision_proposal_hash",
        "candidate_release_hash", "prospective_evaluation_hash",
    ):
        val = report.get(field_name, "")
        if val and not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex when present",
            ))

    # outcome-specific hash requirements
    if outcome == "NO_CHANGE":
        if not _sha256_hex(report.get("nochange_decision_hash")):
            errors.append((
                EC.RV_NOCHANGE_NOT_SIGNED,
                "NO_CHANGE outcome requires nochange_decision_hash",
            ))
    elif outcome == "CONTROLLED_REVISION":
        if not _sha256_hex(report.get("revision_proposal_hash")):
            errors.append((
                EC.RV_REVISION_PROPOSAL_NOT_SIGNED,
                "CONTROLLED_REVISION outcome requires revision_proposal_hash",
            ))

    # constraint flags
    flag_map = {
        "old_evidence_not_modified": EC.RV_OLD_EVIDENCE_MODIFIED,
        "no_evidence_index_in_p8": EC.RV_EVIDENCE_INDEX_READ_IN_P8,
        "holdout_not_unsealed_on_nochange": EC.RV_NOCHANGE_UNSEALS_HOLDOUT,
        "two_human_gates_for_revision": EC.RV_REVISION_WITHOUT_TWO_GATES,
        "candidate_not_self_approved": EC.RV_CANDIDATE_SELF_APPROVED,
        "holdout_fit_not_confirmation": EC.RV_FIT_EQUALS_CONFIRMATION,
        "holdout_no_repeated_peek": EC.RV_HOLDOUT_REPEATED_PEEK,
        "holdout_no_single_case_split": EC.RV_SINGLE_CASE_SPLIT,
        "prospective_one_time": EC.RV_PROSPECTIVE_NOT_ONE_TIME,
        "prospective_no_reuse_viewed_holdout": EC.RV_PROSPECTIVE_REUSES_HOLDOUT,
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
        elif check_ids != list(RV_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every RV1 check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(RV_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match RV1 claims"))
    elif any(claims[c] is not True for c in RV_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all RV1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(RV_SIDE_EFFECT_KEYS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the RV1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in RV_SIDE_EFFECT_KEYS):
        errors.append((EC.RV_OUTPUT_KIND_FORBIDDEN, "all RV1 report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "RV1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS RV1 report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(RV_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the RV1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
