# Pass 2 原语提炼：fuxi（伏羲代，219-252号文档）

## 统计
- 输入思想片段数：958
- 筛选后原语候选数：约 220（去重前，含重复表述）
- 归并后原语数：61（16 existing + 45 new-candidate）
  - 操作原语：9 existing + 25 new = 34
  - 结构原语：7 existing + 20 new = 27
- 概念框架候选数：9
- 性质标准候选数：2
- 拒绝数：约 247

## 原语清单

---

### 一、已有原语（16个）——新来源补充

#### [existing] base-change（换基）
- **已有定义**：primitives/operational/base-change.md
- **新来源补充**：220-P4/P8/P14/P15/P18/P20/P22 补充了换基的子模式分类（冗余/隐藏乘积/虚假自由度/隐藏直和）、不变量识别操作、适用性判断、代价权衡；236-P5/P6 补充了换基作为"识别不自然→产生操作方向"的检索触发机制；239-P14 补充了子模式作为检索细粒度匹配维度；248-P33 补充了问题拓扑→思维拓扑映射架构
- **验证状态更新**：无变化（作为数学操作 tested，作为系统原语 untested）

#### [existing] non-specificity（非特定性）
- **已有定义**：primitives/operational/non-specificity.md
- **新来源补充**：224-P3/P31/P32 从拓扑连续性角度深化——非特定性是策略在拓扑τ开集上连续有效的自然推论；225-1-P5/P22/P23 补充了自然性四检查测试；226-P9 补充了可证交换条件；236-P6 补充了"边界以外可用性=非特定性=边界推进能力"；239-P19 补充了"方法从边界以外使用仍产生有用证书目标"
- **验证状态更新**：无变化（tested）

#### [existing] continuous-questioning（连续发问）
- **已有定义**：primitives/operational/continuous-questioning.md
- **新来源补充**：238-P28 补充六层框架（观察→联想→描述→尝试→推进→卡点处理）；238-P35 层间信息流动；238-P36 纯非特定Q序列设计；242-P1 6层元认知指令序列结构
- **验证状态更新**：无变化（tested，但243-P9指出必要性未验证）

#### [existing] safe-first-step（安全第一步）
- **已有定义**：primitives/operational/safe-first-step.md
- **新来源补充**：238-P29/P30 "描述题目结构形状"作为安全第一步的具体操作；252-P16 与连续发问的组合使用
- **验证状态更新**：无变化（tested，同continuous-questioning局限）

#### [existing] execution-contract（执行契约）
- **已有定义**：primitives/operational/execution-contract.md
- **新来源补充**：229-P1/P6/P7 四字段结构（改变什么处境/预期降低什么困难/编译成什么计算任务/返回后如何更新语义场）；230-P24 "后两项必须填"约束；235-P27 "预期降低"允许填"探索性移动"；236-P9 对应边界跨越四个环节；239-P20 完整四字段协议；252-P8/P10 与闭环循环集成
- **验证状态更新**：无变化（untested）。229-P13 风险：强制结构化可能丢失数学思考流动性

#### [existing] implicit-filtering（隐含筛选）
- **已有定义**：primitives/operational/implicit-filtering.md
- **新来源补充**：238-P32 "即使Q形式非特定，选择性引用AI内容已是特定化判断"；240-P9 "引导者通过选择性引用AI选的方向隐含确认正确路径"；242-P7 隐含筛选可能是成功关键的争议；243-P8 实验结论——非必要条件但可能提高效率
- **验证状态更新**：无变化（tested_negative）

#### [existing] minimal-knowledge-transfer（最小知识传递）
- **已有定义**：primitives/operational/minimal-knowledge-transfer.md
- **新来源补充**：238-P17 形式化目标 argmax ΣLevel(h_i)；241-P18 Level越高越偏思维模式；248-P18 完整回溯机制设计；249-P15 20万token分配方案；250-P25 受约束多目标选择问题形式化
- **验证状态更新**：无变化（partial）。243-P7 前提：被传递的知识必须是系统自身无法获取的

#### [existing] dfs-guidance（DFS引导）
- **已有定义**：primitives/operational/dfs-guidance.md
- **新来源补充**：238-P20/P21 DFS树结构（节点=AI状态，边=引导Q）和Level降序贪心策略；252-P3 "一次发一个Q，走不通就回溯"的树状探索
- **验证状态更新**：无变化（untested）

#### [existing] backtrack-fresh-session（回溯铁律）
- **已有定义**：primitives/operational/backtrack-fresh-session.md
- **新来源补充**：238-P22 三个原因（压缩边界风险/context污染/推理不可靠）；238-P23/P24 重放Q序列机制和A/A'有效性判断
- **验证状态更新**：无变化（untested）

#### [existing] certificate（证书）
- **已有定义**：primitives/structural/certificate.md
- **新来源补充**：227-P2/P3 六字段结构（claim/scope/strength/dependencies/checker/status）；228-v0-P2/P3 证书不是单一偏序而是带索引的证书范畴——固定claim和scope的纤维内有偏序；230-P6/P7 范围收缩不是加强；235-P9/P10 三类证书（正向/反驳/诊断反馈）
- **验证状态更新**：无变化（untested）

#### [existing] cognitive-activation（认知激活）
- **已有定义**：primitives/structural/cognitive-activation.md
- **新来源补充**：241-P10 guided_001实证证据；241-P36 Pipe间连接两种类型（数据传递 vs 认知激活）；252-P4 "一个Pipe发给另一个的不只是当前处境，还有你该往哪看"
- **验证状态更新**：无变化（partial）

#### [existing] data-pedestal（数据基座）
- **已有定义**：primitives/structural/data-pedestal.md
- **新来源补充**：231-P3 基本单位是"数学工程单元"（含10个字段）；231-P6 五层成熟度；232-P5 九类内容分基础层和派生层；234-P6/P7 按形式化边界关系分四阶段组织；235-P19/P20 数据基座是形式化边界的显式记录；239-P2/P4 完整四阶段定义
- **验证状态更新**：无变化（untested）

#### [existing] pipe
- **已有定义**：primitives/structural/pipe.md
- **新来源补充**：241-P05/P06 "Pipe只应看到上游传来的东西"的合法性判据；241-P07/P08/P09 三个Pipe角色定义；252-P06 AI在Pipeline网络中承载多种角色原语
- **验证状态更新**：无变化（untested）

#### [existing] math-reasoning-engine（数学推理引擎）
- **已有定义**：primitives/structural/math-reasoning-engine.md
- **新来源补充**：241-P37 可能还有子角色（猜想生成引擎/反例搜索引擎/表示变换引擎/证书验证引擎）；252-P06 作为Pipeline网络中的可放置Pipe
- **验证状态更新**：无变化（功能tested，角色untested）

