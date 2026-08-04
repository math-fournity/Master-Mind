#!/usr/bin/env python3
"""TopologyVerifier —— 拓扑覆盖验证

验证展开图拓扑骨架G'_topo覆盖依赖图G的所有节点和边。
这是确定性验证，不是"文字随机匹配"。

对应78号文档中的数学本质：
- 节点覆盖：∀ v ∈ V, ∃ v' ∈ V'_topo
- 边覆盖：∀ e ∈ E, ∃ e' ∈ E'_topo
- 螺旋环路覆盖：每个环路圈数保持
- KC忠实：∀ v, f(v) 忠实于 kᵢ
"""
from arango import ArangoClient
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CoverageResult:
    """覆盖验证结果"""
    total: int = 0
    covered: int = 0
    uncovered: list = field(default_factory=list)

    @property
    def coverage_rate(self) -> float:
        if self.total == 0:
            return 1.0
        return self.covered / self.total

    @property
    def passed(self) -> bool:
        return len(self.uncovered) == 0


@dataclass
class TopologyVerifyReport:
    """完整拓扑覆盖验证报告"""
    nodes: CoverageResult = field(default_factory=CoverageResult)
    edges: CoverageResult = field(default_factory=CoverageResult)
    cross_palace_edges: CoverageResult = field(default_factory=CoverageResult)
    loops: list = field(default_factory=list)  # [{loop_id, expected, actual, match}]

    @property
    def passed(self) -> bool:
        return (
            self.nodes.passed
            and self.edges.passed
            and self.cross_palace_edges.passed
            and all(l["match"] for l in self.loops)
        )

    def summary(self) -> str:
        lines = []
        lines.append("=" * 60)
        lines.append("拓扑覆盖验证报告")
        lines.append("=" * 60)
        lines.append(f"\n节点覆盖: {self.nodes.covered}/{self.nodes.total} = {self.nodes.coverage_rate:.1%}")
        if self.nodes.uncovered:
            lines.append(f"  未覆盖节点: {self.nodes.uncovered}")
        lines.append(f"\n边覆盖: {self.edges.covered}/{self.edges.total} = {self.edges.coverage_rate:.1%}")
        if self.edges.uncovered:
            lines.append(f"  未覆盖边: {self.edges.uncovered}")
        lines.append(f"\n跨宫边覆盖: {self.cross_palace_edges.covered}/{self.cross_palace_edges.total} = {self.cross_palace_edges.coverage_rate:.1%}")
        if self.cross_palace_edges.uncovered:
            lines.append(f"  未覆盖跨宫边: {self.cross_palace_edges.uncovered}")
        lines.append(f"\n螺旋环路:")
        for loop in self.loops:
            status = "✅" if loop["match"] else "❌"
            lines.append(f"  {status} {loop['loop_id']}: 期望{loop['expected']}圈, 实际{loop['actual']}圈")
        lines.append(f"\n{'✅ 拓扑覆盖验证通过' if self.passed else '❌ 拓扑覆盖验证未通过'}")
        return "\n".join(lines)


