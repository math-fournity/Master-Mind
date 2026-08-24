# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2017p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2017P6.lean
- **来源**: IMO 2017 P6
- **ArangoDB progress记录_key**: 329243（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2017P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：称(x,y)∈ℤ×ℤ为本原点如果gcd(x,y)=1。设S是有限个本原点的集合。证明存在n>0和整数a₀,a₁,...,aₙ使得 a₀xⁿ+a₁xⁿ⁻¹y+...+aₙyⁿ=1 对每个(x,y)∈S成立。
- 解答核心思路（1-2句话）：构造一个齐次多项式（HForm），通过CRT构造一个在各代表元处非零且与类间行列式互素的g，再用Euler定理和修正形式使最终形式F=g^K-Σ修正形式在每个代表元处取值1，偶次对称性处理对径点。
- 解答关键步骤列表：
  1. 对径类归约：将S中的点按{s,-s}分组，选代表元集合T
  2. 构造局部形式Gform(p)：p=2时用x²+xy+y²，奇素数p时用x^(p-1)+y^(p-1)，这些在本原点处mod p非零
  3. CRT构造g：用中国剩余定理组合各局部形式的幂，使g在T中每点非零且与行列式乘积D互素；用平移避免零值
  4. Bézout线性形式：Lf(t)=gcdA(t₁,t₂)x+gcdB(t₁,t₂)y在t处取值1
  5. 消没形式：ell(t)=t₂x-t₁y在t处为零但在其他代表元处非零
  6. Euler定理：v(t)=g(t)与Δ(t)=∏ell(t')(t)^E互素，故Δ(t)|v(t)^K-1（K=|T|·∏totient）
  7. 修正形式：hform(t)=c(t)·Lf(t)^m·P(t)，P(t)是其他类ell的幂的乘积，在t以外消没
  8. 最终形式：F=g^K-Σhform(t)，在每点取值v^K-(v^K-1)=1；偶次对称性处理-s

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
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的数学结构：我们在寻找什么类型的数学对象？这些对象需要满足什么约束？点的本原性条件意味着什么？ | 我们要找一个正次数的齐次多项式F(x,y)∈ℤ[x,y]，使其在S中每个本原点处取值1。本原性gcd(x,y)=1意味着Bézout恒等式可用：存在整数a,b使ax+by=1。齐次性是关键约束——多项式每一项次数相同。 |
| 2 | 自由列举 | 0.6 | 列出所有可能构造这样一个齐次多项式的方法方向。考虑：插值、数论工具、代数几何、格论方法等。 | 可能方向：(1)直接系数插值——但齐次约束使自由度有限；(2)利用Bézout线性形式ax+by=1在单点处取值1；(3)乘积形式——线性形式的乘积在多点处取值0或1；(4)数论工具如CRT、Euler定理；(5)对径对称性——偶次齐次式在(x,y)和(-x,-y)处取值相同。 |
| 3 | 小尝试 | 0.4 | 试试最直接的方法：对单个本原点(x₀,y₀)，用Bézout构造线性形式Lf=ax+by使其在(x₀,y₀)处取值1。能否简单地把多个点的线性形式乘起来推广到多点？ | 单点：由gcd(x₀,y₀)=1，Bézout给出a,b使ax₀+by₀=1，Lf=ax+by是次数1的齐次式。但多点乘积：∏Lfᵢ在点tⱼ处取值为∏(aᵢxⱼ+bᵢyⱼ)，不是1而是各点Bézout值的乘积。而且次数会增长为|S|，无法控制取值恰好为1。直接乘积不行。 |
| 4 | 思维操作引导 | 0.7 | 考虑将S中的点按对径类{s,-s}分组，选代表元集合T。为什么偶次齐次式可以同时处理s和-s？这个归约如何简化问题？ | 偶次齐次式F满足F(-x,-y)=F(x,y)（因为(-1)^n=1当n偶）。所以只需在代表元集合T上构造F取值1，对径点-s自动满足。这把问题从|S|个点归约到|T|≤|S|/2个代表元，且只需考虑偶次形式。 |
| 5 | 思维操作引导 | 0.5 | 现在需要在T的每个代表元处构造一个非零且与所有类间行列式互素的齐次式g。关键工具：对每个素数p|D（D=行列式乘积），局部形式Gform(p)在本原点处mod p非零（p=2用x²+xy+y²，奇p用x^(p-1)+y^(p-1)）。如何用CRT组合这些局部形式？ | 设D的所有素因子为Ps。对每个p∈Ps，Gform(p)在本原点处mod p非零（由Fermat小定理/直接验证）。取E=2∏(p-1)为偶数，使每个Gform(p)的次数整除E。将Gform(p)^(E/deg)提升到次数E，再用CRT权重uₚ·Mₚ组合（Mₚ=∏_{q≠p}q，uₚ由Bézout给出uₚMₚ≡1 mod p）。最后加一个平移项M·t₀·(x^E+y^E)避免零值，得到g。 |
| 6 | 推进 | 0.6 | 有了g之后，v(t)=g(t)与Δ(t)=∏_{t'≠t}(ell(t')(t))^E互素（因为g与D互素）。如何用Euler定理得到v(t)^K≡1 mod Δ(t)？如何构造在t以外消没的修正形式？ | 由互素性，Euler定理给出v(t)^φ(|Δ(t)|)≡1 mod |Δ(t)|。取K=|T|·∏φ(|Δ(t)|)使φ(|Δ(t)|)|K，则v(t)^K≡1 mod Δ(t)。修正形式hform(t)=c(t)·Lf(t)^m·P(t)，其中c(t)=(v(t)^K-1)/Δ(t)，P(t)=∏_{t'≠t}ell(t')^E在t处取值Δ(t)，在其他代表元t''处消没（因为ell(t)(t'')=t₂t''₁-t₁t''₂≠0但ell(t'')(t'')=0使P(t'')含零因子）。 |
| 7 | 能量传递引导 | 0.3 | 现在组装最终形式F=g^K-Σ_{t∈T}hform(t)。验证：在代表元t处F取值是多少？在对径点-s处呢？ | 在t处：g^K=v(t)^K，Σhform只hform(t)非零=c(t)·1^m·Δ(t)=v(t)^K-1，故F=v(t)^K-(v(t)^K-1)=1。在-s处：F(-t₁,-t₂)=F(t₁,t₂)（偶次）=1。故F在S中每点取值1。F的次数n=K·E>0，系数为整数。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- problem_type: structural_existence（存在性构造：证明存在齐次多项式在有限本原点集上取值1）
- structure_features: 有限本原点集合S，齐次多项式约束（所有项同次），多点取值恰好为1的约束，对径对称性{s,-s}归约，局部-全局CRT构造，消没形式修正
- key_objects: 本原点(gcd(x,y)=1的整数对)，齐次多项式HForm，对径类代表元集合T，类间行列式乘积D，局部形式Gform(p)，CRT组合g，消没线性形式ell(t)=t₂x-t₁y，Bézout线性形式Lf(t)，Euler定理指数K，修正形式hform(t)，最终形式F=g^K-Σhform(t)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["对径对称性归约——利用偶次齐次式在对径点处取值相同，将|S|个点归约到|T|≤|S|/2个代表元", "局部-全局构造——对每个素因子p构造局部形式Gform(p)使其mod p非零，再用CRT组合为全局形式g", "消没-修正模式——用消没形式ell(t')在t处为零、在t'处非零的性质，构造只在一点非零的修正形式", "数论工具应用——Bézout恒等式构造取值1的线性形式，Euler定理保证g^K≡1 mod Δ(t)", "平移避零——在CRT组合后加平移项避免g在代表元处取零值"]
- primary_pattern: 局部-全局构造（local-global construction via CRT）
- knowledge_required: ["Bézout恒等式（本原点处存在线性形式取值1）", "中国剩余定理（CRT组合局部形式）", "Euler定理/Fermat小定理（g^K≡1 mod Δ(t)）", "齐次多项式的基本性质（乘法、幂、偶次对称性）", "本原点与互素性", "素数分解与素因子", "行列式与共线性的关系"]
- key_insight: 用CRT构造一个在各代表元处非零且与所有类间行列式互素的g，再用Euler定理使g^K≡1 mod Δ(t)，最后用消没形式ell的幂乘积构造修正项，使F=g^K-Σ修正形式在每个代表元处恰好取值1

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 数论局部方法（模p非零性、CRT、Euler定理）+ 单点Bézout线性形式
- translation_to: 齐次多项式的全局显式构造（在有限点集上取值1）
- translation_type: method_translation（将数论局部工具翻译为代数构造的全局对象）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["齐次多项式", "本原点", "对径归约", "CRT局部形式", "Euler定理", "消没形式", "Bézout线性形式", "行列式互素", "平移避零"]
- expected_ai_method: bare AI预期会尝试直接插值或简单乘积线性形式——不知道如何处理齐次约束下多点取值恰好为1的问题，也不知道对径归约和CRT局部-全局构造
- correct_method: 对径类归约选代表元T → CRT构造与D互素的全局形式g → Euler定理使g^K≡1 mod Δ(t) → 消没形式ell的幂乘积构造修正项 → F=g^K-Σ修正形式在每点取值1

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
- [x] 当前拓扑分类是否够用——这道题的problem_type(structural_existence)/ai_method_type(direct_calculation)/gap_type(structural_transformation)能归入已有的拓扑类别
- [x] 粒度是否一致——structural_existence是抽象级，direct_calculation是抽象级，structural_transformation是中等级，粒度与已有值一致
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，当前拓扑分类够用

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
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中的tell_hint_pairs字段（7轮，每轮含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）。
全局pairs详见profile.json中的global_tell_hint_pairs字段（1个path_feature型+1个implicit型，含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接插值或简单乘积线性形式，无法处理齐次约束下多点取值恰好为1的问题。具体错误：(1)不知道对径归约简化问题；(2)不知道用CRT构造与行列式互素的全局形式g；(3)不知道用Euler定理使g^K≡1 mod Δ(t)；(4)不知道用消没形式ell构造只在一点非零的修正项。大概率卡在"如何让多项式在多点同时取值1"这一步。
- suitable_for_poc: ["hint_injection", "tell_identification", "knowledge_bottleneck_detection"]
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

**将完整JSON写入工作目录的 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329243"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2017p6"
   - extracted_by改为"subagent"

**示例代码**：
```python
from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

# 读取profile.json
with open('profile.json', 'r') as f:
    profile = json.load(f)

# 写入problem_profiles
db.collection('problem_profiles').insert(profile, overwrite=True)

# 更新problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '329243',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2017p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2017p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2017p6
- solution_method_type: constructive_existence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，当前拓扑分类够用（structural_existence / direct_calculation / structural_transformation均可归入已有值）
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
