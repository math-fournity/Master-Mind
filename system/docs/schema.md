# 数据结构设计说明书

**模块**：`system/schema.py`
**定义来源**：319号§1（形式化定义）+ 330号（双轨术语/FCA对应说明）

---

## 1. 概述

system/schema.py定义了第六代AI数学系统的所有数据结构——25个dataclass。这些数据结构是Pipe之间传递的数据的类型。

### 数据结构分类

| 分类 | dataclass | 说明 |
|---|---|---|
| 基础概念 | Problem, Hint, Tell, Trace | 系统的核心概念 |
| 脉络相关 | Vein, Segment, Branch, LevelView | 格化和trace识别的产物 |
| 树相关 | MathSituation, TreeEdge, TreeState | 引导树/解题树 |
| 过程输入 | Thinking, SolutionRecord | 解题引导/解答吸收的输入 |
| Pipe 0 | SolverInput, SolverOutput | Solver AI的输入输出 |
| Pipe 1 | AnalysisInput, AnalysisOutput | 脉络分析的输入输出 |
| Pipe 2 | MatchInput, MatchOutput, TraceTellMatch | Telling AI的输入输出 |
| Pipe 3 | GuideExpansionInput, GuideExpansionOutput | Guide AI的输入输出 |
| 其他 | DirectionExtractionOutput, KnowledgeDepositOutput, Session | 辅助数据结构 |

---

## 2. FCA术语映射（双轨术语——330号）

**双轨术语原则**：FCA语言用于术语规范化，不用于算法实现。工程术语trace/tell/hint/格化/Level视图保持不变——它们承载系统设计意图的语义，FCA术语无法承载。

### 核心术语映射

| 工程术语 | FCA术语 | 说明 |
|---|---|---|
| 脉络（Vein） | 形式上下文 (G, M, I) | G（对象集）= segments，M（属性集）= 所有段特征的并集，I（关系）= 段具有某个特征 |
| 段（Segment） | 对象 g ∈ G | 段是形式上下文的对象 |
| 段特征 | 属性 m ∈ M | segment_features对应对象g的属性集 g' = {m ∈ M \| (g, m) ∈ I} |
| 格化 | 计算概念格 B(G,M,I) | 在形式上下文上计算概念格 |
| Level视图（LevelView） | 形式概念 (A, B) | merged_segments对应外延A（extent），view_features对应内涵B（intent），level对应概念在Hasse图中的深度 |
| 闭元素 | 满足A''=A的子集A | Next Closure算法枚举所有闭元素 |
| trace | 概念内涵 B | trace对应FCA形式概念的内涵——一个可识别的思维模式的属性集 |
| 去特化 | 缩放（scaling） | trace去特化后存入tell库，对应FCA的跨上下文概念 |
| 可泛化 | 跨上下文普适性 | trace的"可泛化性"对应概念的"跨上下文普适性" |

### Level视图和FCA概念的对应

- **最细Level（Level 0）** = 最细概念——每个段是一个外延
- **最粗Level** = 最粗概念——所有段是一个外延
- **中间Level** = 中间概念——几个段合并成一个外延

**注意**：trace比FCA的内涵承载更多语义——trace强调"可泛化的思维模式"，这是工程人话的语义，FCA的"内涵"无法承载这个语义（双轨术语原则）。

### FCA立场声明

FCA语言用于术语规范化，不用于算法实现。system/vein_analysis.py选方式A——用提示词驱动AI做格化，不直接实现FCA的Next Closure/In-Close/Close-by-One算法。但提示词中用的术语（格化、Level视图、闭元素等）用FCA的数学定义来规范化，确保术语的精确性。

---

## 3. 核心数据结构详解

### Trace

trace——从脉络的某个Level视图上识别出的思维模式。trace是脉络分析阶段的产出，trace匹配阶段的输入。

**观察Level是参数不是属性**（08号分类学v2修正）：
- local：局部trace，来自单个段
- non_local：非局部trace，跨多个段
- global：全局trace，整个脉络层面

**FCA对应**：trace对应FCA形式概念的内涵B。trace去特化后存入tell库，对应FCA的跨上下文概念——在多个形式上下文中都出现的形式概念。trace的"可泛化性"对应概念的"跨上下文普适性"。

### Tell

tell——从推理AI的thinking中读出的分叉信号。tell有四个组成成分（000号文档）：
1. **branch_signal**：分叉信号——可以分叉但AI没分叉的位置
2. **branch_type**：分叉类型——翻译类型/操作路径类型/...
3. **unexplored_diagnosis**：未探索诊断——AI为什么没走这条路
4. **direction_matching**：方向匹配——从诊断到翻译方向的映射

**分类学四层位置**（313号§4.1）：
- domain：第一层——数论/代数/...
- trace_type：第二层——local/non_local/global
- segment_pattern：第三层——段结构模式（非局部trace）
- specific_concept：第四层——具体概念

### Segment

段——脉络中的一个推理步骤或一段推理。

**FCA对应**：段对应FCA形式上下文(G,M,I)中的对象g∈G。segment_features对应对象g的属性集g'={m∈M | (g,m)∈I}。

### LevelView

Level视图——脉络在某个Level上的看法（格化产物）。

**FCA对应**：Level视图对应FCA的形式概念(A,B)：
- merged_segments对应外延A（extent）——合并的段集合（对象集）
- view_features对应内涵B（intent）——这些段的共同特征（属性集）
- level对应概念在概念格Hasse图中的深度

---

## 4. 和运行代码的关系

system/schema.py是真正的运行定义——25个dataclass被system/中的代码直接import使用。

six/types.py（已删除，见343号方案）曾经是架构描述层面的dataclass定义，有16个dataclass。system/schema.py在six/types.py的基础上新增了9个运行需要的数据结构（AnalysisInput/AnalysisOutput/MatchInput/MatchOutput/TraceTellMatch/DirectionExtractionOutput/GuideExpansionInput/GuideExpansionOutput/KnowledgeDepositOutput/Session）。

本文件（schema.md）记录的是设计层面的说明——FCA对应说明、设计来源、分类学位置等。运行层面的字段定义看schema.py代码。

---

## 5. 来源文档

| 文档 | 内容 |
|---|---|
| 319号§1 | 形式化定义——所有dataclass的最初定义 |
| 330号 | FCA数学语言类比与术语规范化——21个术语的工程→FCA映射 |
| 000号 | 引导树闭环-识别端结构定义——Tell的四个成分 |
| 313号§4.1 | Tell分类学——分类维度四层 |
| 314号问题2 | 推理脉络的格化——Level视图和trace的关系 |
| 315号§6.2.2 | 解题引导中分叉位置本身可能就是trace |
