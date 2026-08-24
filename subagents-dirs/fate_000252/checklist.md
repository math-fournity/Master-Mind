# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000252
- **文件路径**: subagents-dirs/fate_000252/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396362（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000252/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let H be a subgroup of finite index of a group G. Show that there exists a subset S of G, such that S is both a set of representatives of the left and the right cosets of H in G.
- 解答核心思路（1-2句话）：将G分解为双陪集HgH，在每个双陪集内每个左陪集与每个右陪集都相交（通过元素h₁gh₂），且左陪集数等于右陪集数，因此在每个双陪集内做完美匹配，合并即得公共代表系S。
- 解答关键步骤列表：
  1. 将G分解为双陪集 G = ⊔ Hg_iH
  2. 在每个双陪集内，左陪集{h₁gH}和右陪集{Hgh₂}，元素h₁gh₂同时属于两者，故二部图完全
  3. 左陪集数[H:H∩gHg⁻¹] = 右陪集数[H:H∩g⁻¹Hg]（共轭不变性）
  4. 在每个双陪集内做完美匹配，选h₁g_ih₂为代表元
  5. 合并所有双陪集的代表元得到S

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（8轮Q&A）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：左陪集代表系和右陪集代表系分别是什么？"同时"意味着什么？ | 左/右代表系各取一元/陪集，S需同时满足两者，|S|=n=[G:H] |
| 2 | 自由列举 | 0.7 | 列出所有可能的证明方法 | Hall定理、归纳、贪心构造、置换表示约化、双陪集分解 |
| 3 | 小尝试 | 0.4 | 尝试Hall婚配定理，验证Hall条件，哪里卡住？ | 计数论证|I|·|H|≤|N(I)|·|H|需要|H|有限，但H可能无限 |
| 4 | 思维操作引导 | 0.5 | 将G分解为双陪集HgH，左/右陪集如何分布？ | 每个双陪集是左陪集并和右陪集并，双陪集划分G |
| 5 | 推进 | 0.4 | 在双陪集内取左陪集h₁gH和右陪集Hgh₂，找交集元素 | h₁gh₂同时属于h₁gH和Hgh₂，二部图完全 |
| 6 | 思维操作引导 | 0.3 | 验证双陪集内左陪集数=右陪集数 | [H:H∩gHg⁻¹]=[H:H∩g⁻¹Hg]，共轭不变性 |
| 7 | 推进 | 0.4 | 在完全二部图K_{m,m}内做匹配，如何合并？ | 每个双陪集内做双射匹配，选h₁g_ih₂为代表元，合并得S |
| 8 | 能量传递引导 | 0.6 | 组装完整证明 | S是所有双陪集局部代表元的并集，|S|=n，每左/右陪集恰一元 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: finite index subgroup, simultaneous left/right coset representatives, double coset decomposition partitions G, complete bipartite structure within each double coset, equal number of left and right cosets per double coset
- key_objects: group G, subgroup H of finite index, left cosets gH, right cosets Hg, double cosets HgH, common transversal S, intersection H ∩ gHg⁻¹

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [double_coset_decomposition, local_to_global, element_witness, counting_argument, conjugation_invariance]
- primary_pattern: double_coset_decomposition
- knowledge_required: [group theory: cosets and subgroups, double cosets H\G/H and their properties, left and right transversals, index of a subgroup, conjugation preserving subgroup order, coset counting within double cosets]
- key_insight: 在每个双陪集HgH内，元素h₁gh₂同时属于左陪集h₁gH和右陪集Hgh₂，使二部图完全，且左/右陪集数相等，完美匹配平凡存在。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: combinatorial matching via Hall's marriage theorem
- translation_to: double coset decomposition with structural element-witness matching
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [double coset decomposition, left transversal, right transversal, common system of representatives, coset intersection within double cosets, conjugation invariance of subgroup order]
- expected_ai_method: Bare AI会尝试Hall婚配定理的计数论证（H无限时失败），或贪心构造S而不识别双陪集结构
- correct_method: 将G分解为双陪集HgH，观察每个双陪集内左陪集与右陪集完全相交（通过h₁gh₂），计数左/右陪集数相等，在每个双陪集内做匹配

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence / direct_manipulation / structural_transformation 均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 8 对（每轮一个，含per-pair拓扑和小概念）
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试Hall婚配定理的计数论证|I|·|H|≤|N(I)|·|H|，但H可能无限导致失败；或贪心构造/归纳而不识别双陪集结构。双陪集分解和h₁gh₂同时隶属的关键洞察是非显然的结构选择。
- suitable_for_poc: [tell_hint_injection, structural_decomposition_guidance, knowledge_bottleneck_identification]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `subagents-dirs/fate_000252/profile.json`

**字段清单逐项检查**：
- [x] _key（=fate_000252）
- [x] source_id（=FATE-X-3）
- [x] source_dataset（=FATE）
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain（=Abstract Algebra）
- [x] subfield（=Group Theory）
- [x] answer_type（=proof）
- [x] answer（=存在S同时是左/右陪集代表系）
- [x] problem_type（=structural_existence）
- [x] solution_method_type（=double_coset_decomposition）
- [x] structure_features
- [x] key_objects
- [x] thinking_patterns
- [x] primary_pattern
- [x] knowledge_required
- [x] key_insight
- [x] translation_from / translation_to / translation_type
- [x] tell_topology（profile级）
- [x] tell_small_concepts（profile级）
- [x] expected_ai_method
- [x] correct_method
- [x] tell_hint_pairs（8个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个全局pair，含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected / bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R6"为字符串）
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000252
- solution_method_type: double_coset_decomposition
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（structural_existence / direct_manipulation / structural_transformation）足够覆盖
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