#### [existing] pattern-recognition-engine（模式识别引擎）
- **已有定义**：primitives/structural/pattern-recognition-engine.md
- **新来源补充**：221-P06 两步执行（识别问题拓扑→映射到思维拓扑）；221-P13 三因子乘积（感知×匹配×判断不匹配）；236-P06 "识别不自然→产生操作方向"的成功标志；239-P15 模式识别是"元拓扑"
- **验证状态更新**：无变化（功能有争议tested，角色untested）

#### [existing] constraint-solver-engine（多约束求解引擎）
- **已有定义**：primitives/structural/constraint-solver-engine.md
- **新来源补充**：241-P09 "在多个约束下搜索满足条件的解或反例"的Pipe角色定义
- **验证状态更新**：无变化（功能tested，角色untested）

---

### 二、新原语候选——操作原语（25个）

#### [new-candidate] semantic-energy-descent（语义能量下降）
- **定义**：计算当前处境的六分量能量向量（表示复杂度/证书距离/自由度残差/粘合缺陷/反例压力/形式化缺口），以Pareto改善或受控交换为判据选择能降低能量的语义移动
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：每个分量有具体可计算定义（如表示复杂度=变量数+表达式长度，粘合缺陷=不一致局部证书对数），Pareto改善判据可机械执行
  - 可验证性：比较有能量引导 vs 无能量引导时AI的移动选择差异
  - 构造性：是引导信号生成器，放置在闭环中作为AI决策的输入
- **来源片段**：225-1-P18, 225-P13, 226-P11/P17/P18/P19, 227-P19/P20, 228-v0-P16, 230-P22/P23, 235-P18, 236-P22
- **溯源**：225号doc, 226号doc, 227号doc, 228号doc, 230号doc, 235号doc, 236号doc
- **验证状态**：untested
- **依赖关系**：依赖 certificate-ledger（证书距离需账本），支撑 dual-output-closed-loop

#### [new-candidate] three-stage-retrieval（三阶段检索）
- **定义**：检索分三阶段执行——粗筛用结构化字段匹配（处境类型+移动类型+证书类型），精化用图查询在依赖图中找连通路径，排序（可选）用向量检索在剩余候选中排序
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：每阶段有明确的查询操作（字段匹配→AQL图遍历→向量排序）
  - 可验证性：比较各阶段输出质量和召回率
  - 构造性：是检索管线组件，可放置在系统中
- **来源片段**：234-P10, 235-P22/P35/P36/P37/P38, 236-P1/P2, 239-P1, 247-P4, 252-P1
- **溯源**：234号doc, 235号doc, 236号doc, 239号doc, 247号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 dependency-graph-k, subgraph-extraction, seed-selection

#### [new-candidate] naturality-test（自然性测试）
- **定义**：换表示/换参数/取变体后，检查方法是否仍产生同类证书目标——先换表示再用方法 vs 先用方法再换表示，两条路径的证书目标应相容
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的操作步骤（换表示→应用方法→比较证书目标）
  - 可验证性：测试方法在变体上的稳定性，统计成功率
  - 构造性：是检索条目质量检查工具，用于决定模式是否入库
- **来源片段**：225-1-P5, 225-P22/P23, 226-P7/P13, 227-P7, 228-v0-P6, 230-P16/P17, 235-P15/P33, 237-P4, 239-P10
- **溯源**：225-1号doc, 225号doc, 226号doc, 227号doc, 228号doc, 230号doc, 235号doc, 237号doc, 239号doc
- **验证状态**：untested
- **依赖关系**：依赖 certificate-pullback, representation-atlas；约束于 criteria/naturality

#### [new-candidate] result-reflection（结果反射）
- **定义**：将经典计算的结果（成功/反例/障碍/未知）反射回语义场，改变AI的语义理解——成功则猜想过强、因式分解则隐藏结构可能是乘积、类型不匹配则对象边界未说清
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的反射操作（读取结果→更新处境字段）
  - 可验证性：比较有反射 vs 无反射时AI后续决策差异
  - 构造性：是闭环的关键环节，没有它闭环就断了
- **来源片段**：225-1-P4/P20, 225-P09/P30, 226-P6/P10, 228-v0-P18, 230-P25, 235-P28, 236-P5, 239-P22, 252-P10
- **溯源**：225-1号doc, 225号doc, 226号doc, 228号doc, 230号doc, 235号doc, 236号doc, 239号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 certificate-ledger, verifiable-compilation；与 verifiable-compilation 互为V-R对

#### [new-candidate] verifiable-compilation（可证化编译）
- **定义**：将AI提出的语义移动编译成可检查的证书目标集合——一个语义移动可能产生零个、一个或多个证书目标，每个目标指定可交给什么工具检查
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的编译操作（语义移动→证书目标列表）
  - 可验证性：检查编译出的目标是否确实可被工具检查
  - 构造性：是连接语义场和证书系统的桥梁
- **来源片段**：225-1-P8, 225-P09, 226-P5/P10, 227-P11, 230-P18, 235-P16, 252-P10
- **溯源**：225-1号doc, 225号doc, 226号doc, 227号doc, 230号doc, 235号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 certificate；与 result-reflection 互为V-R对

#### [new-candidate] stuck-detection（卡点检测）
- **定义**：检测AI是否卡住并分类卡住类型——区分"不知道下一步做什么"（方向缺失）和"知道方向但做不下去"（执行障碍），检测7种卡点类型（必要探索/语义重复/矛盾未处理/工具阻塞/表示不合适/策略耗尽/超时）
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的检测操作（阈值比较/字符串比较/计数）
  - 可验证性：比较检测结果与人工标注
  - 构造性：是检索的触发条件——不检测卡点就不知道何时该检索
- **来源片段**：223-P19, 242-P13, 250-P24, 252-P15
- **溯源**：223号doc, 242号doc, 250号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 dynamic-workspace；支撑 three-stage-retrieval（触发检索）

#### [new-candidate] four-gate-leak-audit（四门泄漏审计）
- **定义**：对提示内容执行四门检查——门1字面匹配（是否直接出现答案字面片段）、门2等价映射（是否包含答案等价表述）、门3候选空间缩减（是否把可能答案空间缩小）、门4盲恢复（撤掉提示后AI能否独立继续）
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：每门有明确的检查操作
  - 可验证性：比较审计通过 vs 未审计的提示的泄漏率
  - 构造性：是提示质量保证组件
- **来源片段**：248-P19, 249-P24, 250-P17, 251-P8, 252-P19/P24
- **溯源**：248号doc, 249号doc, 250号doc, 251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 truth-vault；约束于 non-specificity

#### [new-candidate] hint-gradient（提示梯度分级）
- **定义**：将提示按泄漏风险分为5级——Hint-0只提示检查类型（很低泄漏）、Hint-1提示思维操作（低）、Hint-2提示候选工具/概念（中）、Hint-3提示确定方向（高）、Hint-4提示具体步骤（很高），检索结果按梯度分级返回
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的分级标准和操作
  - 可验证性：比较不同级别提示的泄漏率和帮助率
  - 构造性：是信息流控制组件
