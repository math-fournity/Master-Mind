# 原语提取：92-经典计算展开依赖图方案·topo_generator

## 文档概述

本文档描述了一个经典计算方案 `topo_generator.py`，从 ArangoDB 中的依赖图 G 自动生成展开图拓扑骨架 G'_topo，保证 TopologyVerifier 一次通过 100% 覆盖。方案采用 L0-L3 四层分层架构：经典计算负责骨架展开、类型推断和 section 划分推荐（L0-L2），AI 负责语义标注（L3）。文档与检索机制的关系在于：它定义了从依赖图中提取、排序、分类、分段的完整算法流程，这些算法和数据结构直接可作为检索机制的构造积木——拓扑排序提供检索顺序、类型推断提供检索过滤维度、section 划分提供检索结果的聚类组织、全覆盖保证提供检索完整性约束。

## 提取的原语

### 原语：L0-L3 四层分层架构
- **ID**：92-P1
- **类型**：概念框架
- **描述**：将图展开任务分为四层——L0 骨架展开（经典计算）、L1 类型推断（经典计算）、L2 section 划分推荐（经典计算）、L3 语义标注（AI），每层有明确的执行者和职责边界。
- **溯源**：92, 第15-21行, 原文引用："| L0 | 骨架展开（节点/边拷贝 + 拓扑排序 + traversal_order） | 经典计算 | ✅ | | L1 | 类型推断（static/dynamic + connection 类型） | 经典计算 | ✅ | | L2 | section 划分推荐 | 经典计算 | ✅（推荐，AI可调整） | | L3 | 语义标注（section 命名 + spiral 类型最终确认） | AI | ❌（保留给AI） |"
- **依赖关系**：
  - 依赖：无（顶层架构原语）
  - 支撑：92-P2（骨架展开）、92-P6（类型推断）、92-P9（section划分）
- **与检索机制的关系**：分层架构是检索 pipeline 的骨架——L0 保证结构完整性（检索不遗漏），L1 提供过滤维度（按类型检索），L2 提供聚类组织（按 section 检索），L3 提供语义质量（语义匹配）。检索机制可以复用这种"经典计算保证结构 + AI 保证语义"的分层模式。

### 原语：骨架展开——节点/边直接拷贝 + 拓扑排序
- **ID**：92-P2
- **类型**：操作原语
- **描述**：从源图 G 直接拷贝节点集和边集到目标图 G'_topo，同时对节点做拓扑排序生成 traversal_order，保证拓扑同构。
- **溯源**：92, 第46-97行, 原文引用："def generate_skeleton(db): """L0: 骨架展开——从 G 直接推导 G'_topo，保证拓扑同构""" ... # 4. 拓扑排序（Kahn 算法，只对 depends_on 边） topo_order = topological_sort(node_ids, dg_edges, edge_type="depends_on") ... # 6. 构建 G'_topo 边（直接拷贝，加 connection 类型）"
- **依赖关系**：
  - 依赖：92-P3（拓扑排序算法）
  - 支撑：92-P1（分层架构的 L0 层）
- **与检索机制的关系**：骨架展开是检索的"全量提取"操作——从认知图中提取所有 Pattern 节点和依赖边，同时赋予拓扑顺序。检索机制可以复用这种"拷贝 + 排序"的模式来构建检索索引。

