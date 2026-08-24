# 项目宪法：从完整 Git 历史重建数学大师制造系统认知

本文件是 `~/master-mind-glm5.2-worktree` 的项目宪法，也是后续 Session 的强制
工作指南。用户于 2026-08-24 明确裁定：在继续目录重组、文件退役或第六代现状 repo 建设前，
必须先从目标分支完整 Git 历史倒序重建项目认知。

任何旧 README、任务追踪、技术说明、交接文档、代码注释或先前 AI 报告，都只能作为有日期的
证据来源；未经 Git diff、当前代码和直接验证证据核对，不得自动冒充当前真值。

## 一、最终目标

最终目标不是简单清理目录，也不是把旧文件机械搬到新位置，而是重建一套完整、一致、可审计的
第六代系统现状 repo，使未来 AI 看见的系统认知与目标分支真实历史完全一致。

最终结果必须同时满足：

1. 能从高层架构逐步进入组件、代码、POC、研究问题和原始证据；
2. 当前目标、当前实现、已验证能力、正在研究内容、历史研究和已废止路线彼此不混淆；
3. 历史上形成的重要概念、设计选择、失败、反例和替代关系都可回到具体 commit、diff 和实物；
4. 任何文件迁移或退役都建立在语义认知完成之后，不因目录清爽而丢失有效知识；
5. 后续目录治理看起来可以像项目从第一天就在治理框架下开发，但不得改写 Git 历史来伪造这种
   外观；
6. 新 Session 能只依赖 repo 内落盘资产，恢复调查边界、进度、证据和下一步。

在五个认知方向尚未全面闭合前，目录重塑只是候选后续动作，不是当前第一任务。

## 二、工作标的与 Git 边界

### 2.1 唯一目标分支

- 用户口头所称的 `glm-5.2`，在本 repo 中真实 Git ref 名是 **`glm5.2`**。
- 后续历史重建的唯一目标分支是 `glm5.2`。
- 开始或恢复工作时必须先运行 `git branch --show-current`；不是 `glm5.2` 时停止实质工作并查明原因。
- 不默认新建分支，不切到先前治理分支继续删除；只有新的用户明确指令可以改变工作分支。

### 2.2 历史锚点

- 原始产品开发 tip：`08ad266e9e3506d4d57fba372cef91516070459b`。
- 原始工作区封存提交：`c1b934ab56d6f0554c7a7e9d89bb8b5d66b6baaa`。
- 封存 tag：`pre-governance-alignment-2026-08-24`。
- 本宪法提交以后，`glm5.2` 会继续向前；调查快照必须记录当时的完整 HEAD，而不能把上述锚点
  错写成永远不变的当前 HEAD。

必须分析 `glm5.2` 可达的全部 commits，包括根提交、原始产品 tip、基线封存提交和后续治理提交。
分析对象是目标分支历史，不是 `git log --all` 混入其他实验分支后的合集。

### 2.3 先前治理分支的身份

- `codex/governance-alignment-2026-08-24`
- `codex/sixth-gen-current-repo-2026-08-24`
- `pre-sixth-gen-current-repo-2026-08-24`

这些 ref 保存先前治理尝试和可恢复工作，只能在独立完成目标分支调查后用于交叉检查。不得把其中
的摘要、分类或删除计划直接当成 `glm5.2` 的权威结论，也不得继续执行先前暂停的批量退役。

禁止 reset、rebase、filter、强制移动 tag 或其他 Git 历史改写。禁止 push，除非用户当轮明确授权。

## 三、必须全面重建的五个认知方向

五个方向是同一系统的五个观察面，必须互相连接，不能各写一份彼此不一致的故事。

### 3.1 系统架构

需要恢复：

- 每个时代系统试图解决什么问题；
- 系统边界、组件、角色、Pipe、数据流、控制流、两棵树、Trace/Tell/Hint、Grove、VMS 等概念
  如何形成和变化；
- 当前目标架构与当前实际架构分别是什么；
- 哪些组件已经接线，哪些只是设计、stub、实验工具或外部 repo；
- 代际继承、分叉、合并、替代和退役关系；
- 数据库、D 盘、Prompt、模型角色、外部 Solver、运行目录和证据目录的边界。

系统架构结论必须能回到定义它、修改它、否定它或实现它的 commits 和当前代码。

### 3.2 过往的所有 POC

需要找出所有显式或隐式实验，不只搜索文件名中的 `POC`：

