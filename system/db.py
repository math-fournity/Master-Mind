"""
数据库操作模块——system运行时和ArangoDB交互的统一接口。

本模块封装所有数据库操作，其他模块（vein_analysis.py等）通过本模块读写数据库，
不直接操作ArangoDB客户端。

当前实现：
1. problem_entries集合——题目录入记录（抓手）
2. sessions集合——会话记录

设计原则：
- 每个数据库操作都有明确的函数签名和docstring
- 写入操作记录时间戳（ISO 8601格式）
- 读取操作返回dict或None，不抛异常
- 集合不存在时自动创建
"""

import os
import time
from datetime import datetime, timezone
from typing import Optional, Any

from arango import ArangoClient
from arango.exceptions import CollectionCreateError, DocumentInsertError


# ============================================================================
# 数据库连接
# ============================================================================

_client: Optional[ArangoClient] = None
_db: Optional[Any] = None


def _get_db():
    """获取ArangoDB数据库连接（单例）

    从环境变量读取连接配置：
    - ARANGO_HOST: 主机地址（默认http://localhost:8529）
    - ARANGO_DB: 数据库名（默认xishujuzhen_math_glm52）
    - ARANGO_USER: 用户名（默认root）
    - ARANGO_PASS: 密码（默认空）
    """
    global _client, _db
    if _db is not None:
        return _db

    host = os.environ.get("ARANGO_HOST", "http://localhost:8529")
    db_name = os.environ.get("ARANGO_DB", "xishujuzhen_math_glm52")
    user = os.environ.get("ARANGO_USER", "root")
    password = os.environ.get("ARANGO_PASS", "")

    _client = ArangoClient(hosts=host)
    _db = _client.db(db_name, username=user, password=password)
    return _db


def _ensure_collection(name: str):
    """确保集合存在，不存在则创建"""
    db = _get_db()
    if not db.has_collection(name):
        db.create_collection(name)
        print(f"创建集合: {name}")
    return db.collection(name)


def _now_iso() -> str:
    """当前时间ISO 8601格式"""
    return datetime.now(timezone.utc).isoformat()


def _timestamp() -> str:
    """当前时间戳（用于生成唯一ID）"""
    return str(int(time.time() * 1000))


def get_next_run_id() -> int:
    """获取下一个递增的入题序号

    每次入题（无论是新题还是同一道题再次入题）都分配一个唯一的、递增的数字序号。
    这是可审计性的保障——通过序号可以追溯每一次入题的完整记录。

    用ArangoDB的counters集合实现原子递增：
    - counters集合中有一个文档{_key: "run_id", value: 当前最大序号}
    - 每次调用原子递增并返回新值

    Returns:
        下一个递增的入题序号（从1开始）
    """
    db = _get_db()
    col = _ensure_collection("counters")
    try:
        # 尝试原子递增
        doc = col.get("run_id")
        if doc is None:
            # 第一次——初始化为1
            col.insert({"_key": "run_id", "value": 1})
            return 1
        else:
            next_val = doc["value"] + 1
            col.update({"_key": "run_id", "value": next_val})
            return next_val
    except Exception as e:
        # 并发冲突——重试一次
        doc = col.get("run_id")
        if doc is None:
            col.insert({"_key": "run_id", "value": 1})
            return 1
        next_val = doc["value"] + 1
        col.update({"_key": "run_id", "value": next_val})
        return next_val


def format_run_id(run_id: int, problem_id: str) -> str:
    """格式化入题标识——{4位数字序号}_{problem_id}

    例：0001_imo2009p6, 0002_imo2009p6, 0003_imo1985p6

    Args:
        run_id: 递增的入题序号
        problem_id: 题目标识（如imo2009p6）

    Returns:
        格式化的入题标识
    """
    return f"{run_id:04d}_{problem_id}"


# ============================================================================
# problem_entries——题目录入记录（抓手）
# ============================================================================

