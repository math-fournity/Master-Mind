# 项目 AGENTS.md · Grove — Parallel Guided Tree Growth Engine

> **⚠️ 本文件顶部「Grove 独立 repo 认知」章节是本 repo 专属内容。下游 `## 项目定位` 起的内容继承自上游 D repo（`/data/master-mind/`），属于项目方法论本体，与本 repo 的隔离规则无关。**
> **未来 AI 进入本 repo 时，必须先读完本章节再做事。**

---

## 角色说明 · 你当前是什么 AI

本 AGENTS.md 可能被多种 AI 加载，进入本 repo 时请先确认自己的角色：

| 角色 | 工作目录 | 职责 | 看到本 AGENTS.md 时该做什么 |
|---|---|---|---|
| **Grove AI** | `/data/master-mind-glm5.2-grove/` | 实现、迭代 Grove 树生长引擎 | 遵守本 AGENTS.md 全部约束，执行工作 |
| **Subagent** | 由 Grove AI 通过 Devin CLI/tmux 启动 | 执行被分配的子任务 | 只执行分配的任务，不承担 Grove AI 的全部责任；若不确定就问 Grove AI |

**关键区分**：
- Grove AI 负责**做工作**（写代码、审计、测试、commit）
- Subagent 负责**完成 Grove AI 分配给它的具体任务**，然后回去汇报

**如果你是 subagent**：
- 你看到的是 Grove AI 的 AGENTS.md，因为 Devin CLI 启动 subagent 时会加载项目 AGENTS.md
- 但你不等于 Grove AI，不需要承担 Grove AI 的长期工作系统迭代责任
- 你的任务是：完成 Grove AI 通过 tmux/Devin CLI 交给你的具体任务
- 任务完成后，把成果汇报给 Grove AI

---

## Grove 独立 repo 认知（最高优先级）

### 本 repo 是什么

本目录 `/data/master-mind-glm5.2-grove/` 是 **Grove — Parallel Guided Tree Growth Engine** 的独立工作 repo。

**Grove 命名含义**：
- **Grove** = 小树林——多个推理AI并发探索，每个AI的探索贡献一棵树，多棵树并发形成树林
- 系统是这片树林的**园丁**——采集trajectory、整理两棵树、在节点上识别方向、启动新AI给脉络
- 和两棵树的概念自然呼应——引导展开树（生长中）和解题记录树（完成态）都在这片grove中
- 全称：**Grove — Parallel Guided Tree Growth Engine**

### 本 repo 的来历（2026-08-08）

1. **上游 repo**：`/data/master-mind/` —— 数学大师制造项目的原始 repo，另一个AI在其中活跃工作
2. **中间 repo（已废弃）**：`~/master-mind-glm5.2-worktree/` —— 之前从上游 clone 的独立工作目录，GLM-5.2 曾在此工作。因和另一个AI共享同一台机器存在协调负担，已废弃
3. **本 repo（Grove）**：`/data/master-mind-glm5.2-grove/` —— 从中间 repo 完整复制而来，是 Grove 任务主线的独立工作 repo。从此之后，本 repo 由 Grove AI 单独使用

**交接文档**：`dev-docs/268-v0-2026-08-08-04工作线交接文档.md` —— 新 Session 的 Grove AI 必须全文加载此文档，恢复 04 工作线（端到端效果验证→树生长引擎）的完整工作意识。

### ⚠️ 绝对禁止碰的路径

**以下路径是其他AI的工作目录，绝对不要以任何方式读取、写入、执行命令：**

- ❌ `~/master-mind-glm5.2-worktree/` —— 旧的工作目录，已废弃，但文件还在
- ❌ `/data/master-mind/` —— 上游 repo，另一个AI的活跃工作目录

**所有文件读写、代码改动、文档落盘、构建产物，只能在 `/data/master-mind-glm5.2-grove/` 内。**

误触碰上述路径 → 立即停止，告知用户。不要自行回滚——那可能破坏另一个AI的未提交工作。

### 硬约束 1 · 文件操作边界

**所有文件读写、代码改动、文档落盘、构建产物，只能在 `/data/master-mind-glm5.2-grove/` 内。**

- **禁止**以任何方式写入 `/data/master-mind/`（上游 repo）或 `~/master-mind-glm5.2-worktree/`（旧工作目录）。
- **禁止**在上述路径内执行 `git`、`python`、`arangodb` 等任何会改动文件的命令。
- 读取上游 repo 用于参考是可以的，但写只能写本 repo。
- 误写入禁止路径 → 立即停止，告知用户，由用户决定如何处理。

### 硬约束 2 · Git 规则

1. **只在 `glm5.2` 分支上工作**。不要 commit 到本地 `main`。
2. **显式路径 add**：禁止 `git add -A`/`git add .`/`git add -u`，只 add 具体路径。
3. **改前清干净 + 改后立即 commit**：遵守全局 Git 管理协议。
4. **不 push 到上游**：本 repo 是独立工作 repo，不需要和上游同步。如需同步，必须经用户当轮明确授权。

### 硬约束 3 · 数据库隔离

**本 repo 与上游 repo 共享同一台机器上的同一个 ArangoDB 实例（`localhost:8529`）。如果不做数据库隔离，两个 AI 的研究数据会互相覆盖、互相污染——这是最危险的隐性冲突。**

**本 repo 专用数据库名**：`grove_math`（通过 `.env` 文件覆盖 `ARANGO_DB` 环境变量实现隔离）

**数据库隔离硬规则**：
1. **本 repo 启动任何会连 ArangoDB 的脚本/服务前**，必须确认 `ARANGO_DB` 环境变量已设为 `grove_math`。
2. **禁止**以 `xishujuzhen_math`（上游数据库名）连接 ArangoDB 做任何写操作。读可以（用于对比/迁移），但写绝对禁止。
3. **本 repo 首次初始化数据库时**，用 `arangodb_init.py`（环境变量化后）创建 `grove_math`，不要复用上游的 `xishujuzhen_math`。
4. **运行 POC、研究 runtime、事件存储、启发规则存储**等所有会写库的代码前，先核对环境变量。
5. **每次运行前必须确认 `echo $ARANGO_DB` 输出 `grove_math`**。若忘了 source `.env`，脚本会 fallback 到默认值 `xishujuzhen_math`（上游数据库）。

### 硬约束 4 · 其他共享资源意识

- **ArangoDB 实例** `localhost:8529`：共享，通过 DB_NAME 隔离（见上）。
- **网络端口**：如果本 repo 要起服务（如 ArangoDB Web、自定义 HTTP 服务），注意端口不要和上游冲突。起服务前先 `lsof -i :<port>` 检查。
- **Python 环境**：本 repo 用独立 venv（`.venv/`，python3.14 + python-arango 8.3.3，被 gitignore）。
- **mitmproxy** `localhost:18889`：launchd 系统服务，两AI共享，通过 workdir_mapping 区分。
- **Solver工作目录**：`/data/grove-agents-dir/`（Grove专用，上游用 `/data/math-agent-{1,2}/`）
- **Trajectory存储**：`/data/grove-agents-trajectory/`（Grove专用）
- **Parser工作目录**：`/data/grove-parser-{1,2,3}/`（Grove专用）

### 硬约束 4.5 · 隔离意识（元组：isolation-awareness + isolation-audit）

**隔离不是一次性工程，而是持续 vigilance。** 每次使用新的共享资源、修改路径常量、创建子进程工作目录时，必须过隔离检查清单。

- **Rule**：`.devin/rules/isolation-awareness.md`——always-on触发，列出隔离层次和触发条件
- **Skill**：`.devin/skills/isolation-audit/SKILL.md`——按需加载的8步审计工作流
- **经验文档**：`dev-docs/269-v0-2026-08-08-共享机器多AI隔离经验与持续维护清单.md`——完整隔离经验、检查清单、演进历史

**隔离黄金法则**：两个AI的任何资源标识（库名、目录名、session名、端口）都应**完全不同前缀**，不能只靠后缀区分。

### 硬约束 5 · Solver 工作目录隔离

**数学大师 Solver 的 devin cli 实例必须在外部目录运行，不能在本 repo 内运行。**

原因：本 repo 的 AGENTS.md 包含工作系统规则（CP1-CP3、认知种子、七步骤pipeline等），如果 Solver 在本 repo 内运行 devin cli，这些规则会劫持 Solver 的行为——Solver 不做数学，而是去加载认知种子。这在 run_20260806_guided_001/002 中已验证发生。