- `POC-*`、`VMS-*`、canary、qualification、baseline、A/B、dry-run、audit、验证轮次、真实运行和
  没有正式编号的实验；
- 每个 POC 的问题、假设、输入、版本、Prompt/模型/工具、样本、执行方式、产物和判定标准；
- PASS、FAIL、PARTIAL、INCONCLUSIVE、ABORTED、NOT_QUALIFIED 等原始 verdict；
- 正向结果、失败、事故、污染、泄漏、协议缺陷和负向证据；
- 它验证了什么、没有验证什么、后来被哪个实验或设计取代；
- 对架构、代码和研究方向产生了什么实际影响。

失败 POC 和未达门槛的实验不能因最终目录重塑而消失，也不能被后来的成功叙事改写。

### 3.3 已经实现的代码

需要恢复：

- 每个 current 或 historical 模块何时引入、为何引入、经历过哪些关键变化；
- 实际实现、部分实现、stub、废弃实现、迁出外部 repo 和纯实验脚本的区别；
- 代码与架构组件、POC、研究问题、Prompt、配置、schema、数据和测试的对应关系；
- 当前 `glm5.2` tip 上真正存在且可调用的行为；
- 单元测试、离线验证、一次运行、live 资格和生产能力各自能证明到哪里；
- 删除、重命名和迁移后的替代路径与消费者状态。

代码存在只证明代码存在。当前行为回到 branch tip 的代码/config/schema；验证状态回到真实测试和
运行实物，不能从文档标题反推。

### 3.4 正在进行的研究

需要恢复当前仍然有效的研究线：

- 当前研究问题、目标、假设、未决冲突和下一步；
- 最近且未被替代的计划、任务追踪和用户裁定；
- 正在使用的代码、Prompt、POC、数据和证据；
- active、paused、blocked、candidate、待用户裁定等状态；
- 与第六代当前系统目标的关系。

“提交时间较新”“文档写着进行中”或“目录仍存在”都不足以证明研究仍 active。必须检查后续 commit
是否完成、否定、暂停、迁出或替代它。无法从历史决定的内容标为有证据的 unknown，不能猜测。

### 3.5 过往进行的研究

需要恢复所有重要历史研究线：

- 研究问题的起点、阶段、关键发现、失败和终点；
- 最终状态：completed、failed、abandoned、superseded、split、merged、externalized 或 unknown；
- 对后续架构、POC、代码和术语的影响；
- 后继路线、替代文档、外部 repo 或仅 Git 可恢复的结束状态；
- 今天仍应保留的教训与不再参与当前设计的历史内容。

历史研究不是当前 TODO，但它必须足以解释“为什么当前系统变成这样”。

## 四、工作顺序：从高到低，再回到底层证据

本任务采用语义优先、广度优先的顺序：

1. 先对目标分支全部 commits 做全景普查，建立时间轴和五方向粗分类；
2. 建立系统代际、架构组件和研究线的高层总图；
3. 为每个架构组件连接相关 POC、实现代码、当前研究和历史研究；
4. 再逐 commit、逐 diff 深化字段和证据；
5. 用 branch tip 的代码、测试和实物重建当前态；
6. 最后才做路径归属、目录设计、迁移和退役。

文件清单和 path migration map 是最终无遗漏审计工具，不是理解项目的第一主轴。不得再次从几千个
路径的删除动作开始，反过来猜测系统语义。

## 五、倒序分析完整 Git Log 的强制工作法

### 5.1 冻结调查快照

每轮正式调查开始时记录：

```bash
git status --short --branch --untracked-files=all
git branch --show-current
git rev-parse HEAD
git rev-list --count glm5.2
git log -1 --format=fuller glm5.2
```

将 snapshot HEAD、commit 总数、时间和工作树状态写入调查入口。若调查期间 `glm5.2` HEAD 改变，
先判断新 commits 是否使原进度失效，再扩展快照；不能静默改变分母。

### 5.2 建立一行不漏的 commit 总账

按 newest-to-oldest 顺序枚举 `glm5.2` 可达全部 commits。总账至少包含：

```text
ordinal
commit
parents
author_date
committer_date
subject
changed_path_count
architecture_impact
poc_impact
implementation_impact
active_research_impact
historical_research_impact
review_status
notes
```

每个 commit 恰好一行。`review_status` 至少区分 `metadata-only`、`stat-reviewed`、`diff-reviewed` 和
`blocked`。最终完成要求所有 commits 都达到 `diff-reviewed`，或有具体、可审计的 blocked 原因。

