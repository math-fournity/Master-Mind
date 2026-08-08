# 任务追踪 · 端到端效果验证-接真实Solver

> **本文件是跨Session的工作追踪文档。新Session的AI进入本工作线后，先读本文件，了解"之前做了什么、现在在做什么、接下来该做什么"。**
>
> **维护规则**：每完成一个工作单元，立即更新对应条目的状态。新增任务时追加到末尾。不删除历史条目——它们是工作积累的记录。

---

## 0. 当前工作焦点

**主线**：✅ **阶段2核心循环已转通**——串行多AI树生长引擎（Grove）的三个推动关系都成立。AI-1→检索→AI-2→检索→AI-3，树持续生长。

**当前状态**：2026-08-08，case_253实验验证了核心循环完整转动。3个AI实例，19个节点，2条边。AI-1探索矩条件极差题→AI-2继续数值验证+多项式方法→AI-3用badly approximable性质推|D|下界。

**待修复的已知问题**：
1. `retrieve_directions`匹配逻辑——hgraph规则按`node_types`匹配，但六元组没有该字段，当前手动注入方向Q
2. `sessions_db_reader.init()`重复提取——从-1开始导致每次extract重新提取所有thinking
3. `serial_multi_ai.py`脚本主循环模式与"你就是主循环"认知冲突

**⚠️ 未来系统面相认知（跨压缩边界必须携带）**：

A/B实验是树生长引擎的**简化版本**（阶段1：1个AI串行展开）。用户已注入"未来系统面相"认知（267号文档），核心转变是：

> **从"让AI停下接受提示"到"系统与推理AI并行运行"。**

未来系统的演进路径：
- **阶段1（当前A/B实验，已完成）**：1个推理AI，串行展开，thinking完成→解析→检索→选提示→注入→下一轮thinking
- **阶段2（脉络注入，下一步）**：1个推理AI跑完（或崩溃）后，系统整理其脉络→在脉络终点节点检索识别方向→启动新推理AI给它脉络继续探索。不需要"让AI停下"——AI自然终止后系统再分配
- **阶段3（并发展开）**：N个推理AI并发（如5个额度），系统实时采集所有AI的trajectory整理两棵树→在节点上识别方向分配新AI→停机条件：与正确解答脉络相遇
- **阶段4（自我增殖）**：解题记录树完成后提炼Pattern存入数据基座→数据基座Pattern积累→未来树长得更快更准

**关键认知**：之前花大量时间修复的HintInjector时序问题（等thinking完成再注入、tmux send-keys排队、状态检测等），在未来系统中**不再是问题**——因为未来系统不需要让推理AI停下接受提示，而是启动新的推理AI实例给它脉络。这些修复工作验证的能力（mitmproxy截获/parser/retrieval/policy/harness）都会在未来系统中复用。

**267号文档是本工作线的认知转折点**——它不是方案文档（不规定具体实现步骤），而是设计认知文档，为未来系统设计提供认知基础。跨压缩边界后的AI进入本工作线时，**必须先读267号文档**再继续工作。

**下一步**：
1. 04工作线核心目标（A/B效果验证）已达成
2. 未来工作带着267号面相认知进行——不再设计"让AI停下接受提示"的机制，设计"系统与推理AI并行运行"的机制
3. 可进入03-VMS-POC验证（带着树生长引擎认知设计），或直接向阶段2（脉络注入）演进

---

## 1. 已完成的工作

### 1.1 端到端效果验证方案设计

**为什么做**：01工作线验证了"检索机制能选出正确的Q"（253号A7→Q8），但这只是"选出了正确提示"，没有验证"选出提示后AI是否真的突破卡点"。从"原型验证"到"效果验证"是性质不同的阶段——原型验证用的是已生成的QA记录（离线），效果验证需要实时解析+实时检索+实时提示注入（在线）。不验证效果，检索机制可能只是"理论上正确"但实际无效。

- [x] 分析效果验证的复杂度——涉及多模块实时集成
- [x] 确定本工作线是01工作线和02工作线的交汇点
- [x] 创建本任务追踪文档

### 1.2 实时解析管线实现（§2.3-2.5）

**为什么做**：01工作线的parser是离线的——解析预先生成的A_i文本。效果验证需要在线实时解析——Solver每输出一段，立即解析为ParseResult，检索Pattern，选择提示，注入到Solver。不搭建实时管线，检索机制无法接入实时Solver。

