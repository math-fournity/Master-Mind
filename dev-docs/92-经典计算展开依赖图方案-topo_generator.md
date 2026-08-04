# 92-经典计算展开依赖图方案·topo_generator

> **文档定位**：实现90号文档愿景的详细方案——经典计算负责依赖图 G 的展开（生成 G'_topo），保证全覆盖，AI 只做语义细化。
>
> **依据**：90号愿景分析（分层可行性）+ 88号 POC-2 结果（步骤2 meta AI 生成的 G'_topo 作为基准）

## 一、方案目标

### 1.1 核心目标

编写 `topo_generator.py`，从 ArangoDB 中的依赖图 G 自动生成 G'_topo 骨架，保证 TopologyVerifier 1次通过 100%覆盖。

### 1.2 分层实现

| 层 | 内容 | 执行者 | 本方案实现 |
|---|---|---|---|
| L0 | 骨架展开（节点/边拷贝 + 拓扑排序 + traversal_order） | 经典计算 | ✅ |
| L1 | 类型推断（static/dynamic + connection 类型） | 经典计算 | ✅ |
| L2 | section 划分推荐 | 经典计算 | ✅（推荐，AI可调整） |
| L3 | 语义标注（section 命名 + spiral 类型最终确认） | AI | ❌（保留给AI） |

### 1.3 与七步骤工作流的集成

| 当前（POC-2） | 升级后 |
|---|---|
| 步骤2：meta AI 生成 G'_topo | 步骤2：**经典计算生成 G'_topo 骨架（L0+L1+L2）** + AI 语义细化（L3） |
| 步骤3：TopologyVerifier 验证（可能需要回退） | 步骤3：TopologyVerifier 验证（**1次通过，不需要回退**） |

## 二、算法设计

### 2.1 L0：骨架展开

#### 输入

- ArangoDB 中的 `dg_nodes`（节点集）
- ArangoDB 中的 `dg_edges`（边集，含 edge_type: depends_on / calls）
- ArangoDB 中的 `loops`（螺旋环路，graph=dependency_graph）

#### 输出

- G'_topo JSON（写入文件 + 导入 ArangoDB 的 ut_nodes / ut_edges）

#### 算法

```python
def generate_skeleton(db):
    """L0: 骨架展开——从 G 直接推导 G'_topo，保证拓扑同构"""
    
    # 1. 读取 G 的节点
    dg_nodes = list(db.collection("dg_nodes").all())
    node_ids = [n["node_id"] for n in dg_nodes]
    
    # 2. 读取 G 的边
    dg_edges = list(db.collection("dg_edges").all())
    
    # 3. 读取 G 的螺旋环路
    loops = list(db.collection("loops").find({"graph": "dependency_graph"}))
    
    # 4. 拓扑排序（Kahn 算法，只对 depends_on 边）
    topo_order = topological_sort(node_ids, dg_edges, edge_type="depends_on")
    
    # 5. 构建 G'_topo 节点
    ut_nodes = []
    for i, node_id in enumerate(topo_order):
        node = get_node(dg_nodes, node_id)
        ut_nodes.append({
            "node_id": node_id,
            "type": infer_type(node),  # L1
            "section": "",  # L2 填充
            "position": 0,  # L2 填充
            "traversal_order": i + 1,
        })
    
    # 6. 构建 G'_topo 边（直接拷贝，加 connection 类型）
    ut_edges = []
    for edge in dg_edges:
        ut_edges.append({
            "from_node_id": edge["from_node_id"],
            "to_node_id": edge["to_node_id"],
            "edge_type": edge["edge_type"],
            "section": "",  # L2 填充
            "connection": infer_connection(edge, topo_order),  # L1
        })
    
    # 7. 构建 G'_topo 螺旋环路（直接拷贝，圈数保持）
    ut_loops = []
    for loop in loops:
        ut_loops.append({
            "loop_id": loop["loop_id"],
            "nodes": loop["nodes"],
            "circles": loop["circles"],  # 保持不变
            "section": "",  # L2 填充
            "traversal": infer_traversal(loop, dg_nodes),  # L1
        })
    
    return {"nodes": ut_nodes, "edges": ut_edges, "loops": ut_loops}
```

#### 拓扑排序（Kahn 算法）

