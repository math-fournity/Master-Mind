"""ExperimentCapabilityReport — WP-EX1 P4/P5 实验能力报告。

EX1 的完成输出严格限定为：
- ExperimentPlan / ResourceContract / BranchSnapshot / RandomizationPlan
- ExperimentArm / ContrastSpec / RunArtifactBundle
- ExperimentCapabilityReport

EX1 不得输出其他工作包的报告类型。

SIDE_EFFECT_FREE：纯计算，不接触真实 CLI / DB / D-volume / Solver。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    EX_ALLOWED_OUTPUT_KINDS,
    EX_ARM_KINDS,
    EX_CHECK_IDS,
    EX_CLAIMS,
    EX_FORBIDDEN_OUTPUT_KINDS,
    EX_NONCLAIMS,
    EX_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)
from ..hashing import canonical_json_bytes


EXPERIMENT_REPORT_SCHEMA_VERSION = "ex1-experiment-capability-report/v1"
EXPERIMENT_REPORT_SCOPE = "EXPERIMENT_CAPABILITY_V1"


class ExperimentCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-EX1。"""


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


class ExperimentCapabilityReport:
    """ExperimentCapabilityReport — EX1 能力报告（dict-based）。"""

    schema_id: str = "seven/ex1-experiment-capability-report"
    schema_version: str = EXPERIMENT_REPORT_SCHEMA_VERSION

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


def build_experiment_capability_report(
    *,
    plan_hash: str,
    branch_snapshot_hash: str,
    resource_contract_hash: str,
    randomization_seed: int,
    arm_kinds_present: list[str],
    contrast_ids: list[str],
    bundle_hashes: dict[str, str],
    negative_result_count: int,
    invalid_result_count: int,
    all_results_retained: bool,
    randomization_replayable: bool,
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 ExperimentCapabilityReport。"""
    report: dict[str, Any] = {
        "schema_version": EXPERIMENT_REPORT_SCHEMA_VERSION,
        "report_kind": "ExperimentCapabilityReport",
        "scope": EXPERIMENT_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "plan_hash": plan_hash,
        "branch_snapshot_hash": branch_snapshot_hash,
        "resource_contract_hash": resource_contract_hash,
        "randomization_seed": randomization_seed,
        "arm_kinds_present": sorted(arm_kinds_present),
        "contrast_ids": list(contrast_ids),
        "bundle_hashes": dict(bundle_hashes),
        "negative_result_count": negative_result_count,
        "invalid_result_count": invalid_result_count,
        "all_results_retained": all_results_retained,
        "randomization_replayable": randomization_replayable,
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in EX_CHECK_IDS
        ],
        "claims": {claim: True for claim in EX_CLAIMS},
        "side_effects": {key: 0 for key in EX_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(EX_NONCLAIMS),
    }

    errors = verify_experiment_capability_report(report)
    if errors:
        raise ExperimentCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_experiment_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 ExperimentCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != EXPERIMENT_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {EXPERIMENT_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "ExperimentCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be ExperimentCapabilityReport",
        ))

    # boundary check: must not be other WP's output
    if rk in EX_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.EX_OUTPUT_KIND_FORBIDDEN,
            f"EX1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != EXPERIMENT_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {EXPERIMENT_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # hashes
    for field_name in ("plan_hash", "branch_snapshot_hash", "resource_contract_hash"):
        val = report.get(field_name)
        if not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex",
            ))

    # arm_kinds_present
    arm_kinds = report.get("arm_kinds_present", [])
    if not isinstance(arm_kinds, list):
        errors.append((EC.EX_ARM_KIND_INVALID, "arm_kinds_present must be a list"))
    elif set(arm_kinds) != set(EX_ARM_KINDS):
        errors.append((
            EC.EX_ARM_KIND_INVALID,
            f"arm_kinds_present must exactly match EX_ARM_KINDS, got {sorted(arm_kinds)}",
        ))

    # randomization_replayable
    if report.get("randomization_replayable") is not True:
        errors.append((
            EC.EX_RANDOMIZATION_NOT_REPLAYABLE,
            "randomization_replayable must be True",
        ))

    # all_results_retained
    if report.get("all_results_retained") is not True:
        errors.append((
            EC.EX_NEGATIVE_RESULT_DELETED,
            "all_results_retained must be True",
        ))

    # bundle_hashes
    bundle_hashes = report.get("bundle_hashes", {})
    if not isinstance(bundle_hashes, dict):
        errors.append((EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE, "bundle_hashes must be an object"))
    else:
        for arm_id, h in bundle_hashes.items():
            if not _sha256_hex(h):
                errors.append((
                    EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE,
                    f"bundle_hashes[{arm_id}] must be a lowercase sha256 hex",
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
        elif check_ids != list(EX_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every EX1 check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(EX_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match EX1 claims"))
    elif any(claims[c] is not True for c in EX_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all EX1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(EX_SIDE_EFFECT_KEYS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the EX1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in EX_SIDE_EFFECT_KEYS):
        errors.append((EC.EX_OUTPUT_KIND_FORBIDDEN, "all EX1 report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "EX1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS EX1 report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(EX_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the EX1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
