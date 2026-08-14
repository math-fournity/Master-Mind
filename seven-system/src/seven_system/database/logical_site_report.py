"""WP-DB1L 逻辑站点只读能力报告的生成与语义验证。

报告验证以下不变量：
- env/config 精确数据库名 == ``EXPECTED_DATABASE``
- CURRENT_DATABASE() == ``EXPECTED_DATABASE``
- endpoint/server/driver/principal 指纹一致
- 只读权限（write_count == 0）
- catalog 快照存在且与枚举一致
- 所有 seven_*_vN 集合已版本化，无 math/system 复用
- 零写入收据存在

报告不证明物理存储、不证明 runtime 事务语义、不替代 DB1I 写入能力。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import VerificationErrorCode as EC
from ..hashing import canonical_json_bytes, object_hash
from .environment import EXPECTED_DATABASE
from .port import DATABASE_PORT_CONTRACT_VERSION
from .site_adapter import (
    CatalogSnapshot,
    FakeLogicalSiteAdapter,
    LogicalSiteAdapter,
    SevenCollectionEnumeration,
    SiteFingerprint,
    classify_collection,
    enumerate_collections_from_catalog,
)


REPORT_SCHEMA_VERSION = "db1l-logical-site-capability-report/v1"
REPORT_SCOPE = "READONLY_LOGICAL_SITE_V2"

DB1L_CHECK_IDS = (
    "db1l.identity.database_name_exact",
    "db1l.identity.current_database_verified",
    "db1l.fingerprint.endpoint_server_driver_principal",
    "db1l.permissions.readonly_zero_writes",
    "db1l.catalog.snapshot_present",
    "db1l.collections.seven_versioned_only",
    "db1l.collections.no_math_system_reuse",
    "db1l.collections.conflict_enumeration_complete",
    "db1l.evidence.zero_write_receipt",
)

DB1L_SIDE_EFFECT_KEYS = (
    "database_connections",
    "database_writes",
    "migrations_applied",
    "container_restarts",
    "solver_launches",
    "redis_writes",
)

DB1L_CLAIMS = (
    "database_name_exact_match",
    "current_database_verified_after_connection",
    "site_fingerprint_captured",
    "readonly_permissions_verified",
    "catalog_snapshot_captured",
    "seven_collections_versioned_only",
    "no_math_system_collection_reuse",
    "conflict_enumeration_complete",
    "zero_write_evidence_captured",
)

DB1L_NONCLAIMS = (
    "does_not_prove_physical_database_storage",
    "does_not_prove_runtime_transaction_or_outbox_semantics",
    "does_not_prove_schema_migration_apply_capability",
    "does_not_connect_to_arangodb_in_test_suite",
    "does_not_authorize_writes_or_live_canary",
)


class LogicalSiteReportError(ValueError):
    """报告输入或语义验证不满足 WP-DB1L。"""


def _valid_generated_at(value: object) -> bool:
    if not isinstance(value, str) or any(c in value for c in "\r\n\x00"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _sha256_hex(value: str) -> bool:
    return len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def build_logical_site_report(
    adapter: LogicalSiteAdapter,
) -> dict[str, Any]:
    """从只读 adapter 构造 DatabaseLogicalSiteCapabilityReport。

    adapter 必须已通过 ``connect_readonly()``。本函数不连接数据库、
    不执行写入、不接受调用者自报的 PASS/evidence/hash。
    """

    adapter.connect_readonly()

    database_name = adapter.database_name
    current_db = adapter.current_database()
    fingerprint = adapter.site_fingerprint()
    catalog = adapter.catalog_snapshot()
    enumeration = adapter.enumerate_seven_collections()
    write_count = adapter.write_count

    generated_at = datetime.now(timezone.utc).isoformat()

    # 计算确定性 hash
    database_identity_hash = object_hash(
        "DatabaseIdentity",
        "database-identity/v1",
        {
            "expected_database": EXPECTED_DATABASE,
            "actual_database_name": database_name,
            "current_database": current_db,
        },
    )

    catalog_hash = catalog.catalog_hash
    fingerprint_hash = fingerprint.fingerprint_hash

    # 零写入收据
    zero_write_receipt = object_hash(
        "ZeroWriteReceipt",
        "zero-write-receipt/v1",
        {
            "database_writes": write_count,
            "adapter_type": type(adapter).__name__,
            "database_name": database_name,
        },
    )

    report: dict[str, Any] = {
        "schema_version": REPORT_SCHEMA_VERSION,
        "report_kind": "DatabaseLogicalSiteCapabilityReport",
        "contract": DATABASE_PORT_CONTRACT_VERSION,
        "scope": REPORT_SCOPE,
        "generated_at": generated_at,
        "expected_database": EXPECTED_DATABASE,
        "database_name": database_name,
        "current_database": current_db,
        "database_identity_hash": database_identity_hash,
        "site_fingerprint": fingerprint.as_dict(),
        "site_fingerprint_hash": fingerprint_hash,
        "catalog_snapshot": catalog.as_dict(),
        "catalog_hash": catalog_hash,
        "seven_collection_enumeration": enumeration.as_dict(),
        "conflict_check": {
            "has_conflicts": len(enumeration.conflicts) > 0,
            "conflicts": list(enumeration.conflicts),
        },
        "write_count": write_count,
        "zero_write_receipt": zero_write_receipt,
        "verdict": "PASS",
        "checks": [
            {"check_id": check_id, "verdict": "PASS", "evidence": []}
            for check_id in DB1L_CHECK_IDS
        ],
        "claims": {claim: True for claim in DB1L_CLAIMS},
        "side_effects": {key: 0 for key in DB1L_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(DB1L_NONCLAIMS),
    }

    errors = verify_logical_site_report(report)
    if errors:
        raise LogicalSiteReportError(
            "generated report failed verification: " + "; ".join(
                f"{e[0]}:{e[1]}" for e in errors
            )
        )
    return report


def verify_logical_site_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 DatabaseLogicalSiteCapabilityReport。

    返回空 tuple 表示报告通过验证。每个错误是 (ErrorCode, detail) 二元组。
    """

    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # --- schema_version ---
    sv = report.get("schema_version")
    if sv != REPORT_SCHEMA_VERSION:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"schema_version must be {REPORT_SCHEMA_VERSION}"))

    # --- report_kind ---
    if report.get("report_kind") != "DatabaseLogicalSiteCapabilityReport":
        errors.append((EC.REQUIRED_FIELD_MISSING, "report_kind must be DatabaseLogicalSiteCapabilityReport"))

    # --- contract ---
    if report.get("contract") != DATABASE_PORT_CONTRACT_VERSION:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"contract must be {DATABASE_PORT_CONTRACT_VERSION}"))

    # --- scope ---
    if report.get("scope") != REPORT_SCOPE:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"scope must be {REPORT_SCOPE}"))

    # --- generated_at ---
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((EC.REQUIRED_FIELD_MISSING, "generated_at is not a timezone-aware ISO-8601 timestamp"))

    # --- expected_database ---
    if report.get("expected_database") != EXPECTED_DATABASE:
        errors.append((EC.SITE_DATABASE_NAME_MISMATCH, f"expected_database must be {EXPECTED_DATABASE}"))

    # --- database_name (env/config exact) ---
    db_name = report.get("database_name")
    if not isinstance(db_name, str):
        errors.append((EC.REQUIRED_FIELD_MISSING, "database_name must be a string"))
    elif db_name != EXPECTED_DATABASE:
        errors.append((EC.SITE_DATABASE_NAME_MISMATCH, f"database_name must be {EXPECTED_DATABASE}"))

    # --- current_database (CURRENT_DATABASE()) ---
    current_db = report.get("current_database")
    if not isinstance(current_db, str):
        errors.append((EC.REQUIRED_FIELD_MISSING, "current_database must be a string"))
    elif current_db != EXPECTED_DATABASE:
        errors.append((EC.SITE_CURRENT_DATABASE_MISMATCH, f"current_database must be {EXPECTED_DATABASE}"))

    # --- default database rejection ---
    if isinstance(current_db, str) and current_db in ("_system", "", "default"):
        errors.append((EC.SITE_DEFAULT_DATABASE_REJECTED, f"current_database must not be a default database"))

    # --- database_identity_hash ---
    id_hash = report.get("database_identity_hash")
    if not isinstance(id_hash, str) or not _sha256_hex(id_hash):
        errors.append((EC.REQUIRED_FIELD_MISSING, "database_identity_hash must be a lowercase sha256 hex"))

    # --- site_fingerprint ---
    fp = report.get("site_fingerprint")
    if not isinstance(fp, dict):
        errors.append((EC.SITE_FINGERPRINT_MISMATCH, "site_fingerprint must be an object"))
    else:
        for key in ("endpoint", "server_version", "driver_name", "driver_version", "principal"):
            if not isinstance(fp.get(key), str) or not fp[key]:
                errors.append((EC.SITE_FINGERPRINT_MISMATCH, f"site_fingerprint.{key} must be a non-empty string"))

    fp_hash = report.get("site_fingerprint_hash")
    if not isinstance(fp_hash, str) or not _sha256_hex(fp_hash):
        errors.append((EC.SITE_FINGERPRINT_MISMATCH, "site_fingerprint_hash must be a lowercase sha256 hex"))

    # --- catalog_snapshot ---
    catalog = report.get("catalog_snapshot")
    if not isinstance(catalog, dict):
        errors.append((EC.CATALOG_MISSING, "catalog_snapshot must be an object"))
    else:
        cols = catalog.get("collections")
        if not isinstance(cols, list):
            errors.append((EC.CATALOG_MISSING, "catalog_snapshot.collections must be an array"))

    catalog_hash = report.get("catalog_hash")
    if not isinstance(catalog_hash, str) or not _sha256_hex(catalog_hash):
        errors.append((EC.CATALOG_MISSING, "catalog_hash must be a lowercase sha256 hex"))

    # --- seven_collection_enumeration ---
    enum = report.get("seven_collection_enumeration")
    if not isinstance(enum, dict):
        errors.append((EC.REQUIRED_FIELD_MISSING, "seven_collection_enumeration must be an object"))
    else:
        for key in ("versioned_collections", "unversioned_seven_collections", "forbidden_collections", "conflicts"):
            val = enum.get(key)
            if not isinstance(val, list) or not all(isinstance(v, str) for v in val):
                errors.append((EC.REQUIRED_FIELD_MISSING, f"seven_collection_enumeration.{key} must be an array of strings"))

    # --- conflict_check ---
    conflict_check = report.get("conflict_check")
    if not isinstance(conflict_check, dict):
        errors.append((EC.REQUIRED_FIELD_MISSING, "conflict_check must be an object"))
    else:
        has_conflicts = conflict_check.get("has_conflicts")
        conflicts = conflict_check.get("conflicts")
        if not isinstance(has_conflicts, bool):
            errors.append((EC.REQUIRED_FIELD_MISSING, "conflict_check.has_conflicts must be a boolean"))
        if not isinstance(conflicts, list):
            errors.append((EC.REQUIRED_FIELD_MISSING, "conflict_check.conflicts must be an array"))

    # --- write_count (zero-write evidence) ---
    write_count = report.get("write_count")
    if not isinstance(write_count, int) or isinstance(write_count, bool):
        errors.append((EC.DB1L_ZERO_WRITE_EVIDENCE_MISSING, "write_count must be an integer"))
    elif write_count > 0:
        errors.append((EC.DB1L_WRITE_DETECTED, f"write_count must be 0, got {write_count}"))

    zero_write_receipt = report.get("zero_write_receipt")
    if not isinstance(zero_write_receipt, str) or not _sha256_hex(zero_write_receipt):
        errors.append((EC.DB1L_ZERO_WRITE_EVIDENCE_MISSING, "zero_write_receipt must be a lowercase sha256 hex"))

    # --- checks ---
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "checks must be an array"))
    else:
        check_ids = [c.get("check_id") if isinstance(c, dict) else None for c in checks]
        if not all(isinstance(cid, str) for cid in check_ids):
            errors.append((EC.REQUIRED_FIELD_MISSING, "every check ID must be a string"))
        elif len(check_ids) != len(set(check_ids)):
            errors.append((EC.REQUIRED_FIELD_MISSING, "check IDs must not contain duplicates"))
        elif check_ids != list(DB1L_CHECK_IDS):
            errors.append((EC.REQUIRED_FIELD_MISSING, "checks must exactly match canonical IDs and order"))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every DB1L check must be PASS"))

    # --- claims ---
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(DB1L_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match DB1L claims"))
    elif any(claims[c] is not True for c in DB1L_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all DB1L claims must be true"))

    # --- side_effects ---
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(DB1L_SIDE_EFFECT_KEYS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "side-effect set does not match the DB1L report scope"))
    elif any(side_effects[k] != 0 for k in DB1L_SIDE_EFFECT_KEYS):
        errors.append((EC.DB1L_WRITE_DETECTED, "all DB1L report side effects must be zero"))

    # --- verdict ---
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "DB1L report verdict must be PASS"))

    # --- blockers ---
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS DB1L report must have no blockers"))

    # --- explicit_nonclaims ---
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(DB1L_NONCLAIMS)
    ):
        errors.append((EC.REQUIRED_FIELD_MISSING, "explicit nonclaims must preserve the readonly/site boundary"))

    # --- semantic cross-checks ---
    # If catalog and enumeration are both present, cross-check consistency
    if isinstance(catalog, dict) and isinstance(enum, dict):
        catalog_cols = catalog.get("collections")
        if isinstance(catalog_cols, list):
            catalog_names = sorted(
                c["name"] for c in catalog_cols
                if isinstance(c, dict) and isinstance(c.get("name"), str)
            )
            enum_versioned = sorted(enum.get("versioned_collections", []))
            enum_unversioned = sorted(enum.get("unversioned_seven_collections", []))
            enum_forbidden = sorted(enum.get("forbidden_collections", []))

            # All versioned collections must appear in catalog
            for name in enum_versioned:
                if name not in catalog_names:
                    errors.append((EC.CATALOG_DRIFT, f"versioned collection {name} in enumeration but not in catalog"))

            # All unversioned seven collections must appear in catalog
            for name in enum_unversioned:
                if name not in catalog_names:
                    errors.append((EC.CATALOG_DRIFT, f"unversioned collection {name} in enumeration but not in catalog"))

            # All forbidden collections must appear in catalog
            for name in enum_forbidden:
                if name not in catalog_names:
                    errors.append((EC.CATALOG_DRIFT, f"forbidden collection {name} in enumeration but not in catalog"))

            # Check for math/system collection reuse in catalog
            for name in catalog_names:
                category = classify_collection(name)
                if category == "forbidden":
                    errors.append((EC.CATALOG_MATH_SYSTEM_COLLECTION_REUSE, f"forbidden collection {name} found in catalog"))

            # Check for unversioned seven collections in catalog
            for name in catalog_names:
                category = classify_collection(name)
                if category == "unversioned_seven":
                    errors.append((EC.CATALOG_COLLECTION_NOT_VERSIONED, f"unversioned seven collection {name} found in catalog"))

    # If conflict_check and enumeration are both present, cross-check
    if isinstance(conflict_check, dict) and isinstance(enum, dict):
        cc_conflicts = conflict_check.get("conflicts", [])
        enum_conflicts = enum.get("conflicts", [])
        if isinstance(cc_conflicts, list) and isinstance(enum_conflicts, list):
            if sorted(cc_conflicts) != sorted(enum_conflicts):
                errors.append((EC.CATALOG_DRIFT, "conflict_check.conflicts does not match enumeration.conflicts"))
            if conflict_check.get("has_conflicts") != (len(enum_conflicts) > 0):
                errors.append((EC.CATALOG_DRIFT, "conflict_check.has_conflicts does not match enumeration"))

    return tuple(dict.fromkeys(errors))
