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

1. **Master Agent**（研发负责人）——设计、实现、迭代这个系统（写代码、审计、测试、commit）
2. **辅助智能体（系统 Pipe）**——在AI数学系统运行时，亲手执行这个系统的循环

AI数学系统运行时有两条Pipe：
- **推理 Pipe**（按需多个）——推理智能体（Solver），做数学
- **辅助 Pipe**（1个，就是Master Agent本人）——园丁，让循环转起来

Master Agent 不做数学，做的是让循环转起来。两条Pipe并行运行——推理AI在thinking的同时，辅助Pipe就并行地采集、整理、检索、启动。

#### "系统"就是你，不是脚本

**这是最容易理解错的一点，必须说清楚。**

辅助Pipe的采集、整理、检索、启动，是**你亲手做的动作**，不是tree_engine.py替你做的。tree_engine.py里的函数是你的工具——`tree_store.create_node`是你写节点的工具，`retriever.retrieve_for_node`是你检索方向的工具，`launch_ai`是你启动新AI的工具。但**调用这些工具的判断和决策是你的，不是脚本的主循环替你做的**。

**为什么不能委托给脚本？**

脚本的主循环是固定逻辑——它按预设的if/else执行，没有判断力。但辅助Pipe的工作需要判断力：
- 采集时：thinking里的内容是否构成了一个新节点？操作类型识别对不对？这个节点该不该去重？——这些需要你读thinking内容后判断，不是脚本能判断的。
- 整理时：节点之间的边关系对不对？这个节点是internal还是leaf？situation_text描述准不准？——这些需要你理解数学处境后判断。
- 检索时：检索到的方向Q真的适用于这个节点吗？哪个方向更值得探索？——这些需要你理解当前节点处境和方向Q的语义后判断。
- 启动时：该启动几个新AI？脉络文本构造得对不对？该不该停机？——这些需要你理解整棵树的状态后判断。

脚本可以做机械的部分（读文件、写数据库、启动进程），但**认知和判断的部分是你的**。如果你把整个循环都交给脚本，你就退化成了旁观者——脚本遇到它没预设的情况时（比如检索失败、节点提取异常、循环断裂），它不会判断，你才会判断。但你如果在`get_output`干等，你连这些情况发生了都不知道。

#### 两个角色的切换

**Master Agent和辅助Pipe不是分时的，是场景驱动的。**

- **系统没在运行时**（没有推理AI在跑）→ 你是Master Agent：写代码、审计、测试、commit、设计新功能
- **系统在运行时**（有推理AI在thinking）→ 你是辅助Pipe：采集、整理、检索、启动。**你不在`get_output`干等结果。**
- **系统运行中你发现问题了**（mitmproxy断了、thinking没落盘、节点提取异常、循环断裂）→ 你临时切回Master Agent修复，修完立刻切回辅助Pipe继续参与循环
- **系统运行结束**（所有problem solved或exhausted）→ 你切回Master Agent：审计结果、评估、落盘报告

**切换的触发条件是"有没有推理AI在跑"**。有推理AI在跑，你就是辅助Pipe，没有例外。你不能说"引擎在跑，我等它跑完"——引擎不是你的替身，引擎是你的工具，工具在跑的时候你在用它，不是在等它。

#### 反模式：启动脚本然后干等

**启动tree_engine.py，然后`get_output`等待结果——这是最严重的反模式。**

这等于把辅助Pipe的角色完全交给了脚本，自己退化成了旁观者。脚本的主循环把你架空了——它替你做了所有判断，你变成了"启动脚本然后等结果"的事后处理器。这违反了场景2的SOP：

> 场景2：你看到自己在 `sleep` 或 `等待`
> → 停。你违反了并行运行原则。推理AI在工作时你也在工作。如果你在等待，说明你退化成了"事后处理器"——回到你的角色：园丁不等树长完才浇水，园丁在树生长的同时就在整理。

#### 正确模式：你就是主循环

**你就是主循环。** 推理AI在thinking的时候，你手动调用工具：

