# POC-0 资产 · CasePack v0 简化版（10字段 + 5否决项审查）

**日期**：2026-08-17
**来源**：382号CasePack v0的22道题，按399号§5.1的10字段格式简化
**格式说明**：每道题包含简化CaseCard（10字段）+ 5否决项审查结果（399号§5.2）
**目标Tell家族**：局部-全局表示切换（Local Representation Switch）

---

## 10字段格式说明（399号§5.1）

```yaml
CaseCard:
  case_id:                    # 唯一标识
  source:                     # 来源（historical_bare_failure/olympiad_mechanism/constructed等）
  role:                       # 角色（source_trace/positive_transfer/metamorphic/false_friend/boundary/composition）
  statement:                  # 题面
  verified_solution:          # 解答+核验状态（verified/partial/unverified）
  bare_status:                # bare失败状态+failure_mode
  expected_decision:          # 预期selector决策（select/reject/abstain/boundary）
  expected_progress_signal:   # 预期过程信号
  leakage_risk:               # 泄漏风险（low/medium/high）
  frozen_role:                # 冻结的角色——实验后不能改
```

## 5否决项说明（399号§5.2）

1. **bare真实失败**——有完整bare失败记录（正迁移题必须满足；source trace题可以不满足）
2. **解答可核验**——有verified solution
3. **泄漏安全**——Tell只给策略不给答案信息
4. **经典风险可控**——外壳与路线有足够新鲜度
5. **过程可观察**——thinking中能看见目标过程信号

---

# 一、Source Trace 题（CC-001 ~ CC-004）

---

## CC-001：1631 Mersenne型递推素数长度

```yaml
CaseCard_CC001:
  case_id: CC-001
  source: historical_bare_failure（359号索引第4.1节，283号VMS-8实验结果）
  role: source_trace + positive_transfer
  statement: |
    对正整数a，定义x₁=a，x_{n+1}=2x_n+1。令y_n=2^{x_n}-1。
    求最大k使存在某个a，y₁,...,y_k全素数。
  verified_solution: |
    答案：k=2。verified。
    核心思路：x₃≡7(mod 8) → 2是模x₃的二次剩余 → Euler准则 → x₃|y₂，矛盾。
  bare_status: |
    failed，route_failure。VMS-7g-v3/VMS-8/VMS-9均bare失败，无proof.md。
    自然错误路径：AI尝试枚举奇素数a逐个验证，无法收敛到一般性证明。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始分析x₃ mod 8
    2. AI引入二次剩余/Legendre符号概念
    3. AI应用Euler准则
    4. AI建立x₃|y₂的整除关系
  leakage_risk: low
  frozen_role: source_trace + positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 通过 | VMS-7g-v3/VMS-8/VMS-9三次bare失败，记录完整 |
| 解答可核验 | 通过 | verified solution完整 |
| 泄漏安全 | 通过 | Tell只给"切换到模8分析"策略，不给Euler准则细节 |
| 经典风险可控 | 通过 | Mersenne型问题有一定训练痕迹但具体题面不常见（medium→可控） |
| 过程可观察 | 通过 | 模8分析、Euler准则在thinking中高度可观察 |

---

## CC-002：1843 擦去线性因子使方程无实根

```yaml
CaseCard_CC002:
  case_id: CC-002
  source: historical_bare_failure（359号索引第4.1节，283号VMS-8实验结果）
  role: source_trace + positive_transfer
  statement: |
    板上写着方程 (x-1)(x-2)…(x-2016)=(x-1)(x-2)…(x-2016)。
    擦去两边的一些线性因子，使每边至少剩一个因子，
    且结果方程无实根。求最少擦除数。
  verified_solution: |
    答案：2016。verified。
    核心思路：|A|=|B|=1008后，按模4分类——k≡0,1(mod 4)的因子乘积与k≡2,3(mod 4)符号相反。
  bare_status: |
    failed，route_failure。VMS-7g-v3/VMS-8/VMS-9均bare失败。
    自然错误路径：AI尝试多项式符号分析但2016个因子的符号分析太复杂。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始讨论"模4"或"按模分类"
    2. AI将因子按mod 4分组
    3. AI分析各组乘积的符号关系
    4. AI建立符号配对使方程无实根
  leakage_risk: low
  frozen_role: source_trace + positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 通过 | VMS-7g-v3/VMS-8/VMS-9三次bare失败，记录完整 |
