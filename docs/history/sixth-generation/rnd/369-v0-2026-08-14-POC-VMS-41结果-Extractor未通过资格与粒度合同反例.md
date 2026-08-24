# POC-VMS-41结果：Event Extractor未通过资格与粒度合同反例

**日期**：2026-08-14  
**阶段**：`SV-S2`  
**状态**：`LIVE_BUNDLE_SEALED / POSTHOC_DIAGNOSTIC_SEALED / NOT_QUALIFIED`  
**预注册协议**：368号  
**任务追踪**：363号  
**候选profile**：Devin CLI `3000.4.25 (7e8e528a)` / `glm-5-2` / normalized effort `high`  

---

## 1. 先给结论

VMS-41没有资格化当前Event Extractor profile。

结论必须分成四层：

| 层 | Verdict | 含义 |
|---|---|---|
| artifact integrity | `PASS` | 四个attempt、原始export、候选、evaluation、final receipt和COMMITTED均完整，可只读重算 |
| execution identity | `PASS_WITH_RECORDED_TOOL_DEVIATIONS` | 四次均fresh、exact `glm-5-2`、exit 0、零retry；但至少两个case真实违反冻结写入边界 |
| frozen mechanical science | `FAIL`（4/4） | 四题都未通过exact event count、coarse-anchor direct edge或kind/status/MERGE合同 |
| protocol / component | `INCONCLUSIVE_PROTOCOL / NOT_QUALIFIED` | 冻结tool auditor含路径正则伪阳性，且人工审计盲性已被破坏；不能把失败全部归因于模型，也绝不能写成PASS |

这不是“再跑一次就行”的失败。四个attempt ID已经消费，原ID永久不得重跑。任何新资格实验都必须使用新版本合同、新未见case、新freeze和新attempt lineage。

---

## 2. 冻结身份与物证

```text
freeze manifest:
system/tests/solve_vein_analysis/live_fixtures/poc_vms_41.freeze.json
SHA-256=2ae350c66d2d94bd63a8de1a702278a9d1b9e49d96f3ba39401d8147859db59e

protocol SHA-256:
50404e907e97499ed8a71355f6ee53db419682dd09f392fef1a0467c63cd1e4e

test gate SHA-256:
02ffe772553fa34ee20c2a360496b337d74075f818fc6e3a02ad78344fb80a13

model catalog SHA-256:
1a158307705a2c23b8002df3f2be271d21d7bda3233ea1c61075f9be8f3922c8

live bundle:
/data/master-mind-solve-vein-data/poc-results/poc-vms-41-event-extractor-qualification-20260814/
```

freeze绑定90个文件、112项测试、161个入题侧保护文件、四个case、四个exact attempt ID、唯一D盘结果根、Devin binary/version/catalog、用户级`~/.config/devin/AGENTS.md`的路径/大小/hash，以及零DB/Redis/Solver/subagent合同。

首次freeze命令曾因Python 3.14错误使用`unittest.discover(..., top_level_dir=...)`在零写入、零模型处fail-closed；修复后重新通过112项测试，才生成上面的首次有效freeze。该事故没有消费attempt。

---

## 3. 执行时间线

四次调用严格串行，acceptable set只在四次调用全部终止后才由runner读取评分：

| case | attempt | wallclock | exit | effective model | retry | deviations in invocation receipt |
|---|---|---:|---:|---|---:|---|
| `V41-SYN-FALSE-MERGE` | `poc-vms-41-syn-false-merge-a1` | 177.829745s | 0 | exact `glm-5-2` | 0 | `[]` |
| `V41-SYN-TRUE-MERGE` | `poc-vms-41-syn-true-merge-a1` | 115.350427s | 0 | exact `glm-5-2` | 0 | `[]` |
| `V41-REAL-SPIRAL` | `poc-vms-41-real-spiral-a1` | 359.652332s | 0 | exact `glm-5-2` | 0 | `[]` |
| `V41-REAL-BATTERY` | `poc-vms-41-real-battery-a1` | 432.052820s | 0 | exact `glm-5-2` | 0 | `[]` |

