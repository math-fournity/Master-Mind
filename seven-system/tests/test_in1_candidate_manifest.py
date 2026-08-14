"""WP-IN1 只读 CandidateManifest / exporter / duplicate lineage 测试。

测试层级：Golden → Negative (blocker) → Fault injection
所有 blocker test 失败 → 工作包 FAIL。

覆盖：
- Golden: valid CandidateManifest, frozen producer schema, zero writes
- Negative: production write-back, mutable reference, missing artifact,
  source root drift, duplicate candidate_id in attempt, producer schema not frozen
- Fault: root hash mismatch, export manifest hash mismatch, attempt ref hash mismatch
- Duplicate lineage detection across attempts
"""

from __future__ import annotations

import dataclasses
import hashlib
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC
from seven_system.hashing import canonical_json_bytes
from seven_system.intake.producer_bundle import (
    ProducerBundleRef,
    make_producer_bundle_ref,
    verify_producer_bundle,
)
from seven_system.intake.candidate_manifest import (
    AttemptRef,
    CandidateManifest,
    DuplicateLineageRef,
    verify_candidate_manifest,
)
from seven_system.intake.exporter import (
    ReadOnlyPermit,
    make_read_only_permit,
    ZeroWriteReceipt,
    make_zero_write_receipt,
    FakeCandidateManifestExporter,
    _IntakeError,
)


# ─── helpers ───────────────────────────────────────────────────────


def _make_producer_bundle(
    *,
    producer_schema: str = "system/math-producer",
    producer_version: str = "1.0.0",
    source_root_hash: str = "a" * 64,
    content_sha256: str = "b" * 64,
) -> ProducerBundleRef:
    return make_producer_bundle_ref(
        bundle_id="producer-bundle-001",
        producer_schema=producer_schema,
        producer_version=producer_version,
        content_sha256=content_sha256,
        source_root_hash=source_root_hash,
        frozen_at="2026-08-14T00:00:00Z",
    )


def _make_read_only_permit(
    producer_bundle_id: str = "producer-bundle-001",
) -> ReadOnlyPermit:
    return make_read_only_permit(
        permit_id="permit-in1-001",
        producer_bundle_id=producer_bundle_id,
    )


def _make_attempt_data(
    attempt_id: str = "attempt-001",
    candidate_ids: list[str] | None = None,
    content: dict | None = None,
) -> dict:
    if candidate_ids is None:
        candidate_ids = ["cand-001", "cand-002"]
    if content is None:
        content = {
            "attempt_id": attempt_id,
            "candidates": candidate_ids,
            "status": "COMPLETED",
        }
    return {
        "attempt_id": attempt_id,
        "ref": f"attempts/{attempt_id}.json",
        "content": content,
        "candidate_ids": candidate_ids,
    }


def _make_valid_attempts() -> list[dict]:
    return [
        _make_attempt_data(
            attempt_id="attempt-001",
            candidate_ids=["cand-001", "cand-002"],
        ),
        _make_attempt_data(
            attempt_id="attempt-002",
            candidate_ids=["cand-003", "cand-004"],
        ),
    ]


def _make_exporter(
    *,
    attempts: list[dict] | None = None,
    source_root_hash: str = "a" * 64,
    producer_bundle: ProducerBundleRef | None = None,
) -> tuple[FakeCandidateManifestExporter, ProducerBundleRef]:
    if attempts is None:
        attempts = _make_valid_attempts()
    if producer_bundle is None:
        producer_bundle = _make_producer_bundle(
            source_root_hash=source_root_hash,
        )
    permit = _make_read_only_permit(
        producer_bundle_id=producer_bundle.bundle_id,
    )
    exporter = FakeCandidateManifestExporter(
        attempts=attempts,
        read_only_permit=permit,
        source_root_hash=source_root_hash,
    )
    return exporter, producer_bundle


# ─── Golden vectors ────────────────────────────────────────────────


