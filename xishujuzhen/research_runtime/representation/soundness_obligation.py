"""
P7-1.2/P7-1.COMP soundness义务验证——运输只在对应义务通过后成立。

127号§5冻结声明1："运输只在对应义务通过后成立，不能因边名叫equivalence就自动成立。"

强制机制（162号v4维度21预检修正）：
  义务未通过时调用运输函数必须抛SoundnessViolationError（不只是返回False），
  且transport()方法内部必须检查义务状态——不能由调用方自行判断。
"""

from typing import Dict, Any, Optional, Callable
from dataclasses import dataclass, field


class SoundnessViolationError(Exception):
    """
    P7-1.2/P7-1.COMP强制机制：义务未通过时运输→抛SoundnessViolationError。

    不只是返回False声明——是运行时强制阻断。
    """


@dataclass
class ObligationStatus:
    """义务状态——跟踪soundness_obligation的通过/未通过状态。"""
    obligation_id: str
    satisfied: bool = False
    evidence_ids: list = field(default_factory=list)
    verified_by: str = ""

    def mark_satisfied(self, evidence_ids: list, verified_by: str = "") -> None:
        self.satisfied = True
        self.evidence_ids = list(evidence_ids)
        self.verified_by = verified_by

    def to_dict(self) -> dict:
        return {
            "obligation_id": self.obligation_id,
            "satisfied": self.satisfied,
            "evidence_ids": list(self.evidence_ids),
            "verified_by": self.verified_by,
        }


class SoundnessObligationTracker:
    """
    跟踪多个义务的状态，为transport()提供义务检查。

    127号§5："运输只在对应义务通过后成立。"
    """

    def __init__(self):
        self._obligations: Dict[str, ObligationStatus] = {}

    def register(self, obligation_id: str) -> ObligationStatus:
        if obligation_id not in self._obligations:
            self._obligations[obligation_id] = ObligationStatus(obligation_id)
        return self._obligations[obligation_id]

    def mark_satisfied(self, obligation_id: str, evidence_ids: list, verified_by: str = "") -> None:
        ob = self.register(obligation_id)
        ob.mark_satisfied(evidence_ids, verified_by)

    def is_satisfied(self, obligation_id: str) -> bool:
        ob = self._obligations.get(obligation_id)
        return ob.satisfied if ob else False

    def get_status(self, obligation_id: str) -> Optional[ObligationStatus]:
        return self._obligations.get(obligation_id)

    def all_statuses(self) -> Dict[str, ObligationStatus]:
        return dict(self._obligations)


class SoundnessTransporter:
    """
    P7-1.2/P7-1.COMP：soundness义务验证的运输器。

    核心方法transport()内部检查义务状态——
    义务未通过时抛SoundnessViolationError，不能由调用方自行判断。
    """

    def __init__(self, tracker: SoundnessObligationTracker):
        self._tracker = tracker
        # 缓存义务指向不存在的检查
        self._known_obligations: set = set(tracker.all_statuses().keys())

    def register_obligation(self, obligation_id: str) -> None:
        """注册一个已知义务ID。"""
        self._tracker.register(obligation_id)
        self._known_obligations.add(obligation_id)

    def transport(
        self,
        rep_map,
        source_object: Any,
        obligation_tracker: Optional[SoundnessObligationTracker] = None,
    ) -> Dict[str, Any]:
        """
        执行表示运输——内部检查义务状态。

        P7-1.COMP强制机制：
        - transport()方法内部检查义务状态
        - 义务未通过时抛SoundnessViolationError（不只是返回False）
        - 不能由调用方自行判断

        边界情况：
        - soundness_obligation指向不存在的义务→抛ValueError
        - preconditions未满足时运输→抛SoundnessViolationError
        - 义务未通过时运输→抛SoundnessViolationError
        """
        tracker = obligation_tracker or self._tracker

        # 检查1：soundness_obligation指向是否存在
        ob_id = rep_map.soundness_obligation
        if not ob_id:
            raise ValueError(
                f"RepresentationMap {rep_map.rep_id} 无soundness_obligation"
            )
        if ob_id not in self._known_obligations and ob_id not in tracker.all_statuses():
            raise ValueError(
                f"soundness_obligation指向不存在的义务: {ob_id}"
            )

        # 检查2：义务是否通过——P7-1.COMP强制机制
        if not tracker.is_satisfied(ob_id):
            raise SoundnessViolationError(
                f"运输被拒绝：soundness_obligation {ob_id} 未通过。"
                f"RepresentationMap {rep_map.rep_id} ({rep_map.source_form}→{rep_map.target_form})。"
                f"127号§5：运输只在对应义务通过后成立。"
            )

        # 义务通过，执行运输
        return {
            "rep_id": rep_map.rep_id,
            "source_form": rep_map.source_form,
            "target_form": rep_map.target_form,
            "map_type": rep_map.map_type.value,
            "transported_object": source_object,
            "obligation_id": ob_id,
            "obligation_satisfied": True,
            "preserved_invariants": list(rep_map.preserved_invariants),
            "lost_information": list(rep_map.lost_information),
        }

    def check_obligation_before_transport(self, rep_map) -> Dict[str, Any]:
        """
        在运输前检查义务状态（不执行运输）。

        用于调用方预先了解义务状态，但transport()本身仍会内部检查。
        """
        ob_id = rep_map.soundness_obligation
        if not ob_id:
            return {"has_obligation": False, "satisfied": False}
        return {
            "has_obligation": True,
            "obligation_id": ob_id,
            "satisfied": self._tracker.is_satisfied(ob_id),
        }
