"""P8 边界检查——P8 不得读取/生成 EvidenceIndex 或其他阶段产物。

来自 docs/implementation/15-work-package-implementation-contracts.md WP-RV1：

blocker与故障验收: 读取尚未生成的最终EvidenceIndex

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    RV_FORBIDDEN_OUTPUT_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


def check_no_evidence_index_in_p8(outputs: dict[str, Any]) -> VerificationResult:
    """检查 P8 输出中不含 EvidenceIndex。"""
    errors: list[EC] = []
    details: list[str] = []

    for key, value in outputs.items():
        kind = ""
        if isinstance(value, dict):
            kind = value.get("report_kind", value.get("schema_id", ""))
        if not kind:
            kind = key
        if kind.startswith("seven/"):
            kind = kind.split("/")[-1]
        if kind == "EvidenceIndex" or key == "EvidenceIndex":
            errors.append(EC.RV_EVIDENCE_INDEX_READ_IN_P8)
            details.append("EvidenceIndex read/generated in P8 — only P9 generates it")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_p8_output_boundary(outputs: dict[str, Any]) -> VerificationResult:
    """检查 P8 输出边界——只允许 RV_ALLOWED_OUTPUT_KINDS，禁止 RV_FORBIDDEN_OUTPUT_KINDS。"""
    errors: list[EC] = []
    details: list[str] = []

    for key, value in outputs.items():
        kind = ""
        if isinstance(value, dict):
            kind = value.get("report_kind", value.get("schema_id", ""))
        if not kind:
            kind = key
        if kind.startswith("seven/"):
            kind = kind.split("/")[-1]
        if kind in RV_FORBIDDEN_OUTPUT_KINDS:
            errors.append(EC.RV_OUTPUT_KIND_FORBIDDEN)
            details.append(f"P8 must not produce {kind}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