```python
def topological_sort(node_ids, edges, edge_type="depends_on"):
    """Kahn 算法拓扑排序
    
    只对 edge_type == "depends_on" 的边构建 DAG。
    calls 边不参与拓扑排序（它们是"调用"关系，不是"依赖"关系）。
    
    如果 depends_on 有环，报错（数学证明的依赖链不应该有环）。
    """
    # 构建邻接表和入度表
    adj = {nid: [] for nid in node_ids}
    in_degree = {nid: 0 for nid in node_ids}
    
    for edge in edges:
        if edge["edge_type"] == edge_type:
            adj[edge["from_node_id"]].append(edge["to_node_id"])
            in_degree[edge["to_node_id"]] += 1
    
    # Kahn 算法
    queue = [nid for nid in node_ids if in_degree[nid] == 0]
    order = []
    
    while queue:
        # 取入度为0的节点（如果有多个，按字母序保证确定性）
        queue.sort()
        node = queue.pop(0)
        order.append(node)
        
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(order) != len(node_ids):
        # 有环——检查是否是 calls 边导致的（calls 边不参与排序）
        # 如果是 depends_on 有环，报错
        remaining = set(node_ids) - set(order)
        raise ValueError(f"depends_on 边有环，无法拓扑排序。未排序节点: {remaining}")
    
    return order
```

**关键设计决策**：
- **只对 depends_on 边做拓扑排序**——calls 边是"调用"关系（如"步骤A calls 意识B"），不是"依赖"关系。意识节点不被 depends_on，所以自然排在后面。
- **多入度0节点按字母序**——保证确定性（多次运行结果相同）。
- **depends_on 有环报错**——数学证明的依赖链不应该有环。如果有环，说明依赖图设计有误。

### 2.2 L1：类型推断

```python
def infer_type(node):
    """推断节点类型：step/substep → static，意识 → dynamic"""
    if node["type"] in ["step", "substep"]:
        return "static"
    elif node["type"] == "意识":
        return "dynamic"
    else:
        return "static"  # 默认

def infer_connection(edge, topo_order):
    """推断边的 connection 类型"""
    from_order = topo_order.index(edge["from_node_id"])
    to_order = topo_order.index(edge["to_node_id"])
    
    # 回边（to 在 from 之前）→ shortcut（环路回边）
    if to_order < from_order:
        return "shortcut"
    
    # 相邻（to 紧跟 from）→ linear
    if to_order == from_order + 1:
        return "linear"
    
    # 其他 → cross_section
    return "cross_section"

def infer_traversal(loop, dg_nodes):
    """推断螺旋环路的遍历类型"""
    node_types = []
    for nid in loop["nodes"]:
        node = get_node(dg_nodes, nid)
        node_types.append(node["type"])
    
    # 全是意识节点 → spiral_dynamic
    if all(t == "意识" for t in node_types):
        return "spiral_dynamic"
    # 包含 static 节点 → spiral_static
    return "spiral_static"
```

### 2.3 L2：section 划分推荐

```python
def recommend_sections(topo_order, dg_nodes, dg_edges):
    """推荐 section 划分
    
    策略：
    1. 意识节点（dynamic）全部归为最后一章
    2. 证明步骤（static）按依赖链分段
    3. 段边界：depends_on 链的"自然断点"（如从"极差sqrt5下界"到"紧性归约"是逻辑转折）
    """
    sections = {}
    current_section = 1
    current_section_nodes = []
    
    for node_id in topo_order:
        node = get_node(dg_nodes, node_id)
        
        if node["type"] == "意识":
            # 意识节点归为最后一章
            sections[node_id] = f"第{current_section + 1}章"
            continue
        
        # 证明步骤
        current_section_nodes.append(node_id)
        sections[node_id] = f"第{current_section}章"
        
        # 检查是否应该分段：如果下一个节点不被当前节点 depends_on，可能需要新段
        # （简化版：每5个节点分一段）
        if len(current_section_nodes) >= 5:
            current_section += 1
            current_section_nodes = []
    
    return sections

def assign_positions(topo_order, sections):
    """根据 section 划分分配 position（section 内位置）"""
    section_counters = {}
    positions = {}
    
    for node_id in topo_order:
        section = sections[node_id]
        if section not in section_counters:
            section_counters[section] = 0
        section_counters[section] += 1
        positions[node_id] = section_counters[section]
    
    return positions

def assign_edge_sections(ut_edges, sections):
    """分配边的 section（取 from 节点的 section）"""
    for edge in ut_edges:
        edge["section"] = sections.get(edge["from_node_id"], "")
    return ut_edges
```