禁止每个 commit 建一个文档；使用总账和按实体组织的注册表。

### 5.3 Commit message 只负责发现，diff 才能决定事实

对每个 commit 至少检查：

```bash
git show --find-renames --find-copies --stat --summary --format=fuller <commit>
git diff-tree --root --no-commit-id --name-status -r -M -C <commit>
git show --find-renames --find-copies --format=fuller <commit> -- <relevant-paths...>
```

必须回答：

1. 提交者声称做了什么；
2. 实际增加、修改、删除、移动了什么；
3. 修改前后的语义差异是什么；
4. 它影响五个方向中的哪些方向；
5. 它引入、修正、否定、完成或替代了哪些实体；
6. 它留下哪些未实现、未验证或冲突项；
7. 哪些结论需要继续查看后续或更早 commits 才能成立。

大型提交不能只读 subject 或 `--stat`。可以按组件分批审阅 diff，但总账必须记录覆盖范围和剩余项。
二进制、生成物和大运行产物至少记录路径、身份、hash/manifest、所属 POC 和可恢复位置。

### 5.4 倒序分析时的时间语义

倒序从当前向过去阅读，先看见的是较新的结论。遇到更老说法时：

- 不用旧说法覆盖新结论；
- 记录它是当前概念的来源、旧版本、竞争路线还是已被否定方案；
- 找到真正完成替代的 commit，而不是仅凭编号或日期推断；
- 同时保留目标设计和当时实际实现；
- 对改名、移动、拆分和外迁建立 alias 与 lineage。

如果倒序阅读发现“当前结论没有来源”，继续向前追溯到首次引入；如果发现后续结论没有落到代码，
状态只能是 documented/design，不得写成 implemented。

### 5.5 五方向实体提取

审阅 commit 后，将结论归入以下唯一职责资产：

```text
dev-docs/git-history-reconstruction/
├── README.md
├── commit-ledger.tsv
├── system-architecture.md
├── poc-registry.tsv
├── implementation-registry.tsv
├── research-registry.tsv
└── unresolved-conflicts.md
```

这些是调查阶段资产；稳定结论以后再按治理框架进入 README、Feature、MEMORY、rulings 和 docs。

`poc-registry.tsv` 至少记录：POC ID/aliases、问题、组件、协议、实现 commits、run/artifact、verdict、
证据上限、失败、替代关系和 unknown。

`implementation-registry.tsv` 至少记录：架构组件、代码路径、引入 commit、最后关键变更、branch-tip
状态、实现程度、消费者、测试/运行证据和历史替代。

`research-registry.tsv` 同时登记 current 和 historical 研究：研究线 ID、问题、起止 commits、最后
有效状态、相关 POC、架构/代码影响、后继路线和证据。当前活跃项以后只在 MEMORY 保留摘要和指针，
不得维护两份完整 current 状态。

`system-architecture.md` 从高到低描述代际、组件和当前/目标边界，并链接三个注册表；它不能用理想
架构覆盖 branch-tip 实现缺口。

### 5.6 两遍法提高速度但不降低完整度

第一遍对全部 commits 读取 metadata、message、changed paths 和 stat，快速建立五方向全景、别名和
高价值转折点。第二遍仍按倒序逐 commit 检查实际 diff，优先从架构转折、POC verdict、代码接线和
研究状态变化处向上下游展开，最终补齐所有普通 commits。

第一遍用于发现和路由，不能作为“完整分析”结论；只有第二遍 diff coverage 对账后才能宣布完成。

## 六、证据与冲突规则

按事实类型使用权威，不使用一条粗暴的全局优先级：

- 当前用户目标、分支和授权：本文件及最新用户明确指令；
- 历史发生了什么：目标分支的 exact commit/diff；
- 当前实现是什么：`glm5.2` snapshot tip 的代码、配置和机器 schema；
- 是否验证：测试断言、真实执行结果、run artifact、receipt 和审计；
- 文档当时声称什么：该文档在对应 commit 的内容；
- 当前研究状态：最新未被替代的用户裁定、计划、实现和证据的组合；
- 先前治理分支：交叉检查线索，不是目标分支真值。

必须区分 `documented`、`designed`、`implemented`、`offline-verified`、`live-observed`、`qualified`、
`historical` 和 `superseded`。

来源冲突时记录双方、commit、事实类型、时效和裁决理由。无法裁决的 unknown 必须说明搜索范围和
对结论的影响；不得把“没有看到”写成“不存在”。

