# POC-VMS-41R1 fake live bundle与盲审包materializer：零模型

**日期**：2026-08-14  
**状态**：`PLAN_ONLY_NO_FILES_WRITTEN / LIVE_NOT_AUTHORIZED`  
**阶段**：`SV-S2.14`  
**前置**：376号hidden join simulator  
**代码入口**：`system/tests/solve_vein_analysis/vms41r1_fake_live_bundle_materializer.py`

---

## 1. 本阶段做什么

本阶段继续保持零模型，只生成未来两个物理包的**计划manifest**：

1. fake live bundle plan；
2. blind review package plan。

它使用hidden reference candidate作为fake candidate output，目的是验证未来blind review package的文件集合、hash和hidden隔离，不伪装成真实Devin输出。

---

## 2. Reviewer可见文件

每个case的Reviewer包只允许出现：

- `problem.md`；
- `raw_solver_trajectory.txt`；
- `reasoning-trajectory-candidate-v2.json`；
- `DONE.md`；
- `candidate-output-manifest.json`。

这些文件在本阶段只以hash manifest形式出现，不实际写目录。

---

## 3. 绝对禁止暴露的hidden文件

以下文件不得进入Reviewer包：

- `acceptable-sets.json`；
- `reference-candidates.json`；
- `negative-checks.json`；
- `thresholds.json`；
- `blind-review-rubric.md`。

`reference-candidates.json`当前只作为fake candidate output来源被程序读取，计划对象必须把它标记为`HIDDEN_REFERENCE_CANDIDATE_AS_FAKE_LIVE_OUTPUT`，并明确非真实Devin输出。

---

## 4. 命令

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_fake_live_bundle_materializer.py
```

预期：

- `schema_version = solve-vein/vms41r1-fake-live-bundle-materializer/v1`；
- `materializer_status = PLAN_ONLY_NO_FILES_WRITTEN`；
- `case_count = 6`；
- `hidden_public_split_verdict = PASS`；
- `fake_live_output_count = blind_review_package_count = 6`；
- 全部side effects为0。

---

## 5. 非主张

本阶段不主张：

- 创建了真实live bundle；
- 创建了真实blind review package；
- 有真实Devin candidate output；
- 有真实人工review；
- Event Extractor profile已资格化；
- live attempt已获授权。

---

## 6. 下一步

下一步可以继续零模型实现：

- materialized fake package写入临时目录的append-only测试；
- final qualification join receipt schema；
- fake end-to-end bundle。

要进入真实VMS-41R1 live资格实验，仍必须先获得新的明确人签LiveRunPermit。
