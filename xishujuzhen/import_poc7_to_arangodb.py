#!/usr/bin/env python3
"""将POC-7的JSON依赖图导入ArangoDB

把poc7_prompt_b.json中的71节点106边2螺旋环路导入ArangoDB的dependency_graph。
同时把含knowledge_content的节点导入kcs集合。
"""
import json
from arango import ArangoClient

# 连接
client = ArangoClient(hosts="http://localhost:8529")
db = client.db("xishujuzhen", username="root", password="REDACTED-DB-PASSWORD")

# 读取JSON
with open("xishujuzhen/poc/poc7_prompt_b.json") as f:
    data = json.load(f)

dg = data["dependency_graph"]
nodes = dg["nodes"]
edges = dg["edges"]
cycles = data.get("cycles", [])
stats = dg.get("stats", {})

print(f"JSON依赖图: {len(nodes)}节点, {len(edges)}边, {len(cycles)}螺旋环路")
print(f"stats: {stats}")

# ============================================================
# 1. 导入节点到dg_nodes
# ============================================================

# 先清空（如果之前有数据）
db.collection("dg_nodes").truncate()
db.collection("dg_edges").truncate()
db.collection("kcs").truncate()
db.collection("loops").truncate()
print("\n已清空旧数据")

# 导入节点
node_docs = []
kc_docs = []
for node in nodes:
    node_id = node["id"]
    doc = {
        "node_id": node_id,
        "type": node.get("type", "step"),
        "context": node.get("context", ""),
        "desc": node.get("desc", ""),
        "section": node.get("section", ""),
        "knowledge_content": node.get("knowledge_content", ""),
        "has_kc": "knowledge_content" in node and node["knowledge_content"],
    }
    node_docs.append(doc)

    # 如果有knowledge_content，同时导入kcs集合
    if doc["has_kc"]:
        kc_docs.append({
            "node_id": node_id,
            "knowledge_content": doc["knowledge_content"],
            "source": "poc7",
            "version": 1,
        })

# 批量插入节点
result = db.collection("dg_nodes").import_bulk(node_docs)
print(f"✅ 导入dg_nodes: {len(node_docs)}个节点")

# 批量插入KC
if kc_docs:
    result = db.collection("kcs").import_bulk(kc_docs)
    print(f"✅ 导入kcs: {len(kc_docs)}个知识内容")

# ============================================================
# 2. 导入边到dg_edges
# ============================================================

# 需要把node_id映射到ArangoDB的_id
# ArangoDB会自动生成_id，格式为 dg_nodes/<_key>
# 我们需要先查询所有节点的_key

node_key_map = {}
for doc in db.collection("dg_nodes").all():
    node_key_map[doc["node_id"]] = doc["_id"]

edge_docs = []
cross_palace_count = 0
for edge in edges:
    from_id = edge["from"]
    to_id = edge["to"]
    edge_type = edge.get("type", "depends_on")

    if edge.get("cross_palace"):
        cross_palace_count += 1

    from_arango_id = node_key_map.get(from_id)
    to_arango_id = node_key_map.get(to_id)

    if not from_arango_id or not to_arango_id:
        print(f"⚠️  边的节点不存在: {from_id}→{to_id}")
        continue

    edge_doc = {
        "_from": from_arango_id,
        "_to": to_arango_id,
        "edge_type": edge_type,
        "from_node_id": from_id,
        "to_node_id": to_id,
        "desc": edge.get("desc", ""),
        "reason": edge.get("reason", ""),
        "cross_palace": edge.get("cross_palace", False),
    }
    if edge.get("cross_palace"):
        edge_doc["edge_type"] = "cross_palace"
    edge_docs.append(edge_doc)

result = db.collection("dg_edges").import_bulk(edge_docs)
print(f"✅ 导入dg_edges: {len(edge_docs)}条边 (其中跨宫边{cross_palace_count}条)")

# ============================================================
# 3. 导入螺旋环路到loops
# ============================================================

loop_docs = []
for i, cycle in enumerate(cycles):
    loop_doc = {
        "loop_id": cycle.get("id", f"loop_{i}"),
        "graph": "dependency_graph",
        "nodes": cycle.get("nodes", []),
        "circles": cycle.get("circles", cycle.get("iterations", 1)),
        "type": cycle.get("type", "spiral"),
        "contexts": cycle.get("contexts", []),
        "desc": cycle.get("desc", ""),
    }
    loop_docs.append(loop_doc)

if loop_docs:
    result = db.collection("loops").import_bulk(loop_docs)
    print(f"✅ 导入loops: {len(loop_docs)}个螺旋环路")

# ============================================================
# 4. 验证
# ============================================================

print("\n" + "=" * 60)
print("导入验证")
print("=" * 60)

dg_nodes_count = db.collection("dg_nodes").count()
dg_edges_count = db.collection("dg_edges").count()
kcs_count = db.collection("kcs").count()
loops_count = db.collection("loops").count()

print(f"dg_nodes: {dg_nodes_count} (期望71)")
print(f"dg_edges: {dg_edges_count} (期望106)")
print(f"kcs: {kcs_count}")
print(f"loops: {loops_count} (期望2)")

# 验证跨宫边
cross_palace_query = """
RETURN LENGTH(
  FOR e IN dg_edges
    FILTER e.edge_type == 'cross_palace'
    RETURN true
)
"""
cross_palace_count_db = list(db.aql.execute(cross_palace_query))[0]
print(f"跨宫边: {cross_palace_count_db} (期望10)")

# 验证节点类型分布
type_query = """
FOR v IN dg_nodes
  COLLECT type = v.type WITH COUNT INTO count
  RETURN {type, count}
"""
type_dist = list(db.aql.execute(type_query))
print(f"\n节点类型分布:")
for t in type_dist:
    print(f"  {t['type']}: {t['count']}")

# 验证边类型分布
edge_type_query = """
FOR e IN dg_edges
  COLLECT type = e.edge_type WITH COUNT INTO count
  RETURN {type, count}
"""
edge_type_dist = list(db.aql.execute(edge_type_query))
print(f"\n边类型分布:")
for t in edge_type_dist:
    print(f"  {t['type']}: {t['count']}")

# 图遍历测试：从命宫分析出发，找所有可达节点
# 先获取命宫分析的_id
minggong_doc = list(db.collection("dg_nodes").find({"node_id": "命宫分析"}))
if minggong_doc:
    minggong_id = minggong_doc[0]["_id"]
    traversal_query = f"""
    FOR v, e, p IN 1..5 OUTBOUND '{minggong_id}' dg_edges
      RETURN DISTINCT v.node_id
    """
    reachable = list(db.aql.execute(traversal_query))
    print(f"\n图遍历测试: 从'命宫分析'出发5步可达 {len(reachable)} 个节点")
    if reachable:
        print(f"  示例: {reachable[:10]}")
else:
    print("\n⚠️  未找到'命宫分析'节点")

print("\n✅ POC-7依赖图导入ArangoDB完成")
