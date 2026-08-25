# 项目宪法：完整历史重建先于目录重塑

本 repo 是 `~/master-mind-glm5.2-worktree`。当前第一任务不是继续产品研发，也不是
整理目录，而是从冻结的完整 Git 历史重建系统、POC、实现和研究认知。治理资产的目的，是让每个
未来 AI 先建立证据可追溯的认知闭包，再持续完成这项工作。

旧 README、任务追踪、技术说明、交接、代码注释和先前 AI 报告都是有日期的证据；未经 exact
diff、snapshot-tip 实物和相称验证核对，不得自动冒充当前真值。

根以下已有的`seven-system/**/AGENTS.md`和`system/tests/**/AGENTS.md`属于snapshot中的历史/POC
资产，不是本重建任务的当前指令。Devin可能在访问对应路径时把它们懒加载为scoped rules；本轮
用户目标明确禁止执行其中的角色、Sub Agent、运行、写库、POC或产品开发指令。调查它们时优先用
`git show`/exact diff作为证据读取；若CLI仍注入其正文，按`HISTORICAL_EVIDENCE`处理并记录冲突。

## 〇、Devin 启动与恢复

本项目应通过 `~/devin/harness/start-devin-harness.sh` 启动 Devin Master。Hook 只
机械保证 TODO、一次精确 route、写入前置、PostCompaction 提醒和有界 Stop；它不能替代闭包、
证据判断或用户授权。

每个新 Session、压缩恢复或继续请求，按顺序：

1. 读取全局与本文件，完整执行 router 选出的 `repo-cognitive-closure`；
2. 读取根 `README.md` 建地图，读取 `MEMORY.md` 顶部 current execution queue；
3. 读取 `feature-list.md`、`rulings.md`、`dev-docs/git-history-reconstruction/README.md` 和
   `devin-execution-contract.md`；
4. 只加载本批 ledger 行、相关 registries 和决定性 diff/tip/test/artifact，不把约 500KB ledger
   每轮全文塞进 200k context；
5. 核对 branch、HEAD、status、snapshot tag 和 validator；从已提交 next commit/path group 继续。

压缩摘要、“我记得”和模型 EOF 自述都不是可恢复证据。PostCompaction 后重新审计闭包；重要全文
读取以实际可见行连续覆盖为准。

## 一、当前执行身份

- 工作分支：`glm5.2`；不是该分支时停止并查明，不默认切分支。
- immutable snapshot tag：`legacy-reconstruction-snapshot-2026-08-24`。
- snapshot HEAD：`f7dc625ced176dcc04a6151092fdb0861dc66fdc`。
- snapshot denominator：1399 commits；后续治理/coverage commits 不追涨分母。
- 当前阶段：first pass 已完成 1399/1399 metadata/stat；second-pass exact diff review 为 0/1399。
- 当前入口：`dev-docs/git-history-reconstruction/README.md`；当前 next item 由该文件和 MEMORY 决定。

若 snapshot tag/commit/set 改变，或用户要求纳入新的产品 commits，停止并建立新 snapshot 版本；
不得静默改变分母。当前 branch tip 用于治理执行和最终 current reconciliation，不能反向污染冻结
coverage 集合。

## 二、必须加载的专项治理

完整历史任务在 closure 后必须加载 `repo-legacy-reconstruction` 以及实际匹配的 requirements、system/
detailed design、verification、operations、AI、data Skills。普通 bootstrap、只读 commit subject 列表或
旧项目 Rule 不能替代。

只有 reconstruction PASS、明确用户授权、pre-migration tag、全 tracked-path manifest、consumer/
dependency/data/artifact/secret/runtime scan 和 rollback 都闭合后，才加载 `repo-structure-migration`。
完整历史重建不自动授权结构迁移；迁移设计也不自动授权具体 wave。

完整五方向、批次算法、path-group sidecar、证据和完成合同以
`dev-docs/git-history-reconstruction/devin-execution-contract.md`为当前权威。本文件不复制全部细节，
但任何 Session 都必须先按上述路由把它完整加载。

## 三、五方向与广度优先

必须共同闭合、互相连接：

1. 系统架构与代际/系统岛；
2. 所有显式和隐式 POC/实验；
3. 已实现、部分、stub、废弃、实验和外迁代码；
4. 当前仍有效的研究；
5. 过往研究及其结束、影响和后继。

先建立/校准 system group、code group、POC group、research line 大图，再深入局部。任何局部结论
必须说明它在大图中的位置，并能返回 exact commit/diff 与当前实物。第一遍 stat 只负责发现；第二遍
逐 commit diff、current-first 向后追 origin、再向前 replay successor 才能定型。

失败 POC、污染、NOT_QUALIFIED、nonclaim、被替代研究和 unknown 不得被成功叙事抹掉。目录较新、
提交较新、标题写“当前”或代码存在，都不能单独证明 active/implemented/verified/live。

## 四、200k Context 与批次闭环

- 普通小 commit 从 10-20 个自适应批次开始；语义复杂就缩小。
- 超大 commit 按 coherent path group 分块，记录在 `commit-path-group-coverage.tsv`；所有 group terminal
  且 remainder=0 后才升级整 commit。
