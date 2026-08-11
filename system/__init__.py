"""
system——AI数学系统的物理实现代码。

两个入口：
- enter.py（入题）：外部解答进入系统，提炼tell/hint，tell库增长
- solve.py（解题）：系统解答题目，引导树展开

两个过程：
- 解题引导（process_solve）：推理探索→脉络分析→trace匹配→方向取用→引导展开
- 解答吸收（process_absorb）：解答录入→脉络分析→trace匹配→知识沉淀

参考依据：six/ 目录（架构描述，后续逐步放弃）
设计依据：第六代系统技术说明书/
"""

from .schema import (
    Problem, Hint, Tell, Trace,
    Thinking, MathSituation, TreeEdge, TreeState,
    SolutionRecord, Segment, Branch, Vein, LevelView,
    SolverInput, SolverOutput,
    AnalysisInput, AnalysisOutput,
    MatchInput, MatchOutput, TraceTellMatch,
    DirectionExtractionOutput,
    GuideExpansionInput, GuideExpansionOutput,
    KnowledgeDepositOutput,
    Session,
)