- **来源片段**：250-P4, 250-P25, 251-P7, 252-P24
- **溯源**：250号doc, 251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：约束于 non-specificity, minimal-knowledge-transfer

#### [new-candidate] dual-route-comparison（双路线对照）
- **定义**：同一批问题用两条路线分别跑——单纯AI路线（不强制执行契约/不维护证书账本/不强制结果回流）vs 闭环路线（强制这三件事），控制变量（AI模型/Prompt/温度/Python计算相同），用统一指标比较
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的实验执行流程
  - 可验证性：比较两组指标差异
  - 构造性：是验证方法，用于验证闭环路线的增益
- **来源片段**：229-P4, 230-P26, 235-P29, 239-P30, 240-P10
- **溯源**：229号doc, 230号doc, 235号doc, 239号doc, 240号doc
- **验证状态**：untested
- **依赖关系**：依赖 execution-contract, certificate-ledger

#### [new-candidate] baseline-verification（裸跑基线验证）
- **定义**：在测试任何引导/检索机制之前，必须先验证无引导（裸跑）基线性能，确认系统裸跑确实做不出来——否则无法证明机制的价值
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的操作（不给任何提示让AI做题）
  - 可验证性：比较裸跑结果与引导后结果
  - 构造性：是实验设计的基础组件
- **来源片段**：243-P1/P2
- **溯源**：243号doc
- **验证状态**：tested（guided_003实验中已执行裸跑对照）
- **依赖关系**：支撑 dual-route-comparison

#### [new-candidate] causal-intervention-validation（因果干预验证）
- **定义**：验证一个Hint是"因果干预"而非"答案传递"——选取多个会在P处停滞的运行，在相同状态注入不超过预定H级别的X提示，设置未提示对照组，比较通过率差异
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的实验协议（选运行→注入提示→设对照组→比较）
  - 可验证性：比较干预组 vs 对照组的通过率
  - 构造性：是验证启发规则有效性的方法
- **来源片段**：250-P16, 251-P17, 252-P25
- **溯源**：250号doc, 251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 stuck-detection, hint-gradient；支撑 heuristic-rule-lifecycle, gain-attribution

#### [new-candidate] dead-end-marking（死路标记）
- **定义**：经典计算标记已验证不可行的路径为死路，形成搜索空间中的障碍集，为后续导航提供约束——避免重复走已验证不可行的路径
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的标记操作（验证不可行→写入死路集合）
  - 可验证性：比较有死路标记 vs 无标记时的搜索效率
  - 构造性：是搜索空间裁剪组件
- **来源片段**：224-P20, 228-v0-P5, 230-P31
- **溯源**：224号doc, 228号doc, 230号doc
- **验证状态**：untested
- **依赖关系**：依赖 dependency-graph-k

#### [new-candidate] counterexample-search（反例搜索）
- **定义**：经典计算搜索小模型、随机样本、极端边界和约束满足解，给出具体对象让猜想失败——反例作为高价值语义反馈改变AI方向
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的搜索操作（枚举小模型/边界情况）
  - 可验证性：比较有无反例搜索时AI的猜想修正率
  - 构造性：是负知识生产组件
- **来源片段**：228-v0-P3, 228-v0-P29, 230-P29
- **溯源**：228号doc, 230号doc
- **验证状态**：untested
- **依赖关系**：支撑 dead-end-marking, result-reflection

#### [new-candidate] subgraph-extraction（子图提取）
- **定义**：给定当前分析上下文，从依赖图中用BFS/DFS遍历提取相关的依赖子图（控制深度和大小），组织成合理大小的结构化文本呈现给AI作为提示
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的图遍历操作
  - 可验证性：比较不同提取策略的子图质量
  - 构造性：是检索的核心操作
- **来源片段**：223-P2/P9, 248-P5, 249-P5/P13, 250-P19, 252-P1
- **溯源**：223号doc, 248号doc, 249号doc, 250号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 dependency-graph-k, seed-selection；支撑 three-stage-retrieval

#### [new-candidate] seed-selection（种子选择）
- **定义**：三级种子选择流水线——第一级层次索引定位（问题领域→3层主题树）、第二级语义检索（问题embedding→top-20节点）、第三级图遍历扩展（BFS/DFS深度3-5层，剪枝）
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：每级有明确的查询操作
  - 可验证性：比较种子质量（与问题相关的节点比例）
  - 构造性：是检索的起点——先找到与问题最相关的知识节点
- **来源片段**：248-P10, 249-P14, 250-P18
- **溯源**：248号doc, 249号doc, 250号doc
- **验证状态**：untested
- **依赖关系**：依赖 dependency-graph-k；支撑 subgraph-extraction

#### [new-candidate] shape-matching（形状匹配）
- **定义**：不是基于"这道题能不能用反证法"（太宽泛），而基于"当前卡点的形状是否匹配反证法曾经成功突破过的形状"——先描述思维图中的局部形状，再在启发图中匹配规则
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的匹配操作（描述形状→子图模式匹配→guard条件检查）
  - 可验证性：比较形状匹配 vs 关键词匹配的启发命中率
  - 构造性：是启发规则触发的核心机制
- **来源片段**：238-P7/P12/P13/P14, 248-P16, 249-P34, 250-P7, 251-P28
- **溯源**：238号doc, 248号doc, 249号doc, 250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：依赖 thinking-trajectory-graph, heuristic-rule

#### [new-candidate] heuristic-rule-lifecycle（启发规则生命周期）
- **定义**：启发规则有完整生命周期管理——observed（从轨迹差分观察到）→candidate（已形式化）→intervened（已做最小提示干预）→validated（重复验证有效）→retired（模型升级后不再需要），candidate状态禁止在线匹配
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的状态转移操作
  - 可验证性：跟踪规则状态变化，检查是否经过验证才上线
  - 构造性：是启发规则质量管理组件
- **来源片段**：250-P13/P14/P42, 251-P5
- **溯源**：250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：依赖 heuristic-rule, causal-intervention-validation

#### [new-candidate] level-based-hint-ordering（Level排序提示）
- **定义**：提示生成器在选择提示时按Level排序，优先选高Level（更通用）的提示；当AI卡住时先给高Level提示，不够再逐步降低Level——形式化为 argmax ΣLevel(h_i) s.t. AI在H引导下完成解题
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的排序和贪心选择操作
  - 可验证性：比较不同Level排序策略的成功率和轮次
  - 构造性：是引导策略控制组件
- **来源片段**：238-P4/P17/P18/P19/P21, 241-P18, 242-P2, 248-P21, 249-P23, 252-P3
- **溯源**：238号doc, 241号doc, 242号doc, 248号doc, 249号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 level-perception；约束于 concepts/level-spectrum；支撑 minimal-knowledge-transfer

