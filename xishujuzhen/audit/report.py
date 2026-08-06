"""报告生成器——JSON和Markdown格式。"""

from __future__ import annotations

import json
import os
from typing import List

from xishujuzhen.audit.framework import AuditReport


def generate_json_report(reports: List[AuditReport], output_path: str) -> str:
    """生成JSON审计报告。"""
    data = []
    for r in reports:
        data.append({
            "run_id": r.run_id,
            "timestamp": r.timestamp,
            "standard_id": r.standard_id,
            "standard_name": r.standard_name,
            "overall_verdict": r.overall_verdict,
            "summary": {
                "passed": r.passed_count,
                "defect": r.defect_count,
                "fail": r.fail_count,
                "na": r.na_count,
            },
            "results": [
                {
                    "item_id": cr.item_id,
                    "name": cr.name,
                    "verdict": cr.verdict,
                    "detail": cr.detail,
                    "evidence": cr.evidence,
                }
                for cr in r.results
            ],
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return output_path


def generate_markdown_report(reports: List[AuditReport], output_path: str) -> str:
    """生成Markdown审计报告。"""
    lines = []
    lines.append("# 自动化审计报告\n")

    for r in reports:
        lines.append(f"## {r.standard_id}号 · {r.standard_name}\n")
        lines.append(f"- **run_id**: {r.run_id}")
        lines.append(f"- **审计时间**: {r.timestamp}")
        lines.append(f"- **总判定**: **{r.overall_verdict}**")
        lines.append(f"- 通过: {r.passed_count} | 有缺陷: {r.defect_count} | 失败: {r.fail_count} | N/A: {r.na_count}\n")

        lines.append("| 检查项ID | 名称 | 判定 | 说明 |")
        lines.append("|---|---|---|---|")
        for cr in r.results:
            lines.append(f"| {cr.item_id} | {cr.name} | {cr.verdict} | {cr.detail} |")

        lines.append("")

    content = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return output_path
