"""TaxonomySnapshot / AttributeDictionaryVersion / FCAContextSnapshot.

WP-TX1 的冻结分类学坐标对象：

- TaxonomySnapshot: 冻结的分类坐标、枚举、定义和适用版本。Append-only，
  content_hash，supersedes_ref 版本链。
- AttributeDictionaryVersion: 冻结属性字典，version + content_hash +
  supersedes_ref。
- FCAContextSnapshot: 保存用于校准/重分类的 object-attribute context。
  不是自动真理源——显式标记为 calibration aid only。

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    TX_TAXONOMY_SNAPSHOT_STATES,
    TX_EVIDENCE_INHERITANCE_SCOPES,
    VerificationErrorCode as EC,
)


_SCHEMA_ID = "seven/taxonomy-snapshot"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"

_ATTR_DICT_SCHEMA_ID = "seven/attribute-dictionary-version"
_ATTR_DICT_SCHEMA_VERSION = 1

_FCA_SCHEMA_ID = "seven/fca-context-snapshot"
_FCA_SCHEMA_VERSION = 1


# ─── TaxonomySnapshot ────────────────────────────────────────────────


@dataclass(frozen=True)
class TaxonomyCoordinate:
    """单个分类坐标——一个枚举值在其所属轴上的冻结定义。"""

    axis: str
    value: str
    definition: str = ""
    applicable_versions: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "axis": self.axis,
            "value": self.value,
            "definition": self.definition,
            "applicable_versions": list(self.applicable_versions),
        }


@dataclass(frozen=True)
class TaxonomyEnumeration:
    """冻结的枚举集合——一个轴上的全部合法值。"""

    axis: str
    values: tuple[str, ...] = ()
    definitions: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "axis": self.axis,
            "values": list(self.values),
            "definitions": dict(self.definitions),
        }


@dataclass(frozen=True)
class TaxonomySnapshot:
    """冻结的分类学快照。

    Append-only：一旦 content_hash 计算并冻结，不可修改。
    版本链通过 supersedes_ref 指向前一个 snapshot。

    字段：
        snapshot_id: 唯一标识
        version: 版本号（冻结）
        state: FROZEN / SUPERSEDED / DEPRECATED
        coordinates: 冻结的分类坐标列表
        enumerations: 冻结的枚举集合列表
        definitions: 冻结的定义文本
        applicable_versions: 本 snapshot 适用的 system 版本
        supersedes_ref: 前一个 snapshot 的引用（{snapshot_id, content_hash}）
        frozen_at: 冻结时间（ISO 8601 UTC）
        content_hash: 由其他字段计算的内容哈希
    """

    snapshot_id: str
    version: str
    state: str = "FROZEN"
    coordinates: tuple[TaxonomyCoordinate, ...] = ()
    enumerations: tuple[TaxonomyEnumeration, ...] = ()
    definitions: dict[str, str] = field(default_factory=dict)
    applicable_versions: tuple[str, ...] = ()
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "snapshot_id": self.snapshot_id,
            "version": self.version,
            "state": self.state,
            "coordinates": [c.to_dict() for c in self.coordinates],
            "enumerations": [e.to_dict() for e in self.enumerations],
            "definitions": dict(self.definitions),
            "applicable_versions": list(self.applicable_versions),
            "supersedes_ref": dict(self.supersedes_ref),
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        """计算 content_hash（content_hash 字段置 null）。"""
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def is_frozen(self) -> bool:
        return bool(self.version) and self.state in TX_TAXONOMY_SNAPSHOT_STATES

    @property
    def is_append_only(self) -> bool:
        """已冻结的 snapshot 不可修改——content_hash 非空即视为冻结。"""
        return bool(self.content_hash)


def make_taxonomy_snapshot(
    *,
    snapshot_id: str,
    version: str,
    state: str = "FROZEN",
    coordinates: tuple[TaxonomyCoordinate, ...] = (),
    enumerations: tuple[TaxonomyEnumeration, ...] = (),
    definitions: dict[str, str] | None = None,
    applicable_versions: tuple[str, ...] = (),
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> TaxonomySnapshot:
    """构建 TaxonomySnapshot 并自动计算 content_hash。"""
    snap = TaxonomySnapshot(
        snapshot_id=snapshot_id,
        version=version,
        state=state,
        coordinates=coordinates,
        enumerations=enumerations,
        definitions=definitions or {},
        applicable_versions=applicable_versions,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(snap, content_hash=snap.compute_content_hash())


@dataclass(frozen=True)
class TaxonomySnapshotVerificationResult:
    """TaxonomySnapshot 验证器的结构化结果。"""

    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    snapshot_id: str = ""
    version: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_taxonomy_snapshot(
    snapshot: TaxonomySnapshot,
    *,
    known_snapshots: dict[str, TaxonomySnapshot] | None = None,
) -> TaxonomySnapshotVerificationResult:
    """验证 TaxonomySnapshot 的 schema + 语义完整性。

    检查：
    - schema_id / schema_version
    - version 已冻结（非空）
    - state 合法
    - content_hash 与计算值一致
    - append-only：已冻结的 snapshot content_hash 非空
    - supersedes_ref 链完整（如果指向已知 snapshot，hash 必须匹配）
    """
    errors: list[EC] = []
    details: list[str] = []

    if snapshot.schema_id != _SCHEMA_ID if hasattr(snapshot, "schema_id") else False:
        pass  # schema_id 不作为字段，嵌入 to_dict

    d = snapshot.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # version frozen
    if not snapshot.version:
        errors.append(EC.TX_TAXONOMY_VERSION_NOT_FROZEN)
        details.append("version is empty — must be frozen (non-empty)")

    # state valid
    if snapshot.state not in TX_TAXONOMY_SNAPSHOT_STATES:
        errors.append(EC.TX_TAXONOMY_VERSION_NOT_FROZEN)
        details.append(
            f"state '{snapshot.state}' not in {sorted(TX_TAXONOMY_SNAPSHOT_STATES)}"
        )

    # content_hash
    if not snapshot.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif snapshot.content_hash != snapshot.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {snapshot.content_hash}, "
            f"computed {snapshot.compute_content_hash()}"
        )

    # append-only: frozen snapshot must have content_hash
    if snapshot.state == "FROZEN" and not snapshot.content_hash:
        errors.append(EC.TX_TAXONOMY_APPEND_ONLY_VIOLATED)
        details.append("FROZEN snapshot must have non-empty content_hash")

    # supersedes_ref lineage
    sr = snapshot.supersedes_ref
    if sr:
        if not sr.get("snapshot_id") or not sr.get("content_hash"):
            errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
            details.append(
                "supersedes_ref must contain snapshot_id and content_hash"
            )
        elif known_snapshots is not None:
            prev = known_snapshots.get(sr["snapshot_id"])
            if prev is None:
                errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
                details.append(
                    f"supersedes_ref points to unknown snapshot "
                    f"{sr['snapshot_id']}"
                )
            elif prev.content_hash != sr["content_hash"]:
                errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
                details.append(
                    f"supersedes_ref hash mismatch: claims "
                    f"{sr['content_hash']}, actual {prev.content_hash}"
                )

    verdict = "PASS" if not errors else "FAIL"
    return TaxonomySnapshotVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        snapshot_id=snapshot.snapshot_id,
        version=snapshot.version,
    )


# ─── AttributeDictionaryVersion ──────────────────────────────────────


@dataclass(frozen=True)
class AttributeDefinition:
    """单个属性的定义——名称、类型、约束。"""

    name: str
    attr_type: str
    description: str = ""
    constraints: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "attr_type": self.attr_type,
            "description": self.description,
            "constraints": dict(self.constraints),
        }


@dataclass(frozen=True)
class AttributeDictionaryVersion:
    """冻结的属性字典版本。

    字段：
        dict_id: 唯一标识
        version: 版本号（冻结）
        attributes: 冻结的属性定义列表
        supersedes_ref: 前一个版本的引用
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    dict_id: str
    version: str
    attributes: tuple[AttributeDefinition, ...] = ()
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _ATTR_DICT_SCHEMA_ID,
            "schema_version": _ATTR_DICT_SCHEMA_VERSION,
            "dict_id": self.dict_id,
            "version": self.version,
            "attributes": [a.to_dict() for a in self.attributes],
            "supersedes_ref": dict(self.supersedes_ref),
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

    @property
    def is_frozen(self) -> bool:
        return bool(self.version) and bool(self.content_hash)