#### [new-candidate] certificate-pullback（证书拉回）
- **定义**：给定表示变换τ:S'→S，将S上的证书翻译到S'上的操作——这是跨表示检索的基础操作，使得在一个表示中获得的结论可以翻译到另一个表示
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的翻译操作（沿态射拉回证书）
  - 可验证性：检查拉回后的证书在新表示中是否有效
  - 构造性：是跨表示组合证书的基础
- **来源片段**：227-P14, 230-P21/P40, 235-P17
- **溯源**：227号doc, 230号doc, 235号doc
- **验证状态**：untested
- **依赖关系**：依赖 certificate, representation-atlas；支撑 naturality-test, obstruction-detection

#### [new-candidate] obstruction-detection（粘合障碍检测）
- **定义**：检查不同局部表示的局部证书在重叠处是否能粘合成全局证书，粘合失败分四级——descent failure→obstruction object→Čech 1-cocycle→H¹ class，失败时系统知道需要修复的是表示之间的翻译而非局部证明
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的检查操作（比较重叠处证书→分类失败级别）
  - 可验证性：检测到的障碍是否有数学内容（能否指导修复方向）
  - 构造性：是诊断信号生成器，指导AI修复表示翻译
- **来源片段**：225-1-P15/P16, 226-P15/P16, 227-P18, 228-v0-P4, 230-P8, 235-P12, 236-P21, 239-P27
- **溯源**：225-1号doc, 226号doc, 227号doc, 228号doc, 230号doc, 235号doc, 236号doc, 239号doc
- **验证状态**：untested
- **依赖关系**：依赖 representation-atlas, certificate-pullback

#### [new-candidate] dual-output-closed-loop（单任务双产出）
- **定义**：求解闭环运行一次，同时产出问题的解和数据基座条目——每步语义移动被记录、每个证书目标被编译、每个验证结果被回写，不需要单独做抽取
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的操作（在闭环每步自动记录条目）
  - 可验证性：检查运行后是否产出了数据基座条目
  - 构造性：是数据基座增长机制——没有它数据基座只能靠人工抽取
- **来源片段**：234-P1/P2, 235-P24, 236-P18, 237-P9, 239-P21, 252-P12
- **溯源**：234号doc, 235号doc, 236号doc, 237号doc, 239号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 execution-contract, data-pedestal, certificate-ledger

#### [new-candidate] gain-attribution（增益归因）
- **定义**：对每次干预/引导，验证并归因其产生的增益——检索到的Pattern是否真正帮助了解题，增益来自哪个Pattern
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的归因操作（比较干预前后状态变化→匹配到具体Pattern）
  - 可验证性：比较归因结果与人工分析
  - 构造性：是启发规则验证的闭环环节
- **来源片段**：252-P19/P25
- **溯源**：252号doc
- **验证状态**：untested
- **依赖关系**：依赖 causal-intervention-validation

#### [new-candidate] honest-downgrade（诚实降级）
- **定义**：当新证据出现时，原语的验证状态应当动态降级（如从tested降为partial），并记录降级原因——验证状态不是一次性标签，而是随证据持续更新的
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的状态更新操作（新证据→评估→降级/升级→记录原因）
  - 可验证性：跟踪状态变化历史，检查是否与证据一致
  - 构造性：是知识库完整性维护组件
- **来源片段**：243-P5, 241-P38, 252-P19
- **溯源**：243号doc, 241号doc, 252号doc
- **验证状态**：tested（guided_003后non-specificity从tested_negative升级为tested；243后cognitive-activation降为partial）
- **依赖关系**：无

#### [new-candidate] progressive-pattern-extraction（渐进式模式提取）
- **定义**：模式提取不是在解答末尾标注"此题用了反证法"（总结性的），而是在解答的每个关键转折点标注"这里从正面假设转向了反面假设"（过程性的）
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的标注操作（在每个转折点标注模式）
  - 可验证性：比较过程性标注 vs 总结性标注的检索命中率
  - 构造性：是模式库构建的核心操作
- **来源片段**：238-P8/P9
- **溯源**：238号doc
- **验证状态**：untested
- **依赖关系**：依赖 thinking-trajectory-graph

#### [new-candidate] level-perception（Level感知）
- **定义**：Level不是被算法赋值的，而是通过AI的相对比较感受出来的——把两个元素放在一起，AI能感知"这个比那个更抽象/更泛化"
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的操作（让AI比较两个元素的抽象度）
  - 可验证性：比较AI的Level感知与专家判断的一致性
  - 构造性：是Level标签的生产方式——没有它依赖图中的Level标签无法填充
- **来源片段**：238-P3/P5, 241-P18, 244-P19
- **溯源**：238号doc, 241号doc, 244号doc
- **验证状态**：untested
- **依赖关系**：约束于 concepts/level-spectrum；支撑 level-based-hint-ordering

#### [new-candidate] multi-level-verification（多级验证）
- **定义**：对AI输出执行四种验证——形式化验证（证明步骤合法性）、约束求解（约束是否满足）、类型检查（类型是否匹配）、知识库查询（引用的定理是否存在），每种验证有不同粒度和速度
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：每种验证有明确的检查操作
  - 可验证性：比较有验证 vs 无验证时AI输出的错误率
  - 构造性：是输出质量保证组件
- **来源片段**：223-P3/P4, 224-P5, 228-v0-P28, 249-P28
- **溯源**：223号doc, 224号doc, 228号doc, 249号doc
- **验证状态**：untested
- **依赖关系**：支撑 result-reflection, dead-end-marking

#### [new-candidate] meta-normal-separation（meta/normal操作分离）
- **定义**：meta operation（拓扑规划、拓扑验证、审计）和normal operation（转译、分析）必须由不同AI实例完成，防止审计者与被审计者耦合
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的操作（分配不同AI实例给不同操作类型）
  - 可验证性：比较有分离 vs 无分离时审计的独立性
  - 构造性：是审计完整性保障组件
- **来源片段**：248-P7, 249-P20
- **溯源**：248号doc, 249号doc
- **验证状态**：untested
- **依赖关系**：无

#### [new-candidate] spiral-loop-detection（螺旋环路检测）
- **定义**：依赖图中存在环路（非DAG），需区分平面环路（循环论证，应停止追溯）和螺旋上升环路（深化分析，应继续追溯），判别标准是追溯一圈后是否产生新的判断维度
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的检测操作（追溯环路→检查是否有新维度）
  - 可验证性：比较分类结果与专家判断
  - 构造性：是依赖图遍历控制组件
- **来源片段**：249-P4, 236-P14
- **溯源**：249号doc, 236号doc
- **验证状态**：untested
- **依赖关系**：依赖 dependency-graph-k

