"""
系统Schema——解题引导和解答吸收两个过程的数据结构定义。

两个过程是系统思维的两个入口：
- 解题引导（solve）：系统解答题目，在推理过程中引导新方向，引导树展开
- 解答吸收（absorb）：外部解答进入系统，系统从中提炼tell/hint，tell库增长

两个过程共享脉络分析和trace匹配两个阶段，用 process 字段区分输入来源。

命名约定：
- process="solve"  → 解题引导
- process="absorb" → 解答吸收
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
    domain: Optional[str] = None        # 数论/代数/组合/几何/分析/跨域
    answer: Optional[str] = None        # 已知答案（如果有）


@dataclass
class Hint:
    """方向提示——引导推理AI从一个处境移动到另一个处境的语义移动

    tell和hint是多对多关系（333号§2.1）：
    - 一个tell可以对应多个hint
    - 一个hint也可能被多个tell指到
    """
    hint_id: str
    hint_text: str                      # 提示内容
    hint_level: int                     # Level梯度（0=最具体, N=最抽象）
    tell_id: str                        # 关联的tell（多对多关系中的一个）


@dataclass
class Tell:
    """tell——从推理AI的thinking中读出的分叉信号的标准化描述

    tell的四个组成成分（000号文档）：
    1. branch_signal——分叉信号：可以分叉但AI没分叉的位置
    2. branch_type——分叉类型：翻译类型/操作路径类型/...
    3. unexplored_diagnosis——未探索诊断：AI为什么没走这条路
    4. direction_matching——方向匹配：从诊断到翻译方向的映射

    分类学位置（坐标轴上的坐标，336号——高Level概念是坐标轴不是点）：
    - domain：第一层坐标轴
    - segment_pattern：第二层坐标轴（段结构模式）
    - specific_concept：domain × segment_pattern 的交叉

    验证状态（333号§6.4）：
    - mathematics：来自数学证明的实际案例
    - system：来自系统运行的实际案例
    - none：没有实际案例，只是提到了方向
    """
    tell_id: str
    branch_signal: str
    branch_type: str
    unexplored_diagnosis: str
    direction_matching: str
    # 分类学位置
    domain: str                         # 数论/代数/组合/几何/分析/跨域
    segment_pattern: Optional[str] = None    # 段结构模式
    specific_concept: Optional[str] = None   # 具体概念
    case_source: Literal["mathematics", "system", "none"] = "none"


@dataclass
class Trace:
    """trace——从脉络的某个Level视图上识别出的思维模式

    trace是脉络分析阶段的产出，trace匹配阶段的输入。
    trace描述"推理AI在这里可以分叉但没分叉"（解题引导）
    或"解答者在这里做了某个操作"（解答吸收）。

    观察Level是参数不是属性（08号分类学v2修正）：
    - local：局部trace，来自单个段
    - non_local：非局部trace，跨多个段
    - global：全局trace，整个脉络层面
    """
    trace_id: str
    level: int                          # 来自哪个Level视图（0=最细, N=最粗）
    trace_type: Literal["local", "non_local", "global"]
    pattern_description: str            # 模式描述
    source_segment_ids: list[str]       # 涉及的段ID
    is_branch_position: bool = False    # 分叉位置本身的trace（仅解题引导）


# ============================================================================
# 脉络相关数据结构（两个过程共享）
# ============================================================================

@dataclass
class Segment:
    """段——脉络中的一个推理步骤或一段推理"""
    segment_id: str
    segment_text: str
    segment_features: dict[str, Any]    # 段特征（用于格化的属性）
    order: int                          # 在脉络中的顺序


@dataclass
class Branch:
    """分叉——脉络中AI选了A没选B的位置（仅解题引导）"""
    branch_id: str
    at_segment_id: str
    chosen_path: str
    unchosen_paths: list[str]


@dataclass
class Vein:
    """脉络——从推理内容中分析出的思维脉络

    解题引导：从Thinking中分析 → 可能是有分叉的树/DAG
    解答吸收：从SolutionRecord中分析 → 通常是线性脉络
    """
    vein_id: str
    source_id: str                      # 推理AI的ID 或 解答记录的ID
    source_type: Literal["thinking", "solution_record"]
    structure: Literal["linear", "tree", "dag"]
    segments: list[Segment]
    branches: Optional[list[Branch]] = None     # 仅解题引导


@dataclass
class LevelView:
    """Level视图——脉络在某个Level上的看法（格化产物）

    最细Level：每个段是一个节点
    最粗Level：整个脉络是一个节点
    中间Level：几个段合并成一段
    """
    view_id: str
    vein_id: str
    level: int                          # 0=最细, N=最粗
    merged_segments: list[list[str]]    # 合并后的段分组
    view_features: dict[str, Any]       # 这个Level视图的特征


# ============================================================================
# 解题引导的输入输出
# ============================================================================

@dataclass
class Thinking:
    """推理AI的thinking——推理探索阶段的产出，脉络分析阶段的输入"""
    solver_ai_id: str
    problem_id: str
    trajectory: str                     # 完整思维过程文本
    rounds: list[dict]                  # 按round分组
    entry_node_id: str                  # 从引导树哪个节点进入
    entry_hint: Optional[Hint] = None   # 进入时收到的方向（第一个AI为None）


@dataclass
class MathSituation:
    """数学处境——引导树的节点"""
    node_id: str
    problem_id: str
    node_type: Literal["root", "internal", "leaf_success", "leaf_deadend", "leaf_truncated"]
    situation_text: str
    depth: int
    path_from_root: list[str]


@dataclass
class TreeEdge:
    """引导树的边——一个方向提示"""
    edge_id: str
    from_node: str
    to_node: str
    hint: Hint
    level: int                          # 局部trace=单节点级，非局部trace=段级


@dataclass
class TreeState:
    """引导树状态"""
    problem_id: str
    nodes: list[MathSituation]
    edges: list[TreeEdge]
    status: Literal["growing", "solved", "exhausted"]
    running_solvers: list[str]          # 正在运行的推理AI的ID


# ============================================================================
# 解答吸收的输入输出
# ============================================================================

@dataclass
class SolutionRecord:
    """外部解答记录——解答录入阶段的产出，脉络分析阶段的输入

    和Thinking的区别：解答记录是已完成的、正确的、通常线性的脉络；
    Thinking是未完成的、可能有错误的、可能有分叉的脉络。
    """
    record_id: str
    problem: Problem
    solution_text: str                  # 完整解答文本
    is_verified: bool = True            # 外部解答记录默认是已验证的正确解答


# ============================================================================
# 阶段间传递的数据包
# ============================================================================

# --- 脉络分析阶段（两个过程共享，用process区分） ---

@dataclass
class AnalysisInput:
    """脉络分析阶段的输入"""
    process: Literal["solve", "absorb"]     # solve=解题引导, absorb=解答吸收
    thinking: Optional[Thinking] = None             # 解题引导的输入
    solution_record: Optional[SolutionRecord] = None  # 解答吸收的输入
    orphan_traces: Optional[list[Trace]] = None     # 解答吸收特有：孤悬trace启发信号


@dataclass
class AnalysisOutput:
    """脉络分析阶段的产出"""
    traces: list[Trace]                 # 全Level trace集合
    veins: list[Vein]                   # 分析出的脉络
    level_views: list[LevelView]        # 所有Level视图
    process: Literal["solve", "absorb"]


# --- trace匹配阶段（两个过程共享） ---

@dataclass
class MatchInput:
    """trace匹配阶段的输入"""
    traces: list[Trace]
    tell_library_path: str


@dataclass
class TraceTellMatch:
    """一个trace→tell匹配结果"""
    trace_id: str
    tell_id: str
    confidence: float
    matched: bool


@dataclass
class MatchOutput:
    """trace匹配阶段的产出"""
    matches: list[TraceTellMatch]       # 匹配结果
    unmatched_traces: list[Trace]       # 没匹配到tell的trace（孤悬trace）


# --- 方向取用阶段（仅解题引导） ---

@dataclass
class DirectionExtractionOutput:
    """方向取用阶段的产出

    匹配到tell的trace → 从tell取hint（多对多，一个tell可对应多个hint全取）
    没匹配到tell的trace → 孤悬trace，存档后启发解答吸收
    """
    hints: list[Hint]                   # 从匹配到的tell取出的方向提示
    orphan_traces: list[Trace]          # 没匹配到tell的trace → 存档 → 启发解答吸收


# --- 引导展开阶段（仅解题引导） ---

@dataclass
class SolverInput:
    """推理探索阶段的输入"""
    problem: Problem
    path_text: str                      # 脉络文本（从根到当前节点的路径+方向）
    hint: Optional[Hint] = None         # 方向（第一个AI为None——裸做题）


@dataclass
class SolverOutput:
    """推理探索阶段的产出"""
    thinking: Thinking
    final_status: Literal["solved", "deadend", "truncated", "ongoing"]
    final_situation: MathSituation      # AI终止时的终点节点


@dataclass
class GuideExpansionInput:
    """引导展开阶段的输入"""
    hints: list[Hint]                   # 方向取用阶段产出的hint
    problem_id: str
    tree_state: TreeState               # 当前引导树状态


@dataclass
class GuideExpansionOutput:
    """引导展开阶段的产出"""
    new_edges: list[TreeEdge]           # 引导树新边
    new_solver_inputs: list[SolverInput]  # 新推理AI的输入
    tree_state: TreeState               # 更新后的引导树状态
    stop: bool                          # 是否停机


# --- 知识沉淀阶段（仅解答吸收） ---

@dataclass
class KnowledgeDepositOutput:
    """知识沉淀阶段的产出

    解答吸收中没匹配到tell的trace可以直接成为新tell——
    因为外部解答记录是完整正确解答，trace被验证过。
    解题引导的trace是探索中的，可能走对了也可能走错了，不能直接升级。
    """
    new_tells: list[Tell]               # 新建立的tell → 存入tell库
    new_hints: list[Hint]               # 新建立的hint → 关联新tell


# ============================================================================
# 会话——一次入题或一次解题在数据库中的记录
# ============================================================================

@dataclass
class Session:
    """会话——一次入题或一次解题的数据库记录

    一次入题 = 一条Session记录（type=absorb）
    一次解题 = 一条Session记录（type=solve）

    devin cli实例的启动目录在 `palyground/` 下，按过程/阶段/题目ID隔离：
    - 解题引导：palyground/solve/{stage}/{problem_id}/
    - 解答吸收：palyground/absorb/{stage}/{problem_id}/
    stage是阶段名（inference_explore/vein_analysis/trace_match/guide_expand/knowledge_deposit）

    数据库表设计是迭代的——当前只定义最小字段，后续随系统实现推进逐步增加。
    """
    session_id: str                     # 会话唯一ID
    session_type: Literal["absorb", "solve"]    # absorb=入题, solve=解题
    problem_id: str                     # 关联的题目ID
    status: Literal["running", "completed", "failed"] = "running"
    started_at: Optional[str] = None    # 启动时间（ISO格式）
    completed_at: Optional[str] = None  # 完成时间（ISO格式）
    working_directory: Optional[str] = None    # devin cli启动目录的绝对路径
    result_summary: Optional[str] = None       # 会话结果摘要
