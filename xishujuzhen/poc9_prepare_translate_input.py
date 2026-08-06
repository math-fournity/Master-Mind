#!/usr/bin/env python3
"""为步骤4（normal AI转译）准备输入文件：G'_topo + KC + 依赖图desc"""
import os
import json
from arango import ArangoClient

client = ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
db = client.db(os.environ.get("ARANGO_DB", "xishujuzhen"), username=os.environ.get("ARANGO_USER", "root"), password=os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD"))

# 读取G'_topo
with open("xishujuzhen/poc/poc9_g_prime_topo.json", encoding="utf-8") as f:
    topo = json.load(f)

# 读取KC
kc_map = {}
for doc in db.collection("kcs").all():
    kc_map[doc["node_id"]] = doc["knowledge_content"]

# 读取dg_nodes的desc
desc_map = {}
for doc in db.collection("dg_nodes").all():
    desc_map[doc["node_id"]] = {
        "desc": doc.get("desc", ""),
        "context": doc.get("context", ""),
        "type": doc.get("type", ""),
    }

# 读取dg_edges的desc
edge_desc_map = {}
for doc in db.collection("dg_edges").all():
    key = f"{doc['from_node_id']}→{doc['to_node_id']}"
    edge_desc_map[key] = doc.get("desc", "")

# 合并成转译输入
translate_input = {
    "graph_name": "unfold_full",
    "source_topo": "unfold_topo",
    "stats": topo["stats"],
    "nodes": [],
    "edges": [],
    "loops": topo["loops"],
}

for n in topo["nodes"]:
    nid = n["node_id"]
    node_info = {
        "node_id": nid,
        "section": n.get("section", ""),
        "position": n.get("position", 0),
        "type": n.get("type", ""),
        "traversal_order": n.get("traversal_order", 0),
        "desc": desc_map.get(nid, {}).get("desc", ""),
        "context": desc_map.get(nid, {}).get("context", ""),
        "knowledge_content": kc_map.get(nid, ""),
        "has_kc": nid in kc_map,
    }
    translate_input["nodes"].append(node_info)

for e in topo["edges"]:
    key = f"{e['from_node_id']}→{e['to_node_id']}"
    edge_info = {
        "from_node_id": e["from_node_id"],
        "to_node_id": e["to_node_id"],
        "edge_type": e.get("edge_type", ""),
        "section": e.get("section", ""),
        "connection": e.get("connection", ""),
        "desc": edge_desc_map.get(key, ""),
    }
    translate_input["edges"].append(edge_info)

output_path = "xishujuzhen/poc/poc9_translate_input.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(translate_input, f, ensure_ascii=False, indent=2)

print(f"✅ 生成转译输入文件: {output_path}")
print(f"   节点: {len(translate_input['nodes'])} (其中{sum(1 for n in translate_input['nodes'] if n['has_kc'])}个有KC)")
print(f"   边: {len(translate_input['edges'])}")
print(f"   螺旋环路: {len(translate_input['loops'])}")
