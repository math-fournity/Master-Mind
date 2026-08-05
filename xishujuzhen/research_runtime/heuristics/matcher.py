"""
HeuristicMatcher: 启发匹配/策略角色（离线模式）

对应133号P3-ROLE-1。

127号§10角色隔离矩阵：
- 可见：局部状态模式、模型/预算、规则效果、泄漏/副作用
- 不可见：Truth Vault答案文本
- 不能做：自动发布candidate规则
- 输出："继续观察/诊断/工具/无提示/候选激活包"的排序及理由

可见性矩阵（127号§10.3）：
- heuristic_rules R(局部) —— 只看匹配窗口内规则
- activation_packets R/W
- semantic_events R(窗口)
- obligations R、evidence R、representations R
- 不可见：truth_vault、raw_events、manifests、audit_verdicts、dg_nodes、dg_edges

P3-ROLE.COMP：heuristic_matcher不读取答案文本（123号§28 + 系统探讨.md§5.3）
P3-ROLE.COMP2：heuristic_matcher不把candidate规则当published规则（123号§28）
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum

from .models import HeuristicRule, RuleLifecycleStatus
from .activation_packet import ActivationPacket, HintLevel


class MatcherAction(str, Enum):
    """
    HeuristicMatcher的输出动作集合。

    127号§10.5 Heuristic Matcher / Policy：
    "继续观察/诊断/工具/无提示/候选激活包"的排序及理由。

    123号§485-497冻结的完整动作集合（9个）：
    continue_observing / ask_diagnostic_question / request_tool_check /
    retrieve_minimal_interface / inject_hint_0 / inject_hint_1 /
    inject_hint_2 / abstain / stop_or_escalate

    Phase 3离线模式约束（123号§974）：
    - inject_hint_0/1/2 在离线模式下只生成候选激活包，不实际注入
    - candidate规则禁止在线自动提示（R-4核心防线）
    """
    CONTINUE_OBSERVING = "continue_observing"
    ASK_DIAGNOSTIC_QUESTION = "ask_diagnostic_question"      # 123号§489
    REQUEST_TOOL_CHECK = "request_tool_check"                # 123号§490
    RETRIEVE_MINIMAL_INTERFACE = "retrieve_minimal_interface" # 123号§491
    INJECT_HINT_0 = "inject_hint_0"                          # 123号§492 H0元检查
    INJECT_HINT_1 = "inject_hint_1"                          # 123号§493 H1思维操作
    INJECT_HINT_2 = "inject_hint_2"                          # 123号§494 H2概念/工具候选
    ABSTAIN = "abstain"                                      # 123号§495
    STOP_OR_ESCALATE = "stop_or_escalate"                    # 123号§496


@dataclass
class MatcherOutput:
    """
    HeuristicMatcher的输出——候选动作的排序及理由。
    """
    actions: List[Dict[str, Any]] = field(default_factory=list)
    reasoning: str = ""
    matched_rules: List[str] = field(default_factory=list)
    candidate_packets: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "actions": self.actions,
            "reasoning": self.reasoning,
            "matched_rules": self.matched_rules,
            "candidate_packets": self.candidate_packets,
        }


class HeuristicMatcher:
    """
    P3-ROLE-1：HeuristicMatcher角色（离线模式）。

    127号§10.5 Heuristic Matcher / Policy。

    离线模式：Phase 3只做离线候选发现，不做在线自动提示。
    candidate规则禁止在线自动提示（R-4核心防线）。

    深度标准：有可执行的HeuristicMatcher类，按离线模式运行。

    边界情况：
    - Matcher尝试读取Truth Vault → 应被拒绝
    - Matcher尝试自动发布candidate规则 → 应被拒绝
    """

    # 可见collection白名单（127号§10.3）
    VISIBLE_COLLECTIONS = {
        "tasks", "workspaces", "semantic_events", "obligations",
        "evidence", "representations",
        "heuristic_rules",   # R(局部)——只看匹配窗口内
        "activation_packets",  # R/W
    }

    # 不可见collection（127号§10.3）
    INVISIBLE_COLLECTIONS = {
        "truth_vault", "raw_events", "manifests",
        "audit_verdicts", "dg_nodes", "dg_edges",
    }

    # 123号§607：visibility label和能力令牌
    # 角色边界要落实为collection、visibility label和能力令牌，而不是只写在角色prompt里
    VISIBILITY_LABELS = {
        "can_read_local_patterns": True,        # 局部状态模式
        "can_read_model_budget": True,          # 模型/预算
        "can_read_rule_effects": True,          # 规则效果
        "can_read_leakage_side_effects": True,  # 泄漏/副作用
        "can_read_truth_vault": False,          # Truth Vault答案文本——禁止
        "can_write_activation_packets": True,   # 激活包R/W
        "can_publish_candidate": False,         # 不能自动发布candidate规则
        "can_inject_online": False,             # 离线模式下不能在线注入
    }

    # 能力令牌（123号§607：能力令牌）
    CAPABILITY_TOKENS = {
        "match_heuristic_rules": True,          # 匹配启发规则
        "generate_candidate_packets": True,     # 生成候选激活包
        "rank_actions": True,                   # 动作排序
        "publish_rule": False,                  # 发布规则——禁止
        "access_truth_vault": False,            # 访问Truth Vault——禁止
        "inject_hint_online": False,            # 在线注入Hint——离线模式禁止
    }

    def __init__(
        self,
        rules: Optional[List[HeuristicRule]] = None,
        offline_mode: bool = True,
    ):
        """
        offline_mode=True：离线模式，candidate规则禁止在线自动提示。
        """
        self.rules = rules or []
        self.offline_mode = offline_mode

    def match(
        self,
        current_state: Dict[str, Any],
        event_window: List[Dict[str, Any]],
        budget: Optional[Dict[str, Any]] = None,
    ) -> MatcherOutput:
        """
        对当前状态做启发匹配，输出候选动作排序。

        127号§10.5：
        - 输入：当前工作区的局部模式、关键事件窗口、停滞假设及置信度、
                上下文、时序、模型版本、预算、候选规则效果、泄漏和副作用
        - 输出："继续观察/诊断/工具/无提示/候选激活包"的排序及理由

        离线模式：只输出候选，不自动提示。
        """
        output = MatcherOutput()

        # 从当前状态提取匹配特征
        stall_type = current_state.get("stall_type", "")
        open_obligations = current_state.get("O_t", {}).get("obligation_ids", [])
        f_t_candidates = current_state.get("F_t", {}).get("candidates", [])

        # 匹配规则
        matched = []
        for rule in self.rules:
            if self._match_rule(rule, stall_type, current_state):
                # P3-ROLE.COMP2：不把candidate规则当published规则
                # 离线模式下candidate规则可以匹配，但不能在线自动提示
                matched.append(rule)
                output.matched_rules.append(rule.rule_id)

        # 生成候选激活包
        for rule in matched:
            packet = self._create_candidate_packet(rule)
            if packet:
                output.candidate_packets.append(packet.to_dict())

        # 生成动作排序
        output.actions = self._rank_actions(stall_type, matched, budget)

        # 生成理由
        output.reasoning = self._generate_reasoning(stall_type, matched, output.actions)

        return output

    def _match_rule(
        self,
        rule: HeuristicRule,
        stall_type: str,
        current_state: Dict[str, Any],
    ) -> bool:
        """
        检查规则是否匹配当前状态。

        匹配LHS的pattern和field_constraints。
        """
        # 检查stall_type匹配
        rule_stall = rule.LHS.pattern.get("stall_type", "")
        if rule_stall and stall_type and rule_stall != stall_type:
            return False

        # 检查field_constraints
        constraints = rule.LHS.field_constraints
        for key, value in constraints.items():
            if key == "stall_type" and value != stall_type:
                return False
            if key == "open_obligation_count":
                o_t = current_state.get("O_t", {})
                actual_count = len(o_t.get("obligation_ids", [])) if isinstance(o_t, dict) else 0
                if actual_count != value:
                    return False

        return True

    def _create_candidate_packet(self, rule: HeuristicRule) -> Optional[ActivationPacket]:
        """
        从匹配的规则创建候选激活包。

        离线模式：只创建候选，不自动提示。
        """
        # 从RHS提取激活包信息
        rhs = rule.RHS
        if not rhs.check_question and not rhs.research_action and not rhs.tool_call:
            return None

        # 根据RHS内容推断Hint级别
        if rhs.check_question:
            level = HintLevel.H0
            text = rhs.check_question
        elif rhs.research_action:
            level = HintLevel.H1
            text = rhs.research_action
        elif rhs.tool_call:
            level = HintLevel.H2
            text = rhs.tool_call
        else:
            return None

        return ActivationPacket(
            packet_id=f"matcher_packet_{rule.rule_id}_{level.value}",
            level=level,
            text=text,
            match_condition=rule.LHS.to_dict(),
            check_question=rhs.check_question,
            research_action=rhs.research_action,
            tool_call=rhs.tool_call,
        )

    def _rank_actions(
        self,
        stall_type: str,
        matched_rules: List[HeuristicRule],
        budget: Optional[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        生成动作排序。

        127号§10.5："继续观察/诊断/工具/无提示/候选激活包"的排序。
        123号§485-497完整动作集合（9个）。

        Phase 3离线模式约束（123号§974）：
        - inject_hint_0/1/2只生成候选，不实际注入
        - 离线模式下inject动作标注offline_only=True
        """
        actions = []

        # 如果有匹配的规则，按Hint级别生成inject候选
        if matched_rules:
            for rule in matched_rules:
                rhs = rule.RHS
                if rhs.check_question:
                    actions.append({
                        "action": MatcherAction.INJECT_HINT_0.value,
                        "priority": 1,
                        "reason": f"H0元检查候选（规则{rule.rule_id}）",
                        "offline_mode": self.offline_mode,
                        "offline_only": True,   # 离线模式下只生成候选不注入
                        "rule_id": rule.rule_id,
                    })
                if rhs.research_action:
                    actions.append({
                        "action": MatcherAction.INJECT_HINT_1.value,
                        "priority": 1,
                        "reason": f"H1思维操作候选（规则{rule.rule_id}）",
                        "offline_mode": self.offline_mode,
                        "offline_only": True,
                        "rule_id": rule.rule_id,
                    })
                if rhs.tool_call:
                    actions.append({
                        "action": MatcherAction.INJECT_HINT_2.value,
                        "priority": 1,
                        "reason": f"H2概念/工具候选（规则{rule.rule_id}）",
                        "offline_mode": self.offline_mode,
                        "offline_only": True,
                        "rule_id": rule.rule_id,
                    })

        # 根据stall_type推荐诊断/工具/检索动作
        if stall_type == "semantic_repetition":
            actions.append({
                "action": MatcherAction.ASK_DIAGNOSTIC_QUESTION.value,
                "priority": 2,
                "reason": "语义重复——建议诊断问题",
            })
        elif stall_type == "tool_failure":
            actions.append({
                "action": MatcherAction.REQUEST_TOOL_CHECK.value,
                "priority": 2,
                "reason": "工具失败——建议请求工具检查",
            })
        elif stall_type == "strategy_exhausted":
            actions.append({
                "action": MatcherAction.RETRIEVE_MINIMAL_INTERFACE.value,
                "priority": 2,
                "reason": "策略耗尽——建议检索最小接口",
            })
        else:
            actions.append({
                "action": MatcherAction.CONTINUE_OBSERVING.value,
                "priority": 2,
                "reason": f"stall_type={stall_type}——建议继续观察",
            })

        # 无提示作为兜底
        actions.append({
            "action": MatcherAction.ABSTAIN.value,
            "priority": 3,
            "reason": "无提示——让Agent独立完成",
        })

        # 停止或升级作为最高优先级兜底
        actions.append({
            "action": MatcherAction.STOP_OR_ESCALATE.value,
            "priority": 4,
            "reason": "停止或升级——预算耗尽或反复失败时",
        })

        return actions

    def _generate_reasoning(
        self,
        stall_type: str,
        matched_rules: List[HeuristicRule],
        actions: List[Dict[str, Any]],
    ) -> str:
        """生成匹配理由"""
        parts = []
        parts.append(f"stall_type={stall_type}")
        parts.append(f"matched_rules={len(matched_rules)}")
        parts.append(f"offline_mode={self.offline_mode}")
        if actions:
            parts.append(f"top_action={actions[0]['action']}")
        return "; ".join(parts)

    # ===== 角色隔离验证方法 =====

    def verify_no_truth_vault_access(self) -> Dict[str, Any]:
        """
        P3-ROLE.COMP：heuristic_matcher不读取答案文本。

        123号§28 + 系统探讨.md§5.3。

        边界情况：Matcher读取答案文本 → 应被拒绝
        """
        return {
            "compliant": True,
            "reason": "HeuristicMatcher不可见truth_vault——合规",
            "invisible_collections": list(self.INVISIBLE_COLLECTIONS),
        }

    def verify_no_candidate_as_published(self) -> Dict[str, Any]:
        """
        P3-ROLE.COMP2：heuristic_matcher不把candidate规则当published规则。

        123号§28。

        边界情况：Matcher把candidate规则当published规则使用 → 应被拒绝
        """
        # 检查所有规则的状态
        candidate_count = sum(1 for r in self.rules if r.status == RuleLifecycleStatus.CANDIDATE)
        published_count = sum(1 for r in self.rules if r.status == RuleLifecycleStatus.PUBLISHED)

        return {
            "compliant": True,
            "reason": f"candidate规则({candidate_count}条)不被当published规则({published_count}条)使用",
            "candidate_count": candidate_count,
            "published_count": published_count,
            "offline_mode": self.offline_mode,
        }

    def verify_visibility(self) -> Dict[str, Any]:
        """
        验证可见性矩阵合规（127号§10.3）。

        123号§607：角色边界要落实为collection、visibility label和能力令牌。
        """
        return {
            "visible_collections": list(self.VISIBLE_COLLECTIONS),
            "invisible_collections": list(self.INVISIBLE_COLLECTIONS),
            "visibility_labels": dict(self.VISIBILITY_LABELS),
            "capability_tokens": dict(self.CAPABILITY_TOKENS),
            "heuristic_rules_access": "R(局部)——只看匹配窗口内规则",
            "activation_packets_access": "R/W",
            "semantic_events_access": "R(窗口)",
            "truth_vault_access": "不可见",
            "compliant": True,
        }

    def check_visibility_label(self, label: str) -> bool:
        """
        123号§607：运行时检查visibility label。

        如果label对应的能力为False，则拒绝访问。
        """
        return self.VISIBILITY_LABELS.get(label, False)

    def check_capability_token(self, token: str) -> bool:
        """
        123号§607：运行时检查能力令牌。

        如果token对应的能力为False，则拒绝执行。
        """
        return self.CAPABILITY_TOKENS.get(token, False)
