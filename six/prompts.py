"""
第六代系统提示词索引

六代系统势必积累很多提示词，用于启发AI完成相关的工作。
提示词是系统的核心资产，和代码同等重要。

每个提示词有：
- prompt_id：提示词ID
- 用于哪个Pipe/子pipe：对应six/pipes.py中的函数
- 版本：V1/V2/V3
- 内容：提示词文本（或指向内容的位置）
- 验证状态：由哪个POC验证，验证结果如何
- 来源文档：提示词的设计来源

来源：321号——第六代系统设计认知·提示词是核心资产
"""

from dataclasses import dataclass, field
from typing import Optional, Literal


@dataclass
class Prompt:
    """
    提示词——启发AI完成相关工作的文本

    提示词是六代系统的核心资产，和代码同等重要。
    每个Pipe/子pipe的AI都需要提示词来启发工作。
    提示词不是一次定型的——POC验证后改进，反射后改进，使用经验积累后改进。
    """
    prompt_id: str                         # 提示词ID
    pipe: str                              # 用于哪个Pipe/子pipe
    version: str                           # 版本号（V1/V2/V3）
    content_ref: str                       # 提示词内容的位置（文件路径或文档章节）
    verification_poc: Optional[str] = None # 由哪个POC验证
    verification_status: Literal["pending", "verified", "failed", "partial"] = "pending"
    source_doc: Optional[str] = None       # 提示词的设计来源文档
    notes: Optional[str] = None            # 备注（改进原因等）


# ============================================================================
# 提示词清单
# ============================================================================

PROMPTS = [
    Prompt(
        prompt_id="prompt_solver_001",
        pipe="pipe_0_solver",
        version="第五代已验证",
        content_ref="第五代系统技术说明书/03-引导树闭环.md",
        verification_poc="POC-VMS-0到VMS-8",
        verification_status="verified",
        source_doc="第五代系统技术说明书",
        notes="Solver AI的提示词=脉络文本+方向Q。第五代已验证，第六代继承。",
    ),
    Prompt(
        prompt_id="prompt_parser_grid_001",
        pipe="pipe_1_parser/step_2_grid_vein",
        version="V1",
        content_ref="320号§2.3",
        verification_poc="VMS-28",
        verification_status="pending",
        source_doc="320号——POC-VMS-28执行方案",
        notes="格化+trace识别提示词V1。包含FCA闭包算子概念但不运行FCA算法。待VMS-28验证。",
    ),
    Prompt(
        prompt_id="prompt_parser_grid_002",
        pipe="pipe_1_parser/step_2_grid_vein",
        version="V2",
        content_ref="322号§1",
        verification_poc="VMS-28",
        verification_status="pending",
        source_doc="322号——POC-VMS-28提示词V2",
        notes="格化+trace识别提示词V2。用FCA和Hasse图启发AI直觉，举8段划分例子，列8种复杂情况（嵌套/跨域构造/反证法+归约/构造-分析-排除/探索-诊断-修复/辅助函数+非负性/模分析无尽追逐/段间依赖），要求AI反思可能漏掉的Level视图和trace。比V1更丰富。",
    ),
    Prompt(
        prompt_id="prompt_parser_grid_003",
        pipe="pipe_1_parser/step_2_grid_vein",
        version="V3",
        content_ref="323号§1",
        verification_poc="VMS-28",
        verification_status="pending",
        source_doc="323号——POC-VMS-28提示词V3",
        notes="格化+trace识别提示词V3。在V2基础上新增三个章节：第零部分'为什么我们要拿trace'（trace驱动引导树生长，trace层次决定引导树生长层次），第零点五部分'影响例子'（局部/非局部/全局trace被拿到后的不同影响——单步层面/策略层面/战略层面），第三点五部分'反模式'（7种：只看两极/把每步当trace/机械合并/只识别操作型/描述太具体或太抽象/忽略跨域构造/不反思）。",
    ),
    Prompt(
        prompt_id="prompt_parser_analyze_001",
        pipe="pipe_1_parser/step_1_analyze_vein",
        version="待设计",
        content_ref="待设计",
        verification_poc="VMS-14",
        verification_status="pending",
        source_doc="315号——完整工作流",
        notes="分析脉络提示词。过程A和过程B可能需要不同版本。",
    ),
    Prompt(
        prompt_id="prompt_telling_001",
        pipe="pipe_2_telling",
        version="待设计",
        content_ref="待设计",
        verification_poc="VMS-15",
        verification_status="pending",
        source_doc="311号——并发Telling AI方案",
        notes="Telling AI匹配提示词。每个Telling AI在对应分类目录中遍历tell做匹配。",
    ),
    Prompt(
        prompt_id="prompt_step5a_archive_001",
        pipe="step_5_branch/过程A",
        version="待设计",
        content_ref="待设计",
        verification_poc="VMS-19",
        verification_status="pending",
        source_doc="315号——完整工作流§6.2",
        notes="存档孤悬trace提示词。按tell分类学分类积累。",
    ),
    Prompt(
        prompt_id="prompt_step5b_new_tell_001",
        pipe="step_5_branch/过程B",
        version="待设计",
        content_ref="待设计",
        verification_poc="VMS-16",
        verification_status="pending",
        source_doc="315号——完整工作流§6.2.1",
        notes="建立新tell提示词。从外部解答记录中识别trace，没匹配到tell的trace去特化后建立新(tell,hint)。",
    ),
    Prompt(
        prompt_id="prompt_guide_001",
        pipe="pipe_3_guide",
        version="待设计",
        content_ref="待设计",
        verification_poc="VMS-17",
        verification_status="pending",
        source_doc="315号——完整工作流§6.5/6.6",
        notes="Guide AI引导树填充提示词。判断hint在引导树哪个Level开新边。",
    ),
]


