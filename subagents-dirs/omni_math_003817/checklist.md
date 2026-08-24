# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003817
- **文件路径**: subagents-dirs/omni_math_003817/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333696（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003817/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：对每个整数a_0>1，定义序列a_0,a_1,a_2,...，递归为：若√a_n为整数则a_{n+1}=√a_n，否则a_{n+1}=a_n+3。求所有a_0使得存在A满足a_n=A对无穷多个n成立。（IMO 2017 P1 / Shortlist N1）
- 解答核心思路（1-2句话）：答案为3|a_0。通过mod 3不变性分析：3|a_0时序列始终在3的倍数中运行，通过归纳证明"峰值"递减最终进入周期{3,6,9}；3∤a_0时序列不可能周期（≡2 mod 3永远加3发散，≡1 mod 3最终到达≡2 mod 3后发散）。
- 解答关键步骤列表：
  1. mod 3不变性：3|a_0 ⟹ 3|a_n ∀n（+3和√都保持3|）；3∤a_0 ⟹ 3∤a_n ∀n
  2. a_0≡2 mod 3：2不是QR mod 3，序列永远加3，发散
  3. 3|a_0时序列收敛：a_n=(3s)²=9s²时√a_n=3s，从3s出发在到达9s²前先遇到9(s-1)²（因3s≤9(s-1)²对s≥2成立），峰值递减至s=1进入{3,6,9}周期
  4. a_0≡1 mod 3时不可能周期：周期最大值M=(3s+1)²，从√M=3s+1出发在回到M前先遇到(3(s-1)+1)²（因3s+1≤(3s-2)²对s≥2成立），s=1时M=16→4→2≡2 mod 3发散

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这个递归定义的序列的结构：什么条件下取平方根，什么条件下加3？题目要求什么？ | 序列有两个分支：a_n是完全平方数时取√a_n，否则加3。目标是找到所有a_0使序列无限次回到某个值A，即序列最终周期。 |
| 2 | 自由列举 | 0.7 | 要让a_n=A对无穷多个n成立，序列必须有什么性质？列出你能想到的所有分析方向。 | 序列必须最终周期；可分析mod 3；可分析哪些数是完全平方数；可考虑序列是否有界；可试小例子观察模式。 |
| 3 | 小尝试 | 0.5 | 试几个小例子：a_0=2,3,4,5,7,12，观察序列行为。 | a_0=2: 2,5,8,11,...发散；a_0=3: 3,6,9,3,...周期；a_0=4: 4,2,5,8,...发散；a_0=7: 7,10,13,16,4,2,...发散；a_0=12: 12,15,...,36,6,9,3,...周期。观察到3|a_0时周期。 |
| 4 | 思维操作引导 | 0.4 | 分析mod 3：如果3|a_0，那么3|a_n对所有n成立吗？如果a_0≡1或2 mod 3呢？ | 3|a_0时+3和√都保持3|，所以3|a_n ∀n。a_0≡2 mod 3时2非QR mod 3，永远加3发散。a_0≡1 mod 3时√可能≡1或2 mod 3。 |
| 5 | 思维操作引导 | 0.4 | 对于3|a_0的情况，证明序列最终进入周期{3,6,9}。提示：分析a_n=(3s)²=9s²时，从3s出发能否在到达9s²之前先到达9(s-1)²？ | 从3s出发加3直到遇到完全平方数。因3s≤9(s-1)²对s≥2成立，9(s-1)²在3s到9s²之间，所以先遇到更小的完全平方数，峰值递减至s=1进入{3,6,9}。 |
| 6 | 思维操作引导 | 0.4 | 对于a_0≡1 mod 3的情况，证明序列不可能周期。提示：假设周期中最大值为M=(3s+1)²，分析从√M=3s+1出发能否在回到M之前先到达(3(s-1)+1)²？ | 从3s+1出发，因3s+1≤(3s-2)²对s≥2成立，先遇到(3(s-1)+1)²<M，M不可能在周期中。s=1时M=16→4→2≡2 mod 3发散。 |
| 7 | 能量传递引导 | 0.6 | 综合以上分析，给出完整解答。 | 3|a_0当且仅当序列最终周期。a_0≡2 mod 3永远加3发散；a_0≡1 mod 3最终到达≡2 mod 3后发散；3|a_0时峰值递减进入{3,6,9}周期。答案：3|a_0。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: null
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 递归序列带分支条件（完全平方数取根vs加3），周期性条件，mod 3不变性分析，归纳证明峰值递减
- key_objects: 整数序列，完全平方数，模3剩余类，周期循环{3,6,9}，峰值（完全平方数项）

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["modular_arithmetic_analysis", "case_analysis_by_residue", "induction_on_peak_values", "small_case_exploration", "boundedness_argument"]
- primary_pattern: modular_arithmetic_analysis
- knowledge_required: ["quadratic residues mod 3", "periodicity of sequences", "perfect squares", "mathematical induction"]
- key_insight: mod 3不变性是核心枢纽——3|a_0时序列始终在3的倍数中运行，通过归纳证明"峰值"递减（从(3s)²的根3s出发在回到(3s)²前先遇到(3(s-1))²），最终进入周期{3,6,9}

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 枚举小例子观察模式
- translation_to: mod 3不变性分析 + 归纳证明峰值递减
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["mod 3 invariance", "quadratic residue", "peak value decreasing", "periodic cycle {3,6,9}", "perfect square detection"]
- expected_ai_method: enumeration_brute_force（bare AI会枚举小例子猜出3|a_0但无法严格证明）
- correct_method: modular_arithmetic_analysis + induction on peak values

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/enumeration_brute_force/method_translation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 无需新拓扑维度

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中tell_hint_pairs字段。
全局pairs详见profile.json中global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI很可能通过枚举小例子猜出3|a_0的答案，但无法完成严格证明。关键失败点：(1)不会主动分析mod 3不变性作为结构工具；(2)即使分析了mod 3，也不会想到"峰值递减"的归纳论证；(3)对a_0≡1 mod 3的情况，不会想到用类似的归纳论证排除周期性。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-identification", "POC-VMS-path-feature-retrieval"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整JSON已写入 `subagents-dirs/omni_math_003817/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, answer="3 | a_0", per-pair拓扑存在, why_not_visible_locally非None）

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003817
- solution_method_type: modular_arithmetic_analysis_with_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无
- 是否遇到异常: problem.lean中Solution被截断（仅29行），通过web搜索IMO 2017 P1解答重建完整solution_text

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
