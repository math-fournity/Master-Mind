# hint数据基座schema

**前置阅读**：03-hint端/01-hint字典的结构.md
**关联文件**：02-tell端/07-tell数据基座schema.md、07-工程规格/05-ArangoDB-schema.md
**来源**：281号、282号vms8_translation_dictionary.json格式、267号ArangoDB schema

---

## 1. hint字典在ArangoDB中的集合

hint字典存储在ArangoDB的`hint_db`集合中（document类型）。每个翻译方向是一个文档。

## 2. hint文档的字段结构

```json
{
  "direction_id": "T01",
  "domain": "number_theory",
  "high_level_direction": "translation",
  "concrete_form": "翻译到模算术",
  "Q_text": "把整数方程/不等式转化为模p的同余问题",
  "level": 0.5,
  "non_specificity": 0.7,
  "hint_level": "H1",
  "tell_ids": ["tell-001", "tell-003"],
  "source": "281号工程化"
}
```

## 3. 各字段详解

### direction_id
翻译方向的唯一标识符。命名规范：`T<序号>`，如T01-T24。

### domain
方向所属的数学领域。如number_theory / algebra / combinatorics / geometry / cross_domain。

### high_level_direction
来源的高Level方向。当前字典中的24个方向都来自"translation"（翻译语言）。未来扩展其他高Level方向时会有新的值，如"auxiliary_construction"（辅助对象构造）、"pincer_contradiction"（夹击矛盾）等。

### concrete_form
具体翻译形式的简短描述，如"翻译到模算术"。

### Q_text
给AI的方向提示文本。这是实际注入给新AI的提示内容。

### level
方向的Level（0-1实数）。翻译方向通常是0.5-0.8——它们是跨领域的思维模式但有一定具体性。

### non_specificity
方向的非特定性（0-1实数）。翻译方向通常非特定性较低（0.6-0.8）——不需要知道答案就能发出这些方向。

### hint_level
Hint泄漏分级（H0-H4）。翻译方向通常是H1（思维操作，不泄漏答案）。

### tell_ids
关联的tell ID列表——该方向可以被哪些tell触发。这是tell和hint多对多关系的反向关联。

通过这个字段和tell_db的hint_ids字段双向关联。

### source
方向的来源——记录是从哪个高Level方向工程化而来。

## 4. tell和hint的多对多关联

tell和hint通过以下字段双向关联：

- **tell_db文档的`hint_ids`字段**：存储该tell关联的所有hint方向ID
- **hint_db文档的`tell_ids`字段**：存储该hint方向可以被哪些tell触发

### AQL查询关联

```sql
-- 查询某个tell关联的所有hint方向
FOR hint IN hint_db
  FILTER @tell_id IN hint.tell_ids
  RETURN hint

-- 查询某个hint方向可以被哪些tell触发
FOR tell IN tell_db
  FILTER @direction_id IN tell.hint_ids
  RETURN tell
```

## 5. 字典的冻结机制

字典离线建好后**冻结**——之后不再修改。冻结的含义：

- 不修改已有方向的Q_text（方向提示文本不变）
- 不删除已有方向（方向不会被移除）
- 不改变已有方向的hint_level（泄漏级别不变）

冻结的目的是确保字典的预测力——字典是在不知道题目的情况下建的，如果事后修改就失去了预测意义。

## 6. 字典的扩展机制

虽然已有字典冻结不修改，但可以**新增独立字典**——当系统需要新的高Level方向（如"辅助对象构造"）时，用同样的方法遍历各领域low level化，形成新的字典。

新字典和已有字典并存，通过`high_level_direction`字段区分。检索时可以根据tell的分叉类型选择对应的高Level方向字典。

## 7. POC-VMS-8字典的完整结构

POC-VMS-8使用的24个翻译方向字典存储在`runs/vms_poc_0/vms8_translation_dictionary.json`中。完整结构：

```json
{
  "dictionary_id": "vms8-translation",
  "high_level_direction": "translation",
  "frozen": true,
  "created_at": "2026-08-08",
  "directions": [
    {
      "direction_id": "T01",
      "domain": "number_theory",
      "concrete_form": "翻译到模算术",
      "Q_text": "把整数方程/不等式转化为模p的同余问题",
      "level": 0.5,
      "non_specificity": 0.7,
      "hint_level": "H1"
    },
    {
      "direction_id": "T02",
      "domain": "number_theory",
      "concrete_form": "翻译到p-adic赋值",
      "Q_text": "把整除/幂次问题转化为p-adic赋值分析",
      "level": 0.6,
      "non_specificity": 0.7,
      "hint_level": "H1"
    },
    ...  // 共24个方向
  ]
}
```

## 8. 索引设计

| 索引 | 字段 | 用途 |
|---|---|---|
| domain索引 | domain | 按领域筛选方向 |
| high_level_direction索引 | high_level_direction | 按高Level方向筛选 |
| tell_ids索引 | tell_ids | 查询某个tell关联的所有方向 |
