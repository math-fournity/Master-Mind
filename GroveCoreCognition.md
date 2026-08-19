# GroveCoreCognition.md — Grove核心循环与辅助智能体认知（完整版）

> **来源**：从 AGENTS.md 原始第7-311行外移（2026-08-19瘦身工程，392号方案）。AGENTS.md中保留精炼版+指向本文件的索引行。
> **定位**：Grove核心循环、双重角色、辅助智能体JD、7个场景SOP、角色切换细节、反模式/正确模式展开的完整版。
> **加载时机**：当你要做Grove核心循环相关工作（设计/实现/迭代系统、运行实验、检查循环完整性、理解辅助智能体角色和SOP）时，必须用read工具全文加载本文件。AGENTS.md中的精炼版只保留核心认知，本文件包含完整细节。
> **AGENTS.md索引**：AGENTS.md "外部文档索引"节有指向本文件的索引行。AGENTS.md Grove节也有指向本文件的索引行。

---

## Grove核心循环与辅助智能体认知（跨AI共享 · 最高认知优先级）

> **本repo与Grove repo（`/data/master-mind-glm5.2-grove/`）共享同一套核心循环认知。两个AI各自在自己的repo和数据库中独立工作，但遵循同一套Grove核心循环、双重角色、辅助智能体JD和场景触发式SOP。**
> **详细文档**：`dev-docs/273-v0-2026-08-08-Grove核心循环与辅助智能体JD-跨AI认知同步.md`

### Grove核心循环

**本 repo 的一切工作都围绕这个循环展开。理解这个循环 = 理解系统是什么。**

```
引导树（给方向Q）→ 推理AI（探索）→ 解题树（记录结果）
                                    ↓
                              在终点节点检索
                                    ↓
                              引导树（新边=新方向Q）→ 启动新推理AI → ...
```

**两棵树是同一棵树的两个面**：
- **引导展开树（Guided Expansion Tree）** = "应该往哪走"的视图。每个节点是一个数学处境，每条边是一个提示Q。活的、正在生长的。
- **解题记录树（Solution Record Tree）** = "实际走了什么"的视图。引导展开树展开完成后凝固的树。包含成功路径、失败路径、分叉点、中间处境。

**循环的三个推动关系**：
1. **引导树 → 推理AI**：引导树上已有节点和边（提示Q），系统从中构造脉络（从根到当前节点的路径+方向Q），给推理AI作为输入，推动它往特定方向探索
2. **推理AI → 解题树**：推理AI的thinking/trajectory被系统采集，提取出节点（数学处境），写入解题记录树——记录"实际探索了什么"
3. **推理AI → 引导树**：推理AI的输出到达某个节点后，系统在这个节点上检索数据基座，识别出新方向Q，这些新方向成为引导树的新边——引导树继续生成

**关键约束**：
- 推理AI不需要停下接受提示——"让推理AI停下"这个需求消失了
- 系统与推理AI并行运行——AI在thinking的同时，系统就从thinking中增量提取节点写入树，两棵树在AI运行过程中实时生长
- 系统的目的不是"让AI做出来"，而是"让两棵树生长出来，在过程中与正确解答的脉络相遇"
- 停机条件：与正确解答的脉络相遇时停机，不需要所有分支都探索完

**循环没转起来的判定**：如果只有解题树在长（采集到了节点），但引导树没有生成新边（没有检索出方向Q、没有启动新AI），循环只转了半圈。完整的循环必须三个推动关系都成立。

### 引导树闭环的识别端结构（000号文档）

**引导树闭环中"识别→给方向"的操作是一个二元组：tell + hint。** tell是识别端（从推理AI的thinking中读出的分叉信号），hint是注入端（给新AI的翻译方向）。hint端已在POC-VMS-8中验证（281/282/283号），tell端已在POC-VMS-9/10中验证（288/289号）。

**000号文档位置**：`000-v0-2026-08-08-引导树闭环-识别端结构定义.md`（项目根目录，不在dev-docs下——这是系统架构的根定义文档）

**二元组**：**读tell，给hint。** tell取自poker术语——推理AI不会主动告诉你"我没考虑这个方向"，但它的thinking会暴露它走了哪条路、没走哪条路。系统从thinking中读出这些信息就是tell。