| 解答可核验 | 通过 | verified solution完整 |
| 泄漏安全 | 通过 | Tell只给"切换到模4分类"策略 |
| 经典风险可控 | 通过 | 多项式实根问题有一定训练痕迹但具体题面不常见（medium→可控） |
| 过程可观察 | 通过 | 模4分类、符号配对在thinking中可观察 |

---

## CC-003：1709 t(k)最大奇因子差被4整除

```yaml
CaseCard_CC003:
  case_id: CC-003
  source: historical_bare_failure（359号索引第4.3节，289号VMS-10实验结果）
  role: source_trace + positive_transfer
  statement: |
    对每个正整数k，令t(k)为k的最大奇因子。
    求所有正整数a，使存在正整数n，让
    t(n+a)-t(n), t(n+a+1)-t(n+1), ..., t(n+2a-1)-t(n+a-1)
    全部被4整除。
  verified_solution: |
    答案：a是2的幂（a=1,2,4,8,...）。verified。
    核心思路：t(k)=k/2^{v_2(k)}，2-adic赋值分析t(k) mod 4的结构。
  bare_status: |
    failed，route_failure。VMS-10 bare失败，无proof.md。
    自然错误路径：AI尝试枚举a和函数分析，bare thinking约66037字符，未找到2-adic赋值方法。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始讨论"2-adic"或"v_2"或"2的幂次"
    2. AI用v_2表达t(k)
    3. AI建立v_2(n+i)与v_2(n+i-a)的关系
    4. AI从v_2约束推导a必须是2的幂
  leakage_risk: low
  frozen_role: source_trace + positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 通过 | VMS-10 bare失败，记录完整 |
| 解答可核验 | 通过 | verified solution完整 |
| 泄漏安全 | 通过 | Tell只给"切换到2-adic赋值"策略 |
| 经典风险可控 | 通过 | 经典风险low |
| 过程可观察 | 通过 | v_2分析在thinking中可观察 |

---

## CC-004：1962 正整数三元组ab-c等均为2的幂

```yaml
CaseCard_CC004:
  case_id: CC-004
  source: historical_bare_failure（359号索引第4.1节，283号VMS-8实验结果）
  role: source_trace + boundary_case_for_direction_vs_path
  statement: |
    求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是2的幂。
    （2的幂是形如2^n的整数，n为非负整数。）
  verified_solution: |
    答案：(2,2,2), (1,1,1)等（需要完整验证）。partial。
    核心思路：v_2(ab-c)=u等，利用v_2性质建立方程约束(a,b,c)的结构。
  bare_status: |
    failed，route_failure。VMS-7g-v3/VMS-8 bare失败，VMS-8 tree组仍失败。
    关键教训：tree组给了p-adic方向但AI仍无法完成——"给方向"不够，需要操作路径。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始系统计算v_2
    2. AI按奇偶性分case
    3. AI在每个case中建立v_2方程
    4. AI从v_2约束推导(a,b,c)的可能值
  leakage_risk: low
  frozen_role: source_trace + boundary_case_for_direction_vs_path
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 通过 | VMS-7g-v3/VMS-8 bare失败+tree组失败，记录完整 |
| 解答可核验 | 待确认 | verification_status: partial——一般情形需要完整验证 |
| 泄漏安全 | 通过 | Tell只给"切换到p-adic赋值"策略 |
| 经典风险可控 | 通过 | 经典风险low |
| 过程可观察 | 通过 | v_2分析在thinking中可观察 |

---

# 二、正迁移题（CC-005 ~ CC-008）

---

## CC-005：1974 n皇后式rook配置最大空方块

