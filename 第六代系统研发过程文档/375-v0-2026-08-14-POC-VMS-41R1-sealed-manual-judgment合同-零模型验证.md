# POC-VMS-41R1 sealed manual judgment合同：零模型验证

**日期**：2026-08-14  
**状态**：`MANUAL_JUDGMENT_CONTRACT_FROZEN / NO_REAL_REVIEW_IMPORTED`  
**阶段**：`SV-S2.12`  
**前置**：374号不可消费LiveRunPermit/盲审包计划  
**代码入口**：`system/tests/solve_vein_analysis/vms41r1_manual_judgment_contract.py`

---

## 1. 为什么需要这一层

374号已经说明Reviewer什么时候能看candidate输出、什么时候不能看hidden acceptable set。下一层要解决的是：Reviewer真正给出的人工判断如何落盘，才能在未来和hidden机械评分join时保持可审计。

如果人工判断只是自由文本，后面会有三个危险：

1. 看过hidden答案后补写“人工判断”，伪装盲审；
2. 某个关键轴失败，却把总体写成`MANUAL_PASS`；
3. case/attempt身份漂移，导致人工判断被join到错误candidate。

因此本阶段先冻结sealed manual judgment的机器合同。

---

## 2. 当前命令

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_manual_judgment_contract.py
```

预期输出合同摘要：

- `judgment_schema_version = solve-vein/vms41r1-sealed-manual-judgment/v1`；
- `case_count = 6`；
- 包含6个case到attempt ID的冻结映射；
- 全部side effects为0；
- 明确不执行真实人工审稿、不运行hidden grader、不资格化profile。

---

## 3. Judgment对象

未来真实人工判断对象必须包含：

- `schema_version`；
- `review_id`；
- `case_id`；
- `attempt_id`；
- `blinded_package_sha256`；
- `reviewer_blinding_attestation`；
- `axis_verdicts`；
- `final_manual_verdict`；
- `reviewer_notes`；
- `sealed_status`；
- `explicit_nonclaims`。

`case_id`和`attempt_id`必须匹配374号计划中的冻结映射。

---

## 4. Blinding attestation

`reviewer_blinding_attestation`必须精确等于：

```json
{
  "reviewer_view_only": true,
  "hidden_acceptable_set_seen": false,
  "reference_candidate_seen": false,
  "mechanical_grader_result_seen": false
}
```

任何字段为true、缺字段、额外字段或含糊表达，都不得进入后续hidden join。

---

## 5. 必需轴

`axis_verdicts`必须精确覆盖：

1. `occurrence_fidelity`
2. `source_span_fidelity`
3. `typed_relation_fidelity`
4. `temporal_status_fidelity`
5. `merge_contribution_fidelity`
6. `file_boundary_cleanliness`

每个轴只允许：

```text
PASS | FAIL | INCONCLUSIVE
```

若任何轴不是`PASS`，总体不得写成`MANUAL_PASS`。若总体写成`MANUAL_FAIL`，至少必须有一个轴为`FAIL`。不确定时使用`MANUAL_INCONCLUSIVE`。

---

## 6. 非主张

本阶段不主张：

- 已经完成真实人工盲审；
- 已经导入真实reviewer签名；
- 已经运行hidden acceptable-set grader；
- Event Extractor profile已资格化；
- live attempt已经获得授权。

---

## 7. 下一步

下一步可以继续零模型实现：

- sealed manual judgment import receipt；
- hidden join前的完整性检查；
- fake judgment + fake candidate package的end-to-end join simulator。

仍然不得启动Devin live attempt，除非获得新的明确人签LiveRunPermit。
