#!/usr/bin/env python3
"""cognition_import_math.py —— 导入认知单元到ArangoDB

读取 xishujuzhen/poc/cognition_units_math.json，导入到 xishujuzhen_math 数据库的
cognition_units / cog_edges / cog_versions 集合。
"""
import json
import os
import sys
from datetime import datetime

from arango import ArangoClient

DB_NAME = "xishujuzhen_math"
JSON_PATH = os.path.join(os.path.dirname(__file__), "poc", "cognition_units_math.json")


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    client = ArangoClient(hosts="http://localhost:8529")
    db = client.db(DB_NAME, username="root", password="REDACTED-DB-PASSWORD")

    units_col = db.collection("cognition_units")
    edges_col = db.collection("cog_edges")
    versions_col = db.collection("cog_versions")

    # 清空已有数据（幂等导入）
    for col in [units_col, edges_col, versions_col]:
        col.truncate()
        print(f"  清空 {col.name}")

    now = datetime.utcnow().isoformat() + "Z"

    # 导入认知单元
    unit_key_map = {}  # cog_id -> _id
    for u in data["units"]:
        doc = {
            "_key": u["cog_id"],
            "cog_id": u["cog_id"],
            "title": u["title"],
            "category": u["category"],
            "status": u.get("status", "active"),
            "key_cognition": u["key_cognition"],
            "source_docs": u.get("source_docs", []),
            "current_version": u.get("current_version", "v1"),
            "created_at": now,
        }
        result = units_col.insert(doc, overwrite=True)
        unit_key_map[u["cog_id"]] = result["_id"]
    print(f"✅ 导入 {len(data['units'])} 个认知单元")

    # 导入依赖边
    edge_count = 0
    for e in data["edges"]:
        from_id = unit_key_map.get(e["from"])
        to_id = unit_key_map.get(e["to"])
        if not from_id or not to_id:
            print(f"  ⚠️  跳过边（找不到端点）: {e}")
            continue
        doc = {
            "_from": from_id,
            "_to": to_id,
            "from_cog_id": e["from"],
            "to_cog_id": e["to"],
            "edge_type": e["type"],
            "created_at": now,
        }
        edges_col.insert(doc)
        edge_count += 1
    print(f"✅ 导入 {edge_count} 条依赖边")

    # 导入版本记录
    version_count = 0
    for v in data.get("versions", []):
        doc = {
            "cog_id": v["cog_id"],
            "version": v["version"],
            "version_order": v.get("version_order"),
            "doc": str(v["doc"]),
            "summary": v.get("summary", ""),
            "created_at": now,
        }
        versions_col.insert(doc)
        version_count += 1

    # 为没有显式版本记录的认知单元补充v1
    for u in data["units"]:
        cog_id = u["cog_id"]
        existing = list(versions_col.find({"cog_id": cog_id}))
        if not existing:
            versions_col.insert({
                "cog_id": cog_id,
                "version": "v1",
                "version_order": 1,
                "doc": str(u["source_docs"][0]) if u.get("source_docs") else "",
                "summary": "初始版本",
                "created_at": now,
            })
            version_count += 1
    print(f"✅ 导入 {version_count} 条版本记录")

    # 验证
    print("\n" + "=" * 60)
    print("导入验证")
    print("=" * 60)
    from collections import Counter
    units = list(units_col.all())
    cats = Counter(u.get("category", "?") for u in units)
    print(f"认知单元: {len(units)}个")
    print(f"  分类: {dict(cats)}")
    print(f"边: {edges_col.count()}条")
    print(f"版本: {versions_col.count()}条")


if __name__ == "__main__":
    main()