## 七、完成门

只有同时通过以下检查，五方向历史重建才算完成：

1. commit 总账行数等于冻结 snapshot 的 `git rev-list --count glm5.2`，commit 集合完全一致；
2. 每个 commit 已检查实际 diff，或有具体 blocked 证据；
3. 每个架构组件都有来源、演进、当前/目标状态和实现/证据入口；
4. 每个显式或隐式 POC 都进入注册表，原始 verdict、失败和 nonclaim 未丢失；
5. branch-tip 每个项目代码模块都归属于架构组件，并标明实现和验证状态；
6. 每条 current research 有最新有效依据、开放问题和下一步；
7. 每条重要 historical research 有起止、最终状态、影响和恢复入口；
8. 所有 superseded/renamed/moved/externalized 关系有 old/new identity 和 commit；
9. 所有 unknown 都有明确原因、已查范围和是否阻塞，不存在未解释遗漏；
10. 从五个方向分别抽样回到 commit/diff、代码、测试和 artifact，结论一致；
11. 才允许生成最终路径处置表；任何待退役路径必须已经由当前真值、历史注册表或 exact Git pointer
    覆盖，不能存在 orphan concept、orphan POC 或 orphan research line。

完成前不得声称“全部 POC 已梳理”“当前研究已确定”“无遗漏”或“可以安全删除历史目录”。

## 八、跨 Session 续做协议

新 Session 必须按以下顺序恢复：

1. 完整读取本 `AGENTS.md`；
2. 确认分支是 `glm5.2`，读取 status、HEAD 和 commit count；
3. 读取根 `README.md` 作为历史导航，但不把其中未核验状态当成当前真值；
4. 若 `dev-docs/git-history-reconstruction/README.md` 尚不存在，先创建第五节规定的调查入口和空账本，
   冻结首个 snapshot；若已存在，读取其中的 snapshot、进度和 next commit；
5. 读取 commit 总账中最后一个已完成批次及相应五方向注册表；
6. 检查 HEAD 或关键资产是否变化；变化则先审计闭包是否失效；
7. 从明确记录的 next commit 继续，不重做整段，也不跳过未完成 diff；
8. 每个有意义批次更新进度、覆盖计数、冲突和五方向资产，并使用显式 pathspec commit。

进度入口必须记录 snapshot HEAD、总 commit 数、已 stat-reviewed、已 diff-reviewed、blocked、next commit
和本批提交范围。不得依赖聊天记忆或“上一个 AI 应该看过”。

## 九、当前禁止事项与安全边界

- 在五方向认知闭合前，不批量删除、移动或重命名历史目录和文件；
- 不执行先前治理分支中暂停的 retirement path list；
- 不写 ArangoDB、Redis 或其他数据库；
- 不启动 Solver 批次、Devin/tmux live POC、模型资格实验或外部运行系统；
- 不使用 subagent，除非先向用户解释策略并取得明确同意；
- 不读取、展示或提交 secret；credential-like 内容只记录存在和风险，不复述值；
- 不修改两个外部解题 repo，除非用户另行指定并先读取各自 AGENTS；
- Git 只 stage 精确路径，禁止 `git add -A`、`git add .` 和 `git add -u`；
- 不 push，不改写历史，不覆盖 tag，不把未提交源移动或删除。

任何现有文件编辑前执行：

```bash
~/codex/tools/check_file_baseline.sh <path>...
```

调查本身优先只读。需要创建调查资产时，先建立最小完整入口，再广度优先填充五方向，不在一个
局部 POC 或一个组件上无限深挖后才开始其他方向。

## 十、本宪法的成功标准

本宪法不是为了增加流程，而是为了让未来 AI 更快、更完整地理解项目。若后续工作不能回答下面
五个问题，就说明仍未完成：

1. 第六代系统的目标架构和当前实际架构分别是什么，怎样从历代系统演化而来？
2. 历史上做过哪些 POC，每个 POC 真正证明了什么、失败了什么、影响了什么？
3. 当前到底实现了哪些代码，接线和验证到什么程度？
4. 哪些研究今天仍在进行，证据和下一步是什么？
5. 历史上研究过什么，它们为何结束、被什么替代、给当前系统留下什么？

所有回答必须能沿注册表返回 exact commit/diff 和底层实物。满足这一点以后，才进入最终治理结构、
目录重塑和历史内容退役。
