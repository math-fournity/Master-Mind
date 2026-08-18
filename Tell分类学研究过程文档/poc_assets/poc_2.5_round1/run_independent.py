#!/usr/bin/env python3
"""
POC-2.5 独立批量执行脚本
不使用solver_harness，避免与另一个AI冲突。
用独立tmux session + devin -p --export + trajectory_monitor.py。

数据采集：
1. --export → conversation.json（content + tool_calls，ATIF格式，不含thinking）
2. trajectory_monitor.py → trajectory.jsonl（从共享sessions.db提取，含thinking）
"""
import subprocess
import json
import os
import time
import sys
from pathlib import Path
from datetime import datetime

PROBLEMS_DIR = "/tmp/poc2.5/problems"
WORK_BASE = "/tmp/poc2.5/workdirs"
TRAJ_BASE = "/tmp/poc2.5/trajectories"
os.makedirs(WORK_BASE, exist_ok=True)
os.makedirs(TRAJ_BASE, exist_ok=True)

TRAJECTORY_MONITOR = "xishujuzhen/trajectory_monitor.py"
PYTHON = ".venv/bin/python3"

# 16个run的配置
RUNS = []
for cc_id in ["CC-101", "CC-103", "CC-104", "CC-105"]:
    for cond in ["bare", "vein", "vein_hint", "hint"]:
        exp_id = f"p25-{cc_id}-{cond}"
        RUNS.append({
            "cc_id": cc_id,
            "condition": cond,
            "problem_file": f"{PROBLEMS_DIR}/{cc_id}_{cond}.txt",
            "exp_id": exp_id,
            "work_dir": f"{WORK_BASE}/{exp_id}",
            "traj_dir": f"{TRAJ_BASE}/{exp_id}",
        })

def launch_run(run_config):
    """启动单个run：tmux session + devin -p + trajectory_monitor."""
    exp_id = run_config["exp_id"]
    work_dir = run_config["work_dir"]
    traj_dir = run_config["traj_dir"]
    problem_file = run_config["problem_file"]
    
    os.makedirs(work_dir, exist_ok=True)
    os.makedirs(traj_dir, exist_ok=True)
    os.makedirs(f"{traj_dir}/exports", exist_ok=True)
    
    export_path = f"{traj_dir}/exports/conversation.json"
    traj_jsonl = f"{traj_dir}/trajectory.jsonl"
    
    # tmux session名（用下划线避免点号问题）
    tmux_name = f"p25-{exp_id}"
    dbmon_name = f"p25-dbmon-{exp_id}"
    
    # 1. 启动trajectory_monitor（从sessions.db提取thinking）
    dbmon_cmd = f"{PYTHON} {TRAJECTORY_MONITOR} --work-dir {work_dir} --interval 5 --max-wait 3600 -o {traj_jsonl}"
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", dbmon_name, dbmon_cmd],
        capture_output=True
    )
    
    # 2. 复制problem文件到work_dir（devin --prompt-file 从work_dir读）
    import shutil
    shutil.copy(problem_file, f"{work_dir}/problem.txt")
    
    # 3. 启动devin -p（无头模式 + --export，不走mitmproxy）
    devin_cmd = (
        f"cd {work_dir} && "
        f"devin --prompt-file {work_dir}/problem.txt "
        f"--model glm-5-2 "
        f"--respect-workspace-trust false "
        f"--permission-mode dangerous "
        f"--export {export_path}; "
        f"echo DEVIN_CLI_EXITED code=$?; "
        f"sleep 30"
    )
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", tmux_name, devin_cmd],
        capture_output=True
    )
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Launched {exp_id}")
    print(f"  tmux: {tmux_name}")
    print(f"  dbmon: {dbmon_name}")
    print(f"  work_dir: {work_dir}")
    print(f"  export: {export_path}")
    print(f"  trajectory: {traj_jsonl}")
    
    return {
        "exp_id": exp_id,
        "tmux_name": tmux_name,
        "dbmon_name": dbmon_name,
        "work_dir": work_dir,
        "traj_dir": traj_dir,
        "export_path": export_path,
        "traj_jsonl": traj_jsonl,
        "start_time": time.time(),
    }

