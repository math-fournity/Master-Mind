# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003880
- **文件路径**: subagents-dirs/omni_math_003880/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333759（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003880/problem.lean`

**产出**：
- 题目原文（数学描述）：D(x,y)定义为唯一整数d满足2^d≤|x-y|<2^{d+1}。给定实数集F，x∈F的scales是D(x,y)对y∈F,y≠x的值。给定正整数k，每个x∈F在F中至多有k个不同scales。求F的最大可能size。答案2^k。来源：IMO 2019 Shortlist C9 (Italy)。
- 解答核心思路（1-2句话）：构造F={0,1,...,2^k-1}达到2^k；上界通过加权引理w(S)=Σ2^{-r_S(x)}≤1（r_S(x)是x在S中的scale数），用归纳法证明。关键洞察：最小scale d只出现在相邻元素之间（非相邻元素距离≥2·2^d=2^{d+1}），因此按奇偶拆分最大d-scale连续段可消除scale d。
- 解答关键步骤列表：
  1. 构造：F={0,1,...,2^k-1}，每个元素恰好k个scales {0,...,k-1}
  2. 定义权重 w(S)=Σ_{x∈S} 2^{-r_S(x)}，证明w(S)≤1
  3. 归纳基础|S|=1：r=0, w=1
  4. 关键观察：最小scale d只出现在相邻元素间（非相邻距离≥2^{d+1}）
  5. 找最大d-scale连续段x_i,...,x_j，按奇偶分为E（偶数下标）和O（奇数下标），R为剩余
  6. S_O=R∪O, S_E=R∪E，均比S小，归纳假设w(S_O),w(S_E)≤1
  7. R中元素：r不变；O中元素在S_O中失去scale d（r减1）；E中元素在S_E中失去scale d
  8. w(S)≤(1/2)(w(S_O)+w(S_E))≤1
  9. 由w(F)≥|F|·2^{-k}得|F|≤2^k

---

## Step 2: QA序列分析——局部视角7步 [x]

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：D(x,y)是什么？每个元素的scales是什么？约束条件和目标分别是什么？ | D(x,y)是dyadic scale函数，将距离映射到整数d使2^d≤|x-y|<2^{d+1}。x的scales是{x到F中所有其他元素的D值集合}。约束：每个x至多k个不同scales。目标：最大化|F|。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用于解决这道题的方法方向，包括直接计数、归纳法、构造法、加权方法等 | 可能方向：1)小case分析(k=1,2)猜答案；2)对k归纳，空间拆分F；3)构造达到下界的例子；4)用势函数/权函数方法；5)图论方法(将scales看作边着色)；6)信息论方法 |
| 3 | 小尝试 | 0.5 | 试k=1和k=2的小case，猜测答案形式，并尝试构造达到该答案的集合F | k=1:|F|≤2(3个元素中中间元素有2个scale)。k=2:猜测|F|≤4，构造F={0,1,2,3}每个元素scales={0,1}。猜测答案2^k，构造F={0,...,2^k-1} |
| 4 | 思维操作引导 | 0.4 | 对排序后的F={x_1<...<x_n}，设d是最小scale。证明：d只出现在相邻元素之间，即对任意j-i>1，D(x_i,x_j)>d | 因为d是最小scale，所有距离≥2^d。对j-i>1，|x_i-x_j|=|x_i-x_{i+1}|+...+|x_{j-1}-x_j|≥2·2^d=2^{d+1}，所以D(x_i,x_j)≥d+1>d。关键：最小scale的相邻性 |
| 5 | 思维操作引导 | 0.3 | 定义权重w(S)=Σ_{x∈S} 2^{-r_S(x)}，其中r_S(x)是x在S中的scale数。解释为什么证明w(S)≤1就能得到|F|≤2^k | 因为r_F(x)≤k对所有x，所以2^{-r_F(x)}≥2^{-k}，因此w(F)≥|F|·2^{-k}。若w(F)≤1则|F|≤2^k。权重设计使得scale多的元素贡献小，恰好匹配二分拆分的1/2因子 |
| 6 | 推进 | 0.3 | 利用最小scale d的相邻性，设计一个将S拆分为两个更小子集S_O和S_E的方案，使得归纳假设可以应用 | 找最大d-scale连续段x_i,...,x_j，按奇偶分E(偶下标)O(奇下标)，R为剩余。S_O=R∪O, S_E=R∪E。O中元素在S_O中失去scale d(r减1)，E中元素在S_E中失去scale d，R中元素r不变 |
| 7 | 能量传递引导 | 0.2 | 将以上所有观察组合，完成w(S)≤1的归纳证明 | w(S)=Σ_R 2^{-r}+Σ_O 2^{-r}+Σ_E 2^{-r}≤(1/2)Σ_R(2^{-r_SO}+2^{-r_SE})+(1/2)Σ_O 2^{-r_SO}+(1/2)Σ_E 2^{-r_SE}=(1/2)(w(S_O)+w(S_E))≤1。QED |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.3+0.3+0.2=3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: dyadic scale function on ordered reals, per-element scale count constraint, extremal set size problem, minimum scale adjacency property
- key_objects: D(x,y) dyadic scale, scales of x, set F, positive integer k, weight function w(S)=Σ2^{-r_S(x)}

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["small_case_analysis", "weighted_potential_function", "induction_on_set_size", "parity_split", "extremal_construction"]
- primary_pattern: weighted_potential_function
- knowledge_required: ["dyadic intervals and scales", "mathematical induction", "extremal combinatorics", "potential function method"]
- key_insight: 最小scale d只出现在相邻元素之间（非相邻距离≥2^{d+1}），因此按奇偶拆分最大d-scale连续段可消除scale d，使权重w(S)=Σ2^{-r_S(x)}的归纳以(1/2)(w(S_O)+w(S_E))≤1闭合

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_size_bound（直接对|F|做归纳，空间拆分）
- translation_to: weighted_potential_induction（对权重函数w(S)做归纳，奇偶拆分）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["dyadic_scale", "minimum_scale_adjacency", "weighted_potential", "parity_split", "induction_on_set_size"]
- expected_ai_method: direct_calculation（bare AI会尝试直接对|F|归纳，空间拆分F为两半，但cross-scale与within-scale重叠导致k无法递减）
- correct_method: weighted_potential_induction（正确方法用权重函数w(S)=Σ2^{-r_S(x)}和奇偶拆分归纳）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial、ai_method_type=direct_calculation、gap_type=method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新拓扑维度

**拓扑进化建议**：无。现有分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中的tell_hint_pairs字段。
全局pairs详见profile.json中的global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接对|F|做归纳，用空间拆分（如中位数拆分或最小scale分组），但cross-scale与within-scale重叠导致k无法在子问题中递减。不会发现权重函数w(S)=Σ2^{-r_S(x)}这一非显然的势函数，也不会想到用奇偶拆分来消除最小scale。最终可能猜到答案2^k但无法证明上界。
- suitable_for_poc: ["tell_hint_injection", "weighted_potential_discovery", "structural_insight_verification"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_003880/profile.json`。所有字段均已填写，包括：
- _key, source_id, source_dataset, schema_version=3
- problem_text, solution_text, solution_summary
- domain, subfield, answer_type, answer=2^k
- problem_type, solution_method_type, structure_features, key_objects
- thinking_patterns, primary_pattern, knowledge_required, key_insight
- translation_from, translation_to, translation_type
- tell_topology, tell_small_concepts, expected_ai_method, correct_method
- tell_hint_pairs (7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts)
- global_tell_hint_pairs (2个全局pair：1个path_feature型+1个implicit型，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts)
- bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels
- qa_sequence (7轮rounds + stats含knowledge_bottleneck="R5", thinking_bottleneck="R6")
- analysis_metadata

---

## Step 10: 入库ArangoDB [x]

- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, answer=2^k, knowledge_bottleneck=R5, thinking_bottleneck=R6）

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003880
- solution_method_type: weighted_potential_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，现有分类体系足够
- 是否遇到异常: 否（problem.lean中solution被截断，但从IMO 2019 Shortlist官方PDF获取了完整解答）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
