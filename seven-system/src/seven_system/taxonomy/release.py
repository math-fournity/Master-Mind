"""TellStrategyRelease / MathValidityRecord / SystemEfficacyRecord /
ReleaseLineage / EvidenceForeignKeyMigration / InvalidationRules.

WP-TX1 的发布谱系、数学有效性、系统效力和失效规则。

关键约束（blocker）：
- TellStrategyRelease 锁定 Core/boundary/selector/renderer/injection/critic/
  composition/taxonomy/scope 到 hash manifest，发布后不可变
- Release 版本链 supersedes_ref 完整
- 旧 Evidence 引用必须用外键迁移（release 变化时）
- Gate 不能直接改 pointer
- MathValidity 和 SystemEffication 分开记录
- SystemEfficacy 必须有 solver/resource context
- MechanismContract core/boundary 变化 → Coverage/Case applicability 重裁定
- Renderer/Selector/TargetSolver 版本变化 → efficacy 和 cost evidence 重测

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    TX_RELEASE_STATES,
    TX_VALIDITY_STATUSES,
    TX_EFFICACY_STATUSES,
    TX_EVIDENCE_INHERITANCE_SCOPES,
    TX_INVALIDATION_TARGETS,
    VerificationErrorCode as EC,
)


_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"

_RELEASE_SCHEMA_ID = "seven/tell-strategy-release"
_RELEASE_SCHEMA_VERSION = 1

_VALIDITY_SCHEMA_ID = "seven/math-validity-record"
_VALIDITY_SCHEMA_VERSION = 1

_EFFICACY_SCHEMA_ID = "seven/system-efficacy-record"
_EFFICACY_SCHEMA_VERSION = 1


# ─── TellStrategyRelease ─────────────────────────────────────────────


@dataclass(frozen=True)
class ReleaseComponentRef:
    """Release 中的单个组件引用——{kind, id, version, content_hash}。"""

    kind: str
    component_id: str
    version: str = ""
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "component_id": self.component_id,
            "version": self.version,
            "content_hash": self.content_hash,
        }


@dataclass(frozen=True)
class TellStrategyRelease:
    """锁定 Core/boundary/selector/renderer/injection/critic/composition/
    taxonomy/scope 到 hash manifest。

    发布后不可变。版本链 supersedes_ref。

    字段：
        release_id: 唯一标识
        version: 版本号
        state: DRAFT / RELEASED / SUPERSEDED / REVOKED
        core_ref: TellCore 引用
        boundary_ref: ApplicabilityBoundary 引用
        selector_ref: SelectorDecision 引用
        renderer_ref: HintRenderer 引用
        injection_ref: InjectionPolicy 引用
        critic_ref: CriticContract 引用
        composition_ref: CompositionContract 引用
        taxonomy_ref: TaxonomySnapshot 引用
        scope: 适用范围描述
        supersedes_ref: 前一个 release 引用
        frozen_at: 冻结时间
        manifest_hash: 组件 manifest 哈希
        content_hash: 完整内容哈希
    """

    release_id: str
    version: str
    state: str = "DRAFT"
    core_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="TellCore", component_id=""))
    boundary_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="ApplicabilityBoundary", component_id=""))
    selector_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="SelectorDecision", component_id=""))
    renderer_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="HintRenderer", component_id=""))
    injection_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="InjectionPolicy", component_id=""))
    critic_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="CriticContract", component_id=""))
    composition_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="CompositionContract", component_id=""))
    taxonomy_ref: ReleaseComponentRef = field(default_factory=lambda: ReleaseComponentRef(kind="TaxonomySnapshot", component_id=""))
    scope: str = ""
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    manifest_hash: str = ""
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _RELEASE_SCHEMA_ID,
            "schema_version": _RELEASE_SCHEMA_VERSION,
            "release_id": self.release_id,
            "version": self.version,
            "state": self.state,
            "core_ref": self.core_ref.to_dict(),
            "boundary_ref": self.boundary_ref.to_dict(),
            "selector_ref": self.selector_ref.to_dict(),
            "renderer_ref": self.renderer_ref.to_dict(),
            "injection_ref": self.injection_ref.to_dict(),
            "critic_ref": self.critic_ref.to_dict(),
            "composition_ref": self.composition_ref.to_dict(),
            "taxonomy_ref": self.taxonomy_ref.to_dict(),
            "scope": self.scope,
            "supersedes_ref": dict(self.supersedes_ref),
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "manifest_hash": self.manifest_hash,
            "content_hash": self.content_hash,
        }

    def _manifest_payload(self) -> list[dict[str, Any]]:
        return [
            self.core_ref.to_dict(),
            self.boundary_ref.to_dict(),
            self.selector_ref.to_dict(),
            self.renderer_ref.to_dict(),
            self.injection_ref.to_dict(),
            self.critic_ref.to_dict(),
            self.composition_ref.to_dict(),
            self.taxonomy_ref.to_dict(),
        ]

    def compute_manifest_hash(self) -> str:
        return hashlib.sha256(
            canonical_json_bytes(self._manifest_payload())
        ).hexdigest()

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        d["manifest_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def is_manifest_hash_valid(self) -> bool:
        return self.manifest_hash == self.compute_manifest_hash()

    @property
    def is_released(self) -> bool:
        return self.state == "RELEASED"

    @property
    def is_immutable(self) -> bool:
        """RELEASED 状态的 release 不可变。"""
        return self.state == "RELEASED" and bool(self.content_hash)


def make_tell_strategy_release(
    *,
    release_id: str,
    version: str,
    state: str = "DRAFT",
    core_ref: ReleaseComponentRef | None = None,
    boundary_ref: ReleaseComponentRef | None = None,
    selector_ref: ReleaseComponentRef | None = None,
    renderer_ref: ReleaseComponentRef | None = None,
    injection_ref: ReleaseComponentRef | None = None,
    critic_ref: ReleaseComponentRef | None = None,
    composition_ref: ReleaseComponentRef | None = None,
    taxonomy_ref: ReleaseComponentRef | None = None,
    scope: str = "",
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> TellStrategyRelease:
    rel = TellStrategyRelease(
        release_id=release_id,
        version=version,
        state=state,
        core_ref=core_ref or ReleaseComponentRef(kind="TellCore", component_id=""),
        boundary_ref=boundary_ref or ReleaseComponentRef(kind="ApplicabilityBoundary", component_id=""),
        selector_ref=selector_ref or ReleaseComponentRef(kind="SelectorDecision", component_id=""),
        renderer_ref=renderer_ref or ReleaseComponentRef(kind="HintRenderer", component_id=""),
        injection_ref=injection_ref or ReleaseComponentRef(kind="InjectionPolicy", component_id=""),
        critic_ref=critic_ref or ReleaseComponentRef(kind="CriticContract", component_id=""),
        composition_ref=composition_ref or ReleaseComponentRef(kind="CompositionContract", component_id=""),
        taxonomy_ref=taxonomy_ref or ReleaseComponentRef(kind="TaxonomySnapshot", component_id=""),
        scope=scope,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    mh = rel.compute_manifest_hash()
    rel = dataclasses.replace(rel, manifest_hash=mh)
    return dataclasses.replace(rel, content_hash=rel.compute_content_hash())


@dataclass(frozen=True)
class TellStrategyReleaseVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    release_id: str = ""
    version: str = ""
    is_immutable: bool = False

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_tell_strategy_release(
    release: TellStrategyRelease,
    *,
    known_releases: dict[str, TellStrategyRelease] | None = None,
) -> TellStrategyReleaseVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = release.to_dict()
    if d.get("schema_id") != _RELEASE_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_RELEASE_SCHEMA_ID}")

    # state valid
    if release.state not in TX_RELEASE_STATES:
        errors.append(EC.TX_RELEASE_STATE_INVALID)
        details.append(
            f"state '{release.state}' not in {sorted(TX_RELEASE_STATES)}"
        )

    # all component refs must be present
    components = [
        ("core_ref", release.core_ref),
        ("boundary_ref", release.boundary_ref),
        ("selector_ref", release.selector_ref),
        ("renderer_ref", release.renderer_ref),
        ("injection_ref", release.injection_ref),
        ("critic_ref", release.critic_ref),
        ("composition_ref", release.composition_ref),
        ("taxonomy_ref", release.taxonomy_ref),
    ]
    for name, ref in components:
        if not ref.component_id:
            errors.append(EC.TX_RELEASE_COMPONENT_MISSING)
            details.append(f"{name}.component_id is empty — release must lock all components")
        if not ref.content_hash:
            errors.append(EC.TX_RELEASE_COMPONENT_HASH_MISMATCH)
            details.append(f"{name}.content_hash is empty — component must be frozen")

    # manifest_hash
    if not release.manifest_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("manifest_hash is empty")
    elif release.manifest_hash != release.compute_manifest_hash():
        errors.append(EC.TX_RELEASE_HASH_MISMATCH)
        details.append(
            f"manifest_hash mismatch: claims {release.manifest_hash}, "
            f"computed {release.compute_manifest_hash()}"
        )

    # content_hash
    if not release.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif release.content_hash != release.compute_content_hash():
        errors.append(EC.TX_RELEASE_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {release.content_hash}, "
            f"computed {release.compute_content_hash()}"
        )

    # immutability: RELEASED must have content_hash
    is_immutable = release.is_immutable
    if release.state == "RELEASED" and not release.content_hash:
        errors.append(EC.TX_RELEASE_NOT_IMMUTABLE)
        details.append("RELEASED state must have non-empty content_hash")

    # supersedes_ref lineage
    sr = release.supersedes_ref
    if sr:
        if not sr.get("release_id") or not sr.get("content_hash"):
            errors.append(EC.TX_RELEASE_SUPERSEDES_REF_MISSING)
            details.append("supersedes_ref must contain release_id and content_hash")
        elif known_releases is not None:
            prev = known_releases.get(sr["release_id"])
            if prev is None:
                errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
                details.append(
                    f"supersedes_ref points to unknown release {sr['release_id']}"
                )
            elif prev.content_hash != sr["content_hash"]:
                errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
                details.append(
                    f"supersedes_ref hash mismatch: claims "
                    f"{sr['content_hash']}, actual {prev.content_hash}"
                )

    verdict = "PASS" if not errors else "FAIL"
    return TellStrategyReleaseVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        release_id=release.release_id,
        version=release.version,
        is_immutable=is_immutable,
    )


# ─── ReleaseLineage ──────────────────────────────────────────────────


@dataclass(frozen=True)
class ReleaseLineage:
    """Release 版本链——有序的 release 引用列表。

    字段：
        lineage_id: 唯一标识
        releases: 有序的 release 引用列表（从旧到新）
        head_release_id: 链头 release ID
        head_content_hash: 链头 content_hash
    """

    lineage_id: str
    releases: tuple[dict[str, str], ...] = ()
    head_release_id: str = ""
    head_content_hash: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": "seven/release-lineage",
            "schema_version": 1,
            "lineage_id": self.lineage_id,
            "releases": [dict(r) for r in self.releases],
            "head_release_id": self.head_release_id,
            "head_content_hash": self.head_content_hash,
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


def make_release_lineage(
    *,
    lineage_id: str,
    releases: tuple[dict[str, str], ...] = (),
) -> ReleaseLineage:
    head = releases[-1] if releases else {}
    lin = ReleaseLineage(
        lineage_id=lineage_id,
        releases=releases,
        head_release_id=head.get("release_id", ""),
        head_content_hash=head.get("content_hash", ""),
    )
    return dataclasses.replace(lin, content_hash=lin.compute_content_hash())


@dataclass(frozen=True)
class ReleaseLineageVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    lineage_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_release_lineage(
    lineage: ReleaseLineage,
    *,
    known_releases: dict[str, TellStrategyRelease] | None = None,
) -> ReleaseLineageVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    if not lineage.releases:
        errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
        details.append("lineage has no releases")
    else:
        # each release ref must have release_id and content_hash
        for i, r in enumerate(lineage.releases):
            if not r.get("release_id") or not r.get("content_hash"):
                errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
                details.append(
                    f"lineage[{i}] missing release_id or content_hash"
                )
            elif known_releases is not None:
                rel = known_releases.get(r["release_id"])
                if rel is None:
                    errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
                    details.append(
                        f"lineage[{i}] points to unknown release {r['release_id']}"
                    )
                elif rel.content_hash != r["content_hash"]:
                    errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
                    details.append(
                        f"lineage[{i}] hash mismatch: claims "
                        f"{r['content_hash']}, actual {rel.content_hash}"
                    )

        # head must match last release
        if lineage.releases:
            last = lineage.releases[-1]
            if lineage.head_release_id != last.get("release_id"):
                errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
                details.append(
                    f"head_release_id '{lineage.head_release_id}' != "
                    f"last release '{last.get('release_id')}'"
                )
            if lineage.head_content_hash != last.get("content_hash"):
                errors.append(EC.TX_RELEASE_LINEAGE_BROKEN)
                details.append(
                    f"head_content_hash '{lineage.head_content_hash}' != "
                    f"last release hash '{last.get('content_hash')}'"
                )

    if not lineage.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif lineage.content_hash != lineage.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {lineage.content_hash}, "
            f"computed {lineage.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ReleaseLineageVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        lineage_id=lineage.lineage_id,
    )


# ─── EvidenceForeignKeyMigration ─────────────────────────────────────


@dataclass(frozen=True)
class EvidenceForeignKeyMigration:
    """旧 Evidence 引用的外键迁移记录。

    当 release 变化时，旧 Evidence 引用必须通过外键迁移指向新 release，
    不能直接修改旧 Evidence。

    字段：
        migration_id: 唯一标识
        old_release_ref: 旧 release 引用
        new_release_ref: 新 release 引用
        evidence_ids: 被迁移的 Evidence ID 列表
        inheritance_scope: 继承 scope（TX_EVIDENCE_INHERITANCE_SCOPES）
        migrated_by: 迁移者（必须是 registry，不是 Gate）
        migrated_at: 迁移时间
        content_hash: 内容哈希
    """

    migration_id: str
    old_release_ref: dict[str, str] = field(default_factory=dict)
    new_release_ref: dict[str, str] = field(default_factory=dict)
    evidence_ids: tuple[str, ...] = ()
    inheritance_scope: str = "EXACT"
    migrated_by: str = "REGISTRY"
    migrated_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": "seven/evidence-foreign-key-migration",
            "schema_version": 1,
            "migration_id": self.migration_id,
            "old_release_ref": dict(self.old_release_ref),
            "new_release_ref": dict(self.new_release_ref),
            "evidence_ids": list(self.evidence_ids),
            "inheritance_scope": self.inheritance_scope,
            "migrated_by": self.migrated_by,
            "migrated_at": self.migrated_at,
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


def make_evidence_foreign_key_migration(
    *,
    migration_id: str,
    old_release_ref: dict[str, str] | None = None,
    new_release_ref: dict[str, str] | None = None,
    evidence_ids: tuple[str, ...] = (),
    inheritance_scope: str = "EXACT",
    migrated_by: str = "REGISTRY",
    migrated_at: str = "",
) -> EvidenceForeignKeyMigration:
    m = EvidenceForeignKeyMigration(
        migration_id=migration_id,
        old_release_ref=old_release_ref or {},
        new_release_ref=new_release_ref or {},
        evidence_ids=evidence_ids,
        inheritance_scope=inheritance_scope,
        migrated_by=migrated_by,
        migrated_at=migrated_at,
    )
    return dataclasses.replace(m, content_hash=m.compute_content_hash())


@dataclass(frozen=True)
class EvidenceMigrationVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    migration_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_evidence_foreign_key_migration(
    migration: EvidenceForeignKeyMigration,
    *,
    unmigrated_evidence_ids: set[str] | None = None,
    actor_is_gate: bool = False,
) -> EvidenceMigrationVerificationResult:
    """验证外键迁移。

    参数：
        unmigrated_evidence_ids: 仍未迁移的 Evidence ID（用于 blocker 测试）
        actor_is_gate: 迁移者是否是 Gate（blocker: Gate 不能改 pointer）
    """
    errors: list[EC] = []
    details: list[str] = []

    if not migration.old_release_ref.get("release_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("old_release_ref must contain release_id")

    if not migration.new_release_ref.get("release_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("new_release_ref must contain release_id")

    if migration.inheritance_scope not in TX_EVIDENCE_INHERITANCE_SCOPES:
        errors.append(EC.TX_OLD_EVIDENCE_FOREIGN_KEY_NOT_MIGRATED)
        details.append(
            f"inheritance_scope '{migration.inheritance_scope}' not in "
            f"{sorted(TX_EVIDENCE_INHERITANCE_SCOPES)}"
        )

    # blocker: old evidence not migrated
    if unmigrated_evidence_ids:
        missing = unmigrated_evidence_ids & set(migration.evidence_ids)
        if missing != unmigrated_evidence_ids:
            errors.append(EC.TX_OLD_EVIDENCE_FOREIGN_KEY_NOT_MIGRATED)
            details.append(
                f"evidence not fully migrated: expected "
                f"{sorted(unmigrated_evidence_ids)}, got "
                f"{sorted(missing)}"
            )
        # check all old evidence covered
        not_covered = unmigrated_evidence_ids - set(migration.evidence_ids)
        if not_covered:
            errors.append(EC.TX_OLD_EVIDENCE_FOREIGN_KEY_NOT_MIGRATED)
            details.append(
                f"old evidence not covered by migration: "
                f"{sorted(not_covered)}"
            )

    # blocker: Gate cannot change pointer
    if actor_is_gate or migration.migrated_by == "GATE":
        errors.append(EC.TX_RELEASE_POINTER_CHANGED_BY_GATE)
        details.append(
            "migrated_by is GATE — Gate cannot change release pointer directly; "
            "only registry can migrate foreign keys"
        )

    if not migration.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif migration.content_hash != migration.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {migration.content_hash}, "
            f"computed {migration.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return EvidenceMigrationVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        migration_id=migration.migration_id,
    )


# ─── MathValidityRecord ──────────────────────────────────────────────


@dataclass(frozen=True)
class MathValidityRecord:
    """数学有效性记录——与 Solver 无关的数学正确性。

    字段：
        record_id: 唯一标识
        core_id: 关联的 TellCore ID
        status: VALID / INVALID / UNDETERMINED / SUPERSEDED
        validity_basis: 有效性依据
        supersedes_ref: 前一个版本引用
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    record_id: str
    core_id: str
    status: str = "UNDETERMINED"
    validity_basis: str = ""
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _VALIDITY_SCHEMA_ID,
            "schema_version": _VALIDITY_SCHEMA_VERSION,
            "record_id": self.record_id,
            "core_id": self.core_id,
            "status": self.status,
            "validity_basis": self.validity_basis,
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