```yaml
CaseCard_CC005:
  case_id: CC-005
  source: historical_bare_failure（359号索引第4.1节）
  role: positive_transfer
  statement: |
    在n×n棋盘上放置rook（不能互相攻击），使得存在一个k×k的空方块
    （方块内无rook）。求保证存在空方块的最大k。
    （具体n值和完整条件见原始题面）
  verified_solution: |
    需要从OlympiadBench获取完整解答。partial。
  bare_status: |
    failed，route_failure。VMS-8 bare失败，未形成成功闭环。
    自然错误路径：AI尝试直接构造和计数，未找到模算术/不变量分析路径。
  expected_decision: select（弱正迁移候选——模p分析是否是主路需验证）
  expected_progress_signal: |
    1. AI开始讨论"模p"或"周期性"
    2. AI在模p下分析rook分布
    3. AI建立空方块与模p结构的关系
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 通过 | VMS-8 bare失败 |
| 解答可核验 | 待确认 | verification_status: partial，需从OlympiadBench获取完整解答 |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 待确认 | classicality_risk: medium，需确认题面新鲜度 |
| 过程可观察 | 待确认 | 模p分析信号可能较弱（过程可观察评分1分） |

**注**：本题是弱正迁移候选。模p分析是否是低搜索成本主路尚不确定。

---

## CC-006：1760 旁切圆几何

```yaml
CaseCard_CC006:
  case_id: CC-006
  source: historical_bare_failure（359号索引第3节，VMS-7g-v3）
  role: positive_transfer + boundary_case_for_domain
  statement: |
    旁切圆几何题，求两个角。
    （具体题面见OlympiadBench ID 1760）
  verified_solution: |
    两角均90°。verified。
  bare_status: |
    failed，route_failure。VMS-7g-v3 bare失败。
    自然错误路径：AI尝试直接几何分析，未找到关键的角度关系。
  expected_decision: boundary
  expected_progress_signal: |
    信号可能微弱——AI是否引入了模分析视角。
    （几何问题中模p分析可能不直接适用，但角度关系的模分析如mod 180°可能有弱关联）
  leakage_risk: low
  frozen_role: positive_transfer + boundary_case_for_domain
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 通过 | VMS-7g-v3 bare失败 |
| 解答可核验 | 通过 | verified solution（两角均90°） |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 不通过 | classicality_risk: high——经典几何题，训练痕迹可能强 |
| 过程可观察 | 待确认 | 信号可能微弱，过程可观察评分1分 |

**注**：本题是跨域边界案例。经典风险高，用于测试selector的boundary决策。

---

## CC-007：1681 满射f:N→N保持素数整除等价

```yaml
CaseCard_CC007:
  case_id: CC-007
  source: historical_bare_failure（359号索引第3节，VMS-7g-v3）
  role: positive_transfer
  statement: |
    求所有满射f:N→N，使得对所有正整数n和所有素数p，
    p|n当且仅当p|f(n)。
  verified_solution: |
    答案：f(n)=n。verified。
  bare_status: |
    failed，route_failure。VMS-7g-v3 bare失败。
    自然错误路径：AI尝试直接分析函数方程，未利用素数整除性条件的模p结构。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始对每个素数p分析f mod p
    2. AI利用满射条件约束f
    3. AI从所有p的约束综合出f(n)=n
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 通过 | VMS-7g-v3 bare失败 |
| 解答可核验 | 通过 | verified solution（f(n)=n） |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: medium→可控 |
| 过程可观察 | 通过 | 模p分析在thinking中可观察 |

---

## CC-008：人工构造正迁移候选——模p下的隐藏周期

```yaml
CaseCard_CC008:
  case_id: CC-008
  source: constructed（382号首次构造）
  role: positive_transfer（待bare验证）
  statement: |
    对正整数n，定义a_n = 3^n + (-2)^n。
    求所有素数p，使得对任意正整数n，
    p | a_n 当且仅当 p | a_{n+p-1}。
  verified_solution: |
    答案：p=5（以及p=2, p=3需要特殊分析）。partial。
    核心思路：Fermat小定理给出a_{n+p-1}≡a_n(mod p)（p≠2,3时）。
  bare_status: |
    not_run。尚未bare测试——需要后续bare验证。
    预测AI可能尝试直接计算a_n的值并寻找模式，未利用Fermat小定理的模p周期性。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始对素数p取模分析
    2. AI引入Fermat小定理
    3. AI建立a_{n+p-1}≡a_n(mod p)的关系
  leakage_risk: medium
  frozen_role: positive_transfer（待bare验证）
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不通过 | 尚未bare测试——需要后续验证 |
| 解答可核验 | 待确认 | verification_status: partial，特殊p需要完整验证 |
| 泄漏安全 | 待确认 | leakage_risk: medium——"模p分析"可能过于接近Fermat小定理关键lemma |
| 经典风险可控 | 通过 | classicality_risk: medium→可控 |
| 过程可观察 | 通过 | Fermat小定理在thinking中可观察 |