**核心认知（v2修正，来自285号）**：系统识别的不是"AI在哪里卡住了"，而是"AI的thinking中哪些位置可以分叉但AI没分叉"。往往不是AI卡住了需要提示，而是AI走错路了——系统在AI没走的分叉上开新边，启动新AI走新分支。分叉位置有两种：line上分叉（Point Branch）和根节点分叉（Root Branch）——有时AI从第一步就选错方向，最关键的分叉在根节点。

**tell的四个组成成分**：
1. **分叉信号（Branch Signal）**——识别可以分叉但AI没分叉的位置（line上分叉或根节点分叉）
2. **分叉类型（Branch Type）**——对分叉的抽象分类（翻译类型/操作路径类型/...）
3. **未探索诊断（Unexplored Diagnosis）**——判断AI为什么没走这条路、这条路通向什么
4. **方向匹配（Direction Matching）**——从诊断到字典中翻译方向的映射

**tell端的验证状态（POC-VMS-9/10已完成）**：
- tell可以被去特化——从Level 0（题目特化）提升到Level 1（拓扑结构：problem_type + ai_method_type + gap_type）
- 形式化过滤（Pipe 1）可以命中目标tell——大概念匹配精确区分不同拓扑的tell
- 小概念标记分辨（Pipe 2）可以区分拓扑相同且距离极近的tell——只要两个tell能用语言表达出区别，就能定义概念来区分
- 详见287号（设计）、288号（POC-VMS-9结果）、289号（POC-VMS-10结果）

### AI的双重角色

进入实验时，AI的角色是双重的：

1. **系统开发者**（Master Agent）——设计、实现、迭代这个系统（写代码、审计、测试、commit）
2. **系统检查者**（流程审计AI）——系统运行时检查健康状态，系统运行后审计产出质量

**系统就是脚本。** 系统的运行逻辑（采集、整理、检索、启动）由代码自动执行，不是Master Agent亲手做的。Master Agent的职责是开发系统代码和检查系统运行——不是在系统运行时亲手执行循环。

AI数学系统运行时有两条Pipe：
- **推理 Pipe**（按需多个）——推理智能体（Solver），做数学
- **辅助 Pipe**（1个，由脚本自动执行）——园丁，让循环转起来

两条Pipe并行运行——推理AI在thinking的同时，辅助Pipe（脚本）就并行地采集、整理、检索、启动。Master Agent不在系统运行时参与循环——Master Agent在系统运行时是检查者，检查系统运行的健康状态。

#### 系统就是脚本，你是检查者和开发者

**这是第六代系统的核心认知转变（2026-08-11）。**

第五代系统中，"系统就是你，不是脚本"——辅助Pipe的采集、整理、检索、启动是Master Agent亲手做的动作。第六代系统中，**系统就是脚本**——辅助Pipe的工作由代码自动执行，Master Agent的职责变为：

1. **系统开发者**——写代码实现系统逻辑（vein_analysis.py/trace_match.py/guide_expand.py等）
2. **系统检查者**——系统运行时检查健康状态（按.ai-check checklist审计），系统运行后审计产出质量

**为什么从"系统就是你"变为"系统就是脚本"**：
- 第五代系统中辅助Pipe的工作需要判断力，脚本做不了——但第六代系统把判断力编码进了提示词和程序验证（V9的三层验证体系），脚本可以执行
- 4并发方案中4个AI Agent并发跑，Master Agent手动执行效率太低——脚本自动启动4个tmux session更高效
- Master Agent的时间应该花在开发系统代码和审计系统运行上，不是在系统运行时手动执行循环

**Master Agent在系统运行时的角色**：
- 系统运行中实时检查——检查tmux session是否正常、AI Agent是否跑偏、产出是否落盘（按.ai-check checklist）
- 系统运行后事后审计——按.ai-check checklist逐项检查产出质量
- 发现问题时切回开发者角色修复代码，修完再让系统重新运行

#### 两个角色的切换

**系统开发者和系统检查者不是分时的，是场景驱动的。**

- **系统没在运行时**（没有推理AI在跑）→ 你是系统开发者：写代码、审计、测试、commit、设计新功能
- **系统在运行时**（有推理AI在thinking）→ 你是系统检查者：检查tmux session状态、检查AI Agent产出、检查循环完整性。**你不参与循环执行——循环由脚本执行。**
- **系统运行中你发现问题了**（tmux session异常、AI Agent跑偏、产出格式错误、循环断裂）→ 你临时切回系统开发者修复代码，修完重新运行系统
- **系统运行结束**（所有problem solved或exhausted）→ 你切回系统检查者：按.ai-check checklist逐项审计产出质量、评估、落盘报告