def create_problem_entry(
    problem_id: str,
    process: str,
    working_directory: str,
    run_id: Optional[int] = None,
    record_id: Optional[str] = None,
    versions: Optional[list] = None,
    version_workdirs: Optional[dict] = None,
    session_names: Optional[dict] = None,
    has_orphan_traces: bool = False,
    session_id: Optional[str] = None,
) -> str:
    """创建题目录入记录——vein_analysis启动时调用

    这是每道题入题的抓手记录。从这条记录可以找到：
    - 入题序号（run_id）——唯一的、递增的数字序号，可审计性保障
    - 工作目录（所有产出文件的根路径）
    - 会话ID
    - 4个AI实例的工作目录和tmux session名
    - 程序验证报告路径、合并trace路径（完成后更新）

    Args:
        problem_id: 题目ID（如imo2009p6）
        process: "absorb"或"solve"
        working_directory: 工作目录绝对路径
        run_id: 入题序号——如果未提供，自动从数据库获取下一个递增序号
        record_id: 关联的解答记录ID（absorb模式有）
        versions: 4并发版本列表（如["V5","V7","V8","V9"]）
        version_workdirs: 各版本工作目录路径
        session_names: 各版本tmux session名
        has_orphan_traces: 是否有孤悬trace启发信号
        session_id: 关联的会话ID

    Returns:
        录入记录ID（_key）——格式为{4位数字序号}_{problem_id}
    """
    # 如果未提供run_id，自动获取下一个递增序号
    if run_id is None:
        run_id = get_next_run_id()

    entry_key = format_run_id(run_id, problem_id)

    collection = _ensure_collection("problem_entries")
    doc = {
        "_key": entry_key,
        "run_id": run_id,
        "problem_id": problem_id,
        "process": process,
        "session_id": session_id,
        "status": "running",
        "working_directory": working_directory,
        "record_id": record_id,
        "versions": versions or [],
        "version_workdirs": version_workdirs or {},
        "session_names": session_names or {},
        "ai_instance_ids": {},
        "output_paths": {},
        "audit_report_path": None,
        "merged_traces_path": None,
        "trace_count": None,
        "has_orphan_traces": has_orphan_traces,
        "started_at": _now_iso(),
        "completed_at": None,
        "error_detail": None,
        # 三阶段架构字段（§4.3）
        "phase1_session_ids": {},        # {version: session_id}——4个格化session
        "phase1_output_paths": {},       # {version: {segments, formal_context}}——格化产出路径
        "phase1_5_output_paths": {},     # {version: closed_elements_path}——程序枚举产出路径
        "phase2_session_id": None,       # 综合分析session的ID
        "phase2_output_paths": {},       # {output_json, output_md}——综合分析产出路径
    }

    result = collection.insert(doc)
    print(f"创建题目录入记录: {entry_key}")
    return entry_key


def update_problem_entry(
    entry_key: str,
    status: Optional[str] = None,
    session_names: Optional[dict] = None,
    ai_instance_ids: Optional[dict] = None,
    output_paths: Optional[dict] = None,
    audit_report_path: Optional[str] = None,
    merged_traces_path: Optional[str] = None,
    trace_count: Optional[int] = None,
    error_detail: Optional[str] = None,
    # 三阶段架构字段（§4.3）
    phase1_session_ids: Optional[dict] = None,
    phase1_output_paths: Optional[dict] = None,
    phase1_5_output_paths: Optional[dict] = None,
    phase2_session_id: Optional[str] = None,
    phase2_output_paths: Optional[dict] = None,
    # 339号方案——研发资产管理字段
    manifest_path: Optional[str] = None,
    archive_path: Optional[str] = None,
    git_commit: Optional[str] = None,
):
    """更新题目录入记录——vein_analysis各阶段完成时调用

    Args:
        entry_key: 录入记录ID（create_problem_entry返回的_key）
        status: 新状态（"running"/"completed"/"failed"）
        session_names: 各版本tmux session名
        ai_instance_ids: 各版本AI实例ID
        output_paths: 各版本产出文件路径
        audit_report_path: 程序验证报告路径
        merged_traces_path: 合并trace文件路径
        trace_count: 合并后的trace总数
        error_detail: 失败原因
        phase1_session_ids: {version: session_id}——4个格化session的ID
        phase1_output_paths: {version: {segments, formal_context}}——格化产出路径
        phase1_5_output_paths: {version: closed_elements_path}——程序枚举产出路径
        phase2_session_id: 综合分析session的ID
        phase2_output_paths: {output_json, output_md}——综合分析产出路径
    """
    collection = _ensure_collection("problem_entries")
    doc = collection.get(entry_key)
    if doc is None:
        print(f"⚠️ 题目录入记录不存在: {entry_key}")
        return

    if status is not None:
        doc["status"] = status
    if session_names is not None:
        doc["session_names"] = session_names
    if ai_instance_ids is not None:
        doc["ai_instance_ids"] = ai_instance_ids
    if output_paths is not None:
        doc["output_paths"] = output_paths
    if audit_report_path is not None:
        doc["audit_report_path"] = audit_report_path
    if merged_traces_path is not None:
        doc["merged_traces_path"] = merged_traces_path
    if trace_count is not None:
        doc["trace_count"] = trace_count
    if error_detail is not None:
        doc["error_detail"] = error_detail
    # 三阶段架构字段
    if phase1_session_ids is not None:
        doc["phase1_session_ids"] = phase1_session_ids
    if phase1_output_paths is not None:
        doc["phase1_output_paths"] = phase1_output_paths
    if phase1_5_output_paths is not None:
        doc["phase1_5_output_paths"] = phase1_5_output_paths
    if phase2_session_id is not None:
        doc["phase2_session_id"] = phase2_session_id
    if phase2_output_paths is not None:
        doc["phase2_output_paths"] = phase2_output_paths
    # 339号方案——研发资产管理字段
    if manifest_path is not None:
        doc["manifest_path"] = manifest_path
    if archive_path is not None:
        doc["archive_path"] = archive_path
    if git_commit is not None:
        doc["git_commit"] = git_commit
    if status in ("completed", "failed"):
        doc["completed_at"] = _now_iso()

    collection.update(doc)
    print(f"更新题目录入记录: {entry_key} (status={status or doc['status']})")