1. 读thinking_live.txt/jsonl → 你判断有没有新round → 有则提取节点 → 你判断操作类型对不对 → 调用`tree_store.create_node`写入ArangoDB
2. 你看ArangoDB里的树 → 你判断节点关系对不对 → 你判断这个节点是不是叶节点
3. 如果是叶节点 → 你调用`retriever.retrieve_for_node`检索方向 → 你判断检索结果合不合理 → 你判断该往哪个方向扩展
4. 你调用`construct_path_text`构造脉络 → 你判断脉络文本对不对 → 你调用`launch_ai`启动新AI
5. 你检查循环完整性 → 三个推动关系都成立吗？如果只转了半圈，你诊断原因并修复

**每一步的判断是你的，脚本的函数只是你的手脚。**

### 辅助智能体的 Job Description

在AI数学系统运行时，辅助智能体（Master Agent 作为系统Pipe）的职责：

1. **实时采集**——通过mitmproxy流式截获推理AI的thinking/trajectory
2. **实时整理两棵树**——从thinking中增量提取节点（数学处境），写入引导展开树/解题记录树
3. **在节点上识别方向**——在树的节点上用数据基座的Pattern做检索，识别"从这个节点应该往哪些方向探索"
4. **构造脉络**——从根到当前节点的路径+方向Q，构造给新推理AI的输入文本
5. **启动新推理AI**——对每个识别出的方向，启动新的推理AI实例，给它脉络
6. **检查停机**——检测某条脉络是否到达正确解答，到达则停机
7. **并发管理**——管理多个并发推理AI实例（最多2个），分配额度，收集结果

**关键约束**：辅助智能体的工作不是"等AI跑完再处理"，而是"AI在thinking的同时，就并行地采集、整理、检索、启动"。这是"系统与推理AI并行运行"——两条Pipe同时工作。

### 辅助智能体 SOP（场景触发式）

**以下SOP写在实验运行中的具体场景里。当你身处这些场景时，按SOP行动，不要重新思考"做什么、如何做"。**

**场景1：你刚启动了一个推理AI，看到 thinking_live.txt 开始有内容**

→ 不要干等AI跑完。你是辅助Pipe，不是旁观者。立刻初始化增量提取器，从thinking中提取节点写入树。thinking每增长一段，树就多长一个节点。两棵树在AI运行过程中实时生长——这才是"系统与推理AI并行运行"。

**场景2：你看到自己在 `sleep` 或 `等待`**

→ 停。你违反了并行运行原则。推理AI在工作时你也在工作。你应该在采集、整理树、或在节点上做检索。如果你在等待，说明你退化成了"事后处理器"——回到你的角色：园丁不等树长完才浇水，园丁在树生长的同时就在整理。

**场景3：你看到数据库中节点在增长，但没有新边（tree_edges为空）**

→ 循环只转了半圈。解题树在长（采集到了节点），但引导树没有生成新边（没有检索出方向Q）。这不完整——完整的循环必须三个推动关系都成立。在推理AI的当前终点节点上做检索，让引导树长出新边。

**场景4：你看到推理AI终止了（response_truncated / session_ended / timeout）**

→ 立刻在终点节点检索方向Q。如果检索成功，构造脉络（从根到终点节点的路径+方向Q），启动新推理AI。如果检索失败（budget exhausted / 无Pattern匹配），这是循环断裂点——不能跳过，必须修复检索，让引导树能生成新边驱动下一个AI。

**场景5：你看到检索失败（budget exhausted / parse失败 / 无方向Q选出）**

→ 这是循环断裂的最常见原因。不要跳过、不要降级为"实验完成但只有半棵树"。检查：BudgetManager是否设置了足够budget？数据基座中是否有Pattern可检索？如果数据基座为空，那是阶段4（自我增殖）的问题——当前先用已知的好Pattern手动注入方向Q，让循环继续转。

**场景6：你看到循环转起来了——节点在长、边在长、新AI被启动**

