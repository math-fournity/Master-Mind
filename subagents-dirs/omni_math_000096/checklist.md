# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000096
- **文件路径**: subagents-dirs/omni_math_000096/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329967（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000096/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find all functions f:Z→Z such that for any integers a,b,c: 2f(a²+b²+c²) - 2f(ab+bc+ca) = f(a-b)² + f(b-c)² + f(c-a)²
- 解答核心思路（1-2句话）：通过b=c=0代入得到f(x²)=f(x)²，由f(1)=f(1)²分两种情况(f(1)=0或f(1)=1)，利用代数恒等式a²+b²+c²-ab-bc-ca=[(a-b)²+(b-c)²+(c-a)²]/2和递推证明f≡0或f=id。
- 解答关键步骤列表：
  1. 令b=c=0: 2f(a²)-2f(0)=2f(a)² → f(a²)=f(a)²+f(0)
  2. 令a=0: f(0)=f(0)²+f(0) → f(0)²=0 → f(0)=0 (f(0)=1矛盾)
  3. 得到f(a²)=f(a)²对所有a成立
  4. 令a=b,c=0: f(2a²)=2f(a²)
  5. f(1)=f(1)² → f(1)∈{0,1}
  6. 利用代数恒等式重写方程: 2f(S)-2f(P)=f(d₁)+f(d₂)+f(d₃), d₁+d₂+d₃=2(S-P)
  7. f(1)=0情形: 证明f≡0
  8. f(1)=1情形: 证明f(x)=x
  9. 结论: f(x)=0或f(x)=x

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察这个函数方程的结构：左边是2f(三项平方和)-2f(三项乘积和)，右边是三个f(差)的平方。你能描述出这个方程的结构特征吗？已知条件和未知是什么？ | 这是一个定义在Z→Z上的函数方程，有三个自由变量a,b,c。LHS涉及f在a²+b²+c²和ab+bc+ca处的值，RHS涉及f(a-b)²+f(b-c)²+f(c-a)²。需要找出所有满足条件的f。 |
| 2 | 自由列举 | 0.7 | 对于这类三元函数方程，你有哪些可能的代入方向来简化方程？ | 可以尝试：a=b=c、b=c=0、c=0、a=0、a=b、a=-b、令某些变量相等、令某些变量为0或1等。 |
| 3 | 小尝试 | 0.5 | 试试a=b=c这个方向，看看能得到什么。 | 令a=b=c: 2f(3a²)-2f(3a²)=0+0+0=0，恒等成立，没有提取到任何信息。这个方向是平凡的。 |
| 4 | 思维操作引导 | 0.4 | 试试b=c=0的代入，然后利用结果再令a=0，你能推导出f(0)和f(x²)的关系吗？ | 令b=c=0: 2f(a²)-2f(0)=2f(a)²，即f(a²)=f(a)²+f(0)。再令a=0: f(0)=f(0)²+f(0)→f(0)²=0→f(0)=0。因此f(a²)=f(a)²对所有a成立。 |
| 5 | 推进 | 0.5 | 有了f(x²)=f(x)²后，令a=b,c=0能推出什么？再结合f(1)=f(1)²，f(1)的可能值是什么？ | 令a=b,c=0: 2f(2a²)-2f(a²)=2f(a)²=2f(a²)，所以f(2a²)=2f(a²)。由f(1)=f(1)²，f(1)∈{0,1}，需要分两种情况讨论。 |
| 6 | 思维操作引导 | 0.4 | 注意到代数恒等式a²+b²+c²-(ab+bc+ca)=[(a-b)²+(b-c)²+(c-a)²]/2。利用这个恒等式和f(x²)=f(x)²，原方程可以怎样重写？这对证明f的性质有什么帮助？ | 原方程变为2f(S)-2f(P)=f(d₁)+f(d₂)+f(d₃)，其中d₁+d₂+d₃=2(S-P)。如果f是可加的，则RHS=f(d₁+d₂+d₃)=f(2(S-P))=2f(S-P)，与LHS一致。关键是通过具体代入证明f的可加性。 |
| 7 | 能量传递引导 | 0.6 | 现在分两种情况：f(1)=0时证明f恒为0；f(1)=1时利用已建立的递推关系和f(x²)=f(x)²证明f(x)=x。你能完成这两个情况的证明吗？ | f(1)=0: 由f(n²)=f(n)²=0和方程递推可得f≡0。f(1)=1: f(2)=2,f(5)=5等，通过归纳和方程递推证明f(n)=n对所有n成立。因此f(x)=0或f(x)=x。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+小尝试+推进+能量传递引导）: 5
- knowledge_rounds（思维操作引导）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.5+0.4+0.6=3.9
- knowledge_bottleneck: "R4"
- thinking_bottleneck: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 三元函数方程(f:Z→Z)，LHS为f在平方和与乘积和处的线性组合，RHS为f在差处的平方和。方程结构蕴含代数恒等式a²+b²+c²-ab-bc-ca=[(a-b)²+(b-c)²+(c-a)²]/2。
- key_objects: ["f:Z→Z", "函数方程", "代数恒等式a²+b²+c²-ab-bc-ca", "f(x²)=f(x)²", "f(1)∈{0,1}"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["specialization_substitution", "algebraic_identity_recognition", "case_analysis", "inductive_building", "additivity_deduction"]
- primary_pattern: specialization_substitution
- knowledge_required: ["函数方程基本技巧(变量代入)", "代数恒等式识别", "整数归纳法", "可加性概念"]
- key_insight: 令b=c=0得到f(x²)=f(x)²，由f(1)=f(1)²分出f≡0和f=id两条路径，代数恒等式将方程化简为可加性验证。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接函数方程操作（暴力代入和化简）
- translation_to: 代数恒等式识别+情况分析（利用隐藏的代数结构将方程转化为可加性条件）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["specialization_substitution", "algebraic_identity", "f(x²)=f(x)²", "case_split_on_f(1)", "additivity"]
- expected_ai_method: direct_manipulation（bare AI会尝试直接操作方程，不识别隐藏的代数恒等式）
- correct_method: 代入特化+代数恒等式识别+情况分析

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization、ai_method_type=direct_manipulation、gap_type=structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

局部pairs详见profile.json中的tell_hint_pairs字段。
全局pairs详见profile.json中的global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接操作方程或枚举代入，但不会识别隐藏的代数恒等式a²+b²+c²-ab-bc-ca=[(a-b)²+(b-c)²+(c-a)²]/2，也无法从f(x²)=f(x)²正确分出f(1)=0和f(1)=1两种情况并分别完成归纳证明。很可能在得到f(x²)=f(x)²后卡住，不知道如何利用三元方程进一步推导可加性。
- suitable_for_poc: ["hint_injection_efficiency", "tell_extraction_from_thinking", "topology_matching_accuracy"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_000096/profile.json`。
所有字段已检查：_key, source_id, source_dataset, schema_version, problem_text, solution_text, solution_summary, domain, subfield, answer_type, answer, problem_type, solution_method_type, structure_features, key_objects, thinking_patterns, primary_pattern, knowledge_required, key_insight, translation_from, translation_to, translation_type, tell_topology, tell_small_concepts, expected_ai_method, correct_method, tell_hint_pairs(7个), global_tell_hint_pairs(3个), bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels, qa_sequence, analysis_metadata。

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 3 global pairs, answer非None, why_not_visible_locally非None, per-pair拓扑存在）

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_000096
- solution_method_type: specialization_and_case_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3 (1 path_feature + 2 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无
- 是否遇到异常: 无
- ArangoDB入库: 成功，progress记录329967已更新为completed

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
