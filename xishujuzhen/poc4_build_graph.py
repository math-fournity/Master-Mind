#!/usr/bin/env python3
"""
POC-4: Klein瓶同调群计算——依赖图构建与导入ArangoDB
12节点 + 15边 + 1个新意识节点(structural_thinking)
"""
import sys
sys.path.insert(0, "/data/master-mind/xishujuzhen")
from cognition_sdk_math import CognitionSDK

sdk = CognitionSDK()
db = sdk.db

# ============================================================
# 1. 新增意识节点 structural_thinking
# ============================================================
print("=== 1. 新增意识节点 structural_thinking ===")

st_doc = {
    "_key": "structural_thinking",
    "cog_id": "structural_thinking",
    "title": "结构思维",
    "category": "awareness",
    "status": "active",
    "key_cognition": "识别数学对象的代数结构（CW结构→链复形→同调群），结构决定计算路径。不是先算再想，而是先看结构再决定怎么算。",
    "source_docs": [113],
    "current_version": "v1",
    "domain": "algebraic_topology",
    "discovery_poc": "POC-4"
}

cog_col = db.collection("cognition_units")
if not cog_col.has("structural_thinking"):
    cog_col.insert(st_doc)
    print(f"  创建: structural_thinking")
else:
    print(f"  已存在: structural_thinking")

# 版本链
ver_col = db.collection("cog_versions")
ver_col.insert({
    "_key": "structural_thinking_v1",
    "cog_id": "structural_thinking",
    "version": "v1",
    "version_order": 1,
    "doc_ref": "dev-docs/113",
    "summary": "POC-4发现：代数拓扑中结构思维是核心——CW结构决定链复形，链复形决定同调群",
    "created_at": "2026-08-04"
})

# ============================================================
# 2. 创建dg_nodes (12节点)
# ============================================================
print("\n=== 2. 创建dg_nodes (12节点) ===")

nodes = [
    {"node_id": "Klein瓶同调群计算", "type": "step", "context": "计算Klein瓶K的整系数同调群H_n(K)", "kc": "Klein瓶K的CW结构为1个0-cell, 2个1-cell(a,b), 1个2-cell。计算H_0(K), H_1(K), H_2(K)。"},
    {"node_id": "Klein瓶CW结构", "type": "substep", "context": "确定CW结构", "kc": "Klein瓶有CW结构：1个0-cell, 2个1-cell(a,b), 1个2-cell。粘贴映射为aba^{-1}b。"},
    {"node_id": "胞腔链复形", "type": "substep", "context": "构造cellular chain complex", "kc": "链复形为 0→Z --d_2--> Z² --d_1--> Z → 0，其中Z对应2-cell, Z²对应1-cell(a,b), Z对应0-cell。"},
    {"node_id": "边界映射d_2", "type": "substep", "context": "计算d_2: Z→Z²", "kc": "Klein瓶粘贴映射aba^{-1}b的非定向性导致d_2(1)=0·a+2·b=2b。关键：系数为2是因为b边在粘贴中同向出现两次。"},
    {"node_id": "边界映射d_1", "type": "substep", "context": "计算d_1: Z²→Z", "kc": "d_1(a)=0, d_1(b)=0（每个1-cell的两端都粘到同一个0-cell）。"},
    {"node_id": "H_2计算", "type": "substep", "context": "H_2=ker(d_2)", "kc": "d_2: Z→Z², d_2(1)=2b。d_2是单射（2b≠0），所以ker(d_2)=0，H_2(K)=0。关键：非定向曲面H_2=0。"},
    {"node_id": "H_1计算", "type": "substep", "context": "H_1=ker(d_1)/im(d_2)", "kc": "ker(d_1)=Z²（因为d_1=0），im(d_2)=<2b>。H_1=Z²/<2b>=Z⊕Z/2Z。关键：有挠部分Z/2Z。"},
    {"node_id": "H_0计算", "type": "substep", "context": "H_0=coker(d_1)", "kc": "H_0=Z/im(d_1)=Z/0=Z。Klein瓶是连通的，所以H_0=Z。"},
    {"node_id": "Euler特征数验证", "type": "substep", "context": "χ验证同调群自洽", "kc": "χ(K)=#0-cell-#1-cell+#2-cell=1-2+1=0。rank(H_0)-rank(H_1)+rank(H_2)=1-1+0=0 ✓。验证通过。"},
    {"node_id": "CW复形", "type": "concept", "domain": "algebraic_topology", "source": "standard"},
    {"node_id": "胞腔同调", "type": "concept", "domain": "algebraic_topology", "source": "arxiv:2408.16795"},
    {"node_id": "定向性检验", "type": "concept", "domain": "algebraic_topology", "source": "standard", "kc": "定向闭曲面H_2=Z，非定向闭曲面H_2=0。Klein瓶是非定向的（粘贴映射aba^{-1}b中有b同向两次），所以H_2=0。"},
]

