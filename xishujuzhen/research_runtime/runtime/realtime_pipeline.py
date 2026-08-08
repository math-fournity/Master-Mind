"""
RealtimePipeline: 编排实时闭环——trajectory适配器 → parser → stall检测
→ retrieval → policy → 提示注入。

这是04工作线（端到端效果验证）的核心组件，把01工作线的4个模块
（MathParser, StallDetector, RetrievalPipeline, ConstrainedPolicy）
与02工作线的solver-harness trajectory数据集成起来。

数据流：
  solver-harness → sessions_db/trajectory.jsonl
  → TrajectoryAdapter.poll_new_turns() → List[ParseRequest]
  → MathParser.parse() → ParseResult（语义事件+六元组）
  → StallDetector.detect() → 卡点检测
  → （检测到卡点时）RetrievalPipeline.retrieve() → List[MatchedRule]
  → ConstrainedPolicy.select() → SelectionResult
  → HintInjector.inject() → 提示注入到Solver session
  → （Solver收到提示后继续推理，循环）
"""

import time
import json
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from datetime import datetime, timezone

from .trajectory_adapter import TrajectoryAdapter
from .hint_injector import HintInjector
from ..parser.parser import MathParser
from ..parser.models import ParseRequest, ParseResult, SixTuple
from ..verification.stall_detector import StallDetector, StallType
from ..retrieval.retrieval_pipeline import RetrievalPipeline
from ..policy.constrained_optimizer import ConstrainedPolicy
from ..heuristics.rule_store import HeuristicRuleStore


@dataclass
class RealtimeResult:
    """实时管线的运行结果。"""
    exp_id: str
    total_rounds: int = 0
    total_parses: int = 0
    stall_detections: List[Dict] = field(default_factory=list)
    hints_injected: List[Dict] = field(default_factory=list)
    final_six_tuple: Optional[Dict] = None
    done: bool = False
    done_reason: str = ""
    start_time: float = 0.0
    end_time: float = 0.0

    @property
    def duration(self) -> float:
        return self.end_time - self.start_time

    def to_dict(self) -> dict:
        return {
            "exp_id": self.exp_id,
            "total_rounds": self.total_rounds,
            "total_parses": self.total_parses,
            "stall_detections": list(self.stall_detections),
            "hints_injected": list(self.hints_injected),
            "final_six_tuple": self.final_six_tuple,
            "done": self.done,
            "done_reason": self.done_reason,
            "duration": self.duration,
        }


