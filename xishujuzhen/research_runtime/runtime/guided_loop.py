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

    def _generate_hint(self, stall_reason: str, last_response: str) -> tuple:
        """步骤8-9: 模式匹配 + 选择动作——简化版，根据卡点原因生成hint

        203-A.2: 提示发出前调用四门泄漏审计
        返回 (hint_text, hint_level, leakage_audit_result)
        """
        # 从HINT_REGISTRY取提示
        entry = HINT_REGISTRY.get(stall_reason, HINT_REGISTRY["unknown_stall"])
        hint = entry["text"]
        level = entry["level"]

        # 203-A.2: 调用四门泄漏审计
        leakage_audit = self._run_leakage_audit(hint)

        # 如果审计fail，降级为meta级提示
        if leakage_audit and leakage_audit.get("overall_result") == "fail":
            hint = FALLBACK_META_HINT
            level = "meta"
            leakage_audit["degraded"] = True

        return hint, level, leakage_audit

    def _run_leakage_audit(self, hint: str) -> Optional[Dict[str, Any]]:
        """203-A.2: 调用leakage_audit.py的四门审计"""
        try:
            from ..heuristics.leakage_audit import AnswerEquivalenceAuditor
            auditor = AnswerEquivalenceAuditor()
            # task为空时四门审计仍可执行（gate1/gate2检查字面匹配）
            task = {"goal": getattr(self, '_truth_vault_answer', '')}
            result = auditor.run_four_gates(hint, task)
            return result
        except Exception as e:
            # 审计失败时不阻塞——返回None，提示照常发出
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
