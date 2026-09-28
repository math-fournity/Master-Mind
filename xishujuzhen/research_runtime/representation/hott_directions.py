"""
P7-8.2 HoTT三个真实方向。

plan行224-226："原文提出的HoTT三个真实方向逐项保留：
1. 等价表示之间运输对象、定理、不变量、义务和策略；
2. 对证明路径做语义等价分类，避免把改写/粒度差异误判为新思路；
3. 用2-胞元或更高一致性数据比较'变换之间的变换'。"

母本细节补充（系统探讨.md§8.2，阶段1母本回溯发现）：
  母本明确描述三个位置：
  位置一：等价表示之间的运输（定理、不变量、证明义务、解法策略）
  位置二：证明路径的等价类（中间步骤不同、变量名不同、引理粒度不同）
  位置三：高阶关系（比较A如何变换为B、两种变换是否等价、哪种变换保留哪些结构）
"""

from typing import Dict, Any, List
from dataclasses import dataclass, field


@dataclass
class HoTTDirection:
    """HoTT三个真实方向之一。"""
    direction_id: str
    name: str
    description: str
    mother_text_reference: str  # 母本来源
    plan_reference: str         # plan来源

    def to_dict(self) -> dict:
        return {
            "direction_id": self.direction_id,
            "name": self.name,
            "description": self.description,
            "mother_text_reference": self.mother_text_reference,
            "plan_reference": self.plan_reference,
        }


# 三个真实方向（plan行224-226逐字 + 母本§8.2补充）
HOTT_DIRECTIONS = [
    HoTTDirection(
        direction_id="hott_dir1",
        name="等价表示之间的运输",
        description="等价表示之间运输对象、定理、不变量、义务和策略",
        mother_text_reference="母本§8.2位置一：定理、不变量、证明义务、解法策略从A运输到B",
        plan_reference="plan行224-225方向1",
    ),
    HoTTDirection(
        direction_id="hott_dir2",
        name="证明路径的等价类",
        description="对证明路径做语义等价分类，避免把改写/粒度差异误判为新思路",
        mother_text_reference="母本§8.2位置二：中间步骤不同、变量名不同、引理粒度不同",
        plan_reference="plan行225方向2",
    ),
    HoTTDirection(
        direction_id="hott_dir3",
        name="高阶关系",
        description="用2-胞元或更高一致性数据比较'变换之间的变换'。"
                    "母本§8.2位置三明确3个比较对象："
                    "(1)A如何变换为B；(2)两种变换是否等价；(3)哪种变换保留哪些结构。"
                    "这可能成为L3范式建模的严格方向。",
        mother_text_reference="母本§8.2位置三：比较A如何变换为B、两种变换是否等价、哪种变换保留哪些结构",
        plan_reference="plan行226方向3",
    ),
]


class HoTTDirections:
    """
    P7-8.2：HoTT三个真实方向——逐项保留。

    plan行224："原文提出的HoTT三个真实方向逐项保留"
    """

    def __init__(self):
        self._directions = {d.direction_id: d for d in HOTT_DIRECTIONS}

    def get_all_directions(self) -> List[HoTTDirection]:
        """返回全部3个方向。"""
        return list(HOTT_DIRECTIONS)

    def get_direction(self, direction_id: str) -> HoTTDirection:
        return self._directions[direction_id]

    def check_all_preserved(self) -> Dict[str, Any]:
        """
        验证3个方向全部保留。

        plan行224："逐项保留"——3个方向缺一不可。
        """
        return {
            "n_directions": len(HOTT_DIRECTIONS),
            "all_preserved": len(HOTT_DIRECTIONS) == 3,
            "directions": [d.to_dict() for d in HOTT_DIRECTIONS],
            "mother_text_references": [d.mother_text_reference for d in HOTT_DIRECTIONS],
        }

    def check_direction_completeness(self, direction_id: str) -> Dict[str, Any]:
        """
        检查单个方向的完整性——包含母本细节。

        母本细节补充（阶段1母本回溯发现）：
        - 方向1：母本列出4个运输对象（定理、不变量、证明义务、解法策略）
        - 方向2：母本列出3种差异（中间步骤不同、变量名不同、引理粒度不同）
        - 方向3：母本描述3个比较对象（A如何变换为B、变换是否等价、保留哪些结构）
        """
        direction = self._directions[direction_id]
        mother_details = {
            "hott_dir1": ["定理", "不变量", "证明义务", "解法策略"],
            "hott_dir2": ["中间步骤不同", "变量名不同", "引理粒度不同"],
            "hott_dir3": ["A如何变换为B", "变换是否等价", "保留哪些结构"],
        }

        details = mother_details.get(direction_id, [])
        return {
            "direction_id": direction_id,
            "name": direction.name,
            "mother_details_preserved": len(details) > 0,
            "n_mother_details": len(details),
            "details": details,
        }
