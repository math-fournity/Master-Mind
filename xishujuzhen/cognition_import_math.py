#!/usr/bin/env python3
"""cognition_import_math.py —— 导入认知单元到ArangoDB（merge/upsert模式）

[P0-8.1] 改为merge/upsert模式，不truncate。
读取 xishujuzhen/poc/cognition_units_math.json，upsert到 xishujuzhen_math 数据库的
cognition_units / cog_edges / cog_versions 集合。
ArangoDB中有但JSON没有的记录保留不动，标记为orphan待人工确认。
"""
import json
import os
import sys
from datetime import datetime

from arango import ArangoClient

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
JSON_PATH = os.path.join(os.path.dirname(__file__), "poc", "cognition_units_math.json")


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    client = ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
    db = client.db(DB_NAME, username=os.environ.get("ARANGO_USER", "root"), password=os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD"))

    units_col = db.collection("cognition_units")
    edges_col = db.collection("cog_edges")
    versions_col = db.collection("cog_versions")

    # [P0-8.1] 不再truncate，使用merge/upsert模式
    # 记录导入前的ArangoDB状态
    before_units = set(u["_key"] for u in units_col.all())
    before_edges = edges_col.count()
    before_versions = versions_col.count()
    print(f"导入前: {len(before_units)}个单元, {before_edges}条边, {before_versions}条版本")

    now = datetime.utcnow().isoformat() + "Z"

    # upsert认知单元（overwrite=True实现upsert）
    unit_key_map = {}  # cog_id -> _id
    imported_cog_ids = set()
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
        imported_cog_ids.add(u["cog_id"])
    print(f"✅ upsert {len(data['units'])} 个认知单元")

    # 检测orphan（ArangoDB有但JSON没有的单元）
    after_units = set(u["_key"] for u in units_col.all())
    orphans = after_units - imported_cog_ids
    if orphans:
        print(f"  ⚠️  {len(orphans)}个orphan单元（ArangoDB有但JSON没有，保留不动）: {orphans}")

    # upsert依赖边（用确定性_key实现upsert）
    edge_count = 0
    for e in data["edges"]:
        from_id = unit_key_map.get(e["from"])
        to_id = unit_key_map.get(e["to"])
        if not from_id or not to_id:
            print(f"  ⚠️  跳过边（找不到端点）: {e}")
            continue
        edge_key = f"{e['from']}__{e['to']}__{e['type']}"
        doc = {
            "_key": edge_key,
            "_from": from_id,
            "_to": to_id,
            "from_cog_id": e["from"],
            "to_cog_id": e["to"],
            "edge_type": e["type"],
            "created_at": now,
        }
        edges_col.insert(doc, overwrite=True)
        edge_count += 1
    print(f"✅ upsert {edge_count} 条依赖边")

    # upsert版本记录（用cog_id+version作为确定性key）
    version_count = 0
    for v in data.get("versions", []):
        ver_key = f"{v['cog_id']}__{v['version']}"
        doc = {
            "_key": ver_key,
            "cog_id": v["cog_id"],
            "version": v["version"],
            "version_order": v.get("version_order"),
            "doc": str(v["doc"]),
            "summary": v.get("summary", ""),
            "created_at": now,
        }
        versions_col.insert(doc, overwrite=True)
        version_count += 1

    # 为没有显式版本记录的认知单元补充v1
    for u in data["units"]:
        cog_id = u["cog_id"]
        existing = list(versions_col.find({"cog_id": cog_id}))
        if not existing:
            ver_key = f"{cog_id}__v1"
            versions_col.insert({
                "_key": ver_key,
                "cog_id": cog_id,
                "version": "v1",
                "version_order": 1,
                "doc": str(u["source_docs"][0]) if u.get("source_docs") else "",
                "summary": "初始版本",
                "created_at": now,
            }, overwrite=True)
            version_count += 1
    print(f"✅ upsert {version_count} 条版本记录")

    # 验证
    print("\n" + "=" * 60)
    print("导入验证（merge模式，不truncate）")
    print("=" * 60)
    from collections import Counter
    units = list(units_col.all())
    cats = Counter(u.get("category", "?") for u in units)
    print(f"认知单元: {len(units)}个 (导入{len(imported_cog_ids)}, orphan{len(orphans)})")
    print(f"  分类: {dict(cats)}")
    print(f"边: {edges_col.count()}条")
    print(f"版本: {versions_col.count()}条")


if __name__ == "__main__":
    main()
