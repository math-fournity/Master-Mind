# AQL查询模板

**前置阅读**：07-工程规格/05-ArangoDB-schema.md、07-工程规格/03-Pipe-1接口定义.md
**来源**：267号§6.3、288号AQL查询

---

## 1. Pipe 1形式化过滤

```sql
// 按大概念拓扑查询候选tell
FOR tell IN tell_db
  FILTER tell.big_concept_topology.problem_type == @problem_type
    AND tell.big_concept_topology.ai_method_type == @ai_method_type
    AND tell.big_concept_topology.gap_type == @gap_type
  RETURN {
    tell_id: tell.tell_id,
    match_score: 4,
    big_concept_topology: tell.big_concept_topology,
    standard_description: tell.standard_description,
    small_concept_markers: tell.small_concept_markers,
    hint_ids: tell.hint_ids
  }
```

## 2. 树节点查询

```sql
// 获取某棵树的所有节点
FOR node IN tree_nodes
  FILTER node.problem_id == @problem_id
  RETURN node

// 获取从根到某节点的路径（利用path_from_root冗余字段）
FOR node IN tree_nodes
  FILTER node._key == @node_key
  RETURN node.path_from_root

// 获取所有可分配新AI的节点
FOR node IN tree_nodes
  FILTER node.problem_id == @problem_id
    AND node.status == "growing"
    AND node.retrieval_done == true
    AND node.directions_identified != []
  RETURN node

// 获取某棵树的成功路径
FOR node IN tree_nodes
  FILTER node.problem_id == @problem_id
    AND node.node_type == "leaf_success"
  RETURN node.path_from_root
```

## 3. 树边查询

```sql
// 获取某棵树的所有边
FOR edge IN tree_edges
  FILTER edge.problem_id == @problem_id
  RETURN edge
```

## 4. tell和hint关联查询

```sql
// 查询某个tell关联的所有hint
FOR hint IN hint_db
  FILTER @tell_id IN hint.tell_ids
  RETURN hint

// 查询某个hint可以被哪些tell触发
FOR tell IN tell_db
  FILTER @direction_id IN tell.hint_ids
  RETURN tell
```

## 5. 概念树查询

```sql
// 获取所有大概念
FOR c IN concept_tree
  FILTER c.concept_level == "big"
  RETURN c

// 获取某个大概念下的所有小概念
FOR c IN concept_tree
  FILTER c.parent_concept_id == @big_concept_id
    AND c.concept_level == "small"
  RETURN c

// 按大概念拓扑加载小概念（Pipe 2使用）
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

## 6. AI实例查询

```sql
// 获取某道题的所有AI实例
FOR ai IN ai_instances
  FILTER ai.problem_id == @problem_id
  RETURN ai

// 获取所有正在运行的AI实例
FOR ai IN ai_instances
  FILTER ai.status == "running"
  RETURN ai
```
