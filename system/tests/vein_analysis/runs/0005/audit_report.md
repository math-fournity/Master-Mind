# 审计报告——run_id=0005

**生成时间**：2026-08-11T06:50:23.329654

---

## 当前运行指标

| 维度 | 值 |
|---|---|
| trace数量 | 43 |
| trace类型分布 | {'local': 21, 'nonlocal': 7, 'global': 8, 'cross_case_merge': 1, 'cross_element_meta_pattern': 6} |
| 闭元素数量 | 37 |
| AI优势元素 | 6 |
| 关键实体 | 9 |
| 元反思trace | 2 |
| adv_3(aₙ跳过障碍) | ✅ |

## 逐对比结果

### vs baseline

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 49 | 持平 |
| trace类型-nonlocal | 7 | 26 | 退化 |
| trace类型-cross_element_meta_pattern | 6 | 0 | 进步 |
| trace类型-cross_case_merge | 1 | 0 | 进步 |
| trace类型-local | 21 | 18 | 进步 |
| trace类型-global | 8 | 5 | 进步 |
| closed_elements | 37 | 41 | 持平 |
| ai_advantage | 6 | 11 | 退化 |
| key_entities | 9 | 11 | 持平 |
| meta_reflection | 2 | 2 | 持平 |
| adv3 | True | True | 持平 |

**退化点**：
- trace类型nonlocal: 7 vs 26（<70%）
- AI优势元素: 6 vs 11（<70%）

**进步点**：
- trace类型cross_element_meta_pattern: 6 > 0
- trace类型cross_case_merge: 1 > 0
- trace类型local: 21 > 18
- trace类型global: 8 > 5

### vs 0004

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 11 | 进步 |
| trace类型-nonlocal | 7 | 0 | 进步 |
| trace类型-cross_element_meta_pattern | 6 | 3 | 进步 |
| trace类型-cross_case_merge | 1 | 1 | 持平 |
| trace类型-local | 21 | 3 | 进步 |
| trace类型-global | 8 | 4 | 进步 |
| closed_elements | 37 | 68 | 退化 |
| ai_advantage | 6 | 4 | 进步 |
| key_entities | 9 | 10 | 持平 |
| meta_reflection | 2 | 2 | 持平 |
| adv3 | True | True | 持平 |

**退化点**：
- 闭元素: 37 vs 68（<80%）

**进步点**：
- trace数量: 43 > 11
- trace类型nonlocal: 7 > 0
- trace类型cross_element_meta_pattern: 6 > 3
- trace类型local: 21 > 3
- trace类型global: 8 > 4
- AI优势元素: 6 > 4

### vs 0005

| 维度 | 当前 | 历史 | 状态 |
|---|---|---|---|
| trace_count | 43 | 43 | 持平 |
| trace类型-nonlocal | 7 | 7 | 持平 |
| trace类型-cross_element_meta_pattern | 6 | 6 | 持平 |
| trace类型-cross_case_merge | 1 | 1 | 持平 |
| trace类型-local | 21 | 21 | 持平 |
| trace类型-global | 8 | 8 | 持平 |
| closed_elements | 37 | 37 | 持平 |
| ai_advantage | 6 | 6 | 持平 |
| key_entities | 9 | 9 | 持平 |
| meta_reflection | 2 | 2 | 持平 |
| adv3 | True | True | 持平 |

## 总体判定

**❌ 有退化**——以下维度退化：

- [vs baseline] trace类型nonlocal: 7 vs 26（<70%）
- [vs baseline] AI优势元素: 6 vs 11（<70%）
- [vs 0004] 闭元素: 37 vs 68（<80%）

需要继续改进，直到和所有历史运行对比无退化。
