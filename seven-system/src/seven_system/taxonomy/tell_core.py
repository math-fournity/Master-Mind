"""TellCore / TellFamily / TellManifestation / ObservationView / TellRecognitionRecord.

WP-TX1 的 Tell 因果本体与观察分层：

- TellCore: 因果身份，不变核，认知动作，family lineage。是 invariant kernel。
- TellFamily: 把共享 lineage 的 Core 分组。
- TellManifestation: 同一 latent Tell 在不同观察粒度/trace 位置的显现。
  必须不等于 Core（blocker: manifestation=Core 被拒绝）。
- ObservationView: 观察视图，不同粒度。
- TellRecognitionRecord: 识别事件记录——span, observer, confidence,
  candidate branches, taxonomy snapshot reference。

关键约束（blocker）：
- TellManifestation.kind 必须在 TX_TELL_MANIFESTATION_KINDS 中
- TellManifestation 必须不等于其 Core（manifestation_core_id != core_id 且
  content_hash 不同）
- TellCore.cognitive_action 必须在 TX_TELL_CORE_ACTIONS 中
- TellCore 是不变核——invariant_kernel_hash 必须与计算值一致
- TellFamily lineage 链完整

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    TX_TELL_MANIFESTATION_KINDS,
    TX_TELL_CORE_ACTIONS,
    VerificationErrorCode as EC,
)


_TELL_CORE_SCHEMA_ID = "seven/tell-core"
_TELL_CORE_SCHEMA_VERSION = 1

_TELL_FAMILY_SCHEMA_ID = "seven/tell-family"
_TELL_FAMILY_SCHEMA_VERSION = 1

_MANIFESTATION_SCHEMA_ID = "seven/tell-manifestation"
_MANIFESTATION_SCHEMA_VERSION = 1

_OBS_VIEW_SCHEMA_ID = "seven/observation-view"
_OBS_VIEW_SCHEMA_VERSION = 1

_RECOGNITION_SCHEMA_ID = "seven/tell-recognition-record"
_RECOGNITION_SCHEMA_VERSION = 1

_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


# ─── TellCore ────────────────────────────────────────────────────────


@dataclass(frozen=True)
class TellCore:
    """Tell 的不变核——因果身份。

    字段：
        core_id: 唯一标识
        family_id: 所属 TellFamily 的 ID
        cognitive_action: 不变认知动作（TX_TELL_CORE_ACTIONS）
        invariant_description: 不变量的文本描述
        lineage_ref: family lineage 引用（{family_id, lineage_hash}）
        supersedes_ref: 前一个 Core 版本的引用
        frozen_at: 冻结时间
        invariant_kernel_hash: 不变核哈希
        content_hash: 完整内容哈希
    """

    core_id: str
    family_id: str
    cognitive_action: str
    invariant_description: str = ""
    lineage_ref: dict[str, str] = field(default_factory=dict)
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    invariant_kernel_hash: str = ""
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _TELL_CORE_SCHEMA_ID,
            "schema_version": _TELL_CORE_SCHEMA_VERSION,
            "core_id": self.core_id,
            "family_id": self.family_id,
            "cognitive_action": self.cognitive_action,
            "invariant_description": self.invariant_description,
            "lineage_ref": dict(self.lineage_ref),
            "supersedes_ref": dict(self.supersedes_ref),
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "invariant_kernel_hash": self.invariant_kernel_hash,
            "content_hash": self.content_hash,
        }

    def _invariant_payload(self) -> dict[str, Any]:
        """不变核 payload——只包含因果身份不变的部分。"""
        return {
            "core_id": self.core_id,
            "family_id": self.family_id,
            "cognitive_action": self.cognitive_action,
            "invariant_description": self.invariant_description,
        }

    def compute_invariant_kernel_hash(self) -> str:
        return hashlib.sha256(
            canonical_json_bytes(self._invariant_payload())
        ).hexdigest()

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        d["invariant_kernel_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def is_invariant_kernel_valid(self) -> bool:
        return self.invariant_kernel_hash == self.compute_invariant_kernel_hash()

    @property
    def is_frozen(self) -> bool:
        return (
            bool(self.core_id)
            and bool(self.family_id)
            and self.cognitive_action in TX_TELL_CORE_ACTIONS
            and bool(self.content_hash)
        )


def make_tell_core(
    *,
    core_id: str,
    family_id: str,
    cognitive_action: str,
    invariant_description: str = "",
    lineage_ref: dict[str, str] | None = None,
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> TellCore:
    core = TellCore(
        core_id=core_id,
        family_id=family_id,
        cognitive_action=cognitive_action,
        invariant_description=invariant_description,
        lineage_ref=lineage_ref or {},
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    ikh = core.compute_invariant_kernel_hash()
    core = dataclasses.replace(core, invariant_kernel_hash=ikh)
    return dataclasses.replace(core, content_hash=core.compute_content_hash())


@dataclass(frozen=True)
class TellCoreVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    core_id: str = ""
    family_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_tell_core(
    core: TellCore,
    *,
    known_cores: dict[str, TellCore] | None = None,
) -> TellCoreVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = core.to_dict()
    if d.get("schema_id") != _TELL_CORE_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_TELL_CORE_SCHEMA_ID}")

    if not core.core_id or not core.family_id:
        errors.append(EC.TX_TELL_CORE_NOT_FROZEN)
        details.append("core_id and family_id must be non-empty")

    # cognitive_action valid
    if core.cognitive_action not in TX_TELL_CORE_ACTIONS:
        errors.append(EC.TX_TELL_CORE_ACTION_INVALID)
        details.append(
            f"cognitive_action '{core.cognitive_action}' not in "
            f"{sorted(TX_TELL_CORE_ACTIONS)}"
        )

    # invariant kernel hash
    if not core.invariant_kernel_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("invariant_kernel_hash is empty")
    elif core.invariant_kernel_hash != core.compute_invariant_kernel_hash():
        errors.append(EC.TX_TELL_CORE_INVARIANT_VIOLATED)
        details.append(
            f"invariant_kernel_hash mismatch: claims "
            f"{core.invariant_kernel_hash}, computed "
            f"{core.compute_invariant_kernel_hash()}"
        )

    # content_hash
    if not core.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif core.content_hash != core.compute_content_hash():
        errors.append(EC.TX_TELL_CORE_INVARIANT_VIOLATED)
        details.append(
            f"content_hash mismatch: claims {core.content_hash}, "
            f"computed {core.compute_content_hash()}"
        )

    # lineage_ref
    if not core.lineage_ref.get("family_id") or not core.lineage_ref.get("lineage_hash"):
        errors.append(EC.TX_TELL_FAMILY_LINEAGE_REF_MISSING)
        details.append("lineage_ref must contain family_id and lineage_hash")

    # supersedes_ref chain
    sr = core.supersedes_ref
    if sr:
        if not sr.get("core_id") or not sr.get("content_hash"):
            errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
            details.append("supersedes_ref must contain core_id and content_hash")
        elif known_cores is not None:
            prev = known_cores.get(sr["core_id"])
            if prev is None:
                errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
                details.append(
                    f"supersedes_ref points to unknown core {sr['core_id']}"
                )
            elif prev.content_hash != sr["content_hash"]:
                errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
                details.append(
                    f"supersedes_ref hash mismatch: claims "
                    f"{sr['content_hash']}, actual {prev.content_hash}"
                )

    verdict = "PASS" if not errors else "FAIL"
    return TellCoreVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        core_id=core.core_id,
        family_id=core.family_id,
    )


# ─── TellFamily ──────────────────────────────────────────────────────


@dataclass(frozen=True)
class TellFamily:
    """把共享 lineage 的 TellCore 分组。

    字段：
        family_id: 唯一标识
        family_name: 人类可读名称
        lineage_root_core_id: lineage 根 Core 的 ID
        member_core_ids: 家族成员 Core ID 列表
        supersedes_ref: 前一个 family 版本的引用
        frozen_at: 冻结时间
        lineage_hash: lineage 哈希
        content_hash: 内容哈希
    """

    family_id: str
    family_name: str = ""
    lineage_root_core_id: str = ""
    member_core_ids: tuple[str, ...] = ()
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    lineage_hash: str = ""
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _TELL_FAMILY_SCHEMA_ID,
            "schema_version": _TELL_FAMILY_SCHEMA_VERSION,
            "family_id": self.family_id,
            "family_name": self.family_name,
            "lineage_root_core_id": self.lineage_root_core_id,
            "member_core_ids": list(self.member_core_ids),
            "supersedes_ref": dict(self.supersedes_ref),
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "lineage_hash": self.lineage_hash,
            "content_hash": self.content_hash,
        }

    def compute_lineage_hash(self) -> str:
        payload = {
            "family_id": self.family_id,
            "lineage_root_core_id": self.lineage_root_core_id,
            "member_core_ids": list(self.member_core_ids),
        }
        return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        d["lineage_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def is_lineage_hash_valid(self) -> bool:
        return self.lineage_hash == self.compute_lineage_hash()


def make_tell_family(
    *,
    family_id: str,
    family_name: str = "",
    lineage_root_core_id: str = "",
    member_core_ids: tuple[str, ...] = (),
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> TellFamily:
    fam = TellFamily(
        family_id=family_id,
        family_name=family_name,
        lineage_root_core_id=lineage_root_core_id,
        member_core_ids=member_core_ids,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    lh = fam.compute_lineage_hash()
    fam = dataclasses.replace(fam, lineage_hash=lh)
    return dataclasses.replace(fam, content_hash=fam.compute_content_hash())


@dataclass(frozen=True)
class TellFamilyVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    family_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_tell_family(
    family: TellFamily,
    *,
    known_families: dict[str, TellFamily] | None = None,
) -> TellFamilyVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = family.to_dict()
    if d.get("schema_id") != _TELL_FAMILY_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_TELL_FAMILY_SCHEMA_ID}")

    if not family.family_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("family_id is empty")

    if not family.lineage_root_core_id:
        errors.append(EC.TX_TELL_FAMILY_LINEAGE_BROKEN)
        details.append("lineage_root_core_id is empty — lineage broken")

    if not family.lineage_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("lineage_hash is empty")
    elif family.lineage_hash != family.compute_lineage_hash():
        errors.append(EC.TX_TELL_FAMILY_LINEAGE_BROKEN)
        details.append(
            f"lineage_hash mismatch: claims {family.lineage_hash}, "
            f"computed {family.compute_lineage_hash()}"
        )

    if not family.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif family.content_hash != family.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {family.content_hash}, "
            f"computed {family.compute_content_hash()}"
        )

    sr = family.supersedes_ref
    if sr:
        if not sr.get("family_id") or not sr.get("content_hash"):
            errors.append(EC.TX_TELL_FAMILY_LINEAGE_BROKEN)
            details.append("supersedes_ref must contain family_id and content_hash")
        elif known_families is not None:
            prev = known_families.get(sr["family_id"])
            if prev is None:
                errors.append(EC.TX_TELL_FAMILY_LINEAGE_BROKEN)
                details.append(
                    f"supersedes_ref points to unknown family {sr['family_id']}"
                )
            elif prev.content_hash != sr["content_hash"]:
                errors.append(EC.TX_TELL_FAMILY_LINEAGE_BROKEN)
                details.append(
                    f"supersedes_ref hash mismatch: claims "
                    f"{sr['content_hash']}, actual {prev.content_hash}"
                )

    verdict = "PASS" if not errors else "FAIL"
    return TellFamilyVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        family_id=family.family_id,
    )


# ─── ObservationView ─────────────────────────────────────────────────


@dataclass(frozen=True)
class ObservationView:
    """观察视图——不同观察粒度上的 Tell 观察。

    字段：
        view_id: 唯一标识
        core_id: 关联的 TellCore ID
        observation_granularity: 观察粒度标签
        trace_position: trace 位置描述
        span: 观察跨度描述
        content_hash: 内容哈希
    """

    view_id: str
    core_id: str
    observation_granularity: str = ""
    trace_position: str = ""
    span: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _OBS_VIEW_SCHEMA_ID,
            "schema_version": _OBS_VIEW_SCHEMA_VERSION,
            "view_id": self.view_id,
            "core_id": self.core_id,
            "observation_granularity": self.observation_granularity,
            "trace_position": self.trace_position,
            "span": self.span,
            "frozen_at": self.frozen_at,
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


def make_observation_view(
    *,
    view_id: str,
    core_id: str,
    observation_granularity: str = "",
    trace_position: str = "",
    span: str = "",
    frozen_at: str = "",
) -> ObservationView:
    view = ObservationView(
        view_id=view_id,
        core_id=core_id,
        observation_granularity=observation_granularity,
        trace_position=trace_position,
        span=span,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(view, content_hash=view.compute_content_hash())


# ─── TellManifestation ───────────────────────────────────────────────


@dataclass(frozen=True)
class TellManifestation:
    """同一 latent Tell 在不同观察粒度/trace 位置的显现。

    blocker: 必须不等于 Core。
      - manifestation_core_id != core_id（不是同一个对象）
      - content_hash != core content_hash（内容不同）
      - kind 在 TX_TELL_MANIFESTATION_KINDS 中

    字段：
        manifestation_id: 唯一标识
        core_id: 关联的 TellCore ID（latent Tell）
        manifestation_core_id: 本 manifestation 自身的核心标识
          （必须 != core_id，否则 manifestation=Core）
        kind: manifestation kind（TX_TELL_MANIFESTATION_KINDS）
        observation_view_id: 关联的 ObservationView ID
        span: 显现跨度
        content_hash: 内容哈希
    """

    manifestation_id: str
    core_id: str
    manifestation_core_id: str
    kind: str
    observation_view_id: str = ""
    span: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _MANIFESTATION_SCHEMA_ID,
            "schema_version": _MANIFESTATION_SCHEMA_VERSION,
            "manifestation_id": self.manifestation_id,
            "core_id": self.core_id,
            "manifestation_core_id": self.manifestation_core_id,
            "kind": self.kind,
            "observation_view_id": self.observation_view_id,
            "span": self.span,
            "frozen_at": self.frozen_at,
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


def make_tell_manifestation(
    *,
    manifestation_id: str,
    core_id: str,
    manifestation_core_id: str,
    kind: str,
    observation_view_id: str = "",
    span: str = "",
    frozen_at: str = "",
) -> TellManifestation:
    man = TellManifestation(
        manifestation_id=manifestation_id,
        core_id=core_id,
        manifestation_core_id=manifestation_core_id,
        kind=kind,
        observation_view_id=observation_view_id,
        span=span,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(man, content_hash=man.compute_content_hash())


@dataclass(frozen=True)
class TellManifestationVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    manifestation_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_tell_manifestation(
    manifestation: TellManifestation,
    *,
    core: TellCore | None = None,
) -> TellManifestationVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = manifestation.to_dict()
    if d.get("schema_id") != _MANIFESTATION_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_MANIFESTATION_SCHEMA_ID}")

    # kind valid
    if manifestation.kind not in TX_TELL_MANIFESTATION_KINDS:
        errors.append(EC.TX_MANIFESTATION_KIND_INVALID)
        details.append(
            f"kind '{manifestation.kind}' not in "
            f"{sorted(TX_TELL_MANIFESTATION_KINDS)}"
        )

    # blocker: manifestation must NOT equal Core
    if manifestation.manifestation_core_id == manifestation.core_id:
        errors.append(EC.TX_MANIFESTATION_EQUALS_CORE)
        details.append(
            f"manifestation_core_id '{manifestation.manifestation_core_id}' "
            f"equals core_id '{manifestation.core_id}' — manifestation must "
            f"NOT equal Core"
        )

    # if core provided, check content_hash differs
    if core is not None:
        if core.core_id == manifestation.manifestation_core_id:
            errors.append(EC.TX_MANIFESTATION_EQUALS_CORE)
            details.append(
                "manifestation_core_id matches a known TellCore — "
                "manifestation must NOT equal Core"
            )
        if core.content_hash == manifestation.content_hash:
            errors.append(EC.TX_MANIFESTATION_EQUALS_CORE)
            details.append(
                "manifestation content_hash equals core content_hash — "
                "manifestation must NOT equal Core"
            )

    if not manifestation.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif manifestation.content_hash != manifestation.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {manifestation.content_hash}, "
            f"computed {manifestation.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return TellManifestationVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        manifestation_id=manifestation.manifestation_id,
    )


# ─── TellRecognitionRecord ───────────────────────────────────────────


@dataclass(frozen=True)
class CandidateBranch:
    """识别记录中的候选分支。"""

    branch_id: str
    branch_type: str = ""
    direction: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "branch_id": self.branch_id,
            "branch_type": self.branch_type,
            "direction": self.direction,
        }


@dataclass(frozen=True)
class TellRecognitionRecord:
    """Tell 识别事件记录。

    字段：
        record_id: 唯一标识
        core_id: 识别到的 TellCore ID
        manifestation_id: 关联的 TellManifestation ID
        span: 识别跨度
        observer: 观察者标识
        confidence: 置信度 [0.0, 1.0]
        candidate_branches: 候选分支列表
        taxonomy_snapshot_ref: 关联的 TaxonomySnapshot 引用
        observed_at: 观察时间
        content_hash: 内容哈希
    """

    record_id: str
    core_id: str
    manifestation_id: str = ""
    span: str = ""
    observer: str = ""
    confidence: float = 0.0
    candidate_branches: tuple[CandidateBranch, ...] = ()
    taxonomy_snapshot_ref: dict[str, str] = field(default_factory=dict)
    observed_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _RECOGNITION_SCHEMA_ID,
            "schema_version": _RECOGNITION_SCHEMA_VERSION,
            "record_id": self.record_id,
            "core_id": self.core_id,
            "manifestation_id": self.manifestation_id,
            "span": self.span,
            "observer": self.observer,
            "confidence": self.confidence,
            "candidate_branches": [cb.to_dict() for cb in self.candidate_branches],
            "taxonomy_snapshot_ref": dict(self.taxonomy_snapshot_ref),
            "observed_at": self.observed_at,
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


def make_tell_recognition_record(
    *,
    record_id: str,
    core_id: str,
    manifestation_id: str = "",
    span: str = "",
    observer: str = "",
    confidence: float = 0.0,
    candidate_branches: tuple[CandidateBranch, ...] = (),
    taxonomy_snapshot_ref: dict[str, str] | None = None,
    observed_at: str = "",
) -> TellRecognitionRecord:
    rec = TellRecognitionRecord(
        record_id=record_id,
        core_id=core_id,
        manifestation_id=manifestation_id,
        span=span,
        observer=observer,
        confidence=confidence,
        candidate_branches=candidate_branches,
        taxonomy_snapshot_ref=taxonomy_snapshot_ref or {},
        observed_at=observed_at,
    )
    return dataclasses.replace(rec, content_hash=rec.compute_content_hash())


@dataclass(frozen=True)
class TellRecognitionVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    record_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_tell_recognition_record(
    record: TellRecognitionRecord,
) -> TellRecognitionVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = record.to_dict()
    if d.get("schema_id") != _RECOGNITION_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_RECOGNITION_SCHEMA_ID}")

    # taxonomy_snapshot_ref required
    if not record.taxonomy_snapshot_ref.get("snapshot_id"):
        errors.append(EC.TX_TELL_RECOGNITION_TAXONOMY_REF_MISSING)
        details.append(
            "taxonomy_snapshot_ref must contain snapshot_id — recognition "
            "must reference a frozen taxonomy snapshot"
        )

    if not record.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif record.content_hash != record.compute_content_hash():
        errors.append(EC.TX_TELL_RECOGNITION_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {record.content_hash}, "
            f"computed {record.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return TellRecognitionVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        record_id=record.record_id,
    )
