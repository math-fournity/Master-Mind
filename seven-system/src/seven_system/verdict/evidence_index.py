"""EvidenceIndex — P9 DAG index from Verdict back to all evidence。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

EvidenceIndex 仅由 P9 生成（NOT P7 or P8）。References all sealed
EvidenceRecords, RunAudits, RunArtifactBundles, etc. by hash.

关键约束（blocker）：
- EvidenceIndex 在 P9 之前生成 → VR_EVIDENCE_INDEX_BEFORE_P9
- evidence 不可从 verdict 反查 → VR_NON_RETRACEABLE
- index hash 不匹配 → VR_EVIDENCE_INDEX_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/evidence-index"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class EvidenceEntry:
    """EvidenceIndex 中的单条引用。"""

    object_kind: str  # EvidenceRecord | RunAudit | RunArtifactBundle | ...
    object_hash: str  # sealed 对象的 content_hash
    phase: str  # P0-P8 哪个阶段产出
    wp_id: str = ""  # 对应工作包

    def to_dict(self) -> dict[str, Any]:
        return {
            "object_kind": self.object_kind,
            "object_hash": self.object_hash,
            "phase": self.phase,
            "wp_id": self.wp_id,
        }


@dataclass(frozen=True)
class EvidenceIndex:
    """P9 EvidenceIndex — DAG index from Verdict back to all evidence。

    仅由 P9 生成。引用所有 sealed EvidenceRecords, RunAudits,
    RunArtifactBundles 等的 hash。

    字段：
        index_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        verdict_hash: 对应 MachineVerdict 的 content_hash
        entries: 所有 evidence 引用（按 hash 排序）
        entry_count: 引用数量
        root_hash: 所有 entry hash 的排序哈希
        generated_in_phase: 生成阶段（必须 P9）
        hash_algorithm: 哈希算法
        content_hash: index 自身内容哈希
    """

    index_id: str
    dag_hash: str = ""
    verdict_hash: str = ""
    entries: tuple[EvidenceEntry, ...] = ()
    entry_count: int = 0
    root_hash: str = ""
    generated_in_phase: str = "P9"
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "index_id": self.index_id,
            "dag_hash": self.dag_hash,
            "verdict_hash": self.verdict_hash,
            "entries": [e.to_dict() for e in self.entries],
            "entry_count": self.entry_count,
            "root_hash": self.root_hash,
            "generated_in_phase": self.generated_in_phase,
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

    def lookup(self, object_hash: str) -> EvidenceEntry | None:
        """从 verdict 反查 evidence——通过 hash 查找 entry。"""
        for e in self.entries:
            if e.object_hash == object_hash:
                return e
        return None

    def all_hashes(self) -> list[str]:
        """返回所有引用的 hash（有序）。"""
        return sorted(e.object_hash for e in self.entries)


def _compute_root_hash(entries: list[EvidenceEntry]) -> str:
    """计算 root hash——所有 entry hash 的排序哈希。"""
    hashes = sorted(e.object_hash for e in entries)
    return hashlib.sha256(canonical_json_bytes(hashes)).hexdigest()


def make_evidence_index(
    *,
    index_id: str,
    dag_hash: str,
    verdict_hash: str,
    entries: list[EvidenceEntry],
    generated_in_phase: str = "P9",
) -> EvidenceIndex:
    """构建 EvidenceIndex。

    仅由 P9 生成。entries 按 object_hash 排序。
    """
    sorted_entries = tuple(sorted(entries, key=lambda e: e.object_hash))
    root = _compute_root_hash(list(sorted_entries))
    index = EvidenceIndex(
        index_id=index_id,
        dag_hash=dag_hash,
        verdict_hash=verdict_hash,
        entries=sorted_entries,
        entry_count=len(sorted_entries),
        root_hash=root,
        generated_in_phase=generated_in_phase,
    )
    return dataclasses.replace(
        index, content_hash=index.compute_content_hash()
    )


def verify_evidence_index(index: EvidenceIndex) -> VerificationResult:
    """验证 EvidenceIndex。

    blocker：
    - 在 P9 之前生成 → VR_EVIDENCE_INDEX_BEFORE_P9
    - 不可反查 → VR_NON_RETRACEABLE
    - root_hash 不匹配 → VR_EVIDENCE_INDEX_HASH_MISMATCH
    - content_hash 不匹配 → VR_EVIDENCE_INDEX_HASH_MISMATCH
    - 不完整 → REQUIRED_FIELD_MISSING
    """
    errors: list[EC] = []
    details: list[str] = []

    d = index.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not index.index_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("index_id is empty")

    if not index.dag_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dag_hash is empty")

    if not index.verdict_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("verdict_hash is empty")

    # 必须在 P9 生成
    if index.generated_in_phase != "P9":
        errors.append(EC.VR_EVIDENCE_INDEX_BEFORE_P9)
        details.append(
            f"EvidenceIndex generated in {index.generated_in_phase}, "
            f"not P9 — only P9 generates EvidenceIndex"
        )

    # entries 完整性
    if index.entry_count == 0 or not index.entries:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("EvidenceIndex has no entries — incomplete")
    if index.entry_count != len(index.entries):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append(
            f"entry_count {index.entry_count} != "
            f"len(entries) {len(index.entries)}"
        )

    # 重复检测
    hashes = [e.object_hash for e in index.entries]
    if len(hashes) != len(set(hashes)):
        errors.append(EC.VR_DUPLICATE_OBJECT)
        details.append("EvidenceIndex contains duplicate object_hash")

    # root_hash 一致性
    if index.entries and index.root_hash:
        expected_root = _compute_root_hash(list(index.entries))
        if index.root_hash != expected_root:
            errors.append(EC.VR_EVIDENCE_INDEX_HASH_MISMATCH)
            details.append(
                f"root_hash mismatch: claims {index.root_hash}, "
                f"computed {expected_root}"
            )

    # 反查能力——每个 entry 必须可从 verdict hash 反查
    # (verdict_hash 绑定 + lookup 可用)
    if index.verdict_hash and index.entries:
        for e in index.entries:
            if not e.object_hash:
                errors.append(EC.VR_NON_RETRACEABLE)
                details.append(
                    f"entry {e.object_kind} has empty object_hash — "
                    f"not retraceable"
                )
                break

    # content_hash
    if not index.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif index.content_hash != index.compute_content_hash():
        errors.append(EC.VR_EVIDENCE_INDEX_HASH_MISMATCH)
        details.append("EvidenceIndex content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


def check_evidence_index_in_p9(index: EvidenceIndex) -> VerificationResult:
    """检查 EvidenceIndex 在 P9 生成。"""
    errors: list[EC] = []
    details: list[str] = []
    if index.generated_in_phase != "P9":
        errors.append(EC.VR_EVIDENCE_INDEX_BEFORE_P9)
        details.append(
            f"EvidenceIndex generated in {index.generated_in_phase} — "
            f"only P9 generates EvidenceIndex"
        )
    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


def check_retraceable(index: EvidenceIndex, object_hash: str) -> VerificationResult:
    """检查指定 hash 可从 EvidenceIndex 反查。"""
    errors: list[EC] = []
    details: list[str] = []
    entry = index.lookup(object_hash)
    if entry is None:
        errors.append(EC.VR_NON_RETRACEABLE)
        details.append(
            f"object_hash {object_hash} not found in EvidenceIndex — "
            f"not retraceable from verdict"
        )
    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )
