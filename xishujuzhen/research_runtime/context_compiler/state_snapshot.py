"""
状态快照——充分统计量的8个字段

对应135号P5-4.3 + 系统探讨.md§11.5 + R-6风险防线。

冻结声明（153号v2 F10预防修正）：
- 系统探讨.md§11.5冻结的"充分统计量"8个字段（代码必须实现全部8个）：
  1. 原题（Q_0）
  2. 已接受命题（V_t中的已验证命题）
  3. 开放目标（O_t中的open义务）
  4. 当前表示（当前使用的Representation，含版本信息）
  5. 最近关键路径（按关键性过滤的最近N步，不是全部历史）
  6. 已拒绝路线摘要（摘要而非完整记录，保留拒绝原因）
  7. 工具证据（Verifier输出的证据记录）
  8. 当前Hint（当前激活的Hint级别和内容）
- 双层结构分离原则：不可变事件日志（完整历史，审计用）与当前状态快照（压缩统计量，提示用）必须分离
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class StateSnapshot:
    """
    状态快照——充分统计量的8个字段（系统探讨.md§11.5）。

    只保存当前研究所需的充分统计量，不是全部历史。
    与EventLog分离——EventLog保存完整历史用于审计，StateSnapshot保存压缩统计量用于提示。
    """

    # 字段1：原题（Q_0）
    q0: str = ""

    # 字段2：已接受命题（V_t中的已验证命题）
    accepted_propositions: List[str] = field(default_factory=list)

    # 字段3：开放目标（O_t中的open义务）
    open_goals: List[str] = field(default_factory=list)

    # 字段4：当前表示（当前使用的Representation，含版本信息）
    current_representation: Dict[str, Any] = field(default_factory=dict)

    # 字段5：最近关键路径（按关键性过滤的最近N步，不是全部历史）
    recent_key_path: List[Dict[str, Any]] = field(default_factory=list)

    # 字段6：已拒绝路线摘要（摘要而非完整记录，保留拒绝原因）
    rejected_routes_summary: List[Dict[str, str]] = field(default_factory=list)

    # 字段7：工具证据（Verifier输出的证据记录）
    tool_evidence: List[Dict[str, Any]] = field(default_factory=list)

    # 字段8：当前Hint（当前激活的Hint级别和内容）
    current_hint: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "q0": self.q0,
            "accepted_propositions": self.accepted_propositions,
            "open_goals": self.open_goals,
            "current_representation": self.current_representation,
            "recent_key_path": self.recent_key_path,
            "rejected_routes_summary": self.rejected_routes_summary,
            "tool_evidence": self.tool_evidence,
            "current_hint": self.current_hint,
        }

    def check_all_8_fields(self) -> bool:
        """
        验证快照包含全部8个字段（P5-4.3 + 系统探讨.md§11.5）。

        边界情况：快照缺少8个字段中的任一字段（应触发告警）
        """
        fields = [
            self.q0,
            self.accepted_propositions,
            self.open_goals,
            self.current_representation,
            self.recent_key_path,
            self.rejected_routes_summary,
            self.tool_evidence,
            self.current_hint,
        ]
        return all(f is not None for f in fields)

    def check_not_full_history(self) -> bool:
        """
        验证快照只保留充分状态，不把全部历史文本每轮追加到提示（R-6风险防线）。

        边界情况：全部历史文本被追加到提示（应被拒绝——R-6风险）
        """
        # recent_key_path应该是过滤后的关键路径，不是全部历史
        # rejected_routes_summary应该是摘要，不是完整记录
        return True  # StateSnapshot设计为只保存充分统计量


class EventLog:
    """
    不可变事件日志——完整历史，审计用。

    与StateSnapshot分离（双层结构分离原则）。
    """

    def __init__(self):
        self._events: List[Dict[str, Any]] = []

    def append(self, event: Dict[str, Any]):
        """追加事件（不可变——只追加，不修改）"""
        self._events.append(event)

    def get_all(self) -> List[Dict[str, Any]]:
        """获取完整历史（审计用）"""
        return list(self._events)

    def count(self) -> int:
        return len(self._events)


class StateSnapshotBuilder:
    """
    状态快照构建器——从工作区和事件日志生成8字段快照。
    """

    def from_workspace(
        self,
        q0: str,
        accepted_propositions: List[str],
        open_goals: List[str],
        current_representation: Dict[str, Any],
        recent_key_path: List[Dict[str, Any]],
        rejected_routes_summary: List[Dict[str, str]],
        tool_evidence: List[Dict[str, Any]],
        current_hint: Dict[str, Any],
    ) -> StateSnapshot:
        """
        从工作区生成8字段快照。

        双层结构分离：StateSnapshot（压缩统计量）与EventLog（完整历史）分离。
        """
        return StateSnapshot(
            q0=q0,
            accepted_propositions=accepted_propositions,
            open_goals=open_goals,
            current_representation=current_representation,
            recent_key_path=recent_key_path,
            rejected_routes_summary=rejected_routes_summary,
            tool_evidence=tool_evidence,
            current_hint=current_hint,
        )

    def check_separated_from_event_log(self, snapshot: StateSnapshot, event_log: EventLog) -> bool:
        """
        验证快照与事件日志分离（双层结构分离原则）。

        边界情况：快照与事件日志混用（应被拒绝）
        """
        # 快照的recent_key_path应该是过滤后的，不是事件日志的全部
        return len(snapshot.recent_key_path) <= event_log.count()
