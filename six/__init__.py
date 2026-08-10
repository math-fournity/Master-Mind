"""
第六代AI数学系统架构

本包是第六代AI数学系统的形式化架构定义。

四个Pipe：
  Pipe 0: Solver AI   —— 推理探索
  Pipe 1: Parser AI   —— 提取格化全Level Trace
  Pipe 2: Telling AI  —— 并发trace→tell匹配
  Pipe 3: Guide AI    —— 引导树填充

两个过程：
  过程A：分析推理AI上下文（Grove核心循环）
  过程B：分析外部解答记录（tell库增长循环）

步骤1-3在过程A和过程B中相似但不完全相同（输入性质不同）。
步骤4在过程A和过程B中完全相同。
步骤5在过程A和过程B中不同。

来源文档：
  - 319号：形式化定义（本包的源文档）
  - 318号：Pipe命名与AI命名
  - 316号：理想化工作过程
  - 315号：完整工作流+完备性检查
  - 314号：三个必须着力解决的问题
  - 311号：并发Telling AI方案
  - 304号：FCA与工程方案对应
"""

from .types import (
    # 基础数据结构
    Problem, Hint, Tell, Trace, MathSituation, TreeEdge,
    Thinking, SolutionRecord,
    # 脉络相关
    Vein, Segment, Branch, LevelView,
    # Pipe 0
    SolverInput, SolverOutput,
    # Pipe 1
    ParserInput, ParserOutput,
    # Pipe 2
    TellingInput, TellingResult, TraceTellMatch, TellingOutput,
    # 步骤5
    Step5Input, Step5Output,
    # Pipe 3
    GuideInput, TreeState, GuideOutput,
)
from .pipes import (
    pipe_0_solver,
    pipe_1_parser,
    pipe_2_telling,
    step_5_branch,
    pipe_3_guide,
)
from .loops import (
    grove_core_loop,
    tell_library_growth_loop,
    archive_orphan_traces,
    get_archived_orphan_traces,
    save_tell_to_agents_md,
)
from .references import DOCS, TYPE_REFS, POCS, CORE_PROBLEMS, FUNDAMENTAL_INSIGHT

__all__ = [
    # 基础数据结构
    "Problem", "Hint", "Tell", "Trace", "MathSituation", "TreeEdge",
    "Thinking", "SolutionRecord",
    # 脉络相关
    "Vein", "Segment", "Branch", "LevelView",
    # Pipe 0
    "SolverInput", "SolverOutput",
    # Pipe 1
    "ParserInput", "ParserOutput",
    # Pipe 2
    "TellingInput", "TellingResult", "TraceTellMatch", "TellingOutput",
    # 步骤5
    "Step5Input", "Step5Output",
    # Pipe 3
    "GuideInput", "TreeState", "GuideOutput",
    # Pipe函数
    "pipe_0_solver", "pipe_1_parser", "pipe_2_telling",
    "step_5_branch", "pipe_3_guide",
    # 流程函数
    "grove_core_loop", "tell_library_growth_loop",
    "archive_orphan_traces", "get_archived_orphan_traces",
    "save_tell_to_agents_md",
    # 研发文档索引（晾衣架）
    "DOCS", "TYPE_REFS", "POCS", "CORE_PROBLEMS", "FUNDAMENTAL_INSIGHT",
]
