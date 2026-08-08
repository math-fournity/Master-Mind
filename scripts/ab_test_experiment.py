#!/usr/bin/env python3
"""
04工作线§6.6 A/B对照实验：检索机制对Solver突破卡点的效果验证。

方案见 dev-docs/265-v0-2026-08-08-AB对照实验方案-检索机制对Solver突破卡点的效果验证.md

A组（实验组）：Solver + RealtimePipeline（实时解析+检索+提示注入）
B组（对照组）：Solver裸跑，无任何提示

用法：
  # 跑B组（对照组）3次
  .venv/bin/python3 scripts/ab_test_experiment.py --group B --runs 3

  # 跑A组（实验组）3次
  .venv/bin/python3 scripts/ab_test_experiment.py --group A --runs 3

  # 跑两组各3次
  .venv/bin/python3 scripts/ab_test_experiment.py --group both --runs 3

  # 分析结果
  .venv/bin/python3 scripts/ab_test_experiment.py --analyze

前提条件：
  - mitmproxy已启动（solver-harness mitm start）
  - .env已source（ARANGO_DB=xishujuzhen_math_glm52）
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

# 确保PYTHONPATH
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from xishujuzhen.research_runtime.parser.test_data.case_253 import PROBLEM_TEXT
from xishujuzhen.research_runtime.hgraph import create_case_253_graph, build_case_253_rules
from xishujuzhen.research_runtime.realtime.pipeline import RealtimePipeline
from xishujuzhen.research_runtime.realtime.devin_cli_parser import DevinCliParserProvider
from xishujuzhen.research_runtime.parser.parser import MathParser
from xishujuzhen.research_runtime.parser.llm_parser import LLMParser
from xishujuzhen.research_runtime.retrieval import RetrievalPipeline
from xishujuzhen.research_runtime.policy.constrained_optimizer import ConstrainedPolicy
from xishujuzhen.research_runtime.budget import BudgetManager, BudgetType

# 实验参数
MAX_TIME = 600        # 每次实验最大时间（秒）
MAX_ROUNDS = 10       # A组最大提示注入轮次
HINT_BUDGET = 10      # A组最大提示注入次数
MODEL = "glm-5-2"
SOLVER_HARNESS = str(REPO_ROOT / "xishujuzhen/solver_harness/solver_harness.py")
TRAJECTORY_BASE = "/data/math-agent-glm5.2-tmux-agents-trajectory"


def write_problem_file(exp_id: str) -> str:
    """写problem.txt，返回路径。"""
    problem_file = f"/tmp/{exp_id}_problem.txt"
    with open(problem_file, "w") as f:
        f.write(
            f"你是数学大师。请解答以下数学题。\n\n"
            f"题目：\n{PROBLEM_TEXT}\n\n"
            f"要求：\n"
            f"1. 给出完整的解答过程\n"
            f"2. 数学公式用LaTeX\n"
            f"3. 如果你不知道，明确说\"我不知道\"\n"
        )
    return problem_file


def launch_solver(exp_id: str) -> dict:
    """用solver-harness启动Solver（--interactive模式，--no-mitm避免连接问题）。"""
    problem_file = write_problem_file(exp_id)
    cmd = [
        "python3", SOLVER_HARNESS, "launch",
        "--exp-id", exp_id,
        "--problem-file", problem_file,
        "--model", MODEL,
        "--interactive",
        "--no-mitm",  # mitmproxy会导致交互模式连接失败，A/B实验不需要MITM trajectory
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR: launch failed: {result.stderr}")
        return {}

    session_info_path = f"{TRAJECTORY_BASE}/{exp_id}/session_info.json"
    if os.path.exists(session_info_path):
        with open(session_info_path) as f:
            return json.load(f)
    return {}


def stop_solver(exp_id: str):
    """停止solver-harness实验（自动decode-all）。"""
    cmd = ["python3", SOLVER_HARNESS, "stop", "--exp-id", exp_id]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)


def run_b_group(run_id: int) -> dict:
    """B组（对照组）：Solver裸跑，无RealtimePipeline。"""
    exp_id = f"ab-test-b-253-run{run_id}"
    print(f"\n{'='*60}")
    print(f"B组 run{run_id} ({exp_id})")
    print(f"{'='*60}")

    # 1. 启动Solver
    print(f"[1] 启动Solver（裸跑，无提示）...")
    session_info = launch_solver(exp_id)
    if not session_info:
        return {"exp_id": exp_id, "status": "launch_failed"}
    session_id = session_info.get("devin_session_id", "")
    print(f"  session_id: {session_id}")

    # 2. 等待MAX_TIME（不启动RealtimePipeline）
    print(f"[2] 等待{MAX_TIME}秒（Solver裸跑中）...")
    for remaining in range(MAX_TIME, 0, -60):
        print(f"  剩余 {remaining}秒...")
        time.sleep(min(60, remaining))

    # 3. 停止Solver
    print(f"[3] 停止Solver...")
    stop_solver(exp_id)

    # 4. 收集结果
    result = collect_result(exp_id, group="B", run_id=run_id, session_id=session_id)
    print(f"[4] 结果: status={result.get('final_status')}, trajectory_nodes={result.get('trajectory_node_count')}")
    return result


def run_a_group(run_id: int) -> dict:
    """A组（实验组）：Solver + RealtimePipeline。"""
    exp_id = f"ab-test-a-253-run{run_id}"
    print(f"\n{'='*60}")
    print(f"A组 run{run_id} ({exp_id})")
    print(f"{'='*60}")

    # 1. 启动Solver
    print(f"[1] 启动Solver（--interactive模式）...")
    session_info = launch_solver(exp_id)
    if not session_info:
        return {"exp_id": exp_id, "status": "launch_failed"}
    session_id = session_info.get("devin_session_id", "")
    print(f"  session_id: {session_id}")

    # 2. 启动RealtimePipeline
    print(f"[2] 启动RealtimePipeline（DevinCliParserProvider + 253号H图）...")
    results = run_pipeline(exp_id, session_id)

    # 3. 停止Solver
    print(f"[3] 停止Solver...")
    stop_solver(exp_id)

    # 4. 收集结果
    result = collect_result(exp_id, group="A", run_id=run_id, session_id=session_id)
    result["pipeline_results"] = results
    result["hints_injected"] = sum(1 for r in results if hasattr(r, "injected") and r.injected)
    print(f"[4] 结果: status={result.get('final_status')}, hints_injected={result['hints_injected']}")
    return result


def run_pipeline(exp_id: str, session_id: str) -> list:
    """启动RealtimePipeline，返回结果列表。"""
    # 构建H图
    hgraph = create_case_253_graph()
    for rule in build_case_253_rules():
        hgraph.add_rule(rule)

    # 构建DevinCliParserProvider
    provider = DevinCliParserProvider(timeout=180, max_retries=1)
    llm_parser = LLMParser(mock_response_provider=provider)
    math_parser = MathParser(llm_parser=llm_parser)

    # 构建pipeline
    budget = BudgetManager()
    budget.set_budget(BudgetType.HINT, HINT_BUDGET)
    tmux_session = f"harness-{exp_id}"
    pipeline = RealtimePipeline(
        session_id=session_id,
        hgraph=hgraph,
        problem_text=PROBLEM_TEXT,
        math_parser=math_parser,
        retrieval_pipeline=RetrievalPipeline(),
        policy=ConstrainedPolicy(),
        budget_manager=budget,
        tmux_session=tmux_session,
    )

    print(f"  pipeline启动: tmux={tmux_session}, max_time={MAX_TIME}s, max_rounds={MAX_ROUNDS}")

    # 运行
    results = pipeline.run(max_rounds=MAX_ROUNDS, max_time=MAX_TIME, auto_inject=True)

    # 保存pipeline结果
    result_path = f"{TRAJECTORY_BASE}/{exp_id}/realtime_result.json"
    with open(result_path, "w") as f:
        json.dump(
            [str(r) for r in results],
            f, indent=2, ensure_ascii=False, default=str
        )

    return results


def collect_result(exp_id: str, group: str, run_id: int, session_id: str) -> dict:
    """收集实验结果。"""
    result = {
        "exp_id": exp_id,
        "group": group,
        "run_id": run_id,
        "session_id": session_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # 读trajectory.jsonl（sessions_db）
    traj_path = f"{TRAJECTORY_BASE}/{exp_id}/sessions_db/trajectory.jsonl"
    nodes = []
    if os.path.exists(traj_path):
        with open(traj_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        nodes.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass

    result["trajectory_node_count"] = len(nodes)
    result["trajectory_nodes"] = nodes

    # 读mitm trajectory（如果已decode）
    mitm_path = f"{TRAJECTORY_BASE}/{exp_id}/mitm/trajectory.jsonl"
    if os.path.exists(mitm_path):
        result["mitm_available"] = True
    else:
        result["mitm_available"] = False

    # 读exports
    export_path = f"{TRAJECTORY_BASE}/{exp_id}/exports/conversation.json"
    if os.path.exists(export_path):
        with open(export_path) as f:
            export_data = json.load(f)
        result["export_available"] = True
        # 提取最终输出
        if isinstance(export_data, dict):
            messages = export_data.get("messages", [])
            if messages:
                last_msg = messages[-1]
                result["final_output"] = str(last_msg.get("content", ""))[:500]
    else:
        result["export_available"] = False

    # 判定最终状态
    result["final_status"] = judge_status(nodes, result.get("final_output", ""))

    return result


def judge_status(nodes: list, final_output: str) -> str:
    """判定Solver的最终状态。"""
    if not nodes:
        return "no_data"

    # 检查是否有"我不知道"或stuck关键词
    all_content = " ".join(n.get("content", "") + n.get("thinking", "") for n in nodes if n.get("role") == "assistant")
    stuck_keywords = ["我不知道", "I don't know", "无法", "不会", "stuck"]
    if any(kw in all_content for kw in stuck_keywords) and len(all_content) < 500:
        return "stuck"

    # 检查是否有证明完成标记
    completion_keywords = ["证毕", "QED", "证明完毕", "证完", "因此原命题得证"]
    if any(kw in all_content for kw in completion_keywords):
        return "completed"

    # 检查输出长度
    if len(all_content) > 1000:
        return "substantial_progress"

    if len(all_content) > 200:
        return "some_progress"

    return "stuck"


def run_experiments(group: str, runs: int) -> list:
    """跑指定组的实验。"""
    all_results = []

    if group in ("B", "both"):
        print(f"\n{'#'*60}")
        print(f"# B组实验（对照组·裸跑）")
        print(f"{'#'*60}")
        for i in range(1, runs + 1):
            result = run_b_group(i)
            all_results.append(result)
            # 保存中间结果
            save_results(all_results, "B")

    if group in ("A", "both"):
        print(f"\n{'#'*60}")
        print(f"# A组实验（实验组·有检索系统）")
        print(f"{'#'*60}")
        for i in range(1, runs + 1):
            result = run_a_group(i)
            all_results.append(result)
            # 保存中间结果
            save_results(all_results, "A")

    return all_results


def save_results(results: list, group: str):
    """保存结果到文件。"""
    output_path = str(REPO_ROOT / f"runs/ab_test_253_{group.lower()}_results.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
    print(f"  结果已保存: {output_path}")


def analyze_results():
    """分析A/B对照结果。"""
    print(f"\n{'='*60}")
    print(f"A/B对照实验结果分析")
    print(f"{'='*60}")

    b_path = str(REPO_ROOT / "runs/ab_test_253_b_results.json")
    a_path = str(REPO_ROOT / "runs/ab_test_253_a_results.json")

    b_results = []
    a_results = []
    if os.path.exists(b_path):
        with open(b_path) as f:
            b_results = json.load(f)
    if os.path.exists(a_path):
        with open(a_path) as f:
            a_results = json.load(f)

    print(f"\n--- B组（对照组·裸跑）---")
    print(f"  实验次数: {len(b_results)}")
    for r in b_results:
        print(f"  run{r.get('run_id')}: status={r.get('final_status')}, "
              f"nodes={r.get('trajectory_node_count')}")

    print(f"\n--- A组（实验组·有检索系统）---")
    print(f"  实验次数: {len(a_results)}")
    for r in a_results:
        hints = r.get("hints_injected", 0)
        print(f"  run{r.get('run_id')}: status={r.get('final_status')}, "
              f"nodes={r.get('trajectory_node_count')}, hints={hints}")

    # 汇总
    b_stuck = sum(1 for r in b_results if r.get("final_status") == "stuck")
    b_completed = sum(1 for r in b_results if r.get("final_status") == "completed")
    a_stuck = sum(1 for r in a_results if r.get("final_status") == "stuck")
    a_completed = sum(1 for r in a_results if r.get("final_status") == "completed")
    a_breakthrough = sum(1 for r in a_results if r.get("hints_injected", 0) > 0 and r.get("final_status") != "stuck")

    print(f"\n--- 汇总 ---")
    print(f"  B组: stuck={b_stuck}/{len(b_results)}, completed={b_completed}/{len(b_results)}")
    print(f"  A组: stuck={a_stuck}/{len(a_results)}, completed={a_completed}/{len(a_results)}")
    print(f"  A组突破率: {a_breakthrough}/{len(a_results)}")

    # 判定
    if len(a_results) > 0 and len(b_results) > 0:
        if a_completed > 0 and b_completed == 0:
            print(f"\n  ✅ 检索机制有效——A组有做对的，B组没有")
        elif a_stuck < b_stuck:
            print(f"\n  ✅ 检索机制有一定效果——A组stuck少于B组")
        elif a_stuck == b_stuck:
            print(f"\n  ⚠️  检索机制效果不明显——A/B组stuck数量相同")
        else:
            print(f"\n  ❌ 检索机制无效——A组stuck不少于B组")

    # 生成报告
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "b_group": {
            "total": len(b_results),
            "stuck": b_stuck,
            "completed": b_completed,
            "results": b_results,
        },
        "a_group": {
            "total": len(a_results),
            "stuck": a_stuck,
            "completed": a_completed,
            "breakthrough": a_breakthrough,
            "results": a_results,
        },
    }
    report_path = str(REPO_ROOT / "runs/ab_test_253_report.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n  报告已保存: {report_path}")


def main():
    parser = argparse.ArgumentParser(description="04工作线§6.6 A/B对照实验")
    parser.add_argument("--group", choices=["A", "B", "both"], default="both", help="跑哪组")
    parser.add_argument("--runs", type=int, default=3, help="每组重复次数")
    parser.add_argument("--analyze", action="store_true", help="只分析结果，不跑实验")
    args = parser.parse_args()

    if args.analyze:
        analyze_results()
        return 0

    # A/B实验用--no-mitm，不需要启动mitmproxy
    #（mitmproxy会导致交互模式devin cli连接失败）

    # 跑实验
    results = run_experiments(args.group, args.runs)

    # 自动分析
    analyze_results()

    return 0


if __name__ == "__main__":
    sys.exit(main())
