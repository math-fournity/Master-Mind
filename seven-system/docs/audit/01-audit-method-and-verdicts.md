# 审计方法、独立性与Finding

## 冻结被审对象

审计开始时保存：

- commit/tree hash、tracked/untracked状态；
- CompletionBundle hash；
- 可选evidence-index commit及其tree hash；
- spec/ADR/Schema hashes；
- Python/CLI/provider/DB/OS/volume fingerprints；
- repo外取得的站点owner pinned HumanGate trust-root hash、channel ID、观察时间和observation receipt；
- owner签名AuditAssignment、root/roster/policy/algorithm registry、audit plan/spec、audit attempt ID、auditor principal/attestation public key和独立性；
- 审计所需外部副作用的EEA、不可扩权LiveRunPermit、允许action/额度/到期、精确ordinal和初始`RESERVED` ConsumptionReceipt。

被审树发生变化即停止，不能在移动目标上继续签PASS。

## 审计顺序

1. 先用已证明会拒绝`not-a-date`和非法日历日期的RFC 3339 parser/JSON Schema validator验证AuditAssignment，再独立重算JCS/Ed25519、repo外pinned trust root三方一致、key lifecycle、时间、nonce和审计者职责分离；
2. 按“两提交/外部bundle”协议对账：subject tree不含CompletionBundle，测试收据绑定精确subject commit，外部bundle先于可选index commit生成，index commit只记录bundle ref/hash，bundle不得反向包含index commit；
3. CompletionBundle、subject commit/tree、可选index commit与真实树逐项对账；
4. RequirementTraceability与NormativeRequirementIndex remainder检查；
5. OperatorCommandRegistry和RoleQualificationMatrix双向completeness检查；
6. 静态旁路和权限扫描；
7. Schema+semantic verifier攻击；
8. 独立重跑unit/contract/component；
9. 只有在EEA→LiveRunPermit→原子reserve成立时，才在permit范围内运行capability canary；
10. 故障注入与恢复；
11. 适用时运行最小golden slice；
12. Evidence DAG replay和orphan检查；
13. 核对claims/nonclaims；
14. 生成每条finding显式绑定轴的四轴AuditRecord，不直接修复finding；只把unsigned canonical bytes交给模型不可达的AttestationSignerPort，由HumanGateService独立验收后才改变状态。

## Finding严重度

| 级别 | 典型问题 | 处理 |
|---|---|---|
| P0 | 答案泄漏、错误DB、证据覆盖、重复Solver、HumanGate旁路、可伪造科学PASS | 立即FAIL/QUARANTINE |
| P1 | 幂等/fence/recovery破坏、profile伪PASS、双计科学样本 | 不得晋级 |
| P2 | 成本/观测/scope不完整、文档与实现漂移 | PARTIAL或修复后复审 |
| P3 | 局部可维护性、非阻断说明问题 | 记录follow-up |

## 审计者独立性

- 实现者可以做自审和修复，但不能签独立PASS；
- 审计者发现问题后若亲自改代码，当前audit终止；
- 新commit必须由另一独立审计或重新建立独立上下文/职责；
- 使用同模型新session只算context independence，报告中不得升级成model independence；
- 审计者不得自行创建AuditAssignment、把自己的key加入信任根或签署最终状态跃迁。
- 审计AI不得持有attestation私钥；Signer只签Assignment允许的精确bytes，不决定finding，也不接受调用者替换principal/key/subject。

## Evidence等级

- E0：文档/观察；
- E1：静态代码或单元测试；
- E2：受控component/integration；
- E3：真实能力canary或故障注入；
- E4：完整golden slice、跨环境/模型复验。

Capability、live recovery和最终DONE不能只凭E0/E1。

## 合法负结果

- 实验科学假设失败不等于Factory FAIL；
- capability probe FAIL可以说明adapter未资格化，但控制面正确阻断仍可PASS；
- 一致的Gate FAIL是有效artifact，不是完整性损坏；
- 协议损坏是INCONCLUSIVE/BLOCKED，不能硬算科学负结果。
