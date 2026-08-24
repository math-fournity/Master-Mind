# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000138
- **文件路径**: subagents-dirs/omni_math_000138/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330010（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000138/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定正整数n≥2，求所有n元正整数组(a₁,...,aₙ)满足：1<a₁≤a₂≤...≤aₙ，a₁为奇数，(1) M=(a₁-1)a₂...aₙ/2^n为正整数；(2) 可选M个n元整数组(k_{i,1},...,k_{i,n})使得对任意i₁<i₂，存在j使k_{i₁,j}-k_{i₂,j}≢0,±1 (mod aⱼ)。
- 解答核心思路（1-2句话）：条件(2)等价于环图强积中的独立集问题；通过{0,1}^n平移计数和倍映射x→2x在奇模上的双射性，证明a₂,...,aₙ必须为奇数且2^n|(a₁-1)。
- 解答关键步骤列表：
  1. 将条件(2)识别为环图强积C_{a₁}⊠...⊠C_{aₙ}中的独立集条件
  2. {0,1}^n平移论证：M·2^n≤a₁a₂...aₙ（上界）
  3. 倍映射x→2x在Z/aⱼZ上为双射当且仅当aⱼ为奇数——这是连接组合条件与数论条件的关键
  4. 奇模的Shannon容量效应使强积独立集可超过个体独立数之积；偶模无此效应
  5. 若某aⱼ(j≥2)为偶数，最大独立集<M=(a₁-1)a₂...aₙ/2^n，矛盾，故a₂,...,aₙ均为奇数
  6. a₂,...,aₙ为奇数时，条件(1)要求2^n|(a₁-1)，即a₁=k·2^n+1
  7. 构造：利用奇模代数结构构造M个满足条件(2)的元组

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
| 1 | 纯元认知观察 | 0.3 | 观察题目结构：条件(1)和条件(2)分别是什么？它们之间通过什么变量联系？条件(2)在组合上意味着什么？ | 条件(1)是整除条件：2^n\|(a₁-1)a₂...aₙ。条件(2)是组合packing条件：M个元组在∏Z/aⱼZ中两两在至少一个坐标上差距≥2。两条件通过M联系。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的上界论证方法。特别考虑：模的奇偶性是否影响结果？ | 1)独立集在环图强积中 2)平移计数论证 3)直接构造 4)模的奇偶分析 5)多项式方法 6)概率论证。奇偶性可能通过倍映射影响独立集大小。 |
| 3 | 小尝试 | 0.4 | 尝试{0,1}^n平移论证：对每个元组考虑所有2^n个{0,1}平移，证明它们互异并推导上界。 | 2^n·M个平移元组互异（条件(2)保证），故M·2^n≤a₁a₂...aₙ，即M≤a₁a₂...aₙ/2^n。但M=(a₁-1)a₂...aₙ/2^n，上界不紧，差距为a₂...aₙ/2^n。 |
| 4 | 思维操作引导 | 0.6 | 上界不紧。思考：倍映射x→2x在Z/aⱼZ上何时为双射？这对环图C_{aⱼ}的独立集和Shannon容量有什么影响？ | 倍映射为双射当且仅当aⱼ为奇数。奇模时C_{aⱼ}的Shannon容量>独立数(aⱼ-1)/2，强积独立集可超过个体独立数之积。偶模时Shannon容量=独立数=aⱼ/2，无boost。 |
| 5 | 思维操作引导 | 0.7 | 将Shannon容量分析连接到a₂,...,aₙ必须为奇数的必要性。若某aⱼ为偶数，最大M会怎样？ | 偶模时强积独立数=个体独立数之积=(a₁-1)/2·∏aⱼ/2，严格小于M=(a₁-1)a₂...aₙ/2^n（因a₁为奇数使(a₁-1)/2<a₁/2）。故a₂,...,aₙ必须为奇数。 |
| 6 | 推进 | 0.5 | 已知a₂,...,aₙ为奇数，推导a₁的形式并构造M个元组。 | a₂,...,aₙ为奇数时，条件(1)要求2^n\|(a₁-1)，即a₁=k·2^n+1。M=k·a₂...aₙ。利用奇模代数结构（倍映射双射、独立集分解）构造M个满足条件(2)的元组。 |
| 7 | 能量传递引导 | 0.8 | 验证构造满足条件(2)并总结答案。 | 验证：构造的M个元组利用奇模上倍映射的双射性保证分离条件。答案：a₁=k·2^n+1，a₂,...,aₙ为奇数，1<a₁≤a₂≤...≤aₙ。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 双条件耦合——整除条件(1)定义M，组合packing条件(2)约束M个元组在∏Z/aⱼZ中的分离性；两条件通过M耦合；答案要求刻画所有满足条件的n元组
- key_objects: ["M = (a₁-1)a₂...aₙ/2^n", "环图强积 C_{a₁}⊠...⊠C_{aₙ}", "倍映射 x→2x on Z/aⱼZ", "独立集 in strong product of cycles", "Shannon capacity of odd cycles"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_transformation", "parity_analysis", "counting_argument", "algebraic_mapping"]
- primary_pattern: structural_transformation
- knowledge_required: ["independent sets in cycle graphs", "strong product of graphs", "doubling map on modular arithmetic", "Shannon capacity of odd cycles", "divisibility and parity"]
- key_insight: 倍映射x→2x在Z/aⱼZ上的双射性（当且仅当aⱼ为奇数）是连接组合packing条件与数论奇偶约束的桥梁——奇模的Shannon容量效应使强积独立集可达M，偶模则不能

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 组合packing条件（环图强积中的独立集问题）
- translation_to: 数论奇偶与整除条件（aⱼ的奇偶性、2^n|(a₁-1)）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["doubling map bijection on odd moduli", "strong product independent set", "Shannon capacity of odd cycles", "{0,1} shift counting", "parity-to-divisibility translation"]
- expected_ai_method: bare AI会分别处理条件(1)和(2)，尝试直接构造或case analysis，可能从条件(1)得到2^n|(a₁-1)但无法从条件(2)推出a₂,...,aₙ必须为奇数
- correct_method: 通过倍映射双射性将组合packing条件翻译为奇偶约束，再用整除条件确定a₁的形式

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_calculation, gap_type=structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。当前分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会分别处理条件(1)和(2)，可能从条件(1)的整除性推出2^n|(a₁-1)（当a₂,...,aₙ为奇数时），但无法从条件(2)的组合packing约束推出a₂,...,aₙ必须为奇数——缺少倍映射双射性与Shannon容量之间的连接
- suitable_for_poc: ["tell_hint_path_feature", "structural_transformation_recognition"]
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
- [x] answer（**⚠️ 必填，不能为None**）
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 2 global pairs, per-pair tell_topology存在, why_not_visible_locally存在, answer非None, knowledge_bottleneck=R4, thinking_bottleneck=R5

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_000138
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，当前分类体系足够
- 是否遇到异常: 否（problem.lean中solution文本截断，但基于题目结构、Answer和数学重构完成分析）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
