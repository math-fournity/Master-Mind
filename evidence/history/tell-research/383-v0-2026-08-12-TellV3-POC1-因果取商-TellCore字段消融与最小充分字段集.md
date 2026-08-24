# 383号 · TellV3 POC-1因果取商——TellCore字段消融与最小充分字段集

**日期**：2026-08-12  
**状态**：POC-1分析稿；不启动Solver，不修改代码，不写入数据库。  
**触发原因**：382号CasePack v0冻结后，用户确认TellCore v0采纳候选C（局部-全局表示切换），并要求下一步做POC-1因果取商。  
**前置文档**：372号（非特化全需求与六门审计），373号（POC套装设计方案第6节POC-1），382号（CasePack v0）。  
**适用对象**：准备执行POC-2~POC-8的AI。

---

## 0. 一句话结论

对TellCore v0候选C（局部-全局表示切换）做12字段逐项消融后，确定**最小充分字段集为7个字段**（invariant_claim、trigger_boundary、negative_boundary、parameter_slots、internal_policy、progress_model、termination），3个字段为重要补充（binding_rules、critic、composition_contract），2个字段为元数据/输入（name、source_branch_events）。TellCore v0通过POC-1全部7项通过标准，但CC-014和CC-017的假朋友拒绝需要selector和critic协同设计。

---

## 1. POC-1的目标与方法

### 1.1 目标（来自373号第6节）

POC-1回答：

> 从trace中抽出的TellCore，是否保留了真正起作用的结构？

具体而言，POC-1对TellCore做"因果取商"——把源题对象、符号、叙事和偶然路径压掉，只保留能解释成功转向的关系结构、触发条件、动作策略和证据要求。

### 1.2 方法

对TellCore v0候选C的每个字段做消融分析：

```text
对每个字段 F：
  问1：删除F后，TellCore是否仍可在新题上执行？
  问2：删除F后，TellCore是否仍能解释迁移？
  问3：删除F后，替换表面外壳后是否保持作用？
  问4：删除F后，改变关键结构后是否应拒绝？
  问5：删除F后，是否能解释正例和负例的差异？
  
  若全部"是" → F非必要
  若有"否" → F必要或重要
```

然后验证373号第6.4节的7项通过标准。

### 1.3 分析对象

TellCore v0候选C的12个字段：

| 编号 | 字段 | 类型 |
|---|---|---|
| F1 | name | 元数据 |
| F2 | invariant_claim | 核心主张 |
| F3 | source_branch_events | 历史证据（输入） |
| F4 | trigger_boundary | 触发条件 |
| F5 | negative_boundary | 负触发条件 |
| F6 | parameter_slots | 参数槽 |
| F7 | binding_rules | 绑定规则 |
| F8 | internal_policy | 内部策略（6步） |
| F9 | progress_model | 进展模型 |
| F10 | termination | 终止条件 |
| F11 | critic | 自检 |
| F12 | composition_contract | 组合接口 |

---

## 2. 逐字段消融分析

### F1：name（元数据）

**删除后影响**：无功能性影响。name是标识符，不参与执行、选择或归责。

**判定**：**非必要**。属于元数据，不纳入最小充分字段集。

---

### F2：invariant_claim（核心主张）

**原内容**：当问题在全局/自然表示下陷入困境时，切换到局部表示（Z/pZ或Q_p），在局部表示下揭示隐藏的代数结构，将局部发现提升为全局结论。

**删除后影响**：
- 问1（可执行）：internal_policy仍给出步骤，但AI不知道"为什么"要做这些步骤。执行变为机械操作，无法在意外情况下调整。
- 问2（迁移解释）：无法解释为什么同一策略在1631（模8+二次剩余）和1843（模4+符号配对）上都有效——因为缺少"局部-全局"这个统一解释。
- 问3（表面替换）：无法解释为什么改变底数（CC-009）或改变p（CC-011）后策略仍有效。
- 问4（结构改变）：无法解释为什么"素数"条件（CC-018）使策略失效——因为缺少"局部表示需要整除性/幂结构"的解释。
- 问5（正负例差异）：无法解释为什么假朋友（CC-013级数收敛）不应触发——因为缺少"代数结构vs分析结构"的区分。

