#!/usr/bin/env python3
"""
入题——外部持续向系统添加题目（及其解答记录），系统从中提炼tell/hint，tell库增长。

这是系统的两个入口之一。另一个入口是 solve.py（解题）。

用法：
    python system/enter.py <解答记录路径或目录>

输入：外部题目及其解答记录
输出：tell库增长（新tell+新hint存入tell库）

内部调用解答吸收过程（process_absorb.absorb）。
"""

import sys
import os

# 将 system 目录加入 path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from schema import SolutionRecord, Problem, Tell
from process_absorb import absorb


def main():
    if len(sys.argv) < 2:
        print("用法: python system/enter.py <解答记录路径或目录>")
        print("  解答记录是JSON文件，包含problem和solution_text")
        sys.exit(1)

    input_path = sys.argv[1]
    tell_library_path = os.environ.get("TELL_LIBRARY_PATH", "tell_library")

    # 加载解答记录（待实现——根据输入路径加载JSON/批量加载目录）
    solution_records = load_solution_records(input_path)

    # 解答吸收：从外部解答中提炼tell/hint，tell库增长
    new_tells = absorb(solution_records, tell_library_path)

    print(f"解答吸收完成：新增 {len(new_tells)} 个tell到tell库")


def load_solution_records(path: str) -> list[SolutionRecord]:
    """从路径加载解答记录

    待实现——根据路径是文件还是目录，加载单个或批量解答记录。
    解答记录格式待定义（JSON/JSONL/其他）。
    """
    raise NotImplementedError("加载解答记录 待实现")


if __name__ == "__main__":
    main()