def make_math_validity_record(
    *,
    record_id: str,
    core_id: str,
    status: str = "UNDETERMINED",
    validity_basis: str = "",
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> MathValidityRecord:
    r = MathValidityRecord(
        record_id=record_id,
        core_id=core_id,
        status=status,
        validity_basis=validity_basis,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class MathValidityVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    record_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_math_validity_record(
    record: MathValidityRecord,
) -> MathValidityVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = record.to_dict()
    if d.get("schema_id") != _VALIDITY_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_VALIDITY_SCHEMA_ID}")

    if record.status not in TX_VALIDITY_STATUSES:
        errors.append(EC.TX_VALIDITY_STATUS_INVALID)
        details.append(
            f"status '{record.status}' not in {sorted(TX_VALIDITY_STATUSES)}"
        )

    if not record.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif record.content_hash != record.compute_content_hash():
        errors.append(EC.TX_VALIDITY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {record.content_hash}, "
            f"computed {record.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return MathValidityVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        record_id=record.record_id,
    )


# ─── SystemEfficacyRecord ────────────────────────────────────────────


@dataclass(frozen=True)
class SolverResourceContext:
    """Solver/resource context——efficacy 特定的上下文。"""

    solver_id: str = ""
    solver_version: str = ""
    resource_profile: str = ""
    renderer_version: str = ""
    selector_version: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "solver_id": self.solver_id,
            "solver_version": self.solver_version,
            "resource_profile": self.resource_profile,
            "renderer_version": self.renderer_version,
            "selector_version": self.selector_version,
        }