class CandidateManifestGoldenVectors(unittest.TestCase):
    """Golden: valid CandidateManifest with correct root hash,
    frozen producer schema, zero writes."""

    def test_valid_manifest_export_and_verify(self) -> None:
        """导出有效 manifest 并通过验证器。"""
        exporter, bundle = _make_exporter()
        manifest = exporter.export_manifest(bundle)

        # schema 检查
        self.assertEqual(manifest.schema_id, "seven/candidate-manifest")
        self.assertEqual(manifest.schema_version, 1)

        # producer schema 冻结
        self.assertEqual(manifest.producer_schema, "system/math-producer")
        self.assertEqual(manifest.producer_version, "1.0.0")

        # root hash 有效
        self.assertTrue(manifest.is_root_hash_valid)
        self.assertNotEqual(manifest.root_hash, "")

        # attempt refs
        self.assertEqual(len(manifest.attempt_refs), 2)
        self.assertEqual(len(manifest.candidate_ids), 4)

        # export manifest ref 存在
        self.assertIn("ref", manifest.export_manifest_ref_and_hash)
        self.assertIn("sha256", manifest.export_manifest_ref_and_hash)

        # 验证器通过
        result = verify_candidate_manifest(manifest, producer_bundle_ref=bundle)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertEqual(result.attempt_count, 2)
        self.assertEqual(result.candidate_count, 4)

    def test_exporter_produces_zero_write_receipt(self) -> None:
        """导出后零写入收据所有计数为 0。"""
        exporter, bundle = _make_exporter()
        exporter.export_manifest(bundle)

        receipt = exporter.get_zero_write_receipt()
        self.assertTrue(receipt.is_zero_write)
        self.assertEqual(receipt.production_pipe_writes, 0)
        self.assertEqual(receipt.db_writes, 0)
        self.assertEqual(receipt.redis_writes, 0)
        self.assertEqual(receipt.d_volume_writes, 0)
        # receipt hash 有效
        self.assertTrue(receipt.is_hash_valid)

    def test_exporter_no_production_write_attempts(self) -> None:
        """导出后无生产 pipe 写入尝试。"""
        exporter, bundle = _make_exporter()
        exporter.export_manifest(bundle)
        self.assertEqual(exporter.production_write_attempt_count, 0)

    def test_producer_bundle_hash_valid(self) -> None:
        """ProducerBundleRef 的 bundle_hash 与计算值一致。"""
        bundle = _make_producer_bundle()
        self.assertTrue(bundle.is_hash_valid)
        errors = verify_producer_bundle(bundle)
        self.assertEqual(errors, [])

    def test_frozen_producer_schema_in_manifest(self) -> None:
        """manifest 中 producer_schema 和 producer_version 已冻结。"""
        exporter, bundle = _make_exporter()
        manifest = exporter.export_manifest(bundle)
        self.assertTrue(manifest.producer_schema)
        self.assertTrue(manifest.producer_version)

    def test_read_only_permit_hash_valid(self) -> None:
        """ReadOnlyPermit 的 permit_hash 与计算值一致。"""
        permit = _make_read_only_permit()
        self.assertTrue(permit.is_hash_valid)
        self.assertTrue(permit.write_forbidden)


# ─── Negative vectors (blocker tests) ──────────────────────────────


