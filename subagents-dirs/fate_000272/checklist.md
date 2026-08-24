# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000272
- **文件路径**: subagents-dirs/fate_000272/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396382（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000272/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let f(X) ∈ Z[X] be an irreducible polynomial, n_p is the number of solutions of f(X) in F_p, show that lim_{s→1+} (Σ_{p prime} n_p/p^s) / (Σ_{p prime} 1/p^s) = 1.
- 解答核心思路（1-2句话）：利用Chebotarev密度定理和Burnside引理：n_p等于Frobenius元素在根上的不动点数，不可约性保证Galois群传递作用，Burnside引理给出平均不动点数为1，Chebotarev等分布将群平均转化为素数密度平均，从而极限为1。
- 解答关键步骤列表：
  1. 对非分歧素数p，n_p = Frob_p在f的根上的不动点数
  2. f不可约 → G = Gal(K/Q)传递作用在根上
  3. Burnside引理：(1/|G|) Σ_{g∈G} fix(g) = 1（传递作用的平均不动点数）
  4. Chebotarev密度定理：Frob_p在G的共轭类中等分布
  5. 密度加权平均 = 群平均不动点数 = 1 → 极限 = 1
  - 注：Lean文件中定理用sorry占位，无形式化证明。解答为数学证明思路。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察这个问题的结构。分子和分母分别是什么？这个比值极限在数学上属于什么类型的问题？ | 分子是Σ_p n_p/p^s，n_p是f模p的根数；分母是Σ_p 1/p^s。这是一个Dirichlet密度型问题——比值极限衡量的是n_p在素数集合上的密度加权平均。 |
