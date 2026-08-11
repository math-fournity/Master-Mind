# 审计报告——run_id=0009

**生成时间**：2026-08-11T08:23:39.425679

---

## 当前运行指标

| 维度 | 值 |
|---|---|
| trace数量 | 43 |
| trace类型分布 | {'local': 21, 'nonlocal': 5, 'cross_case_merge': 6, 'global': 7, 'cross_element_meta_pattern': 4} |
| 闭元素数量 | 52 |
| AI优势元素 | 7 |
| 关键实体 | 10 |
| 元反思trace | 3 |
| adv_3(aₙ跳过障碍) | ✅ |

## 逐对比结果

### vs baseline

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 49 | 持平 |
| trace类型-cross_element_meta_pattern | 4 | 0 | 进步 |
| trace类型-local | 21 | 18 | 进步 |
| trace类型-global | 7 | 5 | 进步 |
| trace类型-nonlocal | 5 | 26 | 退化 |
| trace类型-cross_case_merge | 6 | 0 | 进步 |
| closed_elements | 52 | 41 | 进步 |
| ai_advantage | 7 | 11 | 退化 |
| key_entities | 10 | 11 | 持平 |
| meta_reflection | 3 | 2 | 进步 |
| adv3 | True | True | 持平 |

**退化点**：
- trace类型nonlocal: 5 vs 26（<70%）
- AI优势元素: 7 vs 11（<70%）

**进步点**：
- trace类型cross_element_meta_pattern: 4 > 0
- trace类型local: 21 > 18
- trace类型global: 7 > 5
- trace类型cross_case_merge: 6 > 0
- 闭元素: 52 > 41
- 元反思trace: 3 > 2

### vs 0004

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 11 | 进步 |
| trace类型-cross_element_meta_pattern | 4 | 3 | 进步 |
| trace类型-local | 21 | 3 | 进步 |
| trace类型-global | 7 | 4 | 进步 |
| trace类型-nonlocal | 5 | 0 | 进步 |
| trace类型-cross_case_merge | 6 | 1 | 进步 |
| closed_elements | 52 | 68 | 退化 |
| ai_advantage | 7 | 4 | 进步 |
| key_entities | 10 | 10 | 持平 |
| meta_reflection | 3 | 2 | 进步 |
| adv3 | True | True | 持平 |

**退化点**：
- 闭元素: 52 vs 68（<80%）

**进步点**：
- trace数量: 43 > 11
- trace类型cross_element_meta_pattern: 4 > 3
- trace类型local: 21 > 3
- trace类型global: 7 > 4
- trace类型nonlocal: 5 > 0
- trace类型cross_case_merge: 6 > 1
- AI优势元素: 7 > 4
- 元反思trace: 3 > 2

### vs 0005

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 43 | 持平 |
| trace类型-cross_element_meta_pattern | 4 | 6 | 退化 |
| trace类型-local | 21 | 21 | 持平 |
| trace类型-global | 7 | 8 | 持平 |
| trace类型-nonlocal | 5 | 7 | 持平 |
| trace类型-cross_case_merge | 6 | 1 | 进步 |
| closed_elements | 52 | 37 | 进步 |
| ai_advantage | 7 | 6 | 进步 |
| key_entities | 10 | 9 | 进步 |
| meta_reflection | 3 | 2 | 进步 |
| adv3 | True | True | 持平 |

**退化点**：
- trace类型cross_element_meta_pattern: 4 vs 6（<70%）

**进步点**：
- trace类型cross_case_merge: 6 > 1
- 闭元素: 52 > 37
- AI优势元素: 7 > 6
- 关键实体: 10 > 9
- 元反思trace: 3 > 2

### vs 0008

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 19 | 进步 |
| trace类型-cross_element_meta_pattern | 4 | 3 | 进步 |
| trace类型-local | 21 | 7 | 进步 |
| trace类型-global | 7 | 0 | 进步 |
| trace类型-nonlocal | 5 | 5 | 持平 |
| trace类型-cross_case_merge | 6 | 4 | 进步 |
| closed_elements | 52 | 37 | 进步 |
| ai_advantage | 7 | 5 | 进步 |
| key_entities | 10 | 8 | 进步 |
| meta_reflection | 3 | 1 | 进步 |
| adv3 | True | True | 持平 |

**进步点**：
- trace数量: 43 > 19
- trace类型cross_element_meta_pattern: 4 > 3
- trace类型local: 21 > 7
- trace类型global: 7 > 0
- trace类型cross_case_merge: 6 > 4
- 闭元素: 52 > 37
- AI优势元素: 7 > 5
- 关键实体: 10 > 8
- 元反思trace: 3 > 1

### vs 0009

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 43 | 持平 |
| trace类型-cross_element_meta_pattern | 4 | 4 | 持平 |
| trace类型-local | 21 | 21 | 持平 |
| trace类型-global | 7 | 7 | 持平 |
| trace类型-nonlocal | 5 | 5 | 持平 |
| trace类型-cross_case_merge | 6 | 6 | 持平 |
| closed_elements | 52 | 52 | 持平 |
| ai_advantage | 7 | 7 | 持平 |
| key_entities | 10 | 10 | 持平 |
| meta_reflection | 3 | 3 | 持平 |
| adv3 | True | True | 持平 |

## 总体判定

**❌ 有退化**——以下维度退化：

- [vs baseline] trace类型nonlocal: 5 vs 26（<70%）
- [vs baseline] AI优势元素: 7 vs 11（<70%）
- [vs 0004] 闭元素: 52 vs 68（<80%）
- [vs 0005] trace类型cross_element_meta_pattern: 4 vs 6（<70%）

需要继续改进，直到和所有历史运行对比无退化。
