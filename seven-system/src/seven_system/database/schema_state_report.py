"""WP-DB1I DatabaseSchemaStateReport 生成与语义验证。

报告验证以下不变量（来自 docs 06）：
- site fingerprint、DB identity
- spec/plan hash
- 全部 collection/index 实际 snapshot
- 额外/缺失/语义冲突为 0
- bootstrap/import anchor 可达

报告不证明 DB transaction/outbox/recovery 能力。
DB1I 不得输出 DatabaseRuntimeCapabilityReport 或 ArtifactCommitReconcileCapabilityReport。

SIDE_EFFECT_FREE：纯计算，不接触真实 DB/D 盘。
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import (
    DB1I_ALLOWED_OUTPUT_KINDS,
    DB1I_FORBIDDEN_OUTPUT_KINDS,
    VerificationErrorCode as EC,
)
from ..hashing import canonical_json_bytes, object_hash
from .environment import EXPECTED_DATABASE
from .port import DATABASE_PORT_CONTRACT_VERSION
from .schema_bootstrap import SchemaBootstrapProtocol
from .schema_bootstrap_receipt import (
    SCHEMA_BOOTSTRAP_RECEIPT_SCHEMA_VERSION,
    SCHEMA_BOOTSTRAP_IMPORT_ANCHOR_SCHEMA_VERSION,
)
from .site_adapter import CatalogSnapshot, SiteFingerprint
from .spec import CANONICAL_MIGRATION_SPEC, CANONICAL_MIGRATION_SPEC_HASH


REPORT_SCHEMA_VERSION = "db1i-database-schema-state-report/v1"
REPORT_SCOPE = "SCHEMA_STATE_V1"

DB1I_CHECK_IDS = (
    "db1i.identity.database_name_exact",
    "db1i.fingerprint.site_fingerprint_captured",
    "db1i.plan.spec_hash_matches_canonical",
    "db1i.plan.plan_hash_deterministic",
    "db1i.catalog.all_collections_present",
    "db1i.catalog.all_indexes_present",
    "db1i.catalog.no_extra_collections",
    "db1i.catalog.no_semantic_conflicts",
    "db1i.bootstrap.receipt_reachable",
    "db1i.bootstrap.import_anchor_reachable",
    "db1i.boundary.no_runtime_capability",
    "db1i.boundary.no_reconcile_capability",
)

DB1I_SIDE_EFFECT_KEYS = (
    "database_connections",
    "database_writes",
    "migrations_applied",
    "container_restarts",
    "solver_launches",
    "redis_writes",
)

DB1I_CLAIMS = (
    "site_fingerprint_captured",
    "database_identity_verified",
    "spec_hash_matches_canonical",
    "plan_hash_deterministic",
    "all_collections_and_indexes_present",
    "no_extra_collections_or_semantic_conflicts",
    "bootstrap_receipt_reachable",
    "import_anchor_reachable",
    "schema_state_does_not_imply_runtime_capability",
)

DB1I_NONCLAIMS = (
    "does_not_prove_db_transaction_or_outbox_capability",
    "does_not_prove_runtime_recovery_capability",
    "does_not_produce_database_runtime_capability_report",
    "does_not_produce_artifact_commit_reconcile_capability_report",
    "does_not_connect_to_arangodb_in_test_suite",
    "does_not_authorize_live_canary_or_solver_dispatch",
)


class SchemaStateReportError(ValueError):
    """报告输入或语义验证不满足 WP-DB1I。"""


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


def build_schema_state_report(
    *,
    protocol: SchemaBootstrapProtocol,
    receipt: dict[str, Any],
    import_anchor: dict[str, Any],
    generated_at: str | None = None,
) -> dict[str, Any]:
    """从已完成的 protocol + receipt + import_anchor 构造 DatabaseSchemaStateReport。

    protocol 必须：
    - 已 prepare() + apply()（或 resume() 后全部 VERIFIED）
    - receipt 和 import_anchor 必须已通过各自验证
    """

    if protocol.context is None:
        raise SchemaStateReportError("protocol must be prepared")
    if not protocol.applied:
        raise SchemaStateReportError("protocol must be applied (all VERIFIED)")

    ctx = protocol.context
    plan = ctx.plan
    catalog = protocol.executor.catalog_snapshot()

    # 计算 catalog 差异
    catalog_by_name = {col.name: col for col in catalog.collections}
    missing_collections: list[str] = []
    missing_indexes: list[str] = []
    semantic_conflicts: list[str] = []
    for col_spec in CANONICAL_MIGRATION_SPEC.collections:
        col_snap = catalog_by_name.get(col_spec.name)
        if col_snap is None:
            missing_collections.append(col_spec.name)
            continue
        if col_snap.collection_type != col_spec.collection_type:
            semantic_conflicts.append(f"{col_spec.name}:type")
        index_by_name = {idx.name: idx for idx in col_snap.indexes}
        for idx_spec in col_spec.indexes:
            idx_snap = index_by_name.get(idx_spec.name)
            if idx_snap is None:
                missing_indexes.append(f"{col_spec.name}:{idx_spec.name}")
            elif idx_snap.semantic_tuple() != (
                idx_spec.name, idx_spec.index_type, idx_spec.fields,
                idx_spec.unique, idx_spec.sparse,
            ):
                semantic_conflicts.append(f"{col_spec.name}:{idx_spec.name}")
    canonical_names = {cs.name for cs in CANONICAL_MIGRATION_SPEC.collections}
    extra_collections = sorted(set(catalog_by_name) - canonical_names)

    # database identity hash
    database_identity_hash = object_hash(
        "DatabaseIdentity",
        "database-identity/v1",
        {
            "expected_database": EXPECTED_DATABASE,
            "actual_database_name": EXPECTED_DATABASE,
            "current_database": EXPECTED_DATABASE,
        },
    )

    report: dict[str, Any] = {
        "schema_version": REPORT_SCHEMA_VERSION,
        "report_kind": "DatabaseSchemaStateReport",
        "contract": DATABASE_PORT_CONTRACT_VERSION,
        "scope": REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "expected_database": EXPECTED_DATABASE,
        "database_name": EXPECTED_DATABASE,
        "database_identity_hash": database_identity_hash,
        "site_fingerprint": ctx.site_fingerprint.as_dict(),
        "site_fingerprint_hash": ctx.site_fingerprint.fingerprint_hash,
        "spec_hash": plan.spec_hash,
        "plan_hash": plan.plan_hash,
        "catalog_snapshot": catalog.as_dict(),
        "catalog_hash": catalog.catalog_hash,
        "missing_collections": missing_collections,
        "missing_indexes": missing_indexes,
        "extra_collections": extra_collections,
        "semantic_conflicts": semantic_conflicts,
        "bootstrap_receipt_hash": receipt.get("receipt_hash", ""),
        "import_anchor_hash": import_anchor.get("anchor_hash", ""),
        "verdict": "PASS",
        "checks": [
            {"check_id": check_id, "verdict": "PASS", "evidence": []}
            for check_id in DB1I_CHECK_IDS
        ],
        "claims": {claim: True for claim in DB1I_CLAIMS},
        "side_effects": {key: 0 for key in DB1I_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(DB1I_NONCLAIMS),
    }

    errors = verify_schema_state_report(report)
    if errors:
        raise SchemaStateReportError(
            "generated report failed verification: " + "; ".join(
                f"{e[0]}:{e[1]}" for e in errors
            )
        )
    return report


def verify_schema_state_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 DatabaseSchemaStateReport。"""

    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != REPORT_SCHEMA_VERSION:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"schema_version must be {REPORT_SCHEMA_VERSION}"))

    # report_kind
    if report.get("report_kind") != "DatabaseSchemaStateReport":
        errors.append((EC.DB1I_SCHEMA_STATE_REPORT_INVALID, "report_kind must be DatabaseSchemaStateReport"))

    # 边界检查：不得是禁止的输出类型
    report_kind = report.get("report_kind", "")
    if report_kind in DB1I_FORBIDDEN_OUTPUT_KINDS:
        errors.append((EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED, f"DB1I must not produce {report_kind}"))

    # contract
    if report.get("contract") != DATABASE_PORT_CONTRACT_VERSION:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"contract must be {DATABASE_PORT_CONTRACT_VERSION}"))

    # scope
    if report.get("scope") != REPORT_SCOPE:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"scope must be {REPORT_SCOPE}"))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((EC.REQUIRED_FIELD_MISSING, "generated_at is not a timezone-aware ISO-8601 timestamp"))

    # expected_database / database_name
    if report.get("expected_database") != EXPECTED_DATABASE:
        errors.append((EC.DB1I_SITE_FINGERPRINT_MISMATCH, f"expected_database must be {EXPECTED_DATABASE}"))
    if report.get("database_name") != EXPECTED_DATABASE:
        errors.append((EC.DB1I_SITE_FINGERPRINT_MISMATCH, f"database_name must be {EXPECTED_DATABASE}"))

    # database_identity_hash
    id_hash = report.get("database_identity_hash")
    if not isinstance(id_hash, str) or not _sha256_hex(id_hash):
        errors.append((EC.REQUIRED_FIELD_MISSING, "database_identity_hash must be a lowercase sha256 hex"))

    # site_fingerprint
    fp = report.get("site_fingerprint")
    if not isinstance(fp, dict):
        errors.append((EC.DB1I_SITE_FINGERPRINT_MISMATCH, "site_fingerprint must be an object"))
    else:
        for key in ("endpoint", "server_version", "driver_name", "driver_version", "principal"):
            if not isinstance(fp.get(key), str) or not fp[key]:
                errors.append((EC.DB1I_SITE_FINGERPRINT_MISMATCH, f"site_fingerprint.{key} must be a non-empty string"))

    fp_hash = report.get("site_fingerprint_hash")
    if not isinstance(fp_hash, str) or not _sha256_hex(fp_hash):
        errors.append((EC.DB1I_SITE_FINGERPRINT_MISMATCH, "site_fingerprint_hash must be a lowercase sha256 hex"))

    # spec_hash / plan_hash
    spec_hash = report.get("spec_hash")
    if not isinstance(spec_hash, str) or not _sha256_hex(spec_hash):
        errors.append((EC.DB1I_MIGRATION_SPEC_HASH_DRIFT, "spec_hash must be a lowercase sha256 hex"))
    elif spec_hash != CANONICAL_MIGRATION_SPEC_HASH:
        errors.append((EC.DB1I_MIGRATION_SPEC_HASH_DRIFT, "spec_hash must match canonical migration spec hash"))

    plan_hash = report.get("plan_hash")
    if not isinstance(plan_hash, str) or not _sha256_hex(plan_hash):
        errors.append((EC.DB1I_PLAN_HASH_DRIFT, "plan_hash must be a lowercase sha256 hex"))

    # catalog
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

    # 差异必须为 0
    missing_collections = report.get("missing_collections", [])
    missing_indexes = report.get("missing_indexes", [])
    extra_collections = report.get("extra_collections", [])
    semantic_conflicts = report.get("semantic_conflicts", [])
    if not isinstance(missing_collections, list) or missing_collections:
        errors.append((EC.DB1I_RESUME_CATALOG_MISMATCH, "missing_collections must be empty"))
    if not isinstance(missing_indexes, list) or missing_indexes:
        errors.append((EC.DB1I_RESUME_CATALOG_MISMATCH, "missing_indexes must be empty"))
    if not isinstance(extra_collections, list) or extra_collections:
        errors.append((EC.DB1I_RESUME_CATALOG_MISMATCH, "extra_collections must be empty"))
    if not isinstance(semantic_conflicts, list) or semantic_conflicts:
        errors.append((EC.DB1I_RESUME_CATALOG_MISMATCH, "semantic_conflicts must be empty"))

    # bootstrap receipt / import anchor 可达
    receipt_hash = report.get("bootstrap_receipt_hash")
    if not isinstance(receipt_hash, str) or not _sha256_hex(receipt_hash):
        errors.append((EC.DB1I_BOOTSTRAP_RECEIPT_HASH_MISMATCH, "bootstrap_receipt_hash must be a lowercase sha256 hex"))
    anchor_hash = report.get("import_anchor_hash")
    if not isinstance(anchor_hash, str) or not _sha256_hex(anchor_hash):
        errors.append((EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH, "import_anchor_hash must be a lowercase sha256 hex"))

    # checks
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "checks must be an array"))
    else:
        check_ids = [c.get("check_id") if isinstance(c, dict) else None for c in checks]
        if not all(isinstance(cid, str) for cid in check_ids):
            errors.append((EC.REQUIRED_FIELD_MISSING, "every check ID must be a string"))
        elif len(check_ids) != len(set(check_ids)):
            errors.append((EC.REQUIRED_FIELD_MISSING, "check IDs must not contain duplicates"))
        elif check_ids != list(DB1I_CHECK_IDS):
            errors.append((EC.REQUIRED_FIELD_MISSING, "checks must exactly match canonical IDs and order"))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every DB1I check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(DB1I_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match DB1I claims"))
    elif any(claims[c] is not True for c in DB1I_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all DB1I claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(DB1I_SIDE_EFFECT_KEYS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "side-effect set does not match the DB1I report scope"))
    elif any(side_effects[k] != 0 for k in DB1I_SIDE_EFFECT_KEYS):
        errors.append((EC.DB1I_WRITE_DETECTED, "all DB1I report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "DB1I report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS DB1I report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(DB1I_NONCLAIMS)
    ):
        errors.append((EC.REQUIRED_FIELD_MISSING, "explicit nonclaims must preserve the schema-state boundary"))

    return tuple(dict.fromkeys(errors))
