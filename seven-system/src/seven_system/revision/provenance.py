"""ProvenanceSnapshot — P8 开始时对 sealed P7 EvidenceRecord 集合冻结的只读快照。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P8 节和
docs/implementation/15-work-package-implementation-contracts.md WP-RV1：

P7 唯一阶段输出是 sealed EvidenceRecord 集合及其 seal/root hash；它不生成
EvidenceIndex 或 ProvenanceSnapshot。P8 开始时才对该 sealed 集合冻结只读
ProvenanceSnapshot，最终 EvidenceIndex 仅由 P9 生成。

关键约束（blocker）：
- ProvenanceSnapshot 必须只读（不得修改 sealed evidence）→ RV_PROVENANCE_SNAPSHOT_NOT_READONLY
- ProvenanceSnapshot 不得引用/读取尚未生成的最终 EvidenceIndex → RV_EVIDENCE_INDEX_READ_IN_P8
- ProvenanceSnapshot 不完整（无 records / seal hash 缺失）→ RV_PROVENANCE_SNAPSHOT_INCOMPLETE
- snapshot hash 不匹配 → RV_PROVENANCE_SNAPSHOT_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/provenance-snapshot"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class ProvenanceSnapshot:
    """P8 开始时冻结的只读 ProvenanceSnapshot。

    对 sealed P7 EvidenceRecord 集合 + lineage 的只读快照。
    NOT the final EvidenceIndex（P9 才生成）。

    字段：
        snapshot_id: 唯一标识
        plan_id: 对应的 ExperimentPlan ID
        evidence_seal_hash: P7 EvidenceSeal 的 seal_hash 引用
        evidence_seal_root_hash: P7 EvidenceSeal 的 root_hash 引用
        record_hashes: 所有 sealed EvidenceRecord 的 content_hash 列表（有序）
        record_count: record 数量
        lineage: lineage 引用（上游阶段 sealed 产物的 hash 引用）
        frozen_at: 冻结时间
        readonly: 是否只读（必须 True）
        hash_algorithm: 哈希算法
        content_hash: snapshot 自身内容哈希
    """

    snapshot_id: str
    plan_id: str
    evidence_seal_hash: str = ""
    evidence_seal_root_hash: str = ""
    record_hashes: tuple[str, ...] = ()
    record_count: int = 0
    lineage: tuple[dict[str, str], ...] = ()
    frozen_at: str = ""
    readonly: bool = True
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "snapshot_id": self.snapshot_id,
            "plan_id": self.plan_id,
            "evidence_seal_hash": self.evidence_seal_hash,
            "evidence_seal_root_hash": self.evidence_seal_root_hash,
            "record_hashes": list(self.record_hashes),
            "record_count": self.record_count,
            "lineage": [dict(item) for item in self.lineage],
            "frozen_at": self.frozen_at,
            "readonly": self.readonly,
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

    @property
    def is_readonly(self) -> bool:
        return self.readonly


@dataclass(frozen=True)
class ProvenanceSnapshotVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    snapshot_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def _compute_snapshot_root_hash(record_hashes: list[str]) -> str:
    """计算 snapshot root hash——所有 record hash 的排序哈希。"""
    return hashlib.sha256(canonical_json_bytes(sorted(record_hashes))).hexdigest()


def make_provenance_snapshot(
    *,
    snapshot_id: str,
    plan_id: str,
    evidence_seal_hash: str,
    evidence_seal_root_hash: str,
    record_hashes: list[str],
    lineage: list[dict[str, str]] | None = None,
    frozen_at: str | None = None,
) -> ProvenanceSnapshot:
    """构建只读 ProvenanceSnapshot。

    对 sealed P7 EvidenceRecord 集合冻结只读快照。
    """
    frozen_at = frozen_at or datetime.now(timezone.utc).isoformat()
    sorted_hashes = tuple(sorted(record_hashes))
    snapshot = ProvenanceSnapshot(
        snapshot_id=snapshot_id,
        plan_id=plan_id,
        evidence_seal_hash=evidence_seal_hash,
        evidence_seal_root_hash=evidence_seal_root_hash,
        record_hashes=sorted_hashes,
        record_count=len(sorted_hashes),
        lineage=tuple(dict(item) for item in (lineage or ())),
        frozen_at=frozen_at,
        readonly=True,
    )
    return dataclasses.replace(snapshot, content_hash=snapshot.compute_content_hash())


def verify_provenance_snapshot(
    snapshot: ProvenanceSnapshot,
) -> ProvenanceSnapshotVerificationResult:
    """验证 ProvenanceSnapshot。

    blocker：
    - 只读标志不为 True → RV_PROVENANCE_SNAPSHOT_NOT_READONLY
    - 引用 EvidenceIndex → RV_EVIDENCE_INDEX_READ_IN_P8
    - 不完整（无 records / seal hash 缺失）→ RV_PROVENANCE_SNAPSHOT_INCOMPLETE
    - content_hash 不匹配 → RV_PROVENANCE_SNAPSHOT_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = snapshot.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not snapshot.snapshot_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("snapshot_id is empty")

    if not snapshot.plan_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("plan_id is empty")

    # 只读约束
    if not snapshot.readonly:
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_NOT_READONLY)
        details.append("ProvenanceSnapshot must be readonly")

    # 不得引用 EvidenceIndex
    blob = canonical_json_bytes(d)
    if b"EvidenceIndex" in blob:
        errors.append(EC.RV_EVIDENCE_INDEX_READ_IN_P8)
        details.append("ProvenanceSnapshot references EvidenceIndex — only P9 generates it")

    # seal hash 引用
    if not snapshot.evidence_seal_hash:
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_INCOMPLETE)
        details.append("evidence_seal_hash is empty")
    if not snapshot.evidence_seal_root_hash:
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_INCOMPLETE)
        details.append("evidence_seal_root_hash is empty")

    # records 完整性
    if snapshot.record_count == 0 or not snapshot.record_hashes:
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_INCOMPLETE)
        details.append("ProvenanceSnapshot has no records — incomplete")
    if snapshot.record_count != len(snapshot.record_hashes):
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_INCOMPLETE)
        details.append(
            f"record_count {snapshot.record_count} != len(record_hashes) {len(snapshot.record_hashes)}"
        )

    # root hash 一致性（snapshot record_hashes 排序后哈希应与 evidence_seal_root_hash 一致）
    if snapshot.record_hashes and snapshot.evidence_seal_root_hash:
        expected_root = _compute_snapshot_root_hash(list(snapshot.record_hashes))
        if snapshot.evidence_seal_root_hash != expected_root:
            errors.append(EC.RV_PROVENANCE_SNAPSHOT_HASH_MISMATCH)
            details.append(
                f"evidence_seal_root_hash mismatch: claims {snapshot.evidence_seal_root_hash}, "
                f"computed {expected_root}"
            )

    # content_hash
    if not snapshot.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif snapshot.content_hash != snapshot.compute_content_hash():
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_HASH_MISMATCH)
        details.append("ProvenanceSnapshot content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return ProvenanceSnapshotVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        snapshot_id=snapshot.snapshot_id,
    )


def check_provenance_readonly(snapshot: ProvenanceSnapshot) -> VerificationResult:
    """检查 ProvenanceSnapshot 是否只读。"""
    errors: list[EC] = []
    details: list[str] = []
    if not snapshot.readonly:
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_NOT_READONLY)
        details.append("ProvenanceSnapshot must be readonly — sealed evidence cannot be modified")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_no_evidence_index_in_provenance(snapshot: ProvenanceSnapshot) -> VerificationResult:
    """检查 ProvenanceSnapshot 不引用 EvidenceIndex。"""
    errors: list[EC] = []
    details: list[str] = []
    blob = canonical_json_bytes(snapshot.to_dict())
    if b"EvidenceIndex" in blob:
        errors.append(EC.RV_EVIDENCE_INDEX_READ_IN_P8)
        details.append("ProvenanceSnapshot references EvidenceIndex — P8 must not read final EvidenceIndex")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
