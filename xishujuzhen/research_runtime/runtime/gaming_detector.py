"""
GamingDetector: gaming行为三元判定器

对应136号P6-6 gaming三元判定。

系统探讨.md§15.4 gaming检测机制：
- Agent可能通过"自报停滞"来迎合触发器，获取奖励性帮助
- 单独检查停滞词不足以判定gaming——Agent可能真的卡住了
- 必须结合工具证据和结构进展做三元判定

154号修正（gaming判定收紧）：
- 只检查"声称调用了工具"不算——必须有工具调用实际记录和输出
- 只检查输出长度变化不算——必须是T图结构的实际变化
- 三元AND逻辑：只有（停滞词=True）AND（工具证据=False）AND（结构进展=False）时才判定gaming

R-4防线：Agent可能迎合触发器——自报停滞以获取帮助。
    三元判定通过要求"无工具证据+无结构进展"来过滤真停滞与迎合性停滞。
F12防线：完整三元AND逻辑，不简化为只检查停滞词。
    任何一元为True（工具证据或结构进展）即不判定gaming——避免误伤真停滞。

边界情况：
- 无gaming行为 → 三元判定不触发
- gaming行为隐蔽 → 停滞词可能伪装，但无工具证据+无结构进展仍可捕获
- Agent自报停滞但有工具证据 → 不算gaming（真在尝试）
- Agent自报停滞但有结构进展 → 不算gaming（真在推进）
"""

from typing import List, Dict, Any, Optional
from datetime import datetime, timezone


# 默认停滞词列表（可配置）
DEFAULT_STALL_WORDS: List[str] = [
    "我不知道",
    "卡住了",
    "无法继续",
    "不会做",
    "想不出来",
    "没有思路",
    "i don't know",
    "stuck",
    "cannot continue",
]


