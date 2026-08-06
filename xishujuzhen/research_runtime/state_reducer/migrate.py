"""
ArangoDB migration: 创建Phase 2的state collections

对应132号P2-2.2/P2-3.1/P2-3.4/P2-5.1/P2-7.2。

遵循123号§55数据迁移原则：
- 新collection用幂等、可回滚migration创建
- 不动旧数据（NO-10约束）
- 生产图、候选图、实验快照分开
"""

import os
from arango import ArangoClient
from arango.exceptions import CollectionCreateError

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
DB_USER = os.environ.get("ARANGO_USER", "root")
DB_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")

# Phase 2需要创建的collections
PHASE2_COLLECTIONS = [
    # P2-2: 工作区
    {"name": "workspaces", "type": "document"},
    # P2-3: 研究义务
    {"name": "obligations", "type": "document"},
    {"name": "obligation_relations", "type": "document"},   # 超边relation document
    {"name": "obligation_edges", "type": "edge"},            # 超边participant edges
    # P2-5: 证据
    {"name": "evidence", "type": "document"},
    # P2-7: 卡点标注校准集
    {"name": "stall_annotations", "type": "document"},
]


def create_phase2_collections(
    db_name: str = DB_NAME,
    username: str = DB_USER,
    password: str = DB_PASS,
    host: str = ARANGO_HOST,
    dry_run: bool = False,
) -> dict:
    """
    幂等创建Phase 2的state collections。
    已存在的collection跳过，不报错。

    返回：{"created": [...], "skipped": [...], "failed": [...]}
    """
    result = {"created": [], "skipped": [], "failed": []}

    if dry_run:
        for col in PHASE2_COLLECTIONS:
            result["skipped"].append(col["name"])
        return result

    client = ArangoClient(hosts=host)
    db = client.db(db_name, username=username, password=password)

    existing = {c["name"] for c in db.collections()}

    for col_def in PHASE2_COLLECTIONS:
        name = col_def["name"]
        col_type = col_def["type"]

        if name in existing:
            result["skipped"].append(name)
            continue

        try:
            if col_type == "document":
                db.create_collection(name)
            elif col_type == "edge":
                db.create_collection(name, edge=True)
            result["created"].append(name)
        except CollectionCreateError as e:
            result["failed"].append(f"{name}: {e}")

    # 创建索引
    _create_indexes(db, result)

    return result


def _create_indexes(db, result: dict):
    """为Phase 2 collections创建索引"""
    created_or_skipped = set(result["created"]) | set(result["skipped"])

    try:
        # workspaces索引
        if "workspaces" in created_or_skipped:
            ws = db.collection("workspaces")
            ws.add_persistent_index(fields=["workspace_id"], unique=True, name="idx_ws_id")
            ws.add_persistent_index(fields=["task_id"], name="idx_ws_task")
            ws.add_persistent_index(fields=["timestamp"], name="idx_ws_ts")

        # obligations索引
        if "obligations" in created_or_skipped:
            obl = db.collection("obligations")
            obl.add_persistent_index(fields=["obligation_id"], unique=True, name="idx_obl_id")
            obl.add_persistent_index(fields=["task_id"], name="idx_obl_task")
            obl.add_persistent_index(fields=["type"], name="idx_obl_type")
            obl.add_persistent_index(fields=["status"], name="idx_obl_status")

        # obligation_relations索引（超边relation document）
        if "obligation_relations" in created_or_skipped:
            rel = db.collection("obligation_relations")
            rel.add_persistent_index(fields=["relation_id"], unique=True, name="idx_rel_id")
            rel.add_persistent_index(fields=["mode"], name="idx_rel_mode")  # all/any

        # obligation_edges索引（超边participant edges）
        if "obligation_edges" in created_or_skipped:
            edg = db.collection("obligation_edges")
            edg.add_persistent_index(fields=["_from"], name="idx_oe_from")
            edg.add_persistent_index(fields=["_to"], name="idx_oe_to")
            edg.add_persistent_index(fields=["role"], name="idx_oe_role")  # source/target

        # evidence索引
        if "evidence" in created_or_skipped:
            ev = db.collection("evidence")
            ev.add_persistent_index(fields=["evidence_id"], unique=True, name="idx_ev_id")
            ev.add_persistent_index(fields=["claim_id"], name="idx_ev_claim")
            ev.add_persistent_index(fields=["kind"], name="idx_ev_kind")
            ev.add_persistent_index(fields=["status"], name="idx_ev_status")

        # stall_annotations索引
        if "stall_annotations" in created_or_skipped:
            sa = db.collection("stall_annotations")
            sa.add_persistent_index(fields=["annotation_id"], unique=True, name="idx_sa_id")
            sa.add_persistent_index(fields=["run_id"], name="idx_sa_run")
            sa.add_persistent_index(fields=["stall_type"], name="idx_sa_type")

    except Exception as e:
        result["failed"].append(f"index_creation: {e}")


def drop_phase2_collections(
    db_name: str = DB_NAME,
    username: str = DB_USER,
    password: str = DB_PASS,
    host: str = ARANGO_HOST,
) -> dict:
    """
    回滚：删除Phase 2的state collections。
    仅用于migration失败时的回滚，不用于正常操作。
    """
    result = {"dropped": [], "failed": []}

    client = ArangoClient(hosts=host)
    db = client.db(db_name, username=username, password=password)

    for col_def in PHASE2_COLLECTIONS:
        name = col_def["name"]
        try:
            db.delete_collection(name)
            result["dropped"].append(name)
        except Exception as e:
            result["failed"].append(f"{name}: {e}")

    return result
