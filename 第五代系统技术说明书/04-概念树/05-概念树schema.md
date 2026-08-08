# 概念树schema

**前置阅读**：04-概念树/02-概念文件格式.md
**关联文件**：07-工程规格/05-ArangoDB-schema.md
**来源**：287号、289号概念文件设计

---

## 1. 概念树在ArangoDB中的存储

概念树存储在ArangoDB的`concept_tree`集合中（document类型）。每个概念（大概念或小概念）是一个文档。

同时，概念文件也存储在文件系统中，与ArangoDB保持同步。

## 2. concept_tree集合的字段结构

```json
{
  "concept_id": "concept-001",
  "parent_concept_id": null,
  "concept_level": "big",
  "concept_name": "structural-enumeration-mismatch",
  "big_concept_topology": {
    "problem_type": "structural_existence",
    "ai_method_type": "enumeration_brute_force",
    "gap_type": "method_problem_mismatch"
  },
  "standard_description": null,
  "signal_markers": [],
  "related_tell_ids": [],
  "related_hint_ids": []
}
```

小概念文档：

```json
{
  "concept_id": "concept-001-A",
  "parent_concept_id": "concept-001",
  "concept_level": "small",
  "concept_name": "素数存在性",
  "big_concept_topology": null,
  "standard_description": "AI在枚举序列参数a的值，试图用covering system覆盖所有情况，但问题是Mersenne素数的存在性，需要用二次剩余/Euler准则",
  "signal_markers": ["mersenne", "primality", "covering", "covering_system"],
  "related_tell_ids": ["tell-A-1631"],
  "related_hint_ids": ["T03"]
}
```

## 3. 各字段详解

### concept_id
概念的唯一标识符。命名规范：`concept-<序号>`（大概念）或`concept-<父序号>-<字母>`（小概念）。

### parent_concept_id
父概念的ID。大概念的parent_concept_id为null（根节点），小概念的parent_concept_id指向所属的大概念。

### concept_level
概念级别：`big`（大概念）或`small`（小概念）。

### concept_name
概念名称。大概念的名称由拓扑维度拼接而成（如"structural-enumeration-mismatch"），小概念的名称是描述性的（如"素数存在性"）。

### big_concept_topology
大概念的拓扑结构。只在大概念文档中填写，小概念文档中为null。

### standard_description
标准化语言描述。只在小概念文档中填写，大概念文档中为null。

### signal_markers
小概念信号词列表。只在小概念文档中填写，大概念文档中为空列表。

### related_tell_ids
关联的tell ID列表。小概念关联到使用该概念的具体tell。

### related_hint_ids
关联的hint方向ID列表。通过tell的hint_ids间接关联。

## 4. 大概念节点和小概念节点

### 大概念节点

```
concept_id: concept-001
concept_level: big
concept_name: structural-enumeration-mismatch
big_concept_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_problem_mismatch}
signal_markers: []  # 大概念没有信号词
related_tell_ids: []  # 大概念不直接关联tell
```

### 小概念节点

```
concept_id: concept-001-A
parent_concept_id: concept-001  # 指向大概念
concept_level: small
concept_name: 素数存在性
signal_markers: [mersenne, primality, covering, covering_system]
related_tell_ids: [tell-A-1631]
```

## 5. 概念文件的文件系统存储

除了ArangoDB存储，概念文件也存储在文件系统中：

```
concept_files/
├── CF-structural-existence-enumeration_brute_force-method_problem_mismatch.json
├── CF-discrete_combinatorial-continuous_analytic-method_problem_mismatch.json
└── ...
```

每个概念文件是一个JSON文件，包含一个大概念下的所有小概念。文件名由大概念拓扑维度拼接而成。

文件系统存储和ArangoDB存储保持同步——修改一处时同步更新另一处。

## 6. 概念树的查询

### 获取所有大概念

```sql
FOR c IN concept_tree
  FILTER c.concept_level == "big"
  RETURN c
```

### 获取某个大概念下的所有小概念

```sql
FOR c IN concept_tree
  FILTER c.parent_concept_id == @big_concept_id
    AND c.concept_level == "small"
  RETURN c
```

### 按大概念拓扑加载小概念（Pipe 2使用）

```sql
FOR c IN concept_tree
  FILTER c.concept_level == "small"
    AND c.parent_concept_id IN (
      FOR big IN concept_tree
        FILTER big.big_concept_topology.problem_type == @problem_type
          AND big.big_concept_topology.ai_method_type == @ai_method_type
          AND big.big_concept_topology.gap_type == @gap_type
        RETURN big.concept_id
    )
  RETURN c
```

## 7. 索引设计

| 索引 | 字段 | 用途 |
|---|---|---|
| parent_concept_id索引 | parent_concept_id | 查询某个大概念下的所有小概念 |
| concept_level索引 | concept_level | 按级别筛选（big/small） |
| big_concept_topology索引 | big_concept_topology.problem_type + ai_method_type + gap_type | 按大概念拓扑快速查找 |

## 8. 概念树与tell数据基座的同步

当新的tell被加入tell_db时，需要同步更新concept_tree：

1. 检查新tell的大概念拓扑是否已有对应的大概念节点
   - 如果有→在已有大概念下检查是否需要新建小概念
   - 如果没有→新建大概念节点
2. 检查新tell的标准化语言描述是否属于已有小概念
   - 如果属于→在已有小概念的related_tell_ids中新增该tell
   - 如果不属于→新建小概念节点，提取信号词
3. 同步更新文件系统中的概念文件

这个同步过程可以自动化——用NLP方法从新tell的标准化语言描述中自动判断属于哪个小概念，或是否需要新建小概念。这是未来的自动化方向。
