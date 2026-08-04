#!/usr/bin/env python3
"""topo_generator.py —— 经典计算展开G'_topo骨架

从ArangoDB中的依赖图G（dg_nodes/dg_edges）自动生成G'_topo骨架（ut_nodes/ut_edges）。

分层实现：
  L0 骨架展开：节点/边拷贝 + Kahn拓扑排序 → 保证全覆盖
  L1 类型推断：static/dynamic + connection类型（linear/shortcut/cross_palace）
  L2 section划分：每N个一段 + 意识单独成章（推荐，AI可在L3调整）

经典计算保证L0全覆盖，TopologyVerifier必然1次通过100%覆盖。
L3语义标注（section命名/spiral类型最终确认）保留给AI。

对应92号方案。
"""
import argparse
import json
import os
import sys
from collections import defaultdict, deque
from datetime import datetime

from arango import ArangoClient

DB_NAME = "xishujuzhen_math"


class TopoGenerator:
    """经典计算展开G'_topo骨架"""

    def __init__(self, host="localhost", port=8529, db_name=DB_NAME,
                 username="root", password="REDACTED-DB-PASSWORD"):
        client = ArangoClient(hosts=f"http://{host}:{port}")
        self.db = client.db(db_name, username=username, password=password)

    # ============================================================
    # L0: 骨架展开
    # ============================================================
    def topological_sort(self, nodes, edges):
        """Kahn算法拓扑排序（只对depends_on边）

        calls边不参与排序（calls是"调用"关系，不是"依赖"关系）。
        意识节点不被depends_on，自然排在后面。
        多入度0节点按字母序，保证确定性。
        """
        # 构建邻接表和入度（只对depends_on边）
        node_ids = {n["node_id"] for n in nodes}
        adj = defaultdict(list)
        in_degree = defaultdict(int)
        for n in node_ids:
            in_degree[n] = 0

        for e in edges:
            etype = e.get("edge_type", e.get("type", "depends_on"))
            # 拓扑排序考虑所有有向边类型（depends_on/solution_path/cross_domain等）
            # 但invokes边指向cognition_units，不在当前node_ids中，自然被跳过
            if etype != "invokes":
                src = e.get("from_node_id", "")
                dst = e.get("to_node_id", "")
                if src in node_ids and dst in node_ids:
                    adj[src].append(dst)
                    in_degree[dst] += 1

        # Kahn算法
        queue = deque(sorted([n for n in node_ids if in_degree[n] == 0]))
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in sorted(adj[node]):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 检查是否有环
        if len(order) != len(node_ids):
            remaining = node_ids - set(order)
            # 螺旋环路是允许的——把环路中的节点按字母序加入
            # （环路结构通过loops集合单独记录，不影响骨架展开的覆盖性）
            print(f"  [信息] 检测到环路，涉及{len(remaining)}个节点: {remaining}")
            print(f"  [处理] 环路节点按字母序加入拓扑排序，环路结构通过loops集合保留")
            order.extend(sorted(remaining))

        return order

    def generate_skeleton(self, nodes, edges):
        """生成G'_topo骨架——节点/边拷贝 + 拓扑排序

        L0层：纯结构拷贝，保证拓扑同构。
        """
        topo_order = self.topological_sort(nodes, edges)

        # 节点拷贝（保留所有字段，添加traversal_order）
        ut_nodes = []
        for i, node_id in enumerate(topo_order, 1):
            node = next(n for n in nodes if n["node_id"] == node_id)
            ut_node = {
                "node_id": node["node_id"],
                "type": node.get("type", "substep"),
                "context": node.get("context", ""),
                "traversal_order": i,
            }
            ut_nodes.append(ut_node)

        # 边拷贝
        ut_edges = []
        for e in edges:
            etype = e.get("edge_type", e.get("type", "depends_on"))
            if etype == "invokes":
                continue  # invokes边指向认知图，不在依赖图展开范围内
            ut_edge = {
                "from_node_id": e.get("from_node_id", ""),
                "to_node_id": e.get("to_node_id", ""),
                "edge_type": etype,
            }
            ut_edges.append(ut_edge)

        return ut_nodes, ut_edges

    # ============================================================
    # L1: 类型推断
    # ============================================================
    def infer_type(self, node, edges, loops):
        """推断节点的static/dynamic类型

        规则：
        - 意识节点 → static（意识是静态背景）
        - 在螺旋环路中的节点 → dynamic
        - 其他 → static
        """
        node_id = node["node_id"]
        if node.get("type") == "意识":
            return "static"

        # 检查是否在环路中
        loop_node_ids = set()
        for loop in loops:
            if loop.get("graph") == "dependency_graph":
                loop_node_ids.update(loop.get("nodes", []))
        if node_id in loop_node_ids:
            return "dynamic"

        return "static"

    def infer_connection(self, edge, ut_nodes_map):
        """推断边的connection类型

        规则：
        - depends_on → linear（顺序依赖）
        - calls → shortcut（调用是跳转）
        - 跨section的边 → cross_palace
        """
        if edge["edge_type"] == "calls":
            return "shortcut"
        # 检查是否跨section（L2之后才能确定，这里先默认linear）
        return "linear"

    def infer_traversal(self, node, loops):
        """推断节点的traversal类型（spiral_static/spiral_dynamic/linear）"""
        node_id = node["node_id"]
        for loop in loops:
            if loop.get("graph") == "dependency_graph" and node_id in loop.get("nodes", []):
                return loop.get("traversal", "spiral_static")
        return "linear"

    def apply_type_inference(self, ut_nodes, ut_edges, nodes, edges, loops):
        """L1：对ut_nodes和ut_edges应用类型推断"""
        nodes_map = {n["node_id"]: n for n in nodes}
        for utn in ut_nodes:
            orig = nodes_map.get(utn["node_id"], {})
            utn["type"] = self.infer_type(orig, edges, loops)
            utn["traversal"] = self.infer_traversal(orig, loops)

        for ute in ut_edges:
            ute["connection"] = self.infer_connection(ute, {})
        return ut_nodes, ut_edges

    # ============================================================
    # L2: section划分
    # ============================================================
    def recommend_sections(self, ut_nodes, edges, nodes_per_section=5):
        """推荐section划分

        规则：
        - 每N个节点一段（默认5）
        - 意识节点单独成章
        - section命名：第X章§Y
        """
        # 分离意识节点和步骤节点
        step_nodes = [n for n in ut_nodes if n["type"] != "static" or n.get("traversal") != "linear"]
        # 实际上用原始type判断
        step_nodes = []
        awareness_nodes = []
        for n in ut_nodes:
            orig_type = n.get("type", "")
            if orig_type == "意识" or (n.get("traversal", "").startswith("spiral")):
                awareness_nodes.append(n)
            else:
                step_nodes.append(n)

        # 步骤节点按traversal_order分段
        step_nodes.sort(key=lambda n: n.get("traversal_order", 0))
        sections = {}
        current_section = 1
        current_section_nodes = []

        for node in step_nodes:
            current_section_nodes.append(node)
            if len(current_section_nodes) >= nodes_per_section:
                section_name = f"第{chinese_num(current_section)}章"
                for n in current_section_nodes:
                    pos = current_section_nodes.index(n) + 1
                    sections[n["node_id"]] = f"{section_name}§{pos}"
                current_section += 1
                current_section_nodes = []

        # 剩余节点
        if current_section_nodes:
            section_name = f"第{chinese_num(current_section)}章"
            for n in current_section_nodes:
                pos = current_section_nodes.index(n) + 1
                sections[n["node_id"]] = f"{section_name}§{pos}"

        # 意识节点单独成章
        if awareness_nodes:
            section_name = f"第{chinese_num(current_section)}章"
            for n in awareness_nodes:
                pos = awareness_nodes.index(n) + 1
                sections[n["node_id"]] = f"{section_name}§{pos}"

        return sections

    def assign_positions(self, topo_order, sections):
        """根据section划分分配position（section内位置）"""
        section_counters = {}
        positions = {}
        for node_id in topo_order:
            section = sections.get(node_id, "未分类")
            if section not in section_counters:
                section_counters[section] = 0
            section_counters[section] += 1
            positions[node_id] = section_counters[section]
        return positions

    def assign_edge_sections(self, ut_edges, ut_nodes_map):
        """为边分配section（from节点所在section）"""
        for ute in ut_edges:
            from_node = ut_nodes_map.get(ute["from_node_id"], {})
            ute["section"] = from_node.get("section", "未分类")
        return ut_edges

    def apply_section_division(self, ut_nodes, ut_edges, edges):
        """L2：应用section划分"""
        sections = self.recommend_sections(ut_nodes, edges)
        for utn in ut_nodes:
            utn["section"] = sections.get(utn["node_id"], "未分类")

        ut_nodes_map = {n["node_id"]: n for n in ut_nodes}
        # 重新推断跨section边
        for ute in ut_edges:
            from_sec = ut_nodes_map.get(ute["from_node_id"], {}).get("section", "")
            to_sec = ut_nodes_map.get(ute["to_node_id"], {}).get("section", "")
            if from_sec and to_sec and from_sec != to_sec:
                ute["connection"] = "cross_palace"
            utn_from = ut_nodes_map.get(ute["from_node_id"], {})
            ute["section"] = utn_from.get("section", "未分类")
        return ut_nodes, ut_edges

    # ============================================================
    # 螺旋环路拷贝
    # ============================================================
    def copy_loops(self, loops):
        """拷贝螺旋环路到unfold_topo图

        不从图论算法推导，直接从G的loops集合拷贝，保证圈数不变。
        """
        ut_loops = []
        for loop in loops:
            if loop.get("graph") == "dependency_graph":
                ut_loop = {
                    "loop_id": loop["loop_id"],
                    "nodes": loop["nodes"],
                    "circles": loop["circles"],
                    "traversal": loop.get("traversal", "spiral_static"),
                    "contexts": loop.get("contexts", []),
                    "graph": "unfold_topo",
                    "type": "spiral",
                }
                ut_loops.append(ut_loop)
        return ut_loops

    # ============================================================
    # 主流程
    # ============================================================
    def generate(self, write_to_db=True, clear_existing=True):
        """完整生成G'_topo（L0+L1+L2+loops拷贝）"""
        # 读取G
        nodes = list(self.db.collection("dg_nodes").all())
        raw_edges = list(self.db.collection("dg_edges").all())
        loops = list(self.db.collection("loops").find({"graph": "dependency_graph"}))

        # 兼容两种边格式：
        # POC-2格式: from_node_id/to_node_id/edge_type
        # Phase A格式: _from/_to/type（ArangoDB标准）
        edges = []
        for e in raw_edges:
            if "from_node_id" in e:
                edges.append(e)
            else:
                # Phase A格式 → 标准化
                from_id = e.get("_from", "").split("/")[-1]
                to_id = e.get("_to", "").split("/")[-1]
                # _from可能是dg_nodes/xxx或cognition_units/xxx
                # 需要用node_id查实际名称
                from_node = list(self.db.aql.execute(
                    'FOR n IN dg_nodes FILTER n._key == @k RETURN n.node_id',
                    bind_vars={"k": from_id}))
                to_node = list(self.db.aql.execute(
                    'FOR n IN dg_nodes FILTER n._key == @k RETURN n.node_id',
                    bind_vars={"k": to_id}))
                from_name = from_node[0] if from_node else from_id
                to_name = to_node[0] if to_node else to_id
                edges.append({
                    "from_node_id": from_name,
                    "to_node_id": to_name,
                    "edge_type": e.get("type", e.get("edge_type", "depends_on")),
                    "_source": e.get("source", ""),
                })

        print(f"读取G: {len(nodes)}节点, {len(edges)}边, {len(loops)}环路")

        # L0: 骨架展开
        ut_nodes, ut_edges = self.generate_skeleton(nodes, edges)
        print(f"L0骨架: {len(ut_nodes)}节点, {len(ut_edges)}边")

        # L1: 类型推断
        ut_nodes, ut_edges = self.apply_type_inference(
            ut_nodes, ut_edges, nodes, edges, loops
        )
        print(f"L1类型推断完成")

        # L2: section划分
        ut_nodes, ut_edges = self.apply_section_division(ut_nodes, ut_edges, edges)
        print(f"L2 section划分完成")

        # 螺旋环路拷贝
        ut_loops = self.copy_loops(loops)
        print(f"环路拷贝: {len(ut_loops)}个")

        if write_to_db:
            self.write_to_db(ut_nodes, ut_edges, ut_loops, clear_existing)

        return ut_nodes, ut_edges, ut_loops

    def write_to_db(self, ut_nodes, ut_edges, ut_loops, clear_existing=True):
        """写入ArangoDB的ut_nodes/ut_edges/loops集合"""
        ut_nodes_col = self.db.collection("ut_nodes")
        ut_edges_col = self.db.collection("ut_edges")
        loops_col = self.db.collection("loops")

        if clear_existing:
            ut_nodes_col.truncate()
            ut_edges_col.truncate()
            # 只删除unfold_topo的loops，保留dependency_graph的
            existing_ut_loops = list(loops_col.find({"graph": "unfold_topo"}))
            for l in existing_ut_loops:
                loops_col.delete(l["_key"])
            print("  清空 ut_nodes, ut_edges, unfold_topo loops")

        now = datetime.utcnow().isoformat() + "Z"

        # 写入ut_nodes
        for utn in ut_nodes:
            doc = dict(utn)
            doc["created_at"] = now
            ut_nodes_col.insert(doc)

        # 写入ut_edges（需要_from/_to指向ut_nodes的_id）
        # 先建node_id -> _id映射
        ut_node_ids = {}
        for n in list(ut_nodes_col.all()):
            ut_node_ids[n["node_id"]] = n["_id"]

        for ute in ut_edges:
            from_id = ut_node_ids.get(ute["from_node_id"])
            to_id = ut_node_ids.get(ute["to_node_id"])
            if from_id and to_id:
                doc = dict(ute)
                doc["_from"] = from_id
                doc["_to"] = to_id
                doc["created_at"] = now
                ut_edges_col.insert(doc)

        # 写入loops
        for utl in ut_loops:
            doc = dict(utl)
            doc["created_at"] = now
            loops_col.insert(doc)

        print(f"✅ 写入 ut_nodes: {len(ut_nodes)}条")
        print(f"✅ 写入 ut_edges: {len(ut_edges)}条")
        print(f"✅ 写入 unfold_topo loops: {len(ut_loops)}条")

    def verify_coverage(self):
        """调用TopologyVerifier验证覆盖"""
        sys.path.insert(0, os.path.dirname(__file__))
        from topology_verifier import TopologyVerifier
        tv = TopologyVerifier(db_name=DB_NAME)
        return tv.verify_all()


def chinese_num(n):
    """阿拉伯数字转中文数字（1-20）"""
    nums = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
            "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十"]
    if 0 <= n <= 20:
        return nums[n]
    return str(n)


def main():
    parser = argparse.ArgumentParser(description="经典计算展开G'_topo骨架")
    parser.add_argument("--mode", choices=["skeleton", "full"], default="full",
                        help="skeleton=只L0, full=L0+L1+L2")
    parser.add_argument("--no-write", action="store_true", help="不写入ArangoDB，只输出")
    parser.add_argument("--verify", action="store_true", help="生成后调用TopologyVerifier验证")
    args = parser.parse_args()

    gen = TopoGenerator()
    ut_nodes, ut_edges, ut_loops = gen.generate(
        write_to_db=not args.no_write
    )

    print(f"\n生成完成: {len(ut_nodes)}节点, {len(ut_edges)}边, {len(ut_loops)}环路")

    if args.verify:
        print("\n" + "=" * 60)
        print("TopologyVerifier验证")
        print("=" * 60)
        report = gen.verify_coverage()
        print(report.summary())


if __name__ == "__main__":
    main()