**注**：bare基线0分。在bare验证完成前只能作为候选，不能作为正迁移证据。如果bare验证后AI在bare中就想到Fermat小定理，则不适合作为正迁移题。

---

# 三、结构保持变形题（CC-009 ~ CC-012）

---

## CC-009：1631变体——底数3的Mersenne型递推

```yaml
CaseCard_CC009:
  case_id: CC-009
  source: metamorphic_variant（基于CC-001/1631构造，382号首次构造）
  role: metamorphic
  statement: |
    对正整数a，定义x₁=a，x_{n+1}=3x_n+2。
    令y_n=3^{x_n}-2。求最大k使存在某个a，y₁,...,y_k全素数。
  verified_solution: |
    预期思路：与1631同构，底数从2变为3。需要分析x₃ mod 某个数的结构。unverified。
  bare_status: |
    not_run。尚未bare测试。
    预测AI尝试枚举a，与1631类似的困境。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始分析x_n mod p
    2. AI引入剩余理论
    3. AI建立整除关系
  leakage_risk: low
  frozen_role: metamorphic
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不通过 | 尚未bare测试 |
| 解答可核验 | 不通过 | unverified——解答未核验 |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | 模分析在thinking中可观察 |

**注**：解答未核验，在核验前只能作为变形题候选，不能进入结果层验证。

---

## CC-010：1843变体——n=2022的因子方程

```yaml
CaseCard_CC010:
  case_id: CC-010
  source: metamorphic_variant（基于CC-002/1843构造，382号首次构造）
  role: metamorphic
  statement: |
    板上写着方程 (x-1)(x-2)…(x-2022)=(x-1)(x-2)…(x-2022)。
    擦去两边的一些线性因子，使每边至少剩一个因子，
    且结果方程无实根。求最少擦除数。
  verified_solution: |
    预期思路：与1843类似但n=2022不是4的倍数，需要选择不同的模数（如模6）。unverified。
  bare_status: |
    not_run。尚未bare测试。
    预测AI与1843类似——多项式符号分析太复杂。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始模分类分析
    2. AI发现n=2022不是4的倍数，需要调整模数
    3. AI选择新模数并建立符号配对
  leakage_risk: low
  frozen_role: metamorphic
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不通过 | 尚未bare测试 |
| 解答可核验 | 不通过 | unverified——解答未核验 |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: medium→可控 |
| 过程可观察 | 通过 | 模分类在thinking中可观察 |

**注**：测试AI能否调整模数选择，而非机械复用模4。解答需核验后才能用于结果层验证。

---

## CC-011：1709变体——最大不被3整除的因子

```yaml
CaseCard_CC011:
  case_id: CC-011
  source: metamorphic_variant（基于CC-003/1709构造，382号首次构造）
  role: metamorphic
  statement: |
    对每个正整数k，令s(k)为k的最大不被3整除的因子。
    求所有正整数a，使存在正整数n，让
    s(n+a)-s(n), s(n+a+1)-s(n+1), ..., s(n+2a-1)-s(n+a-1)
    全部被9整除。
  verified_solution: |
    预期思路：与1709同构——2-adic赋值替换为3-adic赋值。预期答案a是3的幂。unverified。
  bare_status: |
    not_run。尚未bare测试。
    预测与1709类似——枚举/函数分析无法收敛。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始讨论"3-adic"或"v_3"
    2. AI用v_3表达s(k)
    3. AI建立v_3关系
  leakage_risk: low
  frozen_role: metamorphic
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不通过 | 尚未bare测试 |
| 解答可核验 | 不通过 | unverified——解答未核验 |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | v_3分析在thinking中可观察 |

**注**：完美p-adic变形。最能测试"非特化"主张——如果AI只在2-adic场景触发而3-adic不触发，说明TellCore仍特化于p=2。

---

## CC-012：1962变体——ab-c等均为3的幂

```yaml
CaseCard_CC012:
  case_id: CC-012
  source: metamorphic_variant（基于CC-004/1962构造，382号首次构造）
  role: metamorphic
  statement: |
    求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是3的幂。
    （3的幂是形如3^n的整数，n为非负整数。）
  verified_solution: |
    预期思路：与1962同构——2-adic赋值替换为3-adic赋值。unverified。
  bare_status: |
    not_run。尚未bare测试。
    预测与1962类似——代数变形无法约束。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始系统计算v_3
    2. AI按3-adic结构分case
    3. AI建立v_3方程
  leakage_risk: low
  frozen_role: metamorphic
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不通过 | 尚未bare测试 |
| 解答可核验 | 不通过 | unverified——解答未核验 |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | v_3分析在thinking中可观察 |

