# 审计汇总报告 — batch=audit-test1

> 生成时间: 2026-08-16T05:13:31.165540+00:00
> 审计结果总数: 5

## 1. 审计状态分布

| 审计状态 | 数量 | 占比 | 说明 |
|---|---|---|---|
| PASS_NOT_SELECTABLE | 2 | 40.0% | 通过但不可操作（D1-D4不通过） |
| FAIL_CONTENT_CORRUPT | 1 | 20.0% | 内容损坏（XML泄漏/占位符泄漏） |
| FAIL_INCOMPLETE | 1 | 20.0% | 不完整（A2-A6任一不通过） |
| PASS_SELECTABLE | 1 | 20.0% | 通过且可选题（d1=DE + D1-D4通过） |

## 2. 各检查项通过率

| 检查项 | PASS | FAIL | 通过率 |
|---|---|---|---|
| A1 | 5 | 0 | 100.0% |
| A2 | 5 | 0 | 100.0% |
| A3 | 5 | 0 | 100.0% |
| A4 | 4 | 1 | 80.0% |
| A5 | 5 | 0 | 100.0% |
| A6 | 5 | 0 | 100.0% |
| B1 | 4 | 1 | 80.0% |
| B2 | 5 | 0 | 100.0% |
| B3 | 4 | 1 | 80.0% |
| C1 | 4 | 1 | 80.0% |
| C2 | 5 | 0 | 100.0% |
| C3 | 4 | 1 | 80.0% |
| D1 | 2 | 3 | 40.0% |
| D2 | 4 | 1 | 80.0% |
| D3 | 5 | 0 | 100.0% |
| D4 | 5 | 0 | 100.0% |

## 3. 选题池大小

- **PASS_SELECTABLE**（优先选题）: 1
- **PASS**（可进入选题）: 0
- **PASS_NOT_SELECTABLE**（通过但不可操作）: 2
- **总可选题池**: 1
- **不通过**: 2

## 4. 主要问题分布

| 问题 | 数量 |
|---|---|
| XML tag leak in dimension2_explanation (embedded ` | 1 |
| D1 fails: dimension1_explanation lacks any required action verb from the operability list despite adequate length. | 1 |
| dimension2_explanation is null despite d1=DIRECTION_ERROR requiring a d2 value (A4 | 1 |
| B3 | 1 |
| C1 | 1 |
| C3 fail); dimension1_explanation lacks a required action verb (D1 fail) | 1 |
| D1 fails: dimension1_explanation lacks any of the required action verbs from the operability list. | 1 |

## 5. 结论

- 审计通过率: 3/5 (60.0%)
- 可选题池: 1题
- ⚠️ 审计通过率<80%，需要分析常见问题并修正后再选题