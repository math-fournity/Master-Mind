# Pipe 1：形式化过滤

**前置阅读**：02-tell端/03-Pipe-0-拓扑化.md
**关联文件**：02-tell端/05-Pipe-2-小概念标记分辨.md、07-工程规格/03-Pipe-1接口定义.md
**来源**：287号、288号Pipe 1实现、290号继承1/23

---

## 1. Pipe 1的职责

Pipe 1的工作是：**利用拓扑相似/拓扑等价缩小tell范围（大概念匹配），从海量tell中筛出一部分候选。**

这是tell端三层Pipe的第二层。Pipe 0已经把thinking编码为拓扑结构，Pipe 1用这个拓扑结构去tell数据基座中做匹配，筛出候选tell。

## 2. Pipe 1是硬约束不是优化选项

**Pipe 1是必须先做的，不能跳过。** 这是架构上的硬约束，不是优化选项。

用户在287号中明确指出：

> "识别已经用穷举的方式，降低了思维难度的海量的tell，绝对不能只依靠辅助AI或subagent去暴力遍历整个数据基座中对tell集合的积累。而是首先要用其他技术手段，尤其是形式化的技术手段，缩小最终要提交给辅助AI或subagent去具体查看的tell的范围。"

为什么不能跳过Pipe 1？因为当tell规模达到10万级别时，不能假设系统的全部tell可以放入辅助AI的上下文中，不能假设辅助AI可以暴力遍历所有tell。必须先用形式化方法缩小范围，然后辅助AI只在缩小的范围内做精准识别。

## 3. Pipe 1的目标是不漏

Pipe 1的设计目标是**不漏**——可以多送（无效tell≤50%），但不能少送（不能漏掉真tell）。

| 目标 | 要求 | 说明 |
|---|---|---|
| 不漏（recall优先） | 目标tell必须在候选列表中 | 如果漏掉了真tell，后续Pipe 2无法补救——Pipe 2只能从Pipe 1给的候选中选 |
| 可多送 | 无效tell≤50% | 允许一些不应该被识别到的tell也进入候选列表，Pipe 2会过滤掉它们 |
| 初始无效比例 | ≤50% | 如果无效tell占比太高，可以去优化Pipe 0的拓扑化精度和Pipe 1的过滤精度 |

这个"不漏但可多送"的设计来自用户的原文要求——"确实其他手段、Pipe都上了，但如果继续过滤，那么真的会漏掉tell，所以会有一些tell，虽然不应该被识别到，但是也送给辅助AI进行分析了。"

## 4. 匹配分数计算

Pipe 1用大概念拓扑字段做匹配，计算每个候选tell的匹配分数。

### POC-VMS-9中的匹配结果

**1843题**（tell-1的题目，tell-1是目标tell，tell-2是干扰tell）：

| 候选tell | 大概念拓扑 | 匹配分数 | 角色 |
|---|---|---|---|
| tell-1 (连续→离散) | discrete_combinatorial + continuous_analytic + method_problem_mismatch | 4 | ← 目标tell |
| tell-2 (穷举→结构) | structural_existence + enumeration_brute_force + method_problem_mismatch | 0 | ← 干扰tell |

Pipe 0把1843题的thinking拓扑化为(discrete, continuous)——和tell-1的拓扑完全匹配（3个维度全部匹配，分数=4），和tell-2的拓扑完全不匹配（3个维度全部不匹配，分数=0）。

**1631题**（tell-2的题目）：

| 候选tell | 大概念拓扑 | 匹配分数 | 角色 |
|---|---|---|---|
| tell-2 (穷举→结构) | structural_existence + enumeration_brute_force + method_problem_mismatch | 4 | ← 目标tell |
| tell-1 (连续→离散) | discrete_combinatorial + continuous_analytic + method_problem_mismatch | 0 | ← 干扰tell |

Pipe 0把1631题的thinking拓扑化为(structural, enumeration)——和tell-2完全匹配（分数=4），和tell-1完全不匹配（分数=0）。

### 匹配分数的计算方法

每个拓扑维度匹配成功得一定分数。在POC-VMS-9中，3个维度各匹配成功得1分，加上gap_type匹配的额外加权，总分=4。3个维度全部不匹配则总分为0。

## 5. Pipe 1的输入输出

| | 内容 | 数据类型 |
|---|---|---|
| **输入** | Pipe 0产出的拓扑结构 + tell数据基座 | TopologyResult + ArangoDB tell_db集合 |
| **输出** | 候选tell列表 | List[TellCandidate] |

TellCandidate的数据结构：

```python
class TellCandidate:
    tell_id: str                    # tell的唯一标识
    match_score: float              # 大概念匹配分数
    big_concept_topology: dict      # tell的大概念拓扑（problem_type/ai_method_type/gap_type）
    standard_description: str       # tell的标准化语言描述
    small_concept_markers: list     # tell的小概念信号词列表
    hint_ids: list                  # 关联的hint方向ID列表
```

## 6. AQL查询实现

Pipe 1用ArangoDB AQL查询做结构化字段匹配。这继承了第一代（盘古）的AQL集合差集思路和第三代（伏羲）的路径结构匹配思路——**不是RAG（embedding相似度），而是结构化字段匹配**。

AQL查询模板：

```sql
FOR tell IN tell_db
  FILTER tell.big_concept_topology.problem_type == @problem_type
    AND tell.big_concept_topology.ai_method_type == @ai_method_type
    AND tell.big_concept_topology.gap_type == @gap_type
  SORT match_score DESC
  LIMIT @max_candidates
  RETURN tell
```

详细的AQL查询模板见07-工程规格/06-AQL查询模板.md。

## 7. 继承来源

Pipe 1的设计继承了前几代的两项关键设计：

1. **盘古的拓扑覆盖验证/AQL集合差集**——用结构化字段做数学确定性的匹配，不是模糊的语义相似
2. **伏羲的路径结构匹配（非RAG）**——粗筛（结构化字段匹配）→精化（图查询）→排序的三层检索架构。Pipe 1是粗筛，Pipe 2是精化，combined_score是排序

详细的继承关系见06-四代继承/01-盘古的遗产.md和06-四代继承/04-伏羲的遗产.md。
