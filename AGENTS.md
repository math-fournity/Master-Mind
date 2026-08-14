# 项目 AGENTS.md · 数学大师制造

> **未来 AI 进入本 repo 时，必须先读完本文件顶部的硬约束再做事。**

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
- Seven复用现有Arango服务和逻辑数据库`xishujuzhen_math_glm52`，未来只创建隔离的`seven_*_v1`集合/索引；物理engine是否已迁到D盘是独立运维状态，不是逻辑数据库复用的前置Gate；
- `/data`缺失、卷README缺失、数据根未批准或空间不足时fail-closed，不得fallback到repo/Home/`/tmp`。

**硬约束**：

1. Devin Solver仍只能经`xishujuzhen/solver_harness/solver_harness.py launch`；
2. Solver必须无工具；Prompt写“不要用工具”不等于能力PASS，缺独立NoTool能力报告时live运行必须BLOCK；
3. DB访问仍须先确认`ARANGO_DB=xishujuzhen_math_glm52`，禁止默认库和直接raw client；
4. Evidence/Artifact/WorkEvent append-only，禁止覆盖、删除负证据或retry until solved；
5. 自动化不得跨人工Gate、自动切active release或把PARTIAL升级为PASS。

**当前真实实现上限**：`seven-system` v0.1.0实现P0只读preflight、P1 scaffold dry-run，以及WP-1的D盘站点存储前置检查和**离线**Strict DB契约报告（都不是387号完整P1）。生产包没有site verifier或apply/DDL primitive，尚未连接真实DB，也没有创建任何`seven_*_v1`集合；因此逻辑站点能力与Schema初始化仍为`NOT_IMPLEMENTED`。Arango物理数据目录未落D盘的事实保留为`DEFERRED_WARNING`，不再阻塞复用原逻辑数据库。不连接DB/Redis、不启动Solver。以`seven-system/docs/implementation-status.md`为准，完整故障恢复矩阵和P2-P9均不得冒充已实现。

**最新数据库决策记录**：`Tell分类学研究过程文档/389-v0-2026-08-13-seven-system非特化证据工厂工程化落盘-双系统吸收与P0P1首版.md` §14。它替代同文§12-13中“物理未落D盘必然阻断逻辑数据库接入”的政策推论，但不改写当时的只读观测事实。

---

## 角色说明 · 你当前是什么 AI

本 AGENTS.md 可能被多种 AI 加载，进入本 repo 时请先确认自己的角色：

| 角色 | 工作目录 | 职责 | 看到本 AGENTS.md 时该做什么 |
|---|---|---|---|
| **Master Agent** | `~/master-mind-glm5.2-worktree/` | 实现、审计、迭代数学大师系统 | 遵守本 AGENTS.md 全部约束，执行工作 |
| **Subagent** | 由 Master 通过 Devin CLI/tmux 启动 | 执行被分配的子任务 | 只执行分配的任务，不承担 Master 的全部责任；若不确定就问 Master |

**如果你是 subagent**：你看到的是 Master 的 AGENTS.md，但你不等于 Master，不需要承担 Master 的长期工作系统迭代责任。你的任务是完成 Master 交给你的具体任务，任务完成后汇报。

---

## 本 repo 基本信息

- **路径**：`~/master-mind-glm5.2-worktree/`
- **工作分支**：`glm5.2`
- **origin**：`/data/master-mind`（fetch/push 都指向它）
- **Python 环境**：独立 venv（`.venv/`，python3.14 + python-arango 8.3.3，被 gitignore）
- **数据库**：ArangoDB `localhost:8529`，本 repo 专用数据库名 `xishujuzhen_math_glm52`（通过 `.env` 文件设置 `ARANGO_DB` 环境变量）

### 硬约束 1 · 数据库连接

**本 repo 专用数据库名**：`xishujuzhen_math_glm52`（通过 `.env` 文件覆盖 `ARANGO_DB` 环境变量）。

**硬规则**：
1. **启动任何会连 ArangoDB 的脚本/服务前**，必须确认 `ARANGO_DB` 环境变量已设为 `xishujuzhen_math_glm52`。
2. **每次运行前必须确认 `echo $ARANGO_DB` 输出 `xishujuzhen_math_glm52`**。若忘了 source `.env`，脚本会 fallback 到默认值 `xishujuzhen_math`，那是错误的数据库。
3. **运行 POC、研究 runtime、事件存储、启发规则存储**等所有会写库的代码前，先核对环境变量。

**题目录入信息抓手**：`problem_entries`集合——每道题入题一条记录，是查找该题目所有录入信息的抓手。从这条记录可以找到工作目录、会话ID、4个AI实例ID、产出路径、程序验证报告路径、合并trace路径。查找方法：`db.find_problem_entries_by_problem_id(problem_id)`。`system/`及本repo原有业务代码的数据库操作统一通过`system/db.py`模块，不直接操作ArangoDB客户端。

**Seven System例外（独立repo边界）**：`seven-system/`不得`import system.*`，其数据库访问只能通过Seven自身的`seven_system.database.StrictDatabasePort`；只有该端口唯一的Arango backend可以封装`ArangoClient`，其余Seven代码同样禁止直接使用raw client。Seven复用同一Arango服务与逻辑数据库`xishujuzhen_math_glm52`，但不得复用现有业务集合；未来仅允许隔离的`seven_*_v1`命名空间。这个架构许可不构成当前写授权：真实Schema初始化仍须通过精确数据库身份、只读catalog核验、显式计划哈希、人工确认、受控DDL入口和执行收据。Arango实际data dir未落D盘只形成独立运维警告，不得再把它写成逻辑接入的硬阻塞。

### 硬约束 2 · Git 规则

1. **只在 `glm5.2` 分支上工作**。不要 commit 到本地 `main`。
2. **显式路径 add**：禁止 `git add -A`/`git add .`/`git add -u`，只 add 具体路径。
3. **改前清干净 + 改后立即 commit**：遵守全局 Git 管理协议。
4. **push 需用户明确授权**。

### 硬约束 3 · Solver 工作目录隔离

**数学大师 Solver 的 devin cli 实例必须在外部目录运行，不能在本 repo 内运行。**

原因：本 repo 的 AGENTS.md 包含工作系统规则（CP1-CP3、认知种子、七步骤pipeline等），如果 Solver 在本 repo 内运行 devin cli，这些规则会劫持 Solver 的行为——Solver 不做数学，而是去加载认知种子。这在 run_20260806_guided_001/002 中已验证发生。

**当前模式 · tmux-agents-dir（2026-08-07起）**：每个实验在 `/data/math-agent-glm5.2-tmux-agents-dir/` 下有独立的工作目录，运行后保留全部记录。目录命名规范：`<dev-docs编号>-<实验名>`。AGENTS.md模板：`templates/solver_agents_md.md`（bare）和`templates/solver_agents_md_guided.md`（guided）。

**旧模式 · 三固定目录（legacy，已废弃）**：`/data/math-agent-glm5.2-{1,2,3}`，目录在run之间被清理复用，运行记录不保留。

**Solver角色定义**：直接做数学，不走工作系统流程。可以搜索通用数学知识（定理/定义/公式），但禁止搜索题目答案/解答。允许exec（Python/SymPy计算验证）、read/write/edit、web_search。不知道就说"我不知道"，系统通过提示引导。**启动必须加`--permission-mode dangerous`**——否则exec被rejected，AI只做2步就停。

**Solver监控操作手册**：`.devin/skills/solver-monitoring/SKILL.md`（启动/观察/已知问题处理/判断是否做出来了）。

**元组：solver-batch-health-check**（批量集群健康检查）

> **触发条件**：用户说"检查进度"/"看看有没有问题"/"检查链接问题"时；批量Solver集群运行时；新session接手批量系统时。
> **Rule**：`.devin/rules/solver-batch-health-check.md`——三条铁律（用batch_status.py不现写脚本/DB数字会骗人必须到最前线/发现问题先修检查工具再修监控逻辑）+ 并发上限经验（管道化系统实测：60并发最优，100并发触发限流）+ 已知问题清单（10个已修复问题，含2026-08-13的collector误杀/中文proof/rate_limited检测3个修复）。
> **Skill**：`.devin/skills/solver-batch-health-check/SKILL.md`——7项检查清单（批次活着/running数合理/活跃度/僵尸session/错误分类/feed/泄漏）+ 手动清理僵尸session脚本 + 并发调整命令。
> **并发约束Rule**：`.devin/rules/solver-concurrency.md`——3秒启动间隔铁律（runner.py第333行不可改）+ 并发经验表（40/50/60/80/100实测数据）+ Redis实时调整命令。
> **检查工具**：`xishujuzhen/solver_harness/batch_status.py`（8个命令：status/active/errors/solved/feed/leak/dead/all，dead支持--cleanup自动清理僵尸session）。

### 硬约束 4 · Solver启动必须通过solver-harness（最重要）

**启动数学大师Solver的devin cli实例，必须通过`xishujuzhen/solver_harness/solver_harness.py launch`，禁止任何其他方式。**

**禁止的方式**：手动tmux、exec后台、nohup、subprocess直接调用、任何绕过solver-harness的脚本。

**适用所有场景**（无一例外）：裸跑测试、GuidedLoop引导、批量测试、DFS回溯实验、MathArena测试、FATE测试、A/B对照实验。

**为什么是硬约束**：solver-harness自动完成tmux启动+pipe-pane记录+sessions.db轮询+export保存，并修复了`--no-http2`多轮交互Connection failed问题和`NODE_EXTRA_CA_CERTS` SSL验证问题。

**mitmproxy已禁用**（2026-08-12）：mitmproxy代理曾用于捕获token级thinking+tool_calls，但实测发现mitmproxy进程虽活着但代理不通（curl返回000），所有solver API调用走坏代理导致秒退。已设`mitm_enabled: False`默认值，launch时加`--no-mitm`。devin cli自身的`thinking_readable_path`和`--export`已提供完整thinking数据，不需要mitmproxy。

**例外**：`realtime/devin_cli_parser.py`中的`DevinCliParserProvider`用`devin -p`做LLM parser（不是Solver，不采集trajectory），可以保留直接调用。

**具体启动规范见** `.devin/rules/solver-tmux-launch.md` 和 `.devin/skills/solver-tmux-launch/SKILL.md`。

### 硬约束 5 · Solver批次系统架构认知（已归档）

> **第一代批量系统（batch_problem_runner.py）已被管道化系统（pipe/5服务）完全替代，当前不再运行。**
>
> **完整架构说明已移到**：`dev-docs/旧模式batch_problem_runner系统说明.md`——运行模式/命令/TUI直出/`-p`vs交互模式/答案泄漏防护/选题feed/限流/并发上限/DB schema/批次状态查询脚本。
> **操作SOP已移到**：`dev-docs/旧模式batch_problem_runner操作SOP.md`——16个SOP（启动/检查健康/验证STALLED/处理dead/落盘/看thinking/扫描状态/恢复export/停止/手动feed+resume）。
>
> **何时需要读**：管理仍在运行的旧模式实例时（当前无）；需要了解`-p`模式vs交互模式的历史演变时。
>
> **跨系统共享信息**（DB schema表/数据完整性表/看Solver方法）已迁移到下方管道化系统节中。

---

### 硬约束 6 · 自动化运营系统（已归档）

> **第二代批量系统（auto_runner.py + enqueue_problem.py）是batch_problem_runner到管道化系统之间的过渡方案，已被管道化系统（pipe/5服务）完全替代，当前不再运行。**
>
> **完整架构说明已移到**：`dev-docs/旧模式auto_runner系统说明.md`——架构/三个组件/送题命令/启动runtime/监控命令/problem_queue字段/固定目录/AI工作循环/与旧模式的区别。
>
> **何时需要读**：需要了解auto_runner的problem_queue表结构时；需要了解从batch_problem_runner到管道化系统的演进过程时。

---

### 通用SOP（适用于管道化系统）

> **以下SOP是通用规范，适用于当前管道化系统（pipe/5服务）。旧系统（batch_problem_runner/auto_runner）的SOP已归档到dev-docs/。**

**SOP G1 · 编译验证（改代码后必须做）**

```bash
cd ~/master-mind-glm5.2-worktree
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/feeder.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/runner.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/collector.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/reporter.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/retry_infrastructure.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/pipe/pipe_control.py && \
.venv/bin/python -m py_compile xishujuzhen/solver_harness/solver_harness.py && \
echo "compile OK"
```

**SOP G2 · 资产追溯规范（2026-08-12）**

> **所有运行资产必须可追溯**——从DB记录能找到文件路径，从文件路径能找到DB记录。不允许放临时目录。

**运行ID唯一性保证**：

exp_id格式：`{batch_id}-{ordinal:02d}-p{progress_key}-r{run_id:07d}-{problem_id}`

- `run_id`是ArangoDB counter（`devin_counters` collection的`run_id`键）原子自增的全局运行ID
- 每次`create_batch`/`add_cases`/`create_attempt_from_queue`创建attempt时调`next_run_id(db)`获取，确保exp_id全局唯一
- 同一道题在不同batch中跑→run_id不同→exp_id不同✓
- 同batch内重跑→run_id不同→exp_id不同✓
- 两个runner并发→ArangoDB事务保证原子递增→run_id不冲突✓
- DB attempt记录中有`run_id`字段，便于从run_id反查attempt
- **目录名以exp_id开头，exp_id含run_id，所以目录永远唯一，不会错乱**

**资产存放位置**：

| 资产 | 位置 | 持久化 | 追溯方式 |
|---|---|---|---|
| **trajectory文件**（export/pipe/thinking_capture/tmux.log） | `/data/math-agent-glm5.2-tmux-agents-trajectory/<exp_id>/` | 是 | DB attempt.paths指向 |
| **solver工作目录**（problem.txt/proof.md/AGENTS.md） | `/data/math-agent-glm5.2-tmux-agents-dir/<exp_id>/` | 是 | DB attempt.paths指向 |
| **monitor日志** | `/data/math-agent-glm5.2-tmux-agents-dir/logs/batch-<label>.log` | 是 | tmux session名对应 |
| **auto_runner日志** | `/data/math-agent-glm5.2-tmux-agents-dir/logs/auto_runner.log` | 是 | 固定路径 |
| **DB记录**（attempt/event/batch/queue） | ArangoDB | 是 | batch_id → attempt → paths |
| **sessions.db** | `~/.local/share/devin/cli/sessions.db` | 是 | devin_session_id关联 |

**从DB查运行时目录和文件位置**：
```bash
# 从problem_id查所有attempt及其文件路径
.venv/bin/python -c "
from arango import ArangoClient; import os
c = ArangoClient(hosts=os.environ.get('ARANGO_HOST','http://localhost:8529'))
db = c.db(os.environ['ARANGO_DB'], username=os.environ.get('ARANGO_USER','root'), password=os.environ.get('ARANGO_PASS',''))
for a in db.aql.execute('FOR a IN devin_problem_runs FILTER a.problem_id == @pid RETURN a', bind_vars={'pid': '<PID>'}):
    print(f'run_id={a.get(\"run_id\",0)} status={a[\"status\"]} batch={a[\"batch_id\"]}')
    print(f'  exp_id={a[\"exp_id\"]}')
    print(f'  export: {a[\"paths\"][\"export_path\"]}')
    print(f'  thinking_capture: {a[\"paths\"][\"tmux_pipe_path\"].replace(\"tmux_pipe.log\",\"thinking_capture.txt\")}')
    print(f'  solver_dir: {a[\"paths\"][\"solver_dir\"]}')
"
```

**禁止**：
- **禁止放`/tmp/`**——重启丢失，无法追溯
- **禁止只存DB不存文件**——DB只有paths指针，文件丢了paths指向空
- **禁止只存文件不存DB**——没有DB记录无法从batch_id查到attempt

**SOP G3 · AI失败题分类与Response truncated处理（2026-08-12）**

> **AI做不出来的题分4类**，全部记录到DB的`devin_problem_runs`中，`status`+`end_reason`字段标识失败类型。完整追溯文档见374号文档。

**AI自身问题导致的失败**：

| status | 含义 | end_reason | 是AI的问题？ |
|---|---|---|---|
| `failed_no_proof` | session结束但没输出`### PROOF COMPLETE`标记 | `tmux_session_ended` | 是——AI做了题但没按格式输出标记 |
| `failed_token_limit` | token用完没做出来 | `tmux_session_ended` / `idle_token_limited` / `response_truncated_max_token_limit` | 是——AI能力不足/效率不够 |
| `failed_tool_stall` | 工具调用卡住超时 | `stall_seconds` | 是——AI行为异常 |
| `answer_leak` | AI检测到答案泄漏主动拒绝 | `answer_leak_detected_by_solver` | 是——AI主动拒绝 |

**基础设施问题导致的失败（不算AI做不出来）**：

| status | 含义 | 归因 |
|---|---|---|
| `dead_session` | devin cli已退出(DEVIN_CLI_EXITED)但无proof | 基础设施 |
| `failed_connection` | 网络连接断开 | 网络 |
| `failed_network_stuck` | 网络不稳定卡死 | 网络 |
| `launch_error` | 启动失败 | 系统 |
| `stopped` | 手动停止 | 操作 |

**Response truncated的处理**：

> **Response truncated不是网络问题**——是模型输出达到max token limit被截断。TUI显示`⚠︎ Response truncated`，session空闲等待用户发消息继续。这属于AI做不出来的情况——AI的输出长度不够完成证明。

**处理流程**：
1. `scan-thinking`扫描发现IDLE的session
2. 看pane内容——`Response truncated`是token limit，`Connection error`是网络断开
3. **Response truncated**：可以发"继续"让AI继续输出，但如果反复truncated说明题对AI来说太长→最终标记`failed_token_limit`
4. **Connection error**：网络问题，发"继续"重试，反复失败则标记`failed_connection`

**手动落盘PROOF COMPLETE的session**（auto_runner的refresh循环会自动做，但如果需要手动做）：
- 先`capture_thinking(attempt)`保留thinking数据
- 再`stop_attempt(db, attempt, batch_dir, decode=False)`让devin cli写export
- 等3秒后kill tmux session
- 更新DB：`status=candidate_solved`, `end_reason=manual_pane_proof_complete`
- 记录event：`event_type=attempt_solved`

**查询所有AI失败的题**：
```bash
.venv/bin/python -c "
from arango import ArangoClient; import os
from collections import Counter
c = ArangoClient(hosts=os.environ.get('ARANGO_HOST','http://localhost:8529'))
db = c.db(os.environ['ARANGO_DB'], username=os.environ.get('ARANGO_USER','root'), password=os.environ.get('ARANGO_PASS',''))
for s, n in sorted(Counter(a['status'] for a in db.aql.execute('FOR a IN devin_problem_runs FILTER a.status IN [\"failed_no_proof\",\"failed_token_limit\",\"failed_tool_stall\",\"answer_leak\"] RETURN a')).items()):
    print(f'  {s}: {n}')
"
```

---

### 旧模式SOP（batch_problem_runner直接操作 · 已归档）

> **以下SOP来自2026-08-12的调试实战，适用于batch_problem_runner.py直接操作模式。该系统已被管道化系统完全替代，当前不再运行。**
>
> **完整操作SOP已移到**：`dev-docs/旧模式batch_problem_runner操作SOP.md`——16个SOP（SOP 1启动批次/SOP 2检查批次健康/SOP 3验证STALLED/SOP 4处理dead session/SOP 5批量落盘/SOP 6看thinking内容/SOP 7停止批次/SOP 9扫描thinking状态/SOP 10恢复export=0B/SOP 13手动feed+resume）+ 数据完整性表 + 已知根因清单。
>
> **何时需要读**：管理仍在运行的旧模式实例时（当前无）。

---

## 任务追踪（跨Session工作意识维持）

**任务追踪文档目录**：`任务追踪/`——每个工作线一个独立文件，顺序编号化，自包含，互不干扰。

**`任务追踪/README.md`** — 导航枢纽，记录各任务追踪文档之间的依赖关系DAG。

**当前活跃的任务追踪文档**：

| 文件 | 工作线 | 焦点 |
|---|---|---|
| `任务追踪/01-253号检索机制验证.md` | 253号检索机制验证 | P0+P1原型验证完成，泛化验证通过 |
| `任务追踪/02-trajectory采集与solver-harness.md` | Trajectory采集基础设施 | solver-harness方案v1完成 |
| `任务追踪/03-虚拟数学系统VMS-POC验证.md` | 虚拟数学系统POC验证 | POC-VMS-0到VMS-10全部完成 |
| `任务追踪/04-端到端效果验证-接真实Solver.md` | 端到端效果验证 | ✅A/B实验完成，已演进到Grove核心循环 |
| `任务追踪/05-题目侧写Profiling系统.md` | 题目侧写Profiling系统 | 设计完成 |

**任务追踪文档编写要求**：自包含、Checklist化、结构统一（§0当前焦点/§1已完成/§2待办/§3关键决策/§4 Git Commit历史/§5跨Session读取指南）、不删除历史、新建时更新README.md、记录git commit ID和全部产出资产path。详见`任务追踪/README.md`。

---

## 题目侧写Profile提取工作（活文档 · 数据基座建设）

> **本节记录题目侧写（problem profile）提取工作的进度、方法和产出。这是系统数据基座的核心建设线。**
> **详细审计日志**：`subagents-dirs/review-log.md`（每批审计结果）
> **任务追踪文档**：`任务追踪/05-题目侧写Profiling系统.md`

### 工作方法

每道题通过subagent完成11步分析：读题目解答→QA序列分析→问题拓扑层→解答思维模式层→翻译方向层→tell拓扑层→提取(tell,hint)对→实验适用性层→输出profile JSON→入库ArangoDB→汇报。

Master Agent对每批3题做完整6-Phase审计：格式检查（situation_type/hint_level/per-pair拓扑/必填字段/QA序列结构）+数学内容审查（题目理解/解答理解/key_insight准确性/瓶颈标注合理性）+落盘audit-checklist.md。

### 数据库存储

- **ArangoDB集合**：`problem_profiles`（_key=problem_id，含完整profile JSON）
- **ArangoDB集合**：`problem_extraction_progress`（_key=数字ID，含global_sequence/extraction_status/metadata）
- **数据库**：`xishujuzhen_math_glm52`，localhost:8529

### 完成进度（截至2025-01-24）

| 层级 | 来源 | 完成数/总数 | 状态 |
|---|---|---|---|
| **Tier 1** | 高难度竞赛题（IMO/IMO SL/Putnam/China TST/FATE-X等） | **452/452** | ✅全部完成 |
| **Tier 2** | IMO Shortlist剩余+IMO剩余+Putnam剩余+IMO Longlists+China TST剩余+Balkan MO SL+China NOL+ToT+IMC+Yau+Alibaba | 3/606 | 进行中 |
| **Tier 3** | USAMO+FATE-H+HMMT系列+SMT+CMIMC+Iranian+Brazilian | 0/3127 | 待处理 |
| **Tier 4** | OlympiadBench+FATE-M+AIME 2024 | 0/860 | 待处理 |
| **Tier 5** | pascal+fermat+cayley+mathd | 0/942 | 待处理 |
| **Tier 6+** | olympiads+Hendrycks MATH+AoPS 2024等 | 0/62000+ | 暂不规划 |

**当前总进度**：455/67838（0.67%），但Tier 1高难度题已100%完成。

### Token统计

| 指标 | 数值 |
|---|---|
| profile总数 | 455 |
| 局部tell数量 | 3,192 |
| 全局tell数量 | 972 |
| tell总数 | 4,164 |
| tell字段总token | ~122K |
| 完整profile总token（含所有文本字段） | ~407K |
| 平均每profile token | ~893 |

### 质量记录

- **连续0个小问题批次**：129批（从第41批至今）
- **subagent静默失败处理**：少数题目subagent返回空结果，Master Agent手动创建profile（如omni_math_004296）
- **原解答问题处理**：部分题目原Lean解答有计算错误/不严谨/模糊/hand-wavy/事实错误，subagent在profile中重构或注明
- **空答案字段处理**：部分题目answer为空，subagent从解答中推导答案

### Tier 2后续优先级（难的先处理）

1. IMO Shortlist剩余96题（起始seq=1955）← 当前进行中
2. IMO剩余89题（起始seq=1403）
3. Putnam剩余88题（起始seq=1756）
4. IMO Longlists剩余39题（起始seq=1994）
5. China TST剩余80题（起始seq=1443）
6. Balkan MO SL剩余31题（起始seq=1862）
7. China NOL剩余35题（起始seq=1446）
8. ToT剩余54题（起始seq=1956）
9. IMC剩余67题（起始seq=1627）
10. Yau Contest剩余6题（起始seq=1630）
11. Alibaba Contest剩余21题（起始seq=1597）

### 关键文件

- `subagents-dirs/review-log.md`：完整审计日志（每批的seq范围/题目/审计结果/修复内容/数学审查结论）
- `subagents-dirs/<problem_id>/`：每题的工作目录（problem.lean/checklist.md/profile.json/audit-checklist.md）
- `subagents-dirs/audit-checklist-template.md`：审计checklist模板
- `subagents-dirs/checklist-template.md`：subagent工作checklist模板
- `scripts/prepare_subagent_dir.py`：subagent工作目录准备脚本
- `scripts/ingest_problem_extraction_progress.py`：progress记录入库脚本

---

## 认知资产索引（活文档）

认知资产索引（隔离实施状态、ArangoDB 初始化状态、认知图/依赖图/题库统计）在 `xishujuzhen/cognition_asset_index.md`，由工作系统持续维护。每次新增认知单元、新增 dev-docs、ArangoDB 状态变更后更新该文档。

---

## 系统设计原语目录（活文档）

系统设计原语分四层管理（244号重构 + 245号面相独立 + 257号全库原语找回）：
- **`primitives/`** — 原语（构造系统的积木，72个）：`operational/`（操作原语47个）+ `structural/`（结构原语25个）。验证状态四等级：tested 35 / partial 16 / untested 20 / tested_negative 1。
- **`concepts/`** — 概念框架（8个）：形式化边界、两种计算、闭环、处境等。
- **`criteria/`** — 性质标准与探索性隐喻（3个）。
- **`facets/`** — 面相（7个）：两种计算/语料双路径/Pipeline网络/树的生长 + 实践涌现/知识选取/设计过程自举。

详见 `dev-docs/257-v0-2026-08-07-全量原语目录更新方案-以253号检索问题为抓手的全库原语找回.md`。每次跑实验后更新相关原语的验证状态。

---