**判定**：**必要**。invariant_claim是因果解释的核心——它解释了"为什么局部化有效"和"什么时候局部化不适用"。

---

### F3：source_branch_events（历史证据）

**原内容**：列出1631/1843/1709/1962的分支事件。

**删除后影响**：
- 问1（可执行）：仍可执行。source_branch_events是TellCore的提取来源，不是运行时使用的字段。
- 问2（迁移解释）：迁移解释由invariant_claim提供，不由历史事件提供。
- 问3-5：无影响。

**判定**：**非必要（运行时）**。source_branch_events是POC-1的**输入**（从trace中提取TellCore时使用），不是TellCore的**运行时字段**。在运行时TellCore中可以不保留。但在POC-1分析中，它是验证因果取商是否成功的依据——如果删除source事件后TellCore仍保持结构，说明取商成功。

**重要区分**：source_branch_events不属于TellCore运行时，但属于POC-1的验证证据。POC-1的通过条件之一是"删除源题对象后是否仍可执行"——source_branch_events正是源题对象的载体。

---

### F4：trigger_boundary（触发条件）

**原内容**：
- 问题涉及整数的代数结构（整除性、素性、符号、幂、周期性）
- 自然表示下的分析陷入困境
- 问题中存在可以局部化的对象

**删除后影响**：
- 问1（可执行）：internal_policy的step1是"识别自然表示陷入困境的信号"——如果没有trigger_boundary，AI不知道什么时候启动这个策略。
- 问2（迁移解释）：无法解释为什么1631和1843都触发了这个策略——因为缺少"整除性/符号/周期性"这个共同触发条件。
- 问5（正负例差异）：无法区分正例（1631涉及素性=整除性）和负例（CC-013涉及收敛性=分析性）——trigger_boundary的"代数结构"条件是区分关键。

**判定**：**必要**。trigger_boundary是"可选择"门的核心——没有它，selector无法知道何时选这个Tell。

---

### F5：negative_boundary（负触发条件）

**原内容**：
- 问题核心在构造性而非分析性
- 问题核心在几何结构而非代数结构
- 问题已经在局部表示下
- 问题在自然表示下有直接解法
- 问题的核心困难在搜索空间大小而非结构隐藏

**删除后影响**：
- 问4（结构改变）：无法解释为什么CC-013（级数收敛）不应触发——negative_boundary的"构造性vs分析性"区分是拒绝CC-013的关键。
- 问5（正负例差异）：假朋友题CC-013/015/016的拒绝依赖negative_boundary。删除后，selector对假朋友题可能误触发。

**逐条消融**：

| 负触发条件 | 删除后哪些假朋友会误触发 | 重要性 |
|---|---|---|
| 构造性vs分析性 | CC-015（构造性组合） | 高 |
| 几何vs代数 | CC-006（几何边界——但CC-006应标boundary而非reject） | 中 |
| 已在局部表示下 | 无直接对应假朋友，但防止重复触发 | 低 |
| 自然表示有直接解法 | 防止过度触发简单题 | 中 |
| 搜索空间vs结构隐藏 | CC-016（组合计数——搜索空间大但非结构隐藏） | 高 |

**判定**：**必要**。negative_boundary是"可选择"门的另一半——没有它，selector无法知道何时拒绝这个Tell。

---

### F6：parameter_slots（参数槽）

**原内容**：p（局部化目标）、level（模p或p-adic）、objects（局部化对象）、target_structure（寻找的结构类型）

**删除后影响**：
- 问1（可执行）：AI不知道要绑定什么到新题上。internal_policy说"确定局部化目标p和层次"——但如果没有parameter_slots，AI不知道p和level是需要绑定的参数。
- 问3（表面替换）：无法解释为什么CC-009（底数3）仍可执行——因为parameter_slots的p可以绑定到不同的素数。

**逐槽消融**：

