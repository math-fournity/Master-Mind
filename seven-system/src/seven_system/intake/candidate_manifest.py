"""CandidateManifest — 只读候选清单对象与验证器。

IN1 的核心产物：从冻结 producer bundle 只读导出的候选清单。
包含 producer schema/version、export manifest 引用、root hash、
attempt 引用、candidate IDs 和 duplicate lineage 记录。

验证器执行 schema + semantic 检查：
- schema_id / schema_version 匹配
- root hash 与计算值一致
- export manifest hash 与实际内容一致
- 每个 attempt ref 的 sha256 与实际内容一致
- producer schema/version 已冻结
- 无缺失 artifact
- 同一 attempt 内无重复 candidate_id
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_CANDIDATE_MANIFEST_SCHEMA_ID = "seven/candidate-manifest"
_CANDIDATE_MANIFEST_SCHEMA_VERSION = 1
_ROOT_HASH_ALGORITHM = "sha256(canonical-json-with-root_hash-null)"


@dataclass(frozen=True)
class AttemptRef:
    """单个 attempt 的只读引用。

    字段：
        attempt_id: attempt 唯一标识
        ref: artifact 引用路径（相对于 producer bundle root）
        sha256: attempt artifact 内容的 SHA-256
        candidate_ids: 该 attempt 产出的 candidate ID 列表
    """

    attempt_id: str
    ref: str
    sha256: str
    candidate_ids: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "ref": self.ref,
            "sha256": self.sha256,
            "candidate_ids": list(self.candidate_ids),
        }


@dataclass(frozen=True)
class DuplicateLineageRef:
    """duplicate lineage 记录——同一 candidate_id 出现在多个 attempt 中。

    这不是错误（跨 attempt 的重复是合法的 provenance 信息），
    但必须被检测和记录。
    """

    candidate_id: str
    attempt_ids: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "attempt_ids": list(self.attempt_ids),
        }


@dataclass(frozen=True)
class CandidateManifest:
    """只读候选清单。

    字段：
        schema_id: 固定为 "seven/candidate-manifest"
        schema_version: 固定为 1
        producer_schema: producer 的 schema 标识（冻结）
        producer_version: producer 的版本号（冻结）
        export_manifest_ref_and_hash: export manifest artifact 引用与哈希
        root_hash: 整个清单内容的 root 哈希
        attempt_refs: 所有 attempt 的只读引用
        candidate_ids: 所有 candidate ID 的去重列表
        duplicate_lineage_refs: 跨 attempt 重复 candidate 的 lineage 记录
    """

    schema_id: str = _CANDIDATE_MANIFEST_SCHEMA_ID
    schema_version: int = _CANDIDATE_MANIFEST_SCHEMA_VERSION
    producer_schema: str = ""
    producer_version: str = ""
    export_manifest_ref_and_hash: dict[str, str] = field(default_factory=dict)
    root_hash: str = ""
    attempt_refs: tuple[AttemptRef, ...] = ()
    candidate_ids: tuple[str, ...] = ()
    duplicate_lineage_refs: tuple[DuplicateLineageRef, ...] = ()
    root_hash_algorithm: str = _ROOT_HASH_ALGORITHM

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "producer_schema": self.producer_schema,
            "producer_version": self.producer_version,
            "export_manifest_ref_and_hash": dict(self.export_manifest_ref_and_hash),
            "root_hash": self.root_hash,
            "attempt_refs": [ar.to_dict() for ar in self.attempt_refs],
            "candidate_ids": list(self.candidate_ids),
            "duplicate_lineage_refs": [
                dl.to_dict() for dl in self.duplicate_lineage_refs
            ],
            "root_hash_algorithm": self.root_hash_algorithm,
        }

    def compute_root_hash(self) -> str:
        """计算 root hash（root_hash 字段置 null）。"""
        d = self.to_dict()
        d["root_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_root_hash_valid(self) -> bool:
        """root_hash 是否与计算值一致。"""
        return self.root_hash == self.compute_root_hash()


@dataclass(frozen=True)
class CandidateManifestVerificationResult:
    """CandidateManifest 验证器的结构化结果，不抛异常。"""

    verdict: str  # "PASS" | "FAIL"
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    producer_schema: str = ""
    producer_version: str = ""
    attempt_count: int = 0
    candidate_count: int = 0
    duplicate_lineage_count: int = 0

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def _compute_export_manifest_hash(
    attempt_refs: tuple[AttemptRef, ...],
) -> str:
    """从 attempt_refs 计算_export_manifest 的内容哈希。"""
    payload = [ar.to_dict() for ar in attempt_refs]
    return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def verify_candidate_manifest(
    manifest: CandidateManifest,
    *,
    producer_bundle_ref: Any = None,
    expected_export_manifest_sha256: str | None = None,
    attempt_content_hashes: dict[str, str] | None = None,
) -> CandidateManifestVerificationResult:
    """验证 CandidateManifest 的 schema + semantic 完整性。

    参数：
        manifest: 待验证的 CandidateManifest
        producer_bundle_ref: 可选的 ProducerBundleRef，用于交叉验证 producer schema/version
        expected_export_manifest_sha256: 可选的 export manifest 实际内容哈希
        attempt_content_hashes: 可选的 {attempt_id: actual_sha256} 映射，
            用于验证每个 attempt ref 的 sha256

    返回结构化结果，不抛异常。
    """
    errors: list[EC] = []
    details: list[str] = []

    # ── Schema 检查 ──────────────────────────────────────────────

    # schema_id
    if manifest.schema_id != _CANDIDATE_MANIFEST_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(
            f"schema_id mismatch: expected {_CANDIDATE_MANIFEST_SCHEMA_ID}, "
            f"got {manifest.schema_id}"
        )

    # schema_version
    if manifest.schema_version != _CANDIDATE_MANIFEST_SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(
            f"schema_version mismatch: expected "
            f"{_CANDIDATE_MANIFEST_SCHEMA_VERSION}, "
            f"got {manifest.schema_version}"
        )

    # ── Producer schema/version 冻结检查 ─────────────────────────

    if not manifest.producer_schema or not manifest.producer_version:
        errors.append(EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN)
        details.append(
            f"producer_schema='{manifest.producer_schema}', "
            f"producer_version='{manifest.producer_version}' — "
            f"both must be non-empty (frozen)"
        )

    # 交叉验证 producer bundle
    if producer_bundle_ref is not None:
        from .producer_bundle import ProducerBundleRef, verify_producer_bundle

        if isinstance(producer_bundle_ref, ProducerBundleRef):
            if producer_bundle_ref.producer_schema != manifest.producer_schema:
                errors.append(EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN)
                details.append(
                    f"producer_schema mismatch: manifest has "
                    f"'{manifest.producer_schema}', bundle has "
                    f"'{producer_bundle_ref.producer_schema}'"
                )
            if producer_bundle_ref.producer_version != manifest.producer_version:
                errors.append(EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN)
                details.append(
                    f"producer_version mismatch: manifest has "
                    f"'{manifest.producer_version}', bundle has "
                    f"'{producer_bundle_ref.producer_version}'"
                )
        else:
            errors.append(EC.IN1_MUTABLE_REFERENCE_REJECTED)
            details.append(
                f"producer_bundle_ref is not a frozen ProducerBundleRef, "
                f"got {type(producer_bundle_ref).__name__}"
            )

    # ── Export manifest 引用检查 ──────────────────────────────────

    em = manifest.export_manifest_ref_and_hash
    if not em or not em.get("ref") or not em.get("sha256"):
        errors.append(EC.IN1_MISSING_ARTIFACT)
        details.append(
            "export_manifest_ref_and_hash is missing ref or sha256"
        )
    elif expected_export_manifest_sha256 is not None:
        if em.get("sha256") != expected_export_manifest_sha256:
            errors.append(EC.IN1_EXPORT_MANIFEST_HASH_MISMATCH)
            details.append(
                f"export manifest hash mismatch: manifest claims "
                f"{em.get('sha256')}, actual content hash is "
                f"{expected_export_manifest_sha256}"
            )

    # ── Root hash 检查 ────────────────────────────────────────────

    if not manifest.root_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("root_hash is empty")
    elif manifest.root_hash != manifest.compute_root_hash():
        errors.append(EC.IN1_ROOT_HASH_MISMATCH)
        details.append(
            f"root_hash mismatch: manifest claims {manifest.root_hash}, "
            f"computed {manifest.compute_root_hash()}"
        )

    # ── Attempt refs 检查 ─────────────────────────────────────────

    for ar in manifest.attempt_refs:
        # 缺失 artifact 检查
        if not ar.ref or not ar.sha256:
            errors.append(EC.IN1_MISSING_ARTIFACT)
            details.append(
                f"attempt {ar.attempt_id} has empty ref or sha256"
            )
            continue

        # sha256 格式检查
        if len(ar.sha256) != 64:
            errors.append(EC.IN1_ATTEMPT_REF_HASH_MISMATCH)
            details.append(
                f"attempt {ar.attempt_id} sha256 is not 64 hex chars: "
                f"{ar.sha256}"
            )
            continue

        # attempt ref hash 交叉验证
        if attempt_content_hashes is not None:
            actual = attempt_content_hashes.get(ar.attempt_id)
            if actual is not None and actual != ar.sha256:
                errors.append(EC.IN1_ATTEMPT_REF_HASH_MISMATCH)
                details.append(
                    f"attempt {ar.attempt_id} hash mismatch: "
                    f"manifest claims {ar.sha256}, actual {actual}"
                )

        # 同一 attempt 内重复 candidate_id 检查
        seen: set[str] = set()
        for cid in ar.candidate_ids:
            if cid in seen:
                errors.append(EC.IN1_DUPLICATE_CANDIDATE_IN_ATTEMPT)
                details.append(
                    f"duplicate candidate_id '{cid}' in attempt "
                    f"{ar.attempt_id}"
                )
            seen.add(cid)

    # ── 返回结果 ──────────────────────────────────────────────────

    verdict = "PASS" if not errors else "FAIL"
    return CandidateManifestVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        producer_schema=manifest.producer_schema,
        producer_version=manifest.producer_version,
        attempt_count=len(manifest.attempt_refs),
        candidate_count=len(manifest.candidate_ids),
        duplicate_lineage_count=len(manifest.duplicate_lineage_refs),
    )
