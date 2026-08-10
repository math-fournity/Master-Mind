"""
第六代系统Pipe接口定义

四个Pipe函数 + 步骤5分叉函数。
每个函数目前只有签名和docstring，实现待POC验证后填充。

来源：319号§1
"""

from .types import (
    # Pipe 0
    SolverInput, SolverOutput,
    # Pipe 1
    ParserInput, ParserOutput,
    # Pipe 2
    TellingInput, TellingOutput,
    # 步骤5
    Step5Input, Step5Output,
    # Pipe 3
    GuideInput, GuideOutput,
)


# ============================================================================
# Pipe 0: Solver AI —— 推理探索
# ============================================================================

def pipe_0_solver(input: SolverInput) -> SolverOutput:
    """
    Pipe 0: Solver AI —— 推理探索

    职责：
      - 推理AI对题目探索，产生thinking/trajectory
      - 不需要停下接受提示——持续推理，走到哪里都可以
      - 自然终止（token用尽/证毕/崩溃）后输出终点节点

    并行关系：
      - Solver AI在thinking的同时，Parser AI就从thinking中增量提取trace
      - 多个Solver AI可以并发（每个走一个方向）

    停机条件：
      - 某条脉络到达正确解答 → final_status="solved"
      - 走不通 → final_status="deadend"
      - token用尽/崩溃 → final_status="truncated"
      - 还在跑 → final_status="ongoing"

    POC验证状态：
      - 第五代已验证核心循环（POC-VMS-0到VMS-8）
      - 第六代继承，不需要重新验证
    """
    raise NotImplementedError("Pipe 0 Solver AI 待实现")


# ============================================================================
# Pipe 1: Parser AI —— 提取格化全Level Trace
# ============================================================================

def pipe_1_parser(input: ParserInput) -> ParserOutput:
    """
    Pipe 1: Parser AI —— 提取格化全Level Trace

    核心能力：提取格化全Level Trace——在过程A和过程B中都用。

    步骤1-3在过程A和过程B中相似但不完全相同：

    ┌─────────────────────────────────────────────────────────────────────┐
    │ 步骤1：分析脉络                                                      │
    │   过程A：从Thinking中分析 → 可能是有分叉的树/DAG                      │
    │   过程B：从SolutionRecord中分析 → 通常是线性脉络                      │
    │                                                                     │
    │ 步骤2：格化脉络 → 所有Level视图                                       │
    │   过程A：在有分叉的脉络上格化 → 多个分支分别格化                       │
    │   过程B：在线性脉络上格化                                             │
    │                                                                     │
    │ 步骤3：识别trace（全Level）                                           │
    │   过程A：分叉位置本身可能就是trace（AI选了A没选B）                     │
    │         → is_branch_position=True                                   │
    │   过程B：不需要考虑分叉位置                                           │
    │         → is_branch_position=False                                  │
    └─────────────────────────────────────────────────────────────────────┘

    并行关系：
      - 和Solver AI并行——Solver AI在thinking的同时Parser AI就增量提取trace
      - 过程A和过程B可以并行——系统运行过程A的同时间歇运行过程B

    依赖：
      - 步骤2的格化方法由VMS-28/29/30的POC验证结果决定
        （方式A：AI做全部 / 方式B：脚本做格化 / 方式C：AI做+FCA验证）

    POC验证状态：
      - VMS-11：非局部trace识别能力
      - VMS-12：脉络格化能力
      - VMS-14：完整管线（步骤1-4）
      - VMS-27：已有产物二次分析
      - VMS-28：格化方法方式A——2026-08-10验证成功
        结果：7个Level（6个中间Level）、23个非局部trace、识别出
        "强归纳+情况分析+鸽巢计数"组合策略。4个成功条件全部满足。
        step_2_grid_vein()选方式A——用提示词驱动AI做格化，不用FCA算法。
        审计发现：V4提示词的§4"反思"太软——subagent可以说"我觉得没漏"
        就结束。V5把反思升级为自我审计报告（9项硬要求）。
        详见329号§8.3审计报告。
      - VMS-28b：V5提示词验证——待执行（用同一道题重跑，对比V4和V5）
      - VMS-29/30：方式B/C——方式A已成功，B/C优先级降低
    """
    raise NotImplementedError("Pipe 1 Parser AI 待实现")