**实现的模块**（`xishujuzhen/research_runtime/realtime/`）：
- `trajectory_watcher.py`：监控sessions.db，从Devin CLI trajectory提取Round（一个Round = Solver一轮完整输出，对应离线的A_i）
- `stall_detector.py`：卡点检测（语义检测"我不知道"等关键词 + 超时检测N秒无新节点）
- `pipeline.py`：RealtimePipeline整合watcher + stall_detector + MathParser + RetrievalPipeline + ConstrainedPolicy
- `hint_injector.py`：通过tmux send-keys注入提示到Solver session
- `test_realtime.py`：mock测试——用253号A7数据验证完整流程

**测试结果**：
- StallDetector：语义检测✅（匹配"我不知道"）、超时检测✅
- RealtimePipeline：解析✅（4事件4节点）、六元组✅（V_t=6/F_t=2/O_t=7/U_t=1）、检索✅（5条匹配规则）、策略选择✅（选中Q8）
- HintInjector：dry-run✅（不存在的session正确返回False）
- TrajectoryWatcher：mock Round构建✅
- **关键验证**：选中Q8与离线test_e2e_253结果一致——实时管线正确复现了离线检索流程

### 1.3 DevinCliParserProvider实现（解决6.5降级parser限制）

**为什么做**：6.5端到端集成测试用降级parser（只产生observation事件），每次选中Q1而非Q8。需要真实LLM parser来正确解析resolution事件，使检索机制能选出有针对性的提示。但本地没有可用的LLM API端点（无OpenAI兼容API key）。解决方案：用devin cli本身作为parser的LLM——`devin -p`发送解析prompt，捕获JSON输出。

**实现的模块**：
- `realtime/devin_cli_parser.py`：DevinCliParserProvider——实现LLMParser的mock_response_provider接口，用`devin -p`调用devin cli执行260号§3.1的LLM粗解析
- `realtime/test_devin_cli_parser.py`：parser单元测试
- `realtime/test_realtime_devin_cli.py`：完整管线测试（devin cli parser + retrieval + policy）
- `parser/models.py`容错改进：MathObject.from_dict支持字符串输入，Evidence.from_dict支持字段名变体

**测试结果**（253号A7）：
- devin cli解析时间：25-41秒/次
- 解析质量：4事件4节点，parse_confidence=0.88，SymPy验证3/4通过
- 完整管线（devin cli parser + retrieval + policy）：33.4秒
- 选中Q4（与mock LLM的Q8不同——devin cli的六元组解析结果与mock有差异，V_t=9 vs 6, O_t=2 vs 7，导致策略选择不同。这是真实场景下的预期行为——不同LLM解析出的结构化表示有差异）

**关键设计决策**：
- parser的devin cli在独立工作目录运行（`/data/grove-parser-1/`），不复用Solver工作目录
- parser的devin cli用`-p`单轮模式（不需要交互）
- parser的devin cli不需要MITM（不采集trajectory）
- JSON提取容错：支持纯JSON、markdown代码块、花括号提取等多种格式

---

## 2. 待办清单（按优先级排序）

### P0-前置条件（必须先完成） ✅

#### 2.1 等待01工作线P1原语升级tested ✅

**为什么做**：本工作线要用完整的检索机制（P0+P1全部模块），如果P1原语还是partial（只在253号单一案例上验证），在新案例上跑可能出问题。先在01工作线完成P1升级tested，确保检索机制本身可靠。

- [x] 01工作线P1原语升级tested完成（tested 35/72，8个P1原语在数论和组合2个新案例上全部通过）

#### 2.2 等待02工作线solver-harness实施完成 ✅

**为什么做**：本工作线需要实时采集Solver的trajectory（thinking+tool_calls+results），这是02工作线solver-harness的核心能力。没有solver-harness，无法实时获取Solver的推理过程，也就无法实时解析和检索。

- [x] 02工作线solver-harness v1实施完成（全局共享mitmproxy + 事后批量解码 + 端到端测试通过）
- [x] 所有场景统一用solver-harness（rule+skill+AGENTS.md硬约束已写入）

### P1-核心实施

#### 2.3 实时解析管线搭建 ✅

**为什么做**：01工作线的parser模块是离线的——解析预先生成的A_i文本。效果验证需要在线实时解析——Solver每输出一段，立即解析为语义事件+T_t节点+六元组。不搭建实时管线，检索机制无法接入实时Solver。

- [x] 设计实时解析管线架构（TrajectoryWatcher监控sessions.db → 提取Round → MathParser解析）
- [x] 实现trajectory数据到ParseRequest的适配器（`_nodes_to_agent_output`：thinking+content+tool_calls → agent_output文本）
- [x] mock测试通过（253号A7解析出4事件4节点，六元组V_t=6/F_t=2/O_t=7/U_t=1）
- [x] 验证实时解析结果与离线解析结果一致（mock数据下一致）