#### [new-candidate] topology-coverage-verification（拓扑覆盖验证）
- **定义**：在转译前先构造展开图拓扑骨架G'_topo（纯结构无文字），用AQL集合差集验证G'_topo覆盖G的所有节点/边/跨领域边/螺旋环路圈数，实现确定性验证
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的验证操作（构造骨架→AQL差集查询）
  - 可验证性：检查覆盖是否完整
  - 构造性：是图展开质量保证组件
- **来源片段**：248-P6, 248-P14, 249-P6/P33
- **溯源**：248号doc, 249号doc
- **验证状态**：untested
- **依赖关系**：依赖 dependency-graph-k

#### [new-candidate] incremental-context-compilation（增量上下文编译）
- **定义**：上下文编译器不能只在任务开始时工作一次，而应在每次状态变化后增量工作——Q_t + 当前思维图T_t → 匹配启发关系 → 选择最小激活包 → 编译为增量提示
- **类型**：操作原语
- **三判据验证**：
  - 可执行性：有明确的增量更新操作
  - 可验证性：比较有增量 vs 全量编译的效率和效果
  - 构造性：是上下文管理效率组件
- **来源片段**：250-P6, 251-P11
- **溯源**：250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：依赖 dynamic-workspace, heuristic-rule

---

### 三、新原语候选——结构原语（20个）

#### [new-candidate] certificate-ledger（证书账本）
- **定义**：系统在时刻t的状态是证书偏序C的向下封闭理想I_t——如果c'∈I_t且c→c'（c'加强c），则c∈I_t；单调增长I_t⊆I_{t+1}（每一步只加证书不删），已确认证书不会无声消失
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为数据库中的证书集合+偏序索引
  - 可验证性：检查账本是否单调增长、是否向下封闭
  - 构造性：是已验证知识的累积存储——没有它每次推理从零开始
- **来源片段**：225-P08, 226-P3/P6, 228-v0-P7, 230-P15, 235-P11, 236-P8, 239-P8, 252-P11
- **溯源**：225号doc, 226号doc, 228号doc, 230号doc, 235号doc, 236号doc, 239号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 certificate；支撑 semantic-energy-descent, result-reflection, dual-route-comparison

#### [new-candidate] representation-atlas（表示图册）
- **定义**：一个处境不能被单一表示完全看清，需要一组可切换、可重叠、可拼合的局部表示（图册A(S)），每种表示是一个能看清某些结构的局部视角——包含原始表示、规范化表示、对偶表示、形式化表示
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为处境对象中的多表示字段
  - 可验证性：检查图册是否覆盖处境的所有结构特征
  - 构造性：是多视角检索的基础结构
- **来源片段**：225-P04, 225-P17, 226-P12, 227-P14/P15/P16, 230-P20/P40, 235-P17, 236-P15, 239-P12
- **溯源**：225号doc, 226号doc, 227号doc, 230号doc, 235号doc, 236号doc, 239号doc
- **验证状态**：untested
- **依赖关系**：支撑 certificate-pullback, obstruction-detection, naturality-test

#### [new-candidate] three-graph-architecture（三图架构）
- **定义**：系统由三张图构成——K数学知识图（客观依赖关系）、T外显思维图（Agent实际思维轨迹）、H启发激活图（条件→动作→效果证据），三图是投影而非独立真相库
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为ArangoDB中的三个图集合
  - 可验证性：检查三图是否正确分离、投影关系是否成立
  - 构造性：是系统核心数据架构
- **来源片段**：248-P3, 249-P9, 250-P1/P39, 251-P1
- **溯源**：248号doc, 249号doc, 250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：包含 dependency-graph-k, thinking-trajectory-graph, heuristic-rule

#### [new-candidate] dynamic-workspace（动态工作区）
- **定义**：系统在时刻t的完整状态用六元组表示——V_t（已验证核心，只增不减）、F_t（猜想前沿，可升级或被否定）、O_t（开放义务，AND/OR超图）、R_t（表示状态）、E_t（证据）、U_t（未解决问题），状态从事件流归约得出
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为运行时状态容器
  - 可验证性：检查状态是否正确从事件流归约
  - 构造性：是运行时状态管理的基础结构
- **来源片段**：250-P11, 251-P2/P29, 252-P5
- **溯源**：250号doc, 251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 event-sourcing；支撑 stuck-detection, incremental-context-compilation

#### [new-candidate] heuristic-rule（启发规则）
- **定义**：H图中的启发边不是普通边，而是带条件的图改写规则——(L, guard) ⇒ R，L=LHS当前思维图中应出现的局部子图，guard=上下文/时序/模型/失败类型等条件，R=RHS应加入的概念/子目标/工具/反例方向
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为ArangoDB中的规则集合
  - 可验证性：检查规则是否正确匹配和触发
  - 构造性：是启发式检索的核心数据结构
- **来源片段**：248-P17, 249-P10, 250-P2/P3/P35, 251-P5/P6
- **溯源**：248号doc, 249号doc, 250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：依赖 thinking-trajectory-graph；支撑 shape-matching, heuristic-rule-lifecycle, incremental-context-compilation

#### [new-candidate] event-sourcing（事件溯源）
- **定义**：研究过程中的每一步都是不可变的事件，系统在第t时刻的状态是这些事件的投影——从所有已发生事件中归约出来的当前快照，事件一旦发生就不可修改
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为不可变事件日志+状态归约器
  - 可验证性：重放事件流，检查状态重建一致性
  - 构造性：是运行时架构的基础——支持回放、审计、恢复
- **来源片段**：250-P9/P10/P37, 251-P9/P10, 252-P14
- **溯源**：250号doc, 251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：支撑 dynamic-workspace

#### [new-candidate] truth-vault（真值保险库）
- **定义**：答案和完整证明存储在隔离的truth_vault collection中，访问权限严格限制——写入仅truth_curator，读取仅auditor，Controller和其他角色无权访问
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为数据库中的隔离集合+权限控制
  - 可验证性：检查答案是否被正确隔离、无未授权访问
  - 构造性：是信息隔离的最高级别保障
- **来源片段**：248-P19, 250-P22, 251-P16, 252-P19
- **溯源**：248号doc, 250号doc, 251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：支撑 four-gate-leak-audit

#### [new-candidate] obligation-hypergraph（义务超图）
- **定义**：开放义务用AND/OR有向超图表达——AND约束（所有子目标都必须解决）、OR约束（任一路径成功即可），超边e=(source, {targets}, type)记录义务的分解结构
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为ArangoDB中的超图集合
  - 可验证性：检查义务是否被正确分解和追踪
  - 构造性：是目标管理结构——支持复杂证明的子目标追踪
- **来源片段**：250-P12, 251-P4
- **溯源**：250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：支撑 dynamic-workspace

