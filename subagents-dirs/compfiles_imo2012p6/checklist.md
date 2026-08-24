# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2012p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2012P6.lean
- **来源**: IMO 2012 P6
- **ArangoDB progress记录_key**: 329224（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2012P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find all positive integers n for which there exist non-negative integers a₁, a₂, ..., aₙ such that 1/2^a₁ + 1/2^a₂ + ··· + 1/2^aₙ = 1/3^a₁ + 2/3^a₂ + ··· + n/3^aₙ = 1
- 解答核心思路（1-2句话）：答案为 n ≡ 1 或 2 (mod 4)。必要性通过对第二个方程乘以 3^m 后取 mod 2 得到 n(n+1)/2 为奇数；充分性通过归纳构造（基例 n=1,5,9，归纳步 4k+1→4k+2 和 4k+1→4k+13）覆盖所有 n ≡ 1,2 (mod 4)。
- 解答关键步骤列表：
  1. 必要性：设 m = max(aᵢ)，将第二个方程 Σ i/3^aᵢ = 1 两边乘以 3^m，得 3^m = Σ i·3^(m-aᵢ)
  2. 取 mod 2：因 3^k ≡ 1 (mod 2)，得 1 ≡ Σi = n(n+1)/2 (mod 2)，即 n(n+1)/2 为奇数
  3. n(n+1)/2 为奇数当且仅当 n ≡ 1 或 2 (mod 4)
  4. 充分性基例：n=1 (a₁=0)，n=5 (a₁=a₂=a₃=2, a₄=a₅=3)，n=9 (显式构造)
  5. 归纳步1：4k+1 是解 → 4k+2 是解（将第 j=2k+1 项拆分为两个 aⱼ+1 的项）
  6. 归纳步2：4k+1 是解 → 4k+13 是解（将一项扩展为 13 项）
  7. 覆盖性：任何 n ≡ 1,2 (mod 4) 可写为 12k+4l+r (r∈{1,2}, l<3)，由基例和归纳步覆盖

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | What is the structure of this problem? What are we given and what are we looking for? | We need to find all positive integers n such that there exist non-negative integers a₁,...,aₙ with two simultaneous equations: Σ 1/2^aᵢ = 1 and Σ i/3^aᵢ = 1. This is a characterization problem. |
| 2 | 自由列举 | 0.5 | What approaches could work for this problem? List all directions you can think of. | Possible approaches: (1) Try small cases and look for a pattern. (2) Modular arithmetic. (3) Direct construction. (4) Induction. (5) Generating functions. (6) Analyze constraint structure. |
| 3 | 小尝试 | 0.2 | Try small cases. What happens for n=1,2,3,4,5? | n=1: a₁=0 works. n=2: a₁=a₂=1 works. n=3: fails (e.g. a=(1,2,2) gives 8/9≠1 in second eq). n=4: fails. n=5: works (a₁=a₂=a₃=2, a₄=a₅=3). Pattern suggests n ≡ 1,2 (mod 4). |
| 4 | 思维操作引导 | 0.6 | Look at the second equation Σ i/3^aᵢ = 1. Let m = max(aᵢ). Multiply both sides by 3^m to clear denominators. What integer equation do you get? | 3^m = Σ i · 3^(m-aᵢ). This is an integer equation where each term is a non-negative integer since m ≥ aᵢ for all i. |
| 5 | 推进 | 0.4 | Reduce the equation 3^m = Σ i·3^(m-aᵢ) mod 2. Since 3^k ≡ 1 (mod 2) for all k, what condition on n do you get? | Since 3^k ≡ 1 (mod 2), we get 1 ≡ Σi = n(n+1)/2 (mod 2). So n(n+1)/2 is odd, which happens iff n ≡ 1 or 2 (mod 4). This proves necessity. |
| 6 | 思维操作引导 | 0.7 | Now for sufficiency - if n ≡ 1 or 2 (mod 4), how to construct the aᵢ? What base cases and inductive steps do you need? | Base cases: n=1,5,9. Inductive steps: (1) 4k+1→4k+2 (split term j=2k+1 into two with exponent aⱼ+1). (2) 4k+1→4k+13 (replace one term with 13 terms). Any n ≡ 1,2 (mod 4) = 12k+4l+r with r∈{1,2}, l<3, covered by base cases + induction. |
| 7 | 能量传递引导 | 0.3 | Put it all together - state the complete characterization and proof structure. | The answer is n ≡ 1 or 2 (mod 4). Necessity: mod 2 reduction gives n(n+1)/2 ≡ 1 (mod 2). Sufficiency: base cases n=1,5,9 plus inductive steps 4k+1→4k+2 and 4k+1→4k+13. QED. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 两个联立方程共享变量 aᵢ；第一个方程是 1/2^aᵢ 的无权和（等于1），第二个是 i/3^aᵢ 的加权和（系数为1,2,...,n，等于1）。问题要求刻画所有使得这样的 aᵢ 存在的正整数 n。必要性方向只需第二个方程（mod 2 约束），充分性方向需要同时满足两个方程的构造。
- key_objects: ["正整数 n", "非负整数序列 (a₁,...,aₙ)", "二进有理数 1/2^aᵢ", "加权三进有理数 i/3^aᵢ", "mod 2 奇偶条件", "归纳构造步骤"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["necessity_sufficiency_split", "modular_reduction", "inductive_construction", "pattern_recognition_from_small_cases"]
- primary_pattern: modular_reduction
- knowledge_required: ["modular arithmetic (mod 2)", "parity of n(n+1)/2", "mathematical induction", "sum formula Σi = n(n+1)/2", "3^k ≡ 1 (mod 2)"]
- key_insight: 将第二个方程乘以 3^m（m = max aᵢ）后取 mod 2，因 3^k ≡ 1 (mod 2) 得 n(n+1)/2 ≡ 1 (mod 2)，即 n ≡ 1 或 2 (mod 4)。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: rational_equation_manipulation（有理方程操作）
- translation_to: modular_arithmetic_mod_2（模2算术）
- translation_type: method_translation（方法翻译——从有理方程的精确操作翻译到模算术的奇偶性分析）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: case_by_case, gap_type: method_problem_mismatch}
- tell_small_concepts: ["modular arithmetic reduction", "parity condition", "simultaneous equations", "inductive construction", "base cases", "splitting lemma"]
- expected_ai_method: bare AI 会枚举小案例 (n=1,2,3,4,5,...)，发现 n=1,2,5,6,9,10,... 可行，猜出 n ≡ 1,2 (mod 4) 的模式，但无法证明必要性（mod 2 约简不直观）和充分性（归纳构造需要找到正确的基例和归纳步）。
- correct_method: 必要性通过对第二个方程清分母后取 mod 2 得到 n(n+1)/2 的奇偶条件；充分性通过归纳构造，基例 n=1,5,9，归纳步 4k+1→4k+2 和 4k+1→4k+13。

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization 已有，ai_method_type=case_by_case 已有，gap_type=method_problem_mismatch 已有
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 不需要新维度——三个维度足以区分这道题的 tell
- [ ] 无需进化建议

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs**：

