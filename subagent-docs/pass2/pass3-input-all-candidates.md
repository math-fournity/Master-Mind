# Pass 3 输入：全部新原语候选（7组汇总）

来源：Pass 2 的7个提炼结果文件中的 [new-candidate] 条目

---


## pangu-a (15 candidates)

### 依赖图（dependency-graph）
- 类型: 结构原语
- 定义: 用有向图表示知识间的依赖关系——节点带类型（step/substep/意识）、上下文元数据、知识内容；边带类型（depends_on/calls）；可有跨域边和螺旋环路。说"用依赖图"就知道要构建节点、编码边、嵌入知识、标注上下文。
- 验证: tested
- 来源: 63-P1, 63-P11, 64-P04, 68-P1, 68-P3, 68-P4, 68-P5, 68-P9, 70-P1, 70-P2, 70-P5, 7
- 依赖: 依赖 data-pedestal（存储基础设施）；支撑 graph-traversal-retrieval, topology-coverage-verification, spiral-cycle-detection, classical

### 拓扑骨架（topology-skeleton）
- 类型: 结构原语
- 定义: 依赖图G的纯拓扑同构拷贝G'_topo——结构相同但不含文字内容，每个节点标注其在文字展开中的位置（section/position），每条边标注连接方式，螺旋环路保持圈数。说"生成拓扑骨架"就知道要从G拷贝节点和边、做拓扑排序、分配位置、
- 验证: tested
- 来源: 78-P7, 78-P8, 86-P16, 86-P17, 86-P18, 86-P19, 87-P6, 87-P12, 88-P4, 90-P1, 90-P1
- 依赖: 依赖 dependency-graph, classical-unfolding；支撑 topology-coverage-verification

### 认知单元（cognitive-unit）
- 类型: 结构原语
- 定义: 认知图的基本节点，包含cog_id、title、category（core/process/support）、key_cognition（核心认知摘要）、source_docs（来源文档）、current_version（当前版本指针）、s
- 验证: tested
- 来源: 89-P15, 91-P03, 91-P08, 91-P21, 91-P23, 91-P24, 91-P25, 93-P03, 93-P05, 93-P09, 
- 依赖: 依赖 data-pedestal；支撑 cognitive-checkpoint, graph-traversal-retrieval, version-chain

### 版本链（version-chain）
- 类型: 结构原语
- 定义: 认知单元的演化历史——有序版本序列（v1→v2→v3...），每个版本记录来源POC编号和验证结果，current_version指针指向最新版本。说"用版本链"就知道要创建版本记录、建立evolves_to边、更新current_vers
- 验证: tested
- 来源: 89-P15, 89-P16, 91-P07, 93-P08, 95-P10, 96-P09, 97-P06, 98-P05, 98-P06, 99-P08, 
- 依赖: 依赖 cognitive-unit；支撑 cognitive-checkpoint, three-layer-extraction

### 种子推荐表（seed-recommendation-table）
- 类型: 结构原语
- 定义: 为每类问题建立"问题类型→种子认知单元/意识"的映射表，实现从问题特征到检索起点的路由。说"用种子推荐表"就知道根据问题类型查表选种子，然后从种子出发做图遍历。
- 验证: untested
- 来源: 99-P04, 99-P01, 96-P04
- 依赖: 依赖 cognitive-unit, dependency-graph；支撑 graph-traversal-retrieval, cognitive-checkpoint

### 图遍历检索（graph-traversal-retrieval）
- 类型: 操作原语
- 定义: 从种子节点出发，沿depends_on边进行有界深度BFS/AQL图遍历，返回路径上所有相关节点作为检索结果。说"做图遍历检索"就知道要选种子、设深度、执行遍历、返回子图。
- 验证: tested
- 来源: 63-P5, 64-P07, 80-P1, 89-P09, 89-P12, 91-P01, 91-P06, 94-P01, 94-P05, 94-P07, 95
- 依赖: 依赖 dependency-graph, cognitive-unit；支撑 cognitive-checkpoint, topology-coverage-verification

### 拓扑覆盖验证（topology-coverage-verification）
- 类型: 操作原语
- 定义: 用AQL集合差集运算确定性验证一个图是否完全覆盖另一个图的所有节点、边和螺旋环路——计算差集，差集为空即100%覆盖。说"做拓扑覆盖验证"就知道要跑TopologyVerifier、检查四个维度、差集非空则回退。
- 验证: tested
- 来源: 78-P9, 78-P12, 78-P19, 78-P20, 79-P06, 79-P07, 86-P05, 86-P11, 87-P05, 87-P08, 8
- 依赖: 依赖 dependency-graph, topology-skeleton, data-pedestal；支撑 classical-unfolding, cognitive-checkpoint

### 螺旋环路检测（spiral-cycle-detection）
- 类型: 操作原语
- 定义: 用Tarjan SCC算法发现图中所有环，然后对每个SCC检查节点的上下文元数据——上下文相同→平面环路（标记已处理，停止追溯），上下文不同→螺旋环路（保留，继续追溯）。说"做螺旋环路检测"就知道要跑SCC、检查上下文、分类环路。
- 验证: tested
- 来源: 63-P4, 64-P05, 66-P8, 69-P2, 70-P4, 71-P5, 78-P4, 84-P6, 84-P7, 84-P11, 85-P3, 8
- 依赖: 依赖 dependency-graph；支撑 topology-skeleton, classical-unfolding

### 经典计算展开（classical-unfolding）
- 类型: 操作原语
- 定义: 用Kahn拓扑排序+节点/边直接拷贝从依赖图G生成拓扑骨架G'_topo，分四层：L0骨架展开（节点/边拷贝+拓扑排序）、L1类型推断（step→static, 意识→dynamic）、L2 section划分推荐（按依赖链分段）、L3语义
- 验证: tested
- 来源: 78-P7, 90-P1, 90-P2, 90-P3, 90-P4, 90-P5, 90-P6, 90-P7, 90-P8, 90-P11, 90-P16, 9
- 依赖: 依赖 dependency-graph, spiral-cycle-detection；支撑 topology-skeleton, topology-coverage-verification

### 交叉审计（cross-audit）
- 类型: 操作原语
- 定义: 用独立AI实例审计另一个AI的输出——审计AI获得原始基准（JSON依赖图）和被审计输出，但不获得生成方的自审报告，保持审计独立性。说"做交叉审计"就知道要启动独立AI、给基准+输出、收审计报告。
- 验证: tested
- 来源: 71-P14, 72-P06, 72-P07, 72-P08, 72-P09, 73-P01, 73-P12, 74-P10, 75-P07, 78-P11, 
- 依赖: 依赖 role-separation；支撑 closed-loop-audit-correction

### 闭环审计修正（closed-loop-audit-correction）
- 类型: 操作原语
- 定义: 审计→发现瑕疵→结构化反馈（位置/问题/修正建议三字段）→修正→再审计→直到无瑕疵或达到最大轮数。三级终止：硬终止（瑕疵数=0）、软终止（最大轮数上限）、降级终止（超限后降级为开环模式记录残余瑕疵）。说"做闭环审计修正"就知道要跑审计循环、
- 验证: tested
- 来源: 76-P01, 76-P02, 76-P03, 76-P05, 76-P07, 76-P08, 76-P10, 76-P11, 76-P12, 76-P13, 
- 依赖: 依赖 cross-audit, certificate；支撑 pipe（作为Pipe中的质量门控环节）

### 认知检查点（cognitive-checkpoint）
- 类型: 操作原语
- 定义: 六步检查点工作流——CP1种子选择（选3-5个认知单元作为遍历起点）→CP2认知加载（AQL图遍历）→CP3缺口检查（集合差集验证覆盖）→CP4认知捕获（检查是否产生新认知）→CP5认知图更新（新增版本/新边）→CP6任务-认知映射（记录用
- 验证: tested
- 来源: 89-P11, 91-P10, 91-P11, 91-P19, 91-P26, 91-P35, 94-P28, 94-P29, 94-P30, 95-P13, 
- 依赖: 依赖 cognitive-unit, version-chain, graph-traversal-retrieval, topology-coverage-verification；支撑 data-pedestal（认知图的持续维护）

### 三层提取（three-layer-extraction）
- 类型: 操作原语
- 定义: 多遍管道从解法中提取三层知识——第一遍直接记录L1路径（具体步骤序列），第二遍AI二次分析从L1抽象出L2思维模式（弥漫性Pattern，带evidence_step溯源），第三遍AI三次分析从多个L2综合出L3范式思维（跨领域结构同构，改
- 验证: partial
- 来源: 83-P01, 83-P02, 83-P06, 83-P07, 83-P08, 83-P09, 83-P10, 83-P11, 83-P12, 83-P13, 
- 依赖: 依赖 dependency-graph（L3改变图拓扑）, version-chain（L1→v1, L2→v2, L3→v3）, pattern-recognition-engine；支撑 incremental-graph-expans

### 增量图扩展（incremental-graph-expansion）
- 类型: 操作原语
- 定义: 在已有依赖图基础上新增节点和边，保留已有子图结构不变——而非重新设计。扩展时保留已验证的节点/意识，在新上下文中复用。说"做增量图扩展"就知道要在已有图上加节点/边、标记新增vs复用、跑回归验证。
- 验证: tested
- 来源: 64-P17, 65-P01, 68-P07, 70-P16, 82-P07, 87-P15, 99-P12, 99-P15, 99-P21
- 依赖: 依赖 dependency-graph, three-layer-extraction（新发现的知识成为新节点/边）；支撑 cognitive-checkpoint（CP5认知图更新）

### 角色分离（role-separation）
- 类型: 操作原语
- 定义: meta operation（拓扑规划、拓扑验证、KC审计、分析审计）和normal operation（转译、分析）必须由不同的AI实例完成——不让被审计者同时担任审计者，避免利益冲突。meta AI不直接产出知识内容，只做结构规划和质量
- 验证: tested
- 来源: 78-P11, 86-P15, 87-P09, 87-P10, 88-P10, 88-P15, 89-P04, 89-P20, 89-P24, 91-P12, 
- 依赖: 支撑 cross-audit, closed-loop-audit-correction, classical-unfolding（meta AI做规划，normal AI做转译）


## pangu-b (35 candidates)

### 三层提取（three-layer-extraction）
- 类型: 操作原语
- 定义: 从数学解法中按三个抽象层次提取知识——L1（具体步骤/程序性知识）、L2（思维模式/可复用策略）、L3（范式思维/跨领域映射），每层比前一层更抽象、更可跨题复用。L2通过AI二次分析提取，L3通过AI三次分析提取。
- 验证: tested（POC-3验证L2/L3在远迁移中产生显著增量；但L3-2被降级为L2，说明L3标准需迭代）
- 来源: 100-P8, 105-P1, 105-P23, 105-P24, 106-P1, 106-P22, 107-P1, 108-P14, 108-P15, 108
- 依赖: 依赖 dependency-graph-storage（提取结果存入依赖图）；支撑 cross-domain-mapping-edges（L3提取产生跨领域映射边）

### A/B对照实验协议（ab-controlled-experiment）
- 类型: 操作原语
- 定义: 设置A组（无提示/无依赖图）和B组（有提示/有依赖图）两个对照组，在相同题目和相同隔离条件下并行执行，通过B组得分减A组得分计算边际增益，量化提示/检索机制的因果效果。
- 验证: tested（POC-1/3/4/5/6多次使用，是项目核心验证方法）
- 来源: 100-P15, 105-P4, 105-P8, 106-P12, 106-P15, 113-P9, 114-P1, 114-P4, 114-P6, 115-P
- 依赖: 依赖 isolation-testing-protocol（隔离环境保障对照有效性）；支撑 hypothesis-driven-validation（假设通过A/B增量验证）

### 检索管线（retrieval-pipeline）
- 类型: 操作原语
- 定义: 三级递进检索机制——第一级层次索引定位到2-5个主题，第二级语义检索返回top-20种子节点，第三级图遍历从种子扩展到200-800节点子图。根据节点总数渐进启用：小图全遍历，中图层次索引+图遍历，大图加embedding语义检索。
- 验证: partial（POC中手动替代了自动检索；253号目标是自动化此过程）
- 来源: 100-P3, 100-P17, 110-P9, 110-P11, 110-P12, 110-P13, 110-P25, 122v1-P11, 122v1-P1
- 依赖: 依赖 dependency-graph-storage（图遍历的数据源）；支撑 context-compiler（检索结果作为编译输入）；依赖 subgraph-budget-extraction（剪枝控制子图大小）

### 反应式救援（reactive-rescue）
- 类型: 操作原语
- 定义: Agent先独立尝试解题，形成自然思维轨迹，系统检测到真实停滞/卡点后才匹配启发规则并注入最小提示，从当前checkpoint继续而非从原题重做。与"主动式导航"（预先灌入全部启发）对立。
- 验证: untested（设计阶段提出，尚未实现在线运行时）
- 来源: 122v2-P34, 122v2-P35, 122v2-P37, 122v3-P09, 122v3-P14, 123-P07, 123-P30, 124-P10
- 依赖: 依赖 stagnation-detection（检测卡点才触发）；依赖 thought-trace-graph（需要T图建模Agent状态）；支撑 checkpoint-intervention（从checkpoint继续注入）

### 停滞检测（stagnation-detection）
- 类型: 操作原语
- 定义: 从Agent的外显思维轨迹中检测8种停滞信号：重复同一候选无新证据、多轮只改同一参数、发现矛盾仍沿原路、工具结果与结论冲突、子目标长期无出边、多分支回到同一卡点、预算耗尽、策略耗尽。用precision和recall衡量检测质量。
- 验证: untested
- 来源: 122v2-P36, 122v3-P37, 123-P73, 124-P07, 124-P42, 128-P11, 128-P39
- 依赖: 依赖 thought-trace-graph（从T图检测停滞）；支撑 reactive-rescue（停滞检测触发救援）

### Pattern生命周期管理（pattern-lifecycle）
- 类型: 操作原语
- 定义: 每条启发规则（Pattern）经历完整生命周期：observed（从A/B差分观察到）→candidate（已抽取为候选）→intervened（已做最小提示干预）→validated（干预验证有效）→transferred（跨题迁移验证）
- 验证: untested（生命周期框架设计完成，但尚无Pattern走完完整生命周期）
- 来源: 122v2-P31, 122v3-P06, 123-P63, 124-P33, 124-P38, 127-P34, 127-P35, 128-P35, 130-
- 依赖: 依赖 ab-controlled-experiment（干预验证）；支撑 heuristic-activation-graph（生命周期状态存储在H图中）

### Checkpoint干预（checkpoint-intervention）
- 类型: 操作原语
- 定义: 提示后必须从当前状态继续而非从原题重做。系统保存checkpoint：提示前思维图、触发模式、注入内容、提示后新增节点和边、是否越过卡点、最终结果。A/B对比时，干预组和对照组在干预点之前的状态必须等价（用checkpoint内容哈希验证）
- 验证: untested
- 来源: 122v2-P37, 123-P58, 123-P59, 124-P41, 124-P48, 128-P48
- 依赖: 依赖 event-sourcing（checkpoint从事件序列重建）；支撑 ab-controlled-experiment（checkpoint等价确保对照有效）

### 隔离测试协议（isolation-testing-protocol）
- 类型: 操作原语
- 定义: 通过物理目录隔离+AGENTS.md规则注入+tmux监督实现实验隔离：每个agent有独立工作目录（含定制AGENTS.md），AGENTS.md注入硬约束（禁止web_search、禁止访问特定目录），tmux capture-pane
- 验证: tested（POC-1/3/4/5/6均使用此协议，多维度审计验证有效）
- 来源: 116-P1, 116-P2, 116-P3, 116-P4, 116-P5, 116-P6, 116-P7, 116-P8, 116-P11, 116-P13
- 依赖: 支撑 ab-controlled-experiment（隔离保障对照有效性）

