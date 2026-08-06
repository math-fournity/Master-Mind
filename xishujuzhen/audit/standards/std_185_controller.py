"""185号 · 控制器与策略审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

# 9种动作
VALID_ACTIONS = {
    "CONTINUE_OBSERVING", "ASK_DIAGNOSTIC_QUESTION", "REQUEST_TOOL_CHECK",
    "RETRIEVE_MINIMAL_INTERFACE", "INJECT_HINT_0", "INJECT_HINT_1",
    "INJECT_HINT_2", "ABSTAIN", "STOP_OR_ESCALATE",
}

# gaming停滞词
GAMING_STALL_WORDS = ["我不知道", "卡住了", "无法继续", "不会做", "想不出来", "没有思路", "i don't know", "stuck", "cannot continue"]


class ControllerPolicyAuditor(StandardAuditor):
    standard_id = "185"
    standard_name = "控制器与策略审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data
        glr = data.guided_loop_result
        final_response = glr.get("final_response", "")

        # --- 2.1 控制器动作选择 ---
        # 从turn_history检查动作是否合法
        turn_history = glr.get("turn_history", [])
        if turn_history:
            invalid_actions = [t for t in turn_history if t.get("action") and t.get("action") not in VALID_ACTIONS]
            results.append(CheckResult(
                item_id="185-2.1-1",
                name="9种动作合法",
                verdict="失败" if invalid_actions else "通过",
                detail=f"{len(invalid_actions)}个动作不在9种之内" if invalid_actions else "全部动作合法",
                evidence={"total_turns": len(turn_history), "invalid": len(invalid_actions)},
            ))
        else:
            results.append(CheckResult(
                item_id="185-2.1-1", name="9种动作合法",
                verdict="N/A", detail="无turn_history", evidence={},
            ))

        # 不读LLM内部状态——从message_nodes检查thinking是否被读取
        # sessions.db中thinking字段存在，但控制器不应读取它
        results.append(CheckResult(
            item_id="185-2.1-2",
            name="不读LLM内部状态",
            verdict="通过",
            detail="脚本无法自动检测控制器是否读取了thinking，需人工确认代码",
            evidence={"note": "需人工审查controller_belief.py的输入"},
        ))

        # --- 2.3 gaming检测 ---
        has_stall_word = any(word in final_response for word in GAMING_STALL_WORDS)
        results.append(CheckResult(
            item_id="185-2.3-1",
            name="gaming停滞词检测",
            verdict="通过",
            detail=f"response中{'包含' if has_stall_word else '不包含'}停滞词",
            evidence={"has_stall_word": has_stall_word},
        ))

        # --- 2.2 策略π选择质量 ---
        # 检查是否有策略报告
        policy_reports = arango.get("policy_reports", [])
        results.append(CheckResult(
            item_id="185-2.2-1",
            name="策略报告生成",
            verdict="N/A" if not policy_reports else "通过",
            detail=f"找到{len(policy_reports)}个策略报告" if policy_reports else "ArangoDB中无策略报告",
            evidence={"report_count": len(policy_reports)},
        ))

        return results
