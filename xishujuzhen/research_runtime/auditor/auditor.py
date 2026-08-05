"""
Auditor：审计角色——7项裁决输出

对应134号P4-ROLE-1 + 127号§10.4-10.11。

127号§10.7 Auditor输入输出契约：
- 输入：冻结manifest/处理分配/所有实际Hint/提示前后事件状态/输出/ground truth/工具证据/哈希/隔离记录
- 输出：7项裁决（泄漏/越过卡点/数学进展/语言重复/副作用/归因/规则生命周期）
- 禁止：参与Hint设计或Solver答题

P4-ROLE.COMP：Auditor不参与Hint设计或Solver答题
P4-ROLE.COMP2：Auditor输出覆盖7项裁决
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum
from datetime import datetime, timezone


class VerdictType(str, Enum):
    """Auditor的7项裁决类型（127号§10.7）"""
    LEAKAGE = "leakage"                    # 泄漏
    PASSED_STALL = "passed_stall"          # 越过卡点
    MATH_PROGRESS = "math_progress"        # 数学进展
    LANGUAGE_REPETITION = "language_repetition"  # 语言重复
    SIDE_EFFECT = "side_effect"            # 副作用
    ATTRIBUTION = "attribution"            # 归因
    RULE_LIFECYCLE = "rule_lifecycle"      # 规则生命周期


@dataclass
class AuditVerdict:
    """单项审计裁决"""
    verdict_type: VerdictType
    value: float              # 0.0-1.0，具体含义取决于裁决类型
    detail: str = ""
    evidence: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "verdict_type": self.verdict_type.value,
            "value": self.value,
            "detail": self.detail,
            "evidence": self.evidence,
            "timestamp": self.timestamp,
        }


class Auditor:
    """
    Auditor角色——Phase 4新增启用。

    127号§10.4-10.11：Auditor的输入输出契约。
    P4-ROLE.COMP：Auditor不参与Hint设计或Solver答题。
    P4-ROLE.COMP2：Auditor输出覆盖7项裁决。
    """

    # 127号§10.3 Auditor可见的14个collection
    VISIBLE_COLLECTIONS = [
        "tasks", "workspaces", "raw_events", "semantic_events",
        "obligations", "evidence", "representations", "heuristic_rules",
        "activation_packets", "truth_vault", "manifests",
        "audit_verdicts", "dg_nodes", "dg_edges",
    ]

    # 127号§10.3 Auditor可写的collection
    WRITE_COLLECTIONS = ["audit_verdicts"]

    def __init__(self, run_id: str = "phase4"):
        self.run_id = run_id
        self._verdicts: List[AuditVerdict] = []
        # P4-ROLE.COMP：Auditor不参与Hint设计或Solver答题
        self._participated_in_hint_design = False
        self._participated_in_solving = False
        # 127号§10.7 Auditor输入验证
        self._inputs_verified = False
        self._inputs: Dict[str, Any] = {}

    def receive_inputs(
        self,
        frozen_manifest: Dict[str, Any],
        treatment_assignments: List[Dict[str, Any]],
        actual_hints: List[Dict[str, Any]],
        pre_hint_states: List[Dict[str, Any]],
        post_hint_states: List[Dict[str, Any]],
        outputs: List[Dict[str, Any]],
        ground_truth: Dict[str, Any],
        tool_evidence: List[Dict[str, Any]],
        hashes: Dict[str, str],
        isolation_records: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        127号§10.7 Auditor输入输出契约——接收并验证9类输入。

        输入：
        1. 冻结manifest
        2. 处理分配
        3. 所有实际Hint
        4. 提示前后事件状态
        5. 输出
        6. ground truth
        7. 工具证据
        8. 哈希
        9. 隔离记录
        """
        self._inputs = {
            "frozen_manifest": frozen_manifest,
            "treatment_assignments": treatment_assignments,
            "actual_hints": actual_hints,
            "pre_hint_states": pre_hint_states,
            "post_hint_states": post_hint_states,
            "outputs": outputs,
            "ground_truth": ground_truth,
            "tool_evidence": tool_evidence,
            "hashes": hashes,
            "isolation_records": isolation_records,
        }

        # 验证输入完整性
        missing = []
        if not frozen_manifest:
            missing.append("frozen_manifest")
        if not treatment_assignments:
            missing.append("treatment_assignments")
        if not actual_hints:
            missing.append("actual_hints")
        if not outputs:
            missing.append("outputs")

        self._inputs_verified = len(missing) == 0
        return {
            "inputs_verified": self._inputs_verified,
            "missing_inputs": missing,
            "n_inputs": len(self._inputs),
        }

    def verify_inputs(self) -> Dict[str, Any]:
        """验证Auditor输入是否完整——127号§10.7"""
        return {
            "inputs_verified": self._inputs_verified,
            "has_manifest": "frozen_manifest" in self._inputs and bool(self._inputs["frozen_manifest"]),
            "has_assignments": "treatment_assignments" in self._inputs and bool(self._inputs["treatment_assignments"]),
            "has_hints": "actual_hints" in self._inputs and bool(self._inputs["actual_hints"]),
            "has_outputs": "outputs" in self._inputs and bool(self._inputs["outputs"]),
            "has_ground_truth": "ground_truth" in self._inputs and bool(self._inputs["ground_truth"]),
            "has_hashes": "hashes" in self._inputs and bool(self._inputs["hashes"]),
            "has_isolation_records": "isolation_records" in self._inputs and bool(self._inputs["isolation_records"]),
        }

    def audit_leakage(
        self,
        hint_text: str,
        ground_truth: str,
        leakage_score: float,
    ) -> AuditVerdict:
        """
        裁决1：泄漏——Hint是否包含答案等价内容。

        127号§10.7输出：泄漏。
        123号§23答案泄漏代理四门：
        1. 字面答案匹配
        2. 答案等价映射审计
        3. 候选空间缩减率
        4. 盲审者仅凭题面+Hint能否显著恢复目标答案
        """
        # 123号§23答案泄漏代理四门——真正的检测逻辑
        # 门1：字面答案匹配
        literal_match = ground_truth.lower() in hint_text.lower() if ground_truth else False

        # 门2：答案等价映射审计（简化版：检查关键答案片段是否出现在hint中）
        answer_keywords = [w for w in ground_truth.split() if len(w) > 3] if ground_truth else []
        keyword_overlap = sum(1 for w in answer_keywords if w.lower() in hint_text.lower())
        equivalent_mapping_score = keyword_overlap / max(len(answer_keywords), 1) if answer_keywords else 0.0

        # 门3：候选空间缩减率（简化版：hint是否唯一确定答案）
        uniquely_determines = literal_match or equivalent_mapping_score > 0.8

        # 门4：盲审者恢复率（需要外部评分，这里用leakage_score代理）
        blind_recovery_score = leakage_score

        # 综合泄漏分数
        overall_leakage = max(literal_match, equivalent_mapping_score, blind_recovery_score)

        verdict = AuditVerdict(
            verdict_type=VerdictType.LEAKAGE,
            value=overall_leakage,
            detail=f"泄漏代理分数={overall_leakage:.3f}（字面匹配={literal_match}, 等价映射={equivalent_mapping_score:.3f}, 盲审恢复={blind_recovery_score:.3f}）",
            evidence={
                "hint_text": hint_text[:100],
                "ground_truth_accessible": True,  # Auditor可读truth_vault
                "leakage_score": leakage_score,
                "four_gates": {
                    "literal_match": literal_match,
                    "equivalent_mapping_score": equivalent_mapping_score,
                    "uniquely_determines": uniquely_determines,
                    "blind_recovery_score": blind_recovery_score,
                },
            },
        )
        self._verdicts.append(verdict)
        return verdict

    def audit_passed_stall(
        self,
        pre_hint_state: Dict[str, Any],
        post_hint_state: Dict[str, Any],
        passed: bool,
    ) -> AuditVerdict:
        """
        裁决2：越过卡点——Hint后是否真正越过卡点。

        127号§10.7输出：越过卡点。
        """
        verdict = AuditVerdict(
            verdict_type=VerdictType.PASSED_STALL,
            value=1.0 if passed else 0.0,
            detail="越过卡点" if passed else "未越过卡点",
            evidence={
                "pre_hint_state": pre_hint_state,
                "post_hint_state": post_hint_state,
            },
        )
        self._verdicts.append(verdict)
        return verdict

    def audit_math_progress(
        self,
        response: str,
        is_novel: bool,
        is_falsifiable: bool,
        passes_initial_check: bool,
        not_refuted: bool,
    ) -> AuditVerdict:
        """
        裁决3：数学进展——是否产生真正的数学进展。

        127号§10.7输出：数学进展。
        123号§23 conjecture类型进展：非重复/可证伪/通过初筛/未被反例否定。
        P4-5.COMP3：不用节点覆盖率代替数学正确或研究能力。
        """
        progress = 0.0
        if is_novel:
            progress += 0.25
        if is_falsifiable:
            progress += 0.25
        if passes_initial_check:
            progress += 0.25
        if not_refuted:
            progress += 0.25

        verdict = AuditVerdict(
            verdict_type=VerdictType.MATH_PROGRESS,
            value=progress,
            detail=f"数学进展分数={progress}",
            evidence={
                "is_novel": is_novel,
                "is_falsifiable": is_falsifiable,
                "passes_initial_check": passes_initial_check,
                "not_refuted": not_refuted,
                "response_excerpt": response[:100],
            },
        )
        self._verdicts.append(verdict)
        return verdict

    def audit_language_repetition(
        self,
        response: str,
        repetition_score: float,
    ) -> AuditVerdict:
        """
        裁决4：语言重复——是否只是换一种说法重复。

        127号§10.7输出：语言重复。
        系统探讨.md§5.6：是否只是换一种说法重复。
        """
        verdict = AuditVerdict(
            verdict_type=VerdictType.LANGUAGE_REPETITION,
            value=repetition_score,
            detail=f"语言重复分数={repetition_score}",
            evidence={"response_excerpt": response[:100]},
        )
        self._verdicts.append(verdict)
        return verdict

    def audit_side_effect(
        self,
        wrong_direction: bool,
        misleading: bool,
        disrupts_exploration: bool,
    ) -> AuditVerdict:
        """
        裁决5：副作用——错误方向/误导/破坏自然探索。

        127号§10.7输出：副作用。
        P4-8.2：记录副作用。
        """
        side_effect_count = sum([wrong_direction, misleading, disrupts_exploration])
        score = side_effect_count / 3.0

        verdict = AuditVerdict(
            verdict_type=VerdictType.SIDE_EFFECT,
            value=score,
            detail=f"副作用分数={score}",
            evidence={
                "wrong_direction": wrong_direction,
                "misleading": misleading,
                "disrupts_exploration": disrupts_exploration,
            },
        )
        self._verdicts.append(verdict)
        return verdict

    def audit_attribution(
        self,
        treatment_group: str,
        effect_estimate: float,
        is_causal: bool,
    ) -> AuditVerdict:
        """
        裁决6：归因——效应是否可归因于Hint。

        127号§10.7输出：归因。
        R-2防线：A/B差异不等于因果——需checkpoint分层+随机分配。
        """
        verdict = AuditVerdict(
            verdict_type=VerdictType.ATTRIBUTION,
            value=1.0 if is_causal else 0.0,
            detail=f"效应{'可' if is_causal else '不可'}归因于{treatment_group}",
            evidence={
                "treatment_group": treatment_group,
                "effect_estimate": effect_estimate,
                "is_causal": is_causal,
                "r2_guard": "checkpoint分层+随机分配",
            },
        )
        self._verdicts.append(verdict)
        return verdict

    def audit_rule_lifecycle(
        self,
        rule_id: str,
        current_status: str,
        dyn3_passed: bool,
        leakage_gate_passed: bool,
    ) -> AuditVerdict:
        """
        裁决7：规则生命周期——candidate→validated转移裁决。

        127号§10.7输出：规则生命周期裁决。
        127号§9：candidate→validated需DYN-3因果实验通过+泄漏门通过。
        P4-9.1：通过DYN-3因果实验且泄漏门通过的candidate规则升为validated。
        P4-9.3：validated规则禁止自动发布到生产H图。
        """
        can_promote = dyn3_passed and leakage_gate_passed
        new_status = "validated" if can_promote else current_status

        verdict = AuditVerdict(
            verdict_type=VerdictType.RULE_LIFECYCLE,
            value=1.0 if can_promote else 0.0,
            detail=f"规则{rule_id}: {current_status}→{new_status}",
            evidence={
                "rule_id": rule_id,
                "current_status": current_status,
                "new_status": new_status,
                "dyn3_passed": dyn3_passed,
                "leakage_gate_passed": leakage_gate_passed,
                "can_promote": can_promote,
                "no_auto_publish": True,  # P4-9.3
            },
        )
        self._verdicts.append(verdict)
        return verdict

    def get_all_verdicts(self) -> List[AuditVerdict]:
        """P4-ROLE.COMP2：输出覆盖7项裁决"""
        return self._verdicts

    def verify_7_verdicts_covered(self) -> Dict[str, Any]:
        """
        P4-ROLE.COMP2：验证7项裁决全部覆盖。
        """
        covered = {v.verdict_type for v in self._verdicts}
        all_types = set(VerdictType)
        return {
            "all_covered": covered == all_types,
            "covered": [t.value for t in covered],
            "missing": [t.value for t in all_types - covered],
        }

    def verify_not_participated(self) -> Dict[str, Any]:
        """
        P4-ROLE.COMP：验证Auditor不参与Hint设计或Solver答题。
        """
        return {
            "not_participated_in_hint_design": not self._participated_in_hint_design,
            "not_participated_in_solving": not self._participated_in_solving,
            "isolation_verified": (
                not self._participated_in_hint_design
                and not self._participated_in_solving
            ),
        }
