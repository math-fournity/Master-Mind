#!/usr/bin/env python3
"""串行多AI树生长实验编排脚本（阶段2）。

流程：
  1. 在tree_store中创建problem + root_node
  2. 启动AI-1（给problem.txt，不给脉络）
  3. 等待AI-1终止
  4. 从AI-1的trajectory提取节点 → 写入tree_store
  5. 在AI-1的终点节点检索方向 → 选出Q
  6. 构造脉络文本
  7. 启动AI-2（给脉络+Q）
  8. 重复3-7，直到找到解答或达到max_ai_count

用法：
  PYTHONUNBUFFERED=1 .venv/bin/python3 scripts/serial_multi_ai.py \
    --problem-id case_253 \
    --max-ai 3 \
    --max-time-per-ai 600 \
    --model glm-5-2

前提条件：
  - mitmproxy已启动（solver-harness mitm start）
  - .env已source（ARANGO_DB=grove_math）
  - parser工作目录存在（/data/grove-parser-1/）
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

from xishujuzhen.research_runtime.tree_engine.tree_store import (
    TreeStore, TreeNode, TreeEdge, AIInstance,
)
from xishujuzhen.research_runtime.tree_engine.node_extractor import NodeExtractor
from xishujuzhen.research_runtime.tree_engine.path_constructor import PathConstructor
from xishujuzhen.research_runtime.tree_engine.termination_detector import TerminationDetector
from xishujuzhen.research_runtime.parser.test_data.case_253 import PROBLEM_TEXT
from xishujuzhen.research_runtime.hgraph.case_253_rules import create_case_253_graph
from xishujuzhen.research_runtime.retrieval import RetrievalPipeline
from xishujuzhen.research_runtime.policy.constrained_optimizer import (
    ConstrainedPolicy,
    MatchedRule as PolicyMatchedRule,
)
from xishujuzhen.research_runtime.realtime.pipeline import RealtimePipeline
from xishujuzhen.research_runtime.realtime.devin_cli_parser import DevinCliParserProvider
from xishujuzhen.research_runtime.parser.parser import MathParser
from xishujuzhen.research_runtime.parser.llm_parser import LLMParser
from xishujuzhen.research_runtime.realtime.trajectory_watcher import Round

SOLVER_HARNESS = REPO_ROOT / "xishujuzhen" / "solver_harness" / "solver_harness.py"
TRAJECTORY_BASE = Path("/data/grove-agents-trajectory")


def read_thinking_readable(exp_id: str) -> str:
    """读取mitmproxy流式截获的thinking_readable.txt。"""
    path = TRAJECTORY_BASE / exp_id / "mitm" / "thinking_readable.txt"
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def write_problem_file(exp_id: str, content: str) -> str:
    """写problem.txt到临时文件。"""
    problem_file = f"/tmp/{exp_id}_problem.txt"
    with open(problem_file, "w") as f:
        f.write(content)
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

    session_info_path = TRAJECTORY_BASE / exp_id / "session_info.json"
    if session_info_path.exists():
        with open(session_info_path) as f:
            return json.load(f)
    return {}


def stop_solver(exp_id: str):
    """停止Solver。"""
    subprocess.run(
        [".venv/bin/python3", str(SOLVER_HARNESS), "stop", "--exp-id", exp_id, "--no-decode"],
        capture_output=True, text=True, cwd=str(REPO_ROOT),
    )


def retrieve_directions(
    node: TreeNode,
    hgraph,
    problem_text: str,
) -> str:
    """
    在节点上检索方向，返回选中的提示Q。

    用RealtimePipeline的process_round做解析+检索+策略选择。
    """
    from xishujuzhen.research_runtime.budget import BudgetManager, BudgetType

    # 构建pipeline组件
    provider = DevinCliParserProvider(timeout=180, max_retries=1)
    llm_parser = LLMParser(mock_response_provider=provider)
    math_parser = MathParser(llm_parser=llm_parser)

    # 设置足够的budget（阶段2每个节点检索一次方向）
    budget = BudgetManager()
    budget.set_budget(BudgetType.HINT, 100)

    pipeline = RealtimePipeline(
        session_id=f"retrieve_{node._key}",
        hgraph=hgraph,
        problem_text=problem_text,
        math_parser=math_parser,
        retrieval_pipeline=RetrievalPipeline(),
        policy=ConstrainedPolicy(),
        budget_manager=budget,
    )

    # 用节点的situation_text构造Round
    agent_output = node.situation_text or node.trajectory_segment.get("thinking", "")
    if not agent_output:
        return ""

    round_data = Round(
        round_index=0,
        agent_output=agent_output[:8000],
        thinking=agent_output[:8000],
        content="",
        tool_calls=[],
        node_ids=[],
        start_timestamp=time.time(),
        end_timestamp=time.time(),
    )

    result = pipeline.process_round(round_data)

    if result.selected_q:
        return result.selected_q
    elif result.error:
        print(f"  [retrieve] 错误: {result.error}")
        return ""
    else:
        print(f"  [retrieve] 未选中提示（无匹配规则）")
        if result.matched_rules:
            print(f"    matched_rules: {len(result.matched_rules)}")
        return ""


def run_serial_multi_ai(
    problem_id: str,
    problem_text: str,
    max_ai_count: int = 3,
    max_time_per_ai: int = 600,
    model: str = "glm-5-2",
    exp_id_prefix: str = "serial",
):
    """
    串行多AI树生长实验。

    流程：
    1. 创建problem + root_node
    2. 启动AI-1（给problem.txt）
    3. 等待AI-1终止
    4. 从AI-1的trajectory提取节点
    5. 在终点节点检索方向
    6. 构造脉络
    7. 启动AI-2（给脉络+方向）
    8. 重复3-7
    """
    print("=" * 60)
    print("阶段2：串行多AI树生长实验")
    print(f"题目ID: {problem_id}")
    print(f"最大AI数: {max_ai_count}")
    print(f"每AI最大时间: {max_time_per_ai}s")
    print(f"模型: {model}")
    print("=" * 60)

    # 确认数据库隔离
    db_name = os.environ.get("ARANGO_DB", "grove_math")
    print(f"\nARANGO_DB={db_name}")
    if db_name != "grove_math":
        print("⚠️ 警告：ARANGO_DB不是grove_math！请先source .env")
        return

    # 初始化组件
    print("\n初始化组件...")
    tree_store = TreeStore()
    hgraph = create_case_253_graph()
    path_constructor = PathConstructor(tree_store)
    termination_detector = TerminationDetector(timeout=300.0)  # 5分钟无新node才判定终止

    # 如果problem已存在，先删除重建
    existing = tree_store.get_problem(problem_id)
    if existing:
        print(f"  题目{problem_id}已存在，将创建新树（不删除旧数据）")
        problem_id = f"{problem_id}_{int(time.time())}"
        print(f"  新题目ID: {problem_id}")

    # Step 1: 创建problem + root_node
    print(f"\n[Step 1] 创建题目和根节点...")
    root_key = tree_store.create_problem(problem_id, problem_text)
    print(f"  root_node_key: {root_key}")

    ai_results = []

    for ai_index in range(1, max_ai_count + 1):
        exp_id = f"{exp_id_prefix}-{problem_id}-ai{ai_index}"
        print(f"\n{'='*40}")
        print(f"[AI-{ai_index}] exp_id={exp_id}")
        print(f"{'='*40}")

        # Step 2: 构造给AI的输入
        if ai_index == 1:
            # AI-1：原始题目，不给脉络
            ai_input = (
                f"你是数学大师。请解答以下数学题。\n\n"
                f"题目：\n{problem_text}\n\n"
                f"要求：\n"
                f"1. 给出完整的解答过程\n"
                f"2. 数学公式用LaTeX\n"
                f"3. 如果你不知道某个知识，明确说\"我不知道[X]\"\n"
            )
            entry_node_key = root_key
            entry_edge = None
            hint_q = ""
        else:
            # AI-2+：脉络 + 方向Q
            # 找到上一个AI的终点节点
            last_ai = ai_results[-1]
            last_node_key = last_ai["last_node_key"]
            direction_q = last_ai["direction_q"]

            if not direction_q:
                print(f"  上一AI未选出方向Q，无法继续")
                break

            path_text = path_constructor.construct_path_text(last_node_key, direction_q)
            ai_input = (
                f"你是数学大师。你正在一个团队中解答一道数学题，之前的AI已经做了一些探索。\n\n"
                f"{path_text}\n"
            )
            entry_node_key = last_node_key
            entry_edge = TreeEdge(
                problem_id=problem_id,
                _from=f"tree_nodes/{last_node_key}",
                hint_q=direction_q,
                ai_instance_id="",
            )
            edge_key = tree_store.add_edge(problem_id, entry_edge)
            entry_edge._key = edge_key
            hint_q = direction_q

            print(f"  脉络文本长度: {len(path_text)} 字符")
            print(f"  方向Q: {direction_q[:80]}...")

        # Step 3: 注册AI实例
        ai_instance = AIInstance(
            problem_id=problem_id,
            entry_node_key=entry_node_key,
            entry_edge_key=entry_edge._key if entry_edge else None,
            path_text=ai_input[:500],
            hint_q=hint_q,
            tmux_session=f"harness-{exp_id}",
            trajectory_dir=str(TRAJECTORY_BASE / exp_id),
        )
        ai_key = tree_store.register_ai(ai_instance)
        print(f"  ai_instance_key: {ai_key}")

        # 更新entry_edge的ai_instance_id
        if entry_edge:
            if tree_store.in_memory:
                doc = tree_store._memory["tree_edges"].get(entry_edge._key)
                if doc:
                    doc["ai_instance_id"] = ai_key
            else:
                col = tree_store.db.collection("tree_edges")
                doc = col.get(entry_edge._key)
                if doc:
                    doc["ai_instance_id"] = ai_key
                    col.replace(doc)

        # Step 4: 启动Solver
        print(f"\n  启动Solver...")
        problem_file = write_problem_file(exp_id, ai_input)
        session_info = launch_solver(exp_id, problem_file, model)
        if not session_info:
            print(f"  Solver启动失败，跳过")
            tree_store.update_ai_status(ai_key, "crashed", end_reason="launch_failed")
            continue

        tmux_session = f"harness-{exp_id}"
        devin_session_id = session_info.get("devin_session_id", "")
        tree_store.update_ai_status(ai_key, "running")
        # 更新devin_session_id
        tree_store.update_ai_status(ai_key, "running")
        if tree_store.in_memory:
            doc = tree_store._memory["ai_instances"].get(ai_key)
            if doc:
                doc["devin_session_id"] = devin_session_id
        else:
            col = tree_store.db.collection("ai_instances")
            doc = col.get(ai_key)
            if doc:
                doc["devin_session_id"] = devin_session_id
                col.replace(doc)

        # Step 5: 等待AI终止 + 实时增量提取节点（从sessions.db读取thinking）
        print(f"\n  等待AI终止（max {max_time_per_ai}s）...")
        print(f"  ⚡ 辅助智能体模式：你是系统Pipe，不是旁观者。AI在thinking时你实时采集、实时整理树。不要干等。")
        print(f"  📡 thinking来源：sessions.db（不依赖MITM）")
        termination_detector.reset()
        termination_detector.set_session_id(devin_session_id)
        start_time = time.time()
        term_event = None

        # 初始化sessions.db模式的增量提取器
        extractor = NodeExtractor(tree_store=tree_store)
        extractor.init_sessions_db(
            ai_instance_id=ai_key,
            problem_id=problem_id,
            devin_session_id=devin_session_id,
            entry_node_key=entry_node_key,
            entry_edge=entry_edge,
            problem_text=problem_text,
        )
        total_nodes_extracted = 0

        while (time.time() - start_time) < max_time_per_ai:
            term_event = termination_detector.check_terminated(tmux_session, exp_id)
            if term_event:
                break
            elapsed = time.time() - start_time

            # 从sessions.db轮询新thinking
            new_keys = extractor.extract_from_sessions_db()
            if new_keys:
                total_nodes_extracted += len(new_keys)
                thinking_len = extractor._db_reader.get_total_thinking_length() if extractor._db_reader else 0
                print(f"  [{elapsed:.0f}s] 🌳 新增{len(new_keys)}节点 (总{total_nodes_extracted}) | thinking: {thinking_len} chars")
            else:
                thinking_len = extractor._db_reader.get_total_thinking_length() if extractor._db_reader else 0
                if thinking_len > 0:
                    print(f"  [{elapsed:.0f}s] thinking: {thinking_len} chars | 节点{total_nodes_extracted} | 等待新thinking...")
                else:
                    print(f"  [{elapsed:.0f}s] 等待thinking开始...")
            time.sleep(10)

        if term_event:
            print(f"\n  AI终止: {term_event.reason} - {term_event.details}")
            end_reason = term_event.reason
        else:
            print(f"\n  AI超时（{max_time_per_ai}s），手动停止")
            end_reason = "manual_stop"

        # Step 6: 停止Solver
        stop_solver(exp_id)

        # Step 7: flush剩余的thinking
        print(f"\n  刷新剩余thinking...")
        flush_keys = extractor.flush_sessions_db()
        if flush_keys:
            total_nodes_extracted += len(flush_keys)
            print(f"  🌳 flush新增{len(flush_keys)}节点")

        node_keys = extractor.get_all_incremental_keys()
        thinking_len = extractor._db_reader.get_total_thinking_length() if extractor._db_reader else 0
        print(f"  thinking: {thinking_len} chars | 总节点: {len(node_keys)}")

        if not node_keys:
            print(f"  未提取到节点，跳过检索")
            tree_store.update_ai_status(ai_key, "completed", end_reason=end_reason, nodes_contributed=[])
            ai_results.append({
                "ai_key": ai_key,
                "exp_id": exp_id,
                "end_reason": end_reason,
                "last_node_key": entry_node_key,
                "direction_q": "",
                "thinking_size": thinking_len,
            })
            continue

        # 更新AI实例的nodes_contributed
        tree_store.update_ai_status(ai_key, "completed", end_reason=end_reason, nodes_contributed=node_keys)

        # Step 8: 在终点节点检索方向
        last_node_key = node_keys[-1]
        last_node = tree_store.get_node(last_node_key)
        print(f"\n  在终点节点 {last_node_key} 检索方向...")

        direction_q = retrieve_directions(last_node, hgraph, problem_text)
        if direction_q:
            print(f"  选出方向Q: {direction_q[:80]}...")
            # 更新节点的retrieval_done和directions_identified
            tree_store.update_node(last_node_key, {
                "retrieval_done": True,
                "directions_identified": [direction_q],
            })
        else:
            print(f"  未选出方向Q")
            tree_store.update_node(last_node_key, {
                "retrieval_done": True,
                "directions_identified": [],
            })

        ai_results.append({
            "ai_key": ai_key,
            "exp_id": exp_id,
            "end_reason": end_reason,
            "last_node_key": last_node_key,
            "direction_q": direction_q,
            "thinking_size": len(thinking_text),
            "nodes_extracted": len(node_keys),
        })

        # 如果没有选出方向Q，无法继续
        if not direction_q:
            print(f"\n  未选出方向Q，无法启动下一个AI")
            break

    # Step 9: 输出实验结果
    print(f"\n{'='*60}")
    print("实验完成")
    print(f"{'='*60}")

    # 获取树的统计
    all_nodes = tree_store.get_nodes_by_problem(problem_id)
    all_edges = tree_store.get_edges_by_problem(problem_id)
    all_ais = tree_store.get_ais_by_problem(problem_id)

    print(f"题目ID: {problem_id}")
    print(f"AI实例数: {len(all_ais)}")
    print(f"节点数: {len(all_nodes)}")
    print(f"边数: {len(all_edges)}")
    print(f"树的最大深度: {max((n.depth for n in all_nodes), default=0)}")

    for r in ai_results:
        print(f"\n  AI-{ai_results.index(r)+1}:")
        print(f"    exp_id: {r['exp_id']}")
        print(f"    end_reason: {r['end_reason']}")
        print(f"    thinking_size: {r.get('thinking_size', 0)}")
        print(f"    nodes_extracted: {r.get('nodes_extracted', 0)}")
        print(f"    direction_q: {r.get('direction_q', '')[:80]}")

    # 保存结果
    result_data = {
        "problem_id": problem_id,
        "total_ais": len(all_ais),
        "total_nodes": len(all_nodes),
        "total_edges": len(all_edges),
        "max_depth": max((n.depth for n in all_nodes), default=0),
        "ai_results": ai_results,
    }

    result_path = TRAJECTORY_BASE / exp_id_prefix / "serial_result.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    with open(result_path, "w") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    print(f"\n结果保存到: {result_path}")


def main():
    parser = argparse.ArgumentParser(description="阶段2：串行多AI树生长实验")
    parser.add_argument("--problem-id", default="case_253", help="题目ID")
    parser.add_argument("--max-ai", type=int, default=3, help="最大AI数")
    parser.add_argument("--max-time-per-ai", type=int, default=600, help="每AI最大时间（秒）")
    parser.add_argument("--model", default="glm-5-2", help="模型名")
    parser.add_argument("--exp-id-prefix", default="serial", help="实验ID前缀")
    args = parser.parse_args()

    run_serial_multi_ai(
        problem_id=args.problem_id,
        problem_text=PROBLEM_TEXT,
        max_ai_count=args.max_ai,
        max_time_per_ai=args.max_time_per_ai,
        model=args.model,
        exp_id_prefix=args.exp_id_prefix,
    )


if __name__ == "__main__":
    main()