#### 2.4 实时检索管线搭建 ✅

**为什么做**：01工作线的retrieval-pipeline是离线的——对单个ParseResult跑一次检索。效果验证需要在线实时检索——每解析出一个新的ParseResult，立即检索Pattern并选择提示。不搭建实时检索，无法在Solver卡住时及时给出提示。

- [x] 设计实时检索管线架构（ParseResult → RetrievalPipeline → ConstrainedPolicy → 提示选择）
- [x] 实现卡点检测的实时触发（StallDetector：语义检测"我不知道"等关键词 + 超时检测）
- [x] mock测试通过（检索5条匹配规则，策略选中Q8）
- [x] 验证实时检索结果与离线检索结果一致（选中Q8与test_e2e_253一致）

#### 2.5 提示注入机制 ✅

**为什么做**：01工作线验证了"constrained-policy选中Q8"，但没有实际发送Q8给Solver。效果验证需要实时提示注入——选出的提示要实际发送到Solver的session中，影响Solver的后续推理。不验证提示注入，不知道提示是否能被Solver正确接收和利用。

- [x] 设计提示注入机制（HintInjector：通过tmux send-keys注入到Solver session）
- [x] 实现提示注入的时序控制（wait_idle等待pane空闲 + 逐行send-keys + Enter提交）
- [x] dry-run测试通过（不存在的session正确返回False）
- [ ] 验证提示注入后Solver的trajectory中能看到提示（需真实Solver实验）

#### 2.6 端到端效果验证实验 ✅

**为什么做**：这是本工作线的核心目标——验证"检索机制选出提示后，AI是否真的能突破卡点"。不跑这个实验，整个检索机制的价值未经验证。

- [x] 选择实验题目（253号题第二问，竞赛级难题）
- [x] 设计A/B对照实验：
  - A组：有检索系统（实时解析+实时检索+提示注入）
  - B组：无检索系统（Solver裸跑，无提示）
- [x] 跑B组实验3次（裸跑对照组）
- [x] 跑A组实验3次（有检索系统实验组）
- [x] 对比A/B组：
  - 成功率：A组substantial_progress 2/3，B组 0/3
  - 突破卡点：A组在收到提示后trajectory_nodes 22 vs 6，thinking_count 6.7 vs 3.3
  - 效率：A组平均hints注入9.3次/实验
  - 提示质量：检索系统注入Q1-Q10启发式规则，引导Solver思考而非替Solver做题
- [x] 落实验报告（267号文档）

**关键结果**：
| 指标 | B组（裸跑） | A组（有检索系统） |
|---|---|---|
| truncated | 3/3 (100%) | 1/3 (33%) |
| substantial_progress | 0/3 (0%) | 2/3 (67%) |
| 平均trajectory_nodes | 6 | 16.3 |
| 平均thinking_count | 3.3 | 6.7 |

**技术问题修复**（实验过程中）：
- mitmproxy workdir_mapping缓存60秒导致新实验匹配失败 → 缓存减至10秒+匹配失败强制刷新重试
- mitmproxy启动时D盘未挂载导致文件句柄失效 → 重启修复

### P2-后续深化

#### 2.7 多案例效果验证

**为什么做**：单一案例的效果验证可能偶然性高。多个案例的效果验证才能确认检索机制的普遍有效性。

- [ ] 在3-5个不同领域的案例上跑A/B对照
- [ ] 统计整体成功率和突破率
- [ ] 分析失败案例——是检索选错了提示，还是提示本身无效？

#### 2.8 controlled-experiment框架化

**为什么做**：手动跑A/B对照效率低，且不可复现。框架化后可以自动跑多个案例的对照实验。

- [ ] 基于checkpoint模块实现实验快照和复现
- [ ] 实现A/B对照的自动化脚本
- [ ] 生成实验报告（成功率/突破率/效率/提示质量）

### P3-未来演进（267号面相认知驱动 · 跨压缩边界必须携带）

> **⚠️ 以下任务基于267号"未来系统面相"认知。跨压缩边界后的AI进入本工作线时，必须先读267号文档理解这些任务的认知基础。**

#### 2.9 阶段2：脉络注入——串行多AI ✅ 核心循环已转通

**为什么做**：267号面相认知指出，未来系统不需要让推理AI停下接受提示，而是启动新推理AI给它脉络继续探索。阶段2是A/B实验（阶段1）到并发展开（阶段3）的中间形态——仍然串行，但不需要"让AI停下"。

**认知基础**：267号§4"从A/B实验到未来系统的演进路径"阶段2