| 参数槽 | 删除后影响 | 重要性 |
|---|---|---|
| p | AI不知道要选择哪个素数做模分析 | 必要 |
| level | AI不知道该用模p还是p-adic——可能导致1962用模p而非p-adic | 必要 |
| objects | AI不知道要对哪些对象取模 | 必要 |
| target_structure | AI不知道在局部表示下找什么——可能盲目搜索 | 重要 |

**判定**：**必要**（p、level、objects三个槽）；**重要**（target_structure槽）。

---

### F7：binding_rules（绑定规则）

**原内容**：
- 从问题条件推断局部化目标p和层次
- 整除性/符号/周期性 → 模p（层次1）
- "是p的幂"/"被p^k整除" → p-adic赋值（层次2）
- 将所有相关对象映射到局部表示

**删除后影响**：
- 问1（可执行）：parameter_slots存在但不知道怎么填。AI可能猜对p但选错level（如1962用模2而不是v_2）。
- 问2（迁移解释）：无法解释为什么1631用模8（层次1）而1962用v_2（层次2）——binding_rules的"整除性→模p，幂→p-adic"是区分关键。

**判定**：**重要**。binding_rules可以从trigger_boundary和parameter_slots部分推断，但显式规则显著提高绑定准确性。不纳入最小充分集，但纳入重要补充。

---

### F8：internal_policy（内部策略，6步）

**原内容**：step1-6（识别困境→确定p和层次→映射→寻找结构→提升全局→fallback）

**删除后影响**：
- 问1（可执行）：TellCore退化为一句口号"切换到局部表示"。这正是1962在tree组失败的原因——只给方向（"切换到p-adic"）不够，AI需要操作路径。
- 问5（正负例差异）：无法解释为什么1962在tree组失败但1631/1843成功——因为1962需要更详细的操作路径（分case、建立v_2方程），而internal_policy的step3-6提供了这个路径。

**逐步消融**：

| 步骤 | 删除后影响 | 重要性 |
|---|---|---|
| step1（识别困境信号） | AI可能过早取模，在自然表示有直接解法时也强行局部化 | 重要 |
| step2（确定p和层次） | AI可能选错p或选错层次——这是最关键的决策点 | 必要 |
| step3（映射到局部表示） | 核心动作缺失——不知道怎样做局部化 | 必要 |
| step4（寻找隐藏结构） | 核心动作缺失——局部化后不知道找什么 | 必要 |
| step5（提升为全局结论） | 局部发现无法连接回原问题——"局部-全局"的"全局"半缺失 | 必要 |
| step6（fallback/组合） | 不完整结果时无法让位——"可终止"门受影响 | 重要 |

**判定**：**必要**（step2-5为最小充分）；**重要**（step1和step6为补充）。

**关键发现**：1962在VMS-8 tree组失败，正是因为tree组给的Tell只有方向（"切换到p-adic赋值"）而没有操作路径（怎样分case、怎样建立v_2方程）。TellCore v0候选C的internal_policy step2-5正是对这个失败的回应。这是POC-1最重要的因果取商发现：

```text
方向Tell（"切换到p-adic"）→ 1962失败
操作路径Tell（step2-5的系统步骤）→ 预期1962可执行
```

---

### F9：progress_model（进展模型）

**原内容**：4个信号（取模/p-adic讨论→发现隐藏结构→与原问题建立联系→提升为全局结论）

**删除后影响**：
- "可终止"门：不知道什么是"进展"——无法区分"执行中"和"原地打转"。
- "可归责"门：无法归因——不知道是哪一步失败的。
- 问5（正负例差异）：无法解释为什么CC-013（级数收敛）即使AI尝试取模也不会出现信号2-4——因为级数收敛问题在模p下没有"隐藏结构"可发现。

**判定**：**必要**。progress_model是"可终止"和"可归责"两门的基础。

---

### F10：termination（终止条件）

**原内容**：4个条件（成功、无进展、部分进展、冲突）

**删除后影响**：
- "可终止"门：AI可能无限围绕同一模数打转，或过早放弃有效方向。
- 1962的失败也部分源于termination缺失——AI在2-adic计算中陷入复杂代数但不知道何时退出。

**判定**：**必要**。termination是"可终止"门的直接载体。

