"""RuntimeCheckpoint — P9 checkpoint for recovery。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

P9 RuntimeCheckpoint 包含状态快照 + hash。允许从 checkpoint replay。

关键约束（blocker）：
- checkpoint hash 不匹配 → VR_CHECKPOINT_HASH_MISMATCH
- checkpoint 无效 → VR_RUNTIME_CHECKPOINT_INVALID

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


_SCHEMA_ID = "seven/verdict-runtime-checkpoint"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-checkpoint_hash-null)"

# Checkpoint 状态
CHECKPOINT_STATES: frozenset[str] = frozenset(
    {"RECORDED", "VERIFIED", "RECOVERED", "INCOMPLETE"}
)


@dataclass(frozen=True)
class VerdictCheckpoint:
    """P9 verdict checkpoint — 状态快照 + hash。

    字段：
        checkpoint_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        verdict_hash: MachineVerdict content_hash
        gate_verdict_hash: SixGateVerdict content_hash
        evidence_index_hash: EvidenceIndex content_hash
        replay_hash: EvidenceReplay content_hash
        state_snapshot: 状态快照（各阶段 sealed 状态）
        created_at: 创建时间
        state: checkpoint 状态
        hash_algorithm: 哈希算法
        checkpoint_hash: checkpoint 自身内容哈希
    """

    checkpoint_id: str
    dag_hash: str = ""
    verdict_hash: str = ""
    gate_verdict_hash: str = ""
    evidence_index_hash: str = ""
    replay_hash: str = ""
    state_snapshot: tuple[tuple[str, str], ...] = ()
    created_at: str = ""
    state: str = "RECORDED"
    hash_algorithm: str = _HASH_ALGORITHM
    checkpoint_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "checkpoint_id": self.checkpoint_id,
            "dag_hash": self.dag_hash,
            "verdict_hash": self.verdict_hash,
            "gate_verdict_hash": self.gate_verdict_hash,
            "evidence_index_hash": self.evidence_index_hash,
            "replay_hash": self.replay_hash,
            "state_snapshot": [list(item) for item in self.state_snapshot],
            "created_at": self.created_at,
            "state": self.state,
            "hash_algorithm": self.hash_algorithm,
            "checkpoint_hash": self.checkpoint_hash,
        }

    def compute_checkpoint_hash(self) -> str:
        d = self.to_dict()
        d["checkpoint_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.checkpoint_hash == self.compute_checkpoint_hash()

    @property
    def is_verified(self) -> bool:
        return self.state == "VERIFIED"

    @property
    def is_recovered(self) -> bool:
        return self.state == "RECOVERED"


def make_verdict_checkpoint(
    *,
    checkpoint_id: str,
    dag_hash: str,
    verdict_hash: str,
    gate_verdict_hash: str,
    evidence_index_hash: str,
    replay_hash: str,
    state_snapshot: dict[str, str] | None = None,
    created_at: str | None = None,
) -> VerdictCheckpoint:
    """构建 P9 verdict checkpoint。"""
    created_at = created_at or datetime.now(timezone.utc).isoformat()
    snapshot_tuple = tuple(
        sorted((k, v) for k, v in (state_snapshot or {}).items())
    )
    checkpoint = VerdictCheckpoint(
        checkpoint_id=checkpoint_id,
        dag_hash=dag_hash,
        verdict_hash=verdict_hash,
        gate_verdict_hash=gate_verdict_hash,
        evidence_index_hash=evidence_index_hash,
        replay_hash=replay_hash,
        state_snapshot=snapshot_tuple,
        created_at=created_at,
        state="RECORDED",
    )
    return dataclasses.replace(
        checkpoint, checkpoint_hash=checkpoint.compute_checkpoint_hash()
    )


def verify_verdict_checkpoint(
    checkpoint: VerdictCheckpoint,
) -> VerificationResult:
    """验证 P9 verdict checkpoint。

    blocker：
    - checkpoint hash 不匹配 → VR_CHECKPOINT_HASH_MISMATCH
    - 状态不在合法集合 → VR_RUNTIME_CHECKPOINT_INVALID
    - 必要字段缺失 → REQUIRED_FIELD_MISSING
    """
    errors: list[EC] = []
    details: list[str] = []

    d = checkpoint.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not checkpoint.checkpoint_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("checkpoint_id is empty")

    if not checkpoint.dag_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dag_hash is empty")

    if not checkpoint.verdict_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("verdict_hash is empty")

    if not checkpoint.gate_verdict_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("gate_verdict_hash is empty")

    if not checkpoint.evidence_index_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("evidence_index_hash is empty")

    if not checkpoint.replay_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("replay_hash is empty")

    if checkpoint.state not in CHECKPOINT_STATES:
        errors.append(EC.VR_RUNTIME_CHECKPOINT_INVALID)
        details.append(
            f"checkpoint state {checkpoint.state} not in "
            f"{sorted(CHECKPOINT_STATES)}"
        )

    if not checkpoint.created_at:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("created_at is empty")

    # checkpoint_hash
    if not checkpoint.checkpoint_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("checkpoint_hash is empty")
    elif checkpoint.checkpoint_hash != checkpoint.compute_checkpoint_hash():
        errors.append(EC.VR_CHECKPOINT_HASH_MISMATCH)
        details.append("VerdictCheckpoint checkpoint_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


def verify_checkpoint_against_hashes(
    checkpoint: VerdictCheckpoint,
    *,
    verdict_hash: str,
    gate_verdict_hash: str,
    evidence_index_hash: str,
    replay_hash: str,
    dag_hash: str,
) -> VerificationResult:
    """验证 checkpoint 与实际 hash 一致（用于 replay 恢复）。"""
    errors: list[EC] = []
    details: list[str] = []

    if checkpoint.dag_hash != dag_hash:
        errors.append(EC.VR_CHECKPOINT_HASH_MISMATCH)
        details.append(
            f"dag_hash mismatch: checkpoint={checkpoint.dag_hash}, "
            f"actual={dag_hash}"
        )
    if checkpoint.verdict_hash != verdict_hash:
        errors.append(EC.VR_CHECKPOINT_HASH_MISMATCH)
        details.append(
            f"verdict_hash mismatch: checkpoint={checkpoint.verdict_hash}, "
            f"actual={verdict_hash}"
        )
    if checkpoint.gate_verdict_hash != gate_verdict_hash:
        errors.append(EC.VR_CHECKPOINT_HASH_MISMATCH)
        details.append(
            f"gate_verdict_hash mismatch: "
            f"checkpoint={checkpoint.gate_verdict_hash}, "
            f"actual={gate_verdict_hash}"
        )
    if checkpoint.evidence_index_hash != evidence_index_hash:
        errors.append(EC.VR_CHECKPOINT_HASH_MISMATCH)
        details.append(
            f"evidence_index_hash mismatch: "
            f"checkpoint={checkpoint.evidence_index_hash}, "
            f"actual={evidence_index_hash}"
        )
    if checkpoint.replay_hash != replay_hash:
        errors.append(EC.VR_CHECKPOINT_HASH_MISMATCH)
        details.append(
            f"replay_hash mismatch: checkpoint={checkpoint.replay_hash}, "
            f"actual={replay_hash}"
        )

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )
