"""RealtimePipeline: 实时解析+检索+决策管线。

整合TrajectoryWatcher + StallDetector + MathParser + RetrievalPipeline +
ConstrainedPolicy，实现从Solver trajectory到提示选择的完整实时流程。

数据流：
  solver-harness → sessions.db
       ↓
  TrajectoryWatcher.poll() → Round(agent_output)
       ↓
  StallDetector.check() → StallEvent
       ↓
  MathParser.parse() → ParseResult
       ↓
  RetrievalPipeline.retrieve() → List[MatchedRule]
       ↓
  ConstrainedPolicy.select() → SelectionResult(选中的Q)
       ↓
  HintInjector.inject() → tmux send-keys到Solver

两种运行模式：
1. 被动模式：外部调用pipeline.process_round(round_data)，返回提示选择结果
2. 主动模式：pipeline.run()持续监控，检测到卡点时自动处理
"""

import json
import time
from dataclasses import dataclass, field
from typing import Optional, List, Callable

from .trajectory_watcher import TrajectoryWatcher, Round
from .stall_detector import StallDetector, StallEvent
from ..parser.models import ParseRequest, ParseResult, SixTuple, TurnRecord
from ..parser.parser import MathParser
from ..parser.llm_parser import LLMParser
from ..retrieval import RetrievalPipeline
from ..hgraph.hgraph_store import HeuristicRuleGraph
from ..policy.constrained_optimizer import (
    ConstrainedPolicy,
    MatchedRule as PolicyMatchedRule,
    ConstraintValues,
    SelectionResult,
    leakage_risk,
)
from ..budget import BudgetManager, BudgetType


@dataclass
class PipelineResult:
    """管线一次处理的结果。"""
    round_index: int
    stall_event: Optional[StallEvent] = None
    parse_result: Optional[ParseResult] = None
    matched_rules: list = field(default_factory=list)  # List[MatchedRule]
    selection_result: Optional[SelectionResult] = None
    selected_q: str = ""             # 选中的提示文本
    injected: bool = False           # 是否已注入
    error: str = ""                  # 错误信息
    timestamp: float = 0.0


class RealtimePipeline:
    """
    实时解析+检索+决策管线。

    用法（被动模式）：
        pipeline = RealtimePipeline(
            session_id="xxx",
            hgraph=case_253_graph,
            problem_text="...",
        )
        # 外部循环调用
        for round_data in watcher.watch():
            result = pipeline.process_round(round_data)
            if result.selected_q:
                pipeline.inject_hint(result.selected_q)

    用法（主动模式）：
        pipeline = RealtimePipeline(
            session_id="xxx",
            hgraph=case_253_graph,
            problem_text="...",
            tmux_session="harness-exp001",
        )
        pipeline.run(max_rounds=10)
    """

    def __init__(
        self,
        session_id: str,
        hgraph: HeuristicRuleGraph,
        problem_text: str,
        math_parser: Optional[MathParser] = None,
        retrieval_pipeline: Optional[RetrievalPipeline] = None,
        policy: Optional[ConstrainedPolicy] = None,
        budget_manager: Optional[BudgetManager] = None,
        stall_detector: Optional[StallDetector] = None,
        tmux_session: str = "",
        hint_injector: Optional[Callable[[str, str], bool]] = None,
    ):
        """
        Args:
            session_id: Devin CLI session ID
            hgraph: 启发规则图（含已发布的Q规则）
            problem_text: 题目原文
            math_parser: 解析器（默认创建，用mock LLM）
            retrieval_pipeline: 检索管线（默认创建）
            policy: 约束策略（默认创建）
            budget_manager: 预算管理器（默认创建）
            stall_detector: 卡点检测器（默认创建）
            tmux_session: tmux session名（用于hint注入）
            hint_injector: 自定义提示注入函数（text, tmux_session）→ bool
        """
        self.session_id = session_id
        self.hgraph = hgraph
        self.problem_text = problem_text
        self.math_parser = math_parser or MathParser()
        self.retrieval_pipeline = retrieval_pipeline or RetrievalPipeline()
        self.policy = policy or ConstrainedPolicy()
        self.budget_manager = budget_manager or BudgetManager()
        self.stall_detector = stall_detector or StallDetector()
        self.tmux_session = tmux_session
        self.hint_injector = hint_injector or self._default_injector

        # 状态
        self._history: List[TurnRecord] = []
        self._current_six_tuple: Optional[SixTuple] = None
        self._round_count: int = 0
        self._last_node_timestamp: float = time.time()

    def _default_injector(self, hint_text: str, tmux_session: str) -> bool:
        """
        默认提示注入：通过tmux send-keys注入到Solver session。

        Args:
            hint_text: 提示文本
            tmux_session: tmux session名

        Returns:
            True if成功
        """
        if not tmux_session:
            return False
        import subprocess
        try:
            # 用tmux send-keys注入提示
            # 把多行文本用send-keys逐行发送
            lines = hint_text.strip().split("\n")
            for line in lines:
                subprocess.run(
                    ["tmux", "send-keys", "-t", tmux_session, line],
                    check=True,
                    capture_output=True,
                )
            # 发送Enter
            subprocess.run(
                ["tmux", "send-keys", "-t", tmux_session, "Enter"],
                check=True,
                capture_output=True,
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"[HintInjector] tmux send-keys失败: {e}")
            return False

    def process_round(self, round_data: Round) -> PipelineResult:
        """
        处理一个Round：解析 → 检索 → 决策。

        这是被动模式的核心方法。外部调用者通过TrajectoryWatcher获取Round，
        然后调用本方法处理。

        Args:
            round_data: 从TrajectoryWatcher获取的轮次数据

        Returns:
            PipelineResult，包含解析结果、匹配规则、选中的提示
        """
        result = PipelineResult(
            round_index=round_data.round_index,
            timestamp=time.time(),
        )

        # ---- 第一步：卡点检测 ----
        stall_event = self.stall_detector.check_semantic(round_data)
        if stall_event:
            result.stall_event = stall_event

        # ---- 第二步：解析 ----
        try:
            parse_request = ParseRequest(
                agent_output=round_data.agent_output,
                round_index=round_data.round_index,
                problem_text=self.problem_text,
                history=list(self._history),
                current_six_tuple=self._current_six_tuple,
                run_id=self.session_id,
                model_version="realtime",
                timestamp=str(round_data.end_timestamp),
            )
            parse_result = self.math_parser.parse(parse_request)
            result.parse_result = parse_result

            # 更新六元组状态
            self._current_six_tuple = parse_result.six_tuple

            # 更新历史
            self._history.append(TurnRecord(
                q_text="(auto-detected round)",
                a_text=round_data.agent_output[:500],
                round_index=round_data.round_index,
            ))

        except Exception as e:
            result.error = f"parse error: {e}"
            return result

        # ---- 第三步：检索 ----
        try:
            matched_rules = self.retrieval_pipeline.retrieve(
                parse_result, self.hgraph, top_k=5,
            )
            result.matched_rules = matched_rules
        except Exception as e:
            result.error = f"retrieval error: {e}"
            return result

        # ---- 第四步：预算检查 ----
        if self.budget_manager.is_hint_exhausted():
            result.error = "budget exhausted"
            return result

        # ---- 第五步：策略选择 ----
        if not matched_rules:
            return result

        try:
            # 转换matching.MatchedRule到policy.MatchedRule格式
            # matching.MatchedRule: {rule_id, match_score, guard_passed, rule}
            # policy.MatchedRule: {rule: HeuristicRule, match_score}
            policy_candidates = []
            for mr in matched_rules:
                # mr.rule已经是HeuristicRule对象
                policy_candidates.append(PolicyMatchedRule(
                    rule=mr.rule,
                    match_score=mr.match_score,
                ))

            if not policy_candidates:
                return result

            selection = self.policy.select(policy_candidates, parse_result.six_tuple)
            result.selection_result = selection

            if selection.selected_rule:
                result.selected_q = selection.selected_rule.rhs

        except Exception as e:
            result.error = f"policy error: {e}"
            return result

        return result

    def inject_hint(self, hint_text: str) -> bool:
        """
        注入提示到Solver session。

        Args:
            hint_text: 提示文本

        Returns:
            True if成功
        """
        return self.hint_injector(hint_text, self.tmux_session)

    def run(
        self,
        max_rounds: int = 10,
        max_time: float = 600.0,
        auto_inject: bool = True,
    ) -> List[PipelineResult]:
        """
        主动模式：持续监控sessions.db，自动处理轮次。

        Args:
            max_rounds: 最大轮次数
            max_time: 最大运行时间（秒）
            auto_inject: 是否自动注入提示

        Returns:
            所有处理结果列表
        """
        watcher = TrajectoryWatcher(session_id=self.session_id)
        results = []
        start_time = time.time()

        while len(results) < max_rounds and (time.time() - start_time) < max_time:
            # 轮询新轮次
            new_rounds = watcher.poll()

            for round_data in new_rounds:
                result = self.process_round(round_data)
                results.append(result)

                # 自动注入
                if auto_inject and result.selected_q:
                    success = self.inject_hint(result.selected_q)
                    result.injected = success

                if len(results) >= max_rounds:
                    break

            # 超时卡点检测
            elapsed_since_last = time.time() - self._last_node_timestamp
            if elapsed_since_last > self.stall_detector.timeout:
                # 尝试解析当前未完成的轮次
                partial = watcher.get_current_partial()
                if partial and partial.agent_output:
                    result = self.process_round(partial)
                    if auto_inject and result.selected_q:
                        success = self.inject_hint(result.selected_q)
                        result.injected = success
                    results.append(result)

            time.sleep(watcher.poll_interval)

        return results
