"""
第六代系统数据结构定义

所有数据结构用dataclass形式化定义。
这些数据结构是Pipe之间传递的数据的类型。

来源：319号§1
"""

from dataclasses import dataclass, field
from typing import Optional, Literal, Any


# ============================================================================
# 基础数据结构
# ============================================================================

@dataclass
class Problem:
    """题目"""
    problem_id: str
    problem_text: str
    domain: Optional[str] = None        # 数论/代数/组合/分析/...
    answer: Optional[str] = None        # 已知答案（如果有）


@dataclass
class Hint:
    """提示Q——引导从一个处境移动到另一个处境的语义移动"""
    hint_id: str
    hint_text: str                      # 提示内容
    hint_level: int                     # Level梯度（0=最具体, N=最抽象）
    tell_id: str                        # 关联的tell


@dataclass
class Tell:
    """tell——从推理AI的thinking中读出的分叉信号"""
    tell_id: str
    branch_signal: str                  # 分叉信号：可以分叉但AI没分叉的位置
    branch_type: str                    # 分叉类型：翻译类型/操作路径类型/...
    unexplored_diagnosis: str           # 未探索诊断：AI为什么没走这条路
    direction_matching: str             # 方向匹配：从诊断到翻译方向的映射
    # 分类学位置
    domain: str                         # 第一层：domain（数论/代数/...）
    trace_type: Literal["local", "non_local", "global"]  # 第二层：trace类型
    segment_pattern: Optional[str] = None  # 第三层：段结构模式（非局部trace）
    specific_concept: Optional[str] = None # 第四层：具体概念


@dataclass
class Trace:
    """
    trace——从脉络的某个Level视图上识别出的思维模式

    trace是Parser AI的产出，Telling AI的输入。
    trace描述"推理AI在这里可以分叉但没分叉"（解题引导）
    或"解答者在这里做了某个操作"（解答吸收）。

    【自我审计要求——V5提示词§4，2026-08-10】
    Parser AI产出trace时，必须同时产出自我审计报告（9项）：
    1. 段划分完备性论证——为什么只有N段
    2. Level视图完备性论证——为什么只有N个Level视图
    3. trace完备性论证——逐Level论证为什么只有这些trace
    4. 7种反模式自查——逐一回答是/否
    5. 8种复杂情况逐一检查——逐一回答有/无
    6. trace去重检查——有没有重复或高度相似的trace
    7. trace可泛化性检查——逐个检查太具体/太抽象
    8. 不确定性承认——至少识别1个不确定性
    9. tell库对接预期——哪些能匹配已有tell/哪些是新类型

    来源：329号§8.3审计报告——VMS-28审计发现V4的反思太软，
    subagent可以说"我觉得没漏"就结束。V5把反思升级为9项硬要求。
    self_audit_report字段存储自我审计报告的文本。

    【FCA对应】（双轨术语——330号/双轨术语rule）
    trace对应FCA形式概念的**内涵** B——一个可识别的思维模式的属性集。
    trace去特化后存入tell库，对应FCA的**跨上下文概念**——在多个形式上下文中
    都出现的形式概念。trace的"可泛化性"对应概念的"跨上下文普适性"。
    注意：trace比FCA的内涵承载更多语义——trace强调"可泛化的思维模式"，
    这是工程人话的语义，FCA的"内涵"无法承载这个语义（双轨术语原则）。
    """
    trace_id: str
    level: int                          # 来自哪个Level视图（0=最细, N=最粗）
    trace_type: Literal["local", "non_local", "global"]
    pattern_description: str            # 模式描述
    source_segment_ids: list[str]       # 涉及的段ID（局部trace=1个段，非局部trace=多个段）
    # 解题引导特有
    is_branch_position: bool = False    # 是否是分叉位置本身的trace（仅解题引导）
    # 自我审计（V5提示词§4要求，2026-08-10）
    # self_audit_report: Optional[str] = None  # 自我审计报告文本（9项）
    # 注：self_audit_report是Parser AI产出的一部分，但不是每个trace一个——
    # 它是整批trace的审计报告，应该放在ParserOutput中而不是每个Trace中。


@dataclass
class MathSituation:
    """数学处境——引导树/解题树的节点"""
    node_id: str
    problem_id: str
    node_type: Literal["root", "internal", "leaf_success", "leaf_deadend", "leaf_truncated"]
    situation_text: str                 # 处境的自然语言描述
    depth: int                          # 在树中的深度
    path_from_root: list[str]           # 从根到本节点的路径（节点ID序列）
    parent_edge_key: Optional[str] = None


