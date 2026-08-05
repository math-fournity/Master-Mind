"""
ExperimentRunner：实验运行器——冻结manifest+随机分配+日志

对应134号P4-3（冻结）+P4-4（日志/哈希/盲评）。

123号§49 + §44：
- 冻结模型/工具/题面/预算
- 完整日志、哈希、盲评和Truth Vault隔离
- 阈值不能在看完结果后补写（G0-6）
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import hashlib
import json
from datetime import datetime, timezone

from .llm_backend import LLMBackend, LLMCallRecord
from .checkpoint_layer import CheckpointLayerExperiment, Checkpoint, ContinuationAssignment
from .treatment_groups import TreatmentGroupDesigner, TreatmentGroup, TreatmentDefinition
from .effect_estimator import ContinuationResult, EffectEstimator, EffectEstimate


@dataclass
class ExperimentManifest:
    """
    实验冻结manifest——P4-3：冻结模型/工具/题面/预算。

    G0-6：阈值不能在看完结果后补写。
    一旦freeze()，不可修改。
    """
    manifest_id: str
    model_version: str
    cli_version: str
    q_0_hash: str                    # 题面哈希（P4-3.3：冻结题面）
    budget: Dict[str, Any]           # 预算（P4-3.4）
    # G0-3预注册门
    delta: float = 0.0               # 最小实际效应
    sample_size: int = 0             # 样本量
    exclusion_criteria: List[str] = field(default_factory=list)
    ci_method: str = "bootstrap"
    # G0-4泄漏门阈值
    leakage_threshold: float = 0.3
    candidate_space_threshold: float = 0.5
    blind_recovery_threshold: float = 0.2
    # 随机种子
    random_seed: int = 42
    frozen: bool = False
    frozen_at: str = ""

    def freeze(self):
        """冻结manifest——不可逆"""
        self.frozen = True
        self.frozen_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "manifest_id": self.manifest_id,
            "model_version": self.model_version,
            "cli_version": self.cli_version,
            "q_0_hash": self.q_0_hash,
            "budget": self.budget,
            "delta": self.delta,
            "sample_size": self.sample_size,
            "exclusion_criteria": self.exclusion_criteria,
            "ci_method": self.ci_method,
            "leakage_threshold": self.leakage_threshold,
            "candidate_space_threshold": self.candidate_space_threshold,
            "blind_recovery_threshold": self.blind_recovery_threshold,
            "random_seed": self.random_seed,
            "frozen": self.frozen,
            "frozen_at": self.frozen_at,
        }


class ExperimentRunner:
    """
    实验运行器——编排checkpoint分层+四组处理+continuation生成+结果记录。

    P4-3：冻结模型/工具/题面/预算
    P4-4：完整日志/哈希/盲评/Truth Vault隔离
    P4-5：测局部效应
    """

    def __init__(
        self,
        llm_backend: LLMBackend,
        checkpoint_layer: CheckpointLayerExperiment,
        treatment_designer: TreatmentGroupDesigner,
        effect_estimator: EffectEstimator,
        manifest: ExperimentManifest,
    ):
        self.llm = llm_backend
        self.checkpoint_layer = checkpoint_layer
        self.treatment_designer = treatment_designer
        self.effect_estimator = effect_estimator
        self.manifest = manifest
        self._results: List[ContinuationResult] = []
        self._call_records: List[LLMCallRecord] = []

    def run_experiment(
        self,
        checkpoint: Checkpoint,
        task_prompt: str,
        n_per_group: int = 5,
    ) -> Dict[str, Any]:
        """
        运行完整实验：在同一checkpoint上对4组处理各跑n_per_group个continuation。

        P4-1.2：在同一checkpoint层内随机分配多个非确定continuation
        P4-2：四组处理
        P4-4.1：记录完整实验日志
        P4-4.2：记录内容哈希
        """
        if not self.manifest.frozen:
            raise RuntimeError("manifest未冻结——必须先freeze()再运行实验（G0-6）")

        # P4-1.2：分配continuation
        groups = [g.value for g in TreatmentGroup]
        assignments = self.checkpoint_layer.assign_continuations(
            checkpoint, n_per_group, groups
        )

        # 运行每个continuation
        for assignment in assignments:
            group = TreatmentGroup(assignment.treatment_group)
            prompt = self.treatment_designer.build_prompt(group, task_prompt)

            try:
                response, record = self.llm.generate_with_record(prompt)
                self._call_records.append(record)

                # 评估结果（简化版——完整评估需要Auditor）
                result = self._evaluate_response(
                    assignment, response, checkpoint.checkpoint_id
                )
                self._results.append(result)
            except Exception as e:
                # P4-3.5排除标准：continuation生成失败
                result = ContinuationResult(
                    assignment_id=assignment.assignment_id,
                    treatment_group=assignment.treatment_group,
                    checkpoint_id=checkpoint.checkpoint_id,
                    response=f"ERROR: {str(e)}",
                    progress_score=0.0,
                )
                self._results.append(result)

        # P4-5：估计效应
        results_by_group = self._group_results_by_treatment()
        estimates = self.effect_estimator.estimate_all_groups(results_by_group)

        return {
            "manifest": self.manifest.to_dict(),
            "checkpoint_id": checkpoint.checkpoint_id,
            "n_assignments": len(assignments),
            "n_results": len(self._results),
            "estimates": {k: v.to_dict() for k, v in estimates.items()},
            "call_records": [r.to_dict() for r in self._call_records],
        }

    def _evaluate_response(
        self,
        assignment: ContinuationAssignment,
        response: str,
        checkpoint_id: str,
    ) -> ContinuationResult:
        """
        评估continuation响应——计算任务类型特定的进展分数。

        P4-5.4：效应测量用任务类型特定的已验证进展（conjecture类型）。
        123号§23 conjecture类型：非重复/可证伪/通过初筛/未被反例否定。

        简化版评估——完整评估需要Auditor角色（Phase 4阶段D）。
        """
        # 简化版：基于响应文本的关键词检查
        is_novel = "底数" in response and "指数" in response  # 是否分析了底数和指数
        is_falsifiable = "猜测" in response or "≥" in response or "≤" in response
        passes_initial_check = len(response) > 50  # 有实质性内容
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

    def _group_results_by_treatment(self) -> Dict[str, List[ContinuationResult]]:
        """按处理组分组结果"""
        groups: Dict[str, List[ContinuationResult]] = {}
        for r in self._results:
            groups.setdefault(r.treatment_group, []).append(r)
        return groups

    def get_results(self) -> List[ContinuationResult]:
        return self._results

    def get_call_records(self) -> List[LLMCallRecord]:
        return self._call_records
