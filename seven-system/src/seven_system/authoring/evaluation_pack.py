"""AuthoringEvaluationPack — 冻结的评估包。

来自 docs/implementation/04-object-and-schema-catalog.md：

AuthoringEvaluationPack 定义：
- frozen calibration/qualification use
- brief/cell set
- blinding（作者身份隐去）
- metrics
- stop conditions
- forbidden downstream lane flow

冻结对象，不可修改。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    QA_BAKEOFF_A_METRICS,
    QA_BAKEOFF_A_FORBIDDEN_METRICS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/authoring-evaluation-pack"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AuthoringEvaluationPack"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class AuthoringEvaluationPack:
    """AuthoringEvaluationPack — 冻结的评估包。不可变。

    用于 Bakeoff-A 校准/资格评估。
    blinding=True 时作者身份隐去。
    """

    pack_id: str
    calibration_use: str
    brief_ref_and_hash: dict[str, str]
    coverage_cell_ref_and_hash: dict[str, str]
    blinding: bool
    metrics: list[str]
    stop_conditions: list[str]
    forbidden_downstream_lane_flow: list[str]
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    content_hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "pack_id": self.pack_id,
            "calibration_use": self.calibration_use,
            "brief_ref_and_hash": dict(self.brief_ref_and_hash),
            "coverage_cell_ref_and_hash": dict(self.coverage_cell_ref_and_hash),
            "blinding": self.blinding,
            "metrics": list(self.metrics),
            "stop_conditions": list(self.stop_conditions),
            "forbidden_downstream_lane_flow": list(self.forbidden_downstream_lane_flow),
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _check_ref_hash(obj: Any, field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref_id and sha256"))
        return errors
    if not obj.get("ref_id"):
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name}.ref_id is empty"))
    sha = obj.get("sha256", "")
    if not isinstance(sha, str) or not _HASH_RE.match(sha):
        errors.append((EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not valid sha256"))
    return errors


def build_authoring_evaluation_pack(
    *,
    pack_id: str,
    calibration_use: str,
    brief_ref_and_hash: dict[str, str],
    coverage_cell_ref_and_hash: dict[str, str],
    blinding: bool,
    metrics: list[str],
    stop_conditions: list[str],
    forbidden_downstream_lane_flow: list[str],
) -> AuthoringEvaluationPack:
    """构建 AuthoringEvaluationPack，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "pack_id": pack_id,
        "calibration_use": calibration_use,
        "brief_ref_and_hash": dict(brief_ref_and_hash),
        "coverage_cell_ref_and_hash": dict(coverage_cell_ref_and_hash),
        "blinding": blinding,
        "metrics": list(metrics),
        "stop_conditions": list(stop_conditions),
        "forbidden_downstream_lane_flow": list(forbidden_downstream_lane_flow),
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return AuthoringEvaluationPack(
        pack_id=pack_id,
        calibration_use=calibration_use,
        brief_ref_and_hash=dict(brief_ref_and_hash),
        coverage_cell_ref_and_hash=dict(coverage_cell_ref_and_hash),
        blinding=blinding,
        metrics=list(metrics),
        stop_conditions=list(stop_conditions),
        forbidden_downstream_lane_flow=list(forbidden_downstream_lane_flow),
        content_hash=content_hash,
    )


def verify_authoring_evaluation_pack(
    pack: dict[str, Any] | AuthoringEvaluationPack,
) -> VerificationResult:
    """验证 AuthoringEvaluationPack 的结构合法性。

    检查：
    1. schema 常量
    2. pack_id 非空
    3. brief / coverage_cell ref 结构合法
    4. blinding 是 bool
    5. metrics 全部在 QA_BAKEOFF_A_METRICS 中
    6. metrics 不含 QA_BAKEOFF_A_FORBIDDEN_METRICS 中的任何指标
    7. stop_conditions / forbidden_downstream_lane_flow 是 list
    8. content_hash 正确
    """
    if isinstance(pack, AuthoringEvaluationPack):
        pack = pack.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if pack.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if pack.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if pack.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not pack.get("pack_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("pack_id must not be empty")
    if not pack.get("calibration_use"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("calibration_use must not be empty")

    for code, detail in _check_ref_hash(
        pack.get("brief_ref_and_hash", {}), "brief_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)
    for code, detail in _check_ref_hash(
        pack.get("coverage_cell_ref_and_hash", {}), "coverage_cell_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)

    if not isinstance(pack.get("blinding"), bool):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("blinding must be a bool")

    metrics = pack.get("metrics", [])
    if not isinstance(metrics, list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("metrics must be a list")
    else:
        for m in metrics:
            if m not in QA_BAKEOFF_A_METRICS:
                errors.append(EC.QA_BAKEOFF_A_METRIC_NOT_ALLOWED)
                details.append(f"metric {m!r} not in allowed set {QA_BAKEOFF_A_METRICS}")
            if m in QA_BAKEOFF_A_FORBIDDEN_METRICS:
                errors.append(EC.QA_BAKEOFF_A_USING_BARE)
                details.append(f"forbidden metric sneaked in: {m!r}")

    if not isinstance(pack.get("stop_conditions"), list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("stop_conditions must be a list")
    if not isinstance(pack.get("forbidden_downstream_lane_flow"), list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("forbidden_downstream_lane_flow must be a list")

    if pack.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {pack.get('content_hash_algorithm')}")

    computed = _compute_content_hash(pack)
    if pack.get("content_hash") != computed:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {pack.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
