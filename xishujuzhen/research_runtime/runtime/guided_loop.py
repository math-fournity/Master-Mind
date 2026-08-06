"""
GuidedLoop：系统引导数学大师的完整循环

把DevinCliAdapter连接到12步运行时，形成真正的引导循环：

  1. 系统给数学大师一个数学问题（turn 1: solo explore）
  2. 捕获数学大师的输出（event capture）
  3. 分析状态（state reduce + stall detect）
  4. 如果卡住，匹配规则、编译hint（pattern match + compile）
  5. 发送hint给数学大师（turn N: guided explore）
  6. 重复2-5直到完成或预算耗尽
  7. 归因收口（attribution close）

对应178-182号全程监控方案 + 136号Phase 6。
这是"审计整个大师数学系统工作全过程"的核心实现。
"""

import json
import os
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

from .devin_cli_adapter import DevinCliAdapter, TurnRecord

# 203-A.0: 提示分级定义
# knowledge: 给具体数学事实（如"ex(n,C_4)=O(n^{3/2})"）
# strategy: 给解题方向/方法选择（如"从小情形开始验证"）
# meta: 给元提示（如"请给出更详细的分析"）
HINT_LEVELS = {"knowledge", "strategy", "meta"}

# 203-A.1: 5条硬编码提示逐条标注级别
HINT_REGISTRY = {
    "lack_knowledge": {
        "level": "knowledge",
        "text": "提示：考虑C_4是偶圈，具有二部结构。已知R_k(C_4)的上界来自Bipartite Ramsey理论，下界来自射影平面构造。请查阅Conlon关于Ramsey数的讲义。",
    },
    "uncertain": {
        "level": "strategy",
        "text": "提示：尝试从小情形开始验证。先计算k=2,3,4时的R_k(C_4)精确值，看是否能发现模式。",
    },
    "need_more_info": {
        "level": "knowledge",
        "text": "提示：关键信息是C_4的二部性使得ex(n,C_4)=O(n^{3/2})，而C_3的ex(n,C_3)=O(n^2)。这个差异直接决定了Ramsey数的阶。",
    },
    "response_too_short": {
        "level": "meta",
        "text": "请给出更详细的分析，包括：1) 已知上下界的来源，2) 你的猜测，3) 支撑猜测的推理。",
    },
    "unknown_stall": {
        "level": "strategy",
        "text": "继续分析。尝试从极值图论的角度思考：C_4-free图的边数上界如何决定Ramsey数的阶？",
    },
}

# 降级提示（泄漏审计fail时使用）
FALLBACK_META_HINT = "请继续深入分析，给出更详细的推理过程。"


@dataclass
class LoopState:
    """引导循环的状态"""
    turn: int = 0
    phase: str = "init"  # init / solo / guided / done / budget_exhausted
    last_response: str = ""
    stall_detected: bool = False
    stall_reason: str = ""
    hint_given: str = ""
    hint_level: str = ""  # 203-A.3: 记录提示级别
    leakage_audit: Optional[Dict[str, Any]] = None  # 203-A.3: 记录泄漏审计结果
    hints_used: int = 0
    max_turns: int = 5
    max_hints: int = 3
    completed: bool = False
    completion_reason: str = ""


@dataclass
class GuidedLoopResult:
    """引导循环的最终结果"""
    run_id: str
    session_id: str
    problem: str
    n_turns: int
    n_hints: int
    final_response: str
    completed: bool
    completion_reason: str
    turn_history: List[Dict[str, Any]] = field(default_factory=list)
    total_tokens: Dict[str, int] = field(default_factory=dict)
    # 203-A.3: 提示级别和泄漏审计结果
    hint_levels: List[str] = field(default_factory=list)
    leakage_audits: List[Dict[str, Any]] = field(default_factory=list)
    # 205-A.3: AI诊断结果
    ai_diagnoses: List[Dict[str, Any]] = field(default_factory=list)
    # 205-C: AI规划结果
    ai_plans: List[Dict[str, Any]] = field(default_factory=list)
    # 205-D: AI调用成本
    ai_call_count: int = 0
    ai_call_log: List[Dict[str, Any]] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "run_id": self.run_id,
            "session_id": self.session_id,
            "problem": self.problem,
            "n_turns": self.n_turns,
            "n_hints": self.n_hints,
            "final_response": self.final_response,
            "completed": self.completed,
            "completion_reason": self.completion_reason,
            "turn_history": self.turn_history,
            "total_tokens": self.total_tokens,
            "hint_levels": self.hint_levels,  # 203-A.3
            "leakage_audits": self.leakage_audits,  # 203-A.3
            "ai_diagnoses": self.ai_diagnoses,  # 205-A.3
            "ai_plans": self.ai_plans,  # 205-C
            "ai_call_count": self.ai_call_count,  # 205-D
            "ai_call_log": self.ai_call_log,  # 205-D
            "timestamp": self.timestamp,
        }


