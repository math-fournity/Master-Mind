#!/usr/bin/env python3
"""导入数学依赖图到 ArangoDB (xishujuzhen_math 数据库)"""
import os
import json
from arango import ArangoClient

# 连接
client = ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
db = client.db(os.environ.get("ARANGO_DB", "xishujuzhen_math"), username=os.environ.get("ARANGO_USER", "root"), password=os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD"))

# 读取依赖图 JSON
with open("/data/master-mind/xishujuzhen/poc/poc2/math_dependency_graph.json") as f:
    graph_data = json.load(f)

# 清空已有数据（如果重新导入）
for col_name in ["dg_nodes", "dg_edges", "kcs", "loops"]:
    col = db.collection(col_name)
    for doc in col.all():
        col.delete(doc["_id"])

# 导入节点到 dg_nodes
dg_nodes = db.collection("dg_nodes")
node_key_map = {}  # node_id -> _id
for node in graph_data["nodes"]:
    doc = {
        "node_id": node["node_id"],
        "type": node["type"],
        "context": node["context"],
        "kc": node.get("kc", ""),
    }
    result = dg_nodes.insert(doc)
    node_key_map[node["node_id"]] = result["_id"]

print(f"✅ 导入 {len(graph_data['nodes'])} 个节点到 dg_nodes")

# 导入边到 dg_edges
dg_edges = db.collection("dg_edges")
for edge in graph_data["edges"]:
    doc = {
        "_from": node_key_map[edge["from_node_id"]],
        "_to": node_key_map[edge["to_node_id"]],
        "from_node_id": edge["from_node_id"],
        "to_node_id": edge["to_node_id"],
        "edge_type": edge["edge_type"],
    }
    dg_edges.insert(doc)

print(f"✅ 导入 {len(graph_data['edges'])} 条边到 dg_edges")

# 导入 KC 到 kcs
kcs = db.collection("kcs")
for node in graph_data["nodes"]:
    if node.get("kc"):
        doc = {
            "node_id": node["node_id"],
            "knowledge_content": node["kc"],
        }
        kcs.insert(doc)

print(f"✅ 导入 {len([n for n in graph_data['nodes'] if n.get('kc')])} 个 KC 到 kcs")

# 导入螺旋环路到 loops
loops_col = db.collection("loops")
for loop in graph_data["loops"]:
    doc = {
        "loop_id": loop["loop_id"],
        "nodes": loop["nodes"],
        "circles": loop["circles"],
        "traversal": loop["traversal"],
        "contexts": loop.get("contexts", []),
        "graph": "dependency_graph",
    }
    loops_col.insert(doc)

print(f"✅ 导入 {len(graph_data['loops'])} 个螺旋环路到 loops")

# 验证
print("\n" + "=" * 60)
print("导入验证")
print("=" * 60)
print(f"dg_nodes: {dg_nodes.count()} 个")
print(f"dg_edges: {dg_edges.count()} 条")
print(f"kcs: {kcs.count()} 个")
print(f"loops: {loops_col.count()} 个")

# 按类型统计节点
aql = """
FOR n IN dg_nodes
  COLLECT type = n.type WITH COUNT INTO count
  RETURN {type, count}
"""
for r in db.aql.execute(aql):
    print(f"  节点类型 {r['type']}: {r['count']} 个")

# 按类型统计边
aql = """
FOR e IN dg_edges
  COLLECT type = e.edge_type WITH COUNT INTO count
  RETURN {type, count}
"""
for r in db.aql.execute(aql):
    print(f"  边类型 {r['type']}: {r['count']} 条")
