# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003920
- **文件路径**: subagents-dirs/omni_math_003920/problem.lean
- **来源**: omni_math
- **ArangoDB progress记录_key**: 333799（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003920/problem.lean`

**产出**：
- 题目原文（数学描述）：Denote by N the set of all positive integers. Find all functions f: N -> N such that for all positive integers m and n, the integer f(m)+f(n)-mn is nonzero and divides mf(m)+nf(n).
- 解答核心思路（1-2句话）：通过特殊值代入(m=n=1)得到f(1)=1，猜测f(x)=x²，利用因式分解m³+n³=(m+n)(m²-mn+n²)验证整除关系成立。
- 解答关键步骤列表：
  1. 直接代数变形（设k展开）导致矛盾kmn=0，走不通
  2. 代入m=n=1，由2f(1)-1|2f(1)推出f(1)=1
  3. 猜测f(x)=x²，代入验证m²+n²-mn|m³+n³
  4. 利用m³+n³=(m+n)(m²-mn+n²)因式分解，m²-mn+n²恰好是除数，整除成立

---

## Step 2: QA序列分析——局部视角7步 [x]

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 观察这个题目的结构：条件涉及哪些数学对象？已知什么、求什么？ | 条件涉及函数f:N->N，对所有正整数m,n，f(m)+f(n)-mn非零且整除mf(m)+nf(n)。要求找出所有满足条件的函数。 |
| 2 | 自由列举 | 0.5 | 对于这类函数方程问题，你想到哪些可能的解题方向？ | 1)直接代数变形；2)代入特殊值；3)猜测函数形式再验证；4)利用整除性质推导约束。 |
| 3 | 小尝试 | 0.2 | 试试直接代数变形：设mf(m)+nf(n)=k(f(m)+f(n)-mn)，展开后能得到什么？ | 展开得(m-k)f(m)=(k-n)f(n)，m,n独立变化导致矛盾kmn=0不可能。直接变形走不通。 |
| 4 | 思维操作引导 | 0.4 | 直接变形走不通时，试试代入最简单的特殊值。令m=n=1，能得到什么约束？ | 2f(1)-1|2f(1)，设d=2f(1)-1则d|d+1故d=1，f(1)=1。 |
| 5 | 推进 | 0.5 | 已知f(1)=1。继续代入m=1,n=2和m=2,n=2，能推出更多约束吗？尝试猜测f的形式。 | f(2)在{2,4}中，若f(x)=x²则f(2)=4验证通过。模式提示f(x)=x²。 |
| 6 | 思维操作引导 | 0.6 | 猜测f(x)=x²，验证它是否满足原条件。想想m³+n³如何因式分解？ | m³+n³=(m+n)(m²-mn+n²)，而m²+n²-mn=m²-mn+n²恰好是因式的一项，整除成立。 |
| 7 | 能量传递引导 | 0.3 | 验证完成。总结一下关键转折是什么？ | 关键转折在于m²+n²-mn恰好是m³+n³因式分解中的一个因子。路径：特殊值→猜测→因式分解验证。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4（R1纯元认知观察+R2自由列举+R5推进+R7能量传递引导）
- knowledge_rounds: 2（R4思维操作引导+R6思维操作引导）
- level_sum: 2.8
- knowledge_bottleneck: R6（需要联想立方和因式分解公式）
- thinking_bottleneck: R3（直接变形陷入矛盾，需要策略转换）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（刻划所有满足条件的函数）
- structure_features: 函数方程+整除条件，双变量(m,n)约束，要求找出所有满足条件的函数f:N->N。整除关系d=f(m)+f(n)-mn | mf(m)+nf(n)隐含代数恒等式结构。
- key_objects: f:N->N, divisibility relation, d=f(m)+f(n)-mn, m²+n²-mn, m³+n³=(m+n)(m²-mn+n²)

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [specialization, pattern_recognition, guess_and_verify, algebraic_factorization]
- primary_pattern: specialization_and_guess_verify
- knowledge_required: [divisibility_properties, algebraic_factorization_identities, functional_equation_techniques, sum_of_cubes_factorization]
- key_insight: m²+n²-mn恰好是m³+n³=(m+n)(m²-mn+n²)的一个因子，使整除关系自然成立

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_algebraic_manipulation（直接代数变形）
- translation_to: specialization_and_factorization_verification（特殊值代入+因式分解验证）
- translation_type: method_translation（方法翻译——从直接变形翻译到特殊值策略）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: method_problem_mismatch}
- tell_small_concepts: [函数方程, 整除条件, 特殊值代入, 因式分解, m²-mn+n², 策略转换]
- expected_ai_method: 直接代数变形：设k使得mf(m)+nf(n)=k(f(m)+f(n)-mn)，展开后比较系数
- correct_method: 特殊值代入获取约束→猜测二次形式→因式分解验证整除关系

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_manipulation, gap_type=method_problem_mismatch均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- 拓扑进化建议：无，当前分类体系足够

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
- bare_ai_error_prediction: Bare AI会尝试直接代数变形，设k展开后得到矛盾(kmn=0不可能)，然后卡住。不会主动转向特殊值代入策略，也不会联想到m³+n³的因式分解来验证猜测。
- suitable_for_poc: [hint_injection_effectiveness, strategy_switch_detection, knowledge_gap_identification]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：完整profile JSON已写入工作目录的 `profile.json` 文件

**字段检查**：
- [x] _key（=omni_math_003920）
- [x] source_id, source_dataset, schema_version(=3)
- [x] problem_text, solution_text, solution_summary
- [x] domain, subfield, answer_type, answer(="f(x) = x^2")
- [x] problem_type, solution_method_type, structure_features, key_objects
- [x] thinking_patterns, primary_pattern, knowledge_required, key_insight
- [x] translation_from, translation_to, translation_type
- [x] tell_topology（profile级）, tell_small_concepts（profile级）
- [x] expected_ai_method, correct_method
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_003920
- solution_method_type: specialization_guess_verify
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，当前分类体系足够
- 是否遇到异常: 否

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
