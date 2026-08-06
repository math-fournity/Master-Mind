"""186号 · 预算审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

# 5种预算类型
BUDGET_TYPES = ("token", "compute", "tool", "branch", "hint")


class BudgetAuditor(StandardAuditor):
    standard_id = "186"
    standard_name = "预算审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        glr = data.guided_loop_result

        # --- 2.1 预算覆盖完整性 ---
        # 从guided_loop_result检查预算信息
        total_tokens = glr.get("total_tokens", {})
        has_token_budget = bool(total_tokens and total_tokens.get("total_prompt_tokens", 0) > 0)
        results.append(CheckResult(
            item_id="186-2.1-1",
            name="token预算记录",
            verdict="通过" if has_token_budget else "有缺陷",
            detail=f"total_tokens={total_tokens}" if has_token_budget else "无token预算记录",
            evidence={"total_tokens": total_tokens},
        ))

        # --- 2.2 Hint预算防线 ---
        n_hints = glr.get("n_hints", 0)
        max_hints = 3  # budget.py中hint.total=3
        results.append(CheckResult(
            item_id="186-2.2-1",
            name="Hint预算不超限",
            verdict="通过" if n_hints <= max_hints else "失败",
            detail=f"n_hints={n_hints}, max_hints={max_hints}",
            evidence={"n_hints": n_hints, "max_hints": max_hints},
        ))

        # --- 2.3 预算超限处理 ---
        completion_reason = glr.get("completion_reason", "")
        if completion_reason == "budget_exhausted":
            results.append(CheckResult(
                item_id="186-2.3-1",
                name="预算超限触发停止",
                verdict="通过",
                detail="completion_reason=budget_exhausted，正确触发停止",
                evidence={"completion_reason": completion_reason},
            ))
        else:
            results.append(CheckResult(
                item_id="186-2.3-1",
                name="预算超限触发停止",
                verdict="N/A",
                detail=f"completion_reason={completion_reason}，非预算超限",
                evidence={"completion_reason": completion_reason},
            ))

        # --- 2.4 预算分配合理性 ---
        n_turns = glr.get("n_turns", 0)
        max_turns = 5
        results.append(CheckResult(
            item_id="186-2.4-1",
            name="turn预算不超限",
            verdict="通过" if n_turns <= max_turns else "失败",
            detail=f"n_turns={n_turns}, max_turns={max_turns}",
            evidence={"n_turns": n_turns, "max_turns": max_turns},
        ))

        return results