def make_attribute_dictionary_version(
    *,
    dict_id: str,
    version: str,
    attributes: tuple[AttributeDefinition, ...] = (),
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> AttributeDictionaryVersion:
    adv = AttributeDictionaryVersion(
        dict_id=dict_id,
        version=version,
        attributes=attributes,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(adv, content_hash=adv.compute_content_hash())


@dataclass(frozen=True)
class AttributeDictionaryVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    dict_id: str = ""
    version: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_attribute_dictionary_version(
    adv: AttributeDictionaryVersion,
    *,
    known_versions: dict[str, AttributeDictionaryVersion] | None = None,
) -> AttributeDictionaryVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = adv.to_dict()
    if d.get("schema_id") != _ATTR_DICT_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_ATTR_DICT_SCHEMA_ID}")

    if not adv.version:
        errors.append(EC.TX_ATTRIBUTE_DICT_VERSION_NOT_FROZEN)
        details.append("version is empty — must be frozen")

    if not adv.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif adv.content_hash != adv.compute_content_hash():
        errors.append(EC.TX_ATTRIBUTE_DICT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {adv.content_hash}, "
            f"computed {adv.compute_content_hash()}"
        )

    sr = adv.supersedes_ref
    if sr:
        if not sr.get("dict_id") or not sr.get("content_hash"):
            errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
            details.append("supersedes_ref must contain dict_id and content_hash")
        elif known_versions is not None:
            prev = known_versions.get(sr["dict_id"])
            if prev is None:
                errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
                details.append(
                    f"supersedes_ref points to unknown dict {sr['dict_id']}"
                )
            elif prev.content_hash != sr["content_hash"]:
                errors.append(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN)
                details.append(
                    f"supersedes_ref hash mismatch: claims "
                    f"{sr['content_hash']}, actual {prev.content_hash}"
                )

    verdict = "PASS" if not errors else "FAIL"
    return AttributeDictionaryVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        dict_id=adv.dict_id,
        version=adv.version,
    )