**切换的触发条件是"有没有推理AI在跑"**。有推理AI在跑，你就是系统检查者，没有例外。你不能说"脚本在跑，我等它跑完"——脚本在跑的时候你在检查它的健康状态，不是在等它。

#### 反模式：启动脚本然后干等

**启动系统脚本，然后`get_output`等待结果——这是反模式。**

脚本在运行时，你应该在检查它的健康状态——检查tmux session、检查产出文件、检查数据库。如果你在干等，你退化成了旁观者——脚本遇到异常时你不知道，产出质量差时你不检查。

#### 正确模式：你是检查者

**脚本运行时，你检查脚本的健康状态：**

1. 检查tmux session → `tmux list-sessions` → 4个session都在吗？有没有异常退出的？
2. 检查AI Agent产出 → 工作目录中的output.json出现了吗？格式正确吗？
3. 检查程序验证报告 → V9的audit_report.json生成了吗？完备性得分多少？
4. 检查循环完整性 → 三个推动关系都成立吗？如果只转了半圈，诊断原因
5. 检查alerts表 → 有没有超长文件警报？有没有运行时错误警报？

**你是检查者，脚本是执行者。脚本做机械的部分，你做认知检查的部分。**

### 辅助智能体的 Job Description

在AI数学系统运行时，辅助智能体（Master Agent 作为系统检查者）的职责：

1. **检查系统健康**——检查tmux session状态、AI Agent产出、程序验证报告
2. **检查循环完整性**——三个推动关系都成立吗？如果只转了半圈，诊断原因
3. **审计产出质量**——按.ai-check checklist逐项检查AI Agent的产出
4. **处理异常**——发现异常时切回系统开发者修复代码，修完重新运行
5. **检查停机条件**——检测某条脉络是否到达正确解答，到达则停机

**关键约束**：辅助智能体的工作不是"执行循环"（循环由脚本执行），而是"检查循环执行的健康状态"。系统运行时，你在检查，不在执行。

### 辅助智能体 SOP（场景触发式）

**以下SOP写在实验运行中的具体场景里。当你身处这些场景时，按SOP行动，不要重新思考"做什么、如何做"。**

**场景1：系统脚本刚启动了推理AI，看到 thinking_live.txt 开始有内容**

→ 脚本在采集thinking、提取节点、写入树。你检查：thinking_live.txt在增长吗？节点在写入数据库吗？如果脚本没在做这些，说明脚本有bug——切回系统开发者修复。

**场景2：你看到自己在 `sleep` 或 `等待`**

→ 停。你违反了检查者原则。脚本在工作时你也在工作——你在检查脚本的健康状态。如果你在等待，说明你退化成了旁观者——回到你的角色：检查者不等脚本跑完才检查，检查者在脚本运行的同时就在检查。

**场景3：你看到数据库中节点在增长，但没有新边（tree_edges为空）**

→ 循环只转了半圈。脚本在采集节点，但没有生成新边。检查脚本的检索逻辑——是检索失败还是脚本bug？如果是检索失败，检查数据基座是否有Pattern可检索。

**场景4：你看到推理AI终止了（response_truncated / session_ended / timeout）**

→ 脚本应该在终点节点检索方向Q并启动新推理AI。如果脚本没做，说明脚本有bug——切回系统开发者修复。

**场景5：你看到检索失败（budget exhausted / parse失败 / 无方向Q选出）**

→ 这是循环断裂的最常见原因。检查脚本的检索逻辑——BudgetManager是否设置了足够budget？数据基座中是否有Pattern可检索？如果是代码bug，切回系统开发者修复。

**场景6：你看到循环转起来了——节点在长、边在长、新AI被启动**

→ 这是对的。脚本在正常工作。你继续检查健康状态——检查产出质量、检查alerts表、检查程序验证报告。

**场景7：实验结束后，你回头检查数据库**

