"""WP-DB1I SchemaBootstrapReceipt + SchemaBootstrapImportAnchor。

SchemaBootstrapReceipt：
- 全部 DDL actions 验证后生成
- 绑定 ledger root hash、permit consumption、post-catalog hash、fence
- 与外部 root-seal 一起构成 bootstrap 完成证据

SchemaBootstrapImportAnchor：
- seven_schema_migrations_v1 可用后，将 plan/events/receipts 按原 hash 导入
- anchor 同时记录 D 盘 root seal 和 DB 导入 record IDs/hash 列表
- 正反向校验集合完全相等后才可完成 bootstrap

SIDE_EFFECT_FREE：纯计算，不接触真实 DB/D 盘。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import VerificationErrorCode as EC
from ..hashing import canonical_json_bytes, object_hash
from .schema_bootstrap import ActionReceipt, SchemaBootstrapContext, SchemaBootstrapProtocol


SCHEMA_BOOTSTRAP_RECEIPT_SCHEMA_VERSION = "seven-schema-bootstrap-receipt/v1"
SCHEMA_BOOTSTRAP_IMPORT_ANCHOR_SCHEMA_VERSION = "seven-schema-bootstrap-import-anchor/v1"


class SchemaBootstrapReceiptError(Exception):
    """receipt/anchor 构造或验证不满足 WP-DB1I。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def _compute_receipt_hash(receipt: dict[str, Any]) -> str:
    """计算 receipt_hash = sha256(canonical_json(receipt with receipt_hash=null))。"""
    obj = dict(receipt)
    obj["receipt_hash"] = None
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def _compute_anchor_hash(anchor: dict[str, Any]) -> str:
    """计算 anchor_hash = sha256(canonical_json(anchor with anchor_hash=null))。"""
    obj = dict(anchor)
    obj["anchor_hash"] = None
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def build_schema_bootstrap_receipt(
    protocol: SchemaBootstrapProtocol,
    *,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """从已完成的 protocol 构造 SchemaBootstrapReceipt。

    protocol 必须：
    - 已 prepare()
    - 已 apply() 且全部 VERIFIED（或 resume() 后全部 VERIFIED）
    """

    if protocol.context is None:
        raise SchemaBootstrapReceiptError(
            EC.DB1I_BOOTSTRAP_RECEIPT_HASH_MISMATCH,
            "protocol must be prepared before building receipt",
        )
    if not protocol.applied:
        raise SchemaBootstrapReceiptError(
            EC.DB1I_BOOTSTRAP_RECEIPT_HASH_MISMATCH,
            "protocol must be applied (all VERIFIED) before building receipt",
        )

    ctx = protocol.context
    plan = ctx.plan

    # 验证全部 action 为 VERIFIED
    for receipt in protocol.action_receipts:
        if receipt.state != "VERIFIED":
            raise SchemaBootstrapReceiptError(
                EC.DB1I_UNKNOWN_OUTCOME,
                f"action {receipt.action_id} state is {receipt.state}, not VERIFIED",
            )

    ledger_root_hash = protocol.ledger_root_hash
    post_catalog_hash = protocol.post_catalog_hash

    receipt: dict[str, Any] = {
        "schema_version": SCHEMA_BOOTSTRAP_RECEIPT_SCHEMA_VERSION,
        "report_kind": "SchemaBootstrapReceipt",
        "generated_at": generated_at or _now_utc(),
        "plan_hash": plan.plan_hash,
        "spec_hash": plan.spec_hash,
        "site_fingerprint_hash": ctx.site_fingerprint.fingerprint_hash,
        "permit_id": ctx.permit.get("permit_id", ""),
        "gate_decision_id": ctx.gate_decision.get("decision_id", ""),
        "gate_decision_verified": ctx.gate_decision_verified,
        "fence_token": ctx.fence_token,
        "maintenance_window": ctx.maintenance_window,
        "ledger_root_hash": ledger_root_hash,
        "post_catalog_hash": post_catalog_hash,
        "action_count": len(protocol.action_receipts),
        "action_receipts": [r.as_dict() for r in protocol.action_receipts],
        "receipt_hash_algorithm": "sha256(canonical-json-with-receipt_hash-null)",
        "receipt_hash": None,
    }
    receipt["receipt_hash"] = _compute_receipt_hash(receipt)
    return receipt


def verify_schema_bootstrap_receipt(
    receipt: dict[str, Any],
) -> tuple[tuple[EC, str], ...]:
    """语义验证 SchemaBootstrapReceipt。"""

    errors: list[tuple[EC, str]] = []

    if not isinstance(receipt, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "receipt must be an object"),)

    if receipt.get("schema_version") != SCHEMA_BOOTSTRAP_RECEIPT_SCHEMA_VERSION:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"schema_version must be {SCHEMA_BOOTSTRAP_RECEIPT_SCHEMA_VERSION}"))
    if receipt.get("report_kind") != "SchemaBootstrapReceipt":
        errors.append((EC.REQUIRED_FIELD_MISSING, "report_kind must be SchemaBootstrapReceipt"))

    # hash 字段
    for field_name in ("plan_hash", "spec_hash", "site_fingerprint_hash", "ledger_root_hash", "post_catalog_hash"):
        val = receipt.get(field_name, "")
        if not isinstance(val, str) or len(val) != 64:
            errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must be 64-char hex"))

    # gate decision
    if not receipt.get("gate_decision_verified"):
        errors.append((EC.DB1I_HUMAN_GATE_DECISION_MISSING, "gate_decision_verified must be true"))

    # action receipts
    action_receipts = receipt.get("action_receipts", [])
    if not isinstance(action_receipts, list) or not action_receipts:
        errors.append((EC.REQUIRED_FIELD_MISSING, "action_receipts must be a non-empty array"))
    else:
        for idx, ar in enumerate(action_receipts):
            if not isinstance(ar, dict):
                errors.append((EC.REQUIRED_FIELD_MISSING, f"action_receipt {idx} must be an object"))
                continue
            if ar.get("state") != "VERIFIED":
                errors.append((EC.DB1I_UNKNOWN_OUTCOME, f"action_receipt {idx} state is {ar.get('state')}, not VERIFIED"))

    # receipt_hash 重算
    expected_hash = _compute_receipt_hash(receipt)
    if receipt.get("receipt_hash") != expected_hash:
        errors.append((EC.DB1I_BOOTSTRAP_RECEIPT_HASH_MISMATCH, "receipt_hash mismatch"))

    return tuple(dict.fromkeys(errors))