---

### F11：critic（自检）

**原内容**：4个自检问题（p和层次是否匹配、局部发现是否对应目标、是否过早局部化、局部发现是否足以提升全局）

**删除后影响**：
- 问1（可执行）：首次执行仍可执行，但质量可能下降。
- "可持续学习"门：无法从失败中学习——critic的自检问题是修订trigger/binding的起点。
- CC-017（代数几何诱饵）：需要critic来识别"f≡g，方程恒成立，无分析必要"——trigger可能误触发，但critic可以拦截。

**判定**：**重要**。critic不是首次执行的必要条件，但是"可持续学习"门和复杂假朋友拒绝的必要条件。不纳入最小充分集，但纳入重要补充。

---

### F12：composition_contract（组合接口）

**原内容**：prerequisites、enables、conflicts_with、redundant_with、handoff_rule

**删除后影响**：
- "可组合"门：无法与其他Tell协同工作。
- 但对POC-1（因果取商）和POC-3（可执行）不直接影响——这两个POC测试单Tell执行，不测试组合。
- 对POC-5（可组合）是必要条件。

**判定**：**重要（对POC-5）**。不纳入最小充分集（POC-1不要求），但纳入重要补充（POC-5要求）。

---

## 3. 最小充分字段集

### 3.1 字段分级

| 级别 | 字段 | 数量 | 说明 |
|---|---|---:|---|
| **必要** | invariant_claim, trigger_boundary, negative_boundary, parameter_slots(p+level+objects), internal_policy(step2-5), progress_model, termination | 7 | 删除任一导致TellCore无法通过至少一门审计 |
| **重要补充** | binding_rules, internal_policy(step1+step6), critic, composition_contract, parameter_slots(target_structure) | 5 | 删除导致特定POC或特定场景失败 |
| **元数据/输入** | name, source_branch_events | 2 | 不参与运行时执行 |

### 3.2 最小充分字段集

```yaml
TellCore_minimal:
  invariant_claim: |
    当问题在全局/自然表示下陷入困境时，
    切换到局部表示（Z/pZ或Q_p），
    在局部表示下揭示隐藏的代数结构，
    将局部发现提升为全局结论。
  trigger_boundary:
    - 问题涉及整数的代数结构（整除性、素性、符号、幂、周期性）
    - 自然表示下的分析陷入困境
    - 问题中存在可以局部化的对象
  negative_boundary:
    - 问题核心在构造性而非分析性
    - 问题核心在几何结构而非代数结构
    - 问题已经在局部表示下
    - 问题在自然表示下有直接解法
    - 问题的核心困难在搜索空间大小而非结构隐藏
  parameter_slots:
    - p: 局部化的目标素数
    - level: 模p 或 p-adic赋值
    - objects: 需要局部化的对象
  internal_policy:
    step2: 分析问题条件，确定局部化目标p和层次
    step3: 将问题映射到局部表示
    step4: 在局部表示下寻找隐藏结构
    step5: 将局部发现提升为全局结论或约束
  progress_model:
    - 信号1: AI开始讨论"取模"或"p-adic赋值"
    - 信号2: AI在局部表示下发现了隐藏结构
    - 信号3: AI将局部发现与原问题目标建立联系
    - 信号4: AI成功将局部发现提升为全局结论
  termination:
    - 成功: 局部发现直接解决原问题或给出关键约束
    - 无进展: 尝试多个p或层次后未发现有用结构 → 退出
    - 部分进展: 局部发现给出部分约束 → 标记，考虑组合或分case
    - 冲突: 局部化导致丢失必要信息 → 让位给全局分析Tell
```

### 3.3 完整生产级字段集

在最小充分字段集基础上，添加重要补充字段：

