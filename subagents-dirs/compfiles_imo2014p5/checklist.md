# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2014p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2014P5.lean
- **来源**: IMO 2014 P5
- **ArangoDB progress记录_key**: 329231（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2014P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：For every positive integer n, the Bank of Cape Town issues coins of denomination 1/n. Given a finite collection of such coins (of not necessarily different denominations) with total value at most 99 + 1/2, prove that it is possible to split this collection into 100 or fewer groups, such that each group has total value at most 1.
- 解答核心思路（1-2句话）：对硬币数量做强归纳，定义容量函数cap(k)=k-k/(2k+1)。通过合并偶数面额对（1/(2m)+1/(2m)=1/m）和提取完整奇数面额组（(2m+1)×1/(2m+1)=1）进行归一化，然后贪心装箱剩余轻硬币。
- 解答关键步骤列表：
  1. 定义cap(k)=k-k/(2k+1)，证明cap(k)-1≤cap(k-1)
  2. 对硬币数N做强归纳
  3. Case 1（偶数合并）：面额2m出现≥2次时，合并两枚1/(2m)为一枚1/m，减少硬币数，用IH
  4. Case 2（奇数提取）：面额2m+1出现≥2m+1次时，提取2m+1枚为价值1的组，剩余用k-1组的IH
  5. Case 3（归一化）：偶数面额≤1次，奇数面额2m+1≤2m次。将(2m+1,2m+2)配对入k个箱子，每箱价值<1，贪心分配轻硬币
  6. 验证cap(100)=20000/201≈99.5025>99.5

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**每轮必须标注**：
- **question**：给AI的提示/问题（Q）
- **expected_answer**：预期回复（A）
- **situation_type**：**⚠️ 只能取以下6个值之一，禁止自创**：
  - `纯元认知观察`——让AI描述题目结构、识别已知/未知
  - `自由列举`——让AI列出所有可能方向
  - `小尝试`——让AI试一个方向（可能走错的）
  - `思维操作引导`——给AI具体的思维操作指令
  - `推进`——让AI继续推进当前方向
  - `能量传递引导`——给AI信心/能量，收尾
- **level**：**⚠️ 必须是0-1之间的浮点数**（0=完全具体，1=完全抽象。禁止用1-4整数）

**QA序列设计原则**：
1. 第1轮通常是`纯元认知观察`——让AI描述题目结构
2. 第2轮通常是`自由列举`——让AI列出所有可能方向
3. 第3轮通常是`小尝试`——让AI试一个可能走错的方向
4. 中间几轮根据情况用`思维操作引导`或`推进`
5. 最后一轮通常是`能量传递引导`——收尾

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：已知（硬币面额1/n，总值≤99.5）、未知（如何分组）、难点（1/n的算术结构） | 99.5接近100几乎没有余量，朴素平均论证失败，需要利用1/n的特殊结构 |
| 2 | 自由列举 | 0.5 | 列出所有可能方法：贪心装箱、归纳、概率方法、面额结构分析等 | 归纳+面额结构分析最有前景，因为1/n有特殊代数性质 |
| 3 | 小尝试 | 0.2 | 试朴素贪心：按面额排序逐组填充，什么会出错？ | 贪心不利用1/n结构，小硬币累积导致溢出，紧界下任何误算都致命 |
| 4 | 思维操作引导 | 0.6 | 1/n有什么特殊结构？1/(2m)+1/(2m)=1/m，(2m+1)×1/(2m+1)=1，能否归一化？ | 关键恒等式允许合并偶数对和提取奇数组，归一化后偶数≤1次、奇数2m+1≤2m次 |
| 5 | 思维操作引导 | 0.7 | 设计容量函数cap(k)做强归纳：合并偶数对、提取奇数组、否则归一化 | cap(k)=k-k/(2k+1)，三种case分别处理，归一化case单独处理 |
| 6 | 推进 | 0.5 | 归一化case：配对(2m+1,2m+2)入箱，每箱<1，贪心分配轻硬币 | 箱B_m价值≤2m/(2m+1)+1/(2m+2)<1，轻硬币≤1/(2k+1)，贪心矛盾给出总值>cap(k) |
| 7 | 能量传递引导 | 0.3 | 验证cap(100)=20000/201≈99.5025>99.5，证明完成！ | cap(100)>99.5，定理对k=100成立，证明完成 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**操作**：从题目结构中提取

**要求**：
- `problem_type`：问题类型大概念。**优先使用已有值**（见下方拓扑分类体系），如需新建确保粒度一致
- `structure_features`：题目结构特征描述
- `key_objects`：核心数学对象列表

