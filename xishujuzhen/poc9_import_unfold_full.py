#!/usr/bin/env python3
"""将normal AI转译结果（大师提示词）写入ArangoDB的uf_nodes和uf_edges"""
import json
from arango import ArangoClient

client = ArangoClient(hosts="http://localhost:8529")
db = client.db("xishujuzhen", username="root", password="REDACTED-DB-PASSWORD")

# 读取转译输入（包含G'_topo结构+KC）
with open("xishujuzhen/poc/poc9_translate_input.json", encoding="utf-8") as f:
    translate_input = json.load(f)

# 清空旧数据
db.collection("uf_nodes").truncate()
db.collection("uf_edges").truncate()
print("已清空uf_nodes和uf_edges")

# 导入uf_nodes（含文字内容）
node_docs = []
for n in translate_input["nodes"]:
    node_docs.append({
        "node_id": n["node_id"],
        "section": n.get("section", ""),
        "position": n.get("position", 0),
        "traversal_order": n.get("traversal_order", 0),
        "type": n.get("type", ""),
        "text_content": n.get("knowledge_content", "") if n.get("has_kc") else n.get("desc", ""),
        "desc": n.get("desc", ""),
        "context": n.get("context", ""),
        "has_kc": n.get("has_kc", False),
        "kc_fidelity": True,  # 默认标记为忠实，审计时再验证
    })
db.collection("uf_nodes").import_bulk(node_docs)
print(f"✅ 导入uf_nodes: {len(node_docs)}个节点")

# 建立 node_id → _id 映射
node_key_map = {}
for doc in db.collection("uf_nodes").all():
    node_key_map[doc["node_id"]] = doc["_id"]

# 导入uf_edges（含文字内容）
edge_docs = []
for e in translate_input["edges"]:
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
        "text_content": e.get("desc", ""),
    })
db.collection("uf_edges").import_bulk(edge_docs)
print(f"✅ 导入uf_edges: {len(edge_docs)}条边")

# 验证
print(f"\nuf_nodes: {db.collection('uf_nodes').count()}")
print(f"uf_edges: {db.collection('uf_edges').count()}")