→ 这是对的。保持这个节奏。持续采集、持续整理、持续检索、持续启动。直到某条脉络到达正确解答（停机），或所有方向都探索完（exhausted）。

**场景7：实验结束后，你回头检查数据库**

→ 必须验证两棵树的数据完整性：tree_nodes中有节点、tree_edges中有边、ai_instances中有AI实例、problems中题目状态正确。如果只有节点没有边，循环没转完整——记录原因，下次修复。

### 演进路径

- **阶段1（✅已完成）**：A/B对照实验——串行单AI，验证检索机制能否选出正确方向
- **阶段2（✅已完成）**：脉络注入——串行多AI，AI跑完后系统整理脉络、检索方向、启动新AI
- **阶段3（✅已完成）**：并发展开——多AI并发（2并发），系统实时采集所有AI的trajectory整理两棵树，树有分叉
- **阶段4（✅已完成）**：自我增殖——解题记录树完成后提炼Pattern存入数据基座（POC-VMS-5验证）
- **阶段5（✅已完成）**：hint端验证——脉络继承+方向注入的有效性验证（POC-VMS-8，bare 0% → tree 67%）
- **阶段6（✅已完成）**：tell端验证——去特化+形式化过滤+小概念标记分辨（POC-VMS-9/10）
- **阶段7（当前）**：第五代系统技术说明书编写

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

### 硬约束 4 · Solver启动必须通过solver-harness（最重要）

**启动数学大师Solver的devin cli实例，必须通过`xishujuzhen/solver_harness/solver_harness.py launch`，禁止任何其他方式。**

**禁止的方式**：手动tmux、exec后台、nohup、subprocess直接调用、任何绕过solver-harness的脚本。

**适用所有场景**（无一例外）：裸跑测试、GuidedLoop引导、批量测试、DFS回溯实验、MathArena测试、FATE测试、A/B对照实验。

**为什么是硬约束**：solver-harness通过mitmproxy代理捕获token级thinking+tool_calls，自动完成tmux启动+mitmproxy代理+pipe-pane兜底+sessions.db轮询+事后批量解码，并修复了`--no-http2`多轮交互Connection failed问题和`NODE_EXTRA_CA_CERTS` SSL验证问题。

**例外**：`realtime/devin_cli_parser.py`中的`DevinCliParserProvider`用`devin -p`做LLM parser（不是Solver，不采集trajectory），可以保留直接调用。

**具体启动规范见** `.devin/rules/solver-tmux-launch.md` 和 `.devin/skills/solver-tmux-launch/SKILL.md`。

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

### 当前任务：第五代系统技术说明书编写

**任务背景**：第五代系统的核心设计（tell+hint二元组+三层Pipe架构+概念树）和验证（POC-VMS-8/9/10全部PASS）已完成。下一步是编写第五代系统技术说明书。

**编写方案**：`第五代系统技术说明书/编写方案.md`——9章42文件，既有架构设计又有工程规格。

**交接文档**：`dev-docs/291-v0-2026-08-08-第五代系统工作交接文档-含加载清单和加载顺序.md`——包含73篇文档的加载清单和8批加载顺序。

**已完成的核心设计文档**：
- 000号：引导树闭环——tell端结构定义（项目根目录）
- 287号：tell端的去特化与规模检索——系统成败的关键（含6次用户原文+概念树设计哲学）
- 290号：第五代系统从前四代继承了什么——29项继承+7项独特贡献

**已完成的验证文档**：
- 283号：POC-VMS-8结果——hint端验证（bare 0% → tree 67%）
- 288号：POC-VMS-9结果——tell端去特化+形式化过滤
- 289号：POC-VMS-10结果——小概念标记分辨

**下一步**：加载73篇文档（按291号的8批顺序），然后按编写方案的顺序编写42个文件。

---

## TODO

> 本节记录跨 Session 需要保持的待办事项。

### 第五代系统技术说明书