### 假设驱动验证（hypothesis-driven-validation）
- 类型: 操作原语
- 定义: 实验前预设明确假设（如H1: B>A总分, H2: B>A关键维度, H3: 意识节点泛化, H4: 方法论跨领域增益一致），每个假设有具体验证标准和阈值，实验后逐一判定（通过/部分通过/不通过），确保验证有明确目标，不事后编造解释。
- 验证: tested（POC-1/3/4/5/6均使用假设驱动验证）
- 来源: 106-P21, 113-P11, 114-P12, 115-P20, 118-P25, 119-P09, 121-P10, 121-P19, 124-P35
- 依赖: 支撑 ab-controlled-experiment（假设通过A/B增量验证）

### 盲评（blind-evaluation）
- 类型: 操作原语
- 定义: 评分者不知道哪份回答来自哪个实验组（A/B/C），消除评分者主观偏差。评分AI独立于执行组和审计组，确保评估结果的客观性。
- 验证: tested（POC-3使用盲评，由第四个独立subagent评分）
- 来源: 105-P7, 105-P21, 106-P09, 121-P08
- 依赖: 支撑 ab-controlled-experiment（盲评保障评分客观性）

### 方向性节点内容（direction-only-content）
- 类型: 操作原语
- 定义: 依赖图节点内容只能是方向性引导（"考虑X""检验Y""比较A和B"），不能是直接答案或等价答案。方向性节点采用三种形式：①适用性引导（"考虑是否适用于你的猜测"）②出发点引导（"从X出发分析"）③分解引导（"可以分解为A和B，变化的是哪一部
- 验证: tested（POC-6审计发现两个节点直接给答案导致作弊，修正后验证方向性节点有效）
- 来源: 120-P2, 120-P3, 120-P14, 121-P1, 121-P2, 121-P13, 121-P18, 121-P21, 122v3-P23, 1
- 依赖: 约束 dependency-graph-storage（节点内容必须方向性）；支撑 non-specificity（方向性内容是非特定性的具体实现）

### 子图预算提取（subgraph-budget-extraction）
- 类型: 操作原语
- 定义: 从种子节点出发图遍历提取子图，在token预算内通过多维剪枝控制子图大小：深度控制（max_depth=3避免爆炸）、宽度剪枝（每节点只保留top-K最相关邻居）、token预算剪枝（累计达70%预算时停止）、螺旋环路完整保留、跨领域边优先
- 验证: untested（设计阶段提出，POC中手动替代）
- 来源: 100-P17, 110-P12, 110-P13, 110-P20, 110-P21, 110-P27, 110-P28, 122v1-P13, 122v1-
- 依赖: 依赖 retrieval-pipeline（作为第三级图遍历的实现）；支撑 context-compiler（提取的子图作为编译输入）

### arXiv映射提升（arxiv-mapping-promotion）
- 类型: 操作原语
- 定义: arXiv论文不直接成为依赖图节点，而是作为知识节点的出处。论文按映射级别分四级：L1定理级（重要定理成为concept节点）、L2方法级（新方法成为节点）、L3意识级（思维范式成为paradigm节点）、L4未激活（论文元数据存于独立co
- 验证: partial（239K论文元数据已导入ArangoDB，但映射提升流程未自动化）
- 来源: 112-P1, 112-P2, 112-P3, 112-P9, 112-P10, 112-P11, 112-P12, 112-P13, 112-P14, 112
- 依赖: 依赖 dependency-graph-storage（提升后节点存入依赖图）；支撑 retrieval-pipeline（更多节点意味着更丰富的检索）

### 因子化模式匹配（factor-based-matching）
- 类型: 操作原语
- 定义: 将Pattern（启发规则）分解为可组合的因子（LHS匹配条件/interface绑定接口/RHS执行动作/guard前置守卫），不做全量规则扫描，而是利用稀疏性只匹配可能相关的规则子集。匹配结果不预先全部计算，而是在需要时才物化。只有高频
- 验证: untested
- 来源: 122v2-P19, 122v2-P20, 122v2-P21, 124-P15, 128-P18, 128-P19, 128-P20
- 依赖: 依赖 heuristic-activation-graph（匹配的对象是H图中的规则）；支撑 reactive-rescue（匹配结果触发干预）

### Phase门控（phase-gate）
- 类型: 操作原语
- 定义: 系统开发分为Phase 0-7共8个阶段，每个Phase有入口门和出口门。入口门确认前一Phase完成，出口门审计本Phase全部交付物（术语/字段/权限/版本规则审计、数据未变验证、架构裁决在Schema中体现），通过后才进入下一Phas
- 验证: tested（Phase
- 来源: 124-P48, 124-P53, 125-P06, 125-P07, 129-P22, 129-P30, 130-P02, 130-P03, 130-P36,
- 依赖: 支撑 legacy-freeze-adapter（Phase 0冻结旧数据后才进入Phase 1）

### Legacy冻结+只读适配器（legacy-freeze-adapter）
- 类型: 操作原语
- 定义: 旧数据（dg_nodes/dg_edges/loops）不原地清空或迁移，保留原貌作为只读历史数据。新数据写入新collection。通过只读adapter从旧数据生成候选K投影，不修改原数据。新collection用幂等、可回滚的migr
- 验证: tested（Phase
- 来源: 121-P16, 123-P67, 123-P68, 124-P44, 126-P26, 126-P32, 129-P04, 129-P28, 130-P27,
- 依赖: 依赖 phase-gate（Phase 0冻结后才进入Phase 1）

### 依赖图存储（dependency-graph-storage）
- 类型: 结构原语
- 定义: 用ArangoDB图数据库存储认知单元及其依赖关系，节点是认知单元/数学元素/思维模式，边是依赖关系。节点按type分七种（concept/domain_concept/paradigm/problem/step/substep/aware
- 验证: tested（1719个dg_nodes
- 来源: 100-P18, 100-P19, 103-P1, 103-P2, 103-P6, 103-P7, 103-P10, 104-P1, 104-P5, 104-P
- 依赖: 支撑 retrieval-pipeline（图遍历的数据源）；支撑 three-layer-extraction（提取结果存入图）；支撑 cross-domain-mapping-edges（跨领域边存储在图中）；依赖 version-ch

### 冷热温微四级存储（cold-warm-hot-micro-tiers）
- 类型: 结构原语
- 定义: 知识存储分为四层——冷存储层（全量数据，永久存储，不装入上下文，如239K arXiv论文）、温查询层（按需查询，追加到热工作集，每次返回10-50节点）、热工作集（当前问题相关200-800节点子图，装入AI上下文~80K token）、
- 验证: partial（冷层239K论文已入库，热层在POC中手动构建，温层和微层未实现）
- 来源: 110-P3, 110-P4, 110-P5, 110-P6, 110-P28, 112-P5, 122v1-P14, 122v1-P66, 128-P22, 
- 依赖: 依赖 dependency-graph-storage（热层是依赖图的子图）；支撑 subgraph-budget-extraction（预算控制在热层内）；支撑 context-compiler（编译从热层到AI上下文）

### 上下文编译器（context-compiler）
- 类型: 结构原语
- 定义: 把机器可查询的数学子图变成AI此刻能可靠使用的研究上下文。执行八步：决定节点展开顺序、决定内容分辨率、把边翻译成思考关系、保留分叉汇聚反馈环、标注事实/猜测/意识/工具/警告、记录来源、token预算删减（保留删减清单）、输出可审计的"上下
- 验证: untested（设计阶段提出，POC中用裸JSON替代编译后上下文）
- 来源: 122v1-P15, 122v1-P30, 122v1-P49, 122v1-P50, 122v1-P51, 122v1-P52, 122v1-P53, 122
- 依赖: 依赖 subgraph-budget-extraction（编译输入是提取的子图）；依赖 content-resolution-levels（编译时选择节点分辨率）；支撑 reactive-rescue（编译增量Hint注入Agent）

### 提示梯度（hint-gradient）
- 类型: 结构原语
- 定义: 建立五级提示梯度而非"有提示/无提示"二分：Hint-0元检查（"你是否只在改指数？"，泄漏风险很低）、Hint-1思维操作（"把底数和指数分开分析"，低泄漏）、Hint-2候选工具/概念（"迭代对数作为候选工具"，中等泄漏）、Hint-3
- 验证: untested（设计阶段提出，POC中用"有/无依赖图"二分替代梯度）
- 来源: 122v2-P25, 122v3-P04, 123-P70, 128-P41
- 依赖: 约束 pattern-lifecycle（Pattern的Hint级别是生命周期管理的维度之一）；支撑 minimal-knowledge-transfer（梯度从低到高实现最小知识传递）

### 外显思维图（thought-trace-graph）
- 类型: 结构原语
- 定义: 对Agent的当前思维过程建模为外显思维图T_t，从Agent独立尝试的输出中提取思维形状。节点有10种类型（observation/claim/representation/subgoal/candidate/test/tool_resu
- 验证: untested（设计阶段提出，事件捕获器未实现）
- 来源: 122v2-P07, 122v2-P09, 122v2-P10, 122v2-P11, 122v2-P12, 122v2-P38, 122v3-P03, 122
- 依赖: 依赖 event-sourcing（T图从事件序列构建）；支撑 stagnation-detection（从T图检测停滞）；支撑 factor-based-matching（T图是模式匹配的输入）

### 启发激活图（heuristic-activation-graph）
- 类型: 结构原语
- 定义: H图保存的不是数学真理也不是某次轨迹，而是经过实验验证的"触发→激活"关系。每条启发关系形式化为(LHS, Guard, RHS, η)：LHS=当前思维图中应出现的局部子图（匹配形状），Guard=上下文/时序/模型/失败类型等条件（匹配
- 验证: untested（H图设计完成，但无Pattern走完完整验证生命周期）
- 来源: 122v2-P13, 122v2-P14, 122v2-P16, 122v2-P17, 122v2-P19, 122v2-P26, 122v2-P27, 122
- 依赖: 依赖 thought-trace-graph（T图是匹配输入）；依赖 pattern-lifecycle（生命周期状态存储在H图中）；支撑 factor-based-matching（H图是匹配对象）；支撑 reactive-rescue（

### K/T/H三图分离（kth-three-graph-separation）
- 类型: 结构原语
- 定义: 系统必须维护三种不同的图：K（数学知识图——客观数学关系，定理依赖/方法适用性/推广反驳/领域对偶/工具验证能力）、T（外显思维图——实际思维轨迹，节点是事件记录而非规范知识）、H（启发激活图——条件化干预策略，"当前T出现何种模式时，应从
- 验证: untested（设计阶段提出，当前只有K图——dg_*集合）
- 来源: 122v2-P07, 122v2-P08, 122v2-P15, 122v2-P47, 122v3-P01, 122v3-P22, 123-P02, 123-P
- 依赖: 包含 dependency-graph-storage（K图的实现）；包含 thought-trace-graph（T图的实现）；包含 heuristic-activation-graph（H图的实现）

### 角色隔离矩阵（role-isolation-matrix）
- 类型: 结构原语
- 定义: 系统定义8种角色（Solver/Event Capture/State Reducer/Retriever/Heuristic Matcher/Verifier/Auditor/Orchestrator），每个角色有明确的可见性矩阵（8角色
- 验证: partial（POC中用物理目录+AGENTS.md软限制实现了简化版隔离；完整8角色矩阵未实现）
- 来源: 116-P4, 116-P5, 116-P8, 116-P16, 122v3-P05, 122v3-P39, 124-P26, 124-P27, 127-P32
- 依赖: 包含 truth-vault（角色隔离的具体应用之一）；支撑 ab-controlled-experiment（角色隔离保障实验可信度）

### 真值库（truth-vault）
- 类型: 结构原语
- 定义: 定义一个受保护的Truth Vault（真值库），存储系统确认为正确的知识（ground truth答案、正确证明路径），与可修改的启发规则隔离。只有truth_curator可写、只有auditor可读，Solver/Runner不可见。
- 验证: untested
- 来源: 122v3-P05, 122v3-P39, 124-P27, 127-P36, 129-P11, 130-P17
- 依赖: 依赖 role-isolation-matrix（角色隔离保障Truth Vault的访问控制）

### 事件溯源（event-sourcing）
- 类型: 结构原语
- 定义: 工作智能体的每次输出定义为不可变原始事件（含event_id/type/timestamp/run_id/content_hash），在RawEvent之上抽取语义事件（增加obligation_ref/evidence_ref/confl
- 验证: untested（设计阶段提出，事件捕获器未实现）
- 来源: 123-P17, 123-P18, 123-P51, 127-P07, 127-P08, 127-P09, 127-P11, 127-P12, 128-P02,
- 依赖: 支撑 thought-trace-graph（T图从事件序列构建）；支撑 checkpoint-intervention（checkpoint从事件序列重建）；支撑 state-reducer（状态从事件派生）

### 义务图（obligation-graph）
- 类型: 结构原语
- 定义: 将未完成的研究目标定义为义务节点（含status: open/discharged/suspended/failed），义务间的依赖关系用超边（非普通边）表示——AND超边要求全部前置义务达到证据门，OR超边要求任一候选达到证据门。定义10
- 验证: untested
- 来源: 123-P12, 123-P15, 123-P16, 127-P13, 127-P14, 127-P15, 127-P16, 127-P45, 128-P07
- 依赖: 依赖 event-sourcing（义务状态从事件派生）；支撑 progress-potential-function（义务完成情况决定进展势）

### 表示变换图（representation-transformation-graph）
- 类型: 结构原语
- 定义: 表示变换图的顶点是数学表示（整数方程、椭圆曲线等），边是等价/编码/归约/松弛/对偶/函子化候选。每条边必须说明输入结构、输出结构、保留量、信息损失和soundness条件。表示运输只在对应义务通过后成立。大师经常通过换语言而非在原表示中硬
- 验证: untested
- 来源: 123-P05, 123-P22, 123-P23, 127-P17, 127-P18, 127-P19, 128-P12
- 依赖: 支撑 heuristic-activation-graph（"何时换语言"的启发存储在H图中）；依赖 obligation-graph（表示运输只在对应义务通过后成立）

### 证据系统（evidence-system）
- 类型: 结构原语
- 定义: 将证据定义为多维度结构：kind（6种类型：literature/numerical/symbolic/formal_proof/counterexample/human_audit）、polarity（support/refute）、st
- 验证: untested
- 来源: 123-P52, 123-P53, 127-P20, 127-P21, 127-P22, 127-P24, 128-P08, 129-P11
- 依赖: 支撑 obligation-graph（证据门决定义务是否释放）；支撑 certificate（证据系统是证书的实现基础）

### 版本链（version-chain）
- 类型: 结构原语
- 定义: 为每个认知单元建立版本链（v1→v2→...→vN），每个版本记录summary和来源，current_version指向最新理解深度。认知单元和提取方法都有版本链——方法不是一次性设计完成的，而是在实验中不断迭代改进。新增认知单元只需在图
- 验证: partial（认知单元版本链已在ArangoDB中实现，cog_versions集合存储版本记录）
- 来源: 100-P6, 100-P7, 100-P9, 100-P16, 104-P02, 106-P19, 106-P20, 121-P16
- 依赖: 支撑 dependency-graph-storage（版本链管理图中的认知单元）；支撑 pattern-lifecycle（版本链是Pattern生命周期管理的底层机制）