### 2.4 完整流程

```python
def generate_g_prime_topo(db_name="xishujuzhen_math"):
    """完整流程：从 ArangoDB 中的 G 生成 G'_topo"""
    
    # 连接 ArangoDB
    client = ArangoClient(hosts="http://localhost:8529")
    db = client.db(db_name, username="root", password="REDACTED-DB-PASSWORD")
    
    # L0: 骨架展开
    skeleton = generate_skeleton(db)
    
    # L1: 类型推断（已在 generate_skeleton 中完成）
    
    # L2: section 划分推荐
    sections = recommend_sections(
        [n["node_id"] for n in skeleton["nodes"]],
        list(db.collection("dg_nodes").all()),
        list(db.collection("dg_edges").all())
    )
    positions = assign_positions(
        [n["node_id"] for n in skeleton["nodes"]],
        sections
    )
    
    # 填充 section 和 position
    for node in skeleton["nodes"]:
        node["section"] = sections[node["node_id"]]
        node["position"] = positions[node["node_id"]]
    
    # 填充边的 section
    skeleton["edges"] = assign_edge_sections(skeleton["edges"], sections)
    
    # 填充环路的 section
    for loop in skeleton["loops"]:
        loop["section"] = sections.get(loop["nodes"][0], "")
    
    return skeleton
```

## 三、验证方案

### 3.1 用 POC-2 的依赖图测试

POC-2 的依赖图（18节点25边2环路）已经有 meta AI 生成的 G'_topo 作为基准。用 `topo_generator.py` 生成经典计算版本，对比：

| 对比维度 | 验证方法 |
|---|---|
| 节点覆盖 | TopologyVerifier 验证：经典计算版本是否 18/18 覆盖 |
| 边覆盖 | TopologyVerifier 验证：经典计算版本是否 25/25 覆盖 |
| 螺旋环路圈数 | 验证：loop_0=2圈，loop_1=1圈 |
| traversal_order | 对比：经典计算的拓扑序与 meta AI 的 traversal_order 的差异 |
| section 划分 | 对比：经典计算的 section 与 meta AI 的 section 的差异 |
| connection 类型 | 对比：经典计算的 connection 与 meta AI 的 connection 的差异 |

### 3.2 预期结果

| 维度 | 经典计算 | meta AI | 说明 |
|---|---|---|---|
| 节点覆盖 | 18/18 ✅ | 18/18 ✅ | 都保证覆盖 |
| 边覆盖 | 25/25 ✅ | 25/25 ✅ | 都保证覆盖 |
| 螺旋环路 | 2+1 ✅ | 2+1 ✅ | 都保持圈数 |
| traversal_order | 拓扑排序确定 | AI 判断 | **可能不同**——拓扑排序是确定性的，AI 可能按语义调整顺序 |
| section 划分 | 启发式（每5个一段+意识单独成章） | AI 按逻辑结构划分 | **可能不同**——AI 的划分更符合数学逻辑 |
| connection 类型 | 启发式（相邻=linear，回边=shortcut，其他=cross_section） | AI 判断 | **基本一致**——启发式规则覆盖了大部分情况 |

### 3.3 关键验证：TopologyVerifier 1次通过

**经典计算版本的 G'_topo 必然通过 TopologyVerifier 验证**，因为：
- 节点集和边集是从 G 直接拷贝的（拓扑同构）
- 螺旋环路圈数保持不变
- TopologyVerifier 只验证节点覆盖、边覆盖、螺旋环路圈数——这些都被 L0 保证

## 四、与七步骤工作流的集成

### 4.1 升级后的步骤2

```python
# 步骤2（升级后）：经典计算生成 G'_topo 骨架 + AI 语义细化

# 2a. 经典计算生成骨架
g_prime_topo_skeleton = generate_g_prime_topo(db_name="xishujuzhen_math")

# 2b. 写入 ArangoDB
import_topo_to_arangodb(g_prime_topo_skeleton, db_name="xishujuzhen_math")

# 2c. TopologyVerifier 验证（必然1次通过）
report = topology_verifier.verify_all()
assert report.node_coverage == 1.0
assert report.edge_coverage == 1.0

# 2d. [可选] AI 语义细化（L3）
# AI 读取骨架，调整 section 命名、确认 spiral 类型
# 这一步是可选的——骨架已经可以用于步骤4 转译
```

### 4.2 步骤2 的两种模式

| 模式 | 内容 | 适用场景 |
|---|---|---|
| **纯经典计算** | L0+L1+L2，不需要 AI | 快速验证、小规模依赖图、POC 预测试 |
| **经典计算 + AI 细化** | L0+L1+L2 经典计算，L3 AI 语义标注 | 正式 POC、大规模依赖图、需要语义质量 |

## 五、文件设计

### 5.1 topo_generator.py

```python
#!/usr/bin/env python3
"""topo_generator.py: 经典计算生成 G'_topo 骨架

从 ArangoDB 中的依赖图 G 自动生成展开图拓扑骨架 G'_topo。
保证 TopologyVerifier 1次通过 100%覆盖。

使用方法:
    # 生成 G'_topo 并写入文件
    .venv/bin/python3 xishujuzhen/topo_generator.py generate --output poc/poc2/poc2_g_prime_topo_auto.json
    
    # 生成并直接导入 ArangoDB
    .venv/bin/python3 xishujuzhen/topo_generator.py generate --import-db
    
    # 生成并验证
    .venv/bin/python3 xishujuzhen/topo_generator.py generate --import-db --verify
    
    # 对比经典计算版本与 AI 版本
    .venv/bin/python3 xishujuzhen/topo_generator.py compare --auto poc/poc2/poc2_g_prime_topo_auto.json --ai poc/poc2/poc2_g_prime_topo.json
"""
```

### 5.2 函数清单

| 函数 | 层 | 功能 |
|---|---|---|
| `generate_skeleton(db)` | L0 | 骨架展开：节点/边拷贝 + 拓扑排序 |
| `topological_sort(node_ids, edges, edge_type)` | L0 | Kahn 算法拓扑排序 |
| `infer_type(node)` | L1 | 推断 static/dynamic |
| `infer_connection(edge, topo_order)` | L1 | 推断 linear/shortcut/cross_section |
| `infer_traversal(loop, dg_nodes)` | L1 | 推断 spiral_static/spiral_dynamic |
| `recommend_sections(topo_order, dg_nodes, dg_edges)` | L2 | 推荐 section 划分 |
| `assign_positions(topo_order, sections)` | L2 | 分配 section 内 position |
| `assign_edge_sections(ut_edges, sections)` | L2 | 分配边的 section |
| `generate_g_prime_topo(db_name)` | 全流程 | 完整生成 G'_topo |
| `compare_with_ai_version(auto, ai)` | 验证 | 对比经典计算版本与 AI 版本 |
| `verify_coverage(db_name)` | 验证 | 调用 TopologyVerifier 验证覆盖 |

## 六、Check List

### 阶段1：L0 骨架展开
- [ ] 编写 `topo_generator.py` 的 `topological_sort` 函数
- [ ] 编写 `generate_skeleton` 函数
- [ ] 用 POC-2 依赖图测试：生成骨架
- [ ] 验证：节点数=18，边数=25，环路数=2

### 阶段2：L1 类型推断
- [ ] 编写 `infer_type`、`infer_connection`、`infer_traversal`
- [ ] 用 POC-2 依赖图测试：类型推断结果
- [ ] 对比：与 meta AI 的 G'_topo 的类型差异

### 阶段3：L2 section 划分
- [ ] 编写 `recommend_sections`、`assign_positions`、`assign_edge_sections`
- [ ] 用 POC-2 依赖图测试：section 划分结果
- [ ] 对比：与 meta AI 的 section 划分差异

### 阶段4：验证
- [ ] 编写 `verify_coverage` 函数（调用 TopologyVerifier）
- [ ] 生成经典计算版 G'_topo → 导入 ArangoDB → TopologyVerifier 验证
- [ ] 验证结果：1次通过，18/18节点，25/25边，2/2环路

### 阶段5：对比
- [ ] 编写 `compare_with_ai_version` 函数
- [ ] 对比经典计算版与 meta AI 版的差异
- [ ] 记录差异点，分析哪些差异是 L3（AI 语义标注）可以弥补的

### 阶段6：集成
- [ ] 在七步骤工作流中用 `topo_generator.py` 替代步骤2 的 meta AI
- [ ] 端到端测试：步骤1导入 → 步骤2经典计算生成 → 步骤3验证 → 步骤4转译
- [ ] 验证：整个流程不需要 meta AI 参与（L3 可选）

## 七、诚实面对的不确定性

1. **section 划分的质量**：L2 的启发式规则（每5个一段+意识单独成章）是粗糙的近似。meta AI 的 section 划分更符合数学证明的逻辑结构。但 L2 的目的是提供合理默认值，不是最优划分。

2. **traversal_order 的差异**：拓扑排序的顺序可能与 AI 的语义顺序不同。例如，AI 可能把"紧性归约"放在第二章开头（逻辑转折），而拓扑排序可能把它放在第一章末尾（依赖链连续）。这个差异由 L3 的 AI 细化来弥补。

3. **connection 类型的边界情况**：L1 的启发式规则在 POC-2 的简单图上有效（18节点25边），但在更复杂的图上（如三层提取 POC 的大图）可能不准确。需要更多测试。

4. **L3 可能不可省略**：如果 section 命名和 spiral 类型的语义标注对转译质量很重要，L3 不能省略。但 L0+L1+L2 已经保证了全覆盖和合理结构，L3 只是锦上添花。

## 八、与方案1的关系

| 方案1（cognition 基座） | 方案2（topo_generator） | 集成点 |
|---|---|---|
| `seven_step_workflow` 认知单元 | `topo_generator.py` | 方案2升级了 seven_step_workflow 的步骤2 |
| `cognition_sdk_math.py` | `topo_generator.py` | SDK 可以调用 topo_generator |
| CP4 检查清单 | G'_topo 全覆盖 | L0 保证全覆盖是 CP4 的一个检查项 |
| `topology_verifier` 认知单元 | `verify_coverage` | 方案2调用 TopologyVerifier |

两个方案可以并行实现。方案2的 `topo_generator.py` 可以独立于方案1的 cognition 系统运行。最终集成时，`topo_generator.py` 成为 `cognition_sdk_math.py` 的一个方法。

## 九、其他AI如何复用

### 9.1 最小实现

如果只需要经典计算展开的骨架（L0）：

1. 实现`topological_sort`函数（Kahn算法，只对depends_on边）
2. 实现`generate_skeleton`函数（节点/边拷贝 + 拓扑排序）
3. 验证：TopologyVerifier 1次通过100%覆盖

不需要：L1类型推断、L2 section划分、L3语义标注

### 9.2 完整实现

需要L0+L1+L2（经典计算生成完整骨架+推荐）：

1. 上述最小实现
2. 实现`infer_type`、`infer_connection`、`infer_traversal`（L1类型推断）
3. 实现`recommend_sections`、`assign_positions`、`assign_edge_sections`（L2 section划分）
4. 验证：用POC-2依赖图测试，对比经典计算版与meta AI版的差异

### 9.3 增强实现

需要L0+L1+L2+验证+对比：

1. 上述完整实现
2. 实现`verify_coverage`函数（调用TopologyVerifier）
3. 实现`compare_with_ai_version`函数（对比经典计算版与AI版）
4. 集成到七步骤工作流（步骤2从meta AI变为经典计算+AI细化）

### 9.4 关键实现细节

1. **拓扑排序只对depends_on边**：calls边不参与排序（calls是"调用"关系，不是"依赖"关系）。意识节点不被depends_on，自然排在后面。
2. **多入度0节点按字母序**：保证确定性（多次运行结果相同）。
3. **depends_on有环报错**：数学证明的依赖链不应该有环。如果有环，说明依赖图设计有误。
4. **螺旋环路圈数直接拷贝**：不从图论算法推导，直接从G的loops集合拷贝，保证不变。
5. **L2是推荐不是强制**：AI可以在L3阶段调整section边界。经典计算的section划分是默认值，不是最优值。
6. **L3保留给AI**：section命名和spiral类型最终确认需要语义理解，经典计算做不到。
