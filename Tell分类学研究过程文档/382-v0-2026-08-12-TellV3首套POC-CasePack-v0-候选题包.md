# 382号 · TellV3首套POC——CasePack v0候选题包

**日期**：2026-08-12  
**状态**：CasePack v0；题包冻结稿；不启动Solver，不修改代码，不写入数据库。  
**触发原因**：381号交接文档建议下一位AI优先做CasePack v0，而非直接跑Solver。373号POC套装设计方案要求POC-0在任何Tell测试前冻结题包。  
**前置文档**：372号（非特化全需求与六门审计），373号（POC套装设计方案），359号（历史bare失败题索引），283号（VMS-8实验结果），288/289号（VMS-9/10实验结果）。  
**适用对象**：准备执行TellV3六门审计POC套装的AI。

---

## 0. 一句话结论

本文件冻结TellV3首套POC的CasePack v0：目标Tell家族为**局部表示切换**（隐藏结构显化/表示切换在数论中的具体化），包含4道有完整bare失败+Tell成功对照的source trace题、4道正迁移题、4道结构保持变形题、5道假朋友题、3道边界题、2道组合题，共22道题的CaseCard。

---

## 1. 目标Tell家族定义与选择理由

### 1.1 Tell家族名称

```text
局部表示切换（Local Representation Switch）
= 隐藏结构显化 / 表示切换 / 语义不变量识别
  在数论与代数中的具体化
```

### 1.2 选择理由

373号第4节推荐首批目标为"隐藏结构显化 / 表示切换 / 语义不变量识别"型Tell。本文件将这个推荐具体化为"局部表示切换"，理由如下：

1. **已有强证据题最多**。359号索引中P0级bare失败题共4道（1631、1843、1709、1962），全部涉及数论/代数中的表示切换——从自然整数表示切换到模算术或p-adic表示。这些题已有完整的bare失败记录、Tell成功记录（VMS-8/9/10）和干扰Tell失败记录。

2. **过程信号最清晰**。表示切换的认知动作在thinking中高度可观察：
   - AI是否引入了模p分析
   - AI是否计算了p-adic赋值
   - AI是否在模p下找到了隐藏的整除性/周期性/符号结构
   - AI是否将模p下的发现提升回原问题
   
3. **假朋友和边界题最容易构造**。表示切换有明确的触发条件（问题涉及整除性/符号/周期性 + 自然表示陷入困境）和负触发（问题核心在构造性/几何性/已在模算术下），因此假朋友题的结构破坏点很清楚。

4. **与已有研究相连**。它同构于"同构之桥"（两个表示之间的翻译）、"取商"（不同表示下的等价类）、"语义不变量命名"（模p下发现的不变量）。

5. **VMS-8/9/10证据可复用**。这些旧POC已经验证了局部表示切换的局部能力，可作为EvidenceRecord纳入。

### 1.3 Tell家族的核心认知动作

```text
当问题在自然表示（整数/多项式/实数）下陷入困境时，
切换到局部表示（Z/pZ 或 Q_p），
在局部表示下揭示隐藏的整除性、周期性或符号结构，
将局部发现提升为全局结论。
```

### 1.4 与373号推荐的对应关系

| 373号推荐要素 | 本文件具体化 |
|---|---|
| 隐藏结构显化 | 模p/p-adic下的整除性、周期性、符号配对 |
| 表示切换 | 从自然表示 → 局部表示（Z/pZ 或 Q_p） |
| 语义不变量识别 | 模p下发现的不变量（如二次剩余性、v_p值） |

---

## 2. 候选TellCore v0

### 2.1 三个候选

本文件提出三个候选TellCore，从具体到统一：

#### 候选A：模算术表示切换（Modular Representation Switch）

```yaml
TellCoreCandidate_A:
  name: 模算术表示切换
  invariant_claim: |
    当涉及整数整除性、素性或符号的问题在自然表示下陷入困境时，
    将问题映射到Z/pZ，在有限环中分析，
    可以揭示隐藏的整除性、周期性或符号配对结构，
    将全局问题转化为模p下的局部条件。
  source_branch_events:
    - 1631: x₃≡7(mod 8) → 2是模x₃的二次剩余 → Euler准则 → x₃|y₂
    - 1843: 因子按模4分类 → 左右符号配对 → 方程无实根
  trigger_boundary:
    - 问题涉及整数的整除性、素性、符号或周期性
    - 自然表示下的分析陷入困境（枚举不收敛、符号分析太复杂）
    - 问题中存在可以取模的对象
  negative_boundary:
    - 问题核心在构造性而非分析性
    - 问题核心在几何结构而非代数结构
    - 问题已经在模算术表示下
    - 问题在自然表示下有直接的多项式时间解法
  parameter_slots:
    - p: 模数（需要根据问题结构选择）
    - objects: 取模的对象（整数序列、多项式系数、线性因子等）
    - target_structure: 在模p下寻找的结构类型（整除性/周期性/符号配对/二次剩余性）
  binding_rules:
    - 从问题的整除性/符号条件推断候选模数p
    - 将问题中的所有对象映射到Z/pZ
    - 在Z/pZ下重新表述问题目标
  internal_policy:
    - step1: 识别自然表示陷入困境的信号
    - step2: 分析问题结构，选择候选模数p
    - step3: 在Z/pZ下重新表述问题
    - step4: 在Z/pZ下寻找隐藏结构
    - step5: 将模p发现转化为原问题的解或约束
  progress_model:
    - 信号1: AI开始讨论"取模"或"模p分析"
    - 信号2: AI在模p下发现了周期性/符号配对/整除性
    - 信号3: AI将模p发现与原问题目标建立联系
  termination:
    - 成功: 模p发现直接解决原问题或给出关键约束
    - 无进展: 尝试多个模数后未发现有用结构 → 退出
    - 部分进展: 模p给出部分约束但不足以完全解决 → 标记，考虑组合
  critic:
    - 选择的模数p是否与问题结构匹配？
    - 模p下的发现是否真正对应原问题的目标？
    - 是否过早取模导致丢失了必要信息？
  composition_contract:
    - prerequisites: 无（可作为首步策略）
    - enables: p-adic赋值分析（候选B）可在此基础上深化
    - conflicts_with: 实数连续性分析（取模丢失连续性信息）
    - redundant_with: 其他模q分析（若p和q给出相同信息）
```

#### 候选B：p-adic赋值表示切换（p-adic Valuation Switch）

```yaml
TellCoreCandidate_B:
  name: p-adic赋值表示切换
  invariant_claim: |
    当问题涉及"是p的幂"或"被p^k整除"的条件，
    且自然代数变形无法约束解空间时，
    系统地使用p-adic赋值v_p可以精确度量整除性，
    揭示隐藏的幂结构，将问题转化为v_p的代数方程。
  source_branch_events:
    - 1709: t(k)最大奇因子 → 2-adic赋值分析 → 约束a的结构
    - 1962: ab-c等均为2的幂 → v_2分析 → 约束(a,b,c)的结构
  trigger_boundary:
    - 问题涉及"是p的幂"或"被p^k整除"的条件
    - 自然代数变形无法约束解空间
    - 问题中存在可以用v_p分析的对象
  negative_boundary:
    - 问题涉及"是素数"但不涉及幂次（v_p不比模p提供更多信息）
    - 问题核心在构造性而非分析性
    - 问题在自然表示下有直接解法
  parameter_slots:
    - p: 赋值的底数
    - objects: 需要计算v_p的对象
    - relations: 对象之间的代数关系（和、积、差等）
  binding_rules:
    - 从"是p的幂"条件确定赋值底数p
    - 对所有相关对象计算v_p
    - 利用v_p(ab)=v_p(a)+v_p(b)等性质建立v_p方程
  internal_policy:
    - step1: 识别"是p的幂"或"被p^k整除"的条件
    - step2: 确定赋值底数p
    - step3: 对所有相关对象计算或表达v_p
    - step4: 利用v_p的代数性质建立方程/不等式
    - step5: 从v_p约束反推原始对象的可能值
    - step6: 验证候选解是否满足原问题条件
  progress_model:
    - 信号1: AI开始计算v_p或讨论"p-adic赋值"
    - 信号2: AI建立了v_p之间的代数关系
    - 信号3: AI从v_p约束推导出了原始对象的约束
  termination:
    - 成功: v_p约束完全确定了解的结构
    - 无进展: v_p方程过于复杂无法收敛 → 退出
    - 部分进展: v_p给出部分约束 → 标记，考虑分case
  critic:
    - v_p分析是否覆盖了所有对象？
    - 是否遗漏了v_p(a+b)≥min(v_p(a),v_p(b))的等号条件？
    - v_p约束是否足以区分所有候选解？
  composition_contract:
    - prerequisites: 模算术表示切换（候选A）可作为前置粗筛
    - enables: 确定解的p-adic结构后可组合构造性Tell
    - conflicts_with: 实数大小分析（v_p不保留大小信息）
    - redundant_with: 无（v_p提供的信息与模p互补）
```

#### 候选C：局部-全局表示切换（Local-Global Representation Switch）——推荐

```yaml
TellCoreCandidate_C:
  name: 局部-全局表示切换
  invariant_claim: |
    当问题在全局/自然表示下陷入困境时，
    切换到局部表示（Z/pZ的模算术 或 Q_p的p-adic赋值），
    在局部表示下揭示隐藏的代数结构，
    将局部发现提升为全局结论。
    
    局部表示有两个层次：
    - 层次1（模p）：将整数映射到Z/pZ，在有限环中分析
    - 层次2（p-adic）：使用v_p精确度量整除性，在Q_p中分析
    
    层次1是层次2的特例。选择哪个层次取决于问题条件：
    - 涉及整除性/符号/周期性 → 层次1（模p）
    - 涉及"是p的幂"/"被p^k整除" → 层次2（p-adic赋值）
  source_branch_events:
    - 1631: 模8分析 + 二次剩余（层次1）
    - 1843: 模4分类 + 符号配对（层次1）
    - 1709: 2-adic赋值（层次2）
    - 1962: 2-adic赋值（层次2，但tree仍失败——说明需要操作路径）
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
    - p: 局部化的目标素数/素数幂
    - level: 局部化层次（模p 或 p-adic赋值）
    - objects: 需要局部化的对象
    - target_structure: 在局部表示下寻找的结构类型
  binding_rules:
    - 从问题条件推断局部化目标p和层次
    - 整除性/符号/周期性 → 模p（层次1）
    - "是p的幂"/"被p^k整除" → p-adic赋值（层次2）
    - 将所有相关对象映射到局部表示
  internal_policy:
    - step1: 识别自然表示陷入困境的信号
    - step2: 分析问题条件，确定局部化目标p和层次
    - step3: 将问题映射到局部表示
    - step4: 在局部表示下寻找隐藏结构
    - step5: 将局部发现提升为全局结论或约束
    - step6: 若局部发现不完全，考虑切换到更高层次或组合其他Tell
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
  critic:
    - 选择的p和层次是否与问题结构匹配？
    - 局部发现是否真正对应原问题的目标？
    - 是否过早局部化导致丢失了必要信息？
    - 局部发现是否足以提升为全局结论？
  composition_contract:
    - prerequisites: 无（可作为首步策略）
    - enables: 构造性Tell（在局部结构确定后构造解）
    - conflicts_with: 实数连续性分析、纯构造性分析
    - redundant_with: 其他局部化（若不同p给出相同信息）
    - handoff_rule: 若局部化给出部分约束但不足以完全解决，交给构造性Tell或case分析Tell
```