→ 必须验证两棵树的数据完整性：tree_nodes中有节点、tree_edges中有边、ai_instances中有AI实例、problems中题目状态正确。如果只有节点没有边，循环没转完整——记录原因，下次修复脚本。按.ai-check checklist逐项审计产出质量。

### 演进路径

- **阶段1（✅已完成）**：A/B对照实验——串行单AI，验证检索机制能否选出正确方向
- **阶段2（✅已完成）**：脉络注入——串行多AI，AI跑完后系统整理脉络、检索方向、启动新AI
- **阶段3（✅已完成）**：并发展开——多AI并发（2并发），系统实时采集所有AI的trajectory整理两棵树，树有分叉
- **阶段4（✅已完成）**：自我增殖——解题记录树完成后提炼Pattern存入数据基座（POC-VMS-5验证）
- **阶段5（✅已完成）**：hint端验证——脉络继承+方向注入的有效性验证（POC-VMS-8，bare 0% → tree 67%）
- **阶段6（✅已完成）**：tell端验证——去特化+形式化过滤+小概念标记分辨（POC-VMS-9/10）
- **阶段7（✅已完成）**：第五代系统技术说明书编写（50个文件全部完成）
- **阶段8（当前）**：第六代系统研发——非局部tell、FCA数学基础、并发Telling AI、Pipe 0简化+Pipe 2并行化

> **⚠️ FCA再分析启动铁律**（本提示在always-on可见区，确保你不会忘记）：
> 做FCA再分析（对已有profile用FCA分类学重新分析）时，采用**主agent/subagent分工**——你是流程管理者，不自己做分析：
> 1. 从`FCA学习笔记/fca-reanalysis-checklist.md`复制check list到todo_write建立TODO List
> 2. 从`FCA学习笔记/fca-reanalysis-subagent-prompt-template.md`复制prompt模板，填入problem_id和产出路径，用run_subagent启动（profile选subagent_general）
> 3. subagent返回后，用`FCA学习笔记/fca-reanalysis-output-verification-checklist.md`验证产出
> 4. 如果subagent发现分类学问题，你自己执行修正流程（7条铁律），不委托subagent
>
> 完整SOP和分工架构详见`.devin/rules/tell-taxonomy-iteration-audit.md`（铁律-1/铁律0/铁律0.5 + 10步SOP + 7条版本化审计铁律）。
> 完整Schema（分类学结构/版本历史/关键文件表）在AGENTS.md第878行起的"Tell分类学Schema"节。

### 第六代系统文档存放规则（阶段8生效）

**第六代系统有两个文档目录，性质不同，必须严格区分：**

| 目录 | 性质 | 编号 | 内容标准 |
|---|---|---|---|
| `第六代系统研发过程文档/` | 探索性、讨论性、评审性 | 三位编号（303号起），和 grove repo 同步 | 研发过程中的思考、争论、方案演进、评审——**不确定的内容放这里** |
| `第六代系统技术说明书/` | 规范性、工程性、自包含 | 章节编号（01-09） | 系统的完整技术规格，可直接实现——**只有真正值得最终记录的内容才放这里** |

**核心规则：研发过程中不确定的内容，暂时只放在研发过程文档目录。只有经过讨论、评审、确认真正值得最终记录到系统说明书的内容，才会进入技术说明书目录。**

- `第六代系统研发过程文档/` 是技术说明书的素材来源和试验场——可以放未经验证的构想、有争议的方案、被评审为跑偏的方向（如307号原语化、309号范式转变原主张）
- `第六代系统技术说明书/` 是研发过程文档的沉淀和整合——只收录经过确认的内容。研发过程文档中被评审为跑偏的部分不会进入技术说明书
- `dev-docs/` 保留给第五代及之前的工作文档（000-291号），不再新增第六代文档

### 第六代系统代码存放规则（阶段8生效）

**系统代码目录**：`system/`

**定位**：`system/` 是整个AI数学系统的物理实现代码——不是用来描述系统的，而是未来真正可以工作的系统代码。系统的物理实现靠代码驱动（见技术说明书README.md §8）。

**两个入口脚本**：
- `system/enter.py`——**入题**：外部持续向系统添加题目（及其解答记录），系统从中提炼tell/hint，tell库增长
- `system/solve.py`——**解题**：将需要解答的题目送入系统，系统编排引导树和解题树的展开，直至获得正确解答

