#!/usr/bin/env python3
"""
解题——将需要解答的题目送入系统，系统编排引导树和解题树的展开，直至获得正确解答。

这是系统的两个入口之一。另一个入口是 enter.py（入题）。

用法：
    python system/solve.py <题目路径>

输入：需要解答的题目
输出：引导树最终状态（solved或exhausted）

内部调用解题引导过程（process_solve.solve）。
"""

import sys
import os

# 将 system 目录加入 path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from schema import Problem
from process_solve import solve


def main():
    if len(sys.argv) < 2:
        print("用法: python system/solve.py <题目路径>")
        print("  题目是JSON文件，包含problem_id和problem_text")
        sys.exit(1)

    input_path = sys.argv[1]
    tell_library_path = os.environ.get("TELL_LIBRARY_PATH", "tell_library")

    # 加载题目（待实现——根据输入路径加载JSON）
    problem = load_problem(input_path)

    # 解题引导：系统解答题目，引导树展开
    tree_state = solve(problem, tell_library_path)

    print(f"解题引导完成：引导树状态={tree_state.status}")
    print(f"  节点数={len(tree_state.nodes)}，边数={len(tree_state.edges)}")


def load_problem(path: str) -> Problem:
    """从路径加载题目

    待实现——根据路径加载题目JSON。
    题目格式待定义（JSON）。
    """
    raise NotImplementedError("加载题目 待实现")


if __name__ == "__main__":
    main()