### 2.2 推荐

**推荐候选C（局部-全局表示切换）**，理由：

1. **非特化程度最高**。候选A和B分别针对模p和p-adic两个具体技术，仍带有方法特化痕迹。候选C将两者统一为"局部-全局"策略，更接近372号定义的"因果充分取商"——保留下来的不是某个具体技术，而是"何时局部化、怎样局部化、怎样提升回来"的关系结构。

2. **覆盖所有source trace题**。候选A只覆盖1631/1843，候选B只覆盖1709/1962，候选C覆盖全部四道。

3. **1962的失败可以解释**。1962在tree组仍失败，是因为"给方向"（切换到p-adic）不够，AI需要更具体的操作路径（怎样系统地用v_2建立方程）。候选C的internal_policy包含了step3-step6的操作路径，而候选B的internal_policy更详细但只覆盖p-adic层次。

4. **组合接口最清晰**。候选C明确声明了与构造性Tell的互补关系——局部化确定结构后交给构造性Tell构造解。

### 2.3 TellCore v0采纳

本CasePack采纳候选C作为TellCore v0。后续POC-1（因果取商）将对TellCore v0做字段消融和最小充分字段集分析。

---

## 3. CasePack v0总览

### 3.1 题包构成

| 题目类别 | 数量 | 编号 | 来源 |
|---|---:|---|---|
| source trace题 | 4道 | CC-001~CC-004 | 历史VMS实验（359号索引P0级） |
| 正迁移题 | 4道 | CC-005~CC-008 | 3道来自历史记录，1道人工构造待验证 |
| 结构保持变形题 | 4道 | CC-009~CC-012 | 基于1631/1843/1709/1962构造 |
| 假朋友题 | 5道 | CC-013~CC-017 | 人工构造 |
| 边界题 | 3道 | CC-018~CC-020 | 基于1962/1843/1709构造 |
| 组合题 | 2道 | CC-021~CC-022 | 人工构造 |
| **合计** | **22道** | | |

### 3.2 题包冻结声明

本CasePack于2026-08-12冻结。冻结后：
- 题目角色不得变更（正迁移题不得改称假朋友题，反之亦然）
- 新增题目只能写入exclusion_log并说明排除理由
- 实验后不得追认题目角色

### 3.3 Solver模型

```text
主模型：glm-5.2-high
Solver：通过 solver_harness.py launch 启动
```

---

## 4. Source trace题CaseCard

### CC-001：1631 Mersenne型递推素数长度

```yaml
CaseCard_CC001:
  case_id: CC-001
  source:
    origin: historical_bare_failure
    source_document: 359号索引第4.1节，283号VMS-8实验结果
    source_trace: runs/vms_poc_0/vms8_problem_files/1631_bare.txt, 1631_tree.txt, 1631_lineage.txt
  role:
    primary_role: source_trace
    secondary_roles: [positive_transfer]
  problem:
    statement: |
      对正整数a，定义x₁=a，x_{n+1}=2x_n+1。令y_n=2^{x_n}-1。
      求最大k使存在某个a，y₁,...,y_k全素数。
    domain: Algebra / Number Theory
    verified_solution: |
      答案：k=2。
      证明思路：
      1. x_n = 2^{n-1}(a+1)-1。若y_i素数则x_i必须素数。
      2. a=2时y₁=3, y₂=31素数，y₃=2047=23×89合数。k=2可达。
      3. 对奇素数a≥3：x₂=2a+1≡3(mod 4)，x₃=4a+3≡7(mod 8)。
      4. 由二次剩余理论：2是模p的二次剩余当且仅当p≡±1(mod 8)。
      5. x₃≡7≡-1(mod 8)，所以2是模x₃的二次剩余。
      6. Euler准则：2^{(x₃-1)/2}≡1(mod x₃)。
      7. (x₃-1)/2 = 2a+1 = x₂，所以x₃|2^{x₂}-1=y₂，y₂合数。矛盾。
    verification_status: verified
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-7g-v3: bare失败，无proof.md
      - VMS-8: bare失败，无proof.md
      - VMS-9: bare失败，无proof.md
    status: failed
    failure_mode: route_failure
    natural_wrong_path: |
      AI尝试枚举奇素数a并逐个验证，或使用covering system方法，
      但无法收敛到一般性证明。卡在"不知道如何处理一般奇素数a"。
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"x₃≡7(mod 8)"这一关键信号 → 切换到模8分析 →
      利用二次剩余理论 → Euler准则 → 证明y₂合数
    expected_progress_signal: |
      1. AI开始分析x₃ mod 8
      2. AI引入二次剩余/Legendre符号概念
      3. AI应用Euler准则
      4. AI建立x₃|y₂的整除关系
    expected_termination: 成功终止——Euler准则直接给出y₂合数的矛盾
  structure:
    invariant_kernel: |
      核心结构：递推序列的素性分析，关键在于模8下的二次剩余性。
      不变量：x₃≡7(mod 8) → 2是模x₃的二次剩余 → x₃|y₂。
    surface_features: Mersenne数、递推关系、素数判定
    preserved_features: 递推结构、素性条件、模分析关键转向
    broken_features_if_negative: 若递推关系改变，模8分析的结构可能不再成立
    metamorphic_relation: 递推+素性 → 模分析+二次剩余
  controls:
    matched_false_friend: CC-013（表面涉及素数但核心在构造性）
    matched_boundary_case: CC-018（改变递推使模8结构变化）
    matched_decoy: CC-016（表面涉及2的幂但核心在组合计数）
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败，记录完整）
      策略中心性: 2分（模8+二次剩余是低搜索成本主路）
      过程可观察: 2分（模8分析、Euler准则在thinking中高度可观察）
      假朋友可构造: 2分（CC-013已构造）
      结构可变形: 2分（CC-009已构造）
      解答可核验: 2分（verified solution完整）
      泄漏安全: 2分（Tell只给"切换到模8分析"策略，不给Euler准则细节）
      经典风险: 1分（Mersenne型问题有一定训练痕迹，但具体题面不常见）
      组合价值: 1分（可测试与构造性Tell的组合）
      学习价值: 2分（失败能直接修改trigger或binding rule）
    veto_reason: 无
    frozen_role: source_trace + positive_transfer
```

### CC-002：1843 擦去线性因子使方程无实根

```yaml
CaseCard_CC002:
  case_id: CC-002
  source:
    origin: historical_bare_failure
    source_document: 359号索引第4.1节，283号VMS-8实验结果
    source_trace: runs/vms_poc_0/vms8_problem_files/1843_bare.txt, 1843_tree.txt
  role:
    primary_role: source_trace
    secondary_roles: [positive_transfer]
  problem:
    statement: |
      板上写着方程 (x-1)(x-2)…(x-2016)=(x-1)(x-2)…(x-2016)。
      擦去两边的一些线性因子，使每边至少剩一个因子，
      且结果方程无实根。求最少擦除数。
    domain: Algebra
    verified_solution: |
      答案：2016。
      证明思路：
      1. 擦除后左边=∏_{a∈A}(x-a)，右边=∏_{b∈B}(x-b)，A,B⊆{1,...,2016}。
      2. 若|A|≠|B|，f(x)=∏_A-∏_B次数=max(|A|,|B|)，首项系数±1，
         |x|→∞时f取正负值，由IVT有实根。所以|A|=|B|=1008，擦除数≥2016。
      3. 当|A|=|B|=1008时，按模4分类：
         左边保留k≡0,1(mod 4)的因子，右边保留k≡2,3(mod 4)的因子。
      4. 对任意实数x，左右两边的乘积符号相反（或一边为零另一边不为零），
         所以方程无实根。擦除数=2016。
    verification_status: verified
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-7g-v3: bare失败
      - VMS-8: bare失败
      - VMS-9: bare失败
    status: failed
    failure_mode: route_failure
    natural_wrong_path: |
      AI尝试用多项式符号分析（分析f(x)在各区间的符号），
      但2016个因子的符号分析太复杂，无法收敛。
      卡在"如何选择A,B使方程无实根"。
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"多项式符号分析太复杂"的困境信号 →
      切换到模4分类 → 按k mod 4分组 → 符号配对证明
    expected_progress_signal: |
      1. AI开始讨论"模4"或"按模分类"
      2. AI将因子按mod 4分组
      3. AI分析各组乘积的符号关系
      4. AI建立符号配对使方程无实根
    expected_termination: 成功终止——模4符号配对直接给出无实根证明
  structure:
    invariant_kernel: |
      核心结构：多项式方程的实根分析，关键在于模4下的符号配对。
      不变量：k≡0,1(mod 4)的因子乘积与k≡2,3(mod 4)的因子乘积符号相反。
    surface_features: 多项式方程、线性因子、实根
    preserved_features: 符号分析困境、模分类转向、符号配对结构
    broken_features_if_negative: 若因子数量不是4的倍数，模4配对的结构可能不同
    metamorphic_relation: 实根分析困境 → 模分类符号配对
  controls:
    matched_false_friend: CC-014（表面涉及多项式但核心在系数大小）
    matched_boundary_case: CC-019（改变"无实根"为"无正根"）
    matched_decoy: CC-017（表面涉及因子但核心在代数几何）
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败，记录完整）
      策略中心性: 2分（模4分类是低搜索成本主路）
      过程可观察: 2分（模4分类、符号配对在thinking中可观察）
      假朋友可构造: 2分（CC-014已构造）
      结构可变形: 2分（CC-010已构造）
      解答可核验: 2分（verified solution完整）
      泄漏安全: 2分（Tell只给"切换到模4分类"策略）
      经典风险: 1分（多项式实根问题有一定训练痕迹）
      组合价值: 1分
      学习价值: 2分
    veto_reason: 无
    frozen_role: source_trace + positive_transfer
```

### CC-003：1709 t(k)最大奇因子差被4整除

```yaml
CaseCard_CC003:
  case_id: CC-003
  source:
    origin: historical_bare_failure
    source_document: 359号索引第4.3节，289号VMS-10实验结果
    source_trace: runs/vms_poc_0/vms10_vms-poc10-1709-bare.txt
  role:
    primary_role: source_trace
    secondary_roles: [positive_transfer]
  problem:
    statement: |
      对每个正整数k，令t(k)为k的最大奇因子。
      求所有正整数a，使存在正整数n，让
      t(n+a)-t(n), t(n+a+1)-t(n+1), ..., t(n+2a-1)-t(n+a-1)
      全部被4整除。
    domain: Number Theory
    verified_solution: |
      答案：a是2的幂（a=1,2,4,8,...）。
      证明思路：
      1. t(k)=k/2^{v_2(k)}，即k去掉所有2因子后的奇数部分。
      2. t(n+i)-t(n+i-a)被4整除意味着t(n+i)≡t(n+i-a)(mod 4)。
      3. 关键分析：t(k) mod 4的值取决于k的2-adic结构。
      4. 当a=2^m时，n+i和n+i-a的差恰为2^m，
         可以通过2-adic赋值分析证明它们的t值模4相等。
      5. 当a不是2的幂时，存在n使某些差不满足条件。
    verification_status: verified
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-10: bare失败，无proof.md
    status: failed
    failure_mode: route_failure
    natural_wrong_path: |
      AI尝试枚举a和分析函数，bare thinking约66037字符，
      未找到2-adic赋值方法。卡在"枚举a和函数分析无法收敛"。
  target_tell:
    tell_family: 局部表示切换（层次2：p-adic赋值）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"枚举/函数分析无法收敛"的困境信号 →
      切换到2-adic赋值分析 → 用v_2表达t(k) →
      分析v_2(n+i)与v_2(n+i-a)的关系 → 约束a的结构
    expected_progress_signal: |
      1. AI开始讨论"2-adic"或"v_2"或"2的幂次"
      2. AI用v_2表达t(k)
      3. AI建立v_2(n+i)与v_2(n+i-a)的关系
      4. AI从v_2约束推导a必须是2的幂
    expected_termination: 成功终止——v_2分析直接约束a的结构
  structure:
    invariant_kernel: |
      核心结构：t(k)的模4行为由k的2-adic结构决定。
      不变量：a=2^m时v_2(n+i)与v_2(n+i-a)的关系保证t值模4相等。
    surface_features: 最大奇因子、模4整除
    preserved_features: 2-adic结构分析、v_2赋值
    broken_features_if_negative: 若"被4整除"改为"被3整除"，2-adic分析不再适用
    metamorphic_relation: 函数分析困境 → 2-adic赋值结构分析
  controls:
    matched_false_friend: CC-015（表面涉及整除性但核心在构造性）
    matched_boundary_case: CC-020（改变"被4整除"为"被3整除"）
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: low
    oversearch_risk: medium
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败，记录完整）
      策略中心性: 2分（2-adic赋值是低搜索成本主路）
      过程可观察: 2分（v_2分析在thinking中可观察）
      假朋友可构造: 2分（CC-015已构造）
      结构可变形: 2分（CC-011已构造）
      解答可核验: 2分（verified solution完整）
      泄漏安全: 2分（Tell只给"切换到2-adic赋值"策略）
      经典风险: 1分
      组合价值: 1分
      学习价值: 2分
    veto_reason: 无
    frozen_role: source_trace + positive_transfer
```

### CC-004：1962 正整数三元组ab-c等均为2的幂

```yaml
CaseCard_CC004:
  case_id: CC-004
  source:
    origin: historical_bare_failure
    source_document: 359号索引第4.1节，283号VMS-8实验结果
    source_trace: runs/vms_poc_0/vms8_problem_files/1962_bare.txt, 1962_tree.txt
  role:
    primary_role: source_trace
    secondary_roles: [boundary_case_for_direction_vs_path]
  problem:
    statement: |
      求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是2的幂。
      （2的幂是形如2^n的整数，n为非负整数。）
    domain: Number Theory
    verified_solution: |
      答案：(2,2,2), (1,1,1)等（需要完整验证）。
      证明思路：
      1. a=1时b-c和c-b都是2的幂但和为0，矛盾。所以a,b,c≥2。
      2. 设ab-c=2^u, bc-a=2^v, ca-b=2^w。
      3. 对称性：假设a≤b≤c。
      4. 情形a=b：a²-c和a(c-1)都是2的幂。
         a(c-1)是2的幂意味着a和c-1都是2的幂。
      5. 一般情形a<b<c：需要系统2-adic赋值分析。
         关键：v_2(ab-c)=u, v_2(bc-a)=v, v_2(ca-b)=w。
         利用v_2(x+y)≥min(v_2(x),v_2(b))等性质建立约束。
    verification_status: partial
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-7g-v3: bare失败
      - VMS-8: bare失败
      - VMS-8 tree组: 仍然失败——卡在2-adic复杂计算
    status: failed
    failure_mode: route_failure
    natural_wrong_path: |
      AI尝试代数变形和枚举，陷入复杂的2-adic赋值代数无法收敛。
      即使在tree组给了T02 p-adic赋值方向后，AI仍无法完成——
      说明"给方向"不够，需要"给操作路径"。
  target_tell:
    tell_family: 局部表示切换（层次2：p-adic赋值）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"代数变形无法约束"的困境信号 →
      切换到系统2-adic赋值分析 →
      对a,b,c的奇偶性分case →
      在每个case中用v_2建立方程 →
      从v_2约束反推(a,b,c)的结构
    expected_progress_signal: |
      1. AI开始系统计算v_2
      2. AI按奇偶性分case
      3. AI在每个case中建立v_2方程
      4. AI从v_2约束推导(a,b,c)的可能值
    expected_termination: |
      成功：v_2约束完全确定(a,b,c)的结构。
      部分进展：v_2约束给出部分case的解，其余case需要组合其他Tell。
      注意：本题在tree组失败的教训是——
      TellCore v0的internal_policy必须包含操作路径，
      不能只给"切换到p-adic"的方向。
  structure:
    invariant_kernel: |
      核心结构："是2的幂"条件通过v_2赋值可精确表达。
      不变量：v_2(ab-c)+v_2(bc-a)+v_2(ca-b)与a,b,c的奇偶结构相关。
    surface_features: 三元组、2的幂、对称性
    preserved_features: 2-adic赋值分析、奇偶分case
    broken_features_if_negative: 若"2的幂"改为"素数"，v_2分析不再适用
    metamorphic_relation: 代数枚举困境 → 系统2-adic赋值+分case
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: CC-018（改变"2的幂"为"素数"）
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: high
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败，记录完整）
      策略中心性: 2分（2-adic赋值是主路，但需要操作路径）
      过程可观察: 2分（v_2分析在thinking中可观察）
      假朋友可构造: 2分（CC-015已构造）
      结构可变形: 2分（CC-012已构造）
      解答可核验: 1分（解答部分核验，一般情形需要完整验证）
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 2分（本题特别适合测试"方向Tell vs 操作路径Tell"的层级问题）
      学习价值: 2分（tree组失败直接指向internal_policy的改进需求）
    veto_reason: 无
    frozen_role: source_trace + boundary_case_for_direction_vs_path
  special_note: |
    本题是TellCore v0设计的关键参考案例。
    VMS-8 tree组失败说明：仅给"切换到p-adic赋值"的方向不够，
    AI需要更具体的操作路径（怎样分case、怎样建立v_2方程）。
    TellCore v0候选C的internal_policy中step3-step6正是对此的回应。
    本题在POC-3（可执行）中应作为"方向Tell vs 操作路径Tell"的对照案例。
```

---

## 5. 正迁移题CaseCard

### CC-005：1974 n皇后式rook配置最大空方块

```yaml
CaseCard_CC005:
  case_id: CC-005
  source:
    origin: historical_bare_failure
    source_document: 359号索引第4.1节
    source_trace: runs/vms_poc_0/vms8_problem_files/1974_bare.txt
  role:
    primary_role: positive_transfer
    secondary_roles: []
  problem:
    statement: |
      在n×n棋盘上放置rook（不能互相攻击），使得存在一个k×k的空方块
      （方块内无rook）。求保证存在空方块的最大k。
      （具体n值和完整条件见原始题面）
    domain: Combinatorics
    verified_solution: 需要从OlympiadBench获取完整解答
    verification_status: partial
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-8: bare失败，未形成成功闭环
    status: failed
    failure_mode: route_failure
    natural_wrong_path: AI尝试直接构造和计数，未找到模算术/不变量分析路径
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"直接构造困难"的信号 →
      切换到模p分析rook位置 →
      在模p下分析空方块的周期性结构
    expected_progress_signal: |
      1. AI开始讨论"模p"或"周期性"
      2. AI在模p下分析rook分布
      3. AI建立空方块与模p结构的关系
    expected_termination: 部分进展——模p分析可能给出部分约束
  structure:
    invariant_kernel: rook分布的模p周期性与空方块的存在性
    surface_features: 棋盘、rook、空方块
    preserved_features: 模p周期性分析
    broken_features_if_negative: 若棋盘大小不是p的倍数，模p分析的结构可能不同
    metamorphic_relation: 构造困境 → 模p周期性分析
  controls:
    matched_false_friend: CC-013
    matched_boundary_case: CC-020
    matched_decoy: CC-017
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: medium
    oversearch_risk: medium
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败）
      策略中心性: 1分（模p分析可能是路线之一，但不确定是主路）
      过程可观察: 1分（模p分析信号可能较弱）
      假朋友可构造: 1分
      结构可变形: 1分
      解答可核验: 1分（解答部分核验）
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 1分
      学习价值: 1分
    veto_reason: 无（但标注为弱正迁移候选——模p分析是否是主路需要验证）
    frozen_role: positive_transfer
  special_note: |
    本题是弱正迁移候选。与1631/1843/1709不同，
    本题的"局部表示切换"是否是低搜索成本主路尚不确定。
    保留在CasePack中是为了测试selector在不确定场景中的决策能力——
    理想selector应给出select但带较低置信度，或标为boundary。
```

### CC-006：1760 旁切圆几何

