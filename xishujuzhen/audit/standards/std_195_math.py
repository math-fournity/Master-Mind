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

# 完成信号——证明类
PROOF_COMPLETION_SIGNALS = ["证毕", "QED", "结论是", "综上所述", "证明完毕", "得证", "证完", "定理得证", "原命题得证", "■", "□"]
# 完成信号——发现新方向类
DISCOVERY_COMPLETION_SIGNALS = ["适用边界", "结构类比", "类似之处", "共同骨架", "统一视角", "结构同构"]
# 完成信号——反驳类
REFUTE_COMPLETION_SIGNALS = ["反例", "猜想错误", "不成立", "命题错误", "矛盾"]


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

        # 2. 数学内容存在性——区分超时和空回复
        has_math = any(re.search(p, final_response) for p in MATH_PATTERNS)
        is_timeout = final_response.strip().startswith("[TIMEOUT]")
        is_too_short = len(final_response.strip()) < 50
        if not has_math:
            if is_timeout:
                math_verdict = "有缺陷"  # 超时不是Solver的错
                math_detail = "response为[TIMEOUT]——超时导致无数学内容（非Solver责任）"
            elif is_too_short:
                math_verdict = "有缺陷"
                math_detail = f"response过短（{len(final_response.strip())}字符），无数学内容"
            else:
                math_verdict = "失败"
                math_detail = "response中无数学内容"
        else:
            math_verdict = "通过"
            math_detail = "response中有数学内容"
        results.append(CheckResult(
            item_id="195-证明-1",
            name="数学内容存在性",
            verdict=math_verdict,
            detail=math_detail,
            evidence={"has_math": has_math, "is_timeout": is_timeout, "is_too_short": is_too_short},
        ))

        # 3. 完成信号存在性——按任务子类型选择信号列表
        problem = glr.get("problem", "")
        is_refute = any(kw in problem for kw in ["是否正确", "反例", "错误", "成立吗"])
        is_discovery = any(kw in problem for kw in ["类比", "视角", "解释", "结构上"])
        if is_refute:
            signals = REFUTE_COMPLETION_SIGNALS + PROOF_COMPLETION_SIGNALS
            task_type = "反驳类"
        elif is_discovery:
            signals = DISCOVERY_COMPLETION_SIGNALS + PROOF_COMPLETION_SIGNALS
            task_type = "发现新方向类"
        else:
            signals = PROOF_COMPLETION_SIGNALS
            task_type = "证明类"
        has_signal = any(sig in final_response for sig in signals)
        results.append(CheckResult(
            item_id="195-证明-2",
            name="完成信号存在性",
            verdict="有缺陷" if not has_signal else "通过",
            detail=f"({task_type}) response中{'有' if has_signal else '无'}完成信号",
            evidence={"has_signal": has_signal, "task_type": task_type},
        ))

        # 4. 边界情况检查——按任务子类型区分
        if is_refute:
            # 反驳类：只需找到反例，不需要检查所有边界
            has_counterexample = any(kw in final_response for kw in ["反例", "取n=", "令n=", "当n="])
            results.append(CheckResult(
                item_id="195-证明-3",
                name="边界情况检查",
                verdict="通过" if has_counterexample else "有缺陷",
                detail=f"(反驳类) {'提供了' if has_counterexample else '未提供'}反例",
                evidence={"task_type": "反驳类", "has_counterexample": has_counterexample},
            ))
        elif is_discovery:
            # 发现新方向类：检查是否有具体例子和适用边界
            has_example = any(kw in final_response for kw in ["例子", "例如", "具体", "instance", "example"])
            has_boundary = any(kw in final_response for kw in ["边界", "局限", "不适用", "适用范围"])
            results.append(CheckResult(
                item_id="195-证明-3",
                name="边界情况检查",
                verdict="通过" if (has_example and has_boundary) else "有缺陷",
                detail=f"(发现新方向类) 例子={'有' if has_example else '无'}, 适用边界={'有' if has_boundary else '无'}",
                evidence={"task_type": "发现新方向类", "has_example": has_example, "has_boundary": has_boundary},
            ))
        else:
            # 证明类：检查基础情形
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
                detail=f"(证明类) {'提到' if has_base_case else '未提到'}基础情形(n=1)",
                evidence={"task_type": "证明类", "has_base_case": has_base_case},
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