# ============================================================================
# 提示词设计认知
# ============================================================================

PROMPT_DESIGN_PRINCIPLE = {
    "核心认知": "提示词是六代系统的核心资产，和代码同等重要",
    "来源": "321号——用户指出'六代系统势必积累很多提示词，用于启发AI完成相关的工作'",
    "必然性": [
        "每个Pipe都需要提示词——Solver/Parser/Telling/Guide四个Pipe的AI都需要提示词",
        "每个子pipe也需要提示词——解放思想原则下Pipe会拆分为子pipe",
        "反射会产生新提示词——反射原则下系统改进提示词产生新版本",
        "不同过程需要不同提示词——过程A和过程B的Parser AI用不同提示词",
        "不同Level需要不同提示词——局部trace和非局部trace识别可能需要不同提示词",
    ],
    "和算法的关系": {
        "纯算法": "有明确数学定义、可系统化枚举的操作（如FCA格遍历）",
        "纯提示词": "需要直觉判断、语义理解的操作（如AI做格化+trace识别）",
        "提示词+算法": "先用提示词做大部分，再用算法验证补漏（如VMS-30方式C）",
        "六代系统的倾向": "优先用提示词——因为AI的智能性很强，算法用于验证和补漏",
    },
    "管理需求": {
        "积累": "每个Pipe/子pipe的提示词需要记录和积累，演进过程需要记录",
        "管理": "提示词和Pipe/POC的对应关系需要管理，版本需要管理",
        "版本化": "每个版本记录版本号/内容/改进原因/验证状态/使用效果，旧版本保留用于对比和回退",
        "是代码的一部分": "提示词和代码一起版本化管理，可通过references.py索引查到",
    },
    "和设计原则的关系": {
        "解放思想": "提示词是'多种方式'中的一种——和算法是平等的实现方式",
        "反射": "提示词是反射的主要改进对象——运行中发现效果不够好就改进提示词",
        "交汇点": "提示词是反射和解放思想的交汇点——解放思想产生V1，反射改进为V2",
    },
}