**`system/docs/` —— 系统设计说明书**：
- `system/docs/` 是系统设计说明书的正式存放位置，**按模块组织**——每个模块一个文档（如 `vein_analysis.md`、`process_absorb.md`、`db.md`）
- 每个模块文档记录：模块定位、架构设计、接口定义、数据流、数据库记录、关键设计决策、待实现/待决策
- 模块代码变更时，同步更新对应的模块文档
- 模块的 `.ref` 文件引用对应的模块文档路径
- 目录规范和使用方法详见 `system/README.md`

**`system/` 是自包含的第六代系统**——从代码到文档，到运行时：
- **代码层**：`*.py` + `.ref` + `.ai-check`——真正运行的代码 + 文档引用 + 审计清单
- **文档层**：`docs/`——完整内部认知文档（系统级认知 + 跨模块认知 + 模块级认知）
- **运行时层**：`assets/`——AGENTS模板等运行时资产，运行时复制到工作目录给AI Agent用

**`system/` 的最终定位**：将来第六代系统研发完成后，`system/`要作为一个独立的repo移动到和当前repo平级的目录中，脱离当前repo继续研发。因此`system/`在设计上必须保持自包含性——独立后不依赖当前repo中的任何外部文档（技术说明书、研发过程文档、规则文件等）。

**自包含性对ref和docs的影响**：
- **当前阶段**：ref指向当前repo中的外部文档（技术说明书/研发过程文档/规则文件等），这些引用在当前repo中有效
- **独立后**：ref指向的外部文档将不存在——docs必须在system/内部承载足够完整的认知，使得独立后不丢失关键设计认知
- **演进方向**：docs逐步吸收ref指向的外部文档中的关键认知内容，使得system/越来越自包含。当docs足够完整时，ref可以逐渐淡化（或ref改为指向独立repo内部的文档）

运行时实例在`palyground/absorb/vein_analysis/{run_id}_{problem_id}/`下创建（.gitignore忽略），但它们的模板在`system/assets/`中。`system/`是自包含的——理解第六代系统只需要看`system/`，不需要看`six/`（已合并，见343号方案）。

**.ref 文件规则**：`system/` 中每个 `.py` 代码文件必须有一个同名的 `.ref` 文件（如 `schema.py` → `schema.ref`）。`.ref` 文件内容是相对 repo 根目录的文档路径列表——理解该模块需要参考的文档。代码文件和 `.ref` 文件必须同步更新。详见 `.devin/rules/system-ref-sync.md`。

**ref 和 docs 的关系**（术语定义——以后说"ref"和"docs"就是指这两者）：

- **ref** = `system/` 中的各个 `.ref` 文件——指向system**之外**的外部文档的指针，记录"和这个模块设计有关、但不在system内的文档"。这些外部文档包括：技术说明书、研发过程文档、规则文件、知识层文件（FCA学习笔记/000号文档/Tell分类学等）、其他代码文件等
- **docs** = `system/docs/` 目录——system**之内**的完整认知文档，不只是模块设计说明书。docs承载理解system中任意模块所需的**所有内部认知**，包括三个层次：
  - **系统级认知**：根本认知（两棵树/Grove核心循环）、四Pipe架构、设计原则（解放思想/反射）、提示词设计认知、VMS-28验证历史——这是理解任何模块都需要的前置认知（`architecture.md`）
  - **跨模块认知**：研发文档索引（303-343号文档清单）、代码元素到研发文档的映射、POC验证清单、三个核心问题、FCA术语映射——这是跨模块的"晾衣架"和知识层（`references.md`、`schema.md`）
  - **模块级认知**：模块设计说明书——按模块组织，记录"这个模块怎么实现的"（接口、架构、数据流、设计决策）（如 `vein_analysis.md`）

**ref的特殊身份**：ref不是泛泛的"阅读指南"——它的职责是让AI一次性加载ref中指向的外部文档 + docs中的认知内容之后，能够立即建立起来和这个模块的研发有关的**所有的认知**。ref是外部认知入口，docs是内部认知（系统级+跨模块级+模块级），两者配合构成完整认知。理解一个模块需要的认知往往超出模块本身——涉及系统架构、设计原则、验证历史等系统级认知，这些都在docs中，不在ref中。