**注**：1962在2-adic下tree组仍失败，本题测试3-adic下是否同样困难。

---

# 四、假朋友题（CC-013 ~ CC-017）

---

## CC-013：假朋友——递推序列收敛性

```yaml
CaseCard_CC013:
  case_id: CC-013
  source: constructed_false_friend（382号首次构造）
  role: false_friend
  statement: |
    对正整数a，定义序列x₁=a，x_{n+1}=2x_n+1。
    令S_n = Σ_{i=1}^{n} 1/x_i。
    证明：对所有正整数a，序列S_n收敛，
    并求lim_{n→∞} S_n的值。
  verified_solution: |
    答案：S = 1/(a+1)。verified。
    核心：实分析问题——级数收敛性，不是数论问题。模p分析不直接适用。
  bare_status: |
    不适用（假朋友题不要求bare失败）。
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 假朋友题不要求bare失败 |
| 解答可核验 | 通过 | verified solution |
| 泄漏安全 | 通过 | leakage_risk: low（不应触发目标Tell） |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | 如果selector误触发，说明trigger过宽——可观察 |

**表面相似**：递推关系x_{n+1}=2x_n+1与1631完全相同。
**结构缺失**：核心在级数收敛性（实分析），不在素性/整除性。模p分析不适用。

---

## CC-014：假朋友——多项式系数大小

```yaml
CaseCard_CC014:
  case_id: CC-014
  source: constructed_false_friend（382号首次构造）
  role: false_friend
  statement: |
    设P(x)=(x-1)(x-2)…(x-2016)。
    求P(x)的展开式中绝对值最大的系数。
  verified_solution: |
    核心在计算特定位置的elementary symmetric polynomial的值，不在符号分析或模p配对。partial。
  bare_status: |
    不适用（假朋友题不要求bare失败）。
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 假朋友题不要求bare失败 |
| 解答可核验 | 待确认 | verification_status: partial |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: medium→可控 |
| 过程可观察 | 通过 | 如果selector误触发，trigger+critic需协同拦截 |

**表面相似**：多项式(x-1)...(x-2016)与1843完全相同。
**结构缺失**：核心在系数大小，不在实根/符号分析。
**注意**：383号POC-1分析指出CC-014的假朋友拒绝需要critic协同——trigger可能误触发（多项式涉及符号），需要critic拦截。

---

## CC-015：假朋友——构造性整除问题

```yaml
CaseCard_CC015:
  case_id: CC-015
  source: constructed_false_friend（382号首次构造）
  role: false_friend
  statement: |
    构造一个正整数集合S⊆{1,2,...,100}，
    使得S中任意两个不同元素x,y的差|x-y|都是2的幂，
    且|S|尽可能大。求|S|的最大值。
  verified_solution: |
    构造性组合问题。核心在构造满足条件的集合，不在分析整除性结构。partial。
  bare_status: |
    不适用（假朋友题不要求bare失败）。
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 假朋友题不要求bare失败 |
| 解答可核验 | 待确认 | verification_status: partial |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | 如果selector误触发，说明trigger"分析性"条件不够严格 |

**表面相似**：条件涉及"2的幂"（与1962表面相似）。
**结构缺失**：核心在构造性组合，不在p-adic赋值分析。

---

## CC-016：假朋友——组合计数中的2的幂

```yaml
CaseCard_CC016:
  case_id: CC-016
  source: constructed_false_friend（382号首次构造）
  role: false_friend + decoy
  statement: |
    在{1,2,...,2^n}中，有多少个子集S满足：
    S中所有元素的和恰好是2的幂？
    求这个数量的精确公式（用n表达）。
  verified_solution: |
    组合计数问题。核心在计算满足条件的子集数量，不在分析元素的p-adic结构。unverified。
  bare_status: |
    不适用（假朋友题不要求bare失败）。
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend + decoy
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 假朋友题不要求bare失败 |
| 解答可核验 | 不通过 | unverified |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: medium→可控 |
| 过程可观察 | 通过 | 如果selector误触发，说明negative_boundary"搜索空间vs结构隐藏"不够严格 |

