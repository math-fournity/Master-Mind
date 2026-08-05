#!/usr/bin/env python3
"""
Auditor Agent 主控脚本

负责语义审计Worker的SOP汇报。
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List

ROOT = Path(__file__).parent
TASKS_FILE = ROOT / "tasks.json"
RUNTIME_DIR = ROOT / "runtime"
CHECKPOINTS_DIR = RUNTIME_DIR / "checkpoints"
AUDIT_DIR = RUNTIME_DIR / "audit_logs"
AUDITOR_PROMPTS_DIR = RUNTIME_DIR / "auditor_prompts"


def load_tasks() -> Dict:
    """加载任务队列"""
    if not TASKS_FILE.exists():
        return {"version": "1.0", "workers": {}, "tasks": []}
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def load_checkpoint(worker_id: str, task_id: str, section_id: str) -> Dict:
    """加载检查点"""
    section_id_safe = section_id.replace("/", "_")
    checkpoint_file = CHECKPOINTS_DIR / f"{worker_id}_{task_id}_{section_id_safe}.json"
    
    if not checkpoint_file.exists():
        return {}
    
    with open(checkpoint_file, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_semantic_audit_prompt(worker_id: str, task_id: str, section_id: str, checkpoint: Dict) -> str:
    """生成语义审计提示词"""
    
    # 提取SOP汇报
    sop_report = checkpoint.get("sop_report", {})
    dimensions = sop_report.get("dimensions", [])
    maturity = sop_report.get("maturity", {})
    computability = sop_report.get("computability", {})
    
    # 提取检查点信息
    phase = checkpoint.get("phase", "未知")
    note = checkpoint.get("note", "无")
    evidence_count = checkpoint.get("evidence_count", 0)
    
    prompt = f"""你是一个Auditor Agent，负责审计Worker的SOP汇报。

任务信息：
- 任务ID: {task_id}
- Section: {section_id}
- Worker: {worker_id}
- 阶段: {phase}
- 备注: {note}
- 证据数量: {evidence_count}

Worker汇报的SOP三要素：

1. 维度汇报：
   {json.dumps(dimensions, ensure_ascii=False, indent=2)}

2. 成熟度汇报：
   {json.dumps(maturity, ensure_ascii=False, indent=2)}

3. 可计算性汇报：
   {json.dumps(computability, ensure_ascii=False, indent=2)}

请按照以下标准进行语义审计：

## 维度审计标准
- 维度类型是否正确分类？（算子/集合/命题/状态/时间/体系）
- 每个维度是否有具体例子支撑？
- 是否发现了新的维度类型？

## 成熟度审计标准
- 每个指标是否有具体说明？（不是简单的"已提升"，而是具体提升了什么）
- 指标之间是否有逻辑关系？
- 是否有可验证的证据？

## 可计算性审计标准
- 每个层次是否有具体说明？
- 是否有可执行的算法或公式？
- 是否有验证结果？