#### 当前模式 · tmux-agents-dir（2026-08-07起）

**每个实验在 `/data/grove-agents-dir/` 下有独立的工作目录，运行后保留全部记录（AGENTS.md、problem.txt、proof、exports、tmux_pipe.log等）。**

**目录命名规范**：`<dev-docs编号>-<实验名>`，例如：
- `255-poc-1` —— 255号POC系列的第1个POC
- `255-poc-2` —— 255号POC系列的第2个POC
- `guided-006` —— guided系列第6次实验

**每个实验目录的结构**（自包含，运行后保留）：
```
/data/grove-agents-dir/<experiment-id>/
├── AGENTS.md              # Solver角色定义（从templates/solver_agents_md.md复制，可定制）
├── .devin/                # devin cli本地配置（config.local.json等）
├── problem.txt            # 题目文件（运行前写入，运行后保留）
├── hint.txt               # 提示文件（多轮引导时写入，运行后保留）
├── proof*.md              # AI写的证明草稿（运行后保留）
├── exports/               # --export导出的对话JSON（运行后保留）
│   └── session_*.json
├── tmux_pipe.log          # pipe-pane兜底记录（运行后保留）
├── dfs_tree.json          # DFS树状态（guided模式，运行后保留）
└── session_info.json      # session元信息（run_id/session_name/model/start_timestamp等）
```

**AGENTS.md模板**：`templates/solver_agents_md.md`（本repo内，git-tracked）。每个新实验目录创建时从此模板复制。不同实验可定制AGENTS.md（如POC-6需要AI-B角色定义，与标准Solver不同）。

**DevinCliAdapter**（`runtime/devin_cli_adapter.py`）的 `work_dir` 参数指向实验目录。run的导出文件同时写入实验目录的 `exports/` 子目录。

#### 旧模式 · 三固定目录（legacy，2026-08-07前）

以下三个目录是旧模式，仍可用但已废弃（deprecated）：
- `/data/math-agent-glm5.2-1`
- `/data/math-agent-glm5.2-2`
- `/data/math-agent-glm5.2-3`

旧模式的问题：目录在run之间被清理复用，运行记录（problem.txt、proof、hint等）不保留。新模式解决了这个问题——每个实验有独立目录，运行后全部保留。

**Solver角色定义**（无论新旧模式，AGENTS.md内容一致）：
- 直接做数学，不走工作系统流程
- **可以搜索通用数学知识（定理/定义/公式），但禁止搜索题目答案/解答**——搜索纪律详见`templates/solver_agents_md.md`
- 允许 `exec`（Python/SymPy计算验证）、`read`/`write`/`edit`（保存证明草稿）、`web_search`（搜通用数学知识）
- 不知道就说"我不知道"，系统通过提示引导
- **启动必须加`--permission-mode dangerous`**——否则exec被rejected，AI只做2步就停

### 硬约束 6 · Solver启动必须通过solver-harness（最重要）

**启动数学大师Solver的devin cli实例，必须通过`xishujuzhen/solver_harness/solver_harness.py launch`，禁止任何其他方式。**

**禁止的方式**：
- ❌ 手动`tmux new-session ... devin`
- ❌ `exec`后台（`timeout=0`）直接跑`devin`
- ❌ `nohup devin ... &`
- ❌ `subprocess.run(["devin", "-p", ...])`直接调用
- ❌ 任何绕过solver-harness的脚本

**适用所有场景**（无一例外）：
- 裸跑测试、GuidedLoop引导、批量测试、DFS回溯实验
- MathArena测试、FATE测试、A/B对照实验

**为什么这是硬约束**：
1. solver-harness通过mitmproxy代理（launchd系统服务，端口18889）捕获token级thinking+tool_calls——手动启动无法采集MITM trajectory
2. solver-harness自动完成：tmux启动 + mitmproxy代理 + pipe-pane兜底 + sessions.db轮询 + 事后批量解码
3. `--no-http2`修复了多轮交互的Connection failed问题——只有通过harness启动才能享受这个修复
4. `NODE_EXTRA_CA_CERTS`修复了SSL验证问题——只有通过harness启动才会设置这个环境变量

**已知的违规脚本**（必须修复，新AI不要模仿）：
- `scripts/matharena_batch_test.py` — 直接`subprocess.run(["devin", "-p", ...])`
- `scripts/fate_batch_test.py` — 直接`subprocess.run(["devin", "-p", ...])`
- `scripts/guided_exp_runner.py` — 直接`tmux new-session ... devin`
- `xishujuzhen/research_runtime/runtime/devin_cli_adapter.py` — 直接`subprocess.run(["devin", "-p", ...])`

**例外**：`xishujuzhen/research_runtime/realtime/devin_cli_parser.py`中的`DevinCliParserProvider`用`devin -p`做LLM parser（不是Solver，不采集trajectory），可以保留直接调用。

**具体启动规范见** `.devin/rules/solver-tmux-launch.md` 和 `.devin/skills/solver-tmux-launch/SKILL.md`。

### 任务追踪（跨Session工作意识维持）

**任务追踪文档目录**：`任务追踪/`——每个工作线一个独立文件，顺序编号化（`01-`、`02-`、...），自包含，互不干扰。

**`任务追踪/README.md`** — 任务追踪目录的导航枢纽，记录各任务追踪文档之间的**依赖关系DAG**。新Session的AI先读README.md了解工作线全貌和依赖关系，再选择对应工作线的任务追踪文档深入。

**当前活跃的任务追踪文档**：

| 文件 | 工作线 | 焦点 |
|---|---|---|
| `任务追踪/01-253号检索机制验证.md` | 253号检索机制验证 | P0+P1原型验证完成，泛化验证通过（3领域6指标达标），P1原语升级tested完成（tested 35/72） |
| `任务追踪/02-trajectory采集与solver-harness.md` | Trajectory采集基础设施 | solver-harness方案v1完成，实施待做 |
| `任务追踪/03-虚拟数学系统VMS-POC验证.md` | 虚拟数学系统POC验证 | 方案设计完成，7阶段全部未开始，前置工作（258号挑战类型分析）待执行 |
| `任务追踪/04-端到端效果验证-接真实Solver.md` | 端到端效果验证→Grove树生长引擎 | ✅A/B实验完成（A组2/3突破，B组0/3）。267号面相认知注入：Grove树生长引擎方向——阶段2脉络注入→阶段3并发展开→阶段4自我增殖 |

**Grove AI 的主任务方向**：04工作线 → Grove树生长引擎。交接文档268号。新Session先读268号，再全文加载267号（认知转折点）。

**任务追踪文档编写要求**（硬性规范，所有任务追踪文档必须遵守）：

1. **自包含**——文档必须自包含，读者不需要回溯对话历史就能理解。每个条目说清楚"做了什么"和"为什么做"（为什么做比做了什么更重要——它是跨Session后恢复工作意识的锚点）。
2. **Checklist化**——所有任务用`- [x]`/`- [ ]`格式列出，状态一目了然。完成一个立即打勾，不批量更新。
3. **结构统一**——包含以下章节：
   - §0 当前工作焦点（1-2句话，当前在做什么）
   - §1 已完成的工作（按时间顺序，每项含"为什么做"+ checklist）
   - §2 待办清单（按优先级排序，每项含"为什么做"+ checklist）
   - §3 关键决策记录（为什么做了某个选择，而不是另一个）
   - §4 Git Commit历史（本工作线的commit列表）
   - §5 跨Session读取指南（新AI进入本工作线后该读哪些文档）
4. **不删除历史**——历史条目是工作积累的记录，只打勾不删除。
5. **新建时必须更新README.md**——新建任务追踪文档时，AI必须考虑更新`任务追踪/README.md`的内容。如果有必要，需写清楚新任务和原有任务之间的逻辑关系（依赖、起源、阻塞等）。不能只新建文件而不更新DAG——那样其他AI无法理解新工作线在全局中的位置。同时，文件名必须顺序编号化（`01-`、`02-`、`03-`、...），编号按创建顺序递增。
6. **与AGENTS.md的分工**：AGENTS.md是项目总目录（always-on硬约束+认知资产索引），不写任何具体工作线的当前状态。任务追踪是工作流追踪（当前在做什么+接下来做什么）。AGENTS.md指向任务追踪目录，任务追踪指向具体dev-docs和代码模块。
7. **记录git commit ID和全部产出资产path**——每个工作单元完成并commit后，在§4 Git Commit历史中记录commit hash和本次产出的**全部资产**的完整路径（相对于repo根目录）。格式：`| <hash> | <描述> | <产出资产路径列表> |`。**"全部资产"包括**：dev-docs文档、代码模块（.py/.js等）、测试脚本、原语文件（primitives/）、配置文件、数据文件（.json/.db等）、任务追踪文档本身——凡是本次commit中新增或修改的文件，都属于本次产出资产。**路径必须完整**：写`xishujuzhen/research_runtime/parser/evaluate_accuracy.py`而非`evaluate_accuracy.py`；写`dev-docs/260-v0-2026-08-07-缺口1攻关方案-自然语言到结构化表示的解析器.md`而非`260号文档`。

