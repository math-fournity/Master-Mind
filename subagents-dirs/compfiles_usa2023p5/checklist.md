# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2023p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2023P5.lean
- **来源**: USA 2023 P5
- **ArangoDB progress记录_key**: 329500（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2023P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let n > 2. Arrange numbers 1..n² into n×n grid. Row-valid = each row permutable to AP. Column-valid = each column permutable to AP. Determine values of n for which any row-valid arrangement can be transformed into column-valid by permuting within rows.
- 解答核心思路（1-2句话）：Answer is n must be prime. For prime n, AP residue class bijectivity enables column construction in two cases (difference divisible/not divisible by n). For composite n, Trygub counterexample using smallest prime factor q blocks column-validity.
- 解答关键步骤列表：
  1. Prime case: extract each row's AP data (permutation p_r, common difference k_r)
  2. Case A: some row has k_r | n → all rows have k_r | n → each row is one residue class mod n → place by quotient → columns are APs with diff 1
  3. Case B: no row has k_r | n → each row hits all residues mod n (prime property) → place by residue → columns are APs with diff n
  4. Composite case: let q = smallest prime factor of n, construct Trygub arrangement (row 0 = 0..n-1, rows 1..q = APs with diff q, rest in reading order)
  5. Show column containing 1 must have difference exactly n (bounding argument)
  6. Then n+1 and 2n+1 both in row 2 → contradiction

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | What is the structure of this problem? What does row-valid mean, what does column-valid mean, and what transformation are we allowed to use? | We have an n×n grid with numbers 1..n². Row-valid means each row can be permuted into an AP. Column-valid means each column can be permuted into an AP. We can only permute within rows. We need to determine for which n this is always possible. |
| 2 | 自由列举 | 0.5 | List all possible directions to explore: what values of n should we try? What mathematical tools might be relevant? | Try small cases: n=3 (prime), n=4 (composite), n=5 (prime), n=6 (composite). Consider prime vs composite distinction. Think about modular arithmetic, residue classes, and what structure APs have mod n. |
| 3 | 小尝试 | 0.4 | Try n=4 (composite): can you construct a row-valid arrangement that cannot be made column-valid? | Attempt to construct a counterexample. Simple constructions may fail — e.g., a grid where all rows are APs with difference 1 can easily be rearranged. Need a more clever construction that exploits the composite structure of n. |
| 4 | 思维操作引导 | 0.6 | What property of prime n ensures that an AP of length n with common difference k (not divisible by n) hits every residue class mod n exactly once? How does this connect to the problem? | For prime n, if n∤k then k is invertible mod n, so the map m ↦ a + mk mod n is a bijection on Z/nZ. This means each row's AP covers all residue classes mod n exactly once. This bijectivity is key to constructing column permutations. |
| 5 | 推进 | 0.5 | Using the prime insight, prove that for prime n any row-valid arrangement can be made column-valid. Consider two cases based on whether any row's AP difference is divisible by n. | Case A: some row has difference divisible by n → all rows must (otherwise two rows share a value) → each row is one residue class, place by quotient. Case B: no row's difference divisible by n → each row hits all residues, place by residue. Both give column APs. |
| 6 | 思维操作引导 | 0.7 | For composite n with smallest prime factor q, construct a specific row-valid arrangement (Trygub construction) that cannot be made column-valid. How does q create the obstruction? | Construct: row 0 = 0,1,...,n-1 (diff 1); rows 1..q = APs with diff q filling n..nq+n-1; remaining rows in reading order (diff 1). This is row-valid. The key is that rows 1..q have APs with difference q, creating a structure that blocks column rearrangement. |
| 7 | 能量传递引导 | 0.3 | Verify the counterexample works: show the column containing 1 must have difference n, but then n+1 and 2n+1 both fall in row 2 — contradiction. You're almost done! | By bounding (base ≤ n-1, max ≥ n²-n), the column difference must be n-1, n, or n+1. Only n works for the column containing 1. Then n+1 and 2n+1 are in this column, but both lie in row 2 of the Trygub arrangement — impossible since they'd need different rows. QED. |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: n×n grid with numbers 1..n²; row-valid = each row permutable to AP; column-valid = each column permutable to AP; transformation = permuting within rows only; characterize n
- key_objects: ["arithmetic progressions", "n×n grid", "permutations", "residue classes mod n", "prime numbers", "quotient-remainder decomposition"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["case_analysis", "modular_arithmetic_reasoning", "constructive_counterexample", "bifurcation_by_divisibility", "bijectivity_argument"]
- primary_pattern: bifurcation_by_divisibility — the key split is whether any row's AP difference is divisible by n
- knowledge_required: ["arithmetic progressions", "modular arithmetic", "prime numbers and ZMod", "bijectivity of finite maps", "residue classes", "quotient-remainder decomposition"]
- key_insight: For prime n, an AP of length n with difference not divisible by n hits every residue class mod n exactly once — this bijectivity is what makes the column construction work

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: combinatorial grid arrangement
- translation_to: modular arithmetic / residue class analysis
- translation_type: method_translation — translating the grid permutation problem into modular arithmetic structure

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "case_by_case", gap_type: "method_translation"}
- tell_small_concepts: ["arithmetic progression", "residue class", "prime divisibility", "bijectivity", "quotient-remainder", "counterexample construction"]
- expected_ai_method: case_by_case — bare AI might try case analysis on small values without seeing the modular arithmetic structure
- correct_method: modular arithmetic with prime structure — using residue classes and the prime property to construct column permutations

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/case_by_case/method_translation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

局部pairs详见profile.json中的tell_hint_pairs字段。
全局pairs详见profile.json中的global_tell_hint_pairs字段。

关键全局pair：
1. path_feature型：整个证明结构的bifurcation（prime→residue bijectivity, composite→counterexample）
2. implicit型（observation_point=R4）：primality与AP residue class coverage的隐藏联系
3. path_feature型：composite case的Trygub counterexample构造及其验证

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI would likely try small cases and perhaps guess that the answer is 'all n' or 'prime n' but fail to construct the full proof. The key obstacles are: (1) seeing the prime/AP/residue class connection, (2) the two-case split in the prime proof by divisibility of AP differences, (3) constructing the Trygub counterexample for composite n with the delicate bounding argument
- suitable_for_poc: ["tell_hint_injection", "topology_matching", "knowledge_bottleneck_detection"]
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
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已写入 subagents-dirs/compfiles_usa2023p5/profile.json

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 3 global pairs, knowledge_bottleneck=str(R4), thinking_bottleneck=str(R6), answer非None, why_not_visible_locally非None, per-pair tell_topology存在

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2023p5
- solution_method_type: case_analysis_with_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3 (2 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。已有分类体系（characterization/case_by_case/method_translation等）足够覆盖此题
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
