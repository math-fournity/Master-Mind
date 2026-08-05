# dev-docs/112-arXiv论文导入ArangoDB与节点映射规则方案

## 一、问题

109号方案设计了~325000节点的穷尽式知识宇宙。110号方案设计了三层访问架构（冷存储→热工作集→温查询）来操作化这个规模。

但当前依赖图（dg_nodes）只有1697节点（题库Phase A手工构建），而239472篇arXiv元数据和1305篇全文只是JSON文件和Markdown文件——**它们在仓库里，但不在系统里**。系统不知道它们的存在，无法查询、无法激活、无法在证明时被引用。

本方案解决：**如何把239K篇arXiv论文从"仓库里的文件"变成"ArangoDB里可查询、可激活的知识资产"，并为论文→依赖图节点的映射建立规则。**

## 二、核心设计决策

### 决策1：论文不是节点，论文是节点的出处

arXiv论文不应直接成为dg_nodes中的节点。原因：

- 239K篇全部成为节点 → 依赖图变成无差别的论文堆，无法体现"哪些知识是重要的"
- 109号方案的~325000节点是**数学知识节点**（定理/引理/方法/概念），不是论文节点
- 一篇论文可能包含多个定理，一个定理可能跨多篇论文——论文和知识节点是多对多关系

**正确的关系**：
```
论文（arxiv_papers collection） → 包含/证明 → 知识节点（dg_nodes）
知识节点（dg_nodes）.source字段 → 引用 → 论文（arxiv_papers collection）
```

### 决策2：四级映射规则

并非所有论文都与依赖图有同等关系。按111号"难妙新"优先级和知识重要性，分四级：

| 级别 | 论文特征 | 映射方式 | 存储位置 | 估算数量 |
|---|---|---|---|---|
| **L1 定理级** | 证明重要定理/解决开放问题/突破性结果 | 论文中的定理成为dg_nodes的concept节点，source指向arXiv ID | dg_nodes + arxiv_papers | ~数百 |
| **L2 方法级** | 引入新方法/新技术/新工具 | 方法名成为dg_nodes的concept或domain_concept节点 | dg_nodes + arxiv_papers | ~数千 |
| **L3 意识级** | 体现数学思维范式转变 | 成为dg_nodes的paradigm节点，含domains_connected | dg_nodes + arxiv_papers | ~数十 |
| **L4 索引级** | 绝大多数论文 | 仅存储在arxiv_papers中，可搜索可查询，但不在dg_nodes中 | arxiv_papers only | ~23万 |

**关键原则**：L4论文不是"不重要"，而是"尚未被激活"。当某个数学问题需要用到某篇L4论文时，它可以被提升为L1/L2/L3——这正是"大师的一次在场"。

### 决策3：arxiv_papers作为独立collection

新增`arxiv_papers` collection存储239K篇元数据，与dg_nodes/cognition_units分开。原因：

- 239K篇论文不是"认知单元"也不是"数学知识节点"，是"原始知识资产"
- 独立collection便于按分类/日期/作者/关键词查询
- 不污染现有依赖图的遍历性能（1697节点 vs 239K论文）
- 符合110号三层架构：arxiv_papers是"冷存储层"，dg_nodes子图是"热工作集"

## 三、ArangoDB Schema设计

### 新增collection

| collection | 类型 | 内容 | 预估文档数 |
|---|---|---|---|
| `arxiv_papers` | document | 239K篇arXiv论文元数据 | 239472 |

### arxiv_papers文档结构

```json
{
  "_key": "2608_00157",           // arXiv ID，.替换为_
  "arxiv_id": "2608.00157",
  "title": "...",
  "authors": ["Author1", "Author2"],
  "abstract": "...",
  "primary_category": "math.AG",
  "all_categories": ["math.AG", "math.NT"],
  "published": "2026-08-01T00:00:00Z",
  "updated": "2026-08-01T00:00:00Z",
  "doi": "...",
  "comment": "...",
  "journal_ref": "...",
  "html_url": "https://arxiv.org/html/2608.00157",
  "has_fulltext": true,            // 是否有HTML全文
  "fulltext_path": "knowledge/arxiv/fulltext/math_AG_2608_00157.md",
  "mapping_level": "L4",           // 当前映射级别
  "linked_nodes": []               // 已映射到的dg_nodes的node_id列表
}
```

### 新增索引

| 索引 | 类型 | 字段 | 用途 |
|---|---|---|---|
| `idx_arxiv_primary_cat` | persistent | `primary_category` | 按主分类查询 |
| `idx_arxiv_published` | persistent | `published` | 按日期查询 |
| `idx_arxiv_all_cats` | inverted | `all_categories[*]` | 按任意分类查询 |
| `idx_arxiv_title_abstract` | inverted | `title, abstract` | 全文搜索标题和摘要 |
| `idx_arxiv_authors` | inverted | `authors[*]` | 按作者查询 |

### dg_nodes的source字段扩展

现有dg_nodes的`source`字段格式为`"MATH-001/MATH-001-S1"`（题目/解法编号）。扩展为支持arXiv引用：

```
source: "MATH-001/MATH-001-S1"           // 题库来源（现有）
source: "arxiv:2608.00157"                // arXiv论文来源（新增）
source: "arxiv:2608.00157, MATH-001/..."  // 混合来源
```

## 四、论文→依赖图节点的映射规则

### L1 定理级映射规则

