#!/usr/bin/env python3
"""cognition系统 ArangoDB初始化 —— 在xishujuzhen_math中创建5个新collections

对应91号方案第三节。不破坏已有的dg_nodes/dg_edges/loops/kcs/ut_nodes/ut_edges/uf_nodes/uf_edges。
"""
from arango import ArangoClient

client = ArangoClient(hosts="http://localhost:8529")
sys_db = client.db("_system", username="root", password="REDACTED-DB-PASSWORD")

DB_NAME = "xishujuzhen_math"
if not sys_db.has_database(DB_NAME):
    sys_db.create_database(DB_NAME)
    print(f"✅ 创建数据库: {DB_NAME}")
else:
    print(f"⚠️  数据库已存在: {DB_NAME}")

db = client.db(DB_NAME, username="root", password="REDACTED-DB-PASSWORD")

# ============================================================
# 1. 认知图collections
# ============================================================
cognition_collections = [
    ("cognition_units", False),   # 认知单元（节点）
    ("cog_versions", False),      # 版本记录
    ("cognition_tasks", False),   # 任务记录
    ("cog_edges", True),          # 认知单元间的依赖边（边集合）
    ("cog_version_edges", True),  # 版本链边（边集合）
]

for name, is_edge in cognition_collections:
    if not db.has_collection(name):
        db.create_collection(name, edge=is_edge)
        kind = "边集合" if is_edge else "文档集合"
        print(f"✅ 创建{kind}: {name}")
    else:
        print(f"⚠️  集合已存在: {name}")

# ============================================================
# 2. 认知图（Graph）
# ============================================================
if not db.has_graph("cognition_graph"):
    db.create_graph(
        name="cognition_graph",
        edge_definitions=[
            {
                "edge_collection": "cog_edges",
                "from_vertex_collections": ["cognition_units"],
                "to_vertex_collections": ["cognition_units"],
            }
        ],
        orphan_collections=["cognition_units"],
    )
    print("✅ 创建图: cognition_graph")
else:
    print("⚠️  图已存在: cognition_graph")

# ============================================================
# 3. 索引
# ============================================================
def add_index_if_missing(col, fields, unique=False, idx_type="persistent"):
    if not any(idx["fields"] == fields for idx in col.indexes()):
        if idx_type == "persistent":
            col.add_persistent_index(fields=fields, unique=unique)
        print(f"✅ 创建索引: {col.name}.{fields} (unique={unique})")

cu = db.collection("cognition_units")
add_index_if_missing(cu, ["cog_id"], unique=True)
add_index_if_missing(cu, ["category"])
add_index_if_missing(cu, ["status"])

ce = db.collection("cog_edges")
add_index_if_missing(ce, ["edge_type"])

cv = db.collection("cog_versions")
add_index_if_missing(cv, ["cog_id"])
add_index_if_missing(cv, ["version_order"])

ct = db.collection("cognition_tasks")
add_index_if_missing(ct, ["task_description"])

# ============================================================
# 4. 验证
# ============================================================
print("\n" + "=" * 60)
print("cognition系统 ArangoDB初始化完成")
print("=" * 60)
print(f"\n数据库: {DB_NAME}")
print(f"\n全部集合:")
for col_info in db.collections():
    if not col_info["name"].startswith("_"):
        col = db.collection(col_info["name"])
        print(f"  - {col_info['name']} ({'edge' if col_info['type'] == 'edge' else 'document'}): {col.count()}条")

print(f"\n图列表:")
for graph_info in db.graphs():
    print(f"  - {graph_info['name']}")