没有resume、fallback、补跑或选择性删除。外层runner exit 0并从`.partial`原子rename为final bundle。

冻结的只读verifier返回：

```json
{
  "artifact_integrity": "PASS",
  "mechanical_replay": "PASS",
  "live_attempt_status": "INCONCLUSIVE_PROTOCOL",
  "manual_semantic_audit": "PENDING",
  "component_qualification": "NOT_YET_DECIDABLE",
  "errors": []
}
```

这里的`mechanical_replay=PASS`只表示能够重算出同一个失败结果，不表示候选科学PASS。

---

## 4. 冻结grader结果

| case | expected events | observed events | mapped anchors | required edges passed | forbidden edges | unmatched | frozen case status |
|---|---:|---:|---:|---:|---:|---:|---|
| false merge | 4 | 7 | 4/4 | 0/3 | 0 | 1 | `INCONCLUSIVE_PROTOCOL` |
| true merge | 5 | 6 | 5/5 | 1/5 | 0 | 3 | `FAIL` |
| real spiral | 8 | 14 | 8/8 | 4/7 | 0 | 1 | `INCONCLUSIVE_PROTOCOL` |
| real battery | 10 | 25 | 10/10 | 1/10 | 0 | 1 | `INCONCLUSIVE_PROTOCOL` |

四题共同事实：

1. source identity、span bounds和span hash都通过；
2. 所有预注册anchor都被某个candidate event覆盖，合计`27/27`；
3. forbidden edge count四题均为0；
4. candidate保留了大量gold未建anchor、但在raw中真实发生的中间状态、折返、例子和复核；
5. exact event count四题均失败；
6. coarse anchor之间常被一个或多个细粒度event隔开，所以direct-edge grader把reachability误当adjacency，required edge recall骤降。

因此，本结果同时包含两类信号：

- **真实模型缺陷**：kind/status存在事后回填；真MERGE的定位与父贡献不稳定；个别`REUSE`证据不足；工具边界有真实越界。
- **资格合同缺陷**：一个合理的细粒度切分只要插入真实事件，就必然破坏`expected_event_count`和anchor间direct-edge；这与VMS-40已经接受多视图/多粒度真值的原则冲突。

---

## 5. 工具边界：真违规与审计器伪阳性必须分开

冻结tool auditor用正则提取exec文本中所有以`/`开头的片段。它把数学字符串中的`/2`、`/liminf`、`/d_X`和schema字符串`/reasoning-trajectory/v1`也当成绝对路径，因此出现伪阳性。

逐attempt回看原始ATIF后：

| case | frozen tool verdict | post-hoc事实分类 |
|---|---|---|
| false merge | FAIL | **真实违规**：在`/tmp/extract_spans.py`写入并执行脚本；另有数学slash伪阳性 |
| true merge | PASS | 未发现workspace外读写；本地Python只处理允许文件 |
| real spiral | FAIL | **真实违规**：额外创建并删除`build_trajectory.py`，违反“只写output与DONE”；同时存在数学slash伪阳性 |
| real battery | FAIL | 当前证据只见允许workspace内的read/write/python校验；失败来自数学slash和schema slash伪阳性，诊断上应为PASS，但冻结结果不得回写 |

这说明工具审计不能继续用“扫描任意命令字符串里的slash token”替代shell/file effect审计。原audit必须保持不变；修正版只能作为新版本、新实验的输入。

---

## 6. 逐case语义诊断

### 6.1 False merge

候选把错误结论、反例、弃路、独立因式分解和最终验证拆成7个事件，整体比4-anchor gold更细且来源忠实；没有制造`MERGE`。但最终事件从“反例检查”标出`REUSE`，而raw明确说弃用配方法论证，是否算复用存在争议；同时`/tmp`写入是明确协议违规。

诊断：`CONTENT_MOSTLY_FAITHFUL / RELATION_AMBIGUOUS / TOOL_BOUNDARY_FAIL`。

### 6.2 True merge

