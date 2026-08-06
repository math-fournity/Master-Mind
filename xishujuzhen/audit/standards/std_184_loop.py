"""184号 · 12步循环与引导循环审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

# 完成信号关键词
COMPLETION_SIGNALS = ["证毕", "QED", "结论是", "综上所述", "一句话总结", "证明完毕", "得证"]

# 工作系统劫持关键词
HIJACK_KEYWORDS = ["加载认知种子", "CP1-CP3", "CP1", "七步骤", "种子推荐表", "工作系统"]

# 数学卡点信号
STALL_SIGNALS = ["我不知道", "无法确定", "不确定", "不会", "难以", "卡住"]


class LoopAuditor(StandardAuditor):
    standard_id = "184"
    standard_name = "12步循环与引导循环审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        glr = data.guided_loop_result
        results: List[CheckResult] = []

        # --- 2.2 引导循环有效性 ---

        # 1. solo explore先于guided
        turn_history = glr.get("turn_history", [])
        if turn_history:
            first_is_hint = turn_history[0].get("is_hint", False)
            results.append(CheckResult(
                item_id="184-2.2-1",
                name="solo explore先于guided",
                verdict="通过" if not first_is_hint else "失败",
                detail=f"turn_history[0].is_hint={first_is_hint}",
                evidence={"first_turn_is_hint": first_is_hint},
            ))
        else:
            results.append(CheckResult(
                item_id="184-2.2-1", name="solo explore先于guided",
                verdict="N/A", detail="无turn_history", evidence={},
            ))

        # 2. hint只在卡点后给
        n_hints = glr.get("n_hints", 0)
        # solo阶段是turn 1，如果n_hints>0且n_turns==1则说明solo阶段给了hint
        n_turns = glr.get("n_turns", 0)
        solo_stage_hint = (n_hints > 0 and n_turns == 1 and glr.get("completion_reason") != "completed_after_hint")
        results.append(CheckResult(
            item_id="184-2.2-2",
            name="hint只在卡点后给",
            verdict="失败" if solo_stage_hint else "通过",
            detail=f"n_hints={n_hints}, n_turns={n_turns}",
            evidence={"n_hints": n_hints, "n_turns": n_turns, "solo_stage_hint": solo_stage_hint},
        ))

        # 3. hint数量不超过预算
        max_hints = 3  # 默认值
        results.append(CheckResult(
            item_id="184-2.2-3",
            name="hint数量不超过预算",
            verdict="通过" if n_hints <= max_hints else "失败",
            detail=f"n_hints={n_hints}, max_hints={max_hints}",
            evidence={"n_hints": n_hints, "max_hints": max_hints},
        ))

        # 4. turn数量不超过预算
        max_turns = 5  # 默认值
        results.append(CheckResult(
            item_id="184-2.2-4",
            name="turn数量不超过预算",
            verdict="通过" if n_turns <= max_turns else "失败",
            detail=f"n_turns={n_turns}, max_turns={max_turns}",
            evidence={"n_turns": n_turns, "max_turns": max_turns},
        ))

        # 5. 完成判定合理
        completed = glr.get("completed", False)
        final_response = glr.get("final_response", "")
        has_completion_signal = any(sig in final_response for sig in COMPLETION_SIGNALS)
        has_error = final_response.startswith("[ERROR")
        reason = glr.get("completion_reason", "")

        if completed:
            if has_error:
                verdict5 = "有缺陷"
                detail5 = f"completed=True但response以[ERROR开头: {final_response[:100]}"
            elif not has_completion_signal and reason != "no_stall_no_completion_stop":
                verdict5 = "有缺陷"
                detail5 = f"completed=True但response无完成信号: {final_response[:100]}"
            elif reason == "no_stall_no_completion_stop" and not has_completion_signal:
                verdict5 = "失败"
                detail5 = f"completed=True但reason=no_stall_no_completion_stop且无完成信号"
            else:
                verdict5 = "通过"
                detail5 = f"completed=True, 有完成信号, reason={reason}"
        else:
            verdict5 = "通过"
            detail5 = "completed=False"

        results.append(CheckResult(
            item_id="184-2.2-5",
            name="完成判定合理",
            verdict=verdict5,
            detail=detail5,
            evidence={"completed": completed, "has_completion_signal": has_completion_signal,
                      "has_error": has_error, "reason": reason},
        ))

        # 6. 卡点检测准确
        has_hijack = any(kw in final_response for kw in HIJACK_KEYWORDS)
        has_stall = any(sig in final_response for sig in STALL_SIGNALS)
        stall_detected = any(t.get("stall_detected", False) for t in turn_history)

        if has_hijack:
            verdict6 = "失败"
            detail6 = "response包含工作系统关键词，应标记为'非数学卡点'"
        elif stall_detected and not has_stall and n_turns > 1:
            verdict6 = "有缺陷"
            detail6 = "stall_detected=True但response无数学卡点信号"
        elif not stall_detected and n_hints > 0:
            verdict6 = "有缺陷"
            detail6 = "给了hint但未检测到卡点"
        else:
            verdict6 = "通过"
            detail6 = f"stall_detected={stall_detected}, has_stall_signal={has_stall}"

        results.append(CheckResult(
            item_id="184-2.2-6",
            name="卡点检测准确",
            verdict=verdict6,
            detail=detail6,
            evidence={"stall_detected": stall_detected, "has_stall": has_stall, "has_hijack": has_hijack},
        ))

        # 7. hint内容相关
        if n_hints == 0:
            verdict7 = "N/A"
            detail7 = "没有给hint"
        else:
            # 检查hint的stall_reason是否与response卡点信号一致
            hint_turns = [t for t in turn_history if t.get("is_hint", False)]
            if hint_turns:
                hint_reason = hint_turns[0].get("stall_reason", "")
                if has_hijack:
                    verdict7 = "失败"
                    detail7 = f"hint内容与工作系统有关而非数学卡点: {hint_reason}"
                elif has_stall:
                    verdict7 = "通过"
                    detail7 = f"hint_reason={hint_reason}, response有卡点信号"
                else:
                    verdict7 = "有缺陷"
                    detail7 = f"hint_reason={hint_reason}, 但response无卡点信号"
            else:
                verdict7 = "有缺陷"
                detail7 = "n_hints>0但turn_history中无hint turn"

        results.append(CheckResult(
            item_id="184-2.2-7",
            name="hint内容相关",
            verdict=verdict7,
            detail=detail7,
            evidence={"n_hints": n_hints},
        ))

        return results
