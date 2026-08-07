---
name: guided-backtrack
description: >
  引导式数学解题元组群·Skill 4：回溯。
  DFS路径失败时，启动新session+重放Q序列+在岔口换方向。
  WHEN to use: 元组群guided-math-solving中，Skill 3遇到死路需要回溯时。
  WHEN NOT to use: 路径仍在推进中、首次探索（无需回溯）。
---

# guided-backtrack skill

## 用途

元组群 `guided-math-solving` 的 Skill 4。当Skill 3（交互引导）的当前DFS路径走不通时，执行回溯操作：启动新session，重放Q序列到岔口，在岔口换方向。

## 回溯铁律（来自规则，always-on）

**禁止在同一个Session中让AI回溯到思路岔口。** 必须启动新Session。原因：
1. 压缩边界风险——session可能已压缩
2. context污染——失败路径的推理痕迹影响AI换方向
3. context不可逆——AI不能"忘记"已走过的路

## 前置条件

- `runs/<run_id>/dfs_tree.json` 存在且记录了当前DFS路径
- 当前路径的最新节点状态为 stuck 或 dead_end
- 当前节点的候选Q列表中还有未尝试的候选

## 工作流

### 步骤1：确定回溯目标

从dfs_tree.json读取当前路径。确定要回溯到哪个岔口：

- **优先回溯到最近的岔口**——当前节点的父节点（如果父节点还有未试候选）
- **如果父节点候选已耗尽**——继续向上回溯到祖父节点
- **如果所有路径都耗尽**——回溯到根节点换第一个Q的方向

```python
tree = DFSTree("runs/<run_id>/dfs_tree.json")
# 找到有未试候选的最近祖先
fork_node_id = find_fork_with_untried_candidates(tree)
```

### 步骤2：记录回溯决策

在dfs_tree.json中记录：
- 从哪个节点回溯（当前死路节点）
- 回溯到哪个节点（岔口节点）
- 回溯原因（AI卡住/走错方向/候选耗尽）
- 考虑过的替代方案

### 步骤3：启动新session

**新session = 干净context，无压缩风险，无context污染。**

```bash
# 杀掉旧session
tmux kill-session -t ${SESSION_NAME}

# 启动新session
EXPORT_PATH="${EXPORT_DIR}/session_$(date +%s).json"
tmux new-session -d -s ${SESSION_NAME} \
  "cd ${WORK_DIR} && devin --model glm-5-2 --export ${EXPORT_PATH}"

# 处理trust prompt
sleep 5
tmux capture-pane -t ${SESSION_NAME} -p
# 如果有trust prompt，发送"1"
tmux send-keys -t ${SESSION_NAME} "1" Enter
sleep 8

# 启动pipe-pane
tmux pipe-pane -t ${SESSION_NAME} "cat >> ${RUN_DIR}/tmux_pipe.log"
```

### 步骤4：重放Q序列到岔口

从dfs_tree.json获取从根到岔口的Q序列（不包括岔口本身的Q——因为要换方向）：

```python
q_sequence = tree.get_replay_q_sequence(fork_node_id)
for q in q_sequence:
    tmux_send(q, wait=45)
    a = tmux_capture()
    # 记录A变体（如果和原来的A不同）
```

**重放后的A'可能和原来的A有细微差异**——这是正常的（AI非确定性）。按规则中的节点同一性策略处理：不判断同一性，判断适用性——"下一个Q对A'还有效吗？"

### 步骤5：在岔口换方向

在岔口节点，不发原来的Q（已试过的），发候选列表中的下一个Q（Level次高的）：

```python
# 获取岔口节点的候选列表
fork_node = tree.nodes[fork_node_id]
next_candidate_idx = len(fork_node.tried_candidate_indices)
next_q = fork_node.candidates[next_candidate_idx]

# 发送新Q
tmux_send(next_q, wait=45)
a = tmux_capture()

# 在dfs_tree中添加新子节点（岔口的新分支）
new_child_id = tree.add_child(fork_node_id, next_q, ...)
tree.update_a(new_child_id, a, judge_a_status(a))
```

引导者可以说：
> "你刚才的方向我理解了。但在继续之前，你能不能先换一个角度思考——[新的Q]"

### 步骤6：回到Skill 3

回溯完成，新session已在岔口走上新分支。回到Skill 3 `guided-interaction` 继续引导。

## 注意事项

1. **必须杀旧session启动新session**——不能在原session中回溯（铁律）
2. **重放Q序列从dfs_tree.json读取**——不依赖Session上下文
3. **重放后A'可能不同**——按适用性判断，不按同一性判断
4. **新session使用新的export文件**——不与旧分支混淆
5. **回溯决策必须记录**——为什么回溯、回溯到哪、考虑过什么替代
6. **pipe-pane必须重新启动**——新session需要新的兜底记录
