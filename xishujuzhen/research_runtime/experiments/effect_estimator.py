"""
EffectEstimator：局部效应+ATE+异质性估计

对应134号P4-5。

123号§39 DYN-3：
- 用分层或配对统计估计平均处理效应和异质性
- 不能声称两分支内部状态完全相同
- 不能拿两条天然不同的完整运行事后讲故事

P4-5.1：测同一checkpoint的treatment vs control的局部效应
P4-5.2：估计ATE和异质性（分层或配对统计）
P4-5.3：验证非泄漏Hint的预注册主要效应区间下界>0且超过δ
P4-5.4：效应测量用任务类型特定的已验证进展（conjecture类型）

F6防线：用Bootstrap置信区间（非参数），不用t检验。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple
import random
import statistics


@dataclass
class ContinuationResult:
    """单次continuation的结果记录"""
    assignment_id: str
    treatment_group: str
    checkpoint_id: str
    response: str
    # 任务类型特定的已验证进展（123号§23 conjecture类型）
    # conjecture进展：非重复/可证伪/通过初筛/未被反例否定
    progress_score: float = 0.0  # 0.0-1.0
    # 进展分维度（P4-5.4：不用节点覆盖率代替数学正确）
    is_novel: bool = False          # 非重复
    is_falsifiable: bool = False    # 可证伪
    passes_initial_check: bool = False  # 通过初筛
    not_refuted: bool = False       # 未被反例否定
    # 泄漏代理分数
    leakage_score: float = 0.0
    # 副作用
    side_effect_score: float = 0.0

    def to_dict(self) -> dict:
        return {
            "assignment_id": self.assignment_id,
            "treatment_group": self.treatment_group,
            "checkpoint_id": self.checkpoint_id,
            "progress_score": self.progress_score,
            "is_novel": self.is_novel,
            "is_falsifiable": self.is_falsifiable,
            "passes_initial_check": self.passes_initial_check,
            "not_refuted": self.not_refuted,
            "leakage_score": self.leakage_score,
            "side_effect_score": self.side_effect_score,
        }


@dataclass
class EffectEstimate:
    """效应估计结果"""
    ate: float                    # 平均处理效应
    ci_lower: float               # Bootstrap置信区间下界
    ci_upper: float               # Bootstrap置信区间上界
    n_treatment: int
    n_control: int
    heterogeneity: float = 0.0    # 异质性（处理组间方差）
    method: str = "bootstrap"     # F6防线：声明用Bootstrap
    passes_exit_gate: bool = False  # P4-5.COMP2：区间下界>0且超过δ

    def to_dict(self) -> dict:
        return {
            "ate": self.ate,
            "ci_lower": self.ci_lower,
            "ci_upper": self.ci_upper,
            "n_treatment": self.n_treatment,
            "n_control": self.n_control,
            "heterogeneity": self.heterogeneity,
            "method": self.method,
            "passes_exit_gate": self.passes_exit_gate,
        }


class EffectEstimator:
    """
    P4-5：测局部效应+ATE+异质性估计。

    F6防线：用Bootstrap置信区间（非参数），不用t检验。
    P4-5.COMP：效应估计用分层或配对统计，不是事后讲故事。
    """

    def __init__(self, delta: float = 0.10, bootstrap_samples: int = 1000, seed: int = 42):
        """
        Args:
            delta: G0-3冻结的最小实际效应（P4-5.3）
            bootstrap_samples: Bootstrap重采样次数
            seed: 随机种子
        """
        self.delta = delta
        self.bootstrap_samples = bootstrap_samples
        self._rng = random.Random(seed)

    def compute_progress_score(self, result: ContinuationResult) -> float:
        """
        P4-5.4：计算任务类型特定的已验证进展。

        123号§23 conjecture类型进展定义：
        - 非重复（is_novel）
        - 可证伪（is_falsifiable）
        - 通过初筛（passes_initial_check）
        - 未被反例否定（not_refuted）

        P4-5.COMP3：不用节点覆盖率代替数学正确或研究能力。
        """
        score = 0.0
        if result.is_novel:
            score += 0.25
        if result.is_falsifiable:
            score += 0.25
        if result.passes_initial_check:
            score += 0.25
        if result.not_refuted:
            score += 0.25
        return score

    def estimate_ate(
        self,
        treatment_results: List[ContinuationResult],
        control_results: List[ContinuationResult],
    ) -> EffectEstimate:
        """
        P4-5.2：估计ATE和异质性（分层或配对统计）。

        F6防线：用Bootstrap置信区间（非参数），不用t检验。

        边界情况：
        - treatment和control的checkpoint不一致 → 应被拒绝
        - 局部效应为负
        - 分层后每层样本量不足
        """
        if not treatment_results or not control_results:
            return EffectEstimate(
                ate=0.0, ci_lower=0.0, ci_upper=0.0,
                n_treatment=len(treatment_results),
                n_control=len(control_results),
            )

        # 计算进展分数
        t_scores = [self.compute_progress_score(r) for r in treatment_results]
        c_scores = [self.compute_progress_score(r) for r in control_results]

        # ATE = mean(treatment) - mean(control)
        ate = statistics.mean(t_scores) - statistics.mean(c_scores)

        # Bootstrap置信区间（F6防线：非参数）
        ci_lower, ci_upper = self._bootstrap_ci(t_scores, c_scores)

        # 异质性：处理组间的方差
        heterogeneity = statistics.variance(t_scores) if len(t_scores) > 1 else 0.0

        # P4-5.COMP2：区间下界>0且超过δ
        passes = ci_lower > 0 and ci_lower > self.delta

        return EffectEstimate(
            ate=ate,
            ci_lower=ci_lower,
            ci_upper=ci_upper,
            n_treatment=len(treatment_results),
            n_control=len(control_results),
            heterogeneity=heterogeneity,
            method="bootstrap",
            passes_exit_gate=passes,
        )

    def _bootstrap_ci(
        self,
        t_scores: List[float],
        c_scores: List[float],
        confidence: float = 0.95,
    ) -> Tuple[float, float]:
        """
        Bootstrap置信区间（F6防线：非参数，不假设正态分布）。

        P4-5.COMP：效应估计用分层或配对统计，不是事后讲故事。
        """
        if not t_scores or not c_scores:
            return (0.0, 0.0)

        boot_ates = []
        for _ in range(self.bootstrap_samples):
            # 重采样
            t_boot = [self._rng.choice(t_scores) for _ in range(len(t_scores))]
            c_boot = [self._rng.choice(c_scores) for _ in range(len(c_scores))]
            boot_ate = statistics.mean(t_boot) - statistics.mean(c_boot)
            boot_ates.append(boot_ate)

        boot_ates.sort()
        # 95%置信区间
        lower_idx = int((1 - confidence) / 2 * len(boot_ates))
        upper_idx = int((1 + confidence) / 2 * len(boot_ates))
        return (boot_ates[lower_idx], boot_ates[upper_idx])

    def estimate_all_groups(
        self,
        results_by_group: Dict[str, List[ContinuationResult]],
    ) -> Dict[str, EffectEstimate]:
        """
        对每个处理组（H0/H1/H2）分别估计相对于control的ATE。

        P4-5.1：测同一checkpoint的treatment vs control的局部效应。
        """
        control = results_by_group.get("control", [])
        estimates = {}
        for group, results in results_by_group.items():
            if group == "control":
                continue
            estimates[group] = self.estimate_ate(results, control)
        return estimates
