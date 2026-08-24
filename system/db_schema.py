"""
数据库表设计——系统运行所需的数据存储结构。

表设计是迭代的——当前只定义最小必要的表和字段，后续随系统实现推进逐步增加。

当前表：
1. sessions——会话表，记录每次入题或解题
2. problem_entries——题目录入表，每道题入题一条记录，是查找该题目所有录入信息的抓手

后续待增加的表（随系统实现推进）：
- orphan_traces——孤悬trace存档表（解题引导产出，解答吸收消费）
- tell_library_changes——tell库变更日志（新tell添加、tell修正）
- ai_instances——AI实例记录（每个devin cli实例的启动参数和产出）
- tree_nodes——引导树节点表
- tree_edges——引导树边表
- alerts——系统警报表（文件超长、运行时错误等）
"""

from dataclasses import dataclass
from typing import Optional, Literal


# ============================================================================
# sessions 表——会话记录
# ============================================================================

SESSIONS_TABLE_SCHEMA = {
    "table_name": "sessions",
    "description": "会话表——一次入题或一次解题一条记录",
    "fields": {
        "session_id": {
            "type": "TEXT PRIMARY KEY",
            "description": "会话唯一ID",
        },
        "session_type": {
            "type": "TEXT NOT NULL",
            "description": "会话类型：absorb=入题（解答吸收），solve=解题（解题引导）",
            "values": ["absorb", "solve"],
        },
        "problem_id": {
            "type": "TEXT NOT NULL",
            "description": "关联的题目ID——devin cli启动目录以此ID命名",
        },
        "status": {
            "type": "TEXT NOT NULL DEFAULT 'running'",
            "description": "会话状态",
            "values": ["running", "completed", "failed"],
        },
        "started_at": {
            "type": "TEXT",
            "description": "启动时间（ISO 8601格式）",
        },
        "completed_at": {
            "type": "TEXT",
            "description": "完成时间（ISO 8601格式）",
        },
        "working_directory": {
            "type": "TEXT",
            "description": "devin cli启动目录的绝对路径——workspace/absorb/{problem_id}/ 或 workspace/solve/{problem_id}/",
        },
        "result_summary": {
            "type": "TEXT",
            "description": "会话结果摘要——入题：新增tell数量；解题：引导树最终状态",
        },
    },
    "indexes": [
        {"name": "idx_sessions_problem_id", "fields": ["problem_id"]},
        {"name": "idx_sessions_type", "fields": ["session_type"]},
        {"name": "idx_sessions_status", "fields": ["status"]},
    ],
}


# ============================================================================
# 启动目录路径约定
# ============================================================================

# palyground/ 是运行时工作目录根
# 不同阶段的devin cli实例启动在不同的子目录中，每个子目录下以题目ID创建工作目录
# 结构：palyground/{process}/{stage}/{problem_id}/

# 解题引导的阶段
SOLVE_STAGES = ["inference_explore", "vein_analysis", "trace_match", "guide_expand"]

# 解答吸收的阶段
ABSORB_STAGES = ["vein_analysis", "trace_match", "knowledge_deposit"]

# 解答录入和方向取用是纯系统逻辑，不需要devin cli，没有工作目录


def get_working_directory(session_type: Literal["absorb", "solve"],
                          stage: str,
                          problem_id: str,
                          base_dir: str = "palyground") -> str:
    """获取devin cli实例的启动目录路径

    启动目录结构：{base_dir}/{session_type}/{stage}/{problem_id}/
    不同过程、不同阶段的devin cli实例彼此隔离，工作目录以题目ID命名。

    Args:
        session_type: "absorb"=入题（解答吸收）, "solve"=解题（解题引导）
        stage: 阶段名——
            解题引导: inference_explore / vein_analysis / trace_match / guide_expand
            解答吸收: vein_analysis / trace_match / knowledge_deposit
        problem_id: 题目ID
        base_dir: 运行时工作目录根，默认为 "palyground"

    Returns:
        启动目录路径：{base_dir}/{session_type}/{stage}/{problem_id}/

    示例：
        get_working_directory("solve", "inference_explore", "FLT_001")
        → "palyground/solve/inference_explore/FLT_001"
    """
    valid_stages = SOLVE_STAGES if session_type == "solve" else ABSORB_STAGES
    if stage not in valid_stages:
        raise ValueError(
            f"阶段 '{stage}' 不是 {session_type} 的有效阶段。"
            f"有效阶段: {valid_stages}"
        )
    return f"{base_dir}/{session_type}/{stage}/{problem_id}"


# ============================================================================
# 待增加的表（占位，随系统实现推进逐步定义）
# ============================================================================