def get_problem_entry(entry_key: str) -> Optional[dict]:
    """读取题目录入记录"""
    collection = _ensure_collection("problem_entries")
    return collection.get(entry_key)


def find_problem_entries_by_problem_id(problem_id: str) -> list:
    """查找一道题的所有录入记录——未来查找题目录入信息的主入口

    Args:
        problem_id: 题目ID

    Returns:
        录入记录列表，按时间倒序
    """
    collection = _ensure_collection("problem_entries")
    cursor = collection.find({"problem_id": problem_id})
    entries = list(cursor)
    entries.sort(key=lambda x: x.get("started_at", ""), reverse=True)
    return entries


# ============================================================================
# sessions——会话记录
# ============================================================================

def create_session(
    session_type: str,
    problem_id: str,
    working_directory: str,
) -> str:
    """创建会话记录

    Args:
        session_type: "absorb"或"solve"
        problem_id: 题目ID
        working_directory: 工作目录绝对路径

    Returns:
        会话ID（_key）
    """
    collection = _ensure_collection("sessions")
    session_key = f"{session_type}_{problem_id}_{_timestamp()}"

    doc = {
        "_key": session_key,
        "session_type": session_type,
        "problem_id": problem_id,
        "status": "running",
        "started_at": _now_iso(),
        "completed_at": None,
        "working_directory": working_directory,
        "result_summary": None,
    }

    collection.insert(doc)
    print(f"创建会话记录: {session_key}")
    return session_key


def update_session(
    session_key: str,
    status: Optional[str] = None,
    result_summary: Optional[str] = None,
):
    """更新会话记录

    Args:
        session_key: 会话ID
        status: 新状态
        result_summary: 结果摘要
    """
    collection = _ensure_collection("sessions")
    doc = collection.get(session_key)
    if doc is None:
        print(f"⚠️ 会话记录不存在: {session_key}")
        return

    if status is not None:
        doc["status"] = status
    if result_summary is not None:
        doc["result_summary"] = result_summary
    if status in ("completed", "failed"):
        doc["completed_at"] = _now_iso()

    collection.update(doc)
    print(f"更新会话记录: {session_key} (status={status or doc['status']})")


# ============================================================================
# ai_instances——AI实例记录
# ============================================================================

def create_ai_instance(
    session_id: str,
    ai_role: str,
    working_directory: str,
    problem_id: str,
    tmux_session: str,
    version: Optional[str] = None,
) -> str:
    """创建AI实例记录

    Args:
        session_id: 关联的会话ID
        ai_role: AI角色（"parser"/"solver"/"telling"/"guide"）
        working_directory: 工作目录绝对路径
        problem_id: 题目ID
        tmux_session: tmux session名
        version: 版本名（脉络分析AI的V5/V7/V8/V9）

    Returns:
        AI实例ID（_key）
    """
    collection = _ensure_collection("ai_instances")
    ai_key = f"ai_{session_id}_{version or ai_role}_{_timestamp()}"

    doc = {
        "_key": ai_key,
        "session_id": session_id,
        "ai_role": ai_role,
        "working_directory": working_directory,
        "problem_id": problem_id,
        "tmux_session": tmux_session,
        "version": version,
        "status": "running",
        "started_at": _now_iso(),
        "ended_at": None,
        "end_reason": None,
        "output_summary": None,
    }

    collection.insert(doc)
    print(f"创建AI实例记录: {ai_key}")
    return ai_key


def update_ai_instance(
    ai_key: str,
    status: Optional[str] = None,
    end_reason: Optional[str] = None,
    output_summary: Optional[str] = None,
):
    """更新AI实例记录

    Args:
        ai_key: AI实例ID
        status: 新状态
        end_reason: 结束原因
        output_summary: 产出摘要
    """
    collection = _ensure_collection("ai_instances")
    doc = collection.get(ai_key)
    if doc is None:
        print(f"⚠️ AI实例记录不存在: {ai_key}")
        return

    if status is not None:
        doc["status"] = status
    if end_reason is not None:
        doc["end_reason"] = end_reason
    if output_summary is not None:
        doc["output_summary"] = output_summary
    if status in ("completed", "failed"):
        doc["ended_at"] = _now_iso()

    collection.update(doc)
