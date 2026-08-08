"""
提示梯度模块（261号§4.5）。

按261号§4.5的实现路径，对同一义务ID的规则按Level排列形成梯度，
从高Level（低泄漏）到低Level（高泄漏）。
当某条规则泄漏风险>0.5时，降级到更高Level（更低泄漏）的替代规则。

梯度级别定义（基于Level和非特定性）：
- Level 1.0（元检查/思维操作）："你现在有什么？还缺什么？"
- Level 0.3（方向暗示）："注意稳定性方程中的量D"
- Level 0.5（量级感知）："D能等于0吗？至少有多大？"（Q8）
- Level 0.2（知识注入）："用badly approximable性质"（Q9）

降级触发条件：leakage_risk > 0.5
降级路径：从高泄漏级别降到低泄漏级别（即Level升高）
"""

from typing import List, Optional

from ..hgraph.hgraph_store import HeuristicRule, HeuristicRuleGraph
from ..policy.constrained_optimizer import MatchedRule, leakage_risk


# ---------------------------------------------------------------------------
# 梯度级别定义（261号§4.5）
# ---------------------------------------------------------------------------

# (Level, 提示文本) —— 从高Level（低泄漏）到低Level（高泄漏）
_GRADIENT_LEVELS = [
    (1.0, "你现在有什么？还缺什么？"),          # 元检查/思维操作
    (0.3, "注意稳定性方程中的量D"),               # 方向暗示
    (0.5, "D能等于0吗？至少有多大？"),            # 量级感知（Q8）
    (0.2, "用badly approximable性质"),            # 知识注入（Q9）
]

# 降级触发阈值
_DEGRADE_THRESHOLD = 0.5

# 降级时的默认目标Level（量级感知级）
_DEGRADE_TARGET_LEVEL = 0.5

# 降级时的默认非特定性
_DEGRADE_TARGET_NON_SPECIFICITY = 0.7

# 降级时的默认rhs（量级感知级提示）
_DEGRADE_TARGET_RHS = "D能等于0吗？至少有多大？"


class HintGradient:
    """
    提示梯度（261号§4.5）。

    对同一义务ID的规则按Level降序排列形成梯度（从高Level=低泄漏到低Level=高泄漏）。
    当某条规则泄漏风险>0.5时，降级到更高Level的替代规则。
    """

    @staticmethod
    def gradient_levels() -> List[tuple]:
        """获取梯度级别定义（261号§4.5）。返回 (Level, 提示文本) 列表。"""
        return list(_GRADIENT_LEVELS)

    def generate_gradient(
        self,
        obligation_id: str,
        hgraph: HeuristicRuleGraph,
    ) -> List[HeuristicRule]:
        """
        梯度生成（261号§4.5）。

        对某个义务ID，从H图中找出所有标注该义务的规则，
        按Level降序排列（从高到高=从低泄漏到高泄漏），
        返回梯度列表。
        """
        rules = [
            r for r in hgraph.get_all_rules()
            if r.obligation_id == obligation_id
        ]
        # 按Level降序排列（高Level=低泄漏在前）
        rules.sort(key=lambda r: r.level, reverse=True)
        return rules

    def degrade(
        self,
        rule: HeuristicRule,
        matched_rules: List[MatchedRule],
    ) -> HeuristicRule:
        """
        降级方法（261号§4.5）。

        如果rule的leakage_risk > 0.5，寻找同义务ID但Level更高的替代规则。
        如果找不到替代，生成一个降级版（去掉特定知识，提高Level）。
        返回降级后的规则。

        降级路径：从高泄漏级别降到低泄漏级别（Level升高）。
        """
        risk = leakage_risk(rule)
        if risk <= _DEGRADE_THRESHOLD:
            # 泄漏风险可接受，无需降级
            return rule

        # 寻找同义务ID但Level更高的替代规则
        replacement = self._find_higher_level_replacement(rule, matched_rules)
        if replacement is not None:
            return replacement

        # 找不到替代，生成降级版（去掉特定知识，提高Level）
        return self._generate_degraded_rule(rule)

    @staticmethod
    def _find_higher_level_replacement(
        rule: HeuristicRule,
        matched_rules: List[MatchedRule],
    ) -> Optional[HeuristicRule]:
        """
        在候选列表中寻找同义务ID且Level更高的替代规则。

        要求替代规则的泄漏风险 <= 0.5（确实更安全）。
        """
        candidates = []
        for matched in matched_rules:
            other = matched.rule
            if other.rule_id == rule.rule_id:
                continue
            if other.obligation_id != rule.obligation_id:
                continue
            if other.level > rule.level and leakage_risk(other) <= _DEGRADE_THRESHOLD:
                candidates.append(other)
        if not candidates:
            return None
        # 选Level最高的替代
        return max(candidates, key=lambda r: r.level)

    @staticmethod
    def _generate_degraded_rule(rule: HeuristicRule) -> HeuristicRule:
        """
        生成降级版规则（261号§4.5）。

        去掉特定知识，提高Level到量级感知级（0.5），
        rhs替换为不包含特定知识的通用提示。
        """
        return HeuristicRule(
            rule_id=f"{rule.rule_id}_degraded",
            lhs=dict(rule.lhs),
            guard=[],  # 降级版去掉特定guard
            rhs=_DEGRADE_TARGET_RHS,
            level=_DEGRADE_TARGET_LEVEL,
            non_specificity=_DEGRADE_TARGET_NON_SPECIFICITY,
            lifecycle_state=rule.lifecycle_state,
            obligation_id=rule.obligation_id,  # 保留义务ID
        )