```yaml
TellCore_production:
  # ...（包含最小充分字段集的全部内容）
  parameter_slots:
    - p: 局部化的目标素数
    - level: 模p 或 p-adic赋值
    - objects: 需要局部化的对象
    - target_structure: 在局部表示下寻找的结构类型  # 补充
  binding_rules:                    # 补充
    - 整除性/符号/周期性 → 模p（层次1）
    - "是p的幂"/"被p^k整除" → p-adic赋值（层次2）
    - 将所有相关对象映射到局部表示
  internal_policy:
    step1: 识别自然表示陷入困境的信号    # 补充
    step2: 分析问题条件，确定局部化目标p和层次
    step3: 将问题映射到局部表示
    step4: 在局部表示下寻找隐藏结构
    step5: 将局部发现提升为全局结论或约束
    step6: 若局部发现不完全，考虑切换层次或组合其他Tell  # 补充
  critic:                            # 补充
    - 选择的p和层次是否与问题结构匹配？
    - 局部发现是否真正对应原问题的目标？
    - 是否过早局部化导致丢失了必要信息？
    - 局部发现是否足以提升为全局结论？
  composition_contract:              # 补充
    - prerequisites: 无（可作为首步策略）
    - enables: 构造性Tell
    - conflicts_with: 实数连续性分析、纯构造性分析
    - redundant_with: 其他局部化（若不同p给出相同信息）
    - handoff_rule: 局部化给出部分约束时交给构造性Tell或case分析Tell
```

---

## 4. 通过标准验证（373号第6.4节）

### 4.1 标准1：没有源题对象泄漏

**检查**：TellCore v0的运行时字段中是否包含1631、1843、1709、1962的特定对象、符号或叙事？

- invariant_claim：使用"Z/pZ"和"Q_p"——通用数学概念，非源题特有
- trigger_boundary：使用"整除性、素性、符号、幂、周期性"——通用条件，非源题特有
- negative_boundary：使用"构造性、几何性"——通用条件
- parameter_slots：使用"p、level、objects"——通用参数名
- internal_policy：使用"局部化目标p和层次"——通用操作
- progress_model：使用"取模、p-adic赋值"——通用操作
- termination：使用"局部发现、全局结论"——通用概念

**source_branch_events**包含源题特定信息（1631的x₃≡7(mod 8)等），但这个字段不属于运行时TellCore——它是POC-1的输入，不是运行时输出。

**结论**：**PASS**。运行时TellCore没有源题对象泄漏。

---

### 4.2 标准2：至少有一个明确trigger和一个明确negative trigger

**trigger_boundary**：
1. 问题涉及整数的代数结构（整除性、素性、符号、幂、周期性）
2. 自然表示下的分析陷入困境
3. 问题中存在可以局部化的对象

**negative_boundary**：
1. 问题核心在构造性而非分析性
2. 问题核心在几何结构而非代数结构
3. 问题已经在局部表示下
4. 问题在自然表示下有直接解法
5. 问题的核心困难在搜索空间大小而非结构隐藏

**结论**：**PASS**。有3条正触发条件和5条负触发条件，全部明确可操作。

---

### 4.3 标准3：参数槽可以绑定到新题对象

**验证**：用CasePack中的变形题验证参数槽绑定：

| 变形题 | p绑定到 | level绑定到 | objects绑定到 | 绑定成功？ |
|---|---|---|---|---|
| CC-009(1631变体,底数3) | 待定（需要分析3的剩余理论） | 模p（层次1） | x_n序列 | 是 |
| CC-010(1843变体,n=2022) | 待定（可能模6而非模4） | 模p（层次1） | 线性因子集合 | 是 |
| CC-011(1709变体,p=3) | 3 | p-adic赋值（层次2） | s(k)序列 | 是 |
| CC-012(1962变体,p=3) | 3 | p-adic赋值（层次2） | (a,b,c)三元组 | 是 |

**关键发现**：CC-009和CC-010的p绑定不是机械的——CC-009需要分析底数3的剩余理论来确定模数，CC-010需要识别n=2022不是4的倍数来调整模数。这说明parameter_slots的绑定需要binding_rules的辅助。

**结论**：**PASS（有条件）**。参数槽可以绑定到新题对象，但p的绑定需要binding_rules辅助。最小充分字段集中的parameter_slots(p+level+objects)足够声明参数，但准确绑定需要重要补充中的binding_rules。

---

### 4.4 标准4：internal policy不是一句口号