@dataclass
class TreeEdge:
    """树的边——一个提示Q"""
    edge_id: str
    from_node: str                      # 父节点ID
    to_node: str                        # 子节点ID
    hint: Hint                          # 边对应的提示Q
    level: int                          # 边的Level（局部trace=单节点级，非局部trace=段级）


@dataclass
class Thinking:
    """推理AI的thinking/trajectory——Pipe 0的输出，Pipe 1解题引导的输入"""
    solver_ai_id: str
    problem_id: str
    trajectory: str                     # 完整的thinking文本
    rounds: list[dict]                  # 按round分组的thinking
    entry_node_id: str                  # 从哪个节点进入树
    entry_hint: Optional[Hint] = None   # 进入时收到的方向Q（第一个AI为None）


@dataclass
class SolutionRecord:
    """
    外部解答记录——Pipe 1解答吸收的输入

    和Thinking的区别：解答记录是已完成的、正确的、通常线性的脉络；
    Thinking是未完成的、可能有错误的、可能有分叉的脉络。
    """
    record_id: str
    problem: Problem
    solution_text: str                  # 完整的解答文本
    is_verified: bool = True            # 外部解答记录默认是已验证的正确解答


# ============================================================================
# 脉络相关数据结构
# ============================================================================

@dataclass
class Vein:
    """
    脉络——从推理内容中分析出的思维脉络

    解题引导：从Thinking中分析 → 可能是有分叉的树/DAG
    解答吸收：从SolutionRecord中分析 → 通常是线性脉络

    【FCA对应】（双轨术语——330号/双轨术语rule）
    脉络对应FCA的**形式上下文** (G, M, I)：
    - G（对象集）= segments（脉络的段序列）
    - M（属性集）= 所有段特征的并集
    - I（关系）= 段具有某个特征
    脉络的segments构成形式上下文的对象集，格化就是在这个形式上下文上计算概念格。
    """
    vein_id: str
    source_id: str                      # Thinking.solver_ai_id 或 SolutionRecord.record_id
    source_type: Literal["thinking", "solution_record"]
    structure: Literal["linear", "tree", "dag"]  # 脉络结构
    segments: list["Segment"]           # 脉络的段序列
    branches: Optional[list["Branch"]] = None     # 分叉（仅解题引导的tree/dag结构）


@dataclass
class Segment:
    """
    段——脉络中的一个推理步骤或一段推理

    【FCA对应】（双轨术语——330号/双轨术语rule）
    段对应FCA形式上下文(G, M, I)中的**对象** g ∈ G。
    segment_features对应对象g的属性集 g' = {m ∈ M | (g, m) ∈ I}。
    """
    segment_id: str
    vein_id: str
    segment_text: str                   # 段内容
    segment_features: dict[str, Any]    # 段特征（用于FCA形式上下文的属性）
    order: int                          # 在脉络中的顺序


@dataclass
class Branch:
    """分叉——脉络中AI选了A没选B的位置（仅解题引导）"""
    branch_id: str
    vein_id: str
    at_segment_id: str                  # 在哪个段分叉
    chosen_path: str                    # AI选择的路径
    unchosen_paths: list[str]           # AI没选的路径


@dataclass
class LevelView:
    """
    Level视图——脉络在某个Level上的看法

    格化脉络后产出的所有有意义的Level视图。
    最细Level：每个段是一个节点
    最粗Level：整个脉络是一个节点
    中间Level：几个段合并成一段

    【FCA对应】（双轨术语——330号/双轨术语rule）
    Level视图对应FCA的**形式概念** (A, B)：
    - merged_segments对应**外延** A（extent）——合并的段集合（对象集）
    - view_features对应**内涵** B（intent）——这些段的共同特征（属性集）
    - level对应概念在概念格Hasse图中的深度
    最细Level（Level 0）对应最细概念——每个段是一个外延
    最粗Level对应最粗概念——所有段是一个外延
    中间Level对应中间概念——几个段合并成一个外延
    """
    view_id: str
    vein_id: str
    level: int                          # Level编号（0=最细, N=最粗）
    merged_segments: list[list[str]]    # 合并后的段分组（每组是一段）
    view_features: dict[str, Any]       # 这个Level视图的特征


# ============================================================================
# Pipe 0: Solver AI —— 输入输出
# ============================================================================

@dataclass
class SolverInput:
    """Pipe 0的输入"""
    problem: Problem
    path_text: str                      # 脉络文本（从根到当前节点的路径+方向Q）
    hint: Optional[Hint] = None         # 方向Q（第一个AI为None——裸做题）


