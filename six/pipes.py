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

    【FCA立场声明】（双轨术语——330号/双轨术语rule）
      FCA语言用于术语规范化，不用于算法实现。
      step_2_grid_vein()选方式A——用提示词驱动AI做格化，不直接实现FCA的
      Next Closure/In-Close/Close-by-One算法。但提示词中用的术语（格化、
      Level视图、闭元素等）用FCA的数学定义来规范化，确保术语的精确性。
      这不是矛盾——FCA的数学框架提供了精确的术语体系，即使算法不直接使用。
      工程术语trace/tell/hint/格化/Level视图保持不变——它们承载系统设计意图
      的语义，FCA术语无法承载（双轨术语原则）。

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
      - VMS-28b：V5提示词验证——2026-08-10验证成功（V5改进有效）
        结果：9项自我审计报告全部有效，其中2项极有效：
        （1）审计项2中subagent自己发现"跨Case非相邻合并不在标准FCA的
        闭元素中"——FCA框架的局限性，但方式A不受此限制
        （2）审计项8中subagent识别了4个不确定性——V4说"我都很确定"
        V5的审计项9让subagent为tell库对接做了准备。
        step_2_grid_vein()的提示词应该用V5（或V6加术语表后）。
        详见329号§8.7。
      - VMS-28c：V7提示词验证——2026-08-10验证
        V7=V6+机械化过程描述+规范化审计+JSON输出（系统创新）。
        闭元素完备性：程序运行Next Closure算法验证完全格B(G,M,I)共17个
        闭元素，AI声称17个全部正确，0遗漏0错误，闭元素完备性得分100%。
        3个AI优势元素（跨Case非相邻合并）经程序验证确实不是FCA闭元素。
        trace完备性：V5 vs V7逐个对比发现V7漏掉了3个有价值的跨闭元素
        元模式trace（特别是"关键变量x贯穿整个证明"——V4/V5最有价值trace
        之一）。V7的AI优势元素定义太窄——只覆盖跨Case非相邻合并，没覆盖
        跨闭元素元模式。需要V8改进。
        verify_lattice_completeness.py应成为Pipe 1标准审计工具
        （验证闭元素完备性，不验证trace完备性）。
        详见332号§8.1-8.10。
      - VMS-28d：V8提示词验证——2026-08-10验证
        V8=V7+AI优势元素扩展（新增cross_element_meta_pattern类型）。
        闭元素完备性：100%（15/15），与V7一致。
        4个AI优势元素（1 cross_case_merge + 3 cross_element_meta_pattern）。
        trace完备性修复：V7漏掉的3个trace中2个完全补回
        （"x贯穿整个证明"列为最有价值trace第2名，
         "aₙ作为跳过障碍工具"列为最有价值trace第1名），
        1个部分补回（"归纳递降三种方式"识别了跨闭元素角色但没区分递降幅度）。
        6条成功条件全部满足。
        step_2_grid_vein()的提示词应该用V8。
        详见332号§8.11。

        **运行时闭环反馈机制**（系统创新的设计延伸）：
        verify_lattice_completeness.py不只是研发工具，也是运行时组件。
        Pipe 1每次产出JSON后，程序验证完备性：
        - 完备性得分≥80% → 通过，进入Pipe 2
        - 得分<80% → 反馈遗漏列表给Parser AI，请求补充（最多2轮）
        - 遗漏的都是平凡合并（B为空集或只有1个特征）→ 直接通过
        反馈只给遗漏列表，不给建议判定——AI自己判断入选/排除。
        程序只验证完备性，不判断语义价值。
        详见.devin/rules/six-mechanization-reference.md §5。
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