## 原语化AI数学工程系统设计（活文档 · 论文原语化版）

**`原语化AI数学工程系统设计/`** — 256号论文的原语化升级版（v5）。29个自包含的Markdown文件，通过前置阅读和关联原语链接形成阅读网络。README.md是导航枢纽。包含四代系统的完整设计文档。

---

## 系统技术说明书系列（活文档 · 系统演进主线）

数学大师系统经历了五代演进，每一代有中国神话命名和独立技术说明书。命名规则见 `.devin/rules/system-generation-naming.md`。

| 代际 | 神话名 | 核心理念 | 技术说明书 |
|---|---|---|---|
| 第一代 | **盘古** | 静态图前置 | `dev-docs/249-v0-2026-08-07-第一代数学大师系统-最完整技术说明书.md` |
| 中间代 | **女娲** | 动态控制+角色隔离 | `dev-docs/250-v0-2026-08-07-中间代数学大师系统-技术说明书.md` |
| 第二代 | **燧人** | 非特定元认知提问 | `dev-docs/238-v1-2026-08-07-非特定高Level启发式提问方案完整梳理.md` |
| 第三代 | **伏羲** | 形式化边界推进 | `dev-docs/239-v0-2026-08-07-AI数学工程系统-最完整技术说明书.md` |
| **第五代** | **（待命名）** | **集大成者：tell+hint二元组+三层Pipe架构+概念树** | **编写中：`第五代系统技术说明书/编写方案.md`** |

**第五代系统**是四代的集大成者——整合盘古的拓扑覆盖、女娲的T图/W_t、燧人的形状匹配/Level/DFS引导架构、伏羲的不自然识别/形式化边界/两种计算，加上tell+hint闭环和概念树。从前四代继承了29项具体内容（详见`dev-docs/290-v0-2026-08-08-第五代系统从前四代继承了什么-详细梳理.md`），另有7项独特贡献是四代都没有的。

**第五代验证状态**：POC-VMS-8（hint端，bare 0%→tree 67%）、POC-VMS-9（tell端去特化+形式化过滤）、POC-VMS-10（小概念标记分辨）全部PASS。

**第五代交接文档**：`dev-docs/291-v0-2026-08-08-第五代系统工作交接文档-含加载清单和加载顺序.md`

**代际转折点**：盘古→女娲（122-v1诊断架构断层）→燧人（200-202号危机诊断）→伏羲（218号非特定性危机+222号形式化边界）→第五代（tell+hint闭环+概念树，285-291号）

---

## 工作原则

### 从星学项目继承的工作原则

- **新系统本体纪律**：本项目中的"新系统"专指为数学研究建设的知识系统与导航系统。不得把星学代码、星学知识文件或星学运行时称为新系统。
- **有机积累纪律**：新认知应融入已有概念、步骤、专题和来源网络；不能总在文件末尾追加孤立段落，也不能重复制造平行定义。
- **结构可修订纪律**：现有知识系统结构只是当前状态。材料暴露结构问题时，先修正结构，再安放内容。
- **不确定性保留纪律**：不同证明路径、不同数学流派的差异必须保留。没有充分证据时使用"候选、待考、类比"，不能强行统一。
- **AGENTS 高价值内容保全纪律**：重构 AGENTS.md 时，不得把原有高价值规则、操作门槛、索引直接删除。确需移出时，必须已有明确承接文件、保留强约束摘要、保留索引、说明迁出原因。
- **细节推出纪律**：从 AGENTS.md 推出到 dev-docs/ 的内容，不能被视为废弃内容。未来 Session 必须能通过 AGENTS 的索引找回。

### 数学项目特有工作原则

- **渐进积累、迭代测试**：一边装入一边充分测试——每装入一批知识/依赖边/意识节点，就立即用POC验证其价值，验证通过再继续装入。
- **穷尽式知识吸收**：全能数学大师应该知道一切可得的数学知识。十三大来源详见109号方案。
- **数学计算交给工具，数学知识由知识系统承载，数学判断由 AI 执行，三者不混用。**
- **依赖图构建需要数学功力**：判断"代数拓扑依赖范畴论"是一条边——这个判断需要"综述博士"参与。
- **方法论迁移不是照搬**：星学的依赖图结构不适用于数学，数学的依赖图需要重新设计。

### 明确不做清单（123号第五十九节 · 硬约束）

以下8项是项目级硬约束，任何Phase都不得违反：

1. **不先扩张到325000知识节点再验证核心闭环**——先通过DYN-0—DYN-4，证明状态可建模且最小Hint有效
2. **不把完整答案路线改写成"意识"后继续做B组提示**——这是答案泄漏的根因
3. **不用节点覆盖率代替数学正确或研究能力**——100%拓扑覆盖只证明结构保真
4. **不要求或伪造隐藏chain-of-thought**——只处理公开研究产物与工具事件
5. **不让同一Master同时持有答案、设计Hint、运行Solver和评分**——角色隔离是硬约束
6. **不把L1/L2/L3当成同一认知单元的版本号**——L1/L2/L3是提取层次，版本链独立编号
7. **不在状态空间未定义时宣称找到了同调洞**——HoTT/同调/几何方法在对象与分布假设成熟后进入
8. **不让在线一次成功自动写入production H**——candidate规则禁止在线自动提示

### 其他规则指针

- **提示策略路线选择与Level连续谱**：详见 `dev-docs/214-v1-2026-08-06-提示策略路线选择与Level连续谱.md`。核心决策：走路线B（思维模式）而非路线A（堆砌知识）。
- **元组群guided-math-solving**：5个Skill详见 `.devin/rules/guided-math-solving.md`。
- **Tell分类学迭代审计铁律**：对已有profile做FCA再分析、Tell分类学修正时的SOP流程和版本化审计要求。详见 `.devin/rules/tell-taxonomy-iteration-audit.md`。**触发条件**：对已有profile做FCA再分析时；Tell分类学（`FCA学习笔记/08-先验Tell分类学.md`）需要修正时；用FCA理论审查分类学自洽性时。**核心约束**：再分析9步SOP + 版本化审计6条铁律（明面版本历史、四要素记录、覆盖性检查、版本总表、文件结构完整、关联文件同步）。
- **Tell分类学Schema维护铁律**：AGENTS.md中"Tell分类学Schema"节是跨压缩边界保真的核心，分类学修正后必须同步更新该节。详见 `.devin/rules/tell-taxonomy-schema-maintenance.md`。**触发条件**：Tell分类学版本号变化/段结构模式变化/domain变化/结构框架变化/观察Level参数变化/关键修正认知变化时。**核心约束**：08号文件和AGENTS.md Schema节必须一致，不一致即违反rule。
- **Tell分类学研究过程文档存放规则**：Tell分类学相关的研发过程文档（探索性、讨论性、评审性、方案演进性）记录到 `Tell分类学研究过程文档/`目录，不放在`第六代系统研发过程文档/`。编号从343号开始（333-340号已迁移至本目录，341-342号已被第六代研发过程文档占用）。**每次新增文档必须同步更新 `Tell分类学研究过程文档/README.md` 索引。** 详见 `.devin/rules/tell-taxonomy-research-docs.md`。
- **system/ 代码与 .ref 文件同步规则**：`system/` 中每个 `.py` 文件必须有同名 `.ref` 文件，内容是理解该模块需要参考的文档路径列表（相对 repo 根目录）。**改代码或改设计文档后都必须同步检查 .ref**——改了 `.py` 检查 `.ref` 是否还准确，改了设计文档检查引用该文档的 `.ref` 是否需要更新。详见 `.devin/rules/system-ref-sync.md`。
- **审计方法论**：F1-F15断层类型学、D1-D4深度等级、21审计维度，详见 `dev-docs/146-v4-2026-08-05-审计方法论手册-*.md`。
- **形式化思维规则**：从星学继承，适配数学。详见第一代技术说明书249号。
- **项目定位与核心假设**：数学大师制造项目，详见 `原语化AI数学工程系统设计/README.md`。核心假设从星学信念降级为可证伪假设，详见123号。
- **K维度多层知识结构（L1-L4）**：详见 `dev-docs/201号`系列。
- **AI在运行过程中的角色**：经典计算给候选，AI做最终判断。详见 `dev-docs/202号`。

---

## 工作系统技术说明

> 本节是工作系统（AI自己的工作认知管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用工作系统"的认知。

### CP1-CP6工作流

工作系统的核心是CP1-CP6六个检查点，通过`cognition_checkpoint_math.py`执行：

| CP | 时机 | 内容 | 命令 |
|---|---|---|---|
| CP1 | 工作开始前 | 种子选择：确定本次任务需要哪些种子认知单元 | `cognition_checkpoint_math.py start --seeds <cog_id1>,<cog_id2>` |
| CP2 | 工作开始前 | 认知加载：AQL图遍历，从种子出发沿depends_on边找到所有前置认知 | CP1命令自动执行 |
| CP3 | 工作开始前 | 缺口检查：验证已加载的认知是否覆盖任务所需 | CP1命令自动执行 |
| CP4 | 工作结束时 | 认知捕获：检查本次工作是否产生新方法论/新依赖/新版本/新术语/临场脚本 | git post-commit hook自动打印 |
| CP5 | 工作结束时 | 认知图更新：新版本/新边写入ArangoDB | `cognition_sdk_math.py`的add_version/add_edge |
| CP6 | 工作结束时 | 任务-认知映射：记录"这个任务用了哪些种子" | `cognition_sdk_math.py`的record_task |

**关键参数**：max_depth=7（数学项目路径比星学长，星学用5）

### Hook机制

| hook | 触发时机 | 脚本 | 作用 |
|---|---|---|---|
| SessionStart | 新session/压缩后 | `session_start_hook_math.py` | 注入认知图统计+工作纪律 |
| UserPromptSubmit | 每次用户提问 | `user_prompt_submit_hook_math.py` | 从`UserPromptSubmit.txt`读取提醒注入 |
| git post-commit | 每次commit后 | `githooks/post-commit` | 打印CP4检查清单（从稀疏矩阵动态查询） |

**改提醒内容**：直接编辑`xishujuzhen/UserPromptSubmit.txt`。**不要用Stop hook**：Stop hook会影响subagent。

### 工作系统纪律

1. **新术语必须追加到词汇表**（认知单元 `glossary`）。
2. **临场脚本沉淀纪律**：现写的一次性脚本，如果操作模式可复用，结束后必须沉淀到 `cognition_sdk_math.py`。
3. **必须 commit**：commit 后 git post-commit hook 会打印 CP4 检查清单。
4. **认知图变更后跑回归验证**：运行 `cognition_audit_math.py poc-regression`。
5. **边吸收边测试**：每次往依赖图/认知图装入新内容后，必须立即跑测试验证。
6. **"检查依赖"触发词**：当用户说"检查依赖"时，AI 立即执行CP4检查清单中的第3、4项。

---

## 当前任务意识跨压缩边界保有用的一节

> 本节是**临时性**的，用于跨压缩边界保持当前活跃任务的完整工作意识。任务完成后清空，把需要长期保持的认知迁移到TODO或Memory Section。

### 当前任务：第六代系统研发

**任务背景**：第五代系统技术说明书50个文件已全部完成。当前进入第六代系统研发阶段——围绕非局部tell、FCA数学基础、并发Telling AI、Pipe 0简化+Pipe 2并行化等方向展开。

**文档存放**：第六代有两个文档目录，性质不同——
- `第六代系统研发过程文档/`：探索性、讨论性、评审性文档，三位编号（303号起），和 grove repo 同步。研发过程中不确定的内容放这里。
- `第六代系统技术说明书/`：规范性、工程性技术规格，章节编号（01-09）。只有经过讨论、评审、确认真正值得最终记录的内容才放这里。
- 详见上方"第六代系统文档存放规则"小节。

**第五代系统技术说明书**：`第五代系统技术说明书/` 目录下50个文件已全部完成，作为第六代研发的参照系。加载顺序见 `第五代系统技术说明书/README.md`。

**第六代研发已完成的关键文档**（均在 `第六代系统研发过程文档/`）：
- 303-309号：从 grove repo 复制的7份探索文档（非局部tell、FCA、原语化、trace-tell-hint命名等）
- 310号：worktree侧对grove侧303-309号文档的评审——判断哪些方向有闪光点、哪些跑偏
- 311号：并发Telling AI方案——Pipe 0简化（粗domain分类）+ Pipe 2并行化（多Telling AI并行trace识别+汇总AI精筛）
- 312号：第六代系统的两个核心问题——Trace识别与Trace→Tell匹配
- 313号：Tell分类学研究——建立第六代Tell的分类体系
- 314号：第六代系统必须着力解决的三个问题——非局部tell库缺失/推理脉络格化/Tell分类学
- 315号：第六代系统的完整工作流——从推理AI探索到引导树填充+完备性检查（6个缺失全部不是问题）+Parser AI定义+脉络分析管线
- 316号：第六代系统理想化工作过程——规范化完整描述（9个章节）
- 317号：第六代系统POC验证方案——20个POC三层组织（基础能力/管线验证/系统验证）
- 318号：第六代系统流程Pipe图——Pipe命名与AI命名（Solver/Parser/Telling/Guide）
- 319号：第六代系统流程Pipe图——形式化定义（Python代码+dataclass）
- 320号：POC-VMS-28执行方案——AI一眼做格化+trace识别（IMO 2009 P6蚱蜢问题）
- 321号：第六代系统设计认知——提示词是核心资产
- 322号：POC-VMS-28提示词V2——用FCA和Hasse图启发AI，列8种复杂情况
- 323号：POC-VMS-28提示词V3——加上为什么、影响例子、反模式三个章节
- 324号：POC-VMS-28提示词V4——一份基础+两个附加章节（树状输入过程A/线性输入过程B）
- 325号：第六代系统设计认知——多套提示词并发
- 326号：第六代系统设计认知——三处对齐同步（目录/代码清单/POC验证）
- 327号：POC-VMS-28执行方案v1——用V4提示词做第一次POC（一次一套set_A）
- 328号：第六代系统设计认知——文档自包含与可审计标准（通用，适用于所有研发过程文档）
- 329号：POC-VMS-28执行方案v2——自包含版（按328号标准重写）
- 333号：脉络分析Pipe内细化方案——格化与trace识别分离（三阶段架构：格化→程序枚举→综合分析）
- 334号：脉络分析新管线审计结果与改进方案——nonlocal trace退化修复（审计维度+历史运行对比+迭代终止条件）
- 335号：V8格化session的thinking过大问题分析——保守方案（不拆分，简化提示词+超时降级；v1修订：方案D 2步文件拆分，验证不退化）
- 336号：综合分析阶段文件拆分流程控制方案——不会退化的4阶段拆分（验证大幅提升：trace 43→88）
- 337号：全管线验证计划——格化+综合分析双文件拆分（6个验证维度+通过标准）
- 338号：全管线非退化审计方案——各V各阶段历史对比（3层审计+7个历史轮次+文件版本追踪）
- 339号：研发资产管理改进方案——从文件版本追踪的痛苦中提炼（run_manifest.json+4层保证）
- 340号：子管线超时降级方案——不卡住整个系统（独立超时+至少1个通过即可+数据库记录+入口返回值）
- 341号：全流程日志方案——滚动日志到system/logs/（单文件1MB+目录500MB+循环滚动）
- 342号：系统时间意识方案——全管线全子管线运行时间记录（3层时间记录+数据库timing字段+耗时摘要）
- 343号：six/合并到system/方案——system成为自包含的第六代系统（代码层+文档层+运行时层，终止six/维护）

### 系统时间意识与效率意识（342号方案落实）

**这是系统的功能，不是可选的附加**——整个系统必须有时间意识、效率意识。

**3层时间记录**：

1. **日志时间戳**（341号方案）：每条日志带`[YYYY-MM-DD HH:MM:SS]`时间戳，关键位置记录耗时（"格化版本V8完成，耗时200秒"）

2. **数据库结构化时间记录**：`problem_entries`集合的`timing`字段记录全管线全子管线运行时间：
   - `total_duration_sec`：总耗时
   - `phase1_grading.duration_sec` + `versions.{V5/V7/V8/V10}.duration_sec`：格化阶段总耗时+各版本耗时
   - `phase1_5_enumerate.duration_sec` + `versions.{V7/V8/V10}.closed_elements_count`：枚举阶段耗时+各版本闭元素数
   - `phase2_synthesis.duration_sec` + `steps.{step1-4}.duration_sec`：综合分析总耗时+4阶段拆分各步耗时

3. **运行结束耗时摘要**：运行结束时打印耗时摘要表：
   ```
   === 耗时摘要 ===
   阶段1 格化: 300秒（V5:180s V7:超时 V8:200s V10:280s）
   阶段1.5 枚举: 5秒（V7:闭元素27 V8:闭元素46 V10:闭元素26）
   阶段2 综合分析: 720秒（step1:120s step2:240s step3:150s step4:210s）
   总耗时: 1025秒（17分钟）
   ```

**时间数据用途**：
- 效率分析——定位瓶颈（格化慢还是综合分析慢？哪个版本最慢？综合分析哪个step最耗时？）
- 超时阈值调优——340号方案的超时时间需要历史耗时数据支撑
- 运行对比——不同run_id的耗时对比，发现性能退化

### 研发资产管理（339号方案落实）

**运行资产**：
- 每次运行的工作目录：`palyground/absorb/vein_analysis/{run_id:04d}_{problem_id}/`
- 每次运行的归档目录：`system/tests/vein_analysis/runs/{run_id:04d}/`（vein_analysis.py自动归档）
- 每次运行必须生成`run_manifest.json`——记录所有提示词文件、AGENTS模板、step要求文件、代码的md5和git commit
- 回头审计时从run_manifest.json找文件版本，不需要md5对比git历史

**目录命名**：
- 正式运行：`{run_id:04d}_{problem_id}`（如`0011_imo2009p6`）
- 单独测试：`{run_id:04d}_{problem_id}_{test_type}`（test_type只能是`synthtest`/`v8test`等预定义值）
- 不允许无run_id的目录（早期`imo2009p6`是历史遗留，不再新增）

**数据库记录**：
- 每次运行必须写`problem_entries`集合，包含`manifest_path`/`archive_path`/`git_commit`字段
- 中断的运行必须标记为`interrupted`（不是`running`）——TODO，优先级低
- 单独测试也要写数据库——TODO，优先级低

**审计流程**（改进后）：
1. 从数据库查run_id → 直接得到`manifest_path`和`archive_path`
2. 读run_manifest.json → 直接得到所有文件版本、md5、git commit
3. `git show <commit>:<文件路径>` → 查看当时的文件内容

**第六代系统架构文档**（`system/docs/`）——system是自包含的第六代系统：

> **核心定位**：`system/`是自包含的第六代系统——从代码到文档，到运行时。`six/`目录已合并到`system/`（343号方案），不再维护。理解第六代系统只需要看`system/`。
>
> **三层结构**：
> - **代码层**：`*.py` + `.ref` + `.ai-check`——真正运行的代码
> - **文档层**：`docs/`——模块设计说明书 + 系统架构文档
> - **运行时层**：`assets/`——AGENTS模板等运行时资产

**系统架构文档**（`system/docs/architecture.md`）——四个Pipe+两个过程+设计原则+验证历史：

> 包含：四个Pipe（Solver/Parser/Telling/Guide）+两个过程（解题引导/解答吸收）+设计原则（解放思想/反射）+提示词设计认知+VMS-28到28e验证历史+4并发方案+根本认知。

**研发文档索引**（`system/docs/references.md`）——研发过程的"晾衣架"：

> 研发过程文档清单（303-343号）+代码元素到研发文档的映射+POC验证清单（VMS-11到VMS-30）+三个核心问题+系统根本认知+三阶段架构+文件拆分流程控制+脉络分析审计+超时降级+全流程日志+系统时间意识。

**数据结构设计说明书**（`system/docs/schema.md`）——25个dataclass+FCA术语映射：

> 25个dataclass分类+FCA术语映射（双轨术语330号）+核心数据结构详解（Trace/Tell/Segment/LevelView的FCA对应说明）。

**设计原则——解放思想**：

> **核心原则**：不要觉得每个函数只能一个AI、一种方式去做。时时考虑三个维度：
> 1. **多种方式**——同一个函数可以用多种方式实现，用POC验证决定哪种方式可行（如VMS-28/29/30验证三种格化方式）
> 2. **多个AI**——同一个函数可以由多个AI实例并发执行（如311号的并发Telling AI）
> 3. **多个子pipe**——一个函数可以进一步迭代，拆分为多个子函数，每个子pipe独立验证、独立实现

**设计原则——反射**：

> **核心原则**：系统的各处不应该是完全固化的，而是随着系统运行、使用经验丰富而成长发展。流程中必须在合适的地方进行反射——系统停下来审视自己的行为，从中学习，改进自己。
>
> **反射的三层对象**：反射自己的产出 / 反射自己的流程 / 反射自己的认知
> **反射的触发时机**：每次循环结束后 / 匹配失败时 / 停机后 / 周期性反思 / 人工触发
> **和解放思想的关系**：解放思想是设计时的开放性（不要固化设计），反射是运行时的开放性（不要固化运行）。两者配套。

**设计认知——提示词是核心资产**（321号）：

> **核心认知**：六代系统势必积累很多提示词，用于启发AI完成相关的工作。提示词是系统的核心资产，和代码同等重要。
>
> **提示词管理**：提示词需要积累、管理、版本化。每个版本记录版本号/内容/改进原因/验证状态/使用效果。旧版本保留用于对比和回退。提示词和代码一起版本化管理。

**提示词积累目录**（`第六代系统提示词积累目录/`）：

> 提示词完整文本在`第六代系统提示词积累目录/`中按目录结构积累：`Pipe阶段/子pipe/set_<编号>_<简短描述>/v<版本号>.md` + `README.md`
>
> **当前积累**：
> - `pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/`：套A（用FCA/Hasse图启发），V5/V7/V8/V10四个版本+综合分析提示词+4阶段step要求
> - 其他Pipe阶段的目录已建，待积累
>
> **三处对齐同步（326号，硬约束）**：提示词在三个地方有记录，必须对齐同步——
> - **A：提示词积累目录**（`第六代系统提示词积累目录/`）——提示词的完整文本
> - **B：运行时资产**（`system/assets/`）——AGENTS模板（运行时复制到工作目录）
> - **C：POC验证文档**（`第六代系统研发过程文档/3xx号`）——提示词的验证结果
>
> 新增提示词时三处同步创建；改进提示词时三处同步更新版本；POC验证完成后三处同步更新验证状态。

**Schema——晾衣架的完整地形图**：

| 代码位置 | 内容 | 对应的研发文档 | 什么时候看 |
|---|---|---|---|
| `system/schema.py` → `Problem` | 题目数据结构 | 第五代01-基础概念/04-两棵树.md | 讨论题目时 |
| `system/schema.py` → `Hint` | 提示Q数据结构 | 000号+315号§5阶段6 | 讨论hint时 |
| `system/schema.py` → `Tell` | tell数据结构（含分类学四层位置） | 000号+313号§4.1+287号+315号§4.1 | 讨论tell时 |
| `system/schema.py` → `Trace` | trace数据结构（含is_branch_position） | 309号+314号问题2+313号§4.1+315号§6.2.2 | 讨论trace时 |
| `system/schema.py` → `Vein/Segment/Branch/LevelView` | 脉络相关数据结构 | 312号+304号§8.9+318号§4+314号问题2 | 讨论脉络格化时 |
| `system/schema.py` → `Thinking/SolutionRecord` | Pipe 0输出/过程B输入 | 第五代03-引导树闭环.md+315号§6.2.1 | 讨论过程A/B输入时 |
| `system/schema.py` → `SolverInput/SolverOutput` | Pipe 0输入输出 | 319号§1+315号§6.8 | 讨论Solver AI时 |
| `system/schema.py` → `AnalysisInput/AnalysisOutput` | Pipe 1输入输出 | 333号+335号+336号 | 讨论Parser AI时 |
| `system/vein_analysis.py` → `vein_analysis_three_phase()` | 三阶段脉络分析 | 333号+336号 | 讨论脉络分析时 |
| `system/verify_lattice_completeness.py` | 闭元素枚举+三层验证 | 332号 | 讨论程序验证时 |

**第六代系统词汇表**（术语定义 + 代码Schema结合）：

> 以下每个术语给出：定义、来源文档、对应的代码Schema（dataclass/字段）。AI看到术语时，既知道定义，又知道代码中的对应。术语新增时必须追加到此表（工作系统纪律第1条）。

**基础概念**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **题目（Problem）** | 一道数学题——有problem_id/problem_text/domain/answer | 第五代01-基础概念 | `types.py`→`Problem`：problem_id, problem_text, domain, answer |
| **提示Q / hint** | 引导从一个数学处境移动到另一个处境的语义移动。tell的注入端。tell+hint构成二元组。 | 000号§引导树闭环 | `types.py`→`Hint`：hint_id, hint_text, hint_level(0=最具体,N=最抽象), tell_id |
| **tell** | 从trace去特化后存入库中的可泛化思维模式。tell是trace的"泛化版"——从这道题的trace提取出可以启发其他题的思维模式。tell的四个成分：分叉信号/分叉类型/未探索诊断/方向匹配。 | 000号+285号v2修正 | `types.py`→`Tell`：tell_id, branch_signal, branch_type, unexplored_diagnosis, direction_matching, domain, trace_type, segment_pattern, specific_concept |
| **trace** | 在脉络的某个Level视图上识别出的思维模式。trace是Parser AI的产出，Telling AI的输入。过程A描述"AI在这里可以分叉但没分叉"，过程B描述"解答者在这里做了某个操作"。 | 309号+314号问题2+319号 | `types.py`→`Trace`：trace_id, level(0=最细,N=最粗), trace_type(local/non_local/global), pattern_description, source_segment_ids, is_branch_position(仅过程A) |
| **局部trace** | 在单个段上（Level 0）识别出的思维模式。 | 322号§1第二部分 | `Trace.trace_type="local"`，`Trace.source_segment_ids`长度=1 |
| **非局部trace** | 跨多个段的思维模式——只有把几个段合在一起看才能识别出的模式。中间Level视图上的trace。 | 303号+322号§1第二部分 | `Trace.trace_type="non_local"`，`Trace.source_segment_ids`长度>1 |
| **全局trace** | 整个脉络层面的策略模式——只有把所有段合在一起看（最粗Level）才能识别出的模式。 | 322号§1第二部分 | `Trace.trace_type="global"`，`Trace.source_segment_ids`包含所有段 |
| **数学处境（MathSituation）** | 引导树/解题树的节点——一个数学处境。有node_type(root/internal/leaf_success/leaf_deadend/leaf_truncated)。 | 第五代04-两棵树 | `types.py`→`MathSituation`：node_id, problem_id, node_type, situation_text, depth, path_from_root, parent_edge_key |
| **树的边（TreeEdge）** | 引导树/解题树的边——一个提示Q。连接父节点和子节点。 | 第五代04-两棵树 | `types.py`→`TreeEdge`：edge_id, from_node, to_node, hint(Hint), level |