**表面相似**：条件涉及"2的幂"。
**结构缺失**：核心在组合计数，不在代数分析。

---

## CC-017：假朋友——代数几何表面

```yaml
CaseCard_CC017:
  case_id: CC-017
  source: constructed_false_friend（382号首次构造）
  role: false_friend + decoy
  statement: |
    设f(x)=(x-1)(x-2)…(x-n)，g(x)=(x-1)(x-2)…(x-n)。
    考虑曲线C: f(x)-g(x)=0在复平面上的几何性质。
    当n→∞时，C的"洞"（genus）的行为如何？
    （本题故意使用模糊的代数几何语言作为诱饵）
  verified_solution: |
    f(x)-g(x)=0恒成立（因为f=g），所以C是全平面，没有"洞"。verified。
    陷阱题——表面涉及多项式方程（与1843相似），但实际是平凡的恒等式问题。
  bare_status: |
    不适用（假朋友题不要求bare失败）。
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend + decoy
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 假朋友题不要求bare失败 |
| 解答可核验 | 通过 | verified solution（f≡g，恒等式） |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | 测试selector是否被"代数几何"表面语言误导 |

**表面相似**：多项式方程f(x)=g(x)（与1843相似）。
**结构缺失**：f≡g，方程恒成立，无分析必要。
**注意**：383号POC-1分析指出CC-017的假朋友拒绝需要critic协同——trigger可能误触发（多项式方程），需要critic"是否过早局部化"拦截。

---

# 五、边界题（CC-018 ~ CC-020）

---

## CC-018：边界——1962变体"2的幂"改为"素数"

```yaml
CaseCard_CC018:
  case_id: CC-018
  source: boundary_variant（基于CC-004/1962构造，382号首次构造）
  role: boundary
  statement: |
    求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是素数。
  verified_solution: |
    预期分析：与1962结构相同但"2的幂"替换为"素数"。p-adic赋值分析不再直接适用。
    素数条件不能用v_p精确表达。unverified。
  bare_status: |
    不适用（边界题不要求bare失败）。
  expected_decision: boundary
  expected_progress_signal: |
    如果AI尝试p-adic分析但发现不适用，这是正确的边界行为。
    如果AI强行使用p-adic分析并陷入困境，说明termination机制需要改进。
  leakage_risk: low
  frozen_role: boundary
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 边界题不要求bare失败 |
| 解答可核验 | 不通过 | unverified |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | 测试AI的termination行为——发现不适用后能否退出 |

**与1962的唯一差异**："2的幂"→"素数"。这个改变破坏p-adic赋值分析的适用性。

---

## CC-019：边界——1843变体"无实根"改为"无正根"

```yaml
CaseCard_CC019:
  case_id: CC-019
  source: boundary_variant（基于CC-002/1843构造，382号首次构造）
  role: boundary
  statement: |
    板上写着方程 (x-1)(x-2)…(x-2016)=(x-1)(x-2)…(x-2016)。
    擦去两边的一些线性因子，使每边至少剩一个因子，
    且结果方程无正实根。求最少擦除数。
  verified_solution: |
    预期分析：模4分类仍然部分适用，但符号配对策略需要调整——只需保证正实轴上无根。unverified。
  bare_status: |
    不适用（边界题不要求bare失败）。
  expected_decision: boundary
  expected_progress_signal: |
    AI开始模4分析 → 发现"无正根"约束与"无实根"不同 → 调整符号配对策略
  leakage_risk: low
  frozen_role: boundary
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 边界题不要求bare失败 |
| 解答可核验 | 不通过 | unverified |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: medium→可控 |
| 过程可观察 | 通过 | 测试AI能否在模4分析基础上调整策略 |

**与1843的唯一差异**："无实根"→"无正实根"。模4分类仍然有用，但配对策略需要修改。

---

## CC-020：边界——1709变体"被4整除"改为"被3整除"

```yaml
CaseCard_CC020:
  case_id: CC-020
  source: boundary_variant（基于CC-003/1709构造，382号首次构造）
  role: boundary
  statement: |
    对每个正整数k，令t(k)为k的最大奇因子。
    求所有正整数a，使存在正整数n，让
    t(n+a)-t(n), t(n+a+1)-t(n+1), ..., t(n+2a-1)-t(n+a-1)
    全部被3整除。
  verified_solution: |
    预期分析：2-adic赋值分析t(k)结构仍然适用，但"被3整除"条件需要额外的模3分析。
    需要组合2-adic和模3分析。unverified。
  bare_status: |
    不适用（边界题不要求bare失败）。
  expected_decision: boundary
  expected_progress_signal: |
    AI开始2-adic分析 → 发现"被3整除"需要额外模3分析 → 组合2-adic和模3分析
  leakage_risk: low
  frozen_role: boundary
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不适用 | 边界题不要求bare失败 |
| 解答可核验 | 不通过 | unverified |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | 测试组合能力——2-adic+模3分析 |