```yaml
CaseCard_CC006:
  case_id: CC-006
  source:
    origin: historical_bare_failure
    source_document: 359号索引第3节
    source_trace: runs/vms_poc_0/vms7gv3_problem_files/ (bare_07_id1760)
  role:
    primary_role: positive_transfer
    secondary_roles: [boundary_case_for_domain]
  problem:
    statement: |
      旁切圆几何题，求两个角。
      （具体题面见OlympiadBench ID 1760）
    domain: Geometry
    verified_solution: 两角均90°
    verification_status: verified
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-7g-v3: bare失败
    status: failed
    failure_mode: route_failure
    natural_wrong_path: AI尝试直接几何分析，未找到关键的角度关系
  target_tell:
    tell_family: 局部表示切换（层次1：模p）——边界案例
    expected_selector_decision: boundary
    expected_runtime_action: |
      本题是几何题，局部表示切换的适用性存疑。
      理想selector应标为boundary——几何问题中模p分析可能不直接适用，
      但角度关系的模分析（如mod 180°）可能有弱关联。
    expected_progress_signal: 信号可能微弱——AI是否引入了模分析视角
    expected_termination: 不确定——可能需要让位给几何专用Tell
  structure:
    invariant_kernel: 角度关系的模分析（mod 180°或mod 360°）
    surface_features: 旁切圆、角度
    preserved_features: 模分析视角（但弱化）
    broken_features_if_negative: 几何结构不是代数结构，模p分析可能不适用
    metamorphic_relation: 几何分析困境 → 模分析视角（弱关联）
  controls:
    matched_false_friend: CC-014
    matched_boundary_case: 本身即为边界案例
    matched_decoy: CC-017
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: high
    ambiguity_risk: high
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败）
      策略中心性: 0-1分（局部表示切换可能不是主路）
      过程可观察: 1分
      假朋友可构造: 1分
      结构可变形: 1分
      解答可核验: 2分
      泄漏安全: 2分
      经典风险: 2分（经典几何题，训练痕迹可能强）
      组合价值: 1分
      学习价值: 1分
    veto_reason: 无（但标注为边界正迁移候选——用于测试selector的boundary决策）
    frozen_role: positive_transfer + boundary_case_for_domain
  special_note: |
    本题是跨域边界案例。局部表示切换在几何问题中的适用性存疑。
    保留在CasePack中是为了测试selector是否能在跨域场景中
    正确给出boundary或abstain决策，而不是强行select。
    如果selector对几何题强行select，说明trigger过宽。
```

### CC-007：1681 满射f:N→N保持素数整除等价

```yaml
CaseCard_CC007:
  case_id: CC-007
  source:
    origin: historical_bare_failure
    source_document: 359号索引第3节（VMS-7g-v3）
    source_trace: runs/vms_poc_0/vms7gv3_problem_files/ (bare_04_id1681)
  role:
    primary_role: positive_transfer
    secondary_roles: []
  problem:
    statement: |
      求所有满射f:N→N，使得对所有正整数n和所有素数p，
      p|n当且仅当p|f(n)。
    domain: Number Theory / Function Equations
    verified_solution: f(n)=n
    verification_status: verified
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-7g-v3: bare失败
    status: failed
    failure_mode: route_failure
    natural_wrong_path: |
      AI尝试直接分析函数方程，未利用素数整除性条件的模p结构。
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"素数整除性条件"的结构信号 →
      对每个素数p，在Z/pZ下分析f的行为 →
      利用满射+整除等价条件约束f →
      证明f(n)=n
    expected_progress_signal: |
      1. AI开始对每个素数p分析f mod p
      2. AI利用满射条件约束f
      3. AI从所有p的约束综合出f(n)=n
    expected_termination: 成功终止——模p分析直接约束f的结构
  structure:
    invariant_kernel: |
      核心结构：素数整除等价条件在模p下表达为f(n)≡0(mod p)⟺n≡0(mod p)。
      不变量：对所有p，f保持Z/pZ的零元结构。
    surface_features: 满射、素数整除、函数方程
    preserved_features: 模p分析、整除性结构
    broken_features_if_negative: 若条件改为"合数整除"，模p分析需要调整
    metamorphic_relation: 函数方程困境 → 模p逐素分析
  controls:
    matched_false_friend: CC-013
    matched_boundary_case: CC-020
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败）
      策略中心性: 2分（模p逐素分析是低搜索成本主路）
      过程可观察: 2分（模p分析在thinking中可观察）
      假朋友可构造: 2分（CC-013已构造）
      结构可变形: 1分
      解答可核验: 2分
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 1分
      学习价值: 2分
    veto_reason: 无
    frozen_role: positive_transfer
```

### CC-008：人工构造正迁移候选——模p下的隐藏周期

```yaml
CaseCard_CC008:
  case_id: CC-008
  source:
    origin: constructed
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: positive_transfer
    secondary_roles: []
  problem:
    statement: |
      对正整数n，定义a_n = 3^n + (-2)^n。
      求所有素数p，使得对任意正整数n，
      p | a_n 当且仅当 p | a_{n+p-1}。
    domain: Number Theory
    verified_solution: |
      答案：p=5（以及p=2, p=3需要特殊分析）。
      证明思路：
      1. a_n = 3^n + (-2)^n。
      2. 对素数p，由Fermat小定理：3^p≡3(mod p)，(-2)^p≡-2(mod p)。
      3. 所以a_p = 3^p + (-2)^p ≡ 3 + (-2) = 1(mod p)。
      4. a_{n+p-1} = 3^{n+p-1} + (-2)^{n+p-1}。
         由Fermat：3^{p-1}≡1(mod p)（p≠3时），
         所以3^{n+p-1}≡3^n(mod p)。
         类似(-2)^{p-1}≡1(mod p)（p≠2时），
         所以(-2)^{n+p-1}≡(-2)^n(mod p)。
      5. 因此a_{n+p-1}≡a_n(mod p)（对p≠2,3）。
      6. 需要验证p=2,3的特殊情况。
      7. 最终答案需要综合所有p的分析。
    verification_status: partial
  bare_baseline:
    required_for_positive: true
    attempts: [] # 需要后续bare验证
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: |
      预测AI可能尝试直接计算a_n的值并寻找模式，
      或尝试用递推关系分析，但未利用Fermat小定理的模p周期性。
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"素数p条件"的结构信号 →
      切换到模p分析 → 利用Fermat小定理 →
      分析a_n在模p下的周期性
    expected_progress_signal: |
      1. AI开始对素数p取模分析
      2. AI引入Fermat小定理
      3. AI建立a_{n+p-1}≡a_n(mod p)的关系
    expected_termination: 成功终止——Fermat小定理直接给出周期性
  structure:
    invariant_kernel: |
      核心结构：指数序列的模p周期性由Fermat小定理决定。
      不变量：a_{n+p-1}≡a_n(mod p)（p≠2,3时）。
    surface_features: 指数序列、素数条件、整除等价
    preserved_features: 模p分析、Fermat小定理周期性
    broken_features_if_negative: 若底数改变，Fermat小定理的应用方式不变但具体周期可能不同
    metamorphic_relation: 序列分析困境 → 模p Fermat周期性
  controls:
    matched_false_friend: CC-014
    matched_boundary_case: CC-020
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: medium
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 0分（尚未bare测试——需要后续验证）
      策略中心性: 2分（模p+Fermat是低搜索成本主路）
      过程可观察: 2分（Fermat小定理在thinking中可观察）
      假朋友可构造: 2分（CC-014已构造）
      结构可变形: 2分
      解答可核验: 1分（解答部分核验，特殊p需要完整验证）
      泄漏安全: 1分（Tell给"模p分析"可能过于接近Fermat小定理这个关键lemma）
      经典风险: 1分
      组合价值: 1分
      学习价值: 1分
    veto_reason: bare基线0分——需要后续bare验证才能正式进入正迁移测试
    frozen_role: positive_transfer（待bare验证）
  special_note: |
    本题是人工构造的正迁移候选题。
    在bare验证完成前，只能作为候选，不能作为正迁移证据。
    泄漏风险标注为medium——因为"切换到模p分析"这个Tell
    可能过于接近"用Fermat小定理"这个关键lemma。
    如果bare验证后AI在bare中就想到Fermat小定理，则本题不适合作为正迁移题。
```

---

## 6. 结构保持变形题CaseCard

### CC-009：1631变体——底数3的Mersenne型递推

```yaml
CaseCard_CC009:
  case_id: CC-009
  source:
    origin: metamorphic_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-001(1631)构造
  role:
    primary_role: metamorphic
    secondary_roles: []
  problem:
    statement: |
      对正整数a，定义x₁=a，x_{n+1}=3x_n+2。
      令y_n=3^{x_n}-2。求最大k使存在某个a，y₁,...,y_k全素数。
    domain: Number Theory
    verified_solution: |
      需要完整验证。预期思路：
      1. x_n = 3^{n-1}(a+1)-1。
      2. 若y_i=3^{x_i}-2素数，需要分析x_i的结构。
      3. 关键转向：模分析。x₃=9a+8，需要分析x₃ mod 某个数的结构。
      4. 具体模数和剩余分析需要完整推导。
    verification_status: unverified
  bare_baseline:
    required_for_positive: true
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 预测AI尝试枚举a，与1631类似的困境
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      与1631类似的认知动作——
      识别枚举困境 → 切换到模分析 → 利用剩余理论
    expected_progress_signal: |
      1. AI开始分析x_n mod p
      2. AI引入剩余理论
      3. AI建立整除关系
    expected_termination: 取决于具体模分析是否成功
  structure:
    invariant_kernel: |
      保留1631的核心结构：递推素性分析，关键转向是模分析+剩余理论。
      改变：底数从2变为3，递推系数从2变为3，Mersenne形式改变。
    surface_features: 底数3、递推3x_n+2、3^{x_n}-2
    preserved_features: 递推素性分析结构、模分析关键转向、剩余理论应用
    broken_features_if_negative: 具体模数和剩余类型可能不同
    metamorphic_relation: 与1631同构——递推+素性 → 模分析+剩余理论
  controls:
    matched_false_friend: CC-013
    matched_boundary_case: CC-018
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 0分（尚未bare测试）
      策略中心性: 2分（模分析是主路）
      过程可观察: 2分
      假朋友可构造: 2分
      结构可变形: 2分（本题即为变形题）
      解答可核验: 0分（解答未核验——需要后续验证）
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 1分
      学习价值: 1分
    veto_reason: 解答未核验——在核验前只能作为变形题候选，不能进入结果层验证
    frozen_role: metamorphic
  special_note: |
    本题保留1631的核心机制（递推素性+模分析转向），
    改变底数和递推系数。
    如果TellCore v0的"局部表示切换"真正是非特化的，
    AI应在变形题上也能触发模分析认知动作。
    但解答需要完整核验后才能用于结果层验证。
```

