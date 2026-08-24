# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000291
- **文件路径**: subagents-dirs/fate_000291/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396401（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000291/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设k为任意域。A = k[[x,y]]/(f)，B = k[[u,v]]/(g)，其中f = xy，g = uv + δ，δ ∈ (u,v)³。证明A与B同构。
- 解答核心思路（1-2句话）：利用k[[u,v]]的完备性，通过逐次逼近构造形式自同构σ，使σ(uv) = uv + δ，从而诱导商环同构A ≅ B。关键在于δ ∈ (u,v)³恰好保证坐标变换的线性部分为恒等映射。
- 解答关键步骤列表：
  1. 识别δ ∈ (u,v)³意味着δ仅含次数≥3的项
  2. 设σ(u) = u + f, σ(v) = v + h，需求(u+f)(v+h) = uv + δ，即uh + vf + fh = δ
  3. 逐次逼近：第一步取f₁, h₁ ∈ (u,v)²使uh₁ + vf₁ = δ (mod (u,v)⁴)，残差δ' ∈ (u,v)⁴
  4. 继续迭代：第n步取fₙ, hₙ ∈ (u,v)^{n+1}，残差进入(u,v)^{n+3}
  5. 由k[[u,v]]的(u,v)-adic完备性，f = Σfₙ, h = Σhₙ收敛
  6. σ = (u↦u+f, v↦v+h)是形式自同构（线性部分为恒等），σ(uv) = uv + δ
  7. σ诱导环同构k[[u,v]]/(uv) → k[[u,v]]/(uv+δ)，即A ≅ B

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的数学结构：已知什么对象、什么条件、要证明什么结论？特别地，δ ∈ (u,v)³这个条件在说什么？ | A = k[[x,y]]/(xy)和B = k[[u,v]]/(uv+δ)是两个形式幂级数环的商环。δ ∈ (u,v)³表示δ是极大理想的三次方中的元素，即δ只含次数≥3的项。要证明A ≅ B。 |
| 2 | 自由列举 | 0.7 | 列出所有可能证明两个商环同构的方法方向。 | 1) 直接构造环同态A→B；2) 找ambient ring的自同构把一个理想映到另一个；3) 用泛性质；4) 用Hensel引理；5) 用Cohen结构定理；6) 比较不变量（维数、奇点类型等）验证同构可能性。 |
| 3 | 小尝试 | 0.5 | 尝试直接构造一个环同态A → B，即把x和y映到B中的某个元素。你会遇到什么困难？ | 需要把x映到B中某元素a，y映到b，使得ab = 0 in B（因为xy = 0 in A）。但B = k[[u,v]]/(uv+δ)，ab = 0意味着ab ∈ (uv+δ)。不知道δ的具体形式，很难直接找到这样的a, b。直接构造法受阻于δ的未知性。 |
| 4 | 思维操作引导 | 0.4 | 换一个层次思考：如果能找到k[[u,v]]的自同构σ使得σ(uv) = uv + δ = g，那么σ能诱导什么？ | σ(uv) = g意味着σ把理想(uv)映到理想(g)。因此σ诱导商环同构k[[u,v]]/(uv) → k[[u,v]]/(g)，这正是A → B的同构（重命名变量后）。所以问题转化为：构造形式自同构σ使σ(uv) = uv + δ。 |
| 5 | 思维操作引导 | 0.3 | 设σ(u) = u + f, σ(v) = v + h，写出σ(uv) = uv + δ的方程。f和h应该属于哪个理想？为什么？ | (u+f)(v+h) = uv + uh + vf + fh = uv + δ，所以uh + vf + fh = δ。因为δ ∈ (u,v)³，而uv的次数为2，所以f和h的最低次数应≥2（即f, h ∈ (u,v)²），这样uh和vf的次数≥3才能匹配δ的次数。线性部分为恒等映射保证σ是自同构。 |
| 6 | 推进 | 0.2 | 用逐次逼近求解uh + vf + fh = δ。第一步如何取f₁, h₁？残差进入哪个理想？为什么这个过程收敛？ | 第一步：将δ的每个次数≥3的单项式u^a v^b分配到uh₁或vf₁中（当a≥1时放入u·(u^{a-1}v^b)给h₁，当b≥1时放入v·(u^a v^{b-1})给f₁）。取f₁, h₁ ∈ (u,v)²使uh₁ + vf₁ = δ。残差δ' = δ - uh₁ - vf₁ - f₁h₁ ∈ (u,v)⁴（因为f₁h₁ ∈ (u,v)⁴）。第n步残差 ∈ (u,v)^{n+2}，修正fₙ, hₙ ∈ (u,v)^{n+1}。由k[[u,v]]的(u,v)-adic完备性，f = Σfₙ, h = Σhₙ收敛。 |
| 7 | 能量传递引导 | 0.6 | 总结完整论证，确认每一步都成立。 | 1) δ ∈ (u,v)³保证f, h ∈ (u,v)²，线性部分为恒等；2) 逐次逼近在完备拓扑下收敛；3) σ(u) = u+f, σ(v) = v+h是k[[u,v]]的形式自同构；4) σ(uv) = uv+δ = g；5) σ诱导环同构k[[u,v]]/(uv) ≅ k[[u,v]]/(g)，即A ≅ B。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 两个形式幂级数环的商环，其中一个的理想生成元是另一个加上高阶扰动项；需要证明存在环同构。核心结构是"ambient ring + ideal + 扰动条件"。
- key_objects: ["形式幂级数环 k[[u,v]]", "极大理想 (u,v)", "商环 A = k[[x,y]]/(xy)", "商环 B = k[[u,v]]/(uv+δ)", "形式自同构 σ", "逐次逼近序列 fₙ, hₙ"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_translation", "successive_approximation", "coordinate_change", "completeness_convergence"]
- primary_pattern: structural_translation
- knowledge_required: ["形式幂级数环", "完备局部环", "环自同构", "逐次逼近/Hensel提升", "理想adic拓扑", "商环同构的诱导"]
- key_insight: δ ∈ (u,v)³恰好保证坐标变换σ(u)=u+f, σ(v)=v+h的线性部分为恒等映射，使得逐次逼近在完备拓扑下收敛，从而σ(uv)=uv+δ诱导商环同构。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接构造商环之间的环同态（商环层面）
- translation_to: 构造ambient ring的形式自同构使一个理想映到另一个（ambient ring层面）
- translation_type: level_translation（从商环层面提升到ambient ring层面）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["形式幂级数环商", "极大理想幂次条件", "ambient ring自同构", "逐次逼近收敛", "坐标变换"]
- expected_ai_method: 直接构造商环A→B的环同态，试图把x和y映到B中的具体元素，受阻于δ的未知形式
- correct_method: 构造k[[u,v]]的形式自同构σ使σ(uv)=uv+δ，通过逐次逼近在完备拓扑下收敛，诱导商环同构

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence, ai_method_type=direct_manipulation, gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足够。

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
- bare_ai_error_prediction: Bare AI会尝试直接构造商环A→B的环同态，把x和y映到B中的具体元素，但不知道δ的具体形式无法找到合适的像。AI不会意识到应该切换到ambient ring层面构造自同构，也不会想到用逐次逼近在完备拓扑下求解。可能误认为需要知道δ的具体形式才能证明，或误用Hensel引理的方向。
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "method_translation_poc"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成。

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: fate_000291, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000291
- solution_method_type: formal automorphism via successive approximation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类足够
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
