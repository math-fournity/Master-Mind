"""ProducerBundleRef — 冻结、哈希、版本化的外部 system/ producer 引用。

AGENTS.md 规则 9：``system/` 是外部 producer，不是 Python 依赖；
只能通过冻结、哈希、版本化 bundle 接入。'

本模块定义 ProducerBundleRef，它是外部 producer 在某一时刻的冻结快照引用。
IN1 exporter 只接受有效的 ProducerBundleRef，不接受可变 dict 或裸路径。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_PRODUCER_BUNDLE_SCHEMA_ID = "seven/producer-bundle-ref"
_PRODUCER_BUNDLE_SCHEMA_VERSION = 1
_BUNDLE_HASH_ALGORITHM = "sha256(canonical-json-with-bundle_hash-null)"


@dataclass(frozen=True)
class ProducerBundleRef:
    """冻结、哈希、版本化的外部 producer 引用。

    字段：
        bundle_id: 唯一标识符
        producer_schema: producer 的 schema 标识（冻结时记录）
        producer_version: producer 的版本号（冻结时记录）
        content_sha256: producer 内容的 SHA-256（冻结时计算）
        source_root_hash: 源根目录的哈希（冻结时计算，用于检测 drift）
        frozen_at: 冻结时间（ISO 8601 UTC）
        bundle_hash: 由其他字段计算的 bundle 哈希（计算时置 null）
    """

    bundle_id: str
    producer_schema: str
    producer_version: str
    content_sha256: str
    source_root_hash: str
    frozen_at: str
    bundle_hash_algorithm: str = _BUNDLE_HASH_ALGORITHM
    bundle_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _PRODUCER_BUNDLE_SCHEMA_ID,
            "schema_version": _PRODUCER_BUNDLE_SCHEMA_VERSION,
            "bundle_id": self.bundle_id,
            "producer_schema": self.producer_schema,
            "producer_version": self.producer_version,
            "content_sha256": self.content_sha256,
            "source_root_hash": self.source_root_hash,
            "frozen_at": self.frozen_at,
            "bundle_hash_algorithm": self.bundle_hash_algorithm,
            "bundle_hash": self.bundle_hash,
        }

    def compute_bundle_hash(self) -> str:
        """计算 bundle 哈希（bundle_hash 字段置 null）。"""
        d = self.to_dict()
        d["bundle_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        """bundle_hash 是否与计算值一致。"""
        return self.bundle_hash == self.compute_bundle_hash()

    @property
    def is_frozen(self) -> bool:
        """producer_schema 和 producer_version 是否已冻结（非空）。"""
        return bool(self.producer_schema) and bool(self.producer_version)


def make_producer_bundle_ref(
    *,
    bundle_id: str,
    producer_schema: str,
    producer_version: str,
    content_sha256: str,
    source_root_hash: str,
    frozen_at: str,
) -> ProducerBundleRef:
    """构建 ProducerBundleRef 并自动计算 bundle_hash。"""
    ref = ProducerBundleRef(
        bundle_id=bundle_id,
        producer_schema=producer_schema,
        producer_version=producer_version,
        content_sha256=content_sha256,
        source_root_hash=source_root_hash,
        frozen_at=frozen_at,
    )
    # frozen dataclass 不可变，需要用 object.__new__ 重建或用 dataclasses.replace
    import dataclasses

    return dataclasses.replace(ref, bundle_hash=ref.compute_bundle_hash())


def verify_producer_bundle(ref: ProducerBundleRef | Any) -> list[tuple[EC, str]]:
    """验证 ProducerBundleRef 的完整性。

    返回 (error_code, detail) 列表；空列表表示通过。
    不抛异常——调用方根据返回值判断。
    """
    errors: list[tuple[EC, str]] = []

    # 必须是 ProducerBundleRef（冻结 dataclass），不接受可变 dict
    if not isinstance(ref, ProducerBundleRef):
        errors.append((
            EC.IN1_MUTABLE_REFERENCE_REJECTED,
            f"expected frozen ProducerBundleRef, got {type(ref).__name__}",
        ))
        return errors

    # producer_schema / producer_version 必须冻结（非空）
    if not ref.is_frozen:
        errors.append((
            EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN,
            f"producer_schema='{ref.producer_schema}', "
            f"producer_version='{ref.producer_version}' — both must be non-empty",
        ))

    # bundle_hash 必须匹配
    if not ref.is_hash_valid:
        errors.append((
            EC.IN1_PRODUCER_BUNDLE_INVALID,
            f"bundle_hash mismatch: expected {ref.compute_bundle_hash()}, "
            f"got {ref.bundle_hash}",
        ))

    # content_sha256 必须是有效的 64 字符 hex
    if len(ref.content_sha256) != 64:
        errors.append((
            EC.IN1_PRODUCER_BUNDLE_INVALID,
            f"content_sha256 must be 64 hex chars, got {len(ref.content_sha256)}",
        ))

    # source_root_hash 必须非空
    if not ref.source_root_hash:
        errors.append((
            EC.IN1_PRODUCER_BUNDLE_INVALID,
            "source_root_hash is empty",
        ))

    return errors
