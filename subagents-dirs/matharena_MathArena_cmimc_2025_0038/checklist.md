# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: matharena_MathArena_cmimc_2025_0038
- **文件路径**: subagents-dirs/matharena_MathArena_cmimc_2025_0038/problem.lean
- **来源**: MathArena MathArena_cmimc_2025
- **ArangoDB progress记录_key**: 329670（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/matharena_MathArena_cmimc_2025_0038/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定三角形ABC，AB=78, BC=50, AC=112。在三角形外侧构造正方形ABXY, BCPQ, ACMN。L1, L2, L3分别为MP, QX, YN的中点。求三角形L1L2L3的面积。
- 解答核心思路（1-2句话）：用向量法和90°旋转算子系统计算三个外正方形的顶点坐标，再求中点L1/L2/L3，用叉积求面积。面积公式简化为 Area = (a²+b²+c²)/4 + (7/4)·Area(ABC)。
- 解答关键步骤列表：
  1. 用余弦定理确定三角形ABC的坐标（B在原点，C在(50,0)，A由cos(B)=-33/65, sin(B)=56/65算出）
  2. 用90°旋转算子系统计算三个外正方形的顶点X,Y,P,Q,M,N
  3. 计算中点L1=(M+P)/2, L2=(Q+X)/2, L3=(Y+N)/2
  4. 用向量叉积计算三角形L1L2L3的面积
  5. 验证公式：Area = (a²+b²+c²)/4 + (7/4)·Area(ABC) = 21128/4 + 7·1680/4 = 5282 + 2940 = 8222

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | 观察这道题的结构：已知什么？要求什么？三个外正方形和三个中点之间有什么连接关系？ | 已知三角形三边AB=78,BC=50,AC=112，构造三个外正方形ABXY,BCPQ,ACMN。L1是MP中点，L2是QX中点，L3是YN中点。注意MP连接的是AC正方形和BC正方形的顶点，QX连接BC正方形和AB正方形，YN连接AB正方形和AC正方形——形成循环连接。要求的是三角形L1L2L3的面积。 |
| 2 | 自由列举 | 0.6 | 列出所有可能解决这道题的方法方向，包括坐标法、向量法、复数法、纯综合几何等 | 1) 坐标法：建系后逐个计算正方形顶点坐标，再算中点和面积；2) 向量法：用向量表示顶点，利用旋转算子简化；3) 复数法：用复数乘法表示90°旋转；4) 纯综合几何：利用正方形和三角形面积关系；5) 三角法：用余弦/正弦定理直接算面积。 |
| 3 | 小尝试 | 0.3 | 试着用纯坐标法：把B放原点，C放(50,0)，算出A的坐标，然后直接计算所有正方形顶点 | A=(-39.6, 67.2)。但手动计算6个正方形顶点坐标非常繁琐，容易出错。每个正方形需要判断旋转方向（顺时针还是逆时针），而且中点MP/QX/YN的连接关系容易搞混。数值计算量大，难以看出简化模式。 |
| 4 | 思维操作引导 | 0.4 | 用向量旋转算子来系统化处理：定义R为90°逆时针旋转，对每条边的外正方形，用R或-R统一表示顶点位置。先确定每条边的外正方形应该用哪个方向的旋转 | 对AB边，C在A→B的左侧，外正方形在右侧=R_cw=-R；对BC边，A在B→C的左侧，外正方形在右侧=-R；对AC边，B在A→C的右侧，外正方形在左侧=R。于是：X=BR(-u), Y=A+R(-u), P=C+(-Rv), Q=B+(-Rv), M=C+R(v-u), N=A+R(v-u)，其中u=BA, v=BC。 |
| 5 | 推进 | 0.4 | 继续用向量表示计算L1, L2, L3的坐标，然后用叉积求面积 | L1=(M+P)/2=v-Ru/2, L2=(Q+X)/2=R(u-v)/2, L3=(Y+N)/2=u+Rv/2。计算(L2-L1)×(L3-L1)，利用恒等式Ra×b=-(a·b), a×Rb=a·b, Ra×Rb=a×b展开，得到=-c²-a²+(u·v)+(7/4)(u×v)。 |
| 6 | 思维操作引导 | 0.5 | 将结果用三角形边长和面积表达：u·v=(a²+c²-b²)/2, |u×v|=2·Area(ABC)。代入简化 | -c²-a²+(a²+c²-b²)/2+(7/4)·2·Area(ABC) = -(a²+b²+c²)/2 + (7/2)·Area(ABC)。取绝对值后：2·Area(L1L2L3) = (a²+b²+c²)/2 + (7/2)·Area(ABC)，即 Area = (a²+b²+c²)/4 + (7/4)·Area(ABC)。 |
| 7 | 能量传递引导 | 0.6 | 代入具体数值验证这个优美公式，确认答案 | a²+b²+c²=50²+112²+78²=21128, Area(ABC)=1680（海伦公式s=120, √(120·70·8·42)=1680）。Area=21128/4+7·1680/4=5282+2940=8222。公式简洁优美，答案确认。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.7+0.6+0.3+0.4+0.4+0.5+0.6=3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction（给定三角形三边约束，计算特定几何构造的面积值）
- structure_features: 三角形三边已知→构造三个外正方形→取跨正方形顶点连线的中点→求中点三角形面积。关键结构是"循环连接"：MP连接AC正方形和BC正方形，QX连接BC正方形和AB正方形，YN连接AB正方形和AC正方形。
- key_objects: 三角形ABC（边长78,50,112）、外正方形ABXY/BCPQ/ACMN、中点L1/L2/L3、向量旋转算子R（90°逆时针）、向量叉积

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [结构识别, 方法系统化, 向量代数化, 恒等式简化, 公式验证]
- primary_pattern: 向量代数化（用旋转算子将几何构造翻译为向量运算，再用叉积恒等式简化）
- knowledge_required: [余弦定理, 90°旋转算子, 向量叉积, 叉积恒等式(Ra×b=-(a·b), a×Rb=a·b), 海伦公式]
- key_insight: 用90°旋转算子R统一表示三个外正方形的顶点位置后，中点L1/L2/L3的表达式极其简洁，叉积展开时利用Ra×b=-(a·b)等恒等式，面积公式自动简化为(a²+b²+c²)/4+(7/4)·Area(ABC)

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 几何构造语言（外正方形顶点、中点连线）
- translation_to: 向量代数语言（旋转算子R、叉积、点积恒等式）
- translation_type: structural_transformation（将几何构造系统性翻译为向量运算，核心是90°旋转算子作为正方形构造的代数表示）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: [外正方形构造, 90°旋转算子, 向量叉积, 中点三角形面积, 叉积恒等式, 循环连接]
- expected_ai_method: bare AI会尝试直接坐标法——逐个计算6个正方形顶点的数值坐标，再算中点和面积。容易在旋转方向判断上出错，且数值计算量大难以发现简化公式。
- correct_method: 向量法——用90°旋转算子R统一表示外正方形顶点，中点表达式简洁，叉积展开利用恒等式自动简化为(a²+b²+c²)/4+(7/4)·Area(ABC)。

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——constraint_satisfaction/direct_calculation/method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新拓扑维度——三个维度足够区分
- 无进化建议

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中的tell_hint_pairs数组。
全局pairs详见profile.json中的global_tell_hint_pairs数组。

