#!/usr/bin/env python3
"""
Master Agent 主控脚本

用于分配任务、监控进度、收集结果。
"""

import json
import sys
import argparse
import os
import shlex
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# 路径配置
ROOT = Path(__file__).parent
TASKS_FILE = ROOT / "tasks.json"
RUNTIME_DIR = ROOT / "runtime"
CHECKPOINTS_DIR = RUNTIME_DIR / "checkpoints"
RESULTS_DIR = RUNTIME_DIR / "results"
AUDIT_DIR = RUNTIME_DIR / "audit_logs"


def load_tasks() -> Dict:
    """加载任务队列"""
    if not TASKS_FILE.exists():
        return {"version": "1.0", "workers": {}, "tasks": []}
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(data: Dict):
    """保存任务队列"""
    with open(TASKS_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def cmd_status(args):
    """查看系统状态"""
    data = load_tasks()
    
    # 统计任务状态
    status_counts = {}
    for task in data["tasks"]:
        status = task["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    
    # 统计Worker状态
    worker_status = {}
    for worker_id, worker in data["workers"].items():
        worker_status[worker_id] = worker["status"]
    
    print("=" * 60)
    print("Master Agent 状态")
    print("=" * 60)
    print(f"\n任务统计:")
    for status, count in status_counts.items():
        print(f"  {status}: {count}")
    
    print(f"\nWorker 状态:")
    for worker_id, status in worker_status.items():
        print(f"  {worker_id}: {status}")
    
    # 检查检查点
    if CHECKPOINTS_DIR.exists():
        checkpoints = list(CHECKPOINTS_DIR.glob("*.json"))
        print(f"\n检查点: {len(checkpoints)} 个")
    
    # 检查结果
    if RESULTS_DIR.exists():
        results = list(RESULTS_DIR.glob("*.json"))
        print(f"\n结果: {len(results)} 个")
    
    print("\n" + "=" * 60)


def cmd_assign(args):
    """分配任务给Worker"""
    data = load_tasks()
    
    # 查找任务
    task = None
    for t in data["tasks"]:
        if t["id"] == args.task_id:
            task = t
            break
    
    if not task:
        print(f"错误：找不到任务 {args.task_id}", file=sys.stderr)
        sys.exit(1)
    
    if task["status"] != "queued":
        print(f"错误：任务 {args.task_id} 状态不是 queued，而是 {task['status']}", file=sys.stderr)
        sys.exit(1)
    
    # 检查依赖
    if task["dependencies"]:
        completed_ids = {t["id"] for t in data["tasks"] if t["status"] == "completed"}
        for dep in task["dependencies"]:
            if dep not in completed_ids:
                print(f"错误：任务 {args.task_id} 的依赖 {dep} 未完成", file=sys.stderr)
                sys.exit(1)
    
    # 查找空闲Worker
    worker_id = args.worker_id
    if worker_id not in data["workers"]:
        print(f"错误：Worker {worker_id} 不存在", file=sys.stderr)
        sys.exit(1)
    
    if data["workers"][worker_id]["status"] != "idle":
        print(f"错误：Worker {worker_id} 不是空闲状态", file=sys.stderr)
        sys.exit(1)
    
    # 分配任务
    task["status"] = "leased"
    task["assigned_to"] = worker_id
    task["updated_at"] = datetime.now().isoformat()
    
    data["workers"][worker_id]["status"] = "busy"
    data["workers"][worker_id]["current_task"] = args.task_id
    
    save_tasks(data)
    
    print(f"已将任务 {args.task_id} 分配给 Worker {worker_id}")
    print(f"任务标题: {task['title']}")


def cmd_checkpoint(args):
    """记录检查点"""
    checkpoint_file = CHECKPOINTS_DIR / f"{args.worker_id}_{args.task_id}.json"
    
    checkpoint = {
        "worker_id": args.worker_id,
        "task_id": args.task_id,
        "phase": args.phase,
        "cursor_line": args.cursor_line,
        "evidence_count": args.evidence_count,
        "note": args.note,
        "timestamp": datetime.now().isoformat(),
    }
    
    with open(checkpoint_file, "w") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    
    print(f"已记录检查点: {checkpoint_file.name}")


def cmd_complete(args):
    """完成任务"""
    data = load_tasks()
    
    # 查找任务
    task = None
    for t in data["tasks"]:
        if t["id"] == args.task_id:
            task = t
            break
    
    if not task:
        print(f"错误：找不到任务 {args.task_id}", file=sys.stderr)
        sys.exit(1)
    
    # 完成任务
    task["status"] = "completed"
    task["completed_at"] = datetime.now().isoformat()
    task["result"] = args.result
    task["updated_at"] = datetime.now().isoformat()
    
    # 释放Worker
    worker_id = task["assigned_to"]
    if worker_id and worker_id in data["workers"]:
        data["workers"][worker_id]["status"] = "idle"
        data["workers"][worker_id]["current_task"] = None
    
    save_tasks(data)
    
    # 保存结果
    result_file = RESULTS_DIR / f"{args.task_id}.json"
    result = {
        "task_id": args.task_id,
        "result": args.result,
        "completed_at": datetime.now().isoformat(),
    }
    with open(result_file, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"任务 {args.task_id} 已完成")
    print(f"结果已保存到: {result_file.name}")


def cmd_may_stop(args):
    """停止门检查"""
    data = load_tasks()
    
    # 检查是否有未完成的任务
    queued_tasks = [t for t in data["tasks"] if t["status"] == "queued"]
    leased_tasks = [t for t in data["tasks"] if t["status"] == "leased"]
    
    # 检查是否有忙碌的Worker
    busy_workers = [w for w, info in data["workers"].items() if info["status"] == "busy"]
    
    can_stop = len(queued_tasks) == 0 and len(leased_tasks) == 0 and len(busy_workers) == 0
    
    print("=" * 60)
    print("停止门检查")
    print("=" * 60)
    print(f"\n排队任务: {len(queued_tasks)}")
    print(f"租赁任务: {len(leased_tasks)}")
    print(f"忙碌Worker: {len(busy_workers)}")
    
    if can_stop:
        print(f"\n✅ 可以停止 (STOP_ALLOWED)")
    else:
        print(f"\n❌ 不能停止 (CONTINUE_REQUIRED)")
        if queued_tasks:
            print(f"   还有 {len(queued_tasks)} 个排队任务")
        if leased_tasks:
            print(f"   还有 {len(leased_tasks)} 个租赁任务")
        if busy_workers:
            print(f"   还有 {len(busy_workers)} 个忙碌Worker")
    
    print("\n" + "=" * 60)
    
    return can_stop


def cmd_list(args):
    """列出任务"""
    data = load_tasks()
    
    # 过滤状态
    tasks = data["tasks"]
    if args.status:
        tasks = [t for t in tasks if t["status"] == args.status]
    
    print("=" * 80)
    print("任务列表")
    print("=" * 80)
    print(f"\n{'ID':<10} {'状态':<12} {'优先级':<10} {'标题':<40}")
    print("-" * 80)
    
    for task in tasks:
        print(f"{task['id']:<10} {task['status']:<12} {task.get('priority', 'medium'):<10} {task['title'][:40]:<40}")
    
    print("\n" + "=" * 80)


def cmd_worker_status(args):
    """查看Worker状态"""
    data = load_tasks()
    
    if args.worker_id:
        # 查看指定Worker
        if args.worker_id not in data["workers"]:
            print(f"错误：Worker {args.worker_id} 不存在", file=sys.stderr)
            sys.exit(1)
        
        worker = data["workers"][args.worker_id]
        print(f"Worker {args.worker_id}: {worker['status']}")
        if worker["current_task"]:
            print(f"当前任务: {worker['current_task']}")
    else:
        # 查看所有Worker
        print("=" * 40)
        print("Worker 状态")
        print("=" * 40)
        for worker_id, worker in data["workers"].items():
            print(f"{worker_id}: {worker['status']}")
            if worker["current_task"]:
                print(f"  当前任务: {worker['current_task']}")
        print("=" * 40)


def cmd_verify_complete(args):
    """验证完整性"""
    from verify_integrity import load_path_tree, generate_completeness_report, save_audit_log
    
    print(f"开始验证 {args.document} 的完整性...")
    
    # 加载path树
    path_tree = load_path_tree()
    
    # 生成报告
    report = generate_completeness_report(path_tree)
    
    # 打印报告
    print(f"\n{'='*60}")
    print("完整性验证报告")
    print(f"{'='*60}")
    print(f"文档: {report['document']}")
    print(f"验证时间: {report['verification_time']}")
    print(f"\n覆盖统计:")
    print(f"  卷: {report['coverage_summary']['volume_coverage']}")
    print(f"  节: {report['coverage_summary']['section_coverage']}")
    print(f"  规则: {report['coverage_summary']['rule_coverage']}")
    print(f"\n判定: {report['verdict']}")
    
    if report['missing_content']:
        print(f"\n遗漏内容:")
        for item in report['missing_content']:
            print(f"  - {item}")
    
    # 保存审计日志
    save_audit_log(report, "master", "full_document")


def cmd_verify_section(args):
    """验证section完整性"""
    from verify_integrity import verify_line_coverage, save_audit_log
    
    print(f"验证 {args.section_id} 的行级覆盖...")
    result = verify_line_coverage(args.worker_id, args.task_id, args.section_id)
    
    print(f"\n{'='*60}")
    print("行级覆盖验证")
    print(f"{'='*60}")
    print(f"Section: {args.section_id}")
    print(f"状态: {result['status']}")
    
    if result['status'] == 'verified':
        print(f"行范围: {result['line_range']['start']}-{result['line_range']['end']} ({result['line_range']['total']}行)")
        print(f"内容哈希: {result['content_hash']}")
    
    # 保存审计日志
    save_audit_log(result, args.worker_id, args.section_id)


def cmd_report_line_coverage(args):
    """报告行级覆盖"""
    # 创建检查点文件
    CHECKPOINTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 将section_id中的斜杠替换为下划线，用于文件名
    section_id_safe = args.section_id.replace("/", "_")
    checkpoint_file = CHECKPOINTS_DIR / f"{args.worker_id}_{args.task_id}_{section_id_safe}.json"
    
    checkpoint = {
        "worker_id": args.worker_id,
        "task_id": args.task_id,
        "section_id": args.section_id,
        "line_range": {
            "start": args.start_line,
            "end": args.end_line,
            "total": args.end_line - args.start_line + 1
        },
        "content_hash": args.content_hash,
        "timestamp": datetime.now().isoformat(),
        "type": "line_coverage_report"
    }
    
    with open(checkpoint_file, "w") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)
    
    print(f"已报告行级覆盖: {checkpoint_file.name}")
    print(f"Section: {args.section_id}")
    print(f"行范围: {args.start_line}-{args.end_line} ({args.end_line - args.start_line + 1}行)")
    print(f"内容哈希: {args.content_hash}")


def cmd_shutdown(args):
    """优雅停止系统"""
    import subprocess
    
    print("=" * 60)
    print("开始优雅停止系统")
    print("=" * 60)
    
    # 1. 检查停止门
    print("\n1. 检查停止门...")
    data = load_tasks()
    
    queued_tasks = [t for t in data["tasks"] if t["status"] == "queued"]
    leased_tasks = [t for t in data["tasks"] if t["status"] == "leased"]
    busy_workers = [w for w, info in data["workers"].items() if info["status"] == "busy"]
    
    if not args.force:
        if queued_tasks or leased_tasks or busy_workers:
            print(f"❌ 无法优雅停止：还有未完成任务")
            print(f"   排队任务: {len(queued_tasks)}")
            print(f"   租赁任务: {len(leased_tasks)}")
            print(f"   忙碌Worker: {len(busy_workers)}")
            print(f"\n使用 --force 强制停止")
            return
    
    # 2. 终止所有Worker会话
    print("\n2. 终止所有Worker会话...")
    for worker_id in data["workers"]:
        session_name = f"worker-{worker_id}"
        try:
            result = subprocess.run(
                ["tmux", "kill-session", "-t", session_name],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"   ✅ 已终止会话: {session_name}")
            else:
                print(f"   ⚠️ 会话不存在或已终止: {session_name}")
        except Exception as e:
            print(f"   ❌ 终止会话失败: {session_name} - {e}")
    
    # 3. 更新任务状态
    print("\n3. 更新任务状态...")
    for task in data["tasks"]:
        if task["status"] == "leased":
            task["status"] = "queued"
            task["assigned_to"] = None
            task["updated_at"] = datetime.now().isoformat()
            print(f"   ✅ 任务 {task['id']} 状态更新为 queued")
    
    # 4. 更新Worker状态
    print("\n4. 更新Worker状态...")
    for worker_id in data["workers"]:
        data["workers"][worker_id]["status"] = "idle"
        data["workers"][worker_id]["current_task"] = None
        print(f"   ✅ Worker {worker_id} 状态更新为 idle")
    
    save_tasks(data)
    
    # 5. 生成停止报告
    print("\n5. 生成停止报告...")
    report = {
        "shutdown_time": datetime.now().isoformat(),
        "shutdown_type": "graceful" if not args.force else "force",
        "tasks_summary": {
            "total": len(data["tasks"]),
            "completed": len([t for t in data["tasks"] if t["status"] == "completed"]),
            "in_progress": len([t for t in data["tasks"] if t["status"] == "in_progress"]),
            "queued": len([t for t in data["tasks"] if t["status"] == "queued"]),
            "leased": len([t for t in data["tasks"] if t["status"] == "leased"])
        },
        "workers_summary": {
            worker_id: {
                "status": info["status"],
                "current_task": info["current_task"]
            }
            for worker_id, info in data["workers"].items()
        },
        "checkpoints_saved": len(list(CHECKPOINTS_DIR.glob("*.json"))) if CHECKPOINTS_DIR.exists() else 0,
        "audit_logs_generated": len(list(AUDIT_DIR.glob("*.json"))) if AUDIT_DIR.exists() else 0
    }
    
    report_file = RUNTIME_DIR / f"shutdown_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"   ✅ 停止报告已保存: {report_file.name}")
    
    # 6. 清理临时文件
    print("\n6. 清理临时文件...")
    temp_dir = RUNTIME_DIR / "temp"
    if temp_dir.exists():
        import shutil
        shutil.rmtree(temp_dir)
        print(f"   ✅ 已清理临时目录: {temp_dir}")
    
    print("\n" + "=" * 60)
    print("✅ 系统已优雅停止")
    print("=" * 60)
    print(f"\n停止类型: {report['shutdown_type']}")
    print(f"任务完成: {report['tasks_summary']['completed']}/{report['tasks_summary']['total']}")
    print(f"检查点: {report['checkpoints_saved']} 个")
    print(f"审计日志: {report['audit_logs_generated']} 个")


def cmd_cleanup(args):
    """清理临时文件和会话"""
    import subprocess
    
    print("=" * 60)
    print("清理临时文件和会话")
    print("=" * 60)
    
    # 1. 清理临时目录
    print("\n1. 清理临时目录...")
    temp_dir = RUNTIME_DIR / "temp"
    if temp_dir.exists():
        import shutil
        shutil.rmtree(temp_dir)
        print(f"   ✅ 已清理: {temp_dir}")
    else:
        print(f"   ⚠️ 临时目录不存在: {temp_dir}")
    
    # 2. 清理已完成的检查点（可选）
    print("\n2. 检查检查点文件...")
    if CHECKPOINTS_DIR.exists():
        checkpoints = list(CHECKPOINTS_DIR.glob("*.json"))
        print(f"   找到 {len(checkpoints)} 个检查点文件")
        print(f"   ⚠️ 检查点文件已保留（用于审计）")
    
    # 3. 清理审计日志（可选）
    print("\n3. 检查审计日志...")
    if AUDIT_DIR.exists():
        logs = list(AUDIT_DIR.glob("*.json"))
        print(f"   找到 {len(logs)} 个审计日志")
        print(f"   ⚠️ 审计日志已保留（用于审计）")
    
    # 4. 清理不存在的tmux会话
    print("\n4. 清理tmux会话...")
    data = load_tasks()
    for worker_id in data["workers"]:
        session_name = f"worker-{worker_id}"
        try:
            result = subprocess.run(
                ["tmux", "has-session", "-t", session_name],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                subprocess.run(
                    ["tmux", "kill-session", "-t", session_name],
                    capture_output=True,
                    text=True
                )
                print(f"   ✅ 已终止会话: {session_name}")
            else:
                print(f"   ⚠️ 会话不存在: {session_name}")
        except Exception as e:
            print(f"   ❌ 检查会话失败: {session_name} - {e}")
    
    print("\n" + "=" * 60)
    print("✅ 清理完成")
    print("=" * 60)


def cmd_status_report(args):
    """生成状态报告"""
    import subprocess
    
    print("=" * 60)
    print("系统状态报告")
    print("=" * 60)
    
    data = load_tasks()
    
    # 1. 任务统计
    print("\n1. 任务统计:")
    status_counts = {}
    for task in data["tasks"]:
        status = task["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    
    for status, count in status_counts.items():
        print(f"   {status}: {count}")
    
    # 2. Worker状态
    print("\n2. Worker状态:")
    for worker_id, worker in data["workers"].items():
        print(f"   {worker_id}: {worker['status']}")
        if worker["current_task"]:
            print(f"      当前任务: {worker['current_task']}")
    
    # 3. 检查点统计
    print("\n3. 检查点统计:")
    if CHECKPOINTS_DIR.exists():
        checkpoints = list(CHECKPOINTS_DIR.glob("*.json"))
        print(f"   总数: {len(checkpoints)}")
        
        # 按Worker分组
        worker_checkpoints = {}
        for cp in checkpoints:
            parts = cp.stem.split("_")
            if len(parts) >= 1:
                worker_id = parts[0]
                worker_checkpoints[worker_id] = worker_checkpoints.get(worker_id, 0) + 1
        
        for worker_id, count in worker_checkpoints.items():
            print(f"   {worker_id}: {count} 个")
    else:
        print("   无检查点目录")
    
    # 4. 审计日志统计
    print("\n4. 审计日志统计:")
    if AUDIT_DIR.exists():
        logs = list(AUDIT_DIR.glob("*.json"))
        print(f"   总数: {len(logs)}")
    else:
        print("   无审计日志目录")
    
    # 5. 停止门状态
    print("\n5. 停止门状态:")
    queued_tasks = [t for t in data["tasks"] if t["status"] == "queued"]
    leased_tasks = [t for t in data["tasks"] if t["status"] == "leased"]
    busy_workers = [w for w, info in data["workers"].items() if info["status"] == "busy"]
    
    can_stop = len(queued_tasks) == 0 and len(leased_tasks) == 0 and len(busy_workers) == 0
    
    if can_stop:
        print("   ✅ 可以停止 (STOP_ALLOWED)")
    else:
        print("   ❌ 不能停止 (CONTINUE_REQUIRED)")
        if queued_tasks:
            print(f"      还有 {len(queued_tasks)} 个排队任务")
        if leased_tasks:
            print(f"      还有 {len(leased_tasks)} 个租赁任务")
        if busy_workers:
            print(f"      还有 {len(busy_workers)} 个忙碌Worker")
    
    # 6. 生成报告文件
    report = {
        "report_time": datetime.now().isoformat(),
        "tasks_summary": status_counts,
        "workers_summary": {
            worker_id: {
                "status": worker["status"],
                "current_task": worker["current_task"]
            }
            for worker_id, worker in data["workers"].items()
        },
        "checkpoints_count": len(list(CHECKPOINTS_DIR.glob("*.json"))) if CHECKPOINTS_DIR.exists() else 0,
        "audit_logs_count": len(list(AUDIT_DIR.glob("*.json"))) if AUDIT_DIR.exists() else 0,
        "can_stop": can_stop
    }
    
    report_file = RUNTIME_DIR / f"status_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n6. 报告已保存: {report_file.name}")
    
    print("\n" + "=" * 60)


def cmd_sop_audit(args):
    """SOP汇报审计"""
    from sop_audit import audit_sop_report, generate_sop_audit_report, save_audit_log
    
    if args.section_id:
        # 审计单个section
        print(f"审计 {args.section_id} 的SOP汇报...")
        result = audit_sop_report(args.worker_id, args.task_id, args.section_id)
        
        print(f"\n{'='*60}")
        print("SOP汇报审计")
        print(f"{'='*60}")
        print(f"Section: {args.section_id}")
        print(f"状态: {result['status']}")
        
        if result['status'] != 'no_checkpoint':
            print(f"\n维度汇报:")
            print(f"  已汇报: {result['dimension_audit']['reported']}")
            print(f"  数量: {result['dimension_audit']['count']}")
            if result['dimension_audit']['missing']:
                print(f"  缺失: {result['dimension_audit']['missing']}")
            
            print(f"\n成熟度汇报:")
            print(f"  已汇报: {result['maturity_audit']['reported']}")
            if result['maturity_audit']['missing']:
                print(f"  缺失: {result['maturity_audit']['missing']}")
            
            print(f"\n可计算性汇报:")
            print(f"  已汇报: {result['computability_audit']['reported']}")
            if result['computability_audit']['missing']:
                print(f"  缺失: {result['computability_audit']['missing']}")
        
        # 保存审计日志
        save_audit_log(result, f"section_{args.section_id.replace('/', '_')}")
    
    else:
        # 审计整个任务
        print(f"审计任务 {args.task_id} 的SOP汇报...")
        result = generate_sop_audit_report(args.worker_id, args.task_id)
        
        print(f"\n{'='*60}")
        print("任务SOP汇报审计报告")
        print(f"{'='*60}")
        print(f"任务: {args.task_id}")
        print(f"状态: {result['status']}")
        print(f"覆盖: {result['coverage_rate']}")
        
        if result['status'] != 'no_checkpoints':
            print(f"\n详细统计:")
            print(f"  总section数: {result['total_sections']}")
            print(f"  完整汇报: {result['complete_sections']}")
            print(f"  不完整汇报: {result['incomplete_sections']}")
            print(f"  缺失检查点: {result['missing_sections']}")
        
        # 保存审计日志
        save_audit_log(result, f"task_{args.task_id}")


def cmd_launch_auditor(args):
    """启动Auditor Agent进行语义审计"""
    import subprocess
    
    print("=" * 60)
    print("启动Auditor Agent进行语义审计")
    print("=" * 60)
    
    # 1. 生成审计提示词
    print("\n1. 生成审计提示词...")
    
    auditor_cmd = [
        sys.executable, "auditor.py", "audit-section",
        "--worker-id", args.worker_id,
        "--task-id", args.task_id,
        "--section-id", args.section_id
    ]
    
    if args.section_id:
        # 审计单个section
        result = subprocess.run(auditor_cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"错误: {result.stderr}")
    else:
        # 审计整个任务
        auditor_cmd = [
            sys.executable, "auditor.py", "audit-task",
            "--worker-id", args.worker_id,
            "--task-id", args.task_id
        ]
        result = subprocess.run(auditor_cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"错误: {result.stderr}")
    
    # 2. 启动Auditor Agent（在tmux中）
    print("\n2. 启动Auditor Agent...")
    
    session_name = f"auditor-{args.worker_id}-{args.task_id}"
    
    # 检查是否已存在会话
    check_cmd = ["tmux", "has-session", "-t", session_name]
    check_result = subprocess.run(check_cmd, capture_output=True, text=True)
    
    if check_result.returncode == 0:
        print(f"   ⚠️ 会话已存在: {session_name}")
        print(f"   请先运行: tmux kill-session -t {session_name}")
        return
    
    provider = args.provider or os.environ.get("MOIRA_AGENT_PROVIDER", "opencode")
    if provider not in {"opencode", "devin"}:
        print(f"   ❌ provider 只支持 opencode 或 devin: {provider}")
        return
    if not shutil.which(provider):
        print(f"   ❌ {provider} 未安装或不在 PATH 中")
        return

    # 构建Auditor Agent提示词
    auditor_prompt = f"""你是一个Auditor Agent，负责语义审计Worker的SOP汇报。

任务信息：
- Worker: {args.worker_id}
- 任务: {args.task_id}
- Section: {args.section_id or '整个任务'}

请执行以下步骤：
1. 读取runtime/auditor_prompts/目录下的审计提示词
2. 按照提示词要求进行语义审计
3. 输出审计结果（JSON格式）
4. 将结果保存到runtime/audit_logs/

审计完成后，请报告审计结果。"""

    prompt_dir = RUNTIME_DIR / "auditor_prompts"
    transcript_dir = RUNTIME_DIR / "transcripts"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    transcript_dir.mkdir(parents=True, exist_ok=True)
    safe_task = args.task_id.replace("/", "_")
    prompt_file = prompt_dir / f"{session_name}_{safe_task}.md"
    export_file = transcript_dir / f"{session_name}_{safe_task}.{provider}.atif.json"
    prompt_file.write_text(auditor_prompt, encoding="utf-8")

    launch_cmd = [
        sys.executable,
        "tools/agent_launcher.py",
        "--role", "auditor",
        "--provider", provider,
        "--prompt-file", str(prompt_file),
        "--export-file", str(export_file),
    ]

    # 在tmux中启动Auditor Agent
    tmux_cmd = [
        "tmux", "new-session", "-d", "-s", session_name,
        "-c", str(ROOT),
        " ".join(shlex.quote(part) for part in launch_cmd)
    ]
    
    try:
        result = subprocess.run(tmux_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ Auditor Agent已启动")
            print(f"   Provider: {provider}")
            print(f"   Prompt: {prompt_file}")
            print(f"   Transcript: {export_file}")
            print(f"   会话: {session_name}")
            print(f"   查看: tmux attach -t {session_name}")
        else:
            print(f"   ❌ 启动失败: {result.stderr}")
    except Exception as e:
        print(f"   ❌ 启动异常: {e}")
    
    print("\n" + "=" * 60)


def build_parser():
    """构建命令行解析器"""
    parser = argparse.ArgumentParser(description="Master Agent 主控脚本")
    parser.set_defaults(func=None)
    sub = parser.add_subparsers(dest="command")
    
    # status
    sp = sub.add_parser("status", help="查看系统状态")
    sp.set_defaults(func=cmd_status)
    
    # assign
    sp = sub.add_parser("assign", help="分配任务给Worker")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.set_defaults(func=cmd_assign)
    
    # checkpoint
    sp = sub.add_parser("checkpoint", help="记录检查点")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--phase", required=True, help="阶段")
    sp.add_argument("--cursor-line", required=True, type=int, help="当前行号")
    sp.add_argument("--evidence-count", required=True, type=int, help="证据数量")
    sp.add_argument("--note", required=True, help="备注")
    sp.set_defaults(func=cmd_checkpoint)
    
    # complete
    sp = sub.add_parser("complete", help="完成任务")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--result", required=True, help="结果")
    sp.set_defaults(func=cmd_complete)
    
    # may-stop
    sp = sub.add_parser("may-stop", help="停止门检查")
    sp.set_defaults(func=cmd_may_stop)
    
    # list
    sp = sub.add_parser("list", help="列出任务")
    sp.add_argument("--status", help="过滤状态")
    sp.set_defaults(func=cmd_list)
    
    # worker-status
    sp = sub.add_parser("worker-status", help="查看Worker状态")
    sp.add_argument("--worker-id", help="Worker ID（可选）")
    sp.set_defaults(func=cmd_worker_status)
    
    # verify-complete
    sp = sub.add_parser("verify-complete", help="验证完整性")
    sp.add_argument("--document", default="星平会海", help="文档名称")
    sp.set_defaults(func=cmd_verify_complete)
    
    # verify-section
    sp = sub.add_parser("verify-section", help="验证section完整性")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--section-id", required=True, help="Section ID")
    sp.set_defaults(func=cmd_verify_section)
    
    # report-line-coverage
    sp = sub.add_parser("report-line-coverage", help="报告行级覆盖")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--section-id", required=True, help="Section ID")
    sp.add_argument("--start-line", required=True, type=int, help="起始行号")
    sp.add_argument("--end-line", required=True, type=int, help="结束行号")
    sp.add_argument("--content-hash", required=True, help="内容SHA256哈希")
    sp.set_defaults(func=cmd_report_line_coverage)
    
    # shutdown
    sp = sub.add_parser("shutdown", help="优雅停止系统")
    sp.add_argument("--force", action="store_true", help="强制停止")
    sp.set_defaults(func=cmd_shutdown)
    
    # cleanup
    sp = sub.add_parser("cleanup", help="清理临时文件和会话")
    sp.set_defaults(func=cmd_cleanup)
    
    # status-report
    sp = sub.add_parser("status-report", help="生成状态报告")
    sp.set_defaults(func=cmd_status_report)
    
    # sop-audit
    sp = sub.add_parser("sop-audit", help="SOP汇报审计")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--section-id", help="Section ID（可选，不指定则审计整个任务）")
    sp.set_defaults(func=cmd_sop_audit)
    
    # launch-auditor
    sp = sub.add_parser("launch-auditor", help="启动Auditor Agent进行语义审计")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--section-id", help="Section ID（可选，不指定则审计整个任务）")
    sp.add_argument("--provider", choices=["opencode", "devin"], help="Agent provider，默认读取 MOIRA_AGENT_PROVIDER 或 opencode")
    sp.set_defaults(func=cmd_launch_auditor)
    
    return parser


def main():
    """主函数"""
    parser = build_parser()
    args = parser.parse_args()
    
    if args.func is None:
        parser.print_help()
        return
    
    args.func(args)


if __name__ == "__main__":
    main()
