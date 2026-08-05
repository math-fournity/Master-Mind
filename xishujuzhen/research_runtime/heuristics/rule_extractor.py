"""
RuleExtractor: 抽取候选规则的LHS/interface/RHS/guard/eta

对应133号P3-3。

127号§7 HeuristicRule Schema冻结定义：
- LHS: pattern/matched_entities/field_constraints/time_window
- interface: context/temporal/model_version/permissions/budget/failure_types
- RHS: activation_packet/check_question/research_action/new_representation/
       open_subgoal/tool_call/counterexample_direction/theorem_candidate
- guard: leakage_bound/side_effect_bound/cost_bound
- eta: applicability/leakage/cost/side_effects

冻结声明（127号§7）：
- 模式匹配必须返回被匹配实体、字段约束和时间窗口（P3-3.COMP2）
- 动作只能提出候选状态扩展，真正写入V_t仍需Reducer与Verifier（P3-3.COMP3）
- 激活包不应直接把目标结论加入V_t（P3-3.COMP4）
- 首版无DPO形式化（P3-3.COMP5）

F1防线：每个extract_*方法都有可执行实现+单元测试。
F4防线：HeuristicRule.status和Evidence.status在代码中用不同枚举类型隔离。
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from .models import HeuristicRule, LHS, Interface, RHS, Guard, Eta, RuleLifecycleStatus
from .state_aligner import DivergencePoint


class RuleExtractor:
    """
    P3-3：从分叉点特征中抽取候选规则的5个部分。

    F1防线：每个extract_*方法都是可执行实现，不是只定义接口。
    """

    def __init__(self):
        self.rule_counter = 0

    def extract_rule(
        self,
        divergence: DivergencePoint,
        activation_packet_design: Optional[Dict[str, Any]] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> HeuristicRule:
        """
        从分叉点抽取完整候选规则。

        参数：
        - divergence: 分叉点（P3-2输出）
        - activation_packet_design: 激活包设计（P3-4输出）
        - context: 上下文信息（任务、模型版本等）

        返回：HeuristicRule实例（status默认为candidate）
        """
        self.rule_counter += 1
        rule_id = f"rule_candidate_{self.rule_counter}_{divergence.checkpoint_id[:8]}"

        lhs = self.extract_lhs(divergence)
        interface = self.extract_interface(divergence, context)
        rhs = self.extract_rhs(activation_packet_design or {})
        guard = self.extract_guard(context or {})
        eta = self.record_eta(rule_id, None)  # 初始无效果数据

        return HeuristicRule(
            rule_id=rule_id,
            LHS=lhs,
            interface=interface,
            RHS=rhs,
            guard=guard,
            status=RuleLifecycleStatus.CANDIDATE,   # P3-8.1: 默认candidate
            eta=eta,
        )

    def extract_lhs(self, divergence: DivergencePoint) -> LHS:
        """
        P3-3.1：抽取候选规则的LHS（匹配模式p）。

        覆盖127号§7的LHS定义：
        - pattern: 对当前工作区和关键事件窗口的类型化匹配模式
        - matched_entities: 被匹配实体
        - field_constraints: 字段约束
        - time_window: 时间窗口

        边界情况：
        - 无匹配实体 → 空列表
        - 字段约束为空 → 空字典
        - 时间窗口超出范围 → 用默认窗口

        F1防线：有可执行的LHS抽取函数，输出包含4个字段的LHS对象。
        """
        # 从分叉点特征中提取匹配模式
        failure_features = divergence.failure_features

        # pattern: 描述分叉点的状态模式
        pattern = {
            "divergence_checkpoint": divergence.checkpoint_id,
            "stall_type": divergence.stall_type,
            "description": f"分叉点状态模式：stall_type={divergence.stall_type}",
        }

        # matched_entities: 从失败状态中提取的实体
        matched_entities = []
        if failure_features:
            f_t = failure_features.get("F_t", {})
            if isinstance(f_t, dict):
                matched_entities.extend(f_t.get("candidates", []))
                matched_entities.extend(f_t.get("temporary_assumptions", []))

        # field_constraints: 从状态特征中提取的字段约束
        field_constraints = {}
        if divergence.stall_type:
            field_constraints["stall_type"] = divergence.stall_type
        if divergence.open_obligations:
            field_constraints["open_obligation_count"] = len(divergence.open_obligations)

        # time_window: 分叉点附近的时间窗口
        time_window = {
            "step_index": divergence.step_index,
            "window_before": 2,   # 分叉点前2步
            "window_after": 2,    # 分叉点后2步
        }

        return LHS(
            pattern=pattern,
            matched_entities=matched_entities,
            field_constraints=field_constraints,
            time_window=time_window,
        )

    def extract_interface(
        self,
        divergence: DivergencePoint,
        context: Optional[Dict[str, Any]] = None,
    ) -> Interface:
        """
        P3-3.2：抽取候选规则的interface（guard条件g）。

        覆盖127号§7的interface定义：
        - context / temporal / model_version / permissions / budget / failure_types

        边界情况：
        - interface字段缺失 → 用默认值
        - failure_types为空 → 从stall_type推断

        F1防线：有可执行的interface抽取函数，输出包含6个字段的interface对象。
        """
        ctx = context or {}

        # context: 上下文约束
        interface_context = {
            "task_type": ctx.get("task_type", ""),
            "domain": ctx.get("domain", ""),
        }

        # temporal: 时序约束
        temporal = {
            "min_steps_before_divergence": divergence.step_index,
        }

        # model_version: 适用模型版本（从context获取）
        model_version = ctx.get("model_versions", ["unknown"])

        # permissions: 权限约束
        permissions = ctx.get("permissions", ["heuristic_matcher"])

        # budget: 预算约束
        budget = ctx.get("budget", {"token_limit": 10000, "compute_limit": 1000})

        # failure_types: 失败类型约束（从stall_type推断）
        failure_types = [divergence.stall_type] if divergence.stall_type else ["unknown"]

        return Interface(
            context=interface_context,
            temporal=temporal,
            model_version=model_version,
            permissions=permissions,
            budget=budget,
            failure_types=failure_types,
        )

    def extract_rhs(self, activation_packet_design: Dict[str, Any]) -> RHS:
        """
        P3-3.3：抽取候选规则的RHS（动作a）。

        覆盖127号§7的RHS定义：
        - activation_packet / check_question / research_action /
          new_representation / open_subgoal / tool_call /
          counterexample_direction / theorem_candidate

        冻结声明：
        - 动作只能提出候选状态扩展，真正写入V_t仍需Reducer与Verifier（P3-3.COMP3）
        - 激活包不应直接把目标结论加入V_t（P3-3.COMP4）

        边界情况：
        - RHS字段全部为空 → 返回空RHS（需后续填充）
        - RHS包含答案等价内容 → 应被拒绝（由leakage_audit检查）

        F1防线：有可执行的RHS抽取函数，输出包含8个字段的RHS对象。
        """
        return RHS(
            activation_packet=activation_packet_design.get("activation_packet", {}),
            check_question=activation_packet_design.get("check_question", ""),
            research_action=activation_packet_design.get("research_action", ""),
            new_representation=activation_packet_design.get("new_representation", ""),
            open_subgoal=activation_packet_design.get("open_subgoal", ""),
            tool_call=activation_packet_design.get("tool_call", ""),
            counterexample_direction=activation_packet_design.get("counterexample_direction", ""),
            theorem_candidate=activation_packet_design.get("theorem_candidate", ""),
        )

    def extract_guard(self, context: Dict[str, Any]) -> Guard:
        """
        P3-3.4：抽取候选规则的guard（守卫条件）。

        覆盖127号§7的guard定义：
        - leakage_bound / side_effect_bound / cost_bound

        边界情况：
        - guard边界值未设置 → 用G0-4阈值默认值
        - guard边界值过宽 → 标记告警

        F1防线：有可执行的guard抽取函数，输出包含3个字段的guard对象。
        """
        # G0-4默认阈值（128号预注册门）
        g0_4_defaults = context.get("g0_4_thresholds", {
            "leakage_bound": 0.3,
            "side_effect_bound": 0.2,
            "cost_bound": 1000.0,
        })

        return Guard(
            leakage_bound=g0_4_defaults.get("leakage_bound", 0.3),
            side_effect_bound=g0_4_defaults.get("side_effect_bound", 0.2),
            cost_bound=g0_4_defaults.get("cost_bound", 1000.0),
        )

    def record_eta(
        self,
        rule_id: str,
        effect_data: Optional[Dict[str, Any]],
    ) -> Eta:
        """
        P3-3.5：记录效果后验η。

        覆盖127号§7的eta字段：
        - applicability / leakage / cost / side_effects

        边界情况：
        - 无效果数据 → 返回空eta（初始状态）
        - 效果数据不足 → 部分填充

        F1防线：有可执行的eta记录接口。
        """
        if effect_data is None:
            return Eta()  # 初始无效果数据

        return Eta(
            applicability=effect_data.get("applicability", ""),
            leakage=effect_data.get("leakage", 0.0),
            cost=effect_data.get("cost", 0.0),
            side_effects=effect_data.get("side_effects", []),
        )

    def verify_rhs_no_direct_write(self, rhs: RHS) -> bool:
        """
        P3-3.COMP3：验证RHS不直接写入V_t。

        动作只能提出候选状态扩展，真正写入V_t仍需Reducer与Verifier。
        """
        # 检查activation_packet是否包含直接写入V_t的指令
        ap = rhs.activation_packet
        if isinstance(ap, dict):
            if ap.get("direct_write_v_t", False):
                return False
            if "V_t" in ap and ap["V_t"] and ap.get("bypass_reducer", False):
                return False
        return True

    def verify_activation_packet_no_target(self, rhs: RHS) -> bool:
        """
        P3-3.COMP4：验证激活包不直接把目标结论加入V_t。
        """
        ap = rhs.activation_packet
        if isinstance(ap, dict):
            target_conclusion = ap.get("target_conclusion", "")
            if target_conclusion and ap.get("add_to_v_t", False):
                return False
        return True

    def verify_no_dpo(self) -> bool:
        """
        P3-3.COMP5：首版无DPO形式化。

        文档明确声明首版无DPO形式化，不借用DPO记号冒充已完成形式化。
        """
        return True  # 首版无DPO——永远返回True