# ─── FCAContextSnapshot ──────────────────────────────────────────────


@dataclass(frozen=True)
class FCAContextSnapshot:
    """保存用于校准/重分类的 object-attribute context。

    关键约束：NOT 自动真理源——is_calibration_aid_only 必须为 True。
    显式标记为 calibration aid only。

    字段：
        context_id: 唯一标识
        taxonomy_snapshot_ref: 关联的 TaxonomySnapshot 引用
        objects: object-attribute 矩阵中的对象集合
        attributes: 属性集合
        incidence: object × attribute 关联矩阵（{object_id: [attr_name, ...]}）
        is_calibration_aid_only: 必须为 True
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    context_id: str
    taxonomy_snapshot_ref: dict[str, str] = field(default_factory=dict)
    objects: tuple[str, ...] = ()
    attributes: tuple[str, ...] = ()
    incidence: dict[str, tuple[str, ...]] = field(default_factory=dict)
    is_calibration_aid_only: bool = True
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _FCA_SCHEMA_ID,
            "schema_version": _FCA_SCHEMA_VERSION,
            "context_id": self.context_id,
            "taxonomy_snapshot_ref": dict(self.taxonomy_snapshot_ref),
            "objects": list(self.objects),
            "attributes": list(self.attributes),
            "incidence": {k: list(v) for k, v in self.incidence.items()},
            "is_calibration_aid_only": self.is_calibration_aid_only,
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


def make_fca_context_snapshot(
    *,
    context_id: str,
    taxonomy_snapshot_ref: dict[str, str] | None = None,
    objects: tuple[str, ...] = (),
    attributes: tuple[str, ...] = (),
    incidence: dict[str, tuple[str, ...]] | None = None,
    is_calibration_aid_only: bool = True,
    frozen_at: str = "",
) -> FCAContextSnapshot:
    ctx = FCAContextSnapshot(
        context_id=context_id,
        taxonomy_snapshot_ref=taxonomy_snapshot_ref or {},
        objects=objects,
        attributes=attributes,
        incidence=incidence or {},
        is_calibration_aid_only=is_calibration_aid_only,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(ctx, content_hash=ctx.compute_content_hash())


@dataclass(frozen=True)
class FCAContextVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    context_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_fca_context_snapshot(
    ctx: FCAContextSnapshot,
) -> FCAContextVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = ctx.to_dict()
    if d.get("schema_id") != _FCA_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_FCA_SCHEMA_ID}")

    # blocker: must be calibration aid only
    if not ctx.is_calibration_aid_only:
        errors.append(EC.TX_FCA_CONTEXT_NOT_CALIBRATION_AID)
        details.append(
            "is_calibration_aid_only is False — FCA context must be "
            "explicitly marked as calibration aid only, not truth source"
        )

    # blocker: must not be marked as truth source
    # (is_calibration_aid_only=False means it's being used as truth)
    if not ctx.is_calibration_aid_only:
        errors.append(EC.TX_FCA_CONTEXT_MARKED_AS_TRUTH)
        details.append(
            "FCA context must NOT be marked as automatic truth source"
        )

    if not ctx.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif ctx.content_hash != ctx.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {ctx.content_hash}, "
            f"computed {ctx.compute_content_hash()}"
        )

    if not ctx.taxonomy_snapshot_ref.get("snapshot_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("taxonomy_snapshot_ref must contain snapshot_id")

    verdict = "PASS" if not errors else "FAIL"
    return FCAContextVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        context_id=ctx.context_id,
    )
