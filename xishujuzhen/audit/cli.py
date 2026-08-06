"""命令行入口——审计一个run并输出报告。"""

from __future__ import annotations

import argparse
import sys
import importlib
from typing import List, Type

from xishujuzhen.audit.framework import StandardAuditor, run_audit
from xishujuzhen.audit.data_sources import load_audit_data
from xishujuzhen.audit.report import generate_markdown_report, generate_json_report


# 标准ID到模块名的映射
STANDARD_MAP = {
    "184": "xishujuzhen.audit.standards.std_184_loop",
    "185": "xishujuzhen.audit.standards.std_185_controller",
    "186": "xishujuzhen.audit.standards.std_186_budget",
    "187": "xishujuzhen.audit.standards.std_187_events",
    "188": "xishujuzhen.audit.standards.std_188_reducer",
    "189": "xishujuzhen.audit.standards.std_189_heuristics",
    "190": "xishujuzhen.audit.standards.std_190_retrieval",
    "191": "xishujuzhen.audit.standards.std_191_context",
    "192": "xishujuzhen.audit.standards.std_192_verification",
    "193": "xishujuzhen.audit.standards.std_193_auditor",
    "194": "xishujuzhen.audit.standards.std_194_solver",
    "195": "xishujuzhen.audit.standards.std_195_math",
}


def load_standards(standard_ids: List[str]) -> List[Type[StandardAuditor]]:
    """加载标准审计器类。"""
    classes = []
    for sid in standard_ids:
        module_name = STANDARD_MAP.get(sid)
        if not module_name:
            print(f"警告: 未知标准ID {sid}", file=sys.stderr)
            continue
        try:
            mod = importlib.import_module(module_name)
            # 找到StandardAuditor的子类
            for attr_name in dir(mod):
                attr = getattr(mod, attr_name)
                if (isinstance(attr, type)
                    and issubclass(attr, StandardAuditor)
                    and attr is not StandardAuditor
                    and attr.standard_id == sid):
                    classes.append(attr)
                    break
        except ImportError:
            print(f"警告: 标准 {sid} 尚未实现（{module_name}）", file=sys.stderr)
    return classes


def main():
    parser = argparse.ArgumentParser(description="数学大师系统审计工具")
    sub = parser.add_subparsers(dest="command")

    # audit子命令
    audit_parser = sub.add_parser("audit", help="审计一个run")
    audit_parser.add_argument("--run-id", required=True, help="run ID")
    audit_parser.add_argument("--standards", default="all", help="标准ID列表，逗号分隔，或'all'")
    audit_parser.add_argument("--runs-root", default="runs", help="run目录根路径")
    audit_parser.add_argument("--no-sessions-db", action="store_true", help="不查sessions.db")
    audit_parser.add_argument("--no-arango", action="store_true", help="不查ArangoDB")
    audit_parser.add_argument("--output-dir", default=None, help="报告输出目录（默认run目录）")

    # report子命令
    report_parser = sub.add_parser("report", help="从已有审计结果生成报告")
    report_parser.add_argument("--run-id", required=True, help="run ID")
    report_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    args = parser.parse_args()

    if args.command == "audit":
        # 确定标准列表
        if args.standards == "all":
            standard_ids = list(STANDARD_MAP.keys())
        else:
            standard_ids = [s.strip() for s in args.standards.split(",")]

        # 加载标准
        standard_classes = load_standards(standard_ids)
        if not standard_classes:
            print("没有可用的标准审计器。", file=sys.stderr)
            sys.exit(1)

        # 加载数据
        print(f"加载run数据: {args.run_id}")
        data = load_audit_data(
            run_id=args.run_id,
            runs_root=args.runs_root,
            use_sessions_db=not args.no_sessions_db,
            use_arango=not args.no_arango,
        )
        print(f"  session_id: {data.session_id}")
        print(f"  message_nodes: {len(data.message_nodes)}")
        print(f"  tool_call_states: {len(data.tool_call_states)}")
        print(f"  arango collections: {len(data.arango_data)}")

        # 执行审计
        print(f"\n执行审计（{len(standard_classes)}个标准）:")
        reports = run_audit(data, standard_classes)

        for r in reports:
            print(f"  {r.standard_id}号 {r.standard_name}: {r.overall_verdict} "
                  f"(通过{r.passed_count}/缺陷{r.defect_count}/失败{r.fail_count}/NA{r.na_count})")

        # 输出报告
        output_dir = args.output_dir or os.path.join(args.runs_root, args.run_id)
        os.makedirs(output_dir, exist_ok=True)

        md_path = os.path.join(output_dir, "auto_audit_report.md")
        json_path = os.path.join(output_dir, "auto_audit_report.json")

        generate_markdown_report(reports, md_path)
        generate_json_report(reports, json_path)

        print(f"\n报告已生成:")
        print(f"  Markdown: {md_path}")
        print(f"  JSON: {json_path}")

    elif args.command == "report":
        print("report子命令尚未实现，请使用audit子命令。")
        sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    import os
    main()
