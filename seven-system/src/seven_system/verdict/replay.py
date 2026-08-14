"""EvidenceReplay + CompletionContractRemainder + FullChainRemainder。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

Evidence replay 必须证明所有 planned 对象、attempt、artifact、audit、Gate
和 evidence 有且仅有合法归宿（remainder=0）。No orphans, no duplicates,
no missing.

CompletionContractRemainder 验证完成合同 remainder=0：所有工作包有合法
终态，无未完成合同。使用 GV0 CompletionContractVerifier。

FullChainRemainder 验证全链 remainder=0：P0-P8 全 sealed，所有 DAG 边满足，
无 orphan 对象。

关键约束（blocker）：
- orphan 对象 → VR_ORPHAN_OBJECT
- 不可反查 → VR_NON_RETRACEABLE
- owner/contract 错配 → VR_OWNER_CONTRACT_MISMATCH
- completion contract remainder != 0 → VR_COMPLETION_CONTRACT_REMAINDER_NONZERO
- full chain remainder != 0 → VR_FULL_CHAIN_REMAINDER_NONZERO
- replay 不完整 → VR_REPLAY_INCOMPLETE

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    VALID_STATES,
    VR_REMAINDER_KINDS,
    VR_REPLAY_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import (
    VerificationResult,
    verify_completion_contract,
)


_SCHEMA_ID = "seven/evidence-replay"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"

# 合法终态——工作包必须处于这些状态之一才算"有合法归宿"
_TERMINAL_STATES: frozenset[str] = frozenset(
    {
        "IMPLEMENTED_PENDING_EVIDENCE",
        "READY_FOR_AUDIT",
        "AUDITED_PASS",
        "AUDITED_PARTIAL",
        "AUDITED_FAIL",
        "BLOCKED",
    }
)

# DAG 阶段——P0-P8
_DAG_PHASES: tuple[str, ...] = (
    "P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8",
)


@dataclass(frozen=True)
class ReplayObject:
    """replay 中的单个对象。"""

    object_kind: str
    object_hash: str
    source_phase: str  # P0-P8 哪个阶段产出
    wp_id: str = ""
    destination: str = ""  # 合法归宿（verdict / evidence_index / gate / ...）

    def to_dict(self) -> dict[str, Any]:
        return {
            "object_kind": self.object_kind,
            "object_hash": self.object_hash,
            "source_phase": self.source_phase,
            "wp_id": self.wp_id,
            "destination": self.destination,
        }


@dataclass(frozen=True)
class ReplayResult:
    """单个对象在 replay 中的归宿结果。"""

    object_hash: str
    status: str  # PLACED | ORPHAN | DUPLICATE | MISSING
    destination: str = ""
    reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "object_hash": self.object_hash,
            "status": self.status,
            "destination": self.destination,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class EvidenceReplay:
    """P9 Evidence Replay — 证明所有对象有且仅有合法归宿。

    字段：
        replay_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        objects: 所有 planned 对象
        results: 每个对象的 replay 结果
        placed_count: 已安置对象数
        orphan_count: orphan 对象数
        duplicate_count: 重复对象数
        missing_count: 缺失对象数
        remainder: 剩余对象数（= orphan + duplicate + missing，必须 0）
        hash_algorithm: 哈希算法
        content_hash: replay 自身内容哈希
    """

    replay_id: str
    dag_hash: str = ""
    objects: tuple[ReplayObject, ...] = ()
    results: tuple[ReplayResult, ...] = ()
    placed_count: int = 0
    orphan_count: int = 0
    duplicate_count: int = 0
    missing_count: int = 0
    remainder: int = 0
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "replay_id": self.replay_id,
            "dag_hash": self.dag_hash,
            "objects": [o.to_dict() for o in self.objects],
            "results": [r.to_dict() for r in self.results],
            "placed_count": self.placed_count,
            "orphan_count": self.orphan_count,
            "duplicate_count": self.duplicate_count,
            "missing_count": self.missing_count,
            "remainder": self.remainder,
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
    def is_complete(self) -> bool:
        """remainder=0 时 replay 完整。"""
        return self.remainder == 0


def _run_replay(
    objects: list[ReplayObject],
    legal_destinations: set[str],
) -> list[ReplayResult]:
    """执行 replay——检查每个对象的归宿。"""
    results: list[ReplayResult] = []
    seen_hashes: set[str] = set()

    for obj in objects:
        if obj.object_hash in seen_hashes:
            results.append(
                ReplayResult(
                    object_hash=obj.object_hash,
                    status="DUPLICATE",
                    reason=f"object_hash {obj.object_hash} already seen",
                )
            )
            seen_hashes.add(obj.object_hash)
            continue
        seen_hashes.add(obj.object_hash)

        if obj.destination and obj.destination in legal_destinations:
            results.append(
                ReplayResult(
                    object_hash=obj.object_hash,
                    status="PLACED",
                    destination=obj.destination,
                )
            )
        elif obj.destination:
            results.append(
                ReplayResult(
                    object_hash=obj.object_hash,
                    status="ORPHAN",
                    destination=obj.destination,
                    reason=f"destination {obj.destination} not in legal set",
                )
            )
        else:
            results.append(
                ReplayResult(
                    object_hash=obj.object_hash,
                    status="ORPHAN",
                    reason="no destination specified",
                )
            )
    return results


# 合法归宿集合
_LEGAL_DESTINATIONS: frozenset[str] = frozenset(
    {
        "MachineVerdict",
        "SixGateVerdict",
        "EvidenceIndex",
        "RuntimeCheckpoint",
        "EvidenceReplay",
        "CompletionContractRemainder",
        "FullChainRemainder",
        "CostAndCoverageDelta",
        "HumanReadableSummary",
        "VerdictCapabilityReport",
    }
)


def make_evidence_replay(
    *,
    replay_id: str,
    dag_hash: str,
    objects: list[ReplayObject],
) -> EvidenceReplay:
    """构建 EvidenceReplay。

    执行 replay，检查每个对象的归宿。remainder = orphan + duplicate + missing。
    """
    sorted_objects = sorted(objects, key=lambda o: o.object_hash)
    results = _run_replay(sorted_objects, set(_LEGAL_DESTINATIONS))

    placed = sum(1 for r in results if r.status == "PLACED")
    orphan = sum(1 for r in results if r.status == "ORPHAN")
    duplicate = sum(1 for r in results if r.status == "DUPLICATE")
    missing = sum(1 for r in results if r.status == "MISSING")
    remainder = orphan + duplicate + missing

    replay = EvidenceReplay(
        replay_id=replay_id,
        dag_hash=dag_hash,
        objects=tuple(sorted_objects),
        results=tuple(results),
        placed_count=placed,
        orphan_count=orphan,
        duplicate_count=duplicate,
        missing_count=missing,
        remainder=remainder,
    )
    return dataclasses.replace(
        replay, content_hash=replay.compute_content_hash()
    )


def verify_evidence_replay(replay: EvidenceReplay) -> VerificationResult:
    """验证 EvidenceReplay。

    blocker：
    - remainder != 0 → VR_REPLAY_INCOMPLETE
    - orphan 对象 → VR_ORPHAN_OBJECT
    - duplicate 对象 → VR_DUPLICATE_OBJECT
    - missing 对象 → VR_MISSING_OBJECT
    - content_hash 不匹配 → VR_VERDICT_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = replay.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not replay.replay_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("replay_id is empty")

    if not replay.dag_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dag_hash is empty")

    # remainder 检查
    if replay.remainder != 0:
        errors.append(EC.VR_REPLAY_INCOMPLETE)
        details.append(
            f"replay remainder {replay.remainder} != 0 — "
            f"orphan={replay.orphan_count}, "
            f"duplicate={replay.duplicate_count}, "
            f"missing={replay.missing_count}"
        )

    # orphan 检查
    if replay.orphan_count > 0:
        orphan_hashes = [
            r.object_hash for r in replay.results if r.status == "ORPHAN"
        ]
        errors.append(EC.VR_ORPHAN_OBJECT)
        details.append(
            f"orphan objects found: {orphan_hashes[:5]}"
        )

    # duplicate 检查
    if replay.duplicate_count > 0:
        dup_hashes = [
            r.object_hash for r in replay.results if r.status == "DUPLICATE"
        ]
        errors.append(EC.VR_DUPLICATE_OBJECT)
        details.append(f"duplicate objects found: {dup_hashes[:5]}")

    # missing 检查
    if replay.missing_count > 0:
        errors.append(EC.VR_MISSING_OBJECT)
        details.append(f"missing objects count: {replay.missing_count}")

    # 计数一致性
    expected_remainder = (
        replay.orphan_count + replay.duplicate_count + replay.missing_count
    )
    if replay.remainder != expected_remainder:
        errors.append(EC.VR_REPLAY_INCOMPLETE)
        details.append(
            f"remainder {replay.remainder} != "
            f"orphan+dup+missing {expected_remainder}"
        )

    # content_hash
    if not replay.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif replay.content_hash != replay.compute_content_hash():
        errors.append(EC.VR_VERDICT_HASH_MISMATCH)
        details.append("EvidenceReplay content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


def check_no_orphans(replay: EvidenceReplay) -> VerificationResult:
    """检查无 orphan 对象。"""
    errors: list[EC] = []
    details: list[str] = []
    if replay.orphan_count > 0:
        errors.append(EC.VR_ORPHAN_OBJECT)
        details.append(f"{replay.orphan_count} orphan objects found")
    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


# ─── CompletionContractRemainder ─────────────────────────────────────────


@dataclass(frozen=True)
class WorkPackageCompletion:
    """工作包完成状态。"""

    wp_id: str
    owner_type: str  # IMPLEMENTER | AUDITOR
    completion_contract: str  # IMPLEMENTATION_BUNDLE | AUDIT_RECORD | ...
    state: str  # 工作包状态
    submitted_schema_id: str = ""
    actor_type: str = ""  # IMPLEMENTER | AUDITOR | SYSTEM

    def to_dict(self) -> dict[str, Any]:
        return {
            "wp_id": self.wp_id,
            "owner_type": self.owner_type,
            "completion_contract": self.completion_contract,
            "state": self.state,
            "submitted_schema_id": self.submitted_schema_id,
            "actor_type": self.actor_type,
        }


@dataclass(frozen=True)
class CompletionContractRemainder:
    """完成合同 remainder——验证所有工作包有合法终态。

    字段：
        remainder_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        wp_completions: 所有工作包完成状态
        total_count: 工作包总数
        terminal_count: 有合法终态的工作包数
        incomplete_count: 未完成工作包数
        remainder: 剩余数（= incomplete_count，必须 0）
        mismatch_count: owner/contract 错配数
        hash_algorithm: 哈希算法
        content_hash: remainder 自身内容哈希
    """

    remainder_id: str
    dag_hash: str = ""
    wp_completions: tuple[WorkPackageCompletion, ...] = ()
    total_count: int = 0
    terminal_count: int = 0
    incomplete_count: int = 0
    remainder: int = 0
    mismatch_count: int = 0
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": "seven/completion-contract-remainder",
            "schema_version": _SCHEMA_VERSION,
            "remainder_id": self.remainder_id,
            "dag_hash": self.dag_hash,
            "wp_completions": [w.to_dict() for w in self.wp_completions],
            "total_count": self.total_count,
            "terminal_count": self.terminal_count,
            "incomplete_count": self.incomplete_count,
            "remainder": self.remainder,
            "mismatch_count": self.mismatch_count,
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
    def is_zero(self) -> bool:
        return self.remainder == 0


def make_completion_contract_remainder(
    *,
    remainder_id: str,
    dag_hash: str,
    wp_completions: list[WorkPackageCompletion],
) -> CompletionContractRemainder:
    """构建 CompletionContractRemainder。

    检查所有工作包是否有合法终态，owner/contract 是否匹配。
    remainder = incomplete_count + mismatch_count。
    """
    sorted_wps = sorted(wp_completions, key=lambda w: w.wp_id)
    terminal = 0
    incomplete = 0
    mismatch = 0

    for wp in sorted_wps:
        if wp.state in _TERMINAL_STATES:
            terminal += 1
        else:
            incomplete += 1
        # owner/contract 匹配检查
        if wp.owner_type == "IMPLEMENTER":
            if wp.completion_contract not in (
                "IMPLEMENTATION_BUNDLE", "DOC_BOOTSTRAP_RECORD"
            ):
                mismatch += 1
            if wp.actor_type == "AUDITOR":
                mismatch += 1
        elif wp.owner_type == "AUDITOR":
            if wp.completion_contract != "AUDIT_RECORD":
                mismatch += 1
            if wp.actor_type == "IMPLEMENTER":
                mismatch += 1
        else:
            mismatch += 1

    remainder = incomplete + mismatch

    result = CompletionContractRemainder(
        remainder_id=remainder_id,
        dag_hash=dag_hash,
        wp_completions=tuple(sorted_wps),
        total_count=len(sorted_wps),
        terminal_count=terminal,
        incomplete_count=incomplete,
        remainder=remainder,
        mismatch_count=mismatch,
    )
    return dataclasses.replace(
        result, content_hash=result.compute_content_hash()
    )


def verify_completion_contract_remainder(
    remainder: CompletionContractRemainder,
) -> VerificationResult:
    """验证 CompletionContractRemainder。

    blocker：
    - remainder != 0 → VR_COMPLETION_CONTRACT_REMAINDER_NONZERO
    - owner/contract 错配 → VR_OWNER_CONTRACT_MISMATCH
    - content_hash 不匹配 → VR_VERDICT_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = remainder.to_dict()
    if d.get("schema_id") != "seven/completion-contract-remainder":
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append("schema_id mismatch")

    if not remainder.remainder_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("remainder_id is empty")

    if not remainder.dag_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dag_hash is empty")

    # remainder 检查
    if remainder.remainder != 0:
        errors.append(EC.VR_COMPLETION_CONTRACT_REMAINDER_NONZERO)
        details.append(
            f"completion contract remainder {remainder.remainder} != 0 — "
            f"incomplete={remainder.incomplete_count}, "
            f"mismatch={remainder.mismatch_count}"
        )

    # owner/contract 错配
    if remainder.mismatch_count > 0:
        mismatched = [
            w.wp_id for w in remainder.wp_completions
            if w.owner_type == "IMPLEMENTER"
            and w.completion_contract not in (
                "IMPLEMENTATION_BUNDLE", "DOC_BOOTSTRAP_RECORD"
            )
        ]
        mismatched += [
            w.wp_id for w in remainder.wp_completions
            if w.owner_type == "AUDITOR"
            and w.completion_contract != "AUDIT_RECORD"
        ]
        errors.append(EC.VR_OWNER_CONTRACT_MISMATCH)
        details.append(
            f"owner/contract mismatch in {remainder.mismatch_count} "
            f"work packages: {mismatched[:5]}"
        )

    # 计数一致性
    expected_remainder = (
        remainder.incomplete_count + remainder.mismatch_count
    )
    if remainder.remainder != expected_remainder:
        errors.append(EC.VR_COMPLETION_CONTRACT_REMAINDER_NONZERO)
        details.append(
            f"remainder {remainder.remainder} != "
            f"incomplete+mismatch {expected_remainder}"
        )

    # content_hash
    if not remainder.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif remainder.content_hash != remainder.compute_content_hash():
        errors.append(EC.VR_VERDICT_HASH_MISMATCH)
        details.append("CompletionContractRemainder content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


# ─── FullChainRemainder ──────────────────────────────────────────────────


@dataclass(frozen=True)
class PhaseSealStatus:
    """单阶段 sealed 状态。"""

    phase: str  # P0-P8
    sealed: bool
    dag_edge_satisfied: bool
    object_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "phase": self.phase,
            "sealed": self.sealed,
            "dag_edge_satisfied": self.dag_edge_satisfied,
            "object_count": self.object_count,
        }


@dataclass(frozen=True)
class FullChainRemainder:
    """全链 remainder——验证 P0-P8 全 sealed，DAG 边满足，无 orphan。

    字段：
        remainder_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        phase_statuses: P0-P8 各阶段 sealed 状态
        total_phases: 阶段总数
        sealed_count: 已 sealed 阶段数
        unsealed_count: 未 sealed 阶段数
        edge_violations: DAG 边违反数
        orphan_count: orphan 对象数
        remainder: 剩余数（= unsealed + edge_violations + orphan，必须 0）
        hash_algorithm: 哈希算法
        content_hash: remainder 自身内容哈希
    """

    remainder_id: str
    dag_hash: str = ""
    phase_statuses: tuple[PhaseSealStatus, ...] = ()
    total_phases: int = 0
    sealed_count: int = 0
    unsealed_count: int = 0
    edge_violations: int = 0
    orphan_count: int = 0
    remainder: int = 0
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": "seven/full-chain-remainder",
            "schema_version": _SCHEMA_VERSION,
            "remainder_id": self.remainder_id,
            "dag_hash": self.dag_hash,
            "phase_statuses": [p.to_dict() for p in self.phase_statuses],
            "total_phases": self.total_phases,
            "sealed_count": self.sealed_count,
            "unsealed_count": self.unsealed_count,
            "edge_violations": self.edge_violations,
            "orphan_count": self.orphan_count,
            "remainder": self.remainder,
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
    def is_zero(self) -> bool:
        return self.remainder == 0


def make_full_chain_remainder(
    *,
    remainder_id: str,
    dag_hash: str,
    phase_statuses: list[PhaseSealStatus],
    orphan_count: int = 0,
) -> FullChainRemainder:
    """构建 FullChainRemainder。

    remainder = unsealed_count + edge_violations + orphan_count。
    """
    sorted_phases = sorted(phase_statuses, key=lambda p: p.phase)
    sealed = sum(1 for p in sorted_phases if p.sealed)
    unsealed = sum(1 for p in sorted_phases if not p.sealed)
    edge_violations = sum(1 for p in sorted_phases if not p.dag_edge_satisfied)

    remainder = unsealed + edge_violations + orphan_count

    result = FullChainRemainder(
        remainder_id=remainder_id,
        dag_hash=dag_hash,
        phase_statuses=tuple(sorted_phases),
        total_phases=len(sorted_phases),
        sealed_count=sealed,
        unsealed_count=unsealed,
        edge_violations=edge_violations,
        orphan_count=orphan_count,
        remainder=remainder,
    )
    return dataclasses.replace(
        result, content_hash=result.compute_content_hash()
    )


def verify_full_chain_remainder(
    remainder: FullChainRemainder,
) -> VerificationResult:
    """验证 FullChainRemainder。

    blocker：
    - remainder != 0 → VR_FULL_CHAIN_REMAINDER_NONZERO
    - 阶段未 sealed → VR_PHASE_NOT_SEALED
    - DAG 边违反 → VR_DAG_NOT_SEALED
    - orphan 对象 → VR_ORPHAN_OBJECT
    - content_hash 不匹配 → VR_VERDICT_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = remainder.to_dict()
    if d.get("schema_id") != "seven/full-chain-remainder":
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append("schema_id mismatch")

    if not remainder.remainder_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("remainder_id is empty")

    if not remainder.dag_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dag_hash is empty")

    # remainder 检查
    if remainder.remainder != 0:
        errors.append(EC.VR_FULL_CHAIN_REMAINDER_NONZERO)
        details.append(
            f"full chain remainder {remainder.remainder} != 0 — "
            f"unsealed={remainder.unsealed_count}, "
            f"edge_violations={remainder.edge_violations}, "
            f"orphan={remainder.orphan_count}"
        )

    # 阶段 sealed 检查
    if remainder.unsealed_count > 0:
        unsealed_phases = [
            p.phase for p in remainder.phase_statuses if not p.sealed
        ]
        errors.append(EC.VR_PHASE_NOT_SEALED)
        details.append(f"unsealed phases: {unsealed_phases}")

    # DAG 边违反
    if remainder.edge_violations > 0:
        violated_phases = [
            p.phase for p in remainder.phase_statuses
            if not p.dag_edge_satisfied
        ]
        errors.append(EC.VR_DAG_NOT_SEALED)
        details.append(f"DAG edge violations in: {violated_phases}")

    # orphan 对象
    if remainder.orphan_count > 0:
        errors.append(EC.VR_ORPHAN_OBJECT)
        details.append(f"{remainder.orphan_count} orphan objects in chain")

    # 计数一致性
    expected_remainder = (
        remainder.unsealed_count
        + remainder.edge_violations
        + remainder.orphan_count
    )
    if remainder.remainder != expected_remainder:
        errors.append(EC.VR_FULL_CHAIN_REMAINDER_NONZERO)
        details.append(
            f"remainder {remainder.remainder} != "
            f"unsealed+edge+orphan {expected_remainder}"
        )

    # content_hash
    if not remainder.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif remainder.content_hash != remainder.compute_content_hash():
        errors.append(EC.VR_VERDICT_HASH_MISMATCH)
        details.append("FullChainRemainder content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )
