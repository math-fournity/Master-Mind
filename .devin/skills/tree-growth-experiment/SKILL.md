# Tree Growth Experiment · 两棵树生长实验SOP

## 定位

本Skill记录在实验中维护两棵树的标准操作流程（SOP）。

**触发**：被 `tree-growth-awareness` 规则触发，或当AI需要跑任何涉及推理AI的实验时手动加载。

**核心原则**：每次实验都必须在ArangoDB中留下两棵树的数据。没有树数据的实验不算完成。

---

## SOP · 串行多AI树生长实验（阶段2）

### 前置检查

```bash
# 1. 确认数据库隔离
source .env && echo $ARANGO_DB  # 必须输出 grove_math

# 2. 确认mitmproxy运行
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm status

# 3. 确认parser工作目录存在
ls /data/grove-parser-1/AGENTS.md

# 4. 确认ArangoDB连接
.venv/bin/python3 -c "
from arango import ArangoClient
c = ArangoClient(hosts='http://localhost:8529')
db = c.db('grove_math', username='root', password='REDACTED-DB-PASSWORD')
print('OK:', [x['name'] for x in db.collections() if not x['name'].startswith('_')])
"
```

### 运行实验

```bash
# 在tmux中运行（长时间任务必须用tmux）
tmux new-session -d -s grove-serial \
  "source .env && cd /data/master-mind-glm5.2-grove && \
   PYTHONUNBUFFERED=1 .venv/bin/python3 scripts/serial_multi_ai.py \
   --problem-id case_253 --max-ai 3 --max-time-per-ai 600 --model glm-5-2"

# 检查进度
tmux capture-pane -t grove-serial -p -S -30
```

### 实验后验证（必须做）

实验结束后，必须验证数据库中有树数据：

```python
# 验证脚本
from xishujuzhen.research_runtime.tree_engine.tree_store import TreeStore

store = TreeStore()

# 1. 检查problems
problems = list(store.db.aql.execute("FOR p IN problems RETURN p"))
print(f"Problems: {len(problems)}")
for p in problems:
    print(f"  {p['_key']}: nodes={p['total_nodes']}, edges={p['total_edges']}, ais={p['ai_instances_used']}, status={p['status']}")

# 2. 检查tree_nodes
nodes = list(store.db.aql.execute("FOR n IN tree_nodes RETURN n"))
print(f"Tree nodes: {len(nodes)}")
for n in nodes[:5]:
    print(f"  {n['_key']}: type={n['node_type']}, depth={n['depth']}, status={n['status']}, text={n.get('situation_text','')[:60]}")

# 3. 检查tree_edges
edges = list(store.db.aql.execute("FOR e IN tree_edges RETURN e"))
print(f"Tree edges: {len(edges)}")
for e in edges[:5]:
    print(f"  {e['_key']}: {e['_from']} -> {e['_to']}, Q={e.get('hint_q','')[:60]}")

# 4. 检查ai_instances
ais = list(store.db.aql.execute("FOR a IN ai_instances RETURN a"))
print(f"AI instances: {len(ais)}")
for a in ais:
    print(f"  {a['_key']}: status={a['status']}, reason={a.get('end_reason','')}, nodes={len(a.get('nodes_contributed',[]))}")
```

**验证标准**：
- `problems` 中有对应题目，`total_nodes > 0`
- `tree_nodes` 中有节点，至少包含root节点
- `ai_instances` 中有AI实例，数量=实验中启动的AI数
- 如果有多个AI，`tree_edges` 中应有边（提示Q驱动的分叉）

### 树数据可视化（可选）

```python
# 打印树结构
from xishujuzhen.research_runtime.tree_engine.tree_store import TreeStore

store = TreeStore()
nodes = store.get_nodes_by_problem("case_253")
edges = store.get_edges_by_problem("case_253")

# 按深度排列
for depth in range(max(n.depth for n in nodes) + 1):
    level_nodes = [n for n in nodes if n.depth == depth]
    print(f"Depth {depth}: {len(level_nodes)} nodes")
    for n in level_nodes:
        text = n.situation_text[:80] if n.situation_text else "(empty)"
        print(f"  [{n._key[:8]}] {n.node_type} | {text}")
        # 显示从此节点出发的边
        children = store.get_child_edges(n._key)
        for e in children:
            print(f"    --Q--> {e._to.split('/')[-1][:8]} | {e.hint_q[:60]}")
```

---

## SOP · 从任何实验中提取树数据

如果实验不是用 `serial_multi_ai.py` 跑的（如A/B实验、裸跑测试），但用户要求树数据：

### 手动提取流程

