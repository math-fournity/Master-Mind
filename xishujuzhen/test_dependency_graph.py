#!/usr/bin/env python3
"""test_dependency_graph.py —— 依赖图6项测试自动化

每批吸收后跑这6项测试：
  T1 依赖图完整性：节点/边/领域覆盖统计
  T2 子图提取：随机选1题提取依赖子图，验证路径完整
  T3 跨领域连通性：跨领域边能否连通不同领域
  T4 topo_generator：能否生成G'_topo
  T5 TopologyVerifier：拓扑覆盖验证
  T6 回归验证：已有POC基线是否仍通过

用法：
  python3 test_dependency_graph.py [--verbose]
"""
import sys
import os
import json
import random
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cognition_sdk_math import CognitionSDK


class DependencyGraphTester:
    """依赖图6项测试"""

    def __init__(self):
        self.sdk = CognitionSDK()
        self.results = []

    def run_all(self):
        """运行全部6项测试"""
        print("=" * 60)
        print("依赖图6项测试")
        print("=" * 60)

        self.test1_completeness()
        self.test2_subgraph_extraction()
        self.test3_cross_domain_connectivity()
        self.test4_topo_generator()
        self.test5_topology_verifier()
        self.test6_regression()

        self.print_summary()
        return all(r["passed"] for r in self.results)

    def add_result(self, test_id, name, passed, details=""):
        self.results.append({
            "test_id": test_id,
            "name": name,
            "passed": passed,
            "details": details
        })
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"\n[{test_id}] {name}: {status}")
        if details:
            for line in details.split("\n"):
                print(f"  {line}")

    def test1_completeness(self):
        """T1: 依赖图完整性"""
        n_nodes = list(self.sdk.db.aql.execute('RETURN COUNT(dg_nodes)'))[0]
        n_edges = list(self.sdk.db.aql.execute('RETURN COUNT(dg_edges)'))[0]
        n_problems = list(self.sdk.db.aql.execute('RETURN COUNT(problems)'))[0]
        n_solutions = list(self.sdk.db.aql.execute('RETURN COUNT(solutions)'))[0]

        # 节点类型分布
        types = list(self.sdk.db.aql.execute(
            'FOR n IN dg_nodes COLLECT t=n.type WITH COUNT INTO c SORT c DESC RETURN {type:t, count:c}'))
        type_str = ", ".join(f"{t['type']}={t['count']}" for t in types)

        # 边类型分布
        etypes = list(self.sdk.db.aql.execute(
            'FOR e IN dg_edges COLLECT t=e.type WITH COUNT INTO c SORT c DESC RETURN {type:t, count:c}'))
        etype_str = ", ".join(f"{e['type']}={e['count']}" for e in etypes)

        # 领域覆盖
        domains = list(self.sdk.db.aql.execute(
            'FOR n IN dg_nodes FILTER n.type=="concept" COLLECT d=n.domain WITH COUNT INTO c SORT c DESC RETURN {domain:d, count:c}'))
        domain_list = [d['domain'] for d in domains if d['domain']]

        # 跨领域边数
        cd_count = list(self.sdk.db.aql.execute(
            'RETURN COUNT(FOR e IN dg_edges FILTER e.type=="cross_domain" RETURN 1)'))[0]

        passed = n_nodes > 0 and n_edges > 0 and len(domain_list) >= 3
        details = (f"题库: {n_problems}道题, {n_solutions}个解法\n"
                   f"节点: {n_nodes} ({type_str})\n"
                   f"边: {n_edges} ({etype_str})\n"
                   f"领域覆盖: {len(domain_list)}个领域 ({', '.join(domain_list[:8])})\n"
                   f"跨领域映射边: {cd_count}")
        self.add_result("T1", "依赖图完整性", passed, details)

    def test2_subgraph_extraction(self):
        """T2: 子图提取——随机选1题验证路径完整"""
        problems = list(self.sdk.db.aql.execute('FOR p IN problems RETURN p.problem_id'))
        if not problems:
            self.add_result("T2", "子图提取", False, "无题目")
            return

        pid = random.choice(problems)
        sols = list(self.sdk.db.aql.execute(
            'FOR s IN solutions FILTER s.problem_id==@pid RETURN s',
            bind_vars={"pid": pid}))

        all_ok = True
        details_lines = [f"选题: {pid} ({len(sols)}个解法)"]
        for sol in sols:
            path = sol.get('path', [])
            concepts = [step['concept'] for step in path]
            # 检查每个concept是否在dg_nodes中
            missing = []
            for c in concepts:
                found = list(self.sdk.db.aql.execute(
                    'FOR n IN dg_nodes FILTER n.node_id==@cid LIMIT 1 RETURN n',
                    bind_vars={"cid": c}))
                if not found:
                    missing.append(c)
            if missing:
                all_ok = False
                details_lines.append(f"  {sol['solution_id']}: ❌ 缺失{len(missing)}个节点")
            else:
                details_lines.append(f"  {sol['solution_id']}: ✅ {len(concepts)}步完整")

        self.add_result("T2", "子图提取", all_ok, "\n".join(details_lines))

    def test3_cross_domain_connectivity(self):
        """T3: 跨领域连通性"""
        cd_edges = list(self.sdk.db.aql.execute(
            'FOR e IN dg_edges FILTER e.type=="cross_domain" LIMIT 20 RETURN {from:SPLIT(e._from,"/")[1], to:SPLIT(e._to,"/")[1]}'))

        if len(cd_edges) < 3:
            self.add_result("T3", "跨领域连通性", False, f"跨领域边太少: {len(cd_edges)}")
            return

        # 尝试从一个领域concept出发，沿跨领域边可达
        if cd_edges:
            start = cd_edges[0]['from']
            try:
                reachable = list(self.sdk.db.aql.execute(
                    'FOR v, e, p IN 1..3 OUTBOUND CONCAT("dg_nodes/", @start) dg_edges FILTER e.type=="cross_domain" RETURN DISTINCT v.node_id',
                    bind_vars={"start": start}))
                passed = len(reachable) >= 1
                details = f"从{start}出发沿跨领域边3步可达: {len(reachable)}个节点\n样例: {reachable[:5]}"
            except:
                passed = False
                details = "图遍历失败"
        else:
            passed = False
            details = "无跨领域边"

        self.add_result("T3", "跨领域连通性", passed, details)

    def test4_topo_generator(self):
        """T4: topo_generator能否生成G'_topo"""
        try:
            from topo_generator import TopoGenerator
            gen = TopoGenerator()
            gen.generate()

            ut_n = list(self.sdk.db.aql.execute('RETURN COUNT(ut_nodes)'))[0]
            dg_n = list(self.sdk.db.aql.execute('RETURN COUNT(dg_nodes)'))[0]

            passed = ut_n == dg_n
            details = f"ut_nodes={ut_n}, dg_nodes={dg_n}, {'节点数匹配' if passed else '节点数不匹配!'}"
        except Exception as e:
            passed = False
            details = f"topo_generator失败: {str(e)[:100]}"

        self.add_result("T4", "topo_generator", passed, details)

    def test5_topology_verifier(self):
        """T5: TopologyVerifier拓扑覆盖验证"""
        try:
            from topology_verifier import TopologyVerifier
            ver = TopologyVerifier()

            nc = ver.verify_node_coverage()
            ec = ver.verify_edge_coverage()

            node_rate = nc.coverage_rate
            edge_rate = ec.coverage_rate

            # 排除invokes边后计算（invokes指向cognition_units，不在ut_edges中是设计预期）
            non_invoke_uncovered = [e for e in ec.uncovered if e.get('edge_type') != 'invokes']
            non_invoke_total = ec.total - sum(1 for e in ec.uncovered if e.get('edge_type') == 'invokes')
            adjusted_edge_rate = (non_invoke_total - len(non_invoke_uncovered)) / non_invoke_total if non_invoke_total > 0 else 0

            passed = node_rate == 1.0 and adjusted_edge_rate >= 0.85
            details = (f"节点覆盖: {nc.covered}/{nc.total} = {node_rate*100:.1f}%\n"
                       f"边覆盖(含invokes): {ec.covered}/{ec.total} = {edge_rate*100:.1f}%\n"
                       f"边覆盖(排除invokes): {non_invoke_total - len(non_invoke_uncovered)}/{non_invoke_total} = {adjusted_edge_rate*100:.1f}%\n"
                       f"未覆盖(排除invokes): {len(non_invoke_uncovered)}条")
        except Exception as e:
            passed = False
            details = f"TopologyVerifier失败: {str(e)[:100]}"

        self.add_result("T5", "TopologyVerifier", passed, details)

    def test6_regression(self):
        """T6: 回归验证——POC基线"""
        try:
            result = os.popen(
                f"{sys.executable} {os.path.join(os.path.dirname(__file__), 'cognition_audit_math.py')} "
                f"poc-regression --seeds seven_step_workflow,invariant_thinking "
                f"--ground-truth seven_step_workflow,invariant_thinking,topology_verifier,classic_expansion,math_awareness_nodes"
            ).read()

            if "100/100" in result:
                passed = True
                details = "POC回归: 100/100"
            else:
                # 提取分数
                import re
                score_match = re.search(r'(\d+)/100', result)
                score = score_match.group(0) if score_match else "未知"
                passed = "100/100" in result
                details = f"POC回归: {score}"
        except Exception as e:
            passed = False
            details = f"回归验证失败: {str(e)[:100]}"

        self.add_result("T6", "回归验证", passed, details)

    def print_summary(self):
        print("\n" + "=" * 60)
        print("测试总结")
        print("=" * 60)
        passed_count = sum(1 for r in self.results if r["passed"])
        total = len(self.results)
        for r in self.results:
            status = "✅" if r["passed"] else "❌"
            print(f"  {status} {r['test_id']} {r['name']}")
        print(f"\n{passed_count}/{total} 通过")
        if passed_count == total:
            print("✅ 全部通过，可以继续下一批吸收")
        else:
            print("⚠️ 有测试未通过，需修复后再继续吸收")


def main():
    parser = argparse.ArgumentParser(description="依赖图6项测试自动化")
    parser.add_argument("--verbose", action="store_true", help="详细输出")
    args = parser.parse_args()

    tester = DependencyGraphTester()
    all_passed = tester.run_all()
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
