# Pipe 0：拓扑化

**前置阅读**：02-tell端/01-tell的四个成分.md、02-tell端/02-tell的去特化.md
**关联文件**：02-tell端/04-Pipe-1-形式化过滤.md、07-工程规格/02-Pipe-0接口定义.md
**来源**：287号用户第三/四次原文、288号Pipe 0实现

---

## 1. Pipe 0的职责

Pipe 0的工作是：**将推理AI的thinking按照系统定义的标准方法，变成带有结构和标注的拓扑结构（或拓扑结构的集合）。**

这是tell端三层Pipe的第一层。没有Pipe 0的拓扑化，Pipe 1就无法做形式化过滤——因为Pipe 1需要的是结构化的拓扑字段，不是原始的自然语言thinking文本。

### 为什么需要拓扑化？

推理AI的thinking是一段自然语言文本（可能包含数学公式），可能数千到数万个token。系统不能直接用这段文本做tell匹配——因为：

1. **不是关键词匹配**——同一关键词在不同上下文含义不同
2. **不是RAG语义相似**——文本相似≠思维状态相似
3. **需要的是结构匹配**——当前思维状态的结构特征和tell数据基座中tell的拓扑标注做匹配

所以需要先把thinking编码为结构化的拓扑表示，然后才能做结构匹配。这就是Pipe 0的工作。

## 2. 拓扑结构的维度

在POC-VMS-9中，Pipe 0提取的拓扑结构有3个维度：

| 维度 | 含义 | 取值举例 |
|---|---|---|
| **problem_type** | 问题的类型 | discrete_combinatorial / structural_existence / ... |
| **ai_method_type** | AI使用的方法类型 | continuous_analytic / enumeration_brute_force / ... |
| **gap_type** | AI的方法和问题之间的缺口类型 | method_problem_mismatch / ... |

这3个维度是**大概念**——粗粒度的拓扑维度，用于Pipe 1的形式化过滤。

当tell数量增加时，可以扩展到更多维度。第二代系统（女娲）定义的外显思维图T有11种节点类型和12种边类型——这些可以作为拓扑化的更细维度。

## 3. 信号词频次提取

Pipe 0的具体实现方法是从thinking中统计特定信号词的出现频次，用于判定拓扑维度的取值。

### POC-VMS-9中的信号词

| 维度 | 信号词举例 |
|---|---|
| continuous（连续方法） | polynomial, symbol, sign, continuous, analytic, derivative, integral... |
| enumeration（穷举方法） | enumerate, list, cover, check, brute, force, try, case... |
| discrete（离散问题） | group, factor, mod, residue, discrete, combinatorial, partition... |
| structural（结构问题） | structure, subgroup, normal, homomorphism, quotient, sylow... |

### 提取过程

1. 读取thinking文本
2. 对每个信号词在thinking中做计数
3. 按维度汇总频次
4. 根据各维度的频次判定拓扑维度的取值

### POC-VMS-9中的实际结果

**1843题**（AI在用连续方法处理离散问题）：
```
signal_counts: {continuous: 92, enumeration: 5, discrete: 115, structural: 18, discrete_specific: 50, structural_specific: 18}
→ problem_type: discrete_combinatorial (discrete频次最高)
→ ai_method_type: continuous_analytic (continuous频次远高于enumeration)
→ gap_type: method_problem_mismatch (problem是discrete但AI用continuous)
```

**1631题**（AI在用穷举方法处理结构问题）：
```
signal_counts: {continuous: 0, enumeration: 28, discrete: 818, structural: 336, discrete_specific: 0, structural_specific: 72}
→ problem_type: structural_existence (structural频次高)
→ ai_method_type: enumeration_brute_force (enumeration频次远高于continuous)
→ gap_type: method_problem_mismatch (problem是structural但AI用enumeration)
```

## 4. Pipe 0的输入输出

| | 内容 | 数据类型 |
|---|---|---|
| **输入** | thinking文本 | string（从mitmproxy流式截获或sessions.db提取） |
| **输出** | 拓扑结构 | TopologyResult对象 |

TopologyResult的数据结构：

```python
class TopologyResult:
    problem_type: str        # 问题类型，如 "discrete_combinatorial"
    ai_method_type: str      # AI方法类型，如 "continuous_analytic"
    gap_type: str            # 缺口类型，如 "method_problem_mismatch"
    signal_counts: dict      # 各信号词的频次，如 {"continuous": 92, "enumeration": 5, ...}
    confidence: float        # 拓扑化置信度，0-1
```

## 5. 形式化方法做确定性提取

Pipe 0用**形式化方法**（信号词匹配/关键词统计）提取确定性信息。这是经典计算管边界以内的部分——可以用规则定义、可以用代码执行。

这和Pipe 2（小概念标记分辨）形成分工：
- Pipe 0做确定性提取（经典计算，边界以内）——信号词频次是客观可统计的
- Pipe 2做模糊匹配（AI智能，边界以外）——小概念标记分辨需要AI的感知能力

这正是第三代（伏羲）"两种计算"的实例——形式化方法管边界以内的提取，AI智能管边界以外的感知。

## 6. Pipe 0是Pipe 1的前提

**Pipe 0（拓扑化）是Pipe 1（形式化过滤）的前提**——thinking必须先被变成带有结构和标注的拓扑结构，才能做拓扑相似/等价匹配。

没有Pipe 0，Pipe 1就没有输入——Pipe 1需要的是结构化的拓扑字段（problem_type/ai_method_type/gap_type），不是原始的自然语言文本。

这和hint端的做法对称——hint分领域low level化后有清晰结构和标注，tell也分领域low level化后有清晰结构和标注。Pipe 0就是把thinking"分领域low level化"为拓扑结构的过程。

## 7. 参考实现

Pipe 0的参考实现在`xishujuzhen/vms/poc9_tell_filter.py`中（329行）。核心函数：

```python
def pipe0_topologize(thinking_text: str) -> TopologyResult:
    """将thinking文本编码为拓扑结构"""
    # 1. 统计各信号词在thinking中的出现频次
    signal_counts = count_signals(thinking_text, SIGNAL_WORDS)
    # 2. 根据频次判定problem_type
    problem_type = determine_problem_type(signal_counts)
    # 3. 根据频次判定ai_method_type
    ai_method_type = determine_ai_method_type(signal_counts)
    # 4. 根据problem_type和ai_method_type判定gap_type
    gap_type = determine_gap_type(problem_type, ai_method_type)
    return TopologyResult(problem_type, ai_method_type, gap_type, signal_counts, confidence)
```

详细的接口规格见07-工程规格/02-Pipe-0接口定义.md。
