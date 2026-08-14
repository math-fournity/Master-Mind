"""ReadOnlyCandidateManifestExporter — 只读候选清单导出器。

IN1 的导出协议：从冻结 producer bundle 只读导出 CandidateManifest。
关键约束：
- READ-ONLY：不写生产 pipe、不写 DB、不写 Redis、不写 D 盘
- 检测 duplicate lineage（同一 candidate_id 跨 attempt 出现）
- 检测同一 attempt 内重复 candidate_id（错误，拒绝）
- 生成零写入收据

本模块提供：
- ReadOnlyPermit：只读许可（冻结输入之一）
- CandidateManifestExporterPort：导出协议接口
- FakeCandidateManifestExporter：side-effect-free 测试用假实现
- ZeroWriteReceipt：零写入收据
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any, Protocol

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from .producer_bundle import (
    ProducerBundleRef,
    verify_producer_bundle,
)
from .candidate_manifest import (
    AttemptRef,
    CandidateManifest,
    DuplicateLineageRef,
    _CANDIDATE_MANIFEST_SCHEMA_ID,
    _CANDIDATE_MANIFEST_SCHEMA_VERSION,
)


# ─── 只读许可 ─────────────────────────────────────────────────────


@dataclass(frozen=True)
class ReadOnlyPermit:
    """只读许可——IN1 的冻结输入之一。

    明确声明 permitted_operation=READ_ONLY_EXPORT，
    所有写操作被禁止。
    """

    permit_id: str
    producer_bundle_id: str
    permitted_operation: str = "READ_ONLY_EXPORT"
    write_forbidden: bool = True
    permit_hash_algorithm: str = "sha256(canonical-json-with-permit_hash-null)"
    permit_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "permit_id": self.permit_id,
            "producer_bundle_id": self.producer_bundle_id,
            "permitted_operation": self.permitted_operation,
            "write_forbidden": self.write_forbidden,
            "permit_hash_algorithm": self.permit_hash_algorithm,
            "permit_hash": self.permit_hash,
        }

    def compute_permit_hash(self) -> str:
        d = self.to_dict()
        d["permit_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.permit_hash == self.compute_permit_hash()


def make_read_only_permit(
    *,
    permit_id: str,
    producer_bundle_id: str,
) -> ReadOnlyPermit:
    """构建 ReadOnlyPermit 并自动计算 permit_hash。"""
    import dataclasses

    permit = ReadOnlyPermit(
        permit_id=permit_id,
        producer_bundle_id=producer_bundle_id,
    )
    return dataclasses.replace(permit, permit_hash=permit.compute_permit_hash())


# ─── 零写入收据 ───────────────────────────────────────────────────


@dataclass(frozen=True)
class ZeroWriteReceipt:
    """零写入收据——证明导出过程未执行任何写入。

    所有写入计数必须为 0。
    """

    export_id: str
    producer_bundle_id: str
    production_pipe_writes: int = 0
    db_writes: int = 0
    redis_writes: int = 0
    d_volume_writes: int = 0
    receipt_hash_algorithm: str = "sha256(canonical-json-with-receipt_hash-null)"
    receipt_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "export_id": self.export_id,
            "producer_bundle_id": self.producer_bundle_id,
            "production_pipe_writes": self.production_pipe_writes,
            "db_writes": self.db_writes,
            "redis_writes": self.redis_writes,
            "d_volume_writes": self.d_volume_writes,
            "receipt_hash_algorithm": self.receipt_hash_algorithm,
            "receipt_hash": self.receipt_hash,
        }

    def compute_receipt_hash(self) -> str:
        d = self.to_dict()
        d["receipt_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_zero_write(self) -> bool:
        """所有写入计数是否全为 0。"""
        return (
            self.production_pipe_writes == 0
            and self.db_writes == 0
            and self.redis_writes == 0
            and self.d_volume_writes == 0
        )

    @property
    def is_hash_valid(self) -> bool:
        return self.receipt_hash == self.compute_receipt_hash()


def make_zero_write_receipt(
    *,
    export_id: str,
    producer_bundle_id: str,
) -> ZeroWriteReceipt:
    """构建 ZeroWriteReceipt 并自动计算 receipt_hash。"""
    import dataclasses

    receipt = ZeroWriteReceipt(
        export_id=export_id,
        producer_bundle_id=producer_bundle_id,
    )
    return dataclasses.replace(receipt, receipt_hash=receipt.compute_receipt_hash())


# ─── 导出协议 ─────────────────────────────────────────────────────


class CandidateManifestExporterPort(Protocol):
    """只读 CandidateManifest 导出协议（IN1 冻结接口）。

    实现者：
    - FakeCandidateManifestExporter: side-effect-free 测试用假实现
    - 未来真实实现：从冻结 producer bundle 只读导出

    任何实现都不得写生产 pipe、DB、Redis 或 D 盘。
    """

    def export_manifest(
        self, producer_bundle_ref: ProducerBundleRef
    ) -> CandidateManifest:
        """从冻结 producer bundle 只读导出 CandidateManifest。

        不写任何生产存储。检测 duplicate lineage 并记录。
        同一 attempt 内重复 candidate_id 视为错误。
        """
        ...

    def get_zero_write_receipt(self) -> ZeroWriteReceipt:
        """获取零写入收据，证明导出过程未执行任何写入。"""
        ...

    def reject_production_write(self, data: Any) -> None:
        """显式拒绝生产 pipe 写入。

        任何实现都必须在调用此方法时抛出 IN1_PRODUCTION_WRITE_REJECTED。
        此方法的存在本身就是只读约束的机器化表达。
        """
        ...


# ─── 内部异常 ─────────────────────────────────────────────────────


class _IntakeError(Exception):
    """IN1 内部异常。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