### 认知资产索引（活文档）

认知资产索引（ArangoDB 初始化状态、认知图/依赖图/题库统计）在 `xishujuzhen/cognition_asset_index.md`，由工作系统持续维护。每次新增认知单元、新增 dev-docs、ArangoDB 状态变更后更新该文档。

### 系统设计原语目录（活文档）

系统设计原语分四层管理（244号重构 + 245号面相独立 + 257号全库原语找回）：
- **`primitives/`** — 原语（构造系统的积木，72个）：`operational/`（操作原语47个：可执行的动作/策略/约束/协议）+ `structural/`（结构原语25个：可放置的组件/角色/接口）。验证状态四等级：tested / tested_negative / partial / untested。257号全库原语找回新增56个原语（18结构+38操作），详见 `dev-docs/257-v0-2026-08-07-全量原语目录更新方案-以253号检索问题为抓手的全库原语找回.md`。
- **`concepts/`** — 概念框架（理解系统的视角，8个）：形式化边界、两种计算、闭环、处境、系统设计即多约束求解等。不需要验证状态，用"适用边界"替代。
- **`criteria/`** — 性质标准与探索性隐喻（3个）：自然性、生死条件（判断标准）+ 语义场（隐喻）。
- **`facets/`** — 面相（切分维度，7个）：系统面相1/2/3/4（两种计算/语料双路径/Pipeline网络/树的生长）+ 设计过程面相A/B/C（实践涌现/知识选取/设计过程自举）。面相横切前三层，通过元素文件"来源"字段中的"面相归属"行正向引用。

原语三判据：可执行性 + 可验证性 + 构造性。不满足的归入concepts/或criteria/。方案见 `dev-docs/241-v1-2026-08-07-系统设计原语目录方案.md`（原始方案）、`dev-docs/244-v0-2026-08-07-原语目录重构方案.md`（三层分类重构）、`dev-docs/245-v0-2026-08-07-面相独立目录与设计元素管理元组群方案.md`（面相独立+管理元组）和 `dev-docs/257-v0-2026-08-07-全量原语目录更新方案-以253号检索问题为抓手的全库原语找回.md`（全库原语找回）。验证状态分布（72个原语）：tested 35 / partial 16 / untested 20 / tested_negative 1。P0+P1原型实现后更新了16个原语验证状态。真实LLM解析验证后，P0的3个原语从partial升级到tested。progress-measurement实现后升级tested，checkpoint实现后升级partial。解析器泛化能力已验证——3个数学领域（代数/分析、数论、组合/概率）6项指标全部达标。P1泛化验证通过后，8个P1原语从partial升级到tested（activation-score/pattern-matching/retrieval-pipeline/constrained-policy/hint-gradient/gain-attribution/pattern-lifecycle/heuristic-rule-graph在数论和组合2个新案例上全部通过）。端到端测试验证253号A7→Q8完整检索流程跑通（mock+真实LLM响应双重验证）。每次跑实验后更新相关原语的验证状态。

### 原语化AI数学工程系统设计（活文档 · 论文原语化版）

**`原语化AI数学工程系统设计/`** — 256号论文的原语化升级版（v5）。系统是原语化的（由原语构造），对系统的描述也应该是原语化的（由原语描述构造）。论文结构镜像系统结构：不是单体叙事文件，而是26个自包含的原语描述文件，通过前置阅读和关联原语链接形成阅读网络。README.md是导航枢纽（系统全景+原语索引+三条阅读路线）。目录结构：00-基础概念（6个）/01-问题（2个）/02-案例（2个）/03-四代系统（5个）/04-核心洞察（5个）/05-两棵树（3个）/06-面相（1个）/07-验证（1个）/08-参考文献。单体叙事版256-v4保留在`dev-docs/256-v0-*`作为历史归档。

### 四代技术说明书系列（系统演进主线 · 活文档）

数学大师系统经历了四代演进，每一代有中国神话命名（便于指称）和独立技术说明书。命名规则见 `.devin/rules/system-generation-naming.md`。

| 代际 | 神话名 | 核心理念 | 技术说明书 |
|---|---|---|---|
| 第一代 | **盘古** | 静态图前置——开天辟地，从无到有创建系统 | `dev-docs/249-v0-2026-08-07-第一代数学大师系统-最完整技术说明书.md` |
| 中间代 | **女娲** | 动态控制+角色隔离——补天（修补架构断层）+造人（角色隔离） | `dev-docs/250-v0-2026-08-07-中间代数学大师系统-技术说明书.md` |
| 第二代 | **燧人** | 非特定元认知提问——钻木取火（不给火而教取火，不给答案而给思维启发） | `dev-docs/238-v1-2026-08-07-非特定高Level启发式提问方案完整梳理.md` |
| 第三代 | **伏羲** | 形式化边界推进——画八卦（建立终极形式化框架） | `dev-docs/239-v0-2026-08-07-AI数学工程系统-最完整技术说明书.md` |

**代际转折点**：
- 盘古→女娲：122-v1诊断架构断层，硬公理降级为可证伪假设
- 女娲→燧人：200-202号危机诊断暴露中间代架构理念层面缺陷（规则匹配粒度、Hint梯度泄漏、角色隔离未实现），催生非特定元认知提问
- 燧人→伏羲：218号非特定性危机+222号形式化边界是本质性的，从"提问策略"升级为"两种计算+闭环推进边界"

**命名含义**：
- **盘古**：开天辟地——第一代从零开始创建系统（稀疏矩阵、依赖图、七步骤）
- **女娲**：补天+造人——中间代修补第一代架构断层（补天），建立8角色隔离矩阵（造人）
- **燧人**：钻木取火——第二代不给AI答案，而是启发AI自己的思维之火（非特定高Level元认知提问）
- **伏羲**：画八卦——第三代建立终极形式化框架（两种计算、闭环、形式化边界推进）

250号编写方案见 `dev-docs/251-v0-2026-08-07-中间代技术说明书250号编写方案与分步提示词.md`。

### TOP10最难题集（baseline评测用）

从10063个数据集中选出AI最做不出来的10套，用于baseline能力边界定位。详情查ArangoDB `math_datasets`集合（`grove_math`），元组`math-datasets`提供查询工作流。

| # | 数据集 | 题量 | 难度 | AI表现 | 有解答 | 状态 |
|---|---|---|---|---|---|---|
| 1 | FATE（北大） | 350 | 博士资格考+ | **FATE-X pass@64: 0%** | ✅Lean4证明 | 🔄下载中 |
| 2 | ConjectureBench | 15,000 | 研究级(开放问题) | 无标准答案 | ❌开放问题 | ✅完成 |
| 3 | MathNet（MIT） | 30,676 | 竞赛级(IMO) | Gemini 78%, GPT-5 69% | ✅专家解答 | 🔄下载中 |
| 4 | Project Euler | 800 | 本科+研究级 | — | ✅详细解答 | 🔄下载中 |
| 5 | Hendrycks MATH | 12,500 | 竞赛级(AMC/AIME) | Level 5极难 | ✅详细解答 | 🔄下载中 |
| 6 | compfiles | 520 | 竞赛级(IMO) | Lean 4验证 | ✅Lean4证明 | ✅完成 |
| 7 | miniF2F（OpenAI） | ~488 | 竞赛+本科 | 形式化标准基准 | ✅Lean/Isabelle证明 | 🔄下载中 |
| 8 | 丘成桐竞赛 | 300 | 研究生+研究级 | — | ❌仅真题无解答 | 🔄部分 |
| 9 | Berkeley Problems | 200 | 研究生(资格考) | — | ✅详细解答 | ✅完成 |
| 10 | AoPS/LiveAoPSBench | 600,000 | 竞赛级 | 时间戳分割检测污染 | ✅论坛解答 | ✅完成 |