**脉络相关概念**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **脉络（Vein）** | 从推理内容中分析出的思维脉络。过程A从Thinking分析→可能有分叉的树/DAG；过程B从SolutionRecord分析→通常线性。 | 312号+319号 | `types.py`→`Vein`：vein_id, source_id, source_type(thinking/solution_record), structure(linear/tree/dag), segments(list[Segment]), branches(list[Branch]) |
| **段（Segment）** | 脉络中的一个推理步骤或一段推理。最细的段划分是把脉络分成最小的推理步骤。段有特征（用于FCA形式上下文的属性）。 | 314号问题2+319号 | `types.py`→`Segment`：segment_id, vein_id, segment_text, segment_features(dict), order |
| **分叉（Branch）** | 脉络中AI选了A没选B的位置（仅过程A）。 | 000号+319号 | `types.py`→`Branch`：branch_id, vein_id, at_segment_id, chosen_path, unchosen_paths(list) |
| **Level视图（LevelView）** | 段的一种合并方式形成的"看法"。最细Level=每个段独立；最粗Level=所有段合并；中间Level=几个段合并。 | 322号§1第一部分+319号 | `types.py`→`LevelView`：view_id, vein_id, level(0=最细,N=最粗), merged_segments(list[list[str]]), view_features(dict) |
| **格化（grid_vein）** | 把脉络分成段后，考虑段的不同合并方式。每种合并方式形成一个Level视图。"有意义的合并"是把"在思维上属于同一层"的段合在一起。 | 314号问题2+319号§step_2_grid_vein | `pipes.py`→`pipe_1_parser()`的子pipe `step_2_grid_vein()`；产出`list[LevelView]` |
| **FCA（形式概念分析）** | 用闭包算子定义"有意义的合并"——闭元素是指属性闭包等于自身的段集合。直觉上说，闭元素就是"在思维上属于同一层"的段集合。 | 304号 | `Segment.segment_features`是FCA形式上下文的属性集 |
| **Hasse图** | 格的可视化——最下面是最细Level，最上面是最粗Level，中间是各个中间Level，节点之间的边表示"从细到粗的合并关系"。 | 322号§1第一部分 | `LevelView`的level字段定义了Hasse图的层次 |

**过程A/B和输入**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **过程A** | 分析推理AI的上下文——输入是树状的（推理AI探索后折返）。Parser AI在过程A中分析推理AI的thinking/trajectory。 | 319号§pipe_1_parser+324号附加章节A | `ParserInput.process="A"`，`ParserInput.thinking: Thinking` |
| **过程B** | 分析已有题目和解答记录——输入是线性的（已完成解答）。Parser AI在过程B中分析外部解答文本。 | 319号§pipe_1_parser+324号附加章节B | `ParserInput.process="B"`，`ParserInput.solution_record: SolutionRecord` |
| **Thinking** | 推理AI的thinking/trajectory——Pipe 0的输出，Pipe 1过程A的输入。 | 第五代03-引导树闭环+315号 | `types.py`→`Thinking`：solver_ai_id, problem_id, trajectory, rounds(list[dict]), entry_node_id, entry_hint(Hint) |
| **解答记录（SolutionRecord）** | 外部解答记录——Pipe 1过程B的输入。和Thinking的区别：解答记录是已完成的、正确的、通常线性的脉络。 | 315号§6.2.1 | `types.py`→`SolutionRecord`：record_id, problem(Problem), solution_text, is_verified |
| **孤悬trace（orphan trace）** | 没匹配到tell的trace。过程A的孤悬trace存档后用于启发过程B——"从什么Level观察外部解答记录"。 | 315号§6.2 | `TellingOutput.unmatched_traces: list[Trace]`；`Step5Output.orphan_traces`；`loops.py`→`archive_orphan_traces()`/`get_archived_orphan_traces()` |

**Pipe和AI角色**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **Pipe 0 / Solver AI** | 推理AI——做数学。输入是题目+脉络文本+方向Q，输出是thinking+最终状态+终点节点。 | 318号§2.1+315号§6.8 | `pipes.py`→`pipe_0_solver()`；`SolverInput`(problem, path_text, hint)→`SolverOutput`(thinking, final_status, final_situation) |
| **Pipe 1 / Parser AI** | 分析AI——从Thinking(过程A)或SolutionRecord(过程B)中分析脉络、格化、识别全Level Trace。三个子step：step_1_analyze_vein / step_2_grid_vein / step_3_identify_traces。 | 318号§3.1+315号§6.2.2+319号 | `pipes.py`→`pipe_1_parser()`；`ParserInput`(process, thinking, solution_record, orphan_traces)→`ParserOutput`(traces, veins, level_views, process) |
| **Pipe 2 / Telling AI** | 匹配AI——把trace匹配到tell库中的tell。311号后改为多AI并发，每个Telling AI负责一个domain分区。不需要汇总AI（315号确认）。 | 318号§2.1+311号+315号§6.3 | `pipes.py`→`pipe_2_telling()`；`TellingInput`(traces, tell_library_path)→`TellingOutput`(results(list[TellingResult]), unmatched_traces) |
| **步骤5分叉** | Pipe 2输出后的分叉——过程A：匹配到tell→取hint送入Pipe 3；没匹配到→孤悬trace存档。过程B：新建tell+hint存入AGENTS.md。 | 315号§6.2.1/6.4+319号 | `pipes.py`→`step_5_branch()`；`Step5Input`(telling_output, process)→`Step5Output`(process, hints, orphan_traces, new_tells, new_hints) |
| **Pipe 3 / Guide AI** | 引导AI——把hint变成引导树的新边，构造新SolverInput，启动新推理AI。 | 318号§2.1+315号§6.5/6.6 | `pipes.py`→`pipe_3_guide()`；`GuideInput`(hints, problem_id, tree_state)→`GuideOutput`(new_edges, new_solver_inputs, tree_state, stop) |
| **引导树（Guided Expansion Tree）** | "应该往哪走"的视图。每个节点是一个数学处境，每条边是一个提示Q。活的、正在生长的。 | AGENTS.md§Grove核心循环 | `types.py`→`TreeState`：problem_id, nodes(list[MathSituation]), edges(list[TreeEdge]), status(growing/solved/exhausted), running_solvers |
| **解题树（Solution Record Tree）** | "实际走了什么"的视图。引导展开树展开完成后凝固的树。包含成功路径、失败路径、分叉点。 | AGENTS.md§Grove核心循环 | 同`TreeState`——两棵树是同一棵树的两个面 |

**系统级概念**：

| 术语 | 定义 | 来源 | 代码Schema |
|---|---|---|---|
| **tell分类学** | tell的四层分类位置——第一层domain(数论/代数/...)、第二层trace_type(local/non_local/global)、第三层segment_pattern(段结构模式)、第四层specific_concept(具体概念)。 | 313号§4.1 | `Tell`的四个字段：domain, trace_type, segment_pattern, specific_concept |
| **三个核心问题** | 314号定义的三个必须着力解决的问题——①非局部tell库缺失②推理脉络格化③Tell分类学。 | 314号 | `system/docs/references.md` §4 |
| **方式A/B/C** | 317号定义的三种格化方式——A：AI做全部格化+trace识别，FCA是理论指导；B：脚本运行FCA格遍历算法；C：AI做+FCA验证。 | 317号§VMS-28/29/30 | `system/docs/architecture.md` §5验证历史 |
| **多套提示词并发** | 同一Pipe阶段可以有多套不同的提示词（不是不同版本号，是完全不同的设计），并发给多个AI实例处理同一输入。 | 325号§1 | `第六代系统提示词积累目录/`中的set_A/set_B/... |
| **三处对齐同步** | 提示词在三个地方有记录——A目录(完整文本)、B运行时资产(system/assets/)、C POC验证文档——三处必须对齐同步。 | 326号§1 | 提示词积累目录+system/assets/+研发过程文档 |
| **trace→tell匹配（TraceTellMatch）** | 一个trace匹配到一个tell的结果——有trace_id/tell_id/confidence/matched。 | 319号 | `system/schema.py`→`TraceTellMatch`：trace_id, tell_id, confidence(float), matched(bool) |
| `system/process_solve.py` | 解题引导过程（Grove核心循环） | 319号§1+第五代03-引导树闭环.md+315号§6 | 讨论端到端工作流时 |
| `system/process_absorb.py` | 解答吸收过程（tell库增长循环） | 319号§1+315号§6.2.1 | 讨论Parser AI处理外部解答时 |
| `system/docs/references.md` → §1 | 研发过程文档清单（303-343号） | 全部 | 需要查文档编号时 |
| `system/docs/references.md` → §2 | 代码元素到研发文档的映射 | 全部 | 需要追溯代码元素来源时 |
| `system/docs/references.md` → §3 | POC验证清单（VMS-11到VMS-30） | 317号 | 讨论POC验证时 |
| `system/docs/references.md` → §4 | 314号三个必须着力解决的问题 | 314号 | 讨论系统核心问题时 |
| `system/docs/references.md` → §5 | 系统的根本认知 | 315号§6.8+第五代 | 讨论系统设计理念时 |

