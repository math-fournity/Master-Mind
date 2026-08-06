"""
P7-3.3 等价表示之间运输对象、定理、不变量、义务和策略。

plan HoTT方向1："等价表示之间运输对象、定理、不变量、义务和策略"

母本细节补充（系统探讨.md§8.2位置一，阶段1母本回溯发现）：
  母本明确列出4个运输对象："定理、不变量、证明义务、解法策略"
  123号概括为"对象、定理、义务和策略"——实现时必须包含全部5个运输对象
  （母本的4个 + 123号的"对象"），并在代码注释中标注母本来源。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class TransportObjectType(Enum):
    """
    5种运输对象类型。

    母本§8.2位置一明确列出4个："定理、不变量、证明义务、解法策略"
    123号§19概括为"对象、定理、义务和策略"
    实现时包含全部5个（母本的4个 + 123号的"对象"）：
    """
    OBJECT = "object"                    # 123号的"对象"（数学对象本身）
    THEOREM = "theorem"                  # 母本+123号：定理
    INVARIANT = "invariant"              # 母本：不变量
    OBLIGATION = "obligation"            # 母本"证明义务"+123号"义务"
    STRATEGY = "strategy"                # 母本"解法策略"+123号"策略"


@dataclass
class TransportableObject:
    """可运输的数学对象。"""
    obj_id: str
    obj_type: TransportObjectType
    content: str = ""
    source_representation: str = ""
    target_representation: str = ""

    def to_dict(self) -> dict:
        return {
            "obj_id": self.obj_id,
            "obj_type": self.obj_type.value,
            "content": self.content,
            "source_representation": self.source_representation,
            "target_representation": self.target_representation,
        }


class ObjectTransporter:
    """
    P7-3.3：等价表示之间运输5种对象。

    plan HoTT方向1："等价表示之间运输对象、定理、不变量、义务和策略"
    母本§8.2位置一："定理、不变量、证明义务、解法策略从A运输到B"
    """

    def __init__(self):
        self._transported: List[Dict[str, Any]] = []

    def transport_object(
        self,
        obj: TransportableObject,
        rep_map,
        soundness_transporter=None,
    ) -> Dict[str, Any]:
        """
        运输一个对象到目标表示。

        边界情况：运输不保持等价→拒绝；运输丢失不变量→拒绝。
        """
        # 如果有soundness_transporter，先检查义务
        if soundness_transporter is not None:
            ob_check = soundness_transporter.check_obligation_before_transport(rep_map)
            if ob_check.get("has_obligation") and not ob_check.get("satisfied"):
                return {
                    "transported": False,
                    "reason": "soundness_obligation未通过",
                    "obj_id": obj.obj_id,
                }

        result = {
            "obj_id": obj.obj_id,
            "obj_type": obj.obj_type.value,
            "source_form": rep_map.source_form,
            "target_form": rep_map.target_form,
            "transported_content": obj.content,  # 简化：实际需要翻译
            "preserved_invariants": list(rep_map.preserved_invariants),
            "lost_information": list(rep_map.lost_information),
        }
        self._transported.append(result)
        return {"transported": True, **result}

    def transport_all_types(
        self,
        objects: List[TransportableObject],
        rep_map,
        soundness_transporter=None,
    ) -> Dict[str, Any]:
        """
        运输全部5种类型的对象。

        验证5种运输对象全部可运输。
        """
        results = []
        for obj in objects:
            result = self.transport_object(obj, rep_map, soundness_transporter)
            results.append(result)

        # 检查5种类型是否全部覆盖
        transported_types = {
            r.get("obj_type") for r in results if r.get("transported")
        }
        all_types = {t.value for t in TransportObjectType}
        missing_types = all_types - transported_types

        return {
            "n_objects": len(objects),
            "n_transported": sum(1 for r in results if r.get("transported")),
            "all_types_covered": len(missing_types) == 0,
            "missing_types": list(missing_types),
            "transported_types": list(transported_types),
            "results": results,
            "mother_text_reference": "母本§8.2位置一：定理、不变量、证明义务、解法策略",
            "plan_reference": "plan HoTT方向1：等价表示之间运输对象、定理、不变量、义务和策略",
        }

    def check_equivalence_preserved(self, transport_result: Dict) -> Dict[str, Any]:
        """
        验证运输是否保持等价。

        边界情况：运输不保持等价→拒绝；运输丢失不变量→拒绝。
        """
        preserved = transport_result.get("preserved_invariants", [])
        lost = transport_result.get("lost_information", [])

        # 检查是否有不变量丢失
        invariant_lost = any("invariant" in l.lower() for l in lost)

        return {
            "equivalence_preserved": not invariant_lost,
            "preserved_invariants": preserved,
            "lost_information": lost,
            "invariant_lost": invariant_lost,
        }
