# POC-VMS-41R1 live-runner与盲审封存协议：零模型骨架

**日期**：2026-08-14  
**状态**：`RUNNER_SHELL_PROTOCOL / ZERO_MODEL_ONLY / LIVE_NOT_AUTHORIZED`  
**所属路线**：363号 `SV-S2.10 Event Extractor V2 live-runner/blind-review seal design`  
**前置冻结**：

- 371号：VMS-41R1 Candidate V2 与file-effect审计合同；
- 372号：全新未见qualification pack、阈值、hidden acceptable set/reference candidates/negative checks与blind-review rubric；
- `system/tests/solve_vein_analysis/live_fixtures/poc_vms_41r1.freeze.json`，SHA-256=`37a9fa407be5341305fe61fe63e5a26894d98271c7d7bd3480e6413d0d7295ad`。

本文档只冻结runner和盲审封存的**零模型骨架**。它不授权Devin live，不创建D盘live bundle，不接触DB/Redis/Solver，不改变入题侧代码或资产。

---

## 1. 为什么需要这一层

372号已经冻结了未见case和hidden grader，但还没有冻结“未来如何运行这些case、如何延迟评分、如何形成盲审包”。如果直接把旧VMS-41 runner改到V2并启动live，会有三个风险：

1. v1/v2输出文件名和Schema不同，旧runner可能把`reasoning-trajectory.json`当作V2输出；
2. hidden reference candidates、negative checks或rubric可能被错误复制进候选workspace；
3. 机械评分和人工盲审的顺序若不先冻结，live之后容易产生hindsight调整。

所以本阶段先做一个只能preflight的runner shell：它读取冻结manifest，机械生成未来attempt计划，核对候选workspace可见文件集合，核对hidden文件不会进入workspace，核对final/partial根状态，最后返回`READY_FOR_AUTHORIZATION`或fail-closed。它不运行模型。

---

## 2. Runner shell输入

