"""WP-IN1 只读 CandidateManifest / exporter / duplicate lineage。

本包实现 IN1 工作包：
- 只读 CandidateManifest 对象与验证器
- ReadOnlyCandidateManifestExporter 导出协议
- ProducerBundleRef（冻结、哈希、版本化的外部 system/ producer 引用）
- Duplicate lineage 检测
- 零写入收据

关键约束：
- READ-ONLY：不写生产 pipe、不写 DB、不写 Redis、不写 D 盘
- system/ 是外部 producer，不是 Python 依赖——只能通过冻结、哈希、版本化 bundle 接入
- SIDE_EFFECT_FREE：测试套件中无真实连接
"""

from .producer_bundle import (
    ProducerBundleRef,
    make_producer_bundle_ref,
    verify_producer_bundle,
)
from .candidate_manifest import (
    AttemptRef,
    CandidateManifest,
    DuplicateLineageRef,
    CandidateManifestVerificationResult,
    verify_candidate_manifest,
)
from .exporter import (
    ReadOnlyPermit,
    make_read_only_permit,
    ZeroWriteReceipt,
    make_zero_write_receipt,
    CandidateManifestExporterPort,
    FakeCandidateManifestExporter,
    _IntakeError,
)

__all__ = [
    "ProducerBundleRef",
    "make_producer_bundle_ref",
    "verify_producer_bundle",
    "AttemptRef",
    "CandidateManifest",
    "DuplicateLineageRef",
    "CandidateManifestVerificationResult",
    "verify_candidate_manifest",
    "ReadOnlyPermit",
    "make_read_only_permit",
    "ZeroWriteReceipt",
    "make_zero_write_receipt",
    "CandidateManifestExporterPort",
    "FakeCandidateManifestExporter",
    "_IntakeError",
]