**解答情况**：8/10有解答。ConjectureBench是开放问题（无答案，测猜想能力）；丘成桐竞赛仅有真题无官方解答（待从其他渠道补充或用于AI自验证测试）。

### MathArena 2024-2026竞赛最难题baseline（已完成）

用5个tmux session并行测试了43道2024-2026年世界级竞赛最难题（各竞赛最后2-3道大题）。数据来源：MathArena（HuggingFace），21个数据集已下载到`knowledge/problem_banks/matharena/`。

**测试范围**：IMO 2025 / Putnam 2025 / USAMO 2024-2026 / IMC 2025 / Miklos Schweitzer 2025 / APEX 2025 / HMMT Feb 2025-2026 / HMMT Nov 2025 / BRUMO 2025 / SMT 2025 / CMIMC 2025 / AIME 2024-2026

**GLM-5.2裸跑结果**（无提示、无引导、禁网搜）：

| 类别 | 题数 | 正确/解决 | 答案错误 | 卡住/无答案 | 正确率 |
|---|---|---|---|---|---|
| 证明题(IMO/USAMO/Putnam/IMC/Miklos) | 11 | 2 | 0 | 8 | 18.2% |
| 数值题(AIME/HMMT/SMT/BRUMO/CMIMC/APEX) | 26 | 4 | 7 | 15 | 15.4% |
| **总计**（排除API error后） | **37** | **7** | **7** | **23** | **18.9%** |

**做出来的题**（7道）：
- IMO 2025 P5（证明题，242.9s）
- IMC 2025 P9（证明题，229.2s）
- SMT 2025 #52（数值题，答案41，96.2s）
- HMMT Feb 2026 #31（数值题，答案10，47.1s）
- CMIMC 2025 #38（数值题，答案8222，133.4s）
- AIME 2024 I #13（数值题，答案104，85.3s）
- AIME 2024 II #12（数值题，答案321，likely_correct，41.5s）

**做不出来的题**（30道，占81.1%）：USAMO全部stuck/error、Putnam全部stuck/error、Miklos全部stuck、BRUMO全部stuck、HMMT Nov全部stuck、AIME 2025-2026 #14全部stuck。

**关键发现**：
1. GLM-5.2在2024+年竞赛最难题上正确率仅18.9%——大量题直接stuck（输出<100字符就说不知道）
2. 证明题能力极弱：USAMO/Putnam/Miklos几乎全部stuck
3. 数值题稍好但也只有15.4%正确率，AIME #14-15（最难的AIME题）全部做不出
4. 6道API error（连接问题，非AI能力问题），需重跑

**Phase 1b验证**（修复截断+文件传递后重测30道做不出来的题）：仍然0/25做出来（排除5 error）。确认这些题是GLM-5.2的真实能力边界，不是基础设施问题。

**测试脚本**：`scripts/matharena_batch_test.py`
**结果文件**：`runs/matharena_hard_{1-5}/solutions.json` + `summary.json`
**方案文档**：`dev-docs/213-v1-2026-08-06-推进GLM-5.2解决30道竞赛最难题计划方案.md`

### 提示策略路线选择与Level连续谱

详见 `dev-docs/214-v1-2026-08-06-提示策略路线选择与Level连续谱.md`（理论记录+参考案例）。

核心决策：提示干预走路线B（思维模式）而非路线A（堆砌知识）。寻找最深的、最通用的、最高抽象度的思维模式——跨知识范围的元认知策略，而非限于同一知识范围的具体定理/技巧。

依赖图中每个元素带Level标签（0到1实数）：→0纯知识，→1纯思维模式，中间是灰色地带。Level是经验的、模糊的、相对的——不是被赋值的，而是被AI通过相对比较感知的。

**元组群 `guided-math-solving`**（引导式数学解题）：214号的操作流程已提取为元组群，规则在 `.devin/rules/guided-math-solving.md`（always-on认知+Skill目录），5个Skill：
- `guided-rehearsal`：预演——生成模拟QA序列和极致提示集合
- `guided-session-launch`：启动session——work_dir+tmux+devin+--export
- `guided-interaction`：交互引导——连续发问框架执行（核心）
- `guided-backtrack`：回溯——新session+重放+换方向
- `guided-data-persist`：数据持久化——ArangoDB+文件系统归档

改造方案见 `dev-docs/216-v0-2026-08-06-214号元组群改造方案.md`。实验方案见 `dev-docs/215-v0-2026-08-06-连续交互启发式引导实验方案.md`。

**相关目录与角色**：
- **本 repo（Grove AI）**：`/data/master-mind-glm5.2-grove/`
- **Master tmux 脚本**：`scripts/start-master.sh`、`scripts/enter-master.sh`、`scripts/stop-master.sh`
- **Grove AI 职责**：实现、迭代 Grove 树生长引擎；**Subagent 职责**：完成 Grove AI 分配的具体任务

---
## 临时章节：如何检查正在工作的Solver AI（2026-08-07）

> 本章节记录Master AI观察和干预在tmux中运行的Solver AI的操作方法。来自bare_q2裸跑测试的实战经验。未来AI在检查Solver工作过程时参考此章节。

### 启动Solver session

```bash
# 1. 创建实验目录（新模式：tmux-agents-dir）
EXP_DIR="/data/grove-agents-dir/<experiment-id>"
mkdir -p ${EXP_DIR}/exports
cp templates/solver_agents_md.md ${EXP_DIR}/AGENTS.md  # 从模板复制

# 检查占用
tmux list-sessions | grep -E "solver|bare|guided"

# 2. 写problem.txt到实验目录
# 3. 用tmux启动devin cli
tmux new-session -d -s <session-name> "cd ${EXP_DIR} && devin"
sleep 8
tmux capture-pane -t <session-name> -p | tail -15  # 检查是否启动

# 4. 如果出现trust prompt，选择"Yes, trust"
tmux send-keys -t <session-name> "1" Enter

# 5. 启动pipe-pane兜底记录（写入实验目录）
tmux pipe-pane -t <session-name> "cat >> ${EXP_DIR}/tmux_pipe.log"

# 6. 发送题目指令
tmux send-keys -t <session-name> "请读取当前目录下的problem.txt文件，然后做题。" Enter
```

### 观察Solver工作过程

```bash
# 基本观察（看最后30行）
tmux capture-pane -t <session-name> -p -S -100 | tail -30

# 深度观察（看最后300行，去掉ANSI噪音）
tmux capture-pane -t <session-name> -p -S -300 | grep -v '^\[' | grep -v '^$' | tail -60

# 检查AI是否写了文件
ls -la ${EXP_DIR}/proof* 2>/dev/null

# 检查AI的thinking字符数（判断思考深度）
# 屏幕上会显示 "Thinking · Xm Ys · (NNNNNc · ctrl+o for details)"
# NNNNNc是thinking的字符数，40k+表示深度思考
```

### 已知问题与处理方法

#### 问题1：Response truncated（输出被截断）

**现象**：AI在thinking阶段花40-50k字符思考，然后在output阶段一次性输出完整证明文本，达到max output token limit被截断。屏幕显示：
```
⚠︎ Response truncated
  The response was cut short because it hit the model's max output token limit.
  Send a message to continue
```

**根因**：GLM-5.2倾向于"想完所有内容然后一次性输出文本"，不主动调用write/exec工具。

**处理方法**：
1. **预防**：在初始指令中就明确要求"把证明写到文件里，不要在对话里输出证明内容。用write工具写proof.md"
2. **预防**：指令要简短——"只做第一问"比"两问都要做"更容易让AI不触发截断
3. **预防**：告诉AI"用python3 -c命令把证明写到文件"——exec工具比write工具更容易被AI调用
4. **截断后**：发"continue"可能再次截断（AI重复同样行为）。更好做法是杀掉session重新开始，用更简短的指令
5. **最有效**：让AI先做数值验证（exec工具），验证完后它会自然过渡到调用write工具写证明

#### 问题2：Connection lost（连接中断）

**现象**：屏幕显示 `⚠︎ Connection lost, retrying...`

**影响**：thinking内容不持久化在对话历史中。connection lost时正在进行的API请求被中断，thinking内容**完全丢失**。重连后模型从头开始thinking，但看不到之前的推理。thinking字符数会突然变少（如从54k降到16k）。

**处理方法**：
- 无法预防，这是API连接问题
- 重连后AI会重新思考，但推理深度可能降低
- 如果重连后thinking字符数远少于之前，考虑杀掉session重新开始（让AI从头思考，而不是在丢失context的状态下继续）