**已有problem_type值**（优先使用）：
- `structural_existence` ✅ 抽象
- `discrete_combinatorial` ✅ 抽象
- `trigonometric_identity` ✅ 中等
- `constraint_satisfaction` ✅ 中等
- `characterization` ✅ 抽象
- `inequality_proof` ✅ 中等
- `absolute_value_system` ⚠️ 偏具体
- `functional_equation_periodicity` ⚠️ 偏具体
- **❌ 不要用太具体的值**（如`word_problem_with_diophantine_constraint`是错误粒度）

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 硬币面额1/n的算术结构；总值界99.5接近100几乎无余量；关键恒等式1/(2m)+1/(2m)=1/m和(2m+1)×1/(2m+1)=1；容量函数cap(k)=k-k/(2k+1)对贪心论证紧
- key_objects: 面额1/n的硬币、容量函数cap(k)、价值≤1的分组、归一化后的硬币集合（偶数≤1次、奇数≤2m次）、配对面额(2m+1,2m+2)的箱子B_m

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["structural_normalization", "strong_induction", "greedy_packing", "capacity_function_design", "case_analysis_with_reduction"]
- primary_pattern: structural_normalization
- knowledge_required: ["harmonic series and reciprocal arithmetic", "bin packing and greedy algorithms", "strong induction on combinatorial objects", "rational number arithmetic", "partition and covering arguments"]
- key_insight: 归一化硬币集合——合并偶数面额对（1/(2m)+1/(2m)=1/m）和提取完整奇数面额组（(2m+1)×1/(2m+1)=1），然后用容量函数cap(k)=k-k/(2k+1)使贪心装箱剩余轻硬币成为可能。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct bin packing（直接装箱）
- translation_to: normalized structural induction with capacity function（归一化结构归纳+容量函数）
- translation_type: structural_transformation（结构变换——通过归一化将问题变换为可贪心处理的形式）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["coin_denomination", "normalization", "capacity_function", "even_merge_identity", "odd_group_identity", "greedy_packing", "consecutive_pairing", "strong_induction"]
- expected_ai_method: 朴素贪心装箱——按面额排序逐组填充，不利用1/n结构，不设计容量函数
- correct_method: 强归纳+归一化（合并偶数对、提取奇数组）+容量函数cap(k)=k-k/(2k+1)+贪心装箱轻硬币

**已有ai_method_type值**（优先使用）：
- `enumeration_brute_force` ✅ 抽象
- `continuous_analytic` ✅ 抽象
- `direct_calculation` ✅ 抽象
- `logical_deduction` ✅ 抽象
- `case_by_case` ✅ 抽象
- `algebraic_identity` ✅ 中等
- `equation_solving` ✅ 抽象
- `direct_manipulation` ✅ 抽象
- **❌ 不要用太长太具体的值**

**已有gap_type值**（优先使用）：
- `method_problem_mismatch` ✅ 抽象
- `knowledge_gap` ✅ 抽象
- `structural_transformation` ✅ 中等
- `search_space_estimation` ✅ 中等
- `method_translation` ✅ 中等
- `global_sorting` ⚠️ 偏具体
- **❌ 不要用太具体的值**

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。discrete_combinatorial（已有）、enumeration_brute_force（已有）、structural_transformation（已有）均适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个维度都用已有值，粒度匹配。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是"需要结构变换才能贪心"，structural_transformation准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。已有拓扑分类完全适用。

**拓扑进化建议**（如有）：无。已有拓扑分类够用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**⚠️ 每个tell_hint_pair必须包含以下所有字段**：
- `qa_round`: int（对应QA序列的第几轮）
- `tell`: string（AI在这个位置的状态/分叉信号）
- `hint`: string（给AI的提示方向）
- `hint_level`: float（**⚠️ 0-1浮点数，禁止1-4整数**）
- `situation_type`: string（**⚠️ 只能取6个规范值之一**）
- `is_knowledge_bottleneck`: boolean（这轮是否是纯知识瓶颈）
- `tell_topology`: object（**⚠️ 每个pair都要有，不能全用profile级拓扑**）
  - `{problem_type, ai_method_type, gap_type}`
  - **不同轮次的pair可能有不同的拓扑**——比如R1是`(inequality_proof, direct_calculation, method_problem_mismatch)`，R2是`(structural_existence, case_by_case, structural_transformation)`
  - `is_knowledge_bottleneck=True`的pair，`gap_type`应该用`knowledge_gap`
- `tell_small_concepts`: array[string]（**⚠️ 每个pair都要有**，是这个tell特有的小概念信号词）

**同时提取全局(tell, hint)对**：
- `scope_type`: "path_feature"（路径特征型）或 "implicit"（蕴含型）
- `scope`: 具体范围描述
- `observation_point`: 蕴含型填Q编号，路径特征型填null
- `tell`: 全局tell
- `hint`: 全局hint
- `hint_level`: float（0-1）
- `generalizability`: "high/medium/low + 泛化描述"
- `why_not_visible_locally`: **必填字段，不能为None**。path_feature型和implicit型都要填。path_feature型填"完整路径特征为什么在局部视角看不到"；implicit型填"这个蕴含信息为什么在局部步骤中不可见"
- `tell_topology`: object（**⚠️ 每个全局pair也要有**）
- `tell_small_concepts`: array[string]（**⚠️ 每个全局pair也要有**）

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试朴素贪心装箱（按面额排序逐组填充），不识别归一化的必要性。失败原因：(1)总值界99.5非常接近100，几乎没有余量；(2)没有结构恒等式1/(2m)+1/(2m)=1/m和(2m+1)×1/(2m+1)=1，无法降维问题；(3)没有容量函数cap(k)=k-k/(2k+1)，贪心论证没有形式化界可用。AI可能尝试简单平均论证（100组平均0.995<1）但这失败因为单组可超1。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-structural-transformation"]
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
- [x] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/compfiles_imo2014p5/profile.json`

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）→ ✅ 完成
2. 更新`problem_extraction_progress`集合中`_key="329231"`的记录 → ✅ 完成

**验证**：入库后查询确认 → ✅ 通过
- compfiles_imo2014p5 存在于 problem_profiles
- 7 local pairs, 3 global pairs
- per-pair topology 存在
- global pair why_not_visible_locally 非 None
- answer 非 None
- knowledge_bottleneck 为字符串类型 "R4"

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2014p5
- solution_method_type: structural_induction_with_normalization
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（path_feature型2个，implicit型1个）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。已有拓扑分类（discrete_combinatorial / enumeration_brute_force / structural_transformation等）完全适用，粒度一致，无需新增维度。
- 是否遇到异常: 否。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
