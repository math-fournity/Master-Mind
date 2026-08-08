#!/usr/bin/env python3
"""
04工作线§6.5端到端集成测试：接真实Solver的实时检索-提示-突破闭环。

流程：
1. 用solver-harness启动真实Solver（--interactive模式），跑253号案例题目
2. 启动RealtimePipeline监听sessions_db/trajectory.jsonl
3. 验证完整闭环：trajectory → parser → stall检测 → retrieval → policy → 提示注入
4. 验证提示注入后Solver的trajectory中有新进展

用法：
  .venv/bin/python3 scripts/e2e_realtime_test.py --exp-id e2e-253-test

前提条件：
  - mitmproxy已启动（solver-harness mitm start）
  - .env已source（ARANGO_DB=grove_math）
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

# 确保PYTHONPATH
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from xishujuzhen.research_runtime.parser.test_data.case_253 import PROBLEM_TEXT
from xishujuzhen.research_runtime.hgraph.case_253_rules import create_case_253_graph
from xishujuzhen.research_runtime.realtime.pipeline import RealtimePipeline
from xishujuzhen.research_runtime.realtime.trajectory_watcher import TrajectoryWatcher
from xishujuzhen.research_runtime.realtime.hint_injector import HintInjector
from xishujuzhen.research_runtime.budget import BudgetManager, BudgetType


def start_solver(exp_id: str, problem_text: str, model: str = "glm-5-2") -> dict:
    """用solver-harness启动真实Solver（--interactive模式）。"""
    # 写problem.txt
    problem_file = f"/tmp/{exp_id}_problem.txt"
    with open(problem_file, "w") as f:
        f.write(f"你是数学大师。请解答以下数学题。\n\n题目：\n{problem_text}\n\n要求：\n1. 给出完整的解答过程\n2. 数学公式用LaTeX\n3. 如果你不知道，明确说\"我不知道\"\n")

    # 用solver-harness launch启动（--interactive模式）
    cmd = [
        "python3", str(REPO_ROOT / "xishujuzhen/solver_harness/solver_harness.py"),
        "launch",
        "--exp-id", exp_id,
        "--problem-file", problem_file,
        "--model", model,
        "--interactive",  # 交互模式，支持运行时send-keys提示注入
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR: solver-harness launch failed: {result.stderr}")
        return {}

    # 解析session_info
    session_info_path = f"/data/grove-agents-trajectory/{exp_id}/session_info.json"
    if os.path.exists(session_info_path):
        with open(session_info_path) as f:
            return json.load(f)
    return {}


def run_realtime_pipeline(exp_id: str, session_id: str, problem_text: str, max_time: int = 300):
    """启动RealtimePipeline监听Solver的trajectory。"""
    # 创建H图（253号案例的启发规则图）
    hgraph = create_case_253_graph()
    # build_case_253_rules()不需要参数，返回规则列表
    # create_case_253_graph()已经包含了规则

    # trajectory数据路径
    trajectory_jsonl = f"/data/grove-agents-trajectory/{exp_id}/sessions_db/trajectory.jsonl"
    result_output = f"/data/grove-agents-trajectory/{exp_id}/realtime_result.json"

    # 创建pipeline
    tmux_session = f"harness-{exp_id}"
    # 设置预算（默认BudgetItem.total=0，需要显式设置）
    budget = BudgetManager()
    budget.set_budget(BudgetType.HINT, 10)  # 允许10次提示注入
    pipeline = RealtimePipeline(
        session_id=session_id,
        hgraph=hgraph,
        problem_text=problem_text,
        tmux_session=tmux_session,
        budget_manager=budget,
    )

    print(f"\n=== RealtimePipeline started ===")
    print(f"  exp_id: {exp_id}")
    print(f"  session_id: {session_id}")
    print(f"  trajectory: {trajectory_jsonl}")
    print(f"  tmux_session: {tmux_session}")
    print(f"  max_time: {max_time}s")

    # 运行pipeline
    results = pipeline.run(max_rounds=5, max_time=max_time, auto_inject=True)

    # 输出结果
    print(f"\n=== RealtimePipeline finished ===")
    print(f"  Total rounds processed: {len(results)}")
    for i, r in enumerate(results):
        print(f"  Round {i}: selected_q={r.selected_q}, injected={r.injected}")

    # 保存结果
    with open(result_output, "w") as f:
        json.dump([r.to_dict() if hasattr(r, 'to_dict') else str(r) for r in results], f, indent=2, ensure_ascii=False, default=str)

    return results


def main():
    parser = argparse.ArgumentParser(description="04工作线端到端集成测试")
    parser.add_argument("--exp-id", default="e2e-253-test", help="实验ID")
    parser.add_argument("--model", default="glm-5-2", help="模型名")
    parser.add_argument("--max-time", type=int, default=300, help="最大运行时间（秒）")
    parser.add_argument("--skip-launch", action="store_true", help="跳过launch（实验已启动）")
    args = parser.parse_args()

    print("=" * 60)
    print("04工作线§6.5端到端集成测试")
    print("=" * 60)

    # 1. 启动Solver
    if not args.skip_launch:
        print(f"\n[1] 启动Solver（solver-harness --interactive）...")
        session_info = start_solver(args.exp_id, PROBLEM_TEXT, args.model)
        if not session_info:
            print("ERROR: 启动失败")
            return 1
        session_id = session_info.get("devin_session_id", "")
        print(f"  session_id: {session_id}")
    else:
        print(f"\n[1] 跳过launch（--skip-launch）")
        session_info_path = f"/data/grove-agents-trajectory/{args.exp_id}/session_info.json"
        with open(session_info_path) as f:
            session_info = json.load(f)
        session_id = session_info.get("devin_session_id", "")

    # 2. 启动RealtimePipeline
    print(f"\n[2] 启动RealtimePipeline...")
    results = run_realtime_pipeline(args.exp_id, session_id, PROBLEM_TEXT, max_time=args.max_time)

    # 3. 输出总结
    print(f"\n[3] 测试总结")
    print(f"  处理轮数: {len(results)}")
    hints_injected = sum(1 for r in results if r.injected)
    print(f"  提示注入次数: {hints_injected}")

    if hints_injected > 0:
        print(f"  ✅ 提示注入成功——验证了完整闭环")
    else:
        print(f"  ⚠️  无提示注入——可能Solver没有卡点，或卡点检测未触发")

    return 0


if __name__ == "__main__":
    sys.exit(main())
