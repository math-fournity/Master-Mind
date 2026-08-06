#!/usr/bin/env python3
"""cognition_export_math.py —— ArangoDB→JSON双向同步

[P0-8.2] 从ArangoDB导出认知单元到 cognition_units_math.json。
定期把ArangoDB当前状态回写到JSON文件，防止"ArangoDB有但JSON没有"的数据丢失。

使用方式：
  .venv/bin/python3 xishujuzhen/cognition_export_math.py           # 导出并覆盖JSON
  .venv/bin/python3 xishujuzhen/cognition_export_math.py --dry-run  # 只显示差异，不写文件
  .venv/bin/python3 xishujuzhen/cognition_export_math.py --diff     # 显示ArangoDB与JSON的差异
"""
import argparse
import json
import os
import sys
from datetime import datetime

from arango import ArangoClient

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
JSON_PATH = os.path.join(os.path.dirname(__file__), "poc", "cognition_units_math.json")


def export_from_arango():
    """从ArangoDB导出全部认知单元、边和版本"""
    client = ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
    db = client.db(DB_NAME, username="root", password="REDACTED-DB-PASSWORD")

    units = list(db.collection("cognition_units").all())
    edges = list(db.collection("cog_edges").all())
    versions = list(db.collection("cog_versions").all())

    # 转换为JSON格式
    json_units = []
    for u in sorted(units, key=lambda x: x.get("cog_id", "")):
        json_units.append({
            "cog_id": u.get("cog_id", ""),
            "title": u.get("title", ""),
            "category": u.get("category", ""),
            "status": u.get("status", "active"),
            "key_cognition": u.get("key_cognition", ""),
            "source_docs": u.get("source_docs", []),
            "current_version": u.get("current_version", "v1"),
        })

    json_edges = []
    for e in sorted(edges, key=lambda x: (x.get("from_cog_id", ""), x.get("to_cog_id", ""))):
        json_edges.append({
            "from": e.get("from_cog_id", ""),
            "to": e.get("to_cog_id", ""),
            "type": e.get("edge_type", "depends_on"),
        })

    json_versions = []
    for v in sorted(versions, key=lambda x: (x.get("cog_id", ""), x.get("version_order", 0))):
        json_versions.append({
            "cog_id": v.get("cog_id", ""),
            "version": v.get("version", ""),
            "version_order": v.get("version_order"),
            "doc": v.get("doc", ""),
            "summary": v.get("summary", ""),
        })

    return {"units": json_units, "edges": json_edges, "versions": json_versions}


def diff_json_arango(json_data, arango_data):
    """比较JSON和ArangoDB数据的差异"""
    json_cog_ids = set(u["cog_id"] for u in json_data["units"])
    arango_cog_ids = set(u["cog_id"] for u in arango_data["units"])

    only_json = json_cog_ids - arango_cog_ids
    only_arango = arango_cog_ids - json_cog_ids
    common = json_cog_ids & arango_cog_ids

    # 检查共同单元的字段差异
    json_map = {u["cog_id"]: u for u in json_data["units"]}
    arango_map = {u["cog_id"]: u for u in arango_data["units"]}
    field_diffs = []
    for cog_id in sorted(common):
        j = json_map[cog_id]
        a = arango_map[cog_id]
        for field in ["title", "status", "key_cognition", "current_version"]:
            if j.get(field, "") != a.get(field, ""):
                field_diffs.append({
                    "cog_id": cog_id,
                    "field": field,
                    "json": j.get(field, "")[:60],
                    "arango": a.get(field, "")[:60],
                })

    return {
        "only_in_json": only_json,
        "only_in_arango": only_arango,
        "field_diffs": field_diffs,
        "json_count": len(json_cog_ids),
        "arango_count": len(arango_cog_ids),
    }


def main():
    parser = argparse.ArgumentParser(description="ArangoDB→JSON导出")
    parser.add_argument("--dry-run", action="store_true", help="只显示差异，不写文件")
    parser.add_argument("--diff", action="store_true", help="显示ArangoDB与JSON的差异")
    args = parser.parse_args()

    # 读取现有JSON
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # 从ArangoDB导出
    arango_data = export_from_arango()

    # 显示差异
    d = diff_json_arango(json_data, arango_data)
    print(f"JSON: {d['json_count']}个单元, ArangoDB: {d['arango_count']}个单元")
    if d["only_in_json"]:
        print(f"  仅JSON有({len(d['only_in_json'])}): {d['only_in_json']}")
    if d["only_in_arango"]:
        print(f"  仅ArangoDB有({len(d['only_in_arango'])}): {d['only_in_arango']}")
    if d["field_diffs"]:
        print(f"  字段差异({len(d['field_diffs'])}):")
        for fd in d["field_diffs"]:
            print(f"    {fd['cog_id']}.{fd['field']}: JSON='{fd['json']}' vs ArangoDB='{fd['arango']}'")

    if args.diff or args.dry_run:
        return

    # 写入JSON
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(arango_data, f, ensure_ascii=False, indent=2)
    print(f"✅ 已导出 {len(arango_data['units'])} 个单元到 {JSON_PATH}")


if __name__ == "__main__":
    main()
