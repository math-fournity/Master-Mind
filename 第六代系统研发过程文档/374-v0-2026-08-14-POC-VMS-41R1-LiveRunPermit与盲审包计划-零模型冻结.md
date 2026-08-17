# POC-VMS-41R1 LiveRunPermit与盲审包计划：零模型冻结

**日期**：2026-08-14  
**状态**：`ZERO_MODEL_PLAN_FROZEN / LIVE_NOT_AUTHORIZED`  
**阶段**：`SV-S2.11`  
**前置**：371号V2合同、372号未见qualification pack、373号runner shell  
**代码入口**：`system/tests/solve_vein_analysis/build_vms41r1_live_permit_review_plan.py`

---

## 1. 本文档解决什么

373号已经把未来live runner的外壳做到`READY_FOR_AUTHORIZATION / NOT_AUTHORIZED`，但仍缺两个会决定后续可审计性的对象：

1. **LiveRunPermit**：未来到底谁、在什么冻结输入和预算下，允许启动哪几个Devin session；
2. **Blind Review Package**：未来候选输出完成后，Reviewer能看什么、不能看什么，何时才能和hidden acceptable set/mechanical grader join。

本文档只冻结这两个对象的**计划形状**。它不授权live、不生成可消费permit、不创建candidate workspace、不做机械评分，也不完成盲审。

---

## 2. 当前硬边界

当前运行只允许：

- 读取`poc_vms_41r1.freeze.json`；
- 读取runner shell的零模型preflight；
- 派生一个不可执行的plan receipt；
- 跑本地确定性测试。

当前禁止：

- 启动Devin session；
- 调用模型、Solver、DB、Redis或网络；
- 创建live workspace、partial bundle或final bundle；
- 给任何attempt写`AUTHORIZED`；
- 把hidden acceptable set、reference candidate、negative check、threshold或rubric放入Reviewer可见包；
- 在人工盲审sealed前运行或展示机械hidden评分。

---

## 3. LiveRunPermit计划语义

当前计划中的`live_run_permit`必须满足：

```text
permit_status = DRAFT_NOT_SIGNED
permit_consumable = false
authorized_live_attempts = 0
required_human_authorization_ref = null
```

它可以记录未来签名permit必须绑定的模板，例如：

- parent freeze SHA；
- runner preflight必须为`READY_FOR_AUTHORIZATION`；
- planned attempts = 6；
- retry_limit = 0；
- requested model UID = `glm-5-2`；
- normalized effort = `high`；
- fresh session required；
- resume forbidden；
- dangerous permission mode required。

但这些字段只是未来permit模板，不是当前授权。任何代码若在没有独立人签授权对象时把这个plan当作permit使用，应判为协议P0。

---

## 4. 盲审包计划语义

每个case未来的Reviewer可见包只允许包含：

- `problem.md`；
- `raw_solver_trajectory.txt`；
- Devin候选输出`reasoning-trajectory-candidate-v2.json`；
- `DONE.md`；
- `candidate-output-manifest.json`。

以下内容在人工盲审sealed前必须不可见：

- `acceptable-sets.json`；
- `reference-candidates.json`；
- `negative-checks.json`；
- `thresholds.json`；
- `blind-review-rubric.md`。

注意：rubric本身已经作为协议资产冻结，但不能放进具体case的Reviewer可见包里，让Reviewer被hidden acceptable-set结构暗示。Reviewer只应按单独发布的审稿任务说明和candidate输出作判断。

---

## 5. Join顺序

未来真正live后的顺序必须是：

```text
candidate output sealed
  → blind review package materialized
  → manual judgment sealed
  → hidden acceptable set / mechanical grader join
  → final qualification verdict
```

禁止：

- 先运行hidden grader再让Reviewer看机械结果；
- Reviewer看到acceptable set或reference candidate；
- live失败后retry until pass；
- 对同一case在看到机械结果后补人工判断并称为盲审。

---

## 6. 当前计划对象

当前零模型命令：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/build_vms41r1_live_permit_review_plan.py
```

预期：

- `schema_version = solve-vein/vms41r1-live-permit-review-plan/v1`；
- `runner_preflight_status = READY_FOR_AUTHORIZATION`；
- `runner_live_authorization_status = NOT_AUTHORIZED`；
- `live_run_permit.permit_consumable = false`；
- `live_run_permit.authorized_live_attempts = 0`；
- `blind_review_plan.case_count = 6`；
- 全部`side_effects`为0。

这个命令默认只向stdout输出计划，不写live目录。`--canonical`只改变输出格式，不改变语义。

---

## 7. 退出条件

本阶段的退出条件是：

1. 计划对象能从冻结freeze和runner preflight确定性派生；
2. 计划对象明确不可消费；
3. reviewer-visible文件集合与hidden文件集合机械分离；
4. hidden join顺序写入对象；
5. 对应测试覆盖正例与关键反例；
6. README、363、route-lock与runbook全部同步；
7. 全量`system/tests/solve_vein_analysis`测试通过。

满足这些条件后，下一阶段才能讨论真正的人工LiveRunPermit签发和live attempt启动。

---

## 8. 非主张

本阶段不主张：

- Event Extractor profile已资格化；
- Devin会按V2合同正确输出；
- blind review已经完成；
- 人工授权已经给出；
- live workspace已经存在；
- mechanical grader可在人工判断前运行；
- VMS-41旧attempt可被重跑。