**如何使用system/docs/**：

1. **用户提到某个概念时**→查`system/docs/references.md` §2，找到对应的代码元素和来源文档
2. **需要查POC验证时**→查`system/docs/references.md` §3
3. **需要查研发文档编号时**→查`system/docs/references.md` §1
4. **需要看某个数据结构的定义时**→看`system/schema.py`中对应的dataclass + `system/docs/schema.md`中的FCA对应说明
5. **需要看系统架构时**→看`system/docs/architecture.md`（四个Pipe+设计原则+验证历史）
6. **需要看脉络分析模块时**→看`system/docs/vein_analysis.md`（三阶段架构+文件拆分）

**如何维护system/docs/**：

1. **新增研发文档时**→在`system/docs/references.md` §1中添加条目
2. **新增或修改数据结构时**→在`system/schema.py`中修改，同时在`system/docs/schema.md`中更新FCA对应说明
3. **新增POC时**→在`system/docs/references.md` §3中添加条目
4. **POC验证完成后**→在`system/docs/references.md` §3中更新状态，在`system/docs/architecture.md`中更新验证历史
5. **修改Pipe接口时**→同步修改`system/schema.py`（输入输出数据结构）+对应模块代码+`system/docs/`中的模块文档
6. **新增核心问题或认知时**→在`system/docs/references.md` §4或§5中添加

**维护规则**：
- 代码元素（dataclass/函数/参数）和`system/docs/references.md`中的映射必须同步——改了一个必须改另一个
- 模块代码变更时同步更新对应的`system/docs/`模块文档
- `system/docs/references.md`是只读索引——不包含实现逻辑，只包含映射关系
- `.ref`文件引用`system/docs/`中的模块文档路径

**设计原则rule绑定**（rule文件在`.devin/rules/`中，AGENTS.md只保留索引）：

| rule | 文件 | 触发条件 | 来源 |
|---|---|---|---|
| **代码为中心铁律** | `.devin/rules/six-codebase-first.md` + `.devin/skills/codebase-first/SKILL.md` | **always-on——任何时候回答或响应用户提问时** | 用户原话 |
| 解放思想原则 | `.devin/rules/six-liberation-principle.md` | 设计或修改任何函数时 | 318号/`principles.py` |
| 反射原则 | `.devin/rules/six-reflection-principle.md` | 设计或修改任何Pipe函数时 | `reflection.py` |
| 提示词原则+三处对齐同步 | `.devin/rules/six-prompt-principle.md` | 设计或修改任何Pipe函数时；新增/改进/验证提示词时 | 321/325/326号/`prompts.py` |
| 文档自包含与可审计 | `.devin/rules/six-doc-selfcontained.md` | 编写或修改任何研发过程文档时 | 328号 |
| 三个核心问题 | `.devin/rules/six-core-problems.md` | 设计或修改任何Pipe时 | 314号/`references.py` |
| POC三层组织 | `.devin/rules/six-poc-organization.md` | 设计新POC时 | 317号/`references.py` |
| 形式化定义同步 | `.devin/rules/six-formal-def-sync.md` | 修改任何dataclass或Pipe函数签名时 | 319号/`types.py`/`pipes.py` |
| 完整工作流对照 | `.devin/rules/six-workflow-alignment.md` | 设计或修改任何Pipe衔接关系时 | 315号/`loops.py` |
| 双轨术语原则 | `.devin/rules/six-dual-terminology.md` | 编写或修订提示词、技术文档、代码注释时涉及术语选择 | 330号§4 |
| 提示词自包含 | `.devin/rules/six-prompt-selfcontained.md` | 创建或修订提示词文件时 | 328号/330号§4建议D |
| **机械化过程描述+程序验证** | `.devin/rules/six-mechanization-reference.md` + `.devin/skills/mechanization-reference/SKILL.md` | 设计提示词时，当认知任务有对应机械化算法且AI用直觉做但产出需完备性保证时 | 332号/用户原话（系统创新） |
| **运行痕迹全程保留** | `.devin/rules/six-trace-preservation.md` | **always-on——设计或实现系统任何运行阶段、阶段间数据传递、AI实例启动、数据库写入时** | 用户原话（系统设计必须既要考虑运行逻辑，也要考虑痕迹保留） |
| **AI Agent启动规范** | `.devin/rules/six-ai-agent-launch.md` | **always-on——启动系统中任何AI Agent实例时** | 用户原话（全部使用tmux，先到指定目录，准备好AGENTS.md和提示词文件，短启动提示词+提示词文件加载） |
| **双重检查机制** | `.devin/rules/six-dual-check-mechanism.md` | **always-on——设计或实现系统任何运行阶段后；系统运行中检查健康状态时；系统运行后审计产出质量时** | 用户原话（代码能保证的用代码检查，无法用代码完成的用流程审计AI检查，.ai-check文件记录checklist） |
| **"更新文档"动作定义** | `.devin/rules/six-update-docs-action.md` | **用户在system系统研发中说"更新文档"时** | 用户原话（"更新文档"代表很多动作，需要思考哪些文档需要更新，以后只说一句更新文档就全面检查） |
| **系统资产分级与上下文预算** | `.devin/rules/six-asset-grading.md` | **always-on——设计或修改AI Agent的AGENTS.md内容时；设计或修改提示词文件时；向AI Agent发送直接提示词时；向system/添加新的资产文件时** | 用户原话（AGENTS.md和可复用提示词是system资产，题目解答放文件中，大块要求放文件中，直接提示词不大块，分类学资产从AGENTS.md拆分到单独文件，单文件300行限制，超长检测+警报） |
| **系统测试规矩** | `.devin/rules/six-test-discipline.md` | **always-on——为系统模块编写测试、POC验证、回归验证时；在`system/tests/`下创建测试资产时；架构改动后需要验证不退化时** | 用户原话（测试不是用完就扔的临时文件，方案先行、按模块组织、内容全留存） |
| **文件拆分流程控制** | `.devin/rules/six-file-staged-flow.md` | **always-on——设计提示词时，当一个AI session的工作流程有多个阶段且thinking可能过大时** | 用户原话（335号V8改进为例） |
| **运行数字ID命名规范** | `.devin/rules/six-run-id-naming.md` | **always-on——任何系统运行、测试、实验、审计存档时** | 用户原话（数字ID是可查可审计的保证，应该在任何它应该出现的地方出现） |
| **数据库-文件双向可追溯性** | `.devin/rules/db-file-traceability.md` + `~/.config/devin/skills/db-file-traceability/SKILL.md` | **always-on——任何向数据库写入记录且同时产出物理文件时；声称"数据已入库"或"文件已落盘"前** | 用户原话（数据库和数据任何时候都可以被"顺藤摸瓜"，要做成AI的工作意识。362号验证发现3个gap后修复） |
| **研发资产管理** | `.devin/rules/six-asset-management.md` | **always-on——运行vein_analysis_three_phase()时；审计历史运行时；从数据库run_id查找运行资产时** | 339号方案（run_manifest.json+自动归档+目录命名规范+数据库字段，回头审计从5步缩减到3步且确定性） |

**第六代研发的核心方向**（截至2026-08-10）：
1. 非局部tell（303/305号）——tell不只在卡点，可以在脉络上任意点或跨多节点范围
2. FCA数学基础（304号）——形式概念分析为三层Pipe架构提供完备性证明和系统化格遍历算法
3. 并发Telling AI（311号）——Pipe 2从单AI串行变为多AI并行，每个Telling AI负责一个tell分区
4. Pipe 0简化（311号）——从精确拓扑化（8种组合+手工信号词）降级为粗domain分类
5. trace/tell/hint命名（309号）——trace=辅助AI识别产物，tell=库中标准化描述，hint=方向提示
6. Parser AI统一（315/318号）——分析AI和Parser AI统一为Parser AI，在过程A和过程B中都用同一套核心能力（提取格化全Level Trace）
7. 脉络分析管线（315/316号）——过程A和过程B共用步骤1-4，只在步骤5分叉
8. 四个Pipe命名（318/319号）——Solver AI/Parser AI/Telling AI/Guide AI

**已识别的跑偏方向**（310号评审结论）：
- 307号原语化——破坏推理AI独立性，拒绝"必须原语化"，保留"可选优化"定位
- 309号"范式转变"原主张——Pipe 0/1/2融合成一次分析在大规模下不成立；但用户后续提出的"分区后并发Telling AI"是Pipe 2并行化，不跑偏

---

## TODO

> 本节记录跨 Session 需要保持的待办事项。

### 第五代系统技术说明书（✅全部完成）

- [x] 编写01-基础概念（6文件）——tell+hint二元组/引导树闭环/两棵树/Level/概念树
- [x] 编写06-四代继承（6文件）——盘古/女娲/燧人/伏羲的遗产+第五代独特贡献+核心洞察继承
- [x] 编写02-tell端（7文件）——四个成分/去特化/Pipe 0/1/2/标准化语言描述/schema
- [x] 编写03-hint端（5文件）——字典结构/Level梯度/脉络继承/方向注入/schema
- [x] 编写04-概念树（5文件）——大概念小概念/概念文件格式/按需加载/概念膨胀应对/schema
- [x] 编写05-引导树闭环（5文件）——三个推动关系/并发DFS/回溯铁律/停机条件/辅助智能体JD
- [x] 编写07-工程规格（9文件）——系统架构总图/Pipe接口定义/ArangoDB schema/AQL查询模板等
- [x] 编写08-验证状态（5文件）——POC-VMS-8/9/10+验证总结+POC系列方案
- [x] 编写09-附录（3文件）——术语表/文档索引/参考文献

### 第六代系统必须着力解决的问题（314号）

> **文档**：`第六代系统研发过程文档/314-v0-2026-08-10-第六代系统必须着力解决的问题.md`
> **问题1（库侧）**：现有4164个tell全部是第五代局部分析方法的产物，没有经过非局部分析。tell库中看不到"反证法"、"同构之桥"、"构造-分析-排除"等高Level/非局部tell。用当前分析方法分析费马大定理证明，AI绝对不会分析出"同构之桥"。
> **问题2（识别侧）**：推理脉络的"格"化——如何找出所有Level的脉络视图。非局部tell存在于中间Level，但要找到中间Level的tell，必须先把推理脉络格化。n个节点的脉络有2^(n-1)种看法，不能全枚举，需要用FCA格遍历算法系统化地找出有意义的Level视图。问题2是问题1的前置。
> **问题3（分类侧）**：Tell的分类学——建立同时覆盖局部tell和非局部tell的分类体系。313号已启动研究任务线。依赖问题1和问题2，但局部tell的分类部分可以独立先行。

- [ ] **定义"有意义的合并"**——什么样的段合并产生有段特征的段？（304号§8.15的三个例子给出线索：构造+分析+排除合并后有"构造的目的"这个段特征）
- [ ] **把推理脉络转化为FCA形式上下文**——对象=脉络的段，属性=段特征，用闭包算子计算概念格，概念格就是所有有意义的Level视图（304号§7的gap+§8.9的对接）
- [ ] **用FCA格遍历算法系统化枚举Level视图**——不暴力枚举2^(n-1)种看法，用Next Closure/In-Close算法枚举闭元素（304号§8.7）
- [ ] **建立非局部trace的识别方法**——在每个Level视图上做trace识别，不只看一个Level（问题1的识别侧）
- [ ] **用非局部分析方法重新分析现有题目**——对现有455个profile的thinking做非局部分析，补充非局部tell到库中（问题1的库侧）
- [ ] **在非局部tell的基础上建立分类学**——分类学要同时覆盖局部tell和非局部tell，不能只覆盖局部tell

### 第六代系统研发（当前）

- [ ] 设计Telling AI提示词模板（311号§6.2）——提示词必须包含非局部分析的指导
- [ ] 定义汇总AI的判断标准——去重/排序/冲突解决（311号§6.3）——315号已确认不需要汇总，此项可能需要修订

### 第六代系统POC验证（317号启动）

> **方案文档**：`第六代系统研发过程文档/317-v0-2026-08-10-第六代系统POC验证方案-大量POC的设计.md`
> **审计后20个POC按三层组织**：基础能力(VMS-11/12/13/20/24/27/28/29/30)→管线验证(VMS-14/15/16/21/22/23/25)→系统验证(VMS-17/18/19/26)

**第一层：基础能力验证（9个可并行）**
- [ ] **POC-VMS-11**：非局部trace识别——用费马大定理证明作为脉络，验证能否识别"同构之桥"等非局部trace
- [ ] **POC-VMS-12**：推理脉络格化——用FCA格遍历算法找出有意义的Level视图
- [ ] **POC-VMS-13**：Tell分类学基础——查数据库了解现有4164个tell的分类现状
- [ ] **POC-VMS-20**：Pipe 0简化版——粗domain分类实现方式验证（311号§3.2）
- [ ] **POC-VMS-24**：当前分析方法局限性验证——费马大定理证明作为基线（314号§1.2）
- [ ] **POC-VMS-27**：已有产物二次分析——提取格化的全Level Trace（3-5个不同domain的profile，依赖VMS-12，314/312号）
- [ ] **POC-VMS-28**：方式A——AI做全部格化+trace识别，FCA是理论指导（316号§5+用户提问）
- [ ] **POC-VMS-29**：方式B——脚本做FCA格化，AI做trace识别（316号§5+用户提问）
- [ ] **POC-VMS-30**：方式C——AI做全部，FCA验证补漏（316号§5+用户提问）

**第二层：管线验证（7个）**
- [ ] **POC-VMS-14**：脉络分析管线——步骤1-4完整管线端到端运行（依赖VMS-11+VMS-12）
- [ ] **POC-VMS-15**：并发Telling AI——多个Devin CLI实例并发做trace→tell匹配（依赖VMS-13）+分区粒度验证
- [ ] **POC-VMS-16**：Parser AI——从外部解答记录识别新(tell,hint)（依赖VMS-14）+两个输入机制验证
- [ ] **POC-VMS-21**：分类维度结构验证——四层层次结构vs正交维度（依赖VMS-13，313号§4.1）
- [ ] **POC-VMS-22**：FCA角色验证——用FCA定义分类体系vs用FCA验证完备性（依赖VMS-13+21，313号§4.3）
- [ ] **POC-VMS-23**：非局部tell库补充——重新分析现有455个profile（依赖VMS-11，314号§2.1）
- [ ] **POC-VMS-25**：Tell存储方案——目录AGENTS.md+Devin CLI启动+可审计遍历（依赖VMS-13+21，315号§4.1）

**第三层：系统验证（4个）**
- [ ] **POC-VMS-17**：端到端工作流——完整7阶段循环（依赖VMS-14+VMS-15）
- [ ] **POC-VMS-18**：引导树妖娆生长——多Level多方向分叉（依赖VMS-17）
- [ ] **POC-VMS-19**：tell库持续增长闭环——过程A→过程B→过程A（依赖VMS-16+VMS-17）+管线统一性验证
- [ ] **POC-VMS-26**：两棵树Level问题——非局部trace的树级位置（依赖VMS-17，315/316号）

### Tell分类学Schema（跨压缩边界保真 · 对抗遗忘）

> **本节是Tell分类学的核心Schema——跨压缩边界也不能忘的东西。** 完整分类学在`FCA学习笔记/08-先验Tell分类学.md`（v3），本节只记录最紧要的结构。如果session压缩后你只记得本节内容，你仍然能知道分类学的结构、当前版本、关键修正历史。**本节的维护规则见`.devin/rules/tell-taxonomy-schema-maintenance.md`。**

#### 分类学结构（v3当前版本）

```
tell的固有属性（形式背景的属性维度——tell本身的特点，不随题目位置变化）：
  第一层：domain（6个：数论/代数/组合/几何/分析/跨域）
  第二层：段结构模式（5大类：构造-分析-排除/探索-诊断-修复/跨域桥接/归约策略/累积-收敛）
  第三层：具体概念（domain×段结构模式的交叉；子模式在此层体现，如"无尽追逐"是"探索-诊断-修复"的子模式）

观察trace的Level选择（不是tell的属性，是检索时的参数——取决于trace结构，不取决于tell本身）：
  局部Level / 非局部Level / 全局Level
```

#### 5大类段结构模式（必须记住的名字和一句话定义）

| 模式 | 一句话定义 |
|---|---|
| 构造-分析-排除 | 构造对象→分析性质→排除不可能 |
| 探索-诊断-修复 | 探索方向→发现gap→诊断→修复（"无尽追逐"是此模式的子模式——诊断环节断裂） |
| 跨域桥接 | 把问题从一个领域翻译到另一个领域 |
| 归约策略 | 把大问题归约到小问题 |
| 累积-收敛 | 逐步累积信息→最终收敛到结论 |

#### 版本历史摘要（全历史在08号文件顶部）

| 版本 | 触发 | 核心修正 | 关键认知 |
|---|---|---|---|
| v1 | 初始建立 | 四层结构：domain→trace类型→段结构模式→具体概念 | 初始构想 |
| v2 | FLT例子 | "局部/非局部/全局"从属性维度移到观察Level参数 | **FLT例子**：同一个tell在"题目就是证明FLT"中表现为全局，在"中间需要FLT"中表现为局部——所以"局部/非局部/全局"不是tell的固有属性，是观察方式 |
| v3 | FCA理论审查 | "无尽追逐"从第二层降级到第三层（"探索-诊断-修复"的子模式） | **FCA属性测试**：tell"应该转向X"在AI追逐时和不追逐但同样需要转向时都出现——tell相同，但"无尽追逐"只在前者中出现——所以"无尽追逐"不是tell的固有属性 |

#### 两个关键修正认知（必须记住的洞察）

**洞察1（v2）**：tell的固有属性和观察trace的方式是正交的两个轴。"局部/非局部/全局"是观察方式（你看trace的粒度），不是tell的属性（tell本身的特点）。同一个tell在不同题目位置（整体目标vs中间步骤）有不同的Level显现，但tell本身不变。

**洞察2（v3）**：FCA要求形式背景的属性必须是对象的固有特征。测试方法：如果同一个对象在不同观察方式下属性值变化，那这个属性不是固有属性。"无尽追逐"是trace特征（AI在trace中的行为模式），不是tell属性——它随AI是否追逐而变化，不随tell本身变化。

#### 高Level概念作为分类学坐标轴（336号·必须记住的洞察）

**洞察3（336号）**：高Level概念（如同构之桥）不是分类学中的"点"（被分类的对象），而是分类学的"坐标轴"（分类的维度本身）。"跨域桥接"是段结构模式这个分类维度上的一个值——它是坐标轴上的一个刻度，不是被分类到一个类别中的对象。降低Level后的具体形式（如"构造Frey曲线"）才是分类学中的"点"。

**结构知识与内容知识分离**：
- **结构知识**（在分类学Schema/解释库中）：domain定义、段结构模式定义、子模式定义（如"同构之桥"是"跨域桥接"的子模式）、高Level概念的三种解释文本——这些是分类学的"坐标轴"
- **内容知识**（在tell库/hint库中）：具体tell条目、具体hint条目，每个条目有{domain, 段结构模式}属性——这些是分类学中的"点"

**高Level概念的存储和使用方式（338号）**：高Level部分和低Level部分一样放入AGENTS.md目录，有专门的devin cli从中启动进行识别。区别在描述方式——高Level部分要"说清楚"+带例子，不能只是一句抽象的话。详见技术说明书`04-概念树/07-高Level概念解释库.md`。

**高Level概念的两种类型（340号）**：
- **第一种（可展开的）**——如构造-分析-排除、累积-收敛、探索-诊断-修复、归约策略：概念本身定义了展开维度（过程的阶段），可以预先降低Level为具体形式列表。组合爆炸可控，覆盖缺口有限。
- **第二种（无法指定展开方向的）**——如同构之桥：概念本身不定义展开维度，目标领域开放，无法预先降低Level。主要靠充分解释+启发式触发+案例积累。组合爆炸风险高，覆盖缺口永远存在。
- 两种类型的Telling AI识别逻辑不同：第一种遍历展开后的具体形式列表，第二种理解概念+格化脉络+判断适用条件（无列表可遍历）。

#### tell和hint的多对多关系（333号·必须记住的洞察）

**洞察4（333号）**：tell和hint是多对多关系——一个tell可以对应多个hint（同一个trace识别结果可以触发多个不同的方向提示），一个hint也可能被多个tell指到（同一个方向提示可能被不同的识别结果触发）。数据库schema中tell_hint_match集合需要支持多对多。

#### 关键文件

| 文件 | 内容 |
|---|---|
| `FCA学习笔记/08-先验Tell分类学.md` | 完整分类学（v3）+版本历史+形式背景+概念格 |
| `FCA学习笔记/09-用FCA重做已完成题目Tell分类-IMO2024P5对比.md` | IMO 2024 P5的FCA再分析对比 |
| `FCA学习笔记/fca-reanalysis-full-plan.md` | **全量处理方案（455题）——分批策略、进度跟踪、恢复机制** |
| `FCA学习笔记/fca-reanalysis-checklist.md` | **执行check list模板——主agent建立TODO List用（铁律0）** |
| `FCA学习笔记/fca-reanalysis-subagent-prompt-template.md` | **subagent prompt模板——主agent构造subagent的prompt用（铁律-1分工架构）** |
| `FCA学习笔记/fca-reanalysis-output-verification-checklist.md` | **产出验证check list——主agent验证subagent产出用（铁律0.5）** |
| `第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/v6.md` | **V6提示词——格化+全Level Trace识别的完整操作指南（679行）。subagent在步骤0加载** |
| `.devin/rules/tell-taxonomy-iteration-audit.md` | 铁律-1（主agent/subagent分工）+ 铁律0（TODO List）+ 铁律0.5（产出验证）+ 再分析10步SOP + 版本化审计7条铁律 |
| `.devin/rules/tell-taxonomy-schema-maintenance.md` | 本Schema节的维护规则 |

---

### Tell分类学研究（当前任务线，313号启动）

> **启动文档**：`第六代系统研发过程文档/313-v0-2026-08-10-Tell分类学研究-建立第六代Tell的分类体系.md`
> **目标**：建立第六代Tell的分类体系，使得每个tell在分类体系中有明确位置、Telling AI可按分类体系分区、trace→tell匹配有匹配key、分类体系可扩展且有FCA数学基础。
> **⚠️ 迭代审计铁律**：Tell分类学不是一次性建成的——它在不断看新题的过程中被修正。修正的全历史审计在`FCA学习笔记/08-先验Tell分类学.md`顶部明面记录。每次修正必须做覆盖性检查。详见`.devin/rules/tell-taxonomy-iteration-audit.md`。
> **⚠️ Schema维护铁律**：上面的"Tell分类学Schema"节是跨压缩边界保真的核心——分类学修正后必须同步更新该节。详见`.devin/rules/tell-taxonomy-schema-maintenance.md`。

**已完成**：
- [x] **先验Tell分类学建立**（`FCA学习笔记/08-先验Tell分类学.md`）——v3版本，三层属性维度（domain→段结构模式→具体概念）+观察Level参数（局部/非局部/全局）。版本历史：v1初始四层→v2 FLT例子修正（"局部/非局部/全局"从属性移到观察参数）→v3 FCA理论审查修正（"无尽追逐"降级为"探索-诊断-修复"子模式）
- [x] **IMO 2024 P5对比分析**（`FCA学习笔记/09-用FCA重做已完成题目Tell分类-IMO2024P5对比.md`）——用FCA先验分类学重做一道已完成题目的Tell分类，发现原始profile遗漏6个非局部/全局tell显现

**待完成**：
- [ ] **第零步：确认现有tell库的局限性**——确认现有4164个tell全是局部tell，没有非局部tell（314号问题）
- [ ] **第一步：现状调查**——查数据库了解当前4164个tell的分类现状（有没有domain标签/大概念拓扑标签/972个"全局tell"是什么含义/来源分布是否暗示domain分类）
- [ ] **全量FCA再分析**——对67837道题做FCA再分析，按6层难度从高到低进行（Tier 1的452题可立即启动，Tier 2-5待profile提取完成）。方案见`FCA学习笔记/fca-reanalysis-full-plan.md`，与`任务追踪/06-题目侧写Profile提取完整方案.md`对齐
- [ ] **分类学迭代修正**——在抽样验证中发现的分类学问题，按版本化审计铁律修正08号文件
- [ ] **第二步：分类维度设计**——确定层次结构还是正交维度，确定每层/每维度的具体取值，确定和FCA形式上下文的对接方式
- [ ] **第三步：非局部trace段结构模式收集**——从304号§8.15的三个例子出发，用费马大定理证明过程和真实thinking收集更多段结构模式，确定有多少种（依赖314号问题的解决）
- [ ] **第四步：FCA形式上下文构建**——把分类维度转化为FCA形式上下文（对象=tell，属性=分类维度取值），用闭包算子计算概念格，验证完备性
- [ ] **第五步：Telling AI分区验证**——用分类体系验证311号的分区方案（按domain分/按domain×trace_type分/按更细层次分），验证每区tell数和并发数
- [ ] **第六步：POC验证**——验证trace→tell匹配准确率/Telling AI分区效率/非局部trace段结构模式分类覆盖率

### POC验证已完成项

- [x] **POC-VMS-0到VMS-6v2全部完成**：核心循环、可扩展性、Pattern闭环、跨域迁移、动态引导胜率验证
- [x] **POC-VMS-7g泛化POC完成**：验证了"翻译语言"hint在群论和数论两道题上都被AI采纳
- [x] **POC-VMS-7g-v3奥赛难题版完成**：高Level静态hint没有胜出（bare 0% vs knowledge 25% vs highlevel 12%）
- [x] **POC-VMS-8完成**：引导树闭环验证成功（bare 0% → tree 67%）
- [x] **POC-VMS-9完成**：tell端去特化+形式化过滤验证（全部PASS）
- [x] **POC-VMS-10完成**：拓扑相同且距离极近的tell的小概念标记分辨验证（全部PASS）

### 其他待办

- [ ] 补充1709+T05正确hint实验——验证1709题在正确hint下能成功（POC-VMS-10局限）
- [ ] 扩大同一拓扑下的tell数量——从2个tell扩展到5-10个，验证小概念标记分辨的精度
- [ ] 自动化小概念提取——用NLP方法从tell的标准化语言描述中自动提取小概念信号词
- [ ] 验证概念树管理——当小概念数量膨胀时，验证概念文件的层次结构和按需加载机制

---

## Memory Section

> 本节记录跨 Session 需要保持的认知。

### 虚拟数学系统方法论（POC-VMS）

构造HoTT同构虚拟数学系统，用于POC验证检索系统技术方案。核心原理：虚拟系统和真实数学结构相同（HoTT同构），AI在虚拟系统中做真实推理。像虚拟世界测试自动驾驶——物理引擎虚拟，AI决策过程真实。

**5个技术缺口**（四代合并后仍存在）：状态提取/模式匹配/recall检索/Pattern生成闭环/覆盖度。第五代的三层Pipe架构+概念树解决了前两个缺口。

详见：`原语化AI数学工程系统设计/07-验证/03-虚拟数学系统POC方案.md`

### 第五代系统的核心设计

- **tell+hint二元组**：读tell（从thinking读出分叉信号），给hint（给新AI翻译方向）。详见000号。
- **三层Pipe架构**：Pipe 0拓扑化→Pipe 1大概念过滤→Pipe 2小概念标记分辨。详见287号。
- **概念树**：大概念→小概念→概念树的层次化管理。无论tell数量如何增长、概念树如何膨胀，有限上下文的辅助AI都能系统化应对。详见287号用户第六次原文。
- **tell和hint是多对多关系**：一个tell可以对应多个hint，一个hint可以被多个tell触发。
- **tell可以穷举**：穷举是降低tell识别难度的手段。
- **Pipe 1是硬约束不是优化选项**：不能跳过形式化过滤直接让辅助AI暴力遍历全部tell。

### 第一性原理重构基线（123号v1）

123号以`系统探讨.md`全文为母本，把122号v2的工程直觉严格化为可证伪、可审计的对象。本节是后续schema、POC和运行时必须服从的最高基线。详见123号。

---

## Handover Section

> **第五代系统交接状态和数据丢失事件记录已移到**：`dev-docs/第五代系统交接与历史记录.md`
>
> **何时需要读**：需要了解第五代系统交接状态时；需要排查2026-08-05数据丢失事件时。

---

## 术语备忘

- **xishujuzhen**：稀疏矩阵的拼音。星学项目中建立的依赖图导航系统的代号。数学项目中沿用此名，指代同一套方法论下的数学版导航系统。
- **综述博士 / 论文博士**：用户对两种大师的区分。综述博士 = 知识体系全掌握、全能灵活运用；论文博士 = 负责创新。本项目工程化综述博士。
- **tell / hint**：引导树闭环的二元组。tell取自poker术语——观察对手揭示出的信息。hint是给新AI的翻译方向。
- **Pipe 0/1/2**：tell识别的三层架构。Pipe 0拓扑化，Pipe 1大概念过滤，Pipe 2小概念标记分辨。
- **概念树**：大概念→小概念→概念树的层次化管理，应对tell数量增长和概念膨胀。
- **AGENTS-星学版.md**：本目录中保留的星学项目完整 AGENTS.md，是方法论参考资产，不是工作对象。

---

## 当前工作线：题海梳理与数据基座建设

> **本节是自包含的任务文档。任何AI进入本repo做题海梳理工作时，读完本节即可接手——不依赖Session上下文中的其他内容。**
>
> **本节被AGENTS.md always-on守护。跨压缩边界后，AI加载AGENTS.md时自动看到本节。**

### 任务是什么

分层次地、系统化地梳理所有已下载到本地的有答案的数学题，从每道题的**题目+解答**对中提炼喂给第五代系统数据基座的东西，放入ArangoDB。

### 角色与任务说明——题海梳理工作线

> **本节明确题海梳理工作线中Master Agent和subagent各自做什么。subagent也会看到AGENTS.md，必须知道自己该做什么、不该做什么。**

**Master Agent 的职责**：
1. **找下一个给subagent分析的题目**——从ArangoDB `problem_extraction_progress`中查`extraction_status="pending"`的题，优先选最难的，分配给subagent
2. **为每道题准备工作目录**——用`scripts/prepare_subagent_dir.py`在`subagents-dirs/{problem_id}/`下创建工作目录，生成填充好的checklist.md。派发subagent时告诉它工作目录路径
3. **让整个分析过程以批次进行**——每批3个subagent并发，全部完成后Master Agent逐个审计，审计全部完成后再发起下一批。不是流水线补位，是批次制：3个启动→3个完成→3个审计→下一批3个启动。**⚠️ 每批次必须用`todo_write`工具精确构建7步todo list，步骤名称和顺序固定不变，详见`.devin/rules/batch-todo-list.md`铁律。**
4. **管理批次**——监控当前批次5个subagent的状态，全部完成后开始逐个审计
5. **Schema版本管理**——多个subagent同时发现新维度时合并到Schema文件
6. **处理异常**——subagent失败时记录原因，将题目状态改回`pending`
7. **创建ArangoDB集合、写Schema种子文件、建任务追踪子线文档**——这些基础设施工作不委托给subagent
8. **审查subagent产出质量 + 改进流程**——**这是义务，不是可选项**。Master Agent不只是派发器和入库器，更是审查者和流程改进者。详见下方§Master Agent审查SOP

**subagent 的职责**：
1. **每次只被分配一个题目进行分析**——subagent收到Master Agent分配的一道题和一个工作目录，完整执行"每道题的完整处理流程"（11步，含QA序列分析）
2. **一上来全文加载checklist.md**——Master Agent为每道题在`subagents-dirs/{problem_id}/`下创建工作目录，放入填充好的`checklist.md`。subagent的第一步是用read工具全文读取这个checklist.md，然后按步骤执行，每完成一步把`[ ]`改为`[x]`并填写产出
3. **不要自行分析更多题目**——subagent处理完分配的这道题后，输出profile JSON，入库，更新进度，然后结束。不要自行从数据库中领取下一道题，不要自行决定分析什么题
4. **不要做Master Agent的工作**——不管理并发槽位，不更新Schema版本（如发现新维度，在profile中标注，由Master Agent合并到Schema），不建集合，不写任务追踪文档
5. **任务完成后汇报**——向Master Agent报告这道题的处理结果（profile_doc_id、是否发现新维度、是否遇到异常、拓扑分类是否有进化建议）
6. **拓扑进化是subagent的义务**——分析每道题时，subagent必须思考拓扑分类是否需要进化（见SOP第6步）。这不是Master Agent的工作——Master Agent不分析题目，无法发现拓扑分类的问题。只有subagent在分析具体题目的过程中才能发现"现有拓扑分类不够用/粒度不一致/需要新维度"。发现问题时在汇报中明确提出，由Master Agent决定是否合并到Schema

**subagent工作目录机制**：
- **总目录**：`subagents-dirs/`
- **每道题的子目录**：`subagents-dirs/{problem_id}/`——目录名与题目在数据库中的problem_id一致，方便追溯
- **checklist.md**：Master Agent用`scripts/prepare_subagent_dir.py`从`subagents-dirs/checklist-template.md`模板生成，填充了problem_id、文件路径、来源、ArangoDB progress记录的_key
- **checklist.md的内容**：对应SOP的11个步骤，每步有完整的步骤说明和严格的要求说明。checklist对任务的说明和规范化程度**只能比AGENTS.md中的subagent执行此次任务相关内容多，不能比其中的内容少**
- **subagent执行方式**：一上来全文加载checklist.md，每完成一步更新checklist中的checkbox和产出说明，最终profile.json也写入这个工作目录
- **Master Agent追溯方式**：通过`subagents-dirs/{problem_id}/checklist.md`可以看到subagent每步的完成情况和产出，通过`subagents-dirs/{problem_id}/profile.json`可以看到最终profile

**关键边界**：
- Master Agent负责"找题、派发、持续运行、审查质量、改进流程"，subagent负责"分析单道题"
- subagent不自行领取下一道题——这是Master Agent的职责
- subagent不自行更新Schema——发现新维度或拓扑分类问题在profile中标注并在汇报中提出，Master Agent统一合并
- **拓扑进化的发现权在subagent，决策权在Master Agent**——subagent在分析中发现拓扑分类的问题，Master Agent收到汇报后决定是否修改Schema
- Master Agent不停下来汇报工作——海量题目没处理完之前持续派发
- **但Master Agent必须在检查点执行审查**——审查不是"停下来汇报"，审查是"持续运行的内置环节"

### Master Agent审查SOP

> **审计是Master Agent的核心职责，不是附属工作。**
>
> Master Agent的角色不是"调度器兼审计员"——而是"审计员兼调度器"。调度是手段，审计是目的。整个题海梳理工作线的产出是否有意义，最终取决于审计质量。一个未经审计就入库的profile，可能污染数据基座；一个经审计但不合格的profile被放行，比没有更糟——因为它给了虚假的信心。**审计是整个过程的成果有意义的最终保证。**

> **⚠️ 审计的深度要求——不惜代价地审计，不是走形式**
>
> 审计不是检查格式对不对（situation_type值对不对、hint_level格式对不对、per-pair拓扑存不存在）——这些是最低线的格式检查，是审计的起点不是终点。
>
> 审计是**Master Agent重新理解这道题的数学内容，然后判断subagent的理解对不对**：
> - Master Agent必须**亲自读题目和解答**，理解这道题在数学上是什么、解答的核心思路是什么、关键转折点在哪里
> - Master Agent必须**自己思考**：如果我是AI，我会怎么解这道题？我会在哪里走错路？正确的方向是什么？
> - 然后Master Agent**对比subagent的分析**：
>   - QA序列：这个序列真的能引导AI从题目走到解答吗？有没有遗漏关键步骤？有没有不必要的轮次？每轮的Q真的对应了AI在这个位置需要的提示吗？还是机械地走形式？
>   - tell/hint对：tell真的描述了AI在这个位置的分叉信号吗？还是泛泛而谈？hint真的能帮AI找到正确方向吗？还是"继续努力"之类的废话？全局蕴含型(tell,hint)的why_not_visible_locally真的解释了为什么在局部不可见吗？还是编了一个理由？
>   - 拓扑标注：problem_type真的准确反映了题目的结构类型吗？ai_method_type真的预测了bare AI会用的方法吗？gap_type真的抓住了方法-问题不匹配的核心吗？还是随便填了一个值交差？
>   - key_insight：这个"啊哈时刻"真的是解答中最关键的转折点吗？还是只是随便找了一句话填上去？
>   - bare_ai_error_prediction：这个预测真的具体吗？还是只说"会失败"？
>
> **虽然不是完全重做**（不需要Master Agent从头到尾重新构造完整profile），但Master Agent必须对每道题做**实质性的数学理解**，才能判断subagent的分析质量。审计的成本是值得的——一个不合格的profile入库后会污染数据基座，后续的Pipe检索会被错误的(tell,hint)对误导，代价远大于审计成本。
>
> **审计的底线**：如果你（Master Agent）读完subagent的分析后，无法说出"这个分析我理解了，我认为它是对的"或"这个分析在X处有问题"——说明你的审计深度不够，你需要更深入地理解这道题。

> **⚠️ QA序列拆解不对时的处理——立即干预，不留到Pass 2**
>
> 如果审计发现QA序列拆解有严重问题（遗漏关键步骤、轮次逻辑不通、tell/hint泛泛而谈、拓扑标注严重错误等），**不能只标记"Pass 2重做"就继续派发下一道题**。必须立即采取以下行动之一：
>
> 1. **Master Agent自己重做QA序列**——如果问题集中在QA序列的某几轮，Master Agent可以直接重写这几轮的Q/A/situation_type/level/tell/hint，更新profile入库
> 2. **发给另一个subagent重做，并给必要提示**——如果问题较广泛（整个QA序列框架都不对），派发一个新的subagent重新分析这道题，在prompt中明确告诉它：
>    - 前一个分析哪里错了（"前一个subagent的QA序列遗漏了从X到Y的关键步骤"）
>    - 应该怎么改（"QA序列应该在第N轮包含一个关于Z的提示"）
>    - 前一个分析的profile可以作为参考但不要照抄
>
> **不允许的处理方式**：标记"Pass 2重做"然后继续派发——这等于把问题推到未来，而Pass 2时可能已经积累了大量同类问题，修正成本更高。**问题发现时修正，不是问题积累后修正。**

> **⚠️ 超大规模前瞻——所有设计决策必须考虑10万级数据基座下的可用性**
>
> 现在分析13道题时做的每一个设计决策——拓扑分类的粒度、Schema的字段、(tell,hint)对的格式、situation_type的6个值——在数据基座从13个profile增长到10万个profile时，是否仍然有效？整个AI数学系统在10万级数据基座下能否工作？
>
> Master Agent在审计和做设计变更时，必须同时思考以下前瞻问题：
>
> **拓扑分类的规模化**：
> - 当前13道题已有约10种problem_type值。到10万道题时，会有多少种？如果problem_type膨胀到1000种，Pipe 1的过滤还有效吗？（Pipe 1的设计目标是"从10万级缩小到百级"——如果problem_type太细，每个值只匹配1-2个tell，Pipe 1退化为精确匹配，失去了"缩小范围"的功能；如果太粗，所有tell都匹配，Pipe 1失去过滤能力）
> - 拓扑分类体系需要什么样的治理机制？是否需要层次化分类（粗粒度→中粒度→细粒度），让Pipe 1在不同粒度上做过滤？
>
> **(tell,hint)对的规模化**：
> - 10万个profile，每个5-8个局部pair + 2-4个全局pair = 50-100万个(tell,hint)对。Pipe 1+Pipe 2的检索效率在这个规模下是否可接受？
> - 会不会出现大量拓扑相同、小概念也相同的(tell,hint)对？如果出现，Pipe 2如何区分？是否需要更细的分辨维度？
> - (tell,hint)对的质量在规模化后如何保证？是否需要抽样审计而非全量审计？
>
> **Schema的规模化**：
> - 当前Schema的字段在10万级数据下查询效率如何？是否需要新增索引？是否需要分片？
> - Schema的迭代历史在10万级数据下如何管理？每次Schema变更需要回补多少已有profile？回补成本是否可控？
>
> **设计变更的规模化影响**：
> - 每次你修改拓扑分类体系（归一化、新增维度、改变粒度），影响的是所有已有profile——现在13个可以脚本批量修，到10万个时还能吗？
> - 每次你修改checklist-template.md，影响的是后续所有subagent——变更是否向后兼容？已有profile是否需要重做？
> - **设计变更原则：宁可现在多花时间设计一个能scale的方案，也不要为了快而做一个到10万级时要推倒重来的方案。**
>
> **AI数学系统有效性**：
> - 数据基座的最终用途是支撑AI数学系统的三层Pipe检索。在审计每个profile时，要问自己：**这个(tell,hint)对在AI数学系统运行时真的会被检索到吗？检索到后真的能帮AI找到正确方向吗？** 如果答案是"不确定"或"不会"，这个(tell,hint)对的价值存疑。
> - 数据基座不是"存了就有用"——它必须能被检索、检索结果必须有效。审计时要从"检索有效性"的角度审视每个(tell,hint)对。

#### 检查点1：每批5道subagent全部完成后——逐个完整审计（必须执行）

**批次制工作节奏**：3个subagent并发启动→全部完成→Master Agent逐个审计（3个审计）→审计全部完成→发起下一批3个。不是流水线补位，是批次制。**⚠️ 每批次必须用`todo_write`工具精确构建7步todo list（领取题目+准备文件→并发启动→等待完成+格式检查→数学内容审查→写audit-checklist→更新review-log→git commit），步骤名称和顺序固定不变，详见`.devin/rules/batch-todo-list.md`。**

**审计方式**：使用`subagents-dirs/audit-checklist-template.md`模板。每次审计从一张干净的模板开始，填充`{{PROBLEM_ID}}`、`{{SUBAGENT_ID}}`、`{{AUDIT_TIME}}`、`{{FILE_PATH}}`等占位符，生成`subagents-dirs/{problem_id}/audit-checklist.md`。Master Agent全文加载这个audit-checklist.md，逐项检查，每完成一项把`[ ]`改为`[x]`并填写审计结论。

**⚠️ 所有项目必须全部check完，不允许跳过任何一项。** 审计checklist末尾有"审计员签字"确认区，必须确认所有Phase的所有项目都已check完才能提交审计结论。

**⚠️ 审计纪律铁律（不可违反）**：
1. **必须严格按照`audit-checklist-template.md`逐项检查**——Phase 0到Phase 6的每一项都要实际执行，不允许跳过、不允许合并、不允许用批量脚本替代逐项审查。
2. **Phase 2的16项（2a-2p）必须逐项做**——特别是2e（QA序列逐轮审查，对每一轮单独填写situation_type/question/level/遗漏的判断）和2f/2g（逐对审查tell/hint质量），不允许只读key_insight就判"合格"。
3. **粗审不算审计**——只检查格式+高层读key_insight是粗审，不是审计。审计必须包含数学内容审查（Phase 2）。
4. **审计产出必须落盘**——每个审计过的profile要有`subagents-dirs/{problem_id}/audit-checklist.md`，记录逐项检查结果。

审计checklist包含6个Phase：
- **Phase 0: 加载审计材料**——读profile、读Lean文件亲自理解题目和解答、读subagent的checklist.md和profile.json
- **Phase 1: 格式检查（最低线）**——situation_type值规范、hint_level格式、per-pair拓扑字段存在性、必填字段完整性、QA序列结构
- **Phase 2: 数学内容审查（核心审计，16项）**——题目理解准确性(2a)、解答理解准确性(2b)、solution_method_type vs problem_type区分(2c)、key_insight准确性(2d)、QA序列逐轮合理性(2e)、局部(tell,hint)对质量(2f)、全局(tell,hint)对质量(2g)、拓扑标注准确性(2h)、bare_ai_error_prediction具体性(2i)、thinking_patterns和knowledge_required(2j)、translation分析(2k)、structure_features和key_objects(2l)、expected_ai_method和correct_method(2m)、bare_ai_expected和实验适用性(2n)、answer和answer_type(2o)、analysis_metadata(2p)
- **Phase 3: 拓扑分类体系审查**——拓扑值粒度一致性、是否需要新增拓扑值、拓扑进化建议评估
- **Phase 4: 超大规模前瞻审查**——(tell,hint)对的检索有效性、Schema扩展性、AI数学系统有效性
- **Phase 5: 审计结论**——总体判断、大问题处理、流程改进、审计记录
- **Phase 6: 元审查——审查审查工具本身是否需要改进**——每次审计都必须执行。审计工具本身的不完备会导致系统性漏审。包含：
  - 6a. 本审计checklist自身的完备性（是否有缺失的检查项？表述不清楚的检查项？冗余的检查项？）
  - 6b. 本审计checklist自身的合理性（顺序/Phase划分/粒度/时间成本是否合理？）
  - 6c. 数据库表设计是否需要改进（缺字段？多余字段？值域不合理？索引不支持审计查询？）
  - 6d. subagent用的checklist-template.md是否需要改进（步骤说明不够清楚？约束需要强化？拓扑值列表需要更新？）
  - 6e. AGENTS.md中的SOP是否需要改进（流程环节不合理？步骤需要调整？检查点频率需要调整？拓扑分类体系需要更新？）
  - 6f. subagent的每一个工作项目是否需要反思其是否需要更新（逐个审视SOP的11个步骤，判断审计结果是否暴露了该步骤本身需要改进）
  - 6g. 改进落实（6a-6f中标记"需要改进"的项目是否已落实？未落实的记录为待办）

**审查结果处理**：
- **合格**：标记该题审计通过，继续审计批次中下一道题
- **小问题**（situation_type/hint_level格式错误等）：用脚本批量修正，在checklist-template.md中强化对应约束，继续审计下一道
- **大问题**（QA序列不合理、tell/hint泛泛而谈、拓扑标注严重错误等）：**立即干预**（见上方§QA序列拆解不对时的处理）——Master Agent自己重做有问题的部分，或发给另一个subagent重做并给必要提示。**不允许只标记"Pass 2重做"然后继续。**

**批次完成条件**：批次中10道题全部审计完成（合格或已修正）后，才能发起下一批。

**重做机制**：
- **重做上一批**：如果审计中发现上一批有系统性问题（如多个profile的QA序列都犯了同类错误、拓扑标注整体方向偏了等），可以重新运行上一批——将该批题目的progress状态改回`pending`，重新派发subagent，并在prompt中给出修正提示
- **从头重新运行**：如果审计中发现的问题严重到需要从头开始（如Schema设计根本不对、checklist有系统性缺陷导致所有已完成的profile都需要重做等），记录当前进度到`subagents-dirs/review-log.md`：
  - 记录"重做前最后完成的global_sequence"——每条`problem_extraction_progress`记录有`global_sequence`字段（按difficulty_tier ASC, problem_id ASC排序的全局顺序编号，1~67838），Tier 1范围是2~453
  - 记录重做原因
  - 记录哪些已完成profile需要重做、哪些可以保留
  - 然后将需要重做的题目的progress状态改回`pending`，从第一批重新开始

**进度记录**：每批完成后，在`subagents-dirs/review-log.md`中记录：
- 当前批次号
- 本批的global_sequence范围（如"第3批：seq 22~31"）
- 累计完成数 / Tier 1总数（如"13/452"）
- 审计结果摘要（几个合格、几个小问题、几个大问题）

#### 检查点2：每2批（约20道题）完成后——批量审查（必须执行）

每完成2批（约20道题，累计入库），Master Agent必须做一次更深的跨profile审查：

**2a. 跨profile一致性检查**：
- 所有profile的拓扑值是否粒度一致？（运行AQL查询所有unique的problem_type/ai_method_type/gap_type值，检查是否有太具体或太抽象的异常值）
- solution_method_type是否有重复模式？（如多道题都用"telescoping"，说明这是一个高频思维模式）
- thinking_patterns是否有高频值？

**2b. Schema/Checklist/流程改进评估**：
- 过去2批中，subagent是否在某些步骤反复出错？（如situation_type反复自创→checklist约束不够强）
- 过去2批中，是否发现了Schema中缺失的字段或类别？
- 过去2批中，拓扑分类体系是否需要进化？（subagent的进化建议是否指向同一个方向？）
- checklist-template.md是否需要更新？（某个步骤的说明是否不够清楚导致subagent反复出错？）
- AGENTS.md中的SOP是否需要更新？（某个流程环节是否不合理？）

**2c. 数据库设计评估**：
- 字段是否够用？是否有有价值的信息无处记录？
- 索引是否合理？查询是否高效？
- 是否需要新增集合或字段？

**2d. 亲自重新分析一道题**：
- 从过去2批中选一道，Master Agent亲自重新分析（不委托subagent）
- 对比Master Agent的分析和subagent的分析，找出差异
- 差异如果是subagent遗漏了什么→在checklist中强化对应步骤
- 差异如果是Master Agent也遗漏了什么→说明Schema/SOP有盲区，需要修正

**审查结果处理**：
- 发现问题→**立即修正**（更新AGENTS.md/checklist-template.md/Schema），让后续批次的subagent受益
- 修正后commit，记录变更原因
- 如果问题严重到需要重新分析已完成的题→记录待重做列表，下一批次时处理

#### 检查点3：每5批（约50道题）完成后——全局审查（必须执行）

**3a. 拓扑分类体系健康度**：
- 运行AQL统计所有unique拓扑值，更新AGENTS.md中的"拓扑分类体系"节
- 检查是否有需要归一化的值（太具体的归入更抽象的类）
- 检查是否需要新增维度

**3b. Pattern发现**：
- 跨题分析：哪些(tell, hint)对在多道题中重复出现？这些是高频Pattern，值得特别标注
- 跨题分析：哪些translation_type在多道题中重复？这些是高频翻译方向

**3c. 流程效率评估**：
- 平均每道题的分析耗时（从subagent启动到入库）是否合理？
- subagent的失败率？失败原因分布？
- 是否需要调整并发数、checklist长度、prompt结构？

#### 审查记录

每次审查（检查点1/2/3）的结果必须记录在`subagents-dirs/review-log.md`中：
```
## 审查记录
### [日期时间] 检查点1: {problem_id}
- QA序列合理性: ✅/❌（详情）
- 拓扑标注质量: ✅/❌（详情）
- (tell,hint)对质量: ✅/❌（详情）
- 处理: 合格/修正了X/标记重做

### [日期时间] 检查点2: 第N批5道题
- 跨profile一致性: ...
- Schema/Checklist改进: ...
- 亲自重做对比: ...
- 修正: 更新了X
```

### 为什么要做

第五代系统的核心是tell+hint二元组和三层Pipe架构。系统要工作，需要数据基座中有大量的(tell, hint)对。目前数据基座中的(tell, hint)对只有POC实验中手工积累的少量条目（24个翻译方向、2个tell）。有答案的题海是天然的(tell, hint)对收集源——每道题的解答本质上就是一个"问题处境→正确方向"的映射。遍历完所有有答案的题，数据基座就从实验级增长到生产级。

### 从每道题中提取什么（放入数据库的东西）

每道有答案的题，提取以下内容，存为ArangoDB `problem_profiles`集合中的一个文档：

**元数据层**（从数据源继承，自动提取）：
- `source_id` / `source_dataset` / `domain` / `subfield` / `answer_type` / `answer` / `question_length` / `has_solution`

**问题拓扑层**（tell的大概念——分析题目结构后标注）：
- `problem_type`：问题类型（discrete_combinatorial / structural_existence / extremal / ...）
- `structure_features`：结构特征（存在性/唯一性/极值/构造/判定/...）
- `key_objects`：核心对象（多项式/序列/群/矩阵/图/...）

**解答思维模式层**（hint的高Level分类——分析解答后标注）：
- `thinking_patterns`：思维模式列表（["translation", "contradiction", "invariant", ...]）
- `primary_pattern`：主要思维模式
- `knowledge_required`：需要的知识点列表
- `key_insight`：关键转折点的一句话描述（"啊哈时刻"——解答中从哪里到哪里是关键跳跃）

**翻译方向层**（hint的Low Level具体形式——分析解答中的翻译操作后标注）：
- `translation_from`：翻译的源语言（如"整数方程"）
- `translation_to`：翻译的目标语言（如"模算术" / "p-adic赋值" / "二次剩余" / ...）
- `translation_type`：翻译类型（如"连续→离散" / "穷举→结构" / ...）

**tell拓扑标注层**（这道题贡献给tell数据基座的条目）：
- `tell_topology`：{problem_type, ai_method_type, gap_type}——如果bare AI做这道题，它可能用什么方法（ai_method_type），这个方法和问题类型之间的不匹配是什么类型（gap_type）
- `tell_small_concepts`：小概念信号词列表（从题目和解答中提取的领域特定概念关键词，如["mersenne", "primality", "covering_system"]）
- `expected_ai_method`：bare AI预期会用的方法（可能走错的路）
- `correct_method`：解答中实际用的正确方法

**(tell, hint)对**（这道题贡献给数据基座的核心条目）：
- `tell_hint_pairs`：[{tell_topology, tell_small_concepts, hint_direction, hint_level}]——这道题识别出的tell和对应的hint

**实验适用性层**（用于POC实验选题）：
- `bare_ai_expected`："pass" / "fail" / "marginal"——bare AI能否解出
- `suitable_for_poc`：适合哪些POC实验
- `discriminates_levels`：能否区分高Level hint和低Level hint的效果

### QA序列分析——(tell, hint)对的提取方法

**QA序列是什么**：辅助智能体引导推理智能体解题的完整对话记录。每一轮包含一个Q（辅助智能体发送的提示=hint）和一个A（推理智能体的回复）。QA序列是预演模式的产物——在知道答案的情况下，回溯"什么样的提示序列能引导AI从题目走到解答"。

**为什么必须做QA序列分析**：

1. **数据基座存的是Pattern不是解答**——Pattern是"当AI处于状态S时，给提示Q"的可复用经验单元。数据基座里如果没有Pattern，检索系统就检索不到任何东西，Grove核心循环转不起来。
2. **解答不是Pattern**——"1631题用二次剩余+Euler准则求解"是解答，不是Pattern。它只告诉你"这道题的答案是什么方法"，不告诉你"当AI在枚举Mersenne序列值、没注意到mod 8结构时，该给什么提示"。
3. **QA序列是Pattern的唯一来源**——QA序列把静态解答分解为动态的引导过程，每一步都是一个"AI在什么状态下需要什么提示"的经验单元，也就是一个Pattern。
4. **没有QA序列分析，题海就只是题海，不是数据基座**——遍历6万道题的解答而不做QA序列分析，等于读了6万份答案但没有积累任何引导经验。QA序列分析是整个题海梳理工作的核心转化动作：把静态解答转化为可复用的Pattern，把题海转化为数据基座。
5. **QA序列是第二棵树的一条完整成功脉络（lineage）**——从根节点（题目）到叶子节点（正确解答）的完整路径。因为它是成功的（等到了正确解答），所以它有(tell, hint)提取价值。分析QA序列是在重建解题树上的节点和边。
6. **QA序列分析必须有两种视角**——局部视角（逐轮提取）和全局视角（在整条脉络中识别高Level的、高可泛化的(tell, hint)）。有些高价值、高Level、高可泛化的(tell, hint)不是在单个(Q,A)中可见的，而是需要在某个(Q,A)的位置，看到之前和之后的整个QA序列才能识别出来。全局视角产出的对更可泛化，因为它们描述的是路径结构而非具体操作。

**QA序列中的6种情况类型**（每种Q对应不同Level的hint）：

| 情况类型 | 什么时候出现 | hint Level | 能否用元认知替代 |
|---|---|---|---|
| 纯元认知观察 | 序列开始，让AI描述形状 | 1.0（最高） | 本身就是元认知 |
| 自由列举方向 | 序列早期，让AI发散 | 1.0 | 本身就是元认知 |
| 思维操作引导 | AI卡在某个操作步骤 | 0.7-0.8 | 可以——给操作方向不给知识 |
| 量级感知引导 | AI有方程但不知道下一步问什么 | 0.5 | 可以——引导AI关注正确的量 |
| 知识性提示（必须） | AI遇到纯知识瓶颈 | 0.2（最低） | **不能**——纯知识瓶颈 |
| 能量传递引导 | AI有中间结果但不知道怎么传递 | 0.6 | 可以——引导传递方向 |

**关键洞察**：QA序列中大部分Q是元认知提示（高Level hint），但有时必须提供知识性提示（低Level hint）。系统必须能区分"该给元认知提示"和"必须给知识"这两种情况。知识性提示的Q是低Level的（Level 0.2），因为它是具体知识点，不是思维操作。

**QA序列分析的具体步骤**：

1. **读题目和解答**——理解题目在问什么，解答的完整路径
2. **将解答分解为步骤**——解答中的每一步做了什么，用了什么知识/思维模式
3. **对每一步，重构QA对**：
   - Q：什么样的提示能引导AI走到这一步？（是元认知提示还是知识性提示？）
   - A：AI收到Q后会做什么？（预期回复）
   - 状态（tell）：Q之前AI处于什么状态？（已做了什么，卡在哪里，缺什么）
4. **标注每轮的情况类型**——这轮Q属于6种情况类型中的哪一种
5. **标注每轮的Level和非特定性**——Q有多抽象？有多依赖答案知识？
6. **从QA序列中提取(tell, hint)对**——每轮(Q之前的状态, Q)就是一个(tell, hint)对
7. **识别知识瓶颈**——哪些步骤是纯知识瓶颈（必须给知识性提示），哪些是思维瓶颈（元认知提示就够）

**以上1-7步是局部视角——逐轮提取(tell, hint)对。以下是全局视角——在整条脉络中识别高Level的、高可泛化的(tell, hint)。**

8. **全局视角分析**——在整条QA序列中识别高Level的(tell, hint)。看QA序列绝不仅仅是看某个(Q,A)二元组的局部——有些高价值、高Level、高可泛化的(tell, hint)需要在某个(Q,A)的位置，看到之前和之后的整个QA序列才能识别出来。全局视角有两类：
   - **路径特征型**（示例A/B展现的）：总结整条路径的结构特征
     - 翻译类型：整条路径从什么方法转向什么方法？
     - 知识瓶颈位置：整条序列中哪一轮是唯一的降Level点？
     - 能量传递链：中间结果如何传递到最终目标？
     - 思维模式转换点：序列从什么模式转向什么模式？
   - **蕴含型**（示例C展现的）：在某个(Q,A)位置看到前后，读出AI此刻不知道但前后蕴含的(tell, hint)——这是AI的认知盲区，不是路径特征总结
     - 在观察点时tell还没出现（AI还没走到后面），在tell出现时已过了观察点（AI已经走过了盲区），只有在观察点同时看到前后才能读出
     - 例子：AI有了两个方法但不知道它们是统一的（见示例C的Q5）；AI有了具体案例但不知道案例蕴含一般框架（见示例C的Q8）
     - 蕴含型(tell, hint)比路径特征型更可泛化——因为认知盲区本身（"有方法没看到统一"、"有案例没看到框架"）可以泛化到任何领域

### 完整示例A：1631题（Mersenne序列最大k）的提取全过程

> 这道题在POC-VMS-8/9/10中验证过，tell和hint都已被实验确认有效。用它作为标准demo。

**题目**：定义Mersenne序列 x₀=1, xₙ₊₁=2^xₙ - 1。求使xₙ为素数的最大k。（简化表述，实际题目更具体）

**解答路径**：x₃=4a+3≡7(mod 8) → 2是模x₃的二次剩余 → Euler准则：2^((x₃-1)/2)≡1(mod x₃) → 但x₃ | 2^x₂ - 1意味着2^x₂≡1(mod x₃) → 矛盾（因为x₂和(x₃-1)/2的奇偶性不匹配）→ k≤2

**第一步：QA序列重构**

| 轮 | Q（hint） | A（预期回复） | 情况类型 | Level | tell（Q之前的状态） |
|---|---|---|---|---|---|
| Q1 | "描述这道题的结构形状：结论是什么类型？序列有什么特殊结构？" | 求最大k使xₙ为素数。序列指数增长，xₙ₊₁=2^xₙ-1。需要证明k有上界。 | 纯元认知观察 | 1.0 | 空白——AI还没开始 |
| Q2 | "列出你能想到的所有可能方向" | 枚举前几项看模式、分析模运算性质、尝试归纳、分析素性条件... | 自由列举方向 | 1.0 | AI描述了题目结构 |
| Q3 | "试着计算前几项，看看有什么模式" | x₀=1, x₁=1, x₂=3, x₃=7, x₄=63=7×9... x₃=7是素数，x₄不是 | 小尝试 | 0.9 | AI列出了方向 |
| Q4 | "x₃=7，x₄=63。注意xₙ₊₁=2^xₙ-1。x₃≡? (mod 8)？这个模8的值和2的幂有什么关系？" | x₃=7≡7(mod 8)。2^x₃≡2^7≡0(mod 8)... 不太对。等等，2^xₙ-1，所以x₄=2^7-1=127？不对，让我重新算... | 思维操作引导 | 0.7 | AI算出了前几项但没注意到mod 8结构 |
| Q5 | "关注x₃≡7(mod 8)。在模x₃的世界里，2是什么角色？想想二次剩余" | 2是模7的二次剩余？检查：1²=1, 2²=4, 3²=2(mod 7)。是的！2≡3²(mod 7)。所以2是模7的二次剩余。 | 思维操作引导 | 0.6 | AI注意到了mod 8但不知道往哪走 |
| Q6 | "用Euler准则把'2是模x₃的二次剩余'形式化。然后想想x₃ | 2^x₂-1意味着什么" | Euler准则：2^((x₃-1)/2)≡1(mod x₃)。而x₃ | 2^x₂-1意味着2^x₂≡1(mod x₃)。所以需要(x₃-1)/2 | x₂... 但x₂=3, (x₃-1)/2=3，确实整除！ | 思维操作引导 | 0.5 | AI发现了二次剩余但没形式化 |
| Q7 | "x₂=3, (x₃-1)/2=3。所以2^3≡1(mod x₃)。但Euler准则说2^((x₃-1)/2)≡1。这意味着什么？如果x₄也是素数呢？" | 如果x₄是素数，需要2^((x₄-1)/2)≡1(mod x₄)。但x₄=2^x₃-1，所以(x₄-1)/2=(2^x₃-2)/2=2^x₃/2-1=2^(x₃-1)-1。需要2^(2^(x₃-1)-1)≡1(mod x₄)... 这越来越复杂 | 量级感知引导 | 0.5 | AI形式化了但看不出矛盾 |
| Q8 | "回到x₃。你证明了2^x₂≡1(mod x₃)且2^((x₃-1)/2)≡1(mod x₃)。x₂=3, (x₃-1)/2=3。如果x₃>7呢？x₃≡7(mod 8)对一般情况成立吗？(x₃-1)/2的奇偶性呢？" | x₃=4a+3≡7(mod 8)对一般情况成立。(x₃-1)/2=(4a+2)/2=2a+1是奇数。而x₂=2^x₁-1... 如果x₁>1，x₂=2^x₁-1是奇数。所以2^x₂≡1(mod x₃)需要ord(2)|x₂，而Euler准则说ord(2)|(x₃-1)/2。x₂和(x₃-1)/2都是奇数... | 知识性提示+量级感知 | 0.3 | AI接近矛盾但需要数论知识 |
| Q9 | "关键事实：如果p≡±3(mod 8)，则2是模p的二次非剩余。如果p≡±1(mod 8)，则2是模p的二次剩余。x₃≡7≡-1(mod 8)，所以2是模x₃的二次剩余。但x₃ | 2^x₂-1意味着ord_x₃(2)|x₂。Euler准则说ord_x₃(2)|(x₃-1)/2。你能推出矛盾吗？" | x₃≡7(mod 8)→2是二次剩余→Euler准则：2^((x₃-1)/2)≡1。但x₃|2^x₂-1→2^x₂≡1→ord(2)|x₂。所以ord(2)|gcd(x₂, (x₃-1)/2)。x₃=4a+3, (x₃-1)/2=2a+1（奇）。x₂=2^x₁-1（奇）。如果a>1，gcd可能>1... 需要更仔细 | 知识性提示（必须） | 0.2 | AI需要二次剩余判定的具体知识 |
| Q10 | "整理一下：x₃≡7(mod 8)→2是二次剩余→(x₃-1)/2整除ord... 不对，Euler准则给出的是2^((x₃-1)/2)≡1，意味着ord(2)|(x₃-1)/2。而2^x₂≡1意味着ord(2)|x₂。所以ord(2)|gcd(x₂,(x₃-1)/2)。但x₂=2^x₁-1, (x₃-1)/2=(2^x₂-2)/2=2^(x₂-1)-1。gcd(2^x₁-1, 2^(x₂-1)-1)=2^gcd(x₁,x₂-1)-1。能推出矛盾吗？" | gcd(2^x₁-1, 2^(x₂-1)-1)=2^gcd(x₁,x₂-1)-1。x₁=1→gcd(1,x₂-1)=1→gcd=1→ord(2)=1→2≡1(mod x₃)→x₃|1→x₃=1矛盾！所以k≤2。 | 能量传递引导 | 0.6 | AI有了所有部件但需要组装矛盾 |

**第二步：从QA序列中提取profile**

```json
{
  "source_id": "1631",
  "source_dataset": "olympiadbench",
  "domain": "number_theory",
  "subfield": "Number Theory",
  "answer_type": "Numerical",
  "answer": "k=2",

  "problem_type": "structural_existence",
  "structure_features": "存在性上界——证明k有最大值",
  "key_objects": ["Mersenne序列", "素数", "模运算"],

  "thinking_patterns": ["translation", "contradiction", "case_analysis"],
  "primary_pattern": "translation",
  "knowledge_required": ["quadratic_residue", "euler_criterion", "order_of_element", "gcd_identity"],
  "key_insight": "x₃≡7(mod 8)时2是模x₃的二次剩余，用Euler准则和序列的整除关系推出ord(2)=1的矛盾",

  "translation_from": "Mersenne序列的素性判定",
  "translation_to": "二次剩余/Euler准则",
  "translation_type": "穷举→结构",

  "tell_topology": {
    "problem_type": "structural_existence",
    "ai_method_type": "enumeration_brute_force",
    "gap_type": "method_problem_mismatch"
  },
  "tell_small_concepts": ["mersenne", "primality", "covering_system", "exponential_growth"],
  "expected_ai_method": "枚举前几项+covering system尝试覆盖所有情况",
  "correct_method": "二次剩余+Euler准则推出矛盾",

  "tell_hint_pairs": [
    {
      "tell_topology": {"problem_type": "structural_existence", "ai_method_type": "enumeration_brute_force", "gap_type": "method_problem_mismatch"},
      "tell_small_concepts": ["mersenne", "primality", "covering_system"],
      "hint_direction": "T03 二次剩余——x₃≡7(mod 8)→2是二次剩余→Euler准则",
      "hint_level": 0.6
    },
    {
      "tell_topology": {"problem_type": "structural_existence", "ai_method_type": "enumeration_brute_force", "gap_type": "knowledge_gap"},
      "tell_small_concepts": ["quadratic_residue", "euler_criterion"],
      "hint_direction": "知识注入：p≡±3(mod 8)时2是二次非剩余，p≡±1(mod 8)时2是二次剩余",
      "hint_level": 0.2
    }
  ],

  "bare_ai_expected": "fail",
  "suitable_for_poc": ["VMS-8-translation", "VMS-9-tell-despecialization"],
  "discriminates_levels": true,

  "qa_sequence": {
    "rounds": 10,
    "metacognitive_rounds": 8,
    "knowledge_rounds": 1,
    "level_sum": 6.7,
    "knowledge_bottleneck": "Q9——二次剩余判定定理（p≡±1(mod 8)↔2是二次剩余）是纯知识瓶颈",
    "thinking_bottleneck": "Q4-Q5——从枚举转向mod 8结构分析是思维瓶颈，需要'注意x₃≡7(mod 8)'这个方向引导"
  }
}
```

**第三步：这个profile贡献给数据基座什么**

1. **hint字典新增/确认**：T03二次剩余方向已存在，但这道题确认了它在Mersenne序列问题中的具体形式——"x₃≡7(mod 8)→2是二次剩余→Euler准则"
2. **tell数据基座新增**：tell_topology=(structural_existence, enumeration_brute_force, method_problem_mismatch)——这个拓扑在POC-VMS-9中已验证可被Pipe 0/1识别
3. **小概念积累**：mersenne/primality/covering_system——这些信号词可用于Pipe 2小概念标记分辨
4. **(tell, hint)对**：两个对——一个是思维瓶颈（穷举→结构的翻译），一个是知识瓶颈（二次剩余判定定理）
5. **QA序列分析**：10轮中8轮元认知+1轮知识注入，知识瓶颈在Q9（二次剩余判定定理）

**第四步：全局视角分析——在整条脉络中识别高Level的(tell, hint)**

局部视角（上面的QA序列表）逐轮提取了10个(tell, hint)对。但有些高Level的(tell, hint)只有在整条脉络中才可见：

| 全局特征 | 内容 | 全局(tell, hint) | 比局部更可泛化的原因 |
|---|---|---|---|
| 翻译类型 | 整条路径从Q1-Q3的枚举转向Q4之后的模算术结构分析 | tell="AI在枚举序列值，没注意到序列项的模结构"，hint="翻译到模算术结构分析" | "枚举→结构"可以泛化到任何领域中出现此转换的题目，而"x₃≡7(mod 8)→二次剩余"只适用于Mersenne序列 |
| 知识瓶颈位置 | Q9是整条序列中唯一的降Level点（从0.5-1.0降到0.2） | tell="AI已经形式化了二次剩余条件，但不知道p≡±1(mod 8)↔2是二次剩余这个判定定理"，hint=知识注入：二次剩余判定定理 | "AI有形式化条件但缺判定定理"可以泛化到任何需要判定定理的数论题 |
| 思维模式转换点 | Q4——从"算前几项"转向"注意mod 8结构" | tell="AI算出了前几项但没注意到模结构"，hint="关注序列项的模运算性质" | "算出了值但没注意模结构"可以泛化到任何需要模分析的序列题 |

**全局视角的(tell, hint)对加入profile**：
```json
{
  "global_tell_hint_pairs": [
    {
      "scope": "translation_type",
      "tell": "AI在枚举序列值，没注意到序列项的模结构",
      "hint": "翻译到模算术结构分析",
      "hint_level": 0.8,
      "generalizability": "high——'枚举→结构'适用于任何领域"
    },
    {
      "scope": "knowledge_bottleneck",
      "tell": "AI已形式化二次剩余条件，但缺判定定理",
      "hint": "知识注入：p≡±1(mod 8)↔2是二次剩余",
      "hint_level": 0.2,
      "generalizability": "medium——适用于需要二次剩余判定的数论题"
    },
    {
      "scope": "thinking_mode_shift",
      "tell": "AI算出了序列值但没注意模结构",
      "hint": "关注序列项的模运算性质",
      "hint_level": 0.7,
      "generalizability": "high——适用于任何需要模分析的序列题"
    }
  ]
}
```

### 完整示例B：矩条件极差题第二问的QA序列分析

> 这道题有完整的10轮QA序列（详见`原语化AI数学工程系统设计/02-案例/01-矩条件极差题第二问.md`），是QA序列分析的canonical example。这里只展示提取结果。

**题目**：已知a₁,...,aₙ满足Σaᵢ=n, Σaᵢ²=2n, Σaᵢ³=3n。证明存在C₂>0使max aᵢ - min aᵢ ≥ √5 + C₂n^(-3/2)。

**QA序列核心特征**：10轮中9轮元认知提示（Q1-Q8, Q10），只有1轮知识性提示（Q9）。但如果没有Q9，整个证明无法完成——badly approximable是纯知识瓶颈。

**关键提取结果**：

```json
{
  "problem_type": "extremal",
  "structure_features": "渐近精细下界——从δ≥0提升到δ≥c/n^(3/2)",
  "key_objects": ["矩条件", "多项式q(x)=x²+x-1", "偏差eᵢ", "稳定性方程"],

  "thinking_patterns": ["translation", "invariant", "extremal", "energy_transmission"],
  "primary_pattern": "extremal",
  "knowledge_required": ["badly_approximable", "cauchy_schwarz", "compactness", "quadratic_irrational"],
  "key_insight": "p=(5-√5)/10是二次无理数→badly approximable→|D|≥c/n→偏差能量下界→极差下界",

  "translation_from": "矩条件不等式",
  "translation_to": "badly approximable数论",
  "translation_type": "分析→数论",

  "tell_topology": {
    "problem_type": "extremal",
    "ai_method_type": "direct_computation",
    "gap_type": "knowledge_gap"
  },
  "tell_small_concepts": ["moment_condition", "quadratic_irrational", "badly_approximable", "stability_equation", "energy_transmission"],

  "tell_hint_pairs": [
    {
      "tell_topology": {"problem_type": "extremal", "ai_method_type": "direct_computation", "gap_type": "method_problem_mismatch"},
      "hint_direction": "投影到根+偏差分解——把每个点分解成最近关键点+偏差",
      "hint_level": 0.7
    },
    {
      "tell_topology": {"problem_type": "extremal", "ai_method_type": "direct_computation", "gap_type": "knowledge_gap"},
      "hint_direction": "知识注入：二次无理数是badly approximable——|p-k/n|≥c₀/n²",
      "hint_level": 0.2
    }
  ],

  "qa_sequence": {
    "rounds": 10,
    "metacognitive_rounds": 9,
    "knowledge_rounds": 1,
    "level_sum": 7.8,
    "knowledge_bottleneck": "Q9——badly approximable性质是纯知识瓶颈，元认知无法替代",
    "thinking_bottleneck": "Q6——投影到根+偏差分解是思维瓶颈，需要'分解成最近关键点+偏差'这个方向引导"
  }
}
```

**这道题的特殊价值**：它展示了QA序列分析的核心洞察——10轮中9轮是元认知提示（高Level hint），只有1轮是知识性提示（低Level hint）。但如果没有这1轮知识注入，整个证明无法完成。**系统必须能区分思维瓶颈和知识瓶颈**——思维瓶颈给元认知提示（高Level hint），知识瓶颈必须给知识性提示（低Level hint）。

**全局视角分析——在整条脉络中识别高Level的(tell, hint)**

| 全局特征 | 内容 | 全局(tell, hint) | 比局部更可泛化的原因 |
|---|---|---|---|
| 翻译类型 | 整条路径从Q1-Q7的分析方法转向Q8-Q9的数论方法 | tell="AI在用分析方法处理渐近下界问题，缺少数论工具"，hint="翻译到badly approximable数论" | "分析→数论"可以泛化到任何需要数论工具的分析题，而"D的下界→badly approximable"只适用于这道题 |
| 知识瓶颈位置 | Q9是整条序列中唯一的降Level点（从0.5-1.0降到0.2） | tell="AI有了稳定性方程，知道D需要下界，但不知道badly approximable性质"，hint=知识注入：二次无理数是badly approximable | "AI有方程需要下界但缺数论工具"可以泛化到任何需要Diophantine逼近的题 |
| 能量传递链 | 偏差能量下界(Σe²≥c/n) → 极差下界(δ≥c/n^(3/2))——跨越Q8-Q10 | tell="AI有了偏差能量下界，不知道怎么传递到极差下界"，hint="用q(x)在根附近的行为+柯西不等式传递能量" | "能量传递"可以泛化到任何需要把中间结果传递到最终目标的题 |
| 思维模式转换点 | Q6——从"分析矩条件"转向"投影到根+偏差分解" | tell="AI在直接处理矩条件，没做投影分解"，hint="投影到关键点+偏差分解" | "直接处理→投影分解"可以泛化到任何需要投影结构的极值题 |

**全局视角的(tell, hint)对加入profile**：
```json
{
  "global_tell_hint_pairs": [
    {
      "scope": "translation_type",
      "tell": "AI在用分析方法处理渐近下界问题，缺少数论工具",
      "hint": "翻译到badly approximable数论",
      "hint_level": 0.8,
      "generalizability": "high——'分析→数论'适用于任何需要数论工具的分析题"
    },
    {
      "scope": "knowledge_bottleneck",
      "tell": "AI有方程需要下界但缺数论工具",
      "hint": "知识注入：二次无理数是badly approximable",
      "hint_level": 0.2,
      "generalizability": "medium——适用于需要Diophantine逼近的题"
    },
    {
      "scope": "energy_transmission_chain",
      "tell": "AI有偏差能量下界，不知道怎么传递到极差下界",
      "hint": "用q(x)在根附近的行为+柯西不等式传递能量",
      "hint_level": 0.6,
      "generalizability": "high——'能量传递'适用于任何需要中间结果传递的题"
    },
    {
      "scope": "thinking_mode_shift",
      "tell": "AI在直接处理矩条件，没做投影分解",
      "hint": "投影到关键点+偏差分解",
      "hint_level": 0.7,
      "generalizability": "high——'直接处理→投影分解'适用于任何需要投影结构的极值题"
    }
  ]
}
```

### 完整示例C：虚拟题——展现"蕴含"型全局(tell, hint)的两次出现

> **这个示例专门展现用户指出的特殊情况**：有些高价值、高Level、高可泛化的(tell, hint)不是在单个(Q,A)中可见的，也不是路径特征的简单汇总，而是需要在某个(Q,A)的位置，看到之前和之后的整个QA序列，才能"读出"整条序列**蕴含**的(tell, hint)。
>
> 这个示例是虚拟的——题目和QA序列都是构造的，目的是展现工作模式，不是展现真实数学。

**虚拟题目**：证明对任意正整数n，Σ_{d|n} φ(d) = n，其中φ是Euler函数。

**QA序列（10轮）**：

| 轮 | Q（hint） | A（预期回复） | 情况类型 | Level |
|---|---|---|---|---|
| Q1 | "描述题目结构" | 关于除数函数和Euler函数的恒等式，需要证明n的所有除数的φ值之和等于n | 纯元认知观察 | 1.0 |
| Q2 | "列出所有可能方向" | 直接计算、用φ定义、群论、容斥、生成函数... | 自由列举 | 1.0 |
| Q3 | "试着用φ的定义直接算" | φ(d)=d·∏(1-1/p)，但Σ_{d|n} d·∏(1-1/p)不好直接化简 | 小尝试 | 0.9 |
| Q4 | "试试群论视角——想想Z/nZ" | Z/nZ中阶为d的元素有φ(d)个，每个元素的阶整除n，Σ_{d|n} φ(d) = |Z/nZ| = n | 思维操作引导 | 0.7 |
| Q5 | "这个证明的核心是什么？" | 把数论函数恒等式翻译成群论命题——"阶为d的元素有φ(d)个"是群论事实 | 推进（自我评估） | 1.0 |
| Q6 | "能用纯数论方法证明吗？" | 考虑分数1/n,...,n/n，约分后分母取遍n的所有除数d，分母为d的有φ(d)个，所以Σφ(d)=n | 思维操作引导 | 0.7 |
| Q7 | "这两个证明有什么关系？" | 群论中的"阶为d"对应数论中的"约分后分母为d"。本质相同——都是按某种不变量分类计数 | 推进（自我评估） | 1.0 |
| Q8 | "把φ换成其他数论函数，类似恒等式成立吗？" | Σμ(d)=[n=1]（容斥），Σd=σ(n)（定义）。都是除数结构的不同面相 | 思维操作引导 | 0.6 |
| Q9 | "这些恒等式的共同结构是什么？" | 都是在"n的除数格"上做某种求和。φ对应按阶分类，μ对应容斥，σ对应恒等求和。不同函数=除数格上的不同测度 | 推进（自我评估） | 0.8 |
| Q10 | "回到原题，深层认知是什么？" | 表面是数论恒等式，本质是群论计数。翻译方向是"数论→群论" | 能量传递引导 | 0.6 |

---

**蕴含型全局(tell, hint)的第一次出现——站在Q5的位置看前后**

**在Q5的位置，你看到**：
- **之前（Q1-Q4）**：AI从数论方法（定义、直接计算）出发，在Q3碰壁（φ的定义不好直接化简），在Q4转向群论，找到了群论证明
- **之后（Q6-Q10）**：AI会在Q6用纯数论方法重新证明，在Q7比较两个证明发现本质相同，在Q8-Q9推广到其他函数发现共同框架

**在Q5这个位置，你能读出什么蕴含的(tell, hint)？**

不是"从数论转向群论"——这是路径特征的总结，在Q4就已经可见了。

**蕴含的是**：AI在Q4找到了群论证明，在Q5总结了这个证明的核心，但AI**不知道这个群论证明和数论证明是同一个东西的两个面**。AI此刻以为自己找到了"另一种方法"，但实际上群论证明和数论证明共享一个更深的统一性——这个统一性要到Q7才会被AI发现。

**蕴含的(tell, hint)**：
- tell：AI有了群论证明但认为它是"另一种方法"——AI处于"有两个方法但没看到统一性"的状态。这个tell在Q5时不可见（AI还没做数论证明），在Q7时才可见但已经过了（Q7时AI已经在比较了）。**只有在Q5的位置同时看到前后才能读出。**
- hint：寻找两个证明之间的深层对应——"群论中的阶对应数论中的约分分母，本质都是按不变量分类计数"
- hint_level：0.9（高Level，高可泛化——"寻找不同方法之间的深层统一性"适用于任何领域）
- generalizability：high——"有两个方法但没看到统一性"这个tell可以泛化到任何有多解法的题目

**为什么这不是路径特征总结**：路径特征总结会说"AI从数论转向群论"。但蕴含的(tell, hint)说的是"AI此刻不知道自己有的两个方法其实是统一的"——这是关于AI的认知状态，不是关于路径的走向。你只有在Q5的位置看到"之前AI找到了群论证明"和"之后AI会发现两个证明的统一性"，才能读出"此刻AI不知道统一性的存在"这个tell。

---

**蕴含型全局(tell, hint)的第二次出现——站在Q8的位置看前后**

**在Q8的位置，你看到**：
- **之前（Q1-Q7）**：AI证明了一个具体的恒等式（Σφ(d)=n），用群论和数论两种方法证明了它，并发现两种方法本质相同
- **之后（Q9-Q10）**：AI会发现所有类似恒等式的共同结构——除数格上的测度求和——这是比单个恒等式高一个Level的框架

**在Q8这个位置，你能读出什么蕴含的(tell, hint)？**

不是"推广到其他函数"——这是Q8本身的局部内容。

**蕴含的是**：AI在Q1-Q7中证明了一个具体案例并理解了它的两种证法，但AI**不知道这个案例的证明方法蕴含了一个一般框架**。AI在Q8开始问"能不能推广"，但它还不知道推广后的统一框架长什么样——这个框架要到Q9才会出现。在Q8这个位置，AI处于"有案例但没框架"的状态，而这个状态蕴含了一个高Level的(tell, hint)：**从具体案例的证明方法中抽象出一般框架**。

**蕴含的(tell, hint)**：
- tell：AI有了具体案例的证明但不知道这些证明方法蕴含了一个一般框架——AI处于"有案例但没框架"的状态。这个tell在Q8时不可见（AI还没做Q9的推广），在Q9时才可见但已经过了（Q9时AI已经在框架里了）。**只有在Q8的位置同时看到前后才能读出。**
- hint：从具体案例的证明方法中抽象出一般框架——"不同的数论函数对应除数格上的不同测度"
- hint_level：0.9（高Level，高可泛化——"从案例抽象框架"适用于任何领域）
- generalizability：high——"有案例但没框架"这个tell可以泛化到任何需要从具体推广到一般的题目

**为什么这不是路径特征总结**：路径特征总结会说"AI从具体推广到一般"。但蕴含的(tell, hint)说的是"AI此刻不知道自己的案例里已经蕴含了框架"——这是关于AI的认知盲区，不是关于路径的走向。你只有在Q8的位置看到"之前AI有了具体案例"和"之后AI发现了框架"，才能读出"此刻AI不知道案例蕴含框架"这个tell。

---

**蕴含型全局(tell, hint)的profile JSON**：

```json
{
  "global_tell_hint_pairs": [
    {
      "scope": "implicit_unity",
      "observation_point": "Q5",
      "tell": "AI有了群论证明但认为它是'另一种方法'，不知道两个证明共享更深的统一性",
      "hint": "寻找不同方法之间的深层对应——群论中的阶对应数论中的约分分母",
      "hint_level": 0.9,
      "generalizability": "high——'有多个方法但没看到统一性'适用于任何多解法题目",
      "why_not_visible_locally": "在Q5时AI还没做数论证明（tell不可见），在Q7时AI已经在比较了（tell已过时），只有在Q5看前后才能读出"
    },
    {
      "scope": "implicit_framework",
      "observation_point": "Q8",
      "tell": "AI有了具体案例的证明但不知道证明方法蕴含了一般框架",
      "hint": "从具体案例的证明方法中抽象出一般框架——不同数论函数=除数格上的不同测度",
      "hint_level": 0.9,
      "generalizability": "high——'有案例但没框架'适用于任何需要从具体推广到一般的题目",
      "why_not_visible_locally": "在Q8时AI还没做推广（tell不可见），在Q9时AI已经在框架里了（tell已过时），只有在Q8看前后才能读出"
    }
  ]
}
```

---

**三个示例的对比——三种全局视角(tell, hint)的区别**：

| 类型 | 示例A/B的全局(tell, hint) | 示例C的蕴含型(tell, hint) |
|---|---|---|
| **看到什么** | 路径特征（翻译类型、知识瓶颈位置、能量传递链、思维模式转换点） | AI的认知盲区（不知道两个方法统一、不知道案例蕴含框架） |
| **怎么读出** | 总结整条路径的结构特征 | 在某个位置看到前后，读出AI此刻不知道但前后蕴含的东西 |
| **是路径特征总结吗** | 是——总结"路径从A转向B" | 不是——读出"AI此刻不知道X"，X是前后蕴含的 |
| **可泛化性来源** | 路径结构本身可泛化（"枚举→结构"适用于多领域） | 认知盲区本身可泛化（"有方法没看到统一"适用于多领域） |
| **在局部可见吗** | 部分可见——翻译类型在转换点附近可见 | 完全不可见——在观察点时tell还没出现，在tell出现时已过了观察点 |

**关键认知**：蕴含型(tell, hint)与前两个示例的全局(tell, hint)有本质区别。前两个示例的全局(tell, hint)是"站在高处俯瞰路径"——总结路径特征。蕴含型(tell, hint)是"站在路径中间，看到前和后，读出AI此刻的认知盲区"——这个盲区在观察点时不可见（因为AI还没走到后面），在后面时已过时（因为AI已经走过了盲区），**只有在观察点同时看到前后才能读出**。

**Pass 1（探索性·发现维度）**：分析少量题目（含QA序列分析）→发现新维度/新类别值→追加到Schema。Pass 1的产出是一个不断增长的Schema文件。

**Pass 2（穷举性·完整标注）**：用Schema final对所有题做穷举标注（含QA序列分析），每道题输出完整profile JSON，存入ArangoDB。

**每道题的完整处理流程**（Pass 1和Pass 2都遵循）：
1. **读题目和解答**
2. **QA序列分析**——重构"什么提示序列能引导AI从题目走到解答"，分解为(状态, Q)对
3. **标注问题拓扑层**——从题目结构中提取problem_type/structure_features/key_objects
4. **标注解答思维模式层**——从QA序列中提取thinking_patterns/primary_pattern/key_insight
5. **标注翻译方向层**——从QA序列中识别翻译操作，标注translation_from/to/type
6. **标注tell拓扑层 + 反思拓扑分类是否需要进化**——从QA序列中提取tell_topology/small_concepts/expected_ai_method。**这一步不只是机械标注，subagent必须同时思考以下问题**：
   - **当前拓扑分类是否够用**——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？如果不能，是否需要新增类别值？
   - **粒度是否一致**——已有的拓扑值是否粒度统一？（反例：`structural_existence`很抽象，`word_problem_with_diophantine_constraint`很具体——粒度不一致会导致Pipe 1过滤失效）
   - **是否需要新的拓扑维度**——三个维度(problem_type, ai_method_type, gap_type)是否足够区分这道题的tell和已有tell？如果两个拓扑相同但实际不同的tell无法用小概念区分，是否需要增加第四个维度？
   - **如何在汇报中提出**——如果发现拓扑分类需要进化，在汇报中明确说明：发现了什么问题、建议怎么改、影响哪些已有profile
7. **提取(tell, hint)对**——从QA序列的每轮(状态, Q)中提取。**每个(tell, hint)对必须包含tell_topology和tell_small_concepts**——这是Pipe 0/1/2三层检索架构的依据（见§数据库Schema设计v3）
8. **标注实验适用性层**——判断bare_ai_expected/suitable_for_poc
9. **输出完整profile JSON**
10. **Pass 1额外**：检查是否有Schema中没有的新维度/新类别值，如有则追加到Schema。**同时检查拓扑分类是否需要进化**（见第6步的反思）

**关键递进关系**：
```
Pass 1（5-10道题）→ Schema v1
Pass 1（再5-10道题）→ Schema v2（追加新维度/新类别值）
...
Pass 1（所有题分析完）→ Schema final
Pass 2（用Schema final，对所有题做穷举标注）→ problem_profiles集合
```

**初始Schema种子**：279号文档的四类维度（元数据/难度/思维模式/实验适用性）+ 上面"从每道题中提取什么"中列出的所有维度。Pass 1在种子基础上发现新维度。

### 做到哪了——进度追踪

**ArangoDB集合**：`problem_extraction_progress`——每道题（无论是否处理）都在此集合中有一条记录，精确到单个题目：

```json
{
  "problem_id": "aops_instruct_000001",
  "source_dataset": "aops_instruct",
  "source_dataset_doc_id": "math_datasets/aops_instruct",
  "extraction_status": "completed | pending | skipped | in_progress",
  "skip_reason": "no_solution | not_textualized | pdf_only | null",

  "external_ref": {
    "local_path": "knowledge/problem_banks/aops_instruct/data/problem_000001.json",
    "original_index": 1,
    "original_id_in_source": "..."
  },

  "metadata": {
    "domain": "number_theory",
    "subfield": "Number Theory",
    "difficulty_source": "competition",
    "competition_tier": "IMO",
    "answer_type": "Numerical",
    "has_solution": true,
    "question_length": 234,
    "source_year": 1998,
    "source_competition": "IMO 1998 Problem 3"
  },

  "schema_version": 3,
  "extracted_at": "2026-08-08T...",
  "profile_doc_id": "problem_profiles/aops_instruct_000001",
  "extracted_by_subagent_id": "..."
}
```

**关键约束**：
- **精确到单个题目**——每道题一条记录，不按数据集批量记录
- **外部索引**——`external_ref.local_path`指向硬盘上这道题的原始文件，回头能在硬盘上找到从题目到解答的完整内容
- **元数据记录**——从哪里来的（source_dataset）、原始外部信息中它是什么难度的（difficulty_source）、是第几道题（original_index）、来自什么竞赛/年份等
- **所有题都有记录**——包括没处理的题（`extraction_status="skipped"`，`skip_reason`标注原因），不只是处理了的题

**下一个AI进来怎么知道做到哪了**：
```python
# 查已处理多少题
db.aql.execute('RETURN COUNT(FOR p IN problem_extraction_progress FILTER p.extraction_status == "completed" RETURN 1)')
# 查当前Schema版本
db.aql.execute('FOR p IN problem_extraction_progress SORT p.schema_version DESC LIMIT 1 RETURN p.schema_version')
# 查哪些题还没处理（只查可处理的——有解答且已文本化的）
db.aql.execute('FOR p IN problem_extraction_progress FILTER p.extraction_status == "pending" AND p.skip_reason == null RETURN p')
# 查某个数据集的处理进度
db.aql.execute('FOR p IN problem_extraction_progress FILTER p.source_dataset == "aops_instruct" COLLECT WITH COUNT INTO c RETURN c')
```

**Schema文件路径**：`knowledge/problem_banks/extraction_schema.json`——活的文件，每次Pass 1发现新维度就更新版本号。

### 跨Session怎么续

**新AI进入本repo，看到本节，知道要做题海梳理工作时**：

1. **读Schema文件**：`knowledge/problem_banks/extraction_schema.json`——了解当前所有已发现的维度和类别值
2. **查ArangoDB进度**：`problem_extraction_progress`集合——了解哪些题处理了、当前Schema版本
3. **读最小认知包**（下方§最小认知包）——恢复tell/hint/概念树的操作认知
4. **读QA序列分析方法+完整示例**（上方§QA序列分析和§完整示例A/B/C）——恢复QA序列分析的操作方法
5. **读数据库Schema设计**（下方§数据库Schema设计）——了解集合结构和字段定义
6. **继续处理下一批未处理的题**——按"每道题的完整处理流程"执行（含QA序列分析），可用subagent并发（见下方§并发处理）
7. **每批处理完**：入库`problem_profiles` + 更新`problem_extraction_progress` + 更新Schema（如有新维度）+ commit

### 数据库Schema设计

> **本节记录题海梳理工作线涉及的ArangoDB集合和它们的Schema。**
>
> **⚠️ 数据库设计是可迭代的，不是一成不变的！** 分析题目的过程中，如果发现现有Schema无法记录某个有价值的信息，或者某个字段定义不够精确，**可以而且应该更新数据库设计**。但每次更新必须：
> 1. **更新本节**——修改AGENTS.md中的Schema定义，让所有AI（Master和subagent）看到最新设计
> 2. **记录变更原因**——在本节末尾的"Schema变更历史"中记录为什么改、改了什么
> 3. **向后兼容**——新增字段不破坏已有记录，已有字段改名时保留旧字段为别名
> 4. **通知subagent**——Master Agent在派发下一批任务时，把最新Schema告诉subagent
>
> **当前Schema版本：v3**（2026-08-08，修复v2中丢失的per-pair拓扑标注）

**集合1：`problem_extraction_progress`**——题目处理进度（每道题一条记录，见上方§做到哪了）

```
字段：
  problem_id          : string  (主键，格式：{source_dataset}_{original_index:06d})
  source_dataset      : string  (来源数据集名)
  source_dataset_doc_id: string (math_datasets集合中的文档ID)
  extraction_status   : string  (completed | pending | skipped | in_progress)
  skip_reason         : string  (no_solution | not_textualized | pdf_only | incomplete_solution | null)
  external_ref        : object  ({local_path, original_index, original_id_in_source})
  metadata            : object  ({domain, subfield, difficulty_source, competition_tier,
                                  answer_type, has_solution, question_length,
                                  source_year, source_competition, country})
  difficulty_tier     : int     (1-5，1=最难，5=最易，见§难度分级方案)
  priority            : int     (同difficulty_tier，Master Agent按此升序派发)
  schema_version      : int     (处理时使用的Schema版本)
  extracted_at        : string  (ISO时间戳)
  profile_doc_id      : string  (指向problem_profiles集合中的文档ID)
  extracted_by        : string  (处理此题的AI标识——"master"或subagent ID)
```

**集合2：`problem_profiles`**——题目完整侧写（处理完成的题一条记录）

```
=== 基本元数据 ===
  _key                : string  (同problem_id)
  source_id           : string
  source_dataset      : string
  schema_version      : int     (本profile使用的Schema版本)

=== 题目与解答原文（v2新增——避免subagent每次重新读文件）===
  problem_text        : string  (题目原文，从文件中提取的纯文本)
  solution_text       : string  (解答原文，从文件中提取的纯文本)
  solution_summary    : string  (解答方法的1-2句话概括——不是解答全文，是"用什么方法解的")

=== 题目结构分析 ===
  domain              : string  (数学领域：algebra/number_theory/combinatorics/geometry/analysis)
  subfield            : string  (子领域，如"trigonometric identities"、"constraint satisfaction")
  answer_type         : string  (Proof | Numerical | Expression | Formal Proof)
  answer              : string  (最终答案，proof题则为"QED"或证明结论)

  problem_type        : string  (题目类型——从题目结构读出的类型，如"trigonometric identity verification")
  solution_method_type: string  (v2新增——解答方法类型，如"telescoping sum"、"exhaustive enumeration"
                                          区别于problem_type：同一题型可能有不同解法类型)
  structure_features  : string  (题目结构特征描述)
  key_objects         : array[string]  (题目中的关键数学对象)

=== 思维模式分析 ===
  thinking_patterns   : array[string]  (解答中使用的思维模式，如"telescoping"、"WLOG sorting"、"auxiliary factor")
  primary_pattern     : string  (主导思维模式)
  knowledge_required  : array[string]  (解答所需的前置知识，如"product-to-sum formula"、"permutation")
  key_insight         : string  (一句话描述的关键转折点——"啊哈时刻")

=== 翻译分析 ===
  translation_from    : string  (从什么方法/语言翻译，如"direct calculation")
  translation_to      : string  (翻译到什么方法/语言，如"telescoping sum via auxiliary factor")
  translation_type    : string  (翻译类型分类)

=== tell拓扑与概念 ===
  tell_topology       : object  ({problem_type, ai_method_type, gap_type})
  tell_small_concepts : array[string]  (从题目和解答文本中实际出现的关键概念词)
  expected_ai_method  : string  (bare AI预期会用的方法——可能走错的方法)
  correct_method      : string  (正确方法——解答实际用的方法)

=== (tell, hint)对——局部视角 ===
  tell_hint_pairs     : array[object]  (逐轮QA中提取的(tell, hint)对)
    每个object:
      qa_round        : int     (对应QA序列的第几轮)
      tell            : string  (AI在这个位置的状态/分叉信号)
      hint            : string  (给AI的提示方向)
      hint_level      : float   (**⚠️ 必须是0-1之间的浮点数**，越高越抽象。禁止用1-4整数)
      situation_type  : string  (**⚠️ 只能取以下6个值之一，禁止自创**：
                                  纯元认知观察 | 自由列举 | 小尝试 | 思维操作引导 | 推进 | 能量传递引导)
      is_knowledge_bottleneck: boolean  (这轮是否是纯知识瓶颈——必须给知识性提示)
      tell_topology   : object  (v3恢复——每个tell的拓扑标注，Pipe 0/1检索的依据)
        {problem_type, ai_method_type, gap_type}
        problem_type    : string  (问题类型大概念，如structural_existence/extremal/trigonometric_identity/...)
        ai_method_type  : string  (bare AI在此位置预期会用的方法类型，如enumeration_brute_force/direct_calculation/case_by_case/...)
        gap_type        : string  (AI方法和问题之间的不匹配类型，如method_problem_mismatch/knowledge_gap/structural_transformation/search_space_estimation/...)
      tell_small_concepts: array[string]  (v3恢复——这个tell的小概念信号词，Pipe 2标记分辨的依据)

=== (tell, hint)对——全局视角 ===
  global_tell_hint_pairs: array[object]  (全局视角的(tell, hint)对)
    每个object:
      scope_type      : string  ("path_feature"或"implicit"，区分路径特征型和蕴含型)
      scope           : string  (具体范围描述，如"translation_type"或"implicit_unity")
      observation_point: string (蕴含型：观察点Q编号；路径特征型：null)
      tell            : string  (全局tell)
      hint            : string  (全局hint)
      hint_level      : float   (0-1)
      generalizability: string  (high/medium/low + 泛化描述)
      why_not_visible_locally: string  (蕴含型专用——为什么在局部不可见)
      tell_topology   : object  (v3新增——全局tell的拓扑标注)
        {problem_type, ai_method_type, gap_type}
      tell_small_concepts: array[string]  (v3新增——全局tell的小概念信号词)

=== bare AI预测 ===
  bare_ai_expected    : string  (pass | fail | marginal)
  bare_ai_error_prediction: string  (v2新增——bare AI会犯什么错的具体描述，
                                              如"会试图直接计算cos(π/7)的值而不是变换表达式结构")
  suitable_for_poc    : array[string]  (适合哪些POC实验)
  discriminates_levels: boolean  (是否能区分不同Level的AI)

=== QA序列完整记录（v2重构——从只存统计量改为存完整轮次）===
  qa_sequence         : object
    rounds            : array[object]  (完整QA轮次记录)
      每个object:
        round         : int     (轮次编号，从1开始)
        question      : string  (Q——给AI的提示/问题)
        expected_answer: string (A——预期回复)
        situation_type: string  (情况类型)
        level         : float   (Level值0-1)
    stats             : object  (统计量)
      total_rounds    : int
      metacognitive_rounds: int  (情况类型为纯元认知观察/自由列举/推进/能量传递的轮数)
      knowledge_rounds: int     (情况类型为思维操作引导的轮数)
      level_sum       : float
      knowledge_bottleneck: string  (知识瓶颈在哪轮，或null)
      thinking_bottleneck: string  (思维瓶颈在哪轮，或null)

=== 分析元数据（v2新增）===
  analysis_metadata   : object
    analyzed_by       : string  ("master"或subagent ID)
    analyzed_at       : string  (ISO时间戳)
    analysis_duration : string  (分析耗时，如"15min"——粗略估计)
    notes             : string  (分析过程中的备注，如"此题解答很长，QA序列可能不完整")
```

**集合3：`math_datasets`**（已有）——数据集元数据（不变，见212号）

**集合4：`extraction_schema_versions`**（按需创建）——Schema版本历史

```
字段：
  version             : int
  schema_json         : object  (完整的Schema定义)
  created_at          : string
  created_by          : string
  changes_from_prev   : string  (本版相对上版的变化描述)
```

**索引建议**：
- `problem_extraction_progress`上按`source_dataset`建索引
- `problem_extraction_progress`上按`extraction_status`建索引
- `problem_extraction_progress`上按`difficulty_tier`建索引
- `problem_extraction_progress`上按`priority`建索引
- `problem_profiles`上按`domain`建索引
- `problem_profiles`上按`solution_method_type`建索引
- `problem_profiles`上按`thinking_patterns`建数组索引
- `problem_profiles`上按`tell_small_concepts`建数组索引（用于tell检索）

### 拓扑分类体系（活文档·随分析进化）

> **本节记录tell_topology三个维度的已有类别值和已知问题。subagent分析题目时必须参考本节，确保拓扑标注粒度一致、分类合理。发现问题时在汇报中提出，Master Agent更新本节。**

**当前已有拓扑值**（来自8道已分析题+2道POC题）：

**problem_type**（问题类型大概念）：
| 已有值 | 来源 | 粒度评价 |
|---|---|---|
| structural_existence | 1631题(POC) | ✅ 抽象，好 |
| discrete_combinatorial | 1843题(POC) | ✅ 抽象，好 |
| trigonometric_identity | IMO1963P5 | ✅ 中等 |
| constraint_satisfaction | IMO1963P6 | ✅ 中等 |
| absolute_value_system | IMO1966P5 | ⚠️ 偏具体 |
| word_problem_with_diophantine_constraint | IMO1967P6 | ❌ 太具体，应归入更抽象的类 |
| infinite_sum_evaluation_with_floor | IMO1968P6 | ❌ 太具体 |
| characterization | IMO1967P5 | ✅ 抽象，好 |
| functional_equation_periodicity | IMO1968P5 | ⚠️ 偏具体 |
| inequality_proof | IMO1969P6 | ✅ 中等 |

**ai_method_type**（bare AI预期方法类型）：
| 已有值 | 来源 | 粒度评价 |
|---|---|---|
| enumeration_brute_force | 1631题(POC) | ✅ 抽象，好 |
| continuous_analytic | 1843题(POC) | ✅ 抽象，好 |
| direct_calculation | IMO1963P5 | ✅ 抽象，好 |
| logical_deduction | IMO1963P6 | ✅ 抽象，好 |
| case_by_case | IMO1966P5 | ✅ 抽象，好 |
| brute_force_simulation_or_simultaneous_equations | IMO1967P6 | ❌ 太长太具体 |
| direct_evaluation_or_small_cases_only | IMO1968P6 | ❌ 太长太具体 |
| algebraic_identity | IMO1967P5 | ✅ 中等 |
| equation_solving | IMO1968P5 | ✅ 抽象，好 |
| direct_manipulation | IMO1969P6 | ✅ 抽象，好 |

**gap_type**（方法-问题不匹配类型）：
| 已有值 | 来源 | 粒度评价 |
|---|---|---|
| method_problem_mismatch | 1631/1843题(POC) | ✅ 抽象，好 |
| knowledge_gap | 1631题(POC) | ✅ 抽象，好 |
| structural_transformation | IMO1963P5 | ✅ 中等 |
| search_space_estimation | IMO1963P6 | ✅ 中等 |
| global_sorting | IMO1966P5 | ⚠️ 偏具体 |
| recurrence_solving_and_number_theoretic_argument | IMO1967P6 | ❌ 太具体，应拆分 |
| knowledge_bottleneck_on_floor_identity | IMO1968P6 | ❌ 太具体，应归入knowledge_gap |
| method_translation | IMO1967P5 | ✅ 中等 |
| strategic_algebraic_identity | IMO1968P5 | ⚠️ 偏具体 |
| method_selection_and_hidden_structure_recognition | IMO1969P6 | ❌ 太长，应拆分 |

**已知问题**（subagent分析时需注意）：
1. **粒度不一致**——有些值很抽象（`structural_existence`），有些很具体（`word_problem_with_diophantine_constraint`）。Pipe 1过滤需要粒度统一——如果两个tell的problem_type一个用`structural_existence`一个用`word_problem_with_diophantine_constraint`，它们不会被匹配到一起，即使可能应该匹配。
2. **需要归一化**——太具体的值应归入更抽象的类。例如`word_problem_with_diophantine_constraint`应归入`diophantine`或`number_theory`，`knowledge_bottleneck_on_floor_identity`应归入`knowledge_gap`。
3. **gap_type可能需要更多维度**——当前gap_type混合了"方法不匹配"和"知识缺失"两种不同类型的不匹配。随着分析更多题，可能需要拆分。

**subagent标注拓扑时的规则**：
- **优先使用已有值**——如果这道题的拓扑可以归入已有的某个类别值，用已有的，不要新建
- **新建值时检查粒度**——如果必须新建，确保粒度与同维度其他值一致（参考上表中标注✅的值作为粒度基准）
- **太具体的值要归一化**——如果发现已有的某个值太具体，在汇报中提出归一化建议
- **在汇报中报告拓扑进化建议**——如果发现需要新增类别值、归一化已有值、或增加新维度，在汇报中明确说明

**Schema变更历史**：

| 版本 | 日期 | 变更 | 原因 |
|---|---|---|---|
| v1 | 2026-08-08 | 初始设计 | 279号文档四类维度+AGENTS.md提取维度 |
| v2 | 2026-08-08 | 重大修订 | 3道Tier 1题目分析经验（IMO 1963 P5/P6, IMO 1966 P5） |
| v3 | 2026-08-08 | 修复per-pair拓扑标注 | v2重构时丢失了每个(tell,hint)对的tell_topology和tell_small_concepts |

**v2变更详情**（基于3道题分析经验）：
1. **新增`problem_text`和`solution_text`**——分析时需要反复读题目和解答，每次从文件读取效率低且Lean格式需要解析。存入profile后subagent可以直接用。
2. **新增`solution_summary`**——解答方法的1-2句话概括，用于快速浏览和检索。
3. **新增`solution_method_type`**——区别于`problem_type`。IMO 1963 P5的problem_type是"trigonometric identity verification"，但solution_method_type是"telescoping sum via auxiliary factor"——同一题型可能有不同解法。
4. **`tell_hint_pairs`结构化**——从模糊的"array[object]"改为明确的字段定义（qa_round, tell, hint, hint_level, situation_type, is_knowledge_bottleneck）。
5. **`global_tell_hint_pairs`新增`scope_type`字段**——区分"path_feature"（路径特征型）和"implicit"（蕴含型）。3道题分析中发现这两种全局(tell, hint)有本质区别，必须区分。
6. **新增`why_not_visible_locally`字段**——蕴含型(tell, hint)专用，记录为什么在局部不可见。这是蕴含型的核心特征。
7. **新增`bare_ai_error_prediction`**——不只是pass/fail，还要描述bare AI会犯什么错。如"会试图直接计算cos值而不是变换结构"。
8. **`qa_sequence`从只存统计量重构为存完整轮次**——每轮的Q/A/情况类型/Level都存入`rounds`数组，统计量移入`stats`子对象。
9. **新增`analysis_metadata`**——记录谁分析的、什么时候、分析耗时、备注。
10. **`problem_extraction_progress`新增`difficulty_tier`和`priority`字段**——67837题已入库，含5级难度分级。

**v3变更详情**（修复v2的设计缺陷）：
1. **`tell_hint_pairs`恢复`tell_topology`字段**——v2重构时丢失了每个局部(tell,hint)对的`tell_topology`。原始设计（示例A）中每个pair都有自己的拓扑标注`{problem_type, ai_method_type, gap_type}`，这是Pipe 0/1检索的依据。没有per-pair拓扑标注，数据基座无法按拓扑检索Pattern，整个三层Pipe架构失效。
2. **`tell_hint_pairs`恢复`tell_small_concepts`字段**——同上，v2丢失了每个pair的小概念信号词。这是Pipe 2标记分辨的依据。
3. **`global_tell_hint_pairs`新增`tell_topology`字段**——v2中全局(tell,hint)对没有拓扑标注。全局tell也需要拓扑分类才能被Pipe 0/1检索。
4. **`global_tell_hint_pairs`新增`tell_small_concepts`字段**——全局tell的小概念信号词。
5. **影响范围**：已入库的8个profile（3个master分析+5个subagent分析）都缺少per-pair拓扑标注，需要回补。

### 并发处理——subagent流水线

**可以用subagent并发处理题目，但必须遵守以下约束**：

**最大并发数**：5个subagent同时运行（批次制）。

**批次制工作节奏**：
- 每批5个subagent并发启动→全部完成→Master Agent逐个审计（5个审计）→审计全部完成→发起下一批5个
- 不是流水线补位——不补位，等全批完成
- 审计是批与批之间的门槛——不审计完不发起下一批

**subagent的工作内容**：
每个subagent处理一道题，完整执行"每道题的完整处理流程"（10步，含QA序列分析）：
1. 从ArangoDB `problem_extraction_progress`中领取一道`extraction_status="pending"`的题
2. 将状态改为`in_progress`
3. 通过`external_ref.local_path`从硬盘读取题目和解答
4. 执行QA序列分析（局部视角7步+全局视角1步）
5. 输出完整profile JSON
6. 入库`problem_profiles`
7. 更新`problem_extraction_progress`状态为`completed`
8. 如发现新维度，追加到Schema文件并更新版本号

**subagent需要的信息**（Master Agent在启动subagent时提供）：
- Schema文件路径：`knowledge/problem_banks/extraction_schema.json`
- 数据库连接信息：`localhost:8529`，数据库`xishujuzhen_math_glm52`
- 数据库Schema定义（上方§数据库Schema设计）
- 最小认知包（上方§最小认知包）
- QA序列分析方法+示例（上方§QA序列分析和§完整示例A/B/C）
- 当前要处理的题的`problem_id`

**Master Agent的职责**（不委托给subagent）：
- 管理并发槽位——每批5个subagent，批次制运行
- 监控subagent状态——等全批完成后逐个审计
- Schema版本管理——多个subagent同时发现新维度时合并到Schema
- 处理异常——subagent失败时记录原因，将题目状态改回`pending`

### 最小认知包——做提取工作所需的最低认知

**tell**：从推理AI的thinking中读出的分叉信号——AI走了哪条路、没走哪条路。tell取自poker术语。不是"AI卡住了"，而是"AI走错路了，在它没走的路上开新分支"。

**hint**：给新AI的翻译方向。从字典中匹配的具体翻译方向。高Level hint（"翻译到另一种语言"）太抽象，需要系统化地Low Level化——遍历各数学领域列出具体形式（"翻译到模算术" / "翻译到p-adic赋值" / "翻译到二次剩余" / ...）。Low Level化是有限枚举问题，能应用的数学领域就那么多。

**(tell, hint)对**：tell是输入（从推理AI读出），hint是输出（给新AI注入）。一个tell可以对应多个hint，一个hint可以被多个tell触发——多对多关系。每道有答案的题，它的解答本质上就是一个(问题处境→正确方向)的映射，也就是一个(tell, hint)对。

**大概念/小概念/概念树**：
- 大概念：tell的拓扑结构，用(problem_type, ai_method_type, gap_type)三个维度描述。用于Pipe 1形式化过滤——从10万级tell中缩小范围。
- 小概念：当大概念不足以区分两个相似tell时，用更细的概念信号词区分。只要两个tell能用语言表达出区别，就能定义概念来区分。
- 概念树：当概念数量膨胀时，用树状层次结构管理概念关系。同一细分范围的概念放入同一文件，AI按需加载。

**Pipe 0/1/2**：tell识别的三层架构。Pipe 0将thinking拓扑化（提取大概念），Pipe 1用大概念做形式化过滤缩小范围，Pipe 2用小概念做标记分辨精准识别。

**QA序列**：辅助智能体引导推理智能体解题的完整对话记录。每轮一个Q（hint）和一个A（回复）。QA序列分析是从题目+解答中提取(tell, hint)对的唯一正确方法——把解答分解为一连串(状态, 提示)对，每对就是一个(tell, hint)对。QA序列中有6种情况类型，其中5种是元认知提示（高Level hint），1种是知识性提示（低Level hint，必须提供，元认知无法替代）。详见上方§QA序列分析和§完整示例A/B。

**提取质量标准**：
- problem_type和ai_method_type的标注必须能泛化（不是题目特化的，而是方法类型的）
- key_insight必须是一句话描述的关键转折点（不是解答摘要，而是"啊哈时刻"）
- translation_from/to必须具体（不是"翻译到另一种语言"，而是"翻译到模算术"）
- tell_small_concepts必须是从题目和解答文本中实际出现的关键词（不是凭空构造的）

### 已下载的有答案的题库（提取对象）

**数据存储位置**（2026-08-12起生效）：

> **所有新下载的题库数据统一放到 `/data/math-manify/` 目录。**
>
> - D盘有857GB可用空间，足够存放百万题库
> - 旧的 `knowledge/problem_banks/` 目录保留已有数据，不再新增下载
> - 新数据集按 `math-manify/<source_dataset>/` 子目录组织
> - 策略文档：375号（百万难题筛选策略）
> - 下载后录入 `problem_extraction_progress` 表，用 `enqueue_problem.py` 送入 `problem_queue`

**处理范围约束**：
1. **只分析有解答的题**——没有答案的题（如ConjectureBench）不在提取范围内
2. **只分析已经文本化的题**——不理会PDF中的题目。PDF格式的题（吉米多维奇、Demidovich、Engel等）需要先OCR或人工转录为文本后才处理
3. **数据库中记录所有题的状态**——包括没处理的题（PDF未文本化的、无答案的），都要在数据库中有记录，标注处理状态

**已入库的文本化数据集**（67837题，已全部入库`problem_extraction_progress`集合）：

| 数据集 | 题量 | 有解答 | 格式 | 来源 |
|---|---|---|---|---|
| numina_math | 35153 | 31427有效 | JSONL | 奥赛proof题 |
| hendrycks_math | 12500 | ✅ | Parquet | MATH数据集Level 1-5 |
| mathnet | 7952 | 6900有解答 | Parquet | 59个国家竞赛题 |
| aops_1224 | 5328 | ✅ | JSONL | AoPS社区2024年题 |
| omni_math | 4428 | ✅ | JSONL | 多源奥赛题（含difficulty 1-9.5） |
| olympiadbench | 675 | ✅ | JSONL | 奥赛benchmark |
| compfiles | 507 | ✅ | Lean | IMO/USAMO形式化题 |
| minif2f | 488 | ✅ | Lean | 形式化竞赛题 |
| fate | 380 | ✅ | JSON | 形式化代数证明（FATE-M/FATE-X） |
| matharena | 356 | ✅ | JSON | 2024-2026竞赛（含hard_problems 43题） |
| amc | 40 | ✅ | JSONL | AMC 2023 |
| aime | 30 | ✅ | JSONL | AIME 2024 |

**未文本化的数据集**（PDF格式，不入库，等文本化后再处理）：
吉米多维奇（5000题）、Demidovich（3000题）、Komjáth（700题）、Engel（300题）、俄罗斯546题、莫斯科MO（300题）、Berkeley（200题）、TaichiLi（1000题）

**无答案的数据集**（不入库）：ConjectureBench（15000题，开放问题）

### 难度分级方案与优先级排序

> **已入库的67837题都有`difficulty_tier`和`priority`字段。Master Agent按`priority`升序派发题目（priority=1最先处理）。**

**5级难度分级**（difficulty_tier，1=最难，5=最易）：

| Tier | 含义 | 题量 | 典型来源 |
|---|---|---|---|
| 1 (最难) | IMO P5/P6, USAMO P5/P6, Putnam, FATE-X, MathArena hard(diff_score>=130) | 452 | compfiles IMO P5/P6, FATE-X, MathArena hard |
| 2 (难) | IMO P3/P4, USA TST, HMMT/CMIMC/SMT最后几题, FATE-M, omni_math difficulty>=7 | 1732 | compfiles IMO P3/P4, numina顶级奥赛, AIME #13-15 |
| 3 (中) | IMO P1/P2, USA P1-P4, olympiadbench, numina olympiads, mathnet proof | 40717 | numina大部分, mathnet proof, olympiadbench |
| 4 (中易) | AIME #1-12, AMC, hendrycks Level 5, aops_1224 | 14260 | hendrycks Level 5, aops_1224, mathnet非proof |
| 5 (易) | hendrycks Level 1-4, mathd_algebra/numbertheory, K12 | 10676 | hendrycks Level 1-4, miniF2F mathd |

**先难后易的派发顺序**：
```python
# Master Agent查询下一批要派发的题（按priority升序=先难后易）
db.aql.execute('''
  FOR p IN problem_extraction_progress
    FILTER p.extraction_status == "pending"
    FILTER p.skip_reason == null
    SORT p.priority ASC
    LIMIT 5
    RETURN p
''')
```

**入库脚本**：`scripts/ingest_problem_extraction_progress.py`——扫描所有文本化数据集，为每道题建立记录含难度分级和优先级。可重复运行（先truncate再import）。

### 关键文档引用

- **279号**：题目侧写系统设计（2-Pass工作流的原始设计）
- **281号**：高Level Hint的工程化（hint字典的Low Level化方法论）
- **287号**：tell端的去特化与规模检索（三层Pipe架构+概念树设计哲学）
- **290号**：第五代系统从前四代继承了什么（29项继承+7项独特贡献）
- **212号**：数学各门类可下载题海清单（数据集目录和ArangoDB math_datasets集合）
- **QA序列定义**：`原语化AI数学工程系统设计/00-基础概念/02-QA序列.md`（QA序列的完整定义和6种情况类型）
- **QA序列canonical案例**：`原语化AI数学工程系统设计/02-案例/01-矩条件极差题第二问.md`（10轮完整QA序列，含每轮的情况类型标注和Level/非特定性值）

### 任务追踪

`任务追踪/06-题海梳理与数据基座建设.md`——记录这条工作线的状态、进度、关键决策。

---

## 管道化GLM-5.2能力边界Profile系统（跨Session连续运行手册）

> **本节是自包含的运行手册。任何AI进入本repo做管道化解题运行时，读完本节即可接手——不依赖Session上下文中的其他内容。**
>
> **本节被AGENTS.md always-on守护。跨压缩边界后，AI加载AGENTS.md时自动看到本节。**
>
> **详细文档**：377号（系统设计）、378号（测试策略）、379号（操作手册）在`Tell分类学研究过程文档/`中。

### 系统目标

在2.4M道竞赛级数学题上构建GLM-5.2的数学能力边界Profile。不是让AI做题，是找能力边界——区分基础设施失败（重试，不计入Profile）和模型能力失败（Profile数据，不重试）。

### 系统架构（4服务+Redis队列）

```
ArangoDB (2.4M题) → Feeder → Redis pending队列
                                ↓
                          Runner (30并发) → 启动devin cli (harness-xxx tmux session)
                                ↓
                          Redis running队列
                                ↓
                          Collector (眼见为实判定终态)
                                ↓
                       Redis completed/failed队列
                                ↓
                          Reporter (统计+告警) + Retry (基础设施失败重试)
```

**代码目录**：`xishujuzhen/solver_harness/pipe/`

**服务清单**：

| 服务 | 脚本 | 职责 |
|---|---|---|
| Feeder | `feeder.py` | 从ArangoDB选题入Redis pending队列 |
| Runner | `runner.py` | 从Redis取题启动devin cli（纯启动，不判定） |
| Collector | `collector.py` | 扫描running队列，眼见为实判定终态 |
| Reporter | `reporter.py` | 定时统计报告+告警 |
| Retry | `retry_infrastructure.py` | 基础设施失败自动重试 |

### 启动流程

```bash
cd ~/master-mind-glm5.2-worktree

# 前置检查
docker ps | grep redis          # Redis容器
curl -s http://localhost:8529/_api/version  # ArangoDB
df -h /data                # D盘空间

# 一键启动30并发
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py start \
  --concurrency 30 --tier 1 --batch-size 100 --clear

# 启动重试服务
tmux new-session -d -s pipe-retry ".venv/bin/python3 xishujuzhen/solver_harness/pipe/retry_infrastructure.py --max-retries 3 --interval 60"
```

### 停止流程（优雅停止，不kill harness session）

```bash
# 优雅停止（默认）——发送SIGINT，等待10秒，不kill harness session
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py stop

# 强制停止
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py stop --force

# 停止同时kill所有harness session
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py stop --kill-harness
```

**解耦保证**：停止任何服务不影响已启动的harness-xxx session。harness session独立运行，Collector重启后从Redis running队列继续处理。

### 并发量实时控制（无需重启Runner）

Runner每次poll时从Redis读取并发配置，可以实时调整，不需要重启：

```bash
# 调整并发数
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py concurrency 50

# 调整poll间隔
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py poll-interval 3

# 查看当前配置（status命令也显示实时配置）
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py status

# 一键健康检查（并发量+网络连接+tmux泄漏+failed分类）
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py health

# 或直接用redis-cli
docker exec redis-queue redis-cli SET math:config:concurrency 50
```

**生效机制**：
- Runner在下次poll时（通常2-5秒内）自动读取Redis中的新值
- **当前running的题不受影响**——只影响后续新启动的题
- 降低并发数：Runner不再启动新题，等running自然结束到低于新并发数后才开始新题
- 升高并发数：Runner立即开始启动更多题填补空槽
- Redis键：`math:config:concurrency`（并发数）、`math:config:poll_interval`（poll间隔秒数）

### 断电恢复流程

```bash
# 检查（不修改）
.venv/bin/python3 xishujuzhen/solver_harness/pipe/recover_from_crash.py --dry-run

# 执行恢复
.venv/bin/python3 xishujuzhen/solver_harness/pipe/recover_from_crash.py

# 恢复后自动重启服务
.venv/bin/python3 xishujuzhen/solver_harness/pipe/recover_from_crash.py --auto-restart
```

恢复做了3件事：
1. running队列中session不存在的记录标记`crash_recovered`，移到failed，problem恢复为pending
2. kill孤儿harness session（tmux有但Redis无记录的）
3. 修复ArangoDB中status=running但实际已结束的attempt

### 代码热替换流程

```bash
# 1. 优雅停止要替换的服务（如Collector）
tmux send-keys -t pipe-collector C-c ""
sleep 5
tmux has-session -t pipe-collector 2>/dev/null && tmux kill-session -t pipe-collector

# 2. 替换代码（编辑collector.py）

# 3. 重启服务
tmux new-session -d -s pipe-collector ".venv/bin/python3 xishujuzhen/solver_harness/pipe/collector.py --poll-interval 10 --timeout 1800 --print-mode"

# 4. Collector从Redis running队列继续处理——harness session一直在运行
```

### 监控检查命令

```bash
# 当前状态
.venv/bin/python3 xishujuzhen/solver_harness/pipe/query_progress.py

# 失败分类统计
.venv/bin/python3 xishujuzhen/solver_harness/pipe/query_failures.py --summary

# 数据完整性验证
.venv/bin/python3 xishujuzhen/solver_harness/pipe/verify_completeness.py --all

# 运行完整性验证（无工具调用+真实proof）
.venv/bin/python3 xishujuzhen/solver_harness/pipe/verify_run_integrity.py --batch

# 双向追溯
.venv/bin/python3 xishujuzhen/solver_harness/pipe/audit_trace.py --all

# Profile构建
.venv/bin/python3 xishujuzhen/solver_harness/pipe/build_profile.py --summary

# 精确解题时间提取
.venv/bin/python3 xishujuzhen/solver_harness/pipe/extract_solve_time.py --batch --update-db

# 日志查看
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/_pipe/logs/pipe.log
```

### 眼见为实验证原则（Collector的核心判定逻辑）

Collector判定终态时，不只看标记，要验证真实内容：

1. **真实thinking检测**：clean_ansi后检查数学内容(math_indicator≥2)和thinking标记
2. **真实proof验证**：PROOF COMPLETE标记 + proof内容≥100字符 + math_indicator≥2（中英文都覆盖）
3. **无工具调用验证**：查sessions.db中是否有tool_call类型节点
4. **AI放弃检测**：检查"I CANNOT SOLVE"/"无法"等放弃标记
5. **pane snapshot保存**：判定终态前保存完整pane内容作为物理证据

### `-p`模式核心认知（2026-08-13修正）

> **`-p`模式是非交互的——devin cli是普通进程，不是TUI应用。** 这个认知是2026-08-13调试并发无法维持问题的核心。

**`-p`模式的输出流向**：
- solver_harness用`tmux pipe-pane`把tmux session的所有stdout写入`tmux_pipe.log`
- pane只是tmux的显示区域（500行scrollback），pipe.log有完整输出
- **pane空≠dead**——devin cli连接API、初始化期间无stdout输出，pane和pipe.log都是0字节，但进程活着
- **判断devin cli死活的正确方法**：pipe.log中有`DEVIN_CLI_EXITED`标记 → 已退出；没有 → 还在运行

**`-p`模式的关键技巧**：solver_harness.py在devin cli命令后加`; echo DEVIN_CLI_EXITED code=$?; sleep 999999`——devin cli退出后echo标记+sleep保持tmux session存活（macOS不支持`sleep infinity`）。

**Collector检测源（2026-08-13修正）**：
- **用pipe.log + pane合并检测**（`detect_text = pipe_text + pane_text`），pipe.log是主要源
- pane只有500行scrollback，rate limit等标记可能滚走；pipe.log有完整输出
- thinking检测仍用pane（spinner是动态内容，pipe.log可能不完整）
- **dead_session用`DEVIN_CLI_EXITED`判断**，不用`pane_is_empty`

**2026-08-13修复的3个collector bug**：

| bug | 根因 | 修复 |
|---|---|---|
| 并发无法维持（running掉到3） | `pane_is_empty`判dead_session，初始化中的session被误杀 | 改用`DEVIN_CLI_EXITED`判断 |
| rate_limited要等30分钟timeout | 只在session结束后检测，但devin cli遇到rate limit时session还活着 | 提前到session运行中检测（3.6步） |
| 基础设施失败阻塞主循环120秒 | rate_limited等失败session也等export，但不会写export | `status not in INFRA_FAILURES`跳过export等待 |

**中文proof检测（2026-08-13修正）**：
- `math_indicators`原全是英文（therefore/hence/let/assume等），中文proof只命中`\frac`一个LaTeX标记，被判定为"无足够数学推理"
- 增加中文标记：因此/故/由/设/令/假设/考虑/可得/方程/边界条件/初始条件/解/满足/代入/控制方程/建立模型/边值问题

### 3秒启动间隔铁律（2026-08-13）

> **runner.py第333行的`time.sleep(3)`是铁律，不可修改。** 详见`.devin/rules/solver-concurrency.md`。

- 每个devin cli启动后固定等3秒再启动下一个
- 这是防止API rate limit的关键——并行启动60个session会导致58/60个遇到rate limit
- 3秒间隔意味着：填满60并发需要180秒（3分钟），填满80并发需要240秒（4分钟）
- **恢复慢是正常的**——collector清理完积压session后，runner按3秒间隔逐步填充，不是bug

### 网络切换/断电健壮性（2026-08-14）

> **系统在网络切换/断电后自动恢复，无需人工干预。** 两层保障：collector自动检测zombie + launchd watchdog守护服务。

**问题根因**：网络切换导致tmux server死亡 → 所有harness-* session和pipe-*服务全部消失。旧collector无法自动恢复zombie——session不存在但pipe.log中无`DEVIN_CLI_EXITED`（devin cli没正常退出），走到"未结束"分支永远不会被清理。

**修复A：collector自动检测zombie（collector.py 6.5步）**：

classify函数新增6.5步`crash_recovered`检测：
- 条件：`not is_running` + pipe.log中无`DEVIN_CLI_EXITED` + `elapsed > 60秒`
- 60秒grace period给网络恢复时间（tmux可能重建）
- `crash_recovered`在`INFRA_FAILURES`集合中，retry服务自动重试
- 不再需要手动跑`recover_from_crash.py`

**修复B：launchd watchdog（pipe_watchdog.sh + com.aurolafly.pipe-watchdog.plist）**：

- **脚本**：`xishujuzhen/solver_harness/pipe/pipe_watchdog.sh`
- **plist**：`~/Library/LaunchAgents/com.aurolafly.pipe-watchdog.plist`
- 每30秒检查5个pipe-*服务（feeder/runner/collector/reporter/retry），死了就重启
- 每5分钟跑`recover_from_crash.py`清理zombie（双重保险）
- `KeepAlive=true`，watchdog自身死了也自动重启
- 开机自启，不依赖终端session
- 日志在`/tmp/pipe-watchdog.log`（launchd进程无D盘写权限，用/tmp）

**验证方法**：
```bash
# 检查watchdog是否运行
launchctl list | grep pipe-watchdog
ps aux | grep pipe_watchdog | grep -v grep
cat /tmp/pipe-watchdog.log | tail -10

# 手动测试：杀掉所有pipe-*服务，30秒内watchdog自动重启
tmux kill-session -t pipe-runner; tmux kill-session -t pipe-collector
sleep 35; tmux list-sessions | grep pipe  # 应该全部恢复
```

**feeder全自动选题（2026-08-14）**：

feeder配置`--tier 1,2,3`，三个tier在同一个AQL查询里。tier=1跑完后自动取tier=2，tier=2跑完后自动取tier=3。auto-restart模式保证feeder退出后5秒重启。**246万题全部自动跑完，不需要人工干预。**

### export落盘保证（`-p`模式 vs 交互模式）

**`-p`模式（当前默认）**：devin cli输出完成后自动退出，退出时写export。collector检测到PROOF COMPLETE后等pane中出现`DEVIN_CLI_EXITED`标记（最多120秒），出现后再等2秒让export写完。export落盘率100%（2026-08-12验证，20/20）。**基础设施失败（rate_limited/failed_connection/dead_session）跳过export等待**——devin cli异常退出不会写export，等120秒纯属浪费时间且阻塞主循环。

**交互模式（`--no-print-mode`）**：devin cli完成后不退出，进入"Ask Devin to build"等待输入。collector用三阶段保证：等Ask Devin出现（120秒）→ 发Ctrl-C → 等export（30秒）。历史落盘率约70-100%，存在export丢失问题。

### stop_tmux审计日志

collector中`stop_tmux(session, reason, exp_id)`记录审计日志：
- **KILL活进程** vs **清理已退出session**——区分两种情况
- 记录终态原因（`终态=candidate_solved/failed_timeout/...`）
- 日志级别：`logger.info`（不是debug），确保生产中可见

### 答案泄漏检测（管道化系统两层）

| 层 | 谁做 | 机制 | 检测点 |
|---|---|---|---|
| **第一层** | Runner（启动前） | 检查题目文本是否包含answer字段值（>10字符）或solution片段 | 启动devin cli前，不启动直接标记`answer_leak_in_input` |
| **第二层** | Solver AI（运行时） | AGENTS.md中Answer Leak Self-Check段要求AI自检 | AI输出`### ANSWER LEAK DETECTED: <描述>` |
| **第三层** | Collector（检测后） | 扫描`ANSWER LEAK DETECTED`标记 | 标记`answer_leak`终态，不重新入队 |

**实测数据**（2026-08-12，676题完成）：
- answer_leak_in_input: 15条（Runner层检测，未启动devin cli）
- answer_leak: 2条（Solver AI自检+Collector检测）
- 答案泄漏的题不重新入队，从pending队列移除

### 失败分类（基础设施 vs 模型能力）

| 类别 | verdict | 处理 | 计入Profile |
|---|---|---|---|
| 基础设施失败 | failed_connection/rate_limited/launch_error/dead_session/crash_recovered | 自动重试 | ❌ |
| 模型能力失败 | failed_token_limit/ai_gave_up/failed_thinking_spin/failed_no_proof/failed_stall/failed_timeout | 不重试 | ✅ |
| 成功 | candidate_solved | - | ✅ |
| 无效 | invalid_tool_use/answer_leak | 不重试 | ❌ |

### 精确解题时间

`solve_time_seconds`从tmux_pipe.log的文件创建/修改时间提取（最可靠——覆盖完整解题过程）。

**数据源优先级**（2026-08-12修正）：
1. **tmux/tmux_pipe.log mtime**（首选）——从tmux session创建到结束持续写入，文件时间覆盖完整解题过程
2. exports/conversation.json的steps时间戳（备选）——注意：devin cli的export可能在session结束时一次性写入，steps时间戳只覆盖部分过程（如8个steps在3秒内完成，但实际解题126秒）
3. sessions_db/trajectory.jsonl的created_at（备选）

**历史误判修复**：2026-08-12发现conversation.json的steps时间戳不覆盖完整解题过程，导致solve_time被低估为2-8秒（实际45-574秒）。已修正优先级为tmux_pipe.log mtime首选，并批量更新了DB中46条历史记录。

时间分解：`launch_overhead + init_overhead + solve_time + tail_overhead + judge_delay`

DB记录字段：`solve_time_seconds`（核心指标）、`solve_time_source`、`prompt_tokens`、`completion_tokens`、`cached_tokens`、`total_steps`

**批量修复历史记录**：
```bash
.venv/bin/python3 xishujuzhen/solver_harness/pipe/extract_solve_time.py --batch --limit 100 --update-db
```

### 答案泄漏检测（answer_leak_in_input）

Runner在入队前检查题目文本是否包含answer/solution字段值，防止AI看到答案。

**检测逻辑**（2026-08-12修正）：
- **answer字段**：只对长度>10字符的答案做检测——短答案如`True`/`False`/`2875`等容易在题目文本中自然出现，导致误判
- **solution_text字段**：检查solution前100字符是否出现在题目文本中

**历史误判修复**：2026-08-12发现answer="False"/"True"/"2875"/"\tau_2"等短答案被误判为answer_leak，因为题目文本中自然包含这些词。已将阈值从>3字符提高到>10字符，4道误判的题已重新入队。

### 日志系统

- **目录**：`/data/math-agent-glm5.2-tmux-agents-trajectory/_pipe/logs/`
- **单文件**：1MB分片
- **总量**：10GB循环滚动
- **文件**：runner.log/collector.log/feeder.log/reporter.log/retry.log + 统一pipe.log

### 系统运行监控SOP（AI检查者角色）

**当系统在运行时，AI是检查者，不是旁观者。** 按以下SOP检查系统健康状态：

**检查1：服务存活**（每次检查必做）
```bash
tmux list-sessions | grep pipe-    # 5个服务session必须都在
.venv/bin/python3 xishujuzhen/solver_harness/pipe/pipe_control.py status
```
- feeder/runner/collector/reporter/retry必须✅运行中
- 如果有❌：检查对应日志，可能是崩溃或优雅退出

**检查2：队列流动**（每次检查必做）
- pending应该在减少，running应该接近并发数，completed+failed应该在增长
- 如果running=0但pending>0：Runner可能挂了，或并发配置被改成0
- 如果completed和failed都不增长超过10分钟：Collector可能挂了，或所有running都在长时间解题

**检查3：失败分类**（每100个失败检查一次）
```bash
PYTHONPATH=xishujuzhen/solver_harness/pipe .venv/bin/python3 -c "
from redis_queue import get_redis
import json
from collections import Counter
r = get_redis()
failed = r.lrange('math:failed', 0, -1)
verdicts = Counter()
for item in failed:
    data = json.loads(item)
    verdicts[data.get('verdict', '?')] += 1
for v, c in verdicts.most_common():
    print(f'  {v}: {c}')
"
```
- 基础设施失败（failed_connection/dead_session/launch_error）占比高→检查API连接
- answer_leak_in_input占比高→检查是否有新的误判模式
- failed_tool_stall占比高→AI在工具调用中卡住，可能需要调整timeout

**检查4：solve_time准确性**（每50个完成检查一次）
```bash
PYTHONPATH=xishujuzhen/solver_harness/pipe .venv/bin/python3 -c "
from redis_queue import get_redis
import json
from collections import Counter
r = get_redis()
completed = r.lrange('math:completed', 0, -1)
sources = Counter()
for item in completed:
    data = json.loads(item)
    sources[data.get('solve_time_source', '?')] += 1
for s, c in sources.most_common():
    print(f'  {s}: {c}')
"
```
- tmux_pipe.log mtime应该是主要source——这是最可靠的
- 如果conversation.json占比高：说明tmux_pipe.log可能不存在，检查trajectory目录结构
- solve_time < 10秒的可疑——可能是conversation.json的steps时间戳不完整

**检查5：误判修复**（发现异常verdict时）
- answer_leak_in_input但answer是短字符串（<10字符）→误判，需要重新入队
- solve_time远小于elapsed→solve_time提取有误，用extract_solve_time --batch --update-db修复
- failed_thinking_spin但pane_snapshot中有PROOF COMPLETE→Collector误判，用reclassify_failed.py修复
- candidate_solved但export中无AI输出的PROOF COMPLETE→提示词误匹配bug，用fix_false_positive_solved.py修复
- 修复后记录到本节"历史误判修复"中

**检查5b：export内容质量验证**（每批次结束时抽查）
- 脚本：`scripts/check_export_vs_db.py`——全量检查export内容质量+与数据库交叉验证
- 检查项：
  1. export文件大小分布（0B/<10KB/正常）——0B或<10KB说明export写入不完整
  2. agent step的reasoning_content长度——0B说明AI没输出任何思考
  3. PROOF COMPLETE真伪——用`find_ai_proof_marker`区分AI输出 vs 提示词中的文本
  4. 交叉验证：DB说candidate_solved的，export中是否有真实PROOF COMPLETE
- 误判率 = DB说solved但export无真实证明的数量 / DB说solved的总数
- 正常误判率应<1%；>5%说明collector匹配逻辑有bug

**历史误判修复记录**：
- 2026-08-12 answer_leak短答案误判：阈值>3改为>10，4道题重新入队
- 2026-08-12 solve_time提取误判：conversation.json优先改为tmux_pipe.log mtime优先，46条DB记录更新
- 2026-08-12 failed_thinking_spin误判：has_real_proof只检查PROOF COMPLETE之前内容，但证明在标记之后。改为同时检查前后+过滤TUI UI元素。11条记录从failed→completed
- 2026-08-12 `-p`模式"秒退"误判：早期发现`-p`模式API响应慢时秒退，禁用`-p`改用交互模式。晚期重新测试发现秒退问题已不存在，`-p`模式输出完成后自动退出+写export（138KB）。切换回`-p`模式，export落盘率从70%提升到100%
- 2026-08-12 `-p`模式tmux session消失：`-p`模式devin cli退出后tmux session自动销毁，collector判定为dead_session。修复：命令后加`; echo DEVIN_CLI_EXITED code=$?; sleep 999999`保持session存活
- 2026-08-12 macOS sleep infinity不支持：`sleep infinity`在macOS上报错（usage: sleep number[unit]），改用`sleep 999999`
- 2026-08-12 提示词PROOF COMPLETE误匹配（重大）：collector的has_real_proof在pane中搜索"PROOF COMPLETE"时，匹配到了提示词"结尾输出 ### PROOF COMPLETE"中的文本，而非AI实际输出的标记。导致272个实际未完成的题被误判为candidate_solved（误判率27.4%）。修复：新增`find_ai_proof_marker`函数检查上下文排除提示词匹配（检查"结尾输出"/"请按AGENTS"/"Pro ·"等提示词特征）。272条DB记录重新分类（252 dead_session + 17 token_limit + 3 stall），272道题重新入队。脚本：`scripts/fix_false_positive_solved.py`，验证脚本：`scripts/check_export_vs_db.py`

**检查6：harness session健康**（每30分钟检查一次）
```bash
tmux list-sessions | grep -c harness-p    # 应该接近并发数
```
- harness session数远大于并发数→有僵尸session，运行recover
- harness session数=0但running>0→Redis running队列和tmux不同步，运行recover

### 数据存储位置

| 数据 | 位置 |
|---|---|
| ArangoDB | `xishujuzhen_math_glm52@localhost:8529` |
| Redis | `redis-queue`容器，6379端口，AOF+RDB持久化到`/data/redis/data` |
| 题目数据 | ArangoDB `math_problems`集合 |
| 运行记录 | ArangoDB `devin_problem_runs`集合 |
| Solver工作目录 | `/data/math-agent-glm5.2-tmux-agents-dir/<exp_id>/` |
| Trajectory数据 | `/data/math-agent-glm5.2-tmux-agents-trajectory/<exp_id>/` |
| 日志 | `/data/math-agent-glm5.2-tmux-agents-trajectory/_pipe/logs/` |

### DB schema关键表（跨系统共享）

| 表 | 用途 |
|---|---|
| `devin_batch_runs` | 批次记录（batch_id, concurrency, status, attempt_keys） |
| `devin_problem_runs` | 单题run记录（status, verdict, observability, paths） |
| `devin_run_events` | 事件流（concurrency_changed, cases_added, answer_leak_detected等） |
| `problem_extraction_progress` | 题库（_key, difficulty_tier, source_dataset, external_ref.local_path） |

### 数据完整性表（跨系统共享）

| 层 | 文件 | 有什么 | 没有什么 |
|---|---|---|---|
| **export** | `<exp_id>/exports/conversation.json` | 最终证明输出（ATIF steps）、system/user消息、metrics（token数） | **thinking内容**；**steps时间戳不覆盖完整解题过程**（export可能一次性写入，用tmux_pipe.log mtime提取solve_time更可靠） |
| **pipe** | `<exp_id>/tmux/tmux_pipe.log` | TUI渲染流（ANSI+braille spinner）、UI行（`Thinking · Xm Ys`）；**文件创建/修改时间=solve_time最可靠来源** | **thinking文本内容** |
| **thinking_capture** | `<exp_id>/tmux/thinking_capture.txt` | **完整thinking文本**（Ctrl+O展开后capture-pane抓取） | 无ANSI清理（raw TUI文本） |
| **sessions.db** | `~/.local/share/devin/cli/sessions.db` | 输入消息（system/user） | **assistant输出和thinking** |

> **thinking落盘机制**：`stop_attempt()`调用前自动调`capture_thinking()`——发Ctrl+O展开thinking，capture-pane抓scrollback 5000行，存到`thinking_capture.txt`。

### 看Solver的4种方法（跨系统通用）

```bash
# 方法1：tmux attach（实时看，Ctrl+B D退出）
tmux attach -t <tmux_session_name>

# 方法2：capture-pane（抓当前屏幕，-S -500抓历史500行）
tmux capture-pane -t <tmux_session_name> -p -S -500

# 方法3：看export文件（最终证明输出，ATIF JSON格式）
cat /data/math-agent-glm5.2-tmux-agents-trajectory/<exp_id>/exports/conversation.json | python3 -m json.tool | head -100

# 方法4：看thinking_capture文件（Ctrl+O展开后的完整thinking文本）
cat /data/math-agent-glm5.2-tmux-agents-trajectory/<exp_id>/tmux/thinking_capture.txt | tail -100
```

### 查询/验证脚本清单

| 脚本 | 用途 |
|---|---|
| `query_progress.py` | 运行进度查询 |
| `query_failures.py` | 失败分类统计 |
| `audit_trace.py` | 双向追溯验证（DB↔文件，题目↔运行） |
| `verify_completeness.py` | 数据完备性验证（remainder=0） |
| `verify_run_integrity.py` | 运行完整性验证（无工具调用+真实proof） |
| `check_answer_leak.py` | 答案泄漏检查 |
| `extract_solve_time.py` | 精确解题时间提取 |
| `build_profile.py` | GLM-5.2能力边界Profile构建 |
| `recover_from_crash.py` | 断电恢复+僵尸清理 |
| `pipe_control.py` | 启动/停止/状态管理/健康检查（status/health/concurrency） |
| `check_export_quality.py` | export文件大小+结构抽样检查 |
| `check_export_vs_db.py` | export内容质量+与数据库交叉验证（PROOF COMPLETE真伪、误判率） |
| `fix_false_positive_solved.py` | 修复collector误判的candidate_solved记录+重新入队 |

### AGENTS.md模板（给devin cli的）

Runner为每个题目生成`AGENTS.md`文件，明确禁止任何工具调用：

```markdown
# 解题任务

你是一个数学解题AI。请直接在TUI中输出证明，不要写任何文件。

## 严格规则
1. 不要使用任何工具（不写文件、不执行命令、不搜索、不浏览）
2. 直接在TUI中用thinking解题
3. 结尾输出 ### PROOF COMPLETE
4. 如果实在做不出来，输出 ### I CANNOT SOLVE THIS

## 题目
{problem_text}
```

### 未覆盖因素（待补充）

1. ~~**export导出完整性验证**~~ — ✅已解决（`-p`模式export落盘率100%，2026-08-12验证）
2. **tmux pane scrollback完整性** — 超长proof可能被截断（2000行上限）
3. **proof数学正确性验证** — 需要审稿AI审查（当前只验证有内容）
4. **跨数据集去重验证** — 近似去重防止重复运行
5. **并发健康度监控** — 实时连接错误率、吞吐量告警

### 运行实测数据（2026-08-12，`-p`模式+40并发）

| 指标 | 数值 |
|---|---|
| 已完成 | 744题（修复误判后真实值） |
| 失败 | 414题（含272道误判修复后重新分类的题） |
| 真实成功率 | 64.2%（修复272条误判前显示91.2%是虚高的） |
| 吞吐量 | ~324题/小时（40并发）/ ~270题/小时（30并发） |
| export落盘率 | 100%（20/20） |
| 数据库字段完整度 | 14/14字段全部100% |
| solve_time可信度 | 100%（20/20） |
| dead_session率 | ~15%（`-p`模式devin cli偶发0字节退出，不随并发量变化） |
| 误判修复历史 | 272条candidate_solved误判（提示词PROOF COMPLETE误匹配），已修复 |

> **注意**：修复前的"91.2%成功率"是虚高的——272个实际未完成的题被误判为已解决。修复后真实成功率64.2%。dead_session（`-p`模式偶发0字节退出）是主要失败原因，占失败的60%+。

### 连续运行SOP

**当你要接手连续运行时，按以下步骤行动**：

1. **检查系统状态**：`pipe_control.py status`看当前pending/running/completed/failed
2. **全面健康检查**：`pipe_control.py health`（7项检查：并发/队列/TUI状态/export落盘/DB字段/solve_time/failed分类）
3. **检查服务是否在运行**：`tmux list-sessions`看pipe-feeder/runner/collector/reporter/retry是否在
4. **如果服务没在运行但有running记录**：执行`recover_from_crash.py`恢复，然后重启服务
5. **如果服务在运行**：检查日志`tail -50 .../pipe.log`看是否有异常
6. **export内容质量验证**：`scripts/check_export_vs_db.py`检查PROOF COMPLETE真伪+误判率（正常<1%）
7. **如果需要热替换代码**：按"代码热替换流程"操作
8. **运行结束后**：执行`build_profile.py --summary`构建Profile，`verify_completeness.py --all`验证数据完整性，`scripts/check_export_vs_db.py`做最终export质量审计

### 关键文档索引

- **377号**：`Tell分类学研究过程文档/377-v0-2026-08-12-管道化解题系统设计-4服务分离+Redis队列.md`——完整系统设计（第8节核心验证原则、第9节未覆盖因素、第10节优雅停止+断电恢复）
- **378号**：`Tell分类学研究过程文档/378-v0-2026-08-12-管道化系统测试策略-数据管理与计算流程完备性.md`——测试策略（DM/CF/E2E/RI/FC/PB/ST/LG/UC测试项）
- **379号**：`Tell分类学研究过程文档/379-v0-2026-08-12-管道化解题系统操作手册.md`——完整操作手册