### 原语：Kahn 算法拓扑排序（只对 depends_on 边）
- **ID**：92-P3
- **类型**：操作原语
- **描述**：使用 Kahn 算法对图中的节点做拓扑排序，但只对 edge_type == "depends_on" 的边构建 DAG，calls 边不参与排序。
- **溯源**：92, 第99-141行, 原文引用："def topological_sort(node_ids, edges, edge_type="depends_on"): """Kahn 算法拓扑排序 ... 只对 edge_type == "depends_on" 的边构建 DAG。 calls 边不参与拓扑排序（它们是"调用"关系，不是"依赖"关系）。"""
- **依赖关系**：
  - 依赖：无（基础算法）
  - 支撑：92-P2（骨架展开）、92-P4（边类型区分）、92-P7（connection类型推断）
- **与检索机制的关系**：拓扑排序为检索提供"依赖优先"的遍历顺序——检索 Pattern 时可以按依赖链顺序返回结果，确保被依赖的 Pattern 先于依赖它的 Pattern 出现。这是检索结果排序的核心算法。

### 原语：边类型区分——depends_on vs calls
- **ID**：92-P4
- **类型**：结构原语
- **描述**：图中存在两种边类型——depends_on（依赖关系，参与拓扑排序）和 calls（调用关系，不参与拓扑排序），它们在图遍历和排序中有不同的处理方式。
- **溯源**：92, 第143-146行, 原文引用："**只对 depends_on 边做拓扑排序**——calls 边是"调用"关系（如"步骤A calls 意识B"），不是"依赖"关系。意识节点不被 depends_on，所以自然排在后面。"
- **依赖关系**：
  - 依赖：无（基础设计决策）
  - 支撑：92-P3（拓扑排序算法）
- **与检索机制的关系**：边类型区分是检索的多关系过滤原语——检索 Pattern 时可以按关系类型过滤（只检索 depends_on 关联的 Pattern，或只检索 calls 关联的 Pattern），不同关系类型对应不同的检索语义。

### 原语：多入度0节点按字母序保证确定性
- **ID**：92-P5
- **类型**：性质标准
- **描述**：拓扑排序中当有多个入度为0的节点时，按字母序选择，保证多次运行结果相同（确定性输出）。
- **溯源**：92, 第145行, 原文引用："**多入度0节点按字母序**——保证确定性（多次运行结果相同）。"
- **依赖关系**：
  - 依赖：92-P3（拓扑排序算法）
  - 支撑：无
- **与检索机制的关系**：确定性是检索机制的可复现性保证——相同查询多次执行应返回相同结果。当检索结果有多个等价候选时，需要确定性的 tie-breaking 规则。

### 原语：节点类型推断（static/dynamic）
- **ID**：92-P6
- **类型**：操作原语
- **描述**：根据节点的原始类型推断其展开类型——step/substep → static，意识 → dynamic，默认 → static。
- **溯源**：92, 第150-158行, 原文引用："def infer_type(node): """推断节点类型：step/substep → static，意识 → dynamic""" if node["type"] in ["step", "substep"]: return "static" elif node["type"] == "意识": return "dynamic" else: return "static" # 默认"
- **依赖关系**：
  - 依赖：无（基础推断规则）
  - 支撑：92-P1（分层架构的 L1 层）、92-P9（section划分）
- **与检索机制的关系**：类型推断为检索提供分类过滤维度——检索时可以按 static/dynamic 类型过滤 Pattern，或按类型组织检索结果。这是检索的"分类索引"原语。

### 原语：边 connection 类型推断（linear/shortcut/cross_section）
- **ID**：92-P7
- **类型**：操作原语
- **描述**：根据边两端节点在拓扑序中的位置关系推断 connection 类型——回边（to 在 from 之前）→ shortcut，相邻（to 紧跟 from）→ linear，其他 → cross_section。
- **溯源**：92, 第160-174行, 原文引用："def infer_connection(edge, topo_order): """推断边的 connection 类型""" from_order = topo_order.index(edge["from_node_id"]) to_order = topo_order.index(edge["to_node_id"]) # 回边（to 在 from 之前）→ shortcut（环路回边） if to_order < from_order: return "shortcut" # 相邻（to 紧跟 from）→ linear if to_order == from_order + 1: return "linear" # 其他 → cross_section return "cross_section""
- **依赖关系**：
  - 依赖：92-P3（拓扑排序提供 topo_order）
  - 支撑：92-P1（分层架构的 L1 层）
- **与检索机制的关系**：connection 类型推断为检索提供边的分类维度——检索时可以按连接类型过滤（如只检索 linear 连续依赖链，或只检索 shortcut 回边/环路引用），不同 connection 类型对应不同的检索路径语义。

### 原语：螺旋环路遍历类型推断（spiral_static/spiral_dynamic）
- **ID**：92-P8
- **类型**：操作原语
- **描述**：根据环路中节点的类型推断环路的遍历类型——全是意识节点 → spiral_dynamic，包含 static 节点 → spiral_static。
- **溯源**：92, 第176-188行, 原文引用："def infer_traversal(loop, dg_nodes): """推断螺旋环路的遍历类型""" node_types = [] for nid in loop["nodes"]: node = get_node(dg_nodes, nid) node_types.append(node["type"]) # 全是意识节点 → spiral_dynamic if all(t == "意识" for t in node_types): return "spiral_dynamic" # 包含 static 节点 → spiral_static return "spiral_static""
- **依赖关系**：
  - 依赖：92-P6（节点类型推断）
  - 支撑：92-P1（分层架构的 L1 层）
- **与检索机制的关系**：环路遍历类型为检索提供环路 Pattern 的分类维度——检索时可以按 spiral_static/spiral_dynamic 过滤环路类型的 Pattern，用于区分"静态循环依赖"和"动态意识循环"。

### 原语：section 划分推荐——按依赖链分段 + 意识节点单独成章
- **ID**：92-P9
- **类型**：操作原语
- **描述**：将拓扑排序后的节点序列按依赖链分段聚类——意识节点（dynamic）全部归为最后一章，证明步骤（static）按固定数量分段（简化版每5个一段），生成 section 标签。
- **溯源**：92, 第192-223行, 原文引用："def recommend_sections(topo_order, dg_nodes, dg_edges): """推荐 section 划分 ... 1. 意识节点（dynamic）全部归为最后一章 2. 证明步骤（static）按依赖链分段 3. 段边界：depends_on 链的"自然断点" ... if len(current_section_nodes) >= 5: current_section += 1 current_section_nodes = []"
- **依赖关系**：
  - 依赖：92-P3（拓扑排序）、92-P6（节点类型推断）
  - 支撑：92-P10（position分配）、92-P11（边section继承）