```python
from xishujuzhen.research_runtime.tree_engine.tree_store import (
    TreeStore, TreeNode, TreeEdge, AIInstance
)
from xishujuzhen.research_runtime.tree_engine.node_extractor import NodeExtractor

store = TreeStore()

# 1. 创建problem（如果不存在）
problem_id = "case_253_ab_exp"
if not store.get_problem(problem_id):
    root_key = store.create_problem(problem_id, PROBLEM_TEXT)

# 2. 注册AI实例
ai = AIInstance(
    problem_id=problem_id,
    entry_node_key=root_key,
    tmux_session="harness-ab-253-A1",
    trajectory_dir="/data/grove-agents-trajectory/ab-253-A1",
)
ai_key = store.register_ai(ai)

# 3. 读取thinking
thinking = open("/data/grove-agents-trajectory/ab-253-A1/mitm/thinking_readable.txt").read()

# 4. 提取节点
extractor = NodeExtractor(tree_store=store)
node_keys = extractor.extract_nodes_from_trajectory(
    ai_instance_id=ai_key,
    problem_id=problem_id,
    trajectory=thinking,
    entry_node_key=root_key,
    problem_text=PROBLEM_TEXT,
)

# 5. 更新AI状态
store.update_ai_status(ai_key, "completed", end_reason="manual_extract", nodes_contributed=node_keys)

print(f"提取了 {len(node_keys)} 个节点到树中")
```

---

## 模块索引

| 模块 | 路径 | 职责 |
|---|---|---|
| TreeStore | `xishujuzhen/research_runtime/tree_engine/tree_store.py` | ArangoDB树存储CRUD |
| NodeExtractor | `xishujuzhen/research_runtime/tree_engine/node_extractor.py` | 从trajectory提取树节点 |
| PathConstructor | `xishujuzhen/research_runtime/tree_engine/path_constructor.py` | 脉络构造 |
| TerminationDetector | `xishujuzhen/research_runtime/tree_engine/termination_detector.py` | AI终止检测 |
| 编排脚本 | `scripts/serial_multi_ai.py` | 串行多AI实验编排 |

---

## 维护规则

1. **每次实验后更新本Skill**——如果发现了新的树数据验证需求、新的提取流程、新的可视化方式，追加到本Skill
2. **阶段演进时更新SOP**——阶段3（并发多AI）实现后，新增并发实验的SOP
3. **问题修复时更新SOP**——如果实验中发现树数据写入失败、节点提取降级等问题，记录解决方案
4. **本Skill是活文档**——它记录的是"当前最正确的树生长实验流程"，不是历史档案

---

## 常见问题

### Q: thinking_readable.txt为空怎么办？

检查MITM是否在捕获：
```bash
ls -lt /data/grove-agents-trajectory/_shared/mitm_raw/chatmsg_*.bin | head -3
```
如果raw文件时间戳不更新，MITM可能没在捕获新流量。重启MITM：
```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm stop
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm start
```

### Q: parser解析失败（parse_confidence < 0.5）怎么办？

NodeExtractor有降级处理：situation为空，situation_text用thinking原文前2000字符。节点仍然创建，只是六元组缺失。这是可接受的——树仍在生长，只是节点信息不够丰富。

### Q: 实验跑完但数据库里没有树数据怎么办？

说明实验脚本没有调用tree_store。这是违规的——按规则，每次实验都必须在数据库中留下树数据。需要修复实验脚本。

### Q: thinking_readable.txt为空但MITM在运行？

检查launchd plist的环境变量是否指向正确的目录：
```bash
ps eww $(lsof -i :18889 -t | head -1) | tr ' ' '\n' | grep MITM
```
如果`MITM_RAW_DIR`或`MITM_TRAJECTORY_BASE`指向旧路径（如`/data/math-agent-glm5.2-tmux-agents-trajectory/`），需要更新`~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist`并重载：
```bash
launchctl unload ~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist
launchctl load ~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist
```

### Q: parser太慢导致节点提取超时？

thinking_readable.txt很大时（>50KB），按段落分割会产生太多轮次，每轮次调parser 25-200秒。解决方案：
- `_split_trajectory_into_rounds`已改为合并成2000-4000字符的块，减少parser调用次数
- 如果仍然太慢，可以跳过parser直接用降级模式（situation_text=thinking原文），先保证树数据写入

### Q: 节点depth全是0？

这是因为`parent_node_key`没有设置。同一AI内的轮次之间没有edge但有父子关系，需要通过`parent_node_key`字段让`tree_store.add_node`正确设置`path_from_root`和`depth`。已在代码中修复。

### Q: situation_text显示"SemanticEvent(event_id=...)"？

这是因为SemanticEvent没有`description`字段，它有`payload`字典。`_extract_situation_text`需要从`event.payload.get("description")`提取，而不是`event.description`。已在代码中修复。
