"""
P7-7.1/P7-7.1b TDA数据充分性4限定词检查。

plan行220："持久同调：探索对噪声稳定的轨迹形状特征"
123号§20："只有定义状态空间、邻接、尺度和等价关系后，才可以研究持久同调或层上同调障碍。"

多限定词检查（162号v4维度19扩展修正）：
  §20要求4个限定词"状态空间、邻接、尺度、等价关系"，
  代码必须同时检查4个限定词（has_state_space AND has_adjacency AND has_scale
  AND has_equivalence_relation），不能只检查部分。

强制机制（162号v4维度21预检修正）：
  只满足部分限定词时→抛InsufficientFormalizationError并报告哪些未满足。
"""

from typing import Dict, Any, List


class InsufficientFormalizationError(Exception):
    """
    P7-7.COMP/P7-8.1b强制机制：限定词未全部满足时→抛InsufficientFormalizationError。

    不只是返回False声明——是运行时强制阻断。
    """


class TDAGate:
    """
    P7-7.1/P7-7.1b：TDA数据充分性4限定词检查。

    123号§20："只有定义状态空间、邻接、尺度和等价关系后，才可以研究持久同调。"
    """

    REQUIRED_QUALIFIERS = ["state_space", "adjacency", "scale", "equivalence_relation"]

    def __init__(self):
        self._qualifiers: Dict[str, bool] = {
            "state_space": False,
            "adjacency": False,
            "scale": False,
            "equivalence_relation": False,
        }

    def set_state_space(self, defined: bool) -> None:
        self._qualifiers["state_space"] = defined

    def set_adjacency(self, defined: bool) -> None:
        self._qualifiers["adjacency"] = defined

    def set_scale(self, defined: bool) -> None:
        self._qualifiers["scale"] = defined

    def set_equivalence_relation(self, defined: bool) -> None:
        self._qualifiers["equivalence_relation"] = defined

    def check_all_qualifiers(self) -> Dict[str, Any]:
        """
        检查4个限定词是否全部满足。

        多限定词检查（162号v4维度19扩展）：
        必须同时检查4个限定词，不能只检查部分。
        """
        satisfied = [q for q, v in self._qualifiers.items() if v]
        unsatisfied = [q for q, v in self._qualifiers.items() if not v]

        return {
            "n_qualifiers_required": 4,
            "n_qualifiers_satisfied": len(satisfied),
            "satisfied": satisfied,
            "unsatisfied": unsatisfied,
            "all_satisfied": len(unsatisfied) == 0,
        }

    def assert_can_do_tda(self) -> Dict[str, Any]:
        """
        断言可以做TDA——4限定词未全部满足时抛InsufficientFormalizationError。

        强制机制（162号v4维度21预检修正）：
        只满足部分限定词时→抛InsufficientFormalizationError并报告哪些未满足。

        边界情况：
        - 只满足3个限定词→拒绝
        - 只满足2个限定词→拒绝
        - 只满足1个限定词→拒绝
        - 0个限定词满足→拒绝
        """
        check = self.check_all_qualifiers()

        if not check["all_satisfied"]:
            raise InsufficientFormalizationError(
                f"TDA数据充分性不足：123号§20要求4个限定词全部满足。"
                f"当前只满足{check['n_qualifiers_satisfied']}/4个限定词。"
                f"未满足的限定词: {check['unsatisfied']}。"
                f"只有定义状态空间、邻接、尺度和等价关系后，才可以研究持久同调。"
            )

        return {
            "can_do_tda": True,
            "qualifiers_checked": 4,
            "qualifiers_satisfied": 4,
            "check": check,
        }

    def check_partial_qualifiers(self) -> Dict[str, Any]:
        """
        检查部分限定词满足的情况——用于诊断。

        边界情况：只满足部分限定词时报告哪些未满足。
        """
        check = self.check_all_qualifiers()
        return {
            "partial_satisfaction": not check["all_satisfied"],
            "n_satisfied": check["n_qualifiers_satisfied"],
            "unsatisfied": check["unsatisfied"],
            "needs_more_formalization": len(check["unsatisfied"]) > 0,
        }
