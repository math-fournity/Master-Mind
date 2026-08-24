# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000109
- **文件路径**: subagents-dirs/omni_math_000109/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329980（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000109/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有 f:R²→R 满足：(1) f(0,x)非递减；(2) f(x,y)=f(y,x)对称性；(3) 对任意x,y,z, (f(x,y)-f(y,z))(f(y,z)-f(z,x))(f(z,x)-f(x,y))=0（三元乘积为零，即至少两个相等）；(4) f(x+a,y+a)=f(x,y)+a平移不变性。
- 解答核心思路（1-2句话）：利用条件4将2D问题降为1D（f(x,y)=x+h(y-x)），用对称性得h(t)=h(-t)+t，用三元条件导出每条射线上h的二择性（线性或常数），再用非递减条件排除混合解，最终得h(t)=c+max(0,t)或c+min(0,t)。
- 解答关键步骤列表：
  1. **降维**：由条件4，f(x,y)=x+h(y-x)，其中h(t)=f(0,t)，将2D函数方程化为1D
  2. **对称性约束**：由条件2，h(t)=h(-t)+t，即h(t)-t/2为偶函数
  3. **三元条件重构**：条件3等价于对任意u,v，h(u)=u+h(v)、h(u+v)=u+h(v)、h(u)=h(u+v)中至少一个成立
  4. **射线上二择性**：令b=a得h(2a)=h(a)+a或h(2a)=h(a)，推广得h(na)=h(a)+(n-1)a（线性）或h(na)=h(a)（常数），混合子情形导致矛盾
  5. **非递减强制全局一致**：若某射线线性另一射线常数，非递减性导致矛盾（线性增长vs常数在重叠区域），故全局只能选一种
  6. **两解**：线性情形→h(t)=c+max(0,t)→f=c+max(x,y)；常数情形→h(t)=c+min(0,t)→f=c+min(x,y)
  7. **验证**：两族函数均满足全部四条件

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：有哪些已知条件？哪个条件看起来具有特殊的结构杠杆作用？ | 4个条件：(1)非递减(2)对称(3)三元乘积=0(4)平移不变。条件4看起来最强——直接关联f在不同点的值，可能用于降维。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的解题方向，特别注意条件4的结构角色 | 直接代入试值、假设线性形式、用条件4降维到1D、用条件3做case analysis、尝试min/max特殊函数 |
| 3 | 小尝试 | 0.3 | 试假设f(x,y)=αx+βy+γ，检查哪些条件成立 | 对称要求α=β；平移要求α+β=1故α=β=1/2；但三元乘积=(x-z)(y-x)(z-y)/8一般不为0。线性ansatz失败，解不是光滑函数。 |
| 4 | 思维操作引导 | 0.4 | 定义h(t)=f(0,t)，用条件4把f(x,y)用h表示 | f(x,y)=h(y-x)+x。2D问题化为1D函数h的约束。 |
| 5 | 思维操作引导 | 0.5 | 用h重写条件3，"至少两个相等"在h语言中意味着什么？ | 令u=y-x,v=z-y,w=x-z。三个值h(u),u+h(v),h(u+v)中至少两个相等。即对任意u,v：h(u)=u+h(v)或h(u+v)=u+h(v)或h(u)=h(u+v)至少一个成立。 |
| 6 | 推进 | 0.4 | 令v=u推导h(2a)两种可能，推广到h(na) | h(2a)=h(a)+a（线性）或h(2a)=h(a)（常数）。线性推广h(na)=h(a)+(n-1)a；常数得h(na)=h(a)。混合子情形导致矛盾。 |
| 7 | 思维操作引导 | 0.5 | 不同射线能否选不同情形？用条件1（非递减）排除混合 | 不能混合：线性射线增长vs常数射线恒定，非递减性在重叠区域产生矛盾。故全局一致。 |
| 8 | 能量传递引导 | 0.3 | 写出两个解并验证全部四条件 | 线性→h(t)=c+max(0,t)→f=c+max(x,y)；常数→h(t)=c+min(0,t)→f=c+min(x,y)。均满足四条件。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R7"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 多条件约束的函数方程，2D→1D降维结构，三元乘积=0的组合约束，平移不变性作为降维杠杆，非递减条件作为全局一致性强制器
- key_objects: ["f:R²→R的二元函数", "h(t)=f(0,t)的一维约化", "三元乘积条件(至少两个相等)", "平移不变性f(x+a,y+a)=f(x,y)+a", "射线上的二择性(线性/常数)"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["降维化归(2D→1D)", "条件重构(三元乘积→至少两个相等→三选一)", "特殊化代入(令v=u导出二择性)", "反证法(混合子情形导致矛盾)", "单调性强制全局一致性", "枚举验证"]
- primary_pattern: 降维化归+条件重构→二择性→单调性强制全局一致
- knowledge_required: ["函数方程的基本技巧", "平移不变性与降维", "对称函数的性质", "单调函数的性质", "反证法"]
- key_insight: 条件1(非递减)看似只是正则性条件，实则是排除混合解的关键——它将"每条射线独立二择"提升为"全局统一二择"

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 2D多元函数方程的直接操作（代入、试值、case analysis）
- translation_to: 1D单变量函数h的结构分析（降维+三元条件重构+射线二择性+单调性强制）
- translation_type: structural_transformation（维数降低+条件语义重构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["降维(2D→1D)", "平移不变性", "三元乘积=至少两个相等", "射线二择性", "单调性强制全局一致", "条件角色反转(正则性→判别性)"]
- expected_ai_method: bare AI会尝试直接代入和case-by-case验证条件，可能试线性/多项式ansatz但失败后卡住，不会想到用条件4降维到1D
- correct_method: 用条件4降维到1D函数h，重构三元条件为三选一约束，导出射线二择性，用非递减条件强制全局一致

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_manipulation/structural_transformation能准确描述这道题
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足够区分
- 拓扑进化建议：无。现有分类体系足够。

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs摘要**：
- R1: tell=看到4条件但未识别结构杠杆, hint=描述结构识别杠杆, level=0.8, 纯元认知观察, topo=(characterization, direct_manipulation, structural_transformation)
- R2: tell=列举方向但未识别条件4的降维角色, hint=列举所有方向注意条件4, level=0.7, 自由列举, topo=(characterization, enumeration_brute_force, method_problem_mismatch)
- R3: tell=试线性ansatz失败, hint=试线性检查条件, level=0.3, 小尝试, topo=(characterization, direct_calculation, method_problem_mismatch)
- R4: tell=未降维到1D, hint=定义h用条件4降维, level=0.4, 思维操作引导, topo=(characterization, direct_manipulation, structural_transformation)
- R5: tell=有1D约化但未重构三元条件, hint=用h重写三元条件, level=0.5, 思维操作引导, topo=(characterization, algebraic_identity, structural_transformation)
- R6: tell=有重构但未导出二择性, hint=令v=u导出二择性, level=0.4, 推进, topo=(characterization, logical_deduction, structural_transformation)
- R7: tell=有二择性但未用单调性强制全局, hint=用非递减排除混合, level=0.5, 思维操作引导, topo=(characterization, logical_deduction, knowledge_gap)
- R8: tell=有两解需验证, hint=写出验证, level=0.3, 能量传递引导, topo=(characterization, direct_calculation, knowledge_gap)

**全局pairs摘要**：
- G1(path_feature): tell=三步结构变换(降维→二择性→单调性强制), hint=识别三步结构, level=0.6, why_not_visible_locally=每步依赖前步结果,整体结构从任一单步不可见
- G2(implicit): tell=条件1(非递减)从正则性条件变为判别性条件, hint=条件1是关键判别器, level=0.7, why_not_visible_locally=条件1在早期步骤看似无用,其关键角色仅在二择性导出后才显现

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接代入和试线性/多项式形式，线性失败后可能尝试min/max但无法系统证明完整性。关键缺口：(1)不会想到用条件4降维到1D；(2)即使降维也不会系统导出射线二择性；(3)不会意识到条件1(非递减)是排除混合解的判别器而非 mere 正则性条件。
- suitable_for_poc: ["hint注入实验(降维提示)", "tell识别实验(条件角色反转)", "脉络继承实验(多步结构变换)"]
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
2. 更新`problem_extraction_progress`集合中`_key="329980"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000109"
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
    '_key': '329980',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000109',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000109')
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
- problem_id: omni_math_000109
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，现有分类体系(characterization/direct_manipulation/structural_transformation)足够
- 是否遇到异常: problem.lean中Solution文本被截断，基于数学内容完整重构了解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
