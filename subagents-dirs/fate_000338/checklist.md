# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000338
- **文件路径**: subagents-dirs/fate_000338/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396448（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000338/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Prove that if #G = 336 then G is not simple. （336 = 2^4 × 3 × 7）
- 解答核心思路（1-2句话）：用Sylow定理分析Sylow 7-子群个数n_7∈{1,8}；n_7=1则正规；n_7=8时用共轭作用给出G→S_8的同态，核非平凡则得正规子群，核平凡则G嵌入S_8，通过符号同态（点稳定子AGL(1,7)含奇置换）得指数2正规子群。
- 解答关键步骤列表：
  1. 336 = 2^4 × 3 × 7，用Sylow定理分析n_7：n_7 | 48 且 n_7 ≡ 1 (mod 7)，故 n_7 ∈ {1, 8}
  2. n_7 = 1：唯一Sylow 7-子群正规，G非单
  3. n_7 = 8：共轭作用在8个Sylow 7-子群上给出同态 φ: G → S_8
  4. ker φ ≠ 1：ker φ是真非平凡正规子群（真因为作用非平凡），G非单
  5. ker φ = 1：G嵌入S_8为336阶传递子群，点稳定子为N_G(P)阶42，即AGL(1,7)⊂S_7
  6. AGL(1,7)含奇置换（x↦3x mod 7是6-圈，奇置换），故G⊄A_8
  7. 符号同态sgn: G→{±1}满射，ker(sgn)是指数2正规子群，G非单

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述这道题的结构：G是什么？336的素因数分解是什么？"不是单群"意味着什么？ | G是有限群，|G|=336=2^4×3×7。"不是单群"意味着G存在一个真非平凡正规子群。已知条件是群的阶，目标是证明存在性。 |
| 2 | 自由列举 | 0.5 | 列出你所知道的所有证明一个群不是单群的方法。 | Sylow定理（计数Sylow子群，n_p=1则正规）；群作用（共轭作用给出到对称群的同态，核是正规子群）；计数论证（元素计数导致矛盾）；Burnside定理（p^a q^b阶群可解）；指数论证。 |
| 3 | 小尝试 | 0.3 | 用Sylow定理分析Sylow 2-子群的个数n_2，看看能得到什么。 | n_2 | 21 且 n_2为奇数，故 n_2 ∈ {1, 3, 7, 21}。n_2=1则正规；n_2=3时作用到S_3，核非平凡（|S_3|=6<336）；但n_2=7和n_2=21时S_7和S_21都足够大，嵌入可能，无法直接排除。 |
| 4 | 思维操作引导 | 0.4 | Sylow 2的情况太多，换一个角度：用最大的素数7。计算n_7的约束。 | n_7 | 48 且 n_7 ≡ 1 (mod 7)。48的因子中≡1 mod 7的只有1和8。所以 n_7 ∈ {1, 8}，只有两种情况！ |
| 5 | 推进 | 0.5 | n_7=1已经解决。现在处理n_7=8：G通过共轭作用在8个Sylow 7-子群上，这给出什么同态？核的情况如何？ | 共轭作用给出同态 φ: G → S_8。如果ker φ ≠ 1，它是真非平凡正规子群（真因为作用非平凡，n_7=8>1），G非单。如果ker φ = 1，G嵌入S_8为336阶传递子群。 |
| 6 | 思维操作引导 | 0.7 | G嵌入S_8后，考虑符号同态sgn: G→{±1}。G能否包含在A_8中？分析点稳定子的奇偶性。 | 点稳定子是N_G(P)，阶42。在S_8中它固定一点，作用于其余7点，等于S_7中7-圈的标准正规化AGL(1,7)。AGL(1,7)中x↦3x mod 7是{1,...,6}上的6-圈（奇置换），所以AGL(1,7)⊄A_7，故G⊄A_8。sgn满射，ker(sgn)是指数2正规子群。 |
| 7 | 能量传递引导 | 0.3 | 把所有情况汇总，写出完整证明。 | n_7=1→Sylow 7正规；n_7=8, ker φ≠1→ker φ是正规子群；n_7=8, ker φ=1→符号同态给出指数2正规子群。所有情况G都不是单群。∎ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.2+0.5+0.3+0.4+0.5+0.7+0.3 = 2.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 给定有限群的阶数336=2^4×3×7，证明群不是单群（存在真非平凡正规子群）。核心是通过Sylow定理+群作用+符号同态的组合论证完成存在性证明。
- key_objects: ["有限群G", "Sylow 7-子群", "Sylow定理", "共轭作用", "对称群S_8", "符号同态", "AGL(1,7)"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["sylow_counting", "group_action_homomorphism", "sign_argument", "case_analysis", "stabilizer_analysis"]
- primary_pattern: sylow_counting
- knowledge_required: ["Sylow定理", "群作用与共轭作用", "对称群与交错群", "符号同态", "循环群在对称群中的正规化子(AGL(1,p))", "置换的奇偶性"]
- key_insight: 当n_7=8且G嵌入S_8时，点稳定子AGL(1,7)含奇置换（x↦3x是6-圈），故G⊄A_8，符号同态给出指数2的正规子群。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: sylow_counting（Sylow计数方法，直接数n_p的值）
- translation_to: group_action_sign_argument（群作用+符号同态方法，通过嵌入对称群再利用奇偶性）
- translation_type: method_translation（从计数方法翻译到作用方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "case_by_case", gap_type: "method_translation"}
- tell_small_concepts: ["sylow_7", "n_7_constraints", "conjugation_action", "S_8_embedding", "sign_homomorphism", "AGL_1_7", "odd_permutation", "point_stabilizer"]
- expected_ai_method: bare AI预期会用case_by_case方法逐个检查Sylow 2/3/7子群，但会在n_2=7,21和n_7=8的嵌入情况中卡住，不知道用符号同态收尾。
- correct_method: 先用Sylow定理选最大素数7将情况压缩到{n_1, n_8}两种，再用共轭作用嵌入S_8，最后用符号同态（点稳定子含奇置换）证明G⊄A_8得指数2正规子群。

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence、ai_method_type=case_by_case、gap_type=method_translation均可归入已有拓扑类别。
- [x] 粒度一致——case_by_case和method_translation与已有值粒度统一。
- [x] 不需要新的拓扑维度——三个维度足以区分这道题的tell。
- 无拓扑进化建议。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pair摘要：
- R1: tell=AI识别题目结构但未选工具, hint=描述所见, level=0.2, 纯元认知观察, topology=(structural_existence, direct_calculation, method_problem_mismatch)
- R2: tell=AI列出方法但未承诺Sylow, hint=列举所有方向, level=0.5, 自由列举, topology=(structural_existence, enumeration_brute_force, search_space_estimation)
- R3: tell=AI试Sylow 2但n_2=7,21卡住, hint=试Sylow 2, level=0.3, 小尝试, topology=(structural_existence, case_by_case, method_problem_mismatch)
- R4: tell=AI未考虑Sylow 7, hint=用最大素数7, level=0.4, 思维操作引导, topology=(structural_existence, case_by_case, knowledge_gap)
- R5: tell=AI算出n_7∈{1,8}但不知如何处理n_7=8, hint=用共轭作用, level=0.5, 推进, topology=(structural_existence, logical_deduction, method_translation)
- R6: tell=AI嵌入S_8但未想到符号同态, hint=考虑符号同态和点稳定子奇偶性, level=0.7, 思维操作引导, topology=(structural_existence, logical_deduction, knowledge_gap)
- R7: tell=AI有所有碎片需组装, hint=汇总成完整证明, level=0.3, 能量传递引导, topology=(structural_existence, logical_deduction, method_translation)

全局pair摘要：
- GP1 (path_feature): 完整路径Sylow7→共轭作用→符号同态是全局策略，局部不可见
- GP2 (implicit): AGL(1,7)含奇置换是隐藏属性，在Sylow计数步骤中无信号

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI大概率会先试Sylow 2-子群，发现n_2∈{1,3,7,21}，解决n_2=1和n_2=3后在n_2=7,21卡住。即使转向Sylow 7得到n_7∈{1,8}，在n_7=8的嵌入情况下也不太会想到用符号同态+点稳定子奇偶性来收尾。关键知识瓶颈是AGL(1,7)含奇置换这个事实。
- suitable_for_poc: ["tell_extraction", "hint_injection", "method_translation"]
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
- [x] answer（proof类型填要证明的结论）
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
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**已将完整JSON写入 `subagents-dirs/fate_000338/profile.json`**

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, per-pair拓扑存在）

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000338
- solution_method_type: sylow_theorem_with_group_action
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类够用
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