**与1709的唯一差异**："被4整除"→"被3整除"。2-adic赋值部分适用，但需要组合模3分析。POC-5（可组合）的理想测试材料。

---

# 六、组合题（CC-021 ~ CC-022）

---

## CC-021：组合——局部表示切换+构造性Tell

```yaml
CaseCard_CC021:
  case_id: CC-021
  source: constructed（382号首次构造）
  role: composition
  statement: |
    求所有正整数n，使得存在正整数a₁,a₂,...,a_n满足：
    (1) a₁+a₂+...+a_n = 2n
    (2) 对每个i，a_i | 2n
    (3) 对每对i≠j，a_i - a_j 是2的幂（可为负，即|a_i-a_j|是2的幂）
  verified_solution: |
    预期思路：先用p-adic赋值分析约束a_i的结构（局部表示切换），再用构造性Tell构造序列。
    顺序依赖组合。unverified。
  bare_status: |
    not_run。尚未bare测试。
    预测AI可能尝试直接构造，忽略p-adic结构分析。
  expected_decision: select（局部表示切换作为前置）
  expected_progress_signal: |
    1. AI开始v_2分析a_i结构
    2. AI从v_2约束推导a_i的可能形式
    3. AI在约束范围内开始构造
    4. AI验证构造满足所有条件
  leakage_risk: medium
  frozen_role: composition
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不通过 | 尚未bare测试 |
| 解答可核验 | 不通过 | unverified |
| 泄漏安全 | 待确认 | leakage_risk: medium——组合题的Tell可能涉及构造策略细节 |
| 经典风险可控 | 通过 | classicality_risk: low |
| 过程可观察 | 通过 | v_2分析+构造过程在thinking中可观察 |

**注**：测试POC-5（可组合）——顺序依赖：局部表示切换先于构造性Tell。

---

## CC-022：组合——模p分析+模q分析的互补

```yaml
CaseCard_CC022:
  case_id: CC-022
  source: constructed（382号首次构造）
  role: composition
  statement: |
    求所有正整数n，使得：
    (1) n | 2^n - 1
    (2) n | 3^n - 1
    (3) n不是2或3的倍数
  verified_solution: |
    预期思路：对n的每个素因子p，分别用模p分析2和3的阶。互补协同组合。unverified。
  bare_status: |
    not_run。尚未bare测试。
    预测AI可能只分析一个条件而忽略另一个，或尝试直接枚举n。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始对素因子p取模分析
    2. AI分别分析2和3的阶
    3. AI组合两个分析结果
  leakage_risk: low
  frozen_role: composition
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| bare真实失败 | 不通过 | 尚未bare测试 |
| 解答可核验 | 不通过 | unverified |
| 泄漏安全 | 通过 | leakage_risk: low |
| 经典风险可控 | 通过 | classicality_risk: medium→可控 |
| 过程可观察 | 通过 | 模p分析+组合过程在thinking中可观察 |

**注**：测试POC-5（可组合）——互补协同：模p分析2的阶 + 模p分析3的阶，互相增强。

---

# 七、5否决项审查汇总

## 7.1 按否决项汇总