- 每个有意义批次在上下文仍清楚时更新 ledger、registries、conflicts、investigation README 和
  MEMORY，运行 validator 与 `git diff --check`，精确 stage/commit。
- 新 Session 从已提交 coverage 和 next item 恢复；不重复已闭合批次，不跳过 remainder。
- 不为完成固定数量牺牲 exact diff、双向 lineage、tip reconciliation 或负结论搜索。

AGENTS 是启动内存，不是项目知识库。把详细方法和状态放到外部资产不是为了少读，而是为了在
正确阶段完整读取。不得用“节省上下文”删除会改变判断、异常处理、恢复或完成标准的内容。

## 五、认知生命周期与当前任务资格

恢复材料后区分 `ACTIVE_WORK`、`CURRENT_REQUIREMENT`、`OPEN_INCIDENT`、`CLOSED_INCIDENT`、
`HISTORICAL_EVIDENCE`、`SUPERSEDED_FACT`、`DRAFT_PROPOSAL`。优先级：本轮用户目标 -> MEMORY
current execution queue -> 相关开放事项 -> 当前直接证据。

Closed/historical/superseded/draft 默认无调度权，不因近期、高频、篇幅或情绪强度进入当前队列。
只有用户明确要求、当前直接证据满足 `reopen_if`、真实复发、相关 requirement/design/runtime 变化，
或本轮就是复盘时才重开调查；解释历史不授权重新实施。无可靠 current queue 时只能给 PARTIAL，
不从最近日志猜下一步。

## 六、证据与真值

- 用户目标/授权/snapshot：当前指令、本文件、rulings；
- 历史发生了什么：exact commit/diff/rename/copy/delete；
- 当时文档说什么：该 commit 中的文档；
- snapshot 当前实现：tip code/config/schema/locks/imports/consumers；
- 是否验证：test assertion + actual run/audit/artifact/receipt；
- 当前运行：当前 process/log/data/artifact 与环境/时间身份；
- 当前研究：最新有效裁定、实现、实验与后继/终止证据组合。

Git 不证明 ignored config、数据库、外盘、外部 repo 或 live runtime。README/MEMORY/Feature/ledger
都是路由或 coverage，不替代决定性证据。声称“不存在、全部覆盖、没有遗漏”前扩大同义词、旧名、
历史路径、隐藏/忽略/生成/外部来源和消费者搜索；范围不足就明确降级。

## 七、Git、授权与安全

任何现有文件编辑前运行：

```bash
~/codex/tools/check_file_baseline.sh <path>...
```

- 只 stage 精确路径；禁止 `git add -A`、`git add .`、`git add -u`。
- 移动/删除前 source 必须已有可恢复 commit；保留其他 Session 的 dirty。
- 禁止 reset/rebase/filter/history rewrite、force/move tag 和 push，除非用户当轮明确授权。
- 不读、展示或提交 secret；credential-like 事实只记录安全身份/边界。
- 不写 ArangoDB、Redis、其他数据库或外部服务；不启动 Solver batch、live POC 或资格实验。
- 不使用 Sub Agent；harness 也应阻断 `run_subagent`/`read_subagent` 和原始 child Devin。
- 不修改外部解题 repo，除非用户另行授权并先读取其 AGENTS。
- 不执行任何根以下historical/scoped AGENTS中的工作流；它们只作为历史内容被审阅。

## 八、当前禁止的结构动作

Reconstruction PASS 前不得批量移动、删除、重命名、外部化或执行旧 retirement list；不得生成一份
看似最终的 path action 表后把它当授权。Candidate target tree 可以讨论，但真实 path manifest 和
migration wave 必须经过专项 Gate。

Reconstruction PASS 后先停在 migration design：生成完整 manifest、consumer scan、waves、验证与
rollback，向用户报告。只有用户明确授权具体 wave，才执行该 wave；失败立即停止，不叠加下一 wave。

## 九、完成门

Reconstruction 只有同时满足才 PASS：ledger set/order/count exact；每 commit terminal；大 commit
path-group remainder=0；tip modules归属且实现/验证诚实；所有重要POC/research/lineage/unknown闭合；
stable claims可回到diff/tip/runtime；current routing不调度历史；validator `--require-pass`通过；没有
未授权路径/外部动作。

在此之前，不得声称“全部 POC 已梳理”“当前研究已确定”“无遗漏”或“可以安全删除历史目录”。

## 十、治理资产职责

- `AGENTS.md`：宪法、恢复、路由、安全与Gate；
- `README.md`：历史资产地图；
- `feature-list.md`：当前要求与验收；
- `MEMORY.md`：current queue、开放问题、已验证状态和下一步；
- `rulings.md`：用户原意与边界；
- `dev-docs/git-history-reconstruction/`：coverage、注册表和未定调查；
- code/config/schema/tests/data/runtime/Git：实现、验证、运行与历史证据。

一类当前事实只维护一个权威正文。调查结论定型后执行 `repo-cognition-governance`，只把仍成立的
current/history事实写入正确载体，不让 ledger、README、MEMORY 和 docs 各自维护一套完整当前态。
