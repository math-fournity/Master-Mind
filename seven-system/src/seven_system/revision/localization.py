"""FailureLocalization — P8 第一独立故障定位。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P8 节：

First independent failure localization: Core, boundary, selector, renderer,
injection, critic, model/resource — which layer went wrong.

故障定位是独立分析，输出是 localization result（哪一层出错），不是 revision
decision。引用 EvidenceRecord by hash。

关键约束（blocker）：
- 定位层必须在 RV_LOCALIZATION_LAYERS 中 → RV_LOCALIZATION_LAYER_INVALID
- 定位不完整（无 layer / 无 evidence 引用）→ RV_FAILURE_LOCALIZATION_INCOMPLETE
- 引用 EvidenceIndex → RV_LOCALIZATION_REFERENCES_EVIDENCE_INDEX
- content_hash 不匹配 → RV_LOCALIZATION_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    RV_LOCALIZATION_LAYERS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/failure-localization"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class FailureLocalization:
    """P8 第一独立故障定位——哪一层出错。

    输出是 localization result，不是 revision decision。
    引用 EvidenceRecord by hash。

    字段：
        localization_id: 唯一标识
        provenance_snapshot_hash: 引用的 ProvenanceSnapshot content_hash
        failed_layer: 出错层（RV_LOCALIZATION_LAYERS）
        evidence_refs: 引用的 EvidenceRecord content_hash 列表
        diagnosis: 诊断描述
        localized_at: 定位时间
        hash_algorithm: 哈希算法
        content_hash: 内容哈希
    """

    localization_id: str
    provenance_snapshot_hash: str = ""
    failed_layer: str = ""
    evidence_refs: tuple[str, ...] = ()
    diagnosis: str = ""
    localized_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "localization_id": self.localization_id,
            "provenance_snapshot_hash": self.provenance_snapshot_hash,
            "failed_layer": self.failed_layer,
            "evidence_refs": list(self.evidence_refs),
            "diagnosis": self.diagnosis,
            "localized_at": self.localized_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


@dataclass(frozen=True)
class FailureLocalizationVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    localization_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def make_failure_localization(
    *,
    localization_id: str,
    provenance_snapshot_hash: str,
    failed_layer: str,
    evidence_refs: list[str],
    diagnosis: str = "",
    localized_at: str | None = None,
) -> FailureLocalization:
    """构建 FailureLocalization。"""
    if failed_layer not in RV_LOCALIZATION_LAYERS:
        raise ValueError(
            f"failed_layer {failed_layer!r} not in RV_LOCALIZATION_LAYERS"
        )
    localized_at = localized_at or datetime.now(timezone.utc).isoformat()
    loc = FailureLocalization(
        localization_id=localization_id,
        provenance_snapshot_hash=provenance_snapshot_hash,
        failed_layer=failed_layer,
        evidence_refs=tuple(evidence_refs),
        diagnosis=diagnosis,
        localized_at=localized_at,
    )
    return dataclasses.replace(loc, content_hash=loc.compute_content_hash())


def verify_failure_localization(
    loc: FailureLocalization,
) -> FailureLocalizationVerificationResult:
    """验证 FailureLocalization。

    blocker：
    - failed_layer 不在 RV_LOCALIZATION_LAYERS → RV_LOCALIZATION_LAYER_INVALID
    - 不完整（无 layer / 无 evidence_refs / 无 snapshot hash）→ RV_FAILURE_LOCALIZATION_INCOMPLETE
    - 引用 EvidenceIndex → RV_LOCALIZATION_REFERENCES_EVIDENCE_INDEX
    - content_hash 不匹配 → RV_LOCALIZATION_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = loc.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not loc.localization_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("localization_id is empty")

    # failed_layer 合法性
    if not loc.failed_layer:
        errors.append(EC.RV_FAILURE_LOCALIZATION_INCOMPLETE)
        details.append("failed_layer is empty")
    elif loc.failed_layer not in RV_LOCALIZATION_LAYERS:
        errors.append(EC.RV_LOCALIZATION_LAYER_INVALID)
        details.append(
            f"failed_layer {loc.failed_layer!r} not in RV_LOCALIZATION_LAYERS"
        )

    # provenance snapshot hash 引用
    if not loc.provenance_snapshot_hash:
        errors.append(EC.RV_FAILURE_LOCALIZATION_INCOMPLETE)
        details.append("provenance_snapshot_hash is empty")

    # evidence refs
    if not loc.evidence_refs:
        errors.append(EC.RV_FAILURE_LOCALIZATION_INCOMPLETE)
        details.append("evidence_refs is empty — localization must reference EvidenceRecord by hash")

    # 不得引用 EvidenceIndex
    blob = canonical_json_bytes(d)
    if b"EvidenceIndex" in blob:
        errors.append(EC.RV_LOCALIZATION_REFERENCES_EVIDENCE_INDEX)
        details.append("FailureLocalization references EvidenceIndex — P8 must not read final EvidenceIndex")

    # content_hash
    if not loc.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif loc.content_hash != loc.compute_content_hash():
        errors.append(EC.RV_LOCALIZATION_HASH_MISMATCH)
        details.append("FailureLocalization content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return FailureLocalizationVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        localization_id=loc.localization_id,
    )
