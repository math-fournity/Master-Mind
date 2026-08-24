# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000257
- **文件路径**: subagents-dirs/fate_000257/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396367（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000257/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let A, B ∈ ℚ^× be rational numbers. Consider the quaternion ring D_{A,B,ℝ} = {a+bi+cj+dk | a,b,c,d ∈ ℝ} with i²=A, j²=B, ij=-ji=k. Show that D_{A,B,ℝ} is either isomorphic to ℍ (Hamilton quaternion) or isomorphic to M₂(ℝ) as ℝ-algebras. Lean形式化还要求证明 ℍ ≇ M₂(ℝ)（二者不同构）。
- 解答核心思路（1-2句话）：根据A,B在ℝ中的符号分情况讨论：A,B都为负时通过基向量缩放构造到ℍ的同构；至少一个为正时通过广义Pauli矩阵表示构造到M₂(ℝ)的同构。再通过零因子不变量证明ℍ和M₂(ℝ)不同构。
- 解答关键步骤列表：
  1. 将A,B嵌入ℝ，按符号分情况
  2. Case 1（A<0, B<0）：令i↦√|A|·i_ℍ, j↦√|B|·j_ℍ，验证得到D_{A,B,ℝ}≅ℍ
  3. Case 2（至少一个>0）：WLOG A>0，令i↦diag(√A,-√A), j↦[[0,B],[1,0]]，验证得到D_{A,B,ℝ}≅M₂(ℝ)
  4. 证明ℍ≇M₂(ℝ)：ℍ是除环（无零因子），M₂(ℝ)有零因子，代数同构保持乘法故保持零因子

---