#### 问题3：工具批准提示

**现象**：AI调用exec/write工具时，devin cli会弹出批准提示：
```
❭ 1 Yes  (Approve once)
· 2 Yes, allow `python3` commands
· 3 Yes, always allow `python3` commands in math-agent-glm5.2-<n>
· 4 Yes, always allow `python3` commands in all projects
```

**处理方法**：选3（always allow in this dir）——避免后续重复批准。发送：
```bash
tmux send-keys -t <session-name> "3" Enter
```

对于write工具的批准提示：
```
❭ 1 Yes  (Approve once)
· 2 Yes, switch to accept edits mode
· 3 No
```
选2（accept edits mode）——后续所有文件写入自动批准。

#### 问题4：pipe-pane日志被ANSI转义序列污染

**现象**：pipe-pane记录的日志包含大量ANSI转义序列和spinner字符，难以阅读。

**处理方法**：用perl清理后查看：
```bash
cat runs/<run_id>/tmux_pipe.log | perl -pe 's/\x1b\[[0-9;]*[a-zA-Z]//g' | perl -pe 's/[\x{2800}-\x{28ff}]//g' | grep -v '^$' | tail -60
```

注意：pipe-pane日志可能不完整——tmux的scrollback buffer有限，AI的长输出可能被覆盖。如果需要完整输出，用devin cli的`--export`参数（见solver-tmux-launch skill）。

### 判断Solver是否"做出来了"

1. **检查文件**：`ls -la ${EXP_DIR}/proof*` ——AI是否写了证明文件
2. **读证明**：`cat ${EXP_DIR}/proof.md` ——证明内容是否正确
3. **看对话状态**：AI是否说了"证毕"或"QED"
4. **看thinking字符数**：如果AI在第二问上thinking超过50k字符但没写文件，可能是"想了很多但做不出来"
5. **看工具调用**：AI是否调用了exec做数值验证——调用exec通常表示AI在认真尝试；不调用exec只在thinking里转，可能是卡住了

### 不要做的事

- **不要在AI思考时频繁发消息**——每次消息都会打断AI的thinking，丢失推理
- **不要发"continue"超过2次**——如果AI反复被截断，说明输出策略有问题，应该杀掉session重新开始
- **不要在AI工作期间修改工作目录的文件**——可能干扰AI的文件操作

---

## 项目定位

本项目是 **AI 数学大师制造项目**，不是单纯的写代码项目，也不是星学项目。

项目从星学领域的 POC 实验中继承了“用稀疏关系工程化大师知道该判断什么”的方法论线索，但数学领域的动态启发能力尚未验证。当前目标不是照搬星学静态图，而是制造一个能做数学研究、并能在动态研究状态中接受最小可验证引导的 AI 大师。

**"数学大师"的定义**：本项目语境中的"数学大师"，指能做数学研究的 AI——提出猜想、构造证明、发现新定理、在复杂数学问题面前知道该从哪个方向切入、该调用哪些数学工具、该沿什么路径思考。不是只会做题的解题机器，而是具备研究品味的数学家。

**"最通用的数学大师"**：本项目目标是制造**最通用的数学大师**，不是某个特定数学领域的专家系统。数学大师应该能覆盖代数、几何、分析、拓扑、数论、组合、逻辑、范畴论等全部数学领域，能在任意数学问题面前知道该判断什么。当前以矩条件极差题等具体场景作为POC实验场，但这是验证方法论的实验场景，不是项目的终态边界。依赖图的构建从具体领域切入（如代数拓扑），逐步扩展到全部数学领域——不预设领域边界。

**"新系统"的硬边界**：本项目语境中的"新系统"，默认且专指为数学研究而建设的知识系统与思维导航系统。星学项目中的 `qizheng/`、`study-notes/`、MOIRA Java、Swiss Ephemeris 等是**参考实现和方法论证据链**，不是新系统本体。

### 本项目与星学项目的关系

本项目从 `~/MOIRA_chinese_astrology-main/`（已复制到当前目录 `/data/master-mind/`）的星学研究中继承而来。星学POC是方法论证据来源，但不能自动证明数学研究中的动态启发有效，也不能让星学运行时支配数学架构。

本项目要做的是：**把这条方法论作为可证伪假设，在数学研究领域重新定义对象、实现闭环并独立验证。**

星学是第一个实验场，数学是第二个。如果方法论在数学领域同样成立，它的意义将不限于数学——任何复杂知识体系的"综述博士"角色都可能被工程化。


## 核心假设（从星学信念降级并在数学中重验）

星学项目63号文档提出"完美提示词可以通过经典计算产生"。123号架构已将它从硬公理降为可证伪假设：

> 在部分问题族和研究状态上，确定性结构计算、状态估计、历史因果效果与数学验证，能否共同选择一个低成本、低泄漏、能增加已验证进展的最小干预？

当前纪律：

1. **大师价值的一部分是激活方向**，但不能预设全部价值都等于提示词；
2. **提示是动态策略，不是一次性完整文本**；
3. **经典计算负责确定部分**：类型/前提过滤、遍历、模式匹配、稀疏候选、预算、权限和审计；
4. **启发是否有效必须实验验证**，不能由图中存在一条边定义性保证；
5. **稀疏矩阵是计算视图，不是真值本体**；K/T/H分别是数学语义、事件状态和启发规则的查询投影；
6. 若去掉答案等价信息后增益消失，系统必须降级为诚实的静态知识/证明编译器。

### 两种博士

| 类型 | 特征 | 对应角色 | 本项目是否工程化 |
|---|---|---|---|
| 综述博士 | 知识体系全掌握、全能灵活运用 | 知道在什么时候该看什么、该结合什么 | **是，这是本项目的目标** |
| 论文博士 | 负责创新 | 创造新知识、新方法 | 不在本次工程化范围，但不排斥 |

### 大师的"一次在场"

旧xishujuzhen只编码Master预先写入的关系；新系统允许从成功/失败事件中发现**候选**启发，但候选必须经最小干预、迁移和泄漏审计后才可发布。**大师的一次在场仍然重要，但不能再把一次手写路线冒充系统自主发现。**

## 方法论核心（继承方向，数学动态能力待验证）

星学POC可证明静态关系提示在其场景中的局部价值；迁移到数学时，本体、运行状态、验证标准和答案泄漏边界都必须重做，不能只替换依赖图内容。

### 稀疏关系计算

"三维稀疏矩阵"保留为历史直觉：分析节点×思维意识×上下文。123号后的精确模型不是一张万能矩阵，而是：

- K：按`requires/uses/generalizes/analogous/verified_by`等关系拆分的稀疏视图；
- T：不可变事件、状态快照和时序投影；
- H：规则—条件—动作及效果证据的稀疏因子视图。

稀疏性仍然成立：总知识量很大，但每个具体研究状态只激活少量关系。矩阵负责候选计算，不负责数学真值。

### 两种环路

| 环路类型 | 特征 | 判别标准 | 处理方式 |
|---|---|---|---|
| 平面环路 | 不同时间事件投影回同一规范化状态 | 开放义务、证据门和冲突无改善 | 停止或换策略 |
| 螺旋上升环路 | 返回同一抽象状态类，但更细粒度状态进展 | 同一任务/schema下进展向量不恶化且至少一项严格改善 | 允许继续并保存进展证据 |

### 依赖图作为提示，而非替代思考

系统不是自动推理引擎，而是**提示生成器**。分三层：脚本计算依赖 → AI在依赖图提示下完成分析 → 粒度拆分→小图分析→大图综合。**依赖图的大小必须被控制在一个合理范围内**。

### 系统不做判断，只做依赖计算和提示生成

| 维度 | 系统做 | AI 做 |
|---|---|---|
| 依赖关系 | 计算、存储、遍历、子图提取、环检测 | 理解、沿路径思考 |
| 判断 | 不做 | 在提示下完成数学判断 |
| 创造 | 不能发现未编码的新依赖 | 可以即兴发现新连接（论文博士侧面） |

## 项目目标

建设一个 **"数学知识系统 + 依赖图导航 + AI 智能研究"** 的数学大师系统。

让整套项目可以辅助 AI 完成：