@dataclass(frozen=True)
class SystemEfficacyRecord:
    """系统效力记录——特定于 Solver/resource context 的机制效力。

    与 MathValidityRecord 分开——efficacy 是 context-specific 的。

    字段：
        record_id: 唯一标识
        core_id: 关联的 TellCore ID
        status: EFFICACIOUS / INEFFICACIOUS / INCONCLUSIVE / SUPERSEDED
        solver_context: Solver/resource context（必须非空）
        efficacy_basis: 效力依据
        supersedes_ref: 前一个版本引用
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    record_id: str
    core_id: str
    status: str = "INCONCLUSIVE"
    solver_context: SolverResourceContext = field(default_factory=SolverResourceContext)
    efficacy_basis: str = ""
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _EFFICACY_SCHEMA_ID,
            "schema_version": _EFFICACY_SCHEMA_VERSION,
            "record_id": self.record_id,
            "core_id": self.core_id,
            "status": self.status,
            "solver_context": self.solver_context.to_dict(),
            "efficacy_basis": self.efficacy_basis,
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


def make_system_efficacy_record(
    *,
    record_id: str,
    core_id: str,
    status: str = "INCONCLUSIVE",
    solver_context: SolverResourceContext | None = None,
    efficacy_basis: str = "",
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> SystemEfficacyRecord:
    r = SystemEfficacyRecord(
        record_id=record_id,
        core_id=core_id,
        status=status,
        solver_context=solver_context or SolverResourceContext(),
        efficacy_basis=efficacy_basis,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class SystemEfficacyVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    record_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_system_efficacy_record(
    record: SystemEfficacyRecord,
    *,
    expected_renderer_version: str | None = None,
    expected_selector_version: str | None = None,
    expected_solver_version: str | None = None,
) -> SystemEfficacyVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = record.to_dict()
    if d.get("schema_id") != _EFFICACY_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_EFFICACY_SCHEMA_ID}")

    if record.status not in TX_EFFICACY_STATUSES:
        errors.append(EC.TX_EFFICACY_STATUS_INVALID)
        details.append(
            f"status '{record.status}' not in {sorted(TX_EFFICACY_STATUSES)}"
        )

    # blocker: solver context missing
    ctx = record.solver_context
    if not ctx.solver_id:
        errors.append(EC.TX_EFFICACY_SOLVER_CONTEXT_MISSING)
        details.append(
            "solver_context.solver_id is empty — efficacy is specific to "
            "Solver/resource context"
        )

    # version drift checks
    if expected_renderer_version is not None:
        if ctx.renderer_version != expected_renderer_version:
            errors.append(EC.TX_EFFICACY_RENDERER_VERSION_DRIFT)
            details.append(
                f"renderer_version drift: '{ctx.renderer_version}' != "
                f"expected '{expected_renderer_version}' — efficacy and cost "
                f"evidence must be re-tested"
            )
    if expected_selector_version is not None:
        if ctx.selector_version != expected_selector_version:
            errors.append(EC.TX_EFFICACY_SELECTOR_VERSION_DRIFT)
            details.append(
                f"selector_version drift: '{ctx.selector_version}' != "
                f"expected '{expected_selector_version}' — efficacy and cost "
                f"evidence must be re-tested"
            )
    if expected_solver_version is not None:
        if ctx.solver_version != expected_solver_version:
            errors.append(EC.TX_EFFICACY_TARGET_SOLVER_VERSION_DRIFT)
            details.append(
                f"solver_version drift: '{ctx.solver_version}' != "
                f"expected '{expected_solver_version}' — efficacy and cost "
                f"evidence must be re-tested"
            )

    if not record.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif record.content_hash != record.compute_content_hash():
        errors.append(EC.TX_EFFICACY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {record.content_hash}, "
            f"computed {record.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return SystemEfficacyVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        record_id=record.record_id,
    )


# ─── InvalidationRules ───────────────────────────────────────────────


@dataclass(frozen=True)
class InvalidationNotice:
    """失效通知——MechanismContract 变化触发的重裁定/重测通知。

    字段：
        notice_id: 唯一标识
        trigger: 触发原因（CORE_CHANGED / BOUNDARY_CHANGED /
                  RENDERER_VERSION_CHANGED / SELECTOR_VERSION_CHANGED /
                  TARGET_SOLVER_VERSION_CHANGED）
        targets: 受影响的 target 列表（TX_INVALIDATION_TARGETS 子集）
        requires_readjudication: 是否需要重裁定（Coverage/Case applicability）
        requires_efficacy_retest: 是否需要效力重测
        requires_cost_retest: 是否需要成本重测
        content_hash: 内容哈希
    """

    notice_id: str
    trigger: str = ""
    targets: tuple[str, ...] = ()
    requires_readjudication: bool = False
    requires_efficacy_retest: bool = False
    requires_cost_retest: bool = False
    issued_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": "seven/invalidation-notice",
            "schema_version": 1,
            "notice_id": self.notice_id,
            "trigger": self.trigger,
            "targets": list(self.targets),
            "requires_readjudication": self.requires_readjudication,
            "requires_efficacy_retest": self.requires_efficacy_retest,
            "requires_cost_retest": self.requires_cost_retest,
            "issued_at": self.issued_at,
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


def make_invalidation_notice(
    *,
    notice_id: str,
    trigger: str = "",
    targets: tuple[str, ...] = (),
    requires_readjudication: bool = False,
    requires_efficacy_retest: bool = False,
    requires_cost_retest: bool = False,
    issued_at: str = "",
) -> InvalidationNotice:
    n = InvalidationNotice(
        notice_id=notice_id,
        trigger=trigger,
        targets=targets,
        requires_readjudication=requires_readjudication,
        requires_efficacy_retest=requires_efficacy_retest,
        requires_cost_retest=requires_cost_retest,
        issued_at=issued_at,
    )
    return dataclasses.replace(n, content_hash=n.compute_content_hash())


# 失效触发原因枚举
INVALIDATION_TRIGGERS: frozenset[str] = frozenset(
    {
        "CORE_CHANGED",
        "BOUNDARY_CHANGED",
        "RENDERER_VERSION_CHANGED",
        "SELECTOR_VERSION_CHANGED",
        "TARGET_SOLVER_VERSION_CHANGED",
    }
)


def compute_invalidation_notice(
    *,
    notice_id: str,
    trigger: str,
    issued_at: str = "",
) -> InvalidationNotice:
    """根据触发原因计算失效通知。

    规则：
    - CORE_CHANGED / BOUNDARY_CHANGED → Coverage/Case applicability 重裁定
    - RENDERER_VERSION_CHANGED / SELECTOR_VERSION_CHANGED /
      TARGET_SOLVER_VERSION_CHANGED → efficacy 和 cost evidence 重测
    """
    if trigger not in INVALIDATION_TRIGGERS:
        raise ValueError(f"unknown invalidation trigger: {trigger}")

    if trigger in ("CORE_CHANGED", "BOUNDARY_CHANGED"):
        targets: tuple[str, ...] = (
            "CoverageApplicability",
            "CaseApplicability",
        )
        return make_invalidation_notice(
            notice_id=notice_id,
            trigger=trigger,
            targets=targets,
            requires_readjudication=True,
            requires_efficacy_retest=False,
            requires_cost_retest=False,
            issued_at=issued_at,
        )
    # version change triggers
    targets = ("SystemEfficacyRecord", "CostEvidence")
    return make_invalidation_notice(
        notice_id=notice_id,
        trigger=trigger,
        targets=targets,
        requires_readjudication=False,
        requires_efficacy_retest=True,
        requires_cost_retest=True,
        issued_at=issued_at,
    )


@dataclass(frozen=True)
class InvalidationVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    notice_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_invalidation_notice(
    notice: InvalidationNotice,
    *,
    readjudication_done: bool = True,
    efficacy_retest_done: bool = True,
) -> InvalidationVerificationResult:
    """验证失效通知及其后续动作是否完成。"""
    errors: list[EC] = []
    details: list[str] = []

    if notice.trigger not in INVALIDATION_TRIGGERS:
        errors.append(EC.TX_INVALIDATION_TARGET_UNKNOWN)
        details.append(
            f"trigger '{notice.trigger}' not in {sorted(INVALIDATION_TRIGGERS)}"
        )

    # targets must be in TX_INVALIDATION_TARGETS
    for t in notice.targets:
        if t not in TX_INVALIDATION_TARGETS:
            errors.append(EC.TX_INVALIDATION_TARGET_UNKNOWN)
            details.append(f"target '{t}' not in {sorted(TX_INVALIDATION_TARGETS)}")

    # readjudication required but not done
    if notice.requires_readjudication and not readjudication_done:
        errors.append(EC.TX_INVALIDATION_READJUDICATION_MISSING)
        details.append(
            "requires_readjudication is True but readjudication not done — "
            "Coverage/Case applicability must be re-adjudicated"
        )

    # efficacy retest required but not done
    if notice.requires_efficacy_retest and not efficacy_retest_done:
        errors.append(EC.TX_INVALIDATION_EFFICACY_RETEST_MISSING)
        details.append(
            "requires_efficacy_retest is True but efficacy retest not done — "
            "efficacy and cost evidence must be re-tested"
        )

    if not notice.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif notice.content_hash != notice.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {notice.content_hash}, "
            f"computed {notice.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return InvalidationVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        notice_id=notice.notice_id,
    )
