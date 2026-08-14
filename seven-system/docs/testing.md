# 测试说明

## 一句话结论

当前测试证明 P0/P1 scaffold和WP-1 Strict DB离线契约在隔离环境中fail-closed；测试不得连接真实 DB、Redis 或 Devin CLI。只有显式的报告CLI会把验证后的本地JSON append-once提交到批准的D盘根。

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
- Strict DB报告通过`python -I -S -B`运行只输出机器JSON的固定runner，不继承`PYTHONPATH`、sitecustomize或`ARANGO_*`凭据；收据绑定完整test IDs，allowlist与索引语义测试是required evidence；报告中的DB connection/write、migration、container restart、Redis write和Solver launch均为0；
- 真实Arango adapter只提供只读catalog能力，不暴露raw client或DDL primitive；
- 临时测试卷含自己的 README；
- 所有运行数据只写临时目录；
- 普通单元测试结束由临时目录生命周期回收；只有显式`wp1-db-contract-report`会写批准的D盘capability报告。

当前离线报告绑定的受控DB测试收据是`055ac2d9d9479663b529888295701ddc7f347830bfbbb1372ece775534e4533a`。隔离runner 20项PASS和全量58项PASS是两个口径，不能相互替代。

## 测试没有证明什么

- 没证明 ArangoDB transaction/CAS；
- 没证明Arango engine数据位于D盘；
- 没证明真实集合/索引已经创建，也没证明migration durable ledger/fence/resume；
- 没证明runtime append-only/CAS/outbox delivery，也没认证wall-clock或本地文件不可变性/WORM；
- 没证明 Redis lease/fencing；
- 没证明现有 Harness 真正关闭了工具表面；
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
3. Arango engine迁D盘作为独立运维测试线，不阻塞前两项；
4. Harness 只靠 Prompt 禁工具必须 capability FAIL；
5. `trajectory.jsonl` 缺失/损坏必须 `invalid_observability`；
6. 任意 tool call 对所有终态独立否决；
7. 重复 dispatch 100 次只能产生一个 LaunchReceipt；
8. 旧 fence 晚提交必须被拒；
9. CAS 已提交/DB 未提交可 reconcile；反向缺 CAS 必须 quarantine；
10. Process/Proof/Leakage view 的越权字段必须构建失败；
11. 无人工决定必须永久 `HUMAN_PENDING`；
12. Evidence Index 反查到 RunArtifact 的集合对账 remainder=0。
