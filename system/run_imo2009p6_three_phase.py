"""
运行脚本——用IMO 2009 P6实际运行vein_analysis_three_phase()的三阶段流程。

三阶段架构：
1. 阶段1（4并发格化）：V5/V7/V8/V10各做段划分+形式上下文构造
2. 阶段1.5（程序枚举闭元素）：Next Closure算法枚举所有闭元素
3. 阶段2（1个综合分析Agent）：读4个版本格化结果+程序枚举闭元素，做trace识别+审计+元反思

所有中间结果存到 palyground/absorb/vein_analysis_three_phase/imo2009p6/ 下。
建议在tmux中运行：tmux new -s three_phase "python3 system/run_imo2009p6_three_phase.py"
"""

import os
import sys
import json

# 关闭Python输出缓冲
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

from system.vein_analysis import vein_analysis_three_phase
from system.schema import AnalysisInput, SolutionRecord, Problem


def main():
    # 1. 从profile.json读取IMO 2009 P6的题目和解答
    profile_path = "subagents-dirs/compfiles_imo2009p6/profile.json"
    with open(profile_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    problem_text = profile["problem_text"]
    solution_text = profile["solution_text"]
    problem_id = "imo2009p6"

    print(f"=== IMO 2009 P6 三阶段脉络分析测试 ===")
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
        record_id=f"run_three_phase_{problem_id}",
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

    # 3. 调用vein_analysis_three_phase()
    print("调用 vein_analysis_three_phase()...")
    print("=" * 70)
    output = vein_analysis_three_phase(input)
    print("=" * 70)

    # 4. 打印结果
    print(f"三阶段脉络分析完成")
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
    print("=== 三阶段测试完成 ===")
    print()
    print("下一步：运行POC验证脚本对比基线和新架构")
    print("  python3 system/tests/vein_analysis/run_poc_no_loss.py")


if __name__ == "__main__":
    main()
