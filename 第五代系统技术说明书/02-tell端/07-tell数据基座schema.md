# tell数据基座schema

**前置阅读**：02-tell端/01-tell的四个成分.md、02-tell端/02-tell的去特化.md
**关联文件**：07-工程规格/05-ArangoDB-schema.md、03-hint端/05-hint数据基座schema.md
**来源**：287号、288/289号实验数据格式、267号ArangoDB schema

---

## 1. tell在ArangoDB中的集合

tell存储在ArangoDB的`tell_db`集合中（document类型）。每个tell是一个文档。

## 2. tell文档的字段结构

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

## 3. 各字段详解

### tell_id
tell的唯一标识符。命名规范：`tell-<序号>`或`tell-<来源题号>-<简述>`。

### domain
tell所属的数学领域。如number_theory / algebra / combinatorics / geometry / cross_domain。

### big_concept_topology
tell的大概念拓扑——用于Pipe 1形式化过滤的索引key。包含3个维度：
- **problem_type**：问题类型，如discrete_combinatorial / structural_existence
- **ai_method_type**：AI方法类型，如continuous_analytic / enumeration_brute_force
- **gap_type**：缺口类型，如method_problem_mismatch

这3个维度是Pipe 0从thinking中提取的拓扑结构，Pipe 1用它们做匹配。

### small_concept_markers
tell的小概念信号词列表——用于Pipe 2小概念标记分辨。这些信号词从standard_description中提取。

当Pipe 1给同分（多个tell的大概念拓扑相同）时，Pipe 2用这些信号词在thinking中做标记分辨。

### standard_description
tell的标准化语言描述——包含"AI在做什么/问题是什么/正确方向是什么"三部分的自然语言描述。

这是小概念信号词的来源，也是概念文件的输入。

### hint_ids
关联的hint方向ID列表——tell和hint是多对多关系，一个tell可以关联多个hint。

通过这个字段和hint_db的tell_ids字段双向关联。

### level
tell的Level——0到1实数，表示tell的抽象度。去特化后的tell通常是Level 1（可跨题泛化）。

### non_specificity
tell的非特定性——0到1实数，表示识别这个tell是否需要知道答案。去特化后的tell通常非特定性较低（不需要知道答案就能识别）。

### source
tell的来源——记录是从哪道题、哪个实验中提取的。用于追溯和验证。

## 4. 大概念拓扑字段——Pipe 1的索引key

big_concept_topology中的3个维度是Pipe 1形式化过滤的索引key。在ArangoDB中为这些字段建索引：

```javascript
// 在tell_db集合上建索引
db.tell_db.ensureIndex({
  type: "persistent",
  fields: ["big_concept_topology.problem_type", "big_concept_topology.ai_method_type", "big_concept_topology.gap_type"]
});
```

这样Pipe 1的AQL查询可以快速定位大概念拓扑匹配的tell，不需要全量扫描。

## 5. 小概念标记字段——Pipe 2的输入

small_concept_markers中的信号词是Pipe 2小概念标记分辨的输入。Pipe 2在thinking文本中统计这些信号词的出现频次，计算combined_score。

这些信号词不需要建索引——Pipe 2是在Pipe 1筛出的候选tell中做标记分辨，候选数量已经很小（通常几十到几百个），直接遍历即可。

## 6. tell和hint的关联

tell和hint是多对多关系，通过以下字段双向关联：

- tell_db文档的`hint_ids`字段：存储该tell关联的所有hint方向ID
- hint_db文档的`tell_ids`字段：存储该hint方向可以被哪些tell触发

AQL查询关联：

```sql
// 查询某个tell关联的所有hint
FOR hint IN hint_db
  FILTER @tell_id IN hint.tell_ids
  RETURN hint

// 查询某个hint可以被哪些tell触发
FOR tell IN tell_db
  FILTER @hint_id IN tell.hint_ids
  RETURN tell
```

## 7. 索引设计

| 索引 | 字段 | 用途 |
|---|---|---|
| 大概念拓扑索引 | big_concept_topology.problem_type + ai_method_type + gap_type | Pipe 1形式化过滤的快速查询 |
| domain索引 | domain | 按领域筛选tell |
| hint_ids索引 | hint_ids | 查询某个hint关联的tell |

## 8. 数据基座增长机制

tell数据基座是**单调增长**的——每次引导树闭环运行后，新的tell被提炼并加入数据基座。tell只加不删，随着运行次数增加而增长。

这继承了第三代（伏羲）的"数据基座是形式化边界的显式记录"——数据基座单调增长，证书只加不删。每一次闭环运行，形式化边界向前推进一步，新的tell被固化到数据基座中。

详细的增长机制见05-引导树闭环/01-三个推动关系.md。
