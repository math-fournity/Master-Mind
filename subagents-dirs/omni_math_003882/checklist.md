# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003882
- **文件路径**: subagents-dirs/omni_math_003882/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333761（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003882/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有正整数n，使得存在整数m满足 2^n - 1 | m² + 9。
- 解答核心思路（1-2句话）：将整除条件翻译为二次剩余条件（-9是2^n-1的二次剩余），然后分两个方向证明：n=2^k时用Fermat数分解+CRT证明-9是QR；n有奇因子时用2^q-1≡3(mod 4)推出存在素因子p≡3(mod 4)使-9非QR。
- 解答关键步骤列表：
  1. 小值验证：n=1平凡成立，n=2成立(m=0)，n=3不成立(7∤m²+9)，n=4成立。猜想n=2^k。
  2. 正向(n=2^k)：分解2^{2^k}-1 = F_0·F_1·...·F_{k-1}（Fermat数，两两互素）。对每个F_i证明-9是QR：F_0=3时-9≡0；F_i(i≥1)时F_i≡1(mod 4)故(-1/F_i)=1，且9=3²恒为QR。由CRT得m存在。
  3. 反向(n有奇因子)：设n=2^k·q，q为奇数>1，则2^q-1 | 2^n-1。对q≥3奇数，2^q-1≡3(mod 4)，故至少有一个素因子p≡3(mod 4)。此时(-9/p)=(-1/p)·(9/p)=-1·1=-1，-9非QR mod p，故非QR mod 2^n-1，m不存在。
  4. 结论：n = 2^k (k≥0)。

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
| 1 | 纯元认知观察 | 0.7 | 描述这道题的结构：我们在求什么？已知条件和未知量之间有什么关系？ | 求所有正整数n使存在m满足2^n-1整除m²+9。本质是：对哪些n，-9是2^n-1的二次剩余。这是一个characterization问题，需要双向证明。 |
| 2 | 自由列举 | 0.5 | 面对这个整除条件，你能想到哪些可能的攻击方向？ | ①试小值找规律；②分解2^n-1的结构；③用二次剩余/Legendre符号；④用CRT；⑤考虑2^n-1的素因子结构；⑥考虑n的奇偶性对2^n-1的影响。 |
| 3 | 小尝试 | 0.2 | 试几个小的n值，看看哪些成立哪些不成立，尝试发现规律。 | n=1平凡成立。n=2成立(m=0)。n=3: 2^3-1=7, 需m²≡5(mod 7), QR mod 7为{0,1,2,4}, 5不是QR, 不成立。n=4: 2^4-1=15=3×5, m=6时45=3×15成立。猜想：n=2^k。 |
| 4 | 思维操作引导 | 0.4 | 你猜想n=2^k。现在证明正向：当n=2^k时m存在。提示——考虑2^{2^k}-1的因式分解结构。 | 2^{2^k}-1=F_0·F_1·...·F_{k-1}（Fermat数），两两互素。F_0=3: -9≡0平凡。F_i(i≥1): F_i≡1(mod 4)故(-1/F_i)=1, 9=3²恒QR, 所以(-9/F_i)=1。由CRT得m存在。 |
| 5 | 推进 | 0.5 | 正向已证。现在推进反向：若n不是2的幂，证明m不存在。提示——n有奇因子q时，2^q-1整除2^n-1。 | 设n=2^k·q, q奇>1, 则2^q-1|2^n-1。q≥3奇数时2^q-1≡3(mod 4), 故有素因子p≡3(mod 4)。(-9/p)=(-1/p)·(9/p)=-1·1=-1, -9非QR mod p, 非QR mod 2^q-1, m不存在。 |
| 6 | 思维操作引导 | 0.3 | 验证关键步骤：为什么2^q-1≡3(mod 4)能推出存在素因子p≡3(mod 4)？ | 反证法：若所有素因子≡1(mod 4), 乘积≡1(mod 4)。但2^q-1≡3(mod 4)（q≥3, 2^q≡0 mod 4）, 矛盾。故至少有一个素因子p≡3(mod 4)。 |
| 7 | 能量传递引导 | 0.8 | 将两个方向合起来，完整陈述证明。 | 正向：n=2^k时Fermat数分解+CRT证明m存在。反向：n有奇因子q>1时2^q-1≡3(mod 4)推出存在p≡3(mod 4), -9非QR, m不存在。结论：n=2^k (k≥0)。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4 (R1+R2+R5+R7)
- knowledge_rounds（思维操作引导的轮数）: 2 (R4+R6)
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- problem_type: characterization
- structure_features: 整除条件转化为二次剩余条件，需要双向证明（存在性+非存在性），涉及2^n-1的因式分解结构（Fermat数）和mod 4奇偶论证
- key_objects: ["2^n-1 (Mersenne型数)", "m²+9 (二次型)", "Fermat数 F_i=2^{2^i}+1", "二次剩余/Legendre符号", "CRT", "mod 4素因子分布"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["pattern_recognition (小值归纳)", "bidirectional_proof (正向存在+反向非存在)", "factorization (Fermat数分解)", "quadratic_residue_analysis (Legendre符号)", "parity_argument (mod 4奇偶论证)"]
- primary_pattern: bidirectional_proof_with_quadratic_residue
- knowledge_required: ["二次剩余与Legendre符号", "Fermat数及其互素性质", "中国剩余定理(CRT)", "2^n-1的因式分解", "素因子mod 4分布的性质"]
- key_insight: 将整除条件翻译为二次剩余条件后，关键转折是发现2^q-1≡3(mod 4)（q≥3奇数）强制存在素因子p≡3(mod 4)，在此p上-1是非剩余从而使-9成为非剩余

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 整除条件（2^n-1 | m²+9）
- translation_to: 二次剩余条件（-9是2^n-1的二次剩余），进一步分解为对每个素因子的Legendre符号计算
- translation_type: method_translation（从整除语言翻译到二次剩余语言，再翻译到素因子mod 4分布分析）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["quadratic residue", "Fermat numbers", "Chinese Remainder Theorem", "Legendre symbol", "mod 4 parity argument", "factorization of 2^n-1"]
- expected_ai_method: 试小值找规律，猜想n=2^k，但无法完成证明——缺乏将整除条件翻译为二次剩余条件的思维操作，也不熟悉Fermat数分解
- correct_method: 二次剩余分析：正向用Fermat数分解+CRT证明-9是QR，反向用2^q-1≡3(mod 4)推出存在p≡3(mod 4)使-9非QR

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(characterization)/ai_method_type(enumeration_brute_force)/gap_type(method_translation)都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——标注值与已有值粒度统一，characterization和enumeration_brute_force都是抽象级，method_translation是中等级。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无进化建议。

**拓扑进化建议**（如有）：无。已有拓扑分类足以覆盖此题。

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
- bare_ai_error_prediction: bare AI可能通过试小值猜出n=2^k，但无法完成证明。正向缺乏Fermat数分解的知识，反向缺乏将整除翻译为二次剩余再翻译为mod 4素因子分布的思维操作。很可能停留在"猜想但无法证明"阶段。
- suitable_for_poc: ["POC-VMS-8 (hint端验证：脉络继承+方向注入)", "POC-VMS-9/10 (tell端验证：去特化+形式化过滤)"]
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

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="333761"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003882"
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
    '_key': '333761',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003882',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003882')
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
- problem_id: omni_math_003882
- solution_method_type: quadratic_residue_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类(characterization/enumeration_brute_force/method_translation)足够覆盖
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