#### [new-candidate] three-layer-recording（三层记录）
- **定义**：运行时记录分三层——层次1 devin cli实例轨迹（外部层，终端实际发生什么）、层次2 系统内部结构化执行日志（中间层，系统做了什么决策和为什么）、层次3 数学大师思路轨迹（内层，AI的数学推理过程）
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为三层日志系统
  - 可验证性：检查三层记录是否完整、是否可交叉验证
  - 构造性：是审计基础设施
- **来源片段**：248-P22, 250-P31, 251-P18
- **溯源**：248号doc, 250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：无

#### [new-candidate] topology-feature-vector（拓扑特征向量）
- **定义**：用七个维度（约束类型、结论类型、核心鸿沟、关键桥梁、极值结构、修正来源、稳定性机制）构成的结构化特征向量来表示一个问题的拓扑；用五个维度（输入形状、操作类型、输出形状、适用条件、失败条件）表示思维模式的拓扑
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为问题/模式的特征向量字段
  - 可验证性：检查同一拓扑的题目是否共享特征向量
  - 构造性：是检索索引的结构化表示
- **来源片段**：219-P2/P3, 219-P9/P12, 221-P4/P18/P19
- **溯源**：219号doc, 221号doc
- **验证状态**：untested
- **依赖关系**：支撑 three-stage-retrieval（粗筛匹配维度）

#### [new-candidate] thinking-trajectory-graph（思维轨迹图）
- **定义**：T图记录Agent的实际思维轨迹——一次运行的事件序列，包括AI做了什么操作、得到什么结果、在哪里卡住、在哪里突破，是启发规则匹配的输入
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为ArangoDB中的事件图
  - 可验证性：检查轨迹是否完整记录了AI的实际推理过程
  - 构造性：是启发规则匹配和模式提取的基础
- **来源片段**：248-P3, 249-P9, 250-P1/P15
- **溯源**：248号doc, 249号doc, 250号doc
- **验证状态**：untested
- **依赖关系**：支撑 shape-matching, heuristic-rule, progressive-pattern-extraction

#### [new-candidate] role-isolation-matrix（角色隔离矩阵）
- **定义**：系统功能拆分为8个隔离角色（solver/event_capture/state_reducer/retriever/heuristic_matcher/verifier/auditor/controller），每个角色有明确的职责和权限边界，角色间通过受控接口交互，每个角色在启动时获得一组CapabilityToken
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为角色配置+权限管理系统
  - 可验证性：检查角色间是否有信息越权流动
  - 构造性：是系统架构组件——防止知识泄漏和职责混淆
- **来源片段**：250-P20/P21, 251-P14/P15, 252-P23
- **溯源**：250号doc, 251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 pipe

#### [new-candidate] dependency-graph-k（依赖图K）
- **定义**：K数学知识图的形式化定义——G = (V, E, C, L, K)，V=节点集，E=边集，C=跨领域边，L=螺旋环路集，K=知识内容映射；四种边类型：知识依赖边、工具适用边、跨领域映射边、证明策略边
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为ArangoDB图集合
  - 可验证性：检查图是否正确反映数学知识依赖关系
  - 构造性：是检索机制的核心数据结构
- **来源片段**：223-P8, 247-P2, 248-P2, 249-P2/P3, 250-P1
- **溯源**：223号doc, 247号doc, 248号doc, 249号doc, 250号doc
- **验证状态**：untested
- **依赖关系**：支撑 subgraph-extraction, seed-selection, dead-end-marking, spiral-loop-detection, topology-coverage-verification

#### [new-candidate] schema-freezing（Schema冻结）
- **定义**：将8类数据结构的Schema设为不可变（Task/Workspace/Event/Obligation/Representation/Evidence/HeuristicRule/CognitionUnit），确保数据结构字段定义在运行时不被修改，为检索提供稳定的查询接口
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为Schema定义文件+运行时校验
  - 可验证性：检查Schema是否在运行期间保持不变
  - 构造性：是数据结构稳定性保障
- **来源片段**：248-P13, 250-P27, 251-P22
- **溯源**：248号doc, 250号doc, 251号doc
- **验证状态**：untested
- **依赖关系**：无

#### [new-candidate] multi-level-knowledge-extraction（多层知识提取）
- **定义**：从题解中提取三个层次的知识——L1解题思路（具体步骤，直接记录）、L2数学思维（思维模式，AI二次分析抽象）、L3范式思维（跨领域复用，改变图结构，AI三次分析综合），可选L4哲学/世界观层
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为知识提取管线
  - 可验证性：检查提取的知识层次是否正确
  - 构造性：是知识库构建的核心结构
- **来源片段**：248-P23/P24, 249-P7, 250-P29
- **溯源**：248号doc, 249号doc, 250号doc
- **验证状态**：untested
- **依赖关系**：依赖 thinking-trajectory-graph；支撑 data-pedestal

#### [new-candidate] failure-boundary-record（失败边界记录）
- **定义**：记录哪些相似命题不成立、哪些条件删掉会失败、哪些指数或常数是错的——失败边界是数据基座的一等公民，可作为检索对象避免重复探索已知不可行的方向
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为数据基座中的失败边界字段
  - 可验证性：检查失败边界是否正确标识了不可行方向
  - 构造性：是负知识存储结构
- **来源片段**：231-P15, 234-P16, 235-P34, 239-P11
- **溯源**：231号doc, 234号doc, 235号doc, 239号doc
- **验证状态**：untested
- **依赖关系**：依赖 data-pedestal；支撑 dead-end-marking

#### [new-candidate] pattern-library（模式库）
- **定义**：模式库不只是写着"换基""对偶""归纳"，而是带着触发条件、计算接口、证书模板和失败边界——每个模式附带适用信号、证书模板、失败案例、反例族和验证脚本，是实验室的技术积累
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为模式库集合（每个模式带完整元数据）
  - 可验证性：检查模式是否随闭环运行真实增长
  - 构造性：是可迁移知识的存储结构
- **来源片段**：225-P14, 228-v0-P11/P20, 230-P37, 235-P32/P39, 236-P10, 239-P09
- **溯源**：225号doc, 228号doc, 230号doc, 235号doc, 236号doc, 239号doc
- **验证状态**：untested
- **依赖关系**：依赖 data-pedestal, naturality-test；支撑 three-stage-retrieval

#### [new-candidate] structured-document-index（结构化文档索引）
- **定义**：为每个文档打上二元相关性标签+多维类型标签+压缩摘要+关键段落行号范围+语义段落名称，文档间的引用关系构成依赖图可用于检索时的关联扩展
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为文档索引表
  - 可验证性：检查索引是否正确覆盖文档内容
  - 构造性：是文档检索的基础结构
- **来源片段**：247-pass1-P1/P2/P3/P4/P5/P7/P9/P10/P11
- **溯源**：247号doc（pass1-results）
- **验证状态**：tested（Pass 1已执行，产出了结构化索引）
- **依赖关系**：支撑 three-stage-retrieval

