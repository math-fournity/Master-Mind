"""
解答吸收——从外部解答中提炼tell/hint，tell库增长。

这是系统的"入题"入口（system/enter.py 调用本模块）。

4个阶段：
1. 解答录入——外部题目+解答记录进入系统
2. 脉络分析——分析解答记录，格化脉络，识别trace（接收孤悬trace作为启发信号）
3. trace匹配——用trace匹配tell库
4. 知识沉淀——没匹配到tell的trace去特化，建立新(tell,hint)，tell库增长

和解题引导的关系：
- 解答吸收接收解题引导产出的孤悬trace作为启发信号
- 解答吸收建立的新tell增长tell库，解题引导下一轮可以匹配到更多tell
- 两个过程形成闭环：解题引导→解答吸收→解题引导

和解题引导的关键区别（在知识沉淀阶段）：
- 解答吸收中没匹配到tell的trace可以直接成为新tell——
  因为外部解答记录是完整正确解答，trace被验证过。
- 解题引导的trace是探索中的，可能走对了也可能走错了，不能直接升级。
"""

from .schema import (
    Problem, Hint, Tell, Trace,
    SolutionRecord,
    AnalysisInput, AnalysisOutput,
    MatchInput, MatchOutput,
    KnowledgeDepositOutput,
)
from .vein_analysis import vein_analysis_three_phase


def absorb(solution_records: list[SolutionRecord],
           tell_library_path: str) -> list[Tell]:
    """
    解答吸收——从外部解答中提炼tell/hint，tell库增长。

    Args:
        solution_records: 外部题目及其解答记录列表
        tell_library_path: tell库路径

    Returns:
        新建立的tell列表

    流程（对每条解答记录）：
        解答录入 → 脉络分析 → trace匹配 → 知识沉淀
    """
    new_tells_all = []

    for record in solution_records:
        # 解答录入已在record中完成（SolutionRecord由调用方构造）

        # 获取解题引导产出的孤悬trace（启发信号）
        orphan_traces = get_archived_orphan_traces()

        # 脉络分析：分析解答记录，格化脉络，识别trace（三阶段架构）
        analysis_output = vein_analysis_three_phase(AnalysisInput(
            process="absorb",
            solution_record=record,
            orphan_traces=orphan_traces
        ))

        # trace匹配：用trace匹配tell库
        match_output = trace_match(MatchInput(
            traces=analysis_output.traces,
            tell_library_path=tell_library_path
        ))

        # 知识沉淀：没匹配到tell的trace去特化，建立新(tell,hint)
        deposit = knowledge_deposit(match_output)
        if deposit.new_tells:
            for new_tell in deposit.new_tells:
                save_tell_to_library(new_tell, tell_library_path)
                new_tells_all.append(new_tell)

    return new_tells_all


# ============================================================================
# 阶段函数（待实现的占位）
# ============================================================================

# vein_analysis 已实现——从 .vein_analysis 导入
# absorb模式采用4并发方案（V5/V7/V8/V9并发取trace并集）


def trace_match(input: MatchInput) -> MatchOutput:
    """trace匹配——用trace匹配tell库

    和解题引导完全相同——匹配AI不关心trace来自哪里。
    并发启动多个匹配AI，每个负责一个分类目录。

    实现时并发调用多个匹配AI（devin cli 实例）。
    """
    raise NotImplementedError("trace匹配 待实现")


def knowledge_deposit(match_output: MatchOutput) -> KnowledgeDepositOutput:
    """知识沉淀——没匹配到tell的trace去特化，建立新(tell,hint)

    匹配到tell的trace → 确认匹配（不需要新建，trace来自已验证的正确解答）
    没匹配到tell的trace → 去特化 → 建立新(tell,hint) → 存入tell库

    为什么解答吸收的trace可以直接成为tell：
    外部解答记录是完整正确解答，trace被验证过。
    """
    raise NotImplementedError("知识沉淀 待实现")


def get_archived_orphan_traces() -> list[Trace]:
    """获取存档的孤悬trace——解答吸收的脉络分析AI的启发信号

    孤悬trace来自解题引导——解题引导中没匹配到tell的trace被存档，
    解答吸收的脉络分析AI接收这些trace作为启发信号，
    知道"解题引导中哪些模式没被识别"，从而重点从这些Level观察外部解答记录。
    """
    raise NotImplementedError("获取存档孤悬trace 待实现")


def save_tell_to_library(tell: Tell, library_path: str) -> None:
    """把新tell存入tell库

    新tell来自知识沉淀——没匹配到已有tell的trace去特化后建立新(tell,hint)。
    存入对应分类目录，供解题引导和解答吸收未来的trace匹配使用。
    """
    raise NotImplementedError("存入tell库 待实现")
