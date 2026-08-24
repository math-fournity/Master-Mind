# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000139
- **文件路径**: subagents-dirs/omni_math_000139/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330011（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000139/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设n≥2，X = {(a_1,...,a_n) | a_k ∈ {0,1,...,k}, k=1,...,n}，定义s∨t为分量max，s∧t为分量min。求X的最大真子集A使得A对∨和∧封闭（即A是X的最大真子格）。|X| = 2·3·...·(n+1) = (n+1)!。
- 解答核心思路（1-2句话）：构造：移除"混合角纤维" F = {x : x_{n-1}=0, x_n=n}（大小(n-1)!），该纤维同时满足join-prime和meet-prime条件，故X\F是子格。上界：投影到最后两坐标C_{n-1}×C_n，若投影为真子格则|π(A)|≤n(n+1)-1，每纤维大小(n-1)!，得|A|≤(n+1)!-(n-1)!。
- 解答关键步骤列表：
  1. 识别X为链的乘积（分配格），|X|=(n+1)!
  2. n=2基础情形：枚举发现移除(0,2)或(1,0)（混合角点）可得最大真子格
  3. 构造：移除纤维F={x: x_{n-1}=0, x_n=n}，大小(n-1)!
  4. 验证join-prime：若s∨t∈F则s_{n-1}=t_{n-1}=0且max(s_n,t_n)=n，故s或t∈F
  5. 验证meet-prime：若s∧t∈F则min(s_{n-1},t_{n-1})=0且s_n=t_n=n，故s或t∈F
  6. 上界：投影π:X→C_{n-1}×C_n，π(A)是子格
  7. 若π(A)真子格：|π(A)|≤n(n+1)-1，|A|≤(n(n+1)-1)·(n-1)!=(n+1)!-(n-1)!
  8. 若π(A)满射：格结构迫使至少一个完整混合角纤维缺失，|A|≤(n+1)!-(n-1)!
  9. 计算验证：n=2答案5=3!-1!，n=3答案22=4!-2!，n=4答案114=5!-3!

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述X的数学结构。X是什么类型的对象？有多少元素？∨和∧运算使它成为什么？ | X是链{0,1,...,k}的笛卡尔积(k=1..n)，|X|=2·3·...·(n+1)=(n+1)!。∨和∧是分量max/min，使X成为分配格（链的乘积）。 |
| 2 | 自由列举 | 0.7 | 有哪些方法可以找到这个格的最大真子格？ | 可能方法：(1)小情形暴力枚举找规律；(2)利用格论概念如join-irreducible、素理想/滤子；(3)投影到更少坐标降维；(4)对n归纳；(5)用Birkhoff定理刻画链乘积的子格。 |
| 3 | 小尝试 | 0.4 | 试n=2的情形。枚举X的所有元素，暴力搜索最大真子格。 | n=2时X={0,1}×{0,1,2}共6个元素。检查所有子集，最大真子格大小为5，通过移除(0,2)或(1,0)得到。这两个是"混合角点"——一个坐标取最小值，另一个取最大值。 |
| 4 | 思维操作引导 | 0.5 | 观察被移除的元素(0,2)和(1,0)。它们有什么共同性质？为什么移除恰好一个能保持子格封闭性？ | 两者都是"混合角点"。关键性质：(0,2)只能表示为s∨t当且仅当s₁=t₁=0且至少一个s₂=2（即该元素本身就是(0,2)）。对∧同理。这意味着(0,2)同时是join-prime和meet-prime——移除它不破坏封闭性，因为任何产生(0,2)的join或meet都必须涉及(0,2)本身。 |
| 5 | 推进 | 0.6 | 将构造推广到一般n。应该移除哪个"纤维"？它的大小是多少？验证它是子格。 | 移除纤维F={x∈X: x_{n-1}=0, x_n=n}——固定最后两坐标为混合角(min of C_{n-1}, max of C_n)。|F|=(n-1)!(前n-2个链的乘积)。join-prime验证：若s∨t∈F则s_{n-1}=t_{n-1}=0且max(s_n,t_n)=n，故s或t∈F。meet-prime验证：若s∧t∈F则min(s_{n-1},t_{n-1})=0且s_n=t_n=n，故s或t∈F。因此X\F是子格，大小(n+1)!-(n-1)!。 |
| 6 | 思维操作引导 | 0.5 | 对于上界证明，考虑将X投影到最后两个坐标(n-1,n)。子格条件对投影意味着什么？ | 投影π(A)是C_{n-1}×C_n的子格（2D网格，大小n×(n+1)）。若π(A)是真子格，则|π(A)|≤n(n+1)-1（由n=2基础情形），每纤维大小(n-1)!，故|A|≤(n(n+1)-1)·(n-1)!=(n+1)!-(n-1)!。若π(A)满射，则A命中每条纤维，但A为真子集意味着某元素缺失，格结构迫使至少一个完整混合角纤维缺失，同样得|A|≤(n+1)!-(n-1)!。 |
| 7 | 能量传递引导 | 0.8 | 综合构造和上界，给出最终答案。 | 构造给出大小(n+1)!-(n-1)!的子格，上界证明没有更大的真子格。答案为(n+1)!-(n-1)!。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: `discrete_combinatorial`（已有值，链乘积的子格计数问题）
- structure_features: 链的乘积C₁×...×Cₙ上的分量max/min运算构成分配格；求最大真子格；混合角纤维移除构造；投影降维上界证明
- key_objects: ["链的乘积(product of chains)", "格运算∨/∧(lattice operations)", "子格(sublattice)", "混合角纤维(mixed corner fiber)", "坐标投影(coordinate projection)", "join-prime和meet-prime条件"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["结构识别(structural recognition)——识别X为链乘积分配格", "小情形枚举(small case enumeration)——n=2暴力搜索", "模式识别(pattern recognition)——混合角点模式", "格论抽象(lattice-theoretic abstraction)——join-prime/meet-prime条件", "纤维推广(fiber generalization)——从单元素到纤维", "降维投影(dimensional reduction via projection)——投影到2D做上界", "纤维计数(fiber counting)——上界论证"]
- primary_pattern: 结构识别与降维投影(structural recognition and dimensional reduction)
- knowledge_required: ["格论基础(join, meet, sublattice)", "链的乘积是分配格", "join-prime和meet-prime条件", "坐标投影保持格结构", "2D网格的最大真子格"]
- key_insight: "混合角纤维——固定两坐标为相反极值(一min一max)——同时满足join-prime和meet-prime，移除后保持子格封闭性

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 暴力枚举小情形(brute force enumeration on small cases)
- translation_to: 格论构造+投影上界(lattice-theoretic construction via fiber removal + projection-based upper bound)
- translation_type: method_translation（从计算枚举方法翻译到结构构造方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["product of chains", "mixed corner fiber", "join-prime", "meet-prime", "coordinate projection", "sublattice closure"]
- expected_ai_method: enumeration_brute_force——bare AI会尝试枚举元素和检查子集，对大n不可行，且不会发现混合角纤维模式
- correct_method: 格论构造（混合角纤维移除）+ 投影降维上界证明

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial、ai_method_type=enumeration_brute_force、gap_type=structural_transformation均归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新拓扑维度——三个维度足以区分此题的tell
- 拓扑进化建议：无

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

全局pairs摘要：
1. (path_feature) 从枚举到格论构造的完整路径——跨维度识别混合角纤维模式
2. (implicit, R4) join-prime/meet-prime性质——构造核心原理但非显式陈述
3. (path_feature) 投影降维上界策略——构造与上界使用不同数学操作

详见profile.json中完整tell_hint_pairs和global_tell_hint_pairs。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会枚举小情形但无法识别混合角纤维模式；可能找到n=2的构造但无法推广到一般n；即使找到构造也无法证明上界（投影降维策略不会自发产生）。关键格论概念（join-prime、meet-prime、投影保持子格）不太可能从零发现。
- suitable_for_poc: ["tell_hint_injection", "structural_recognition_test", "knowledge_bottleneck_detection", "method_translation_test"]
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
- [x] answer（"(n+1)! - (n-1)!"）
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
- [x] tell_hint_pairs（7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（3个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**已将完整JSON写入 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过

profile已写入problem_profiles集合（_key=omni_math_000139），progress记录330011已更新为completed。验证确认7个局部pairs、3个全局pairs，per-pair拓扑存在。

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_000139
- solution_method_type: structural_construction（混合角纤维移除+投影降维上界）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature，1个implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类足够
- 是否遇到异常: 题目文件solution被截断，通过计算验证(n=2,3,4)和数学分析重构完整解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