1. **数学研究导航** —— 面对一个数学问题，知道该从哪个方向切入、该调用哪些数学工具、该沿什么路径思考。
2. **猜想提出与验证** —— 在依赖图提示下，提出有意义的数学猜想，并知道该用什么工具验证。
3. **证明构造** —— 沿依赖路径组织证明思路，知道哪些定理是前置、哪些是引理、哪些是工具。
4. **跨领域类比** —— 发现不同数学领域之间的结构同构（如范畴论视角下的统一），并知道这种类比的适用边界。
5. **知识持续深化** —— 把数学文献、研究经验、跨领域洞察消化进知识系统和依赖图，形成能自我演化的数学认知系统。

**总体架构与建设计划状态**：122号v1—v3完成工程断层、K/T/H和证据边界复核；123号以`系统探讨.md`全文为母本，从第一性原理将目标系统定义为类型化任务/工作区、不可变事件、表示变换、启发规则、证据状态和受约束最小干预，并给出DYN-0—7与Phase 0—7。旧七步骤正式降为legacy静态重建器。项目启动认知见80号，证据复核见122号v3，当前最高架构与建设基线见 <ref_file file="/data/master-mind/dev-docs/123-v1-2026-08-05-数学大师系统全景复盘与第一性原理重构计划.md" />。

### 旧七步骤→新12步运行时迁移映射（177号审计修正F-177-4）

旧七步骤（`seven_step_pipeline.py`）已降为legacy静态重建器，新系统用12步在线运行时（123号§32）替代。映射关系：

| 旧七步骤 | 新12步运行时 | 说明 |
|---|---|---|
| 步骤1：依赖图构建 | 步骤1：初始化（manifest+Q_0冻结） | 依赖图改为K投影，由DgAdapter只读生成 |
| 步骤2：子图提取 | 步骤2-3：事件捕获+语义抽取 | 子图提取改为Retriever按需检索 |
| 步骤3：粒度拆分 | 步骤4：状态重建（StateReducer） | 粒度拆分改为义务图超边分解 |
| 步骤4：小图分析 | 步骤5-6：卡点检测+控制器信念 | 小图分析改为Controller不确定性估计 |
| 步骤5：大图综合 | 步骤7：诊断决策 | 大图综合改为HeuristicMatcher离线候选 |
| 步骤6：提示生成 | 步骤8-9：最小干预+激活包 | 提示生成改为受约束多目标选择 |
| 步骤7：验证 | 步骤10-12：验证+状态更新+checkpoint | 验证改为Verifier角色+验证门 |

**关键区别**：旧七步骤是静态的、一次性的、Master预写入的；新12步是动态的、循环的、在线受约束的。旧七步骤的`seven_step_pipeline.py`仍可作为离线工具使用，但不能替代新12步在线运行时。


## 四类载体的分工

| 载体 | 角色 | 不是什么 |
|---|---|---|
| `math-notes/`（待建） | **数学知识系统本体**：数学知识、研究方法、领域地图、工具索引 | 不是教材摘录堆，也不是代码文档 |
| `math-notes/数学意识/`（待建） | **弥漫性数学思维**：数学直觉、美感、类比思维、证明策略等贯穿整个研究过程的底层思维模式 | 不是某个问题的专属解法 |
| `xishujuzhen/`（待建） | **依赖图导航系统**：稀疏矩阵、依赖计算、环检测、提示生成 | 不是知识仓库，不是计算引擎 |
| 数学计算工具（待选型） | **经典计算底座**：符号计算、数值计算、定理证明辅助 | 不是知识系统本体 |
| 星学项目文件（当前目录中） | **方法论参考实现**：POC1-8 验证记录、xishujuzhen 设计文档、星学知识系统结构 | 不是数学项目的工作对象 |
| AI | 读取依赖图提示，依照知识系统做数学研究和判断 | 不能把无出处记忆悄悄当成已证定理 |

### K维度多层知识结构（201号）

大师数学系统的稀疏矩阵K维度不仅存储直接知识（L1），也必须存储AI从内容中提取的高阶抽象知识（L2/L3/L4）。**AI在知识吸收阶段的核心价值是从具体知识中提取高阶知识**——这是规则/脚本无法替代的创造性活动。

| 层级 | 名称 | 内容 | 例子（费马大定理） | 存储位置 |
|---|---|---|---|---|
| L1 | 解题路径 | 具体证明步骤 | "用Ribet定理从Taniyama-Shimura推出费马大定理" | K维度·requires/uses边 |
| L2 | 思维模式 | 弥漫性数学思维 | "从特殊情况反推一般规律"、"用不变量简化问题" | K维度·awareness节点 |
| L3 | 范式 | 跨领域映射 | "椭圆曲线↔模形式对应（改变图结构的范式）" | K维度·cross_domain边 |
| L4 | 哲学/世界观 | 数学哲学洞察 | "等价性比相等性更深刻"、"深刻真理隐藏在无关领域之间" | K维度·philosophy节点（新增） |

**当前状态**：三层提取机制（L1/L2/L3）已在`batch_extractor.py`中设计并在POC3中验证过一次，但未常态化、未连接吸收pipeline、未存入ArangoDB。L4层完全不存在。详见201号文档。

**纪律**：每次吸收新数学内容时，必须由AI执行L1-L4提取，提取结果经质量审计后存入K维度对应位置。不能只存L1不存L2/L3/L4——那样系统只有直接知识，没有高阶知识，Solver只能"查资料"不能"学思维"。

### AI在运行过程中的角色（202号）

大师数学系统在Solver解题的运行过程中，引导决策（步骤7诊断/步骤8匹配/步骤9动作选择/步骤10提示编译）当前全部由经典计算完成——关键词匹配+阈值比较+硬编码规则。**经典计算给出的选项是"死的"，AI能给出"活的"判断。**

**分工原则**：
- 经典计算负责：精确记录、形式化验证、规则检索、给出候选选项
- AI负责：理解Solver思路内容、从候选中选择最合适的、生成针对性提示、多轮引导的智能规划
- 两层协作：经典计算先给候选→AI从候选中选择或调整→AI不可用时fallback到经典计算默认

**"遍历地图"类比**：如果目的是让Solver遍历知识图上的每个角落，经典计算能根据已遍历位置给出可选项，但AI能给出更具智慧的遍历顺序——哪些"桥梁节点"值得优先、哪些方向更有潜力、哪些区域已经充分探索。

**当前状态**：12步运行时（orchestrator.py）的步骤7-10全部经典计算，没有AI参与。GuidedLoop简化版的5条提示全部硬编码。详见202号文档。

**纪律**：引导决策不能只靠经典计算——经典计算只给候选，AI做最终判断。当经典计算给出不确定结果（多卡点类型概率相近/多轮未完成/候选过多）时，必须调用AI分析。


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
- **穷尽式知识吸收（v3：十三大来源）**：全能数学大师应该知道**一切**可得的数学知识。v3从"数学痴狂爱好者"视角发掘了十三大来源（数学家全集/教材/习题集/数学思想书/arXiv/竞赛题/百科数据库/形式化数学库/数学杂志/讲义综述/趣味数学/开放问题/历史哲学），估计~60万条目~325000节点。详见109号方案。
- **数学计算交给工具，数学知识由知识系统承载，数学判断由 AI 执行，三者不混用。**
- **依赖图构建需要数学功力**：判断"代数拓扑依赖范畴论"是一条边——这个判断需要"综述博士"参与。
- **方法论迁移不是照搬**：星学的依赖图结构不适用于数学，数学的依赖图需要重新设计。

### Check List措辞规范与审计方法论

> **完整手册**：`dev-docs/146-v4-2026-08-05-审计方法论手册-*.md`（F1-F15断层类型学、D1-D4深度等级、21审计维度、三文件交叉审计流程、实现前/后协议）。

**核心要点（速查）**：断层类型 F1-F6（定义了=实现了/验证了=完整了/覆盖盲区/概念混淆/权威偏差/方法近似）；实现深度 D1-D4；权威原则——Check List是导航，127号Schema冻结文档是法律。**实现前**：读146号手册第8章 + Check List + 127号原文。**实现后**：按21维度逐项审计。

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

### 回归验证

每次认知图变更（新增/修改/删除认知单元或依赖边）后，运行回归验证：D1覆盖率 + D3版本链 + D4图遍历完整性。满分100，低于95需排查。

### Hook机制

三个hook的分工（均为纯提醒，无硬门禁）：

