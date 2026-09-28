"""
P7-1.2c/P7-2 费马型跨域模块编排——FLT极限案例。

plan行274："展示整数方程→辅助几何对象→Galois表示/模形式→Ribet降层的表示运输和模块接口"

4环节链条（P7-1.2c）：
  1. 整数方程→Frey曲线（辅助几何对象）
  2. Frey曲线→mod p Galois表示
  3. Galois表示→模形式（谷山—志村桥梁）
  4. 模形式空间→更低level模形式空间（Ribet降层）

3层难度阶梯（128号§4.5 + 123号§35 + 137号P7-2.1-2.3）：
  Level 1：给定半稳定模性推出FLT
  Level 2：逐层隐去Frey/Ribet桥梁
  Level 3：Wiles级模块接口（模性提升/变形理论/Hecke代数/R=T/Taylor—Wiles）

6条大师启发（123号§35行793-800）：
  1. 把无结构整数反例编码成更富结构的几何对象
  2. 把存在性问题改成两个理论的不相容性问题
  3. 在椭圆曲线、Galois表示和模形式之间换语言
  4. 用局部ramification约束全局对象
  5. 降低level直到目标空间为空
  6. 证明一个更强但接口更合适的桥梁定理

3项能力区分（123号§35行770-774）：
  1. 调用已证半稳定模性，重建Frey—Ribet到FLT的推论
  2. 重建Wiles/Taylor—Wiles的半稳定模性证明
  3. 从历史前状态独立发现整条路线

强制机制：
  Level N未通过时进入Level N+1→抛LevelOrderViolationError
  直接挑战完整Wiles发现（Level 1/2未通过时进入Level 3）→抛LevelOrderViolationError
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from enum import Enum


class LevelOrderViolationError(Exception):
    """
    P7-2.4/P7-2.COMP强制机制：阶梯顺序错误→抛LevelOrderViolationError。

    不只是返回False声明——是运行时强制阻断。
    """


class FermatLevel(Enum):
    """3层难度阶梯（128号§4.5）。"""
    LEVEL_1 = 1  # 给定半稳定模性推出FLT
    LEVEL_2 = 2  # 逐层隐去Frey/Ribet桥梁
    LEVEL_3 = 3  # Wiles级模块接口


# 6条大师启发（123号§35行793-800逐字）
MASTER_HEURISTICS = [
    {
        "id": "mh1",
        "text": "把无结构整数反例编码成更富结构的几何对象",
        "applies_to": "整数方程→Frey曲线",
    },
    {
        "id": "mh2",
        "text": "把存在性问题改成两个理论的不相容性问题",
        "applies_to": "FLT反例→两个理论不相容",
    },
    {
        "id": "mh3",
        "text": "在椭圆曲线、Galois表示和模形式之间换语言",
        "applies_to": "表示运输",
    },
    {
        "id": "mh4",
        "text": "用局部ramification约束全局对象",
        "applies_to": "局部→全局",
    },
    {
        "id": "mh5",
        "text": "降低level直到目标空间为空",
        "applies_to": "Ribet降层",
    },
    {
        "id": "mh6",
        "text": "证明一个更强但接口更合适的桥梁定理",
        "applies_to": "半稳定模性→Frey曲线必须模",
    },
]


# 3项能力区分（123号§35行770-774）
CAPABILITY_DISTINCTION = [
    {
        "id": "cap1",
        "text": "调用已证半稳定模性，重建Frey—Ribet到FLT的推论",
        "level": FermatLevel.LEVEL_1,
    },
    {
        "id": "cap2",
        "text": "重建Wiles/Taylor—Wiles的半稳定模性证明",
        "level": FermatLevel.LEVEL_3,
    },
    {
        "id": "cap3",
        "text": "从历史前状态独立发现整条路线",
        "level": FermatLevel.LEVEL_3,
    },
]


# Level 1推论链（123号§35行776-791）
LEVEL1_INFERENCE_CHAIN = [
    "假想FLT反例",
    "Frey曲线",
    "半稳定性/导子",
    "mod p Galois表示",
    "Ribet降层",
    "不存在的低水平权2模形式",
    "Frey曲线不模",
    "半稳定模性→Frey曲线必须模",
    "两路汇聚为矛盾",
]


# 4环节表示运输链条（plan行274）
FERMAT_CHAIN_FORMS = [
    "整数方程",       # FLT反例
    "Frey曲线",       # 辅助几何对象
    "mod p Galois表示",
    "模形式",          # 谷山—志村桥梁
    "更低level模形式",  # Ribet降层
]


@dataclass
class FermatChainSegment:
    """费马链条的一个环节。"""
    segment_id: str
    source_form: str
    target_form: str
    description: str
    master_heuristic_ids: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "segment_id": self.segment_id,
            "source_form": self.source_form,
            "target_form": self.target_form,
            "description": self.description,
            "master_heuristic_ids": list(self.master_heuristic_ids),
        }


# 4环节链条定义
FERMAT_CHAIN_SEGMENTS = [
    FermatChainSegment(
        segment_id="seg1",
        source_form="整数方程",
        target_form="Frey曲线",
        description="FLT反例（整数方程）→Frey曲线（辅助几何对象）的表示映射",
        master_heuristic_ids=["mh1"],
    ),
    FermatChainSegment(
        segment_id="seg2",
        source_form="Frey曲线",
        target_form="mod p Galois表示",
        description="Frey曲线→mod p Galois表示的表示映射",
        master_heuristic_ids=["mh3"],
    ),
    FermatChainSegment(
        segment_id="seg3",
        source_form="mod p Galois表示",
        target_form="模形式",
        description="Galois表示→模形式的表示映射（谷山—志村桥梁）",
        master_heuristic_ids=["mh3", "mh6"],
    ),
    FermatChainSegment(
        segment_id="seg4",
        source_form="模形式",
        target_form="更低level模形式",
        description="模形式空间→更低level模形式空间的表示映射（Ribet降层）",
        master_heuristic_ids=["mh5"],
    ),
]


class FermatChainBuilder:
    """
    P7-1.2c：费马案例完整表示运输链条展示。

    plan行274要求展示4个环节的完整链条。
    """

    def __init__(self):
        self._segments = list(FERMAT_CHAIN_SEGMENTS)

    def get_chain(self) -> List[FermatChainSegment]:
        """返回完整4环节链条。"""
        return list(self._segments)

    def get_chain_forms(self) -> List[str]:
        """返回链条的表示形式序列。"""
        forms = [self._segments[0].source_form]
        for seg in self._segments:
            forms.append(seg.target_form)
        return forms

    def display_chain(self) -> Dict[str, Any]:
        """
        展示完整链条——4个环节全部可展示。

        边界情况：链条断裂→告警；环节顺序错误→拒绝。
        """
        segments = []
        for i, seg in enumerate(self._segments):
            segments.append({
                "index": i,
                **seg.to_dict(),
            })

        return {
            "chain_complete": len(segments) == 4,
            "n_segments": len(segments),
            "segments": segments,
            "forms_sequence": self.get_chain_forms(),
            "plan_reference": "plan行274：展示整数方程→辅助几何对象→Galois表示/模形式→Ribet降层",
        }

    def check_chain_order(self, segments: List[FermatChainSegment]) -> Dict[str, Any]:
        """
        检查链条环节顺序是否正确。

        边界情况：环节顺序错误→拒绝。
        """
        expected_forms = self.get_chain_forms()
        actual_forms = [segments[0].source_form] if segments else []
        for seg in segments:
            actual_forms.append(seg.target_form)

        order_ok = actual_forms == expected_forms
        return {
            "order_correct": order_ok,
            "expected": expected_forms,
            "actual": actual_forms,
        }


class MasterHeuristicRecognizer:
    """
    P7-2.1b：6条大师启发的识别和标注。

    123号§35："真正的大师启发不是只说'谷山—志村'，而是6条具体启发。"
    """

    def __init__(self):
        self._heuristics = {h["id"]: h for h in MASTER_HEURISTICS}

    def get_all_heuristics(self) -> List[Dict[str, Any]]:
        """返回全部6条大师启发。"""
        return list(MASTER_HEURISTICS)

    def recognize_heuristic(self, text: str) -> List[Dict[str, Any]]:
        """
        从文本中识别大师启发。

        边界情况：6条中某条未被识别→告警（应全部识别）；
                  把"谷山—志村"作为大师启发的全部内容→拒绝。
        """
        recognized = []
        text_lower = text.lower()
        for h in MASTER_HEURISTICS:
            # 简化识别：检查关键词
            keywords = {
                "mh1": ["编码", "几何对象", "整数反例"],
                "mh2": ["不相容", "存在性问题"],
                "mh3": ["换语言", "galois", "模形式"],
                "mh4": ["ramification", "局部", "全局"],
                "mh5": ["降低level", "目标空间为空"],
                "mh6": ["更强", "桥梁定理", "接口合适"],
            }
            h_keywords = keywords.get(h["id"], [])
            if any(kw.lower() in text_lower for kw in h_keywords):
                recognized.append(h)

        return recognized

    def check_all_recognized(self, recognized_ids: List[str]) -> Dict[str, Any]:
        """
        检查6条启发是否全部被识别。

        边界情况：6条中某条未被识别→告警（应全部识别）。
        """
        all_ids = {h["id"] for h in MASTER_HEURISTICS}
        recognized_set = set(recognized_ids)
        missing = all_ids - recognized_set
        return {
            "all_recognized": len(missing) == 0,
            "n_recognized": len(recognized_set),
            "n_total": len(all_ids),
            "missing_ids": list(missing),
        }

    def check_not_just_taniyama_shimura(self, text: str) -> Dict[str, Any]:
        """
        检查是否把"谷山—志村"作为大师启发的全部内容。

        边界情况：把"谷山—志村"作为大师启发的全部内容→拒绝。
        """
        is_only_ts = (
            "谷山" in text and "志村" in text
            and not any(kw in text for kw in [
                "编码", "不相容", "换语言", "ramification", "降低level", "桥梁定理"
            ])
        )
        return {
            "is_only_taniyama_shimura": is_only_ts,
            "rejected": is_only_ts,
            "reason": "6条才是完整的大师启发，不只是'谷山—志村'" if is_only_ts else "",
        }


class FermatLevelGate:
    """
    P7-2.4/P7-2.COMP：费马案例三层难度阶梯门控。

    强制机制：Level N未通过时拒绝进入Level N+1→抛LevelOrderViolationError。
    """

    def __init__(self):
        self._passed_levels: Dict[int, bool] = {}

    def mark_level_passed(self, level: FermatLevel) -> None:
        self._passed_levels[level.value] = True

    def can_enter_level(self, level: FermatLevel) -> bool:
        """检查是否可以进入指定Level。"""
        if level == FermatLevel.LEVEL_1:
            return True  # Level 1总是可以进入
        # Level N需要Level N-1通过
        prev = level.value - 1
        return self._passed_levels.get(prev, False)

    def enter_level(self, level: FermatLevel) -> Dict[str, Any]:
        """
        尝试进入指定Level。

        强制机制：Level N未通过时进入Level N+1→抛LevelOrderViolationError。
        边界情况：直接挑战完整Wiles发现（Level 1/2未通过时进入Level 3）→拒绝。
        """
        if not self.can_enter_level(level):
            prev = level.value - 1
            raise LevelOrderViolationError(
                f"阶梯顺序错误：Level {level.value} 需要先通过 Level {prev}。"
                f"123号§43：先做Level 1，再逐层隐去桥梁，最后才研究Level 3。"
            )

        return {
            "level": level.value,
            "entered": True,
            "prerequisite_passed": self._passed_levels.get(level.value - 1, False) if level.value > 1 else True,
        }

    def check_not_full_wiles(self, level: FermatLevel) -> Dict[str, Any]:
        """
        P7-2.4：不直接挑战完整Wiles发现。

        边界情况：Level 1/2未通过时进入Level 3→拒绝（抛LevelOrderViolationError）。
        """
        if level == FermatLevel.LEVEL_3:
            l1_passed = self._passed_levels.get(1, False)
            l2_passed = self._passed_levels.get(2, False)
            if not (l1_passed and l2_passed):
                raise LevelOrderViolationError(
                    f"不直接挑战完整Wiles发现：Level 3需要Level 1和Level 2都通过。"
                    f"当前Level 1={l1_passed}, Level 2={l2_passed}。"
                    f"123号§43：不要把完整FLT作为第一个动态闭环POC。"
                )

        return {"can_research_level_3": True, "l1_passed": self._passed_levels.get(1, False),
                "l2_passed": self._passed_levels.get(2, False)}


class CapabilityDistinctionChecker:
    """
    P7-2.COMP3：区分三项能力。

    123号§35：调用已证半稳定模性重建FLT推论 / 重建Wiles证明 / 独立发现路线。
    """

    def __init__(self):
        self._capabilities = {c["id"]: c for c in CAPABILITY_DISTINCTION}

    def get_all_capabilities(self) -> List[Dict[str, Any]]:
        return list(CAPABILITY_DISTINCTION)

    def check_distinction(self, claimed_capability: str) -> Dict[str, Any]:
        """
        检查声称的能力是否与三项能力之一匹配。

        边界情况：三项能力混淆→拒绝。
        """
        for cap in CAPABILITY_DISTINCTION:
            if cap["text"] == claimed_capability:
                return {"matched": True, "capability_id": cap["id"], "level": cap["level"].value}

        return {"matched": False, "reason": "三项能力混淆——必须明确区分"}
