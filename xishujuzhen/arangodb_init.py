#!/usr/bin/env python3
"""xishujuzhen ArangoDB初始化脚本

创建数据库、collections、graphs，对应79号文档中的数据模型设计。
"""
from arango import ArangoClient

# 连接ArangoDB
client = ArangoClient(hosts="http://localhost:8529")
sys_db = client.db("_system", username="root", password="REDACTED-DB-PASSWORD")

# 创建xishujuzhen数据库
DB_NAME = "xishujuzhen_math"
if not sys_db.has_database(DB_NAME):
    sys_db.create_database(DB_NAME)
    print(f"✅ 创建数据库: {DB_NAME}")
else:
    print(f"⚠️  数据库已存在: {DB_NAME}")

db = client.db(DB_NAME, username="root", password="REDACTED-DB-PASSWORD")

# ============================================================
# 1. 文档集合（Collections）
# ============================================================

# --- 依赖图G的节点和边 ---
collections_to_create = [
    # 依赖图G
    ("dg_nodes", False),   # 依赖图节点（文档集合）
    ("dg_edges", True),    # 依赖图边（边集合）

    # 展开图拓扑骨架G'_topo
    ("ut_nodes", False),   # 展开图拓扑节点
    ("ut_edges", True),    # 展开图拓扑边

    # 展开图G'（含文字）
    ("uf_nodes", False),   # 展开图节点（含文字）
    ("uf_edges", True),    # 展开图边（含文字）

    # 文档集合
    ("kcs", False),        # 知识内容库
    ("audits", False),     # 审计报告
    ("analyses", False),   # 分析结果
    ("prompts", False),    # 大师提示词
    ("subjects", False),   # 命主档案
    ("loops", False),      # 螺旋环路定义
]

for name, is_edge in collections_to_create:
    if not db.has_collection(name):
        db.create_collection(name, edge=is_edge)
        kind = "边集合" if is_edge else "文档集合"
        print(f"✅ 创建{kind}: {name}")
    else:
        print(f"⚠️  集合已存在: {name}")

# ============================================================
# 2. 图（Graphs）—— 用于图遍历
# ============================================================

graphs_to_create = [
    {
        "name": "dependency_graph",
        "orphan_collections": ["dg_nodes"],
        "edge_definitions": [
            {
                "edge_collection": "dg_edges",
                "from_vertex_collections": ["dg_nodes"],
                "to_vertex_collections": ["dg_nodes"],
            }
        ],
    },
    {
        "name": "unfold_topo",
        "orphan_collections": ["ut_nodes"],
        "edge_definitions": [
            {
                "edge_collection": "ut_edges",
                "from_vertex_collections": ["ut_nodes"],
                "to_vertex_collections": ["ut_nodes"],
            }
        ],
    },
    {
        "name": "unfold_full",
        "orphan_collections": ["uf_nodes"],
        "edge_definitions": [
            {
                "edge_collection": "uf_edges",
                "from_vertex_collections": ["uf_nodes"],
                "to_vertex_collections": ["uf_nodes"],
            }
        ],
    },
]

for graph_config in graphs_to_create:
    graph_name = graph_config["name"]
    if not db.has_graph(graph_name):
        db.create_graph(
            name=graph_name,
            edge_definitions=graph_config["edge_definitions"],
            orphan_collections=graph_config["orphan_collections"],
        )
        print(f"✅ 创建图: {graph_name}")
    else:
        print(f"⚠️  图已存在: {graph_name}")

# ============================================================
# 3. 索引
# ============================================================

# dg_nodes: 按node_id查询
dg_nodes = db.collection("dg_nodes")
if not any(idx["fields"] == ["node_id"] for idx in dg_nodes.indexes()):
    dg_nodes.add_persistent_index(fields=["node_id"], unique=True)
    print("✅ 创建索引: dg_nodes.node_id (unique)")

# dg_nodes: 按type查询
if not any(idx["fields"] == ["type"] for idx in dg_nodes.indexes()):
    dg_nodes.add_persistent_index(fields=["type"])
    print("✅ 创建索引: dg_nodes.type")

# dg_edges: 按edge_type查询
dg_edges = db.collection("dg_edges")
if not any(idx["fields"] == ["edge_type"] for idx in dg_edges.indexes()):
    dg_edges.add_persistent_index(fields=["edge_type"])
    print("✅ 创建索引: dg_edges.edge_type")

# ut_nodes: 按node_id查询
ut_nodes = db.collection("ut_nodes")
if not any(idx["fields"] == ["node_id"] for idx in ut_nodes.indexes()):
    ut_nodes.add_persistent_index(fields=["node_id"], unique=True)
    print("✅ 创建索引: ut_nodes.node_id (unique)")

# uf_nodes: 按node_id查询
uf_nodes = db.collection("uf_nodes")
if not any(idx["fields"] == ["node_id"] for idx in uf_nodes.indexes()):
    uf_nodes.add_persistent_index(fields=["node_id"], unique=True)
    print("✅ 创建索引: uf_nodes.node_id (unique)")

# kcs: 按node_id查询
kcs = db.collection("kcs")
if not any(idx["fields"] == ["node_id"] for idx in kcs.indexes()):
    kcs.add_persistent_index(fields=["node_id"])
    print("✅ 创建索引: kcs.node_id")

# audits: 按poc_id查询
audits = db.collection("audits")
if not any(idx["fields"] == ["poc_id"] for idx in audits.indexes()):
    audits.add_persistent_index(fields=["poc_id"])
    print("✅ 创建索引: audits.poc_id")

# analyses: 按poc_id查询
analyses = db.collection("analyses")
if not any(idx["fields"] == ["poc_id"] for idx in analyses.indexes()):
    analyses.add_persistent_index(fields=["poc_id"])
    print("✅ 创建索引: analyses.poc_id")

# ============================================================
# 4. 验证
# ============================================================

print("\n" + "=" * 60)
print("ArangoDB xishujuzhen 初始化完成")
print("=" * 60)

print(f"\n数据库: {DB_NAME}")
print(f"ArangoDB版本: {db.version()}")
print(f"\n集合列表:")
for col_info in db.collections():
    if not col_info["name"].startswith("_"):
        print(f"  - {col_info['name']} ({'edge' if col_info['type'] == 'edge' else 'document'})")

print(f"\n图列表:")
for graph_info in db.graphs():
    print(f"  - {graph_info['name']}")

print(f"\n索引列表:")
for col_info in db.collections():
    if not col_info["name"].startswith("_"):
        col = db.collection(col_info["name"])
        for idx in col.indexes():
            if idx["type"] != "primary":
                print(f"  - {col_info['name']}.{idx['fields']} ({idx['type']})")