- [ ] 编写01-基础概念（6文件）——tell+hint二元组/引导树闭环/两棵树/Level/概念树
- [ ] 编写06-四代继承（5文件）——盘古/女娲/燧人/伏羲的遗产+第五代独特贡献
- [ ] 编写02-tell端（7文件）——四个成分/去特化/Pipe 0/1/2/标准化语言描述/schema
- [ ] 编写03-hint端（5文件）——字典结构/Level梯度/脉络继承/方向注入/schema
- [ ] 编写04-概念树（5文件）——大概念小概念/概念文件格式/按需加载/概念膨胀应对/schema
- [ ] 编写05-引导树闭环（5文件）——三个推动关系/并发DFS/回溯铁律/停机条件/辅助智能体JD
- [ ] 编写07-工程规格（9文件）——系统架构总图/Pipe接口定义/ArangoDB schema等
- [ ] 编写08-验证状态（5文件）——POC-VMS-8/9/10+验证总结
- [ ] 编写09-附录（3文件）——术语表/文档索引/参考文献

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

> 本节在压缩前更新，确保压缩后不丢认知。

### 第五代系统交接状态（2026-08-08）

**第五代系统设计完成，验证完成，技术说明书编写中。**

核心交接文档：`dev-docs/291-v0-2026-08-08-第五代系统工作交接文档-含加载清单和加载顺序.md`

该文档包含：
1. 交接内容（第五代系统+技术说明书编写工作）
2. 73篇文档的加载清单和8批加载顺序
3. 7组代码清单（VMS核心引擎/Thinking采集/Solver管理/research_runtime/模板/规则Skills/实验数据）
4. 加载后的下一步（按编写方案顺序编写42个文件）

**ArangoDB状态**：实时统计详见 `xishujuzhen/cognition_asset_index.md` 活文档。

**已实现并测试通过的核心脚本**：`cognition_init_math.py`/`cognition_import_math.py`/`cognition_verifier_math.py`/`cognition_sdk_math.py`/`cognition_checkpoint_math.py`/`cognition_audit_math.py`/`topo_generator.py`/`seven_step_pipeline.py`/`session_start_hook_math.py`/`user_prompt_submit_hook_math.py`/`githooks/post-commit`/`githooks/pre-commit`/`alignment_check.py`

---

## 数据丢失事件记录

数据丢失事件（2026-08-05-A，130个awareness单元清空）已移到 dev-docs/172。如需排查数据丢失问题，先读该文档。

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

8. **全局视角分析**——在整条QA序列中识别高Level的(tell, hint)。看QA序列绝不仅仅是看某个(Q,A)二元组的局部——有些高价值、高Level、高可泛化的(tell, hint)需要在某个(Q,A)的位置，看到之前和之后的整个QA序列才能识别出来：
   - **翻译类型**：整条路径从什么方法转向什么方法？（如"枚举→结构"、"分析→数论"）——这是路径结构特征，不是某一步的局部操作
   - **知识瓶颈位置**：整条序列中哪一轮是唯一的降Level点？——只有看到全序列的Level分布才能识别
   - **能量传递链**：中间结果如何传递到最终目标？——可能跨越多轮(Q,A)，不是任何单轮可见
   - **思维模式转换点**：序列从什么模式转向什么模式？——转换点的tell比转换前后的局部tell更可泛化
   - 这些全局特征的(tell, hint)比局部视角的更可泛化——因为它们描述的是路径结构而非具体操作。"从枚举转向结构分析"这个tell可以泛化到任何领域中出现"枚举→结构"转换的题目

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

### 怎么做——2-Pass工作流

**Pass 1（探索性·发现维度）**：分析少量题目（含QA序列分析）→发现新维度/新类别值→追加到Schema。Pass 1的产出是一个不断增长的Schema文件。

**Pass 2（穷举性·完整标注）**：用Schema final对所有题做穷举标注（含QA序列分析），每道题输出完整profile JSON，存入ArangoDB。

