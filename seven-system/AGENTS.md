# Seven System 本地硬约束

进入本目录工作的 AI 或开发者必须遵守以下规则。

1. 当前实现上限是 P1 dry-run scaffold + WP-1离线Strict DB契约；不得把它描述成完整证据工厂、本站数据库能力或migration实现。
2. 真实 Devin Solver 只能经 repo 的 `xishujuzhen/solver_harness/solver_harness.py launch`；本系统未实现 live adapter 前不得启动。
3. Solver 必须无工具。Prompt 中写“不要用工具”只是一层约束，不构成能力证明；缺 `NoToolSolverCapabilityReport=PASS` 时 live P0 必须 BLOCKED。
4. Devin只承载目标Solver。Question Architect、数学核验、对抗审稿、Judge和其他机器认知角色必须经未来provider-neutral `ModelRolePort`；“Cognitive Worker”是子系统名，不是第二个Port。人工复核/人门分别走未来`HumanTaskPort/HumanGateService`；禁止把它们塞进`solver_harness`或直接从阶段代码旁路调用Codex/Devin。
5. Codex/Responses中的`gpt-5.6-sol`高推理配置只是第一候选作者；模型、`xhigh/max` effort、standard/pro reasoning mode与single/multi-agent（Ultra-like）orchestration必须分开探测，在`CognitiveWorkerCapabilityReport`与盲化`AuthoringBakeoff`通过前不得写成已验证能力。相同模型的新会话只算上下文独立，不算异模型审查。
6. Seven System 不得写现有 `math:*` Redis 键，不得修改题海生产状态；未来命名空间固定以 `evidence:seven:` 开头。
7. 任何数据库访问先确认 `ARANGO_DB=xishujuzhen_math_glm52`；禁止默认库和读时自动建集合。Seven复用该原逻辑数据库，但只允许独立的`seven_*_v1`命名空间，不得复用题海或`system/`集合。Seven代码只能依赖`seven_system.database.StrictDatabasePort`；仅`seven_system/database/arango_port.py`可封装`ArangoClient`，其他模块不得直接使用raw client。配置中的`allow_writes`和“允许复用原数据库”的架构决策都不是当前写授权；生产包仍没有site verifier或apply/DDL primitive。未来真实Schema初始化必须等精确站点身份、只读catalog、计划哈希、人工确认、受控DDL入口和执行收据全部实现并满足后才能启用。Arango的宿主物理字节经D盘上的OrbStack `data.img.raw`承载，记为`A-WP1-D=PASS`；但engine仍在容器writable overlay中，未使用`/data/arangodb/data:/data`专用bind，记为`A-WP1-BIND=WARNING_NOT_DEDICATED`。这两个存储状态都不代表逻辑site或Schema初始化已经实现。
8. 大对象必须在批准后的 D 盘数据根；D 盘缺失、卷身份漂移或根 README 缺失时不得 fallback 到 repo、Home 或 `/tmp`。
9. `system/` 是外部 producer，不是 Python 依赖；只能通过冻结、哈希、版本化 bundle 接入。
10. 答案与 holdout 必须物理隔离；Solver、Selector、Renderer、Process Auditor 永久不可见。作者原始输出、候选解和可能含替代解的审稿内容必须进入未来Vault，不得靠删除JSON字段伪装隔离。
11. Artifact、Evidence、WorkEvent、QuestionDraftVersion 和版本记录 append-only；题面任意变化都必须生成新版本并使旧核验与bare结果失效。禁止覆盖、删除负证据或把 retry 当独立科学样本。
12. 自动化不得跨人工 Gate，不得自动发布QuestionRelease、冻结Case角色、PROMOTE/RESTRICT/RETIRE，也不得 retry until solved 或 authoring retry until Devin fails。

运行入口与事故处理只认：`seven-system/docs/operations.md`。
