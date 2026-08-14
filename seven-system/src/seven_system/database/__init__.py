"""Seven System 的 fail-closed 数据库契约。

这个 package 不会在 import 时读取环境、构造客户端或执行 migration。真实
driver 只允许由 :mod:`seven_system.database.arango_port` 延迟加载。
"""

from .capability import (
    DATABASE_CAPABILITY_CHECK_IDS,
    DATABASE_SITE_CHECK_IDS,
    DATABASE_SITE_CAPABILITY_CHECK_IDS,
    STRICT_DATABASE_CONTRACT_CHECK_IDS,
    DatabaseSiteCapabilitySubject,
    StrictDatabaseContractSubject,
)
from .environment import DatabaseEnvironment, EXPECTED_DATABASE
from .contract_report import (
    StrictDbContractReportError,
    build_strict_db_contract_report,
    strict_db_implementation_tree_files,
    strict_db_implementation_tree_hash,
    verify_strict_db_contract_report,
)
from .errors import (
    CollectionNotAllowedError,
    DatabaseConnectionError,
    DatabaseConfigurationError,
    DatabaseContractError,
    DatabaseDriverUnavailableError,
    DatabaseIdentityError,
    MigrationPlanMismatchError,
    MissingDatabaseEnvironmentError,
    SchemaConflictError,
)
from .migration import MigrationPlan, plan_migration
from .port import (
    CollectionSnapshot,
    DatabaseCatalogPort,
    IndexSnapshot,
    StrictDatabasePort,
)
from .spec import (
    ALLOWED_COLLECTIONS,
    CANONICAL_MIGRATION_SPEC,
    CANONICAL_MIGRATION_SPEC_HASH,
    CollectionSpec,
    IndexSpec,
    MigrationSpec,
    validate_collection_name,
)
from .site_adapter import (
    CatalogSnapshot as SiteCatalogSnapshot,
    FakeLogicalSiteAdapter,
    LogicalSiteAdapter,
    SevenCollectionEnumeration,
    SiteFingerprint,
    classify_collection,
    enumerate_collections_from_catalog,
)
from .logical_site_report import (
    DB1L_CHECK_IDS,
    DB1L_CLAIMS,
    DB1L_NONCLAIMS,
    DB1L_SIDE_EFFECT_KEYS,
    LogicalSiteReportError,
    REPORT_SCHEMA_VERSION as DB1L_REPORT_SCHEMA_VERSION,
    build_logical_site_report,
    verify_logical_site_report,
)

__all__ = [
    "ALLOWED_COLLECTIONS",
    "CANONICAL_MIGRATION_SPEC",
    "CANONICAL_MIGRATION_SPEC_HASH",
    "CollectionNotAllowedError",
    "CollectionSnapshot",
    "CollectionSpec",
    "DATABASE_CAPABILITY_CHECK_IDS",
    "DATABASE_SITE_CHECK_IDS",
    "DatabaseSiteCapabilitySubject",
    "DatabaseCatalogPort",
    "DatabaseConfigurationError",
    "DatabaseConnectionError",
    "DatabaseContractError",
    "DatabaseDriverUnavailableError",
    "DatabaseEnvironment",
    "DatabaseIdentityError",
    "DB1L_CHECK_IDS",
    "DB1L_CLAIMS",
    "DB1L_NONCLAIMS",
    "DB1L_SIDE_EFFECT_KEYS",
    "DB1L_REPORT_SCHEMA_VERSION",
    "EXPECTED_DATABASE",
    "FakeLogicalSiteAdapter",
    "IndexSnapshot",
    "IndexSpec",
    "LogicalSiteAdapter",
    "LogicalSiteReportError",
    "MigrationPlan",
    "MigrationPlanMismatchError",
    "MigrationSpec",
    "MissingDatabaseEnvironmentError",
    "SchemaConflictError",
    "SevenCollectionEnumeration",
    "SiteCatalogSnapshot",
    "SiteFingerprint",
    "StrictDatabasePort",
    "StrictDbContractReportError",
    "STRICT_DATABASE_CONTRACT_CHECK_IDS",
    "DATABASE_SITE_CAPABILITY_CHECK_IDS",
    "StrictDatabaseContractSubject",
    "build_logical_site_report",
    "build_strict_db_contract_report",
    "classify_collection",
    "enumerate_collections_from_catalog",
    "plan_migration",
    "strict_db_implementation_tree_files",
    "strict_db_implementation_tree_hash",
    "validate_collection_name",
    "verify_logical_site_report",
    "verify_strict_db_contract_report",
]
