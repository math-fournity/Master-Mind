# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000350
- **文件路径**: subagents-dirs/fate_000350/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396460（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000350/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设p,q,r为三个不同的素数，t为正整数。G为有限群，H为G的正规子群且|G/H|=r^t。H有一个长度为2的合成列，因子依次为Z/pZ和Z/qZ。G有一个合成列，其中存在i<j使得第i个因子为Z/qZ，第j个因子为Z/pZ。证明H存在一个长度为2的合成列，因子依次为Z/qZ和Z/pZ（即因子顺序可以交换）。
- 解答核心思路（1-2句话）：Lean证明为sorry（无实际证明）。数学证明核心：将G的合成列与H相交，由Zassenhaus（蝴蝶）引理，非平凡因子保持原序，而r-因子相交后变为平凡（因H的合成因子只有Z/pZ和Z/qZ），因此得到H的合成列中Z/qZ在Z/pZ之前。
- 解答关键步骤列表：
  1. 由|G/H|=r^t且r≠p,q，推出G/H的合成因子全为Z/rZ
  2. 由Jordan-Hölder定理，G的合成因子为{Z/pZ, Z/qZ, Z/rZ×t}
  3. 将G的合成列{e}=G_0⊲G_1⊲...⊲G_n=G与H相交，得到H的子群列
  4. 由Zassenhaus引理，每个相交因子(G_{k+1}∩H)/(G_k∩H)或为平凡或同构于G_{k+1}/G_k
  5. 由Jordan-Hölder定理应用于H，r-因子对应的相交因子必为平凡（否则H会有Z/rZ因子，矛盾），p和q因子对应的相交因子非平凡
  6. 去除平凡步骤后，非平凡因子保持G中原序：因i<j（q在p前），得到H的合成列因子依次为Z/qZ、Z/pZ

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：有哪些已知对象？需要证明什么？关键条件之间有什么联系？ | 已知三个不同素数p,q,r，正整数t，有限群G，正规子群H且|G/H|=r^t。H有长度2的合成列，因子依次Z/pZ、Z/qZ。G有合成列且存在i<j使第i因子Z/qZ、第j因子Z/pZ。需证H存在合成列因子依次Z/qZ、Z/pZ。关键联系：G的合成列中因子顺序与H的合成列因子顺序相反。 |
| 2 | 自由列举 | 0.7 | 群论中有哪些工具可以关联G的合成列和H的合成列？列出所有可能的方向。 | Jordan-Hölder定理（合成因子唯一性）、Zassenhaus/蝴蝶引理（子群列相交）、Schreier加细定理、Sylow定理（分析H的结构）、对应定理（G/H的子群与G中包含H的子群）。 |
| 3 | 小尝试 | 0.5 | 尝试用Sylow定理直接分析H的结构。由于|H|=pq，能否直接证明H的两个Sylow子群都正规，从而因子顺序可交换？ | 由合成列长度2知|H|=pq。已知H有正规子群阶为p（Sylow p-子群正规）。但仅凭Sylow定理无法直接推出Sylow q-子群也正规——当p<q时Sylow q-子群必正规，当q<p时未必。更关键的是，这个方向完全没有用到G的合成列条件，可能走错路。 |
| 4 | 思维操作引导 | 0.4 | 换一个角度：条件|G/H|=r^t且r≠p,q告诉了你什么关于G的合成因子归属的信息？ | |G/H|=r^t，r为素数且r≠p,q。G/H的合成因子全为Z/rZ（因为r^t阶群的合成因子只能是Z/rZ）。由Jordan-Hölder定理，G的合成因子={Z/pZ, Z/qZ, Z/rZ×t}。因此G合成列中的Z/pZ和Z/qZ因子必然来自H，Z/rZ因子来自G/H。 |
| 5 | 思维操作引导 | 0.3 | 现在应用Zassenhaus（蝴蝶）引理：将G的合成列与H相交，得到什么？每个相交因子的结构如何？ | 将{e}=G_0⊲...⊲G_n=G与H相交得{e}=G_0∩H⊲...⊲G_n∩H=H。由Zassenhaus引理，(G_{k+1}∩H)/(G_k∩H)同构于G_{k+1}/G_k的某个商群。因G_{k+1}/G_k是单群，相交因子或为平凡或同构于G_{k+1}/G_k本身。 |
| 6 | 推进 | 0.5 | 结合以上观察：r-因子相交后平凡，p和q因子相交后非平凡且保持原序。由此得到H的什么合成列？ | 由Jordan-Hölder应用于H，H的合成因子只有Z/pZ和Z/qZ，所以r-因子对应的相交因子必为平凡（否则H会有Z/rZ因子，矛盾）。去除平凡步骤后，非平凡因子保持G中原序。因i<j（Z/qZ在Z/pZ前），得到H的合成列因子依次为Z/qZ、Z/pZ。 |
| 7 | 能量传递引导 | 0.6 | 验证：这个合成列长度为2吗？因子正确吗？完成证明。 | 是的。H恰有两个非平凡合成因子（Z/pZ和Z/qZ），故长度为2。第一个因子Z/qZ（来自G中位置i），第二个Z/pZ（来自G中位置j）。这正是需要证明的存在性。证明完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 给定群G的合成列中因子的顺序条件，需证明子群H存在特定顺序的合成列。核心结构是将G的合成列与正规子群H相交，利用Zassenhaus引理保持因子顺序。
- key_objects: 有限群G、正规子群H、合成列(composition series)、合成因子(composition factors)、Zassenhaus引理、Jordan-Hölder定理、商群G/H

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_reframing"（从直接分析H重构为利用G的合成列）, "factor_attribution"（将合成因子归属到H或G/H）, "series_intersection"（合成列与子群相交）, "order_preservation"（相交后非平凡因子保持原序）]
- primary_pattern: structural_reframing
- knowledge_required: ["合成列定义与性质", "Jordan-Hölder定理", "Zassenhaus/蝴蝶引理", "Sylow定理（背景知识）", "正规子群与商群", "单群概念"]
- key_insight: |G/H|=r^t且r≠p,q迫使G合成列中的Z/pZ和Z/qZ因子来自H；将G的合成列与H相交，由Zassenhaus引理非平凡因子保持原序，因i<j（q在p前）即得H的合成列因子依次为Z/qZ、Z/pZ。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接分析H的群结构（Sylow定理、pq阶群分类）
- translation_to: 利用G的合成列与H相交（Zassenhaus引理 + Jordan-Hölder定理）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["Zassenhaus引理", "蝴蝶引理", "合成列相交", "因子顺序保持", "G/H商群因子归属", "r^t素数幂商群", "Jordan-Hölder合成因子唯一性"]
- expected_ai_method: bare AI会直接用Sylow定理分析H的群结构（pq阶群），试图证明H是循环群从而因子可交换，但不会利用G的合成列条件
- correct_method: 将G的合成列与H相交，由Zassenhaus引理提取H的合成列，利用因子顺序保持性得到所需结论

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(structural_existence)/ai_method_type(direct_manipulation)/gap_type(method_translation)均可归入已有拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无

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
- bare_ai_error_prediction: bare AI会用Sylow定理直接分析H的群结构（pq阶群），试图证明H是循环群从而两个Sylow子群都正规、因子顺序可交换。但这个方向无法利用G的合成列中q在p前这一关键条件，且当H非循环时Sylow方法无法给出因子可交换的结论。AI不会想到将G的合成列与H相交这一结构性方法。
- suitable_for_poc: ["tell_matching", "hint_injection", "method_translation_poc"]
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
- problem_id: fate_000350
- solution_method_type: zassenhaus_intersection
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类足够
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
