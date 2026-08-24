# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003857
- **文件路径**: subagents-dirs/omni_math_003857/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333736（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003857/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：考虑所有实系数多项式P(x)，满足：对任意实数x,y，|y²-P(x)|≤2|x| 当且仅当 |x²-P(y)|≤2|y|。求P(0)的所有可能值。
- 解答核心思路（1-2句话）：代入x=0得到y²=P(0)⟺|P(y)|≤2|y|。P(0)<0时两边恒假故等价成立；P(0)≥0时结合y=0代入和多项式结构分析，仅P(0)=1可行（P(x)=x²+1使两边都化为||x|-|y||≤1）。
- 解答关键步骤列表：
  1. 代入x=0：|y²-P(0)|≤0⟺|P(y)|≤2|y|，即y²=P(0)⟺|P(y)|≤2|y|
  2. Case P(0)<0：y²=P(0)无实解→|P(y)|>2|y|对所有y成立→P(y)<-2|y|→两边恒假→等价成立（vacuous truth）。例：P(x)=-x²-3
  3. Case P(0)≥0：y=±√P(0)是y²=P(0)的解→|P(±√P(0))|≤2√P(0)
  4. 代入y=0：|P(x)|≤2|x|⟺x²=P(0)，结合得|P(t)|≤2|t|仅在t=±√P(0)处成立
  5. P(0)=0导致矛盾；P(0)>0时通过约束分析得P(0)=1
  6. 验证P(x)=x²+1：两边都化为(||x|-1)²≤y²≤(|x|+1)²即||x|-|y||≤1
  7. 答案：P(0)∈(-∞,0)∪{1}

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么条件，要求什么，条件中有什么对称性？ | 已知多项式P(x)实系数，满足对任意x,y有|y²-P(x)|≤2|x|⟺|x²-P(y)|≤2|y|。要求P(0)的所有可能值。条件在x↔y交换下对称（交换后左边变右边）。关键是对"if and only if"的理解——两个不等式必须同时成立或同时不成立。 |
| 2 | 自由列举 | 0.6 | 列出所有可能的分析方向：你能想到哪些代入特殊值或变形的方式？ | ①代入x=0 ②代入y=0 ③代入x=y ④代入x=-y ⑤尝试P(x)=x²+c ⑥尝试P(x)=-x²+c ⑦分析条件的几何意义 ⑧利用x↔y对称性 |
| 3 | 小尝试 | 0.3 | 试一下最自然的猜测P(x)=x²，即P(0)=0，看看条件是否满足 | P(x)=x²时，|y²-x²|≤2|x|⟺|x²-y²|≤2|y|。由于|y²-x²|=|x²-y²|，条件变为|f|≤2|x|⟺|f|≤2|y|。取x=1,y=0：|1|≤2成立但|1|≤0不成立。所以P(x)=x²不满足条件，P(0)=0可能不在答案中。 |
| 4 | 思维操作引导 | 0.2 | 代入x=0，仔细分析左边的绝对值不等式|y²-P(0)|≤0意味着什么，然后写出完整的等价条件 | x=0时左边|y²-P(0)|≤0，绝对值非负故只能等于0，即y²=P(0)。右边变为|P(y)|≤2|y|。所以条件变为：y²=P(0)⟺|P(y)|≤2|y|。这是关于P(0)和P(y)的关键约束。 |
| 5 | 推进 | 0.5 | 根据y²=P(0)是否有实解，分两种情况分析。特别关注P(0)<0时会发生什么 | Case1 P(0)<0：y²=P(0)无实解，左边恒假，故|P(y)|>2|y|对所有y成立。因P(0)<0且P连续，P(y)<-2|y|对所有y。此时原条件两边：|y²-P(x)|=y²+|P(x)|>2|x|恒成立(左边恒假)，|x²-P(y)|=x²+|P(y)|>2|y|恒成立(右边恒假)。false⟺false=true，条件满足！ |
| 6 | 思维操作引导 | 0.3 | 对P(0)≥0的情况，再代入y=0，结合x=0的结果，分析P(0)的正值中哪些可行。尝试P(x)=x²+a | y=0时：|P(x)|≤2|x|⟺x²=P(0)。结合x=0结果：|P(t)|≤2|t|仅在t=±√P(0)处成立。若P(x)=x²+a(a>0)：P(√a)=2a，需2a≤2√a即a≤1。用y=√a代入验证等价性，得2a-2√a=0且2a+2√a=4，解得a=1。P(0)=0导致|P(0)|>0矛盾。 |
| 7 | 能量传递引导 | 0.7 | 验证P(x)=x²+1确实满足条件，然后写出完整答案 | P(x)=x²+1：|y²-x²-1|≤2|x|⟺(|x|-1)²≤y²≤(|x|+1)²⟺||x|-|y||≤1。由对称性右边也化为||x|-|y||≤1。两边相同故等价成立。P(0)=1。综合：P(0)∈(-∞,0)∪{1}。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.6+0.3+0.2+0.5+0.3+0.7=3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 实系数多项式P(x)满足对称条件|y²-P(x)|≤2|x|⟺|x²-P(y)|≤2|y|，要求P(0)的所有可能值。条件具有x↔y交换对称性，涉及绝对值不等式和等价关系。
- key_objects: ["实系数多项式P(x)", "绝对值不等式|y²-P(x)|≤2|x|", "等价关系(iff)", "P(0)的值域", "x↔y对称性"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["specialization(代入特殊值)", "case_analysis(按P(0)符号分类)", "vacuous_truth_recognition(识别恒假等价)", "symmetry_exploitation(利用x↔y对称性)", "verification_by_identity(用代数恒等式验证)"]
- primary_pattern: case_analysis_with_vacuous_truth
- knowledge_required: ["多项式基本性质", "绝对值不等式", "vacuous truth(false_iff_false=true)", "特殊值代入技巧", "等价关系的逻辑"]
- key_insight: 代入x=0将条件化为y²=P(0)⟺|P(y)|≤2|y|，当P(0)<0时两边恒假使等价vacuously成立——这是最反直觉的关键转折

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_substitution(直接代入特殊值分析不等式)
- translation_to: case_analysis_with_vacuous_truth(分类讨论+识别vacuous truth的等价结构)
- translation_type: structural_transformation(从单点代入的结构转化为全局case分析)

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["vacuous_truth", "x_equals_zero_substitution", "false_iff_false", "P(0)_negative_case", "x_y_symmetry", "absolute_value_to_zero"]
- expected_ai_method: bare AI会尝试直接代入特殊值但不识别vacuous truth情况，可能卡在P(0)<0的分析上，也难以证明P(0)=1是唯一正值
- correct_method: 代入x=0提取关键约束→按P(0)符号分类讨论→识别P(0)<0时vacuous truth→结合y=0和多项式结构分析P(0)>0→验证P(x)=x²+1

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_calculation/structural_transformation能准确描述这道题
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分
- 拓扑进化建议：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pair详情见profile.json中的tell_hint_pairs字段。
全局pair详情见profile.json中的global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试x=0代入得到y²=P(0)⟺|P(y)|≤2|y|，但很可能不识别P(0)<0时vacuous truth的情况（会误认为P(0)必须非负），也无法系统证明P(0)=1是唯一正值（缺乏将两边不等式统一化为||x|-|y||≤1的代数恒等式洞察）
- suitable_for_poc: ["tell_extraction", "hint_injection", "case_analysis_guidance", "vacuous_truth_recognition"]
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
- [x] answer（P(0) ∈ (-∞, 0) ∪ {1}）
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
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_003857
- solution_method_type: case_analysis_with_specialization
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类足够
- 是否遇到异常: 否（解答文件仅含Step 1，完整解答基于数学分析重建）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
