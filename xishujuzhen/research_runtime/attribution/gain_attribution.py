"""
增益归因模块（261号§4.9）。

按261号§4.9的实现路径，记录提示链（Q1→Q2→...→Q10），
对每轮的进展增量归因给该轮发送的Q，
并对归因结果做反事实估计。

进展归因：A_i的进展增量归因给Q_i。
进展增量 = V_t新增条目数 + O_t从open到solved的数量。

反事实估计（简化版）：
- 若U_t中对应义务是blocking → "没有该Q不太可能自发达到进展"
- 若U_t中对应义务是minor → "没有该Q也可能达到进展"
"""

from dataclasses import dataclass, field
from typing import Dict, Optional

from ..hgraph.hgraph_store import HeuristicRule
from ..parser.models import ParseResult, SixTuple
from ..policy.constrained_optimizer import _normalize_obligation


# ---------------------------------------------------------------------------
# 数据结构
# ---------------------------------------------------------------------------

@dataclass
class GainRecord:
    """
    单轮增益归因记录（261号§4.9）。

    - round_index：轮次
    - rule_id：归因到的规则ID（该轮发送的Q）
    - progress_delta：进展增量（V_t新增 + O_t open→solved）
    - attribution_type：归因类型（"progress" / "counterfactual"）
    - detail：归因细节（人话描述）
    """
    round_index: int = 0
    rule_id: str = ""
    progress_delta: float = 0.0
    attribution_type: str = "progress"
    detail: str = ""

    def to_dict(self) -> dict:
        return {
            "round_index": self.round_index,
            "rule_id": self.rule_id,
            "progress_delta": self.progress_delta,
            "attribution_type": self.attribution_type,
            "detail": self.detail,
        }


# ---------------------------------------------------------------------------
# 增益归因
# ---------------------------------------------------------------------------

class GainAttribution:
    """
    增益归因（261号§4.9）。

    记录提示链（Q1→Q2→...→Q10），
    对每轮的进展增量归因给该轮发送的Q，
    并对归因结果做反事实估计。
    """

    def __init__(self) -> None:
        # 提示链：round_index -> 该轮发送的HeuristicRule
        self._hint_chain: Dict[int, HeuristicRule] = {}

    def record_hint(self, round_index: int, rule: HeuristicRule) -> None:
        """
        记录每轮发送的Q（261号§4.9）。

        构建提示链 Q1→Q2→...→Q10。
        """
        self._hint_chain[round_index] = rule

    def get_hint(self, round_index: int) -> Optional[HeuristicRule]:
        """获取某轮记录的Q。"""
        return self._hint_chain.get(round_index)

    def attribute_gain(
        self,
        round_index: int,
        parse_result: ParseResult,
        previous_six_tuple: SixTuple,
    ) -> GainRecord:
        """
        进展归因（261号§4.9）。

        比较parse_result.six_tuple和previous_six_tuple，
        计算进展增量（V_t新增条目数 + O_t从open到solved的数量），
        归因给该轮的Q。
        """
        rule = self._hint_chain.get(round_index)
        rule_id = rule.rule_id if rule is not None else "unknown"

        current = parse_result.six_tuple
        progress_delta = self._compute_progress_delta(current, previous_six_tuple)

        detail = (
            f"轮次{round_index}：Q={rule_id}，"
            f"进展增量={progress_delta:.0f}"
            f"（V_t新增{self._new_v_count(current, previous_six_tuple)}条，"
            f"O_t open→solved {self._solved_count(current, previous_six_tuple)}条）"
        )
        return GainRecord(
            round_index=round_index,
            rule_id=rule_id,
            progress_delta=progress_delta,
            attribution_type="progress",
            detail=detail,
        )

    def estimate_counterfactual(
        self,
        round_index: int,
        gain_record: GainRecord,
        six_tuple: Optional[SixTuple] = None,
    ) -> str:
        """
        反事实估计（261号§4.9，简化版）。

        若U_t中对应义务是blocking → "没有该Q不太可能自发达到进展"
        若U_t中对应义务是minor → "没有该Q也可能达到进展"

        six_tuple参数：用于查U_t的六元组（默认从提示链无法获取，需调用方传入）。
        """
        rule = self._hint_chain.get(round_index)
        rule_id = rule.rule_id if rule is not None else gain_record.rule_id
        obligation_id = rule.obligation_id if rule is not None else ""

        severity = self._match_obligation_severity(obligation_id, six_tuple)

        if severity == "blocking":
            return (
                f"没有{rule_id}，不太可能自发达到进展："
                f"对应义务'{obligation_id}'在U_t中为blocking，"
                f"没有该提示AI难以自发突破此瓶颈"
            )
        # minor 或未知 → 可能自发达到
        return (
            f"没有{rule_id}，也可能达到进展："
            f"对应义务'{obligation_id}'在U_t中为{severity or '未识别'}，"
            f"非blocking瓶颈，AI有可能自发推进"
        )

    # -----------------------------------------------------------------
    # 内部计算方法
    # -----------------------------------------------------------------

    @staticmethod
    def _compute_progress_delta(current: SixTuple, previous: SixTuple) -> float:
        """
        计算进展增量（261号§4.9）。

        progress_delta = V_t新增条目数 + O_t从open到solved的数量。
        """
        return (
            GainAttribution._new_v_count(current, previous)
            + GainAttribution._solved_count(current, previous)
        )

    @staticmethod
    def _new_v_count(current: SixTuple, previous: SixTuple) -> int:
        """V_t新增条目数：current中有而previous中没有的V_t条目。"""
        prev_statements = {v.statement for v in previous.V_t}
        return sum(1 for v in current.V_t if v.statement not in prev_statements)

    @staticmethod
    def _solved_count(current: SixTuple, previous: SixTuple) -> int:
        """O_t从open到solved的数量。"""
        # previous中open的义务描述集合
        prev_open = {
            o.description for o in previous.O_t
            if o.status in ("open", "in_progress")
        }
        # current中这些义务已solved的数量
        solved = 0
        for o in current.O_t:
            if o.status == "solved" and o.description in prev_open:
                solved += 1
        return solved

    @staticmethod
    def _match_obligation_severity(
        obligation_id: str,
        six_tuple: Optional[SixTuple],
    ) -> str:
        """
        在U_t中匹配义务对应的severity（261号§4.9）。

        做双向子串匹配，返回匹配到的severity（blocking/minor/potential），
        未匹配返回空字符串。
        """
        if not six_tuple or not obligation_id:
            return ""
        target = _normalize_obligation(obligation_id)
        for u in six_tuple.U_t:
            desc = _normalize_obligation(u.description)
            if target in desc or desc in target:
                return u.severity
        return ""