## Step 2: QA序列分析——局部视角7步 [x]

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | Describe the structure of this problem: what are the known objects, what is the unknown, and what special properties does the base field ℝ have? | We have a quaternion algebra D_{A,B,ℝ} with parameters A,B ∈ ℚ^×, and we need to show it's isomorphic to either ℍ or M₂(ℝ) as ℝ-algebras. The base field ℝ is an ordered field, which means elements have well-defined signs. |
| 2 | 自由列举 | 0.6 | List all possible approaches to classify D_{A,B,ℝ}: what methods could determine which algebra it's isomorphic to? | Possible approaches: (1) direct construction of isomorphism, (2) universal property, (3) tensor product decomposition, (4) sign-based case analysis on A and B, (5) Hilbert symbol computation, (6) checking if the algebra is a division ring. |
| 3 | 小尝试 | 0.3 | Try constructing an isomorphism D_{A,B,ℝ} → ℍ directly. What goes wrong? | If we try i↦√|A|·i_ℍ, j↦√|B|·j_ℍ, this works when A,B<0. But when A>0, we'd need i_ℍ²=A>0, impossible since i_ℍ²=-1. So a single construction doesn't work — we need to split by signs. |
| 4 | 思维操作引导 | 0.5 | Given the sign-based case split, construct an explicit ℝ-algebra isomorphism D_{A,B,ℝ} → M₂(ℝ) for the case where at least one of A,B is positive. What matrices should i and j map to? | WLOG A>0. Map i↦[[√A,0],[0,-√A]] and j↦[[0,B],[1,0]]. Then i²=A·I, j²=B·I, and ij=-ji. This extends to an ℝ-algebra isomorphism D_{A,B,ℝ}≅M₂(ℝ). |
| 5 | 推进 | 0.4 | Now address the second part: show that ℍ and M₂(ℝ) are not isomorphic as ℝ-algebras. What invariant distinguishes them? | ℍ is a division ring: every nonzero element has an inverse. So ℍ has no zero divisors. But M₂(ℝ) has zero divisors (e.g., E₁₁·E₂₂=0). An algebra isomorphism preserves multiplication, so it would preserve zero divisors — contradiction. |
| 6 | 思维操作引导 | 0.5 | Formalize the non-isomorphism argument: why exactly does an algebra isomorphism preserve the zero divisor property? | If φ:ℍ→M₂(ℝ) is an isomorphism, φ(xy)=φ(x)φ(y). If M₂(ℝ) has XY=0 with X,Y≠0, then φ⁻¹(X)·φ⁻¹(Y)=φ⁻¹(0)=0 with φ⁻¹(X),φ⁻¹(Y)≠0. So ℍ would have zero divisors — contradiction. |
| 7 | 能量传递引导 | 0.8 | Assemble the complete proof from the three parts you've developed. What is the final structure? | Three parts: (1) sign-based case split, (2) Case 1: rescale to ℍ; Case 2: Pauli matrices to M₂(ℝ), (3) ℍ≇M₂(ℝ) via zero divisors. Classification complete. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: Quaternion algebra over ℝ with parameters A,B ∈ ℚ^×; dichotomy between division algebra (ℍ) and split matrix algebra (M₂(ℝ)); classification driven by sign structure of ℝ as ordered field
- key_objects: ["quaternion algebra D_{A,B,ℝ}", "Hamilton quaternions ℍ", "matrix ring M₂(ℝ)", "ℝ-algebra isomorphism", "Hilbert symbol (A,B)_ℝ"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["sign-based case analysis", "explicit isomorphism construction via rescaling", "explicit isomorphism construction via matrix representation", "invariant-based non-isomorphism proof (zero divisors)"]
- primary_pattern: sign-based case analysis with explicit construction
- knowledge_required: ["quaternion algebra definition and multiplication rules", "Hilbert symbol over ℝ", "Hamilton quaternion algebra ℍ as division ring", "matrix ring M₂(ℝ) and its zero divisors", "ℝ-algebra isomorphism definition", "ordered field structure of ℝ"]
- key_insight: Over ℝ, the signs of A and B determine whether the quaternion algebra is a division ring (≅ℍ when both negative) or split (≅M₂(ℝ) otherwise) — ℝ's ordered field structure makes the classification a simple dichotomy

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: abstract algebra classification (quaternion algebra theory over general fields)
- translation_to: explicit sign-based case analysis with concrete matrix constructions over ℝ
- translation_type: abstract_to_concrete

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: ["sign-based dichotomy", "Hilbert symbol over ℝ", "Pauli matrix representation", "division ring invariant", "zero divisors"]
- expected_ai_method: Direct algebraic manipulation attempting to construct a universal isomorphism without case analysis, or trying to use the universal property of quaternion algebras abstractly
- correct_method: Case split on signs of A and B over ℝ, with explicit isomorphism construction (rescaling for ℍ, Pauli matrices for M₂(ℝ)) and zero-divisor invariant for non-isomorphism

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_calculation, gap_type=knowledge_gap 均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 无需新拓扑维度

**拓扑进化建议**：无。现有拓扑分类体系可以充分描述此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs概要**：
- R1: tell=AI未注意到ℝ的序结构驱动分类 / topology=(characterization, logical_deduction, structural_transformation)
- R2: tell=AI列举方法时未列出符号分情况 / topology=(characterization, enumeration_brute_force, method_problem_mismatch)
- R3: tell=AI尝试统一构造失败 / topology=(characterization, direct_calculation, structural_transformation)
- R4: tell=AI不知split case的矩阵表示 / topology=(characterization, direct_calculation, knowledge_gap) [knowledge bottleneck]
- R5: tell=AI未处理非同构证明 / topology=(characterization, logical_deduction, knowledge_gap)
- R6: tell=AI未形式化零因子保持论证 / topology=(characterization, logical_deduction, knowledge_gap) [knowledge bottleneck]
- R7: tell=所有部分已就位 / topology=(characterization, logical_deduction, method_translation)

**全局pairs概要**：
- path_feature: 符号分类二分法——完整路径特征，局部不可见
- implicit: ℝ的序域结构驱动分类——蕴含信息，局部步骤中不可见

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI will likely attempt to construct a single universal isomorphism without case analysis, or try to use abstract properties of quaternion algebras without recognizing the sign-based dichotomy. It may also fail to prove the non-isomorphism part, not realizing that the zero divisor invariant distinguishes ℍ from M₂(ℝ). The knowledge of Hilbert symbols over ℝ and the Pauli matrix representation for split quaternion algebras is a specific knowledge gap.
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_gap_detection"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入 `subagents-dirs/fate_000257/profile.json`

**字段清单检查**：
- [x] _key（=fate_000257）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（proof类型，填要证明的结论）
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
- [x] tell_hint_pairs（7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个全局pair，含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R3"为字符串）
- [x] analysis_metadata

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [ ] _key（=problem_id）
- [ ] source_id
- [ ] source_dataset
- [ ] schema_version（=3）
- [ ] problem_text
- [ ] solution_text
- [ ] solution_summary
- [ ] domain
- [ ] subfield
- [ ] answer_type
- [ ] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
- [ ] problem_type
- [ ] solution_method_type
- [ ] structure_features
- [ ] key_objects
- [ ] thinking_patterns
- [ ] primary_pattern
- [ ] knowledge_required
- [ ] key_insight
- [ ] translation_from
- [ ] translation_to
- [ ] translation_type
- [ ] tell_topology（profile级）
- [ ] tell_small_concepts（profile级）
- [ ] expected_ai_method
- [ ] correct_method
- [ ] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [ ] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [ ] bare_ai_expected
- [ ] bare_ai_error_prediction
- [ ] suitable_for_poc
- [ ] discriminates_levels
- [ ] qa_sequence（含rounds数组和stats子对象）
- [ ] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证详情：
- problem_profiles/fate_000257 已写入
- 7 local pairs, 2 global pairs
- per-pair tell_topology 存在
- global pair why_not_visible_locally 非 None
- answer 非 None
- knowledge_bottleneck="R4" (字符串), thinking_bottleneck="R3" (字符串)
- problem_extraction_progress _key=396367 已更新 (extraction_status=completed, schema_version=3)

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000257
- solution_method_type: case_analysis_with_explicit_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（characterization / direct_calculation / knowledge_gap等）可充分描述此题。
- 是否遇到异常: 无异常

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
