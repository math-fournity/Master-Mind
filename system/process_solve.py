"""
解题引导——系统解答题目，在推理过程中引导新方向，引导树展开。

这是系统的"解题"入口（system/solve.py 调用本模块）。

5个阶段：
1. 推理探索——推理AI做题，产出thinking
2. 脉络分析——分析thinking，格化脉络，识别trace
3. trace匹配——用trace匹配tell库
4. 方向取用——从匹配到的tell取hint，没匹配的trace存档
5. 引导展开——用hint开新边，构造脉络，启动新推理AI

循环直到停机（solved或exhausted）。

和解答吸收的关系：
- 解题引导中没匹配到tell的trace（孤悬trace）存档后启发解答吸收
- 解答吸收建立的新tell增长tell库，解题引导下一轮可以匹配到更多tell
- 两个过程形成闭环：解题引导→解答吸收→解题引导
"""

from .schema import (
    Problem, Hint, Tell, Trace,
    Thinking, MathSituation, TreeEdge, TreeState,
    SolverInput, SolverOutput,
    AnalysisInput, AnalysisOutput,
    MatchInput, MatchOutput,
    DirectionExtractionOutput,
    GuideExpansionInput, GuideExpansionOutput,
)
from .vein_analysis import vein_analysis_three_phase


def solve(problem: Problem, tell_library_path: str,
          max_concurrent: int = 2) -> TreeState:
    """
    解题引导——系统解答题目，引导树展开。

    Args:
        problem: 需要解答的题目
        tell_library_path: tell库路径
        max_concurrent: 最大并发推理AI数

    Returns:
        引导树最终状态（solved或exhausted）

    循环：
        推理探索 → 脉络分析 → trace匹配 → 方向取用 → 引导展开 → 推理探索 → ...
        直到停机（solved或exhausted）
    """
    # 初始化引导树
    tree_state = TreeState(
        problem_id=problem.problem_id,
        nodes=[MathSituation(
            node_id="root",
            problem_id=problem.problem_id,
            node_type="root",
            situation_text=problem.problem_text,
            depth=0,
            path_from_root=["root"]
        )],
        edges=[],
        status="growing",
        running_solvers=[]
    )

    # 推理探索：启动第一个推理AI（裸做题，无方向）
    first_input = SolverInput(
        problem=problem,
        path_text=problem.problem_text,
        hint=None
    )
    solver_output = inference_explore(first_input)

    # 解题引导循环
    while tree_state.status == "growing":
        # 脉络分析：分析thinking，格化脉络，识别trace（三阶段架构）
        analysis_output = vein_analysis_three_phase(AnalysisInput(
            process="solve",
            thinking=solver_output.thinking
        ))

        # trace匹配：用trace匹配tell库
        match_output = trace_match(MatchInput(
            traces=analysis_output.traces,
            tell_library_path=tell_library_path
        ))

        # 方向取用：从匹配到的tell取hint，没匹配的trace存档
        extraction = direction_extract(match_output)
        if extraction.orphan_traces:
            archive_orphan_traces(extraction.orphan_traces)

        # 引导展开：用hint开新边，构造脉络，启动新推理AI
        if extraction.hints:
            expansion = guide_expand(GuideExpansionInput(
                hints=extraction.hints,
                problem_id=problem.problem_id,
                tree_state=tree_state
            ))

            tree_state = expansion.tree_state

            if expansion.stop:
                break

            # 启动新推理AI（并发，受max_concurrent限制）
            for solver_input in expansion.new_solver_inputs:
                if len(tree_state.running_solvers) < max_concurrent:
                    solver_output = inference_explore(solver_input)
                    tree_state.running_solvers.append(
                        solver_output.thinking.solver_ai_id
                    )
                else:
                    break

    return tree_state


# ============================================================================
# 阶段函数（待实现的占位）
# ============================================================================

def inference_explore(input: SolverInput) -> SolverOutput:
    """推理探索——推理AI做题，产出thinking

    输入：题目+脉络+方向（第一个AI无方向）
    产出：thinking（完整思维过程）+ 终点节点

    实现时调用推理AI（LLM API 或 devin cli）。
    """
    raise NotImplementedError("推理探索 待实现")


# vein_analysis 已实现——从 .vein_analysis 导入
# solve模式提示词未设计（TODO-1），当前vein_analysis("solve")会raise NotImplementedError


def trace_match(input: MatchInput) -> MatchOutput:
    """trace匹配——用trace匹配tell库

    并发启动多个匹配AI，每个负责一个分类目录。
    每个匹配AI加载该目录的tell内容，遍历tell做匹配。

    实现时并发调用多个匹配AI（devin cli 实例）。
    """
    raise NotImplementedError("trace匹配 待实现")


def direction_extract(match_output: MatchOutput) -> DirectionExtractionOutput:
    """方向取用——从匹配到的tell取hint，没匹配的trace存档

    匹配到tell的trace → 从tell取hint（多对多，一个tell可对应多个hint全取）
    没匹配到tell的trace → 孤悬trace，存档后启发解答吸收
    """
    raise NotImplementedError("方向取用 待实现")


def guide_expand(input: GuideExpansionInput) -> GuideExpansionOutput:
    """引导展开——用hint开新边，构造脉络，启动新推理AI

    1. 判断每个hint在引导树哪个Level开新边
    2. 在引导树上开新边
    3. 构造脉络（从根到新边的路径+方向）
    4. 生成新推理AI的输入
    5. 检查停机条件

    实现时调用引导AI（LLM API 或 devin cli）。
    """
    raise NotImplementedError("引导展开 待实现")


def archive_orphan_traces(traces: list[Trace]) -> None:
    """存档孤悬trace——按tell分类学分类积累，启发解答吸收

    孤悬trace是解题引导中没匹配到tell的trace。
    它们没有hint，不能驱动引导树生长。
    但它们不是废物——按tell分类学分类积累，等待解答吸收验证后升级为正式tell。
    """
    raise NotImplementedError("存档孤悬trace 待实现")
