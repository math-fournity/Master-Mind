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

### 角色与任务说明——题海梳理工作线

> **本节明确题海梳理工作线中Master Agent和subagent各自做什么。subagent也会看到AGENTS.md，必须知道自己该做什么、不该做什么。**

**Master Agent 的职责**：
1. **找下一个给subagent分析的题目**——从ArangoDB `problem_extraction_progress`中查`extraction_status="pending"`的题，优先选最难的，分配给subagent
2. **为每道题准备工作目录**——用`scripts/prepare_subagent_dir.py`在`subagents-dirs/{problem_id}/`下创建工作目录，生成填充好的checklist.md。派发subagent时告诉它工作目录路径
3. **让整个分析过程持续进行**——始终保持5个subagent在运行（流水线并发），一个完成立刻补一个，不停下来汇报工作，直到所有可处理的题目都处理完
4. **管理并发槽位**——监控5个subagent的状态，完成一个立刻派发下一道题
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

> **Master Agent不只是派发器和入库器，更是审查者和流程改进者。每道题的subagent完成后，Master Agent必须审查其产出质量。每5道题完成后，Master Agent必须做一次批量审查。审查中发现的任何问题——从数据库表设计到checklist.md到AGENTS.md——必须立即修正，让后续的subagent受益。**

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

#### 检查点1：每道subagent完成后——快速质量审查（必须执行）

subagent汇报后、派发下一道题之前，Master Agent必须对刚完成的profile做以下检查：

**1a. QA序列合理性**：
- QA序列是否反映了一个真实的"引导AI从题目走到解答"的过程？还是机械地走形式？
- 第1轮是否是`纯元认知观察`（让AI描述题目结构）？第2轮是否是`自由列举`？如果不是，为什么？
- situation_type值是否是6个规范值之一？（如果不是→subagent违反了checklist约束→需要修正数据+检查checklist是否不够明确）
- hint_level是否是0-1浮点数？（如果不是→同上）
- QA轮数是否在5-8轮之间？过少可能分析不充分，过多可能冗余

**1b. 拓扑标注质量**：
- profile级tell_topology的三个维度值是否在已有拓扑分类体系中？（如果新建了值→检查粒度是否一致）
- per-pair tell_topology是否逐pair不同？（如果所有pair用同一个拓扑→分析太粗糙，per-pair拓扑是Pipe 0/1检索的依据）
- is_knowledge_bottleneck=True的pair，gap_type是否是`knowledge_gap`？（如果不是→标注不一致）

**1c. (tell, hint)对质量**：
- tell是否描述了AI在这个位置的具体状态/分叉信号？还是泛泛而谈？（泛泛而谈→质量不合格）
- hint是否是具体的提示方向？还是"继续努力"之类的废话？
- 全局(tell, hint)对中implicit型的why_not_visible_locally是否真的解释了为什么在局部不可见？
- bare_ai_error_prediction是否具体描述了bare AI会犯什么错？还是只说"会失败"？

**1d. solution_method_type vs problem_type**：
- 两者是否明确区分？problem_type是题目结构类型，solution_method_type是解答方法类型。如果两者相同或混淆→分析不到位

**审查结果处理**：
- **合格**：继续派发下一道题
- **小问题**（situation_type/hint_level格式错误等）：用脚本批量修正，继续派发，在checklist-template.md中强化对应约束
- **大问题**（QA序列不合理、tell/hint泛泛而谈、拓扑标注严重错误等）：记录问题，将该题标记为需要重新分析（progress状态改回pending），继续派发下一道题

#### 检查点2：每5道题完成后——批量审查（必须执行）

每完成5道题（不是每5个subagent完成，是累计5道题入库），Master Agent必须做一次更深的审查：

**2a. 跨profile一致性检查**：
- 所有profile的拓扑值是否粒度一致？（运行AQL查询所有unique的problem_type/ai_method_type/gap_type值，检查是否有太具体或太抽象的异常值）
- solution_method_type是否有重复模式？（如多道题都用"telescoping"，说明这是一个高频思维模式）
- thinking_patterns是否有高频值？

**2b. Schema/Checklist/流程改进评估**：
- 过去5道题中，subagent是否在某些步骤反复出错？（如situation_type反复自创→checklist约束不够强）
- 过去5道题中，是否发现了Schema中缺失的字段或类别？
- 过去5道题中，拓扑分类体系是否需要进化？（subagent的进化建议是否指向同一个方向？）
- checklist-template.md是否需要更新？（某个步骤的说明是否不够清楚导致subagent反复出错？）
- AGENTS.md中的SOP是否需要更新？（某个流程环节是否不合理？）

**2c. 数据库设计评估**：
- 字段是否够用？是否有有价值的信息无处记录？
- 索引是否合理？查询是否高效？
- 是否需要新增集合或字段？

**2d. 亲自重新分析一道题**：
- 从过去5道题中选一道，Master Agent亲自重新分析（不委托subagent）
- 对比Master Agent的分析和subagent的分析，找出差异
- 差异如果是subagent遗漏了什么→在checklist中强化对应步骤
- 差异如果是Master Agent也遗漏了什么→说明Schema/SOP有盲区，需要修正

**审查结果处理**：
- 发现问题→**立即修正**（更新AGENTS.md/checklist-template.md/Schema），让后续的subagent受益
- 修正后commit，记录变更原因
- 如果问题严重到需要重新分析已完成的题→记录待重做列表，Pass 2时处理

#### 检查点3：每20道题完成后——全局审查（必须执行）

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

**最大并发数**：5个subagent同时运行。

**流水线并发，不是批处理并发**：
- ❌ 错误做法：启动5个subagent，等5个都结束了再启动下一组5个——这浪费并发槽位（快的subagent结束后空等慢的）
- ✅ 正确做法：始终保持5个subagent在运行。一个subagent完成了一道题，立刻启动下一个subagent处理下一道题，补满5个槽位。这是流水线并发——任何时刻都有5个槽位在被使用。

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
- 管理并发槽位——始终保持5个subagent在运行
- 监控subagent状态——完成一个立刻补一个
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
