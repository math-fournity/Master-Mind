"""
PilotRunner：Pilot实验运行器——G0-3/G0-4方差估计

对应134号P4-0（G0-3/G0-4预注册门冻结前的pilot）。

123号§44："每个DYN protocol必须先用独立pilot估计方差"。
G0-6：阈值不能在看完结果后补写。

Pilot的预注册（在pilot结果前冻结）：
- pilot样本量：每处理组5次continuation（共20次）
- pilot只用于估计方差，不用于假设检验
- pilot结果不作为Phase 4出口门证据
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple
import statistics

from .llm_backend import LLMBackend
from .checkpoint_layer import CheckpointLayerExperiment, Checkpoint
from .treatment_groups import TreatmentGroupDesigner, TreatmentGroup
from .effect_estimator import ContinuationResult, EffectEstimator


@dataclass
class PilotVarianceEstimate:
    """Pilot方差估计结果——用于冻结G0-3/G0-4"""
    # 效应大小方差
    effect_size_mean: float = 0.0
    effect_size_variance: float = 0.0
    effect_size_std: float = 0.0
    # 泄漏代理方差
    leakage_mean: float = 0.0
    leakage_variance: float = 0.0
    # 样本量
    n_per_group: int = 5
    n_total: int = 0
    # 建议的G0-3冻结值
    suggested_delta: float = 0.0
    suggested_sample_size: int = 0
    # 建议的G0-4冻结值
    suggested_leakage_threshold: float = 0.0

    def to_dict(self) -> dict:
        return {
            "effect_size_mean": self.effect_size_mean,
            "effect_size_variance": self.effect_size_variance,
            "effect_size_std": self.effect_size_std,
            "leakage_mean": self.leakage_mean,
            "leakage_variance": self.leakage_variance,
            "n_per_group": self.n_per_group,
            "n_total": self.n_total,
            "suggested_delta": self.suggested_delta,
            "suggested_sample_size": self.suggested_sample_size,
            "suggested_leakage_threshold": self.suggested_leakage_threshold,
        }


class PilotRunner:
    """
    Pilot实验运行器——估计方差以冻结G0-3/G0-4。

    Pilot的预注册（在pilot结果前冻结）：
    - pilot样本量：每处理组5次continuation（共20次）
    - pilot只用于估计方差，不用于假设检验
    - pilot结果不作为Phase 4出口门证据
    """

    PILOT_N_PER_GROUP = 5  # 预注册：每处理组5次

    def __init__(
        self,
        llm_backend: LLMBackend,
        checkpoint_layer: CheckpointLayerExperiment,
        treatment_designer: TreatmentGroupDesigner,
        effect_estimator: EffectEstimator,
    ):
        self.llm = llm_backend
        self.checkpoint_layer = checkpoint_layer
        self.treatment_designer = treatment_designer
        self.effect_estimator = effect_estimator

    def run_pilot(
        self,
        checkpoint: Checkpoint,
        task_prompt: str,
    ) -> Tuple[List[ContinuationResult], PilotVarianceEstimate]:
        """
        运行pilot实验——每处理组5次continuation。

        边界情况：
        - pilot效应为零（无法估计方差→取保守δ）
        - pilot方差过大（需要大样本→成本评估）
        - continuation生成失败（排除并记录）
        """
        groups = [g.value for g in TreatmentGroup]
        assignments = self.checkpoint_layer.assign_continuations(
            checkpoint, self.PILOT_N_PER_GROUP, groups
        )

        results: List[ContinuationResult] = []
        for assignment in assignments:
            group = TreatmentGroup(assignment.treatment_group)
            prompt = self.treatment_designer.build_prompt(group, task_prompt)
            try:
                response, record = self.llm.generate_with_record(prompt)
                result = self._evaluate_pilot_response(
                    assignment, response, checkpoint.checkpoint_id
                )
                results.append(result)
            except Exception as e:
                # 排除标准：continuation生成失败
                results.append(ContinuationResult(
                    assignment_id=assignment.assignment_id,
                    treatment_group=assignment.treatment_group,
                    checkpoint_id=checkpoint.checkpoint_id,
                    response=f"PILOT_ERROR: {str(e)}",
                ))

        variance_estimate = self._estimate_variance(results)
        return results, variance_estimate

    def _evaluate_pilot_response(
        self,
        assignment: ContinuationAssignment,
        response: str,
        checkpoint_id: str,
    ) -> ContinuationResult:
        """评估pilot响应（简化版——与ExperimentRunner一致）"""
        is_novel = "底数" in response and "指数" in response
        is_falsifiable = "猜测" in response or "≥" in response or "≤" in response
        passes_initial_check = len(response) > 50
        not_refuted = "矛盾" not in response and "错误" not in response.lower()

        return ContinuationResult(
            assignment_id=assignment.assignment_id,
            treatment_group=assignment.treatment_group,
            checkpoint_id=checkpoint_id,
            response=response,
            is_novel=is_novel,
            is_falsifiable=is_falsifiable,
            passes_initial_check=passes_initial_check,
            not_refuted=not_refuted,
        )

    def _estimate_variance(
        self, results: List[ContinuationResult]
    ) -> PilotVarianceEstimate:
        """
        从pilot结果估计方差——用于冻结G0-3/G0-4。

        123号§44："每个DYN protocol必须先用独立pilot估计方差"。
        """
        # 按处理组分组
        by_group: Dict[str, List[ContinuationResult]] = {}
        for r in results:
            by_group.setdefault(r.treatment_group, []).append(r)

        # 计算每组的进展分数
        group_means = {}
        for group, group_results in by_group.items():
            scores = [self.effect_estimator.compute_progress_score(r) for r in group_results]
            group_means[group] = statistics.mean(scores) if scores else 0.0

        # 效应大小 = treatment - control
        control_mean = group_means.get("control", 0.0)
        effect_sizes = []
        for group, mean in group_means.items():
            if group != "control":
                effect_sizes.append(mean - control_mean)

        if effect_sizes:
            eff_mean = statistics.mean(effect_sizes)
            eff_var = statistics.variance(effect_sizes) if len(effect_sizes) > 1 else 0.0
            eff_std = eff_var ** 0.5
        else:
            eff_mean = 0.0
            eff_var = 0.0
            eff_std = 0.0

        # 建议G0-3冻结值
        # δ取保守值：效应大小均值的一半（不要求大效应）
        suggested_delta = max(0.10, abs(eff_mean) * 0.5) if eff_mean != 0 else 0.10
        # 样本量：用方差和δ做简单功效分析（简化版）
        # n ≈ (1.96 * std / delta)^2，95%置信度
        if suggested_delta > 0 and eff_std > 0:
            suggested_n = max(15, int((1.96 * eff_std / suggested_delta) ** 2))
        else:
            suggested_n = 15  # 默认最小样本量

        # 建议G0-4冻结值（泄漏门阈值）
        # 取保守值0.3（123号§23默认）
        suggested_leakage = 0.30

        return PilotVarianceEstimate(
            effect_size_mean=eff_mean,
            effect_size_variance=eff_var,
            effect_size_std=eff_std,
            n_per_group=self.PILOT_N_PER_GROUP,
            n_total=len(results),
            suggested_delta=suggested_delta,
            suggested_sample_size=suggested_n,
            suggested_leakage_threshold=suggested_leakage,
        )