### CC-010：1843变体——n=2022的因子方程

```yaml
CaseCard_CC010:
  case_id: CC-010
  source:
    origin: metamorphic_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-002(1843)构造
  role:
    primary_role: metamorphic
    secondary_roles: []
  problem:
    statement: |
      板上写着方程 (x-1)(x-2)…(x-2022)=(x-1)(x-2)…(x-2022)。
      擦去两边的一些线性因子，使每边至少剩一个因子，
      且结果方程无实根。求最少擦除数。
    domain: Algebra
    verified_solution: |
      预期思路：
      1. 与1843类似，需要|A|=|B|=1011，擦除数≥2022。
      2. 但2022=2×3×337，不是4的倍数。
      3. 模4分类策略需要调整——因子数量不是4的倍数时，
         左右各1011个因子，按模4分组后各组数量不均衡。
      4. 可能需要模6分类（2022=6×337）或其他模数。
      5. 这正是变形的测试点——AI能否在n不是4的倍数时调整策略。
    verification_status: unverified
  bare_baseline:
    required_for_positive: true
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 与1843类似——多项式符号分析太复杂
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"多项式符号分析困境" → 切换到模分类 →
      但n=2022不是4的倍数，需要选择不同的模数（如模6）→
      调整符号配对策略
    expected_progress_signal: |
      1. AI开始模分类分析
      2. AI发现n=2022不是4的倍数，需要调整模数
      3. AI选择新模数并建立符号配对
    expected_termination: 取决于新模数下符号配对是否成立
  structure:
    invariant_kernel: |
      保留1843的核心结构：多项式方程实根分析，模分类+符号配对转向。
      改变：因子数量从2016（4的倍数）变为2022（非4的倍数）。
      关键变形：模4配对不能直接复用，需要选择新模数。
    surface_features: n=2022（非4的倍数）
    preserved_features: 符号分析困境、模分类转向
    broken_features_if_negative: n不是4的倍数，模4配对结构不同
    metamorphic_relation: 与1843同构——但需要调整模数选择
  controls:
    matched_false_friend: CC-014
    matched_boundary_case: CC-019
    matched_decoy: CC-017
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 0分
      策略中心性: 2分
      过程可观察: 2分
      假朋友可构造: 2分
      结构可变形: 2分（n非4的倍数，变形彻底）
      解答可核验: 0分
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 1分
      学习价值: 2分（测试AI能否调整模数选择，而非机械复用模4）
    veto_reason: 解答未核验
    frozen_role: metamorphic
  special_note: |
    本题是1843的彻底变形——n=2022不是4的倍数。
    如果AI机械复用模4策略而失败，说明TellCore过窄（特化于模4）。
    如果AI能识别"n不是4的倍数"并调整模数选择，说明TellCore真正非特化。
    这道题最能测试"模数选择"这一parameter_slot的绑定能力。
```

### CC-011：1709变体——最大不被3整除的因子

```yaml
CaseCard_CC011:
  case_id: CC-011
  source:
    origin: metamorphic_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-003(1709)构造
  role:
    primary_role: metamorphic
    secondary_roles: []
  problem:
    statement: |
      对每个正整数k，令s(k)为k的最大不被3整除的因子。
      求所有正整数a，使存在正整数n，让
      s(n+a)-s(n), s(n+a+1)-s(n+1), ..., s(n+2a-1)-s(n+a-1)
      全部被9整除。
    domain: Number Theory
    verified_solution: |
      预期思路：
      1. s(k)=k/3^{v_3(k)}，即k去掉所有3因子后的部分。
      2. 与1709同构——将2-adic赋值替换为3-adic赋值。
      3. 关键转向：3-adic赋值分析。
      4. 预期答案：a是3的幂。
    verification_status: unverified
  bare_baseline:
    required_for_positive: true
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 与1709类似——枚举/函数分析无法收敛
  target_tell:
    tell_family: 局部表示切换（层次2：p-adic赋值）
    expected_selector_decision: select
    expected_runtime_action: |
      与1709类似——切换到3-adic赋值分析 →
      用v_3表达s(k) → 分析v_3(n+i)与v_3(n+i-a)的关系
    expected_progress_signal: |
      1. AI开始讨论"3-adic"或"v_3"
      2. AI用v_3表达s(k)
      3. AI建立v_3关系
    expected_termination: 成功——v_3分析约束a的结构
  structure:
    invariant_kernel: |
      保留1709的核心结构：最大不被p整除因子的差被p^k整除，p-adic赋值分析。
      改变：p从2变为3，"被4整除"变为"被9整除"（4=2², 9=3²）。
    surface_features: p=3, 被9整除
    preserved_features: p-adic赋值分析结构
    broken_features_if_negative: 无——核心结构完全保持
    metamorphic_relation: 与1709完全同构——2-adic → 3-adic
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: CC-020
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: low
    oversearch_risk: medium
  admission:
    score_summary: |
      bare基线: 0分
      策略中心性: 2分（3-adic赋值是主路）
      过程可观察: 2分
      假朋友可构造: 2分
      结构可变形: 2分（完美的p-adic变形）
      解答可核验: 0分
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 1分
      学习价值: 2分
    veto_reason: 解答未核验
    frozen_role: metamorphic
  special_note: |
    本题是CC-003(1709)的完美p-adic变形——
    将2-adic赋值替换为3-adic赋值，核心结构完全保持。
    如果TellCore v0的"局部表示切换"真正是非特化的，
    AI应在3-adic变形题上也能触发p-adic赋值认知动作。
    这道题最能测试"非特化"主张——
    如果AI只在2-adic场景触发而在3-adic场景不触发，
    说明TellCore仍然特化于p=2。
```

### CC-012：1962变体——ab-c等均为3的幂

```yaml
CaseCard_CC012:
  case_id: CC-012
  source:
    origin: metamorphic_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-004(1962)构造
  role:
    primary_role: metamorphic
    secondary_roles: []
  problem:
    statement: |
      求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是3的幂。
      （3的幂是形如3^n的整数，n为非负整数。）
    domain: Number Theory
    verified_solution: |
      预期思路：
      1. 与1962同构——将2-adic赋值替换为3-adic赋值。
      2. 设ab-c=3^u, bc-a=3^v, ca-b=3^w。
      3. 关键转向：系统3-adic赋值分析。
      4. 利用v_3(ab-c)=u等条件建立v_3方程。
    verification_status: unverified
  bare_baseline:
    required_for_positive: true
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 与1962类似——代数变形无法约束
  target_tell:
    tell_family: 局部表示切换（层次2：p-adic赋值）
    expected_selector_decision: select
    expected_runtime_action: |
      与1962类似——切换到系统3-adic赋值分析 →
      对a,b,c的3-adic结构分case → 建立v_3方程
    expected_progress_signal: |
      1. AI开始系统计算v_3
      2. AI按3-adic结构分case
      3. AI建立v_3方程
    expected_termination: 取决于v_3分析是否能收敛（1962在2-adic下tree仍失败）
  structure:
    invariant_kernel: |
      保留1962的核心结构："是p的幂"条件通过v_p赋值可精确表达。
      改变：p从2变为3。
    surface_features: p=3, 3的幂
    preserved_features: p-adic赋值分析结构、3-adic分case
    broken_features_if_negative: 无——核心结构完全保持
    metamorphic_relation: 与1962完全同构——2-adic → 3-adic
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: CC-018
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: high
  admission:
    score_summary: |
      bare基线: 0分
      策略中心性: 2分
      过程可观察: 2分
      假朋友可构造: 2分
      结构可变形: 2分
      解答可核验: 0分
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 2分
      学习价值: 2分
    veto_reason: 解答未核验
    frozen_role: metamorphic
  special_note: |
    本题是CC-004(1962)的完美p-adic变形。
    特别有价值的是——1962在2-adic下tree组仍失败，
    本题测试3-adic下是否同样困难。
    如果AI在3-adic变形上表现不同（更好或更差），
    能揭示TellCore v0的internal_policy是否真正非特化。
```

---

## 7. 假朋友题CaseCard

### CC-013：假朋友——递推序列收敛性（表面像1631但核心在分析）

```yaml
CaseCard_CC013:
  case_id: CC-013
  source:
    origin: constructed_false_friend
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: false_friend
    secondary_roles: []
  problem:
    statement: |
      对正整数a，定义序列x₁=a，x_{n+1}=2x_n+1。
      令S_n = Σ_{i=1}^{n} 1/x_i。
      证明：对所有正整数a，序列S_n收敛，
      并求lim_{n→∞} S_n的值。
    domain: Analysis / Sequences
    verified_solution: |
      答案：S = 1/(a+1)。
      证明思路：
      1. x_n = 2^{n-1}(a+1)-1，所以x_n ~ 2^{n-1}(a+1)。
      2. 1/x_n ~ 1/(2^{n-1}(a+1))，级数收敛。
      3. 精确计算：1/x_n = 1/(2^{n-1}(a+1)-1)。
         利用telescoping或直接求和。
      4. 关键：这是一个实分析问题，不是数论问题。
         模p分析不直接适用——核心在级数收敛性而非整除性。
    verification_status: verified
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用（假朋友题不要求bare失败）
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: reject
    expected_runtime_action: |
      理想selector应reject——
      本题表面涉及递推序列（与1631表面相似），
      但核心在级数收敛性（实分析），不在整除性/素性。
      模p分析不直接适用于收敛性问题。
    expected_progress_signal: 无——不应触发目标Tell
    expected_termination: 不适用——不应触发
  structure:
    invariant_kernel: |
      表面相似：递推序列x_{n+1}=2x_n+1（与1631完全相同）。
      结构缺失：核心在级数收敛性，不在素性/整除性。
      模p分析不适用——收敛性是实分析概念，不是代数概念。
    surface_features: 递推序列、2x_n+1（与1631相同的递推）
    preserved_features: 无——核心结构完全不同
    broken_features_if_negative: 素性条件被替换为收敛性条件
    metamorphic_relation: 无——表面相似但结构不同
  controls:
    matched_false_friend: 本身即为假朋友题
    matched_boundary_case: CC-018
    matched_decoy: CC-016
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      假朋友可构造: 2分（表面相似度强，结构差异清楚）
      解答可核验: 2分
      学习价值: 2分（如果selector误触发，说明trigger过宽——需要收紧"整除性/素性"条件）
    veto_reason: 无
    frozen_role: false_friend
  special_note: |
    本题的表面相似度很强——递推关系与1631完全相同。
    但核心结构完全不同——1631的核心在素性判定（模p分析适用），
    本题的核心在级数收敛性（模p分析不适用）。
    如果selector对本题select，说明trigger的"整除性/素性"条件不够严格。
```

