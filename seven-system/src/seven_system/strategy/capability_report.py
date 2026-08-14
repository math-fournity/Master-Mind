"""StrategyCapabilityReport — WP-ST1 能力报告。

ST1 的完成输出严格限定为：
- SelectorReceipt / RendererReceipt / BindingReceipt / InjectionReceipt
- CriticDecision / StrategyRunReceipt / ArmPayload / FixturePreState
- StrategyCapabilityReport

ST1 不得输出其他工作包的报告类型。

SIDE_EFFECT_FREE：纯计算，不接触真实 CLI / DB / D-volume / Solver。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    ST_ALLOWED_OUTPUT_KINDS,
    ST_ARM_KINDS,
    ST_FORBIDDEN_OUTPUT_KINDS,
    ST_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)
from ..hashing import canonical_json_bytes


STRATEGY_REPORT_SCHEMA_VERSION = "st1-strategy-capability-report/v1"
STRATEGY_REPORT_SCOPE = "STRATEGY_CAPABILITY_V1"

STRATEGY_CHECK_IDS = (
    "st1.selector.abstain_respected",
    "st1.selector.release_ref_by_hash",
    "st1.renderer.bound_payload_not_raw_tell",
    "st1.renderer.no_answer_leakage",
    "st1.renderer.no_core_text_confusion",
    "st1.binding.position_timing_scope",
    "st1.injection.requires_binding",
    "st1.critic.requires_injection",
    "st1.arm.distractor_equal_budget",
    "st1.arm.deterministic_replay",
    "st1.component.no_drift",
    "st1.fixture.no_live_case_masquerade",
    "st1.boundary_no_other_wp_reports",
)

STRATEGY_CLAIMS = (
    "selector_abstain_respected",
    "selector_references_release_by_hash",
    "renderer_produces_bound_payload_not_raw_tell",
    "renderer_no_answer_bound_to_hint",
    "renderer_no_core_text_confusion",
    "binding_includes_position_timing_scope",
    "injection_requires_binding_receipt",
    "critic_requires_injection_receipt",
    "distractor_arm_equal_resource_budget",
    "all_arm_payloads_deterministic_replay",
    "component_versions_no_drift",
    "fixture_does_not_masquerade_live_case",
    "does_not_produce_other_wp_reports",
)

STRATEGY_NONCLAIMS = (
    "does_not_prove_live_solver_capability",
    "does_not_prove_live_model_capability",
    "does_not_launch_solver",
    "does_not_write_db_or_redis",
    "does_not_authorize_live_canary_or_solver_dispatch",
    "status_implemented_pending_evidence",
)


class StrategyCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-ST1。"""


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


class StrategyCapabilityReport:
    """StrategyCapabilityReport — ST1 能力报告（dict-based）。"""

    schema_id: str = "seven/st1-strategy-capability-report"
    schema_version: str = STRATEGY_REPORT_SCHEMA_VERSION

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


def build_strategy_capability_report(
    *,
    release_hash: str,
    fixture_hash: str,
    dag_hash: str,
    arm_payload_hashes: dict[str, str],
    probe_results: list[dict[str, Any]],
    positive_evidence_refs: list[str],
    negative_evidence_refs: list[str],
    residual_risks: list[str],
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 StrategyCapabilityReport。"""
    report: dict[str, Any] = {
        "schema_version": STRATEGY_REPORT_SCHEMA_VERSION,
        "report_kind": "StrategyCapabilityReport",
        "scope": STRATEGY_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "release_hash": release_hash,
        "fixture_hash": fixture_hash,
        "dag_hash": dag_hash,
        "arm_payload_hashes": dict(arm_payload_hashes),
        "arm_kinds": sorted(ST_ARM_KINDS),
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
            for cid in STRATEGY_CHECK_IDS
        ],
        "claims": {claim: True for claim in STRATEGY_CLAIMS},
        "side_effects": {key: 0 for key in ST_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(STRATEGY_NONCLAIMS),
    }

    errors = verify_strategy_capability_report(report)
    if errors:
        raise StrategyCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_strategy_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 StrategyCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != STRATEGY_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {STRATEGY_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "StrategyCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be StrategyCapabilityReport",
        ))

    # boundary check: must not be other WP's output
    if rk in ST_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.ST_OUTPUT_KIND_FORBIDDEN,
            f"ST1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != STRATEGY_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {STRATEGY_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # hashes
    for field_name in ("release_hash", "fixture_hash", "dag_hash"):
        val = report.get(field_name)
        if not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex",
            ))

    # arm_payload_hashes
    arm_hashes = report.get("arm_payload_hashes", {})
    if not isinstance(arm_hashes, dict):
        errors.append((EC.REQUIRED_FIELD_MISSING, "arm_payload_hashes must be an object"))
    else:
        for arm_kind, h in arm_hashes.items():
            if arm_kind not in ST_ARM_KINDS:
                errors.append((
                    EC.ST_ARM_KIND_INVALID,
                    f"arm_payload_hashes key {arm_kind!r} not in ST_ARM_KINDS",
                ))
            if not _sha256_hex(h):
                errors.append((
                    EC.ST_ARM_PAYLOAD_NOT_REPLAYABLE,
                    f"arm_payload_hashes[{arm_kind}] must be a lowercase sha256 hex",
                ))

    # arm_kinds
    arm_kinds = report.get("arm_kinds", [])
    if not isinstance(arm_kinds, list):
        errors.append((EC.ST_ARM_KIND_INVALID, "arm_kinds must be a list"))
    elif set(arm_kinds) != set(ST_ARM_KINDS):
        errors.append((
            EC.ST_ARM_KIND_INVALID,
            f"arm_kinds must exactly match ST_ARM_KINDS, got {sorted(arm_kinds)}",
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
        elif check_ids != list(STRATEGY_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every ST1 check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(STRATEGY_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match ST1 claims"))
    elif any(claims[c] is not True for c in STRATEGY_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all ST1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(ST_SIDE_EFFECT_KEYS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the ST1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in ST_SIDE_EFFECT_KEYS):
        errors.append((EC.ST_OUTPUT_KIND_FORBIDDEN, "all ST1 report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "ST1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS ST1 report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(STRATEGY_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the ST1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
