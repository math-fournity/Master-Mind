# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000114
- **文件路径**: subagents-dirs/omni_math_000114/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329985（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000114/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let a,b be integers with gcd(a,b) having ≥2 prime factors. S={x∈ℕ: x≡a mod b}. y∈S irreducible if cannot be product of ≥2 elements of S. Show ∃t such that any element of S = product of ≤t irreducibles.
- 解答核心思路（1-2句话）：在算术同余半群(ACM)中，利用d=gcd(a,b)整除所有S元素的性质，建立d²∤x的不可约性判据，再用d的两个素因子做递归分裂，通过Davenport常数给出显式界t=max{2q, q-1+2M}。
- 解答关键步骤列表：
  1. 每个x∈S被d=gcd(a,b)整除
  2. x不可约 ⟺ d²∤x（某素数p|d使v_p(x)=v_p(d)）
  3. 取d的两个不同素因子p,q，将y=y₁·y₂分裂为p-极小和q-极小
  4. p-极小元素的不可约因子数由Davenport常数D(G)控制
  5. 合并得t=max{2q, q-1+2M}，其中q=d最小素因子，M=D(G)-1

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（7轮QA）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | S在乘法下有什么结构？gcd(a,b)在决定S元素时起什么作用？ | S是乘法半群(a²≡a mod b保证封闭性)，每个x∈S被d=gcd(a,b)整除 |
| 2 | 自由列举 | 0.6 | 列出所有可能的不可约因子数上界方法，什么使元素不可约vs可约？ | 可能方法：Z中唯一分解、整除性分析、d的素因子结构、小例子找模式、递归论证 |
| 3 | 小尝试 | 0.5 | 尝试用Z中唯一分解直接界定S中不可约因子数，可行吗？什么障碍？ | 不可行——S是ℤ的真子半群，Z中素数在S中可能可约，S中不可约在Z中可能合数 |
| 4 | 思维操作引导 | 0.4 | d=gcd(a,b)整除a和b，所以d整除S中每个x。若y=y₁·y₂且y₁,y₂∈S，y满足什么整除条件？ | d|y₁且d|y₂所以d²|y。因此d²∤y意味着y不可约。逆：d²|y则可分解 |
| 5 | 思维操作引导 | 0.3 | 已知x不可约⟺d²∤x。d有≥2素因子，如何用两个不同素数p,q|d分裂y∈S？ | 取p,q|d，将y=y₁·y₂使v_p(y₁)=v_p(d)(p-极小)且v_q(y₂)=v_q(d)(q-极小) |
| 6 | 推进 | 0.3 | p-极小元素的不可约因子数如何界定？什么数学不变量给出这个界？ | Davenport常数D(G)控制，G=Z_{p₁^α₁}×...×Z_{p_r^α_r}，通过block monoid零和结构 |
| 7 | 能量传递引导 | 0.2 | 合并双素数分裂与Davenport常数界，t=max{2q,q-1+2M}的两项各来自何处？ | 2q来自最小素因子直接计数，q-1+2M来自Davenport常数结构(M=D(G)-1) |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R5为思维操作引导，R6推进也含知识瓶颈，总计知识相关4轮但按situation_type分knowledge_rounds=2）
- level_sum: 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence（证明存在界t使得S中元素可分解为≤t个不可约元素之积）
- structure_features: 算术同余半群S={x∈ℕ:x≡a mod b}，乘法封闭(a²≡a mod b)，d=gcd(a,b)有≥2素因子构成"全局"结构，不可约性由d²∤x刻画，因子分解界涉及有限交换群的Davenport常数
- key_objects: 算术同余半群S, d=gcd(a,b)(≥2素因子), 不可约元素(d²∤x), Davenport常数D(G), 有限交换群G=Z_{p₁^α₁}×...×Z_{p_r^α_r}, p-adic赋值v_p(x)

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [structural_analysis, divisibility_based_characterization, recursive_factorization_bounding, transfer_homomorphism_to_block_monoid, davenport_constant_application, two_prime_decomposition_strategy]
- primary_pattern: divisibility_based_characterization
- knowledge_required: [arithmetic_congruence_monoids, irreducible_factorization_in_monoids, p-adic_valuations, Davenport_constant_of_finite_abelian_groups, block_monoids_and_zero-sum_theory, Chinese_remainder_theorem, transfer_homomorphisms_in_factorization_theory]
- key_insight: 每个S中元素被d=gcd(a,b)整除，所以x不可约⟺d²∤x（某素数p|d有v_p(x)=v_p(d)）；利用d的两个不同素因子可递归分裂任意元素为p-极小和q-极小部分，通过Davenport常数界定因子分解长度

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_factorization_in_N（直接在自然数中做因子分解）
- translation_to: block_monoid_zero_sum_in_finite_abelian_group（翻译到有限交换群上的block monoid零和问题）
- translation_type: structural_transformation（通过transfer homomorphism将ACM因子分解问题转化为零和问题）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: [d_squared_divisibility_irreducibility_criterion, davenport_constant_bounded_factorization, two_prime_recursive_splitting, p_adic_valuation_minimality, transfer_to_block_monoid]
- expected_ai_method: bare AI会尝试直接在Z中做因子分解并计数不可约因子，可能用唯一分解定理但不认识S的半群结构
- correct_method: 通过d²∤x刻画不可约性，用d的两个素因子做递归分裂，通过Davenport常数给出显式界

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/direct_calculation/knowledge_gap均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足够区分
- 拓扑进化建议：无。已有拓扑分类体系可充分覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

（详细内容见profile.json中的tell_hint_pairs和global_tell_hint_pairs数组）

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会失败因为：(1)不认识S是乘法半群有特殊因子分解结构，(2)不会推导d²∤x的不可约性判据，(3)不知道Davenport常数及其在界定因子分解长度中的角色，(4)可能尝试用Z中唯一分解但不适用于子半群。没有非唯一分解理论知识，无法发现与Davenport常数的联系。
- suitable_for_poc: [tell_detection_poc - d²不可约判据是可从AI thinking中检测的清晰tell, knowledge_bottleneck_poc - Davenport常数是纯知识瓶颈无法推导, structural_transformation_poc - 从直接因子分解到block monoid的结构转化]
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
- [x] answer（t = max{2q, q-1+2M}）
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
- [x] tell_hint_pairs（7对，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（3对，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**已写入 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 3 global pairs, per-pair拓扑存在, why_not_visible_locally存在, answer非None, knowledge_bottleneck="R4", thinking_bottleneck="R5"）

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_000114
- solution_method_type: structural_reduction（通过d²∤x刻画不可约性→双素数递归分裂→Davenport常数界定）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（1个path_feature型，2个implicit型）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类体系可充分覆盖
- 是否遇到异常: problem.lean中解答被截断（仅6行），通过AoPS搜索和ACM文献重建了完整解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
