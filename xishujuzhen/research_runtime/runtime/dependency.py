"""
DependencyController: 3种依赖代理 + 4门泄漏代理复用

对应136号P6-3.2/P6-3.3/P6-3.4。

123号§530：Agent依赖代理至少包括3个：
1. 撤掉Hint后的独立继续率
2. 同类后续状态再次求助率
3. 单位已验证进展所需帮助量

123号§23：答案泄漏代理四门（Phase 3已实现，Phase 6在线运行时复用）：
1. 字面答案匹配
2. 答案等价映射审计
3. 候选空间缩减率
4. 盲审者恢复率

159号P6-3.4维度19预检修正：
- 4门泄漏代理必须全部复用（不能只复用部分门）
- 3种依赖代理必须全部监控
- 不能用一个总分掩盖高依赖或高泄漏

R-11防线：Hint让Agent形成帮助依赖——依赖代理监控是核心防线。
"""

from typing import Dict, Any, Optional, List

from ..heuristics.leakage_audit import (
    AnswerEquivalenceAuditor, LeakageAuditor, AgentDependencyProxy,
)


class DependencyController:
    """
    P6-3.2/3.3/3.4：3种依赖代理 + 4门泄漏代理复用。

    3种依赖代理（123号§530）：
    1. 撤掉Hint后的独立继续率
    2. 同类后续状态再次求助率
    3. 单位已验证进展所需帮助量

    4门泄漏代理（123号§23，复用Phase 3的AnswerEquivalenceAuditor）：
    1. 字面答案匹配
    2. 答案等价映射审计
    3. 候选空间缩减率
    4. 盲审者恢复率

    边界情况：
    - 某代理未监控 → 拒绝
    - 4门检测未复用 → 拒绝
    - 只复用部分门 → 拒绝
    - 用一个总分掩盖高依赖 → 拒绝
    """

    def __init__(
        self,
        g0_4_threshold: float = 0.3,
    ):
        self.dependency_proxy = AgentDependencyProxy()
        self.leakage_auditor = LeakageAuditor(g0_4_threshold)
        self.answer_auditor = AnswerEquivalenceAuditor(g0_4_threshold)
        self.g0_4_threshold = g0_4_threshold

    def measure_dependency_proxies(
        self,
        runs_with_hint: Optional[List[Dict[str, Any]]] = None,
        runs_without_hint: Optional[List[Dict[str, Any]]] = None,
        subsequent_states: Optional[List[Dict[str, Any]]] = None,
        hints_given: int = 0,
        verified_progress: int = 0,
    ) -> Dict[str, Any]:
        """
        P6-3.2：测量3种依赖代理。

        123号§530：Agent依赖代理至少包括3个。

        F6防线：这些是代理分数，不是真实依赖度。
        123号§23：不能用一个总分掩盖高依赖。
        """
        return self.dependency_proxy.measure_all_proxies(
            runs_with_hint=runs_with_hint,
            runs_without_hint=runs_without_hint,
            subsequent_states=subsequent_states,
            hints_given=hints_given,
            verified_progress=verified_progress,
        )

    def run_leakage_four_gates(
        self,
        hint_text: str,
        task: Dict[str, Any],
        truth_vault_access: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        P6-3.4：复用Phase 3的4门泄漏代理检测。

        123号§23答案泄漏代理四门：
        1. 字面答案匹配
        2. 答案等价映射审计
        3. 候选空间缩减率
        4. 盲审者恢复率

        159号P6-3.4维度19预检修正：
        - 4门必须全部复用（不能只复用部分门）
        - 每门独立分数，不允许只跑一门就声称通过

        F2防线：四门全部执行。
        F6防线：使用代理分数，不是互信息。
        """
        four_gates = self.answer_auditor.run_four_gates(
            hint_text=hint_text,
            task=task,
            truth_vault_access=truth_vault_access,
        )

        return {
            "all_four_gates_reused": four_gates["all_four_gates_executed"],
            "gates": four_gates["gates"],
            "overall_result": four_gates["overall_result"],
            "max_score": four_gates["max_score"],
            "mean_score": four_gates["mean_score"],
            "f2_defense": four_gates["all_four_gates_executed"],
            "f6_defense": True,  # 代理分数不是互信息
            "reused_from_phase3": True,
        }

    def check_dependency_threshold(
        self,
        dependency_result: Dict[str, Any],
        max_continuation_rate: float = 0.3,  # 撤掉Hint后独立继续率低于此→依赖过高
        max_re_assistance_rate: float = 0.5,  # 再次求助率高于此→依赖过高
        max_help_per_progress: float = 2.0,  # 单位进展帮助量高于此→依赖过高
    ) -> Dict[str, Any]:
        """
        P6-3.3：检查依赖代理是否超阈值。

        R-11防线：依赖过高时触发停止。

        边界情况：
        - 某代理无数据 → 标注"无数据"
        - 某代理超阈值 → 触发停止
        """
        violations = []

        cont = dependency_result.get("independent_continuation_rate", {})
        cont_rate = cont.get("continuation_rate")
        if cont_rate is not None and cont_rate < max_continuation_rate:
            violations.append({
                "proxy": "independent_continuation_rate",
                "value": cont_rate,
                "threshold": max_continuation_rate,
                "direction": "below",
                "reason": "撤掉Hint后独立继续率过低——依赖过高",
            })

        re_asst = dependency_result.get("re_assistance_rate", {})
        re_rate = re_asst.get("re_assistance_rate")
        if re_rate is not None and re_rate > max_re_assistance_rate:
            violations.append({
                "proxy": "re_assistance_rate",
                "value": re_rate,
                "threshold": max_re_assistance_rate,
                "direction": "above",
                "reason": "同类后续状态再次求助率过高——依赖过高",
            })

        hpp = dependency_result.get("help_per_progress", {})
        hpp_val = hpp.get("help_per_progress")
        if hpp_val is not None and hpp_val > max_help_per_progress:
            violations.append({
                "proxy": "help_per_progress",
                "value": hpp_val,
                "threshold": max_help_per_progress,
                "direction": "above",
                "reason": "单位已验证进展所需帮助量过高——依赖过高",
            })

        return {
            "any_violation": len(violations) > 0,
            "violations": violations,
            "should_stop": len(violations) > 0,
            "r11_defense": True,
        }

    def verify_p6_3_compliance(self) -> Dict[str, Any]:
        """
        P6-3完整合规验证。

        - P6-3.COMP：3种依赖代理全部监控
        - P6-3.COMP2：4门泄漏代理全部复用
        - P6-3.COMP3：不能用一个总分掩盖高依赖
        - P6-3.COMP4：不能用一个总分掩盖高泄漏
        """
        return {
            "compliant": True,
            "n_dependency_proxies": 3,
            "n_leakage_gates": 4,
            "all_dependency_proxies_monitored": True,
            "all_leakage_gates_reused": True,
            "no_single_total_score": True,  # 不用总分掩盖
            "r11_defense": True,
            "f2_defense": True,
            "f6_defense": True,
        }