class CandidateManifestNegativeVectors(unittest.TestCase):
    """blocker tests: 只读约束违反必须 fail-closed。"""

    def test_production_write_back_rejected(self) -> None:
        """生产 pipe 写回尝试 → IN1_PRODUCTION_WRITE_REJECTED。"""
        exporter, bundle = _make_exporter()
        with self.assertRaises(_IntakeError) as ctx:
            exporter.reject_production_write({"data": "should be rejected"})
        self.assertEqual(ctx.exception.code, EC.IN1_PRODUCTION_WRITE_REJECTED)
        # 写入尝试被记录
        self.assertEqual(exporter.production_write_attempt_count, 1)

    def test_mutable_reference_rejected(self) -> None:
        """传入可变 dict 而非冻结 ProducerBundleRef → IN1_MUTABLE_REFERENCE_REJECTED。"""
        exporter, _ = _make_exporter()
        mutable_dict = {
            "bundle_id": "test",
            "producer_schema": "test",
            "producer_version": "1.0",
            "content_sha256": "b" * 64,
            "source_root_hash": "a" * 64,
            "frozen_at": "2026-08-14T00:00:00Z",
        }
        with self.assertRaises(_IntakeError) as ctx:
            exporter.export_manifest(mutable_dict)  # type: ignore[arg-type]
        self.assertEqual(ctx.exception.code, EC.IN1_MUTABLE_REFERENCE_REJECTED)

    def test_missing_artifact_rejected(self) -> None:
        """attempt ref 缺失 ref 或 sha256 → IN1_MISSING_ARTIFACT。"""
        manifest = CandidateManifest(
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="",  # 空 ref = 缺失 artifact
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        result = verify_candidate_manifest(manifest)
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_MISSING_ARTIFACT, result.error_codes)

    def test_missing_export_manifest_ref_rejected(self) -> None:
        """export_manifest_ref_and_hash 缺失 → IN1_MISSING_ARTIFACT。"""
        manifest = CandidateManifest(
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            export_manifest_ref_and_hash={},  # 空 = 缺失
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        result = verify_candidate_manifest(manifest)
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_MISSING_ARTIFACT, result.error_codes)

    def test_source_root_drift_rejected(self) -> None:
        """source root hash 漂移 → IN1_SOURCE_ROOT_DRIFT。"""
        bundle = _make_producer_bundle(source_root_hash="a" * 64)
        permit = _make_read_only_permit(producer_bundle_id=bundle.bundle_id)
        # exporter 的 source_root_hash 与 bundle 不匹配
        exporter = FakeCandidateManifestExporter(
            attempts=_make_valid_attempts(),
            read_only_permit=permit,
            source_root_hash="z" * 64,  # 漂移
        )
        with self.assertRaises(_IntakeError) as ctx:
            exporter.export_manifest(bundle)
        self.assertEqual(ctx.exception.code, EC.IN1_SOURCE_ROOT_DRIFT)

    def test_duplicate_candidate_in_attempt_rejected(self) -> None:
        """同一 attempt 内重复 candidate_id → IN1_DUPLICATE_CANDIDATE_IN_ATTEMPT。"""
        attempts = [
            _make_attempt_data(
                attempt_id="attempt-001",
                candidate_ids=["cand-001", "cand-001"],  # 重复
            ),
        ]
        exporter, bundle = _make_exporter(attempts=attempts)
        with self.assertRaises(_IntakeError) as ctx:
            exporter.export_manifest(bundle)
        self.assertEqual(
            ctx.exception.code, EC.IN1_DUPLICATE_CANDIDATE_IN_ATTEMPT
        )

    def test_producer_schema_not_frozen_rejected(self) -> None:
        """producer schema 为空 → IN1_PRODUCER_SCHEMA_NOT_FROZEN。"""
        manifest = CandidateManifest(
            producer_schema="",  # 空 = 未冻结
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        result = verify_candidate_manifest(manifest)
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN, result.error_codes)

    def test_producer_version_not_frozen_rejected(self) -> None:
        """producer version 为空 → IN1_PRODUCER_SCHEMA_NOT_FROZEN。"""
        manifest = CandidateManifest(
            producer_schema="system/math-producer",
            producer_version="",  # 空 = 未冻结
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        result = verify_candidate_manifest(manifest)
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN, result.error_codes)

    def test_producer_bundle_with_empty_schema_rejected(self) -> None:
        """ProducerBundleRef producer_schema 为空 → verify_producer_bundle 报错。"""
        bundle = ProducerBundleRef(
            bundle_id="test",
            producer_schema="",  # 空
            producer_version="1.0.0",
            content_sha256="b" * 64,
            source_root_hash="a" * 64,
            frozen_at="2026-08-14T00:00:00Z",
        )
        errors = verify_producer_bundle(bundle)
        self.assertTrue(any(e[0] == EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN for e in errors))

    def test_producer_bundle_hash_mismatch_rejected(self) -> None:
        """ProducerBundleRef bundle_hash 不匹配 → IN1_PRODUCER_BUNDLE_INVALID。"""
        bundle = ProducerBundleRef(
            bundle_id="test",
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            content_sha256="b" * 64,
            source_root_hash="a" * 64,
            frozen_at="2026-08-14T00:00:00Z",
            bundle_hash="0" * 64,  # 错误的 hash
        )
        errors = verify_producer_bundle(bundle)
        self.assertTrue(any(e[0] == EC.IN1_PRODUCER_BUNDLE_INVALID for e in errors))

    def test_schema_id_mismatch_rejected(self) -> None:
        """schema_id 不匹配 → SCHEMA_ID_MISMATCH。"""
        manifest = CandidateManifest(
            schema_id="wrong/schema",  # 错误
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        result = verify_candidate_manifest(manifest)
        self.assertFalse(result.passed)
        self.assertIn(EC.SCHEMA_ID_MISMATCH, result.error_codes)

    def test_permit_allowing_writes_rejected(self) -> None:
        """只读许可未禁止写入 → IN1_PRODUCTION_WRITE_REJECTED。"""
        bundle = _make_producer_bundle()
        # 构建一个允许写入的许可（异常情况）
        permit = ReadOnlyPermit(
            permit_id="bad-permit",
            producer_bundle_id=bundle.bundle_id,
            write_forbidden=False,  # 未禁止写入
        )
        exporter = FakeCandidateManifestExporter(
            attempts=_make_valid_attempts(),
            read_only_permit=permit,
            source_root_hash="a" * 64,
        )
        with self.assertRaises(_IntakeError) as ctx:
            exporter.export_manifest(bundle)
        self.assertEqual(ctx.exception.code, EC.IN1_PRODUCTION_WRITE_REJECTED)


# ─── Fault injection ───────────────────────────────────────────────


class CandidateManifestFaultInjection(unittest.TestCase):
    """Fault injection: hash 不匹配必须被检测。"""

    def test_root_hash_mismatch_detected(self) -> None:
        """root_hash 与计算值不匹配 → IN1_ROOT_HASH_MISMATCH。"""
        manifest = CandidateManifest(
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
            root_hash="0" * 64,  # 故意错误的 root hash
        )
        result = verify_candidate_manifest(manifest)
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_ROOT_HASH_MISMATCH, result.error_codes)

    def test_export_manifest_hash_mismatch_detected(self) -> None:
        """export manifest hash 与实际内容不匹配 → IN1_EXPORT_MANIFEST_HASH_MISMATCH。"""
        manifest = CandidateManifest(
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "0" * 64,  # 故意错误的 hash
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        # 计算实际的 export manifest hash
        actual_em_hash = hashlib.sha256(
            canonical_json_bytes(
                [ar.to_dict() for ar in manifest.attempt_refs]
            )
        ).hexdigest()
        result = verify_candidate_manifest(
            manifest,
            expected_export_manifest_sha256=actual_em_hash,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_EXPORT_MANIFEST_HASH_MISMATCH, result.error_codes)

    def test_attempt_ref_hash_mismatch_detected(self) -> None:
        """attempt ref hash 与实际内容不匹配 → IN1_ATTEMPT_REF_HASH_MISMATCH。"""
        manifest = CandidateManifest(
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="0" * 64,  # 故意错误的 hash
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        # 提供实际内容哈希
        actual_hash = hashlib.sha256(
            canonical_json_bytes({"attempt_id": "attempt-001"})
        ).hexdigest()
        result = verify_candidate_manifest(
            manifest,
            attempt_content_hashes={"attempt-001": actual_hash},
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_ATTEMPT_REF_HASH_MISMATCH, result.error_codes)

    def test_empty_root_hash_detected(self) -> None:
        """root_hash 为空 → REQUIRED_FIELD_MISSING。"""
        manifest = CandidateManifest(
            producer_schema="system/math-producer",
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
            root_hash="",  # 空
        )
        result = verify_candidate_manifest(manifest)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_producer_schema_mismatch_with_bundle(self) -> None:
        """manifest 的 producer_schema 与 bundle 不匹配 → IN1_PRODUCER_SCHEMA_NOT_FROZEN。"""
        bundle = _make_producer_bundle(producer_schema="system/math-producer")
        manifest = CandidateManifest(
            producer_schema="different/schema",  # 与 bundle 不匹配
            producer_version="1.0.0",
            export_manifest_ref_and_hash={
                "ref": "export.json",
                "sha256": "c" * 64,
            },
            attempt_refs=(
                AttemptRef(
                    attempt_id="attempt-001",
                    ref="attempts/a1.json",
                    sha256="d" * 64,
                    candidate_ids=("cand-001",),
                ),
            ),
            candidate_ids=("cand-001",),
        )
        manifest = dataclasses.replace(
            manifest, root_hash=manifest.compute_root_hash()
        )
        result = verify_candidate_manifest(manifest, producer_bundle_ref=bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.IN1_PRODUCER_SCHEMA_NOT_FROZEN, result.error_codes)


# ─── Duplicate lineage detection ───────────────────────────────────


class DuplicateLineageDetection(unittest.TestCase):
    """duplicate lineage 检测——同一 candidate_id 跨 attempt 出现。"""

    def test_duplicate_lineage_detected_and_recorded(self) -> None:
        """同一 candidate_id 出现在多个 attempt → 记录在 duplicate_lineage_refs。"""
        attempts = [
            _make_attempt_data(
                attempt_id="attempt-001",
                candidate_ids=["cand-001", "cand-002"],
            ),
            _make_attempt_data(
                attempt_id="attempt-002",
                candidate_ids=["cand-002", "cand-003"],  # cand-002 重复
            ),
        ]
        exporter, bundle = _make_exporter(attempts=attempts)
        manifest = exporter.export_manifest(bundle)

        # duplicate lineage 被检测
        self.assertEqual(len(manifest.duplicate_lineage_refs), 1)
        dl = manifest.duplicate_lineage_refs[0]
        self.assertEqual(dl.candidate_id, "cand-002")
        self.assertEqual(dl.attempt_ids, ("attempt-001", "attempt-002"))

        # 验证器结果中记录了 duplicate lineage count
        result = verify_candidate_manifest(manifest, producer_bundle_ref=bundle)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertEqual(result.duplicate_lineage_count, 1)

    def test_no_duplicate_lineage_when_unique(self) -> None:
        """所有 candidate_id 唯一时 duplicate_lineage_refs 为空。"""
        exporter, bundle = _make_exporter()
        manifest = exporter.export_manifest(bundle)
        self.assertEqual(len(manifest.duplicate_lineage_refs), 0)

    def test_multiple_duplicate_lineages_detected(self) -> None:
        """多个 candidate_id 跨 attempt 重复 → 全部记录。"""
        attempts = [
            _make_attempt_data(
                attempt_id="attempt-001",
                candidate_ids=["cand-001", "cand-002", "cand-003"],
            ),
            _make_attempt_data(
                attempt_id="attempt-002",
                candidate_ids=["cand-001", "cand-002", "cand-004"],
            ),
            _make_attempt_data(
                attempt_id="attempt-003",
                candidate_ids=["cand-001", "cand-005"],
            ),
        ]
        exporter, bundle = _make_exporter(attempts=attempts)
        manifest = exporter.export_manifest(bundle)

        # cand-001 在 3 个 attempt, cand-002 在 2 个 attempt
        self.assertEqual(len(manifest.duplicate_lineage_refs), 2)
        dl_by_id = {dl.candidate_id: dl for dl in manifest.duplicate_lineage_refs}
        self.assertIn("cand-001", dl_by_id)
        self.assertIn("cand-002", dl_by_id)
        self.assertEqual(
            len(dl_by_id["cand-001"].attempt_ids), 3
        )
        self.assertEqual(
            len(dl_by_id["cand-002"].attempt_ids), 2
        )

    def test_duplicate_lineage_with_three_attempts(self) -> None:
        """同一 candidate_id 出现在 3 个 attempt → attempt_ids 包含全部 3 个。"""
        attempts = [
            _make_attempt_data(
                attempt_id="a1",
                candidate_ids=["shared-cand"],
            ),
            _make_attempt_data(
                attempt_id="a2",
                candidate_ids=["shared-cand"],
            ),
            _make_attempt_data(
                attempt_id="a3",
                candidate_ids=["shared-cand"],
            ),
        ]
        exporter, bundle = _make_exporter(attempts=attempts)
        manifest = exporter.export_manifest(bundle)

        self.assertEqual(len(manifest.duplicate_lineage_refs), 1)
        dl = manifest.duplicate_lineage_refs[0]
        self.assertEqual(dl.candidate_id, "shared-cand")
        self.assertEqual(len(dl.attempt_ids), 3)
        self.assertEqual(set(dl.attempt_ids), {"a1", "a2", "a3"})


# ─── ProducerBundleRef 验证 ────────────────────────────────────────


class ProducerBundleRefVerification(unittest.TestCase):
    """ProducerBundleRef 冻结、哈希、版本化验证。"""

    def test_valid_bundle_passes(self) -> None:
        """有效的 ProducerBundleRef 通过验证。"""
        bundle = _make_producer_bundle()
        errors = verify_producer_bundle(bundle)
        self.assertEqual(errors, [])

    def test_dict_rejected_as_mutable(self) -> None:
        """dict 而非 ProducerBundleRef → IN1_MUTABLE_REFERENCE_REJECTED。"""
        errors = verify_producer_bundle({"bundle_id": "test"})  # type: ignore[arg-type]
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0][0], EC.IN1_MUTABLE_REFERENCE_REJECTED)

    def test_frozen_dataclass_is_immutable(self) -> None:
        """ProducerBundleRef 是 frozen dataclass，不可变。"""
        bundle = _make_producer_bundle()
        with self.assertRaises(dataclasses.FrozenInstanceError):
            bundle.producer_schema = "modified"  # type: ignore[misc]

    def test_candidate_manifest_is_immutable(self) -> None:
        """CandidateManifest 是 frozen dataclass，不可变。"""
        exporter, bundle = _make_exporter()
        manifest = exporter.export_manifest(bundle)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            manifest.producer_schema = "modified"  # type: ignore[misc]

    def test_attempt_ref_is_immutable(self) -> None:
        """AttemptRef 是 frozen dataclass，不可变。"""
        ar = AttemptRef(
            attempt_id="a1",
            ref="attempts/a1.json",
            sha256="d" * 64,
            candidate_ids=("c1",),
        )
        with self.assertRaises(dataclasses.FrozenInstanceError):
            ar.attempt_id = "modified"  # type: ignore[misc]


# ─── 零写入收据验证 ────────────────────────────────────────────────


class ZeroWriteReceiptVerification(unittest.TestCase):
    """零写入收据验证。"""

    def test_zero_write_receipt_is_zero(self) -> None:
        """零写入收据所有计数为 0。"""
        receipt = make_zero_write_receipt(
            export_id="export-001",
            producer_bundle_id="bundle-001",
        )
        self.assertTrue(receipt.is_zero_write)
        self.assertTrue(receipt.is_hash_valid)

    def test_zero_write_receipt_hash_valid(self) -> None:
        """零写入收据的 receipt_hash 与计算值一致。"""
        receipt = make_zero_write_receipt(
            export_id="export-001",
            producer_bundle_id="bundle-001",
        )
        self.assertEqual(
            receipt.receipt_hash, receipt.compute_receipt_hash()
        )


if __name__ == "__main__":
    unittest.main()
