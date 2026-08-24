# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1993p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1993P6.lean
- **来源**: IMO 1993 P6
- **ArangoDB progress记录_key**: 329146（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1993P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：圆周上n>1盏灯L₀,...,L_{n-1}，初始全亮。步骤s_i：若L_{i-1}亮则切换L_i，否则不动。证明：(a)存在M(n)>0使M(n)步后全亮；(b)n=2^k时M(n)=n²-1；(c)n=2^k+1时M(n)=n²-n+1。
- 解答核心思路（1-2句话）：将Boolean切换过程翻译为ZMod 2算术模型，定义轮映射L，用加强归纳（四个同时不变量A/B/C/D）和拼接/倍增结构对k归纳，再分析最终阶段得到精确公式。
- 解答关键步骤列表：
  1. step映射在有限状态空间上单射→双射→有限阶→周期性（part a）
  2. Boolean切换翻译为ZMod 2加法（toggle = add predecessor mod 2）
  3. 定义轮映射L：一轮n步后L(x)(p) = x(last) + Σ_{i≤p} x(i) in ZMod 2
  4. 拼接结构cat：L在2n灯上通过cat分解为n灯上的L
  5. 加强归纳：A(n)∧B(n)∧C(n)∧D(n) → A(2n)∧B(2n)∧C(2n)∧D(2n)，对k归纳
  6. n=2^k：n-1轮后L^{n-1}(全1)=eFn（仅末灯亮）→n(n-1)步后仅末灯亮
  7. 最终阶段：仅一灯亮时逐个点亮→n²-1步（case b）
  8. n=2^k+1：移位状态对应cStateVec→n-2轮后仅灯1亮→n(n-2)步后仅灯1亮
  9. 最终阶段：2空步+(n-1)点亮步→n²-n+1步（case c）

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
| 1 | 纯元认知观察 | 0.3 | 描述问题结构：状态空间是什么，step映射如何作用，要证什么？ | 状态空间(Fin n→Bool)×Fin n，step推进位置并条件切换，证周期性和精确公式 |
| 2 | 自由列举 | 0.5 | 列出所有可能的分析方法 | 前向模拟、逆向分析、代数建模、对特殊n归纳、置换分析、轮级抽象 |
| 3 | 小尝试 | 0.2 | 模拟n=2,3,4,5,8,9，观察周期和中间状态 | n=2^k: 周期n²-1，n(n-1)步后仅末灯亮；n=2^k+1: 周期n²-n+1，n(n-2)步后仅灯1亮 |
| 4 | 思维操作引导 | 0.7 | 将Boolean切换翻译为ZMod 2算术，step映射变成什么？ | toggle = XOR = mod 2加法，zstep线性化，L成为线性算子 |
| 5 | 思维操作引导 | 0.7 | 定义轮映射L，L(x)(p)的显式公式和关键性质？ | L(x)(p)=x(last)+Σ_{i≤p}x(i) in ZMod 2，L线性，m轮后状态=(L^m(初始),0) |
| 6 | 推进 | 0.8 | 对n=2^k设k归纳，L在2n灯上如何通过拼接分解，需要哪些不变量？ | catL公式分解，需要A/B/C/D四个同时不变量，证明A∧B∧C∧D for 2n from n |
| 7 | 推进 | 0.4 | 仅一灯亮后的最终阶段如何分析，需要多少步？ | case b: 逐个点亮n-1步→n²-1；case c: 2空步+(n-1)点亮→n²-n+1 |
| 8 | 能量传递引导 | 0.6 | 组合所有部分完成完整证明 | (a)单射→周期；(b)归纳+最终阶段=n²-1；(c)移位对应+最终阶段=n²-n+1 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 6

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
- structure_features: 圆周上n个Boolean灯的条件切换过程，位置模n推进，有限状态空间2^n×n
- key_objects: ["circular lamp array", "step map", "ZMod 2 model (zstep)", "round map L", "concatenation cat", "strengthened induction predicates A/B/C/D", "shifted state cStateVec"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["finite_state_periodicity（有限状态空间单射→双射→周期性）", "algebraic_translation（Boolean切换翻译为ZMod 2算术）", "round_abstraction（n步抽象为单轮映射L）", "strengthened_induction（四不变量A/B/C/D同时归纳）", "concatenation_decomposition（2n灯通过cat分解为n灯问题）", "final_phase_analysis（仅一灯亮后的逐个点亮阶段）", "shifted_state_correspondence（n=2^k+1映射到n=2^k的移位状态）"]
- primary_pattern: strengthened_induction（加强归纳——不证单一性质而证四个同时不变量，使n→2n归纳步可通过）
- knowledge_required: ["有限集上单射映射→双射→有限阶（置换群基础）", "ZMod 2算术（XOR=mod 2加法）", "线性映射迭代与前缀和", "数学归纳法（加强归纳形式）", "拼接分解结构"]
- key_insight: 将Boolean切换过程翻译为ZMod 2线性算子使轮映射L线性化，然后用四个同时不变量A/B/C/D加强归纳假设——不是证一个性质而是证四个同时成立，使得n→2n的归纳步骤可以通过catL公式分解。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: Boolean条件切换过程（if-then-toggle语义，逐步模拟）
- translation_to: ZMod 2线性算子迭代（toggle=XOR=mod 2加法，轮映射L为线性算子，L^m迭代）
- translation_type: method_translation（方法翻译——从组合/过程模拟翻译为代数/线性算子迭代）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["ZMod 2 linearization", "round map L", "strengthened induction A/B/C/D", "concatenation cat decomposition", "shifted state cStateVec", "final phase one-by-one lighting"]
- expected_ai_method: 逐步前向模拟Boolean切换过程，尝试直接计算周期，或对小的n枚举观察规律后猜测公式但无法证明
- correct_method: 将Boolean切换翻译为ZMod 2线性算子，定义轮映射L，用四不变量加强归纳对k归纳，再分析最终阶段

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial、ai_method_type=enumeration_brute_force、gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足以区分这道题的tell和已有tell
- [ ] 无需进化建议

**拓扑进化建议**（如有）：无。当前拓扑分类体系足够覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

### 局部tell_hint_pairs

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对圆周灯阵条件切换问题，状态空间2^n×n，不确定从何入手 | 先描述问题结构：状态空间是什么，step映射如何作用，要证什么 | 0.3 | 纯元认知观察 | false | {discrete_combinatorial, enumeration_brute_force, method_problem_mismatch} | ["state space 2^n×n", "step map", "circular condition"] |
| 2 | AI理解了问题结构但困在组合视角，未想到代数化 | 列出所有可能的分析方法：前向模拟、逆向分析、代数建模、归纳、置换分析、轮级抽象 | 0.5 | 自由列举 | false | {discrete_combinatorial, enumeration_brute_force, search_space_estimation} | ["forward simulation", "algebraic modeling", "round-level abstraction"] |
| 3 | AI开始模拟小例子但未发现ZMod 2结构 | 模拟n=2,3,4,5,8,9，观察周期和中间状态模式 | 0.2 | 小尝试 | false | {discrete_combinatorial, enumeration_brute_force, search_space_estimation} | ["small case simulation", "period observation", "intermediate state pattern"] |
| 4 | AI观察到2^k和2^k+1的规律但无法证明，困在Boolean语义 | 将Boolean切换翻译为ZMod 2算术，toggle=XOR=mod 2加法，step映射变成什么？ | 0.7 | 思维操作引导 | true | {discrete_combinatorial, direct_calculation, knowledge_gap} | ["ZMod 2 linearization", "toggle as XOR", "mod 2 addition"] |
| 5 | AI已将切换线性化但未抽象到轮级别 | 定义轮映射L，L(x)(p)的显式公式和关键性质？ | 0.7 | 思维操作引导 | true | {discrete_combinatorial, algebraic_identity, knowledge_gap} | ["round map L", "prefix sum formula", "linear operator iteration"] |
| 6 | AI有轮映射L但不知道如何对2^k归纳，直接归纳A(n)不够 | 对n=2^k设k归纳，L在2n灯上如何通过拼接分解，需要哪些不变量？ | 0.8 | 推进 | false | {discrete_combinatorial, logical_deduction, structural_transformation} | ["concatenation cat", "catL decomposition", "strengthened induction A/B/C/D"] |
| 7 | AI完成归纳但未分析仅一灯亮后的最终阶段 | 仅一灯亮后的最终阶段如何分析，需要多少步？ | 0.4 | 推进 | false | {discrete_combinatorial, direct_calculation, method_problem_mismatch} | ["final phase", "one-by-one lighting", "idle steps"] |
| 8 | AI有所有部件但未组装成完整证明 | 组合所有部分完成完整证明 | 0.6 | 能量传递引导 | false | {discrete_combinatorial, logical_deduction, method_translation} | ["assembly", "periodicity + induction + final phase"] |

### 全局tell_hint_pairs

**Pair 1 (path_feature)**:
- scope_type: path_feature
- scope: 从R4到R6的完整翻译+归纳路径
- observation_point: null
- tell: AI在组合视角中无法看到Boolean切换过程可以翻译为ZMod 2线性算子迭代，进而通过轮映射L和拼接分解实现加强归纳
- hint: 关键路径是：Boolean→ZMod 2线性化→轮映射L→cat拼接分解→四不变量加强归纳。这条路径的每一步都依赖前一步的翻译，不能跳过中间步骤
- hint_level: 0.8
- generalizability: high——"将组合过程翻译为代数算子迭代+加强归纳"是一个高度泛化的方法论，适用于许多离散动力系统问题
- why_not_visible_locally: 在R4只看到ZMod 2翻译，在R5只看到轮映射L，在R6只看到拼接分解——每一步都是局部翻译操作，但"从组合到代数再到加强归纳"的完整路径特征只有在看到全部步骤后才能识别。局部视角下AI不知道ZMod 2翻译是为了后续的线性算子迭代，线性化是为了轮映射L可分解，L可分解是为了加强归纳——这些因果关系是路径级特征
- tell_topology: {discrete_combinatorial, enumeration_brute_force, method_translation}
- tell_small_concepts: ["ZMod 2 linearization", "round map L", "concatenation decomposition", "strengthened induction"]

**Pair 2 (path_feature)**:
- scope_type: path_feature
- scope: 从R3到R7的最终阶段分析路径
- observation_point: null
- tell: AI在模拟小例子时观察到n(n-1)步后仅一灯亮（2^k）或n(n-2)步后仅灯1亮（2^k+1），但不知道这个中间状态是通向精确公式的关键跳板——最终阶段（逐个点亮）的分析决定了精确步数
- hint: 精确公式n²-1和n²-n+1不是直接从归纳得到的，而是"归纳到达仅一灯亮的中间状态"+"最终阶段逐个点亮的步数分析"两部分拼接的结果。必须先识别中间状态，再分析从中间状态到全亮的最终阶段
- hint_level: 0.6
- generalizability: medium——"识别关键中间状态+分析最终阶段"的模式在周期性问题中常见，但具体中间状态因题而异
- why_not_visible_locally: 在R3模拟小例子时，AI看到的是周期性数字，不知道n(n-1)步后的中间状态是关键跳板。在R6归纳中，AI关注的是A/B/C/D不变量，不直接看到最终阶段。只有将"归纳到达的中间状态"和"最终阶段步数"两部分拼接，才能看到精确公式的完整结构——这是路径级特征，局部步骤中不可见
- tell_topology: {discrete_combinatorial, direct_calculation, structural_transformation}
- tell_small_concepts: ["intermediate state eFn", "final phase lighting", "precise step count formula"]

**Pair 3 (implicit)**:
- scope_type: implicit
- scope: R6中catL公式的结构蕴含
- observation_point: 6
- tell: catL公式L(cat y z) = cat(L y + (y_last+z_last), L z + tot y)中蕴含着"2n灯的L可以分解为两个n灯的L的组合"——这个分解结构是整个加强归纳的技术基础，但AI在看到catL公式时可能只把它当作一个计算结果而非结构性洞察
- hint: catL公式不只是计算工具——它说明2n灯的轮映射可以完全用n灯的轮映射和tot/last值表达。这意味着如果n灯的L有好的性质（A/B/C/D），2n灯的L也继承这些性质。这是"从n到2n"归纳步的本质机制
- hint_level: 0.7
- generalizability: medium——"分解结构蕴含归纳可推进性"的模式在代数归纳中常见，但catL的具体形式因问题而异
- why_not_visible_locally: 在R6的局部视角中，AI看到catL公式作为一个代数等式，关注的是如何用它计算。但catL公式蕴含的"分解→归纳可推进"的结构性洞察不在公式表面——需要理解为什么tot y=0（B不变量）和last值=1（C不变量）使公式简化，才能看到分解结构如何传递不变量。这个蕴含关系在局部步骤中不可见
- tell_topology: {discrete_combinatorial, algebraic_identity, structural_transformation}
- tell_small_concepts: ["catL decomposition formula", "total parity tot", "last lamp value", "invariant propagation"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会困在组合/过程模拟视角，能模拟小例子并猜到n²-1和n²-n+1的公式，但无法证明。关键障碍：(1)不会想到将Boolean切换翻译为ZMod 2线性算子；(2)即使想到代数化，也不会发现需要四个同时不变量A/B/C/D来加强归纳；(3)不会发现cat拼接分解结构；(4)不会分析仅一灯亮后的最终阶段
- suitable_for_poc: ["POC-VMS-hint-injection（hint端验证：注入翻译方向后AI能否走通）", "POC-VMS-tell-detection（tell端验证：从AI thinking中检测到组合视角困局）", "POC-VMS-strengthened-induction（加强归纳模式识别：AI能否从'直接归纳不够'信号中推出需要加强）"]
- discriminates_levels: true——这道题区分度极高：bare AI几乎不可能走通（需要三重翻译+加强归纳+最终阶段分析），有hint的AI可能走通关键步骤

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [ ] _key（=problem_id）
- [ ] source_id
- [ ] source_dataset
- [ ] schema_version（=3）
- [ ] problem_text
- [ ] solution_text
- [ ] solution_summary
- [ ] domain
- [ ] subfield
- [ ] answer_type
- [ ] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
- [ ] problem_type
- [ ] solution_method_type
- [ ] structure_features
- [ ] key_objects
- [ ] thinking_patterns
- [ ] primary_pattern
- [ ] knowledge_required
- [ ] key_insight
- [ ] translation_from
- [ ] translation_to
- [ ] translation_type
- [ ] tell_topology（profile级）
- [ ] tell_small_concepts（profile级）
- [ ] expected_ai_method
- [ ] correct_method
- [ ] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [ ] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [ ] bare_ai_expected
- [ ] bare_ai_error_prediction
- [ ] suitable_for_poc
- [ ] discriminates_levels
- [ ] qa_sequence（含rounds数组和stats子对象）
- [ ] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329146"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1993p6"
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
    '_key': '329146',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1993p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1993p6')
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
- problem_id: compfiles_imo1993p6
- solution_method_type: strengthened_induction
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3（path_feature型2个，implicit型1个）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否——当前拓扑分类体系（problem_type/ai_method_type/gap_type三维度）足够覆盖本题
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
