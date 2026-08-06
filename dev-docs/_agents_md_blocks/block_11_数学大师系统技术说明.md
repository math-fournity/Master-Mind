## 数学大师系统技术说明

> 本节是数学大师系统（目标系统——数学证明的依赖结构管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用数学大师系统"的认知。完整方案见依赖文档。

### 七步骤工作流 [legacy-static]

> **[legacy-static]** 123号v1已将七步骤正式降为legacy静态重建器。保留静态知识图与提示展开价值，不再承担主运行时。主运行时改为12步事件溯源循环（观测→状态归约→候选规则匹配→受约束干预→验证→归因→回写）。旧七步骤的100%拓扑覆盖只证明结构保真，不证明语义或数学真值，也不证明动态思维矫正。

#### 旧七步骤→新12步运行时的迁移映射

> 来源：系统探讨.md第十二节 + plan + 123号第五十三节

| 旧步骤 | 新位置 | 说明 |
|---|---|---|
| 1.导入依赖图 | K图离线构建与发布 | 不再每轮运行时导入，K图是离线维护的 |
| 2.topo_generator | 局部激活包的结构编译器 | 不再全图展开，只编译当前卡点相关的最小结构 |
| 3.TopologyVerifier | 验证选定结构是否完整 | 只验证激活包的结构保真，不证明Hint正确 |
| 4.转译 | 增量Context Compiler | 只编译"当前卡点+一个最小操作+必要接口+可选工具" |
| 5.KC审计 | Hint注入前的知识忠实与泄漏审计 | 由Auditor角色执行，不是meta AI |
| 6.一次性分析 | 循环中的Solver step | Solver在12步循环中的步骤3和步骤10 |
| 7.最终覆盖审计 | 每轮进展审计+最终证明义务审计 | 由Verifier和Auditor分别执行 |

**核心变化**：不是抛弃旧系统，而是把它从"整个运行时"降为"动态控制系统中的局部上下文编译与结构验证模块"。

数学大师系统的核心是七步骤工作流，通过`seven_step_pipeline.py`执行：

| 步骤 | 执行者 | 内容 | 命令 |
|---|---|---|---|
| 1 | 代码 | 依赖图G导入ArangoDB | `seven_step_pipeline.py --steps 1` |
| 2 | **经典计算** | **topo_generator.py生成G'_topo骨架（L0+L1+L2）** + AI语义细化（L3） | `seven_step_pipeline.py --steps 2` |
| 3 | 代码 | TopologyVerifier拓扑覆盖验证（1次通过100%覆盖） | `seven_step_pipeline.py --steps 3` |
| 4 | normal AI | 按G'_topo转译为大师提示词 | `seven_step_pipeline.py --steps 4` |
| 5 | meta AI | KC忠实审计（转译是否忠实于知识内容） | `seven_step_pipeline.py --steps 5` |
| 6 | normal AI | 在大师提示词引导下做数学证明 | `seven_step_pipeline.py --steps 6` |
| 7 | meta AI | 分析覆盖审计（分析是否覆盖G'_topo所有节点和边） | `seven_step_pipeline.py --steps 7` |

**一键执行步骤1-3**（经典计算部分）：
```bash
.venv/bin/python3 xishujuzhen/seven_step_pipeline.py --steps 1,2,3
```

**步骤2的升级**（反哺1）：从"meta AI生成G'_topo"升级为"经典计算生成骨架+AI语义细化"。经典计算保证全覆盖，AI只做L3语义标注（section命名、spiral类型确认）。

### 依赖图导入ArangoDB

依赖图G存储在ArangoDB的`xishujuzhen_math`数据库中：
- `dg_nodes`：节点集（1719个，7种type：concept/domain_concept/paradigm/problem/substep/意识/step）——详见126号只读盘点报告
- `dg_edges`：边集（1483个，edge_type以unknown为主但mapping_type有40+种映射类型）——详见126号只读盘点报告
- `loops`：螺旋环路（4个，含圈数）
- `arxiv_papers`：**arXiv论文库**（239472篇元数据，2023-2026年，44个分类）。支持按分类/日期/作者/关键词查询。每篇论文有mapping_level（L1定理级/L2方法级/L3意识级/L4索引级）和linked_nodes（关联的dg_nodes）。详见112号方案。

