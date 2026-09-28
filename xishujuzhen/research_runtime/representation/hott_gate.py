"""
P7-8.1/P7-8.1b HoTT形式对象充分性3限定词检查。

plan行228："只有当状态空间、等价关系和证明表示被形式化后，才讨论同伦类。"

多限定词检查（162号v4维度19扩展修正）：
  plan行228要求3个限定词"状态空间、等价关系、证明表示"，
  代码必须同时检查3个限定词（has_state_space AND has_equivalence_relation
  AND has_proof_representation），不能只检查部分。

强制机制：
  只满足部分限定词时→抛InsufficientFormalizationError。
"""

from typing import Dict, Any, List
from .tda_gate import InsufficientFormalizationError


class HoTTGate:
    """
    P7-8.1/P7-8.1b：HoTT形式对象充分性3限定词检查。

    plan行228："只有当状态空间、等价关系和证明表示被形式化后，才讨论同伦类。"
    """

    REQUIRED_QUALIFIERS = ["state_space", "equivalence_relation", "proof_representation"]

    def __init__(self):
        self._qualifiers: Dict[str, bool] = {
            "state_space": False,
            "equivalence_relation": False,
            "proof_representation": False,
        }

    def set_state_space(self, defined: bool) -> None:
        self._qualifiers["state_space"] = defined

    def set_equivalence_relation(self, defined: bool) -> None:
        self._qualifiers["equivalence_relation"] = defined

    def set_proof_representation(self, defined: bool) -> None:
        self._qualifiers["proof_representation"] = defined

    def check_all_qualifiers(self) -> Dict[str, Any]:
        """
        检查3个限定词是否全部满足。

        多限定词检查（162号v4维度19扩展）：
        必须同时检查3个限定词，不能只检查部分。
        """
        satisfied = [q for q, v in self._qualifiers.items() if v]
        unsatisfied = [q for q, v in self._qualifiers.items() if not v]

        return {
            "n_qualifiers_required": 3,
            "n_qualifiers_satisfied": len(satisfied),
            "satisfied": satisfied,
            "unsatisfied": unsatisfied,
            "all_satisfied": len(unsatisfied) == 0,
        }

    def assert_can_research_hott(self) -> Dict[str, Any]:
        """
        断言可以研究HoTT——3限定词未全部满足时抛InsufficientFormalizationError。

        强制机制：只满足部分限定词时→抛InsufficientFormalizationError。

        边界情况：
        - 只满足2个限定词→拒绝
        - 只满足1个限定词→拒绝
        - 0个限定词满足→拒绝
        """
        check = self.check_all_qualifiers()

        if not check["all_satisfied"]:
            raise InsufficientFormalizationError(
                f"HoTT形式对象充分性不足：plan行228要求3个限定词全部满足。"
                f"当前只满足{check['n_qualifiers_satisfied']}/3个限定词。"
                f"未满足的限定词: {check['unsatisfied']}。"
                f"只有当状态空间、等价关系和证明表示被形式化后，才讨论同伦类。"
            )

        return {
            "can_research_hott": True,
            "qualifiers_checked": 3,
            "qualifiers_satisfied": 3,
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
