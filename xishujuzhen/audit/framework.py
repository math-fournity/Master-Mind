"""审计框架核心——CheckResult、StandardAuditor基类、AuditData、AuditReport。"""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type


@dataclass(frozen=True)
class CheckResult:
    """单项检查结果。"""

    item_id: str          # 检查项ID，如"184-2.2-1"
    name: str             # 检查项名称
    verdict: str          # "通过" / "有缺陷" / "失败" / "N/A"
    detail: str           # 具体说明
    evidence: Dict[str, Any] = field(default_factory=dict)  # 支撑证据


@dataclass
class AuditData:
    """审计数据容器——从3个数据源提取的全部数据。"""

    run_id: str
    run_dir: str                          # run目录路径
    guided_loop_result: Dict[str, Any]    # guided_loop_result.json
    turn_logs: List[Dict[str, Any]]       # turn_log.json列表
    conversations: List[Dict[str, Any]]   # turn_*_conversation.json列表
    session_id: str                       # devin cli session_id
    session_info: Optional[Dict[str, Any]] = None      # sessions.db session记录
    message_nodes: List[Dict[str, Any]] = field(default_factory=list)  # sessions.db message_nodes
    tool_call_states: List[Dict[str, Any]] = field(default_factory=list)  # sessions.db tool_call_state
    arango_data: Dict[str, Any] = field(default_factory=dict)  # ArangoDB数据（按collection分）


@dataclass
class AuditReport:
    """审计报告。"""

    run_id: str
    timestamp: str
    standard_id: str
    standard_name: str
    results: List[CheckResult]
    overall_verdict: str   # "通过" / "有缺陷" / "失败"

    @property
    def passed_count(self) -> int:
        return sum(1 for r in self.results if r.verdict == "通过")

    @property
    def defect_count(self) -> int:
        return sum(1 for r in self.results if r.verdict == "有缺陷")

    @property
    def fail_count(self) -> int:
        return sum(1 for r in self.results if r.verdict == "失败")

    @property
    def na_count(self) -> int:
        return sum(1 for r in self.results if r.verdict == "N/A")

    def compute_overall(self) -> str:
        if self.fail_count > 0:
            return "失败"
        if self.defect_count > 0:
            return "有缺陷"
        return "通过"


class StandardAuditor:
    """审计器基类——子类按模块实现具体的检查项。"""

    standard_id: str = ""
    standard_name: str = ""

    def audit(self, data: AuditData) -> List[CheckResult]:
        """按检查项逐项执行审计。子类必须实现。"""
        raise NotImplementedError

    def run(self, data: AuditData) -> AuditReport:
        """执行审计并生成报告。"""
        results = self.audit(data)
        report = AuditReport(
            run_id=data.run_id,
            timestamp=datetime.datetime.now().isoformat(),
            standard_id=self.standard_id,
            standard_name=self.standard_name,
            results=results,
            overall_verdict="",
        )
        report.overall_verdict = report.compute_overall()
        return report


def run_audit(
    data: AuditData,
    standards: List[Type[StandardAuditor]],
) -> List[AuditReport]:
    """对一组标准执行审计，返回多个报告。"""
    reports = []
    for std_cls in standards:
        auditor = std_cls()
        report = auditor.run(data)
        reports.append(report)
    return reports
