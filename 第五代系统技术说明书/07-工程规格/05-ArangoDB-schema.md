# ArangoDB schema

**前置阅读**：07-工程规格/01-系统架构总图.md、02-tell端/07-tell数据基座schema.md
**关联文件**：全部07-工程规格文件
**来源**：267号§6、272号、287号、288/289号实验数据格式

---

## 1. 集合总览

| 集合 | 类型 | 用途 |
|---|---|---|
| tree_nodes | document | 树节点（每个=一个数学处境） |
| tree_edges | edge | 树边（每条=一个提示Q引导的转移） |
| problems | document | 题目（每道题一棵树） |
| ai_instances | document | 推理AI实例 |
| tell_db | document | tell数据基座 |
| hint_db | document | hint字典 |
| concept_tree | document | 概念树（大概念和小概念） |
| patterns | document | Pattern集合（来自POC-VMS-1的群论Pattern） |

## 2. tree_nodes集合

```javascript
{
  "_key": "node-001",
  "problem_id": "prob-1843",
  "node_type": "root",  // root / internal / leaf_success / leaf_deadend / leaf_truncated
  "situation": {  // 六元组状态
    "V_t": ["中心化结果", "q(x)定义", "两个恒等式"],
    "F_t": ["稳定性方程"],
    "O_t": ["估计D下界", "传递到δ下界"],
    "R_t": "投影到根的表示",
    "E_t": ["紧性归约条件"],
    "U_t": "D的量级问题"
  },
  "situation_text": "AI得到了稳定性方程5D=3√5(B_r-B_s)+2C，其中D=√5(pn-k)",
  "depth": 5,
  "parent_edge_key": "edge-004",
  "path_from_root": ["node-000", "node-001", "node-002", "node-003", "node-004", "node-005"],
  "created_by_ai": "ai-instance-001",
  "created_at": 1799697600.0,
  "trajectory_segment": { "thinking": "...", "tool_calls": [...] },
  "status": "growing",  // growing / completed / deadend / truncated
  "retrieval_done": false,
  "directions_identified": [],
  "ai_instances_started": []
}
```

## 3. tree_edges集合

```javascript
{
  "_key": "edge-001",
  "_from": "tree_nodes/node-000",
  "_to": "tree_nodes/node-001",
  "problem_id": "prob-1843",
  "hint_q": "把问题翻译到模算术——把因子按模4分类",
  "hint_q_id": "T01",
  "hint_level": 0.5,
  "ai_instance_id": "ai-instance-001",
  "created_at": 1799697600.0,
  "edge_status": "growing"  // growing / completed / deadend / truncated
}
```

## 4. problems集合

```javascript
{
  "_key": "prob-1843",
  "problem_text": "证明存在常数C>0使得...",
  "root_node_key": "node-000",
  "status": "growing",  // growing / solved / exhausted
  "solution_path": null,  // solved时填充
  "created_at": 1799697600.0,
  "solved_at": null,
  "total_nodes": 15,
  "total_edges": 12,
  "ai_instances_used": 3
}
```

## 5. ai_instances集合

```javascript
{
  "_key": "ai-instance-001",
  "problem_id": "prob-1843",
  "entry_node_key": "node-000",
  "entry_edge_key": null,
  "lineage_text": "你正在解答以下数学题：...",
  "hint_q": "把问题翻译到模算术",
  "tmux_session": "harness-prob-1843-branch-A",
  "devin_session_id": "session-uuid-xxx",
  "status": "running",  // running / completed / crashed / truncated
  "started_at": 1799697600.0,
  "ended_at": null,
  "end_reason": null,  // token_limit / crash / solution_found / manual_stop
  "trajectory_dir": "/data/.../prob-1843-branch-A/",
  "nodes_contributed": ["node-001", "node-002", "node-003"]
}
```

## 6. tell_db集合

详见02-tell端/07-tell数据基座schema.md。

## 7. hint_db集合

详见03-hint端/05-hint数据基座schema.md。

## 8. concept_tree集合

详见04-概念树/05-概念树schema.md。

## 9. 索引设计

| 集合 | 索引字段 | 索引类型 | 用途 |
|---|---|---|---|
| tree_nodes | problem_id | persistent | 按题目查询节点 |
| tree_nodes | status | persistent | 按状态筛选可分配节点 |
| tree_edges | problem_id | persistent | 按题目查询边 |
| tell_db | big_concept_topology.problem_type + ai_method_type + gap_type | persistent | Pipe 1形式化过滤 |
| hint_db | domain | persistent | 按领域筛选方向 |
| concept_tree | parent_concept_id | persistent | 查询大概念下的小概念 |
| concept_tree | concept_level | persistent | 按级别筛选 |