# ─── Fake 实现（side-effect-free）─────────────────────────────────


class FakeCandidateManifestExporter:
    """Side-effect-free 假实现——仅用于隔离 fixture 测试。

    从内存中的 attempt 数据构建 CandidateManifest。
    不连接任何真实 DB、Redis 或 D 盘。
    所有写操作被拒绝并记录。
    """

    def __init__(
        self,
        *,
        attempts: list[dict[str, Any]],
        read_only_permit: ReadOnlyPermit,
        source_root_hash: str = "",
        export_manifest_ref: str = "export-manifest.json",
    ) -> None:
        """
        参数：
            attempts: attempt 数据列表，每项包含：
                - attempt_id: str
                - ref: str (artifact 引用路径)
                - content: dict (artifact 内容，用于计算 sha256)
                - candidate_ids: list[str]
            read_only_permit: 只读许可
            source_root_hash: 源根目录哈希（用于检测 drift）
            export_manifest_ref: export manifest 的引用路径
        """
        self._attempts = attempts
        self._permit = read_only_permit
        self._source_root_hash = source_root_hash
        self._export_manifest_ref = export_manifest_ref
        self._production_write_attempts: list[Any] = []
        self._last_manifest: CandidateManifest | None = None

    def export_manifest(
        self, producer_bundle_ref: ProducerBundleRef
    ) -> CandidateManifest:
        """从冻结 producer bundle 只读导出 CandidateManifest。"""

        # 1. 验证只读许可
        if not self._permit.write_forbidden:
            raise _IntakeError(
                EC.IN1_PRODUCTION_WRITE_REJECTED,
                f"permit {self._permit.permit_id} does not forbid writes",
            )

        # 2. 验证 producer bundle（必须是冻结 ProducerBundleRef）
        bundle_errors = verify_producer_bundle(producer_bundle_ref)
        if bundle_errors:
            code, detail = bundle_errors[0]
            raise _IntakeError(code, detail)

        # 3. 检查 source root drift
        if (
            self._source_root_hash
            and producer_bundle_ref.source_root_hash
            and self._source_root_hash != producer_bundle_ref.source_root_hash
        ):
            raise _IntakeError(
                EC.IN1_SOURCE_ROOT_DRIFT,
                f"source root drift: bundle expects "
                f"{producer_bundle_ref.source_root_hash}, "
                f"actual is {self._source_root_hash}",
            )

        # 4. 检查 producer schema/version 冻结
        if not producer_bundle_ref.is_frozen:
            raise _IntakeError(
                EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN,
                f"producer_schema='{producer_bundle_ref.producer_schema}', "
                f"producer_version='{producer_bundle_ref.producer_version}'",
            )

        # 5. 构建 attempt refs（只读，不修改原始数据）
        attempt_refs: list[AttemptRef] = []
        attempt_content_hashes: dict[str, str] = {}

        for attempt_data in self._attempts:
            attempt_id = attempt_data["attempt_id"]
            ref = attempt_data["ref"]
            content = attempt_data["content"]
            candidate_ids = tuple(attempt_data.get("candidate_ids", []))

            # 计算 attempt 内容哈希
            content_hash = hashlib.sha256(
                canonical_json_bytes(content)
            ).hexdigest()
            attempt_content_hashes[attempt_id] = content_hash

            # 检查同一 attempt 内重复 candidate_id
            seen: set[str] = set()
            for cid in candidate_ids:
                if cid in seen:
                    raise _IntakeError(
                        EC.IN1_DUPLICATE_CANDIDATE_IN_ATTEMPT,
                        f"duplicate candidate_id '{cid}' in attempt "
                        f"{attempt_id}",
                    )
                seen.add(cid)

            attempt_refs.append(
                AttemptRef(
                    attempt_id=attempt_id,
                    ref=ref,
                    sha256=content_hash,
                    candidate_ids=candidate_ids,
                )
            )

        # 6. 检测 duplicate lineage（同一 candidate_id 跨 attempt）
        candidate_to_attempts: dict[str, list[str]] = {}
        for ar in attempt_refs:
            for cid in ar.candidate_ids:
                candidate_to_attempts.setdefault(cid, []).append(ar.attempt_id)

        duplicate_lineage_refs: list[DuplicateLineageRef] = []
        all_candidate_ids: list[str] = []
        for cid, attempt_ids in candidate_to_attempts.items():
            all_candidate_ids.append(cid)
            if len(attempt_ids) > 1:
                duplicate_lineage_refs.append(
                    DuplicateLineageRef(
                        candidate_id=cid,
                        attempt_ids=tuple(attempt_ids),
                    )
                )

        # 7. 计算 export manifest 哈希
        export_manifest_payload = [ar.to_dict() for ar in attempt_refs]
        export_manifest_sha256 = hashlib.sha256(
            canonical_json_bytes(export_manifest_payload)
        ).hexdigest()

        # 8. 构建 CandidateManifest
        manifest = CandidateManifest(
            schema_id=_CANDIDATE_MANIFEST_SCHEMA_ID,
            schema_version=_CANDIDATE_MANIFEST_SCHEMA_VERSION,
            producer_schema=producer_bundle_ref.producer_schema,
            producer_version=producer_bundle_ref.producer_version,
            export_manifest_ref_and_hash={
                "ref": self._export_manifest_ref,
                "sha256": export_manifest_sha256,
            },
            attempt_refs=tuple(attempt_refs),
            candidate_ids=tuple(all_candidate_ids),
            duplicate_lineage_refs=tuple(duplicate_lineage_refs),
        )

        # 9. 计算 root hash
        import dataclasses

        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )

        self._last_manifest = manifest
        return manifest

    def get_zero_write_receipt(self) -> ZeroWriteReceipt:
        """获取零写入收据。"""
        export_id = "export-001"
        if self._last_manifest is not None:
            # 用 manifest 的 root_hash 派生 export_id
            export_id = f"export-{self._last_manifest.root_hash[:16]}"
        return make_zero_write_receipt(
            export_id=export_id,
            producer_bundle_id=(
                self._permit.producer_bundle_id
                if self._permit
                else "unknown"
            ),
        )

    def reject_production_write(self, data: Any) -> None:
        """显式拒绝生产 pipe 写入。"""
        self._production_write_attempts.append(data)
        raise _IntakeError(
            EC.IN1_PRODUCTION_WRITE_REJECTED,
            f"production pipe write rejected: read-only permit "
            f"{self._permit.permit_id} forbids all writes",
        )

    @property
    def production_write_attempt_count(self) -> int:
        """生产 pipe 写入尝试次数（应始终为 0）。"""
        return len(self._production_write_attempts)

    @property
    def last_manifest(self) -> CandidateManifest | None:
        """最后一次导出的 CandidateManifest。"""
        return self._last_manifest