# ============================================================================
# Pipe 2: Telling AI —— 并发trace→tell匹配
# ============================================================================

def pipe_2_telling(input: TellingInput) -> TellingOutput:
    """
    Pipe 2: Telling AI —— 并发trace→tell匹配

    步骤4：在每个对应分类目录中启动Devin CLI实例
          加载该目录AGENTS.md，遍历tell做匹配

    过程A和过程B完全相同——Telling AI不关心trace来自哪里。

    并发实现：
      - 每个Telling AI是一个Devin CLI实例
      - 在对应分类目录中启动
      - 加载该目录的AGENTS.md
      - 以可审计方式遍历tell做匹配
      - 各Telling AI独立返回结果，不需要汇总

    输出处理：
      - 匹配到tell的trace → 取hint（过程A）或确认匹配（过程B）
      - 没匹配到tell的trace → 孤悬trace
        - 过程A：存档→启发过程B的Parser AI
        - 过程B：去特化→建立新(tell,hint)→存入AGENTS.md

    POC验证状态：
      - VMS-15：并发Telling AI
      - VMS-25：Tell存储方案（目录AGENTS.md）
    """
    raise NotImplementedError("Pipe 2 Telling AI 待实现")


# ============================================================================
# 步骤5分叉——不是独立Pipe，是Parser AI和Guide AI的后续职责
# ============================================================================

def step_5_branch(input: Step5Input) -> Step5Output:
    """
    步骤5分叉——过程A和过程B不同

    ┌──────────────────────────────┬──────────────────────────────┐
    │ 过程A（推理AI上下文）          │ 过程B（外部解答记录）          │
    │                              │                              │
    │ 匹配到tell:                   │ 匹配到tell:                   │
    │   取hint → 送入Pipe 3         │   确认匹配（不需要新建）        │
    │                              │                              │
    │ 没匹配到tell:                 │ 没匹配到tell:                 │
    │   [Parser AI]存档孤悬trace    │   [Parser AI]去特化trace       │
    │   （按tell分类学分类）         │   建立新(tell,hint)            │
    │   → 启发过程B的Pipe 1         │   存入对应目录AGENTS.md         │
    │                              │   → tell库增长                 │
    └──────────────────────────────┴──────────────────────────────┘

    为什么过程B的trace可以直接成为tell：
      外部解答记录是完整正确解答，trace被验证过。
      过程A的trace是探索中的，可能走对了也可能走错了，
      不能直接升级为tell，只能存档待Parser AI验证。

    POC验证状态：
      - VMS-16：Parser AI（过程B的建立新tell）
      - VMS-19：tell库持续增长闭环（过程A→过程B→过程A）
    """
    raise NotImplementedError("步骤5分叉 待实现")


# ============================================================================
# Pipe 3: Guide AI —— 引导树填充
# ============================================================================

def pipe_3_guide(input: GuideInput) -> GuideOutput:
    """
    Pipe 3: Guide AI —— 引导树填充

    职责：
      1. 判断每个hint在引导树哪个Level开新边
         - 局部trace的hint → 在单节点开新边
         - 非局部trace的hint → 在段级位置开新边
      2. 在引导树上开新边
      3. 构造脉络（从根到新边的路径+方向Q）
      4. 启动新Solver AI
      5. 检查停机条件

    停机条件：
      - 某条脉络到达正确解答 → stop=True, tree_state.status="solved"
      - 所有方向都探索完但没有找到正确解答 → stop=True, tree_state.status="exhausted"
      - 否则 → stop=False, 继续循环

    并发管理：
      - 管理多个并发Solver AI实例
      - 分配额度（MAX_CONCURRENT）
      - 收集结果

    POC验证状态：
      - VMS-17：端到端工作流（Guide AI是其中一环）
      - VMS-18：引导树妖娆生长（Guide AI的产出）
      - VMS-26：两棵树Level问题（Guide AI的Level判断）
    """
    raise NotImplementedError("Pipe 3 Guide AI 待实现")