### 螺旋环路（spiral-loop）
- 类型: 结构原语
- 定义: 依赖图中允许存在环路——某个节点A依赖节点B，同时节点B也依赖节点A，形成螺旋迭代关系，表示两个步骤需要相互验证、反复迭代。螺旋环路的三圈验证流程：第一圈从机制推导出猜测，第二圈用数值验证确认合理性，第三圈用约束检验确认相容性。环路在图遍历
- 验证: tested（POC-1/4/5/6中螺旋环路作为依赖图结构元素使用，B组引用了环路结构）
- 来源: 113-P6, 115-P12, 115-P32, 115-P34, 117-P13, 117-P14, 118-P19, 118-P20, 118-P21, 
- 依赖: 支撑 dependency-graph-storage（环路是图中的特殊结构）；约束 subgraph-budget-extraction（环路在剪枝时优先保留）

### 跨领域映射边（cross-domain-mapping-edges）
- 类型: 结构原语
- 定义: L3范式思维一旦被提取，不只服务于原题，而是在依赖图中增加跨领域映射边——连接不同领域的认知单元。paradigm类型节点（165个）承载跨领域映射关系，带有domains_connected字段记录跨领域连接。structural_ana
- 验证: tested（POC-3验证跨领域映射在远迁移中有效；165个paradigm节点已入库）
- 来源: 105-P16, 105-P27, 106-P05, 107-P07, 107-P08, 107-P24, 112-P22, 126-P04, 126-P10
- 依赖: 依赖 three-layer-extraction（L3提取产生跨领域边）；支撑 dependency-graph-storage（跨领域边存储在图中）；约束 subgraph-budget-extraction（跨领域边优先保留）

### 内容分辨率层级（content-resolution-levels）
- 类型: 结构原语
- 定义: 同一知识节点按详细度分为四级——R1全细节（定义+陈述+证明概要+依赖+交叉引用+思维模式，~300 token）、R2中细节（陈述+关键依赖+领域标签，~100 token）、R3轻量（定义+领域，~30 token）、R4极简（名称，~
- 验证: untested
- 来源: 110-P18, 110-P19, 122v1-P48, 122v1-P64
- 依赖: 支撑 context-compiler（编译时选择节点分辨率）；支撑 subgraph-budget-extraction（分辨率影响token预算计算）

### 状态归约器（state-reducer）
- 类型: 结构原语
- 定义: State Reducer从Event Capture捕获的事件中按明确字段规则派生工作区状态W_t（V_t/F_t/O_t/R_t/D_t/E_t）。归约操作是版本化的，不同版本的状态归约结果可追溯。W_t只能由版本化Reducer从事件
- 验证: untested
- 来源: 123-P14, 127-P52, 128-P09, 128-P23, 128-P27, 129-P31, 130-P22
- 依赖: 依赖 event-sourcing（从事件派生状态）；支撑 thought-trace-graph（T图是状态的一种投影）

### 进展势函数（progress-potential-function）
- 类型: 结构原语
- 定义: 将研究进展量化为多分量向量（目标相关已验证义务权重, -未释放义务权重, -未解决冲突数, -无证据活动候选数, -累计资源成本），按字典序比较。不同任务类型用不同进展度量：prove/refute看义务证据门与反例，construct看候
- 验证: untested
- 来源: 123-P21, 123-P31, 123-P34, 123-P56, 123-P60, 127-P05
- 依赖: 依赖 obligation-graph（义务完成情况决定进展势）；依赖 evidence-system（证据状态影响进展度量）；支撑 reactive-rescue（进展势函数决定是否干预）


## nuwa-a (33 candidates)

### 内容寻址检查点（content-addressed-checkpoint）
- 类型: 结构原语
- 定义: 用SHA-256内容哈希标识状态快照，相同内容产生相同哈希，使状态节点可去重、可精确引用、可内容寻址而非位置寻址。
- 验证: untested（设计了完整机制但未在因果实验中验证分层有效性）
- 来源: 131-P9, 131-P14, 131-P18, 133-P3-4, 134-P2, 134-P11, 136-P14, 136-P16, 139-P4, 1
- 依赖: 依赖 append-only-event-log（事件日志提供checkpoint的内容）；支撑 checkpoint-stratified-experiment（分层变量）、fork-point-detection（分叉点标识）

### 不可变事件日志（append-only-event-log）
- 类型: 结构原语
- 定义: 以append-only方式存储原始事件，每个事件通过causal_predecessors字段记录前驱形成DAG，一旦写入不可修改或删除，确保历史记录的完整性和不可篡改性。
- 验证: untested
- 来源: 131-P3, 131-P7, 131-P8, 131-P10, 131-P13, 135-P20, 139-P3, 139-P5-6, 139-P9, 140
- 依赖: 无前置依赖；支撑 content-addressed-checkpoint（checkpoint从事件流派生）、semantic-extraction（语义事件从原始事件抽取）、state-equivalence-normalization

### 能力令牌（capability-token）
- 类型: 结构原语
- 定义: 将角色的能力具体化为可携带的令牌，令牌定义角色可访问哪些collection、可见哪些visibility label、执行哪些操作；操作前验证令牌是否授权，越权时抛PermissionError。
- 验证: partial（代码已实现并集成测试通过，但未在真实多角色运行中验证隔离有效性）
- 来源: 131-P23, 134-P15, 136-P42, 139-P19-20, 140-P34, 149-P22-24, 150-P5, 151-P15, 153
- 依赖: 支撑 truth-vault-isolation（通过令牌控制答案访问）、pattern-lifecycle-gate（通过令牌控制发布权限）

### 规则生命周期门控（pattern-lifecycle-gate）
- 类型: 操作原语
- 定义: 启发规则有candidate→validated→published→retired四态生命周期，每次状态转移需满足明确条件（DYN-3因果实验+泄漏门→validated；跨3个未参与设计的问题族+2个模型版本→published；效果消
- 验证: untested（设计了完整生命周期但未在长期运行中验证状态转移的有效性）
- 来源: 133-P30-33, 134-P29-30, 136-P1-5, 136-P22, 138-P44, 148-P20-21, 149-P29-30, 149-
- 依赖: 依赖 leakage-detection（泄漏门是validated的前置条件）、migration-validation（迁移验证是published的前置条件）；支撑 sparse-matrix-activation（只有publish

### 四门泄漏检测（leakage-detection）
- 类型: 操作原语
- 定义: 通过四个独立维度检测Hint是否泄漏答案——字面答案匹配（Q中是否包含答案文本）、答案等价映射审计（Q是否等价于答案）、候选空间缩减率（Q是否大幅缩小答案空间）、盲审者恢复率（不知道答案的盲审者能否从Q恢复答案），任一超标即判泄漏。
- 验证: partial（152号给出了具体阈值并进行了pilot实验校准，但未在正式实验中验证四门联合判定的准确性）
- 来源: 133-P23, 134-P7, 136-P13, 148-P17, 149-P37, 151-P26, 152-P6-9, 152-P13, 153-P17,
- 依赖: 支撑 pattern-lifecycle-gate（泄漏门是validated的前置条件）、non-specificity（已有原语的验证机制）

### 稀疏矩阵激活（sparse-matrix-activation）
- 类型: 结构原语
- 定义: 用稀疏矩阵转置乘以状态向量计算每个规则的激活分数——a_t = W_{C,F,τ}^T * p_t，其中W是规则-条件-动作权重矩阵（7种数值维度：干预效果后验/证据运行数/迁移范围/泄漏风险/模型适用性/提示成本/历史副作用），p_t是当
- 验证: untested（公式已实现但未在真实Pattern库上验证激活排序的有效性）
- 来源: 135-P40-41, 136-P9, 138-P20-21, 149-P8-13, 150-P6, 150-P26, 154-P19-20, 155-P26-
- 依赖: 依赖 pattern-lifecycle-gate（只有published规则进入矩阵）；支撑 priority-retrieval（激活分数用于排序候选）

### 四层分级存储（layered-storage）
- 类型: 结构原语
- 定义: 将知识/Pattern存储按访问热度分为冷层（全量原始资料，默认不进上下文）、温层（按义务过滤的中间结果）、热层（当前工作台快照）、微包（单步动作所需的最小数据包），每层有独立的存储和查询接口。
- 验证: partial（代码已实现并集成测试通过，但未在真实大规模知识库上验证分层有效性）
- 来源: 135-P3-8, 140-P20, 155-P1-5, 157-P1-3, 158-P1, 160-P15
- 依赖: 依赖 capability-token（控制各角色对各层的访问权限）；支撑 priority-retrieval（分层存储是分层检索的基础）、context-compiler（微包是编译结果的交付单元）

### 五层优先检索（priority-retrieval）
- 类型: 操作原语
- 定义: 检索按五层优先级依次执行——①类型/前提可用性 → ②表示变换与领域映射 → ③图关系 → ④语义相似 → ⑤历史因果效果，每层结果按当前激活包需求过滤为最小内容，高优先级层未命中才进入下一层。
- 验证: untested
- 来源: 135-P10-11, 140-P21, 155-P7-8, 157-P4-5, 158-P2, 160-P14
- 依赖: 依赖 layered-storage（分层存储提供检索源）、representation-transport（第二层检索依赖表示映射）；支撑 context-compiler（检索结果是编译的输入）

### 表示运输（representation-transport）
- 类型: 结构原语
- 定义: 用12字段的类型化映射数据结构定义数学对象在不同表示形式之间的运输关系（6种map_type：等价/编码/归约/松弛/对偶/函子候选），运输操作只在soundness obligation通过后执行（否则抛SoundnessViolatio
- 验证: untested（数据结构已实现但未在真实跨域推理中验证运输有效性）
- 来源: 135-P14-16, 137-P1-4, 145-P21-24, 150-P12, 155-P10-11, 157-P8-11, 158-P10-11, 16
- 依赖: 支撑 priority-retrieval（第二层检索依赖表示映射）、base-change（已有原语的具体化实现）

### 停滞检测（stall-detection）
- 类型: 操作原语
- 定义: 从事件流和状态中检测7类卡点（必要探索/语义重复/矛盾未处理/工具失败/表示不合适/策略耗尽/预算耗尽），每类有判定条件，需控制误报（不把正常探索误判为停滞）和漏报。
- 验证: partial（143-P13
- 来源: 132-P17-19, 136-P23, 140-P14, 143-P12-13, 144-P4, 144-P18, 154-P23, 160-P4
- 依赖: 依赖 semantic-extraction（从语义事件流检测）、progress-partial-order（用进展偏序判断是否有实质进展）；支撑 gaming-detection（停滞检测是gaming检测的前置）

### 博弈检测（gaming-detection）
- 类型: 操作原语
- 定义: 三元判定机制检测工作智能体是否在"gaming"（假装进展而非真正推进）——（停滞词=True）AND（工具证据=False）AND（结构进展=False）三条件全部满足才判定为gaming，检测到gaming时限制奖励性帮助。
- 验证: partial（代码已实现三元判定逻辑，但未在真实gaming行为上验证检测准确性）
- 来源: 136-P23-25, 153-P5, 160-P5-8, 160-P25, 161-P15-16, 161-P45
- 依赖: 依赖 stall-detection（gaming是停滞的子类）；支撑 pattern-lifecycle-gate（gaming不一致率超阈值触发停止条件）

### 检查点分层因果实验（checkpoint-stratified-experiment）
- 类型: 操作原语
- 定义: 把同一内容哈希checkpoint视为分层变量，在每个checkpoint层内随机分配并重复多个非确定continuation，设置control/H0/H1/H2四组对照，用分层或配对统计估计ATE和异质性，而非事后讲故事。
- 验证: partial（153-P27
- 来源: 134-P2-4, 134-P17-18, 136-P18, 136-P50, 149-P4, 151-P2, 151-P19, 153-P4, 153-P9,
- 依赖: 依赖 content-addressed-checkpoint（checkpoint哈希作为分层变量）、pre-registration-gate（实验参数需预冻结）；支撑 long-term-attribution（因果效应估计是归因的基

### 预注册门（pre-registration-gate）
- 类型: 操作原语
- 定义: 在实验前冻结所有决策参数（最小实际效应δ、样本量、排除标准、区间估计方法、泄漏门阈值、复现标准），冻结后不可回改，如需调整必须产生新协议版本，防止事后合理化和p-hacking。
- 验证: partial（代码已实现冻结机制，152号给出了pilot实验校准过程，但未在正式实验中验证预注册的约束力）
- 来源: 134-P8-9, 134-P45, 136-P34, 152-P1-3, 152-P11, 153-P28-29, 161-P23-26, 161-P38, 
- 依赖: 支撑 checkpoint-stratified-experiment（实验参数需预冻结）、pattern-lifecycle-gate（验证标准需预冻结）

### 受约束多目标策略（constrained-policy）
- 类型: 操作原语
- 定义: 策略π = max_π E[ΔProgress_κ] - λ1*C_hint - λ2*L̂_answer - λ3*D̂_dependence - λ4*C_budget，在进展最大化、泄漏最小化、依赖最小化、成本控制多个约束下选择最优动
- 验证: untested（公式已定义但未在真实运行中验证策略选择的有效性）
- 来源: 136-P32-35, 149-P43, 150-P17, 153-P21, 160-P27-28, 160-P53, 161-P23-25
- 依赖: 依赖 progress-partial-order（进展度量是目标函数的第一项）、leakage-detection（泄漏度量是约束之一）、help-dependency-measurement（依赖度量是约束之一）；支撑 priority

### 长期归因（long-term-attribution）
- 类型: 操作原语
- 定义: 三步归因机制——提示链记录（完整记录从首次提示到当前进展的提示链）→ 进展归因（信用归给首次引入H关系的提示而非最近一次提示）→ 反事实估计（估计"没有该提示是否也会达到进展"），归因不确定时标注不确定而非强行归因。
- 验证: untested
- 来源: 136-P26-27, 136-P65-68, 160-P31-33, 161-P17-20, 161-P42-43
- 依赖: 依赖 checkpoint-stratified-experiment（反事实估计依赖对照组）；支撑 pattern-lifecycle-gate（归因结果是规则升级的证据）

### 上下文编译器（context-compiler）
- 类型: 结构原语
- 定义: 把检索结果编译为可增量注入的最小包（微包），每段输出带5项记录（来源/可见性/证据等级/token成本/裁剪记录），从checkpoint继续增量编译而非每次从头编译，通过冗余审计/缺失审计/预载审计三项确保上下文最小性。
- 验证: partial（代码已实现并集成测试通过，但未在真实检索场景中验证编译结果的最小性）
- 来源: 135-P17, 135-P32-34, 135-P49, 136-P49, 136-P53, 138-P4, 154-P22, 155-P12, 157-P1
- 依赖: 依赖 priority-retrieval（检索结果是编译的输入）、layered-storage（微包是分层存储的交付层）；支撑 cognitive-activation（已有原语，编译结果是激活包的具体内容）

### 深度分级验收（depth-graded-check）
- 类型: 操作原语
- 定义: 将"实现X"从二元勾选[x]/[ ]改为四元深度等级[D1]/[D2]/[D3]/[D4]/[ ]——D1定义（类型/schema存在）、D2逻辑（可执行函数）、D3测试（边界覆盖）、D4集成（上下游集成验证），强制勾选者明确实现深度，消除
- 验证: tested（在多个Phase的实现审计中验证了深度分级能有效发现"定义了=实现了"的断层）
- 来源: 140-P5-7, 142-P4, 142-P13, 146-P4, 147-P11, 147-P16, 150-P11
- 依赖: 支撑 multi-source-audit（深度分级是审计的一个维度）

