#!/usr/bin/env python3
"""
verify_lattice_completeness.py
验证AI产出的闭元素清单相对于完全格B(G,M,I)的完备性。

读取AI输出的JSON（包含形式上下文和闭元素清单），
运行Next Closure算法枚举所有闭元素，
和AI声称的闭元素清单对比，输出审计报告。

用法：
    python3 verify_lattice_completeness.py <ai_output.json>

输出：
    - 完全格B(G,M,I)的闭元素总数
    - AI声称的闭元素数
    - 正确识别的闭元素数
    - 遗漏的闭元素（列出每个的外延和内涵）
    - 错误的闭元素（AI声称但程序不认为是闭元素）
    - 完备性得分

来源：332号——VMS-28c执行方案
技术：机械化过程描述+规范化审计+程序验证（six-mechanization-reference元组）
"""

import json
import sys
from itertools import combinations
from typing import Set, FrozenSet, Dict, List, Tuple


class FormalContext:
    """形式上下文 (G, M, I)"""

    def __init__(self, objects: List[str], attributes: List[str], incidence: List[List[int]]):
        self.objects = objects
        self.attributes = attributes
        self.obj_idx = {o: i for i, o in enumerate(objects)}
        self.attr_idx = {a: i for i, a in enumerate(attributes)}
        # incidence[i][j] = 1 if objects[i] has attributes[j]
        self.incidence = incidence
        # 验证矩阵维度
        n = len(objects)
        k = len(attributes)
        assert len(incidence) == n, f"incidence行数{n}≠对象数{len(objects)}"
        for row in incidence:
            assert len(row) == k, f"incidence列数{len(row)}≠属性数{k}"

    def extent_closure(self, A: Set[str]) -> Set[str]:
        """计算A''（属性闭包）：A' → A''"""
        if not A:
            # 空集的闭包：A'=M（所有属性），A''=所有具有M中所有属性的对象=通常空集
            # 但FCA中空集' = M（空集的对象共有所有属性——vacuously true）
            # 空集'' = M' = 具有所有属性的对象 = 通常空集
            A_prime = set(self.attributes)  # 空集的属性闭包是所有属性
        else:
            # A' = A中所有对象共有的属性
            A_indices = {self.obj_idx[o] for o in A}
            A_prime = set()
            for j, attr in enumerate(self.attributes):
                if all(self.incidence[i][j] == 1 for i in A_indices):
                    A_prime.add(attr)
        # A'' = 具有A'中所有属性的对象
        A_prime_indices = {self.attr_idx[a] for a in A_prime}
        A_double_prime = set()
        for i, obj in enumerate(self.objects):
            if all(self.incidence[i][j] == 1 for j in A_prime_indices):
                A_double_prime.add(obj)
        return A_double_prime

    def intent(self, A: Set[str]) -> Set[str]:
        """计算A'（A中所有对象的共同属性）"""
        if not A:
            return set(self.attributes)
        A_indices = {self.obj_idx[o] for o in A}
        result = set()
        for j, attr in enumerate(self.attributes):
            if all(self.incidence[i][j] == 1 for i in A_indices):
                result.add(attr)
        return result

    def is_closed(self, A: Set[str]) -> bool:
        """判断A是否是闭元素：A'' = A"""
        return self.extent_closure(A) == A

    def enumerate_all_closed_elements(self) -> List[Tuple[FrozenSet[str], FrozenSet[str]]]:
        """
        枚举所有闭元素（形式概念）。
        使用Next Closure算法（lectic order）。

        返回：[(extent, intent), ...] 按lectic order排序
        """
        n = len(self.objects)
        all_objects = set(self.objects)
        closed_elements = []

        # Next Closure算法
        # 从空集开始（如果空集是闭元素）
        # 然后按lectic order依次找下一个闭元素

        current = frozenset()  # 空集

        # 检查空集是否是闭元素
        empty_closure = self.extent_closure(set())
        if len(empty_closure) == 0:
            # 空集是闭元素
            closed_elements.append((frozenset(), frozenset(self.attributes)))

        # 如果空集的闭包不是空集，从空集的闭包开始
        if len(empty_closure) > 0:
            current = frozenset(empty_closure)
            closed_elements.append((current, frozenset(self.intent(set(current)))))

        # Next Closure: 给定当前闭元素A，找下一个闭元素
        # lectic order: 从右往左找第一个可以添加的对象
        objects_list = list(self.objects)

        while current != frozenset(all_objects):
            next_element = self._next_closure(current, objects_list)
            if next_element is None:
                break
            current = next_element
            intent = self.intent(set(current))
            closed_elements.append((current, frozenset(intent)))

        return closed_elements

    def _next_closure(self, A: FrozenSet[str], objects_list: List[str]) -> FrozenSet[str]:
        """
        Next Closure算法的核心：找到A之后的下一个闭元素（lectic order）。

        lectic order: (A < B) ⟺ 存在i使得 i∈B, i∉A, 且对所有j>i, j∈A ⟺ j∈B
        即从最大的index开始找，找到第一个可以"加入"的对象。

        Next Closure算法：
        for i from n-1 down to 0:
            if objects[i] in A: continue
            B = (A ∩ {objects[0..i-1]}) ∪ {objects[i]}
            B'' = closure(B)
            if B'' ∩ {objects[0..i-1]} == A ∩ {objects[0..i-1]}:
                return B''
        return None
        """
        n = len(objects_list)

        for i in range(n - 1, -1, -1):
            obj_i = objects_list[i]
            if obj_i in A:
                continue

            # B = (A ∩ {objects[0..i-1]}) ∪ {objects[i]}
            prefix = set(objects_list[:i])
            B = (set(A) & prefix) | {obj_i}

            # B'' = closure(B)
            B_closed = self.extent_closure(B)

            # 检查lectic condition: B'' ∩ prefix == A ∩ prefix
            if set(B_closed) & prefix == set(A) & prefix:
                return frozenset(B_closed)

        return None


