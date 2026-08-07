#!/usr/bin/env python3
"""
DFS引导树记录器
记录引导者和做题AI的交互过程，支持树状结构、回溯、多session。
"""

import json
import os
import time
from dataclasses import dataclass, field, asdict
from typing import Optional
from pathlib import Path


@dataclass
class TreeNode:
    """DFS树的一个节点"""
    node_id: str                          # 唯一标识，如 "0", "0.1", "0.1.2"
    parent_id: Optional[str]              # 父节点ID，根节点为None
    depth: int                            # 深度，根为0
    q_text: str                           # 引导者发送的Q（提示/发问）
    q_level: float                        # Q的预估Level值 [0,1]
    q_category: str                       # Q的分类（元认知指令/归一化/反证法/...）
    a_text: str = ""                      # 做题AI的回复A
    a_status: str = "pending"             # pending/progressing/stuck/success/dead_end
    candidates: list = field(default_factory=list)   # 引导者在该节点的候选Q列表
    tried_candidate_indices: list = field(default_factory=list)  # 已尝试的候选索引
    current_candidate_idx: int = -1       # 当前正在尝试的候选索引
    session_id: str = ""                  # 对应的devin cli session ID
    export_path: str = ""                 # --export导出文件路径
    timestamp: str = ""                   # 创建时间
    children: list = field(default_factory=list)  # 子节点ID列表