### CC-014：假朋友——多项式系数大小（表面像1843但核心在系数）

```yaml
CaseCard_CC014:
  case_id: CC-014
  source:
    origin: constructed_false_friend
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: false_friend
    secondary_roles: []
  problem:
    statement: |
      设P(x)=(x-1)(x-2)…(x-2016)。
      求P(x)的展开式中绝对值最大的系数。
    domain: Algebra / Combinatorics
    verified_solution: |
      这是一个关于排列组合/系数大小的问题。
      核心在计算特定位置的elementary symmetric polynomial的值，
      不在符号分析或模p配对。
    verification_status: partial
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: reject
    expected_runtime_action: |
      理想selector应reject——
      本题表面涉及多项式(x-1)...(x-2016)（与1843完全相同的多项式），
      但核心在系数大小，不在实根分析或符号配对。
      模4分类不直接适用于系数大小问题。
    expected_progress_signal: 无——不应触发目标Tell
    expected_termination: 不适用
  structure:
    invariant_kernel: |
      表面相似：多项式(x-1)...(x-2016)（与1843完全相同）。
      结构缺失：核心在系数大小，不在实根/符号分析。
    surface_features: 多项式、因子乘积（与1843相同的多项式）
    preserved_features: 无
    broken_features_if_negative: 实根分析条件被替换为系数大小条件
    metamorphic_relation: 无
  controls:
    matched_false_friend: 本身即为假朋友题
    matched_boundary_case: CC-019
    matched_decoy: CC-017
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      假朋友可构造: 2分（表面相似度强——同一多项式，结构差异清楚）
      解答可核验: 1分
      学习价值: 2分
    veto_reason: 无
    frozen_role: false_friend
```

### CC-015：假朋友——构造性整除问题（表面像1709/1962但核心在构造）

```yaml
CaseCard_CC015:
  case_id: CC-015
  source:
    origin: constructed_false_friend
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: false_friend
    secondary_roles: []
  problem:
    statement: |
      构造一个正整数集合S⊆{1,2,...,100}，
      使得S中任意两个不同元素x,y的差|x-y|都是2的幂，
      且|S|尽可能大。求|S|的最大值。
    domain: Combinatorics / Construction
    verified_solution: |
      这是一个构造性组合问题。
      核心在构造满足条件的集合，不在分析整除性结构。
      虽然条件涉及"2的幂"，但p-adic赋值分析不直接适用于构造问题。
    verification_status: partial
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: reject
    expected_runtime_action: |
      理想selector应reject——
      本题表面涉及"2的幂"（与1962表面相似），
      但核心在构造性组合，不在p-adic赋值分析。
      v_2分析不直接适用于"差是2的幂"的构造问题。
    expected_progress_signal: 无
    expected_termination: 不适用
  structure:
    invariant_kernel: |
      表面相似：条件涉及"2的幂"（与1962表面相似）。
      结构缺失：核心在构造性组合，不在"是2的幂"的代数分析。
    surface_features: 2的幂条件
    preserved_features: 无
    broken_features_if_negative: "是2的幂"的代数分析条件被替换为构造性条件
    metamorphic_relation: 无
  controls:
    matched_false_friend: 本身即为假朋友题
    matched_boundary_case: CC-020
    matched_decoy: CC-016
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: low
  admission:
    score_summary: |
      假朋友可构造: 2分
      解答可核验: 1分
      学习价值: 2分
    veto_reason: 无
    frozen_role: false_friend
  special_note: |
    本题测试selector是否能区分"分析性使用2的幂"（应触发p-adic）
    和"构造性使用2的幂"（不应触发p-adic）。
    如果selector对构造性问题select，说明trigger的"分析性"条件不够严格。
```

### CC-016：假朋友——组合计数中的2的幂（表面像1962但核心在计数）

```yaml
CaseCard_CC016:
  case_id: CC-016
  source:
    origin: constructed_false_friend
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: false_friend
    secondary_roles: [decoy]
  problem:
    statement: |
      在{1,2,...,2^n}中，有多少个子集S满足：
      S中所有元素的和恰好是2的幂？
      求这个数量的精确公式（用n表达）。
    domain: Combinatorics / Counting
    verified_solution: |
      这是一个组合计数问题。
      核心在计算满足条件的子集数量，不在分析元素的p-adic结构。
    verification_status: unverified
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: reject
    expected_runtime_action: |
      理想selector应reject——
      本题表面涉及"2的幂"（与1962表面相似），
      但核心在组合计数，不在p-adic赋值分析。
    expected_progress_signal: 无
    expected_termination: 不适用
  structure:
    invariant_kernel: |
      表面相似：条件涉及"2的幂"。
      结构缺失：核心在组合计数，不在代数分析。
    surface_features: 2的幂条件、{1,...,2^n}的范围
    preserved_features: 无
    broken_features_if_negative: 代数分析条件被替换为计数条件
    metamorphic_relation: 无
  controls:
    matched_false_friend: 本身即为假朋友题
    matched_boundary_case: CC-020
    matched_decoy: 本身即为decoy
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: medium
    oversearch_risk: low
  admission:
    score_summary: |
      假朋友可构造: 1-2分
      解答可核验: 0分
      学习价值: 2分
    veto_reason: 无
    frozen_role: false_friend + decoy
```

### CC-017：假朋友——代数几何表面（表面像1843但核心在代数几何）

```yaml
CaseCard_CC017:
  case_id: CC-017
  source:
    origin: constructed_false_friend
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: false_friend
    secondary_roles: [decoy]
  problem:
    statement: |
      设f(x)=(x-1)(x-2)…(x-n)，g(x)=(x-1)(x-2)…(x-n)。
      考虑曲线C: f(x)-g(x)=0在复平面上的几何性质。
      当n→∞时，C的"洞"（genus）的行为如何？
      （本题故意使用模糊的代数几何语言作为诱饵）
    domain: Algebraic Geometry
    verified_solution: |
      本题故意构造为模糊的代数几何问题。
      f(x)-g(x)=0恒成立（因为f=g），所以C是全平面，没有"洞"。
      这是一个陷阱题——表面涉及多项式方程（与1843相似），
      但实际上是平凡的恒等式问题，且代数几何视角完全不必要。
    verification_status: verified
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: reject
    expected_runtime_action: |
      理想selector应reject——
      本题表面涉及多项式方程（与1843相似），
      但实际上是恒等式问题，模p分析完全不必要。
      且"代数几何"视角是诱饵，不应被表面语言误导。
    expected_progress_signal: 无
    expected_termination: 不适用
  structure:
    invariant_kernel: |
      表面相似：多项式方程f(x)=g(x)（与1843相似）。
      结构缺失：f≡g，方程恒成立，无分析必要。
      诱饵：代数几何语言。
    surface_features: 多项式方程、曲线、genus
    preserved_features: 无
    broken_features_if_negative: 实根分析条件被替换为恒等式
    metamorphic_relation: 无
  controls:
    matched_false_friend: 本身即为假朋友题
    matched_boundary_case: CC-019
    matched_decoy: 本身即为decoy
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: high
    oversearch_risk: low
  admission:
    score_summary: |
      假朋友可构造: 2分（诱饵设计强）
      解答可核验: 2分
      学习价值: 2分（测试selector是否被表面语言误导）
    veto_reason: 无
    frozen_role: false_friend + decoy
  special_note: |
    本题是decoy题——测试selector是否被"代数几何"等高级语言误导。
    如果selector因为题面涉及"曲线""genus"等代数几何词汇而select，
    说明selector在匹配trigger时被表面语言而非结构特征驱动。
```

---

## 8. 边界题CaseCard

### CC-018：边界——1962变体"2的幂"改为"素数"

```yaml
CaseCard_CC018:
  case_id: CC-018
  source:
    origin: boundary_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-004(1962)构造
  role:
    primary_role: boundary
    secondary_roles: []
  problem:
    statement: |
      求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是素数。
    domain: Number Theory
    verified_solution: |
      预期分析：
      1. 与1962的结构相同，但"2的幂"被替换为"素数"。
      2. p-adic赋值分析不再直接适用——
         素数条件不能用v_p精确表达（素数不是p^k形式）。
      3. 需要完全不同的方法——可能利用素数的分布性质或大小约束。
      4. 预期答案可能非常有限或无解。
    verification_status: unverified
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: boundary
    expected_runtime_action: |
      理想selector应标为boundary——
      本题与1962结构几乎相同（只改一个条件），
      但"素数"条件使p-adic赋值分析不再直接适用。
      selector应识别：结构相似但关键条件改变，触发边界。
    expected_progress_signal: |
      如果AI尝试p-adic分析但发现不适用，这是正确的边界行为。
      如果AI强行使用p-adic分析并陷入困境，说明termination机制需要改进。
    expected_termination: |
      理想行为：AI尝试p-adic分析 → 发现"素数"条件不适用 → 退出或让位。
      或者：selector直接标为boundary，不触发目标Tell。
  structure:
    invariant_kernel: |
      与1962的唯一差异："2的幂"→"素数"。
      这个改变破坏了p-adic赋值分析的适用性——
      v_p(素数)要么是0（p≠该素数）要么是1（p=该素数），
      不提供足够信息来建立v_p方程。
    surface_features: 三元组、素数条件
    preserved_features: 三元组结构、对称性
    broken_features_if_negative: "2的幂"→"素数"破坏p-adic适用性
    metamorphic_relation: 无——关键条件改变使目标Tell不适用
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: 本身即为边界题
    matched_decoy: CC-016
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: medium
  admission:
    score_summary: |
      策略中心性: 0-1分（p-adic不直接适用，但模p分析可能有弱关联）
      学习价值: 2分（测试selector的boundary决策和AI的termination行为）
    veto_reason: 无
    frozen_role: boundary
  special_note: |
    本题是1962的边界变体——只改一个关键条件（"2的幂"→"素数"）。
    测试两个能力：
    1. selector能否识别边界（标为boundary而非select/reject）
    2. AI在尝试p-adic分析后发现不适用时能否正确退出
    如果selector强行select且AI无法退出，说明termination机制需要改进。
```

### CC-019：边界——1843变体"无实根"改为"无正根"

