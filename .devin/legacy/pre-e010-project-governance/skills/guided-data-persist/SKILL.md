---
name: guided-data-persist
description: >
  引导式数学解题元组群·Skill 5：数据持久化。
  将DFS树、对话导出、引导者决策等完整推理历史记录到ArangoDB+文件系统。
  WHEN to use: 元组群guided-math-solving中，每轮交互后或实验结束时。
  WHEN NOT to use: 非引导实验、数据已持久化。
---

# guided-data-persist skill

## 用途

元组群 `guided-math-solving` 的 Skill 5。将完整推理历史记录到ArangoDB + 文件系统。

**原则**：数据不可复现（AI非确定性），不存就永远没了。从第一轮就完整记录。

## 何时调用

1. **Skill 3每轮交互后**——增量持久化当前轮次的数据
2. **实验结束时**——最终持久化，写入结果验证和性能指标
3. **回溯时（Skill 4）**——记录回溯决策和新session信息

## 数据保留9层（来自214号8.14节）

| 层 | 内容 | 存储位置 |
|---|---|---|
| 1. 题目元数据 | problem_id、题目文本、来源、标准答案 | ArangoDB dfs_cases |
| 2. 运行元数据 | run_id、devin版本、模型版本、AGENTS.md快照 | ArangoDB dfs_cases + 文件系统 session_info.json |
| 3. 预演记录 | 模拟QA脚本、预演Level SUM | ArangoDB dfs_cases + 文件系统 rehearsal.md |
| 4. DFS树 | 完整树结构、成功路径、回溯次数、Level SUM | ArangoDB dfs_nodes+dfs_edges + 文件系统 dfs_tree.json |
| 5. 节点完整记录 | Q文本/Level/候选/选择理由 + A文本/变体/状态/工具使用 | ArangoDB dfs_nodes |
| 6. Session级记录 | --export JSON、tmux capture、pipe-pane日志、压缩事件 | 文件系统 + ArangoDB dfs_sessions |
| 7. 引导者决策日志 | 为什么选这个Q、考虑过什么替代 | ArangoDB dfs_decisions |
| 8. 结果验证 | 最终答案、是否正确、证明完整性 | ArangoDB dfs_cases |
| 9. 性能指标 | 总耗时、轮次、session数、回溯数、token总量 | ArangoDB dfs_cases |

## ArangoDB Collections

```
dfs_cases          (document)  — 第1+2+3+8+9层
dfs_nodes          (document)  — 第5层
dfs_edges          (edge)      — parent→child树边
dfs_decisions      (document)  — 第7层
dfs_sessions       (document)  — 第6层
dfs_compressions   (document)  — 压缩事件
```

**数据库隔离**：使用 `xishujuzhen_math_glm52`（本repo专用数据库，见AGENTS.md硬约束3）。

## 工作流

### 增量持久化（每轮交互后）

```python
# 1. dfs_tree.json 已由 Skill 3 更新（文件系统）

# 2. 同步当前节点到 ArangoDB
node = tree.nodes[current_node_id]
arango_client.collection("dfs_nodes").insert({
    "node_id": node.node_id,
    "case_id": case_id,
    "parent_node_id": node.parent_id,
    "depth": node.depth,
    "q_text": node.q_text,
    "q_level": node.q_level,
    "q_category": node.q_category,
    "q_candidates": node.candidates,
    "q_selected_reason": node.q_selected_reason,
    "a_text": node.a_text,
    "a_variants": node.a_variants,
    "a_status": node.a_status,
    "a_status_reason": node.a_status_reason,
    "session_id": node.session_id,
    "export_path": node.export_path,
    "timestamp": node.timestamp,
})

# 3. 如果有父节点，添加边
if node.parent_id:
    arango_client.collection("dfs_edges").insert({
        "_from": f"dfs_nodes/{node.parent_id}",
        "_to": f"dfs_nodes/{node.node_id}",
        "case_id": case_id,
        "edge_type": "q_prompt",
    })

# 4. 记录引导者决策
arango_client.collection("dfs_decisions").insert({
    "decision_id": f"dec_{node.node_id}",
    "node_id": node.node_id,
    "case_id": case_id,
    "decision_type": "select_q",
    "decision_reason": node.q_selected_reason,
    "alternatives_considered": node.candidates,
    "timestamp": node.timestamp,
})

# 5. 保存tmux capture到文件系统
capture_path = f"{RUN_DIR}/captures/capture_{node.node_id}.txt"
with open(capture_path, 'w') as f:
    f.write(tmux_capture_output)
```

### 最终持久化（实验结束时）

```python
# 1. 创建/更新 dfs_cases 文档
case_doc = {
    "case_id": case_id,
    "problem_id": problem_id,
    "problem_text": problem_text,
    "source_dataset": source_dataset,
    "source_competition": source_competition,
    "run_id": run_id,
    "run_timestamp": start_time,
    "devin_cli_version": devin_version,
    "model_name": model_name,
    "rehearsal_level_sum": rehearsal_level_sum,
    "dfs_tree_summary": tree.summary(),
    "final_answer": final_answer,
    "is_correct": is_correct,
    "verification_method": verification_method,
    "proof_completeness": proof_completeness,
    "proof_correctness": proof_correctness,
    "total_time": total_time,
    "total_turns": total_turns,
    "total_sessions": total_sessions,
    "total_backtracks": total_backtracks,
    "level_sum_achieved": tree.level_sum_on_path(success_node_id),
    "level_drop_count": level_drop_count,
}
arango_client.collection("dfs_cases").insert(case_doc)

# 2. 写入 result_summary.json 到文件系统
with open(f"{RUN_DIR}/result_summary.json", 'w') as f:
    json.dump(case_doc, f, ensure_ascii=False, indent=2)

# 3. 更新认知资产索引
# 在 xishujuzhen/cognition_asset_index.md 中记录case_id
```

### 回溯时持久化

```python
# 记录回溯决策
arango_client.collection("dfs_decisions").insert({
    "decision_id": f"dec_backtrack_{timestamp}",
    "node_id": dead_end_node_id,
    "case_id": case_id,
    "decision_type": "backtrack",
    "decision_reason": "AI卡住/走错方向/候选耗尽",
    "alternatives_considered": [...],
    "timestamp": timestamp,
})

# 记录新session信息
arango_client.collection("dfs_sessions").insert({
    "session_id": new_session_name,
    "case_id": case_id,
    "export_path": new_export_path,
    "start_time": new_session_start,
    "is_backtrack_session": True,
    "fork_node_id": fork_node_id,
})
```

## 注意事项

1. **数据库隔离**：必须使用 `xishujuzhen_math_glm52`，不是 `xishujuzhen_math`（AGENTS.md硬约束3）
2. **文件系统+ArangoDB双写**：文件系统保留原始数据，ArangoDB提供查询能力
3. **不可复现数据优先存**：AI回复、引导者决策、压缩事件
4. **从第一轮就完整记录**：不等到系统成熟
5. **引导者决策和AI回复同等重要**：记录"为什么"不只是"是什么"
6. **工具使用记录**：AI用了exec运行Python吗？运行了什么？结果是什么？
7. **压缩事件**：session在哪一轮压缩了，必须记录