全局pair 1 (path_feature型):
- scope: 完整解题路径R1→R7
- tell: 从纯坐标计算到向量旋转算子的方法升级是贯穿全程的核心路径特征
- hint: 在R3坐标法遇到繁琐计算时，不要坚持数值计算，而是升级到向量旋转算子表示
- hint_level: 0.5
- generalizability: high——任何涉及正方形构造的几何计算问题都可泛化此路径
- why_not_visible_locally: 在R3局部视角只看到"计算繁琐"，看不到这是方法层次的问题而非计算技巧的问题；需要从R3→R4的跳跃中才能看出是方法升级而非局部优化

全局pair 2 (implicit型):
- scope: 面积公式的结构
- observation_point: R6
- tell: 面积公式(a²+b²+c²)/4+(7/4)·Area(ABC)中7/4系数蕴含了外正方形构造与三角形面积的深层关系
- hint: 注意7/4这个系数不是偶然的——它来自叉积展开中(7/4)(u×v)项，反映了三个正方形旋转方向的循环对称性
- hint_level: 0.7
- generalizability: medium——系数7/4对此外正方形构型特定，但"叉积展开系数反映几何对称性"的思路可泛化
- why_not_visible_locally: 在R5的叉积展开中，7/4系数只是代数运算的中间结果，局部视角看不到它对应的几何意义；需要从整体公式结构回看才能识别

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "marginal"
- bare_ai_error_prediction: bare AI可能用坐标法算出正确答案，但容易在旋转方向判断上出错（特别是AC边的外正方形方向与AB/BC相反），导致面积计算错误。即使方向正确，数值精度问题也可能导致答案偏差。AI不太可能自行发现向量旋转算子方法和简化公式。
- suitable_for_poc: ["hint_injection（在R4注入旋转算子方向）", "tell_detection（检测AI在R3是否陷入数值计算而未升级方法）", "method_translation（几何→向量翻译验证）"]
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
2. 更新`problem_extraction_progress`集合中`_key="329670"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/matharena_MathArena_cmimc_2025_0038"
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
    '_key': '329670',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/matharena_MathArena_cmimc_2025_0038',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('matharena_MathArena_cmimc_2025_0038')
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
- problem_id: matharena_MathArena_cmimc_2025_0038
- solution_method_type: direct_calculation（向量旋转算子法）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，现有拓扑分类够用
- 是否遇到异常: 否

**操作**：向Master Agent报告

**汇报内容**：
- problem_id:
- solution_method_type:
- 局部(tell,hint)对数量:
- 全局(tell,hint)对数量:
- 是否发现新维度:
- **拓扑分类是否有进化建议**:
- 是否遇到异常:

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