| hook | 触发时机 | 脚本 | 作用 |
|---|---|---|---|
| SessionStart | 新session/压缩后 | `session_start_hook_math.py` | 注入认知图统计+工作纪律 |
| UserPromptSubmit | 每次用户提问 | `user_prompt_submit_hook_math.py` | 从`UserPromptSubmit.txt`读取提醒注入 |
| git post-commit | 每次commit后 | `githooks/post-commit` | 打印CP4检查清单（从稀疏矩阵动态查询） |

**改提醒内容**：直接编辑`xishujuzhen/UserPromptSubmit.txt`，不用改代码，下次提问立即生效。

**不要用Stop hook**：Stop hook会影响subagent（星学项目实测证实）。用 git post-commit hook 代替。

## 形式化思维规则（从星学继承，适配数学）

**核心命题**：数学本身就是一个形式系统——它有集合、算子、命题、推理规则。知识系统是数学知识在项目中的规范载体：它既保存自然语言语义、证明思路、适用条件，也显式表达集合、算子、命题和关系。

**形式化的工作方式**：

- **每条定理/引理必须可定位**：用精确的引用定位到具体文献、章节、页码，不接受"大概在某本书里"。
- **每个数学构造必须有形式定义**：群、环、域、流形、层、范畴等，必须定义输入类型、输出类型、语义。不接受"就是那种感觉"这种解释。
- **命题必须可求值**：给定一个数学实例，每条命题必须能判定为真/假/不确定。不可求值的命题是未完成的形式化。
- **知识库必须可审计**：新增数学知识必须检查与已有知识的一致性（是否矛盾？是否重复？是否归并？）。
- **形式化是一个开放过程**：不预设"形式系统长什么样"，而是让数学实践告诉我们它长什么样。

**AI 执行此规则的方式**：

当处理任何数学命题时，AI 必须问自己：
1. 这个命题的**数学对象**是什么？（群/流形/层/...）
2. 这个命题的**前提**是什么？
3. 这个命题的**结论**是什么？
4. 这个命题是否**可验证**？（给定实例能否判定真假）
5. 这个命题与已有知识库是否**一致**？


## 当前任务意识跨压缩边界保有用的一节

> **本节的用途和用法**
>
> 本节是**临时性**的，专门用于跨压缩边界保持当前活跃任务的完整工作意识。
>
> - **何时更新**：当有一个跨session的活跃任务正在进行中，且预计会跨越压缩边界时，在本节写入当前任务的完整上下文。
> - **何时清空**：任务完成后，清空本节内容（保留节标题和用法说明），把需要长期保持的认知迁移到TODO或Memory Section。
> - **与TODO/Memory Section的区别**：TODO是长期待办清单，Memory Section是长期认知基线，本节是**当前正在做什么、做到哪了、下一步是什么**的临时快照。
> - **压缩后恢复**：压缩后的AI读到本节，应能立即理解当前任务的全貌并继续工作，不需要重新探索上下文。

### 当前任务：Grove 树生长引擎（从04工作线→267号面相认知→268号交接）

**任务背景**：04工作线A/B实验完成（A组2/3突破，B组0/3），验证了检索机制有效。267号面相认知注入了认知转折点——从"让AI停下接受提示"到"系统与推理AI并行运行"。268号交接文档完整记录了04工作线成果和未来演进路径。Grove = Parallel Guided Tree Growth Engine，是这片树林的园丁——采集trajectory、整理两棵树、在节点上识别方向、启动新AI给脉络。

**当前阶段**：阶段1（串行单AI）已完成（A/B实验），准备进入阶段2（脉络注入/串行多AI）

**已完成的工作**：

1. **04工作线A/B实验**（已commit）：
   - A组突破率2/3，B组0/3，检索机制有效
   - 完整闭环验证：mitmproxy流式截获thinking → parser解析 → retrieval+policy选Q → tmux注入 → Solver接受提示
   - 4个HintInjector时序bug修复

2. **267号面相认知注入**（已commit）：
   - 核心转变：从"让AI停下接受提示"到"系统与推理AI并行运行"
   - ArangoDB表设计（tree_nodes/tree_edges/problems/ai_instances）
   - 系统工作流程详细设计（树生长引擎主循环）

3. **268号交接文档**（已commit）：
   - 跨Session/跨压缩边界完整交接
   - 必须全文加载的5个文档（M1-M5）+ 4个代码文件（C1-C4）

**下一步（Grove演进路径）**：

| 阶段 | 描述 | 状态 |
|---|---|---|
| 阶段1 | 串行单AI——thinking完成→解析→检索→选提示→注入→下一轮thinking | ✅ A/B实验已完成 |
| 阶段2 | 脉络注入——串行多AI。AI跑完（或崩溃）后系统整理脉络→检索识别方向→启动新AI给脉络继续 | **← 当前目标** |
| 阶段3 | 并发展开——多AI并发。N个AI并发，系统实时整理两棵树+分配新AI | 待实现 |
| 阶段4 | 自我增殖——树→Pattern→树。解题记录树完成后提炼Pattern存入数据基座 | 待实现 |

**阶段2需要实现的模块**：
- `path_constructor.py` — 脉络构造（从path_from_root生成给新AI的输入文本）
- `node_extractor.py` — 从trajectory提取树节点（封装DevinCliParserProvider+六元组提取）
- `tree_store.py` — ArangoDB树存储（CRUD）
- 改造`stall_detector.py` — 从"检测卡住"改为"检测终止"

**跨Session恢复指引**：
- 新Session读本节 → 知道Grove树生长引擎是当前活跃工作
- **全文加载268号交接文档**（`dev-docs/268-v0-2026-08-08-04工作线交接文档.md`）→ 完整恢复04工作线意识
- **全文加载267号面相文档**（`dev-docs/267-v0-2026-08-08-未来系统面相-系统与推理AI并行运行.md`）→ 认知转折点，读完之前不要做任何设计决策
- 读 `任务追踪/04-端到端效果验证-接真实Solver.md` → 当前工作状态和待办清单
- 读 268号§8.1 列出的M1-M5五个文档 + §8.2列出的C1-C4四个代码文件 → 安全接续工作的最低认知基线

**关键文件索引**：
- 交接文档：`dev-docs/268-v0-2026-08-08-04工作线交接文档.md`
- 认知转折点：`dev-docs/267-v0-2026-08-08-未来系统面相-系统与推理AI并行运行.md`
- 两棵树理论：`原语化AI数学工程系统设计/05-两棵树/`（01-引导展开树.md / 02-解题记录树.md / 03-系统本质-生长完整的树.md）
- 任务追踪：`任务追踪/04-端到端效果验证-接真实Solver.md`
- A/B实验脚本：`scripts/ab_experiment.py`
- solver-harness：`xishujuzhen/solver_harness/solver_harness.py`
- mitmproxy addon：`xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py`
- 实时管线：`xishujuzhen/research_runtime/realtime/pipeline.py`
- DevinCliParserProvider：`xishujuzhen/research_runtime/realtime/devin_cli_parser.py`
- Solver工作目录：`/data/grove-agents-dir/<experiment-id>/`
- trajectory存储：`/data/grove-agents-trajectory/<exp_id>/`
- Solver AGENTS.md模板：`templates/solver_agents_md.md`
- 验证run：`runs/run_20260806_{verify_001, guided_001-004, complex_001-005}/`



## TODO

> 本节记录跨 Session 需要保持的待办事项。

- [ ] **Phase 1-2**：按123号DYN阶梯和124号Check List推进（DYN-0事件捕获 + DYN-1/2状态重建与卡点检测）
- [ ] **架构调查 A/B/C**：已由 Phase 0-2 接管
- [ ] **最小启发因果POC**：对应DYN-3—DYN-5
- [ ] 设计数学领域的依赖图初始结构——由架构调查B接管
- [ ] 选型数学计算工具（SymPy / SageMath / Lean / Coq）——81号已提出SymPy→SageMath→Lean 4
- [ ] 建立第一个数学知识系统骨架（`math-notes/` 目录结构）
- [x] **大师-POC-1/2/3 完成**：POC-1边际增益+3.50/10，POC-2 +3.27/10，POC-3 L3跨领域迁移+2.6成功
- [x] **题库 Phase A 完成**：15道题42个解法，依赖图452节点393边，认知图57个认知单元
- [x] **arXiv穷尽式搜集完成**：239472篇元数据 + 1305篇HTML全文
- [x] **Phase 0 完成**：冻结legacy与统一语义，8类schema，角色隔离矩阵
- [ ] **POC-6修正版证据闭环**：原始B组依赖图存在答案泄漏，按121号方案重跑和审计
- [ ] **POC-7方向**：依赖POC-6修正版，在更多领域验证"发现型"问题增量
- [ ] **P1知识搜集**：MathLib/OEIS/数学家全集/教材/竞赛题等（109号方案剩余来源）