### arXiv论文查询

```bash
# 按分类查询
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(category='math.AG', limit=5)]"

# 关键词搜索
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(keyword='Ramanujan', limit=5)]"

# 有全文的论文
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(p['arxiv_id'],p['title'][:50]) for p in CognitionSDK().search_arxiv(has_fulltext=True, limit=5)]"

# 提升论文映射级别（L4→L1/L2/L3）
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; print(CognitionSDK().promote_arxiv_paper('2607.27504','L1','Ramanujan_airy_asymptotics'))"
```

### G'_topo生成（经典计算展开）

`topo_generator.py`从G自动生成G'_topo骨架：
- L0骨架展开：节点集+边集直接拷贝（拓扑同构保证全覆盖）+ Kahn拓扑排序确定traversal_order
- L1类型推断：static/dynamic + connection类型（linear/shortcut/cross_section）
- L2 section划分：按依赖链长度分段+意识节点处理
- L3语义标注（AI）：section命名、spiral_static/dynamic最终确认

### TopologyVerifier拓扑覆盖验证（结构保真验证）

> **[结构保真验证]** TopologyVerifier验证的是输出骨架不遗漏输入图节点/边（结构保真），不代表语义或数学正确。100%拓扑覆盖只证明结构完整性，不证明语义真值、数学正确性或动态思维矫正效果。

`topology_verifier.py`验证G'_topo是否覆盖G：
- 节点覆盖：ut_nodes vs dg_nodes的集合差集
- 边覆盖：ut_edges vs dg_edges的集合差集
- 螺旋环路：圈数是否保持
- 结果：passed=True + 100%覆盖 = 结构保真通过（不代表语义或数学正确）

### 三层提取（L1/L2/L3）

83号文档设计的三层提取，L1/L2/L3是提取层次（解题思路→数学思维→范式思维），不是版本号。版本链用v1/v2/v3等独立编号，与L1/L2/L3无映射关系。

| 层次 | 内容 | 复用范围 |
|---|---|---|
| L1解题思路 | 具体步骤序列 | 类似题 |
| L2数学思维 | 从L1抽象出的思维模式（AI二次分析） | 跨题、跨领域 |
| L3范式思维 | 从多个L2综合出的范式（AI三次分析） | 改变图结构 |

**版本链操作**（版本号独立于L1/L2/L3层次）：
```bash
# 添加新版本
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); sdk.add_version('<cog_id>', 'v2', '<doc>', '<summary>', version_order=2); sdk.update_current_version('<cog_id>', 'v2')"
```

**current_version反映文档版本**，与L1/L2/L3提取层次无映射关系。

### 数学意识节点（5个）

| 意识节点 | cog_id | 说明 |
|---|---|---|
| 不变量思维 | invariant_thinking | 识别什么是不变量，在扰动下保持 |
| 局部-全局思维 | local_global_thinking | 局部性质推出全局性质 |
| 逼近论思维 | approximation_thinking | 分析逼近精度和误差阶 |
| 极端检验 | extreme_testing | 在极端构型下验证命题 |
| 数值检验意识 | numerical_check | 用数值例子检验命题自洽性 |

**双重身份**：每个意识节点同时在cognition_units（工作认知）和dg_nodes（数学依赖图）中有记录。

**版本链状态**：5个意识节点都有v1(POC-1发现)→v2(POC-2深化)版本链，current_version=v2。

### 依赖维护

本节的依赖关系存储在认知图稀疏矩阵中（认知单元 `agents_tech_mathmaster`）：
- source_docs: [83, 85, 86, 88, 90, 92, 99, 100]
- depends_on: seven_step_workflow, classic_expansion, topology_verifier, topology_coverage, three_layer_extraction, math_awareness_nodes, spiral_cognition

**查依赖**：`cognition_sdk_math.py traverse(['agents_tech_mathmaster'])`
**反向查询**（当某个dev-docs更新时，查哪些技术说明节需要同步）：
```bash
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(u['cog_id'],u['title']) for u in CognitionSDK().find_dependents_by_doc(88)]"
```

