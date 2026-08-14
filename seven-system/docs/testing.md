# 测试说明

## 一句话结论

当前测试证明 P0/P1 scaffold和WP-1 Strict DB离线契约在隔离环境中fail-closed；测试不得连接真实 DB、Redis、Devin CLI（无论Solver还是认知角色）、Codex或其他远程模型。只有显式的报告CLI会把验证后的本地JSON append-once提交到批准的D盘根。

## 运行全部测试

```bash
SEVEN_WORKSPACE_ROOT="$(git rev-parse --show-toplevel)"
cd "$SEVEN_WORKSPACE_ROOT"
.venv/bin/python -m unittest discover -s seven-system/tests -p 'test_*.py' -v
```

测试全部使用 Python 标准库和 `TemporaryDirectory`，不需要安装新依赖。独立迁出后从Seven repo根使用`python3 -m unittest discover -s tests -p 'test_*.py' -v`。

2026-08-14 对当前共享树实跑结果：隔离runner `tests_run=20, successful=true`；全量`Ran 58 tests ... OK`。

## 当前覆盖

| 测试 | 保护的不变量 |
|---|---|
| `test_hashing_and_storage.py` | JSON 顺序/换行不改变哈希；同内容幂等；异内容绝不覆盖 |
| `test_preflight.py` | dry-run 无 DB；数据根不能在 repo；专属namespace；能力subject/claims/checks绑定；live 始终 BLOCKED |
| `test_epoch.py` | Epoch初建返回前自验与重入；PASS/FAIL Gate均可重放；两级seal+外部receipt；Schema科学非主张；manifest/verdict/report篡改、重算index、非对象JSON、旧P0漂移和symlink逃逸被拒绝 |
| `test_repository_assets.py` | 示例配置可读且真正执行Schema/拒绝未知字段；Solver 资产禁工具且无答案占位符；Schema 是合法 JSON |
| `test_database_environment.py` | 缺/错DB在client前拒绝；连接后再核对当前库；secret不泄漏；raw driver不可绕过；未知/Unicode集合不触达driver；read path不建Schema |
| `test_database_spec.py` | 7集合白名单、13唯一索引、canonical spec hash和Strict/Site subject永久分离 |
| `test_database_migration.py` | fake catalog上的只读确定性plan、非canonical/冲突/额外索引拒绝；生产模块与顶层package都不存在apply/DDL/authorization/receipt primitive |
| `test_database_contract_report.py` | caller不能注入PASS/evidence/receipt，builder不接收时间参数；Schema+语义验证；实现树绑定；畸形合法JSON、篡改、重复check、删除nonclaim、sitecustomize/PYTHONPATH注入和symlink逃逸均拒绝；verifier只验时间格式，报告仅在Seven API层append-once |

## 安全断言

测试期望：

- P0/P1命令不连接DB、不启动Solver、不写Redis；
- P0/P1命令不调用Codex/API或任何认知Worker；
- Strict DB报告通过`python -I -S -B`运行只输出机器JSON的固定runner，不继承`PYTHONPATH`、sitecustomize或`ARANGO_*`凭据；收据绑定完整test IDs，allowlist与索引语义测试是required evidence；报告中的DB connection/write、migration、container restart、Redis write和Solver launch均为0；
- 真实Arango adapter只提供只读catalog能力，不暴露raw client或DDL primitive；
- 临时测试卷含自己的 README；
- 所有运行数据只写临时目录；
- 普通单元测试结束由临时目录生命周期回收；只有显式`wp1-db-contract-report`会写批准的D盘capability报告。

当前离线报告绑定的受控DB测试收据是`055ac2d9d9479663b529888295701ddc7f347830bfbbb1372ece775534e4533a`。隔离runner 20项PASS和全量58项PASS是两个口径，不能相互替代。

## 测试没有证明什么

- 没证明 ArangoDB transaction/CAS；
- 本套单元测试没有证明Arango engine数据位于D盘；当前`A-WP1-D=PASS`来自独立的宿主symlink、实时`data.img.raw`和卷设备只读核验，不能归功于测试；
- 没证明真实集合/索引已经创建，也没证明migration durable ledger/fence/resume；
- 没证明runtime append-only/CAS/outbox delivery，也没认证wall-clock或本地文件不可变性/WORM；
- 没证明 Redis lease/fencing；
- 没证明现有 Harness 真正关闭了工具表面；
- 没证明`TargetSolverPort`、`ModelRolePort`、`DevinCliModelRoleAdapter`、Codex adapter、`HumanTaskPort`或`HumanGateService`已经实现；
- 没证明Codex GPT-5.6、任何推理强度或多智能体编排在本站可用，也没证明其出题优于其他载体；
- 没证明同模型新会话构成异模型/异provider审查；
- 没证明 answer Vault 隔离；
- 没证明 artifact bundle 两阶段 seal；
- 没证明任何数学 proof 或 Tell 效果；
- 没证明高并发吞吐或长期无人值守。
- 没证明387号完整P1的崩溃、lease/fencing、outbox与reconcile矩阵。

