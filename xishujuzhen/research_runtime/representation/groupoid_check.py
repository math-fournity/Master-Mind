"""
P7-1.COMP3 groupoid条件检查——只有可逆且复合封闭的子图才可称为groupoid。

127号§5冻结声明3："只有可逆且复合封闭的子图才可称为groupoid。"

多限定词检查（162号v4维度19扩展修正）：
  §5要求"可逆**且**复合封闭"——有2个限定词"可逆"和"复合封闭"，
  代码必须同时检查2个限定词（is_invertible(subgraph) AND is_composition_closed(subgraph)），
  不能只检查其中一个。

强制机制（162号v4维度21预检修正）：
  不满足2个限定词的子图被称为groupoid时→抛GroupoidViolationError。
"""

from typing import Dict, Any, List, Set, Tuple


class GroupoidViolationError(Exception):
    """
    P7-1.COMP3强制机制：不满足2个限定词的子图被称为groupoid→抛GroupoidViolationError。

    不只是返回False声明——是运行时强制阻断。
    """


class GroupoidChecker:
    """
    P7-1.COMP3：groupoid条件检查器。

    2个限定词必须同时满足：
    1. 可逆（is_invertible）：子图中每条边都有逆边
    2. 复合封闭（is_composition_closed）：子图中边的复合仍在子图中
    """

    def is_invertible(self, edges: List[Tuple[str, str, str]]) -> bool:
        """
        检查子图是否可逆——每条边都有逆边。

        edges是(source, target, edge_id)的列表。
        """
        edge_set = {(s, t) for s, t, _ in edges}
        for s, t, _ in edges:
            if (t, s) not in edge_set:
                return False
        return True

    def is_composition_closed(
        self,
        edges: List[Tuple[str, str, str]],
        compositions: List[Tuple[str, str, str, str, str]] = None,
    ) -> bool:
        """
        检查子图是否复合封闭——边的复合仍在子图中。

        compositions是(source1, target1, source2, target2, composite_target)的列表，
        表示target1==source2时存在复合边(source1, composite_target)。

        如果compositions为None，检查所有可能的复合。
        """
        edge_set = {(s, t) for s, t, _ in edges}
        nodes = set()
        for s, t, _ in edges:
            nodes.add(s)
            nodes.add(t)

        # 检查所有可能的复合：如果A→B和B→C存在，A→C也应存在
        for s1, t1, _ in edges:
            for s2, t2, _ in edges:
                if t1 == s2:
                    # 存在复合A→C
                    if (s1, t2) not in edge_set:
                        return False
        return True

    def check_groupoid(self, edges: List[Tuple[str, str, str]]) -> Dict[str, Any]:
        """
        检查子图是否满足groupoid的2个限定词。

        多限定词检查（162号v4维度19扩展）：
        必须同时检查"可逆"和"复合封闭"2个限定词。
        """
        invertible = self.is_invertible(edges)
        closed = self.is_composition_closed(edges)

        return {
            "is_invertible": invertible,
            "is_composition_closed": closed,
            "both_satisfied": invertible and closed,
            "n_qualifiers_satisfied": int(invertible) + int(closed),
            "n_qualifiers_required": 2,
        }

    def assert_groupoid(self, edges: List[Tuple[str, str, str]]) -> Dict[str, Any]:
        """
        断言子图是groupoid——不满足2个限定词时抛GroupoidViolationError。

        强制机制（162号v4维度21预检修正）：
        不只是返回False声明——是运行时强制阻断。

        边界情况：
        - 不可逆但复合封闭→拒绝（只满足1个限定词）
        - 可逆但不复合封闭→拒绝（只满足1个限定词）
        - 两者都不满足→拒绝（0个限定词满足）
        """
        check = self.check_groupoid(edges)

        if not check["both_satisfied"]:
            satisfied = []
            if check["is_invertible"]:
                satisfied.append("可逆")
            if check["is_composition_closed"]:
                satisfied.append("复合封闭")

            raise GroupoidViolationError(
                f"子图不满足groupoid条件：127号§5要求'可逆**且**复合封闭'（2个限定词）。"
                f"当前只满足{len(satisfied)}个限定词: {satisfied}。"
                f"需要同时满足2个限定词。"
            )

        return {
            "is_groupoid": True,
            "qualifiers_checked": 2,
            "qualifiers_satisfied": 2,
            "check": check,
        }

    def check_not_category(self) -> Dict[str, Any]:
        """
        P7-1.COMP2：首版不宣称已构成范畴。

        127号§5："首版不宣称已构成范畴——升级为真正范畴需另给恒等变换、
        可组合边的复合、结合律和结构保持证明。"
        """
        return {
            "is_category": False,
            "first_version_declaration": "首版不宣称已构成范畴",
            "upgrade_requirements": [
                "恒等变换",
                "可组合边的复合",
                "结合律",
                "结构保持证明",
            ],
        }