dg_nodes = db.collection("dg_nodes")
for n in nodes:
    # 检查是否已存在
    existing = list(db.aql.execute(
        "FOR n IN dg_nodes FILTER n.node_id == @nid RETURN n",
        bind_vars={"nid": n["node_id"]}
    ))
    if existing:
        print(f"  已存在: {n['node_id']}")
    else:
        dg_nodes.insert(n)
        print(f"  创建: {n['node_id']} ({n['type']})")

# ============================================================
# 3. 创建dg_edges (15条)
# ============================================================
print("\n=== 3. 创建dg_edges (15条) ===")

def get_node_id(doc_id_str):
    """通过node_id获取dg_nodes的_id"""
    result = list(db.aql.execute(
        "FOR n IN dg_nodes FILTER n.node_id == @nid RETURN n._id",
        bind_vars={"nid": doc_id_str}
    ))
    return result[0] if result else None

edges = [
    ("Klein瓶同调群计算", "Klein瓶CW结构", "depends_on"),
    ("Klein瓶同调群计算", "胞腔同调", "invokes"),
    ("Klein瓶CW结构", "CW复形", "depends_on"),
    ("Klein瓶CW结构", "胞腔链复形", "depends_on"),
    ("胞腔链复形", "边界映射d_2", "depends_on"),
    ("胞腔链复形", "边界映射d_1", "depends_on"),
    ("边界映射d_2", "定向性检验", "depends_on"),
    ("边界映射d_2", "H_2计算", "depends_on"),
    ("边界映射d_1", "H_1计算", "depends_on"),
    ("边界映射d_1", "H_0计算", "depends_on"),
    ("H_2计算", "Euler特征数验证", "depends_on"),
    ("H_1计算", "Euler特征数验证", "depends_on"),
    ("H_0计算", "Euler特征数验证", "depends_on"),
    ("定向性检验", "H_2计算", "depends_on"),   # 螺旋环路
    ("H_2计算", "定向性检验", "depends_on"),    # 螺旋环路
]

dg_edges = db.collection("dg_edges")
for from_name, to_name, edge_type in edges:
    from_id = get_node_id(from_name)
    to_id = get_node_id(to_name)
    if not from_id or not to_id:
        print(f"  ERROR: 找不到节点 {from_name} 或 {to_name}")
        continue
    # 检查是否已存在
    existing = list(db.aql.execute(
        "FOR e IN dg_edges FILTER e._from == @fid AND e._to == @tid RETURN e",
        bind_vars={"fid": from_id, "tid": to_id}
    ))
    if existing:
        print(f"  已存在: {from_name} → {to_name}")
    else:
        dg_edges.insert({
            "_from": from_id,
            "_to": to_id,
            "from_node_id": from_name,
            "to_node_id": to_name,
            "edge_type": edge_type
        })
        print(f"  创建: {from_name} → {to_name} ({edge_type})")

# ============================================================
# 4. 统计
# ============================================================
print("\n=== 4. 统计 ===")
print(f"dg_nodes: {dg_nodes.count()}")
print(f"dg_edges: {dg_edges.count()}")
print(f"cognition_units: {db.collection('cognition_units').count()}")
print(f"cog_versions: {db.collection('cog_versions').count()}")

# POC-4节点
poc4_nodes = list(db.aql.execute("""
    FOR n IN dg_nodes
    FILTER n.node_id IN ["Klein瓶同调群计算","Klein瓶CW结构","胞腔链复形","边界映射d_2","边界映射d_1","H_2计算","H_1计算","H_0计算","Euler特征数验证","CW复形","胞腔同调","定向性检验"]
    RETURN n.node_id
"""))
print(f"POC-4节点: {len(poc4_nodes)}")
print(f"POC-4节点列表: {poc4_nodes}")
