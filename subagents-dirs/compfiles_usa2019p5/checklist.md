# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2019p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2019P5.lean
- **来源**: USA 2019 P5
- **ArangoDB progress记录_key**: 329482（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2019P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 m, n 为互质正整数。黑板上写着 m/n 和 n/m。Evan 每次可选两个数 x, y，写下它们的算术平均 (x+y)/2 或调和平均 2xy/(x+y)。问对哪些 (m, n)，Evan 能在有限步内写出 1？
- 解答核心思路（1-2句话）：Evan 能写出 1 当且仅当 m+n 是 2 的幂。正向用 dyadic 加权平均逐步逼近；反向用奇素因子不变量排除。
- 解答关键步骤列表：
  1. 正向：若 m+n=2^k，则 1 = (n·(m/n) + m·(n/m))/2^k，这是 dyadic 加权平均，可由反复取算术平均得到（writable_combo 定理）
  2. 反向：若 m+n 不是 2 的幂，则存在奇素数 p | m+n
  3. 关键不变量（Writable.exists_rep）：对每个可写数 a/b，有 p|(a+b) 且 p∤b
  4. 不变量在 base case（m/n, n/m）成立：p|(m+n)，p∤n 且 p∤m（因 gcd(m,n)=1）
  5. 算术平均保持不变量：(a/b + c/d)/2 = (ad+bc)/(2bd)，p|(ad+bc) 由 p|(a+b) 和 p|(c+d) 推出，p∤2bd 因 p 奇且 p∤b,p∤d
  6. 调和平均保持不变量：2(a/b)(c/d)/(a/b+c/d) = 2ac/(ad+bc)，用模运算证明 p|(ad+bc) 且 p∤(ad+bc)，再证 p|(2ac) 由 p|(a+b),p|(c+d) 推出
  7. 若 1 可写，则 1=a/a 满足 p|(2a) 且 p∤a，但 p 奇故 p|a，矛盾

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | 这道题的结构是什么？已知条件有哪些？目标是什么？操作（算术平均、调和平均）的本质是什么？ | 已知 m/n 和 n/m（互为倒数），操作是取两个数的算术平均或调和平均，目标是写出 1。注意 m/n · n/m = 1，两个初始数的乘积已经是 1。算术平均和调和平均都保持某种"中间性"。 |
| 2 | 自由列举 | 0.6 | 列出所有可能的分析方向：哪些 (m,n) 可能可行？你能想到什么不变量或特殊结构？ | 方向1：先试小例子 m=1,n=1 → 已有1。m=1,n=3 → 1/3 和 3，算术平均=5/3，调和平均=3/5... 能否到1？方向2：算术平均和调和平均的关系——两者互为某种对偶。方向3：寻找不变量——什么量在操作下不变？方向4：m+n 的结构——2的幂有什么特殊性？ |
| 3 | 小尝试 | 0.5 | 试 m=1, n=3 的情况。从 1/3 和 3 出发，能否写出 1？尝试几步看看有没有规律。 | 1/3 和 3：AM=(1/3+3)/2=5/3, HM=2·(1/3)·3/(1/3+3)=2/(10/3)=3/5。再取 1/3 和 5/3：AM=1, 成功！等等，(1/3+5/3)/2 = (6/3)/2 = 1。所以 m=1,n=3 可以！但 1+3=4=2^2。再试 m=1,n=5：1+5=6 不是2的幂。1/5 和 5：AM=13/5, HM=10/13... 似乎很难到1。猜想：m+n 是2的幂时可行。 |
| 4 | 思维操作引导 | 0.4 | 现在聚焦不变量方法。考虑 m+n 的素因子。如果奇素数 p 整除 m+n，对每个可写数 a/b（最简分数），p | (a+b) 这个性质是否被两个操作保持？请验证 base case 和归纳步骤。 | Base case: m/n → a=m, b=n, p|(m+n) ✓, p∤n（因 gcd(m,n)=1 且 p|m+n, 若 p|n 则 p|m, 矛盾）。AM: (a/b+c/d)/2 = (ad+bc)/(2bd)。p|(ad+bc) 因为 a≡-b, c≡-d mod p 所以 ad+bc ≡ -bd+(-bd) = -2bd ≡ 0... 等等需要 p|2bd 但 p 奇且 p∤b,p∤d 所以 p∤2bd。需要 p|(ad+bc)：a≡-b(mod p), c≡-d(mod p), 所以 ad+bc ≡ -bd-bd = -2bd ≡ 0(mod p) 需要 p|2bd... 不对。实际上 ad+bc ≡ (-b)d + b(-d) = -2bd (mod p)，所以 p|(ad+bc) 当且仅当 p|2bd，但 p∤2bd。矛盾？不对，应该看新分子 ad+bc 是否满足 p|(ad+bc+2bd)。新表示是 (ad+bc)/(2bd)，需要 p|(ad+bc+2bd)。ad+bc+2bd = (a+b)(c+d)... 不，ad+bc+2bd = d(a+b)+b(c+d)，p|(a+b) 且 p|(c+d) 所以 p|(ad+bc+2bd) ✓。且 p∤2bd ✓。 |
| 5 | 思维操作引导 | 0.4 | 调和平均的情况呢？2xy/(x+y) = 2ac/(ad+bc)。验证不变量：新分子 2ac，新分母 ad+bc。需要 p|(2ac+ad+bc) 和 p∤(ad+bc)。请推导。 | 新表示 2ac/(ad+bc)。需要 p|(2ac + ad+bc) = a(2c+d)+bc。由 c≡-d(mod p)，2c+d ≡ c(mod p)，所以 a(2c+d)+bc ≡ ac+bc = c(a+b) ≡ 0(mod p) ✓。需要 p∤(ad+bc)：ad+bc ≡ -2bd(mod p)，p∤2bd 所以 p∤(ad+bc) ✓。不变量保持！ |
| 6 | 推进 | 0.5 | 现在用不变量完成反向证明：如果 m+n 不是 2 的幂，为什么 1 不可写？ | 若 m+n 不是 2 的幂，则存在奇素数 p|m+n。由不变量，每个可写数 a/b 满足 p|(a+b) 且 p∤b。若 1=a/b 可写，则 a=b，p|2a，p 奇故 p|a，但 p∤b=a，矛盾。所以 1 不可写。正向：m+n=2^k 时，1=(n·(m/n)+m·(n/m))/2^k 是 dyadic 加权平均，可由反复取算术平均得到。 |
| 7 | 能量传递引导 | 0.8 | 整合所有部分，写出完整的充要条件证明。你已经有了正向（dyadic加权平均）和反向（奇素因子不变量），把它们合在一起。 | 充要条件：Evan 能写出 1 ⟺ m+n 是 2 的幂。正向：m+n=2^k 时，1 是 m/n 和 n/m 的 dyadic 加权平均，由 writable_combo 归纳可写。反向：m+n 非 2 的幂时有奇素因子 p，不变量 p|(a+b), p∤b 在两种操作下保持，1=a/a 违反不变量。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R6,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R5）
- level_sum: 0.7+0.6+0.5+0.4+0.4+0.5+0.8 = 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（刻画哪些 (m,n) 满足条件，是充要条件的刻画问题）
- structure_features: 给定递归生成的数集（从 m/n, n/m 出发，反复取算术平均和调和平均），刻画目标值 1 是否在集合中。核心结构是"操作闭包+不变量"——操作定义了可达集，不变量约束了可达集的边界。
- key_objects: [互质正整数 m,n, 有理数 m/n 和 n/m, 算术平均 (x+y)/2, 调和平均 2xy/(x+y), 不变量 p|(a+b) 且 p∤b, m+n 的素因子分解, dyadic 加权平均]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [不变量方法, 小例子实验归纳, 充要条件双向证明, 模运算保持性验证, dyadic加权平均构造]
- primary_pattern: 不变量方法（核心是找到在操作下保持的不变量，用它刻画可达集的边界）
- knowledge_required: [算术平均与调和平均的定义, 模运算与同余, 素因子分解, 互质性, dyadic 有理数, 归纳法]
- key_insight: 关键转折是注意到 m+n 的奇素因子 p 给出不变量 p|(a+b) 且 p∤b，这个不变量在两种操作下都保持，从而 1=a/a 违反不变量；而 m+n=2^k 时无奇素因子，不变量约束消失，1 可达。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 组合操作语言（算术平均/调和平均的递归生成过程）
- translation_to: 数论不变量语言（模 p 同余、素因子分解、整除性）
- translation_type: method_translation（从组合/操作的角度翻译为数论不变量的角度，核心翻译是将"可达性"问题转化为"不变量约束"问题）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: [不变量, 奇素因子, 模p同余, 算术平均保持性, 调和平均保持性, dyadic加权平均, 互质性, m+n的素因子分解]
- expected_ai_method: bare AI 预期会尝试枚举小例子、尝试直接计算可达数集、或尝试用代数恒等式直接构造 1，但不会想到用数论不变量来约束可达集
- correct_method: 用 m+n 的奇素因子构造不变量 p|(a+b) 且 p∤b，证明不变量在两种操作下保持，从而排除 1 的可达性；正向用 dyadic 加权平均构造

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization 已有，enumeration_brute_force 已有，method_translation 已有
- [x] 粒度一致——三个维度都用已有值，粒度统一
- [x] 三个维度足够区分这道题的 tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类完全覆盖。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见 profile.json 中 tell_hint_pairs 字段（7对，每对含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）**

**全局tell_hint_pairs详见 profile.json 中 global_tell_hint_pairs 字段（2对，每对含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI 会尝试枚举小例子并可能猜到 m+n=2^k 的规律，但很难自行发现需要用奇素因子构造不变量来完成反向证明。AI 可能会尝试直接构造或用代数方法证明，但不会想到将操作闭包问题翻译为数论不变量问题。正向的 dyadic 加权平均构造也可能被忽略。
- suitable_for_poc: ["tell端验证——不变量方法的tell识别", "hint端验证——数论翻译方向的注入", "拓扑分类验证——characterization+method_translation的tell去特化"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `subagents-dirs/compfiles_usa2019p5/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329482"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2019p5"
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
    '_key': '329482',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2019p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2019p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2019p5
- solution_method_type: invariant_method
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（characterization + enumeration_brute_force + method_translation）完全覆盖
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
