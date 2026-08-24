# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003839
- **文件路径**: subagents-dirs/omni_math_003839/problem.lean
- **来源**: omni_math
- **ArangoDB progress记录_key**: 333718（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003839/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find the smallest number n such that there exist polynomials f_1, f_2, ..., f_n with rational coefficients satisfying x^2 + 7 = f_1(x)^2 + f_2(x)^2 + ... + f_n(x)^2.
- 解答核心思路（1-2句话）：将多项式平方和问题翻译为二次型表示问题（<1,7>是否被<1,...,1>表示），用Hasse-Minkowski局部-全局原理分析，n≤4在p=2处有局部障碍（行列式不匹配），n=5因维数≥5在各Q_p上迷向故可行。
- 解答关键步骤列表：
  1. 度分析：每个f_i次数≤1，故f_i = a_i*x + b_i
  2. 系数条件：Σa_i²=1, Σa_i*b_i=0, Σb_i²=7
  3. n≤3：7不能写成≤3个有理数平方和（Legendre三平方定理，7≡7 mod 8）
  4. n=4：翻译为二次型<1,7>被<1,1,1,1>表示的问题，用Hasse-Minkowski检查局部条件
  5. n=4在Q_2处失败：det(<1,1,1,1>)=1 ≠ 7=det(<1,7,α,β>) in Q_2*/(Q_2*)²
  6. n=5：<1,1,1,1,1>维数5≥5，在各Q_p上迷向，迷向形式维数≥4时可表示任意正交对
  7. 显式构造：f_1=x, f_2=2, f_3=f_4=f_5=1，验证x²+4+1+1+1=x²+7

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | Describe the structure of this problem. What are we looking for? What constraints do the rational coefficients impose? | We need the smallest n such that x²+7 is a sum of n squares of rational polynomials. Each f_i has degree ≤1, so f_i=a_i*x+b_i. Constraints: Σa_i²=1, Σa_i*b_i=0, Σb_i²=7. |
| 2 | 自由列举 | 0.5 | What approaches could you try to determine the minimum n? List all directions. | Try n=1 (impossible), n=2 (7≡3 mod 4, not sum of 2 squares), n=3 (7≡7 mod 8, Legendre obstruction), n=4 (Lagrange gives 7=4+1+1+1 but need orthogonality), n=5. Also quadratic form theory + Hasse-Minkowski. |
| 3 | 小尝试 | 0.2 | Try n=4 directly. Set f_i=a_i*x+b_i and attempt to find explicit rational coefficients. | Try a=(1,0,0,0): need b₂²+b₃²+b₄²=7, but 7≡7 mod 8 fails Legendre. Try a=(1/2,1/2,1/2,1/2): need t²+s²=7/2, but 7/2 not sum of 2 rational squares. Stuck across all a-vectors. |
| 4 | 思维操作引导 | 0.7 | Translate this to a quadratic form problem. What theorem governs solvability? | This asks whether <1,7> is represented by <1,...,1> over Q. By Hasse-Minkowski, this holds iff it holds over all completions R and Q_p. |
| 5 | 思维操作引导 | 0.8 | Check local conditions for n=4 over Q_2. Compare the determinant invariant. | <1,1,1,1> has det=1. If it represented <1,7>, need <1,1,1,1>≅<1,7>⊥<α,β> with αβ=1/7. Over Q_2, 1/7≡1 mod (Q_2*)², so det(<1,7,α,β>)=7≠1 in Q_2*/(Q_2*)². Contradiction! n=4 fails at p=2. |
| 6 | 推进 | 0.6 | Now check n=5. Does the local obstruction disappear? | <1,1,1,1,1> has dimension 5≥5, isotropic over every Q_p. Isotropic form of dimension≥4 represents any orthogonal pair. So <1,7> is represented over all Q_p and R. By Hasse-Minkowski, n=5 works. |
| 7 | 能量传递引导 | 0.3 | Write down the explicit construction and conclude. | f_1=x, f_2=2, f_3=f_4=f_5=1. Then x²+4+1+1+1=x²+7. Combined with n≤3 fails (Legendre) and n=4 fails (Q_2 obstruction), the answer is n=5. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: Polynomial identity as sum of squares with rational coefficient constraint; minimality requirement; reduces to quadratic form representation over Q via degree analysis; local-global principle governs solvability
- key_objects: ["x^2 + 7", "sum of squares of rational polynomials", "quadratic form <1,7> represented by <1,...,1>", "Hasse-Minkowski local-global principle", "p-adic obstruction at p=2"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["local-global principle", "degree analysis", "quadratic form theory", "explicit construction", "sum of squares number theory", "isotropy argument"]
- primary_pattern: local-global principle
- knowledge_required: ["sum of two squares theorem (primes ≡ 3 mod 4)", "Legendre's three-square theorem (n ≡ 0,4,7 mod 8 excluded)", "Lagrange's four-square theorem", "Hasse-Minkowski theorem", "quadratic forms over Q_p", "Hilbert symbols and local invariants", "isotropy of forms of dimension >= 5 over Q_p"]
- key_insight: The problem reduces to whether the quadratic form <1,7> is represented by <1,...,1> over Q; the local obstruction at p=2 (determinant mismatch 7 ≠ 1 in Q_2*/(Q_2*)^2) prevents n=4, while n=5 works because dimension 5 forms are isotropic over all Q_p

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: polynomial identity problem (sum of squares of rational polynomials)
- translation_to: quadratic form representation theory (diagonal forms over Q)
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["sum of squares", "rational coefficients", "local-global principle", "Hasse-Minkowski", "quadratic form representation", "Legendre three-square", "p-adic obstruction", "determinant in Q_2*/(Q_2*)^2"]
- expected_ai_method: direct_calculation — try to explicitly find polynomials for small n by solving the coefficient equations, without recognizing the quadratic form structure
- correct_method: quadratic form theory via Hasse-Minkowski local-global principle — translate to form representation, check local conditions at each prime

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是，structural_existence / direct_calculation / method_translation 均为已有值
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是，均为抽象/中等粒度
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI will likely try to construct explicit polynomials for n=1,2,3,4 by solving coefficient equations. It may correctly rule out n<=3 using Legendre's theorem, but will likely either (a) incorrectly conclude n=4 works by citing Lagrange's four-square theorem without checking the polynomial orthogonality constraint, or (b) get stuck trying various a-vectors for n=4 without recognizing the quadratic form translation. The key missing knowledge is the Hasse-Minkowski local-global principle and the p-adic determinant obstruction at p=2.
- suitable_for_poc: ["POC-VMS-8 hint injection", "POC-VMS-9 tell detection", "tell-hint pair validation"]
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
- [x] answer（"5"）
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已完成

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="333718"`的记录

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, answer=5, per-pair拓扑存在, progress记录已更新）

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: omni_math_003839
- solution_method_type: quadratic_form_local_global
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类体系完全覆盖
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
