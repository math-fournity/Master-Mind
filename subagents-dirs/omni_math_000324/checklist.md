# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000324
- **文件路径**: subagents-dirs/omni_math_000324/problem.lean
- **来源**: AoPS omni_math (imc)
- **ArangoDB progress记录_key**: 330196（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000324/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：判断是否存在正整数n使得g(n) > n^{0.999n}，其中f(n),g(n)是最小正整数使1+1/1!+1/2!+...+1/n!=f(n)/g(n)（即S_n=sum_{k=0}^n 1/k!的既约分数的分母g(n)）。
- 解答核心思路（1-2句话）：定义"特殊素数"（在f(j)中出现密度超过ε的素数），证明只有有限个特殊素数，然后用非特殊素数构造n使g(n)保留大量素因子从而g(n)>n^{0.999n}。
- 解答关键步骤列表：
  1. 设ε=10^{-10}，定义特殊素数：p特殊若存在k∈{1,...,p-1}使至少εk个j≤k满足p|f(j)
  2. 引理：只有有限个特殊素数（利用f(j) mod p的结构性质证明）
  3. 对非特殊素数p，p在{1,...,k}中至多整除εk个f(j)
  4. 构造n为非特殊素数的乘积，使g(n)保留大量素因子
  5. 证明对构造的n，g(n)>n^{0.999n}

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
| 1 | 纯元认知观察 | 0.8 | 这个问题的结构是什么？g(n)是什么？我们要判断什么存在性？ | g(n)是S_n=sum_{k=0}^n 1/k!的既约分数分母，g(n)|n!。要判断是否存在n使g(n)>n^{0.999n}。这是一个存在性问题。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的研究g(n)大小的方法方向 | 直接计算g(n)小值；用n!的界；研究g(n)的素因子结构；研究哪些素数导致约分；概率方法；构造性方法 |
| 3 | 小尝试 | 0.5 | 试着用g(n)≤n!和Stirling公式来bound，看看能否解决 | n!≈(n/e)^n，而n^{0.999n}/n!→0（因为0.001n·ln n增长快于n），所以g(n)≤n!不够紧，需要更精细的分析 |
| 4 | 思维操作引导 | 0.4 | g(n)什么时候会变小？约分发生在什么时候？从素数整除f(n)的角度思考 | g(n)小是因为f(n)和g(n)有公因子，即素数p同时整除f(n)和n!。关键在于哪些素数p整除f(j)，导致约分使分母变小 |
| 5 | 推进 | 0.5 | 定义一个概念来区分"经常整除f(j)"和"很少整除f(j)"的素数，然后证明关于这个概念的引理 | 定义ε=10^{-10}，p是"特殊素数"若存在k使至少εk个j≤k满足p|f(j)。引理：只有有限个特殊素数。证明利用f(j) mod p的递推结构 |
| 6 | 思维操作引导 | 0.3 | 有了"有限个特殊素数"的引理后，如何用非特殊素数构造n使g(n)大？ | 对非特殊素数p，p在{1,...,k}中至多整除εk个f(j)，所以p在g(n)中保留的概率高。取n为大量非特殊素数的乘积，g(n)保留足够多素因子 |
| 7 | 能量传递引导 | 0.6 | 把所有部分组装起来，完成g(n)>n^{0.999n}的最终证明 | 选择n为足够多非特殊素数的乘积，非特殊素数在g(n)中几乎全部保留，g(n)≈n!的足够大比例，超过n^{0.999n}。存在性得证 |

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
- problem_type: structural_existence
- structure_features: 存在性问题——判断是否存在正整数n使g(n)（e的级数部分和的既约分母）超过n^{0.999n}。核心结构是"分母的素因子保留率"与"指数下界"的关系。
- key_objects: ["g(n)——S_n的既约分母", "f(n)——S_n的既约分子", "特殊素数——高密度整除f(j)的素数", "n!——g(n)的上界", "ε=10^{-10}——密度阈值参数"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["problem_reframing——从直接计算g(n)转为研究素因子结构", "definition_creation——创造特殊素数概念", "lemma_proving——证明有限个特殊素数", "constructive_existence——用非特殊素数构造n", "density_argument——用密度阈值ε区分素数行为"]
- primary_pattern: definition_creation（创造"特殊素数"概念是解题的核心转折）
- knowledge_required: ["数论：素数整除性与约分", "级数部分和的递推结构", "Stirling公式与阶乘渐近", "密度论证方法"]
- key_insight: 定义"特殊素数"（以密度ε为阈值区分素数对f(j)的整除行为），证明只有有限个，从而非特殊素数足够多以构造g(n)大的n。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_computation（直接计算/估计g(n)的大小）
- translation_to: prime_factorization_analysis（研究g(n)的素因子结构，通过素数对f(j)的整除密度分类）
- translation_type: structural_transformation（从计算视角到结构视角的转换）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["g(n)分母", "素数整除f(j)", "约分导致分母变小", "特殊素数密度阈值", "非特殊素数构造", "n^{0.999n}下界"]
- expected_ai_method: direct_calculation（bare AI会尝试直接计算g(n)或用n!上界bound，不会想到素因子结构分析）
- correct_method: prime_factorization_density_analysis（通过定义特殊素数、证明有限性、用非特殊素数构造来证明存在性）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence / direct_calculation / structural_transformation 能准确描述这道题的tell
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——这道题的核心gap是"从计算到结构的转换"，structural_transformation准确描述
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。当前分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中tell_hint_pairs字段。
全局pairs详见profile.json中global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接计算g(n)的小值或用n!上界bound，但不会想到研究g(n)的素因子结构、定义"特殊素数"概念、或用密度论证。核心创造性的概念定义（特殊素数）是bare AI几乎不可能自发产生的。
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_bottleneck_identification", "definition_creation_guidance"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整JSON已写入 `subagents-dirs/omni_math_000324/profile.json`。所有必填字段已检查：
- _key, source_id, source_dataset, schema_version ✓
- problem_text, solution_text, solution_summary ✓
- domain, subfield, answer_type, answer ✓
- problem_type, solution_method_type, structure_features, key_objects ✓
- thinking_patterns, primary_pattern, knowledge_required, key_insight ✓
- translation_from, translation_to, translation_type ✓
- tell_topology, tell_small_concepts, expected_ai_method, correct_method ✓
- tell_hint_pairs (7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts) ✓
- global_tell_hint_pairs (2个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts) ✓
- bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels ✓
- qa_sequence (rounds + stats) ✓
- analysis_metadata ✓

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: omni_math_000324, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

- problem_id: omni_math_000324
- solution_method_type: existence_proof_by_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，当前分类体系足够
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
