"""
PublishedLoader: 只加载published规则到在线运行时

对应136号P6-1。

127号§9 启发规则生命周期状态机：
- candidate: 禁止在线自动提示（R-4核心防线）
- validated: 禁止自动发布到生产H图（NO-8约束）
- published: 生产H图使用（本模块只加载这种状态）
- retired: 归档，禁止任何在线提示

G0-5预注册门：published通用规则复现标准——
跨3个未参与设计的问题族和2个模型版本复现。

159号P6-1维度19预检修正：
- 必须明确列出published标准（G0-5）
- 必须明确拒绝candidate和validated规则
- 必须明确拒绝retired规则
- 必须验证published标准（跨3问题族+2模型版本）
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from ..heuristics.rule_store import HeuristicRuleStore
from ..heuristics.models import HeuristicRule, RuleLifecycleStatus


# G0-5 published标准
PUBLISHED_MIN_PROBLEM_FAMILIES = 3
PUBLISHED_MIN_MODEL_VERSIONS = 2


class PublishedLoader:
    """
    P6-1：只加载lifecycle_status=published的规则到在线运行时。

    127号§9冻结声明：
    - candidate规则禁止在线自动提示（R-4核心防线）
    - validated规则禁止自动发布到生产H图（NO-8约束）
    - published规则可在生产H图使用
    - retired规则归档，禁止任何在线提示

    G0-5预注册门：
    - published标准：跨3个未参与设计的问题族和2个模型版本复现

    边界情况：
    - 无published规则 → 返回空列表+告警
    - published规则过多 → 分页加载
    - candidate/validated规则试图进入在线运行时 → 拒绝+告警
    - retired规则试图进入在线运行时 → 拒绝+告警
    - published规则不满足G0-5标准 → 拒绝+告警
    """

    def __init__(self, store: HeuristicRuleStore):
        self.store = store

    def load_published_rules(
        self,
        model_version: Optional[str] = None,
        applicable_domains: Optional[List[str]] = None,
        page_size: int = 100,
    ) -> Dict[str, Any]:
        """
        P6-1.1：从heuristic_rules中只加载lifecycle_status=published的规则。

        深度标准：D3——不只是加载，还要验证published标准+拒绝非published。

        边界情况：
        - 无published规则 → 返回空列表+告警
        - published规则过多 → 分页加载
        - model_version指定 → 只加载该模型版本验证过的规则
        - applicable_domains指定 → 只加载适用于这些问题族的规则
        """
        if self.store.in_memory:
            all_docs = list(self.store._memory_store.values())
        else:
            cursor = self.store.col.all()
            all_docs = list(cursor)

        published_rules: List[HeuristicRule] = []
        rejected: List[Dict[str, Any]] = []
        warnings: List[str] = []

        for doc in all_docs:
            doc_copy = dict(doc)
            doc_copy.pop("_id", None)
            doc_copy.pop("_rev", None)
            doc_copy.pop("_key", None)
            rule = HeuristicRule.from_dict(doc_copy)

            status = rule.status

            if status == RuleLifecycleStatus.PUBLISHED:
                # 验证G0-5 published标准
                g0_5_check = self._validate_published_standard(rule)
                if not g0_5_check["satisfies_g0_5"]:
                    rejected.append({
                        "rule_id": rule.rule_id,
                        "status": status.value,
                        "reason": "不满足G0-5 published标准",
                        "g0_5_check": g0_5_check,
                    })
                    continue

                # 按model_version过滤
                if model_version and model_version not in rule.model_versions:
                    continue

                # 按applicable_domains过滤
                if applicable_domains:
                    if not any(d in rule.applicable_domains for d in applicable_domains):
                        continue

                published_rules.append(rule)
            else:
                # 拒绝非published规则
                rejected.append({
                    "rule_id": rule.rule_id,
                    "status": status.value,
                    "reason": self._rejection_reason(status),
                })

        # 分页
        total = len(published_rules)
        if total > page_size:
            warnings.append(
                f"published规则过多（{total}条），已分页加载前{page_size}条"
            )
            published_rules = published_rules[:page_size]

        if total == 0:
            warnings.append("无published规则可加载——在线运行时将无规则可用")

        return {
            "loaded": True,
            "published_rules": [r.to_dict() for r in published_rules],
            "n_loaded": len(published_rules),
            "n_total_published": total,
            "rejected": rejected,
            "warnings": warnings,
            "r4_defense": True,   # candidate规则未被加载
            "no8_defense": True,  # validated规则未被加载到生产H图
        }

    def _validate_published_standard(self, rule: HeuristicRule) -> Dict[str, Any]:
        """
        P6-1.2：验证published规则满足G0-5标准。

        G0-5（123号§44）：published通用规则至少跨3个**未参与设计**的问题族
        和2个模型版本复现。

        关键修正：不只检查applicable_domains数量≥3，还要验证其中至少3个
        是"未参与设计"的问题族（applicable_domains - design_participation_domains >= 3）。

        边界情况：
        - applicable_domains少于3 → 不满足
        - model_versions少于2 → 不满足
        - applicable_domains或model_versions为空 → 不满足
        - 所有applicable_domains都参与了设计 → 不满足（无独立验证）
        """
        n_domains = len(rule.applicable_domains)
        n_versions = len(rule.model_versions)

        # 关键修正：计算"未参与设计"的问题族
        design_set = set(rule.design_participation_domains)
        non_design_domains = [d for d in rule.applicable_domains if d not in design_set]
        n_non_design = len(non_design_domains)

        domains_ok = n_non_design >= PUBLISHED_MIN_PROBLEM_FAMILIES
        versions_ok = n_versions >= PUBLISHED_MIN_MODEL_VERSIONS

        return {
            "satisfies_g0_5": domains_ok and versions_ok,
            "n_applicable_domains": n_domains,
            "n_model_versions": n_versions,
            "n_design_participation": len(design_set),
            "n_non_design_domains": n_non_design,  # 关键：未参与设计的问题族数
            "non_design_domains": non_design_domains,
            "min_domains_required": PUBLISHED_MIN_PROBLEM_FAMILIES,
            "min_versions_required": PUBLISHED_MIN_MODEL_VERSIONS,
            "domains_ok": domains_ok,
            "versions_ok": versions_ok,
            "g0_5_correction": "验证未参与设计的问题族数≥3，不只是总applicable_domains数",
        }

    def _rejection_reason(self, status: RuleLifecycleStatus) -> str:
        """根据状态返回拒绝原因"""
        if status == RuleLifecycleStatus.CANDIDATE:
            return "candidate规则禁止在线自动提示（R-4核心防线，127号§9）"
        elif status == RuleLifecycleStatus.VALIDATED:
            return "validated规则禁止自动发布到生产H图（NO-8约束，127号§9）"
        elif status == RuleLifecycleStatus.RETIRED:
            return "retired规则归档，禁止任何在线提示（127号§9）"
        else:
            return f"未知状态{status.value}"

    def validate_no_candidate(self, rules: List[HeuristicRule]) -> Dict[str, Any]:
        """
        P6-1.3：验证加载的规则中无candidate状态。

        R-4核心防线：candidate规则不被在线运行时加载。

        边界情况：发现candidate规则 → 拒绝
        """
        candidate_rules = [
            r for r in rules if r.status == RuleLifecycleStatus.CANDIDATE
        ]

        return {
            "no_candidate": len(candidate_rules) == 0,
            "n_candidate_found": len(candidate_rules),
            "candidate_rule_ids": [r.rule_id for r in candidate_rules],
            "r4_defense": len(candidate_rules) == 0,
        }

    def validate_no_validated_in_production(
        self, rules: List[HeuristicRule]
    ) -> Dict[str, Any]:
        """
        P6-1.4：验证validated规则不自动进入生产H图。

        NO-8约束：不让在线一次成功自动写入production H。

        边界情况：发现validated规则 → 拒绝
        """
        validated_rules = [
            r for r in rules if r.status == RuleLifecycleStatus.VALIDATED
        ]

        return {
            "no_validated_in_production": len(validated_rules) == 0,
            "n_validated_found": len(validated_rules),
            "validated_rule_ids": [r.rule_id for r in validated_rules],
            "no8_defense": len(validated_rules) == 0,
        }

    def validate_published_standard_batch(
        self, rules: List[HeuristicRule]
    ) -> Dict[str, Any]:
        """
        P6-1.5：批量验证published规则满足G0-5标准。

        边界情况：某规则不满足G0-5 → 标记并拒绝
        """
        results = []
        all_satisfy = True

        for rule in rules:
            if rule.status != RuleLifecycleStatus.PUBLISHED:
                continue
            check = self._validate_published_standard(rule)
            if not check["satisfies_g0_5"]:
                all_satisfy = False
            results.append({
                "rule_id": rule.rule_id,
                "satisfies_g0_5": check["satisfies_g0_5"],
                "n_domains": check["n_applicable_domains"],
                "n_versions": check["n_model_versions"],
            })

        return {
            "all_satisfy_g0_5": all_satisfy,
            "n_checked": len(results),
            "results": results,
        }

    def verify_p6_1_compliance(self, loaded_rules: List[HeuristicRule]) -> Dict[str, Any]:
        """
        P6-1.COMP：完整合规性验证。

        - P6-1.COMP：只加载published规则
        - P6-1.COMP2：不让在线一次成功自动写入production H（NO-8约束）
        - P6-1.COMP3：candidate规则不进入在线运行时（R-4防线）
        - P6-1.COMP4：retired规则不进入在线运行时
        """
        no_candidate = self.validate_no_candidate(loaded_rules)
        no_validated = self.validate_no_validated_in_production(loaded_rules)
        g0_5_check = self.validate_published_standard_batch(loaded_rules)

        # 检查retired规则
        retired_rules = [
            r for r in loaded_rules if r.status == RuleLifecycleStatus.RETIRED
        ]

        return {
            "compliant": (
                no_candidate["no_candidate"]
                and no_validated["no_validated_in_production"]
                and g0_5_check["all_satisfy_g0_5"]
                and len(retired_rules) == 0
            ),
            "only_published": all(
                r.status == RuleLifecycleStatus.PUBLISHED for r in loaded_rules
            ),
            "no_candidate": no_candidate,
            "no_validated_in_production": no_validated,
            "g0_5_standard": g0_5_check,
            "no_retired": len(retired_rules) == 0,
            "n_retired_found": len(retired_rules),
            "r4_defense": no_candidate["r4_defense"],
            "no8_defense": no_validated["no8_defense"],
        }
