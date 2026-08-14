"""Artifact seal 协议 — live → partial → seal。

扩展 CompletionArtifactStore，实现 WP-VLT0 的 artifact bundle 封存协议：

  writer live root
  → WRITERS_DRAINED
  → copy to <attempt>.partial
  → validate files/size/schema/hash
  → artifact_manifest.json
  → DB fenced transaction records durable CommitIntent
  → fsync COMMITTED marker + directory
  → atomic rename to content-addressed final bundle
  → DB fenced transaction writes ArtifactRef + COMMITTED + outbox + permit consumption
  → queue ACK

SIDE_EFFECT_FREE：不接触真实 DB。CommitIntent 在内存中模拟。
复用 GV0 CompletionArtifactStore 的 CAS 核心做最终 seal。
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import SEAL_STATES, VerificationErrorCode as EC
from ..storage.artifact_store import CompletionArtifactStore, ArtifactRef


@dataclass
class CommitIntent:
    """Durable CommitIntent — 在 final rename 前持久化。

    绑定 job、attempt、input hashes、manifest hash、
    预期 terminal、目标 CAS URI、authorization/permit hash 和 expiry。
    """

    intent_id: str
    job_id: str
    attempt_id: str
    input_hash: str
    manifest_hash: str
    expected_terminal: str
    target_cas_uri: str
    authorization_hash: str
    permit_hash: str
    fence_token: int
    expiry: str
    created_at: str
    consumed: bool = False
    revoked: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "intent_id": self.intent_id,
            "job_id": self.job_id,
            "attempt_id": self.attempt_id,
            "input_hash": self.input_hash,
            "manifest_hash": self.manifest_hash,
            "expected_terminal": self.expected_terminal,
            "target_cas_uri": self.target_cas_uri,
            "authorization_hash": self.authorization_hash,
            "permit_hash": self.permit_hash,
            "fence_token": self.fence_token,
            "expiry": self.expiry,
            "created_at": self.created_at,
            "consumed": self.consumed,
            "revoked": self.revoked,
        }


@dataclass
class ArtifactManifest:
    """Artifact bundle manifest。"""

    manifest_id: str
    job_id: str
    attempt_id: str
    files: list[dict[str, Any]] = field(default_factory=list)
    total_size_bytes: int = 0
    schema_id: str = ""
    manifest_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "manifest_id": self.manifest_id,
            "job_id": self.job_id,
            "attempt_id": self.attempt_id,
            "files": list(self.files),
            "total_size_bytes": self.total_size_bytes,
            "schema_id": self.schema_id,
            "manifest_hash": self.manifest_hash,
        }

    @classmethod
    def build(
        cls,
        *,
        manifest_id: str,
        job_id: str,
        attempt_id: str,
        files: list[dict[str, Any]],
        schema_id: str = "",
    ) -> "ArtifactManifest":
        """构建 manifest 并计算 hash。"""
        total_size = sum(f.get("size_bytes", 0) for f in files)
        manifest = cls(
            manifest_id=manifest_id,
            job_id=job_id,
            attempt_id=attempt_id,
            files=files,
            total_size_bytes=total_size,
            schema_id=schema_id,
            manifest_hash="",
        )
        d = manifest.to_dict()
        d["manifest_hash"] = None
        manifest.manifest_hash = hashlib.sha256(canonical_json_bytes(d)).hexdigest()
        return manifest


class ArtifactSealProtocol:
    """live → partial → seal 协议。

    SIDE_EFFECT_FREE：纯内存模拟 CommitIntent 和 writer 状态。
    最终 seal 复用 GV0 CompletionArtifactStore CAS 核心。
    """

    def __init__(self, artifact_store: CompletionArtifactStore) -> None:
        self._store = artifact_store
        self._intents: dict[str, CommitIntent] = {}
        self._live_writers: dict[str, bool] = {}  # job_id → alive
        self._partial_manifests: dict[str, ArtifactManifest] = {}  # attempt_id → manifest
        self._sealed_refs: dict[str, ArtifactRef] = {}  # attempt_id → ArtifactRef

    @property
    def store(self) -> CompletionArtifactStore:
        return self._store

    def start_live_writer(self, job_id: str) -> None:
        """标记一个 live writer 为活跃。"""
        self._live_writers[job_id] = True

    def drain_writer(self, job_id: str) -> None:
        """标记 writer 已 drained。"""
        self._live_writers[job_id] = False

    def is_writer_alive(self, job_id: str) -> bool:
        return self._live_writers.get(job_id, False)

    def record_commit_intent(self, intent: CommitIntent) -> None:
        """记录 durable CommitIntent。"""
        if intent.intent_id in self._intents:
            raise _SealError(EC.SEAL_COMMIT_INTENT_MISSING, f"intent {intent.intent_id} already exists")
        self._intents[intent.intent_id] = intent

    def revoke_intent(self, intent_id: str) -> None:
        """撤销一个 CommitIntent。"""
        intent = self._intents.get(intent_id)
        if intent is None:
            raise _SealError(EC.SEAL_COMMIT_INTENT_MISSING, f"intent {intent_id} not found")
        intent.revoked = True

    def get_intent(self, intent_id: str) -> CommitIntent | None:
        return self._intents.get(intent_id)

    def create_partial(
        self,
        *,
        job_id: str,
        attempt_id: str,
        files: list[dict[str, Any]],
        schema_id: str = "",
    ) -> ArtifactManifest:
        """从 live writer 创建 partial bundle。

        前提：writer 已 drained。
        """
        if self.is_writer_alive(job_id):
            raise _SealError(EC.SEAL_LIVE_WRITER_STILL_ACTIVE,
                             f"writer for job {job_id} is still alive, cannot create partial")

        manifest = ArtifactManifest.build(
            manifest_id=f"manifest-{attempt_id}",
            job_id=job_id,
            attempt_id=attempt_id,
            files=files,
            schema_id=schema_id,
        )
        self._partial_manifests[attempt_id] = manifest
        return manifest

    def get_partial(self, attempt_id: str) -> ArtifactManifest | None:
        return self._partial_manifests.get(attempt_id)

    def seal(
        self,
        *,
        attempt_id: str,
        intent_id: str,
        bundle_content: bytes,
        current_time: str,
        current_fence: int,
    ) -> ArtifactRef:
        """将 partial bundle seal 为最终 content-addressed bundle。

        步骤：
        1. 检查 partial 存在
        2. 检查未重复 seal
        3. 检查 CommitIntent 存在、未消耗、未撤销
        4. 检查 fence 有效
        5. 检查 intent 未过期
        6. 验证 manifest hash
        7. 写入 CAS（复用 GV0 CompletionArtifactStore）
        8. 标记 intent consumed
        """
        # 1. partial 存在
        manifest = self._partial_manifests.get(attempt_id)
        if manifest is None:
            raise _SealError(EC.SEAL_PARTIAL_INCOMPLETE,
                             f"no partial bundle for attempt {attempt_id}")

        # 2. 未重复 seal
        if attempt_id in self._sealed_refs:
            raise _SealError(EC.SEAL_ALREADY_SEALED,
                             f"attempt {attempt_id} already sealed")

        # 3. CommitIntent
        intent = self._intents.get(intent_id)
        if intent is None:
            raise _SealError(EC.SEAL_COMMIT_INTENT_MISSING,
                             f"CommitIntent {intent_id} not found")
        if intent.consumed:
            raise _SealError(EC.SEAL_COMMIT_INTENT_MISSING,
                             f"CommitIntent {intent_id} already consumed")
        if intent.revoked:
            raise _SealError(EC.SEAL_COMMIT_INTENT_MISSING,
                             f"CommitIntent {intent_id} revoked")

        # 4. fence
        if intent.fence_token != current_fence:
            raise _SealError(EC.SEAL_FENCE_STALE,
                             f"fence mismatch: intent has {intent.fence_token}, current is {current_fence}")

        # 5. 过期
        if current_time >= intent.expiry:
            raise _SealError(EC.SEAL_COMMIT_INTENT_MISSING,
                             f"CommitIntent expired: current {current_time} >= expiry {intent.expiry}")

        # 6. manifest hash 验证
        bundle_dict = json.loads(bundle_content) if isinstance(bundle_content, bytes) else bundle_content
        if isinstance(bundle_dict, dict):
            bundle_manifest_hash = bundle_dict.get("manifest_hash", "")
            if bundle_manifest_hash and bundle_manifest_hash != manifest.manifest_hash:
                raise _SealError(EC.SEAL_MANIFEST_HASH_MISMATCH,
                                 f"manifest hash mismatch: bundle has {bundle_manifest_hash}, "
                                 f"partial has {manifest.manifest_hash}")

        # 7. 写入 CAS — 复用 GV0 核心
        ref = self._store.put_bytes(bundle_content if isinstance(bundle_content, bytes) else canonical_json_bytes(bundle_content))

        # 8. 标记 consumed
        intent.consumed = True
        self._sealed_refs[attempt_id] = ref

        return ref

    def get_sealed_ref(self, attempt_id: str) -> ArtifactRef | None:
        return self._sealed_refs.get(attempt_id)

    def get_seal_state(self, attempt_id: str) -> str:
        """获取 attempt 的 seal 状态。"""
        if attempt_id in self._sealed_refs:
            return "SEALED"
        if attempt_id in self._partial_manifests:
            return "PARTIAL"
        return "MISSING"


class _SealError(Exception):
    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)