### 多源交叉审计（multi-source-audit）
- 类型: 操作原语
- 定义: 用多个并行subagent分别完整扫描多个权威源文件的每一行，各自提取要求并标注来源，然后汇总做横向对照，冲突时按权威等级裁决（Schema冻结文档>架构母本>设计母本>Check List），不依赖单一文档避免盲区。
- 验证: tested（在145-162号的多轮审计中验证了多源交叉审计能发现单源审计遗漏的断层）
- 来源: 139-P25, 146-P5-6, 147-P5, 147-P28-29, 149-P44-45, 150-P1-3, 150-P28, 159-P4, 16
- 依赖: 依赖 depth-graded-check（深度分级是审计的一个维度）；无直接支撑的原语

### 状态等价规范化（state-equivalence-normalization）
- 类型: 结构原语
- 定义: 状态等价关系~_{α,κ}由任务类型κ和抽象级别α参数化，规范化键包含五个字段（开放义务的类型化同构类、当前表示ID、已验证核心中的目标相关命题ID、活动分支、证据门状态），忽略措辞/变量改名/事件时间，使结构相同但具体内容不同的状态可匹配
- 验证: untested
- 来源: 132-P24, 142-P7-10, 142-P16, 143-P24, 148-P8
- 依赖: 依赖 semantic-extraction（状态从语义事件重建）；支撑 content-addressed-checkpoint（规范化键的哈希是checkpoint标识）、fork-point-detection（分叉点检测依赖状态等价

### 进展偏序（progress-partial-order）
- 类型: 结构原语
- 定义: 进展由5个可测量分量定义的偏序P_κ(S_t)=(v_t, -o_t, -c_t, -u_t, -k_t)——v_t（已验证核心增长）、o_t（开放义务减少）、c_t（冲突减少）、u_t（不确定性减少）、k_t（卡点减少），6种任务类型分别
- 验证: untested
- 来源: 132-P22, 132-P25, 136-P36, 138-P18, 143-P22, 160-P29, 160-P64, 161-P14
- 依赖: 支撑 constrained-policy（进展是目标函数的第一项）、checkpoint-stratified-experiment（进展是效应度量的指标）、long-term-attribution（进展归因依赖进展度量）

### AND/OR义务超图（obligation-hypergraph）
- 类型: 结构原语
- 定义: 研究义务以AND/OR超图存储——超边本体存relation document，role=source/target的participant edges连接义务节点，义务有10种类型和4种状态（open/discharged/suspend
- 验证: partial（代码已实现并集成测试通过，但未在真实研究任务中验证义务图的有效性）
- 来源: 132-P7-10, 143-P9, 144-P1-2, 144-P12, 144-P23-24, 145-P12-14, 145-P51-53
- 依赖: 依赖 semantic-extraction（义务从语义事件提取）；支撑 stall-detection（开放义务减少是进展分量之一）、context-compiler（检索以当前义务为驱动）

### 证据认识状态（evidence-epistemic-state）
- 类型: 结构原语
- 定义: 证据有6种kind（literature/numerical/symbolic/formal_proof/counterexample/human_audit）、4种status（pending/active/superseded/retr
- 验证: partial（代码已实现但未在真实证据集合上验证认识状态推导的正确性）
- 来源: 132-P12-14, 132-P30, 143-P17-19, 144-P3, 145-P15-19, 145-P47-56, 158-P12
- 依赖: 支撑 certificate（已有原语，证据是证书的支撑材料）、verifier-multi-state（验证器的输出基于证据认识状态）

### 验证器六态输出（verifier-multi-state）
- 类型: 结构原语
- 定义: 验证器输出6种状态而非布尔值——proven/formally_verified/computationally_supported/numerically_tested/refuted/inconclusive，验证器只做验证不决定下一研
- 验证: partial（代码已实现但未在真实数学命题上验证6态输出的准确性）
- 来源: 135-P28-31, 144-P5, 145-P20, 150-P13, 155-P19, 157-P25-28, 158-P14, 160-P54
- 依赖: 依赖 evidence-epistemic-state（验证基于证据）、verification-routing（路由到正确的验证工具）；支撑 certificate（已有原语，验证状态是证书的status字段）

### 真理保险库隔离（truth-vault-isolation）
- 类型: 结构原语
- 定义: 将正确答案存储在隔离的collection中（Truth Vault），对Solver和Heuristic Matcher完全不可见，只有Auditor可读，通过capability token和visibility label在代码层面强
- 验证: partial（代码已实现隔离机制，但未在真实多角色运行中验证隔离不被绕过）
- 来源: 131-P24, 134-P13-14, 134-P46, 136-P46, 138-P52, 140-P13, 149-P26, 149-P28, 151-P
- 依赖: 依赖 capability-token（令牌控制访问权限）；支撑 leakage-detection（Truth Vault隔离是防泄漏的基础防线）

### 反应式救援模式（reactive-rescue-mode）
- 类型: 操作原语
- 定义: 闭环失败时退回"先观察再干预"的反应式模式，标注REACTIVE_RESCUE_MODE=True并记录5条理由，反应式是默认运行模式，主动导航需经5阶段升级路径验证后才能开启，主动优于反应式需同时满足3项（长期收益增加/独立性不恶化/泄漏
- 验证: untested
- 来源: 136-P28-31, 136-P37, 136-P40, 136-P71, 153-P35, 154-P11-12, 160-P49-50
- 依赖: 依赖 stall-detection（反应式依赖检测到停滞才干预）、gaming-detection（gaming不一致率超阈值触发回滚）；支撑 constrained-policy（反应式是策略π的默认模式）

### E-图等价饱和（e-graph-saturation）
- 类型: 结构原语
- 定义: 用e-graph（等价图）表示数学表达式的等价类——4核心组件（e-class等价类/e-node表达式节点/union-find并查集/rebuild重建），通过反复应用改写规则使等价表达式达到饱和状态，探索所有等价表示，与证明路径等价分
- 验证: partial（代码已实现简化版——只记录规则应用，不做完整模式匹配引擎）
- 来源: 137-P16-18, 140-P30, 154-P17, 163-P17-19, 164-P23, 165-P23
- 依赖: 支撑 representation-transport（等价表示间的运输依赖等价类管理）

### 轨迹对齐（trajectory-alignment）
- 类型: 操作原语
- 定义: 将推理过程的状态序列嵌入为曲线γ(t)，用4种方法计算两条轨迹的匹配度——Fréchet距离（考虑轨迹形状）、DTW动态时间规整（允许时间轴变形）、Optimal Transport最优运输、图核与图编辑距离，几何相近只作为候选检索依据不能
- 验证: partial（代码已实现但标注为"语义规格"级别——有实现但无生产依赖）
- 来源: 137-P19-22, 140-P27-28, 163-P20-22, 164-P24, 165-P16
- 依赖: 依赖 state-equivalence-normalization（轨迹对齐依赖状态规范化）；支撑 fork-point-detection（轨迹对齐可用于检测分叉点）

### 帮助依赖度量（help-dependency-measurement）
- 类型: 操作原语
- 定义: 用3个代理指标度量工作智能体对提示的依赖程度——撤掉Hint后的独立继续率（衡量是否真正启发而非替代）、同类后续状态再次求助率（衡量是否真正解决瓶颈）、单位已验证进展所需帮助量（衡量效率），超阈值触发停止条件。
- 验证: untested
- 来源: 134-P27, 136-P11-12, 149-P32-36, 151-P24, 160-P34
- 依赖: 支撑 constrained-policy（依赖度量是策略π的约束之一）、pattern-lifecycle-gate（依赖超阈值触发停止条件）

### 迁移验证（migration-validation）
- 类型: 操作原语
- 定义: 在未参与Pattern设计的迁移题上复现效果，验证Pattern的跨题泛化能力——通过集合差集计算non_design_domains = applicable_domains - design_participation_domains，
- 验证: untested
- 来源: 134-P24-26, 136-P4, 153-P11-12, 161-P1-3, 161-P10-12
- 依赖: 支撑 pattern-lifecycle-gate（迁移验证是published的前置条件）

### 语义抽取（semantic-extraction）
- 类型: 操作原语
- 定义: 从原始事件中识别命题、义务、表示、证据和拒绝分支，输出类型化语义事件（14种类型），实现从非结构化文本到结构化语义单元的转换，抽取失败时返回None不丢弃原始事件，语义事件可重新抽取。
- 验证: partial（代码已实现规则based抽取，但Krippendorff
- 来源: 131-P12, 132-P10, 139-P8, 139-P28-29, 140-P12, 143-P10-11, 143-P21
- 依赖: 依赖 append-only-event-log（从原始事件抽取）；支撑 obligation-hypergraph（义务从语义事件提取）、state-equivalence-normalization（状态从语义事件重建）、stall-d

### 验证路由（verification-routing）
- 类型: 操作原语
- 定义: 根据命题类型选择验证工具并分层路由——形式证明类→Lean 4，符号计算类→SymPy/SageMath，数值验证类→NumPy/SciPy，混合型→按验证等级分层路由（numerically_tested→computationally_
- 验证: partial（代码已实现路由逻辑但未在真实混合型命题上验证路由准确性）
- 来源: 135-P23-27, 154-P6, 154-P8, 155-P15-18, 157-P18-24, 158-P15-17, 160-P54
- 依赖: 支撑 verifier-multi-state（路由到正确的验证器才能产生正确的6态输出）、evidence-epistemic-state（工具输出经确认后成为证据）

### 分叉点检测（fork-point-detection）
- 类型: 操作原语
- 定义: 在成功运行和失败运行中找到都经过的checkpoint（稳定共同状态），然后检测在哪个checkpoint开始分叉——分叉点是"此刻需要干预"的精确位置，记录分叉点的状态特征（卡点类型/开放义务/表示/证据状态）作为Pattern触发条件的
- 验证: untested
- 来源: 133-P5-7, 148-P9-11, 148-P7-8
- 依赖: 依赖 content-addressed-checkpoint（checkpoint哈希用于对齐）、state-equivalence-normalization（状态等价比较用于检测分叉）；支撑 sparse-matrix-activat

### 大师启发库（master-heuristics-library）
- 类型: 结构原语
- 定义: 6条可识别和标注的大师启发式策略——①把无结构整数反例编码成更富结构的几何对象；②把存在性问题改成两个理论的不相容性问题；③在椭圆曲线/Galois表示/模形式之间换语言；④沿等价关系把问题运输到另一个空间；⑤用降层把无穷化为有穷；⑥寻找不
- 验证: untested
- 来源: 137-P8, 159-P17, 163-P45, 164-P28
- 依赖: 支撑 representation-transport（大师启发包含换基和运输策略）、base-change（已有原语，大师启发是换基的具体策略）


## nuwa-b (29 candidates)

### 三层存储（three-layer-storage）
- 类型: 结构原语
- 定义: 将Pattern/知识存储分为热层（实时状态快照）、温层（按当前义务过滤的中频Pattern）、冷层（全量历史底层仓库），三层有不同的更新策略和查询方式，检索时逐层递进。
- 验证: untested
- 来源: 183-P08, 183-P09, 183-P10, 183-P11, 190-P07, 190-P09, 190-P28, 190-P29, 190-P30,
- 依赖: 依赖 data-pedestal（存储基础设施），支撑 five-layer-retrieval-priority（分层检索的存储后端）

### 规则生命周期（rule-lifecycle）
- 类型: 结构原语
- 定义: 启发规则/Pattern从candidate（候选/测试中）→validated（因果实验+泄漏门通过）→published（跨问题族复现通过）→retired（退役），只有published状态的规则参与在线匹配，状态转移需满足明确条件并
- 验证: untested
- 来源: 176-P04, 176-P05, 176-P06, 183-P16, 189-P03, 189-P10, 189-P15, 189-P16, 189-P17,
- 依赖: 依赖 certificate（状态转移需审计链），支撑 pattern-recognition-engine（只匹配published规则）

### 角色隔离矩阵（role-isolation-matrix）
- 类型: 结构原语
- 定义: 通过可见性标签（visibility label，角色×collection的权限矩阵）和能力令牌（capability token，collection级/字段级/写入/运行隔离/自动失效的访问控制）双重机制，在代码层面强制执行角色间的信
- 验证: untested
- 来源: 176-P07, 176-P08, 176-P09, 191-P07, 193-P10, 193-P11, 193-P12, 193-P13, 193-P14,
- 依赖: 依赖 data-pedestal（collection定义），支撑 pipe（角色间信息隔离是Pipe合法性的保障）

### Gaming检测（gaming-detection）
- 类型: 操作原语
- 定义: 通过三元AND逻辑检测工作智能体是否在"钻空子"（假装进展而非真正进展）——停滞词出现 AND 工具使用证据缺失 AND 结构进展缺失，三者合取才判定为gaming，检测到时限制奖励/帮助。
- 验证: untested
- 来源: 175-P12, 185-P03, 185-P14, 185-P15, 185-P16, 185-P17, 185-P18, 188-P32, 198-P04
- 依赖: 支撑 constraint-solver-engine（gaming检测结果影响动作选择）

### 卡点检测与环路判别（stall-detection）
- 类型: 操作原语
- 定义: 检测工作智能体是否卡住，分为7种互斥卡点类型（必要探索/语义重复/矛盾未处理/工具阻塞/表示不合适/策略耗尽/预算耗尽），并区分两种环路——平面环路（真正的停滞）和螺旋上升环路（表面重复但有实质进展），客观证据优先于主观自报。
- 验证: untested
- 来源: 176-P20, 183-P38, 192-P07, 192-P08, 192-P09, 192-P10, 192-P11, 192-P12, 198-P03,
- 依赖: 支撑 safe-first-step（solo explore后检测卡点才给hint），依赖 state-reconstruction（需要状态归约结果做判别）

### AND/OR义务超图（obligation-hypergraph）
- 类型: 结构原语
- 定义: 研究义务以AND/OR超图存储——AND超边要求全部前置义务满足才释放，OR超边要求任一前置义务满足就释放，超图必须是DAG（检测自环/双向往返/强连通分量），表达比简单依赖更丰富的逻辑关系。
- 验证: untested
- 来源: 188-P06, 188-P22, 188-P23, 188-P24, 188-P25, 188-P26, 183-P28, 175-P02
- 依赖: 依赖 data-pedestal（ArangoDB存储），支撑 state-reconstruction（义务图是重建状态的7个字段之一）

### 证据状态模型（evidence-state-model）
- 类型: 结构原语
- 定义: 每个命题有证据状态，通过按polarity（支持/反驳）统计派生出4种认识状态（无决定性/仅支持/仅反驳/支持与反驳并存），冲突时不爆炸到全局只生成局部澄清义务，证据有生命周期（active/superseded/retracted），只有
- 验证: untested
- 来源: 188-P07, 188-P27, 188-P28, 188-P29, 192-P06, 183-P29, 175-P27, 192-P03, 192-P04
- 依赖: 支撑 verification-gate（只有满足证据条件的命题才能提升到V_t）

### 验证门（verification-gate）
- 类型: 结构原语
- 定义: 将工作区状态分为V_t（已验证区）和F_t（未验证区）两个严格分离的区域，只有满足验证门的命题（gate_passed=True且有evidence_refs）才能从F_t提升到V_t，refute_only或mixed的命题不能提升，临时
- 验证: untested
- 来源: 188-P09, 188-P30, 188-P36, 188-P37, 188-P38, 188-P39, 183-P31, 188-P57
- 依赖: 依赖 evidence-state-model（验证门的准入条件依赖证据状态），支撑 state-reconstruction（V_t/F_t是重建状态的字段）

