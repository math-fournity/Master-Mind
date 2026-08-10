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
        notes="格化+trace识别提示词V3。在V2基础上新增三个章节：第零部分'为什么我们要拿trace'（trace驱动引导树生长，trace层次决定引导树生长层次），第零点五部分'影响例子'（局部/非局部/全局trace被拿到后的不同影响——单步层面/策略层面/战略层面），第三点五部分'反模式'（7种：只看两极/把操作流水账当trace/机械合并/只识别操作型/描述太具体或太抽象/忽略跨域构造/不反思）。反模式2修正：trace是多level的，Level 0上每步可以有trace，问题不是'每步当trace'而是'把操作流水账当trace'。",
    ),
    Prompt(
        prompt_id="prompt_parser_grid_004",
        pipe="pipe_1_parser/step_2_grid_vein",
        version="V4",
        content_ref="324号§1",
        verification_poc="VMS-28",
        verification_status="verified",
        source_doc="324号——POC-VMS-28提示词V4",
        notes="格化+trace识别提示词V4。在V3基础上采用方案C：基础部分共用（FCA/Hasse图/trace定义/反模式/为什么/影响例子），新增第四点五部分'输入性质——树状vs线性'。附加章节A处理树状输入（过程A——分析推理AI上下文）：5步——识别树结构/拆成N条脉络/每条脉络独立格化/识别分叉位置trace/识别折返后语义关联trace。附加章节B处理线性输入（过程B——分析已有题目和解答）：直接格化，没有分叉位置trace和折返后语义关联trace。AI根据输入性质选读对应附加章节。"
             + "【VMS-28验证结果2026-08-10】成功——7个Level（6个中间Level）、23个非局部trace、识别出'强归纳+情况分析+鸽巢计数'组合策略。4个成功条件全部满足。但发现V4的§4'反思'是软的——subagent可以说'我觉得没漏'就结束。V5把反思升级为自我审计报告（9项硬要求）。详见329号§8.3审计报告。",
    ),
    Prompt(
        prompt_id="prompt_parser_grid_005",
        pipe="pipe_1_parser/step_2_grid_vein",
        version="V5",
        content_ref="第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/v5.md",
        verification_poc="VMS-28b",
        verification_status="verified",
        source_doc="329号§8.3审计报告——VMS-28审计发现V4反思太软",
        notes="格化+trace识别提示词V5。在V4完整版基础上，把§4'反思'升级为§4'自我审计报告'（9项硬要求）："
             "1.段划分完备性论证（为什么只有N段）"
             "2.Level视图完备性论证（为什么只有N个+FCA会找出哪些漏掉的）"
             "3.trace完备性论证（逐Level论证为什么只有这些trace）"
             "4.7种反模式自查（逐一回答是/否）"
             "5.8种复杂情况逐一检查（逐一回答有/无）"
             "6.trace去重检查"
             "7.trace可泛化性检查（逐个检查太具体/太抽象）"
             "8.不确定性承认（至少识别1个不确定性）"
             "9.tell库对接预期（哪些能匹配已有tell/哪些是新类型/哪些太宽泛/太狭窄）"
             "改进原因：VMS-28审计发现V4的反思允许subagent说'我觉得没漏'就结束，无法保证完备性。V5把反思变成硬要求——subagent必须论证为什么只找到这些，不允许'我觉得没有了'。"
             "【VMS-28b验证结果2026-08-10】V5改进有效——9项自我审计报告全部有效，其中2项极有效："
             "（1）审计项2中subagent自己发现'跨Case非相邻合并不在标准FCA的闭元素中'——FCA框架的局限性；"
             "（2）审计项8中subagent识别了4个不确定性——V4的subagent说'我都很确定'。"
             "V5的审计项9让subagent为tell库对接做了准备——预测了7个能匹配已有tell、4个新类型tell。"
             "详见329号§8.7。"
             "【FCA术语映射】（双轨术语——330号/双轨术语rule）"
             "格化=计算概念格B(G,M,I)；Level视图=形式概念(A,B)；"
             "段=对象g∈G；段特征=属性m∈M；"
             "merged_segments=外延A(extent)；view_features=内涵B(intent)；"
             "脉络=形式上下文(G,M,I)；trace=概念内涵B；"
             "去特化=缩放(scaling)；泛化=跨上下文概念普适性。"
             "注意：FCA语言用于术语规范化，不用于算法实现（方式A——AI做全部，不用FCA算法）。"
             "工程术语trace/tell/hint/格化/Level视图保持不变——它们承载系统设计意图的语义，"
             "FCA术语无法承载（双轨术语原则）。",
    ),
    Prompt(
        prompt_id="prompt_parser_grid_006",
        pipe="pipe_1_parser/step_2_grid_vein",
        version="V6",
        content_ref="第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/v6.md",
        verification_poc="VMS-28c",
        verification_status="pending",
        source_doc="330号FCA术语规范化+提示词自包含rule+双轨术语rule",
        notes="格化+trace识别提示词V6。在V5基础上，按提示词自包含原则"
             "（.devin/rules/six-prompt-selfcontained.md）和双轨术语原则"
             "（.devin/rules/six-dual-terminology.md），在提示词开头加入术语表——"
             "每个术语同时给出FCA标准定义（数学语言）和工程含义（人话）。"
             "10个术语：脉络(形式上下文)/段(对象)/段特征(属性)/格化(计算概念格)/"
             "Level视图(形式概念)/闭元素/Hasse图/trace(概念内涵)/"
             "去特化(缩放)/tell库(多上下文概念格)/可泛化(跨上下文普适性)。"
             "改进原因：V5提示词中'去特化'等术语被使用但没有定义——subagent不知道"
             "什么是'去特化'就被要求做去特化。V6在开头建术语表，确保自包含。"
             "待VMS-28c验证——用同一道题重跑，对比V5和V6的产出质量。",
    ),
    Prompt(
        prompt_id="prompt_parser_grid_007",
        pipe="pipe_1_parser/step_2_grid_vein",
        version="V7",
        content_ref="第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/v7.md",
        verification_poc="VMS-28c",
        verification_status="verified",
        source_doc="332号——机械化过程描述+规范化审计+程序验证（系统创新）",
        notes="格化+trace识别提示词V7。在V6基础上，按机械化过程描述原则"
             "（.devin/rules/six-mechanization-reference.md）新增三点："
             "(1)§1.5机械化过程参考——给出FCA Next Closure算法的完整步骤"
             "（构造形式上下文→定义闭包算子→按lectic order枚举所有闭元素→"
             "在每个闭元素上识别trace→输出完全格），标注'不要求你按此执行，"
             "但你的产出应达到此标准——犹如你执行过此过程了一般'；"
             "(2)审计项2升级为完全格元素清单——每个闭元素(A,B)都有入选/排除"
             "判定和理由，不是'你觉得漏了什么'的软反思，而是'每个格元素都有"
             "判定'的硬形式化验证。排除理由必须是形式化的（数学理由/泛化理由/"
             "冗余理由/平凡理由）；"
             "(3)§6结构化JSON输出——AI必须输出JSON（formal_context+"
             "closed_elements+ai_advantage_elements+traces），程序运行"
             "Next Closure算法验证完全格完备性。"
             "新增5个术语：机械化过程描述/规范化审计/程序验证完全格完备性/"
             "Next Closure算法/闭包运算。"
             "这是系统创新——机械化过程描述+规范化审计+程序验证作为提示词设计技术。"
             "FCA术语映射：机械化过程描述→提示词设计技术（无FCA对应）；"
             "规范化审计→提示词设计技术（无FCA对应）；"
             "程序验证→Next Closure算法验证B(G,M,I)完备性；"
             "Next Closure算法→Ganter & Wille 1999经典FCA算法；"
             "闭包运算→A'=共同属性，A''=属性闭包，A''=A则A是闭元素。"
             "立场声明：FCA语言用于机械化过程描述和程序验证，"
             "不要求AI按FCA算法执行——AI用直觉做（方式A），"
             "但产出被FCA算法验证。",
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