**完成状态（2026-08-08）**：核心循环已完整转通——AI-1→检索→AI-2→检索→AI-3，三个推动关系都成立。

- [x] 实现`path_constructor.py`——从根到当前节点的路径，构造给新推理AI的输入文本
- [x] 实现`node_extractor.py`——从推理AI的trajectory中提取树节点（封装DevinCliParserProvider+六元组提取）
- [x] 实现`tree_store.py`——ArangoDB树存储（tree_nodes/tree_edges/problems/ai_instances集合的CRUD）
- [x] 改造`termination_detector.py`——从"检测卡住触发注入"改为"检测AI终止触发检索分配"（移除timeout杀AI逻辑）
- [x] 实现`sessions_db_reader.py`——从sessions.db读取thinking（替代MITM）
- [x] 串行多AI实验：Solver跑完（或崩溃）→系统整理脉络→检索识别方向→启动新Solver给脉络→重复
- [x] **核心循环完整转通验证**：case_253实验，3个AI实例，19个节点，2条边，三个推动关系都成立

**已知问题（待修复）**：
- [ ] `retrieve_directions`匹配逻辑有gap——hgraph规则按`node_types`匹配，但parser解析出的六元组没有`node_types`字段。当前手动注入方向Q绕过。需要修复检索pipeline从六元组推断node_types
- [ ] `sessions_db_reader.init()`从-1开始导致重复提取——每次extract都会重新提取所有thinking，产生重复节点。需要去重或改为增量模式
- [ ] `serial_multi_ai.py`的脚本主循环模式与"你就是主循环"认知冲突——当前实验中辅助Pipe手动执行循环，脚本只做机械部分

#### 2.10 阶段3：并发展开——多AI并发

**为什么做**：267号面相认知指出，多个推理AI可以并发。假设5个并发额度，某个脉络尽头有3条路→启动3个AI各探索一条→剩余2个额度用于实时整理3个AI的trajectory发现新可分配节点。

**认知基础**：267号§4阶段3 + §7.1树生长引擎主循环

- [ ] 实现`ai_manager.py`——并发推理AI管理（额度分配、状态监控、启动/停止）
- [ ] 实现`tree_engine.py`——树生长引擎主循环（采集→整理树→检查停机→检查AI终止→分配新AI→实时检索）
- [ ] 实现`solution_verifier.py`——停机判定（验证证明正确性）
- [ ] 并发多AI实验：5个Solver并发→系统实时整理两棵树→与正确解答脉络相遇时停机

#### 2.11 阶段4：自我增殖——树→Pattern→树

**为什么做**：267号面相认知指出，解题记录树完成后提炼Pattern存入数据基座，数据基座Pattern积累→未来树长得更快更准。这是256号论文描述的"自我增殖的循环"。

**认知基础**：267号§4阶段4 + `原语化AI数学工程系统设计/05-两棵树/03-系统本质-生长完整的树.md`

- [ ] 实现解题记录树→Pattern提炼流程
- [ ] 验证"树越长越全→Pattern越积越多→模式识别越准→未来树长得越全"的自我增殖循环

---

## 3. 关键决策记录

### 3.1 为什么需要独立的工作线

01工作线（253号检索机制验证）验证的是"检索机制能选出正确的Q"——离线、单次、用预生成数据。
本工作线验证的是"选出Q后AI是否真的突破"——在线、实时、用真实Solver。

两者性质不同：
- 01是"组件验证"——各模块是否能独立工作
- 本工作线是"系统集成验证"——各模块串起来能否在真实环境中工作

且本工作线依赖02工作线（solver-harness）的trajectory采集能力，是01和02的交汇点，不属于任何一个的简单延续。

### 3.2 为什么用A/B对照而非单组实验

单组实验（只跑有检索系统的A组）无法排除"AI本来就能做出来"的假设。A/B对照通过比较"有检索系统"和"无检索系统"的差异，才能证明检索机制的价值。

### 3.3 为什么提示质量是关键指标

如果选出的提示是"直接告诉答案"，即使A组成功率更高，也不能说明检索机制有效——那只是替AI做题。提示质量指标验证的是"提示是否引导AI自己思考"而非"提示是否替AI思考"。这是燧人代"不给火而教取火"理念的核心。

---

## 4. Git Commit历史

