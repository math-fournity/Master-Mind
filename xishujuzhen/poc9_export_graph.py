#!/usr/bin/env python3
"""从ArangoDB导出dependency_graph为JSON，作为meta AI拓扑规划的输入"""
import os
import json
from arango import ArangoClient

client = ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
db = client.db(os.environ.get("ARANGO_DB", "xishujuzhen"), username="root", password="REDACTED-DB-PASSWORD")

# 导出节点
nodes = []
for doc in db.collection("dg_nodes").all():
    nodes.append({
        "id": doc["node_id"],
        "type": doc["type"],
        "context": doc.get("context", ""),
        "desc": doc.get("desc", ""),
        "section": doc.get("section", ""),
        "has_kc": doc.get("has_kc", False),
    })

# 导出边
edges = []
for doc in db.collection("dg_edges").all():
    edges.append({
        "from": doc["from_node_id"],
        "to": doc["to_node_id"],
        "type": doc["edge_type"],
        "desc": doc.get("desc", ""),
        "cross_palace": doc.get("cross_palace", False),
    })

# 导出螺旋环路
loops = []
for doc in db.collection("loops").find({"graph": "dependency_graph"}):
    loops.append({
        "id": doc["loop_id"],
        "nodes": doc.get("nodes", []),
        "circles": doc.get("circles", 1),
        "type": doc.get("type", "spiral"),
        "contexts": doc.get("contexts", []),
        "desc": doc.get("desc", ""),
    })

# 导出KC
kcs = []
for doc in db.collection("kcs").all():
    kcs.append({
        "node_id": doc["node_id"],
        "knowledge_content": doc["knowledge_content"],
    })

graph_data = {
    "graph_name": "dependency_graph",
    "stats": {
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "cross_palace_edges": sum(1 for e in edges if e["cross_palace"]),
        "knowledge_content_nodes": len(kcs),
        "loops": len(loops),
    },
    "nodes": nodes,
    "edges": edges,
    "loops": loops,
    "kcs": kcs,
}

output_path = "xishujuzhen/poc/poc9_dependency_graph_export.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(graph_data, f, ensure_ascii=False, indent=2)

print(f"✅ 导出dependency_graph到 {output_path}")
print(f"   节点: {len(nodes)}")
print(f"   边: {len(edges)}")
print(f"   跨宫边: {sum(1 for e in edges if e['cross_palace'])}")
print(f"   KC: {len(kcs)}")
print(f"   螺旋环路: {len(loops)}")