**检查**：internal_policy是否只是一句"切换到局部表示"的口号？

**最小充分集的internal_policy**（step2-5）：
- step2：分析问题条件，确定局部化目标p和层次
- step3：将问题映射到局部表示
- step4：在局部表示下寻找隐藏结构
- step5：将局部发现提升为全局结论或约束

每一步都是具体操作，不是口号。对比1962在tree组的失败——tree组给的Tell是"切换到p-adic赋值"（一句话口号），AI无法完成。TellCore v0的step2-5将这句话分解为4个具体操作。

**关键验证**：用1962验证internal_policy的充分性：

```text
1962的tree组Tell（口号版）：
  "切换到p-adic赋值"
  → AI尝试了但无法收敛 → 失败

1962的TellCore v0 Tell（操作路径版）：
  step2: 确定p=2，level=p-adic赋值（因为"是2的幂"条件）
  step3: 对a,b,c计算v_2，将ab-c=2^u等映射为v_2(ab-c)=u
  step4: 利用v_2(ab)=v_2(a)+v_2(b)等性质建立v_2方程
  step5: 从v_2约束反推(a,b,c)的结构
  → 预期AI可以执行 → 待POC-3验证
```

**结论**：**PASS（待经验验证）**。internal_policy不是口号，是4步操作路径。但"操作路径是否足够"需要POC-3经验验证——POC-1只能验证结构完整性，不能验证经验有效性。

---

### 4.5 标准5：progress model能预测可观察中间信号

**检查**：progress_model的4个信号是否在thinking中可观察？

| 信号 | 可观察性 | 在哪些题中可观察 |
|---|---|---|
| 信号1："取模"或"p-adic赋值" | 高——AI在thinking中会明确讨论"取模"或"v_p" | 1631/1843/1709/1962的tree组proof中均可见 |
| 信号2：发现隐藏结构 | 中-高——AI会发现"整除关系""周期性""符号配对" | 1631的Euler准则、1843的符号配对 |
| 信号3：与原问题建立联系 | 中——AI会将模p发现转化为原问题的约束 | 1631的"x₃\|y₂" |
| 信号4：提升为全局结论 | 中——AI会从局部发现推导最终结论 | 1631的"y₂合数，矛盾" |

**结论**：**PASS**。4个信号在thinking中可观察，且在历史VMS实验中有先例。

---

### 4.6 标准6：termination能说明何时停止或让位

**检查**：termination的4个条件是否覆盖所有场景？

| 条件 | 对应场景 | 在CasePack中的测试题 |
|---|---|---|
| 成功 | 局部发现解决原问题 | CC-001/002/003（source trace成功案例） |
| 无进展 | 尝试多个p后未发现结构 | CC-018（边界——p-adic不适用时应退出） |
| 部分进展 | 局部发现给出部分约束 | CC-019/020（边界——部分适用） |
| 冲突 | 局部化丢失必要信息 | CC-006（几何——局部化可能不适用） |

**结论**：**PASS**。4个终止条件覆盖了成功、无进展、部分进展和冲突四种场景，且有对应的测试题。

---

### 4.7 标准7：能解释为什么假朋友不应触发

**逐题验证**：

| 假朋友题 | 不应触发的原因 | TellCore v0如何解释 | 解释成功？ |
|---|---|---|---|
| CC-013（级数收敛） | 核心在分析性（收敛性），不在代数结构 | negative_boundary: "构造性vs分析性"——收敛性是分析性 | **PASS** |
| CC-014（系数大小） | 核心在系数大小（组合/分析），不在符号配对 | trigger_boundary: "整除性/符号/周期性"——系数大小不在此列 | **PARTIAL**——trigger可能误触发（多项式涉及符号），需要critic拦截 |
| CC-015（构造性组合） | 核心在构造性，不在分析性 | negative_boundary: "构造性而非分析性" | **PASS** |
| CC-016（组合计数） | 核心在计数（搜索空间），不在结构隐藏 | negative_boundary: "搜索空间大小而非结构隐藏" | **PASS** |
| CC-017（代数几何诱饵） | f≡g，方程恒成立，无分析必要 | trigger可能误触发（多项式方程），需要critic: "是否过早局部化" | **PARTIAL**——trigger可能误触发，需要critic拦截 |