1. path_feature型：
   - scope: necessity-sufficiency structure with different techniques
   - tell: 问题需要必要性（mod 2 约简）和充分性（归纳构造），但两半使用完全不同的数学技术，不能互相推导
   - hint: 拆分为必要性和充分性。必要性用模算术，充分性找基例和归纳步
   - why_not_visible_locally: 从QA序列的任何单轮只能看到论证的一半。完整结构——必要性用 mod 2 约简、充分性用归纳（基例1,5,9 + 步骤4k+1→4k+2, 4k+1→4k+13）——只有在整条解题路径走完后才可见

2. implicit型：
   - observation_point: R4
   - scope: 第二个方程携带对n的约束，第一个方程在必要性方向是red herring
   - tell: 同一组 aᵢ 出现在两个方程中，但只有第二个方程（系数1,2,...,n）通过 mod 2 约简产生对 n 的约束。第一个方程（无权和）对 n mod 4 不提供信息
   - hint: 必要性方向聚焦第二个方程。系数 i=1,2,...,n 使 mod 2 约简产生依赖 n 的条件
   - why_not_visible_locally: 在乘以 3^m 并取 mod 2 的局部步骤中，为什么这能work——系数 i 产生 Σi = n(n+1)/2 依赖 n——不是立即可见的。需要完成整个约简才能理解为什么第二个方程单独决定 n mod 4

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI 会枚举小案例，正确猜出 n ≡ 1,2 (mod 4)，但无法证明必要性（清分母后取 mod 2 的约简不直观）和充分性（找到正确的基例 1,5,9 和归纳步 4k+1→4k+2, 4k+1→4k+13 需要大量创造力）
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_classification"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入 `subagents-dirs/compfiles_imo2012p6/profile.json`

**字段清单检查**：
- [x] _key（=compfiles_imo2012p6）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（n ≡ 1 or 2 (mod 4)）
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
- [x] global_tell_hint_pairs（2个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R6"为字符串类型）
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_imo2012p6, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2012p6
- solution_method_type: modular_arithmetic_and_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类（characterization / case_by_case / method_problem_mismatch等）完全够用
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
