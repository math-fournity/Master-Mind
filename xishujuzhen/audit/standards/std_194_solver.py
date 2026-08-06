"""194号 · Solver连接审计标准。"""

from __future__ import annotations

import os
from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

# 工作系统劫持关键词
HIJACK_KEYWORDS = ["加载认知种子", "CP1-CP3", "CP1", "七步骤", "种子推荐表", "工作系统"]

# 正确工作目录前缀
SOLVER_WORKDIR_PREFIX = "/data/math-agent-glm5.2-"


class SolverConnectionAuditor(StandardAuditor):
    standard_id = "194"
    standard_name = "Solver连接审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        glr = data.guided_loop_result
        results: List[CheckResult] = []

        # --- 2.1 连接稳定性 ---

        # 1. devin cli调用成功
        final_response = glr.get("final_response", "")
        has_error = final_response.startswith("[ERROR")
        results.append(CheckResult(
            item_id="194-2.1-1",
            name="devin cli调用成功",
            verdict="失败" if has_error else "通过",
            detail=f"response{'以[ERROR开头' if has_error else '正常'}",
            evidence={"has_error": has_error, "response_prefix": final_response[:80]},
        ))

        # 2. session_id获取
        session_id = glr.get("session_id", "")
        results.append(CheckResult(
            item_id="194-2.1-2",
            name="session_id获取",
            verdict="通过" if session_id else "失败",
            detail=f"session_id='{session_id}'",
            evidence={"session_id": session_id},
        ))

        # 3. export文件生成
        conversations = data.conversations
        has_export = len(conversations) > 0 and all(
            os.path.getsize(os.path.join(data.run_dir, f"turn_{i+1}_conversation.json")) > 0
            for i in range(len(conversations))
            if os.path.exists(os.path.join(data.run_dir, f"turn_{i+1}_conversation.json"))
        )
        results.append(CheckResult(
            item_id="194-2.1-3",
            name="export文件生成",
            verdict="通过" if has_export else "失败",
            detail=f"找到{len(conversations)}个conversation文件",
            evidence={"conversation_count": len(conversations)},
        ))

        # 4. 工作目录正确
        session_info = data.session_info
        if session_info:
            work_dir = session_info.get("working_directory", "")
            is_correct = work_dir.startswith(SOLVER_WORKDIR_PREFIX)
            results.append(CheckResult(
                item_id="194-2.1-4",
                name="工作目录正确",
                verdict="通过" if is_correct else "失败",
                detail=f"working_directory='{work_dir}'",
                evidence={"working_directory": work_dir},
            ))
        else:
            results.append(CheckResult(
                item_id="194-2.1-4",
                name="工作目录正确",
                verdict="有缺陷",
                detail="session_info为空，无法检查工作目录",
                evidence={},
            ))

        # --- 2.3 Solver行为约束 ---

        # 5. 无web_search
        tool_calls = data.tool_call_states
        has_web_search = any(
            "web_search" in str(tc).lower() or "search" in str(tc.get("kind", "")).lower()
            for tc in tool_calls
        )
        results.append(CheckResult(
            item_id="194-2.3-1",
            name="无web_search",
            verdict="失败" if has_web_search else "通过",
            detail=f"tool_call_state中{'有' if has_web_search else '无'}web_search",
            evidence={"tool_call_count": len(tool_calls), "has_web_search": has_web_search},
        ))

        # 6. 无工作系统劫持
        has_hijack = any(kw in final_response for kw in HIJACK_KEYWORDS)
        results.append(CheckResult(
            item_id="194-2.3-2",
            name="无工作系统劫持",
            verdict="失败" if has_hijack else "通过",
            detail=f"response中{'包含' if has_hijack else '不包含'}工作系统关键词",
            evidence={"has_hijack": has_hijack},
        ))

        return results