**关键发现**：CC-014和CC-017的假朋友拒绝不能仅靠trigger_boundary和negative_boundary——需要critic的协同。

- CC-014：trigger会触发（多项式涉及符号），但critic的"局部发现是否真正对应原问题的目标？"可以拦截——系数大小不是局部表示下的隐藏结构。
- CC-017：trigger会触发（多项式方程），但critic的"是否过早局部化导致丢失了必要信息？"可以拦截——f≡g意味着没有需要局部化的对象。

**结论**：**PASS（有条件）**。5道假朋友题中3道可以仅靠trigger/negative_boundary拒绝，2道需要critic协同。这说明：
1. 最小充分字段集可以处理大部分假朋友
2. 完整生产级字段集（含critic）可以处理全部假朋友
3. selector设计时需要考虑critic的拦截能力

---

## 5. 信息泄漏审查

### 5.1 逐字段审查

| 字段 | 是否包含具体lemma | 泄漏风险 |
|---|---|---|
| invariant_claim | 否——只说"局部表示"和"隐藏结构" | low |
| trigger_boundary | 否——只说"整除性/素性/符号" | low |
| negative_boundary | 否——只说"构造性/几何性" | low |
| parameter_slots | 否——只说"p、level、objects" | low |
| binding_rules | 否——只说"整除性→模p，幂→p-adic" | low |
| internal_policy | 否——只说"映射、寻找、提升" | low |
| progress_model | 否——只说"取模、发现结构" | low |
| critic | 否——只说"p是否匹配、发现是否对应" | low |

**关键检查**：TellCore v0是否包含以下具体lemma？

| 具体lemma | 是否在TellCore中 | 说明 |
|---|---|---|
| Euler准则 | 否 | 只在source_branch_events中作为历史证据 |
| Fermat小定理 | 否 | 不在任何字段中 |
| Legendre符号 | 否 | 不在任何字段中 |
| 二次剩余判定 | 否 | 只在source_branch_events中 |
| v_2(a+b)≥min(v_2(a),v_2(b)) | 否 | internal_policy只说"建立v_p方程"，不给具体性质 |

### 5.2 泄漏审查结论

**PASS**。TellCore v0只提供策略方向和操作路径，不提供具体数学lemma。AI拿到TellCore后需要自己知道Euler准则、Fermat小定理等具体工具——TellCore只告诉AI"什么时候用这些工具"和"怎样组织这些工具的使用"，不替AI完成关键数学发现。

---

## 6. POC-1总结

### 6.1 通过标准汇总

| 通过标准 | 结果 | 说明 |
|---|---|---|
| 1. 没有源题对象泄漏 | **PASS** | 运行时字段无源题特定信息 |
| 2. 有明确trigger和negative trigger | **PASS** | 3条正触发+5条负触发 |
| 3. 参数槽可绑定到新题对象 | **PASS（有条件）** | p的绑定需要binding_rules辅助 |
| 4. internal policy不是口号 | **PASS（待经验验证）** | 4步操作路径，但需POC-3验证 |
| 5. progress model能预测信号 | **PASS** | 4个可观察信号 |
| 6. termination能说明何时停止 | **PASS** | 4个终止条件覆盖全场景 |
| 7. 能解释假朋友不应触发 | **PASS（有条件）** | 3/5仅靠trigger，2/5需要critic |

### 6.2 POC-1 verdict

```text
POC-1 因果取商：PASS（有条件）

条件1：完整生产级字段集（含binding_rules和critic）用于POC-2~POC-8
条件2：internal_policy的操作路径充分性需要POC-3经验验证
条件3：CC-014和CC-017的假朋友拒绝需要selector+critic协同设计
```

### 6.3 关键发现

1. **1962的失败是TellCore设计的核心教训**：方向Tell（"切换到p-adic"）不够，需要操作路径Tell（step2-5的系统步骤）。这是因果取商最重要的发现——从4道source trace的成败差异中提取出的因果结构。