**触发条件**（满足任一）：
- 论文标题/摘要包含"we prove" + 定理名
- 论文解决已知开放问题
- 论文被引用次数显著（需要外部数据，当前无法自动判断）

**映射方式**：
```
论文 → 提取定理名 → 创建dg_node(type=concept, node_id=定理名, source="arxiv:<id>")
```

**示例**：论文2608.02413标题"We prove the Ramanujan conjecture for GL(3)" →
- dg_node: node_id="Ramanujan_conjecture_GL3", type="concept", domain="number_theory", source="arxiv:2608.02413"

### L2 方法级映射规则

**触发条件**：
- 论文标题/摘要包含"we introduce" / "we develop" / "new method" / "new technique"
- 论文引入的工具/方法有明确名称

**映射方式**：
```
论文 → 提取方法名 → 创建dg_node(type=concept/domain_concept, node_id=方法名, source="arxiv:<id>")
```

### L3 意识级映射规则

**触发条件**：
- 论文体现跨领域统一视角
- 论文标题/摘要包含"unified" / "analogy" / "correspondence" / "duality between"

**映射方式**：
```
论文 → 创建dg_node(type=paradigm, node_id=范式描述, domains_connected=[...], source="arxiv:<id>")
```

### L4 索引级（默认）

**映射方式**：仅在arxiv_papers中存储，不创建dg_node。可通过AQL查询。

### 映射级别的动态提升

当某个L4论文在POC实验或数学证明中被用到时：
1. 从arxiv_papers中查询到该论文
2. 人工（或AI辅助）判断其属于L1/L2/L3哪一级
3. 创建对应的dg_node
4. 更新arxiv_papers文档的mapping_level和linked_nodes

## 五、论文→依赖图边的映射规则

除了论文成为节点外，论文之间和论文与现有节点之间也可以有边：

| 边类型 | 来源 | 规则 | 存储位置 |
|---|---|---|---|
| `same_category` | 同分类论文 | 同primary_category的论文有弱关联 | arxiv_paper_edges（新collection，可选） |
| `cross_category` | 跨分类论文 | 论文的all_categories跨多个领域 | arxiv_paper_edges |
| `proves` | 论文→定理节点 | L1论文证明的定理与已有dg_nodes的concept相连 | dg_edges (edge_type=proves) |
| `uses_method` | 论文→方法节点 | L2论文使用的方法与已有dg_nodes的concept相连 | dg_edges (edge_type=invokes) |

**初期简化**：只实现`proves`和`uses_method`（直接在dg_edges中），暂不建arxiv_paper_edges。

## 六、实现Check List

- [ ] 1. 创建`arxiv_papers` collection + 5个索引
- [ ] 2. 写`arxiv_to_arangodb.py`脚本：读取`metadata_all_2023plus.json`，批量导入239K篇
- [ ] 3. 批量导入，分批每5000篇一批（避免内存溢出）
- [ ] 4. 验证：文档数=239472，索引正常
- [ ] 5. 写查询SDK：`cognition_sdk_math.py`新增`search_arxiv()`方法
  - 按分类查询：`search_arxiv(category="math.AG", limit=20)`
  - 按关键词搜索：`search_arxiv(keyword="Ramanujan", limit=20)`
  - 按作者查询：`search_arxiv(author="Tao", limit=20)`
  - 按日期范围：`search_arxiv(date_from="2026-01-01", date_to="2026-08-01")`
- [ ] 6. 测试查询功能
- [ ] 7. 系统完整性检查：导入后认知图统计正常 + 回归验证通过
- [ ] 8. 更新AGENTS.md Handover Section

## 七、与110号三层架构的关系

本方案实现110号三层架构的**冷存储层**：

| 层 | 110号方案 | 本方案实现 |
|---|---|---|
| 冷存储层 | ArangoDB全部325000节点 | `arxiv_papers` collection（239K论文）+ `dg_nodes`（1697节点） |
| 热工作集 | 当前问题相关200-800节点子图 | （待实现，需要种子选择+图遍历） |
| 温查询层 | AI推理中按需expand/query | `search_arxiv()` + `cognition_sdk_math.py`图遍历 |

## 八、与后续POC（C方向）的关系

B方向完成后，C方向（跨领域POC验证泛化性）可以这样使用arXiv知识：

1. 选择一个非矩条件极差题的数学领域（如代数拓扑/数论/组合）
2. 用`search_arxiv()`查询该领域的最新论文
3. 从论文中提取关键定理/方法，创建L1/L2级dg_nodes
4. 手工补充该领域的依赖图（节点+边）
5. 用七步骤工作流跑POC，验证方法论在新领域是否成立

arXiv论文为C方向提供了**真实的、最新的数学知识素材**——不再是只靠AI内在知识，而是有出处、可引用的真实研究。

## 九、风险与诚实评估

1. **239K篇导入ArangoDB的性能**：239K文档 + 5索引，预估ArangoDB可承受。需测试导入时间和查询性能。
2. **inverted索引可能需要ArangoDB Enterprise版**：如果Community版不支持inverted索引，改用ArangoSearch或简单persistent索引。
3. **L1/L2/L3映射的自动化程度**：当前方案中L1/L2/L3映射需要人工或AI判断，无法全自动。这是"大师的一次在场"的体现——不是缺点，是设计。
4. **论文引用关系缺失**：arXiv API不提供引用关系。如果需要引用网络，需要从CrossRef/Semantic Scholar获取。当前暂不实现。