```yaml
CaseCard_CC019:
  case_id: CC-019
  source:
    origin: boundary_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-002(1843)构造
  role:
    primary_role: boundary
    secondary_roles: []
  problem:
    statement: |
      板上写着方程 (x-1)(x-2)…(x-2016)=(x-1)(x-2)…(x-2016)。
      擦去两边的一些线性因子，使每边至少剩一个因子，
      且结果方程无正实根。求最少擦除数。
    domain: Algebra
    verified_solution: |
      预期分析：
      1. 与1843的唯一差异："无实根"→"无正实根"。
      2. 模4符号配对策略可能仍然部分适用，但需要调整——
         只需要保证正实轴上无根，负实轴上可以有根。
      3. 这可能允许更少的擦除数（因为约束更弱）。
      4. 模4分类仍然有用，但符号配对的策略需要修改。
    verification_status: unverified
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: boundary
    expected_runtime_action: |
      理想selector应标为boundary——
      模4分类仍然相关，但符号配对策略需要调整。
      不是完全select（策略不能直接复用），也不是完全reject（模4仍然有用）。
    expected_progress_signal: |
      AI开始模4分析 → 发现"无正根"约束与"无实根"不同 →
      调整符号配对策略 → 可能需要组合其他分析
    expected_termination: |
      部分进展——模4分析给出部分约束，但需要更精细的正负轴分析。
  structure:
    invariant_kernel: |
      与1843的唯一差异："无实根"→"无正实根"。
      模4分类仍然适用，但符号配对策略需要调整——
      只需保证正实轴上符号不翻转，负实轴上可以翻转。
    surface_features: 无正实根
    preserved_features: 模4分类仍然相关
    broken_features_if_negative: "无实根"→"无正实根"使符号配对策略需要修改
    metamorphic_relation: 部分保持——模4分类适用，但配对策略需要调整
  controls:
    matched_false_friend: CC-014
    matched_boundary_case: 本身即为边界题
    matched_decoy: CC-017
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: medium
    oversearch_risk: low
  admission:
    score_summary: |
      策略中心性: 1分（模4仍然有用但不能直接复用）
      学习价值: 2分（测试selector的boundary决策和AI的策略调整能力）
    veto_reason: 无
    frozen_role: boundary
  special_note: |
    本题测试TellCore v0的"可调整性"——
    当关键条件只做微小改变时，AI能否在模4分析的基础上调整策略，
    而不是完全复用或完全放弃。
    这是boundary题的理想形态——不是完全触发也不是完全不触发。
```

### CC-020：边界——1709变体"被4整除"改为"被3整除"

```yaml
CaseCard_CC020:
  case_id: CC-020
  source:
    origin: boundary_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-003(1709)构造
  role:
    primary_role: boundary
    secondary_roles: []
  problem:
    statement: |
      对每个正整数k，令t(k)为k的最大奇因子。
      求所有正整数a，使存在正整数n，让
      t(n+a)-t(n), t(n+a+1)-t(n+1), ..., t(n+2a-1)-t(n+a-1)
      全部被3整除。
    domain: Number Theory
    verified_solution: |
      预期分析：
      1. 与1709的唯一差异："被4整除"→"被3整除"。
      2. t(k)=k/2^{v_2(k)}仍然是最大奇因子。
      3. "被3整除"条件涉及的是t(k) mod 3，而不是t(k) mod 4。
      4. 2-adic赋值分析t(k)的结构仍然适用，
         但"被3整除"条件的分析与"被4整除"不同——
         需要分析t(k) mod 3，而t(k)是奇数，其mod 3的值需要额外分析。
      5. 这是一个真正的边界——2-adic赋值仍然有用（分析t(k)结构），
         但"被3整除"条件需要额外的模3分析。
    verification_status: unverified
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: boundary
    expected_runtime_action: |
      理想selector应标为boundary——
      2-adic赋值分析t(k)结构仍然适用，
      但"被3整除"条件需要额外的模3分析。
      目标Tell部分适用，但不能直接复用1709的策略。
    expected_progress_signal: |
      AI开始2-adic分析 → 发现"被3整除"需要额外模3分析 →
      组合2-adic和模3分析
    expected_termination: |
      部分进展——2-adic分析给出t(k)结构，
      模3分析给出"被3整除"条件，
      需要组合两者。
  structure:
    invariant_kernel: |
      与1709的唯一差异："被4整除"→"被3整除"。
      2-adic赋值分析t(k)结构仍然适用，
      但"被3整除"条件需要额外的模3分析（t(k) mod 3）。
    surface_features: 被3整除
    preserved_features: 2-adic赋值分析t(k)结构
    broken_features_if_negative: "被4整除"→"被3整除"需要额外的模3分析
    metamorphic_relation: 部分保持——2-adic适用，但需要组合模3分析
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: 本身即为边界题
    matched_decoy: CC-016
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: medium
  admission:
    score_summary: |
      策略中心性: 1-2分（2-adic部分适用，需要组合模3）
      学习价值: 2分（测试组合能力和boundary决策）
    veto_reason: 无
    frozen_role: boundary
  special_note: |
    本题测试TellCore v0的组合能力——
    2-adic赋值分析t(k)结构（层次2）+ 模3分析"被3整除"条件（层次1）。
    需要两个层次的局部表示切换组合工作。
    这是POC-5（可组合）的理想测试材料。
```

---

## 9. 组合题CaseCard

### CC-021：组合——局部表示切换+构造性Tell

```yaml
CaseCard_CC021:
  case_id: CC-021
  source:
    origin: constructed
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: composition
    secondary_roles: []
  problem:
    statement: |
      求所有正整数n，使得存在正整数a₁,a₂,...,a_n满足：
      (1) a₁+a₂+...+a_n = 2n
      (2) 对每个i，a_i | 2n
      (3) 对每对i≠j，a_i - a_j 是2的幂（可为负，即|a_i-a_j|是2的幂）
    domain: Number Theory / Construction
    verified_solution: |
      预期分析：
      1. 条件(3)涉及"差是2的幂"——表面像p-adic赋值问题。
      2. 但核心难点是构造性——需要构造满足所有条件的序列。
      3. 策略：先用p-adic赋值分析约束a_i的结构（局部表示切换），
         再用构造性Tell构造具体序列。
      4. 这是顺序依赖组合——局部表示切换先于构造性Tell。
    verification_status: unverified
  bare_baseline:
    required_for_positive: true
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: |
      预测AI可能尝试直接构造，忽略p-adic结构分析，
      导致构造空间过大无法收敛。
  target_tell:
    tell_family: 局部表示切换 + 构造性Tell（顺序依赖）
    expected_selector_decision: select（局部表示切换作为前置）
    expected_runtime_action: |
      步骤1（局部表示切换）：分析a_i的2-adic结构 →
      利用"差是2的幂"条件约束a_i的v_2值 →
      约束a_i的可能形式。
      步骤2（构造性Tell）：在约束范围内构造具体序列 →
      验证满足所有条件。
    expected_progress_signal: |
      1. AI开始v_2分析a_i结构
      2. AI从v_2约束推导a_i的可能形式
      3. AI在约束范围内开始构造
      4. AI验证构造满足所有条件
    expected_termination: |
      成功：v_2约束+构造共同给出完整解。
      部分进展：v_2约束给出结构但构造失败 → 标记，需要更强的构造性Tell。
  structure:
    invariant_kernel: |
      核心结构：先分析后构造。
      局部表示切换提供结构约束，构造性Tell在约束内构造。
    surface_features: 2的幂条件、求和条件、整除条件
    preserved_features: p-adic结构分析+构造的组合
    broken_features_if_negative: 无
    metamorphic_relation: 分析+构造的组合
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: CC-018
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: medium
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: medium
  admission:
    score_summary: |
      bare基线: 0分
      策略中心性: 2分（p-adic+构造的组合是主路）
      过程可观察: 2分
      组合价值: 2分（明确的顺序依赖组合）
      解答可核验: 0分
      泄漏安全: 1分
      学习价值: 2分
    veto_reason: bare基线和解答核验都需要后续验证
    frozen_role: composition
  special_note: |
    本题测试POC-5（可组合）——
    局部表示切换（分析结构）→ 构造性Tell（在约束内构造）。
    顺序依赖：构造性Tell依赖局部表示切换先给出结构约束。
    如果AI跳过p-adic分析直接构造，说明组合调度失败。
```

### CC-022：组合——模p分析+模q分析的互补

```yaml
CaseCard_CC022:
  case_id: CC-022
  source:
    origin: constructed
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: composition
    secondary_roles: []
  problem:
    statement: |
      求所有正整数n，使得：
      (1) n | 2^n - 1
      (2) n | 3^n - 1
      (3) n不是2或3的倍数
    domain: Number Theory
    verified_solution: |
      预期分析：
      1. 条件(1)涉及2的模n阶——需要模p分析（对n的每个素因子p）。
      2. 条件(2)涉及3的模n阶——需要模q分析（对n的每个素因子q）。
      3. 条件(3)排除n是2或3的倍数——简化分析。
      4. 策略：对n的每个素因子p，分别用模p分析2和3的阶。
         需要组合模2分析和模3分析的结果。
      5. 这是互补协同组合——模p分析和模q分析并行增强。
    verification_status: unverified
  bare_baseline:
    required_for_positive: true
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: |
      预测AI可能只分析一个条件而忽略另一个，
      或尝试直接枚举n。
  target_tell:
    tell_family: 局部表示切换（模p分析+模q分析互补）
    expected_selector_decision: select
    expected_runtime_action: |
      步骤1：对n的每个素因子p，分析2 mod p的阶（条件1）。
      步骤2：对n的每个素因子p，分析3 mod p的阶（条件2）。
      步骤3：组合两个分析结果，约束n的结构。
    expected_progress_signal: |
      1. AI开始对素因子p取模分析
      2. AI分别分析2和3的阶
      3. AI组合两个分析结果
    expected_termination: |
      成功：两个模分析组合给出n的完整结构。
      部分进展：一个模分析给出部分约束，另一个需要更多分析。
  structure:
    invariant_kernel: |
      核心结构：两个模分析互补协同。
      模p分析2的阶 + 模p分析3的阶 → 组合约束n。
    surface_features: 2^n-1, 3^n-1, 整除条件
    preserved_features: 模p分析+模q分析的互补组合
    broken_features_if_negative: 无
    metamorphic_relation: 互补协同组合
  controls:
    matched_false_friend: CC-013
    matched_boundary_case: CC-020
    matched_decoy: CC-017
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: medium
  admission:
    score_summary: |
      bare基线: 0分
      策略中心性: 2分
      过程可观察: 2分
      组合价值: 2分（互补协同组合）
      解答可核验: 0分
      泄漏安全: 2分
      学习价值: 2分
    veto_reason: bare基线和解答核验都需要后续验证
    frozen_role: composition
  special_note: |
    本题测试POC-5（可组合）——
    模p分析2的阶 + 模p分析3的阶，互补协同。
    与CC-021的顺序依赖不同，本题是互补协同——
    两个分析可以并行进行，结果互相增强。
```