2. **最小充分字段集是7个字段**：invariant_claim、trigger_boundary、negative_boundary、parameter_slots(p+level+objects)、internal_policy(step2-5)、progress_model、termination。这7个字段是TellCore通过六门审计的最低要求。

3. **critic是假朋友拒绝的安全网**：2/5假朋友题（CC-014/017）的拒绝需要critic协同。最小充分字段集可以处理大部分场景，但完整生产级字段集更安全。

4. **TellCore v0不泄漏具体lemma**：Euler准则、Fermat小定理等具体数学工具不在TellCore中——TellCore只提供"何时用"和"怎样组织"，不替AI完成关键发现。

### 6.4 对后续POC的要求

| 后续POC | POC-1发现的要求 |
|---|---|
| POC-2（可选择） | selector需要binding_rules辅助p的绑定；CC-014/017需要critic协同 |
| POC-3（可执行） | 必须用完整生产级字段集（含step1和step6）；必须验证1962是否可执行 |
| POC-4（可终止） | termination的4个条件需要在CC-018/019/020上验证 |
| POC-5（可组合） | composition_contract是必要字段 |
| POC-6（可归责） | progress_model的4个信号是归责依据 |
| POC-7（可持续学习） | critic的自检问题是修订起点 |

---

## 7. 下一步

### 7.1 立即可做（不需要Solver）

1. **设计selector规则**：基于trigger_boundary和negative_boundary，设计selector的匹配规则和评分函数。特别注意CC-014/017需要critic协同。
2. **设计HintRenderer模板**：基于internal_policy的step2-5，设计不同提示强度的HintInstance模板（低强度根提示、line分叉提示、method-only、method+critic、full Tell）。
3. **核验变形题解答**：对CC-009~012和CC-021~022的解答做完整数学验证。

### 7.2 需要Solver后做

1. **POC-3可执行验证**：用完整生产级字段集在CC-001~004上测试HintInstance，验证internal_policy的操作路径是否足够（特别是1962）。
2. **bare验证**：CC-008和CC-009~012的bare测试。

### 7.3 POC-1产出的EvidenceRecord

```yaml
EvidenceRecord_POC1:
  poc_id: POC-1
  target_type: TellCore
  target_component: TellCore v0 Candidate C (局部-全局表示切换)
  intervention: 字段消融分析（12字段逐项消融）
  controls: 382号CasePack v0中的22道题作为验证集
  observations:
    - 最小充分字段集为7个字段
    - 1962的失败指向internal_policy的必要性（方向vs操作路径）
    - CC-014/017的假朋友拒绝需要critic协同
    - TellCore v0不泄漏具体lemma
  supports:
    - TellCore v0候选C具备策略结构（通过7项标准）
    - TellCore v0的因果结构来自4道source trace的成败差异
  contradicts: 无
  alternative_explanations:
    - internal_policy的操作路径充分性未经经验验证（需POC-3）
    - 参数槽绑定的准确性未经经验验证（需POC-2）
  leakage_risk: low
  confidence: medium-high
  scope_limit: |
    POC-1只验证TellCore的结构完整性，不验证经验有效性。
    经验有效性需要POC-2~POC-8在Solver上验证。
  follow_up:
    - POC-2：用selector测试trigger/negative_boundary的区分能力
    - POC-3：用HintInstance测试internal_policy的操作路径充分性
```

---

## 8. 读完后要记住的六句话

1. POC-1因果取商PASS（有条件）——TellCore v0候选C具备策略结构。
2. 最小充分字段集是7个字段——invariant_claim、trigger_boundary、negative_boundary、parameter_slots、internal_policy(step2-5)、progress_model、termination。
3. 1962的失败是核心教训——方向Tell不够，需要操作路径Tell。
4. 2/5假朋友题需要critic协同拒绝——selector设计时必须考虑critic拦截能力。
5. TellCore v0不泄漏具体lemma——只提供"何时用"和"怎样组织"，不替AI完成关键发现。
6. POC-1只验证结构完整性，经验有效性需要POC-2~POC-8在Solver上验证。