### 事件流状态重建（state-reconstruction）
- 类型: 操作原语
- 定义: 工作区状态W_t不是直接读取的，而是由版本化Reducer从事件流（event stream）归约出来——同一事件流+同一Reducer版本必须得到相同结果，状态只能通过Reducer派生不能直接修改，多观察者交叉验证通过Krippendo
- 验证: untested
- 来源: 188-P01, 188-P02, 188-P13, 188-P14, 188-P15, 188-P16, 188-P17, 188-P40, 188-P48,
- 依赖: 依赖 obligation-hypergraph（义务图是重建状态字段），支撑 stall-detection（卡点检测需要重建状态）

### 偏序进展度量（progress-measurement）
- 类型: 操作原语
- 定义: 进展以偏序关系度量（不是所有状态之间都有可比性），进展向量比较产生4种结果（improved/worsened/equal/incomparable），状态等价判定使用规范化键（忽略措辞/变量改名/事件时间，只比较结构本质），不同任务的进展
- 验证: untested
- 来源: 188-P03, 188-P04, 188-P18, 188-P19, 188-P20, 188-P21, 183-P27, 174-P16
- 依赖: 依赖 state-reconstruction（需要重建状态才能比较），支撑 constraint-solver-engine（进展度量是多目标公式的输入）

### 盲评（blind-evaluation）
- 类型: 操作原语
- 定义: 通过打乱运行顺序、隐藏处理组标签，使评分者在评分时不知道哪些run接受了哪些Hint，评分完成后揭晓标签并检查盲评完整性（猜对率<0.5则盲评有效），消除评分偏差。
- 验证: untested
- 来源: 193-P06, 193-P08, 193-P09, 193-P35, 183-P42
- 依赖: 支撑 audit-standard-backtesting（盲评是审计标准验证的方法之一）

### 五层检索优先级（five-layer-retrieval-priority）
- 类型: 操作原语
- 定义: 检索按5层优先级顺序逐层递进——类型/前提→表示变换→图关系→语义相似→历史因果，不允许跳层，确保最相关的Pattern优先被提取，只有第4层是语义相似（embedding匹配），不把检索简化为单一embedding匹配。
- 验证: untested
- 来源: 166-P08, 183-P06, 190-P03, 190-P18, 190-P46, 190-P19
- 依赖: 依赖 three-layer-storage（分层检索的存储后端），支撑 pattern-recognition-engine（检索结果供匹配器使用）

### 上下文编译（context-compilation）
- 类型: 操作原语
- 定义: 将工作智能体的推理输出、累积context、题目本身编译为结构化的上下文表示，每段上下文携带5项元数据（source/visibility/evidence_level/token_cost/pruning_record），从checkpo
- 验证: untested
- 来源: 183-P33, 191-P01, 191-P02, 191-P03, 191-P04, 191-P05, 191-P06, 191-P09, 191-P23,
- 依赖: 依赖 backtrack-fresh-session（从checkpoint继续），支撑 minimality-audit（编译后的上下文是审计对象）

### 最小性审计（minimality-audit）
- 类型: 操作原语
- 定义: 对编译后的上下文进行三项审计——冗余检查（每段内容是否被当前open义务直接需要）、缺失检查（必要内容是否就位）、预载检查（是否预载了未来答案路线，预载是error级违规），确保上下文既不冗余也不缺失。
- 验证: untested
- 来源: 176-P28, 183-P34, 191-P10, 191-P11, 191-P12, 191-P13, 191-P14, 191-P15, 191-P16
- 依赖: 依赖 context-compilation（审计对象是编译后的上下文），支撑 implicit-filtering（预载检查是泄漏检测的一部分）

### 多类型预算硬约束（budget-management）
- 类型: 结构原语
- 定义: 系统管理多种独立预算类型（token/计算/工具/分支/Hint），每种预算对应不同资源维度，每次消耗前检查剩余预算，超限时触发硬性停止（不可绕过），Hint预算单独追踪不与其他预算混用，预算消耗记录为可审计的四元组（时间/类型/数量/原因
- 验证: untested
- 来源: 186-P01, 186-P02, 186-P06, 186-P07, 186-P08, 186-P09, 186-P17, 185-P08, 188-P33,
- 依赖: 支撑 constraint-solver-engine（预算约束是多目标公式的约束条件），支撑 dfs-guidance（branch预算限制DFS分支因子）

### 预注册因果实验（pre-registered-causal-experiment）
- 类型: 操作原语
- 定义: 在实验执行前预先注册实验设计（假设、指标、阈值），用ATE（平均处理效应）+CI下界（置信区间下界）+passes_exit_gate三步验证因果效应，用Bootstrap方法计算置信区间（不假设正态分布），关键参数通过pilot实验估计方
- 验证: untested
- 来源: 174-P05, 174-P25, 174-P08, 175-P34, 175-P35, 175-P36, 175-P38, 174-P09, 174-P21
- 依赖: 支撑 rule-lifecycle（因果实验通过是规则从candidate升级到validated的条件）

### Phase门控（phase-gate）
- 类型: 结构原语
- 定义: 每个Phase有入口门（确认前一Phase完成）和出口门（审计本Phase交付物），前Phase出口门是后Phase入口门，形成Phase间的门控链条，未通过出口门的Phase产出不应被后续Phase使用，跨Phase复用模块时来源Phas
- 验证: untested
- 来源: 174-P04, 174-P27, 175-P37, 175-P23, 174-P28
- 依赖: 支撑 execution-contract（Phase门控是执行契约的验证机制）

### 设计降级检测（design-degradation-detection）
- 类型: 操作原语
- 定义: 检测方案声明了某设计决策但实现降级了的情况（如声明用真实LLM但用Mock、声明"必须"但降为"可选"、前置条件未满足时强行实现后续组件），检测方法是将方案声明与实现代码逐项核对，降级本身可能合理但必须在状态声明中明确标注。
- 验证: untested
- 来源: 174-P31, 175-P21, 177-P06, 177-P07, 177-P11, 177-P18, 177-P27, 177-P36, 173-P02,
- 依赖: 支撑 audit-standard-backtesting（设计降级是审计维度之一）

### 审计标准回测（audit-standard-backtesting）
- 类型: 操作原语
- 定义: 用已知结果的历史run验证审计标准/机制能否正确发现问题和正确判定通过——用已知失败的run验证召回率，用已知通过的run验证精确率，回测中发现的未知问题也需记录，回测→发现缺陷→修订标准→再回测形成持续改进循环。
- 验证: untested
- 来源: 196-P01, 196-P06, 196-P07, 196-P08, 196-P28, 197-P24, 199-P18, 199-P16, 199-P20,
- 依赖: 依赖 design-degradation-detection（回测需要检测标准是否能发现降级）

### 三层轨迹记录（three-layer-trajectory-recording）
- 类型: 结构原语
- 定义: 将运行过程分为三层独立记录——外部层（devin cli轨迹：对话流/工具调用/终端输出）、中间层（系统内部执行日志：12步每步的输入/输出/中间状态）、内部层（思路轨迹：AI的thinking字段推理过程），三层通过run_id+sess
- 验证: untested
- 来源: 178-P02, 178-P03, 178-P04, 178-P05, 178-P17, 178-P18, 178-P19, 179-P14, 181-P03,
- 依赖: 支撑 audit-standard-backtesting（回测需要三层轨迹数据）

### 激活分数计算（activation-score-computation）
- 类型: 操作原语
- 定义: 在H图稀疏表示上计算候选激活分数 a_t = W^T * p_t，其中W是权重向量（组合权重=干预效果后验×0.4+模型适用性×0.3-泄漏风险×0.2-提示成本×0.1），p_t是当前状态在稀疏矩阵中的投影，激活分数作为候选Pattern
- 验证: untested
- 来源: 166-P16, 175-P43, 189-P08, 189-P43, 190-P06, 189-P41, 189-P42
- 依赖: 依赖 cognitive-activation（激活分数是认知激活的计算机制），支撑 pattern-recognition-engine（排序候选Pattern）

### Legacy标记（legacy-marking）
- 类型: 操作原语
- 定义: 系统演化过程中，旧的概念和流程被显式降级为legacy（如七步骤工作流、6步提取流程），用新机制替代而非直接删除，legacy内容通过只读adapter访问（不修改原始数据），确保新旧系统可以共存而不会互相污染。
- 验证: untested
- 来源: 166-P35, 166-P22, 174-P12, 175-P10, 176-P10, 183-P14, 190-P04, 190-P47
- 依赖: 支撑 three-layer-storage（legacy图通过只读adapter接入新检索系统）

### 微包（micro-package）
- 类型: 结构原语
- 定义: 微包是检索返回的基本单元——包含完成一个研究动作所需的定义、接口、工具或Hint，是Pattern的封装形式，每轮增量注入Solver上下文（不一次性全部注入），不预载未来路线，过滤完整解法/最终答案等预载关键词，确保检索结果既足够使用又不
- 验证: untested
- 来源: 183-P07, 190-P10, 190-P20, 190-P32, 190-P33, 190-P34
- 依赖: 依赖 minimal-knowledge-transfer（微包是最小知识传递的封装形式），支撑 pipe（微包是Pipe间传递的数据单元）

### 表示映射（representation-map）
- 类型: 结构原语
- 定义: 表示映射提供从一种数学表示到另一种表示的链式查找能力（find_chain），有6种map_type，每种映射有运输条件（前置义务）——只有运输条件满足时映射才有效，普通跨领域边不自动成为表示变换需要显式声明，支持按关系类型独立检索。
- 验证: untested
- 来源: 176-P19, 183-P12, 190-P11, 190-P23, 190-P35, 190-P36, 190-P37, 190-P38
- 依赖: 支撑 five-layer-retrieval-priority（表示变换是第2层检索）

### K/T/H投影（kth-projection）
- 类型: 结构原语
- 定义: 将认知图中的内容按三种知识层次投影——K=知识（定理/定义/公式）、T=技巧/思维模式（跨题复用）、H=启发式/Hint（跨领域复用），三种投影是查询视图而非独立权威真相库（不把投影当知识库），检索时按K/T/H分别查询，K投影按5种关系矩
- 验证: untested
- 来源: 174-P13, 175-P08, 183-P13, 190-P05, 190-P23, 190-P24, 171-P21, 172-P14
- 依赖: 依赖 data-pedestal（投影从已有collection查询），支撑 five-layer-retrieval-priority（K/T/H是检索的查询对象）

### 冻结状态强制（frozen-state-enforcement）
- 类型: 结构原语
- 定义: 核心数据用frozen dataclass声明不可变性，状态只能通过版本化Reducer派生不能直接修改，需要更新时用replace()创建新实例，冻结检查不只执行一次而是每次读取字段时持续验证，只读访问通过深拷贝+内容哈希校验防止外部修改
- 验证: untested
- 来源: 176-P01, 176-P03, 176-P11, 176-P12, 176-P15, 188-P40, 187-P10, 187-P15, 187-P17,
- 依赖: 依赖 certificate（内容哈希是冻结验证的机制），支撑 state-reconstruction（冻结状态是确定性重建的前提）

### 验证路由（verification-routing）
- 类型: 操作原语
- 定义: 按命题级别将不同类型的验证请求路由到不同的验证器——formal_proof→Lean 4、symbolic→SymPy/SageMath、numerical→NumPy/SciPy、human_audit→人工，混合型按等级从低到高分层路
- 验证: untested
- 来源: 183-P39, 192-P13, 192-P14, 192-P15, 192-P16, 192-P18, 192-P19, 192-P20, 192-P21,
- 依赖: 依赖 evidence-state-model（验证结果更新证据状态），支撑 verification-gate（验证路由的结果决定命题能否进入V_t）

### 优化决策归因（optimization-attribution）
- 类型: 操作原语
- 定义: 将运行未达预期的原因分为7种互斥类型（数据问题/机制问题-匹配/机制问题-状态/提示问题/能力问题/预算问题/停止条件问题），每种有对应的优化行动和验证方式，形成"审计→归因分析→记录优化决策→下次run验证"的闭环。
- 验证: untested
- 来源: 178-P29, 178-P30, 178-P31, 178-P32, 178-P33, 178-P44, 178-P45, 182-P16, 182-P17,
- 依赖: 依赖 three-layer-trajectory-recording（归因分析需要三层轨迹数据），支撑 audit-standard-backtesting（归因结果验证标准有效性）

### 逐步验证标注（step-by-step-verification）
- 类型: 操作原语
- 定义: 让审计AI对证明的每一步进行逐步标注——OK（正确，附依据）、ERROR（错误，附原因）、SKIP（跳步，附缺失推理），形成完整的推理状态图谱，验证方法分三层（自动化首选/AI辅助/人工复杂情形），数学任务分类型适用不同检查项集。
- 验证: untested
- 来源: 195-P25, 195-P26, 195-P04, 195-P05, 195-P06, 195-P07, 195-P08, 195-P10, 195-P11,
- 依赖: 支撑 verification-routing（逐步标注是验证的具体执行方式）


## suiren (32 candidates)

### 四门泄漏审计（four-gate-leak-audit）
- 类型: 操作原语
- 定义: 在提示/检索结果发送给工作智能体之前，依次通过四道独立审计门——字面匹配、等价映射、候选空间缩减、盲恢复——任何一门FAIL则提示被拒绝并降级为meta级提示，实现泄漏的自动化拦截。
- 验证: partial（209号报告泄漏率从40%降到20%，但用历史run回测而非前瞻实验）
- 来源: 200-P4, 200-P5, 200-P6, 200-P7, 200-P8, 200-P10, 200-P31, 203-P2, 203-P3, 203-P4
- 依赖: 依赖 answer-isolation（需要truth_vault中的答案做比对）；支撑 ai-hint-compilation（审计AI编译的提示）；组合 hint-grading（分级标注为审计提供元数据）

### 状态归约（state-reduction）
- 类型: 操作原语
- 定义: 把Solver的自然语言+数学公式输出归约为结构化状态（开放义务V_t/已验证命题F_t/当前表示O_t三个维度），为后续的卡点诊断、模式匹配和决策提供结构化输入。
- 验证: untested
- 来源: 200-P18, 202-P03, 205-P27
- 依赖: 支撑 stall-diagnosis（归约结果供卡点诊断）；支撑 rule-base-matching（归约结果供规则匹配）；支撑 exploration-map（归约结果构建探索地图）

### 卡点诊断（stall-diagnosis）
- 类型: 操作原语
- 定义: 分析Solver卡住的原因，归类为7种预定义类型（必要探索、语义重复、矛盾未处理、工具阻塞、表示不合适、策略耗尽、预算耗尽），每种类型有对应的检测方法，为模式匹配提供分类索引。
- 验证: untested
- 来源: 200-P19, 202-P04, 205-P1, 205-P22, 209-P16, 210-P2
- 依赖: 依赖 state-reduction（需要归约状态作为输入）；支撑 rule-base-matching（诊断结果驱动规则匹配）；支撑 ai-on-demand-intervention（不确定时触发AI介入）

### 提示分级（hint-grading）
- 类型: 操作原语
- 定义: 将每条提示按知识含量分为三级——knowledge（给具体数学事实）、strategy（给解题方向/方法选择）、meta（给元提示如"继续/更详细"）——并在结果文件中记录级别，为提示质量评估和泄漏审计提供元数据。
- 验证: untested
- 来源: 200-P25, 203-P1, 206-P1, 206-P2, 209-P2, 209-P23, 213-P8
- 依赖: 支撑 four-gate-leak-audit（分级为审计提供元数据）；支撑 gain-attribution（分级使增益来源可分解）；与 minimal-knowledge-transfer 关联（Level值与分级相关但不同——Leve