这些都必须在后续独立工作包中增加 contract/integration/security/fault-injection 测试，不能用当前单元测试替代。

## 下一阶段测试矩阵

后续至少补：

1. 先新增逻辑站点v2合同与semantic verifier，再对原逻辑数据库做identity/current DB/principal/catalog只读核验；
2. 对`seven_*_v1`做零写入Schema计划与冲突检查；实际Schema初始化另需人工授权、durable ledger、fence、崩溃resume/reconcile和故障注入；
3. 若把Arango从容器writable overlay改为专用bind/volume，作为独立运维硬化测试线验证备份、停机、回滚和容器重建；不要把它称为“迁到D盘”，也不阻塞前两项；
4. Harness 只靠 Prompt 禁工具必须 capability FAIL；
5. `trajectory.jsonl` 缺失/损坏必须 `invalid_observability`；
6. 任意 tool call 对所有终态独立否决；
7. 重复 dispatch 100 次只能产生一个 LaunchReceipt；
8. 旧 fence 晚提交必须被拒；
9. CAS 已提交/DB 未提交可 reconcile；反向缺 CAS 必须 quarantine；
10. Process/Proof/Leakage view 的越权字段必须构建失败；
11. 无人工决定必须永久 `HUMAN_PENDING`；
12. Evidence Index 反查到 RunArtifact 的集合对账 remainder=0。
13. Cognitive Worker能力探针必须核对requested/effective carrier、model、reasoning effort、reasoning mode、orchestration、工具/网络/sandbox策略和原始事件流；一条profile PASS不得解锁未测组合，不匹配即BLOCK。Devin认知候选还必须核对`glm-5-2`精确UID、catalog快照、每个generation-bearing step的generation model、独立workspace/session/config以及“从不调用solver_harness”。
14. Question Architect、Adversarial Editor、Math Verifier与Proof Judge的view越权、session/workdir复用或缺`ReviewIndependenceRecord`必须失败。
15. QuestionDraft任意文本变化必须使旧候选解、审稿、VerificationDossier和bare结果失效；原地改题测试必须BLOCK。
16. 每个AuthoringBrief达到最大草稿/修订数后必须停止，拒绝`retry until Devin fails`；所有失败草稿和成本仍在Evidence Index中。
17. 在相同MechanismContract/CoverageCell下对Devin `glm-5-2` High、Codex及其他合格profile做两段盲化Authoring Evaluation：QA0的Bakeoff-A不启动Target Solver，只评数学正确、机制忠实、正交距离、捷径/泄漏、多样性和成本；QA1的Bakeoff-B只对已发布不可变calibration releases增加bare准入指标，且不得回流改题。两段calibration都不得进入确认性Evidence。
18. 自然题`P2A→按需P2B→P3N→P3C`与生成题`P3A→P3B→P3C`分别做DAG/remainder测试；P2B/P3B必须是problem-only bare、禁止Tell/Hint，判定层只产BareQualificationResult（物理产物仍含RunArtifactBundle/BareBaseline）且不得计为P5样本；AdmissionDecision只能由P3C签名人门产生。历史物证不足时必须触发P2B或保持discovery-only。
19. 相同Role job重复dispatch只能产生一个`RoleInvocationAttempt`；provider request已接受/生成状态未知时必须quarantine而非重呼，reattach与旧fence cancel/commit都要故障注入。
20. Architect、Editor、Verifier、Proof Judge和Leakage Auditor的solution-bearing raw request/event/output必须进入受限Vault；普通ledger只允许ref/hash，越权sink构建失败。
21. `ModelRolePort`不得签发`HumanGateDecision`；缺HumanGate policy、授权actor roster、职责分离证据、有效签名/验签或readiness时必须保持`HUMAN_PENDING/BLOCKED`。
22. Bakeoff calibration pack不得进入P5/P7确认性证据；默认adapter必须在未见brief qualification pack复验。
23. AI调用收据必须冻结provider原始usage、币种、价格表hash、成本算法版本；multi-agent child/topology不可观察时必须显式`UNOBSERVABLE`，不能伪造分项成本。

完整后续测试与故障注入矩阵见`docs/implementation/10-testing-and-fault-injection.md`；未来独立审计从`docs/audit/README.md`开始。
