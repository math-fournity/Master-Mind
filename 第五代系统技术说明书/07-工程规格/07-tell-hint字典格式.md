# tell-hint字典格式

**前置阅读**：02-tell端/07-tell数据基座schema.md、03-hint端/05-hint数据基座schema.md
**来源**：282号vms8_translation_dictionary.json、288/289号实验数据

---

## 1. tell的JSON格式

```json
{
  "tell_id": "tell-001",
  "domain": "number_theory",
  "big_concept_topology": {
    "problem_type": "discrete_combinatorial",
    "ai_method_type": "continuous_analytic",
    "gap_type": "method_problem_mismatch"
  },
  "small_concept_markers": ["mersenne", "primality", "covering_system"],
  "standard_description": "AI在枚举序列参数a的值，试图用covering system覆盖所有情况，但问题是Mersenne素数的存在性，需要用二次剩余/Euler准则",
  "hint_ids": ["T03"],
  "level": 1,
  "non_specificity": 0.7,
  "source": "1631题, POC-VMS-8"
}
```

## 2. hint的JSON格式

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

## 3. tell和hint的多对多关联

通过tell.hint_ids和hint.tell_ids双向关联。

## 4. POC-VMS-8字典格式

`runs/vms_poc_0/vms8_translation_dictionary.json`：

```json
{
  "dictionary_id": "vms8-translation",
  "high_level_direction": "translation",
  "frozen": true,
  "created_at": "2026-08-08",
  "directions": [
    {"direction_id": "T01", "domain": "number_theory", "concrete_form": "翻译到模算术", ...},
    {"direction_id": "T02", "domain": "number_theory", "concrete_form": "翻译到p-adic赋值", ...},
    ...
  ]
}
```

## 5. POC-VMS-9/10的tell数据格式

`runs/vms_poc_0/vms9_pipe_results.json`：

```json
{
  "experiment": "VMS-9",
  "tells": [
    {
      "tell_id": "tell-1",
      "source": "1843题",
      "big_concept_topology": {"problem_type": "discrete_combinatorial", "ai_method_type": "continuous_analytic", "gap_type": "method_problem_mismatch"},
      "hint_id": "T01",
      "small_concept_markers": [...]
    },
    {
      "tell_id": "tell-2",
      "source": "1631题",
      "big_concept_topology": {"problem_type": "structural_existence", "ai_method_type": "enumeration_brute_force", "gap_type": "method_problem_mismatch"},
      "hint_id": "T03",
      "small_concept_markers": [...]
    }
  ]
}
```

## 6. 字典的冻结与扩展

- 冻结：已有字典不修改（不改Q_text/不删方向/不改hint_level）
- 扩展：新增高Level方向时新建独立字典（通过high_level_direction字段区分）
