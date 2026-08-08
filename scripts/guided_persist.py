#!/usr/bin/env python3
"""
guided_persist.py — 引导式数学解题实验数据入库ArangoDB

实现 guided-data-persist 元组的9层数据保留。
从 runs/<run_id>/dfs_tree.json + result_summary.json 读取数据，
写入ArangoDB的dfs_cases/dfs_nodes/dfs_edges/dfs_decisions/dfs_sessions。

用法：
    source .env
    .venv/bin/python3 scripts/guided_persist.py --run-id guided_001
    .venv/bin/python3 scripts/guided_persist.py --run-id guided_003
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime, timezone

from arango import ArangoClient


# ============ 配置 ============
REPO_ROOT = Path(__file__).parent.parent
RUNS_DIR = REPO_ROOT / "runs"


def get_db():
    """连接ArangoDB（使用.env环境变量）"""
    host = os.environ.get("ARANGO_HOST", "http://localhost:8529")
    db_name = os.environ.get("ARANGO_DB", "grove_math")
    user = os.environ.get("ARANGO_USER", "root")
    password = os.environ.get("ARANGO_PASS", "")
    client = ArangoClient(hosts=host)
    return client.db(db_name, username=user, password=password)


def ensure_collections(db):
    """确保dfs_* collections存在"""
    for col_name in ["dfs_cases", "dfs_nodes", "dfs_decisions", "dfs_sessions"]:
        if not db.has_collection(col_name):
            db.create_collection(col_name)
            print(f"  created {col_name}")
    if not db.has_collection("dfs_edges"):
        db.create_collection("dfs_edges", edge=True)
        print("  created dfs_edges (edge)")


def load_run_data(run_id: str) -> dict:
    """从文件系统加载run数据"""
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        raise FileNotFoundError(f"Run directory not found: {run_dir}")

    data = {"run_id": run_id, "run_dir": str(run_dir)}

    # dfs_tree.json（可能不存在——guided_003没有DFS树）
    dfs_tree_path = run_dir / "dfs_tree.json"
    if dfs_tree_path.exists():
        with open(dfs_tree_path) as f:
            data["dfs_tree"] = json.load(f)
    else:
        data["dfs_tree"] = None

    # result_summary.json
    result_path = run_dir / "result_summary.json"
    if result_path.exists():
        with open(result_path) as f:
            data["result_summary"] = json.load(f)
    else:
        data["result_summary"] = None

    # proof.md（如果存在）
    proof_path = run_dir / "proof.md"
    if proof_path.exists():
        data["proof_text"] = proof_path.read_text()
    else:
        data["proof_text"] = None

    # tmux_pipe.log（如果存在）
    pipe_log_path = run_dir / "tmux_pipe.log"
    if pipe_log_path.exists():
        data["tmux_pipe_log_path"] = str(pipe_log_path)
    else:
        data["tmux_pipe_log_path"] = None

    # exports目录
    exports_dir = run_dir / "exports"
    if exports_dir.exists():
        data["exports_dir"] = str(exports_dir)
        data["export_files"] = list(exports_dir.glob("*.json"))
    else:
        data["exports_dir"] = None
        data["export_files"] = []

    return data


def persist_case(db, run_data: dict) -> str:
    """持久化dfs_cases文档（第1+2+8+9层）"""
    rs = run_data["result_summary"]
    if rs is None:
        raise ValueError(f"No result_summary.json for {run_data['run_id']}")

    case_id = rs.get("case_id", f"case_{run_data['run_id']}")
    col = db.collection("dfs_cases")

    # 检查是否已存在（用case_id去重）
    existing = list(col.find({"case_id": case_id}, limit=1))
    if existing:
        # 更新——保留_key，更新其他字段
        new_doc = _build_case_doc(run_data, case_id)
        new_doc["_key"] = existing[0]["_key"]
        col.update(new_doc)
        print(f"  updated dfs_cases/{case_id}")
        return existing[0]["_key"]

    # 插入
    doc = _build_case_doc(run_data, case_id)
    result = col.insert(doc)
    print(f"  inserted dfs_cases/{case_id} (key={result['_key']})")
    return result["_key"]


def _build_case_doc(run_data: dict, case_id: str) -> dict:
    """构造dfs_cases文档"""
    rs = run_data["result_summary"]
    dfs_tree = run_data.get("dfs_tree")

    # DFS树摘要
    tree_summary = None
    if dfs_tree:
        nodes = dfs_tree.get("nodes", {})
        tree_summary = {
            "total_nodes": len(nodes),
            "max_depth": max((n.get("depth", 0) for n in nodes.values()), default=0),
            "current_path": dfs_tree.get("current_path", []),
            "success_nodes": [nid for nid, n in nodes.items() if n.get("a_status") == "success"],
            "dead_end_nodes": [nid for nid, n in nodes.items() if n.get("a_status") == "dead_end"],
            "stuck_nodes": [nid for nid, n in nodes.items() if n.get("a_status") == "stuck"],
        }

    return {
        "case_id": case_id,
        "run_id": rs.get("run_id", run_data["run_id"]),
        "problem_id": rs.get("problem_id", ""),
        "problem_text": rs.get("problem_text", ""),
        "standard_answer": rs.get("standard_answer", ""),
        "source_dataset": rs.get("source_dataset", ""),
        "source_competition": rs.get("source_competition", ""),
        "run_timestamp": rs.get("start_timestamp", ""),
        "devin_cli_version": rs.get("devin_cli_version", ""),
        "model_name": rs.get("model", ""),
        "work_dir": rs.get("work_dir", ""),
        "session_name": rs.get("session_name", ""),
        # 第3层：预演记录（如果有）
        "rehearsal_level_sum": rs.get("rehearsal_level_sum"),
        # 第4层：DFS树摘要
        "dfs_tree_summary": tree_summary,
        # 第8层：结果验证
        "final_answer": rs.get("final_answer", ""),
        "is_correct": rs.get("is_correct", False),
        "verification_method": rs.get("verification_method", ""),
        "proof_completeness": rs.get("proof_completeness", ""),
        "proof_correctness": rs.get("proof_correctness", ""),
        "proof_path": rs.get("proof_path", ""),
        # 第9层：性能指标
        "total_time_seconds": rs.get("total_time_seconds", 0),
        "total_turns": rs.get("total_turns", 0),
        "total_sessions": rs.get("total_sessions", 0),
        "total_backtracks": rs.get("total_backtracks", 0),
        "level_sum_achieved": rs.get("level_sum_achieved", 0),
        "level_sum_mean": rs.get("level_sum_mean", 0),
        "level_drop_count": rs.get("level_drop_count", 0),
        # 元数据
        "persisted_at": datetime.now(timezone.utc).isoformat(),
        # guided_003特有字段
        "q_sequence_type": rs.get("q_sequence_type", ""),
        "q_sequence": rs.get("q_sequence", []),
        "non_specificity_check": rs.get("non_specificity_check", ""),
        "comparison_with_guided_001": rs.get("comparison_with_guided_001", {}),
        "key_findings": rs.get("key_findings", []),
        "implications_for_primitives": rs.get("implications_for_primitives", {}),
        "notes": rs.get("notes", ""),
    }


def persist_nodes(db, run_data: dict, case_key: str) -> int:
    """持久化dfs_nodes + dfs_edges（第4+5层）"""
    dfs_tree = run_data.get("dfs_tree")
    if dfs_tree is None:
        print(f"  no dfs_tree.json for {run_data['run_id']}——跳过nodes/edges")
        return 0

    nodes = dfs_tree.get("nodes", {})
    nodes_col = db.collection("dfs_nodes")
    edges_col = db.collection("dfs_edges")
    count = 0

    for node_id, node_data in nodes.items():
        # 检查是否已存在
        existing = list(nodes_col.find({"node_id": node_id, "case_id": run_data["result_summary"].get("case_id", "")}, limit=1))
        if existing:
            nodes_col.update(existing[0]["_key"], {
                "q_text": node_data.get("q_text", ""),
                "q_level": node_data.get("q_level", 0),
                "q_category": node_data.get("q_category", ""),
                "q_candidates": node_data.get("candidates", []),
                "a_text": node_data.get("a_text", ""),
                "a_status": node_data.get("a_status", ""),
                "a_variants": node_data.get("a_variants", []),
                "a_status_reason": node_data.get("a_status_reason", ""),
                "session_id": node_data.get("session_id", ""),
                "export_path": node_data.get("export_path", ""),
                "timestamp": node_data.get("timestamp", ""),
                "depth": node_data.get("depth", 0),
                "parent_id": node_data.get("parent_id"),
            })
            node_key = existing[0]["_key"]
        else:
            doc = {
                "node_id": node_id,
                "case_id": run_data["result_summary"].get("case_id", ""),
                "parent_node_id": node_data.get("parent_id"),
                "depth": node_data.get("depth", 0),
                "q_text": node_data.get("q_text", ""),
                "q_level": node_data.get("q_level", 0),
                "q_category": node_data.get("q_category", ""),
                "q_candidates": node_data.get("candidates", []),
                "q_selected_reason": node_data.get("q_selected_reason", ""),
                "a_text": node_data.get("a_text", ""),
                "a_variants": node_data.get("a_variants", []),
                "a_status": node_data.get("a_status", ""),
                "a_status_reason": node_data.get("a_status_reason", ""),
                "session_id": node_data.get("session_id", ""),
                "export_path": node_data.get("export_path", ""),
                "timestamp": node_data.get("timestamp", ""),
            }
            result = nodes_col.insert(doc)
            node_key = result["_key"]

        # 添加边（如果有父节点）
        parent_id = node_data.get("parent_id")
        if parent_id:
            parent_existing = list(nodes_col.find({"node_id": parent_id, "case_id": run_data["result_summary"].get("case_id", "")}, limit=1))
            if parent_existing:
                edge_existing = list(edges_col.find({
                    "_from": f"dfs_nodes/{parent_existing[0]['_key']}",
                    "_to": f"dfs_nodes/{node_key}",
                }, limit=1))
                if not edge_existing:
                    edges_col.insert({
                        "_from": f"dfs_nodes/{parent_existing[0]['_key']}",
                        "_to": f"dfs_nodes/{node_key}",
                        "case_id": run_data["result_summary"].get("case_id", ""),
                        "edge_type": "q_prompt",
                    })

        count += 1

    print(f"  persisted {count} nodes + edges")
    return count


def persist_decisions(db, run_data: dict) -> int:
    """持久化dfs_decisions（第7层——引导者决策日志）"""
    dfs_tree = run_data.get("dfs_tree")
    if dfs_tree is None:
        # guided_003没有dfs_tree——从q_sequence构造决策记录
        rs = run_data["result_summary"]
        q_sequence = rs.get("q_sequence", [])
        case_id = rs.get("case_id", "")
        decisions_col = db.collection("dfs_decisions")
        count = 0
        for q_entry in q_sequence:
            q_id = q_entry.get("q_id", "")
            existing = list(decisions_col.find({"decision_id": f"dec_{case_id}_{q_id}", "case_id": case_id}, limit=1))
            if existing:
                continue
            doc = {
                "decision_id": f"dec_{case_id}_{q_id}",
                "node_id": q_id,
                "case_id": case_id,
                "decision_type": "select_q",
                "decision_reason": f"纯非特定Q序列——{q_entry.get('category', '')}",
                "q_text": q_entry.get("text", ""),
                "q_level": q_entry.get("level", 1.0),
                "q_category": q_entry.get("category", ""),
                "alternatives_considered": [],
                "a_status": q_entry.get("a_status", ""),
                "timestamp": rs.get("start_timestamp", ""),
            }
            decisions_col.insert(doc)
            count += 1
        print(f"  persisted {count} decisions (from q_sequence)")
        return count

    # guided_001有dfs_tree——从nodes构造
    nodes = dfs_tree.get("nodes", {})
    case_id = run_data["result_summary"].get("case_id", "")
    decisions_col = db.collection("dfs_decisions")
    count = 0
    for node_id, node_data in nodes.items():
        existing = list(decisions_col.find({"decision_id": f"dec_{node_id}", "case_id": case_id}, limit=1))
        if existing:
            continue
        doc = {
            "decision_id": f"dec_{node_id}",
            "node_id": node_id,
            "case_id": case_id,
            "decision_type": "select_q",
            "decision_reason": node_data.get("q_category", ""),
            "q_text": node_data.get("q_text", ""),
            "q_level": node_data.get("q_level", 1.0),
            "q_category": node_data.get("q_category", ""),
            "alternatives_considered": node_data.get("candidates", []),
            "a_status": node_data.get("a_status", ""),
            "timestamp": node_data.get("timestamp", ""),
        }
        decisions_col.insert(doc)
        count += 1
    print(f"  persisted {count} decisions (from dfs_tree)")
    return count


def persist_sessions(db, run_data: dict) -> int:
    """持久化dfs_sessions（第6层——Session级记录）"""
    rs = run_data["result_summary"]
    if rs is None:
        return 0

    case_id = rs.get("case_id", "")
    session_name = rs.get("session_name", "")
    sessions_col = db.collection("dfs_sessions")

    existing = list(sessions_col.find({"session_id": session_name, "case_id": case_id}, limit=1))
    if existing:
        print(f"  session {session_name} already exists")
        return 0

    doc = {
        "session_id": session_name,
        "case_id": case_id,
        "run_id": rs.get("run_id", ""),
        "work_dir": rs.get("work_dir", ""),
        "model": rs.get("model", ""),
        "export_files": [str(p) for p in run_data.get("export_files", [])],
        "tmux_pipe_log": run_data.get("tmux_pipe_log_path", ""),
        "proof_path": rs.get("proof_path", ""),
        "start_timestamp": rs.get("start_timestamp", ""),
        "end_timestamp": rs.get("end_timestamp", ""),
        "is_backtrack_session": False,
        "persisted_at": datetime.now(timezone.utc).isoformat(),
    }
    sessions_col.insert(doc)
    print(f"  persisted session {session_name}")
    return 1


def verify_persistence(db, run_id: str) -> dict:
    """验证入库完整性——9层检查"""
    rs_path = RUNS_DIR / run_id / "result_summary.json"
    with open(rs_path) as f:
        rs = json.load(f)
    case_id = rs.get("case_id", "")

    checks = {}

    # 第1层：题目元数据
    case = list(db.collection("dfs_cases").find({"case_id": case_id}, limit=1))
    checks["layer1_problem_metadata"] = bool(case and case[0].get("problem_text"))
    checks["layer2_run_metadata"] = bool(case and case[0].get("model_name"))
    checks["layer3_rehearsal"] = bool(case and case[0].get("rehearsal_level_sum") is not None)
    checks["layer4_dfs_tree"] = bool(case and case[0].get("dfs_tree_summary"))
    checks["layer8_result_verification"] = bool(case and case[0].get("is_correct") is not None)
    checks["layer9_performance"] = bool(case and case[0].get("total_time_seconds", 0) > 0)

    # 第5层：节点完整记录
    node_count = db.collection("dfs_nodes").find({"case_id": case_id}).count()
    checks["layer5_nodes"] = node_count > 0

    # 第6层：Session级记录
    session_count = db.collection("dfs_sessions").find({"case_id": case_id}).count()
    checks["layer6_sessions"] = session_count > 0

    # 第7层：引导者决策
    decision_count = db.collection("dfs_decisions").find({"case_id": case_id}).count()
    checks["layer7_decisions"] = decision_count > 0

    # 汇总
    passed = sum(1 for v in checks.values() if v)
    total = len(checks)
    checks["_summary"] = f"{passed}/{total} layers passed"
    checks["_case_id"] = case_id
    checks["_node_count"] = node_count
    checks["_decision_count"] = decision_count
    checks["_session_count"] = session_count

    return checks


def main():
    parser = argparse.ArgumentParser(description="引导式数学解题实验数据入库ArangoDB")
    parser.add_argument("--run-id", required=True, help="Run ID (e.g. guided_001, guided_003)")
    parser.add_argument("--verify-only", action="store_true", help="只验证不入库")
    args = parser.parse_args()

    print(f"[guided_persist] run_id={args.run_id}")

    db = get_db()
    ensure_collections(db)

    if args.verify_only:
        checks = verify_persistence(db, args.run_id)
        print(f"\n[verify] {args.run_id}:")
        for k, v in checks.items():
            if not k.startswith("_"):
                status = "✓" if v else "✗"
                print(f"  {status} {k}: {v}")
        print(f"  {checks['_summary']}")
        return

    # 加载数据
    print(f"[load] loading from {RUNS_DIR / args.run_id}...")
    run_data = load_run_data(args.run_id)
    print(f"  dfs_tree: {'yes' if run_data['dfs_tree'] else 'no'}")
    print(f"  result_summary: {'yes' if run_data['result_summary'] else 'no'}")
    print(f"  proof: {'yes' if run_data['proof_text'] else 'no'}")
    print(f"  exports: {len(run_data['export_files'])} files")

    # 入库
    print(f"[persist] writing to ArangoDB...")
    case_key = persist_case(db, run_data)
    persist_nodes(db, run_data, case_key)
    persist_decisions(db, run_data)
    persist_sessions(db, run_data)

    # 验证
    print(f"\n[verify] checking 9 layers...")
    checks = verify_persistence(db, args.run_id)
    for k, v in checks.items():
        if not k.startswith("_"):
            status = "✓" if v else "✗"
            print(f"  {status} {k}: {v}")
    print(f"  {checks['_summary']}")
    print(f"  nodes={checks['_node_count']}, decisions={checks['_decision_count']}, sessions={checks['_session_count']}")


if __name__ == "__main__":
    main()
