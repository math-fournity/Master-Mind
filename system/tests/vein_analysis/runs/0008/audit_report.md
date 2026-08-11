# 审计报告——run_id=0008

**生成时间**：2026-08-11T08:01:28.792348

---

## 当前运行指标

| 维度 | 值 |
|---|---|
| trace数量 | 19 |
| trace类型分布 | {'local': 7, 'cross_element_meta_pattern': 3, 'cross_case_merge': 4, 'nonlocal': 5} |
| 闭元素数量 | 37 |
| AI优势元素 | 5 |
| 关键实体 | 8 |
| 元反思trace | 1 |
| adv_3(aₙ跳过障碍) | ✅ |

## 逐对比结果

### vs baseline

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 19 | 49 | 退化 |
| trace类型-cross_case_merge | 4 | 0 | 进步 |
| trace类型-cross_element_meta_pattern | 3 | 0 | 进步 |
| trace类型-nonlocal | 5 | 26 | 退化 |
| trace类型-local | 7 | 18 | 退化 |
| trace类型-global | 0 | 5 | 退化 |
| closed_elements | 37 | 41 | 持平 |
| ai_advantage | 5 | 11 | 退化 |
| key_entities | 8 | 11 | 持平 |
| meta_reflection | 1 | 2 | 退化 |
| adv3 | True | True | 持平 |

**退化点**：
- trace数量: 19 vs 49（<80%）
- trace类型nonlocal: 5 vs 26（<70%）
- trace类型local: 7 vs 18（<70%）
- trace类型global: 0 vs 5（<70%）
- AI优势元素: 5 vs 11（<70%）
- 元反思trace: 1 vs 2

**进步点**：
- trace类型cross_case_merge: 4 > 0
- trace类型cross_element_meta_pattern: 3 > 0

### vs 0004

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 19 | 11 | 进步 |
| trace类型-cross_case_merge | 4 | 1 | 进步 |
| trace类型-cross_element_meta_pattern | 3 | 3 | 持平 |
| trace类型-nonlocal | 5 | 0 | 进步 |
| trace类型-local | 7 | 3 | 进步 |
| trace类型-global | 0 | 4 | 退化 |
| closed_elements | 37 | 68 | 退化 |
| ai_advantage | 5 | 4 | 进步 |
| key_entities | 8 | 10 | 持平 |
| meta_reflection | 1 | 2 | 退化 |
| adv3 | True | True | 持平 |

**退化点**：
- trace类型global: 0 vs 4（<70%）
- 闭元素: 37 vs 68（<80%）
- 元反思trace: 1 vs 2

**进步点**：
- trace数量: 19 > 11
- trace类型cross_case_merge: 4 > 1
- trace类型nonlocal: 5 > 0
- trace类型local: 7 > 3
- AI优势元素: 5 > 4

### vs 0005

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 19 | 43 | 退化 |
| trace类型-cross_case_merge | 4 | 1 | 进步 |
| trace类型-cross_element_meta_pattern | 3 | 6 | 退化 |
| trace类型-nonlocal | 5 | 7 | 持平 |
| trace类型-local | 7 | 21 | 退化 |
| trace类型-global | 0 | 8 | 退化 |
| closed_elements | 37 | 37 | 持平 |
| ai_advantage | 5 | 6 | 持平 |
| key_entities | 8 | 9 | 持平 |
| meta_reflection | 1 | 2 | 退化 |
| adv3 | True | True | 持平 |

**退化点**：
- trace数量: 19 vs 43（<80%）
- trace类型cross_element_meta_pattern: 3 vs 6（<70%）
- trace类型local: 7 vs 21（<70%）
- trace类型global: 0 vs 8（<70%）
- 元反思trace: 1 vs 2

**进步点**：
- trace类型cross_case_merge: 4 > 1

### vs 0008

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 19 | 19 | 持平 |
| trace类型-nonlocal | 5 | 5 | 持平 |
| trace类型-cross_case_merge | 4 | 4 | 持平 |
| trace类型-cross_element_meta_pattern | 3 | 3 | 持平 |
| trace类型-local | 7 | 7 | 持平 |
| closed_elements | 37 | 37 | 持平 |
| ai_advantage | 5 | 5 | 持平 |
| key_entities | 8 | 8 | 持平 |
| meta_reflection | 1 | 1 | 持平 |
| adv3 | True | True | 持平 |

## 总体判定

**❌ 有退化**——以下维度退化：

- [vs baseline] trace数量: 19 vs 49（<80%）
- [vs baseline] trace类型nonlocal: 5 vs 26（<70%）
- [vs baseline] trace类型local: 7 vs 18（<70%）
- [vs baseline] trace类型global: 0 vs 5（<70%）
- [vs baseline] AI优势元素: 5 vs 11（<70%）
- [vs baseline] 元反思trace: 1 vs 2
- [vs 0004] trace类型global: 0 vs 4（<70%）
- [vs 0004] 闭元素: 37 vs 68（<80%）
- [vs 0004] 元反思trace: 1 vs 2
- [vs 0005] trace数量: 19 vs 43（<80%）
- [vs 0005] trace类型cross_element_meta_pattern: 3 vs 6（<70%）
- [vs 0005] trace类型local: 7 vs 21（<70%）
- [vs 0005] trace类型global: 0 vs 8（<70%）
- [vs 0005] 元反思trace: 1 vs 2

需要继续改进，直到和所有历史运行对比无退化。