def load_ai_output(filepath: str) -> dict:
    """加载AI输出的JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_ai_closed_elements(ai_output: dict) -> List[dict]:
    """提取AI声称的闭元素清单"""
    return ai_output.get("closed_elements", [])


def extract_ai_advantage_elements(ai_output: dict) -> List[dict]:
    """提取AI声称的AI优势元素（跨Case非相邻合并）"""
    return ai_output.get("ai_advantage_elements", [])


def verify_completeness(ai_output: dict) -> dict:
    """
    验证AI产出的完备性。

    返回审计报告dict。
    """
    # 1. 构造形式上下文
    fc_data = ai_output["formal_context"]
    fc = FormalContext(
        objects=fc_data["objects"],
        attributes=fc_data["attributes"],
        incidence=fc_data["incidence"]
    )

    # 2. 程序枚举所有闭元素
    print(f"形式上下文: {len(fc.objects)}个对象, {len(fc.attributes)}个属性")
    print("正在运行Next Closure算法枚举完全格...")

    all_closed = fc.enumerate_all_closed_elements()
    print(f"完全格B(G,M,I)共 {len(all_closed)} 个闭元素")

    # 3. 提取AI声称的闭元素
    ai_elements = extract_ai_closed_elements(ai_output)
    ai_advantage = extract_ai_advantage_elements(ai_output)

    # 把AI声称的闭元素转为(extent_frozenset)集合
    ai_extents = {}
    for elem in ai_elements:
        extent = frozenset(elem.get("extent", []))
        ai_extents[extent] = elem

    # AI优势元素也加入（这些是AI认为FCA不会找出但AI识别出的）
    ai_advantage_extents = {}
    for elem in ai_advantage:
        segments = frozenset(elem.get("segments", []))
        ai_advantage_extents[segments] = elem

    # 4. 对比
    program_extents = {ext for ext, _ in all_closed}

    # AI声称是闭元素的
    ai_claimed_closed = set()
    ai_claimed_not_closed = set()
    for extent, elem in ai_extents.items():
        if elem.get("is_closed", True):
            ai_claimed_closed.add(extent)
        else:
            ai_claimed_not_closed.add(extent)

    # 正确识别的闭元素：AI说是闭元素且程序也认为是
    correct = ai_claimed_closed & program_extents

    # 遗漏的闭元素：程序认为是闭元素但AI没有列出
    ai_all_listed = set(ai_extents.keys()) | set(ai_advantage_extents.keys())
    missed = program_extents - ai_all_listed

    # 错误的闭元素：AI说是闭元素但程序不认为是
    wrong = ai_claimed_closed - program_extents

    # 5. 构建审计报告
    report = {
        "formal_context_info": {
            "num_objects": len(fc.objects),
            "num_attributes": len(fc.attributes),
            "objects": fc.objects,
            "attributes": fc.attributes,
        },
        "total_closed_elements": len(all_closed),
        "ai_claimed_closed": len(ai_claimed_closed),
        "ai_claimed_not_closed": len(ai_claimed_not_closed),
        "ai_advantage_elements": len(ai_advantage),
        "correct_identified": len(correct),
        "missed_count": len(missed),
        "wrong_count": len(wrong),
        "completeness_score": len(correct) / len(all_closed) if all_closed else 0,
        "missed_elements": [],
        "wrong_elements": [],
        "ai_advantage_analysis": [],
    }

    # 遗漏的闭元素详情
    intent_map = {ext: intent for ext, intent in all_closed}
    for ext in missed:
        intent = intent_map[ext]
        report["missed_elements"].append({
            "extent": sorted(list(ext)),
            "intent": sorted(list(intent)),
            "size": len(ext),
        })

    # 按size排序遗漏的元素
    report["missed_elements"].sort(key=lambda x: x["size"])

    # 错误的闭元素详情
    for ext in wrong:
        elem = ai_extents.get(ext, {})
        actual_closure = fc.extent_closure(set(ext))
        report["wrong_elements"].append({
            "ai_extent": sorted(list(ext)),
            "ai_intent": elem.get("intent", []),
            "ai_verification": elem.get("closure_verification", ""),
            "actual_closure": sorted(list(actual_closure)),
            "problem": f"AI声称A''=A，但实际A''={sorted(list(actual_closure))}≠A",
        })

    # AI优势元素分析
    for ext, elem in ai_advantage_extents.items():
        is_actually_closed = ext in program_extents
        report["ai_advantage_analysis"].append({
            "segments": sorted(list(ext)),
            "description": elem.get("description", ""),
            "ai_reason": elem.get("reason", ""),
            "is_actually_closed_element": is_actually_closed,
            "verdict": "FCA确实不会找出（AI优势成立）" if not is_actually_closed
                       else "FCA实际上会找出（AI优势不成立——这个合并是闭元素）",
        })

    return report


def print_report(report: dict):
    """打印审计报告"""
    print("\n" + "=" * 70)
    print("完全格完备性审计报告")
    print("=" * 70)

    print(f"\n形式上下文: {report['formal_context_info']['num_objects']}个对象, "
          f"{report['formal_context_info']['num_attributes']}个属性")

    print(f"\n完全格B(G,M,I)共 {report['total_closed_elements']} 个闭元素")
    print(f"AI声称的闭元素: {report['ai_claimed_closed']} 个（其中正确: {report['correct_identified']}）")
    print(f"AI声称的非闭元素: {report['ai_claimed_not_closed']} 个")
    print(f"AI优势元素: {report['ai_advantage_elements']} 个")

    print(f"\n{'─' * 50}")
    print(f"正确识别: {report['correct_identified']} / {report['total_closed_elements']}")
    print(f"遗漏: {report['missed_count']}")
    print(f"错误: {report['wrong_count']}")
    print(f"完备性得分: {report['completeness_score']:.1%}")

    # 判定
    score = report['completeness_score']
    if score >= 0.6:
        verdict = "✅ 成功——完备性得分≥60%"
    elif score >= 0.3:
        verdict = "⚠️ 部分成功——完备性得分30%-60%"
    else:
        verdict = "❌ 失败——完备性得分<30%"
    print(f"判定: {verdict}")

    # 遗漏的闭元素
    if report['missed_elements']:
        print(f"\n{'─' * 50}")
        print(f"遗漏的闭元素（{report['missed_count']}个）:")
        for elem in report['missed_elements']:
            ext_str = ", ".join(elem['extent'])
            int_str = ", ".join(elem['intent'])
            print(f"  [{elem['size']}个段] A={{{ext_str}}}")
            print(f"           B={{{int_str}}}")

    # 错误的闭元素
    if report['wrong_elements']:
        print(f"\n{'─' * 50}")
        print(f"错误的闭元素（{report['wrong_count']}个）:")
        for elem in report['wrong_elements']:
            print(f"  AI声称: A={{{', '.join(elem['ai_extent'])}}}")
            print(f"  AI验证: {elem['ai_verification']}")
            print(f"  实际: A''={{{', '.join(elem['actual_closure'])}}}")
            print(f"  问题: {elem['problem']}")

    # AI优势元素分析
    if report['ai_advantage_analysis']:
        print(f"\n{'─' * 50}")
        print(f"AI优势元素分析（{len(report['ai_advantage_analysis'])}个）:")
        for elem in report['ai_advantage_analysis']:
            print(f"  段: {{{', '.join(elem['segments'])}}}")
            print(f"  描述: {elem['description']}")
            print(f"  AI理由: {elem['ai_reason']}")
            print(f"  程序验证: {elem['verdict']}")

    print("\n" + "=" * 70)


def main():
    if len(sys.argv) < 2:
        print("用法: python3 verify_lattice_completeness.py <ai_output.json>")
        print("      python3 verify_lattice_completeness.py <ai_output.json> --report <report.json>")
        sys.exit(1)

    ai_output_path = sys.argv[1]
    report_path = None
    if len(sys.argv) >= 4 and sys.argv[2] == "--report":
        report_path = sys.argv[3]

    # 加载AI输出
    print(f"加载AI输出: {ai_output_path}")
    ai_output = load_ai_output(ai_output_path)

    # 验证完备性
    report = verify_completeness(ai_output)

    # 打印报告
    print_report(report)

    # 可选：保存报告
    if report_path:
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"审计报告已保存到: {report_path}")


if __name__ == "__main__":
    main()