#### [new-candidate] checkpoint-continuation（检查点续行）
- **定义**：当执行过程中出现失败时，从最近的checkpoint恢复继续执行，而不是从头开始——支持基于断点的检索和恢复
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为checkpoint存储+恢复机制
  - 可验证性：比较从checkpoint恢复 vs 从头开始的效率
  - 构造性：是长流程恢复组件
- **来源片段**：251-P12, 252-P15
- **溯源**：251号doc, 252号doc
- **验证状态**：untested
- **依赖关系**：依赖 event-sourcing

#### [new-candidate] version-chain（版本链）
- **定义**：用版本链（cog_versions集合+cog_version_edges版本链边）处理认知迭代——认知不是简单替换而是演化，每个认知单元有版本历史，版本之间有演化关系
- **类型**：结构原语
- **三判据验证**：
  - 可执行性：可放置为ArangoDB中的版本链集合
  - 可验证性：检查版本链是否正确记录了认知演化
  - 构造性：是认知管理的基础结构
- **来源片段**：249-P30, 221-P15
- **溯源**：249号doc, 221号doc
- **验证状态**：untested
- **依赖关系**：无

---

## 概念框架候选

### [concept] problem-topology-mapping（问题拓扑→思维拓扑映射）
- **定义**：数学思维有拓扑结构——问题有"拓扑"（相似的问题彼此靠近），思维有"拓扑"（相似的策略彼此靠近），模式识别是从问题拓扑到思维拓扑的映射
- **为何不是原语**：不满足构造性——这是理解系统设计为什么有效的视角，不是用来构造系统的积木。具体的映射操作（如形状匹配、拓扑特征向量）才是原语
- **来源片段**：219-P13, 220-P17, 221-P6/P7, 224-P21/P22, 224-P33, 236-P4, 239-P15

### [concept] fibration-framework（纤维化框架）
- **定义**：整个框架的核心结构是问题空间上的纤维化——基空间P（所有问题+拓扑τ）、纤维F_p（问题p的所有解题路径）、投影π（从解题路径映射回它解决的问题）
- **为何不是原语**：不满足可执行性——这是数学形式化框架，描述系统的数学结构，不是可直接执行的操作或可放置的组件。具体的操作（如路径导航、死路标记）才是原语
- **来源片段**：224-P6/P7/P8/P11/P12/P13/P14/P16/P17/P18/P33

### [concept] v-r-adjunction（V-R伴随）
- **定义**：可证化V（语义→证书）和反射R（证书→语义）形成某种双向连接，候选结构从强到弱包括lax adjunction、Galois connection、profunctor、Kleisli范畴——是闭环的数学形式化
- **为何不是原语**：不满足可执行性——这是数学形式化描述，具体的操作（verifiable-compilation和result-reflection）才是原语
- **来源片段**：225-1-P10, 225-P09, 226-P10, 228-v0-P14, 230-P18, 235-P16, 239-P07

### [concept] energy-as-functor（能量函子）
- **定义**：能量下降形式化为从语义场范畴Σ到预序集的函子——能量是一个函子，AI在语义场中的移动使能量函子值下降
- **为何不是原语**：不满足可执行性——这是数学形式化描述，具体的操作（semantic-energy-descent）才是原语
- **来源片段**：225-1-P18, 225-P13, 226-P11

### [concept] design-self-bootstrapping（设计自举）
- **定义**：设计过程是自举的循环——用原语设计系统→发现系统和预期之间的差距→用系统求解如何在原语集合上设计下一代系统→发现新原语→循环，与编译器自举同构
- **为何不是原语**：不满足构造性——这是理解设计过程的视角，不是构造系统的积木
- **来源片段**：246-P8/P9/P13

### [concept] three-plane-architecture（三平面架构）
- **定义**：系统分为知识平面（知道什么）、研究运行平面（怎么工作）、控制平面（如何保证不失控），三平面分离关注点
- **为何不是原语**：不满足构造性——这是理解系统架构的视角，具体的组件（如三图架构、角色隔离矩阵）才是原语
- **来源片段**：248-P4, 248-P41

### [concept] nine-basic-axioms（九条基础公理）
- **定义**：系统建立在九条基础公理之上——固定任务与动态状态分离、数学真值/Agent信念/可观测事件/启发策略分离、只建模可观察研究产物、已验证核心与猜想前沿分离等
- **为何不是原语**：不满足可执行性——这是设计约束/信念框架，不是可执行操作。具体的操作和结构（如dynamic-workspace、event-sourcing）才是原语
- **来源片段**：248-P30, 249-P29, 250-P34, 251-P27

### [concept] phenomenon-boundary-structure-layers（现象/边界/结构三层）
- **定义**：现象层（实际发生了什么）、边界层（边界在推进）、结构层（数学形状）是同一闭环过程的三种描述——结构层的每个概念只有在忠实描述了现象层和边界层时才获得正当性
- **为何不是原语**：不满足构造性——这是理解系统的元视角，不是构造系统的积木
- **来源片段**：236-P23, 239-P33

### [concept] spiral-vs-planar-loop（螺旋上升vs平面环路）
- **定义**：检索-引导过程应该是螺旋上升——返回同一抽象状态类但更细粒度进展，而非平面环路——不同时间事件投影回同一规范化状态无改善
- **为何不是原语**：不满足可执行性——这是对系统行为的描述性概念，具体的检测操作（spiral-loop-detection）才是原语
- **来源片段**：236-P14

---

## 性质标准候选

### [criterion] auditability（可审计性）
- **定义**：每个关键想法从哪里来、解决了什么结构压力、产生了什么证书目标，都应该能追溯——检索过程必须可审计；计算过程可记录、可重复、可复查
- **为何不是原语**：不满足可执行性——这是判断系统设计好坏的标准，不是可执行操作。具体的审计操作（如three-layer-recording、gain-attribution）才是原语
- **来源片段**：225-P24, 223-P27, 230-P36, 236-P27, 251-P30

### [criterion] monotone-growth（单调增长）
- **定义**：数据基座中证书单调增长，形式化边界推进不可逆——已确认证书不应无声消失，要么保留、要么被标注适用范围更窄、要么被更强证书替代；AI感知非单调，边界以外可修正
- **为何不是原语**：不满足可执行性——这是判断证书系统好坏的标准，具体的结构（如certificate-ledger）才是原语
- **来源片段**：226-P3, 228-v0-P7, 230-P15, 233-P9, 235-P4, 236-P28

---

## 拒绝清单（批量列出）

- 拒绝数：约 247
- 主要拒绝原因类型：

### 1. 数学形式化但未操作化（约50个）
这些片段用范畴论/拓扑学/层论等数学语言描述系统结构，但停留在形式化层面，没有对应的可执行操作。具体的操作化版本已被提取为原语。