@dataclass
class SolverOutput:
    """Pipe 0的输出"""
    thinking: Thinking
    final_status: Literal["solved", "deadend", "truncated", "ongoing"]
    final_situation: MathSituation      # AI终止时的终点节点


# ============================================================================
# Pipe 1: Parser AI —— 输入输出
# ============================================================================

@dataclass
class ParserInput:
    """Pipe 1的输入——可能是解题引导的Thinking或解答吸收的SolutionRecord"""
    # 解题引导和解答吸收的输入不同
    process: Literal["solve", "absorb"]   # solve=解题引导, absorb=解答吸收
    thinking: Optional[Thinking] = None         # 解题引导的输入
    solution_record: Optional[SolutionRecord] = None  # 解答吸收的输入
    # 解答吸收特有：解题引导产出的孤悬trace，用于启发"从什么Level观察外部解答记录"
    orphan_traces: Optional[list[Trace]] = None  # 仅解答吸收


@dataclass
class ParserOutput:
    """Pipe 1的输出"""
    traces: list[Trace]                 # 全Level Trace集合
    veins: list[Vein]                   # 分析出的脉络
    level_views: list[LevelView]        # 所有Level视图
    process: Literal["solve", "absorb"]   # solve=解题引导, absorb=解答吸收
    # 自我审计报告（V5提示词§4要求，2026-08-10）
    # 来源：329号§8.3审计报告——VMS-28审计发现V4的反思太软
    # self_audit_report: Optional[str] = None
    #   # Parser AI产出trace时必须同时产出自我审计报告（9项）：
    #   # 1.段划分完备性 2.Level视图完备性 3.trace完备性
    #   # 4.反模式自查 5.复杂情况检查 6.去重检查
    #   # 7.可泛化性检查 8.不确定性承认 9.tell库对接预期
    #   # 详见V5提示词§4


# ============================================================================
# Pipe 2: Telling AI —— 输入输出
# ============================================================================

@dataclass
class TellingInput:
    """Pipe 2的输入"""
    traces: list[Trace]                 # Pipe 1的输出
    tell_library_path: str              # Tell分类学目录路径


@dataclass
class TraceTellMatch:
    """一个trace→tell匹配"""
    trace_id: str
    tell_id: str
    confidence: float                   # 匹配置信度
    matched: bool                       # 是否匹配到tell


@dataclass
class TellingResult:
    """单个Telling AI的匹配结果"""
    telling_ai_id: str
    domain: str                         # 该Telling AI负责的domain
    matches: list[TraceTellMatch]       # 匹配结果


@dataclass
class TellingOutput:
    """Pipe 2的输出"""
    results: list[TellingResult]        # 各Telling AI的匹配结果（不需要汇总）
    unmatched_traces: list[Trace]       # 没匹配到tell的trace（孤悬trace）


# ============================================================================
# 步骤5分叉 —— 输入输出
# ============================================================================

@dataclass
class Step5Input:
    """步骤5的输入——Pipe 2的输出"""
    telling_output: TellingOutput
    process: Literal["solve", "absorb"]   # solve=解题引导, absorb=解答吸收


@dataclass
class Step5Output:
    """步骤5的输出"""
    process: Literal["solve", "absorb"]   # solve=解题引导, absorb=解答吸收
    # 解题引导的输出
    hints: Optional[list[Hint]] = None          # 匹配到tell后取的hint → 送入Pipe 3
    orphan_traces: Optional[list[Trace]] = None # 没匹配到tell的trace → 存档→启发解答吸收
    # 解答吸收的输出
    new_tells: Optional[list[Tell]] = None      # 新建立的tell → 存入AGENTS.md
    new_hints: Optional[list[Hint]] = None      # 新建立的hint → 关联新tell


# ============================================================================
# Pipe 3: Guide AI —— 输入输出
# ============================================================================

@dataclass
class TreeState:
    """引导树状态"""
    problem_id: str
    nodes: list[MathSituation]
    edges: list[TreeEdge]
    status: Literal["growing", "solved", "exhausted"]
    running_solvers: list[str]          # 正在运行的Solver AI ID


@dataclass
class GuideInput:
    """Pipe 3的输入"""
    hints: list[Hint]                   # 步骤5解题引导输出的hint
    problem_id: str
    tree_state: TreeState               # 当前引导树状态


@dataclass
class GuideOutput:
    """Pipe 3的输出"""
    new_edges: list[TreeEdge]           # 引导树新边
    new_solver_inputs: list[SolverInput]  # 新Solver AI的输入
    tree_state: TreeState               # 更新后的引导树状态
    stop: bool                          # 是否停机
