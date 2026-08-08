# 并发DFS

**前置阅读**：05-引导树闭环/01-三个推动关系.md、01-基础概念/04-两棵树.md
**关联文件**：03-hint端/04-方向注入.md、05-引导树闭环/03-回溯铁律与新Session.md
**来源**：256号§6.5命题5、275号POC-VMS-2验证、290号继承29

---

## 1. 并发DFS的定义

并发DFS是第五代的核心展开策略：**识别N个tell→匹配N个hint→启动N个推理AI→每个走一个方向→并发探索。**

这是用户在256号§5.2命题5中提出的核心洞察：

> "甚至可以就在此时，比如识别出了2个模式，那么就把推理智能体当前的完整上下文，分别给两个新的推理智能体，同时把两个后续工作方向分别给这两个推理智能体安排上，这样DFS，都可以并发了。"

## 2. 串行DFS vs并发DFS

| 维度 | 串行DFS（第二代燧人） | 并发DFS（第五代） |
|---|---|---|
| 探索方式 | 一次一个方向，走不通回溯 | 同时多个方向，并发探索 |
| 回溯 | 需要新Session重放Q序列（回溯铁律） | 不需要回溯——每个方向独立推进 |
| 资源消耗 | 1个推理AI | N个推理AI（N=识别出的tell数） |
| 时间效率 | 串行，慢 | 并发，快 |
| Context污染 | 回溯时有风险（回溯铁律的 raison d'être） | 无回溯，无污染 |
| 决策点 | 走不通后回溯到岔口选下一个方向 | 多个方向同时走，哪个先成功用哪个 |

## 3. 并发DFS解决了回溯铁律的痛点

第二代（燧人）的回溯铁律——"禁止在同一个Session中让AI回溯到思路岔口，必须启动新Session重放Q序列"——是因为串行DFS中，回溯会导致context污染和压缩边界风险。

**并发DFS根本不需要回溯**——每个方向从一开始就是独立的Session，独立的推理AI，独立的context。不存在"回溯到岔口"的操作，因为岔口的每个分支都已经有一个独立的探索者在走了。

## 4. 并发DFS的工程要求

1. **多推理智能体并发**——需要同时启动多个devin cli实例，每个在不同的工作目录中运行
2. **上下文复制**——每个并发分支需要继承"当前完整上下文"——把Q序列和A序列重放到岔口的状态，作为新分支的起点
3. **方向注入**——每个并发分支需要注入"后续工作方向"——即识别出的tell对应的hint
4. **结果收集**——需要收集所有并发分支的结果，判断哪个（或哪些）成功了

## 5. 与tmux-agents-dir模式的契合

本项目的Solver工作目录采用tmux-agents-dir模式——每个实验在独立的工作目录中运行，运行后保留全部记录。并发DFS的每个分支就是一个实验目录：

```
/data/math-agent-glm5.2-tmux-agents-dir/
├── experiment-001/                    # 主实验（bare AI或第一个AI）
├── experiment-001-branch-A/           # 并发分支A（tell-1对应的方向）
├── experiment-001-branch-B/           # 并发分支B（tell-2对应的方向）
└── experiment-001-branch-C/           # 并发分支C（tell-3对应的方向）
```

每个分支独立运行，独立记录，独立保留。成功了的结果回收到主实验目录，失败了的结果也保留（用于分析为什么这个方向走不通）。

## 6. 并发管理

系统管理多个并发推理AI实例，分配额度，收集结果：

```python
MAX_CONCURRENT = 2  # 最多2个并发AI（可调整）

while problem.status != "solved" and problem.status != "exhausted":
    # 检查可用额度
    available_slots = MAX_CONCURRENT - count_running_ais()
    
    # 在可分配节点上启动新AI
    if available_slots > 0:
        assignable_nodes = get_assignable_nodes(problem_id)
        for node in assignable_nodes:
            if available_slots <= 0:
                break
            for direction in node.directions_identified:
                if available_slots <= 0:
                    break
                # 构造脉络
                path_text = construct_path_text(node.path_from_root)
                # 启动新AI
                ai = launch_ai(problem_id, node, direction, path_text)
                available_slots -= 1
    
    # 检查停机和AI终止
    for ai in get_running_ais(problem_id):
        if check_solution_found(ai):
            mark_problem_solved(problem_id, ai)
            break
        if check_ai_terminated(ai):
            mark_ai_terminated(ai)
            # 在AI的最后一个节点上做检索（推动关系3）
            last_node = get_last_node(ai)
            if not last_node.retrieval_done:
                directions = retrieve_directions(last_node)
                last_node.directions_identified = directions
                last_node.retrieval_done = true
```

## 7. POC-VMS-2的工程验证

POC-VMS-2验证了并发DFS的工程可行性：

| 指标 | 批量模式结果 | 手动模式结果 |
|---|---|---|
| AI总数 | 30（每题3个AI×10题） | 2（branch1+ext1） |
| solved率 | 10/10 | 1/1 |
| tree_nodes | 267 | 9 |
| tree_edges | 237 | 8 |
| 树深度 | d0-d11 | d0-d8 |
| 循环完整性 | 只转了半圈（0/47叶节点检索） | 完整转了一圈半（1/1叶节点检索+启动新AI） |

### 批量模式的循环半圈问题

批量模式（tree_engine.py主循环）循环只转了半圈——19个叶节点0个检索0个启动新AI。原因是3个token_limit的AI终止时，problem已经被其他并发AI solved了，走"already solved, 停机"分支，跳过了叶节点检索。

### 手动模式的完整循环

手动模式（辅助Pipe亲手执行循环）循环完整转了一圈半——AI-1走到d4 token_limit，叶节点检索启动AI-2，AI-2走到d8 solution_found，problem solved停机。

**关键发现**：辅助Pipe是AI本人不是脚本。批量模式中脚本没有判断力，遇到"problem already solved"就走停机分支。手动模式中AI本人有判断力，知道在叶节点检索方向Q、构造脉络、启动新AI。

详细的辅助智能体角色见05-引导树闭环/05-辅助智能体JD.md。
