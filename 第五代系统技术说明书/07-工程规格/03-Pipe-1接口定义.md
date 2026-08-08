# Pipe 1接口定义

**前置阅读**：02-tell端/04-Pipe-1-形式化过滤.md、07-工程规格/02-Pipe-0接口定义.md
**关联文件**：07-工程规格/04-Pipe-2接口定义.md、07-工程规格/06-AQL查询模板.md
**来源**：288号Pipe 1实现、poc9_tell_filter.py

---

## 1. 输入

| 字段 | 类型 | 说明 |
|---|---|---|
| topology | TopologyResult | Pipe 0产出的拓扑结构 |
| tell_db | ArangoDB集合 | tell数据基座 |

## 2. 输出

```python
class TellCandidate:
    tell_id: str                    # tell的唯一标识
    match_score: float              # 大概念匹配分数
    big_concept_topology: dict      # tell的大概念拓扑
    standard_description: str       # tell的标准化语言描述
    small_concept_markers: list     # tell的小概念信号词列表
    hint_ids: list                  # 关联的hint方向ID列表
```

返回：`List[TellCandidate]`——候选tell列表，允许无效tell≤50%。

## 3. 接口规格

```python
def pipe1_filter(topology: TopologyResult, tell_db_collection) -> List[TellCandidate]:
    """
    Pipe 1：用大概念匹配缩小tell范围
    
    处理流程：
    1. AQL查询tell_db集合
    2. 大概念字段匹配（problem_type + ai_method_type + gap_type）
    3. 计算每个候选tell的匹配分数
    4. 按分数排序
    5. 返回候选列表
    
    约束：
    - 不漏（目标tell必须在候选列表中）
    - 可多送（无效tell≤50%）
    """
```

## 4. 匹配分数计算

每个拓扑维度匹配成功得1分，gap_type匹配额外加权：

```python
def calculate_match_score(tell_topology, thinking_topology):
    score = 0
    if tell_topology["problem_type"] == thinking_topology["problem_type"]:
        score += 1
    if tell_topology["ai_method_type"] == thinking_topology["ai_method_type"]:
        score += 1
    if tell_topology["gap_type"] == thinking_topology["gap_type"]:
        score += 1
    if score == 3:  # 三个维度全部匹配，gap_type额外加权
        score += 1
    return score
```

## 5. AQL查询

```sql
FOR tell IN tell_db
  FILTER tell.big_concept_topology.problem_type == @problem_type
    AND tell.big_concept_topology.ai_method_type == @ai_method_type
    AND tell.big_concept_topology.gap_type == @gap_type
  SORT match_score DESC
  LIMIT @max_candidates
  RETURN {
    tell_id: tell.tell_id,
    match_score: 4,  // 三个维度全匹配
    big_concept_topology: tell.big_concept_topology,
    standard_description: tell.standard_description,
    small_concept_markers: tell.small_concept_markers,
    hint_ids: tell.hint_ids
  }
```

## 6. 参考实现

`xishujuzhen/vms/poc9_tell_filter.py`中的Pipe 1实现。
