# POC-VMS-40结果：多视图真值与 Acceptable Set 确定性验证通过

**日期**：2026-08-14  
**协议**：366号  
**阶段**：SV-S1  
**协议 Verdict**：PASS  
**科学 Verdict**：PASS_WITHIN_FROZEN_MULTIVIEW_FIXTURES  
**总体 Verdict**：PASS_WITHIN_DETERMINISTIC_OFFLINE_SCOPE  
**证据用途**：DEVELOPMENT_ONLY  

---

## 1. 结论

VMS-40 已经证明，在冻结的非线性推理案例中，不需要把真值压成唯一平面 Gold 图。系统可以同时做到：

1. 保存精确 occurrence 集；
2. 把时间、控制流、知识依赖、合流和状态同一性拆成不同 view；
3. 把问题义务、策略、表示、知识状态等拆成正交 state axis；
4. 用不可拆分的完整 alternative 接受多个合法图投影；
5. 拒绝跨 alternative 拼接、半套关系、两套同时命中、假合流和额外关系；
6. 用确定性 evaluator 从逐项检查机械派生总 Verdict。

冻结矩阵包含 6 个 case、26 个 candidate。所有 expected verdict 与 observed verdict 完全一致，mismatch 为空。

这解决了 VMS-35/38 暴露的两个问题：

- ABANDONED 与 CONTRADICTED 可以作为受约束的可接受状态集合，而不是强迫唯一标签；
- 折返/分叉处可以存在两套完整合法投影，但不能把两套投影任意混搭。

---

## 2. 冻结物证

| 对象 | 值 |
|---|---|
| protocol SHA-256 | 8d045365b5cd14d8d98d617ddec7c6607d96aeb1e2a871216fa1c631ca1b6857 |
| fixture file SHA-256 | 062639ec0ddd4a07427449f0b6896123912125cf6c8bdc27c5114dfa61f29851 |
| fixture canonical SHA-256 | d6f3891df46cb91961108869134cd2b015f5da49d2780fcedb3a990ef2ad7053 |
| implementation aggregate SHA-256 | f239453597e2688b1414b2a9dc971cd8608f208e06cb55965eedd8f59e2ca9c4 |
| evaluation matrix file SHA-256 | 1bde2a772ea488a886b4c35a99f7bf49667b912b8d22af8ac2906fefcdbb2394 |
| artifact tree SHA-256 | 18de97c549d99e5e0e7b00062797f9f717ddbcbedc31863e733203cb49b04a29 |
| final receipt file SHA-256 | 6f6a6ea8a3cee64ecc7eb204140f2a1df4bc07a5f102e4552fb6e4967bbfed2c |
| evidence bundle | /data/master-mind-solve-vein-data/poc-results/poc-vms-40-20260814/ |

实现核心：

- system/solve_vein_analysis/semantic_truth.py；
- system/tests/solve_vein_analysis/multiview_fixtures/vms40_cases.json；
- system/tests/solve_vein_analysis/test_semantic_truth.py；
- system/tests/solve_vein_analysis/run_multiview_poc.py；
- system/tests/solve_vein_analysis/verify_multiview_poc.py。

封存时 semantic_truth.py SHA-256 为 a9a97d2d97c85d6d96032bd4792fa02ed63d243f4cf9389bfafcae6d8035620e，runner SHA-256 为 8d766c9c1ddcc55d549a624469fd5db9b3ea06b89b1ac4a31caba4ee04c57d98。

---

## 3. 案例矩阵结果

| Case | 目标 | candidate数 | 结果 |
|---|---|---:|---|
| MV1 | legacy status acceptable set | 3 | ABANDONED、CONTRADICTED PASS；ACTIVE FAIL |
| MV2 | problem/method/representation/knowledge分轴 | 2 | 分轴PASS；单canonical合并FAIL |
| MV3 | 两套完整折返/分叉投影 | 5 | A、B各PASS；混搭、双命中、半套均FAIL |
| MV4 | 真合流要求不同parent occurrence | 4 | 两父PASS；单父FAIL；重复父INVALID；mention-only FAIL |
| MV5 | required/optional/forbidden/unmatched分开 | 5 | required与optional正例PASS；三类负例FAIL |
| MV6 | strict schema、identity、canonicalization | 7 | 正例PASS；unknown/duplicate INVALID；错case、漏/多occurrence、漏axis FAIL |