### 增益归因（gain-attribution）
- 类型: 操作原语
- 定义: 记录每条提示发出后Solver的进展改善，并将改善归因为思路（策略选择）、知识（具体事实）或答案等价信息三类之一，判断提示的有效性来源，使提示的有效性可审计、可分解。
- 验证: untested
- 来源: 200-P12, 203-P13, 203-P14, 213-P13
- 依赖: 依赖 hint-grading（分级使归因可分解）；支撑 three-group-control-experiment（归因需要实验设计验证）

### 三组对照实验（three-group-control-experiment）
- 类型: 操作原语
- 定义: 设计三组对照实验——A组无提示、B组完整提示、C组去掉答案等价信息的提示——对比三组表现差异，判断增益来源：C≈A则降级（增益来自知识=作弊），C≈B则非作弊，A<C<B则需细分。
- 验证: untested
- 来源: 200-P28, 203-P14, 206-P8, 206-P9
- 依赖: 依赖 gain-attribution（实验结果用于归因）；依赖 hint-grading（C组需要去掉特定级别的提示）

### AI按需介入与降级（ai-on-demand-intervention）
- 类型: 操作原语
- 定义: AI不是每步都调用（太昂贵），而是在经典计算给出不确定结果时才按需介入——判定标准是多个候选置信度接近（max_confidence_diff < 0.2）。当AI不可用（预算耗尽或超时）时，系统降级到经典计算的默认选择，保证确定性始终可用
- 验证: untested
- 来源: 202-P19, 202-P20, 202-P21, 202-P22, 202-P23, 202-P24, 205-P8, 205-P21, 205-P30, 
- 依赖: 依赖 ai-budget-constraint（预算约束控制调用频率）；依赖 stall-diagnosis（诊断不确定性触发介入）；支撑 ai-hint-compilation（介入后执行AI编译）

### AI预算约束（ai-budget-constraint）
- 类型: 操作原语
- 定义: 为AI调用设定预算约束——每个run最多调用AI 5次、每次最多2000 token、60秒超时——用预算上限控制成本和延迟，预算耗尽时fallback到经典计算。
- 验证: untested
- 来源: 205-P29, 208-P25, 208-P26, 208-P27
- 依赖: 支撑 ai-on-demand-intervention（预算约束是按需介入的配套）

### 形状匹配（shape-matching）
- 类型: 操作原语
- 定义: 提示触发不基于"这道题能不能用某模式"（适用性太宽泛），而基于"当前卡点的形状是否匹配该模式曾经成功突破过的形状"——基于问题的结构特征、解答的转折结构、思维的拓扑来匹配候选Q，而非基于文本相似性或关键词匹配。
- 验证: untested
- 来源: 214-P6, 214-P7, 214-P11, 214-P12, 215-P11, 216-P26
- 依赖: 依赖 safe-first-step（形状描述来自安全第一步）；支撑 rehearsal（预演中用形状匹配生成候选Q）；与 ultimate-hint-set 组合（提示集合提供候选，形状匹配选择候选）

### 预演（rehearsal）
- 类型: 操作原语
- 定义: 已知答案倒推提示序列——给定题目和答案，生成模拟QA序列和极致提示集合，产出落盘到rehearsal.md。实际引导时读取rehearsal.md获取候选提示，不把所有提示放在Skill/上下文中。
- 验证: untested
- 来源: 216-P17, 216-P39, 217-P4
- 依赖: 依赖 shape-matching（预演中用形状匹配生成候选Q）；支撑 continuous-questioning（预演产出供连续发问使用）；支撑 dfs-guidance（预演产出候选Q列表供DFS使用）

### 质量审计（quality-audit）
- 类型: 操作原语
- 定义: 对知识提取结果进行质量审计——由AI审计L2是否真弥漫性、L3是否真改变图结构、L4是否真有洞察力。审计通过则存储，审计不通过则退回重提取或人工审核，形成反馈循环。
- 验证: partial（POC3中L3有1条通过1条不通过，验证了审计方法可复用）
- 来源: 201-P10, 204-P6, 204-P7, 204-P18, 207-P10, 207-P11
- 依赖: 支撑 knowledge-absorption-pipeline（审计是pipeline的质量门控）；依赖 four-layer-knowledge-structure（各层有不同的质量判据）

### 多次独立验证（multiple-independent-verification）
- 类型: 操作原语
- 定义: 通过多次（≥3次）独立运行判定结果是稳定的还是偶然的——3次全错才算"做不出来"，1次对需扩大样本到5次。用独立于AI的机制（SymPy/Lean）验证结果正确性，不能只看"AI说自己做对了"。
- 验证: tested（在MathArena
- 来源: 210-P4, 210-P27, 211-P19, 211-P21, 212-P21
- 依赖: 支撑 false-completion-detection（多次运行可发现假完成）；支撑 training-data-risk-assessment（多次验证确定AI是否真会）

### 文件传递隔离（file-transfer-isolation）
- 类型: 操作原语
- 定义: 将题目和提示通过文件（problem.txt/hint.txt）传递而非命令行参数，文件作为工作智能体状态的物质化载体。每个turn使用全新session（会话隔离），但将上一轮解答摘要写入hint.txt传递给下一轮，实现隔离下的状态延续
- 验证: tested（guided_001/003实验中已使用problem.txt传递题目）
- 来源: 213-P3, 213-P4, 215-P8, 217-P18
- 依赖: 支撑 solver-role-isolation（文件传递隔离了题目与系统规则）；与 backtrack-fresh-session 组合（新session中通过文件传递状态）

### 训练数据风险评级（training-data-risk-assessment）
- 类型: 操作原语
- 定义: 为每道题评估AI训练数据风险等级（高/中/低），基于时间新旧（2024-2025>2020-2023>2020前）、语言（非英文>英文）、讨论热度（少>多）三个信号综合判断。优先选择AI训练数据中不太可能包含的内容。
- 验证: tested（在MathArena
- 来源: 210-P10, 211-P4, 211-P8, 211-P14, 211-P15
- 依赖: 支撑 dataset-metadata-management（风险评级是元数据的一部分）

### 假完成检测（false-completion-detection）
- 类型: 操作原语
- 定义: AI可能给出错误证明但自认为完成——需要实验后对照标准答案验证，记录"假完成"情况。用独立于AI的机制（SymPy数值验证+人工抽查证明过程）检测假完成。
- 验证: tested（MathArena
- 来源: 210-P5, 215-P25
- 依赖: 依赖 multiple-independent-verification（多次运行帮助发现假完成）

### ABSTAIN动作（abstain-action）
- 类型: 操作原语
- 定义: 策略π的9种动作之一——什么都不做，不发提示。当没有合适的Pattern或发提示的风险大于收益时，选择不干预。不是每次都必须发提示，可以选择ABSTAIN。
- 验证: untested
- 来源: 200-P23, 200-P24
- 依赖: 支撑 rule-base-matching（ABSTAIN是规则匹配的一种动作输出）；与 four-gate-leak-audit 关联（审计失败时可选择ABSTAIN而非降级）

### AI编译提示（ai-hint-compilation）
- 类型: 操作原语
- 定义: 在经典计算生成提示骨架后，调用AI优化提示——AI编译是对经典计算提示的二次加工，不是从零生成。AI编译时遵循分级优先级（优先给strategy，其次meta，最后knowledge），且方向规划（该往哪个方向引导）和内容生成（具体说什么）
- 验证: untested
- 来源: 205-P24, 205-P25, 205-P28, 205-P33, 205-P34, 205-P40, 208-P11, 208-P12, 208-P13,
- 依赖: 依赖 ai-on-demand-intervention（AI编译是AI介入的具体执行）；依赖 state-reduction（需要Solver状态作为输入）；支撑 four-gate-leak-audit（AI编译的提示需经审计）；与 h

### 门控工作流（gate-controlled-workflow）
- 类型: 操作原语
- 定义: 每个功能模块定义入口门（前置条件满足才进入）、出口门（完成条件满足才退出）、停止条件（特定结果触发降级停止），形成工作流门控。模块之间有显式的前置依赖关系，必须按序完成。
- 验证: untested
- 来源: 206-P11, 207-P32, 208-P1, 208-P2
- 依赖: 支撑 knowledge-absorption-pipeline（门控控制pipeline各阶段）；支撑 four-gate-leak-audit（审计是提示发送的出口门）

### 过程性模式标注（process-level-annotation）
- 类型: 操作原语
- 定义: 模式提取不是在解答末尾总结性标注"此题用了反证法"，而是在解答的每个关键转折点标注"这里从正面假设转向了反面假设"——是过程性的、粒度到转折点的，需要AI的洞察力。
- 验证: untested
- 来源: 214-P8
- 依赖: 支撑 knowledge-absorption-pipeline（过程性标注是L2提取的方法）；支撑 shape-matching（转折点标注提供形状信息）

### 跨case语义搜索（cross-case-semantic-search）
- 类型: 操作原语
- 定义: 从历史QA树中检索"和当前题形状相似的题，成功路径是什么"——通过跨case的语义搜索实现知识转移，积累100+个case后才需要。
- 验证: untested（明确提出"积累100+个case后才需要"）
- 来源: 214-P22, 214-P29
- 依赖: 依赖 immutable-event-stream（需要历史QA树存储）；依赖 shape-matching（用形状相似度搜索）

### 答案隔离（answer-isolation）
- 类型: 结构原语
- 定义: 将标准答案存储在独立的truth_vault collection中，仅auditor角色可读，Controller/Matcher/Solver均不可读。为系统中所有collection定义角色-数据的可见性矩阵，精确控制每个角色能读/不
- 验证: untested
- 来源: 200-P2, 200-P3, 200-P32, 203-P9, 203-P10, 203-P11, 203-P12, 203-P18, 206-P5, 206
- 依赖: 支撑 four-gate-leak-audit（审计需要truth_vault中的答案做比对）；与 pipe 关联（可见性矩阵定义了Pipe的输入边界）

### 探索地图（exploration-map）
- 类型: 结构原语
- 定义: 将Solver已经探索的知识节点、方法、方向、失败路线、当前位置表示为一个结构化的"探索地图"（5字段：explored_nodes/explored_methods/explored_directions/failed_routes/cu
- 验证: untested
- 来源: 205-P13, 205-P14, 205-P15, 205-P16, 205-P27, 208-P18, 208-P19, 208-P20, 208-P21
- 依赖: 依赖 state-reduction（归约结果构建地图）；支撑 ai-hint-compilation（地图供AI规划方向）

### 四层知识结构（four-layer-knowledge-structure）
- 类型: 结构原语
- 定义: 知识按抽象度分为四层——L1（基础事实/技能，图边）、L2（思维模式/意识节点，图节点）、L3（跨领域映射，跨领域边）、L4（哲学洞察，图节点）——每层有不同的提取prompt和质量标准，映射到ArangoDB稀疏矩阵K维度的不同存储结构。
- 验证: partial（POC3中验证了L2/L3提取方法，但四层完整结构未验证）
- 来源: 201-P1, 201-P2, 201-P3, 201-P4, 201-P5, 204-P1, 204-P2, 204-P8, 204-P31, 204-P32
- 依赖: 支撑 knowledge-absorption-pipeline（四层是pipeline的提取目标）；与 level-spectrum 关联（Level连续谱是四层结构的连续化）

### 知识吸收pipeline（knowledge-absorption-pipeline）
- 类型: 结构原语
- 定义: 一个标准化的知识吸收流程接口，将原始数学内容到存储的知识转化过程封装为pipeline：AI阅读理解→L1提取→L2提取→L3提取→L4提取→质量审计→存储。每步有明确的输入输出，前段通过才进入后段（门控关系）。每次吸收新内容时自动触发，不
- 验证: untested
- 来源: 201-P13, 201-P25, 204-P3, 204-P16, 204-P26, 207-P1, 207-P2, 207-P3
- 依赖: 包含 four-layer-knowledge-structure（四层是提取目标）；包含 quality-audit（审计是pipeline的质量门控）；依赖 gate-controlled-workflow（门控控制各阶段）

### 四路径数据捕获（four-path-data-capture）
- 类型: 结构原语
- 定义: 通过四条路径捕获实验数据——pipe-pane持续日志（运行期间实时记录）、capture-pane即时捕获（按需截取指定行数）、transcript权威记录（结束后生成）、export导出文件（每轮对话后自动导出）——任一路径失败时其他路
- 验证: tested（guided_001/003实验中已使用四路径捕获）
- 来源: 217-P6, 217-P7, 217-P8, 217-P9
- 依赖: 支撑 dfs-guidance（捕获DFS树数据）；支撑 多次独立验证（捕获的数据供验证）

### 极致提示集合（ultimate-hint-set）
- 类型: 结构原语
- 定义: 预定义的10个极致思维模式提示——归一化、寻找统一编码、恒等式挖掘、紧性归约、投影分解、扰动分析、量级感知、能量传递等——每个提示代表一个思维模式方向，带有Level值和分类标签，作为提示注入的候选库。这些是跨领域通用的最高抽象度提示。
- 验证: untested
- 来源: 215-P12, 215-P40, 216-P27
- 依赖: 支撑 shape-matching（提示集合提供候选，形状匹配选择候选）；支撑 rehearsal（预演产出极致提示集合）

### 规则库匹配（rule-base-matching）
- 类型: 结构原语
- 定义: 用规则库匹配替代硬编码提示——规则以LHS（左件）定义触发条件，RHS（右件）定义动作，匹配时检查当前状态是否满足规则的LHS条件。规则携带applicable_domains和applicable_model_versions字段，只对特
- 验证: untested
- 来源: 200-P20, 200-P27, 202-P07, 202-P10, 202-P11, 205-P2
- 依赖: 依赖 stall-diagnosis（诊断结果驱动规则匹配）；依赖 k-h-dual-storage（H维度存储规则）；支撑 ai-hint-compilation（规则候选供AI编译）

### 不可篡改事件流（immutable-event-stream）
- 类型: 结构原语
- 定义: 以不可篡改的事件流记录Solver的每一步输出，作为后续所有决策的数据基础。从题目到结果的完整链路分9层记录——题目元数据、测试运行元数据、预演记录、DFS树、每个节点完整记录、Session级记录、引导者决策日志、结果验证、性能指标。
- 验证: untested
- 来源: 202-P02, 214-P25, 214-P26, 216-P35
- 依赖: 支撑 decision-chain（事件流是决策链的数据基础）；支撑 cross-case-semantic-search（历史事件供搜索）

### K/H双存储（k-h-dual-storage）
- 类型: 结构原语
- 定义: 系统有两个核心存储：依赖图K（数学知识/定理/技巧的依赖关系图，存储在ArangoDB稀疏矩阵K维度）和启发规则H（解题策略/方法选择的启发式规则，存储在规则库中），分别对应知识缺口和策略缺口的补充来源。
- 验证: untested
- 来源: 213-P14
- 依赖: 支撑 rule-base-matching（H维度存储规则）；支撑 four-layer-knowledge-structure（K维度存储四层知识）；与 data-pedestal 关联（K维度是数据基座的物理实现）

### Solver角色隔离（solver-role-isolation）
- 类型: 结构原语
- 定义: work_dir中的AGENTS.md只定义Solver角色——直接做数学、不走工作系统流程、禁止web_search——确保AI的行为符合做题角色而非系统管理角色。Solver的devin cli实例必须在外部目录运行，不能在项目repo
- 验证: tested（run_20260806_guided_001/002中验证了在repo内运行时Solver被系统规则劫持，外部目录运行后解决）
- 来源: 215-P17, 211-P20
- 依赖: 依赖 file-transfer-isolation（文件传递隔离了题目与系统规则）；支撑 math-reasoning-engine（隔离确保Solver只做数学推理）

