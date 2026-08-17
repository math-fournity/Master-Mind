# POC-VMS-41R1 fake bundle append-only dry-run

**日期**：2026-08-14  
**状态**：`APPEND_ONLY_FAKE_BUNDLE_WRITTEN / TEMP_ROOT_ONLY / LIVE_NOT_AUTHORIZED`  
**阶段**：`SV-S2.16`  
**前置**：377号fake materializer、378号final join receipt  
**代码入口**：`system/tests/solve_vein_analysis/vms41r1_fake_bundle_append_only_dry_run.py`

---

## 1. 本阶段做什么

本阶段仍然不启动模型，但从“只输出hash计划”前进到“在显式临时输出根中真实写出Reviewer可见文件”。它验证未来真实blind-review package的物理写入边界：

- 每个case只写5个Reviewer可见文件；
- hidden acceptable/reference/threshold/rubric/negative checks不写入case目录；
- 文件hash必须与377号materializer计划完全一致；
- 输出根必须为空、不是symlink、不能在repo内；
- 第二次写同一根必须fail-closed。

---

## 2. 命令

必须显式给出输出根。测试只使用`TemporaryDirectory`，不写D盘生产目录：

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_fake_bundle_append_only_dry_run.py \
  --output-root /tmp/vms41r1-fake-bundle-demo
```

预期：

- `schema_version = solve-vein/vms41r1-fake-bundle-append-only-dry-run/v1`；
- `dry_run_status = APPEND_ONLY_FAKE_BUNDLE_WRITTEN`；
- `case_count = 6`；
- `side_effects.local_files_written = 31`；
- `side_effects.hidden_files_written = 0`；
- `profile_qualification_verdict = NOT_QUALIFIED_LIVE_NOT_AUTHORIZED`。

---

## 3. 非主张

本阶段不主张：

- 有真实Devin candidate output；
- 有真实live bundle；
- 有真实人工review；
- 有真实VMS-41R1资格结果；
- 临时目录dry-run可以替代未来D盘append-only evidence bundle；
- Event Extractor profile已资格化。

---

## 4. 下一步

此阶段只补强“落包边界”。进入真实VMS-41R1资格实验仍需新的明确人签LiveRunPermit；没有LiveRunPermit时，不得启动Devin session、不得消费attempt ID，也不得把fake/reference bundle接入hidden grader作为确认性证据。
