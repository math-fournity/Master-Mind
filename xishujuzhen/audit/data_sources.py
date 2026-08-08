"""数据源接口——ArangoDB / sessions.db / run目录。"""

from __future__ import annotations

import json
import os
import sqlite3
from typing import Any, Dict, List, Optional

from xishujuzhen.audit.framework import AuditData


# ---------------------------------------------------------------------------
# run目录接口
# ---------------------------------------------------------------------------

class RunDirSource:
    """从run目录提取数据。"""

    def __init__(self, runs_root: str = "runs"):
        self.runs_root = runs_root

    def load(self, run_id: str) -> AuditData:
        """加载一个run的全部数据。"""
        run_dir = os.path.join(self.runs_root, run_id)

        # guided_loop_result.json
        glr_path = os.path.join(run_dir, "guided_loop_result.json")
        guided_loop_result: Dict[str, Any] = {}
        if os.path.exists(glr_path):
            with open(glr_path, encoding="utf-8") as f:
                guided_loop_result = json.load(f)

        # turn_log.json
        turn_logs: List[Dict[str, Any]] = []
        tl_path = os.path.join(run_dir, "turn_log.json")
        if os.path.exists(tl_path):
            with open(tl_path, encoding="utf-8") as f:
                turn_logs = json.load(f)
            if not isinstance(turn_logs, list):
                turn_logs = [turn_logs]

        # turn_*_conversation.json
        conversations: List[Dict[str, Any]] = []
        for fname in sorted(os.listdir(run_dir)):
            if fname.startswith("turn_") and fname.endswith("_conversation.json"):
                with open(os.path.join(run_dir, fname), encoding="utf-8") as f:
                    conversations.append(json.load(f))

        # session_id
        session_id = guided_loop_result.get("session_id", "")

        return AuditData(
            run_id=run_id,
            run_dir=run_dir,
            guided_loop_result=guided_loop_result,
            turn_logs=turn_logs,
            conversations=conversations,
            session_id=session_id,
        )


# ---------------------------------------------------------------------------
# sessions.db接口
# ---------------------------------------------------------------------------

class SessionsDBSource:
    """从devin cli的sessions.db提取数据。"""

    DB_PATH = os.path.expanduser("~/.local/share/devin/cli/sessions.db")

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or self.DB_PATH

    def enrich(self, data: AuditData) -> AuditData:
        """给AuditData补充sessions.db数据。"""
        if not data.session_id:
            return data

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            # session信息
            row = conn.execute(
                "SELECT id, working_directory, model, created_at, title "
                "FROM sessions WHERE id = ?",
                (data.session_id,),
            ).fetchone()
            if row:
                data.session_info = {
                    "id": row["id"],
                    "working_directory": row["working_directory"],
                    "model": row["model"],
                    "created_at": row["created_at"],
                    "title": row["title"],
                }

            # message_nodes
            rows = conn.execute(
                "SELECT node_id, chat_message FROM message_nodes "
                "WHERE session_id = ? ORDER BY node_id",
                (data.session_id,),
            ).fetchall()
            for r in rows:
                try:
                    msg = json.loads(r["chat_message"])
                    msg["_node_id"] = r["node_id"]
                    data.message_nodes.append(msg)
                except (json.JSONDecodeError, TypeError):
                    pass

            # tool_call_state
            rows = conn.execute(
                "SELECT tool_call_json FROM tool_call_state "
                "WHERE session_id = ?",
                (data.session_id,),
            ).fetchall()
            for r in rows:
                try:
                    tc = json.loads(r["tool_call_json"])
                    data.tool_call_states.append(tc)
                except (json.JSONDecodeError, TypeError):
                    pass
        finally:
            conn.close()

        return data


# ---------------------------------------------------------------------------
# ArangoDB接口
# ---------------------------------------------------------------------------

class ArangoDBSource:
    """从ArangoDB提取数据。"""

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or os.environ.get("ARANGO_DB", "grove_math")

    def enrich(self, data: AuditData) -> AuditData:
        """给AuditData补充ArangoDB数据。"""
        try:
            from arango import ArangoClient
        except ImportError:
            return data

        try:
            client = ArangoClient(hosts="http://localhost:8529")
            db = client.db(self.db_name, username="root", password="")

            # 按collection提取数据
            collections_to_check = [
                "workspaces", "raw_events", "semantic_events",
                "obligations", "evidence", "verification_results",
                "heuristic_rules", "leakage_audits", "stall_detections",
                "checkpoints", "stall_calibration",
            ]
            for coll_name in collections_to_check:
                if db.has_collection(coll_name):
                    coll = db.collection(coll_name)
                    docs = list(coll.find({"run_id": data.run_id}))
                    if not docs:
                        # 尝试不带run_id过滤（某些collection可能不用run_id）
                        docs = list(coll.all())[:100]  # 限制100条防止过大
                    data.arango_data[coll_name] = docs
        except Exception:
            pass  # ArangoDB不可用时静默跳过

        return data


# ---------------------------------------------------------------------------
# 统一加载
# ---------------------------------------------------------------------------

def load_audit_data(
    run_id: str,
    runs_root: str = "runs",
    use_sessions_db: bool = True,
    use_arango: bool = True,
) -> AuditData:
    """从全部数据源加载审计数据。"""
    run_source = RunDirSource(runs_root)
    data = run_source.load(run_id)

    if use_sessions_db and data.session_id:
        sessions_source = SessionsDBSource()
        data = sessions_source.enrich(data)

    if use_arango:
        arango_source = ArangoDBSource()
        data = arango_source.enrich(data)

    return data
