"""
第六代系统完整流程

两个完整流程函数 + 辅助函数。

来源：319号§1
"""

from .types import (
    Problem, Tell, Trace, Hint, SolutionRecord,
    MathSituation, TreeState,
    SolverInput, SolverOutput,
    ParserInput, ParserOutput,
    TellingInput, TellingOutput,
    Step5Input, Step5Output,
    GuideInput, GuideOutput,
)
from .pipes import (
    pipe_0_solver,
    pipe_1_parser,
    pipe_2_telling,
    step_5_branch,
    pipe_3_guide,
)


# ============================================================================
# 完整流程——解题引导（原过程A，Grove核心循环）
# ============================================================================

def grove_core_loop(problem: Problem, tell_library_path: str,
                    max_concurrent: int = 2) -> TreeState:
    """
    解题引导——Grove核心循环的完整流程

    Solver AI → Parser AI → Telling AI → 步骤5分叉(解题引导) → Guide AI → Solver AI → ...

    循环直到停机（solved或exhausted）。

    POC验证：
      - VMS-17：端到端工作流验证这个循环
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

    # 启动第一个Solver AI（裸做题，无hint）
    first_input = SolverInput(
        problem=problem,
        path_text=problem.problem_text,
        hint=None
    )
    first_output = pipe_0_solver(first_input)

    # Grove核心循环
    while tree_state.status == "growing":
        # ---- Pipe 1: Parser AI ----
        # 并行：Solver AI在thinking的同时Parser AI就增量提取trace
        parser_output = pipe_1_parser(ParserInput(
            process="solve",
            thinking=first_output.thinking
        ))

        # ---- Pipe 2: Telling AI ----
        telling_output = pipe_2_telling(TellingInput(
            traces=parser_output.traces,
            tell_library_path=tell_library_path
        ))

        # ---- 步骤5分叉（解题引导）----
        step5_output = step_5_branch(Step5Input(
            telling_output=telling_output,
            process="solve"
        ))

        # 孤悬trace存档（启发解答吸收的Parser AI）
        if step5_output.orphan_traces:
            archive_orphan_traces(step5_output.orphan_traces)

        # ---- Pipe 3: Guide AI ----
        if step5_output.hints:
            guide_output = pipe_3_guide(GuideInput(
                hints=step5_output.hints,
                problem_id=problem.problem_id,
                tree_state=tree_state
            ))

            # 更新引导树状态
            tree_state = guide_output.tree_state

            # 停机检查
            if guide_output.stop:
                break

            # 启动新Solver AI（并发，受max_concurrent限制）
            for solver_input in guide_output.new_solver_inputs:
                if len(tree_state.running_solvers) < max_concurrent:
                    # 并行启动：Solver AI跑的同时回到Pipe 1处理它的thinking
                    new_output = pipe_0_solver(solver_input)
                    first_output = new_output  # 下一轮处理新AI的thinking
                    tree_state.running_solvers.append(new_output.thinking.solver_ai_id)
                else:
                    break

    return tree_state


# ============================================================================
# 完整流程——解答吸收（原过程B，tell库增长循环）
# ============================================================================

def tell_library_growth_loop(
    solution_records: list[SolutionRecord],
    tell_library_path: str
) -> list[Tell]:
    """
    解答吸收——tell库增长循环的完整流程

    外部解答记录 → Parser AI → Telling AI → 步骤5分叉(解答吸收) → Parser AI建立新tell → tell库增长

    和解题引导的区别：
      - 步骤5没匹配到tell时，trace直接成为新tell→建立(tell,hint)
      - 不需要Guide AI（解答记录已有正确答案，不需要引导树）
      - Parser AI参考解题引导产出的孤悬trace作为启发

    POC验证：
      - VMS-16：Parser AI验证解答吸收
      - VMS-19：tell库持续增长闭环验证解题引导→解答吸收→解题引导
    """
    new_tells_all = []

    for record in solution_records:
        # 获取解题引导产出的孤悬trace（启发信号）
        orphan_traces = get_archived_orphan_traces()

        # ---- Pipe 1: Parser AI ----
        parser_output = pipe_1_parser(ParserInput(
            process="absorb",
            solution_record=record,
            orphan_traces=orphan_traces
        ))

        # ---- Pipe 2: Telling AI ----
        telling_output = pipe_2_telling(TellingInput(
            traces=parser_output.traces,
            tell_library_path=tell_library_path
        ))

        # ---- 步骤5分叉（解答吸收）----
        step5_output = step_5_branch(Step5Input(
            telling_output=telling_output,
            process="absorb"
        ))

        # 新tell存入对应目录的AGENTS.md
        if step5_output.new_tells:
            for new_tell in step5_output.new_tells:
                save_tell_to_agents_md(new_tell, tell_library_path)
                new_tells_all.append(new_tell)

    return new_tells_all


# ============================================================================
# 辅助函数（占位）
# ============================================================================

def archive_orphan_traces(traces: list[Trace]) -> None:
    """
    存档孤悬trace（按tell分类学分类）→ 启发解答吸收的Parser AI

    孤悬trace是解题引导中没匹配到tell的trace——它们没有hint，不能驱动引导树生长。
    但它们不是废物——按tell分类学分类积累，等待Parser AI从外部解答记录中
    验证后升级为正式tell。

    POC验证：
      - VMS-19：tell库持续增长闭环（存档是闭环的关键环节）
    """
    raise NotImplementedError("archive_orphan_traces 待实现")


def get_archived_orphan_traces() -> list[Trace]:
    """
    获取存档的孤悬trace（解答吸收的Parser AI的启发信号）

    解答吸收的Parser AI有两个输入：
      1. 已有tell——用于匹配
      2. 没匹配到tell的trace（解题引导产出的孤悬trace）——用于启发"从什么Level观察外部解答记录"

    POC验证：
      - VMS-16：Parser AI两个输入机制验证
      - VMS-19：tell库持续增长闭环
    """
    raise NotImplementedError("get_archived_orphan_traces 待实现")


def save_tell_to_agents_md(tell: Tell, library_path: str) -> None:
    """
    把新tell存入对应分类目录的AGENTS.md

    新tell来自解答吸收——Parser AI从外部解答记录中识别出trace，
    没匹配到已有tell，去特化后建立新(tell,hint)，存入对应目录的AGENTS.md。

    POC验证：
      - VMS-25：Tell存储方案（目录AGENTS.md）
    """
    raise NotImplementedError("save_tell_to_agents_md 待实现")