请输出JSON格式的审计结果：
{{
  "audit_result": {{
    "dimension_audit": {{
      "score": 0-10,
      "comments": "维度审计评语",
      "issues": ["问题1", "问题2"],
      "suggestions": ["建议1", "建议2"]
    }},
    "maturity_audit": {{
      "score": 0-10,
      "comments": "成熟度审计评语",
      "issues": ["问题1", "问题2"],
      "suggestions": ["建议1", "建议2"]
    }},
    "computability_audit": {{
      "score": 0-10,
      "comments": "可计算性审计评语",
      "issues": ["问题1", "问题2"],
      "suggestions": ["建议1", "建议2"]
    }},
    "overall_score": 0-10,
    "overall_comments": "总体评语",
    "pass": true/false
  }}
}}
"""
    return prompt


def save_audit_prompt(prompt: str, worker_id: str, task_id: str, section_id: str):
    """保存审计提示词"""
    AUDITOR_PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    
    section_id_safe = section_id.replace("/", "_")
    prompt_file = AUDITOR_PROMPTS_DIR / f"audit_{worker_id}_{task_id}_{section_id_safe}.md"
    
    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(prompt)
    
    print(f"✅ 审计提示词已保存: {prompt_file.name}")
    return prompt_file


def cmd_audit_section(args):
    """审计单个section"""
    print("=" * 60)
    print("语义审计 - 单个Section")
    print("=" * 60)
    
    # 加载检查点
    checkpoint = load_checkpoint(args.worker_id, args.task_id, args.section_id)
    
    if not checkpoint:
        print(f"❌ 找不到检查点: {args.worker_id}/{args.task_id}/{args.section_id}")
        return
    
    print(f"\nWorker: {args.worker_id}")
    print(f"任务: {args.task_id}")
    print(f"Section: {args.section_id}")
    print(f"阶段: {checkpoint.get('phase', '未知')}")
    
    # 生成审计提示词
    prompt = generate_semantic_audit_prompt(
        args.worker_id, args.task_id, args.section_id, checkpoint
    )
    
    # 保存审计提示词
    prompt_file = save_audit_prompt(
        prompt, args.worker_id, args.task_id, args.section_id
    )
    
    print(f"\n审计提示词已生成: {prompt_file.name}")
    print(f"\n请将此提示词发送给Auditor Agent进行语义审计。")


def cmd_audit_task(args):
    """审计整个任务"""
    print("=" * 60)
    print("语义审计 - 整个任务")
    print("=" * 60)
    
    # 查找该任务的所有检查点
    if not CHECKPOINTS_DIR.exists():
        print("❌ 没有检查点目录")
        return
    
    checkpoints = list(CHECKPOINTS_DIR.glob(f"{args.worker_id}_{args.task_id}_*.json"))
    
    if not checkpoints:
        print(f"❌ 找不到任务 {args.task_id} 的检查点")
        return
    
    print(f"\nWorker: {args.worker_id}")
    print(f"任务: {args.task_id}")
    print(f"找到 {len(checkpoints)} 个检查点")
    
    # 为每个检查点生成审计提示词
    prompts = []
    for cp_file in checkpoints:
        parts = cp_file.stem.split("_")
        if len(parts) >= 3:
            section_id = "_".join(parts[2:]).replace("_", "/")
            
            with open(cp_file, "r", encoding="utf-8") as f:
                checkpoint = json.load(f)
            
            prompt = generate_semantic_audit_prompt(
                args.worker_id, args.task_id, section_id, checkpoint
            )
            
            prompt_file = save_audit_prompt(
                prompt, args.worker_id, args.task_id, section_id
            )
            
            prompts.append({
                "section_id": section_id,
                "prompt_file": str(prompt_file)
            })
    
    print(f"\n已生成 {len(prompts)} 个审计提示词:")
    for p in prompts:
        print(f"  - {p['section_id']}: {p['prompt_file']}")


def cmd_generate_report(args):
    """生成审计报告"""
    print("=" * 60)
    print("生成审计报告")
    print("=" * 60)
    
    # 这里可以读取所有审计结果并生成综合报告
    print("\n功能待实现：")
    print("1. 读取所有审计结果")
    print("2. 统计审计得分")
    print("3. 生成综合报告")
    print("4. 保存到 runtime/audit_logs/")


def build_parser():
    """构建命令行解析器"""
    parser = argparse.ArgumentParser(description="Auditor Agent 主控脚本")
    parser.set_defaults(func=None)
    sub = parser.add_subparsers(dest="command")
    
    # audit-section
    sp = sub.add_parser("audit-section", help="审计单个section")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.add_argument("--section-id", required=True, help="Section ID")
    sp.set_defaults(func=cmd_audit_section)
    
    # audit-task
    sp = sub.add_parser("audit-task", help="审计整个任务")
    sp.add_argument("--worker-id", required=True, help="Worker ID")
    sp.add_argument("--task-id", required=True, help="任务ID")
    sp.set_defaults(func=cmd_audit_task)
    
    # generate-report
    sp = sub.add_parser("generate-report", help="生成审计报告")
    sp.set_defaults(func=cmd_generate_report)
    
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