class TopologyVerifier:
    """拓扑覆盖验证器

    验证G'_topo覆盖G的所有节点和边。
    使用AQL集合差集——确定性验证，不是文字匹配。
    """

    def __init__(self, host: str = "localhost", port: int = 8529,
                 username: str = "root", password: str = "REDACTED-DB-PASSWORD",
                 db_name: str = "xishujuzhen_math"):
        client = ArangoClient(hosts=f"http://{host}:{port}")
        self.db = client.db(db_name, username=username, password=password)

    def verify_node_coverage(self) -> CoverageResult:
        """验证G'_topo覆盖G的所有节点

        AQL: 找出在dg_nodes中但不在ut_nodes中的节点
        """
        query = """
        FOR v IN dg_nodes
          FILTER v.node_id NOT IN (
            FOR n IN ut_nodes
              RETURN n.node_id
          )
          RETURN v.node_id
        """
        cursor = self.db.aql.execute(query)
        uncovered = list(cursor)

        total = self.db.collection("dg_nodes").count()
        return CoverageResult(
            total=total,
            covered=total - len(uncovered),
            uncovered=uncovered,
        )

    def verify_edge_coverage(self) -> CoverageResult:
        """验证G'_topo覆盖G的所有边

        用AQL LEFT JOIN找出dg_edges中没有对应ut_edges的边。
        兼容两种边格式：POC-2格式(from_node_id/to_node_id)和Phase A格式(_from/_to/type)。
        """
        query = """
        FOR e IN dg_edges
          LET efrom = e.from_node_id || (
            FOR n IN dg_nodes FILTER n._key == SPLIT(e._from, "/")[1] LIMIT 1 RETURN n.node_id
          )[0]
          LET eto = e.to_node_id || (
            FOR n IN dg_nodes FILTER n._key == SPLIT(e._to, "/")[1] LIMIT 1 RETURN n.node_id
          )[0]
          LET matched = (
            FOR te IN ut_edges
              FILTER te.from_node_id == efrom
              FILTER te.to_node_id == eto
              RETURN true
          )
          FILTER LENGTH(matched) == 0
          RETURN {
            from: efrom,
            to: eto,
            edge_type: e.edge_type || e.type
          }
        """
        cursor = self.db.aql.execute(query)
        uncovered = list(cursor)

        total = self.db.collection("dg_edges").count()
        return CoverageResult(
            total=total,
            covered=total - len(uncovered),
            uncovered=uncovered,
        )

    def verify_cross_palace_edge_coverage(self) -> CoverageResult:
        """验证跨宫边覆盖

        只检查edge_type为'cross_palace'的边
        """
        query = """
        FOR e IN dg_edges
          FILTER e.edge_type == 'cross_palace'
          LET matched = (
            FOR te IN ut_edges
              FILTER te.edge_type == 'cross_palace'
              FILTER te.from_node_id == e.from_node_id
              FILTER te.to_node_id == e.to_node_id
              RETURN true
          )
          FILTER LENGTH(matched) == 0
          RETURN {
            from: e.from_node_id,
            to: e.to_node_id,
            reason: e.reason
          }
        """
        cursor = self.db.aql.execute(query)
        uncovered = list(cursor)

        # 统计跨宫边总数
        count_query = """
        RETURN LENGTH(
          FOR e IN dg_edges
            FILTER e.edge_type == 'cross_palace'
            RETURN true
        )
        """
        count_cursor = self.db.aql.execute(count_query)
        total = list(count_cursor)[0]

        return CoverageResult(
            total=total,
            covered=total - len(uncovered),
            uncovered=uncovered,
        )

    def verify_loop_coverage(self) -> list:
        """验证螺旋环路圈数保持"""
        loops = list(self.db.collection("loops").find({"graph": "dependency_graph"}))
        results = []
        for loop in loops:
            topo_loop_cursor = self.db.collection("loops").find({
                "graph": "unfold_topo",
                "loop_id": loop["loop_id"],
            })
            topo_loops = list(topo_loop_cursor)
            if topo_loops:
                topo_loop = topo_loops[0]
                results.append({
                    "loop_id": loop["loop_id"],
                    "expected": loop["circles"],
                    "actual": topo_loop["circles"],
                    "match": loop["circles"] == topo_loop["circles"],
                })
            else:
                results.append({
                    "loop_id": loop["loop_id"],
                    "expected": loop["circles"],
                    "actual": 0,
                    "match": False,
                })
        return results

    def verify_all(self) -> TopologyVerifyReport:
        """完整拓扑覆盖验证"""
        return TopologyVerifyReport(
            nodes=self.verify_node_coverage(),
            edges=self.verify_edge_coverage(),
            cross_palace_edges=self.verify_cross_palace_edge_coverage(),
            loops=self.verify_loop_coverage(),
        )

    def verify_kc_fidelity(self) -> dict:
        """验证KC忠实度

        检查uf_nodes中每个节点的text_content是否包含对应的knowledge_content。
        这是文字层面的验证（命理知识），不是拓扑验证。
        """
        query = """
        FOR kc IN kcs
          FOR uf IN uf_nodes
            FILTER uf.node_id == kc.node_id
            RETURN {
              node_id: kc.node_id,
              knowledge_content: kc.knowledge_content,
              text_content: uf.text_content,
              is_faithful: CONTAINS(uf.text_content, kc.knowledge_content)
            }
        """
        cursor = self.db.aql.execute(query)
        results = list(cursor)

        total = len(results)
        faithful = sum(1 for r in results if r["is_faithful"])
        unfaithful = [r["node_id"] for r in results if not r["is_faithful"]]

        return {
            "total": total,
            "faithful": faithful,
            "unfaithful": unfaithful,
            "fidelity_rate": faithful / total if total > 0 else 1.0,
            "details": results,
        }


if __name__ == "__main__":
    verifier = TopologyVerifier()
    report = verifier.verify_all()
    print(report.summary())

    print("\n" + "=" * 60)
    print("KC忠实度验证")
    print("=" * 60)
    kc_report = verifier.verify_kc_fidelity()
    print(f"\nKC忠实: {kc_report['faithful']}/{kc_report['total']} = {kc_report['fidelity_rate']:.1%}")
    if kc_report["unfaithful"]:
        print(f"不忠实的KC: {kc_report['unfaithful']}")