### 决策链（decision-chain）
- 类型: 结构原语
- 定义: 引导决策由诊断→匹配→选择→编译四步串联构成的核心决策链，每步有明确的输入输出契约。诊断（识别Solver状态和卡点类型）→匹配（在规则库中匹配适用规则）→选择（从候选动作中选择一个）→编译（将选择结果编译为具体提示文本）。
- 验证: untested
- 来源: 202-P01
- 依赖: 包含 state-reduction（决策链的输入预处理）；包含 stall-diagnosis（决策链的第一步）；包含 rule-base-matching（决策链的第二步）；包含 ai-hint-compilation（决策链的第四步）

### 数据集元数据管理（dataset-metadata-management）
- 类型: 结构原语
- 定义: ArangoDB作为中央元数据存储，数据集元数据按9类字段组织（标识、价值描述、内容属性、来源归属、HF/GitHub属性、获取、下载状态、项目相关、入库管理）。数据集按多个维度分类索引（source_type/math_domain/di
- 验证: tested（已入库10个数据集到ArangoDB
- 来源: 212-P6, 212-P7, 212-P9, 212-P10, 212-P11, 212-P12, 212-P13
- 依赖: 支撑 training-data-risk-assessment（元数据中的时间/语言/讨论热度字段支撑风险评级）；与 data-pedestal 关联（数据集元数据是数据基座的测试素材层）


## fuxi (50 candidates)

### semantic-energy-descent（语义能量下降）
- 类型: 操作原语
- 定义: 计算当前处境的六分量能量向量（表示复杂度/证书距离/自由度残差/粘合缺陷/反例压力/形式化缺口），以Pareto改善或受控交换为判据选择能降低能量的语义移动
- 验证: untested
- 来源: 225-1-P18, 225-P13, 226-P11/P17/P18/P19, 227-P19/P20, 228-v0-P16, 230-P22/P23, 2
- 依赖: 依赖 certificate-ledger（证书距离需账本），支撑 dual-output-closed-loop

### three-stage-retrieval（三阶段检索）
- 类型: 操作原语
- 定义: 检索分三阶段执行——粗筛用结构化字段匹配（处境类型+移动类型+证书类型），精化用图查询在依赖图中找连通路径，排序（可选）用向量检索在剩余候选中排序
- 验证: untested
- 来源: 234-P10, 235-P22/P35/P36/P37/P38, 236-P1/P2, 239-P1, 247-P4, 252-P1
- 依赖: 依赖 dependency-graph-k, subgraph-extraction, seed-selection

### naturality-test（自然性测试）
- 类型: 操作原语
- 定义: 换表示/换参数/取变体后，检查方法是否仍产生同类证书目标——先换表示再用方法 vs 先用方法再换表示，两条路径的证书目标应相容
- 验证: untested
- 来源: 225-1-P5, 225-P22/P23, 226-P7/P13, 227-P7, 228-v0-P6, 230-P16/P17, 235-P15/P33, 
- 依赖: 依赖 certificate-pullback, representation-atlas；约束于 criteria/naturality

### result-reflection（结果反射）
- 类型: 操作原语
- 定义: 将经典计算的结果（成功/反例/障碍/未知）反射回语义场，改变AI的语义理解——成功则猜想过强、因式分解则隐藏结构可能是乘积、类型不匹配则对象边界未说清
- 验证: untested
- 来源: 225-1-P4/P20, 225-P09/P30, 226-P6/P10, 228-v0-P18, 230-P25, 235-P28, 236-P5, 239
- 依赖: 依赖 certificate-ledger, verifiable-compilation；与 verifiable-compilation 互为V-R对

### verifiable-compilation（可证化编译）
- 类型: 操作原语
- 定义: 将AI提出的语义移动编译成可检查的证书目标集合——一个语义移动可能产生零个、一个或多个证书目标，每个目标指定可交给什么工具检查
- 验证: untested
- 来源: 225-1-P8, 225-P09, 226-P5/P10, 227-P11, 230-P18, 235-P16, 252-P10
- 依赖: 依赖 certificate；与 result-reflection 互为V-R对

### stuck-detection（卡点检测）
- 类型: 操作原语
- 定义: 检测AI是否卡住并分类卡住类型——区分"不知道下一步做什么"（方向缺失）和"知道方向但做不下去"（执行障碍），检测7种卡点类型（必要探索/语义重复/矛盾未处理/工具阻塞/表示不合适/策略耗尽/超时）
- 验证: untested
- 来源: 223-P19, 242-P13, 250-P24, 252-P15
- 依赖: 依赖 dynamic-workspace；支撑 three-stage-retrieval（触发检索）

### four-gate-leak-audit（四门泄漏审计）
- 类型: 操作原语
- 定义: 对提示内容执行四门检查——门1字面匹配（是否直接出现答案字面片段）、门2等价映射（是否包含答案等价表述）、门3候选空间缩减（是否把可能答案空间缩小）、门4盲恢复（撤掉提示后AI能否独立继续）
- 验证: untested
- 来源: 248-P19, 249-P24, 250-P17, 251-P8, 252-P19/P24
- 依赖: 依赖 truth-vault；约束于 non-specificity

### hint-gradient（提示梯度分级）
- 类型: 操作原语
- 定义: 将提示按泄漏风险分为5级——Hint-0只提示检查类型（很低泄漏）、Hint-1提示思维操作（低）、Hint-2提示候选工具/概念（中）、Hint-3提示确定方向（高）、Hint-4提示具体步骤（很高），检索结果按梯度分级返回
- 验证: untested
- 来源: 250-P4, 250-P25, 251-P7, 252-P24
- 依赖: 约束于 non-specificity, minimal-knowledge-transfer

### dual-route-comparison（双路线对照）
- 类型: 操作原语
- 定义: 同一批问题用两条路线分别跑——单纯AI路线（不强制执行契约/不维护证书账本/不强制结果回流）vs 闭环路线（强制这三件事），控制变量（AI模型/Prompt/温度/Python计算相同），用统一指标比较
- 验证: untested
- 来源: 229-P4, 230-P26, 235-P29, 239-P30, 240-P10
- 依赖: 依赖 execution-contract, certificate-ledger

### baseline-verification（裸跑基线验证）
- 类型: 操作原语
- 定义: 在测试任何引导/检索机制之前，必须先验证无引导（裸跑）基线性能，确认系统裸跑确实做不出来——否则无法证明机制的价值
- 验证: tested（guided_003实验中已执行裸跑对照）
- 来源: 243-P1/P2
- 依赖: 支撑 dual-route-comparison

### causal-intervention-validation（因果干预验证）
- 类型: 操作原语
- 定义: 验证一个Hint是"因果干预"而非"答案传递"——选取多个会在P处停滞的运行，在相同状态注入不超过预定H级别的X提示，设置未提示对照组，比较通过率差异
- 验证: untested
- 来源: 250-P16, 251-P17, 252-P25
- 依赖: 依赖 stuck-detection, hint-gradient；支撑 heuristic-rule-lifecycle, gain-attribution

### dead-end-marking（死路标记）
- 类型: 操作原语
- 定义: 经典计算标记已验证不可行的路径为死路，形成搜索空间中的障碍集，为后续导航提供约束——避免重复走已验证不可行的路径
- 验证: untested
- 来源: 224-P20, 228-v0-P5, 230-P31
- 依赖: 依赖 dependency-graph-k

### counterexample-search（反例搜索）
- 类型: 操作原语
- 定义: 经典计算搜索小模型、随机样本、极端边界和约束满足解，给出具体对象让猜想失败——反例作为高价值语义反馈改变AI方向
- 验证: untested
- 来源: 228-v0-P3, 228-v0-P29, 230-P29
- 依赖: 支撑 dead-end-marking, result-reflection

### subgraph-extraction（子图提取）
- 类型: 操作原语
- 定义: 给定当前分析上下文，从依赖图中用BFS/DFS遍历提取相关的依赖子图（控制深度和大小），组织成合理大小的结构化文本呈现给AI作为提示
- 验证: untested
- 来源: 223-P2/P9, 248-P5, 249-P5/P13, 250-P19, 252-P1
- 依赖: 依赖 dependency-graph-k, seed-selection；支撑 three-stage-retrieval

### seed-selection（种子选择）
- 类型: 操作原语
- 定义: 三级种子选择流水线——第一级层次索引定位（问题领域→3层主题树）、第二级语义检索（问题embedding→top-20节点）、第三级图遍历扩展（BFS/DFS深度3-5层，剪枝）
- 验证: untested
- 来源: 248-P10, 249-P14, 250-P18
- 依赖: 依赖 dependency-graph-k；支撑 subgraph-extraction

### shape-matching（形状匹配）
- 类型: 操作原语
- 定义: 不是基于"这道题能不能用反证法"（太宽泛），而基于"当前卡点的形状是否匹配反证法曾经成功突破过的形状"——先描述思维图中的局部形状，再在启发图中匹配规则
- 验证: untested
- 来源: 238-P7/P12/P13/P14, 248-P16, 249-P34, 250-P7, 251-P28
- 依赖: 依赖 thinking-trajectory-graph, heuristic-rule

### heuristic-rule-lifecycle（启发规则生命周期）
- 类型: 操作原语
- 定义: 启发规则有完整生命周期管理——observed（从轨迹差分观察到）→candidate（已形式化）→intervened（已做最小提示干预）→validated（重复验证有效）→retired（模型升级后不再需要），candidate状态禁
- 验证: untested
- 来源: 250-P13/P14/P42, 251-P5
- 依赖: 依赖 heuristic-rule, causal-intervention-validation

### level-based-hint-ordering（Level排序提示）
- 类型: 操作原语
- 定义: 提示生成器在选择提示时按Level排序，优先选高Level（更通用）的提示；当AI卡住时先给高Level提示，不够再逐步降低Level——形式化为 argmax ΣLevel(h_i) s.t. AI在H引导下完成解题
- 验证: untested
- 来源: 238-P4/P17/P18/P19/P21, 241-P18, 242-P2, 248-P21, 249-P23, 252-P3
- 依赖: 依赖 level-perception；约束于 concepts/level-spectrum；支撑 minimal-knowledge-transfer

### certificate-pullback（证书拉回）
- 类型: 操作原语
- 定义: 给定表示变换τ:S'→S，将S上的证书翻译到S'上的操作——这是跨表示检索的基础操作，使得在一个表示中获得的结论可以翻译到另一个表示
- 验证: untested
- 来源: 227-P14, 230-P21/P40, 235-P17
- 依赖: 依赖 certificate, representation-atlas；支撑 naturality-test, obstruction-detection

### obstruction-detection（粘合障碍检测）
- 类型: 操作原语
- 定义: 检查不同局部表示的局部证书在重叠处是否能粘合成全局证书，粘合失败分四级——descent failure→obstruction object→Čech 1-cocycle→H¹ class，失败时系统知道需要修复的是表示之间的翻译而非局部
- 验证: untested
- 来源: 225-1-P15/P16, 226-P15/P16, 227-P18, 228-v0-P4, 230-P8, 235-P12, 236-P21, 239-P2
- 依赖: 依赖 representation-atlas, certificate-pullback

### dual-output-closed-loop（单任务双产出）
- 类型: 操作原语
- 定义: 求解闭环运行一次，同时产出问题的解和数据基座条目——每步语义移动被记录、每个证书目标被编译、每个验证结果被回写，不需要单独做抽取
- 验证: untested
- 来源: 234-P1/P2, 235-P24, 236-P18, 237-P9, 239-P21, 252-P12
- 依赖: 依赖 execution-contract, data-pedestal, certificate-ledger

### gain-attribution（增益归因）
- 类型: 操作原语
- 定义: 对每次干预/引导，验证并归因其产生的增益——检索到的Pattern是否真正帮助了解题，增益来自哪个Pattern
- 验证: untested
- 来源: 252-P19/P25
- 依赖: 依赖 causal-intervention-validation

### honest-downgrade（诚实降级）
- 类型: 操作原语
- 定义: 当新证据出现时，原语的验证状态应当动态降级（如从tested降为partial），并记录降级原因——验证状态不是一次性标签，而是随证据持续更新的
- 验证: tested（guided_003后non-specificity从tested_negative升级为tested；243后cognitive-activation降为partial）
- 来源: 243-P5, 241-P38, 252-P19
- 依赖: 无

### progressive-pattern-extraction（渐进式模式提取）
- 类型: 操作原语
- 定义: 模式提取不是在解答末尾标注"此题用了反证法"（总结性的），而是在解答的每个关键转折点标注"这里从正面假设转向了反面假设"（过程性的）
- 验证: untested
- 来源: 238-P8/P9
- 依赖: 依赖 thinking-trajectory-graph

### level-perception（Level感知）
- 类型: 操作原语
- 定义: Level不是被算法赋值的，而是通过AI的相对比较感受出来的——把两个元素放在一起，AI能感知"这个比那个更抽象/更泛化"
- 验证: untested
- 来源: 238-P3/P5, 241-P18, 244-P19
- 依赖: 约束于 concepts/level-spectrum；支撑 level-based-hint-ordering

### multi-level-verification（多级验证）
- 类型: 操作原语
- 定义: 对AI输出执行四种验证——形式化验证（证明步骤合法性）、约束求解（约束是否满足）、类型检查（类型是否匹配）、知识库查询（引用的定理是否存在），每种验证有不同粒度和速度
- 验证: untested
- 来源: 223-P3/P4, 224-P5, 228-v0-P28, 249-P28
- 依赖: 支撑 result-reflection, dead-end-marking

### meta-normal-separation（meta/normal操作分离）
- 类型: 操作原语
- 定义: meta operation（拓扑规划、拓扑验证、审计）和normal operation（转译、分析）必须由不同AI实例完成，防止审计者与被审计者耦合
- 验证: untested
- 来源: 248-P7, 249-P20
- 依赖: 无

### spiral-loop-detection（螺旋环路检测）
- 类型: 操作原语
- 定义: 依赖图中存在环路（非DAG），需区分平面环路（循环论证，应停止追溯）和螺旋上升环路（深化分析，应继续追溯），判别标准是追溯一圈后是否产生新的判断维度
- 验证: untested
- 来源: 249-P4, 236-P14
- 依赖: 依赖 dependency-graph-k

### topology-coverage-verification（拓扑覆盖验证）
- 类型: 操作原语
- 定义: 在转译前先构造展开图拓扑骨架G'_topo（纯结构无文字），用AQL集合差集验证G'_topo覆盖G的所有节点/边/跨领域边/螺旋环路圈数，实现确定性验证
- 验证: untested
- 来源: 248-P6, 248-P14, 249-P6/P33
- 依赖: 依赖 dependency-graph-k

### incremental-context-compilation（增量上下文编译）
- 类型: 操作原语
- 定义: 上下文编译器不能只在任务开始时工作一次，而应在每次状态变化后增量工作——Q_t + 当前思维图T_t → 匹配启发关系 → 选择最小激活包 → 编译为增量提示
- 验证: untested
- 来源: 250-P6, 251-P11
- 依赖: 依赖 dynamic-workspace, heuristic-rule

### certificate-ledger（证书账本）
- 类型: 结构原语
- 定义: 系统在时刻t的状态是证书偏序C的向下封闭理想I_t——如果c'∈I_t且c→c'（c'加强c），则c∈I_t；单调增长I_t⊆I_{t+1}（每一步只加证书不删），已确认证书不会无声消失
- 验证: untested
- 来源: 225-P08, 226-P3/P6, 228-v0-P7, 230-P15, 235-P11, 236-P8, 239-P8, 252-P11
- 依赖: 依赖 certificate；支撑 semantic-energy-descent, result-reflection, dual-route-comparison