代表片段：225-1-P6/P7/P14（Σ/C/Grothendieck拓扑形式化）, 226-P1/P2/P4（六种态射/三种箭头形式化）, 227-P8/P12/P13/P17（语义移动五层/局部证书预层/Site从可粘合覆盖族长出）, 228-v0-P5（态射加标注替代分层）, 230-P10/P11/P12/P18/P20/P21（Σ范畴/C偏序/V-R候选/图册/site）, 235-P14/P17（Σ是范畴/覆盖和site）, 236-P13/P23/P25（C=已征服领土/现象边界结构三层/工程单元字段对应数学结构）, 239-P7/P25/P33（Σ和C定义/工程单元对应数学结构/三层工作）

### 2. 设计细节/实现选择（约40个）
这些片段描述了具体的实现选择（如token分配、数据格式、工具选型），是设计决策而非可复用原语。

代表片段：223-P10/P11（状态追踪组件/启发规则组件——已被event-sourcing和heuristic-rule覆盖）, 248-P8/P9/P29（ArangoDB选型/三级访问架构/20万token分配）, 249-P11/P15/P16/P27/P28（ArangoDB选型/token分配/冷温热微包四级/arXiv管道/三层验证器阶梯——是实现细节）, 250-P28/P35/P43/P44（五正交字段/稀疏矩阵格子内容/多元关系柯里化/run目录归档）, 251-P23/P24（骨架文件协调/参考文档分配——是文档编写流程细节）

### 3. 描述性陈述/AI能力描述（约60个）
这些片段描述了AI或经典计算的能力/角色/性质，是对已有原语或概念的描述性补充，不是独立的可执行操作。

代表片段：223-P5/P6/P7（AI识别模式/判断不自然/理解语义——是AI能力描述）, 224-P7/P8（AI做四件事/经典计算做四件事——是角色描述）, 225-P25/P26（AI做七件事/经典计算是一组证书内核——是角色描述）, 228-v0-P1/P2/P3（AI压缩模糊意义/经典计算切割/经典计算搜索——是能力描述）, 233-P6/P7（AI黑盒能力/经典计算操作能力——是能力描述）, 235-P5/P6/P7（AI处理未形式化/经典计算精确执行/经典计算产生结构——是能力描述）

### 4. 已有概念/原语的重述（约50个）
这些片段是对已有概念框架或原语的重复表述，没有新增信息。

代表片段：220-P1/P2/P3（参数空间走/近似点修正/约束消解——是换基的具体数学技巧）, 221-P1/P2/P3（检索由不自然触发/匹配目标是不匹配/不匹配是拓扑特征——是问题拓扑映射概念的重述）, 224-P1/P9/P10/P14/P15/P19/P24/P27/P28/P30（策略在拓扑上连续/解题循环/纤维连通/τ近似/启发式是梯度/分工原则/AI-经典对偶/跨领域类比——是纤维化框架和两种计算概念的重述）, 230-P1/P2/P3/P4（AI压缩/问题变形/经典计算产生结构/迁移是表示变换下保持意义——是已有概念的重述）, 235-P1/P5/P6/P7/P8（知识分两种/问题变形/经典计算产生结构/非特定性是表示变换下保持意义——是已有概念的重述）

### 5. 实验设计细节（约25个）
这些片段描述了具体实验的控制变量、指标定义、结果分类等，是实验执行细节而非系统设计原语。

代表片段：229-P10/P11（对照实验控制变量/不预设高阶抽象框架——是方法论约束）, 242-P6/P9/P11/P12（维度矩阵/三种实验结果/物理隔离工作目录/两层超时——是实验设计细节）, 243-P6/P7/P9（路径分化作为证据/最小知识传递前提/多轮引导必要性——是实验结论）, 247-P8/P12/P16/P17（正反例规则/宽松筛选/判断标准一致性/宁可多选——是检索方法论细节）

### 6. 数学技巧/具体操作（约22个）
这些片段描述了具体的数学解题技巧（如参数空间走步、近似点修正），是数学操作而非系统设计原语。

代表片段：220-P1（参数空间沿方向走）, 220-P2（到达近似点量化偏差修正）, 220-P3（约束消解降维）, 220-P6（等价类典范代表）, 220-P7（不同表示浮现不同结构）, 220-P21（表面自由度被全局约束削减）, 220-P22（隐含全局约束变成显式坐标值）

---

## 依赖关系总览

```
dependency-graph-k ──┬── subgraph-extraction ── three-stage-retrieval
                     ├── seed-selection ─────── subgraph-extraction
                     ├── dead-end-marking
                     ├── spiral-loop-detection
                     └── topology-coverage-verification

certificate ──┬── certificate-ledger ──┬── semantic-energy-descent
              │                         ├── result-reflection
              │                         └── dual-route-comparison
              ├── certificate-pullback ──┬── naturality-test
              │                          └── obstruction-detection
              └── verifiable-compilation ── result-reflection (V-R对)

representation-atlas ──┬── certificate-pullback
                       ├── obstruction-detection
                       └── naturality-test

event-sourcing ──┬── dynamic-workspace ──┬── stuck-detection
                  │                       └── incremental-context-compilation
                  └── checkpoint-continuation

thinking-trajectory-graph ──┬── heuristic-rule ──┬── shape-matching
                             │                    ├── heuristic-rule-lifecycle
                             │                    └── incremental-context-compilation
                             └── progressive-pattern-extraction

truth-vault ── four-gate-leak-audit

stuck-detection ──┬── causal-intervention-validation ──┬── heuristic-rule-lifecycle
                   │                                    └── gain-attribution
                   └── three-stage-retrieval (触发)

data-pedestal ──┬── dual-output-closed-loop
                ├── failure-boundary-record
                ├── pattern-library
                └── multi-level-knowledge-extraction

pipe ── role-isolation-matrix
```

## 关键发现

1. **伏羲代是原语密度最高的一代**：958个片段中提炼出45个新原语候选，远超已有16个。原因是伏羲代（219-252号）是系统设计最密集的时期，涵盖了从拓扑化研究到完整技术说明书的全过程。

2. **结构原语远多于操作原语的已验证比例**：45个新候选中只有2个tested（baseline-verification和structured-document-index），其余全部untested——伏羲代的设计大量停留在纸面，尚未落地实验。

3. **检索机制相关原语形成完整链条**：从seed-selection→subgraph-extraction→three-stage-retrieval，配合stuck-detection触发、shape-matching匹配、heuristic-rule执行，构成了完整的检索管线。

4. **V-R闭环是伏羲代的核心架构贡献**：verifiable-compilation（V）和result-reflection（R）构成的闭环，配合certificate-ledger、semantic-energy-descent、execution-contract，形成了完整的闭环推进架构。

5. **大量数学形式化被正确归为概念/拒绝**：225-227号的范畴论形式化（Σ/C/V-R/能量函子/Grothendieck拓扑）虽然数学上优美，但不满足可执行性——它们的操作化版本（如certificate-pullback、obstruction-detection）才是原语。
