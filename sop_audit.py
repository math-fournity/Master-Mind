#!/usr/bin/env python3
"""
SOP汇报审计脚本

审计Worker是否按照SOP要求汇报了维度/成熟度/可计算性。
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

ROOT = Path(__file__).parent
AUDIT_DIR = ROOT / "runtime" / "audit_logs"
CHECKPOINTS_DIR = ROOT / "runtime" / "checkpoints"

# 维度定义
DIMENSION_TYPES = {
    "operator": "算子维度（躔/照/会/守/冲/合/...）",
    "set": "集合维度（Star/Mansion/Palace/...）",
    "proposition": "命题维度（躔度/照宫/交会/...）",
    "state": "状态维度（吉凶/强弱/旺衰/...）",
    "time": "时间维度（原盘/大限/流年/...）",
    "system": "体系维度（七政四余/八字/...）"
}

# 成熟度指标
MATURITY_METRICS = {
    "coverage": "覆盖率",
    "consistency": "一致性",
    "evaluability": "可求值性",
    "explanatory": "解释力",
    "quantitative": "定量化",
    "cross_system": "跨体系",
    "verifiability": "可验证性"
}

# 可计算性层次
COMPUTABILITY_LEVELS = {
    "formal": "形式可计算",
    "quantitative": "定量可计算",
    "deductive": "推演可计算"
}


def load_checkpoint(worker_id: str, task_id: str, section_id: str) -> Dict:
    """加载检查点"""
    section_id_safe = section_id.replace("/", "_")
    checkpoint_file = CHECKPOINTS_DIR / f"{worker_id}_{task_id}_{section_id_safe}.json"
    
    if not checkpoint_file.exists():
        return {}
    
    with open(checkpoint_file, "r", encoding="utf-8") as f:
        return json.load(f)


def audit_sop_report(worker_id: str, task_id: str, section_id: str) -> Dict:
    """审计SOP汇报"""
    checkpoint = load_checkpoint(worker_id, task_id, section_id)
    
    if not checkpoint:
        return {
            "status": "no_checkpoint",
            "message": f"找不到检查点: {worker_id}/{task_id}/{section_id}"
        }
    
    # 检查是否包含SOP汇报字段
    sop_report = checkpoint.get("sop_report", {})
    
    # 审计维度汇报
    dimensions = sop_report.get("dimensions", [])
    dimension_audit = {
        "reported": len(dimensions) > 0,
        "count": len(dimensions),
        "types": dimensions,
        "missing": [d for d in DIMENSION_TYPES if d not in dimensions]
    }
    
    # 审计成熟度汇报
    maturity = sop_report.get("maturity", {})
    maturity_audit = {
        "reported": len(maturity) > 0,
        "metrics": maturity,
        "missing": [m for m in MATURITY_METRICS if m not in maturity]
    }
    
    # 审计可计算性汇报
    computability = sop_report.get("computability", {})
    computability_audit = {
        "reported": len(computability) > 0,
        "levels": computability,
        "missing": [c for c in COMPUTABILITY_LEVELS if c not in computability]
    }
    
    # 综合判定
    all_reported = (
        dimension_audit["reported"] and
        maturity_audit["reported"] and
        computability_audit["reported"]
    )
    
    return {
        "status": "verified" if all_reported else "incomplete",
        "worker_id": worker_id,
        "task_id": task_id,
        "section_id": section_id,
        "dimension_audit": dimension_audit,
        "maturity_audit": maturity_audit,
        "computability_audit": computability_audit,
        "all_reported": all_reported,
        "timestamp": datetime.now().isoformat()
    }


def generate_sop_audit_report(worker_id: str, task_id: str) -> Dict:
    """生成SOP审计报告"""
    # 查找该任务的所有检查点
    if not CHECKPOINTS_DIR.exists():
        return {
            "status": "no_checkpoints",
            "message": "没有检查点目录"
        }
    
    checkpoints = list(CHECKPOINTS_DIR.glob(f"{worker_id}_{task_id}_*.json"))
    
    if not checkpoints:
        return {
            "status": "no_checkpoints",
            "message": f"找不到任务 {task_id} 的检查点"
        }
    
    # 审计每个检查点
    audits = []
    for cp_file in checkpoints:
        parts = cp_file.stem.split("_")
        if len(parts) >= 3:
            section_id = "_".join(parts[2:]).replace("_", "/")
            audit = audit_sop_report(worker_id, task_id, section_id)
            audits.append(audit)
    
    # 统计
    total = len(audits)
    complete = len([a for a in audits if a["status"] == "verified"])
    incomplete = len([a for a in audits if a["status"] == "incomplete"])
    missing = len([a for a in audits if a["status"] == "no_checkpoint"])
    
    return {
        "status": "complete" if complete == total else "partial",
        "worker_id": worker_id,
        "task_id": task_id,
        "total_sections": total,
        "complete_sections": complete,
        "incomplete_sections": incomplete,
        "missing_sections": missing,
        "coverage_rate": f"{complete}/{total} ({complete/total*100:.1f}%)" if total > 0 else "0/0 (0%)",
        "audits": audits,
        "timestamp": datetime.now().isoformat()
    }


def save_audit_log(report: Dict, audit_type: str):
    """保存审计日志"""
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    
    log_file = AUDIT_DIR / f"sop_audit_{audit_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 审计日志已保存: {log_file.name}")
    return log_file


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="SOP汇报审计脚本")
    parser.add_argument("--action", choices=["audit-section", "audit-task", "report"], 
                       default="audit-task", help="审计动作")
    parser.add_argument("--worker-id", help="Worker ID")
    parser.add_argument("--task-id", help="任务ID")
    parser.add_argument("--section-id", help="Section ID")
    
    args = parser.parse_args()
    
    if args.action == "audit-section":
        if not all([args.worker_id, args.task_id, args.section_id]):
            print("错误：audit-section 需要 --worker-id, --task-id, --section-id")
            return
        
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
    
    elif args.action == "audit-task":
        if not all([args.worker_id, args.task_id]):
            print("错误：audit-task 需要 --worker-id, --task-id")
            return
        
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
    
    elif args.action == "report":
        print("生成SOP审计报告...")
        # 这里可以生成综合报告
        print("功能待实现")


if __name__ == "__main__":
    main()
