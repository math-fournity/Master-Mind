# 测试说明

## 一句话结论

首版测试只证明 P0/P1 控制面在临时隔离目录中 fail-closed；测试不得连接真实 DB、Redis、D 盘数据根或 Devin CLI。

## 运行全部测试

```bash
SEVEN_WORKSPACE_ROOT="$(git rev-parse --show-toplevel)"
cd "$SEVEN_WORKSPACE_ROOT"
.venv/bin/python -m unittest discover -s seven-system/tests -p 'test_*.py' -v
```

测试全部使用 Python 标准库和 `TemporaryDirectory`，不需要安装新依赖。独立迁出后从Seven repo根使用`python3 -m unittest discover -s tests -p 'test_*.py' -v`。

## 当前覆盖

| 测试 | 保护的不变量 |
|---|---|
| `test_hashing_and_storage.py` | JSON 顺序/换行不改变哈希；同内容幂等；异内容绝不覆盖 |
| `test_preflight.py` | dry-run 无 DB；数据根不能在 repo；专属namespace；能力subject/claims/checks绑定；live 始终 BLOCKED |
| `test_epoch.py` | Epoch初建返回前自验与重入；PASS/FAIL Gate均可重放；两级seal+外部receipt；Schema科学非主张；manifest/verdict/report篡改、重算index、非对象JSON、旧P0漂移和symlink逃逸被拒绝 |
| `test_repository_assets.py` | 示例配置可读且真正执行Schema/拒绝未知字段；Solver 资产禁工具且无答案占位符；Schema 是合法 JSON |

## 安全断言

测试期望：

- 当前P0/P1命令的静态实现范围内没有DB、Solver、Redis adapter入口；报告中的三个0是这一代码范围声明，不是外部观测计数器；
- 临时测试卷含自己的 README；
- 所有运行数据只写临时目录；
- 测试结束由临时目录生命周期回收，不触及 D 盘。

## 测试没有证明什么

- 没证明 ArangoDB transaction/CAS；
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

1. 错 DB、DB 未设置、read path 自动建集合均必须 BLOCK；
2. Harness 只靠 Prompt 禁工具必须 capability FAIL；
3. `trajectory.jsonl` 缺失/损坏必须 `invalid_observability`；
4. 任意 tool call 对所有终态独立否决；
5. 重复 dispatch 100 次只能产生一个 LaunchReceipt；
6. 旧 fence 晚提交必须被拒；
7. CAS 已提交/DB 未提交可 reconcile；反向缺 CAS 必须 quarantine；
8. Process/Proof/Leakage view 的越权字段必须构建失败；
9. 无人工决定必须永久 `HUMAN_PENDING`；
10. Evidence Index 反查到 RunArtifact 的集合对账 remainder=0。
