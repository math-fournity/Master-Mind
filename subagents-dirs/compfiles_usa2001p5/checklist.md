# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2001p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2001P5.lean
- **来源**: USA 2001 P5
- **ArangoDB progress记录_key**: 329405（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2001P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let S be a set of integers (not necessarily positive) such that (a) there exist a, b ∈ S with gcd(a, b) = gcd(a − 2, b − 2) = 1; (b) if x and y are elements of S (possibly equal), then x² − y also belongs to S. Prove that S is the set of all integers.
- 解答核心思路（1-2句话）：定义"shifty"整数（平移不变性），证明从闭包性质可导出特定的shifty整数，这些整数的gcd为1，由Bézout恒等式得1是shifty的，从而S=ℤ。
- 解答关键步骤列表：
  1. 定义Shifty(S, d)：∀x, x∈S ↔ x+d∈S，证明shifty整数构成ℤ的子群
  2. 核心引理：若u,v∈S，则v²-u²是shifty的（对闭包性质使用两次：u²-x∈S，再v²-(u²-x)=x+(v²-u²)∈S）
  3. 从a,b∈S导出三个shifty整数：a²-b², a³(a-2), b³(b-2)
  4. 数论核心：证明这三个数的gcd为1（用gcd(a,b)=1和gcd(a-2,b-2)=1，对素数p做情况分析）
  5. 由Bézout恒等式（三个数gcd=1），1是这三个shifty整数的整系数线性组合，故1是shifty的
  6. 因为1是shifty的且a∈S，任意整数x = a+(x-a)∈S，故S=ℤ

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
| 1 | 纯元认知观察 | 0.9 | 观察这道题的结构：S是一个整数集合，有两条性质——(a)存在a,b∈S使gcd(a,b)=gcd(a-2,b-2)=1；(b)若x,y∈S则x²-y∈S。需要证明S=ℤ。请描述：闭包性质(b)给出了什么结构？gcd条件(a)的作用可能是什么？ | 闭包性质(b)说S在运算x²-y下封闭，这是一个二次运算。从a,b∈S出发可以生成a²-b, b²-a, a²-a, b²-b等新元素。gcd条件(a)可能用于保证某种"密度"或"覆盖性"——如果生成的元素有公共因子，可能无法覆盖所有整数。目标是证明S=ℤ，需要某种方式证明1或所有整数都在S中。 |
| 2 | 自由列举 | 0.8 | 列出所有可能证明S=ℤ的方向：你可以考虑直接构造、归纳、证明S包含某个生成集、利用ℤ的子群结构、或其他方法。 | 方向列举：(1)直接构造——从a,b出发反复用闭包生成具体整数，试图得到1；(2)归纳法——证明若n∈S则n+1∈S；(3)证明S是ℤ的子群（加法封闭），然后用gcd条件；(4)证明某个固定整数d的倍数都在S中，然后d=1；(5)利用闭包性质导出S在某种变换下不变，再结合数论条件。 |
| 3 | 小尝试 | 0.3 | 试试方向(1)：从a,b∈S出发，用闭包性质能生成哪些元素？能否直接得到1∈S？ | 从a,b∈S：a²-b∈S, b²-a∈S, a²-a∈S, b²-b∈S。继续：(a²-b)²-a∈S, (a²-a)²-a²=a³(a-2)∈S... 生成的值越来越大（二次增长），很难直接控制得到1。直接构造似乎陷入指数增长的值树中，无法系统性地覆盖所有整数。 |
| 4 | 思维操作引导 | 0.5 | 换一个角度：不要问"哪些整数在S中"，而问"什么平移保持S不变"。定义：d是S的"shifty"整数，如果∀x, x∈S↔x+d∈S。证明shifty整数构成ℤ的加法子群。 | Shifty整数的定义：d是shifty的当且仅当平移d保持S的成员关系不变。0是shifty的（平凡）。若d是shifty的，则-d也是（反向平移）。若d,e都是shifty的，则d+e也是（先平移d再平移e）。因此shifty整数构成ℤ的子群，即所有shifty整数是某个固定整数g的倍数。如果能证明g=1，则S=ℤ。 |
| 5 | 推进 | 0.4 | 现在关键问题：如何从闭包性质导出shifty整数？若u,v∈S，证明v²-u²是shifty的。 | 对任意x∈S：由闭包性质，u²-x∈S（因为u,x∈S）。再由闭包性质，v²-(u²-x)∈S（因为v,u²-x∈S）。计算v²-(u²-x)=x+(v²-u²)。所以x∈S→x+(v²-u²)∈S。反向同理：若x+(v²-u²)∈S，则v²-(x+(v²-u²))=u²-x∈S，再u²-(u²-x)=x∈S。故v²-u²是shifty的。 |
| 6 | 思维操作引导 | 0.3 | 从a,b∈S导出三个shifty整数：a²-b², a³(a-2), b³(b-2)。然后利用gcd(a,b)=1和gcd(a-2,b-2)=1，证明这三个数的gcd为1。（提示：对任意素数p，分析p整除这三个数的情况） | 三个shifty整数：a²-b²（直接由a,b∈S），a³(a-2)（由a²-a∈S，再(a²-a)²-a²=a³(a-2)），b³(b-2)（同理）。证明gcd=1：假设素数p整除所有三个数。p|a³(a-2)→p|a或p|(a-2)；p|b³(b-2)→p|b或p|(b-2)；p|a²-b²→p|(a-b)或p|(a+b)。分四种情况：p|a且p|b→与gcd(a,b)=1矛盾；p|a且p|(b-2)→由p|(a-b)或p|(a+b)推出p|b或p|b，矛盾；类似p|(a-2)且p|b也矛盾；p|(a-2)且p|(b-2)→与gcd(a-2,b-2)=1矛盾。故gcd=1。 |
| 7 | 能量传递引导 | 0.6 | 最后一步：三个shifty整数的gcd为1，由Bézout恒等式，1是它们的整系数线性组合。shifty整数构成子群，故1是shifty的。由此推出S=ℤ。完成证明。 | 由Bézout，存在整数m,n,r使m·(a²-b²)+n·a³(a-2)+r·b³(b-2)=1。因为shifty整数构成子群，整系数线性组合仍shifty，故1是shifty的。对任意整数x，x-a是shifty的（1的倍数），所以a∈S→a+(x-a)=x∈S。因此S=ℤ。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R5,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R6）
- level_sum: 0.9+0.8+0.3+0.5+0.4+0.3+0.6=3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
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
- problem_type: structural_existence
- structure_features: 整数集合S在二次运算x²-y下封闭，附加gcd条件gcd(a,b)=gcd(a-2,b-2)=1，证明S=ℤ。核心结构是从闭包性质导出平移不变性（shifty整数），再由数论条件保证shifty整数的gcd=1，Bézout闭合。
- key_objects: ["集合S", "整数a,b", "gcd条件", "闭包运算x²-y", "shifty整数（平移不变性）", "Bézout恒等式", "ℤ的子群结构"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["shift-invariance abstraction（从成员性问题转化为不变性问题）", "algebraic closure exploitation（二次利用闭包性质导出shifty整数）", "number-theoretic gcd argument（素数情况分析证明gcd=1）", "Bézout identity application（用Bézout从gcd=1得到1是shifty的）", "subgroup structure of ℤ（shifty整数构成子群）"]
- primary_pattern: shift-invariance abstraction（从"哪些整数在S中"转化为"什么平移保持S不变"）
- knowledge_required: ["Bézout恒等式（三个整数的扩展形式）", "gcd性质与素数整除", "ℤ的子群结构（每个子群是nℤ）", "素数情况分析技巧"]
- key_insight: 不要问"哪些整数在S中"，而问"什么平移保持S不变"——定义shifty整数，证明它们构成ℤ的子群，从闭包性质导出shifty整数，用gcd条件和Bézout证明1是shifty的，从而S=ℤ。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接成员构造（从a,b出发反复用闭包生成具体整数，试图直接得到1∈S）
- translation_to: 平移不变性+子群结构（定义shifty整数，证明构成ℤ子群，用Bézout证明1是shifty的）
- translation_type: structural_transformation（从成员性问题到不变性问题的结构性转换）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["shift-invariance", "shifty integers", "Bézout identity", "gcd of three integers", "closure under quadratic operation", "subgroup of ℤ", "prime case analysis"]
- expected_ai_method: direct_calculation（bare AI预期会直接从a,b出发构造具体整数，陷入二次增长的值树）
- correct_method: shift-invariance + Bézout（定义shifty整数，从闭包导出shifty整数，用gcd条件和Bézout证明1是shifty的）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，structural_existence / direct_calculation / structural_transformation 都已有且粒度合适
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，都是抽象到中等粒度
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够，不需要新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议：无进化建议

**拓扑进化建议**（如有）：无。现有拓扑分类完全适用。

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

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接从a,b出发用闭包性质构造具体整数，陷入二次增长的值树中，无法发现shift-invariance抽象。即使想到利用ℤ的子群结构，也难以将闭包性质与shifty整数联系起来，更难以完成素数情况分析证明三个shifty整数的gcd=1。
- suitable_for_poc: ["tell_extraction_poc", "hint_injection_poc", "structural_transformation_poc"]
- discriminates_levels: true

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
2. 更新`problem_extraction_progress`集合中`_key="329405"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2001p5"
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
    '_key': '329405',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2001p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2001p5')
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
- problem_id: compfiles_usa2001p5
- solution_method_type: shift_invariance_bezout
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类完全适用（structural_existence / direct_calculation / structural_transformation等已有值粒度合适）
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