### representation-atlas（表示图册）
- 类型: 结构原语
- 定义: 一个处境不能被单一表示完全看清，需要一组可切换、可重叠、可拼合的局部表示（图册A(S)），每种表示是一个能看清某些结构的局部视角——包含原始表示、规范化表示、对偶表示、形式化表示
- 验证: untested
- 来源: 225-P04, 225-P17, 226-P12, 227-P14/P15/P16, 230-P20/P40, 235-P17, 236-P15, 239-P
- 依赖: 支撑 certificate-pullback, obstruction-detection, naturality-test

### three-graph-architecture（三图架构）
- 类型: 结构原语
- 定义: 系统由三张图构成——K数学知识图（客观依赖关系）、T外显思维图（Agent实际思维轨迹）、H启发激活图（条件→动作→效果证据），三图是投影而非独立真相库
- 验证: untested
- 来源: 248-P3, 249-P9, 250-P1/P39, 251-P1
- 依赖: 包含 dependency-graph-k, thinking-trajectory-graph, heuristic-rule

### dynamic-workspace（动态工作区）
- 类型: 结构原语
- 定义: 系统在时刻t的完整状态用六元组表示——V_t（已验证核心，只增不减）、F_t（猜想前沿，可升级或被否定）、O_t（开放义务，AND/OR超图）、R_t（表示状态）、E_t（证据）、U_t（未解决问题），状态从事件流归约得出
- 验证: untested
- 来源: 250-P11, 251-P2/P29, 252-P5
- 依赖: 依赖 event-sourcing；支撑 stuck-detection, incremental-context-compilation

### heuristic-rule（启发规则）
- 类型: 结构原语
- 定义: H图中的启发边不是普通边，而是带条件的图改写规则——(L, guard) ⇒ R，L=LHS当前思维图中应出现的局部子图，guard=上下文/时序/模型/失败类型等条件，R=RHS应加入的概念/子目标/工具/反例方向
- 验证: untested
- 来源: 248-P17, 249-P10, 250-P2/P3/P35, 251-P5/P6
- 依赖: 依赖 thinking-trajectory-graph；支撑 shape-matching, heuristic-rule-lifecycle, incremental-context-compilation

### event-sourcing（事件溯源）
- 类型: 结构原语
- 定义: 研究过程中的每一步都是不可变的事件，系统在第t时刻的状态是这些事件的投影——从所有已发生事件中归约出来的当前快照，事件一旦发生就不可修改
- 验证: untested
- 来源: 250-P9/P10/P37, 251-P9/P10, 252-P14
- 依赖: 支撑 dynamic-workspace

### truth-vault（真值保险库）
- 类型: 结构原语
- 定义: 答案和完整证明存储在隔离的truth_vault collection中，访问权限严格限制——写入仅truth_curator，读取仅auditor，Controller和其他角色无权访问
- 验证: untested
- 来源: 248-P19, 250-P22, 251-P16, 252-P19
- 依赖: 支撑 four-gate-leak-audit

### obligation-hypergraph（义务超图）
- 类型: 结构原语
- 定义: 开放义务用AND/OR有向超图表达——AND约束（所有子目标都必须解决）、OR约束（任一路径成功即可），超边e=(source, {targets}, type)记录义务的分解结构
- 验证: untested
- 来源: 250-P12, 251-P4
- 依赖: 支撑 dynamic-workspace

### three-layer-recording（三层记录）
- 类型: 结构原语
- 定义: 运行时记录分三层——层次1 devin cli实例轨迹（外部层，终端实际发生什么）、层次2 系统内部结构化执行日志（中间层，系统做了什么决策和为什么）、层次3 数学大师思路轨迹（内层，AI的数学推理过程）
- 验证: untested
- 来源: 248-P22, 250-P31, 251-P18
- 依赖: 无

### topology-feature-vector（拓扑特征向量）
- 类型: 结构原语
- 定义: 用七个维度（约束类型、结论类型、核心鸿沟、关键桥梁、极值结构、修正来源、稳定性机制）构成的结构化特征向量来表示一个问题的拓扑；用五个维度（输入形状、操作类型、输出形状、适用条件、失败条件）表示思维模式的拓扑
- 验证: untested
- 来源: 219-P2/P3, 219-P9/P12, 221-P4/P18/P19
- 依赖: 支撑 three-stage-retrieval（粗筛匹配维度）

### thinking-trajectory-graph（思维轨迹图）
- 类型: 结构原语
- 定义: T图记录Agent的实际思维轨迹——一次运行的事件序列，包括AI做了什么操作、得到什么结果、在哪里卡住、在哪里突破，是启发规则匹配的输入
- 验证: untested
- 来源: 248-P3, 249-P9, 250-P1/P15
- 依赖: 支撑 shape-matching, heuristic-rule, progressive-pattern-extraction

### role-isolation-matrix（角色隔离矩阵）
- 类型: 结构原语
- 定义: 系统功能拆分为8个隔离角色（solver/event_capture/state_reducer/retriever/heuristic_matcher/verifier/auditor/controller），每个角色有明确的职责和权限边
- 验证: untested
- 来源: 250-P20/P21, 251-P14/P15, 252-P23
- 依赖: 依赖 pipe

### dependency-graph-k（依赖图K）
- 类型: 结构原语
- 定义: K数学知识图的形式化定义——G = (V, E, C, L, K)，V=节点集，E=边集，C=跨领域边，L=螺旋环路集，K=知识内容映射；四种边类型：知识依赖边、工具适用边、跨领域映射边、证明策略边
- 验证: untested
- 来源: 223-P8, 247-P2, 248-P2, 249-P2/P3, 250-P1
- 依赖: 支撑 subgraph-extraction, seed-selection, dead-end-marking, spiral-loop-detection, topology-coverage-verification

### schema-freezing（Schema冻结）
- 类型: 结构原语
- 定义: 将8类数据结构的Schema设为不可变（Task/Workspace/Event/Obligation/Representation/Evidence/HeuristicRule/CognitionUnit），确保数据结构字段定义在运行时不
- 验证: untested
- 来源: 248-P13, 250-P27, 251-P22
- 依赖: 无

### multi-level-knowledge-extraction（多层知识提取）
- 类型: 结构原语
- 定义: 从题解中提取三个层次的知识——L1解题思路（具体步骤，直接记录）、L2数学思维（思维模式，AI二次分析抽象）、L3范式思维（跨领域复用，改变图结构，AI三次分析综合），可选L4哲学/世界观层
- 验证: untested
- 来源: 248-P23/P24, 249-P7, 250-P29
- 依赖: 依赖 thinking-trajectory-graph；支撑 data-pedestal

### failure-boundary-record（失败边界记录）
- 类型: 结构原语
- 定义: 记录哪些相似命题不成立、哪些条件删掉会失败、哪些指数或常数是错的——失败边界是数据基座的一等公民，可作为检索对象避免重复探索已知不可行的方向
- 验证: untested
- 来源: 231-P15, 234-P16, 235-P34, 239-P11
- 依赖: 依赖 data-pedestal；支撑 dead-end-marking

### pattern-library（模式库）
- 类型: 结构原语
- 定义: 模式库不只是写着"换基""对偶""归纳"，而是带着触发条件、计算接口、证书模板和失败边界——每个模式附带适用信号、证书模板、失败案例、反例族和验证脚本，是实验室的技术积累
- 验证: untested
- 来源: 225-P14, 228-v0-P11/P20, 230-P37, 235-P32/P39, 236-P10, 239-P09
- 依赖: 依赖 data-pedestal, naturality-test；支撑 three-stage-retrieval

### structured-document-index（结构化文档索引）
- 类型: 结构原语
- 定义: 为每个文档打上二元相关性标签+多维类型标签+压缩摘要+关键段落行号范围+语义段落名称，文档间的引用关系构成依赖图可用于检索时的关联扩展
- 验证: tested（Pass
- 来源: 247-pass1-P1/P2/P3/P4/P5/P7/P9/P10/P11
- 依赖: 支撑 three-stage-retrieval

### checkpoint-continuation（检查点续行）
- 类型: 结构原语
- 定义: 当执行过程中出现失败时，从最近的checkpoint恢复继续执行，而不是从头开始——支持基于断点的检索和恢复
- 验证: untested
- 来源: 251-P12, 252-P15
- 依赖: 依赖 event-sourcing

### version-chain（版本链）
- 类型: 结构原语
- 定义: 用版本链（cog_versions集合+cog_version_edges版本链边）处理认知迭代——认知不是简单替换而是演化，每个认知单元有版本历史，版本之间有演化关系
- 验证: untested
- 来源: 249-P30, 221-P15
- 依赖: 无


## other (19 candidates)

### 物理隔离（physical-isolation）
- 类型: 结构原语（基础设施层）
- 定义: 通过物理隔离的独立clone（非git worktree）实现多个AI并发工作互不干扰，每个环境有独立的工作目录、分支和数据库。
- 验证: tested（在glm5.2
- 来源: 001-P01
- 依赖: 支撑 name-isolation

### 名称隔离（name-isolation）
- 类型: 操作原语（基础设施层）
- 定义: 当多个用户/agent共享同一物理实例（如ArangoDB `localhost:8529`）时，通过名称（环境变量DB_NAME）实现逻辑隔离，每个用户只操作自己的命名空间。
- 验证: tested（在glm5.2
- 来源: 001-P02, 003-P21, 004-P035（三处归并）
- 依赖: 依赖 physical-isolation

### 表示映射（representation-map）
- 类型: 结构原语
- 定义: 在不同数学表示之间建立映射关系的数据结构，是状态表示和模式匹配的基础设施——同一段推理可在不同表示空间中编码。
- 验证: untested（文件存在但审计可能发现声明性实现问题）
- 来源: 004-P001
- 依赖: 支撑 commutative-diagram, transport-object, local-view, path-equivalence, trajectory-alignment, groupoid-check, persistent

### 可靠性义务（soundness-obligation）
- 类型: 操作原语
- 定义: 要求每个表示/推理步骤满足可靠性约束的强制机制，确保表示不失真——不是"应该可靠"的标准，而是"强制检查可靠性"的机制。
- 验证: untested（审计重点检查对象——D21维度检查是否声明性而非强制性）
- 来源: 004-P002
- 依赖: 依赖 representation-map；与 certificate 相关（证书验证数学事实的正确性，可靠性义务验证表示的保真性）

### 费马链（fermat-chain）
- 类型: 结构原语
- 定义: 以费马案例为原型的推理链条结构模板，包含多个环节和层阶梯，是Pattern的结构化存储格式。
- 验证: untested
- 来源: 004-P004
- 依赖: 与 data-pedestal 相关（费马链是数据基座条目的结构模板之一）

### 广群检查（groupoid-check）
- 类型: 操作原语
- 定义: 基于广群（groupoid）代数结构对推理步骤间的关系进行一致性检查，验证推理结构的代数性质（可逆性、复合性等）。
- 验证: untested
- 来源: 004-P006
- 依赖: 依赖 representation-map

### 路径等价（path-equivalence）
- 类型: 操作原语
- 定义: 判定两条推理路径是否等价的机制，允许不同推理路径到达相同结论时被识别为"相同状态"——近似匹配的代数基础。
- 验证: untested
- 来源: 004-P007
- 依赖: 依赖 representation-map；支撑 commutative-diagram, trajectory-alignment

### 交换图（commutative-diagram）
- 类型: 结构原语
- 定义: 用交换图表示数学结构之间的映射关系，验证不同路径的复合是否保持结构一致性——多表示空间一致性验证的结构基础。
- 验证: untested
- 来源: 004-P008
- 依赖: 依赖 representation-map, path-equivalence

### 传输对象（transport-object）
- 类型: 结构原语
- 定义: 在表示空间之间传输的数据对象，封装了需要被"搬运"的知识/Pattern的结构化信息——Pattern的标准化封装格式。
- 验证: untested
- 来源: 004-P009
- 依赖: 依赖 representation-map

### 局部视图（local-view）
- 类型: 结构原语
- 定义: 从全局结构中提取局部视图，聚焦于当前推理节点周围的邻域结构——状态感知的聚焦机制和索引粗筛的基础。
- 验证: untested
- 来源: 004-P010
- 依赖: 依赖 representation-map；支撑 hole-detector

### 空洞检测（hole-detector）
- 类型: 操作原语
- 定义: 检测推理结构中的"空洞"——缺失的步骤、未建立的连接、需要填补的推理间隙——直接识别"此刻需要什么类型的提示"。
- 验证: untested
- 来源: 004-P011
- 依赖: 依赖 representation-map, local-view；与 pattern-recognition-engine 相关（空洞检测是模式识别引擎的一种具体检测操作——识别"需要什么"）

### E-图（e-graph）
- 类型: 结构原语
- 定义: 等式饱和（equality saturation）数据结构，允许同一数学表达式的多种等价表示共存并高效匹配——基于等价关系的表达式级匹配基础设施。
- 验证: untested
- 来源: 004-P012
- 依赖: 与 constraint-solver-engine 相关（E-图可用于多约束求解引擎中的表达式化简和等价匹配）

### 轨迹对齐（trajectory-alignment）
- 类型: 操作原语
- 定义: 将两条推理轨迹（当前推理轨迹和Pattern存储的轨迹）进行对齐，识别结构相似性——推理路径级的匹配算法。
- 验证: untested
- 来源: 004-P013
- 依赖: 依赖 representation-map, path-equivalence

### 几何守卫（geometry-guard）
- 类型: 操作原语
- 定义: 对推理结构的几何性质（如距离、角度、曲率）进行守卫检查，确保表示的几何一致性。
- 验证: untested（最理论化的组件——推理结构的"几何性质"定义不明确，可能是声明性实现）
- 来源: 004-P014
- 依赖: 依赖 representation-map

### TDA门控（tda-gate）
- 类型: 操作原语
- 定义: 基于拓扑数据分析（TDA）的门控机制，通过拓扑特征判定是否允许某种操作/匹配——拓扑匹配的门控判定。
- 验证: untested
- 来源: 004-P015
- 依赖: 依赖 persistent-homology（TDA门控使用持续同调计算的拓扑特征做判定）

### 持续同调（persistent-homology）
- 类型: 操作原语
- 定义: 通过持续同调计算推理结构在不同尺度下的拓扑特征（Betti数、持续图），提供尺度不变的拓扑指纹——拓扑匹配的特征提取方法。
- 验证: untested
- 来源: 004-P016
- 依赖: 依赖 representation-map；支撑 tda-gate

### HoTT门控（hott-gate）
- 类型: 操作原语
- 定义: 基于同伦类型论（HoTT）的门控机制，用类型论的同伦层级判定推理状态的类型匹配——拓扑匹配的形式化基础。
- 验证: untested（HoTT是前沿理论，实现可能不完整）
- 来源: 004-P017
- 依赖: 与 hott-directions（concept）相关

### 数学标签（math-label）
- 类型: 结构原语
- 定义: 为数学内容打上结构化标签（如思维模式类型、数学结构类型、Level值），用于分类和索引——Pattern分类索引的实现基础。
- 验证: untested
- 来源: 004-P020
- 依赖: 支撑 phase-gate

### 阶段门控（phase-gate）
- 类型: 操作原语
- 定义: 基于推理阶段（phase）的门控机制，根据当前所处的推理阶段决定允许哪些操作/Pattern——Pattern触发条件中的阶段约束。
- 验证: untested
- 来源: 004-P021
- 依赖: 依赖 math-label；与 dfs-guidance 相关（阶段门控与DFS的Level选择有关联——不同阶段对应不同Level的Pattern）


---
Total: 213 new-candidate primitives
