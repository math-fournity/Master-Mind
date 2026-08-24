# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003239
- **文件路径**: subagents-dirs/omni_math_003239/problem.lean
- **来源**: AoPS omni_math (putnam)
- **ArangoDB progress记录_key**: 333117（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003239/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let n be a positive integer. Determine the largest integer m such that there exist real numbers x_1,...,x_{2n} with -1 < x_1 < x_2 < ... < x_{2n} < 1 where the sum of the lengths of the n intervals [x_1^{2k-1}, x_2^{2k-1}], [x_3^{2k-1}, x_4^{2k-1}], ..., [x_{2n-1}^{2k-1}, x_{2n}^{2k-1}] equals 1 for all integers k with 1 ≤ k ≤ m. (Putnam 2022 A6)
- 解答核心思路（1-2句话）：答案 m=n。下界用 Chebyshev 型构造 x_j=cos((2n+1-j)π/(2n+1))，通过单位根计算幂和等于1（k≤n）；上界用逆自由多重集引理证明幂和匹配不能超过n项。
- 解答关键步骤列表：
  1. 下界构造：取 x_j = cos((2n+1-j)π/(2n+1))，这给出(-1,1)中2n个严格递增的值
  2. 区间长度和改写为 -∑_{j=1}^{2n} (cos(2π(n+1)j/(2n+1)))^{2k-1}
  3. 令 ζ = e^{2πi(n+1)/(2n+1)}，用 cos(θ)=(ζ^j+ζ^{-j})/2 展开为二项式求和
  4. 利用 ζ 是 (2n+1) 次本原单位根，∑_{j=1}^{2n} ζ^{jr} = -1（当 r 不被 2n+1 整除时），对 k≤n 有 |2k-1-2l| ≤ 2n-1 < 2n+1，故每项内和为-1，总和为1
  5. 上界：定义 y_j = (-1)^j x_j，则 ∑ y_j^{2k-1} = 1 对 k=1,...,m 成立
  6. {y_1,...,y_{2n}} 是逆自由多重集（无 y_i + y_j = 0），{1} 也是逆自由多重集
  7. 由逆自由多重集引理（基于 Newton 恒等式和对称函数理论），两个不同大小的逆自由多重集的奇次幂和最多匹配到 min(size) 项，故 m ≤ n

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：我们在优化什么？约束条件是什么？涉及哪些数学对象？ | 我们需要找到最大的m使得存在2n个有序实数x_j∈(-1,1)，使n个区间[x_{2j-1}^{2k-1}, x_{2j}^{2k-1}]的长度之和=1对k=1,...,m成立。核心对象：2n个实数、n个区间、奇次幂指数、等式约束。 |
| 2 | 自由列举 | 0.7 | 列出所有你能想到的构造x_j的方法，包括看起来不太可能的方向。 | 1.等距点 2.对称点 3.三角替换(cos/sin) 4.多项式根 5.Chebyshev节点 6.小情形n=1,2找模式 7.改写为幂和 |
| 3 | 小尝试 | 0.4 | 试n=1：需要x_1<x_2在(-1,1)中使x_2^{2k-1}-x_1^{2k-1}=1对k=1,...,m成立。最大m是多少？ | k=1: x_2-x_1=1→x_2=x_1+1，需-1<x_1<0。k=2: (x_1+1)^3-x_1^3=3x_1^2+3x_1+1=1→x_1=0或-1，均不在(-1,0)内。故m=1=n。 |
| 4 | 思维操作引导 | 0.5 | 将条件∑(x_{2j}^{2k-1}-x_{2j-1}^{2k-1})=1改写为单一幂和形式。什么代换能让它更简洁？ | 令y_j=(-1)^j x_j，则∑_{j=1}^{2n} y_j^{2k-1}=∑(-1)^{j(2k-1)}x_j^{2k-1}=∑(-1)^j x_j^{2k-1}=∑(x_{2j}^{2k-1}-x_{2j-1}^{2k-1})=1。条件变为带符号值的奇次幂和=1。 |
| 5 | 思维操作引导 | 0.6 | 对下界，考虑x_j=cos((2n+1-j)π/(2n+1))。这个选择有什么结构？为什么可能有效？ | 这是Chebyshev型节点——(2n+1)次单位根的实部。关键性质：cos(θ)=(e^{iθ}+e^{-iθ})/2，可将余弦幂和与单位根联系起来。2n个值严格递增在(-1,1)中。 |
| 6 | 推进 | 0.5 | 用ζ=e^{2πi(n+1)/(2n+1)}，证明幂和∑(cos(2π(n+1)j/(2n+1)))^{2k-1}=1对k=1,...,n成立。单位根的什么性质使这成立？ | 用cos=(ζ^j+ζ^{-j})/2展开为二项式：-1/2^{2k-1}∑_l C(2k-1,l)∑_j ζ^{j(2k-1-2l)}。ζ是(2n+1)次本原根，k≤n时|2k-1-2l|≤2n-1<2n+1故ζ^{2k-1-2l}≠1，内和=-1。总和=-1/2^{2k-1}·(-1)·2^{2k-1}=1。 |
| 7 | 思维操作引导 | 0.6 | 对上界(m≤n)，带符号值y_j=(-1)^j x_j构成逆自由多重集，其奇次幂和=1。如何用幂和与对称函数理论证明m不能超过n？ | {y_j}是2n元逆自由多重集，{1}是1元逆自由多重集，奇次幂和均为1。由逆自由多重集引理（基于Newton恒等式），两个不同大小的逆自由多重集的奇次幂和最多匹配到min(大小)项，故m≤n。 |
| 8 | 能量传递引导 | 0.7 | 你现在有两个方向了。总结完整证明m=n。 | 下界：Chebyshev构造x_j=cos((2n+1-j)π/(2n+1))，单位根计算给出幂和=1对k≤n。上界：逆自由多重集引理证明幂和匹配不能超过n项。故m=n。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4 (R1,R2,R6,R8)
- knowledge_rounds（思维操作引导的轮数）: 3 (R4,R5,R7)
- level_sum: 0.8+0.7+0.4+0.5+0.6+0.5+0.6+0.7 = 4.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction
- structure_features: 优化型问题——求最大m使约束系统可满足；约束为奇次幂和等式；需双向证明（构造+不可能性）；涉及2n个有序实数和n个区间
- key_objects: ["有序实数x_1,...,x_{2n}∈(-1,1)", "奇次幂区间长度和", "Chebyshev节点cos((2n+1-j)π/(2n+1))", "(2n+1)次单位根ζ", "逆自由多重集{y_j=(-1)^j x_j}"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["代数改写（区间和→幂和）", "三角替换（Chebyshev节点）", "单位根技术（二项式展开+本原根性质）", "小情形分析（n=1验证）", "双向界（构造+不可能性）", "对称函数理论（逆自由多重集引理）"]
- primary_pattern: 三角替换与单位根技术
- knowledge_required: ["Chebyshev节点", "单位根与本原根", "幂和与Newton恒等式", "对称函数理论", "二项式定理", "逆自由多重集概念"]
- key_insight: 区间长度和条件可改写为带符号值的奇次幂和，而Chebyshev节点将余弦幂和与单位根联系起来，使幂和可通过单位根性质精确计算为1

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 实数区间长度和（代数语言）
- translation_to: 单位根幂和（复分析/代数语言）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["幂和改写", "Chebyshev节点", "单位根", "逆自由多重集", "二项式展开", "三角替换"]
- expected_ai_method: 直接计算和情形分析——尝试具体x_j值并计算区间和，或做代数变形但看不到三角/单位根联系
- correct_method: 两阶段：(1)Chebyshev节点构造+单位根幂和计算（下界），(2)逆自由多重集引理（上界）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——constraint_satisfaction/direct_calculation/method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新拓扑维度

**拓扑进化建议**：无。现有分类体系充分覆盖。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中tell_hint_pairs字段。
全局pairs详见profile.json中global_tell_hint_pairs字段。

全局pair 1 (path_feature): 完整路径特征——从实数区间和到单位根幂和的翻译链在局部步骤中不可见
全局pair 2 (implicit): 蕴含型——上界证明技术（逆自由多重集引理）从下界构造中完全不可推导

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接构造或小情形分析，可能找到n=1的情形但无法推广。不会识别Chebyshev/单位根联系。上界证明（逆自由多重集引理）几乎必然超出bare AI的知识范围。
- suitable_for_poc: ["hint_injection_test", "knowledge_bottleneck_test", "translation_detection_test"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [x] _key（=problem_id）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（=n）
- [x] problem_type
- [x] solution_method_type
- [x] structure_features
- [x] key_objects
- [x] thinking_patterns
- [x] primary_pattern
- [x] knowledge_required
- [x] key_insight
- [x] translation_from
- [x] translation_to
- [x] translation_type
- [x] tell_topology（profile级）
- [x] tell_small_concepts（profile级）
- [x] expected_ai_method
- [x] correct_method
- [x] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出: omni_math_003239, 8 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_003239
- solution_method_type: trigonometric_construction
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，现有分类体系充分覆盖
- 是否遇到异常: problem.lean中Solution被截断，已从Kedlaya Putnam存档重建完整解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
