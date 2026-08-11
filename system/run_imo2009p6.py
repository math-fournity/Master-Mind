"""
运行脚本——用IMO 2009 P6实际运行vein_analysis()的完整4并发流程。

这个脚本会：
1. 构造IMO 2009 P6的AnalysisInput
2. 调用vein_analysis()——内部会准备工作目录、创建数据库记录、启动4个tmux session、等待完成、收集产出
3. 打印结果

vein_analysis()会阻塞等待4个AI完成（最多60分钟）。
建议在tmux中运行：tmux new -s vein_test "python3 system/run_imo2009p6.py"
"""

import os
import sys
import json

# 关闭Python输出缓冲——print立即输出到tmux pane
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)

# 确保在repo根目录
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(repo_root)
sys.path.insert(0, repo_root)

# 加载环境变量
env_path = os.path.join(repo_root, ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                os.environ[key] = value

from system.vein_analysis import vein_analysis
from system.schema import AnalysisInput, SolutionRecord, Problem


def main():
    # 1. 从profile.json读取IMO 2009 P6的题目和解答
    profile_path = "subagents-dirs/compfiles_imo2009p6/profile.json"
    with open(profile_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    problem_text = profile["problem_text"]
    solution_text = profile["solution_text"]
    problem_id = "imo2009p6"

    print(f"=== IMO 2009 P6 并发脉络分析测试 ===")
    print(f"题目ID: {problem_id}")
    print(f"题目长度: {len(problem_text)}字符")
    print(f"解答长度: {len(solution_text)}字符")
    print()

    # 2. 构造AnalysisInput
    problem = Problem(
        problem_id=problem_id,
        problem_text=problem_text,
        domain=profile.get("domain", "combinatorics"),
    )
    record = SolutionRecord(
        record_id=f"run_{problem_id}",
        problem=problem,
        solution_text=solution_text,
        is_verified=True,
    )
    input = AnalysisInput(
        process="absorb",
        thinking=None,
        solution_record=record,
        orphan_traces=None,
    )

    # 3. 调用vein_analysis()——完整4并发流程
    print("调用 vein_analysis()...")
    print("=" * 70)
    output = vein_analysis(input)
    print("=" * 70)

    # 4. 打印结果
    print(f"脉络分析完成")
    print(f"trace数量: {len(output.traces)}")
    print(f"vein数量: {len(output.veins)}")
    print(f"level_view数量: {len(output.level_views)}")

    if output.traces:
        print()
        print("=== trace列表 ===")
        for i, trace in enumerate(output.traces):
            desc = getattr(trace, 'description', str(trace))[:80]
            print(f"  {i+1}. {desc}")

    print()
    print("=== 测试完成 ===")


if __name__ == "__main__":
    main()