| 否决项 | 通过 | 不通过 | 不适用 | 待确认 |
|---|---|---|---|---|
| bare真实失败 | CC-001~004, 007（5道） | CC-008~012, 021, 022（7道未跑） | CC-013~020（10道假朋友/边界题不要求） | CC-005, 006（2道弱/边界正迁移） |
| 解答可核验 | CC-001, 002, 003, 006, 007, 013, 017（7道verified） | CC-009~012, 016, 018~022（10道unverified） | — | CC-004, 005, 014, 015（4道partial） |
| 泄漏安全 | CC-001~007, 009~017, 018~020, 022（20道low） | — | — | CC-008, 021（2道medium） |
| 经典风险可控 | CC-001~004, 007~012, 015, 017~018, 020~021（15道low/可控） | CC-006（1道high） | — | CC-005, 013~014, 016, 019, 022（6道medium→待确认） |
| 过程可观察 | CC-001~004, 007~014, 017~022（18道） | — | — | CC-005, 006, 015, 016（4道信号可能微弱） |

## 7.2 按题目汇总

| 题号 | bare | 解答 | 泄漏 | 经典 | 过程 | 总体 |
|---|---|---|---|---|---|---|
| CC-001 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-002 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-003 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-004 | ✅ | ⚠️待确认 | ✅ | ✅ | ✅ | 通过（解答待完整核验） |
| CC-005 | ⚠️待确认 | ⚠️待确认 | ✅ | ⚠️待确认 | ⚠️待确认 | 弱正迁移候选 |
| CC-006 | ✅ | ✅ | ✅ | ❌不通过 | ⚠️待确认 | 经典风险高——用于boundary测试 |
| CC-007 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-008 | ❌未跑 | ⚠️待确认 | ⚠️待确认 | ✅ | ✅ | 待bare验证 |
| CC-009 | ❌未跑 | ❌未核验 | ✅ | ✅ | ✅ | 待bare+解答核验 |
| CC-010 | ❌未跑 | ❌未核验 | ✅ | ✅ | ✅ | 待bare+解答核验 |
| CC-011 | ❌未跑 | ❌未核验 | ✅ | ✅ | ✅ | 待bare+解答核验 |
| CC-012 | ❌未跑 | ❌未核验 | ✅ | ✅ | ✅ | 待bare+解答核验 |
| CC-013 | N/A | ✅ | ✅ | ✅ | ✅ | 通过 |
| CC-014 | N/A | ⚠️待确认 | ✅ | ✅ | ✅ | 通过（解答partial） |
| CC-015 | N/A | ⚠️待确认 | ✅ | ✅ | ✅ | 通过（解答partial） |
| CC-016 | N/A | ❌未核验 | ✅ | ✅ | ✅ | 通过（解答未核验） |
| CC-017 | N/A | ✅ | ✅ | ✅ | ✅ | 通过 |
| CC-018 | N/A | ❌未核验 | ✅ | ✅ | ✅ | 通过（解答未核验） |
| CC-019 | N/A | ❌未核验 | ✅ | ✅ | ✅ | 通过（解答未核验） |
| CC-020 | N/A | ❌未核验 | ✅ | ✅ | ✅ | 通过（解答未核验） |
| CC-021 | ❌未跑 | ❌未核验 | ⚠️待确认 | ✅ | ✅ | 待bare+解答核验+泄漏确认 |
| CC-022 | ❌未跑 | ❌未核验 | ✅ | ✅ | ✅ | 待bare+解答核验 |

## 7.3 可立即用于POC的题（5否决项全部通过或仅不适用项）

- **CC-001, CC-002, CC-003, CC-007**：全部通过——强证据题，可直接用于所有POC
- **CC-013, CC-017**：假朋友题全部通过——可直接用于selector测试
- **CC-004**：通过（解答待完整核验）——source trace题，特殊价值（方向vs路径）

## 7.4 需要后续验证才能使用的题

- **需bare验证**：CC-008（人工构造正迁移候选）
- **需bare+解答核验**：CC-009~012（变形题）, CC-021, CC-022（组合题）
- **需解答核验**：CC-016, CC-018, CC-019, CC-020
- **需解答完整核验**：CC-004（partial→verified）, CC-005（partial→verified）, CC-014, CC-015（partial→verified）

## 7.5 特殊标注

- **CC-006**：经典风险high——保留用于测试selector在跨域场景中的boundary决策
- **CC-008**：泄漏风险medium——如果bare验证后AI在bare中就想到Fermat小定理，应移入exclusion_log
- **CC-014, CC-017**：假朋友拒绝需要critic协同（383号POC-1发现）——trigger可能误触发
