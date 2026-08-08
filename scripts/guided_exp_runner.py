#!/usr/bin/env python3
"""
215号实验：连续交互启发式引导——矩条件极差题第(1)问

使用tmux + devin cli交互式session + --export + DFS树记录
引导者（本脚本的操作者）通过tmux send-keys发送Q，通过capture-pane收集A
DFS树记录在runs/dfs_tree.json，对话导出在runs/exports/

用法：本脚本是手动操作的辅助工具，不是全自动的。
引导者决定每一步发什么Q，用本脚本记录到DFS树。
"""

import subprocess
import time
import sys
import os
import re
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))
from dfs_tree import DFSTree

# ============ 配置 ============
WORK_DIR = "/data/math-agent-glm5.2-1"
SESSION_NAME = "guided-exp-1"
RUN_DIR = "/data/master-mind-glm5.2-grove/runs/guided_001"
EXPORT_DIR = f"{RUN_DIR}/exports"
TREE_FILE = f"{RUN_DIR}/dfs_tree.json"
LOG_FILE = f"{RUN_DIR}/interaction_log.md"

# ============ 初始化 ============
os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(RUN_DIR, exist_ok=True)

tree = DFSTree(TREE_FILE)


def tmux_send(text: str, wait: int = 30):
    """发送消息到tmux session并等待"""
    subprocess.run(
        ["tmux", "send-keys", "-t", SESSION_NAME, text, "Enter"],
        check=True
    )
    time.sleep(wait)


def tmux_capture() -> str:
    """捕获tmux pane内容"""
    result = subprocess.run(
        ["tmux", "capture-pane", "-t", SESSION_NAME, "-p", "-S", "-200"],
        capture_output=True, text=True
    )
    return result.stdout


def tmux_capture_new_lines(before: str) -> str:
    """捕获before之后的新行"""
    after = tmux_capture()
    if after.startswith(before):
        return after[len(before):]
    return after


def start_session():
    """启动新的tmux session + devin cli"""
    export_path = f"{EXPORT_DIR}/session_{int(time.time())}.json"
    
    # 杀掉旧session
    subprocess.run(["tmux", "kill-session", "-t", SESSION_NAME], 
                   capture_output=True)
    
    # 启动新session
    cmd = f"cd {WORK_DIR} && devin --model glm-5-2 --export {export_path}"
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", SESSION_NAME, cmd],
        check=True
    )
    time.sleep(5)
    
    # 处理trust prompt
    pane = tmux_capture()
    if "trust" in pane.lower():
        subprocess.run(
            ["tmux", "send-keys", "-t", SESSION_NAME, "1", "Enter"],
            check=True
        )
        time.sleep(8)
    
    return export_path


def send_q(q_text: str, level: float, category: str, 
           is_root: bool = False, wait: int = 45) -> str:
    """
    发送一个Q到做题AI，记录到DFS树
    返回node_id
    """
    export_path = f"{EXPORT_DIR}/session_{int(time.time())}.json"
    
    # 记录发送前的pane状态
    before = tmux_capture()
    
    # 发送Q
    tmux_send(q_text, wait)
    
    # 捕获A
    after = tmux_capture()
    a_text = tmux_capture_new_lines(before)
    
    # 判断A的状态
    a_status = judge_a_status(a_text)
    
    # 记录到DFS树
    if is_root:
        node_id = tree.add_root(q_text, level, category, SESSION_NAME, export_path)
    else:
        parent_id = tree.current_node_id()
        node_id = tree.add_child(parent_id, q_text, level, category, 
                                  SESSION_NAME, export_path)
    
    tree.update_a(node_id, a_text, a_status)
    
    # 记录到log
    log_interaction(node_id, q_text, level, category, a_text, a_status)
    
    print(f"\n{'='*60}")
    print(f"[{node_id}] Q (L={level:.2f}, {category}):")
    print(f"  {q_text[:100]}...")
    print(f"  A status: {a_status}")
    print(f"  A preview: {a_text[:200]}...")
    print(f"  Level SUM on path: {tree.level_sum_on_path(node_id):.2f}")
    print(f"{'='*60}")
    
    return node_id


def judge_a_status(a_text: str) -> str:
    """判断A的状态"""
    a_lower = a_text.lower().strip()
    if len(a_lower) < 50:
        return "stuck"
    if any(kw in a_lower for kw in ["证毕", "qed", "证明完毕", "完成", "c = √5", "c=√5", "sqrt(5)"]):
        if any(kw in a_lower for kw in ["证毕", "qed", "证明完毕"]):
            return "success"
    if any(kw in a_lower for kw in ["不知道", "无法", "卡住", "不会", "不确定"]):
        if len(a_lower) < 200:
            return "stuck"
    if len(a_lower) > 200:
        return "progressing"
    return "progressing"


def log_interaction(node_id, q_text, level, category, a_text, a_status):
    """记录到markdown log"""
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## 轮次 {node_id}\n\n")
        f.write(f"**Q** (Level={level:.2f}, 类型={category}):\n")
        f.write(f"```\n{q_text}\n```\n\n")
        f.write(f"**A** (状态={a_status}):\n")
        f.write(f"```\n{a_text[:2000]}\n```\n\n")
        f.write(f"**Level SUM**: {tree.level_sum_on_path(node_id):.2f}\n\n")


def print_status():
    """打印当前树状态"""
    s = tree.summary()
    print(f"\n--- DFS树状态 ---")
    print(f"  总节点: {s['total_nodes']}")
    print(f"  成功: {s['success_nodes']}, 死路: {s['dead_end_nodes']}, 卡住: {s['stuck_nodes']}")
    print(f"  最大深度: {s['max_depth']}")
    print(f"  当前路径: {s['current_path']}")
    print(f"  当前Level SUM: {s['current_level_sum']:.2f}")
    print(f"---\n")
    tree.print_tree()


def new_session_for_backtrack():
    """回溯时启动新session"""
    print("启动新session用于回溯...")
    export_path = start_session()
    return export_path


def replay_to_fork(fork_node_id: str):
    """重放Q序列到岔口"""
    q_sequence = tree.get_replay_q_sequence(fork_node_id)
    print(f"重放 {len(q_sequence)} 个Q到岔口 {fork_node_id}...")
    for i, q in enumerate(q_sequence):
        print(f"  重放Q[{i}]: {q[:60]}...")
        tmux_send(q, wait=45)
    print("重放完成。")


if __name__ == "__main__":
    print("215号实验辅助工具")
    print(f"  RUN_DIR: {RUN_DIR}")
    print(f"  TREE_FILE: {TREE_FILE}")
    print(f"  LOG_FILE: {LOG_FILE}")
    print(f"  当前树状态:")
    print_status()
