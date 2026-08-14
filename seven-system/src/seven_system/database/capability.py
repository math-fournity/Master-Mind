"""离线 StrictDbContract 与真实 DatabaseSiteCapability 的 subject 建模。

两类 subject 永久分开：离线代码/规格证据不依赖、也不能替代站点物理证据；
本模块不读取站点、不生成 PASS。
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from ..hashing import object_hash
from .environment import EXPECTED_DATABASE
from .port import DATABASE_PORT_CONTRACT_VERSION
from .spec import CANONICAL_MIGRATION_SPEC_HASH


STRICT_DATABASE_CONTRACT_CHECK_IDS = (
    "strict_db.environment.required_before_client",
    "strict_db.identity.expected_before_client",
    "strict_db.identity.current_database_verified",
    "strict_db.collections.fixed_allowlist",
    "strict_db.secrets.redacted",
    "strict_db.raw_client.no_public_bypass",
    "strict_db.planner.read_only",
    "strict_db.migration.no_runtime_apply_primitive",
    "strict_db.spec.canonical_hash",
    "strict_db.schema.extra_indexes_rejected",
    "strict_db.capability.site_separation",
)

DATABASE_SITE_CAPABILITY_CHECK_IDS = (
    "database.site.physical_storage.binding_verified",
    "database.site.schema.collections_match_spec",
    "database.site.schema.unique_indexes_verified",
    "database.site.migration.durable_ledger_verified",
    "database.site.migration.fence_and_resume_verified",
    "database.site.append_only_and_cas_semantics_verified",
    "database.site.outbox_idempotency_verified",
)

# 兼容 capability checklist 的汇总视图；不能据此把 contract PASS 升级成 site PASS。
DATABASE_CAPABILITY_CHECK_IDS = (
    *STRICT_DATABASE_CONTRACT_CHECK_IDS,
    *DATABASE_SITE_CAPABILITY_CHECK_IDS,
)
DATABASE_SITE_CHECK_IDS = DATABASE_SITE_CAPABILITY_CHECK_IDS


def _sha256(value: str, label: str) -> str:
    if re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError(f"{label} must be a lowercase sha256")
    return value


@dataclass(frozen=True)
class StrictDatabaseContractSubject:
    """只绑定实现与 canonical spec；不接受物理存储证据字段。"""

    implementation_sha256: str
    migration_spec_sha256: str = CANONICAL_MIGRATION_SPEC_HASH
    expected_database: str = EXPECTED_DATABASE
    adapter_contract: str = DATABASE_PORT_CONTRACT_VERSION

    def __post_init__(self) -> None:
        _sha256(self.implementation_sha256, "implementation_sha256")
        _sha256(self.migration_spec_sha256, "migration_spec_sha256")
        if self.expected_database != EXPECTED_DATABASE:
            raise ValueError("contract subject has the wrong database identity")
        if self.adapter_contract != DATABASE_PORT_CONTRACT_VERSION:
            raise ValueError("contract subject has the wrong adapter contract")

    def as_dict(self) -> dict[str, Any]:
        return {
            "subject_type": "StrictDbContract",
            "expected_database": self.expected_database,
            "adapter_contract": self.adapter_contract,
            "migration_spec_sha256": self.migration_spec_sha256,
            "implementation_sha256": self.implementation_sha256,
            "required_check_ids": list(STRICT_DATABASE_CONTRACT_CHECK_IDS),
        }

    @property
    def subject_hash(self) -> str:
        return object_hash(
            "StrictDatabaseContractSubject",
            "strict-database-contract-subject/v1",
            self.as_dict(),
        )


@dataclass(frozen=True)
class DatabaseSiteCapabilitySubject:
    """真实站点 subject；必须绑定 contract、catalog 与物理存储三份证据。"""

    strict_contract_subject_hash: str
    database_catalog_evidence_sha256: str
    physical_storage_evidence_sha256: str
    expected_database: str = EXPECTED_DATABASE

    def __post_init__(self) -> None:
        _sha256(self.strict_contract_subject_hash, "strict_contract_subject_hash")
        _sha256(
            self.database_catalog_evidence_sha256,
            "database_catalog_evidence_sha256",
        )
        _sha256(
            self.physical_storage_evidence_sha256,
            "physical_storage_evidence_sha256",
        )
        if self.expected_database != EXPECTED_DATABASE:
            raise ValueError("site subject has the wrong database identity")

    def as_dict(self) -> dict[str, Any]:
        return {
            "subject_type": "DatabaseSiteCapability",
            "expected_database": self.expected_database,
            "strict_contract_subject_hash": self.strict_contract_subject_hash,
            "database_catalog_evidence_sha256": self.database_catalog_evidence_sha256,
            "physical_storage_evidence_sha256": self.physical_storage_evidence_sha256,
            "required_check_ids": list(DATABASE_SITE_CAPABILITY_CHECK_IDS),
        }

    @property
    def subject_hash(self) -> str:
        return object_hash(
            "DatabaseSiteCapabilitySubject",
            "database-site-capability-subject/v1",
            self.as_dict(),
        )