def check_run_done(run_info):
    """检查run是否完成（devin进程退出）。"""
    tmux_name = run_info["tmux_name"]
    result = subprocess.run(
        ["tmux", "list-sessions"],
        capture_output=True, text=True
    )
    # 如果tmux session还在，说明devin还在运行（或sleep 30阶段）
    # 检查是否有DEVIN_CLI_EXITED
    return tmux_name not in result.stdout

def wait_all_runs(run_infos, max_wait=3600):
    """等待所有run完成。"""
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Waiting for {len(run_infos)} runs to complete...")
    
    start = time.time()
    while time.time() - start < max_wait:
        pending = []
        for ri in run_infos:
            if not check_run_done(ri):
                elapsed = time.time() - ri["start_time"]
                # 检查export和trajectory
                export_exists = os.path.exists(ri["export_path"])
                traj_lines = 0
                if os.path.exists(ri["traj_jsonl"]):
                    with open(ri["traj_jsonl"]) as f:
                        traj_lines = sum(1 for _ in f)
                if elapsed > 60:  # 只显示运行超过1分钟的
                    print(f"  {ri['exp_id']}: running {elapsed:.0f}s, export={export_exists}, traj_lines={traj_lines}")
                pending.append(ri)
            else:
                # run完成
                elapsed = time.time() - ri["start_time"]
                export_exists = os.path.exists(ri["export_path"])
                export_size = os.path.getsize(ri["export_path"]) if export_exists else 0
                traj_lines = 0
                if os.path.exists(ri["traj_jsonl"]):
                    with open(ri["traj_jsonl"]) as f:
                        traj_lines = sum(1 for _ in f)
                print(f"  ✓ {ri['exp_id']}: DONE {elapsed:.0f}s, export={export_size}B, traj_lines={traj_lines}")
        
        if not pending:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] All runs completed!")
            break
        
        time.sleep(30)
    else:
        print(f"\nTimeout: {len(pending)} runs still pending after {max_wait}s")
    
    # 停止所有dbmon sessions
    for ri in run_infos:
        subprocess.run(["tmux", "kill-session", "-t", ri["dbmon_name"]], capture_output=True)

def main():
    # 启动所有16个run（分批，每批4个避免资源竞争）
    run_infos = []
    
    BATCH_SIZE = 4
    for batch_start in range(0, len(RUNS), BATCH_SIZE):
        batch = RUNS[batch_start:batch_start+BATCH_SIZE]
        print(f"\n{'='*60}")
        print(f"Batch {batch_start//BATCH_SIZE + 1}: {len(batch)} runs")
        print(f"{'='*60}")
        
        for run_config in batch:
            ri = launch_run(run_config)
            run_infos.append(ri)
            time.sleep(2)  # 间隔2秒避免同时启动
        
        # 等待这批完成再启动下一批
        print(f"\nWaiting for batch to complete...")
        wait_all_runs(run_infos[batch_start:batch_start+BATCH_SIZE], max_wait=1200)
    
    # 生成汇总
    print(f"\n{'='*60}")
    print("Final Summary:")
    print(f"{'='*60}")
    for ri in run_infos:
        export_exists = os.path.exists(ri["export_path"])
        export_size = os.path.getsize(ri["export_path"]) if export_exists else 0
        traj_lines = 0
        if os.path.exists(ri["traj_jsonl"]):
            with open(ri["traj_jsonl"]) as f:
                traj_lines = sum(1 for _ in f)
        elapsed = time.time() - ri["start_time"]
        print(f"  {ri['exp_id']}: export={export_size}B, traj_lines={traj_lines}, elapsed={elapsed:.0f}s")
    
    # 保存汇总到JSON
    summary = []
    for ri in run_infos:
        export_exists = os.path.exists(ri["export_path"])
        export_size = os.path.getsize(ri["export_path"]) if export_exists else 0
        traj_lines = 0
        if os.path.exists(ri["traj_jsonl"]):
            with open(ri["traj_jsonl"]) as f:
                traj_lines = sum(1 for _ in f)
        summary.append({
            "exp_id": ri["exp_id"],
            "export_size": export_size,
            "traj_lines": traj_lines,
            "export_path": ri["export_path"],
            "traj_jsonl": ri["traj_jsonl"],
        })
    with open(f"{TRAJ_BASE}/batch_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to {TRAJ_BASE}/batch_summary.json")

if __name__ == "__main__":
    main()