class GuidedLoop:
    """
    系统引导数学大师的完整循环。

    使用方法：
        loop = GuidedLoop(
            run_id="run_20260806_001",
            run_dir="runs/run_20260806_001",
            problem="猜测R_k(C_4)的下界...",
        )
        result = loop.run()
    """

    # 简单的卡点检测信号
    STALL_SIGNALS = [
        "我不知道",
        "无法确定",
        "需要更多信息",
        "不确定",
        "没有思路",
        "难以判断",
        "无法继续",
        "卡住了",
    ]

    # 完成信号
    COMPLETION_SIGNALS = [
        "证明完毕",
        "QED",
        "证毕",
        "结论是",
        "最终答案",
        "综上所述",
        "一句话总结",
        "总结如下",
    ]

    def __init__(
        self,
        run_id: str,
        run_dir: str,
        problem: str,
        model: str = "glm-5-2",
        max_turns: int = 5,
        max_hints: int = 3,
        timeout: int = 300,
        work_dir: Optional[str] = None,
        truth_vault_answer: str = "",  # 203-B.1: truth_vault答案
    ):
        self.run_id = run_id
        self.run_dir = run_dir
        self.problem = problem
        self.model = model
        self.state = LoopState(max_turns=max_turns, max_hints=max_hints)
        self.adapter = DevinCliAdapter(run_dir=run_dir, model=model, timeout=timeout, work_dir=work_dir)
        # 203-A.3: 收集每个hint的级别和审计结果
        self._hint_levels: List[str] = []
        self._leakage_audits: List[Dict[str, Any]] = []
        # 205-A.3: 收集AI诊断结果
        self._ai_diagnoses: List[Dict[str, Any]] = []
        # 205-D: AI调用预算控制
        self._ai_call_count: int = 0
        self._max_ai_calls: int = 5  # 每个run最多调用AI 5次
        self._ai_call_log: List[Dict[str, Any]] = []  # AI调用日志
        # 205-C: AI规划结果收集
        self._ai_plans: List[Dict[str, Any]] = []
        # 203-B.1: truth_vault——答案隔离
        self._truth_vault_answer = truth_vault_answer
        self._truth_vault_checker = None
        if truth_vault_answer:
            self._init_truth_vault()

    def _init_truth_vault(self):
        """203-B.1: 初始化truth_vault隔离检查"""
        try:
            from ..auditor.visibility_labels import VisibilityLabelChecker
            self._truth_vault_checker = VisibilityLabelChecker()
            # 验证truth_vault隔离——Controller(orchestrator)不可读truth_vault
            isolation = self._truth_vault_checker.verify_truth_vault_isolation()
            if not isolation["isolation_verified"]:
                print(f"[GuidedLoop] 警告：truth_vault隔离验证失败: {isolation['violations']}")
            else:
                print(f"[GuidedLoop] truth_vault隔离验证通过——仅auditor可读")
        except Exception as e:
            print(f"[GuidedLoop] truth_vault初始化失败（不阻塞）: {e}")

    def _check_ai_budget(self, call_type: str = "diagnosis") -> bool:
        """205-D: 检查AI调用预算是否还有剩余"""
        if self._ai_call_count >= self._max_ai_calls:
            self._ai_call_log.append({
                "call_type": call_type,
                "blocked": True,
                "reason": "AI调用预算耗尽",
                "ai_call_count": self._ai_call_count,
            })
            return False
        return True

    def _record_ai_call(self, call_type: str, success: bool, detail: str = ""):
        """205-D: 记录AI调用"""
        self._ai_call_count += 1
        self._ai_call_log.append({
            "call_type": call_type,
            "success": success,
            "detail": detail,
            "ai_call_count": self._ai_call_count,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

    def _get_exploration_map(self) -> Dict[str, Any]:
        """205-C.0: 获取探索地图——Solver已探索的区域"""
        return {
            "explored_methods": self._extract_explored_methods(),
            "explored_directions": self._extract_explored_directions(),
            "failed_routes": self._extract_failed_routes(),
            "current_response_length": len(self.state.last_response),
            "turn": self.state.turn,
            "hints_used": self.state.hints_used,
        }

    def _extract_explored_methods(self) -> List[str]:
        """从历史response中提取Solver已尝试的方法"""
        methods = []
        method_keywords = ["归纳法", "生成函数", "反证法", "构造法", "极值方法",
                          "概率方法", "代数方法", "几何方法", "分析方法",
                          "拓扑方法", "组合方法", "数论方法"]
        all_responses = " ".join(t.response for t in self.adapter.turn_history)
        for method in method_keywords:
            if method in all_responses:
                methods.append(method)
        return methods

    def _extract_explored_directions(self) -> List[str]:
        """从历史response中提取Solver已走的方向"""
        directions = []
        direction_keywords = {
            "上界估计": ["上界", "不超过", "至多"],
            "下界估计": ["下界", "至少", "不小于"],
            "精确计算": ["精确", "等于", "计算"],
            "存在性证明": ["存在", "构造"],
            "反例构造": ["反例", "不成立"],
        }
        all_responses = " ".join(t.response for t in self.adapter.turn_history)
        for direction, keywords in direction_keywords.items():
            if any(kw in all_responses for kw in keywords):
                directions.append(direction)
        return directions

    def _extract_failed_routes(self) -> List[str]:
        """从历史response中提取失败的路线"""
        failed = []
        failure_keywords = ["失败", "不行", "过不去", "无法", "不成立", "错误"]
        all_responses = " ".join(t.response for t in self.adapter.turn_history)
        for kw in failure_keywords:
            if kw in all_responses:
                # 提取失败关键词周围的上下文
                idx = all_responses.find(kw)
                context = all_responses[max(0, idx-20):idx+20]
                failed.append(f"...{context}...")
        return failed

    def _ai_plan_next_direction(self, exploration_map: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """205-C.4: AI规划下一步引导方向

        只在第2轮及以后调用（第1轮无已探索区域，无法规划）
        返回：{next_direction, bridge_node, reason}
        """
        if self.state.turn < 2:
            return None  # 第1轮不规划

        if not self._check_ai_budget("planning"):
            return None

        # 205-C.3: AI规划prompt
        prompt = self._build_planning_prompt(exploration_map)

        try:
            plan = self._call_ai_for_planning(prompt, exploration_map)
            self._record_ai_call("planning", True, plan.get("next_direction", ""))
            return plan
        except Exception as e:
            self._record_ai_call("planning", False, str(e))
            print(f"[GuidedLoop] AI规划失败（fallback到经典提示）: {e}")
            return None

    def _build_planning_prompt(self, exploration_map: Dict[str, Any]) -> str:
        """205-C.3: 构造AI规划prompt"""
        return f"""你是数学大师系统的引导规划AI。

Solver的探索地图：
- 已尝试方法：{exploration_map.get('explored_methods', [])}
- 已走方向：{exploration_map.get('explored_directions', [])}
- 失败路线：{exploration_map.get('failed_routes', [])}
- 当前turn：{exploration_map.get('turn', 0)}
- 已用hints：{exploration_map.get('hints_used', 0)}

请规划下一步引导方向：
1. 哪个未探索方向最值得优先？
2. 通过什么方法到达？
3. 给出具体的提示方向（不是提示内容——内容由步骤B生成）

输出JSON：
{{
  "next_direction": "下一步方向",
  "suggested_method": "建议方法",
  "reason": "为什么选择这个方向"
}}"""

    def _call_ai_for_planning(self, prompt: str, exploration_map: Dict[str, Any]) -> Dict[str, Any]:
        """205-C.4: 调用AI做规划

        POC实现：用简化的规则做规划
        实际部署时替换为外部AI调用
        """
        explored_methods = set(exploration_map.get("explored_methods", []))
        explored_directions = set(exploration_map.get("explored_directions", []))
        failed_routes = exploration_map.get("failed_routes", [])

        # 规则1: 如果Solver只尝试了1种方法——建议换方法
        if len(explored_methods) <= 1:
            untried = ["反证法", "构造法", "极值方法", "概率方法"]
            for method in untried:
                if method not in explored_methods:
                    return {
                        "next_direction": "方法 diversification",
                        "suggested_method": method,
                        "reason": f"Solver只尝试了{explored_methods}，建议尝试{method}",
                    }

        # 规则2: 如果Solver只走了上界方向——建议也看下界
        if "上界估计" in explored_directions and "下界估计" not in explored_directions:
            return {
                "next_direction": "下界估计",
                "suggested_method": "构造法",
                "reason": "Solver只做了上界，建议补充下界构造",
            }

        # 规则3: 如果有失败路线——建议绕过
        if failed_routes:
            return {
                "next_direction": "换表示方法",
                "suggested_method": "代数方法",
                "reason": f"Solver有{len(failed_routes)}条失败路线，建议换表示绕过障碍",
            }

        # 默认: 继续当前方向
        return {
            "next_direction": "继续深入",
            "suggested_method": "",
            "reason": "当前方向有潜力，建议继续深入",
        }

    def run(self) -> GuidedLoopResult:
        """执行完整引导循环"""
        print(f"[GuidedLoop] 启动 run_id={self.run_id}")
        print(f"[GuidedLoop] 问题: {self.problem[:100]}...")

        # Turn 1: solo explore——给数学大师问题，不给任何hint
        self.state.phase = "solo"
        self.state.turn = 1
        print(f"\n[GuidedLoop] Turn 1 (solo explore)——给数学大师问题")

        turn1 = self.adapter.send(self.problem)
        self.state.last_response = turn1.response
        print(f"[GuidedLoop] Turn 1完成, response长度={len(turn1.response)}, session={turn1.session_id}")

        # 检查是否已完成
        if self._check_completion(turn1.response):
            self.state.completed = True
            self.state.completion_reason = "solo_explore_completed"
            self.state.phase = "done"
            print(f"[GuidedLoop] 数学大师在solo explore阶段就完成了！")
        else:
            # 进入引导循环
            self._guided_loop()

        # 保存turn log
        log_path = self.adapter.save_turn_log()

        # 构造结果
        result = GuidedLoopResult(
            run_id=self.run_id,
            session_id=self.adapter.session_id or "",
            problem=self.problem,
            n_turns=len(self.adapter.turn_history),
            n_hints=self.state.hints_used,
            final_response=self.state.last_response,
            completed=self.state.completed,
            completion_reason=self.state.completion_reason or self.state.phase,
            turn_history=[t.to_dict() for t in self.adapter.turn_history],
            total_tokens=self.adapter.get_total_tokens(),
            hint_levels=self._hint_levels,  # 203-A.3
            leakage_audits=self._leakage_audits,  # 203-A.3
            ai_diagnoses=self._ai_diagnoses,  # 205-A.3
            ai_plans=self._ai_plans,  # 205-C
            ai_call_count=self._ai_call_count,  # 205-D
            ai_call_log=self._ai_call_log,  # 205-D
        )

        # 保存结果
        result_path = os.path.join(self.run_dir, "guided_loop_result.json")
        with open(result_path, "w") as f:
            json.dump(result.to_dict(), f, indent=2, ensure_ascii=False)

        print(f"\n[GuidedLoop] 循环结束: {result.n_turns}turns, {result.n_hints}hints, completed={result.completed}")
        print(f"[GuidedLoop] 结果已保存: {result_path}")
        return result

    def _guided_loop(self):
        """引导循环——分析状态、检测卡点、给hint"""
        while not self.state.completed and self.state.turn < self.state.max_turns:
            self.state.turn += 1

            # 步骤4-5: 事件捕获 + 状态归约（简化版——分析response）
            self.state.stall_detected = self._detect_stall(self.state.last_response)
            self.state.stall_reason = self._analyze_stall_reason(self.state.last_response)

            # 205-A: 步骤7 AI诊断——经典计算不确定时调用AI
            if self.state.stall_detected and self.state.stall_reason == "unknown_stall":
                if self._check_ai_budget("diagnosis"):
                    ai_diagnosis = self._ai_diagnose_stall(self.state.last_response)
                    if ai_diagnosis:
                        self._record_ai_call("diagnosis", True, ai_diagnosis.get("refined_stall_reason", ""))
                        if ai_diagnosis.get("refined_stall_reason"):
                            self.state.stall_reason = ai_diagnosis["refined_stall_reason"]
                            print(f"[GuidedLoop] AI诊断: {ai_diagnosis['refined_stall_reason']} "
                                  f"(置信度: {ai_diagnosis.get('confidence', 'N/A')})")
                    else:
                        self._record_ai_call("diagnosis", False, "AI返回None")
                    self._ai_diagnoses.append(ai_diagnosis or {})
                else:
                    print(f"[GuidedLoop] AI预算耗尽，跳过AI诊断")
                    self._ai_diagnoses.append({"skipped": True, "reason": "预算耗尽"})

            if not self.state.stall_detected:
                # 没有卡点——检查是否完成
                if self._check_completion(self.state.last_response):
                    self.state.completed = True
                    self.state.completion_reason = "completed_in_guided_loop"
                    self.state.phase = "done"
                    return
                # 没完成也没卡住——继续等一轮（给一个"继续"的提示）
                if self.state.turn > 2:
                    self.state.completed = True
                    self.state.completion_reason = "no_stall_no_completion_stop"
                    self.state.phase = "done"
                    return
                # 第2turn还没卡住——给一个"继续深入"的提示
                hint = "请继续深入分析，给出更具体的猜测和证明思路。"
            else:
                # 步骤7-9: 诊断 + 模式匹配 + 选择动作
                if self.state.hints_used >= self.state.max_hints:
                    self.state.completion_reason = "hint_budget_exhausted"
                    self.state.phase = "budget_exhausted"
                    print(f"[GuidedLoop] Hint预算耗尽({self.state.max_hints})，停止")
                    return

                hint, hint_level, leakage_audit = self._generate_hint(
                    self.state.stall_reason, self.state.last_response
                )

                # 205-C: 多轮智能规划——第2轮及以后调用AI规划
                if self.state.turn >= 2 and self.state.hints_used >= 1:
                    exploration_map = self._get_exploration_map()
                    plan = self._ai_plan_next_direction(exploration_map)
                    if plan and plan.get("next_direction"):
                        print(f"[GuidedLoop] AI规划: {plan['next_direction']} "
                              f"(方法: {plan.get('suggested_method', 'N/A')})")
                        # 把规划结果附加到hint（不替换hint，只补充方向）
                        if plan.get("suggested_method"):
                            hint = f"{hint}\n\n建议方向：{plan['next_direction']}，可尝试{plan['suggested_method']}。"
                    self._ai_plans.append(plan or {})

            self.state.hint_given = hint
            self.state.hint_level = hint_level  # 203-A.3
            self.state.leakage_audit = leakage_audit  # 203-A.3
            self._hint_levels.append(hint_level)  # 203-A.3: 收集
            self._leakage_audits.append(leakage_audit or {})  # 203-A.3: 收集
            self.state.hints_used += 1
            self.state.phase = "guided"

            print(f"\n[GuidedLoop] Turn {self.state.turn} (guided)——给hint: {hint[:80]}...")

            # 步骤10: 增量编译——构造包含之前上下文+hint的prompt
            guided_prompt = self._construct_guided_prompt(hint)

            # 步骤3: 发送给数学大师
            turn = self.adapter.send(guided_prompt, is_hint=True)
            self.state.last_response = turn.response
            print(f"[GuidedLoop] Turn {self.state.turn}完成, response长度={len(turn.response)}")

            # 检查完成
            if self._check_completion(turn.response):
                self.state.completed = True
                self.state.completion_reason = "completed_after_hint"
                self.state.phase = "done"
                return

        if not self.state.completed:
            self.state.completion_reason = "max_turns_reached"
            self.state.phase = "done"

    def _detect_stall(self, response: str) -> bool:
        """步骤6: 卡点检测——简化版，检测卡点信号"""
        response_lower = response.lower()
        for signal in self.STALL_SIGNALS:
            if signal in response or signal.lower() in response_lower:
                return True
        # 另一个信号：response太短（可能没有实质内容）
        if len(response) < 100:
            return True
        return False

    def _analyze_stall_reason(self, response: str) -> str:
        """步骤7: 诊断——分析卡点原因"""
        if "不知道" in response or "没有思路" in response:
            return "lack_knowledge"
        if "不确定" in response or "难以判断" in response:
            return "uncertain"
        if "需要更多信息" in response:
            return "need_more_info"
        if len(response) < 100:
            return "response_too_short"
        return "unknown_stall"

    def _ai_diagnose_stall(self, response: str) -> Optional[Dict[str, Any]]:
        """205-A: 步骤7 AI诊断——经典计算不确定时调用AI分析Solver思路

        调用时机：stall_reason == "unknown_stall"（经典计算无法判定卡点类型）
        返回：{refined_stall_reason, confidence, reasoning, is_real_stall}
        如果AI调用失败，返回None（fallback到经典计算的unknown_stall）
        """
        # 205-A.1: AI诊断prompt
        prompt = self._build_ai_diagnosis_prompt(response)

        # 205-A.2: 调用AI——通过DevinCliAdapter或直接API
        # 注：这里用简化的本地分析作为POC，实际部署时调用外部AI
        try:
            ai_result = self._call_ai_for_diagnosis(prompt, response)
            return ai_result
        except Exception as e:
            print(f"[GuidedLoop] AI诊断失败（fallback到经典计算）: {e}")
            return None

    def _build_ai_diagnosis_prompt(self, response: str) -> str:
        """205-A.1: 构造AI诊断prompt"""
        # 截取response最后2000字符（避免过长）
        response_excerpt = response[-2000:] if len(response) > 2000 else response
        return f"""你是数学大师系统的卡点诊断AI。

Solver（数学大师）的当前输出：
{response_excerpt}

经典计算检测到卡点但无法判定类型（unknown_stall）。

7种卡点类型：
1. lack_knowledge——缺少具体数学知识
2. uncertain——方向不确定，需要验证
3. need_more_info——需要更多信息
4. response_too_short——回答过短
5. unknown_stall——经典计算无法判定
6. strategy_exhaustion——策略耗尽
7. representation_unsuitable——表示不合适

请分析：
1. Solver是真的卡住了，还是在做合理的策略转换？
2. 如果卡住了，真实原因是什么？（从上述类型中选择，或提出新类型）
3. 你的判断依据是什么？

输出JSON：
{{
  "refined_stall_reason": "卡点类型",
  "confidence": 0.0-1.0,
  "reasoning": "判断依据",
  "is_real_stall": true/false
}}

注意：不要只看关键词，要理解Solver的思路内容。"""

    def _call_ai_for_diagnosis(self, prompt: str, response: str) -> Dict[str, Any]:
        """205-A.2: 调用AI做诊断

        POC实现：用简化的本地规则做初步诊断
        实际部署时替换为DevinCliAdapter或外部AI调用
        """
        # POC简化版：基于response内容的规则诊断
        # 实际部署时应调用外部AI
        response_lower = response.lower()

        # 规则1: 如果response包含"尝试"但没"失败"——可能是合理策略转换
        if "尝试" in response and "失败" not in response and "不行" not in response:
            return {
                "refined_stall_reason": "uncertain",
                "confidence": 0.6,
                "reasoning": "Solver在尝试新方法但未确认——可能是合理策略转换",
                "is_real_stall": False,
            }

        # 规则2: 如果response包含"不知道"或"不确定"——lack_knowledge
        if "不知道" in response or "不确定" in response or "不了解" in response:
            return {
                "refined_stall_reason": "lack_knowledge",
                "confidence": 0.8,
                "reasoning": "Solver明确表示不知道——缺少知识",
                "is_real_stall": True,
            }

        # 规则3: 如果response包含"但是"或"然而"——可能有矛盾
        if "但是" in response or "然而" in response or "矛盾" in response:
            return {
                "refined_stall_reason": "uncertain",
                "confidence": 0.65,
                "reasoning": "Solver遇到矛盾或转折——需要验证方向",
                "is_real_stall": True,
            }

        # 规则4: 如果response很短——response_too_short（放最后，避免误判）
        if len(response) < 200:
            return {
                "refined_stall_reason": "response_too_short",
                "confidence": 0.7,
                "reasoning": "回答过短——可能没有展开思路",
                "is_real_stall": True,
            }

        # 默认: 仍为unknown_stall
        return {
            "refined_stall_reason": "unknown_stall",
            "confidence": 0.3,
            "reasoning": "AI诊断无法确定卡点类型——建议给strategy级提示",
            "is_real_stall": True,
        }

    def _generate_hint(self, stall_reason: str, last_response: str) -> tuple:
        """步骤8-9: 模式匹配 + 选择动作——简化版，根据卡点原因生成hint

        203-A.2: 提示发出前调用四门泄漏审计
        205-B: AI编译提示——根据Solver具体思路生成针对性提示
        返回 (hint_text, hint_level, leakage_audit_result)
        """
        # 从HINT_REGISTRY取经典提示骨架
        entry = HINT_REGISTRY.get(stall_reason, HINT_REGISTRY["unknown_stall"])
        classic_hint = entry["text"]
        level = entry["level"]

        # 205-B: AI编译提示——根据Solver具体思路生成针对性提示
        ai_hint, ai_compiled = self._ai_compile_hint(stall_reason, last_response, classic_hint)
        if ai_compiled:
            hint = ai_hint
            # AI编译的提示默认降为strategy级
            # 因为AI编译的prompt要求"优先给策略"，且泄漏审计会拦截knowledge级内容
            level = "strategy"
        else:
            hint = classic_hint

        # 203-A.2 + 205-B: 调用四门泄漏审计（AI生成的提示也要过审计）
        leakage_audit = self._run_leakage_audit(hint)

        # 如果审计fail，降级为meta级提示
        if leakage_audit and leakage_audit.get("overall_result") == "fail":
            hint = FALLBACK_META_HINT
            level = "meta"
            leakage_audit["degraded"] = True

        return hint, level, leakage_audit

    def _ai_compile_hint(
        self, stall_reason: str, solver_response: str, classic_hint: str
    ) -> tuple:
        """205-B: AI编译提示——根据Solver具体思路生成针对性提示

        调用时机：硬编码提示不够针对性时（response包含具体数学内容）
        返回 (ai_hint, ai_compiled)
        如果AI编译失败或response过短，返回 (classic_hint, False)
        """
        # 205-B.0: 调用时机判定
        # response过短时直接用经典提示（<30字符基本无内容可分析）
        if len(solver_response) < 30:
            return classic_hint, False
        # response明确完成时不给提示（由上层检查）
        # 其他情况调用AI编译

        # 205-B.1: 构造AI编译prompt
        prompt = self._build_ai_compile_prompt(stall_reason, solver_response, classic_hint)

        # 205-B.2: 调用AI编译
        try:
            ai_hint = self._call_ai_for_compilation(prompt, stall_reason, solver_response, classic_hint)
            if ai_hint and len(ai_hint) > 20:  # 基本有效性检查
                return ai_hint, True
            return classic_hint, False
        except Exception as e:
            print(f"[GuidedLoop] AI编译失败（fallback到经典提示）: {e}")
            return classic_hint, False

    def _build_ai_compile_prompt(
        self, stall_reason: str, solver_response: str, classic_hint: str
    ) -> str:
        """205-B.1: 构造AI编译prompt"""
        response_excerpt = solver_response[-1500:] if len(solver_response) > 1500 else solver_response
        return f"""你是数学大师系统的提示编译AI。

当前卡点原因：{stall_reason}
Solver的当前输出：
{response_excerpt}

经典计算生成的提示骨架：
{classic_hint}

请生成一条针对性提示，要求：
1. 不包含答案或答案的等价表述（会经过泄漏审计）
2. 针对Solver的具体思路内容，不是通用提示
3. 优先给策略（解题方向），其次给元提示（继续/更详细），最后才给知识
4. 如果Solver的思路方向是对的，只给"继续"的元提示
5. 如果Solver的思路方向不对，给策略提示引导换方向

输出格式：直接输出提示文本，不要JSON包装。"""

    def _call_ai_for_compilation(
        self, prompt: str, stall_reason: str, solver_response: str, classic_hint: str
    ) -> str:
        """205-B.2: 调用AI编译提示

        POC实现：用简化的规则生成针对性提示
        实际部署时替换为外部AI调用
        """
        # POC简化版：基于stall_reason和response内容生成针对性提示
        # 实际部署时应调用外部AI

        # 如果Solver在尝试某个方向——给strategy级提示鼓励继续
        if "尝试" in solver_response and "失败" not in solver_response:
            return f"你正在尝试的方向有潜力。请继续深入，给出更具体的推导步骤。"

        # 如果Solver遇到矛盾——给strategy级提示引导换方向
        if "但是" in solver_response or "然而" in solver_response:
            return f"你遇到了一个障碍。请尝试换一个角度——考虑用不同的数学工具或表示方法。"

        # 如果Solver明确不知道——给strategy级提示（不给knowledge）
        if "不知道" in solver_response or "不确定" in solver_response:
            return f"请从你已知的相关知识出发，尝试建立与这个问题的联系。先考虑最简单的情况。"

        # 默认：用经典提示骨架
        return classic_hint

    def _run_leakage_audit(self, hint: str) -> Optional[Dict[str, Any]]:
        """203-A.2 + 203-B.2: 调用leakage_audit.py的四门审计

        203-B.2: Controller(orchestrator)编译提示时强制检查可见性——
        Controller的可见性标签can_read_truth_vault=False，
        编译提示时只能从K维度取知识，不能从truth_vault取。
        """
        # 203-B.2: 强制检查Controller不可读truth_vault
        if self._truth_vault_checker:
            check = self._truth_vault_checker.check_access("orchestrator", "truth_vault", "R")
            if check["allowed"]:
                # 这不应该发生——orchestrator对truth_vault应该是"—"
                return {
                    "audit_error": "角色隔离违规：orchestrator可读truth_vault",
                    "overall_result": "error",
                    "isolation_violation": True,
                }

        try:
            from ..heuristics.leakage_audit import AnswerEquivalenceAuditor
            auditor = AnswerEquivalenceAuditor()
            # 203-B.1: 使用truth_vault答案做更严格的审计
            # 注意：这里把答案传给auditor是允许的——auditor角色可读truth_vault
            # 但Controller本身不能读——Controller只看到审计结果（pass/fail），不看答案
            task = {"goal": self._truth_vault_answer} if self._truth_vault_answer else {"goal": ""}
            result = auditor.run_four_gates(hint, task)
            return result
        except Exception as e:
            # 审计失败时不阻塞——返回error，提示照常发出
            # 但记录审计失败
            return {"audit_error": str(e), "overall_result": "error"}

    def _construct_guided_prompt(self, hint: str) -> str:
        """步骤10: 增量编译——构造包含上下文+hint的prompt"""
        if self.state.turn == 2:
            # 第2turn：包含原始问题+第1turn回答+hint
            return (
                f"问题：{self.problem}\n\n"
                f"你之前的回答：\n{self.state.last_response}\n\n"
                f"系统提示：{hint}\n\n"
                f"请基于以上信息继续。"
            )
        else:
            # 后续turn：只包含上一次回答+hint（避免prompt过长）
            return (
                f"你之前的回答：\n{self.state.last_response[-2000:]}\n\n"
                f"系统提示：{hint}\n\n"
                f"请继续。"
            )

    def _check_completion(self, response: str) -> bool:
        """检查数学大师是否给出了完整的回答"""
        for signal in self.COMPLETION_SIGNALS:
            if signal in response:
                return True
        # 另一个信号：response很长且包含数学公式（可能已完成）
        if len(response) > 2000 and ("$" in response or "\\(" in response):
            return True
        return False
