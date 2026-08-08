#!/usr/bin/env python3
"""
04工作线§2.6 A/B对照实验：验证检索机制是否帮助Solver突破卡点。

实验设计：
- A组（实验组）：有检索系统——DevinCliParserProvider实时解析 + retrieval + policy + hint注入
- B组（对照组）：无检索系统——Solver裸跑，不注入任何提示

实验题目：253号案例（矩条件极差题第二问）

对比指标：
1. 成功率：是否给出有效证明
2. 突破卡点：A组在收到提示后是否突破卡点
3. 效率：完成时间
4. 提示质量：提示是否引导AI思考（而非替AI做题）

用法：
  # 跑A组（有检索系统）
  .venv/bin/python3 scripts/ab_experiment.py --group A --exp-id ab-253-A

  # 跑B组（无检索系统）
  .venv/bin/python3 scripts/ab_experiment.py --group B --exp-id ab-253-B

  # 跑完整A/B对照
  .venv/bin/python3 scripts/ab_experiment.py --both --exp-id ab-253

前提条件：
  - mitmproxy已启动（solver-harness mitm start）
  - .env已source（ARANGO_DB=xishujuzhen_math_glm52）
  - parser工作目录存在（/data/math-agent-glm5.2-parser-1/）
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from xishujuzhen.research_runtime.parser.test_data.case_253 import PROBLEM_TEXT
from xishujuzhen.research_runtime.parser.models import SixTuple, TurnRecord
from xishujuzhen.research_runtime.parser.parser import MathParser
from xishujuzhen.research_runtime.parser.llm_parser import LLMParser
from xishujuzhen.research_runtime.hgraph.case_253_rules import create_case_253_graph
from xishujuzhen.research_runtime.realtime.pipeline import RealtimePipeline
from xishujuzhen.research_runtime.realtime.devin_cli_parser import DevinCliParserProvider
from xishujuzhen.research_runtime.retrieval import RetrievalPipeline
from xishujuzhen.research_runtime.policy.constrained_optimizer import ConstrainedPolicy
from xishujuzhen.research_runtime.budget import BudgetManager, BudgetType


SOLVER_HARNESS = REPO_ROOT / "xishujuzhen" / "solver_harness" / "solver_harness.py"
TRAJECTORY_BASE = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")


def write_problem_file(exp_id: str, problem_text: str) -> str:
    """写problem.txt到临时文件。"""
    problem_file = f"/tmp/{exp_id}_problem.txt"
    with open(problem_file, "w") as f:
        f.write(
            f"你是数学大师。请解答以下数学题。\n\n"
            f"题目：\n{problem_text}\n\n"
            f"要求：\n"
            f"1. 给出完整的解答过程\n"
            f"2. 数学公式用LaTeX\n"
            f"3. 如果你不知道某个知识，明确说\"我不知道[X]\"\n"
        )
    return problem_file


def launch_solver(exp_id: str, problem_file: str, model: str = "glm-5-2") -> dict:
    """用solver-harness启动真实Solver（--interactive模式）。"""
    cmd = [
        "python3", str(SOLVER_HARNESS),
        "launch",
        "--exp-id", exp_id,
        "--problem-file", problem_file,
        "--model", model,
        "--interactive",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR: solver-harness launch failed: {result.stderr}")
        return {}

    # 解析session_info
    session_info_path = TRAJECTORY_BASE / exp_id / "session_info.json"
    if session_info_path.exists():
        with open(session_info_path) as f:
            return json.load(f)
    return {}


def run_group_a(exp_id: str, model: str, max_time: int):
    """
    A组：有检索系统。

    流程：
    1. solver-harness启动Solver（--interactive）
    2. RealtimePipeline用DevinCliParserProvider实时解析
    3. 检测到卡点时自动检索+选择提示+注入
    """
    print("\n" + "=" * 60)
    print("A组：有检索系统（实时解析+检索+提示注入）")
    print("=" * 60)

    # 1. 启动Solver
    print(f"\n[A.1] 启动Solver（exp_id={exp_id}）...")
    problem_file = write_problem_file(exp_id, PROBLEM_TEXT)
    session_info = launch_solver(exp_id, problem_file, model)
    if not session_info:
        return {"error": "solver launch failed"}
    session_id = session_info.get("devin_session_id", "")
    tmux_session = f"harness-{exp_id}"
    print(f"  session_id: {session_id}")
    print(f"  tmux_session: {tmux_session}")

    # 2. 构建pipeline（用DevinCliParserProvider）
    print(f"\n[A.2] 构建RealtimePipeline（DevinCliParserProvider）...")
    hgraph = create_case_253_graph()

    provider = DevinCliParserProvider(timeout=180, max_retries=1)
    llm_parser = LLMParser(mock_response_provider=provider)
    math_parser = MathParser(llm_parser=llm_parser)

    budget = BudgetManager()
    budget.set_budget(BudgetType.HINT, 10)

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

    print(f"  parser work_dir: {provider.work_dir}")
    print(f"  max_time: {max_time}s")

    # 3. 运行pipeline
    print(f"\n[A.3] 运行RealtimePipeline（监控Solver + 自动注入提示）...")
    start_time = time.time()
    results = pipeline.run(max_rounds=10, max_time=max_time, auto_inject=True)
    elapsed = time.time() - start_time

    # 4. 输出结果
    print(f"\n[A.4] A组完成（{elapsed:.0f}s）")
    print(f"  处理轮数: {len(results)}")
    hints_injected = sum(1 for r in results if r.injected)
    print(f"  提示注入次数: {hints_injected}")

    for i, r in enumerate(results):
        selected = r.selection_result.selected_rule.rule_id if r.selection_result and r.selection_result.selected_rule else "N/A"
        print(f"  Round {i}: selected={selected}, injected={r.injected}, error={r.error or 'none'}")

    # 5. 保存结果
    result_data = {
        "group": "A",
        "exp_id": exp_id,
        "session_id": session_id,
        "elapsed_seconds": elapsed,
        "total_rounds": len(results),
        "hints_injected": hints_injected,
        "rounds": [
            {
                "round_index": r.round_index,
                "selected_rule": r.selection_result.selected_rule.rule_id if r.selection_result and r.selection_result.selected_rule else None,
                "selected_q": r.selected_q,
                "injected": r.injected,
                "error": r.error,
            }
            for r in results
        ],
    }

    result_path = TRAJECTORY_BASE / exp_id / "ab_result.json"
    with open(result_path, "w") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    print(f"  结果保存到: {result_path}")

    return result_data


def run_group_b(exp_id: str, model: str, max_time: int):
    """
    B组：无检索系统（Solver裸跑）。

    流程：
    1. solver-harness启动Solver（--interactive）
    2. 不做任何解析、检索、注入
    3. 等待Solver自然完成或超时
    4. 记录trajectory和最终结果
    """
    print("\n" + "=" * 60)
    print("B组：无检索系统（Solver裸跑）")
    print("=" * 60)

    # 1. 启动Solver
    print(f"\n[B.1] 启动Solver（exp_id={exp_id}）...")
    problem_file = write_problem_file(exp_id, PROBLEM_TEXT)
    session_info = launch_solver(exp_id, problem_file, model)
    if not session_info:
        return {"error": "solver launch failed"}
    session_id = session_info.get("devin_session_id", "")
    tmux_session = f"harness-{exp_id}"
    print(f"  session_id: {session_id}")
    print(f"  tmux_session: {tmux_session}")

    # 2. 等待Solver完成（不做任何干预）
    print(f"\n[B.2] 等待Solver裸跑完成（max_time={max_time}s）...")
    print(f"  观察: tmux attach -t {tmux_session}")

    start_time = time.time()
    while time.time() - start_time < max_time:
        # 检查tmux session是否还在
        check = subprocess.run(
            ["tmux", "has-session", "-t", tmux_session],
            capture_output=True
        )
        if check.returncode != 0:
            print(f"  Solver session已结束（{time.time()-start_time:.0f}s）")
            break
        time.sleep(30)
        print(f"  [{time.time()-start_time:.0f}s] Solver仍在运行...")

    elapsed = time.time() - start_time

    # 3. 输出结果
    print(f"\n[B.3] B组完成（{elapsed:.0f}s）")

    # 4. 保存结果
    result_data = {
        "group": "B",
        "exp_id": exp_id,
        "session_id": session_id,
        "elapsed_seconds": elapsed,
        "total_rounds": 0,
        "hints_injected": 0,
        "note": "B组无干预，Solver裸跑",
    }

    result_path = TRAJECTORY_BASE / exp_id / "ab_result.json"
    with open(result_path, "w") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    print(f"  结果保存到: {result_path}")

    return result_data


def compare_results(a_result: dict, b_result: dict):
    """对比A/B组结果。"""
    print("\n" + "=" * 60)
    print("A/B对照结果")
    print("=" * 60)

    print(f"\n{'指标':<20} {'A组（有检索）':<20} {'B组（无检索）':<20}")
    print("-" * 60)
    print(f"{'实验ID':<20} {a_result.get('exp_id',''):<20} {b_result.get('exp_id',''):<20}")
    print(f"{'运行时间(秒)':<20} {a_result.get('elapsed_seconds',0):<20.0f} {b_result.get('elapsed_seconds',0):<20.0f}")
    print(f"{'处理轮数':<20} {a_result.get('total_rounds',0):<20} {b_result.get('total_rounds',0):<20}")
    print(f"{'提示注入次数':<20} {a_result.get('hints_injected',0):<20} {b_result.get('hints_injected',0):<20}")

    # 详细分析需要人工检查trajectory
    print(f"\n详细分析：")
    print(f"  A组trajectory: {TRAJECTORY_BASE / a_result.get('exp_id','')}")
    print(f"  B组trajectory: {TRAJECTORY_BASE / b_result.get('exp_id','')}")
    print(f"  需人工检查：")
    print(f"    1. A组在收到提示后是否突破卡点？")
    print(f"    2. B组是否卡住无法突破？")
    print(f"    3. A组最终是否给出有效证明？")
    print(f"    4. B组最终是否给出有效证明？")


def main():
    parser = argparse.ArgumentParser(description="04工作线§2.6 A/B对照实验")
    parser.add_argument("--group", choices=["A", "B"], help="只跑A组或B组")
    parser.add_argument("--both", action="store_true", help="跑完整A/B对照")
    parser.add_argument("--exp-id", default="ab-253", help="实验ID前缀")
    parser.add_argument("--model", default="glm-5-2", help="模型名")
    parser.add_argument("--max-time", type=int, default=600, help="每组最大运行时间（秒）")
    args = parser.parse_args()

    print("=" * 60)
    print("04工作线§2.6 A/B对照实验")
    print("题目：253号案例（矩条件极差题第二问）")
    print(f"模型：{args.model}")
    print(f"每组最大时间：{args.max_time}s")
    print("=" * 60)

    if args.both:
        # 跑完整A/B对照
        a_exp_id = f"{args.exp_id}-A"
        b_exp_id = f"{args.exp_id}-B"

        a_result = run_group_a(a_exp_id, args.model, args.max_time)

        # 等待A组Solver完全停止后再启动B组
        print("\n等待10秒后启动B组...")
        time.sleep(10)

        b_result = run_group_b(b_exp_id, args.model, args.max_time)

        compare_results(a_result, b_result)

    elif args.group == "A":
        run_group_a(args.exp_id, args.model, args.max_time)

    elif args.group == "B":
        run_group_b(args.exp_id, args.model, args.max_time)

    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