总计：

~~~text
case_count = 6
candidate_count = 26
mismatches = []
matrix_verdict = PASS
~~~

---

## 4. 关键机制结论

### 4.1 Alternative 是不可拆分的解释单元

relation clause 不把所有合法边放进一个宽松白名单。每个 alternative 是完整边集：

- 完整命中一个允许的方案，才算方案成立；
- 只命中一部分，FAIL；
- EXACTLY_ONE 下同时命中两个方案，FAIL；
- 从 A、B 各取一部分，FAIL。

这让 Acceptable Set 既能容纳真正语义歧义，又不会退化成“什么都对”。

### 4.2 Canonical Math State 不再承担全部语义

MV2 证明同一个 problem obligation 可以在不同 strategy、representation 和 knowledge state 中反复出现。新合同以多轴 binding 判断 must-link/cannot-link，旧 canonical_math_state_id 只保留为兼容投影。

### 4.3 真合流是结构事实

MERGES 的结构门按不同 source occurrence ID 计数。重复同一 parent 不会增加计数；只有文本 mention 或 REUSES 也不会被当成合流。

### 4.4 每个 view 单独报告覆盖

Evaluator 分别报告五类 view 的 required、allowed、candidate、missing、forbidden 和 unmatched。最终 PASS 不能掩盖某一 view 的漏标。

---

## 5. 测试与独立复核

封存包内 controlled test：

~~~text
16 tests
exit_code = 0
verdict = PASS
stderr SHA-256 = f397efccb32a15f6a2634f697039b4f12aa3a78c23c7b457ba7147d001b3f4f6
~~~

封存前全量解题侧回归：

~~~text
91 tests
PASS
~~~

其中包含入题侧保护基线不变检查。没有修改 system/vein_analysis.py、system/process_absorb.py、system/assets/vein_analysis/ 或任何入题侧运行资产。

封存后用独立只读 verifier 重新计算：

- 精确文件集合；
- 每个 artifact 的 size/hash；
- artifact tree hash；
- COMMITTED 对 final receipt 的绑定；
- protocol、fixture 和 implementation provenance；
- 6 case / 26 candidate / 0 mismatch；
- test stdout/stderr；
- side-effect计数和最终 Verdict。

结果：

~~~json
{
  "artifact_integrity": "PASS",
  "errors": []
}
~~~

随后第二次启动同一 run ID，程序以 exit 2 拒绝：

~~~text
append-once destination exists
~~~

没有产生第二个partial目录或覆盖旧物证。

---

## 6. 一次 pre-start 入口失败

第一次直接运行 runner 时，在 import system 处发生 ModuleNotFoundError。失败发生在：

- D盘site验证之前；
- partial/final目录创建之前；
- fixture读取与candidate计算之前。

因此它不是科学attempt，也没有消费 POC run ID。修复方式是复用既有解题侧脚本的 repo-root bootstrap；修复后的 runner 代码被 implementation receipt 精确冻结，然后才执行唯一有效 POC。

该事实保留在结果说明中，不能被省略成“首启即成功”。

---

## 7. 副作用与证据边界

run manifest 的副作用计数全部为0：

~~~text
model_calls = 0
solver_calls = 0
database_connections = 0
redis_connections = 0
network_calls = 0
protected_intake_mutations = 0
~~~

VMS-40 PASS 不证明：

- 真实 trajectory 抽取正确；
- Devin/Codex 的 Extractor、Normalizer、Auditor 已资格化；
- 关系本体覆盖所有数学推理；
- FCA/RCA 已完成规模验证；
- Trace/Tell分片遍历已实现；
- Tell可选择、可执行或可归责；
- 推理树、引导树、Grove和Seven已接通。

---

## 8. 阶段门与下一步

366号 G-S1 的确定性要求已经满足：

- 多视图关系本体：PASS；
- 多轴State：PASS；
- Acceptable Set完整alternative：PASS；
- 正/负/边界fixture：PASS；
- evaluator机械派生：PASS；
- canonicalization：PASS；
- artifact/append-only：PASS；
- 入题侧隔离：PASS。

因此 SV-S1 可以关闭，主指针转向 SV-S2：Event Extractor资格化。下一项 POC 是 VMS-41；必须使用未见 qualification pack、独立acceptable set和冻结角色/profile，不能重用 VMS-38 输出作为确认性测试集。