# TODO: orphan_traces表——孤悬trace存档
#   解题引导中没匹配到tell的trace存档于此，解答吸收的脉络分析AI读取作为启发信号
#   字段：trace_id, problem_id, session_id, trace_type, level, pattern_description,
#         source_segment_ids, archived_at, consumed_by_session_id

# TODO: tell_library_changes表——tell库变更日志
#   记录tell库的每次变更（新tell添加、tell修正）
#   字段：change_id, change_type(add/modify), tell_id, session_id, changed_at, change_detail

# TODO: ai_instances表——AI实例记录
#   记录每个devin cli实例的启动参数和产出
#   字段：ai_id, session_id, ai_role(solver/parser/telling/guide), working_directory,
#         started_at, completed_at, input_summary, output_summary

# TODO: tree_nodes表——引导树节点
#   字段：node_id, problem_id, session_id, node_type, situation_text, depth, path_from_root

# TODO: tree_edges表——引导树边
#   字段：edge_id, problem_id, session_id, from_node, to_node, hint_id, level

# TODO: alerts表——系统警报（见six-asset-grading.md rule TODO-14）
#   字段：alert_id, alert_type, file_path, lines, chars, severity, detected_at, resolved_at, resolved_by, detail


# ============================================================================
# problem_entries 表——题目录入记录（抓手）
# ============================================================================

PROBLEM_ENTRIES_COLLECTION = "problem_entries"

PROBLEM_ENTRIES_SCHEMA = {
    "collection_name": "problem_entries",
    "description": (
        "题目录入表——每道题入题一条记录，是查找该题目所有录入信息的抓手。"
        "从这条记录可以找到：工作目录、会话ID、4个AI实例的产出路径、"
        "程序验证报告路径、合并trace路径等。"
    ),
    "fields": {
        "_key": {
            "type": "TEXT PRIMARY KEY",
            "description": "录入记录ID——格式: {process}_{problem_id}_{timestamp}",
        },
        "problem_id": {
            "type": "TEXT NOT NULL",
            "description": "题目ID",
        },
        "process": {
            "type": "TEXT NOT NULL",
            "description": "过程类型：absorb=入题（解答吸收），solve=解题（解题引导）",
            "values": ["absorb", "solve"],
        },
        "session_id": {
            "type": "TEXT",
            "description": "关联的会话ID（sessions表的_key）",
        },
        "status": {
            "type": "TEXT NOT NULL DEFAULT 'running'",
            "description": "录入状态：running=运行中，completed=完成，failed=失败",
            "values": ["running", "completed", "failed"],
        },
        "working_directory": {
            "type": "TEXT NOT NULL",
            "description": "工作目录绝对路径——palyground/{process}/vein_analysis/{problem_id}/",
        },
        "record_id": {
            "type": "TEXT",
            "description": "关联的解答记录ID（absorb模式有，solve模式无）",
        },
        "versions": {
            "type": "ARRAY",
            "description": "4并发版本列表——[\"V5\", \"V7\", \"V8\", \"V10\"]",
        },
        "version_workdirs": {
            "type": "OBJECT",
            "description": "各版本工作目录路径——{V5: path, V7: path, V8: path, V10: path}",
        },
        "session_names": {
            "type": "OBJECT",
            "description": "各版本tmux session名——{V5: name, V7: name, V8: name, V10: name}",
        },
        "ai_instance_ids": {
            "type": "OBJECT",
            "description": "各版本AI实例ID（ai_instances表的_key）——{V5: id, V7: id, V8: id, V10: id}",
        },
        "output_paths": {
            "type": "OBJECT",
            "description": "各版本产出文件路径——{V5: {json: path, md: path}, ...}",
        },
        "audit_report_path": {
            "type": "TEXT",
            "description": "V10程序验证报告路径——audit_report.json",
        },
        "merged_traces_path": {
            "type": "TEXT",
            "description": "合并trace文件路径——merged_traces.json",
        },
        "trace_count": {
            "type": "INTEGER",
            "description": "合并后的trace总数",
        },
        "has_orphan_traces": {
            "type": "BOOLEAN",
            "description": "是否有孤悬trace启发信号（absorb模式）",
        },
        "started_at": {
            "type": "TEXT",
            "description": "启动时间（ISO 8601格式）",
        },
        "completed_at": {
            "type": "TEXT",
            "description": "完成时间（ISO 8601格式）",
        },
        "error_detail": {
            "type": "TEXT",
            "description": "失败原因（status=failed时有值）",
        },
    },
    "indexes": [
        {"name": "idx_problem_entries_problem_id", "fields": ["problem_id"]},
        {"name": "idx_problem_entries_process", "fields": ["process"]},
        {"name": "idx_problem_entries_status", "fields": ["status"]},
    ],
}