唯一默认入口：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/run_vms41r1_event_extractor_qualification.py
```

默认模式必须满足：

- 不启动Devin；
- 不执行`devin --version`或`devin models list`；
- 不连接DB/Redis/Solver；
- 不写D盘live/final/partial结果；
- 只读repo内冻结文件；
- 输出一个JSON preflight receipt。

输入文件：

| 对象 | 路径 | 作用 |
|---|---|---|
| preexecution freeze | `system/tests/solve_vein_analysis/live_fixtures/poc_vms_41r1.freeze.json` | 唯一运行计划来源 |
| qualification pack | `system/tests/solve_vein_analysis/qualification_fixtures/vms41r1/` | public case输入与hidden grader |
| role asset | `system/assets/solve_vein_analysis/releases/0.4.1/` | candidate-visible V2 role contract |
| runner | `system/tests/solve_vein_analysis/run_vms41r1_event_extractor_qualification.py` | 本阶段新增，只做零模型preflight |

---

## 3. 未来attempt计划

runner shell必须从freeze中派生6个attempt计划，不允许重新排序或重新生成ID：

1. `V41R1-SYN-EXTRA-PATH` → `poc-vms-41r1-syn-extra-path-a1`
2. `V41R1-SYN-TEMPORAL-CORRECTION` → `poc-vms-41r1-syn-temporal-correction-a1`
3. `V41R1-SYN-TRUE-MERGE` → `poc-vms-41r1-syn-true-merge-a1`
4. `V41R1-SYN-REUSE-NOT-MERGE` → `poc-vms-41r1-syn-reuse-not-merge-a1`
5. `V41R1-SYN-FALSE-MERGE-GUARD` → `poc-vms-41r1-syn-false-merge-guard-a1`
6. `V41R1-REAL-GF2-PAGODA` → `poc-vms-41r1-real-gf2-pagoda-a1`

每个未来workspace只允许包含：

- `AGENTS.md`；
- `TASK.md`；
- `problem.md`；
- `raw_solver_trajectory.txt`；
- `reasoning-trajectory-candidate-v2.md`；
- `input-manifest.json`；
- `devin-config.json`；
- `catalog-snapshot.txt`（未来live时由受控runner复制；本阶段只在计划中声明）。

候选模型只允许写：

- `reasoning-trajectory-candidate-v2.json`；
- `DONE.md`。

hidden文件不得进入候选workspace：

- `acceptable-sets.json`；
- `reference-candidates.json`；
- `negative-checks.json`；
- `thresholds.json`；
- `blind-review-rubric.md`。

---

## 4. Live授权边界

本阶段不实现`--execute`，或实现为恒定fail-closed。

未来如果要启用live，必须另有一个不可扩权授权对象，至少绑定：

- freeze SHA；
- runner source SHA；
- exact Devin binary/profile probe；
- case IDs与attempt IDs；
- D盘final/partial根；
- 最大6次Devin role attempt；
- zero retry；
- human approval reference；
- blind-review package输出位置；
- fail/abort/quarantine处理规则。

没有该授权对象时，任何live开关都必须返回`LIVE_NOT_AUTHORIZED`，而不是“preflight通过所以顺便跑”。

---

## 5. 盲审封存设计

未来live完成后，runner必须先完成以下顺序：

1. 所有6个Devin attempt terminal或quarantine；
2. 每个attempt封存raw workspace、stdout/stderr、export、invocation receipt、candidate output和DONE；
3. 只有所有attempt terminal后，trusted grader才读取hidden acceptable set/reference/negative checks；
4. 机械evaluation写入sealed derived artifacts；
5. 生成blind review package：
   - reviewer只能看到problem、raw trajectory、candidate output、source-span projection和rubric；
   - 不看到case hidden reference candidate；
   - 不看到模型日志中的可能非必要控制信息；
   - reviewer看到的case可用masked ID；
6. 人工review结果单独sealed；
7. aggregator在机械与人工报告都sealed之后合并。

本阶段只实现preflight plan，不生成上述live artifacts。

---

## 6. 零模型preflight receipt

默认runner输出必须包含：

```json
{
  "schema_version": "solve-vein/vms41r1-runner-preflight/v1",
  "poc_id": "POC-VMS-41R1",
  "run_id": "poc-vms-41r1-event-extractor-qualification-20260814",
  "freeze_sha256": "37a9fa407be5341305fe61fe63e5a26894d98271c7d7bd3480e6413d0d7295ad",
  "case_count": 6,
  "attempt_count": 6,
  "workspace_plan_verdict": "PASS",
  "hidden_public_split_verdict": "PASS",
  "live_authorization_status": "NOT_AUTHORIZED",
  "overall_status": "READY_FOR_AUTHORIZATION",
  "side_effects": {
    "model_calls": 0,
    "devin_sessions": 0,
    "database_connections": 0,
    "solver_calls": 0
  }
}
```

任何freeze漂移、hidden/public混入、case/attempt不全、final/partial根已存在且无reconcile方案、或live授权缺失但请求执行，都必须fail-closed。

---

## 7. 本阶段PASS条件

本阶段只能写：

`RUNNER_SHELL_PREFLIGHT_PASS / LIVE_NOT_AUTHORIZED`

需要证据：

1. runner默认命令输出preflight receipt；
2. runner不导入/调用Devin、DB、Redis、Solver、network或subagent；
3. tests证明attempt plan、workspace visible set、hidden/public split、freeze drift、execute block和append-only边界；
4. `system/tests/solve_vein_analysis/README.md`索引新增测试与当前全量测试数；
5. 363号与route-lock同步当前指针。

它不能写：

- Event Extractor role qualified；
- blind audit complete；
- live executed；
- Devin effective model observed；
- stream/batch等价；
- Tell/Hint或双树闭环有效。

---

## 8. 下一阶段

如果runner shell通过，下一阶段才是：

1. 设计LiveRunPermit/人工授权对象；
2. 实现真实live runner的`--execute`受控分支；
3. 实现blind review package生成与sealed manual review导入；
4. 获得新的明确授权后，才可消费6个VMS-41R1 live attempt。