| Commit | 描述 | 产出资产（完整路径） |
|---|---|---|
| b5bbae3 | 04工作线§2.3-2.5：实时解析+检索+注入管线实现，mock测试通过（7文件） | **代码**: `xishujuzhen/research_runtime/realtime/__init__.py`, `xishujuzhen/research_runtime/realtime/trajectory_watcher.py`, `xishujuzhen/research_runtime/realtime/stall_detector.py`, `xishujuzhen/research_runtime/realtime/pipeline.py`, `xishujuzhen/research_runtime/realtime/hint_injector.py`, `xishujuzhen/research_runtime/realtime/test_realtime.py` **任务追踪**: `任务追踪/04-端到端效果验证-接真实Solver.md` |
| 22f80dd | 落盘264号方案：端到端效果验证-接真实Solver的实时检索提示突破闭环 | **文档**: `dev-docs/264-v0-2026-08-08-端到端效果验证方案-接真实Solver的实时检索提示突破闭环.md` |
| 829566f | 6.1完成+solver-harness新增--interactive模式 | **代码**: `xishujuzhen/solver_harness/solver_harness.py` **文档**: `dev-docs/264-v0-2026-08-08-端到端效果验证方案-接真实Solver的实时检索提示突破闭环.md` |
| 0e229a0 | 04工作线P0核心实现：TrajectoryAdapter + HintInjector + RealtimePipeline（已删除，与b5bbae3重复） | ~~`xishujuzhen/research_runtime/runtime/trajectory_adapter.py`~~, ~~`xishujuzhen/research_runtime/runtime/hint_injector.py`~~, ~~`xishujuzhen/research_runtime/runtime/realtime_pipeline.py`~~ |
| 9dee6a3 | 合并6.1验证结果到realtime/hint_injector.py + 更新04任务追踪 | **代码**: `xishujuzhen/research_runtime/realtime/hint_injector.py` **文档**: `dev-docs/264-v0-2026-08-08-端到端效果验证方案-接真实Solver的实时检索提示突破闭环.md`, `任务追踪/04-端到端效果验证-接真实Solver.md` |
| e9fd092 | 04工作线§6.5端到端集成测试：完整闭环验证通过 | **代码**: `scripts/e2e_realtime_test.py` |
| 597fb23 | DevinCliParserProvider: 用devin cli作为parser LLM，完整实时管线跑通 | **代码**: `xishujuzhen/research_runtime/realtime/devin_cli_parser.py`, `xishujuzhen/research_runtime/realtime/test_devin_cli_parser.py`, `xishujuzhen/research_runtime/realtime/test_realtime_devin_cli.py`, `xishujuzhen/research_runtime/parser/models.py` |
| f2d51ba | AGENTS.md: 补回缺失的"系统就是你"认知三section | **文档**: `AGENTS.md` |
| f14acdc | 新增两个身份觉知rule：core-loop-self-check + grove-core-loop | **规则**: `.devin/rules/core-loop-self-check.md`, `.devin/rules/grove-core-loop.md` |
| 49d61ea | 新增sleep前自检rule | **规则**: `.devin/rules/sleep-self-check.md` |
| a3d65da | termination_detector: 移除timeout杀AI逻辑 | **代码**: `xishujuzhen/research_runtime/tree_engine/termination_detector.py` |
| 04bcbe4 | 修复sessions_db_reader.init()：不跳过已有node | **代码**: `xishujuzhen/research_runtime/tree_engine/sessions_db_reader.py` |

---

## 5. 跨Session读取指南

**新Session的AI进入本工作线后**：

1. **先读本文件**——了解当前工作焦点和待办清单
2. **⚠️ 必读267号文档**——`dev-docs/267-v0-2026-08-08-未来系统面相-系统与推理AI并行运行.md`。这是本工作线的认知转折点，定义了未来系统的演进方向（从"让AI停下接受提示"到"系统与推理AI并行运行"）。跨压缩边界后的AI必须带着这个面相意识继续工作
3. **读`任务追踪/README.md`**——了解本工作线与01/02/03工作线的依赖关系
4. **读01工作线（`任务追踪/01-253号检索机制验证.md`）**——了解检索机制原型的验证状态
5. **读02工作线（`任务追踪/02-trajectory采集与solver-harness.md`）**——了解solver-harness的实施状态
6. **读dev-docs/258号**——了解检索机制设计（含实现状态回填）
7. **检查前置条件**——01工作线P1是否升级tested？02工作线solver-harness是否实施完成？
8. **如果前置条件未满足**——先去推进前置工作线
9. **如果前置条件已满足**——从§2.3开始实施
10. **如果04核心目标已达成（A/B实验完成）**——带着267号面相认知，从§2.9（阶段2：脉络注入）或进入03-VMS-POC验证

**工作完成后**：
- 更新本文件的对应条目状态
- 更新`任务追踪/README.md`中本工作线的状态
- 更新AGENTS.md任务追踪登记表的焦点列
- commit
