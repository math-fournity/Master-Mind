#!/usr/bin/env python3
"""
POC-2.5 批量执行脚本
逐个运行16个条件（4题×4条件），每个run通过devin -p直接执行。
--export保存对话（content+tool_calls），sessions.db自动保存thinking。
"""
import subprocess
import json
import os
import time
from pathlib import Path
from datetime import datetime

PROBLEMS_DIR = "/tmp/poc2.5/problems"
RESULTS_DIR = "/tmp/poc2.5/results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# 16个run的配置
RUNS = []
for cc_id in ["CC-101", "CC-103", "CC-104", "CC-105"]:
    for cond in ["bare", "vein", "vein_hint", "hint"]:
        RUNS.append({
            "cc_id": cc_id,
            "condition": cond,
            "problem_file": f"{PROBLEMS_DIR}/{cc_id}_{cond}.txt",
            "exp_id": f"poc2.5-{cc_id}-{cond}",
        })

def run_single(run_config):
    """运行单个run，返回结果字典。"""
    exp_id = run_config["exp_id"]
    problem_file = run_config["problem_file"]
    export_path = f"{RESULTS_DIR}/{exp_id}_export.json"
    log_path = f"{RESULTS_DIR}/{exp_id}_log.txt"
    
    print(f"\n{'='*60}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting: {exp_id}")
    print(f"  Problem file: {problem_file}")
    print(f"  Export: {export_path}")
    print(f"{'='*60}")
    
    start_time = time.time()
    
    # 构建devin命令
    # --prompt-file 加载题目文件
    # --export 保存对话到JSON
    # --permission-mode dangerous 允许工具调用
    # --respect-workspace-trust false 不需要信任确认
    cmd = [
        "devin",
        "--prompt-file", problem_file,
        "--model", "glm-5-2",
        "--respect-workspace-trust", "false",
        "--permission-mode", "dangerous",
        "--export", export_path,
    ]
    
    # 运行devin，捕获输出
    with open(log_path, "w") as logf:
        proc = subprocess.run(
            cmd,
            stdout=logf,
            stderr=subprocess.STDOUT,
            timeout=600,  # 10分钟超时
        )
    
    elapsed = time.time() - start_time
    
    # 检查export文件
    export_exists = os.path.exists(export_path)
    export_size = os.path.getsize(export_path) if export_exists else 0
    
    # 检查log中的PROOF COMPLETE
    with open(log_path, "r") as f:
        log_content = f.read()
    has_proof_complete = "### PROOF COMPLETE" in log_content
    has_answer_leak = "### ANSWER LEAK DETECTED" in log_content
    
    result = {
        "exp_id": exp_id,
        "cc_id": run_config["cc_id"],
        "condition": run_config["condition"],
        "elapsed_seconds": round(elapsed, 1),
        "exit_code": proc.returncode,
        "export_exists": export_exists,
        "export_size": export_size,
        "has_proof_complete": has_proof_complete,
        "has_answer_leak": has_answer_leak,
        "log_preview": log_content[-500:] if log_content else "",
    }
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Finished: {exp_id}")
    print(f"  Elapsed: {result['elapsed_seconds']}s")
    print(f"  Exit code: {result['exit_code']}")
    print(f"  Export: {export_exists} ({export_size} bytes)")
    print(f"  PROOF COMPLETE: {has_proof_complete}")
    print(f"  ANSWER LEAK: {has_answer_leak}")
    
    # 保存单个结果
    with open(f"{RESULTS_DIR}/{exp_id}_result.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    return result

def main():
    all_results = []
    
    # 逐个运行16个run
    for i, run_config in enumerate(RUNS):
        print(f"\n{'#'*60}")
        print(f"# Run {i+1}/{len(RUNS)}: {run_config['exp_id']}")
        print(f"{'#'*60}")
        
        try:
            result = run_single(run_config)
            all_results.append(result)
        except subprocess.TimeoutExpired:
            print(f"TIMEOUT: {run_config['exp_id']} exceeded 600s")
            all_results.append({
                "exp_id": run_config["exp_id"],
                "cc_id": run_config["cc_id"],
                "condition": run_config["condition"],
                "elapsed_seconds": 600,
                "exit_code": -1,
                "error": "timeout",
            })
        except Exception as e:
            print(f"ERROR: {run_config['exp_id']}: {e}")
            all_results.append({
                "exp_id": run_config["exp_id"],
                "cc_id": run_config["cc_id"],
                "condition": run_config["condition"],
                "error": str(e),
            })
    
    # 保存汇总结果
    with open(f"{RESULTS_DIR}/batch_summary.json", "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"Batch complete: {len(all_results)} runs")
    print(f"Results saved to: {RESULTS_DIR}/batch_summary.json")
    print(f"{'='*60}")
    
    # 打印汇总
    for r in all_results:
        status = "PROOF COMPLETE" if r.get("has_proof_complete") else "NO PROOF" if r.get("exit_code") == 0 else "ERROR"
        print(f"  {r['exp_id']}: {status} ({r.get('elapsed_seconds',0)}s)")

if __name__ == "__main__":
    main()