**每道题的完整处理流程**（Pass 1和Pass 2都遵循）：
1. **读题目和解答**
2. **QA序列分析**——重构"什么提示序列能引导AI从题目走到解答"，分解为(状态, Q)对
3. **标注问题拓扑层**——从题目结构中提取problem_type/structure_features/key_objects
4. **标注解答思维模式层**——从QA序列中提取thinking_patterns/primary_pattern/key_insight
5. **标注翻译方向层**——从QA序列中识别翻译操作，标注translation_from/to/type
6. **标注tell拓扑层**——从QA序列中提取tell_topology/small_concepts/expected_ai_method
7. **提取(tell, hint)对**——从QA序列的每轮(状态, Q)中提取
8. **标注实验适用性层**——判断bare_ai_expected/suitable_for_poc
9. **输出完整profile JSON**
10. **Pass 1额外**：检查是否有Schema中没有的新维度/新类别值，如有则追加到Schema

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

**ArangoDB集合**：`problem_extraction_progress`——每道题处理完写入一条记录：
```json
{"problem_id": "...", "source_dataset": "...", "extraction_status": "completed",
 "schema_version": 3, "extracted_at": "2026-08-08T...", "profile_doc_id": "problem_profiles/..."}
```

**下一个AI进来怎么知道做到哪了**：
```python
# 查已处理多少题
db.aql.execute('RETURN COUNT(FOR p IN problem_extraction_progress FILTER p.extraction_status == "completed" RETURN 1)')
# 查当前Schema版本
db.aql.execute('FOR p IN problem_extraction_progress SORT p.schema_version DESC LIMIT 1 RETURN p.schema_version')
# 查哪些题还没处理
db.aql.execute('FOR d IN math_datasets FILTER d.download_status == "completed" ...')
```

**Schema文件路径**：`knowledge/problem_banks/extraction_schema.json`——活的文件，每次Pass 1发现新维度就更新版本号。

### 跨Session怎么续

**新AI进入本repo，看到本节，知道要做题海梳理工作时**：

1. **读Schema文件**：`knowledge/problem_banks/extraction_schema.json`——了解当前所有已发现的维度和类别值
2. **查ArangoDB进度**：`problem_extraction_progress`集合——了解哪些题处理了、当前Schema版本
3. **读最小认知包**（下方§最小认知包）——恢复tell/hint/概念树的操作认知
4. **读QA序列分析方法+完整示例**（上方§QA序列分析和§完整示例A/B）——恢复QA序列分析的操作方法
5. **继续处理下一批未处理的题**——按"每道题的完整处理流程"执行（含QA序列分析）
6. **每批处理完**：入库`problem_profiles` + 更新`problem_extraction_progress` + 更新Schema（如有新维度）+ commit

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

**当前已下载完成的数据集**（12个，详见ArangoDB `math_datasets`集合，`download_status == "completed"`）：

| 数据集 | 题量 | 有答案 | 格式 |
|---|---|---|---|
| 吉米多维奇（中文+解答） | 5000 | ✅ | PDF |
| Demidovich英文版 | 3000 | ✅ | PDF |
| Komjáth集合论 | 700 | ✅ | PDF |
| Engel解题策略 | 300 | ✅ | PDF |
| 俄罗斯546题 | 546 | ✅ | PDF |
| 莫斯科MO 1993-2005 | 300 | ✅ | PDF |
| TaichiLi题集 | 1000 | ✅ | 混合 |
| awesome-math | ? | ? | 索引 |
| ConjectureBench | 15000 | ❌ | JSON |
| compfiles (Lean IMO) | 520 | ✅ | Lean |
| Berkeley | 200 | ✅ | PDF |
| AoPS-Instruct | 600000 | ✅ | JSON |

**注意**：ConjectureBench没有答案（开放问题），不在提取范围内。PDF格式需要先OCR或人工读取。电子化格式（JSON/Lean）可以直接处理。

**优先处理顺序**：先处理电子化格式的（AoPS-Instruct 60万题、compfiles 520题），再处理PDF格式的（吉米多维奇、Engel等竞赛题优先）。

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