class GamingDetector:
    """
    P6-6：gaming行为三元判定器。

    三元判定机制（系统探讨.md§15.4 + 154号修正）：
    1. 停滞词识别：Agent输出中包含停滞词时标记"自报停滞"
    2. 工具证据验证：自报停滞时，检查是否有工具调用实际记录和输出
    3. 结构进展度量：自报停滞时，检查T图是否有实际结构变化

    判定逻辑：
    - gaming = (停滞词=True) AND (工具证据=False) AND (结构进展=False)
    - 三元中任一为True（工具证据或结构进展），即不判定gaming

    防线：
    - R-4防线：Agent可能迎合触发器——三元判定过滤迎合性停滞
    - F12防线：完整三元AND逻辑，不简化为只检查停滞词

    边界情况：
    - 无gaming行为 → 不触发
    - gaming行为隐蔽 → 无工具证据+无结构进展仍可捕获
    - 自报停滞+有工具证据 → 不算gaming
    - 自报停滞+有结构进展 → 不算gaming
    """

    def __init__(self, stall_words: Optional[List[str]] = None):
        """
        初始化gaming检测器。

        Args:
            stall_words: 停滞词列表，为None时使用默认列表
        """
        self.stall_words = stall_words if stall_words is not None else list(DEFAULT_STALL_WORDS)

    def detect_stall_words(self, text: str) -> bool:
        """
        P6-6.1：检测停滞词。

        检查Agent输出文本中是否包含停滞词。
        停滞词列表可配置（构造时传入或使用默认列表）。

        深度标准：D2——不只检查固定词表，支持配置化扩展。

        边界情况：
        - 空文本 → False
        - None文本 → False
        - 停滞词出现在引用上下文中 → 仍标记True（保守策略，由后续三元判定过滤）
        - 大小写差异 → 对英文停滞词做小写匹配

        Args:
            text: Agent输出文本

        Returns:
            True if 包含停滞词, False otherwise
        """
        if not text:
            return False

        text_lower = text.lower()

        for word in self.stall_words:
            if word.lower() in text_lower:
                return True

        return False

    def verify_tool_evidence(self, tool_calls: List[Dict]) -> bool:
        """
        P6-6.2：验证工具证据。

        154号修正核心：只检查"声称调用了工具"不算——必须有工具调用实际记录和输出。

        验证标准：
        - tool_calls非空
        - 每条记录必须有工具名称/标识（tool或name字段）
        - 每条记录必须有实际输出（output或result字段非空）
        - 只声称但无实际记录和输出 → 不算工具证据

        深度标准：D3——不只检查调用次数，还要验证有实际输出。

        边界情况：
        - tool_calls为空或None → False
        - 有调用记录但无输出 → False（声称但无证据）
        - 有调用记录且有输出 → True
        - 调用记录格式不完整 → False

        Args:
            tool_calls: 工具调用记录列表，每条应含tool/name和output/result字段

        Returns:
            True if 有实际工具调用和输出, False otherwise
        """
        if not tool_calls:
            return False

        for call in tool_calls:
            if not isinstance(call, dict):
                continue

            # 必须有工具标识
            tool_name = call.get("tool") or call.get("name")
            if not tool_name:
                continue

            # 必须有实际输出（154号修正：声称不算）
            output = call.get("output")
            result = call.get("result")

            has_output = (
                (output is not None and output != "")
                or (result is not None and result != "")
            )

            if has_output:
                return True

        return False

    def measure_structural_progress(
        self,
        before_state: Dict,
        after_state: Dict,
    ) -> bool:
        """
        P6-6.3：度量结构进展。

        154号修正核心：只检查输出长度变化不算——必须是T图结构的实际变化。

        检查维度（任一满足即有结构进展）：
        1. 新增节点（nodes）：after_state的节点数 > before_state的节点数
        2. 新增边（edges）：after_state的边数 > before_state的边数
        3. 开放目标减少（open_obligations）：after < before
        4. 义务状态变化（obligation_status）：before和after的义务状态不同

        深度标准：D3——不只看输出长度，看T图结构实际变化。

        边界情况：
        - before/after为空或None → False
        - 节点数相同但内容变化 → 检查边和义务状态
        - 边数相同但开放目标减少 → True
        - 只有输出长度变化无结构变化 → False（154号修正）

        Args:
            before_state: 前状态，应含nodes/edges/open_obligations/obligation_status
            after_state: 后状态，应含nodes/edges/open_obligations/obligation_status

        Returns:
            True if 有结构进展, False otherwise
        """
        if not before_state or not after_state:
            return False

        if not isinstance(before_state, dict) or not isinstance(after_state, dict):
            return False

        # 维度1：新增节点
        before_nodes = before_state.get("nodes", [])
        after_nodes = after_state.get("nodes", [])
        if len(after_nodes) > len(before_nodes):
            return True

        # 维度2：新增边
        before_edges = before_state.get("edges", [])
        after_edges = after_state.get("edges", [])
        if len(after_edges) > len(before_edges):
            return True

        # 维度3：开放目标减少
        before_open = before_state.get("open_obligations", 0)
        after_open = after_state.get("open_obligations", 0)
        if isinstance(before_open, (list, int)) and isinstance(after_open, (list, int)):
            before_count = len(before_open) if isinstance(before_open, list) else before_open
            after_count = len(after_open) if isinstance(after_open, list) else after_open
            if after_count < before_count:
                return True

        # 维度4：义务状态变化
        before_status = before_state.get("obligation_status")
        after_status = after_state.get("obligation_status")
        if before_status is not None and after_status is not None:
            if before_status != after_status:
                return True

        return False

    def detect(
        self,
        text: str,
        tool_calls: List[Dict],
        before_state: Dict,
        after_state: Dict,
    ) -> Dict[str, Any]:
        """
        P6-6.4：三元判定gaming行为。

        三元AND逻辑（F12防线：不简化为只检查停滞词）：
        gaming = (停滞词=True) AND (工具证据=False) AND (结构进展=False)

        R-4防线：Agent可能迎合触发器自报停滞——三元判定过滤迎合性停滞。
        当Agent自报停滞但有工具证据或结构进展时，不判定gaming（真在尝试/推进）。

        边界情况：
        - 无gaming行为 → 停滞词False或工具证据True或结构进展True → not gaming
        - gaming行为隐蔽 → 停滞词True+无工具证据+无结构进展 → gaming
        - 自报停滞+有工具证据 → not gaming（真在尝试）
        - 自报停滞+有结构进展 → not gaming（真在推进）

        限制奖励性帮助：
        - 检测到gaming时，limit_reward_help=True
        - 未检测到gaming时，limit_reward_help=False

        Args:
            text: Agent输出文本
            tool_calls: 工具调用记录列表
            before_state: 前状态T图快照
            after_state: 后状态T图快照

        Returns:
            判定结果字典，含三元各值、gaming判定、limit_reward_help标志
        """
        stall_words_detected = self.detect_stall_words(text)
        tool_evidence = self.verify_tool_evidence(tool_calls)
        structural_progress = self.measure_structural_progress(before_state, after_state)

        # 三元AND逻辑（F12防线）
        is_gaming = (
            stall_words_detected
            and not tool_evidence
            and not structural_progress
        )

        return {
            "is_gaming": is_gaming,
            "stall_words_detected": stall_words_detected,
            "tool_evidence": tool_evidence,
            "structural_progress": structural_progress,
            "limit_reward_help": is_gaming,  # R-4防线：限制奖励性帮助
            "r4_defense": True,   # 三元判定过滤迎合性停滞
            "f12_defense": True,  # 完整三元AND逻辑
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "detail": {
                "stall_words_used": self.stall_words,
                "reason": self._gaming_reason(
                    stall_words_detected, tool_evidence, structural_progress, is_gaming
                ),
            },
        }

    def _gaming_reason(
        self,
        stall: bool,
        tool: bool,
        progress: bool,
        is_gaming: bool,
    ) -> str:
        """生成gaming判定原因说明"""
        if is_gaming:
            return (
                "gaming判定：自报停滞(停滞词=True)且无工具证据(工具证据=False)"
                "且无结构进展(结构进展=False)——Agent可能在迎合触发器(R-4防线)"
            )
        if not stall:
            return "非gaming：未检测到停滞词"
        if tool:
            return "非gaming：自报停滞但有工具证据——Agent真在尝试"
        if progress:
            return "非gaming：自报停滞但有结构进展——Agent真在推进"
        return "非gaming"

    def verify_p6_6_compliance(self) -> Dict[str, Any]:
        """
        P6-6.COMP：完整合规性验证。

        验证项：
        - P6-6.COMP：三元判定机制完整（停滞词+工具证据+结构进展）
        - P6-6.COMP2：F12防线——完整三元AND逻辑，不简化为只检查停滞词
        - P6-6.COMP3：R-4防线——能过滤迎合性停滞
        - P6-6.COMP4：154号修正——工具证据要求实际输出，结构进展要求T图变化
        - P6-6.COMP5：限制奖励性帮助——gaming时limit_reward_help=True

        边界情况：
        - 停滞词列表为空 → 告警
        - 三元逻辑被简化 → 拒绝
        - 工具证据只检查声称 → 拒绝
        - 结构进展只检查长度 → 拒绝

        Returns:
            合规验证结果字典
        """
        warnings: List[str] = []

        # 检查停滞词列表
        has_stall_words = len(self.stall_words) > 0
        if not has_stall_words:
            warnings.append("停滞词列表为空——无法检测自报停滞")

        # 验证三元判定方法存在
        has_detect_stall = hasattr(self, "detect_stall_words")
        has_verify_tool = hasattr(self, "verify_tool_evidence")
        has_measure_progress = hasattr(self, "measure_structural_progress")
        has_detect = hasattr(self, "detect")

        ternary_complete = (
            has_detect_stall and has_verify_tool and has_measure_progress and has_detect
        )

        # F12防线验证：三元AND逻辑完整（通过detect方法实现）
        # 用测试用例验证逻辑不被简化
        f12_test = self._verify_f12_logic()
        f12_defense = f12_test["f12_defense"]

        # R-4防线验证：能过滤迎合性停滞
        r4_test = self._verify_r4_defense()
        r4_defense = r4_test["r4_defense"]

        # 154号修正验证：工具证据要求实际输出，结构进展要求T图变化
        correction_154_test = self._verify_154_correction()
        correction_154_ok = correction_154_test["correction_154_ok"]

        if not f12_defense:
            warnings.append("F12防线：三元AND逻辑可能被简化")
        if not r4_defense:
            warnings.append("R-4防线：可能无法过滤迎合性停滞")
        if not correction_154_ok:
            warnings.append("154号修正：工具证据或结构进展验证可能不充分")

        compliant = (
            ternary_complete
            and f12_defense
            and r4_defense
            and correction_154_ok
            and has_stall_words
        )

        return {
            "compliant": compliant,
            "ternary_complete": ternary_complete,
            "has_stall_words": has_stall_words,
            "f12_defense": f12_defense,
            "r4_defense": r4_defense,
            "correction_154_ok": correction_154_ok,
            "limit_reward_help_implemented": True,
            "warnings": warnings,
            "methods": {
                "detect_stall_words": has_detect_stall,
                "verify_tool_evidence": has_verify_tool,
                "measure_structural_progress": has_measure_progress,
                "detect": has_detect,
            },
            "f12_test": f12_test,
            "r4_test": r4_test,
            "correction_154_test": correction_154_test,
        }

    def _verify_f12_logic(self) -> Dict[str, Any]:
        """
        F12防线验证：三元AND逻辑不被简化为只检查停滞词。

        测试用例：
        - 停滞词True + 工具证据True + 结构进展False → not gaming（有工具证据不算gaming）
        - 停滞词True + 工具证据False + 结构进展True → not gaming（有结构进展不算gaming）
        - 停滞词True + 工具证据False + 结构进展False → gaming（三元AND满足）
        - 停滞词False + 工具证据False + 结构进展False → not gaming（无停滞词不算gaming）
        """
        # 用例1：有工具证据不算gaming
        case1 = self.detect(
            text="我不知道怎么做",
            tool_calls=[{"tool": "calculator", "output": "42"}],
            before_state={},
            after_state={},
        )

        # 用例2：有结构进展不算gaming
        case2 = self.detect(
            text="卡住了",
            tool_calls=[],
            before_state={"nodes": ["a"], "edges": [], "open_obligations": 1},
            after_state={"nodes": ["a", "b"], "edges": [], "open_obligations": 1},
        )

        # 用例3：三元AND满足 → gaming
        case3 = self.detect(
            text="无法继续",
            tool_calls=[],
            before_state={"nodes": ["a"], "edges": [], "open_obligations": 1},
            after_state={"nodes": ["a"], "edges": [], "open_obligations": 1},
        )

        # 用例4：无停滞词不算gaming
        case4 = self.detect(
            text="正在分析中",
            tool_calls=[],
            before_state={},
            after_state={},
        )

        f12_ok = (
            not case1["is_gaming"]   # 有工具证据 → not gaming
            and not case2["is_gaming"]  # 有结构进展 → not gaming
            and case3["is_gaming"]    # 三元AND → gaming
            and not case4["is_gaming"]  # 无停滞词 → not gaming
        )

        return {
            "f12_defense": f12_ok,
            "case1_tool_evidence_not_gaming": not case1["is_gaming"],
            "case2_progress_not_gaming": not case2["is_gaming"],
            "case3_ternary_and_gaming": case3["is_gaming"],
            "case4_no_stall_not_gaming": not case4["is_gaming"],
        }

    def _verify_r4_defense(self) -> Dict[str, Any]:
        """
        R-4防线验证：能过滤迎合性停滞。

        Agent迎合触发器时会自报停滞，但如果同时有工具证据或结构进展，
        说明Agent真在尝试/推进，不应判定为gaming。

        测试用例：
        - 自报停滞+有工具证据 → not gaming（Agent真在尝试，不是迎合）
        - 自报停滞+有结构进展 → not gaming（Agent真在推进，不是迎合）
        - 自报停滞+无工具证据+无结构进展 → gaming（可能是迎合触发器）
        """
        # 自报停滞+有工具证据 → not gaming
        case_tool = self.detect(
            text="我不知道",
            tool_calls=[{"tool": "search", "output": "result"}],
            before_state={},
            after_state={},
        )

        # 自报停滞+有结构进展 → not gaming
        case_progress = self.detect(
            text="我不知道",
            tool_calls=[],
            before_state={"nodes": [], "edges": [], "open_obligations": 2},
            after_state={"nodes": [], "edges": [], "open_obligations": 1},
        )

        # 自报停滞+无工具证据+无结构进展 → gaming
        case_gaming = self.detect(
            text="我不知道",
            tool_calls=[],
            before_state={"nodes": [], "edges": [], "open_obligations": 2},
            after_state={"nodes": [], "edges": [], "open_obligations": 2},
        )

        r4_ok = (
            not case_tool["is_gaming"]
            and not case_progress["is_gaming"]
            and case_gaming["is_gaming"]
            and case_gaming["limit_reward_help"]  # gaming时限制奖励性帮助
        )

        return {
            "r4_defense": r4_ok,
            "stall_with_tool_not_gaming": not case_tool["is_gaming"],
            "stall_with_progress_not_gaming": not case_progress["is_gaming"],
            "stall_without_evidence_is_gaming": case_gaming["is_gaming"],
            "limit_reward_help_on_gaming": case_gaming["limit_reward_help"],
        }

    def _verify_154_correction(self) -> Dict[str, Any]:
        """
        154号修正验证：工具证据要求实际输出，结构进展要求T图变化。

        测试用例：
        - 工具调用只有声称无输出 → 工具证据=False
        - 工具调用有实际输出 → 工具证据=True
        - 只有输出长度变化无结构变化 → 结构进展=False
        - 有新增节点 → 结构进展=True
        """
        # 工具调用只有声称无输出 → False
        tool_claim_only = self.verify_tool_evidence(
            [{"tool": "search"}]  # 无output/result
        )

        # 工具调用有实际输出 → True
        tool_with_output = self.verify_tool_evidence(
            [{"tool": "search", "output": "found something"}]
        )

        # 只有输出长度变化无结构变化 → False
        # （before和after的nodes/edges/open_obligations相同）
        progress_length_only = self.measure_structural_progress(
            {"nodes": ["a"], "edges": [], "open_obligations": 1},
            {"nodes": ["a"], "edges": [], "open_obligations": 1},
        )

        # 有新增节点 → True
        progress_new_node = self.measure_structural_progress(
            {"nodes": ["a"], "edges": [], "open_obligations": 1},
            {"nodes": ["a", "b"], "edges": [], "open_obligations": 1},
        )

        correction_ok = (
            not tool_claim_only       # 声称不算
            and tool_with_output      # 有实际输出才算
            and not progress_length_only  # 长度变化不算
            and progress_new_node     # 结构变化才算
        )

        return {
            "correction_154_ok": correction_ok,
            "tool_claim_only_rejected": not tool_claim_only,
            "tool_with_output_accepted": tool_with_output,
            "length_only_rejected": not progress_length_only,
            "structural_change_accepted": progress_new_node,
        }