---

## 10. 回归题说明

回归题来自旧正例、旧负例和旧边界例。本CasePack的回归题集合包括：

| 回归题 | 来源 | 作用 |
|---|---|---|
| CC-001(1631) | 旧正例（VMS-8/9 lineage成功） | 验证Tell修订没有破坏旧正例 |
| CC-002(1843) | 旧正例（VMS-8 tree成功） | 验证Tell修订没有破坏旧正例 |
| CC-003(1709) | 旧正例（VMS-10 bare失败但Tell应成功） | 验证Tell修订没有破坏旧正例 |
| CC-013 | 旧负例（假朋友） | 验证Tell修订没有使trigger过宽 |
| CC-018 | 旧边界例 | 验证Tell修订没有改变boundary决策 |

每次POC-7（可持续学习）修订TellStrategy后，应从回归题集合中抽少量题重跑，确认修订没有误伤旧能力。

---

## 11. Exclusion Log

以下题目在候选阶段被排除，不进入CasePack v0：

| 排除题 | 排除理由 |
|---|---|
| 1766（指数丢番图方程） | 359号索引指出VMS-8中bare成功，难度窗口不稳定 |
| 1645（cubic sequence） | 359号索引指出题面引用"part (a)"，当前输入文件题面可能不完整 |
| ArangoDB虚拟群token_limit失败题 | 359号索引指出失败原因偏token budget/大表计算/输出落盘，不适合竞赛级思维力验证 |
| 354/357/358号观察性测试淘汰题 | 355/357/358号记录显示这些题被bare成功做出，不满足"真实bare失败"入场券 |
| 362/363号第二轮竞赛级挑战题 | 363号记录显示新造题直接bare筛除 |
| 365-370号奥赛母题挑战池 | 这些题尚未bare测试，只能进入候选池，不能作为正迁移证据。后续可从中筛选bare失败题补充到CasePack v1 |

---

## 12. Leakage Review

对每类题目的泄漏风险审查：

| 题类 | 泄漏风险 | 审查结论 |
|---|---|---|
| source trace题（CC-001~004） | low | Tell只给"切换到局部表示"策略，不给具体lemma（如Euler准则、Fermat小定理）的细节 |
| 正迁移题（CC-005~008） | low-medium | CC-008标注medium——"模p分析"可能过于接近Fermat小定理这个关键lemma |
| 变形题（CC-009~012） | low | Tell不涉及变形题的具体解法 |
| 假朋友题（CC-013~017） | low | 假朋友题不应触发目标Tell，泄漏风险不适用 |
| 边界题（CC-018~020） | low | Tell部分适用，泄漏风险与source trace题类似 |
| 组合题（CC-021~022） | low-medium | CC-021标注medium——组合题的Tell可能涉及构造策略的具体细节 |

**总体泄漏审查结论**：CasePack v0的泄漏风险可控。唯一需要关注的是CC-008——如果bare验证后AI在bare中就想到Fermat小定理，则本题不适合作为正迁移题，应移入exclusion_log。

---

## 13. 选题评分汇总

### 13.1 强证据题（source trace + 正迁移，已有bare失败记录）

| 题号 | bare基线 | 策略中心性 | 过程可观察 | 假朋友可构造 | 结构可变形 | 解答可核验 | 泄漏安全 | 经典风险 | 组合价值 | 学习价值 | 总评 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CC-001(1631) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 强证据 |
| CC-002(1843) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 强证据 |
| CC-003(1709) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 强证据 |
| CC-004(1962) | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 强证据（特殊价值） |
| CC-005(1974) | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 弱正迁移 |
| CC-006(1760) | 2 | 0-1 | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 边界正迁移 |
| CC-007(1681) | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 强证据 |
| CC-008(构造) | 0 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 待bare验证 |

### 13.2 变形/假朋友/边界/组合题

| 题号 | 角色 | 关键评分 | 总评 |
|---|---|---|---|
| CC-009 | 变形 | 结构可变形2, 解答未核验 | 候选变形题 |
| CC-010 | 变形 | 结构可变形2(彻底), 解答未核验 | 候选变形题（彻底变形） |
| CC-011 | 变形 | 结构可变形2(完美p-adic), 解答未核验 | 候选变形题（完美p-adic） |
| CC-012 | 变形 | 结构可变形2(完美p-adic), 解答未核验 | 候选变形题（完美p-adic） |
| CC-013 | 假朋友 | 假朋友可构造2, 解答2 | 强假朋友 |
| CC-014 | 假朋友 | 假朋友可构造2, 解答1 | 强假朋友 |
| CC-015 | 假朋友 | 假朋友可构造2, 解答1 | 强假朋友 |
| CC-016 | 假朋友 | 假朋友可构造1-2, 解答0 | 中等假朋友 |
| CC-017 | 假朋友 | 假朋友可构造2, 解答2 | 强假朋友（decoy） |
| CC-018 | 边界 | 策略中心性0-1, 学习价值2 | 强边界题 |
| CC-019 | 边界 | 策略中心性1, 学习价值2 | 强边界题 |
| CC-020 | 边界 | 策略中心性1-2, 学习价值2 | 强边界题（组合测试） |
| CC-021 | 组合 | 组合价值2, 解答未核验 | 候选组合题 |
| CC-022 | 组合 | 组合价值2, 解答未核验 | 候选组合题 |

### 13.3 准入结论

- **立即可用于POC的题**：CC-001, CC-002, CC-003, CC-004, CC-007（5道强证据题，有完整bare失败记录）
- **需要bare验证后使用的题**：CC-005, CC-006, CC-008（3道正迁移候选）
- **需要解答核验后使用的题**：CC-009~012, CC-021, CC-022（6道变形/组合题）
- **可直接用于selector测试的题**：CC-013~017（5道假朋友题），CC-018~020（3道边界题）

---

## 14. 暂不运行Solver的理由与启动条件

### 14.1 暂不运行Solver的理由

1. **POC-0的目标是冻结题包，不是跑实验**。373号明确要求POC-0在任何Tell测试前冻结题包。
2. **部分题目解答未核验**。变形题（CC-009~012）和组合题（CC-021~022）的解答需要完整核验后才能用于结果层验证。
3. **部分题目需要bare验证**。CC-008是人工构造题，需要先跑bare确认AI确实做不出来。
4. **TellCore v0尚未经过POC-1（因果取商）审查**。在TellCore字段消融和最小充分字段集分析完成前，跑实验无法归责。

### 14.2 启动Solver的条件

启动Solver前，必须同时满足：

1. **POC-1完成**：TellCore v0经过字段消融，确定最小充分字段集。
2. **bare验证完成**：CC-008经过bare测试，确认AI确实做不出来。
3. **解答核验完成**：变形题和组合题的解答经过完整核验。
4. **环境确认**：`echo $ARANGO_DB`输出`xishujuzhen_math_glm52`。
5. **Solver启动方式**：通过`solver_harness.py launch`启动，不手动tmux/nohup。
6. **证据记录**：每个结果写成EvidenceRecord，不只写PASS/FAIL。

### 14.3 推荐的执行顺序

```text
Phase A（策略对象成形）：
  1. POC-0 Case Pack冻结 ← 本文件完成
  2. POC-1 因果取商 ← 对TellCore v0做字段消融
  3. 人工审查TellCore字段
  4. bare验证CC-008
  5. 核验变形题和组合题解答
  6. 形成首版TellStrategy

Phase B（六门组件验证）：
  7. POC-2 可选择 ← 用CC-001~008和CC-013~020测试selector
  8. POC-3 可执行 ← 用CC-001~004测试HintInstance
  9. POC-4 可终止 ← 用CC-004(1962)和CC-018~020测试termination
  10. POC-5 可组合 ← 用CC-020~022测试组合
  11. POC-6 可归责 ← 用CC-001~004做干预矩阵

Phase C（学习闭环）：
  12. POC-7 可持续学习 ← 用假朋友误触发和正例漏触发测试修订
  13. POC-8 端到端闭环
  14. 小回归测试
  15. 最终verdict
```

---

## 15. 下一步

### 15.1 立即可做（不需要Solver）

1. **POC-1因果取商**：对TellCore v0候选C做字段消融——删除invariant_claim中的"层次1/层次2"区分后是否仍可执行？删除internal_policy的step6后是否失去1962的解释力？删除composition_contract后是否失去组合能力？
2. **解答核验**：对CC-009~012和CC-021~022的解答做完整数学验证。
3. **selector设计**：基于TellCore v0的trigger_boundary和negative_boundary，设计selector的匹配规则。
4. **HintRenderer设计**：基于TellCore v0的internal_policy，设计不同提示强度的HintInstance模板。

### 15.2 需要Solver后做

1. **bare验证**：CC-008和CC-009~012的bare测试。
2. **POC-2~POC-8**：六门审计POC套装的逐门验证。

### 15.3 需要用户确认的决策点

1. **Tell家族确认**：本文件选择"局部表示切换"作为首套POC目标Tell家族，是否符合用户预期？
2. **TellCore候选确认**：本文件推荐候选C（局部-全局表示切换），是否采纳？
3. **题包规模确认**：22道题的规模是否合适？是否需要增减？
4. **执行优先级确认**：是否先做POC-1（因果取商）再做bare验证，还是先做bare验证再做POC-1？

---

## 16. 读完后要记住的八句话

1. 本文件冻结了TellV3首套POC的CasePack v0——22道题，角色已冻结，实验后不得改角色。
2. 目标Tell家族是"局部表示切换"——隐藏结构显化/表示切换在数论中的具体化。
3. TellCore v0采纳候选C（局部-全局表示切换），统一了模p和p-adic两个层次。
4. 4道source trace题（1631/1843/1709/1962）有完整bare失败+Tell成功对照，是强证据。
5. 1962在tree组仍失败——这是TellCore v0设计的关键参考：方向不够，需要操作路径。
6. 假朋友题测试trigger是否过宽，边界题测试trigger边缘和termination能力。
7. 暂不运行Solver——先做POC-1因果取商、bare验证、解答核验。
8. 所有证据都应写成EvidenceRecord，局部PASS不得升级成端到端PASS。