候选识别到“parity lemma被最大闭迹拼接分支复用”，但把真正的结合拆成：先在event 3做`T0 REUSE + T2 CONTINUE`，再在event 4把event 2与event 3标为两个`MERGE`父。于是MERGE比gold晚一层，而且两个父之间已有祖先关系，不能仅凭“两个不同event ID”证明是两个独立贡献。

诊断：`TRUE_COMBINATION_DETECTED / MERGE_LOCALIZATION_AND_PROVENANCE_FAIL`。这是一个协议有效、直接反驳当前角色资格的科学负例。

### 6.3 Real spiral

候选保留14个有来源的事件，包括圆周例、局部等距猜想、圆柱例、角点例、Lebesgue分析、快螺旋失败、慢螺旋成功与最终反例；gold只为其中8个里程碑建anchor。细粒度内容总体忠实，但将早期假设回填为`ABANDONED/CONTRADICTED`，混合了“发生时状态”和“事后结局”；额外helper文件违反写入边界。

诊断：`CONTENT_FAITHFUL_FINE_GRAINED / TEMPORAL_STATUS_HINDSIGHT / TOOL_BOUNDARY_FAIL`。

### 6.4 Real battery

候选把多轮“再确认下界是否严密”的折返完整保留成25个事件，10个anchor全部命中。大量required edge失败不是对应思想缺失，而是anchor之间存在真实中间节点。候选对状态/return种类仍有若干分歧；其MERGE使用了构造与重新验证的Turan下界，但“贡献独立性”不能从父ID数量直接推出。冻结tool FAIL主要来自slash正则伪阳性。

诊断：`CONTENT_FAITHFUL_FINE_GRAINED / STATUS_AND_CONTRIBUTION_SEMANTICS_PARTIAL / FROZEN_TOOL_AUDIT_FALSE_POSITIVE`。

---

## 7. 为什么VMS-41不能简单解释为“模型失败”

若一个Extractor把raw中真实存在的步骤拆得比gold更细，正确的比较对象不应是节点数量和coarse-anchor直接邻接，而应是：

1. 关键anchor是否全部有且只有一个可辩护映射；
2. 额外事件是否有独立source span和真实数学状态变化；
3. 在把细粒度DAG投影到anchor quotient后，预注册关系是否由允许的typed path实现；
4. 被压缩的路径是否引入禁止语义；
5. 同一候选能否同时给出多个版本化观察视图，而不改写occurrence history。

VMS-41使用`exact event count + one anchor per event + direct anchor edge`，实际上把“一个可接受观察视图”错当成“唯一发生史”。这会系统性惩罚细粒度、但来源忠实的提取。

但反过来，也不能因为粒度合同过窄就给模型放行：真MERGE定位、发生时状态、关系证据和工具权限确有实际缺陷。因此正确Verdict是“资格未通过且合同需要修订”，不是PASS，也不是简单的模型能力FAIL。

---

## 8. 下一版理论/技术修正

### 8.1 occurrence真值与observation projection分离

候选先产出细粒度`Occurrence DAG`；审计层再产出一个或多个`ObservationProjection`。gold冻结的是必需anchor与允许投影，不再冻结唯一event count。

### 8.2 从direct edge改成typed path / quotient relation

coarse anchor `A → B`可由candidate中的允许路径实现，例如：

```text
A --CONTINUE--> x --REFINE--> B
```

projection必须记录被折叠节点、边类型组合、禁止类型和证据span。不能把任意reachability都算命中；允许的path regular language必须预注册。

### 8.3 extra event不是自动FAIL

额外事件须满足：source-backed、数学上非空、非重复修辞、时间位置正确、不会吞并两个不可拆anchor、不会制造禁止关系。通过这些门后，它是细粒度真值，不是“多提取了一个错误”。

### 8.4 status拆成发生时与事后状态

至少分：

- `status_at_occurrence`；
- `later_resolution`或独立termination relation。

不能因为路线后来失败，就把它首次提出时的状态回填为`ABANDONED`。

### 8.5 MERGE从父ID计数升级为贡献证明

`minimum_distinct_parent_ids >= 2`不够。需要：

