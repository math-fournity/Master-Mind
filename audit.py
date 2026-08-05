#!/usr/bin/env python3
"""审计记录管理脚本

功能：
1. 生成结构化审计记录
2. 验证审计记录完整性
3. 生成审计报告
4. 保存审计记录到文件

用法：
  python audit.py create --todo-id 20.4 --step "文献普查" --input '{"literature": ["星学大成"]}' --output '{"status": "已获取"}' --judgment PASS --evidence "文献获取结果"
  python audit.py validate --file dev-notes/AUDIT-20.4-文献普查.json
  python audit.py report --todo-id 20.4
  python audit.py list --status FAIL
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# 配置
AUDIT_DIR = Path(__file__).parent / "dev-notes"
TODO_FILE = Path(__file__).parent / "dev-docs" / "todos.json"

# 有效判定
VALID_JUDGMENTS = ["PASS", "FAIL", "PARTIAL", "UNKNOWN"]

# 必需字段
REQUIRED_FIELDS = ["todo_id", "step", "input", "output", "judgment", "evidence", "timestamp"]


class AuditRecord:
    """审计记录类"""
    
    def __init__(self, todo_id, step, input_data, output_data, judgment, evidence, 
                 original_text=None, implementation=None, comparison=None,
                 correction_suggestion=None, metadata=None):
        """
        初始化审计记录
        
        Args:
            todo_id: TODO ID，如 "20.4"
            step: 步骤名称，如 "文献普查"
            input_data: 输入数据（dict或str）
            output_data: 输出数据（dict或str）
            judgment: 判定（PASS/FAIL/PARTIAL/UNKNOWN）
            evidence: 证据（必须提供）
            original_text: 原文引文（可选，逐句考据时使用）
            implementation: 我们的实现（可选，逐句考据时使用）
            comparison: 对比结果（可选，逐句考据时使用）
            correction_suggestion: 修正建议（可选，FAIL/PARTIAL时使用）
            metadata: 元数据（可选，如搜索结果、参考文献等）
        """
        self.todo_id = todo_id
        self.step = step
        self.input_data = input_data
        self.output_data = output_data
        self.judgment = judgment
        self.evidence = evidence
        self.original_text = original_text
        self.implementation = implementation
        self.comparison = comparison
        self.correction_suggestion = correction_suggestion
        self.metadata = metadata or {}
        self.timestamp = datetime.now().isoformat(timespec="seconds")
    
    def to_dict(self):
        """转换为字典"""
        result = {
            "todo_id": self.todo_id,
            "step": self.step,
            "input": self.input_data,
            "output": self.output_data,
            "judgment": self.judgment,
            "evidence": self.evidence,
            "timestamp": self.timestamp
        }
        
        # 添加可选字段
        if self.original_text:
            result["original_text"] = self.original_text
        if self.implementation:
            result["implementation"] = self.implementation
        if self.comparison:
            result["comparison"] = self.comparison
        if self.correction_suggestion:
            result["correction_suggestion"] = self.correction_suggestion
        if self.metadata:
            result["metadata"] = self.metadata
        
        return result
    
    def save(self, filename=None):
        """
        保存审计记录到文件
        
        Args:
            filename: 文件名（可选，默认为 dev-notes/AUDIT-{todo_id}-{step}.json）
        
        Returns:
            保存的文件路径
        """
        if filename is None:
            # 生成文件名：移除特殊字符
            safe_step = self.step.replace("/", "-").replace(" ", "_")
            filename = AUDIT_DIR / f"AUDIT-{self.todo_id}-{safe_step}.json"
        
        # 确保目录存在
        filename.parent.mkdir(parents=True, exist_ok=True)
        
        # 保存JSON
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
        
        return filename


def validate_audit_record(record):
    """
    验证审计记录完整性
    
    Args:
        record: 审计记录（dict）
    
    Returns:
        (bool, str): (是否有效, 消息)
    """
    # 检查必需字段
    for field in REQUIRED_FIELDS:
        if field not in record:
            return False, f"缺少字段: {field}"
    
    # 检查判定是否有效
    if record["judgment"] not in VALID_JUDGMENTS:
        return False, f"无效判定: {record['judgment']}。有效值: {VALID_JUDGMENTS}"
    
    # 检查证据是否提供
    if not record["evidence"]:
        return False, "必须提供证据（evidence字段不能为空）"
    
    # 检查FAIL/PARTIAL是否有证据
    if record["judgment"] in ["FAIL", "PARTIAL"]:
        if not record["evidence"] or len(record["evidence"]) < 10:
            return False, "FAIL/PARTIAL判定必须提供详细证据（至少10个字符）"
    
    return True, "审计记录完整"


def load_audit_records(todo_id=None):
    """
    加载审计记录
    
    Args:
        todo_id: TODO ID（可选，不提供则加载所有）
    
    Returns:
        list: 审计记录列表
    """
    records = []
    
    if not AUDIT_DIR.exists():
        return records
    
    for filename in AUDIT_DIR.glob("AUDIT-*.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                record = json.load(f)
                
                # 过滤TODO ID
                if todo_id and record.get("todo_id") != todo_id:
                    continue
                
                # 添加文件名信息
                record["_file"] = str(filename)
                records.append(record)
        except Exception as e:
            print(f"警告：无法加载 {filename}: {e}", file=sys.stderr)
    
    return records


def generate_report(todo_id=None):
    """
    生成审计报告
    
    Args:
        todo_id: TODO ID（可选，不提供则生成汇总报告）
    
    Returns:
        str: 报告内容
    """
    records = load_audit_records(todo_id)
    
    if not records:
        return "没有找到审计记录。"
    
    # 统计
    total = len(records)
    pass_count = sum(1 for r in records if r["judgment"] == "PASS")
    fail_count = sum(1 for r in records if r["judgment"] == "FAIL")
    partial_count = sum(1 for r in records if r["judgment"] == "PARTIAL")
    unknown_count = sum(1 for r in records if r["judgment"] == "UNKNOWN")
    
    # 生成报告
    report = []
    if todo_id:
        report.append(f"审计报告 - TODO {todo_id}")
    else:
        report.append("审计汇总报告")
    report.append("=" * 50)
    report.append(f"生成时间：{datetime.now().isoformat(timespec='seconds')}")
    report.append(f"总记录数：{total}")
    report.append("")
    
    report.append("判定统计：")
    report.append(f"  PASS:    {pass_count:>3} ({pass_count/total*100:.1f}%)")
    report.append(f"  FAIL:    {fail_count:>3} ({fail_count/total*100:.1f}%)")
    report.append(f"  PARTIAL: {partial_count:>3} ({partial_count/total*100:.1f}%)")
    report.append(f"  UNKNOWN: {unknown_count:>3} ({unknown_count/total*100:.1f}%)")
    report.append("")
    
    # 详细记录
    report.append("详细记录：")
    report.append("-" * 50)
    
    for record in sorted(records, key=lambda r: (r["todo_id"], r["step"])):
        status_icon = {
            "PASS": "✅",
            "FAIL": "❌",
            "PARTIAL": "⚠️",
            "UNKNOWN": "❓"
        }.get(record["judgment"], "?")
        
        report.append(f"\n{status_icon} {record['todo_id']} - {record['step']}")
        report.append(f"   判定：{record['judgment']}")
        report.append(f"   证据：{record['evidence'][:100]}...")
        if record.get("correction_suggestion"):
            report.append(f"   修正建议：{record['correction_suggestion'][:100]}...")
    
    return "\n".join(report)


def list_records(status=None, todo_id=None):
    """
    列出审计记录
    
    Args:
        status: 按状态过滤（PASS/FAIL/PARTIAL/UNKNOWN）
        todo_id: 按TODO ID过滤
    
    Returns:
        list: 审计记录列表
    """
    records = load_audit_records(todo_id)
    
    if status:
        records = [r for r in records if r["judgment"] == status]
    
    return records


def create_record(args):
    """
    创建审计记录
    
    Args:
        args: 命令行参数
    
    Returns:
        AuditRecord: 创建的审计记录
    """
    # 解析输入数据
    try:
        input_data = json.loads(args.input) if args.input else {}
    except json.JSONDecodeError:
        input_data = {"raw": args.input}
    
    # 解析输出数据
    try:
        output_data = json.loads(args.output) if args.output else {}
    except json.JSONDecodeError:
        output_data = {"raw": args.output}
    
    # 创建审计记录
    record = AuditRecord(
        todo_id=args.todo_id,
        step=args.step,
        input_data=input_data,
        output_data=output_data,
        judgment=args.judgment,
        evidence=args.evidence,
        original_text=args.original_text,
        implementation=args.implementation,
        comparison=args.comparison,
        correction_suggestion=args.correction_suggestion
    )
    
    # 保存
    filename = record.save()
    print(f"已创建审计记录：{filename}")
    
    return record


def main():
    parser = argparse.ArgumentParser(description="审计记录管理脚本")
    sub = parser.add_subparsers(dest="command")
    
    # create
    p_create = sub.add_parser("create", help="创建审计记录")
    p_create.add_argument("--todo-id", required=True, help="TODO ID，如 20.4")
    p_create.add_argument("--step", required=True, help="步骤名称，如 文献普查")
    p_create.add_argument("--input", help="输入数据（JSON字符串）")
    p_create.add_argument("--output", help="输出数据（JSON字符串）")
    p_create.add_argument("--judgment", required=True, choices=VALID_JUDGMENTS, help="判定")
    p_create.add_argument("--evidence", required=True, help="证据（必须提供）")
    p_create.add_argument("--original-text", help="原文引文（可选）")
    p_create.add_argument("--implementation", help="我们的实现（可选）")
    p_create.add_argument("--comparison", help="对比结果（可选）")
    p_create.add_argument("--correction-suggestion", help="修正建议（可选）")
    p_create.set_defaults(func=create_record)
    
    # validate
    p_validate = sub.add_parser("validate", help="验证审计记录")
    p_validate.add_argument("--file", required=True, help="审计记录文件路径")
    p_validate.set_defaults(func=lambda args: validate_file(args.file))
    
    # report
    p_report = sub.add_parser("report", help="生成审计报告")
    p_report.add_argument("--todo-id", help="TODO ID（可选）")
    p_report.set_defaults(func=lambda args: print(generate_report(args.todo_id)))
    
    # list
    p_list = sub.add_parser("list", help="列出审计记录")
    p_list.add_argument("--status", choices=VALID_JUDGMENTS, help="按状态过滤")
    p_list.add_argument("--todo-id", help="按TODO ID过滤")
    p_list.add_argument("--format", choices=["table", "json"], default="table", help="输出格式")
    p_list.set_defaults(func=lambda args: list_records_cmd(args))
    
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


def validate_file(filename):
    """验证审计记录文件"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            record = json.load(f)
        
        valid, message = validate_audit_record(record)
        if valid:
            print(f"✅ {message}")
            sys.exit(0)
        else:
            print(f"❌ {message}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ 无法加载文件：{e}")
        sys.exit(1)


def list_records_cmd(args):
    """列出审计记录命令"""
    records = list_records(status=args.status, todo_id=args.todo_id)
    
    if not records:
        print("没有找到审计记录。")
        return
    
    if args.format == "json":
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        print(f"共 {len(records)} 条审计记录：\n")
        print(f"{'TODO ID':<10} {'步骤':<20} {'判定':<10} {'时间':<20} {'证据'}")
        print("-" * 100)
        
        for record in records:
            status_icon = {
                "PASS": "✅",
                "FAIL": "❌",
                "PARTIAL": "⚠️",
                "UNKNOWN": "❓"
            }.get(record["judgment"], "?")
            
            evidence_preview = record["evidence"][:50] + "..." if len(record["evidence"]) > 50 else record["evidence"]
            print(f"{record['todo_id']:<10} {record['step']:<20} {status_icon} {record['judgment']:<8} {record['timestamp']:<20} {evidence_preview}")


if __name__ == "__main__":
    main()
