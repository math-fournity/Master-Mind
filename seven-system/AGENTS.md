# Seven System 本地硬约束

进入本目录工作的 AI 或开发者必须遵守以下规则。

1. 当前实现上限是 P1 dry-run scaffold + WP-1离线Strict DB契约；不得把它描述成完整证据工厂、本站数据库能力或migration实现。
2. 真实 Devin Solver 只能经 repo 的 `xishujuzhen/solver_harness/solver_harness.py launch`；本系统未实现 live adapter 前不得启动。
3. Solver 必须无工具。Prompt 中写“不要用工具”只是一层约束，不构成能力证明；缺 `NoToolSolverCapabilityReport=PASS` 时 live P0 必须 BLOCKED。
4. **只有目标Solver作业可以进入`solver_harness`；Devin CLI并不专属于Solver。** Question Architect、数学核验、对抗审稿、Judge和其他机器认知角色统一经provider-neutral `ModelRolePort`；其中必须同时允许独立的`DevinCliModelRoleAdapter`与`CodexExecModelRoleAdapter`。Devin认知adapter不得复用Solver的port、workspace、session、AGENTS、能力报告、收据或资源池。人工复核/人门分别走未来`HumanTaskPort/HumanGateService`；禁止阶段代码旁路调用任何CLI。
5. Devin认知角色的首个精确候选为`--model glm-5-2`，本机catalog将其标为`GLM-5.2 High`，High编码在model UID而不是独立`--effort`参数中；Codex/Responses中的`gpt-5.6-sol`高推理配置是并列候选。两者都必须按角色和精确profile分别探测requested/effective模型、effort、mode、orchestration、工具/网络/沙箱、事件、成本与隔离，并通过资格测试；盲化`AuthoringBakeoff`只能选择角色默认profile，不能禁止其他已合格adapter。相同模型的新会话只算上下文独立，不算异模型审查。
6. Seven System 不得写现有 `math:*` Redis 键，不得修改题海生产状态；未来命名空间固定以 `evidence:seven:` 开头。
7. 任何数据库访问先确认 `ARANGO_DB=xishujuzhen_math_glm52`；禁止默认库和读时自动建集合。Seven复用该原逻辑数据库，但只允许隔离且显式版本化的`seven_*_vN`命名空间（`N`为正整数），不得复用题海或`system/`集合，也不得创建无版本Seven集合。Seven代码只能依赖`seven_system.database.StrictDatabasePort`；仅`seven_system/database/arango_port.py`可封装`ArangoClient`，其他模块不得直接使用raw client。配置中的`allow_writes`和“允许复用原数据库”的架构决策都不是当前写授权；生产包仍没有site verifier或apply/DDL primitive。未来真实Schema初始化必须等精确站点身份、只读catalog、计划哈希、人工确认、受控DDL入口和执行收据全部实现并满足后才能启用。Arango的宿主物理字节经D盘上的OrbStack `data.img.raw`承载，记为`A-WP1-D=PASS`；但engine仍在容器writable overlay中，未使用`/data/arangodb/data:/data`专用bind，记为`A-WP1-BIND=WARNING_NOT_DEDICATED`。这两个存储状态都不代表逻辑site或Schema初始化已经实现。
8. 大对象必须在批准后的 D 盘数据根；D 盘缺失、卷身份漂移或根 README 缺失时不得 fallback 到 repo、Home 或 `/tmp`。
9. `system/` 是外部 producer，不是 Python 依赖；只能通过冻结、哈希、版本化 bundle 接入。
10. 答案与 holdout 必须物理隔离；Solver、Selector、Renderer、Process Auditor 永久不可见。作者原始输出、候选解和可能含替代解的审稿内容必须进入未来Vault，不得靠删除JSON字段伪装隔离。
11. Artifact、Evidence、WorkEvent、QuestionDraftVersion 和版本记录 append-only；题面任意变化都必须生成新版本并使旧核验与bare结果失效。禁止覆盖、删除负证据或把 retry 当独立科学样本。
12. 自动化不得跨人工 Gate，不得自动发布QuestionRelease、冻结Case角色、PROMOTE/RESTRICT/RETIRE，也不得 retry until solved 或 authoring retry until Devin fails。
13. 完整文档总入口与实施者入口是`seven-system/docs/implementation/README.md`；未来独立审计者从`seven-system/docs/audit/README.md`开始，再回读被冻结的实现规范与CompletionBundle。实施者最高只能把工作包标为`READY_FOR_AUDIT`，不得给自己的实现签`AUDITED_PASS`。
14. 上游`READY_FOR_AUDIT`可以支持下游无副作用开发，但必须继承审计债；真实DB、远程模型、Target Solver、正式HumanGate、canonical P0–P9和科学Evidence属于激活动作，必须有上游`AUDITED_PASS`，或父级EEA精确绑定该次未审canary；每个具体副作用还必须持有不可扩权LiveRunPermit和原子额度预留收据。实施AI最终只能交付`SYSTEM_CANDIDATE_READY_FOR_EXTERNAL_AUDIT`。

运行入口与事故处理只认：`seven-system/docs/operations.md`。