def build_schema_bootstrap_import_anchor(
    *,
    receipt: dict[str, Any],
    ledger_root_hash: str,
    db_import_record_ids: list[str],
    db_import_record_hashes: list[str],
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 SchemaBootstrapImportAnchor。

    seven_schema_migrations_v1 可用后，将 plan/events/receipts 按原 hash 导入 DB。
    anchor 同时记录 D 盘 root seal 和 DB 导入 record IDs/hash 列表。

    db_import_record_ids 和 db_import_record_hashes 长度必须相等，
    且每个 record hash 是对应导入记录的确定性 hash。
    """

    if not isinstance(receipt, dict):
        raise SchemaBootstrapReceiptError(
            EC.REQUIRED_FIELD_MISSING, "receipt must be an object"
        )
    receipt_errors = verify_schema_bootstrap_receipt(receipt)
    if receipt_errors:
        raise SchemaBootstrapReceiptError(
            EC.DB1I_BOOTSTRAP_RECEIPT_HASH_MISMATCH,
            f"receipt verification failed: {receipt_errors[0][1]}",
        )

    if not isinstance(ledger_root_hash, str) or len(ledger_root_hash) != 64:
        raise SchemaBootstrapReceiptError(
            EC.DB1I_LEDGER_TAMPERED, "ledger_root_hash must be 64-char hex"
        )
    if len(db_import_record_ids) != len(db_import_record_hashes):
        raise SchemaBootstrapReceiptError(
            EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH,
            "db_import_record_ids and db_import_record_hashes length mismatch",
        )
    for h in db_import_record_hashes:
        if not isinstance(h, str) or len(h) != 64:
            raise SchemaBootstrapReceiptError(
                EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH,
                "each db_import_record_hash must be 64-char hex",
            )

    anchor: dict[str, Any] = {
        "schema_version": SCHEMA_BOOTSTRAP_IMPORT_ANCHOR_SCHEMA_VERSION,
        "report_kind": "SchemaBootstrapImportAnchor",
        "generated_at": generated_at or _now_utc(),
        "receipt_hash": receipt.get("receipt_hash", ""),
        "plan_hash": receipt.get("plan_hash", ""),
        "spec_hash": receipt.get("spec_hash", ""),
        "site_fingerprint_hash": receipt.get("site_fingerprint_hash", ""),
        "d_volume_root_seal": ledger_root_hash,
        "db_import_record_ids": list(db_import_record_ids),
        "db_import_record_hashes": list(db_import_record_hashes),
        "import_record_count": len(db_import_record_ids),
        "anchor_hash_algorithm": "sha256(canonical-json-with-anchor_hash-null)",
        "anchor_hash": None,
    }
    anchor["anchor_hash"] = _compute_anchor_hash(anchor)
    return anchor


def verify_schema_bootstrap_import_anchor(
    anchor: dict[str, Any],
) -> tuple[tuple[EC, str], ...]:
    """语义验证 SchemaBootstrapImportAnchor。"""

    errors: list[tuple[EC, str]] = []

    if not isinstance(anchor, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "anchor must be an object"),)

    if anchor.get("schema_version") != SCHEMA_BOOTSTRAP_IMPORT_ANCHOR_SCHEMA_VERSION:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"schema_version must be {SCHEMA_BOOTSTRAP_IMPORT_ANCHOR_SCHEMA_VERSION}"))
    if anchor.get("report_kind") != "SchemaBootstrapImportAnchor":
        errors.append((EC.REQUIRED_FIELD_MISSING, "report_kind must be SchemaBootstrapImportAnchor"))

    for field_name in ("receipt_hash", "plan_hash", "spec_hash", "site_fingerprint_hash", "d_volume_root_seal"):
        val = anchor.get(field_name, "")
        if not isinstance(val, str) or len(val) != 64:
            errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must be 64-char hex"))

    # import records
    record_ids = anchor.get("db_import_record_ids", [])
    record_hashes = anchor.get("db_import_record_hashes", [])
    if not isinstance(record_ids, list) or not isinstance(record_hashes, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "db_import_record_ids/hashes must be arrays"))
    elif len(record_ids) != len(record_hashes):
        errors.append((EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH, "record IDs and hashes length mismatch"))
    elif anchor.get("import_record_count") != len(record_ids):
        errors.append((EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH, "import_record_count does not match actual count"))
    else:
        for idx, h in enumerate(record_hashes):
            if not isinstance(h, str) or len(h) != 64:
                errors.append((EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH, f"record hash {idx} must be 64-char hex"))

    # anchor_hash 重算
    expected_hash = _compute_anchor_hash(anchor)
    if anchor.get("anchor_hash") != expected_hash:
        errors.append((EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH, "anchor_hash mismatch"))

    return tuple(dict.fromkeys(errors))
