"""
ArangoDB migration: 创建Phase 1的event collections

遵循123号§55数据迁移原则：
- 新collection用幂等、可回滚migration创建
- 不动旧数据（NO-10约束）
- 生产图、候选图、实验快照分开

对应131号P1-3.2/P1-4.2。
"""

import os
from arango import ArangoClient
from arango.exceptions import CollectionCreateError

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")

# Phase 1需要创建的collections
PHASE1_COLLECTIONS = [
    {"name": "raw_events", "type": "document"},
    {"name": "semantic_events", "type": "document"},
    {"name": "checkpoints", "type": "document"},
    {"name": "run_manifests", "type": "document"},
]


def create_event_collections(
    db_name: str = DB_NAME,
    username: str = DB_USER,
    password: str = DB_PASS,
    host: str = ARANGO_HOST,
    dry_run: bool = False,
) -> dict:
    """
    幂等创建Phase 1的event collections。
    已存在的collection跳过，不报错。

    返回：{"created": [...], "skipped": [...], "failed": [...]}
    """
    result = {"created": [], "skipped": [], "failed": []}

    if dry_run:
        for col in PHASE1_COLLECTIONS:
            result["skipped"].append(col["name"])
        return result

    client = ArangoClient(hosts=host)
    db = client.db(db_name, username=username, password=password)

    existing = {c["name"] for c in db.collections()}

    for col_def in PHASE1_COLLECTIONS:
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
    """为event collections创建索引"""
    try:
        # raw_events索引
        if "raw_events" in result["created"] or "raw_events" in result["skipped"]:
            raw = db.collection("raw_events")
            raw.add_persistent_index(fields=["run_id"], name="idx_raw_run_id")
            raw.add_persistent_index(fields=["event_id"], unique=True, name="idx_raw_event_id")
            raw.add_persistent_index(fields=["timestamp"], name="idx_raw_timestamp")

        # semantic_events索引
        if "semantic_events" in result["created"] or "semantic_events" in result["skipped"]:
            sem = db.collection("semantic_events")
            sem.add_persistent_index(fields=["run_id"], name="idx_sem_run_id")
            sem.add_persistent_index(fields=["event_id"], unique=True, name="idx_sem_event_id")
            sem.add_persistent_index(fields=["raw_event_id"], name="idx_sem_raw_ref")
            sem.add_persistent_index(fields=["type"], name="idx_sem_type")
            sem.add_persistent_index(fields=["timestamp"], name="idx_sem_timestamp")

        # checkpoints索引
        if "checkpoints" in result["created"] or "checkpoints" in result["skipped"]:
            chk = db.collection("checkpoints")
            chk.add_persistent_index(fields=["content_hash"], unique=True, name="idx_chk_hash")
            chk.add_persistent_index(fields=["run_id"], name="idx_chk_run_id")

        # run_manifests索引
        if "run_manifests" in result["created"] or "run_manifests" in result["skipped"]:
            man = db.collection("run_manifests")
            man.add_persistent_index(fields=["run_id"], unique=True, name="idx_man_run_id")
    except Exception as e:
        result["failed"].append(f"index_creation: {e}")


def drop_event_collections(
    db_name: str = DB_NAME,
    username: str = DB_USER,
    password: str = DB_PASS,
    host: str = ARANGO_HOST,
) -> dict:
    """
    回滚：删除Phase 1的event collections。
    仅用于migration失败时的回滚，不用于正常操作。
    """
    result = {"dropped": [], "failed": []}

    client = ArangoClient(hosts=host)
    db = client.db(db_name, username=username, password=password)

    for col_def in PHASE1_COLLECTIONS:
        name = col_def["name"]
        try:
            db.delete_collection(name)
            result["dropped"].append(name)
        except Exception as e:
            result["failed"].append(f"{name}: {e}")

    return result
