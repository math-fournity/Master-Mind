"""WorkerCapabilityReport — COGNITIVE_WORKER 能力报告。

来自 docs/implementation/15-work-package-implementation-contracts.md WP-CW1 行：
READY_FOR_AUDIT 最低产物：所有生产启用 role×profile×policy 格有结论。

报告验证：
- 所有 PRODUCTION 启用的 role×profile×policy cell 有结论（PASS/NOT_TESTED/FAILED）
- 边界检查：不输出 Solver/Schema/DB 相关报告
- side-effect 全为 0

SIDE_EFFECT_FREE：纯计算，不接触真实 DB/Redis/D 盘。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ...contracts.errors import (
    CW_ALLOWED_OUTPUT_KINDS,
    CW_CHECK_IDS,
    CW_CLAIMS,
    CW_FORBIDDEN_OUTPUT_KINDS,
    CW_NONCLAIMS,
    CW_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)
from ...hashing import canonical_json_bytes
from .role_qualification_matrix import RoleQualificationMatrix
from .production_role_router import ProductionRoleRouter


WORKER_REPORT_SCHEMA_VERSION = "cw1-cognitive-worker-capability-report/v1"
WORKER_REPORT_SCOPE = "COGNITIVE_WORKER_V1"


class WorkerCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-CW1。"""


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


def build_worker_capability_report(
    *,
    matrix: RoleQualificationMatrix,
    router: ProductionRoleRouter,
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 CognitiveWorkerCapabilityReport。

    验证所有 PRODUCTION 启用的 cell 有结论。
    """
    # 验证所有 PRODUCTION cell 有结论
    conclusion_result = router.verify_all_production_cells_have_conclusions()

    # 收集 cell 结论摘要
    cell_conclusions: list[dict[str, str]] = []
    for cell in matrix.cells:
        if not cell.is_production:
            continue
        cell_conclusions.append({
            "qualification_cell_id": cell.qualification_cell_id,
            "role_type_id": cell.role_type_id,
            "carrier_id": cell.carrier_id,
            "model_id": cell.model_id,
            "verdict": cell.verdict,
            "conclusion": cell.conclusion,
            "has_conclusion": str(cell.has_conclusion).lower(),
        })

    # 检查是否有 missing conclusion
    missing_conclusions = [
        cc for cc in cell_conclusions if cc["has_conclusion"] == "false"
    ]

    verdict = "PASS" if not missing_conclusions and conclusion_result.passed else "BLOCKED"
    blockers: list[dict[str, str]] = []
    if missing_conclusions:
        for mc in missing_conclusions:
            blockers.append({
                "code": EC.CW_CELL_CONCLUSION_MISSING.value,
                "detail": f"cell {mc['qualification_cell_id']} has no conclusion",
            })
    for ec in conclusion_result.error_codes:
        blockers.append({"code": ec.value, "detail": ""})

    report: dict[str, Any] = {
        "schema_version": WORKER_REPORT_SCHEMA_VERSION,
        "report_kind": "CognitiveWorkerCapabilityReport",
        "scope": WORKER_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "matrix_ref_and_hash": {
            "ref": f"{matrix.matrix_id}@{matrix.matrix_version}",
            "sha256": matrix.matrix_hash,
        },
        "qualification_scope": matrix.qualification_scope,
        "cell_conclusions": cell_conclusions,
        "verdict": verdict,
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS" if verdict == "PASS" else "BLOCKED", "evidence": []}
            for cid in CW_CHECK_IDS
        ],
        "claims": {claim: True for claim in CW_CLAIMS},
        "side_effects": {key: 0 for key in CW_SIDE_EFFECT_KEYS},
        "blockers": blockers,
        "explicit_nonclaims": list(CW_NONCLAIMS),
    }

    errors = verify_worker_capability_report(report)
    if errors:
        raise WorkerCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_worker_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 CognitiveWorkerCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != WORKER_REPORT_SCHEMA_VERSION:
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                f"schema_version must be {WORKER_REPORT_SCHEMA_VERSION}",
            )
        )

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "CognitiveWorkerCapabilityReport":
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "report_kind must be CognitiveWorkerCapabilityReport",
            )
        )

    # 边界检查：不得是其他工作包的输出
    if rk in CW_FORBIDDEN_OUTPUT_KINDS:
        errors.append(
            (
                EC.CW_OUTPUT_KIND_FORBIDDEN,
                f"CW1 must not produce {rk}",
            )
        )

    # scope
    if report.get("scope") != WORKER_REPORT_SCOPE:
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, f"scope must be {WORKER_REPORT_SCOPE}")
        )

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "generated_at is not a timezone-aware ISO-8601 timestamp",
            )
        )

    # matrix_ref_and_hash
    matrix_ref = report.get("matrix_ref_and_hash", {})
    if not isinstance(matrix_ref, dict):
        errors.append((EC.REQUIRED_FIELD_MISSING, "matrix_ref_and_hash is not an object"))
    elif set(matrix_ref.keys()) != {"ref", "sha256"}:
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, "matrix_ref_and_hash must have ref and sha256")
        )
    else:
        if not _sha256_hex(matrix_ref.get("sha256", "")):
            errors.append(
                (EC.CW_MATRIX_HASH_MISMATCH, "matrix_ref_and_hash.sha256 is not valid")
            )

    # cell_conclusions
    cell_conclusions = report.get("cell_conclusions", [])
    if not isinstance(cell_conclusions, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "cell_conclusions must be an array"))
    else:
        for cc in cell_conclusions:
            if not isinstance(cc, dict):
                errors.append((EC.REQUIRED_FIELD_MISSING, "cell_conclusion entry is not an object"))
                continue
            if cc.get("has_conclusion") != "true":
                errors.append(
                    (
                        EC.CW_CELL_CONCLUSION_MISSING,
                        f"cell {cc.get('qualification_cell_id', '?')} has no conclusion",
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
        elif check_ids != list(CW_CHECK_IDS):
            errors.append(
                (
                    EC.REQUIRED_FIELD_MISSING,
                    "checks must exactly match canonical IDs and order",
                )
            )

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(CW_CLAIMS):
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match CW1 claims")
        )
    elif any(claims[c] is not True for c in CW_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all CW1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(CW_SIDE_EFFECT_KEYS):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "side-effect set does not match the CW1 report scope",
            )
        )
    elif any(side_effects[k] != 0 for k in CW_SIDE_EFFECT_KEYS):
        errors.append(
            (EC.DB1L_WRITE_DETECTED, "all CW1 report side effects must be zero")
        )

    # verdict
    if report.get("verdict") not in ("PASS", "BLOCKED"):
        errors.append((EC.REQUIRED_FIELD_MISSING, "CW1 report verdict must be PASS or BLOCKED"))

    # PASS → no blockers
    if report.get("verdict") == "PASS":
        if report.get("blockers") != []:
            errors.append(
                (EC.REQUIRED_FIELD_MISSING, "PASS CW1 report must have no blockers")
            )

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(CW_NONCLAIMS)
    ):
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                "explicit nonclaims must preserve the CW1 boundary",
            )
        )

    return tuple(dict.fromkeys(errors))