class RealtimePipeline:
    """编排实时闭环：trajectory → parser → stall → retrieval → policy → inject。"""

    def __init__(
        self,
        exp_id: str,
        problem_text: str,
        trajectory_jsonl_path: str,
        hgraph_store: HeuristicRuleStore,
        parser: MathParser,
        stall_detector: StallDetector,
        retrieval: RetrievalPipeline,
        policy: ConstrainedPolicy,
        result_output_path: Optional[str] = None,
    ):
        self.exp_id = exp_id
        self.problem_text = problem_text
        self.result_output_path = result_output_path

        # 组件
        self.adapter = TrajectoryAdapter(
            trajectory_jsonl_path=trajectory_jsonl_path,
            problem_text=problem_text,
            run_id=f"realtime-{exp_id}",
        )
        self.parser = parser
        self.stall_detector = stall_detector
        self.retrieval = retrieval
        self.policy = policy
        self.injector = HintInjector(exp_id=exp_id)

        # H图存储（用于retrieval）
        self.hgraph_store = hgraph_store
        self.hgraph = hgraph_store.load_hgraph() if hasattr(hgraph_store, "load_hgraph") else None

        # 运行状态
        self.progress_history: List[Dict[str, Any]] = []
        self.budget: Dict[str, Any] = {"total": 100, "used": 0}
        self.obligations: Dict[str, Any] = {}
        self.last_parse_result: Optional[ParseResult] = None
        self.result = RealtimeResult(exp_id=exp_id)

    def run(
        self,
        max_rounds: int = 20,
        timeout: int = 600,
        poll_interval: float = 3.0,
        stall_check_interval: int = 3,  # 每3轮检测一次卡点
    ) -> RealtimeResult:
        """持续轮询trajectory，解析，检测卡点，检索，注入提示。

        Args:
            max_rounds: 最大轮次（含提示注入轮）
            timeout: 最大运行时间（秒）
            poll_interval: 无新数据时的等待间隔（秒）
            stall_check_interval: 每几轮检测一次卡点

        Returns:
            RealtimeResult
        """
        self.result.start_time = time.time()
        print(f"=== RealtimePipeline started for {self.exp_id} ===")
        print(f"  trajectory: {self.adapter.trajectory_jsonl_path}")
        print(f"  max_rounds: {max_rounds}, timeout: {timeout}s")

        while True:
            # 检查终止条件
            elapsed = time.time() - self.result.start_time
            if elapsed >= timeout:
                self.result.done = True
                self.result.done_reason = "timeout"
                break
            if self.result.total_rounds >= max_rounds:
                self.result.done = True
                self.result.done_reason = "max_rounds"
                break

            # 1. 轮询新turn
            new_requests = self.adapter.poll_new_turns()

            if not new_requests:
                time.sleep(poll_interval)
                continue

            # 2. 解析每个新turn
            for request in new_requests:
                print(f"\n[Round {request.round_index}] Parsing new turn...")
                try:
                    parse_result = self.parser.parse(request)
                    self.last_parse_result = parse_result
                    self.result.total_parses += 1

                    # 更新六元组
                    self.adapter.update_six_tuple(parse_result.six_tuple)

                    # 更新progress_history
                    self.progress_history.append(
                        self._six_tuple_to_progress(parse_result.six_tuple)
                    )

                    # 更新obligations
                    self._update_obligations(parse_result.six_tuple)

                    print(f"  Parsed: {len(parse_result.semantic_events)} events, "
                          f"confidence={parse_result.parse_confidence:.2f}")

                except Exception as e:
                    print(f"  Parse error: {e}")
                    continue

            # 3. 卡点检测（每stall_check_interval轮检测一次）
            if self.result.total_parses > 0 and self.result.total_parses % stall_check_interval == 0:
                print(f"\n[Stall check] Checking for stalls...")
                detections = self.stall_detector.detect(
                    progress_history=self.progress_history,
                    budget=self.budget,
                    obligations=self.obligations,
                )

                # 过滤掉"必要探索"（不是真正卡点）
                real_stalls = [
                    d for d in detections
                    if d.type != StallType.NECESSARY_EXPLORATION
                ]

                if real_stalls:
                    for d in real_stalls:
                        print(f"  Stall detected: {d.type.value} - {d.detail}")
                        self.result.stall_detections.append({
                            "round": self.result.total_parses,
                            "type": d.type.value,
                            "detail": str(d.detail) if hasattr(d, "detail") else "",
                        })

                    # 4. 检索+选择
                    if self.last_parse_result and self.hgraph:
                        print(f"  Retrieving hints...")
                        matched = self.retrieval.retrieve(
                            parse_result=self.last_parse_result,
                            hgraph=self.hgraph,
                        )

                        if matched:
                            print(f"  {len(matched)} rules matched, selecting...")
                            selection = self.policy.select(
                                matched_rules=matched,
                                six_tuple=self.last_parse_result.six_tuple,
                            )

                            if selection.selected_rule and not selection.is_abstain:
                                hint_text = selection.selected_rule.hint_text if hasattr(selection.selected_rule, "hint_text") else str(selection.selected_rule)
                                print(f"  Selected hint: {hint_text[:100]}...")
                                print(f"  Reason: {selection.reason}")

                                # 5. 注入提示
                                success = self.injector.inject(hint_text)
                                if success:
                                    self.result.hints_injected.append({
                                        "round": self.result.total_rounds,
                                        "hint_text": hint_text,
                                        "reason": selection.reason,
                                        "stall_type": real_stalls[0].type.value,
                                    })
                                    self.result.total_rounds += 1
                                    # 提示注入后等待Solver处理
                                    time.sleep(10)
                            elif selection.is_abstain:
                                print(f"  Policy abstained: {selection.reason}")
                        else:
                            print(f"  No rules matched")
                else:
                    print(f"  No stalls detected")

        self.result.end_time = time.time()
        self.result.total_rounds = self.result.total_rounds

        # 记录最终六元组
        if self.last_parse_result:
            self.result.final_six_tuple = self.last_parse_result.six_tuple.to_dict()

        # 写结果文件
        if self.result_output_path:
            with open(self.result_output_path, "w") as f:
                json.dump(self.result.to_dict(), f, indent=2, ensure_ascii=False, default=str)

        print(f"\n=== RealtimePipeline finished ===")
        print(f"  Rounds: {self.result.total_rounds}")
        print(f"  Parses: {self.result.total_parses}")
        print(f"  Stalls detected: {len(self.result.stall_detections)}")
        print(f"  Hints injected: {len(self.result.hints_injected)}")
        print(f"  Done: {self.result.done_reason}")
        print(f"  Duration: {self.result.duration:.1f}s")

        return self.result

    def _six_tuple_to_progress(self, six_tuple: SixTuple) -> Dict[str, Any]:
        """把六元组转换为StallDetector需要的progress_history格式。"""
        return {
            "round": self.result.total_parses,
            "V_t": len(six_tuple.verified_facts) if hasattr(six_tuple, "verified_facts") else 0,
            "F_t": len(six_tuple.frontier_nodes) if hasattr(six_tuple, "frontier_nodes") else 0,
            "O_t": len(six_tuple.open_obligations) if hasattr(six_tuple, "open_obligations") else 0,
            "U_t": len(six_tuple.unsolved_problems) if hasattr(six_tuple, "unsolved_problems") else 0,
        }

    def _update_obligations(self, six_tuple: SixTuple):
        """从六元组更新obligations状态。"""
        if hasattr(six_tuple, "open_obligations"):
            self.obligations = {
                "open": six_tuple.open_obligations if isinstance(six_tuple.open_obligations, list) else [],
            }