- 每个parent的`contribution_claim`；
- 对应source span；
- contribution是否在target中实际使用；
- branch/provenance frontier；
- 祖先相关时为什么仍是不同信息贡献；
- false-friend负例。

### 8.6 工具策略改造

下一资格版本应优先取消候选自行计算hash的必要性：候选只给span边界，runner重算hash并生成DONE/receipt；或提供只读、固定hash的span helper。若保留exec，必须审计结构化file effects，禁止用通用slash正则解析含数学文本的heredoc。

---

## 9. 审计独立性边界

本轮Master在正式语义审计前已经读取机械evaluation和acceptable-set错误摘要，因此不能再宣称人工审计是blind。现已建立独立append-only diagnostic audit bundle，并固定标记：

```text
blindness = BREACHED_BEFORE_MANUAL_AUDIT
purpose = FAILURE_LOCALIZATION_ONLY
confirmation_eligible = false
```

它可以支持设计修订，不能把VMS-41升级为资格PASS。

### 9.1 已封存的事后诊断物证

```text
audit bundle:
/data/master-mind-solve-vein-data/poc-results/
  poc-vms-41-event-extractor-diagnostic-audit-20260814/

manual diagnostic SHA-256:
4ccf008b7712b9cd0b641101f806a3f1aa4f771afbf6d7550b28a52513e98bc8

diagnostic summary SHA-256:
d59896b041acaad4f668d656aa5d5c5763d8837fdd9da68b2d4d6be371d852ba

source binding SHA-256:
e91bbb56b8a8ce36711491b1faee15d5718a05eb6825f6672fa20501691934e1

verifier replay SHA-256:
7752668c4117c532d85c7e94bbff235f79c6d58bca0c23ff63299e554cdcca4e

final receipt file SHA-256:
c46c4d5f609cee158c036a9f44d1d2e0cffd3fe5753993614d8f257688fe1f0c

artifact tree SHA-256:
b51e514dc3a2b188fcf50fba54d613a3ec7e99478f160fcb9a939f57e41da5e0

COMMITTED SHA-256:
e24a1537f9eb9e5e9cdee263de89568f1e23a1ff05dec303397aabf8871365e7
```

审计共覆盖4个case：内容判断3个`PASS`、1个`PARTIAL`；确认2个case存在真实工具边界偏离，1个case只有冻结slash审计器伪阳性。它不裁决“模型全局上能否胜任Extractor”，只把本轮失败定位到模型输出、资格真值和工具审计三层。

首次尝试封存诊断bundle时，历史VMS-41 verifier把“当前测试源码全集”当成冻结成员，因新增事后审计测试而在任何审计文件写入前fail-closed。修复没有改写VMS-41 freeze或live bundle：新sealer改为逐项验证历史freeze中90个成员及其hash，同时把freeze之后新增文件记录为provenance additions。当前只读verifier重新计算live artifact tree、四case evaluation、工具/文件集审计与全部source binding；121项解题侧测试全部通过。

---

## 10. 当前Verdict与停止规则

```text
VMS41_ARTIFACT_FACTORY = PASS
VMS41_FROZEN_MECHANICAL_REPLAY = PASS
VMS41_FROZEN_CASE_PASS_COUNT = 0 / 4
VMS41_PROTOCOL = INCONCLUSIVE_PROTOCOL
EVENT_EXTRACTOR_GLM52_HIGH_PROFILE = NOT_QUALIFIED
MODEL_GLOBAL_CAPABILITY = NOT_DECIDABLE_FROM_THIS_POC
ORIGINAL_ATTEMPT_RETRY = PROHIBITED
```

SV-S2不得直接进入State Normalizer资格化。先封存post-hoc诊断，再建立新的S2修订协议和未见qualification pack。VMS-41的四题从此只能进入development/regression，不能再充当确认性holdout。

事后诊断现已封存，因此下一合法动作是：先冻结修订后的occurrence/projection、typed path、发生时status、MERGE贡献与结构化file-effect合同，再使用全新未见case、新实验ID和新attempt lineage进行资格化；不得回到四个旧case上调参后宣称确认成功。
