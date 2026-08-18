#!/usr/bin/env python3
"""
POC方案文档与执行记录差异审计脚本
================================

对照POC方案文档和执行记录（进度报告），自动检查常见差异类型：
1. 方案文档中的命令是否违反全局规则（nohup vs tmux）
2. 方案文档声明的默认method是否与代码默认值一致
3. 方案文档的规模估算是否与实际method匹配
4. 执行记录是否包含环境检查记录
5. 执行记录是否包含监控纪律记录
6. 执行记录是否包含git commit记录
7. 执行记录是否对照通过标准做判定
8. 执行记录是否引用修正后的流程

用法：
    python3 audit_poc_doc_vs_execution.py --plan <方案文档> --report <执行记录> [--code <代码文件>]

    # 完整审计（方案文档+执行记录+代码）
    python3 audit_poc_doc_vs_execution.py \
        --plan "Tell分类学研究过程文档/415-v0-2026-08-18-POC-2.7-截断vs思维错误.md" \
        --report "POC-2.7/POC-2.7-001-完整进度报告.md" \
        --code "Tell分类学研究过程文档/poc_assets/poc_2.7/batch_continue_948.py"

    # 只审计方案文档
    python3 audit_poc_doc_vs_execution.py --plan <方案文档>

    # 只审计执行记录
    python3 audit_poc_doc_vs_execution.py --report <执行记录>

输出：
    - 终端：检查结果汇总（PASS/WARN/FAIL + 行号定位）
    - JSON：结构化结果（可选 --json <输出路径>）
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


# =============================================================================
# 检查结果数据结构
# =============================================================================

@dataclass
class CheckResult:
    """单项检查结果。"""
    check_id: str           # 检查项ID（如 "PLAN-001"）
    check_name: str         # 检查项名称
    status: str             # PASS / WARN / FAIL / SKIP
    detail: str             # 详细说明
    location: str = ""      # 行号定位（如 "方案文档:338" 或 "执行记录:§11"）
    suggestion: str = ""    # 修正建议


@dataclass
class AuditReport:
    """完整审计报告。"""
    plan_file: str = ""
    report_file: str = ""
    code_file: str = ""
    results: list = field(default_factory=list)

    def summary(self) -> str:
        """生成汇总文本。"""
        counts = {"PASS": 0, "WARN": 0, "FAIL": 0, "SKIP": 0}
        for r in self.results:
            counts[r.status] = counts.get(r.status, 0) + 1
        total = len(self.results)
        lines = [
            f"\n{'='*70}",
            f"POC方案文档与执行记录差异审计报告",
            f"{'='*70}",
            f"方案文档: {self.plan_file or '(未提供)'}",
            f"执行记录: {self.report_file or '(未提供)'}",
            f"代码文件: {self.code_file or '(未提供)'}",
            f"",
            f"汇总: PASS={counts['PASS']}  WARN={counts['WARN']}  "
            f"FAIL={counts['FAIL']}  SKIP={counts['SKIP']}  总计={total}",
            f"{'='*70}",
            f"",
        ]
        for r in self.results:
            icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌", "SKIP": "⏭️ "}[r.status]
            lines.append(f"{icon} [{r.check_id}] {r.check_name}")
            lines.append(f"   状态: {r.status}")
            if r.location:
                lines.append(f"   定位: {r.location}")
            lines.append(f"   详情: {r.detail}")
            if r.suggestion:
                lines.append(f"   建议: {r.suggestion}")
            lines.append("")
        return "\n".join(lines)

    def to_json(self) -> str:
        """生成JSON。"""
        return json.dumps({
            "plan_file": self.plan_file,
            "report_file": self.report_file,
            "code_file": self.code_file,
            "results": [asdict(r) for r in self.results],
        }, ensure_ascii=False, indent=2)


# =============================================================================
# 工具函数
# =============================================================================

def read_file(path: str) -> tuple[str, list[str]]:
    """读取文件，返回(全文, 按行列表)。"""
    p = Path(path)
    if not p.exists():
        print(f"[ERROR] 文件不存在: {path}", file=sys.stderr)
        sys.exit(1)
    text = p.read_text()
    lines = text.splitlines()
    return text, lines


def find_line_with_pattern(lines: list[str], pattern: str,
                            flags: int = 0) -> Optional[int]:
    """找到第一个匹配pattern的行号（1-based），找不到返回None。"""
    regex = re.compile(pattern, flags)
    for i, line in enumerate(lines):
        if regex.search(line):
            return i + 1
    return None


def find_all_lines_with_pattern(lines: list[str], pattern: str,
                                 flags: int = 0) -> list[int]:
    """找到所有匹配pattern的行号（1-based）。"""
    regex = re.compile(pattern, flags)
    return [i + 1 for i, line in enumerate(lines) if regex.search(line)]


# =============================================================================
# 方案文档检查（PLAN-xxx）
# =============================================================================

def check_plan_nohup_vs_tmux(lines: list[str]) -> CheckResult:
    """PLAN-001: 方案文档中是否用了nohup（违反全局AGENTS.md§12 tmux优先铁律）。"""
    nohup_lines = find_all_lines_with_pattern(lines, r"\bnohup\b")
    tmux_lines = find_all_lines_with_pattern(lines, r"\btmux\s+(new-session|kill-session|has-session|list-sessions|capture-pane)\b")

    if nohup_lines:
        locs = ", ".join(f"行{l}" for l in nohup_lines)
        return CheckResult(
            check_id="PLAN-001",
            check_name="tmux优先铁律（禁止nohup）",
            status="FAIL",
            detail=f"方案文档中发现{len(nohup_lines)}处nohup用法",
            location=f"方案文档:{locs}",
            suggestion="把nohup ... &改为tmux new-session -d -s <name> \"...\"（全局AGENTS.md§12）",
        )
    elif tmux_lines:
        return CheckResult(
            check_id="PLAN-001",
            check_name="tmux优先铁律（禁止nohup）",
            status="PASS",
            detail=f"未发现nohup，发现{len(tmux_lines)}处tmux用法",
        )
    else:
        return CheckResult(
            check_id="PLAN-001",
            check_name="tmux优先铁律（禁止nohup）",
            status="SKIP",
            detail="方案文档中既无nohup也无tmux（可能不涉及长时间命令）",
        )


def check_plan_method_vs_code(plan_lines: list[str],
                               code_lines: Optional[list[str]] = None) -> CheckResult:
    """PLAN-002: 方案文档声明的默认method是否与代码默认值一致。"""
    # 从方案文档找method声明
    plan_v1_claim = find_line_with_pattern(plan_lines, r"本POC\s*(?:使用|默认使用)\s*v1方案")
    plan_v2_claim = find_line_with_pattern(plan_lines, r"本POC\s*(?:使用|默认使用)\s*v2方案")

    if not plan_v1_claim and not plan_v2_claim:
        return CheckResult(
            check_id="PLAN-002",
            check_name="方案method声明与代码默认值一致性",
            status="SKIP",
            detail="方案文档中未找到明确的method声明",
        )

    plan_method = "1" if plan_v1_claim else "2"
    plan_loc = plan_v1_claim or plan_v2_claim

    if code_lines is None:
        return CheckResult(
            check_id="PLAN-002",
            check_name="方案method声明与代码默认值一致性",
            status="WARN",
            detail=f"方案文档声明默认v{plan_method}，但未提供代码文件做对比",
            location=f"方案文档:行{plan_loc}",
            suggestion="提供--code参数以检查代码默认值是否一致",
        )

    # 从代码找default值
    code_default_line = find_line_with_pattern(code_lines, r'default\s*=\s*["\']v[12]["\']')
    if code_default_line is None:
        # 尝试找add_argument中的method
        code_default_line = find_line_with_pattern(code_lines, r'--method.*default.*v[12]')
    if code_default_line is None:
        return CheckResult(
            check_id="PLAN-002",
            check_name="方案method声明与代码默认值一致性",
            status="WARN",
            detail=f"方案文档声明默认v{plan_method}，但代码中未找到method默认值",
            location=f"方案文档:行{plan_loc}",
        )

    code_line_text = code_lines[code_default_line - 1]
    code_method_match = re.search(r'v([12])', code_line_text)
    code_method = code_method_match.group(1) if code_method_match else "?"

    if plan_method == code_method:
        return CheckResult(
            check_id="PLAN-002",
            check_name="方案method声明与代码默认值一致性",
            status="PASS",
            detail=f"方案文档声明默认v{plan_method}，代码默认值也是v{code_method}",
            location=f"方案文档:行{plan_loc} / 代码:行{code_default_line}",
        )
    else:
        return CheckResult(
            check_id="PLAN-002",
            check_name="方案method声明与代码默认值一致性",
            status="FAIL",
            detail=f"方案文档声明默认v{plan_method}，但代码默认值是v{code_method}——不一致",
            location=f"方案文档:行{plan_loc} / 代码:行{code_default_line}",
            suggestion=f"更新方案文档的method声明为v{code_method}，或修改代码默认值为v{plan_method}",
        )


def check_plan_scale_estimate_matches_method(plan_lines: list[str]) -> CheckResult:
    """PLAN-003: 方案文档的规模估算是否与声明的method匹配。"""
    plan_v2_claim = find_line_with_pattern(plan_lines, r"本POC\s*(使用|默认使用)\s*v2方案")
    # 找规模估算章节
    scale_section = find_line_with_pattern(plan_lines, r"规模估算|5\.6|§5\.6")

    if scale_section is None:
        return CheckResult(
            check_id="PLAN-003",
            check_name="规模估算与method匹配性",
            status="SKIP",
            detail="方案文档中未找到规模估算章节",
        )

    # 检查规模估算区域是否有v2的估算（2 pipe / 慢2倍等关键词）
    # 取规模估算后20行
    region = plan_lines[scale_section - 1: scale_section + 20]
    region_text = "\n".join(region)
    has_v2_estimate = bool(re.search(r"v2方案|2\s*pipe|慢.*2倍|2倍", region_text))
    has_v1_only = bool(re.search(r"v1方案估算", region_text)) and not has_v2_estimate

    if plan_v2_claim and not has_v2_estimate:
        return CheckResult(
            check_id="PLAN-003",
            check_name="规模估算与method匹配性",
            status="WARN",
            detail="方案文档声明默认v2，但规模估算章节未找到v2方案的估算",
            location=f"方案文档:行{scale_section}",
            suggestion="补充v2方案的规模估算（v2每轮2个pipe，比v1慢约2倍）",
        )
    elif plan_v2_claim and has_v2_estimate:
        return CheckResult(
            check_id="PLAN-003",
            check_name="规模估算与method匹配性",
            status="PASS",
            detail="方案文档声明默认v2，规模估算章节包含v2估算",
            location=f"方案文档:行{scale_section}",
        )
    else:
        return CheckResult(
            check_id="PLAN-003",
            check_name="规模估算与method匹配性",
            status="PASS",
            detail="方案文档声明v1，规模估算章节有v1估算",
            location=f"方案文档:行{scale_section}",
        )


# =============================================================================
# 执行记录检查（REPORT-xxx）
# =============================================================================

def check_report_env_check(lines: list[str]) -> CheckResult:
    """REPORT-001: 执行记录是否包含环境检查记录。"""
    # 找环境检查关键词
    env_patterns = [
        (r"docker\s+ps.*arangodb|docker\s+start\s+arangodb", "ArangoDB检查"),
        (r"/data/math-agent-glm5.2-tmux-agents-trajectory", "D盘检查"),
        (r"which\s+devin", "devin cli检查"),
    ]
    found = []
    missing = []
    for pattern, name in env_patterns:
        if find_line_with_pattern(lines, pattern):
            found.append(name)
        else:
            missing.append(name)

    # 找环境检查章节
    env_section = find_line_with_pattern(lines, r"环境检查|§11\.1|§9\.1")

    if len(found) == 3:
        return CheckResult(
            check_id="REPORT-001",
            check_name="环境检查记录",
            status="PASS",
            detail=f"包含全部3项环境检查: {', '.join(found)}",
            location=f"执行记录:§{env_section or '?'}",
        )
    elif len(found) > 0:
        return CheckResult(
            check_id="REPORT-001",
            check_name="环境检查记录",
            status="WARN",
            detail=f"包含{len(found)}/3项环境检查，缺失: {', '.join(missing)}",
            location=f"执行记录:§{env_section or '?'}",
            suggestion="补充缺失的环境检查记录",
        )
    else:
        return CheckResult(
            check_id="REPORT-001",
            check_name="环境检查记录",
            status="FAIL",
            detail="执行记录中未找到任何环境检查记录",
            suggestion="补充环境检查章节（ArangoDB/D盘/devin cli的检查命令和结果）",
        )


def check_report_monitoring(lines: list[str]) -> CheckResult:
    """REPORT-002: 执行记录是否包含监控纪律记录。"""
    monitor_patterns = [
        (r"tmux\s+list-sessions|tmux\s+capture-pane", "tmux session检查"),
        (r"results\.json.*增长|results\.json.*增长|进度.*检查", "results.json增长检查"),
        (r"proof\.md.*生成|proof\.md.*存在", "proof.md生成检查"),
        (r"log.*异常|log.*error|batch_full\.log", "log异常检查"),
    ]
    found_names = []
    for pattern, name in monitor_patterns:
        if find_line_with_pattern(lines, pattern, re.IGNORECASE):
            found_names.append(name)

    monitor_section = find_line_with_pattern(lines, r"监控纪律|§9\.7|§11\.2")

    if len(found_names) >= 3:
        return CheckResult(
            check_id="REPORT-002",
            check_name="监控纪律记录",
            status="PASS",
            detail=f"包含{len(found_names)}/4项监控检查: {', '.join(found_names)}",
            location=f"执行记录:§{monitor_section or '?'}",
        )
    elif len(found_names) > 0:
        return CheckResult(
            check_id="REPORT-002",
            check_name="监控纪律记录",
            status="WARN",
            detail=f"包含{len(found_names)}/4项监控检查",
            location=f"执行记录:§{monitor_section or '?'}",
            suggestion="补充缺失的监控检查记录",
        )
    else:
        return CheckResult(
            check_id="REPORT-002",
            check_name="监控纪律记录",
            status="FAIL",
            detail="执行记录中未找到监控纪律记录",
            suggestion="补充监控纪律章节（tmux session/results.json/proof.md/log的检查记录）",
        )


def check_report_git_commit(lines: list[str]) -> CheckResult:
    """REPORT-003: 执行记录是否包含git commit记录。"""
    has_commit_hash = bool(find_line_with_pattern(lines, r"\b[0-9a-f]{7,40}\b.*commit|commit.*\b[0-9a-f]{7,40}\b"))
    has_commit_section = bool(find_line_with_pattern(lines, r"git\s+commit|commit记录|§11\.3"))
    has_commit_list = bool(find_line_with_pattern(lines, r"\| *commit *\|"))
    has_git_log = bool(find_line_with_pattern(lines, r"git\s+log"))

    score = sum([has_commit_hash, has_commit_section, has_commit_list, has_git_log])

    if score >= 3:
        return CheckResult(
            check_id="REPORT-003",
            check_name="git commit记录",
            status="PASS",
            detail="执行记录包含git commit历史记录",
        )
    elif score >= 1:
        return CheckResult(
            check_id="REPORT-003",
            check_name="git commit记录",
            status="WARN",
            detail=f"执行记录中git commit记录不完整（score={score}/4）",
            suggestion="补充完整的commit历史表（commit hash + 内容 + 涉及文件）",
        )
    else:
        return CheckResult(
            check_id="REPORT-003",
            check_name="git commit记录",
            status="FAIL",
            detail="执行记录中未找到git commit记录",
            suggestion="补充git commit历史章节",
        )


def check_report_pass_criteria(lines: list[str]) -> CheckResult:
    """REPORT-004: 执行记录是否对照通过标准做判定。"""
    has_pass_criteria_ref = bool(find_line_with_pattern(lines, r"§7\.1|通过标准|COMPLETED.*[><=]"))
    has_sample_vs_full = bool(find_line_with_pattern(lines, r"样本.*正式判定|样本.*全量|10题样本.*919题"))
    has_explicit_verdict = bool(find_line_with_pattern(lines, r"初步.*倾向|正式.*判定|通过/不通过判定"))

    if has_pass_criteria_ref and has_sample_vs_full:
        return CheckResult(
            check_id="REPORT-004",
            check_name="对照通过标准判定",
            status="PASS",
            detail="执行记录对照§7.1通过标准做了判定，并区分了样本结论与全量判定",
        )
    elif has_pass_criteria_ref:
        return CheckResult(
            check_id="REPORT-004",
            check_name="对照通过标准判定",
            status="WARN",
            detail="执行记录引用了通过标准，但未明确区分样本结论与全量判定",
            suggestion="明确标注'N题样本=初步结论，919题全量=正式判定'",
        )
    else:
        return CheckResult(
            check_id="REPORT-004",
            check_name="对照通过标准判定",
            status="FAIL",
            detail="执行记录未对照通过标准做判定",
            suggestion="补充§7.1通过标准的对照判定章节",
        )


def check_report_corrected_workflow(lines: list[str]) -> CheckResult:
    """REPORT-005: 执行记录是否引用修正后的流程。"""
    has_corrected_flow = bool(find_line_with_pattern(lines, r"修正后的选题流程|§10\.7"))
    has_pipe1_redo = bool(find_line_with_pattern(lines, r"Pipe\s*1.*重新分析|完整thinking.*重新分析|续传后.*完整thinking"))

    if has_corrected_flow and has_pipe1_redo:
        return CheckResult(
            check_id="REPORT-005",
            check_name="引用修正后的流程",
            status="PASS",
            detail="执行记录引用了§10.7修正后的选题流程，并说明Pipe 1在完整thinking上重新分析",
        )
    elif has_corrected_flow or has_pipe1_redo:
        return CheckResult(
            check_id="REPORT-005",
            check_name="引用修正后的流程",
            status="WARN",
            detail="执行记录部分引用了修正后的流程",
            suggestion="补充完整的修正流程引用（§10.7 + Pipe 1在完整thinking上重新分析）",
        )
    else:
        return CheckResult(
            check_id="REPORT-005",
            check_name="引用修正后的流程",
            status="FAIL",
            detail="执行记录未引用修正后的流程",
            suggestion="补充§10.7修正后的选题流程引用",
        )


def check_report_no_terminate_discipline(lines: list[str]) -> CheckResult:
    """REPORT-006: 执行记录是否包含"不终止已启动的run"纪律。"""
    has_discipline = bool(find_line_with_pattern(lines, r"不终止.*run|§9\.6|不.*终止.*已启动"))

    if has_discipline:
        return CheckResult(
            check_id="REPORT-006",
            check_name="不终止已启动run纪律",
            status="PASS",
            detail="执行记录包含'不终止已启动的run'纪律记录",
        )
    else:
        return CheckResult(
            check_id="REPORT-006",
            check_name="不终止已启动run纪律",
            status="WARN",
            detail="执行记录中未找到'不终止已启动的run'纪律记录",
            suggestion="补充§9.6'不终止已启动的run'纪律记录",
        )


# =============================================================================
# 主审计流程
# =============================================================================

def audit_plan_document(plan_path: str, code_path: Optional[str] = None) -> list:
    """审计方案文档，返回CheckResult列表。"""
    _, plan_lines = read_file(plan_path)
    code_lines = read_file(code_path)[1] if code_path else None

    return [
        check_plan_nohup_vs_tmux(plan_lines),
        check_plan_method_vs_code(plan_lines, code_lines),
        check_plan_scale_estimate_matches_method(plan_lines),
    ]


def audit_report_document(report_path: str) -> list:
    """审计执行记录，返回CheckResult列表。"""
    _, report_lines = read_file(report_path)

    return [
        check_report_env_check(report_lines),
        check_report_monitoring(report_lines),
        check_report_git_commit(report_lines),
        check_report_pass_criteria(report_lines),
        check_report_corrected_workflow(report_lines),
        check_report_no_terminate_discipline(report_lines),
    ]


def main():
    parser = argparse.ArgumentParser(
        description="POC方案文档与执行记录差异审计脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
检查项：
  方案文档（PLAN-xxx）:
    PLAN-001  tmux优先铁律（禁止nohup）
    PLAN-002  方案method声明与代码默认值一致性
    PLAN-003  规模估算与method匹配性

  执行记录（REPORT-xxx）:
    REPORT-001  环境检查记录
    REPORT-002  监控纪律记录
    REPORT-003  git commit记录
    REPORT-004  对照通过标准判定
    REPORT-005  引用修正后的流程
    REPORT-006  不终止已启动run纪律

示例：
    python3 audit_poc_doc_vs_execution.py \\
        --plan "Tell分类学研究过程文档/415-v0-2026-08-18-POC-2.7-截断vs思维错误.md" \\
        --report "POC-2.7/POC-2.7-001-完整进度报告.md" \\
        --code "Tell分类学研究过程文档/poc_assets/poc_2.7/batch_continue_948.py"
        """,
    )
    parser.add_argument("--plan", help="POC方案文档路径")
    parser.add_argument("--report", help="执行记录（进度报告）路径")
    parser.add_argument("--code", help="执行代码路径（用于对照method默认值）")
    parser.add_argument("--json", help="输出JSON结果到指定路径")
    args = parser.parse_args()

    if not args.plan and not args.report:
        parser.error("至少提供 --plan 或 --report 之一")

    report = AuditReport(
        plan_file=args.plan or "",
        report_file=args.report or "",
        code_file=args.code or "",
    )

    if args.plan:
        report.results.extend(audit_plan_document(args.plan, args.code))

    if args.report:
        report.results.extend(audit_report_document(args.report))

    # 输出到终端
    print(report.summary())

    # 输出JSON
    if args.json:
        Path(args.json).write_text(report.to_json())
        print(f"\nJSON结果已保存到: {args.json}")

    # 退出码：有FAIL=1，只有WARN=0
    has_fail = any(r.status == "FAIL" for r in report.results)
    sys.exit(1 if has_fail else 0)


if __name__ == "__main__":
    main()