| 2 | 自由列举 | 0.7 | 列出所有可能将n_p（模p根数）与素数密度联系起来的方法。 | (a) 直接逐素数估计n_p；(b) Chebotarev密度定理；(c) Dirichlet算术级数素数定理；(d) Galois理论理解n_p的结构；(e) 解析数论中的L函数方法。 |
| 3 | 小尝试 | 0.5 | 尝试直接估计一般不可约多项式的n_p。能否找到规律或界？ | 对deg(f)=n的不可约多项式，n_p≤n。但这个界不足以确定平均行为——我们需要的是密度加权平均，而非逐个素数的估计。直接估计单素数的n_p无法解决问题。 |
| 4 | 思维操作引导 | 0.4 | 用Galois理论重新诠释n_p。f模p的根数与p处的Frobenius元素有什么关系？ | 对非分歧素数p，n_p等于Frobenius元素Frob_p作用在f的根（在分裂域K中）上的不动点数。这将解析问题转化为群论问题。 |
| 5 | 思维操作引导 | 0.5 | f不可约意味着什么？对Galois群在根上的作用应用Burnside引理。 | f不可约→G=Gal(K/Q)传递作用在根上。由Burnside引理（轨道计数定理），传递作用的平均不动点数为1：(1/|G|)Σ_{g∈G} fix(g)=1。 |
| 6 | 推进 | 0.6 | 现在将群论平均与素数和联系起来。什么定理桥接Frobenius元素的等分布与密度极限？ | Chebotarev密度定理：Frobenius元素在G的共轭类中等分布。因此n_p的密度加权平均等于G中元素的平均不动点数=1（Burnside）。所以极限=1。 |
| 7 | 能量传递引导 | 0.7 | 将所有部分组装起来：写出从不可约性到极限为1的完整证明链。 | f不可约→G传递作用→Burnside给出平均不动点=1→Chebotarev等分布→密度加权平均n_p=1→极限=1。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 素数Dirichlet级数的比值极限；n_p为不可约多项式模p的根数；需将解析数论（密度极限）与代数数论（Galois理论）桥接；核心是证明密度加权平均等于1
- key_objects: ["不可约多项式 f ∈ Z[X]", "n_p (模p根数)", "Dirichlet密度", "Frobenius元素", "Galois群 G", "分裂域 K", "Burnside引理", "Chebotarev密度定理"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_reinterpretation", "group_theoretic_averaging", "density_theorem_application", "proof_chain_assembly"]
- primary_pattern: structural_reinterpretation
- knowledge_required: ["Galois理论", "Frobenius元素", "Chebotarev密度定理", "Burnside引理", "Dirichlet密度", "传递群作用"]
- key_insight: n_p等于Frobenius在根上的不动点数，不可约性保证Galois群传递作用，Burnside引理给出平均不动点数为1，Chebotarev等分布将群平均转化为素数密度平均，极限为1

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 解析数论（素数级数与密度极限）
- translation_to: 代数数论+群论（Frobenius元素、Galois群作用、Burnside引理）
- translation_type: domain_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: ["Chebotarev密度定理", "Frobenius元素", "Burnside引理", "传递群作用", "Dirichlet密度", "不动点计数"]
- expected_ai_method: bare AI会尝试直接估计n_p或用初等界，无法连接到Galois理论和密度定理
- correct_method: 利用Frobenius不动点诠释+Burnside引理+Chebotarev等分布的三步链

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_calculation, gap_type=knowledge_gap均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——此题的核心gap是知识缺失（Chebotarev密度定理），knowledge_gap准确描述
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。现有分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs**：

1. path_feature型：
- scope: "从不可约性到密度极限的完整证明链"
- tell: "整个证明需要连接三个深层结果：Frobenius不动点诠释、Burnside引理、Chebotarev密度定理。没有任何单一步骤能揭示这条链。"
- hint: "将证明构建为：重新诠释n_p → 应用Burnside → 应用Chebotarev → 得出极限=1"
- hint_level: 0.7
- generalizability: "high - 将Galois理论与解析数论通过密度定理桥接的模式可推广到代数数论中的许多问题"
- why_not_visible_locally: "三步链（Frobenius诠释→Burnside→Chebotarev）从任何单一步骤都不可见。每一步的必要性只有在完成前一步后才变得清晰。局部视角只看到个别计算，全局视角才看到证明的架构。"
- tell_topology: {problem_type: characterization, ai_method_type: logical_deduction, gap_type: method_translation}
- tell_small_concepts: ["Frobenius-Burnside-Chebotarev链", "Galois-解析桥接", "密度定理应用"]

2. implicit型：
- scope: "不可约性在证明中的角色"
- observation_point: "R5"
- tell: "f的不可约性不只是假设，而是使G传递作用的关键条件，通过Burnside给出平均=1。没有不可约性，极限会不同。"
- hint: "认识到不可约性→传递Galois作用→Burnside平均=1是关键逻辑依赖"
- hint_level: 0.6
- generalizability: "medium - 不可约性与传递群作用的联系在Galois理论中是标准的，但其在密度定理中的角色是此类问题特有的"
- why_not_visible_locally: "在R5中，应用Burnside引理使用了传递性，但传递性成立的深层原因（不可约性）以及为什么这个特定值（1）是答案，只有在追溯整条逻辑链时才可见。局部步骤只说'应用Burnside'，不揭示不可约性是关键枢纽。"
- tell_topology: {problem_type: characterization, ai_method_type: logical_deduction, gap_type: structural_transformation}
- tell_small_concepts: ["不可约性-传递性联系", "Burnside平均值", "关键枢纽假设"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接估计n_p或用初等界（如n_p≤deg f），无法连接到Galois理论和Chebotarev密度定理。可能尝试用Dirichlet定理但无法将n_p的结构与Frobenius元素联系起来。核心知识缺口是Chebotarev密度定理和Frobenius不动点诠释。
- suitable_for_poc: ["POC-VMS-knowledge-gap", "POC-VMS-domain-translation"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入profile.json

**逐项检查**：
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
- [x] answer
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
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: fate_000272, 7 local pairs, 2 global pairs, answer非None, knowledge_bottleneck为str类型"R4", thinking_bottleneck为str类型"R5", 所有pair含tell_topology和tell_small_concepts, 全局pair含why_not_visible_locally

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000272
- solution_method_type: logical_deduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系（characterization / direct_calculation / knowledge_gap等）足够描述此题
- 是否遇到异常: 否。Lean文件用sorry占位无形式化证明，解答为标准数学证明思路（Chebotarev密度定理+Burnside引理）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