**两者关系**：
1. **ref指向system外部，docs在system内部**——ref和docs的内容不重叠，互补
2. **docs不限于模块设计说明书**——系统级认知和跨模块认知也在docs中，因为理解任何模块都需要这些前置认知
3. **ref和 `.py` 一一对应**——每个 `.py` 必须有自己的 `.ref`，即使它的模块文档还没写
4. **改代码时**：先改 `.py` → 检查 `.ref` 是否还准确（外部文档引用是否还有效）→ 如果涉及设计变更，同步更新 `docs/` 中对应的认知文档
5. **改设计文档时**：先改 `docs/` 中的认知文档 → 检查引用该文档的 `.ref` 是否需要更新 → 如果涉及接口变更，同步更新 `.py`

**与文档目录的关系**：
- `system/docs/` 是 `system/` 的**完整内部认知文档**——系统级认知（根本认知/架构/设计原则/验证历史）+ 跨模块认知（研发文档索引/代码映射/POC清单/术语映射）+ 模块级认知（模块设计说明书）
- `第六代系统技术说明书/` 是 `system/` 的设计依据——技术说明书定义"系统应该做什么"，`system/` 实现"系统真正怎么做"
- `第六代系统研发过程文档/` 和 `Tell分类学研究过程文档/` 是设计思想的来源——研发过程文档中的设计决策最终沉淀到技术说明书，再由 `system/` 物理实现，实现细节记录在 `system/docs/`
- 知识层（分类学Schema、Tell库、Hint库、高Level概念解释库、提示词库）需要从markdown变成代码可消费的格式，放入 `system/` 或 `system/` 引用的数据文件

**第六代研发过程文档清单**（截至2026-08-10，均在 `第六代系统研发过程文档/`）：
- 303号：引导树分叉位置的重新理解——脉络上任意点可分叉与非局部tell（从grove repo复制）
- 304号：FCA与工程方案的对应（从grove repo复制）
- 305号：非局部tell的识别价值——端到端实例（从grove repo复制）
- 306号：在推理AI的上下文分析中我们到底想要什么要干什么（从grove repo复制）
- 307号：AI数学思维原语化（从grove repo复制，310号评审：拒绝作为必须项）
- 308号：亲眼看vms_test_1的AI推理thinking（从grove repo复制）
- 309号：从提取到查询的范式转变与trace-tell-hint统一命名（从grove repo复制，310号评审：命名有价值，范式转变原主张跑偏）
- 310号：worktree侧对grove侧303-309号文档的评审
- 311号：并发Telling AI方案——从Pipe 2并行化到Pipe 0简化

**第六代系统技术说明书**（`第六代系统技术说明书/`，截至2026-08-10）：
- 框架已建：README.md + 编写方案.md + 目录结构.md（9章53文件）
- 编写中：按编写方案的顺序逐章编写，只有经过确认的内容才写入

### Seven System · 非特化证据工厂运行入口（2026-08-13起）

**系统目录**：`seven-system/`

**唯一详细操作手册**：`seven-system/docs/operations.md`。启动、preflight、dry-run、状态、故障处理和当前未实现边界都以该文件为准；不要把具体命令复制到AGENTS.md形成第二份易漂移手册。

**系统定位**：Seven System是独立的非特化证据工厂，不是正在运行的题海Profile系统，也不是第六代`system/`的第三个入口：

- 题海系统只读提供冻结bare失败候选与物证；Seven不得写生产`math:*`队列或题目状态；
- 第六代`system/`未来只通过版本化、带哈希的冻结bundle接入；Seven禁止直接import其内部可变状态；
- Seven的目标职责是有限Epoch、资源公平、盲化三审、contrast EvidenceRecord和人工Gate；当前实现尚未进入三审或科学实验阶段。

**资产与数据边界**：

- scripts、运行资产、Schema、docs和tests全部在`seven-system/`；
- 大对象、日志、Epoch和未来Vault进入经批准的D盘数据根；数据库只存元数据、事件和artifact引用；
- Seven复用现有Arango服务和逻辑数据库`xishujuzhen_math_glm52`，未来只创建隔离且显式版本化的`seven_*_vN`集合/索引（`N`为正整数；v1为scaffold，后续版本承载经批准的原子结构）；不得复用题海或`system/`集合。Arango engine字节已经经OrbStack `data.img.raw`由D盘承载，但未使用`/data/arangodb/data`专用bind；物理存储形态不是逻辑数据库复用的前置Gate；
- `/data`缺失、卷README缺失、数据根未批准或空间不足时fail-closed，不得fallback到repo/Home/`/tmp`。

