#!/usr/bin/env python3
"""质量门控脚本

功能：
1. 检查审计记录是否完整
2. 检查一致性判定是否有依据
3. 检查修正建议是否可执行
4. 提供质量门控检查功能

用法：
  python quality_gate.py check --todo-id 20.4
  python quality_gate.py check-all
  python quality_gate.py report
"""

import argparse
import json
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


def quality_gate_check(todo_id):
    """
    质量门控检查
    
    Args:
        todo_id: TODO ID
    
    Returns:
        (bool, str, list): (是否通过, 消息, 详细检查结果)
    """
    records = load_audit_records(todo_id)
    
    if not records:
        return False, "没有找到审计记录", []
    
    checks = []
    all_passed = True
    
    # 步骤1：检查审计记录是否完整
    for record in records:
        valid, message = validate_audit_record(record)
        check_result = {
            "step": record.get("step", "未知"),
            "check": "审计记录完整性",
            "passed": valid,
            "message": message
        }
        checks.append(check_result)
        
        if not valid:
            all_passed = False
    
    # 步骤2：检查一致性判定是否有依据
    for record in records:
        if record["judgment"] in ["FAIL", "PARTIAL"]:
            has_evidence = bool(record.get("evidence") and len(record["evidence"]) >= 10)
            check_result = {
                "step": record.get("step", "未知"),
                "check": "FAIL/PARTIAL判定依据",
                "passed": has_evidence,
                "message": "FAIL/PARTIAL判定必须提供详细证据" if not has_evidence else "证据充分"
            }
            checks.append(check_result)
            
            if not has_evidence:
                all_passed = False
    
    # 步骤3：检查修正建议是否可执行
    for record in records:
        if "correction_suggestion" in record and record["correction_suggestion"]:
            # 检查修正建议是否具体
            is_specific = len(record["correction_suggestion"]) >= 20
            check_result = {
                "step": record.get("step", "未知"),
                "check": "修正建议可执行性",
                "passed": is_specific,
                "message": "修正建议过于笼统" if not is_specific else "修正建议具体可执行"
            }
            checks.append(check_result)
            
            if not is_specific:
                all_passed = False
    
    # 步骤4：检查是否有必要的元数据
    for record in records:
        has_metadata = bool(record.get("metadata"))
        check_result = {
            "step": record.get("step", "未知"),
            "check": "元数据完整性",
            "passed": True,  # 元数据是可选的
            "message": "有元数据" if has_metadata else "无元数据（可选）"
        }
        checks.append(check_result)
    
    # 生成汇总消息
    passed_count = sum(1 for c in checks if c["passed"])
    total_count = len(checks)
    
    if all_passed:
        message = f"质量门控通过（{passed_count}/{total_count} 检查通过）"
    else:
        failed_checks = [c for c in checks if not c["passed"]]
        message = f"质量门控未通过（{passed_count}/{total_count} 检查通过）"
        message += "\n失败的检查：\n"
        for check in failed_checks:
            message += f"  - [{check['step']}] {check['check']}: {check['message']}\n"
    
    return all_passed, message, checks


def check_all_todos():
    """
    检查所有TODO的审计记录
    
    Returns:
        dict: 检查结果，key为TODO ID，value为(是否通过, 消息)
    """
    results = {}
    
    # 加载所有审计记录
    all_records = load_audit_records()
    
    # 按TODO ID分组
    todo_ids = set(r.get("todo_id") for r in all_records if r.get("todo_id"))
    
    for todo_id in sorted(todo_ids):
        passed, message, checks = quality_gate_check(todo_id)
        results[todo_id] = {
            "passed": passed,
            "message": message,
            "checks": checks
        }
    
    return results


def generate_report():
    """
    生成质量门控报告
    
    Returns:
        str: 报告内容
    """
    results = check_all_todos()
    
    if not results:
        return "没有找到审计记录。"
    
    report = []
    report.append("质量门控报告")
    report.append("=" * 50)
    report.append(f"生成时间：{datetime.now().isoformat(timespec='seconds')}")
    report.append(f"检查TODO数：{len(results)}")
    report.append("")
    
    # 统计
    passed_count = sum(1 for r in results.values() if r["passed"])
    failed_count = len(results) - passed_count
    
    report.append("检查统计：")
    report.append(f"  通过：{passed_count:>3} ({passed_count/len(results)*100:.1f}%)")
    report.append(f"  未通过：{failed_count:>3} ({failed_count/len(results)*100:.1f}%)")
    report.append("")
    
    # 详细结果
    report.append("详细结果：")
    report.append("-" * 50)
    
    for todo_id, result in sorted(results.items()):
        status_icon = "✅" if result["passed"] else "❌"
        report.append(f"\n{status_icon} TODO {todo_id}")
        report.append(f"   状态：{'通过' if result['passed'] else '未通过'}")
        report.append(f"   消息：{result['message']}")
    
    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="质量门控脚本")
    sub = parser.add_subparsers(dest="command")
    
    # check
    p_check = sub.add_parser("check", help="检查TODO的审计记录")
    p_check.add_argument("--todo-id", required=True, help="TODO ID")
    p_check.set_defaults(func=lambda args: check_cmd(args.todo_id))
    
    # check-all
    p_check_all = sub.add_parser("check-all", help="检查所有TODO")
    p_check_all.set_defaults(func=lambda args: check_all_cmd())
    
    # report
    p_report = sub.add_parser("report", help="生成质量门控报告")
    p_report.set_defaults(func=lambda args: print(generate_report()))
    
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


def check_cmd(todo_id):
    """检查命令"""
    passed, message, checks = quality_gate_check(todo_id)
    
    if passed:
        print(f"✅ {message}")
        sys.exit(0)
    else:
        print(f"❌ {message}")
        sys.exit(1)


def check_all_cmd():
    """检查所有命令"""
    results = check_all_todos()
    
    if not results:
        print("没有找到审计记录。")
        return
    
    passed_count = sum(1 for r in results.values() if r["passed"])
    failed_count = len(results) - passed_count
    
    print(f"质量门控检查结果：")
    print(f"  总TODO数：{len(results)}")
    print(f"  通过：{passed_count}")
    print(f"  未通过：{failed_count}")
    print()
    
    if failed_count > 0:
        print("未通过的TODO：")
        for todo_id, result in sorted(results.items()):
            if not result["passed"]:
                print(f"  ❌ {todo_id}: {result['message']}")
    
    sys.exit(0 if failed_count == 0 else 1)


if __name__ == "__main__":
    main()
