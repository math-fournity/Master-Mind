"""
ArangoDB migration: 创建Phase 3的heuristics collections

对应133号P3-CODE-1。

遵循123号§55数据迁移原则：
- 新collection用幂等、可回滚migration创建
- 不动旧数据（NO-10约束）
- 生产图、候选图、实验快照分开

新增collections：
- heuristic_rules: HeuristicRule文档存储
- activation_packets: 激活包文档存储
"""

import os
from arango import ArangoClient
from arango.exceptions import CollectionCreateError

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
DB_USER = os.environ.get("ARANGO_USER", "root")
DB_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")

# Phase 3需要创建的collections
PHASE3_COLLECTIONS = [
    # P3-7/P3-8: 启发规则
    {"name": "heuristic_rules", "type": "document"},
    # P3-4: 激活包
    {"name": "activation_packets", "type": "document"},
]


def create_phase3_collections(
    db_name: str = DB_NAME,
    username: str = DB_USER,
    password: str = DB_PASS,
    host: str = ARANGO_HOST,
    dry_run: bool = False,
) -> dict:
    """
    幂等创建Phase 3的heuristics collections。
    已存在的collection跳过，不报错。

    返回：{"created": [...], "skipped": [...], "failed": [...]}
    """
    result = {"created": [], "skipped": [], "failed": []}

    if dry_run:
        for col in PHASE3_COLLECTIONS:
            result["skipped"].append(col["name"])
        return result

    client = ArangoClient(hosts=host)
    db = client.db(db_name, username=username, password=password)

    existing = {c["name"] for c in db.collections()}

    for col_def in PHASE3_COLLECTIONS:
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
    """为Phase 3 collections创建索引"""
    created_or_skipped = set(result["created"]) | set(result["skipped"])

    try:
        # heuristic_rules索引
        if "heuristic_rules" in created_or_skipped:
            hr = db.collection("heuristic_rules")
            hr.add_persistent_index(fields=["rule_id"], unique=True, name="idx_hr_id")
            hr.add_persistent_index(fields=["status"], name="idx_hr_status")
            hr.add_persistent_index(fields=["applicable_domains"], name="idx_hr_domains")

        # activation_packets索引
        if "activation_packets" in created_or_skipped:
            ap = db.collection("activation_packets")
            ap.add_persistent_index(fields=["packet_id"], unique=True, name="idx_ap_id")
            ap.add_persistent_index(fields=["rule_id"], name="idx_ap_rule")

    except Exception as e:
        result["failed"].append(f"index_creation: {e}")


def drop_phase3_collections(
    db_name: str = DB_NAME,
    username: str = DB_USER,
    password: str = DB_PASS,
    host: str = ARANGO_HOST,
) -> dict:
    """
    回滚：删除Phase 3的heuristics collections。
    仅用于migration失败时的回滚，不用于正常操作。
    """
    result = {"dropped": [], "failed": []}

    client = ArangoClient(hosts=host)
    db = client.db(db_name, username=username, password=password)

    for col_def in PHASE3_COLLECTIONS:
        name = col_def["name"]
        try:
            db.delete_collection(name)
            result["dropped"].append(name)
        except Exception as e:
            result["failed"].append(f"{name}: {e}")

    return result
