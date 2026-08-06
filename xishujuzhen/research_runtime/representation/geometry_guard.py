"""
P7-6.COMP 几何方法用途限制——几何相近不等于数学等价。

123号§26："这些方法只用于对齐、聚类和候选检索。
几何相近不等于数学等价，更不等于同一个Hint具有因果效果。"

强制机制：
  几何方法被用于数学等价判定时→抛GeometryMisuseError。
  几何方法的用途标注必须为"对齐/聚类/候选检索"之一。
"""

from typing import Dict, Any, List, Optional
from enum import Enum


class GeometryMisuseError(Exception):
    """
    P7-6.COMP强制机制：几何方法用于数学等价判定→抛GeometryMisuseError。

    不只是返回False声明——是运行时强制阻断。
    """


class GeometryPurpose(Enum):
    """几何方法的合法用途（123号§26）。"""
    ALIGNMENT = "alignment"        # 对齐
    CLUSTERING = "clustering"      # 聚类
    CANDIDATE_RETRIEVAL = "candidate_retrieval"  # 候选检索


class GeometryGuard:
    """
    P7-6.COMP：几何方法用途限制。

    123号§26："这些方法只用于对齐、聚类和候选检索。"
    """

    LEGITIMATE_PURPOSES = {p.value for p in GeometryPurpose}

    def check_purpose(self, purpose: str) -> Dict[str, Any]:
        """
        检查几何方法的使用目的是否合法。

        边界情况：几何方法被用于数学等价判定→拒绝。
        """
        if purpose not in self.LEGITIMATE_PURPOSES:
            return {
                "legitimate": False,
                "purpose": purpose,
                "legitimate_purposes": list(self.LEGITIMATE_PURPOSES),
                "reason": f"几何方法只能用于{list(self.LEGITIMATE_PURPOSES)}，不能用于'{purpose}'",
            }

        return {
            "legitimate": True,
            "purpose": purpose,
        }

    def assert_not_math_equivalence(self, purpose: str) -> Dict[str, Any]:
        """
        断言几何方法不用于数学等价判定。

        强制机制：几何方法被用于数学等价判定时→抛GeometryMisuseError。
        """
        illegitimate = ["math_equivalence", "proof_verification", "theorem_validation"]
        if purpose in illegitimate:
            raise GeometryMisuseError(
                f"几何方法不能用于'{purpose}'。"
                f"123号§26：几何相近不等于数学等价，更不等于同一个Hint具有因果效果。"
                f"几何方法只能用于{list(self.LEGITIMATE_PURPOSES)}。"
            )

        return {
            "purpose_legitimate": True,
            "purpose": purpose,
            "not_math_equivalence": True,
        }

    def check_geometry_distance_not_causality(
        self,
        geometry_distance: float,
        threshold: float = 0.01,
    ) -> Dict[str, Any]:
        """
        验证几何距离不直接裁决数学等价或因果启发。

        123号§26："几何相近不等于数学等价，更不等于同一个Hint具有因果效果。"
        """
        return {
            "geometry_close": geometry_distance < threshold,
            "math_equivalence": "unknown",  # 几何相近不蕴含数学等价
            "hint_causality": "unknown",    # 几何相近不蕴含Hint因果效果
            "requires_causal_validation": True,  # 需要因果干预验证
            "warning": "几何相近不等于数学等价，更不等于同一个Hint具有因果效果",
        }

    def assert_purpose_legitimate(self, purpose: str) -> Dict[str, Any]:
        """
        断言几何方法的用途合法——不合法时抛GeometryMisuseError。

        强制机制：几何方法的用途标注必须为"对齐/聚类/候选检索"之一。
        """
        check = self.check_purpose(purpose)
        if not check["legitimate"]:
            raise GeometryMisuseError(
                f"几何方法用途不合法：'{purpose}'。"
                f"合法用途为{list(self.LEGITIMATE_PURPOSES)}。"
            )

        return {"purpose_legitimate": True, "purpose": purpose}
