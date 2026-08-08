# POC-VMS-9：tell端去特化验证

**前置阅读**：02-tell端/02-tell的去特化.md、02-tell端/03-Pipe-0-拓扑化.md、02-tell端/04-Pipe-1-形式化过滤.md
**来源**：288号

---

## 1. 实验目标

验证两件事：
1. **tell可以去特化**——从POC-VMS-8中提取的tell（Level 0题目特化判断）可以被提升到Level 1（可泛化的拓扑结构）
2. **形式化过滤可以有效命中目标tell**——Pipe 0（拓扑化）+Pipe 1（形式化过滤）能从tell数据基座中命中目标tell，且目标tell排名高于干扰tell

## 2. 两个目标tell

| tell | 来源 | 拓扑结构 | hint |
|---|---|---|---|
| tell-1 | 1843题 | problem_type=discrete_combinatorial, ai_method_type=continuous_analytic, gap_type=method_problem_mismatch | T01模算术——按模4分组 |
| tell-2 | 1631题 | problem_type=structural_existence, ai_method_type=enumeration_brute_force, gap_type=method_problem_mismatch | T03二次剩余——Euler准则 |

## 3. 交叉验证设计

tell-1和tell-2互相作为干扰tell——它们都是真实的、值得收录到数据基座中的(tell, hint)对，不是trivial的。

| 实验 | 题目 | 目标tell | 干扰tell | 预期 |
|---|---|---|---|---|
| 1843 bare | 1843 | — | — | 失败 |
| 1843 target | 1843 | tell-1 | — | 成功 |
| 1843 interference | 1843 | — | tell-2 | **失败**（干扰无效） |
| 1631 bare | 1631 | — | — | 失败 |
| 1631 target | 1631 | tell-2 | — | 成功 |
| 1631 interference | 1631 | — | tell-1 | **失败**（干扰无效） |

## 4. Pipe 0+Pipe 1验证结果

### 1843题

**Pipe 0拓扑化**：problem_type=discrete_combinatorial, ai_method_type=continuous_analytic, gap_type=method_problem_mismatch

**Pipe 1形式化过滤**：
| 候选tell | 匹配分数 | 排名 | 角色 |
|---|---|---|---|
| tell-1 (连续→离散) | 4 | #1 | ← 目标tell |
| tell-2 (穷举→结构) | 0 | #2 | ← 干扰tell |

✅ Pipe 1命中目标tell，目标tell分数4 > 干扰tell分数0

### 1631题

**Pipe 0拓扑化**：problem_type=structural_existence, ai_method_type=enumeration_brute_force, gap_type=method_problem_mismatch

**Pipe 1形式化过滤**：
| 候选tell | 匹配分数 | 排名 | 角色 |
|---|---|---|---|
| tell-2 (穷举→结构) | 4 | #1 | ← 目标tell |
| tell-1 (连续→离散) | 0 | #2 | ← 干扰tell |

✅ Pipe 1命中目标tell，目标tell分数4 > 干扰tell分数0

## 5. 交叉验证结果

| 实验 | 结果 | 详情 |
|---|---|---|
| 1843 bare | ❌ 失败 | 无proof.md |
| 1843 target (T01) | ✅ 成功 | proof.md正确 |
| **1843 interference (T03)** | **❌ 失败** | AI用多项式符号分析，T03二次剩余无效 |
| 1631 bare | ❌ 失败 | 无proof.md |
| 1631 target (T03) | ✅ 成功 | proof.md正确 |
| **1631 interference (T01)** | **❌ 失败** | AI用covering system，T01模算术无效 |

## 6. 验证总结

| 验证项 | 结果 |
|---|---|
| tell可以去特化 | ✅ PASS |
| Pipe 0拓扑化有效 | ✅ PASS |
| Pipe 1不漏（命中目标tell） | ✅ PASS |
| Pipe 1目标tell排名≥干扰tell | ✅ PASS |
| 干扰tell在错误题目上无效 | ✅ PASS |
| 干扰tell不是trivial | ✅ PASS |

**全部PASS。**

## 7. 局限

1. 只有2个tell——无法验证10万级规模
2. 拓扑结构只有3个维度——tell数量增加时可能需要更细粒度
3. Pipe 0的信号词是手工设计的
4. 干扰tell恰好是另一个目标tell——更大规模下干扰tell可能拓扑更相似
