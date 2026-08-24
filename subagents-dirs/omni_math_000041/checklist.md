# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000041
- **文件路径**: subagents-dirs/omni_math_000041/problem.lean
- **来源**: AoPS omni_math (china_national_olympiad)
- **ArangoDB progress记录_key**: 329912（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000041/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 n=p₁^a₁p₂^a₂...p_t^a_t 为n的素因子分解，定义ω(n)=t（不同素因子个数）和Ω(n)=a₁+a₂+...+a_t（素因子总数含重数）。证明或否定：对任意固定正整数k和正实数α,β，存在n>1使得 (i) ω(n+k)/ω(n)>α 且 (ii) Ω(n+k)/Ω(n)<β。
- 解答核心思路（1-2句话）：两个条件分别用不同构造证明——(i)用CRT让n+k被很多不同素数整除+Dirichlet定理保证n为素数(ω(n)=1)；(ii)用Dirichlet定理保证n+k为素数(Ω(n+k)=1)+取n被某素数的高次幂整除(Ω(n)任意大)。
- 解答关键步骤列表：
  1. 条件(i)：取s>α个不同素数q₁,...,q_s，由CRT找n₀使n₀+k≡0 mod q_i (∀i)，由Dirichlet定理存在素数p≡n₀ mod Q(Q=q₁...q_s)，取n=p则ω(n)=1且ω(n+k)≥s>α
  2. 条件(ii)：取素数q∤k，由Dirichlet定理存在无穷多素数p≡k mod q^a，取n=p-k则n+k=p为素数(Ω(n+k)=1)且q^a|n故Ω(n)≥a，比值≤1/a<β（a足够大时）
  3. 两个条件分别可满足，故命题为True

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构。题目要求同时满足两个关于ω和Ω在n与n+k处比值的条件。你能描述出已知条件、目标和两个条件之间的关系吗？ | ω(n)=不同素因子个数，Ω(n)=素因子总数含重数。两个条件：(i)ω(n+k)/ω(n)>α要求n+k比n"素因子种类更多"；(ii)Ω(n+k)/Ω(n)<β要求n+k比n"素因子总数更少"。两个条件方向看似矛盾——一个要n+k"大"一个要n+k"小"。 |
| 2 | 自由列举 | 0.7 | 要控制ω(n+k)/ω(n)任意大同时Ω(n+k)/Ω(n)任意小，你有哪些可能的构造方向？列出所有能想到的工具和方法。 | 可能方向：取n为素数(ω=1,Ω=1)、取n为素数幂(Ω大)、CRT构造同余、Dirichlet素数定理、取n为高度合成数、直接枚举搜索、用素数分布定理等。 |
| 3 | 小尝试 | 0.5 | 试试直接取n为一个大素数，看看两个条件能否同时满足。 | n为素数时ω(n)=1,Ω(n)=1。条件(i)需ω(n+k)>α，可能可行如果n+k有很多素因子。但条件(ii)需Ω(n+k)<β·Ω(n)=β，当β<1时需Ω(n+k)<1即Ω(n+k)=0不可能(n+k>1)。所以单纯取n为素数对条件(ii)失败。 |
| 4 | 思维操作引导 | 0.4 | 条件(i)和(ii)可能需要分开处理。对于条件(i)，如何让ω(n+k)/ω(n)任意大？思考ω(n)最小可以是多少，以及如何让ω(n+k)任意大。 | ω(n)最小为1（n为素数或素数幂）。要ω(n+k)任意大：用CRT取s>α个不同素数q₁,...,q_s，构造n₀+k≡0 mod q_i(∀i)。再用Dirichlet定理保证n≡n₀ mod Q的解中存在素数p，取n=p则ω(n)=1且n+k被q₁,...,q_s整除故ω(n+k)≥s>α。 |
| 5 | 推进 | 0.6 | 很好，条件(i)的CRT+Dirichlet构造已经清晰。现在转向条件(ii)：如何让Ω(n+k)/Ω(n)任意小？思考如何让Ω(n)任意大而Ω(n+k)有界。 | 需要Ω(n)很大但Ω(n+k)很小。取n=2^m则Ω(n)=m但Ω(n+k)≤log₂(n+k)≈m，比值趋于1不够小。需要让n+k本身是素数(Ω=1)同时n含高次素因子幂。可用Dirichlet：取q∤k，存在素数p≡k mod q^a，令n=p-k则n+k=p(Ω=1)且q^a|n故Ω(n)≥a，比值≤1/a→0。 |
| 6 | 思维操作引导 | 0.3 | 对于条件(ii)，关键是用Dirichlet素数定理：取一个不整除k的素数q，由Dirichlet定理存在无穷多素数p≡k mod q^a。令n=p-k，则n+k=p为素数(Ω(n+k)=1)而q^a|n使Ω(n)≥a。请完整写出这个论证。 | 取素数q不整除k（总存在这样的q）。对足够大的a使1/a<β，由Dirichlet定理（gcd(k,q^a)=1），存在素数p≡k mod q^a。令n=p-k>1（取足够大的p），则n+k=p为素数故Ω(n+k)=1，而q^a|n故Ω(n)≥a。因此Ω(n+k)/Ω(n)≤1/a<β。 |
| 7 | 能量传递引导 | 0.7 | 两个条件都已分别证明。现在请将完整证明组装起来，确认命题为True。 | 条件(i)：CRT+Dirichlet构造n为素数(ω(n)=1)且n+k有>s>α个不同素因子。条件(ii)：Dirichlet构造n+k为素数(Ω(n+k)=1)且n被q^a整除(Ω(n)≥a>1/β)。两个条件分别可满足，命题为True。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 两个独立的存在性条件，分别要求ω比值任意大和Ω比值任意小；需要构造n使两个条件分别满足；核心是算术函数在n和n+k处的极端比值控制
- key_objects: ["ω(n)——不同素因子个数", "Ω(n)——素因子总数含重数", "n+k的素因子结构", "CRT同余方程组", "Dirichlet素数定理"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["条件分离——两个看似矛盾的条件分别处理", "极值化构造——让分子或分母取极端值(1或任意大)", "CRT+Dirichlet组合——用CRT构造同余条件用Dirichlet保证素数存在", "逆向构造——从目标比值出发设计n的性质"]
- primary_pattern: 条件分离与分别构造
- knowledge_required: ["ω(n)和Ω(n)的定义与性质", "中国剩余定理(CRT)", "Dirichlet素数定理(算术级数中素数无限)", "素因子分解唯一性"]
- key_insight: 两个条件方向相反但可分别满足——(i)让ω(n)=1且ω(n+k)任意大(CRT+Dirichlet)，(ii)让Ω(n+k)=1且Ω(n)任意大(Dirichlet+高次幂整除)

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 存在性不等式条件（ω比值>α, Ω比值<β）
- translation_to: CRT同余方程组构造 + Dirichlet素数存在性保证
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "enumeration_brute_force", gap_type: "knowledge_gap"}
- tell_small_concepts: ["条件分离", "CRT构造", "Dirichlet素数定理", "ω极小化", "Ω极大化", "算术级数素数"]
- expected_ai_method: bare AI会尝试直接枚举n或取简单形式(如n=素数)同时满足两个条件，发现矛盾后可能放弃或试图用复杂分析估计
- correct_method: 分离两个条件分别构造——(i)CRT+Dirichlet让n为素数且n+k多素因子，(ii)Dirichlet让n+k为素数且n含高次素因子幂

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence / enumeration_brute_force / knowledge_gap 完全适用
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——Dirichlet定理作为知识瓶颈由knowledge_gap捕获，条件分离由structural_existence捕获
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无

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
- bare_ai_error_prediction: bare AI会尝试用一个构造同时满足两个条件（如取n为素数），发现条件(ii)在β<1时不可能后可能放弃；或不知道Dirichlet素数定理无法完成构造；或不知道可以分离两个条件分别处理
- suitable_for_poc: ["hint注入实验——验证条件分离提示+Dirichlet定理知识注入能否引导AI完成证明", "tell识别实验——验证系统能否从AI的thinking中识别出'未分离条件'和'缺乏Dirichlet知识'两个tell"]
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
2. 更新`problem_extraction_progress`集合中`_key="329912"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000041"
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
    '_key': '329912',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000041',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000041')
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
- problem_id: omni_math_000041
- solution_method_type: existence_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类完全适用
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
