"""195号 · 数学正确性验证标准（可自动化部分）。"""

from __future__ import annotations

import re
from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

# web_search检测
def _has_web_search(data: AuditData) -> bool:
    return any(
        "web_search" in str(tc).lower() or "search" in str(tc.get("kind", "")).lower()
        for tc in data.tool_call_states
    )

# 数学内容检测——response中是否有数学公式或推理
MATH_PATTERNS = [
    r"\$",  # LaTeX公式
    r"\\sum", r"\\frac", r"\\prod",  # LaTeX命令
    r"\b证明\b", r"\b定理\b", r"\b引理\b",  # 数学中文关键词
    r"\bproof\b", r"\btheorem\b", r"\blemma\b",  # 数学英文关键词
    r"\b归纳\b", r"\b推导\b", r"\b因为\b", r"\b所以\b",  # 推理关键词
]

# 完成信号
COMPLETION_SIGNALS = ["证毕", "QED", "结论是", "综上所述", "证明完毕", "得证"]


class MathCorrectnessAuditor(StandardAuditor):
    standard_id = "195"
    standard_name = "数学正确性验证"

    def audit(self, data: AuditData) -> List[CheckResult]:
        glr = data.guided_loop_result
        final_response = glr.get("final_response", "")
        results: List[CheckResult] = []

        # --- 二、通用检查项 ---

        # 1. 数据来源纯净性
        has_ws = _has_web_search(data)
        results.append(CheckResult(
            item_id="195-通用-1",
            name="数据来源纯净性",
            verdict="有缺陷" if has_ws else "通过",
            detail=f"{'使用了web_search——数据来源受污染' if has_ws else '未使用web_search'}",
            evidence={"has_web_search": has_ws},
        ))

        # --- 证明类检查（可自动化部分） ---

        # 2. 数学内容存在性
        has_math = any(re.search(p, final_response) for p in MATH_PATTERNS)
        results.append(CheckResult(
            item_id="195-证明-1",
            name="数学内容存在性",
            verdict="失败" if not has_math else "通过",
            detail=f"response中{'有' if has_math else '无'}数学内容",
            evidence={"has_math": has_math},
        ))

        # 3. 完成信号存在性
        has_signal = any(sig in final_response for sig in COMPLETION_SIGNALS)
        results.append(CheckResult(
            item_id="195-证明-2",
            name="完成信号存在性",
            verdict="有缺陷" if not has_signal else "通过",
            detail=f"response中{'有' if has_signal else '无'}完成信号",
            evidence={"has_signal": has_signal},
        ))

        # 4. 边界情况检查——是否提到n=1或基础情形
        has_base_case = bool(
            re.search(r"n\s*=\s*1\b", final_response)
            or "基础" in final_response
            or "归纳基础" in final_response
            or "n=1" in final_response
            or "n = 1" in final_response
        )
        results.append(CheckResult(
            item_id="195-证明-3",
            name="边界情况检查",
            verdict="有缺陷" if not has_base_case else "通过",
            detail=f"{'提到' if has_base_case else '未提到'}基础情形(n=1)",
            evidence={"has_base_case": has_base_case},
        ))

        # 5. 小情形验证（对猜想类任务）——自动用Python验证
        problem = glr.get("problem", "")
        is_conjecture = "猜想" in problem or "猜测" in problem or "下界" in problem or "上界" in problem
        if is_conjecture:
            # 尝试从response中提取数值并验证
            # 这里只做简单的存在性检查——完整的小情形验证需要AI辅助
            has_numerical = bool(re.search(r"\d+", final_response))
            results.append(CheckResult(
                item_id="195-猜想-1",
                name="小情形验证（猜想类）",
                verdict="有缺陷" if not has_numerical else "通过",
                detail=f"猜想类任务，response中{'有' if has_numerical else '无'}数值验证",
                evidence={"is_conjecture": True, "has_numerical": has_numerical},
            ))
        else:
            results.append(CheckResult(
                item_id="195-猜想-1",
                name="小情形验证（猜想类）",
                verdict="N/A",
                detail="非猜想类任务",
                evidence={"is_conjecture": False},
            ))

        # 6. 逻辑链完整性——需要AI辅助，脚本只做初步检查
        # 检查是否有明显的跳步标记
        skip_markers = ["显然", "易得", "易见", "trivially", "obviously", "clearly"]
        has_skip = any(marker in final_response for marker in skip_markers)
        results.append(CheckResult(
            item_id="195-证明-4",
            name="逻辑链完整性（初步检查）",
            verdict="有缺陷" if has_skip else "通过",
            detail=f"{'发现跳步标记: ' + str([m for m in skip_markers if m in final_response]) if has_skip else '未发现明显跳步标记'}（完整检查需AI辅助）",
            evidence={"has_skip_markers": has_skip, "note": "完整逻辑链检查需AI辅助"},
        ))

        return results