class DFSTree:
    """DFS引导树"""
    
    def __init__(self, tree_file: str):
        self.tree_file = tree_file
        self.nodes = {}       # node_id -> TreeNode
        self.root_id = None
        self.current_path = []  # 当前DFS路径（node_id列表）
        
        if os.path.exists(tree_file):
            self.load()
    
    def add_root(self, q_text: str, q_level: float, q_category: str, 
                 session_id: str, export_path: str) -> str:
        """创建根节点"""
        node_id = "0"
        node = TreeNode(
            node_id=node_id,
            parent_id=None,
            depth=0,
            q_text=q_text,
            q_level=q_level,
            q_category=q_category,
            session_id=session_id,
            export_path=export_path,
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        )
        self.nodes[node_id] = node
        self.root_id = node_id
        self.current_path = [node_id]
        self.save()
        return node_id
    
    def add_child(self, parent_id: str, q_text: str, q_level: float, 
                  q_category: str, session_id: str, export_path: str) -> str:
        """添加子节点"""
        parent = self.nodes[parent_id]
        # 子节点ID = parent_id + "." + 序号
        child_idx = len(parent.children)
        node_id = f"{parent_id}.{child_idx}"
        node = TreeNode(
            node_id=node_id,
            parent_id=parent_id,
            depth=parent.depth + 1,
            q_text=q_text,
            q_level=q_level,
            q_category=q_category,
            session_id=session_id,
            export_path=export_path,
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        )
        self.nodes[node_id] = node
        parent.children.append(node_id)
        self.current_path.append(node_id)
        self.save()
        return node_id
    
    def update_a(self, node_id: str, a_text: str, a_status: str):
        """更新节点的A（做题AI回复）"""
        if node_id in self.nodes:
            self.nodes[node_id].a_text = a_text
            self.nodes[node_id].a_status = a_status
            self.save()
    
    def set_candidates(self, node_id: str, candidates: list):
        """设置节点的候选Q列表"""
        if node_id in self.nodes:
            self.nodes[node_id].candidates = candidates
            self.save()
    
    def mark_candidate_tried(self, node_id: str, candidate_idx: int):
        """标记某个候选已尝试"""
        if node_id in self.nodes:
            self.nodes[node_id].tried_candidate_indices.append(candidate_idx)
            self.nodes[node_id].current_candidate_idx = candidate_idx
            self.save()
    
    def backtrack(self) -> Optional[str]:
        """回溯到父节点，返回父节点ID（或None如果已在根）"""
        if len(self.current_path) <= 1:
            return None
        self.current_path.pop()
        return self.current_path[-1]
    
    def current_node_id(self) -> Optional[str]:
        """当前节点ID"""
        return self.current_path[-1] if self.current_path else None
    
    def get_path_to_root(self, node_id: str) -> list:
        """从node_id到根的路径（用于回溯后重放Q序列）"""
        path = []
        current = node_id
        while current is not None:
            path.append(current)
            current = self.nodes[current].parent_id
        return list(reversed(path))
    
    def get_replay_q_sequence(self, to_node_id: str) -> list:
        """获取从根到to_node_id的Q序列（用于新session重放）"""
        path = self.get_path_to_root(to_node_id)
        # 不包括to_node_id本身的Q（因为to_node_id是要换方向的岔口，
        # 在岔口我们要发新的Q而不是旧的）
        return [self.nodes[nid].q_text for nid in path[:-1]]
    
    def level_sum_on_path(self, node_id: str) -> float:
        """计算从根到node_id路径上的Level SUM"""
        path = self.get_path_to_root(node_id)
        return sum(self.nodes[nid].q_level for nid in path)
    
    def save(self):
        """保存树到JSON文件"""
        data = {
            "root_id": self.root_id,
            "current_path": self.current_path,
            "nodes": {nid: asdict(n) for nid, n in self.nodes.items()},
        }
        with open(self.tree_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load(self):
        """从JSON文件加载树"""
        with open(self.tree_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.root_id = data["root_id"]
        self.current_path = data["current_path"]
        self.nodes = {}
        for nid, nd in data["nodes"].items():
            self.nodes[nid] = TreeNode(**nd)
    
    def summary(self) -> dict:
        """返回树的统计摘要"""
        total_nodes = len(self.nodes)
        success_nodes = sum(1 for n in self.nodes.values() if n.a_status == "success")
        dead_end_nodes = sum(1 for n in self.nodes.values() if n.a_status == "dead_end")
        stuck_nodes = sum(1 for n in self.nodes.values() if n.a_status == "stuck")
        max_depth = max((n.depth for n in self.nodes.values()), default=0)
        
        # 当前路径的Level SUM
        current = self.current_node_id()
        current_level_sum = self.level_sum_on_path(current) if current else 0
        
        return {
            "total_nodes": total_nodes,
            "success_nodes": success_nodes,
            "dead_end_nodes": dead_end_nodes,
            "stuck_nodes": stuck_nodes,
            "max_depth": max_depth,
            "current_path": self.current_path,
            "current_level_sum": current_level_sum,
            "current_node": current,
        }
    
    def print_tree(self, node_id: str = None, indent: int = 0):
        """打印树结构"""
        if node_id is None:
            node_id = self.root_id
        if node_id is None:
            print("(empty tree)")
            return
        node = self.nodes[node_id]
        prefix = "  " * indent
        status_icon = {
            "pending": "⏳",
            "progressing": "▶",
            "stuck": "🚫",
            "success": "✅",
            "dead_end": "❌",
        }.get(node.a_status, "?")
        q_preview = node.q_text[:60].replace("\n", " ")
        print(f"{prefix}{status_icon} [{node.node_id}] L={node.q_level:.1f} Q: {q_preview}...")
        for child_id in node.children:
            self.print_tree(child_id, indent + 1)


if __name__ == "__main__":
    # 测试
    tree = DFSTree("/tmp/test_dfs_tree.json")
    root = tree.add_root("描述题目形状", 1.0, "元认知指令", "sess1", "/tmp/exp1.json")
    print(f"Root: {root}")
    child1 = tree.add_child(root, "列出所有方向", 1.0, "元认知指令", "sess1", "/tmp/exp1.json")
    print(f"Child1: {child1}")
    tree.update_a(child1, "我想到了6个方向...", "progressing")
    print(f"Summary: {tree.summary()}")
    tree.print_tree()
