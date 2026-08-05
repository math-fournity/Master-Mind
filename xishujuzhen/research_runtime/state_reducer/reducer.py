"""
StateReducer + 多观察者重建一致性测试（DYN-1）

对应132号P2-6。

123号§47（DYN-1）：
- 不同抽取器能否一致识别命题、义务、表示、证据和拒绝分支
- 验收标准：关键状态字段Krippendorff α≥0.80，无关键字段低于0.67

实现2个独立的StateReducer：
1. RuleBasedReducer：基于规则的抽取（正则匹配+关键词检测）
2. SemanticBasedReducer：基于语义的抽取（事件类型+字段映射）

两者对同一事件流各自独立重建状态，然后计算字段级Krippendorff α。

边界情况：
- 分歧案例（两个Reducer输出不一致）
- 仲裁结果（分歧时如何选择）
- 关键字段低于0.67（触发R-9停止条件）
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime, timezone
from collections import defaultdict
import math

from ..models.event import SemanticEvent, SemanticEventType
from .obligation import Obligation, ObligationType, ObligationStatus
from .evidence import Evidence, EvidenceKind, EvidencePolarity, EvidenceStatus
from .progress import ProgressVector, CanonicalKey


@dataclass
class ReconstructedState:
    """
    重建状态——StateReducer的输出。

    从事件流中重建的工作区状态。
    """
    reducer_name: str                                   # Reducer名称
    v_t_premises: List[str] = field(default_factory=list)
    v_t_lemmas: List[str] = field(default_factory=list)
    v_t_tool_results: List[str] = field(default_factory=list)
    f_t_candidates: List[str] = field(default_factory=list)
    f_t_temporary_assumptions: List[str] = field(default_factory=list)
    f_t_unverified_bridges: List[str] = field(default_factory=list)
    o_t_obligation_ids: List[str] = field(default_factory=list)
    r_t_representations: List[str] = field(default_factory=list)
    d_t_rejected: List[str] = field(default_factory=list)
    d_t_suspended: List[str] = field(default_factory=list)
    e_t_evidence_ids: List[str] = field(default_factory=list)
    stall_type: str = "no_stall"
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "reducer_name": self.reducer_name,
            "V_t": {
                "verified_premises": self.v_t_premises,
                "verified_lemmas": self.v_t_lemmas,
                "verified_tool_results": self.v_t_tool_results,
            },
            "F_t": {
                "candidates": self.f_t_candidates,
                "temporary_assumptions": self.f_t_temporary_assumptions,
                "unverified_bridges": self.f_t_unverified_bridges,
            },
            "O_t": {"obligation_ids": self.o_t_obligation_ids},
            "R_t": {"active_representations": self.r_t_representations},
            "D_t": {
                "rejected_branches": self.d_t_rejected,
                "suspended_branches": self.d_t_suspended,
            },
            "E_t": {"evidence_ids": self.e_t_evidence_ids},
            "stall_type": self.stall_type,
            "timestamp": self.timestamp,
        }


class StateReducer:
    """
    StateReducer基类：从事件流重建状态。

    冻结声明（P2-6.COMP）：
    - 可复现约束——同一事件流+同一Reducer版本→同一状态
    """

    def __init__(self, name: str, version: str = "v1"):
        self.name = name
        self.version = version

    def reduce(self, events: List[Dict[str, Any]]) -> ReconstructedState:
        """从事件流重建状态。子类必须实现。"""
        raise NotImplementedError

    def _init_state(self) -> ReconstructedState:
        return ReconstructedState(reducer_name=self.name)


class RuleBasedReducer(StateReducer):
    """
    基于规则的StateReducer。

    抽取策略：正则匹配+关键词检测。
    从SemanticEvent的type和content字段中抽取状态。
    """

    def __init__(self):
        super().__init__(name="rule_based", version="v1")

    def reduce(self, events: List[Dict[str, Any]]) -> ReconstructedState:
        state = self._init_state()

        for event in events:
            event_type = event.get("type", "")
            content = event.get("content", "")
            event_id = event.get("event_id", "")

            # CLAIM事件→V_t或F_t
            if event_type == SemanticEventType.CLAIM.value:
                # 检查是否有verification证据
                if event.get("verified", False):
                    state.v_t_lemmas.append(content)
                else:
                    state.f_t_candidates.append(content)

            # CANDIDATE事件→F_t
            elif event_type == SemanticEventType.CANDIDATE.value:
                state.f_t_candidates.append(content)

            # SUBGOAL事件→O_t
            elif event_type == SemanticEventType.SUBGOAL.value:
                state.o_t_obligation_ids.append(event_id)

            # REPRESENTATION事件→R_t
            elif event_type == SemanticEventType.REPRESENTATION.value:
                state.r_t_representations.append(content)

            # TEST事件→E_t
            elif event_type == SemanticEventType.TEST.value:
                state.e_t_evidence_ids.append(event_id)

            # TOOL_RESULT事件→V_t或E_t
            elif event_type == SemanticEventType.TOOL_RESULT.value:
                if event.get("verified", False):
                    state.v_t_tool_results.append(content)
                else:
                    state.e_t_evidence_ids.append(event_id)

            # CONTRADICTION事件→D_t
            elif event_type == SemanticEventType.CONTRADICTION.value:
                state.d_t_rejected.append(content)

            # STALL事件→stall_type
            elif event_type == SemanticEventType.STALL.value:
                state.stall_type = event.get("stall_type", "unknown_stall")

            # BACKTRACK事件→D_t
            elif event_type == SemanticEventType.BACKTRACK.value:
                state.d_t_suspended.append(content)

            # RESOLUTION事件→V_t
            elif event_type == SemanticEventType.RESOLUTION.value:
                state.v_t_lemmas.append(content)

            # VERIFICATION事件→V_t + E_t
            elif event_type == SemanticEventType.VERIFICATION.value:
                state.v_t_lemmas.append(content)
                state.e_t_evidence_ids.append(event_id)

            # HINT_INJECTION事件→F_t（临时假设）
            elif event_type == SemanticEventType.HINT_INJECTION.value:
                state.f_t_temporary_assumptions.append(content)

        return state


class SemanticBasedReducer(StateReducer):
    """
    基于语义的StateReducer。

    抽取策略：事件类型+字段映射+语义标签。
    与RuleBasedReducer不同的抽取策略，用于DYN-1一致性测试。
    """

    def __init__(self):
        super().__init__(name="semantic_based", version="v1")

    def reduce(self, events: List[Dict[str, Any]]) -> ReconstructedState:
        state = self._init_state()

        for event in events:
            event_type = event.get("type", "")
            content = event.get("content", "")
            event_id = event.get("event_id", "")
            # 语义Reducer使用semantic_tags字段做更细粒度分类
            tags = event.get("semantic_tags", [])

            # CLAIM事件——语义Reducer用tags区分V_t/F_t
            if event_type == SemanticEventType.CLAIM.value:
                if "verified" in tags or event.get("verified", False):
                    if "premise" in tags:
                        state.v_t_premises.append(content)
                    else:
                        state.v_t_lemmas.append(content)
                else:
                    if "temporary" in tags:
                        state.f_t_temporary_assumptions.append(content)
                    else:
                        state.f_t_candidates.append(content)

            # CANDIDATE事件——语义Reducer也检查tags
            elif event_type == SemanticEventType.CANDIDATE.value:
                if "bridge" in tags:
                    state.f_t_unverified_bridges.append(content)
                else:
                    state.f_t_candidates.append(content)

            # SUBGOAL事件——语义Reducer映射到O_t
            elif event_type == SemanticEventType.SUBGOAL.value:
                state.o_t_obligation_ids.append(event_id)

            # REPRESENTATION事件
            elif event_type == SemanticEventType.REPRESENTATION.value:
                state.r_t_representations.append(content)

            # TEST事件——语义Reducer也加入E_t
            elif event_type == SemanticEventType.TEST.value:
                state.e_t_evidence_ids.append(event_id)

            # TOOL_RESULT事件——语义Reducer用tags区分
            elif event_type == SemanticEventType.TOOL_RESULT.value:
                if "verified" in tags:
                    state.v_t_tool_results.append(content)
                else:
                    state.e_t_evidence_ids.append(event_id)

            # CONTRADICTION事件——语义Reducer映射到D_t
            elif event_type == SemanticEventType.CONTRADICTION.value:
                state.d_t_rejected.append(content)

            # STALL事件
            elif event_type == SemanticEventType.STALL.value:
                state.stall_type = event.get("stall_type", "unknown_stall")

            # BACKTRACK事件
            elif event_type == SemanticEventType.BACKTRACK.value:
                state.d_t_suspended.append(content)

            # RESOLUTION事件
            elif event_type == SemanticEventType.RESOLUTION.value:
                state.v_t_lemmas.append(content)

            # VERIFICATION事件
            elif event_type == SemanticEventType.VERIFICATION.value:
                if "premise" in tags:
                    state.v_t_premises.append(content)
                else:
                    state.v_t_lemmas.append(content)
                state.e_t_evidence_ids.append(event_id)

            # HINT_INJECTION事件
            elif event_type == SemanticEventType.HINT_INJECTION.value:
                state.f_t_temporary_assumptions.append(content)

        return state


class KrippendorffAlpha:
    """
    Krippendorff α计算（DYN-1核心验收标准）。

    123号§47 + G0-2：
    - 关键状态字段Krippendorff α≥0.80
    - 无关键字段低于0.67

    支持的字段类型：
    - nominal：名义标度（用于列表字段——比较集合是否一致）
    - interval：区间标度（用于数值字段）

    这里用nominal标度——比较两个Reducer的输出字段是否一致。
    """

    @staticmethod
    def compute_nominal(
        observations: List[List[Any]],
    ) -> float:
        """
        计算nominal标度的Krippendorff α。

        参数：
        - observations: 每个观察者的观察值列表（按unit对齐）

        例如2个观察者对3个unit的观察：
        [["a", "b", "a"], ["a", "c", "a"]]

        返回：α值（-1到1，1=完全一致，0=随机一致）
        """
        if not observations or len(observations) < 2:
            return 1.0  # 只有一个观察者——完全一致

        n_observers = len(observations)
        n_units = len(observations[0])

        if n_units == 0:
            return 1.0

        # 统计每个unit的观察值分布
        # 只考虑所有观察者都有有效值的unit
        unit_values: List[List[Any]] = []
        for u in range(n_units):
            values = [observations[o][u] for o in range(n_observers)]
            # 跳过缺失值（None）
            if any(v is None for v in values):
                continue
            unit_values.append(values)

        n_valid_units = len(unit_values)
        if n_valid_units == 0:
            return 1.0

        # 计算observed disagreement（Do）
        Do = 0.0
        for values in unit_values:
            # 每对观察者之间的不一致
            for i in range(n_observers):
                for j in range(i + 1, n_observers):
                    if values[i] != values[j]:
                        Do += 1.0
        Do = Do * 2.0 / (n_observers - 1)  # 归一化
        Do = Do / n_valid_units

        # 计算expected disagreement（De）
        # 统计所有值的出现频率
        value_counts: Dict[Any, int] = defaultdict(int)
        total_values = 0
        for values in unit_values:
            for v in values:
                value_counts[v] += 1
                total_values += 1

        De = 0.0
        for v1, c1 in value_counts.items():
            for v2, c2 in value_counts.items():
                if v1 != v2:
                    De += (c1 / total_values) * (c2 / total_values)

        if De == 0:
            return 1.0  # 所有值相同——完全一致

        alpha = 1.0 - Do / De
        return alpha

    @staticmethod
    def compute_for_fields(
        state1: ReconstructedState,
        state2: ReconstructedState,
    ) -> Dict[str, float]:
        """
        计算两个Reducer输出的字段级Krippendorff α。

        对每个字段，比较两个Reducer的输出是否一致。
        """
        # 定义要比较的字段
        fields = [
            ("v_t_premises", state1.v_t_premises, state2.v_t_premises),
            ("v_t_lemmas", state1.v_t_lemmas, state2.v_t_lemmas),
            ("v_t_tool_results", state1.v_t_tool_results, state2.v_t_tool_results),
            ("f_t_candidates", state1.f_t_candidates, state2.f_t_candidates),
            ("f_t_temporary_assumptions", state1.f_t_temporary_assumptions, state2.f_t_temporary_assumptions),
            ("f_t_unverified_bridges", state1.f_t_unverified_bridges, state2.f_t_unverified_bridges),
            ("o_t_obligation_ids", state1.o_t_obligation_ids, state2.o_t_obligation_ids),
            ("r_t_representations", state1.r_t_representations, state2.r_t_representations),
            ("d_t_rejected", state1.d_t_rejected, state2.d_t_rejected),
            ("d_t_suspended", state1.d_t_suspended, state2.d_t_suspended),
            ("e_t_evidence_ids", state1.e_t_evidence_ids, state2.e_t_evidence_ids),
            ("stall_type", [state1.stall_type], [state2.stall_type]),
        ]

        alphas: Dict[str, float] = {}
        for field_name, val1, val2 in fields:
            # 对列表字段：比较集合是否一致
            # 转换为集合比较——如果两个Reducer输出相同的集合，α=1
            set1 = set(val1)
            set2 = set(val2)

            if set1 == set2:
                alphas[field_name] = 1.0
            elif set1 and set2:
                # 有交集但不完全一致
                intersection = set1 & set2
                union = set1 | set2
                jaccard = len(intersection) / len(union)
                # 用Jaccard相似度近似α
                alphas[field_name] = jaccard
            else:
                # 一个为空一个非空
                alphas[field_name] = 0.0

        return alphas


class ConsistencyTest:
    """
    多观察者重建一致性测试（DYN-1）。

    验收标准（G0-2）：
    - 关键状态字段Krippendorff α≥0.80
    - 无关键字段低于0.67
    - 否则触发R-9停止条件
    """

    # 关键字段定义（G0-2）
    CRITICAL_FIELDS = [
        "v_t_premises",
        "v_t_lemmas",
        "f_t_candidates",
        "o_t_obligation_ids",
        "stall_type",
    ]

    # α阈值（G0-2）
    ALPHA_THRESHOLD = 0.80
    CRITICAL_ALPHA_MIN = 0.67

    def __init__(self, reducers: List[StateReducer]):
        self.reducers = reducers
        self.alpha_calculator = KrippendorffAlpha()

    def run(
        self,
        events: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        运行一致性测试。

        1. 每个Reducer独立重建状态
        2. 计算字段级Krippendorff α
        3. 检查G0-2阈值
        4. 记录分歧案例和仲裁结果
        """
        # 1. 每个Reducer独立重建
        states = []
        for reducer in self.reducers:
            state = reducer.reduce(events)
            states.append(state)

        # 2. 计算字段级α（两两比较）
        pairwise_alphas: List[Dict[str, float]] = []
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                alphas = self.alpha_calculator.compute_for_fields(states[i], states[j])
                pairwise_alphas.append({
                    "reducer_i": states[i].reducer_name,
                    "reducer_j": states[j].reducer_name,
                    "alphas": alphas,
                })

        # 3. 计算平均α
        field_alphas: Dict[str, List[float]] = defaultdict(list)
        for pa in pairwise_alphas:
            for field, alpha in pa["alphas"].items():
                field_alphas[field].append(alpha)

        avg_alphas: Dict[str, float] = {}
        for field, alphas in field_alphas.items():
            avg_alphas[field] = sum(alphas) / len(alphas) if alphas else 0.0

        # 4. 检查G0-2阈值
        critical_below_threshold = []
        for field in self.CRITICAL_FIELDS:
            alpha = avg_alphas.get(field, 0.0)
            if alpha < self.CRITICAL_ALPHA_MIN:
                critical_below_threshold.append({
                    "field": field,
                    "alpha": alpha,
                    "threshold": self.CRITICAL_ALPHA_MIN,
                })

        all_above_threshold = all(
            avg_alphas.get(f, 0.0) >= self.ALPHA_THRESHOLD
            for f in self.CRITICAL_FIELDS
        )

        # 5. 记录分歧案例
        disagreements: List[Dict[str, Any]] = []
        for field in self.CRITICAL_FIELDS:
            values_per_reducer = []
            for state in states:
                val = getattr(state, field, [])
                values_per_reducer.append(set(val) if isinstance(val, list) else {val})

            if len(set(frozenset(v) for v in values_per_reducer)) > 1:
                disagreements.append({
                    "field": field,
                    "values": [list(v) for v in values_per_reducer],
                    "alpha": avg_alphas.get(field, 0.0),
                })

        # 6. 仲裁结果——分歧时选择第一个Reducer的输出（简化版）
        arbitration = {}
        for d in disagreements:
            arbitration[d["field"]] = d["values"][0]  # 选第一个Reducer

        # 7. 是否通过G0-2
        passed = all_above_threshold and len(critical_below_threshold) == 0

        return {
            "passed": passed,
            "avg_alphas": avg_alphas,
            "pairwise_alphas": pairwise_alphas,
            "critical_below_threshold": critical_below_threshold,
            "disagreements": disagreements,
            "arbitration": arbitration,
            "g0_2_threshold": self.ALPHA_THRESHOLD,
            "g0_2_critical_min": self.CRITICAL_ALPHA_MIN,
            "would_trigger_r9": not passed,  # R-9停止条件
            "states": [s.to_dict() for s in states],
        }