- **与检索机制的关系**：section 划分是检索结果的聚类组织原语——将检索到的 Pattern 按逻辑段落分组，提供"按 section 检索"的能力。检索机制可以复用这种"按依赖链分段 + 按类型分离"的聚类策略。

### 原语：section 内 position 分配
- **ID**：92-P10
- **类型**：结构原语
- **描述**：根据 section 划分为每个节点分配其在所属 section 内的位置序号（position），实现 section 内的局部排序。
- **溯源**：92, 第225-237行, 原文引用："def assign_positions(topo_order, sections): """根据 section 划分分配 position（section 内位置）""" section_counters = {} positions = {} for node_id in topo_order: section = sections[node_id] if section not in section_counters: section_counters[section] = 0 section_counters[section] += 1 positions[node_id] = section_counters[section] return positions"
- **依赖关系**：
  - 依赖：92-P9（section划分）
  - 支撑：无
- **与检索机制的关系**：position 分配为检索提供"局部排序"维度——检索结果在 section 内部有明确的顺序，支持"检索某 section 的第 N 个 Pattern"这类精确定位查询。

### 原语：边的 section 继承（取 from 节点的 section）
- **ID**：92-P11
- **类型**：结构原语
- **描述**：边的 section 属性继承其 from 节点的 section 属性，实现边与节点的 section 一致性。
- **溯源**：92, 第239-243行, 原文引用："def assign_edge_sections(ut_edges, sections): """分配边的 section（取 from 节点的 section）""" for edge in ut_edges: edge["section"] = sections.get(edge["from_node_id"], "") return ut_edges"
- **依赖关系**：
  - 依赖：92-P9（section划分）
  - 支撑：无
- **与检索机制的关系**：边的 section 继承为检索提供"按 section 过滤边"的能力——检索某个 section 的 Pattern 时，可以同时检索该 section 内的依赖边，保持节点和边的一致性。

### 原语：螺旋环路圈数直接拷贝（不从算法推导）
- **ID**：92-P12
- **类型**：操作原语
- **描述**：螺旋环路的圈数（circles）不从图论算法推导，而是直接从源图 G 的 loops 集合拷贝，保证不变。
- **溯源**：92, 第85-94行, 原文引用："# 7. 构建 G'_topo 螺旋环路（直接拷贝，圈数保持） ut_loops = [] for loop in loops: ut_loops.append({ ... "circles": loop["circles"], # 保持不变 ...})"
- **依赖关系**：
  - 依赖：无
  - 支撑：92-P13（全覆盖保证）
- **与检索机制的关系**：直接拷贝保留结构属性是检索的"保真传递"原语——从认知图检索 Pattern 时，某些结构属性（如环路圈数）应直接保留而非重新计算，避免信息丢失或计算误差。

### 原语：全覆盖保证——从 G 直接拷贝保证拓扑同构
- **ID**：92-P13
- **类型**：性质标准
- **描述**：因为节点集和边集是从源图 G 直接拷贝的（拓扑同构），螺旋环路圈数保持不变，所以 TopologyVerifier 验证必然一次通过，保证 100% 覆盖。
- **溯源**：92, 第313-318行, 原文引用："**经典计算版本的 G'_topo 必然通过 TopologyVerifier 验证**，因为：- 节点集和边集是从 G 直接拷贝的（拓扑同构）- 螺旋环路圈数保持不变 - TopologyVerifier 只验证节点覆盖、边覆盖、螺旋环路圈数——这些都被 L0 保证"
- **依赖关系**：
  - 依赖：92-P2（骨架展开）、92-P12（圈数拷贝）
  - 支撑：92-P14（验证闭环）
- **与检索机制的关系**：全覆盖保证是检索的"完整性约束"原语——检索机制必须保证从认知图中检索到的 Pattern 集合是完整的，不遗漏任何节点或边。直接拷贝 + 拓扑同构是保证完整性的最简单可靠方法。

### 原语：TopologyVerifier 验证闭环
- **ID**：92-P14
- **类型**：操作原语
- **描述**：生成 G'_topo 后调用 TopologyVerifier 验证节点覆盖、边覆盖、螺旋环路圈数，形成"生成→验证"的闭环，保证结果正确性。
- **溯源**：92, 第333-336行, 原文引用："# 2c. TopologyVerifier 验证（必然1次通过） report = topology_verifier.verify_all() assert report.node_coverage == 1.0 assert report.edge_coverage == 1.0"
- **依赖关系**：
  - 依赖：92-P13（全覆盖保证）
  - 支撑：无
- **与检索机制的关系**：验证闭环是检索机制的"质量保证"原语——检索完成后应验证检索结果的完整性和正确性（覆盖率、结构保持），形成"检索→验证"的闭环。这是检索机制可靠性的基础。

### 原语：depends_on 有环报错——图完整性校验
- **ID**：92-P15
- **类型**：操作原语
- **描述**：拓扑排序中如果 depends_on 边构成环（无法完成排序），报错并指出未排序节点，作为依赖图完整性的校验机制。
- **溯源**：92, 第134-138行, 原文引用："if len(order) != len(node_ids): # 有环——检查是否是 calls 边导致的（calls 边不参与排序） # 如果是 depends_on 有环，报错 remaining = set(node_ids) - set(order) raise ValueError(f"depends_on 边有环，无法拓扑排序。未排序节点: {remaining}")"
- **依赖关系**：
  - 依赖：92-P3（拓扑排序算法）
  - 支撑：92-P14（验证闭环）
- **与检索机制的关系**：有环报错是检索的"前置校验"原语——检索前应检查认知图的依赖关系是否有环（循环依赖），如果有环则拓扑排序无法进行，需要先解决循环依赖。这是检索前置条件的校验机制。

### 原语：经典计算 + AI 细化的双模式
- **ID**：92-P16
- **类型**：概念框架
- **描述**：提供两种工作模式——纯经典计算（L0+L1+L2，不需要 AI，适用于快速验证/小规模图）和经典计算 + AI 细化（L0+L1+L2 经典计算 + L3 AI 语义标注，适用于正式场景/大规模图）。
- **溯源**：92, 第343-348行, 原文引用："| 模式 | 内容 | 适用场景 | |---|---|---| | **纯经典计算** | L0+L1+L2，不需要 AI | 快速验证、小规模依赖图、POC 预测试 | | **经典计算 + AI 细化** | L0+L1+L2 经典计算，L3 AI 语义标注 | 正式 POC、大规模依赖图、需要语义质量 |"
- **依赖关系**：
  - 依赖：92-P1（分层架构）
  - 支撑：92-P17（推荐非强制）
- **与检索机制的关系**：双模式是检索机制的"弹性架构"原语——检索机制应支持纯算法检索（快速、确定性）和算法 + AI 语义检索（高质量、语义匹配）两种模式，按场景选择。这是检索机制的适应性设计。

### 原语：L2 推荐非强制——AI 可调整
- **ID**：92-P17
- **类型**：概念框架
- **描述**：L2 的 section 划分是推荐值而非强制值，AI 可以在 L3 阶段调整 section 边界，经典计算的 section 划分是默认值不是最优值。
- **溯源**：92, 第427行, 原文引用："1. **section 划分的质量**：L2 的启发式规则（每5个一段+意识单独成章）是粗糙的近似。meta AI 的 section 划分更符合数学证明的逻辑结构。但 L2 的目的是提供合理默认值，不是最优划分。"
- **溯源2**：92, 第482行, 原文引用："5. **L2是推荐不是强制**：AI可以在L3阶段调整section边界。经典计算的section划分是默认值，不是最优值。"
- **依赖关系**：
  - 依赖：92-P9（section划分）、92-P16（双模式）
  - 支撑：无
- **与检索机制的关系**：推荐非强制是检索的"人机协同"原语——检索机制可以先用算法生成默认的检索结果组织（如聚类、排序），然后允许 AI 或用户调整。这是检索机制的可干预性设计。

### 原语：对比验证——经典计算版与 AI 版差异分析
- **ID**：92-P18
- **类型**：操作原语
- **描述**：生成经典计算版本的 G'_topo 后，与 meta AI 生成的版本进行多维度对比（节点覆盖、边覆盖、traversal_order、section 划分、connection 类型），分析差异点。
- **溯源**：92, 第289-311行, 原文引用："POC-2 的依赖图（18节点25边2环路）已经有 meta AI 生成的 G'_topo 作为基准。用 `topo_generator.py` 生成经典计算版本，对比：| 对比维度 | 验证方法 | ... | traversal_order | 对比：经典计算的拓扑序与 meta AI 的 traversal_order 的差异 | | section 划分 | 对比：经典计算的 section 与 meta AI 的 section 的差异 |"
- **依赖关系**：
  - 依赖：92-P2（骨架展开）、92-P14（验证闭环）
  - 支撑：无
- **与检索机制的关系**：对比验证是检索的"基准评估"原语——检索机制应支持与基准结果（如 AI 生成的结果或人工标注的结果）进行多维度对比，评估检索质量。这是检索机制的可评估性设计。

### 原语：渐进式复用——最小/完整/增强三级实现
- **ID**：92-P19
- **类型**：概念框架
- **描述**：将实现分为三个渐进级别——最小实现（仅 L0 骨架展开）、完整实现（L0+L1+L2）、增强实现（L0+L1+L2+验证+对比），每级在前一级基础上增加功能。
- **溯源**：92, 第448-475行, 原文引用："### 9.1 最小实现 ... 如果只需要经典计算展开的骨架（L0）：1. 实现`topological_sort`函数 ... ### 9.2 完整实现 ... 需要L0+L1+L2（经典计算生成完整骨架+推荐）：... ### 9.3 增强实现 ... 需要L0+L1+L2+验证+对比：..."
- **依赖关系**：
  - 依赖：92-P1（分层架构）
  - 支撑：无
- **与检索机制的关系**：渐进式复用是检索机制的"模块化构建"原语——检索机制可以按需选择实现级别，从最简单的全量检索（最小实现）到带分类过滤的检索（完整实现）到带验证和基准评估的检索（增强实现）。这是检索机制的可扩展性设计。

### 原语：traversal_order 作为节点的全局遍历序号
- **ID**：92-P20
- **类型**：结构原语
- **描述**：每个节点在拓扑排序后被赋予一个全局的 traversal_order（从1开始的序号），作为节点在展开图中的全局遍历顺序标识。
- **溯源**：92, 第64-72行, 原文引用："for i, node_id in enumerate(topo_order): node = get_node(dg_nodes, node_id) ut_nodes.append({ "node_id": node_id, "type": infer_type(node), # L1 "section": "", # L2 填充 "position": 0, # L2 填充 "traversal_order": i + 1, })"
- **依赖关系**：
  - 依赖：92-P3（拓扑排序）
  - 支撑：92-P7（connection类型推断使用topo_order）、92-P10（position分配）
- **与检索机制的关系**：traversal_order 是检索的"全局排序索引"原语——为每个 Pattern 节点赋予全局序号，支持"按全局顺序检索"和"检索第 N 个 Pattern"这类基于位置的查询。与 section 内 position 形成"全局序号 + 局部序号"的双层定位。

### 原语：节点数据结构——node_id + type + section + position + traversal_order 五元组
- **ID**：92-P21
- **类型**：结构原语
- **描述**：展开图中的节点采用五元组数据结构：node_id（唯一标识）、type（static/dynamic）、section（所属段落）、position（section内位置）、traversal_order（全局遍历序号）。
- **溯源**：92, 第66-72行, 原文引用："ut_nodes.append({ "node_id": node_id, "type": infer_type(node), # L1 "section": "", # L2 填充 "position": 0, # L2 填充 "traversal_order": i + 1, })"
- **依赖关系**：
  - 依赖：92-P6（类型推断）、92-P9（section划分）、92-P10（position分配）、92-P20（traversal_order）
  - 支撑：无
- **与检索机制的关系**：节点五元组是检索的"索引结构"原语——每个 Pattern 节点携带五个可检索维度（ID、类型、段落、局部位置、全局位置），支持多维度的检索查询。这是检索索引的基本数据结构。

### 原语：边数据结构——from_node_id + to_node_id + edge_type + section + connection 五元组
- **ID**：92-P22
- **类型**：结构原语
- **描述**：展开图中的边采用五元组数据结构：from_node_id（起点）、to_node_id（终点）、edge_type（depends_on/calls）、section（所属段落）、connection（linear/shortcut/cross_section）。
- **溯源**：92, 第76-83行, 原文引用："ut_edges.append({ "from_node_id": edge["from_node_id"], "to_node_id": edge["to_node_id"], "edge_type": edge["edge_type"], "section": "", # L2 填充 "connection": infer_connection(edge, topo_order), # L1 })"
- **依赖关系**：
  - 依赖：92-P4（边类型区分）、92-P7（connection类型推断）、92-P11（边section继承）
  - 支撑：无
- **与检索机制的关系**：边五元组是检索的"关系索引结构"原语——每条依赖边携带五个可检索维度（起点、终点、关系类型、段落、连接类型），支持多维度的关系检索。这是检索关系索引的基本数据结构。

### 原语：环路数据结构——loop_id + nodes + circles + section + traversal 五元组
- **ID**：92-P23
- **类型**：结构原语
- **描述**：展开图中的螺旋环路采用五元组数据结构：loop_id（环路标识）、nodes（环路包含的节点列表）、circles（圈数）、section（所属段落）、traversal（遍历类型 spiral_static/spiral_dynamic）。
- **溯源**：92, 第87-94行, 原文引用："ut_loops.append({ "loop_id": loop["loop_id"], "nodes": loop["nodes"], "circles": loop["circles"], # 保持不变 "section": "", # L2 填充 "traversal": infer_traversal(loop, dg_nodes), # L1 })"
- **依赖关系**：
  - 依赖：92-P8（环路遍历类型推断）、92-P12（圈数拷贝）、92-P9（section划分）
  - 支撑：无
- **与检索机制的关系**：环路五元组是检索的"环路索引结构"原语——每个环路 Pattern 携带五个可检索维度（环路ID、包含节点、圈数、段落、遍历类型），支持环路 Pattern 的多维度检索。这是检索环路索引的基本数据结构。

### 原语：ArangoDB 集合分离——dg_nodes/dg_edges/loops（源图） vs ut_nodes/ut_edges（展开图）
- **ID**：92-P24
- **类型**：结构原语
- **描述**：源依赖图 G 的数据存储在 ArangoDB 的 dg_nodes/dg_edges/loops 集合中，展开图 G'_topo 的数据存储在 ut_nodes/ut_edges 集合中，实现源图与展开图的物理分离。
- **溯源**：92, 第35-41行, 原文引用："#### 输入 - ArangoDB 中的 `dg_nodes`（节点集）- ArangoDB 中的 `dg_edges`（边集，含 edge_type: depends_on / calls）- ArangoDB 中的 `loops`（螺旋环路，graph=dependency_graph） #### 输出 - G'_topo JSON（写入文件 + 导入 ArangoDB 的 ut_nodes / ut_edges）"
- **依赖关系**：
  - 依赖：无（基础设施层）
  - 支撑：92-P2（骨架展开从dg_*读取写入ut_*）
- **与检索机制的关系**：集合分离是检索的"数据源隔离"原语——认知图（源数据）和检索结果（展开图）存储在不同的集合中，避免读写冲突，支持检索结果的独立管理和版本控制。

### 原语：L3 保留给 AI——语义标注需要语义理解
- **ID**：92-P25
- **类型**：概念框架
- **描述**：section 命名和 spiral 类型最终确认需要语义理解，经典计算做不到，因此 L3 层保留给 AI 处理。
- **溯源**：92, 第433行, 原文引用："4. **L3 可能不可省略**：如果 section 命名和 spiral 类型的语义标注对转译质量很重要，L3 不能省略。但 L0+L1+L2 已经保证了全覆盖和合理结构，L3 只是锦上添花。"
- **溯源2**：92, 第483行, 原文引用："6. **L3保留给AI**：section命名和spiral类型最终确认需要语义理解，经典计算做不到。"
- **依赖关系**：
  - 依赖：92-P1（分层架构）
  - 支撑：92-P16（双模式）、92-P17（推荐非强制）
- **与检索机制的关系**：L3 保留给 AI 是检索的"语义层分离"原语——检索机制中，结构检索（算法可完成）和语义检索（需要 AI 理解）应分层处理。算法负责结构完整的候选集生成，AI 负责语义排序和命名。这是检索机制的"算法 + AI"分工边界。

## 文档中无原语可提取的部分

1. **第六节 Check List（第392-423行）**：这是实现任务清单，属于项目管理内容，不包含可复用的设计决策或机制，不作为原语提取。

2. **第八节"与方案1的关系"中的集成细节（第437-444行）**：这部分描述的是两个具体方案之间的集成点（如 `seven_step_workflow` 认知单元与 `topo_generator.py` 的关系），属于项目特定的集成描述，不是通用的可复用原语。但"方案可并行实现、最终集成时成为 SDK 的一个方法"这一思路有一定参考价值，不过不够具体，不单独提取为原语。

3. **第五节文件设计中的 CLI 使用示例（第354-373行）**：这是具体的命令行使用示例，属于操作说明，不包含可复用的设计决策。
