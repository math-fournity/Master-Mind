# Pipe 2：小概念标记分辨

**前置阅读**：02-tell端/04-Pipe-1-形式化过滤.md、01-基础概念/06-概念树.md
**关联文件**：02-tell端/06-tell的标准化语言描述.md、04-概念树/01-大概念与小概念.md
**来源**：287号用户第六次原文、289号Pipe 2实现

---

## 1. Pipe 2的职责

Pipe 2的工作是：**在Pipe 1缩小的范围内，用小概念标记分辨精准识别出真tell。**

这是tell端三层Pipe的第三层。Pipe 1已经用大概念缩小了候选范围，但可能还有多个候选tell的大概念拓扑相同（Pipe 1给同分）。Pipe 2需要用更细的小概念来区分这些同分候选。

## 2. 大概念无法区分时引入小概念

这是Pipe 2存在的根本原因。当两个tell的大概念拓扑完全相同时，Pipe 1给同分——大概念无法区分。

### POC-VMS-10中的验证

两个拓扑相同且距离极近的tell：

| | tell-A | tell-B |
|---|---|---|
| 来源 | 1631题 | 1709题 |
| 大概念拓扑 | (structural_existence, enumeration_brute_force, method_problem_mismatch) | **完全相同** |
| 距离极近 | 都是数论题，都是穷举a值，都是结构问题 | 同 |
| 小概念：穷举对象 | 序列参数a | 差分参数a |
| 小概念：问题结构 | 素数性（Mersenne素数） | 整除性（被4整除） |
| 小概念：正确方法 | 二次剩余/Euler准则 | 2-adic赋值/模4分析 |
| hint | T03二次剩余 | T05 2-adic赋值 |

**Pipe 1给同分**：两个题的目标tell和干扰tell都得score=4——大概念无法区分。

**Pipe 2小概念标记分辨成功**：

1631题（tell-A的题目）：
| 候选tell | 小概念命中 | combined_score | 角色 |
|---|---|---|---|
| tell-A | mersenne=497, primality=339, covering=20, total=856 | 896 | ← 目标tell胜出 |
| tell-B | divisibility_4=12, total=12 | 52 | ← 干扰tell |

1709题（tell-B的题目）：
| 候选tell | 小概念命中 | combined_score | 角色 |
|---|---|---|---|
| tell-B | largest_odd_divisor=14, divisibility_4=19, p_adic=2, difference=6, total=41 | 81 | ← 目标tell胜出 |
| tell-A | total=0 | 40 | ← 干扰tell |

## 3. 小概念信号词是tell的标准化语言描述的关键词提取

小概念信号词不是凭空构造的，而是从tell的**标准化语言描述**中提取的关键词。

例如：
- tell-A的标准化语言描述："AI在枚举序列参数a的值，试图用covering system覆盖所有情况，但问题是Mersenne素数的存在性，需要用二次剩余/Euler准则"
  - 提取的小概念信号词：mersenne, primality, covering_system
- tell-B的标准化语言描述："AI在枚举差分参数a的值，试图逐一验证条件，但问题是最大奇因子差的整除性判定，需要用2-adic赋值分case分析模4行为"
  - 提取的小概念信号词：largest_odd_divisor, divisibility_4, p_adic, difference

Pipe 2的工作就是：在thinking文本中统计这些小概念信号词的出现频次，频次高的tell就是目标tell。

## 4. 只要两个tell能用语言表达出区别就能定义概念来区分

这是用户第六次原文的核心洞察，也是Pipe 2可行性的理论基础：

> "无论两个tell多么相似，我们都可以用更为细化（小）的概念去进一步区分不同的tell。因为毕竟我们可以用语言表达tell之间的区别，就可以借助定义新的概念这种手段去区分tell。"

这意味着：Pipe 2的区分能力**没有上限**——只要两个tell有区别（而它们一定有区别，否则就是同一个tell），就能定义小概念来区分它们。

## 5. Pipe 2的输入输出

| | 内容 | 数据类型 |
|---|---|---|
| **输入** | Pipe 1的候选tell列表 + thinking文本 + 概念文件 | List[TellCandidate] + string + ConceptFile |
| **输出** | 精准识别的tell（一个或多个） | List[TellResult] |

TellResult的数据结构：

```python
class TellResult:
    tell_id: str                    # tell的唯一标识
    combined_score: float           # 大概念分数 + 小概念命中次数加权
    small_concept_hits: dict        # 各小概念信号词的命中次数
    selected: bool                  # 是否被选为目标tell
```

## 6. combined_score计算

Pipe 2的combined_score = 大概念分数（Pipe 1给出）+ 小概念命中次数加权。

在POC-VMS-10中：
- 1631题：tell-A的combined_score = 4（大概念）+ 856（小概念总命中）= 896（实际实现中可能有加权调整）
- 1709题：tell-B的combined_score = 4（大概念）+ 41（小概念总命中）= 81

combined_score高的tell就是Pipe 2选出的目标tell。

## 7. Pipe 2不是暴力遍历所有tell

**关键**：Pipe 2不是暴力遍历所有tell，而是：

1. Pipe 1用大概念缩小到某个大概念范围
2. Pipe 2加载该大概念对应的**概念文件**（包含该大概念下的所有小概念）
3. Pipe 2用概念文件中的小概念对thinking做标记分辨
4. 标记分辨的结果就是精准识别出的tell

这意味着Pipe 2只需要加载一个概念文件（不是全部概念文件），只需要处理Pipe 1筛出的候选（不是全部tell）。这是有限上下文的辅助AI能系统化应对的关键——无论概念树如何膨胀，Pipe 2只需要加载当前大概念对应的一个概念文件。

## 8. 完整的三层Pipe架构

```
thinking文本
     │
     ▼
[Pipe 0] 拓扑化 → 大概念拓扑 (problem_type, ai_method_type, gap_type)
     │
     ▼
[Pipe 1] 形式化过滤 → 候选tell列表（大概念匹配，允许无效≤50%）
     │           如果候选tell大概念拓扑不同 → Pipe 1已能区分 → 直接选最高分
     │           如果候选tell大概念拓扑相同 → Pipe 1给同分 → 需要Pipe 2
     ▼
[Pipe 2] 小概念标记分辨 → 精准识别（加载概念文件→小概念信号词标记→combined_score排序）
     │
     ▼
识别出的目标tell → 方向匹配 → hint方向 → 启动新AI
```

## 9. 参考实现

Pipe 2的参考实现在`xishujuzhen/vms/poc10_tell_disambiguation.py`中（386行）。核心函数：

```python
def pipe2_disambiguate(candidates, thinking_text, concept_file):
    """在Pipe 1的候选中用小概念标记分辨精准识别"""
    # 1. 加载概念文件中的小概念信号词
    small_concepts = load_concept_file(concept_file)
    # 2. 对每个候选tell，统计其小概念信号词在thinking中的命中次数
    for candidate in candidates:
        hits = count_small_concept_hits(thinking_text, candidate.small_concept_markers)
        candidate.small_concept_hits = hits
        candidate.combined_score = candidate.match_score + sum(hits.values())
    # 3. 按combined_score排序，选最高分
    candidates.sort(key=lambda c: c.combined_score, reverse=True)
    candidates[0].selected = True
    return candidates
```

详细的接口规格见07-工程规格/04-Pipe-2接口定义.md。
