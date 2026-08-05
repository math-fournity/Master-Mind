"""
进展偏序 + 状态等价 + 两种环路判别

对应132号P2-9。

123号§18定义：
- 进展偏序 P_κ(S_t) = (v_t, -o_t, -c_t, -u_t, -k_t)
- v_t = 目标相关已验证义务权重
- o_t = 未释放义务权重
- c_t = 未解决冲突数
- u_t = 尚无可检验证据的活动候选数
- k_t = 累计资源成本
- P_κ(S_i) ≺ P_κ(S_j) 当且仅当所有分量不恶化且至少一项严格改善

123号§18状态等价：
- 状态等价不是万能关系，而是由任务类型κ和抽象级别α参数化的~_{α,κ}
- 规范化键至少包括：开放义务的类型化同构类、当前表示ID、已验证核心中的目标相关命题ID、活动分支和证据门状态
- 规范化键忽略：措辞、变量改名和事件时间
- 只有规范化键一致，才记为 W_i ~_{α,κ} W_j

两种环路（AGENTS.md方法论核心）：
- 平面环路：不同时间事件投影回同一规范化状态，开放义务、证据门和冲突无改善 → 停止或换策略
- 螺旋上升环路：返回同一抽象状态类，但更细粒度状态进展 → 允许继续并保存进展证据

边界情况：
- 5个分量全部恶化
- 4个恶化1个改善（算改善还是恶化？→算改善，因为至少一项严格改善）
- 分量值相同
- 规范化键部分一致
- 不同抽象级别α下的等价判定
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple
from enum import Enum


@dataclass
class ProgressVector:
    """
    进展向量 P_κ(S_t) = (v_t, -o_t, -c_t, -u_t, -k_t)（123号§18）。

    注意：存储的是原始值（v_t, o_t, c_t, u_t, k_t），比较时取负。
    """
    v_t: float = 0.0    # 目标相关已验证义务权重
    o_t: float = 0.0    # 未释放义务权重
    c_t: int = 0        # 未解决冲突数
    u_t: int = 0        # 尚无可检验证据的活动候选数
    k_t: float = 0.0    # 累计资源成本

    def to_comparison_vector(self) -> Tuple[float, float, float, float, float]:
        """
        转换为比较向量 (v_t, -o_t, -c_t, -u_t, -k_t)。

        比较规则：P_κ(S_i) ≺ P_κ(S_j) 当且仅当所有分量不恶化且至少一项严格改善。
        """
        return (self.v_t, -self.o_t, -float(self.c_t), -float(self.u_t), -self.k_t)

    def to_dict(self) -> dict:
        return {
            "v_t": self.v_t,
            "o_t": self.o_t,
            "c_t": self.c_t,
            "u_t": self.u_t,
            "k_t": self.k_t,
        }


class LoopType(str, Enum):
    """
    两种环路类型（AGENTS.md方法论核心）。
    """
    PLATEAU = "plateau"        # 平面环路：无改善 → 停止或换策略
    SPIRAL = "spiral"          # 螺旋上升环路：更细粒度进展 → 允许继续
    NO_LOOP = "no_loop"        # 非环路


@dataclass
class CanonicalKey:
    """
    规范化键（123号§18，F3修正补充）。

    首版规范化键至少包括：
    - 开放义务的类型化同构类
    - 当前表示ID
    - 已验证核心中的目标相关命题ID
    - 活动分支
    - 证据门状态

    规范化键忽略：
    - 措辞
    - 变量改名
    - 事件时间
    """
    open_obligation_classes: List[str] = field(default_factory=list)    # 开放义务的类型化同构类
    representation_id: str = ""                                         # 当前表示ID
    verified_core_proposition_ids: List[str] = field(default_factory=list)  # V_t中目标相关命题ID
    active_branches: List[str] = field(default_factory=list)           # 活动分支
    evidence_gate_states: List[str] = field(default_factory=list)       # 证据门状态

    def to_tuple(self) -> Tuple:
        """转换为可比较的tuple（忽略顺序，排序后比较）。"""
        return (
            tuple(sorted(self.open_obligation_classes)),
            self.representation_id,
            tuple(sorted(self.verified_core_proposition_ids)),
            tuple(sorted(self.active_branches)),
            tuple(sorted(self.evidence_gate_states)),
        )

    def to_dict(self) -> dict:
        return {
            "open_obligation_classes": self.open_obligation_classes,
            "representation_id": self.representation_id,
            "verified_core_proposition_ids": self.verified_core_proposition_ids,
            "active_branches": self.active_branches,
            "evidence_gate_states": self.evidence_gate_states,
        }


class ProgressOrder:
    """
    进展偏序 + 状态等价 + 两种环路判别。

    123号§18冻结声明：
    - 不采用任意加权的万能势函数作为唯一真理
    - 比较只在同一schema、同一任务和同一权重版本下成立
    - 跨任务不直接比较这个向量
    """

    def compare(self, v_i: ProgressVector, v_j: ProgressVector) -> Dict[str, Any]:
        """
        比较两个进展向量。

        P_κ(S_i) ≺ P_κ(S_j) 当且仅当所有分量不恶化且至少一项严格改善。

        边界情况：
        - 5个分量全部恶化 → v_i ≻ v_j（恶化）
        - 4个恶化1个改善 → v_i ≺ v_j（改善——至少一项严格改善）
        - 分量值相同 → 无偏序关系（平行）
        """
        ci = v_i.to_comparison_vector()
        cj = v_j.to_comparison_vector()

        all_not_worse = all(ci_k <= cj_k for ci_k, cj_k in zip(ci, cj))
        any_strictly_better = any(ci_k < cj_k for ci_k, cj_k in zip(ci, cj))

        all_not_better = all(ci_k >= cj_k for ci_k, cj_k in zip(ci, cj))
        any_strictly_worse = any(ci_k > cj_k for ci_k, cj_k in zip(ci, cj))

        if all_not_worse and any_strictly_better:
            relation = "improved"  # v_i ≺ v_j（v_j更好）
        elif all_not_better and any_strictly_worse:
            relation = "worsened"  # v_i ≻ v_j（v_j更差）
        elif not any_strictly_better and not any_strictly_worse:
            relation = "equal"     # 平行
        else:
            relation = "incomparable"  # 有改善也有恶化——不可比较

        return {
            "relation": relation,
            "v_i": v_i.to_dict(),
            "v_j": v_j.to_dict(),
            "all_not_worse": all_not_worse,
            "any_strictly_better": any_strictly_better,
        }

    def states_equivalent(
        self,
        key_i: CanonicalKey,
        key_j: CanonicalKey,
        alpha: str = "default",
        kappa: str = "default",
    ) -> Dict[str, Any]:
        """
        判断两个状态是否等价 W_i ~_{α,κ} W_j（123号§18）。

        状态等价由任务类型κ和抽象级别α参数化。
        只有规范化键一致，才记为等价。

        边界情况：
        - 规范化键部分一致
        - 不同抽象级别α下的等价判定
        - 不同任务类型κ下的等价判定
        """
        ti = key_i.to_tuple()
        tj = key_j.to_tuple()

        is_equivalent = ti == tj

        # 计算部分一致度
        matches = sum(1 for a, b in zip(ti, tj) if a == b)
        total = len(ti)
        partial_match_ratio = matches / total if total > 0 else 0.0

        return {
            "equivalent": is_equivalent,
            "alpha": alpha,
            "kappa": kappa,
            "partial_match_ratio": partial_match_ratio,
            "key_i": key_i.to_dict(),
            "key_j": key_j.to_dict(),
        }

    def classify_loop(
        self,
        key_i: CanonicalKey,
        key_j: CanonicalKey,
        v_i: ProgressVector,
        v_j: ProgressVector,
        alpha: str = "default",
        kappa: str = "default",
    ) -> Dict[str, Any]:
        """
        判别两种环路（AGENTS.md方法论核心）。

        平面环路：不同时间事件投影回同一规范化状态，开放义务、证据门和冲突无改善 → 停止或换策略
        螺旋上升环路：返回同一抽象状态类，但更细粒度状态进展 → 允许继续并保存进展证据

        判别逻辑：
        1. 先判断状态是否等价（规范化键一致）
        2. 如果等价，看进展向量：
           - 无改善 → 平面环路
           - 有改善 → 螺旋上升环路
        3. 如果不等价 → 非环路
        """
        eq = self.states_equivalent(key_i, key_j, alpha, kappa)
        cmp = self.compare(v_i, v_j)

        if not eq["equivalent"]:
            return {
                "loop_type": LoopType.NO_LOOP.value,
                "reason": "规范化键不一致——非环路",
                "equivalent": False,
                "comparison": cmp,
            }

        # 状态等价——判断是平面还是螺旋
        if cmp["relation"] in ("equal", "worsened"):
            # 无改善或恶化 → 平面环路
            return {
                "loop_type": LoopType.PLATEAU.value,
                "reason": "同一规范化状态，进展无改善——平面环路，应停止或换策略",
                "equivalent": True,
                "comparison": cmp,
                "action": "stop_or_switch_strategy",
            }
        elif cmp["relation"] == "improved":
            # 有改善 → 螺旋上升环路
            return {
                "loop_type": LoopType.SPIRAL.value,
                "reason": "同一规范化状态，但进展向量改善——螺旋上升环路，允许继续",
                "equivalent": True,
                "comparison": cmp,
                "action": "continue_and_save_progress_evidence",
            }
        else:
            # 不可比较 → 需要人工判断
            return {
                "loop_type": "uncertain",
                "reason": "同一规范化状态，但进展向量不可比较——需要人工判断",
                "equivalent": True,
                "comparison": cmp,
                "action": "manual_review",
            }

    def compute_progress_vector(
        self,
        verified_obligation_weight: float = 0.0,
        open_obligation_weight: float = 0.0,
        unresolved_conflicts: int = 0,
        active_candidates_without_evidence: int = 0,
        cumulative_cost: float = 0.0,
    ) -> ProgressVector:
        """
        从工作区状态计算进展向量。

        v_t = 目标相关已验证义务权重
        o_t = 未释放义务权重
        c_t = 未解决冲突数
        u_t = 尚无可检验证据的活动候选数
        k_t = 累计资源成本
        """
        return ProgressVector(
            v_t=verified_obligation_weight,
            o_t=open_obligation_weight,
            c_t=unresolved_conflicts,
            u_t=active_candidates_without_evidence,
            k_t=cumulative_cost,
        )

    def compute_canonical_key(
        self,
        open_obligation_classes: List[str],
        representation_id: str,
        verified_core_proposition_ids: List[str],
        active_branches: List[str],
        evidence_gate_states: List[str],
    ) -> CanonicalKey:
        """
        从工作区状态计算规范化键。

        规范化键忽略：措辞、变量改名和事件时间。
        """
        return CanonicalKey(
            open_obligation_classes=sorted(open_obligation_classes),
            representation_id=representation_id,
            verified_core_proposition_ids=sorted(verified_core_proposition_ids),
            active_branches=sorted(active_branches),
            evidence_gate_states=sorted(evidence_gate_states),
        )

    def compare_cross_task(
        self,
        v_i: ProgressVector,
        v_j: ProgressVector,
        task_i: str,
        task_j: str,
    ) -> Dict[str, Any]:
        """
        跨任务比较规则（123号§23：跨任务只比较归一化实验结果，不直接比较|V_t|）。

        边界情况：
        - 不同任务类型的|V_t|比较（应被拒绝）
        - 同任务类型不同难度的|V_t|比较
        """
        if task_i != task_j:
            return {
                "can_compare": False,
                "reason": "跨任务不直接比较进展向量——只比较归一化实验结果（123号§23）",
                "v_i": v_i.to_dict(),
                "v_j": v_j.to_dict(),
            }

        # 同任务——可以直接比较
        cmp = self.compare(v_i, v_j)
        cmp["can_compare"] = True
        return cmp