### POC-VMS系列（虚拟数学系统POC验证）

> 方案详见 `原语化AI数学工程系统设计/07-验证/03-虚拟数学系统POC方案.md`，进度详见 `dev-docs/257-v0-2026-08-08-POC-VMS进度追踪.md`

- [ ] **POC-VMS-0**：虚拟群论基础设施（生成器+题目+baseline）
- [ ] **POC-VMS-1**：预演模式+Pattern生成（验证缺口4）
- [ ] **POC-VMS-2**：小规模检索验证10个Pattern（验证缺口1+2）
- [ ] **POC-VMS-3**：中规模检索验证1000个Pattern（验证Rete/MiniCon scalability）
- [ ] **POC-VMS-4**：大规模检索验证10,000+Pattern（核心验证）
- [ ] **POC-VMS-5**：Pattern生成闭环验证（验证缺口4闭环）
- [ ] **POC-VMS-6**：跨域迁移验证（虚拟Pattern能否用于真实群论）

> 数据丢失修复（事件2026-08-05-A）详见 dev-docs/172。

## Memory Section

> 本节记录跨 Session 需要保持的认知。

### 虚拟数学系统方法论（POC-VMS）

构造HoTT同构虚拟数学系统，用于POC验证检索系统技术方案。核心原理：虚拟系统和真实数学结构相同（HoTT同构），AI在虚拟系统中做真实推理（逻辑推理过程真实，对象虚拟）。像虚拟世界测试自动驾驶——物理引擎虚拟，AI决策过程真实。

**关键技术映射**：
- Pattern匹配 ≅ Rete算法（alpha network=形式化粗筛，beta network=AI精筛）
- Pattern匹配 ≅ MiniCon算法（快速排除+详细检查）
- "形式化先行+AI收尾"架构已有验证（Rete/UL 100,000+规则，MiniCon大量视图）
- 辅助智能体是最后一个环节——看到形式化处理后的结构化状态+候选Pattern集合

**5个技术缺口**（四代合并后仍存在）：
1. 状态提取（形式化+AI混合，难度中）
2. 模式匹配（算法适配缺口，难度中——Rete/MiniCon已有同构方案）
3. recall检索（架构缺口，难度高——最大技术空白）
4. Pattern生成闭环（工程缺口，难度中）
5. 覆盖度（根本性缺口，难度极高——虚拟系统可快速积累Pattern缓解）

**实现路径**：虚拟群论（结构简单/证明丰富/AI有能力/可批量生成）→ 1000虚拟群×8题×6Pattern ≈ 48,000个Pattern → 大规模基座检索测试 → 跨域迁移验证（虚拟Pattern用于真实群论）

**真实难题驱动原则**（用户洞察·核心方法论）：虚拟系统不是自包含的玩具，必须被真实难题驱动——从AI做不出但有解答的真实难题中抽象挑战类型，在虚拟系统中构造同类挑战并打磨系统，最终用真实难题+大量干扰数据验证。每个VMS阶段都嵌入"虚拟→真实有效性审查"，如触发Hard Gate必须停下。详见方案文档"真实难题驱动的虚拟验证"和"虚拟→真实有效性审查机制"章节。

**认知种子**：`virtual_math_system`, `poc_vms_pipeline`（CP1加载用）

详见：`原语化AI数学工程系统设计/07-验证/03-虚拟数学系统POC方案.md` + `02-检索系统的技术缺口分析.md`

### 第一性原理重构基线（123号v1，当前最高架构与建设基线）

123号以`系统探讨.md`全文为母本，把122号v2的工程直觉严格化为可证伪、可审计的对象。本节是后续schema、POC和运行时必须服从的最高基线。

### 明确不做清单（123号第五十九节）

以下8项是项目级硬约束，任何Phase都不得违反：

1. **不先扩张到325000知识节点再验证核心闭环**——先通过DYN-0—DYN-4，证明状态可建模且最小Hint有效
2. **不把完整答案路线改写成"意识"后继续做B组提示**——这是答案泄漏的根因
3. **不用节点覆盖率代替数学正确或研究能力**——100%拓扑覆盖只证明结构保真
4. **不要求或伪造隐藏chain-of-thought**——只处理公开研究产物与工具事件
5. **不让同一Master同时持有答案、设计Hint、运行Solver和评分**——角色隔离是硬约束
6. **不把L1/L2/L3当成同一认知单元的版本号**——L1/L2/L3是提取层次，版本链独立编号
7. **不在状态空间未定义时宣称找到了同调洞**——HoTT/同调/几何方法在对象与分布假设成熟后进入
8. **不让在线一次成功自动写入production H**——candidate规则禁止在线自动提示

### 工作系统纪律（三层维护机制）

以下纪律由三层维护机制保障（CP4提示 + AGENTS.md约束 + 认知图依赖）：

1. **新术语必须追加到词汇表**：工作中产生的新术语，必须追加到工作系统词汇表（认知单元 `glossary`）。
2. **临场脚本沉淀纪律**：工作中现写的一次性脚本，如果操作模式可复用，结束后必须沉淀到 `cognition_sdk_math.py` 或对应模块（认知单元 `sdk_maintenance`）。
3. **必须 commit**：工作结束后必须 commit。commit 后 git post-commit hook 会打印 CP4 检查清单（从认知图稀疏矩阵动态查询）。
4. **不要用 Stop hook**：Stop hook 会影响 subagent（星学项目实测证实）。用 git post-commit hook 代替。
5. **认知图变更后跑回归验证**：认知图每次变更后，运行 `cognition_audit_math.py poc-regression`。
6. **边吸收边测试**（认知单元 `iterative_testing`）：每次往依赖图/认知图装入新内容后，必须立即跑测试验证。
7. **"检查依赖"触发词**：当用户说"检查依赖"时，AI 立即执行CP4检查清单中的第3、4项（`work_matrix_update` + `math_master_matrix_update`）。

## 数据丢失事件记录

数据丢失事件（2026-08-05-A，130个awareness单元清空）已移到 dev-docs/172。如需排查数据丢失问题，先读该文档。

## Handover Section

> 本节在压缩前更新，确保压缩后不丢认知。

### 工作系统实现状态（2026-08-05）

**已实现并测试通过的核心脚本**：
- `cognition_init_math.py`/`cognition_import_math.py`/`cognition_verifier_math.py`/`cognition_sdk_math.py`/`cognition_checkpoint_math.py`/`cognition_audit_math.py`
- `topo_generator.py`（经典计算展开G'_topo，1次通过100%覆盖）/ `seven_step_pipeline.py`（七步骤集成）
- `seed_recommendation_table.json` / `session_start_hook_math.py` / `user_prompt_submit_hook_math.py` / `UserPromptSubmit.txt`
- `githooks/post-commit`（CP4检查清单）/ `githooks/pre-commit`（对齐硬性检查）/ `alignment_check.py`
- `.devin/hooks.v1.json`（SessionStart + PostCompaction + UserPromptSubmit，不含Stop）

**测试结果**：工作系统测试 14/16 通过（98号报告）；反哺方案测试 10/10 通过（100号报告）。

**关键参数**：max_depth=7（数学项目路径比星学长）；git hook shebang 用绝对路径；意识节点名称映射英文cog_id↔中文node_id。

**ArangoDB状态**：
- 数据库：`grove_math`
- 认知图：35个认知单元（事件2026-08-05-A后），51条边
- 数学依赖图：dg_nodes=1719, dg_edges=1483, loops=4（Phase 0冻结值，详见126号）
- 题库：60道题159个解法；arxiv_papers：239472篇
- 5个意识节点版本链：v1(POC-1)→v2(POC-2)，current_version=v2

> 实时统计详见 `xishujuzhen/cognition_asset_index.md` 活文档。

## 术语备忘

- **xishujuzhen**：稀疏矩阵的拼音。星学项目中建立的依赖图导航系统的代号。数学项目中沿用此名，指代同一套方法论下的数学版导航系统。
- **综述博士 / 论文博士**：用户对两种大师的区分。综述博士 = 知识体系全掌握、全能灵活运用；论文博士 = 负责创新。本项目工程化综述博士。
- **AGENTS-星学版.md**：本目录中保留的星学项目完整 AGENTS.md，是方法论参考资产，不是工作对象。
