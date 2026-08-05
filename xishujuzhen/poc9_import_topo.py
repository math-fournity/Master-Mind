#!/usr/bin/env python3
"""将G'_topo写入ArangoDB的ut_nodes和ut_edges集合"""
import json
from arango import ArangoClient

client = ArangoClient(hosts="http://localhost:8529")
db = client.db("xishujuzhen_math", username="root", password="REDACTED-DB-PASSWORD")

with open("xishujuzhen/poc/poc2/poc2_g_prime_topo.json", encoding="utf-8") as f:
    topo = json.load(f)

# 清空旧数据
db.collection("ut_nodes").truncate()
db.collection("ut_edges").truncate()
print("已清空ut_nodes和ut_edges")

# 导入节点
node_docs = []
for n in topo["nodes"]:
    node_docs.append({
        "node_id": n["node_id"],
        "section": n.get("section", ""),
        "position": n.get("position", 0),
        "type": n.get("type", ""),
        "traversal_order": n.get("traversal_order", 0),
    })
db.collection("ut_nodes").import_bulk(node_docs)
print(f"✅ 导入ut_nodes: {len(node_docs)}个节点")

# 建立 node_id → _id 映射
node_key_map = {}
for doc in db.collection("ut_nodes").all():
    node_key_map[doc["node_id"]] = doc["_id"]

# 导入边
edge_docs = []
for e in topo["edges"]:
    from_id = e["from_node_id"]
    to_id = e["to_node_id"]
    from_arango = node_key_map.get(from_id)
    to_arango = node_key_map.get(to_id)
    if not from_arango or not to_arango:
        print(f"⚠️  边节点缺失: {from_id}→{to_id}")
        continue
    edge_docs.append({
        "_from": from_arango,
        "_to": to_arango,
        "from_node_id": from_id,
        "to_node_id": to_id,
        "edge_type": e.get("edge_type", ""),
        "section": e.get("section", ""),
        "connection": e.get("connection", ""),
    })
db.collection("ut_edges").import_bulk(edge_docs)
print(f"✅ 导入ut_edges: {len(edge_docs)}条边")

# 更新loops（unfold_topo版本）
# 先删除旧的unfold_topo loops
db.collection("loops").delete_many({"graph": "unfold_topo"})
print("已清空unfold_topo的loops")

loop_docs = []
for l in topo["loops"]:
    loop_docs.append({
        "loop_id": l["loop_id"],
        "graph": "unfold_topo",
        "nodes": l.get("nodes", []),
        "circles": l.get("circles", 1),
        "type": l.get("type", "spiral"),
        "section": l.get("section", ""),
        "traversal": l.get("traversal", ""),
    })
if loop_docs:
    db.collection("loops").import_bulk(loop_docs)
    print(f"✅ 导入loops(unfold_topo): {len(loop_docs)}个螺旋环路")

# 验证
print(f"\nut_nodes: {db.collection('ut_nodes').count()}")
print(f"ut_edges: {db.collection('ut_edges').count()}")
print(f"loops(unfold_topo): {len(list(db.collection('loops').find({'graph': 'unfold_topo'})))}")