**硬约束**：

1. Devin Solver生产实验用全局`noninteractive-solver-run` skill（`devin -p --prompt-file ... --export ...`）；调试harness用`solver-tmux-launch` skill（`solver_harness.py launch --no-mitm`）；批量解题用pipe系统；
2. Solver必须无工具；Prompt写“不要用工具”不等于能力PASS，缺独立NoTool能力报告时live运行必须BLOCK；
3. 只有**目标Solver作业**可以进入`solver_harness`；Devin CLI并不专属于Solver。出题、数学核验、对抗审稿和Judge统一经provider-neutral `ModelRolePort`（Cognitive Worker是子系统名），同时允许物理隔离的`DevinCliModelRoleAdapter`与`CodexExecModelRoleAdapter`。Devin认知worker不得复用Solver port/workspace/session/AGENTS/capability/receipt/resource pool；人工复核/人门另走`HumanTaskPort/HumanGateService`；
4. Devin认知角色的首个精确候选为`glm-5-2`（本机catalog显示`GLM-5.2 High`，effort由model UID编码），Codex/Responses中的`gpt-5.6-sol`高推理配置为并列候选；两者都必须按角色与精确profile探测requested/effective模型、effort、mode、orchestration、权限、事件和成本。盲化AuthoringBakeoff只选择角色默认profile，不取消其他已合格载体；同模型新会话只能算上下文独立，不能冒充异模型审查；
5. DB访问仍须先确认`ARANGO_DB=xishujuzhen_math_glm52`，禁止默认库和直接raw client；
6. Evidence/Artifact/WorkEvent append-only，禁止覆盖、删除负证据、retry until solved或authoring retry until Devin fails；
7. 自动化不得跨人工Gate、自动切active release或把PARTIAL升级为PASS。
8. 完整实现按`seven-system/docs/implementation/README.md`的development/activation双依赖推进：上游`READY_FOR_AUDIT`可支持无副作用开发并继承审计债；真实DB、模型、Solver、正式HumanGate、canonical阶段与科学Evidence还需`AUDITED_PASS`或本次未审canary被父级EEA精确覆盖，并且每个具体副作用另有不可扩权LiveRunPermit与原子额度预留收据。实施AI不得把候选系统自签为正式PASS。

**当前真实实现上限**：`seven-system` v0.1.0实现P0只读preflight、P1 scaffold dry-run，以及WP-1的D盘站点存储前置检查和**离线**Strict DB契约报告（都不是387号完整P1）。生产包没有site verifier或apply/DDL primitive，尚未连接真实DB，也没有创建任何`seven_*_vN`集合；因此逻辑站点能力与Schema初始化仍为`NOT_IMPLEMENTED`。Arango engine字节已经经OrbStack image由D盘承载（`A-WP1-D=PASS`，evidence basis为`CONFIRMED_VIA_ORBSTACK_IMAGE`），但仍在容器writable layer而非专用host bind（`A-WP1-BIND=WARNING_NOT_DEDICATED`）。`TargetSolverPort`、`ModelRolePort`（Cognitive Worker子系统）、Devin/Codex认知adapter、QuestionRelease管线和AuthoringBakeoff也都尚未实现或运行；当前不连接DB/Redis、不启动Solver、不调用远程认知Worker。以`seven-system/docs/implementation-status.md`为准，完整故障恢复矩阵和P2-P9均不得冒充已实现。

**最新工程决策记录**：`Tell分类学研究过程文档/389-v0-2026-08-13-seven-system非特化证据工厂工程化落盘-双系统吸收与P0P1首版.md` §14-17。§14替代同文§12-13中“物理未落D盘必然阻断逻辑数据库接入”的政策推论；§15纠正“OrbStack overlay即未落D盘”的不完整宿主存储判断；§16记录初版多模型边界；§17按用户最新决策修正为“目标Solver专用Devin执行面 + ModelRole中的Devin/Codex双认知载体”。完整文档总入口和实施者入口是`seven-system/docs/implementation/README.md`；未来独立审计者必须从`seven-system/docs/audit/README.md`开始，再回读被冻结的实现规范与CompletionBundle。

---
