# Phase 1 实验报告：TellCore v0 跨题泛化验证（1843/1709/1962）

> **日期**：2026-08-15
> **实验ID前缀**：eight-p1
> **预注册文档**：preregistration.md（FROZEN）
> **状态**：COMPLETED
> **对应方案§8.5**：Step 5

---

## 1. 实验概述

在3道bare失败题（1843/1709/1962）上验证TellCore v0（局部-全局表示切换）的因果效应，通过R/L/D/LD四组对照隔离lineage和direction各自的因果贡献。验证Phase 0在1631上发现的"认知支架"假说是否跨题成立。

与Phase 0的关键区别：Phase 1是3道题×4组=12次运行，不是1道题4次运行。

## 2. 题目

| 题号 | 领域 | 预期答案 | 283号tree组状态 | 在Phase 1中的角色 |
|---|---|---|---|---|
| 1843 | Algebra | 2016 | bare失败，tree成功 | 与1631类似的P0题 |
| 1709 | Number Theory | a∈{1,3,5} | bare失败（tree组数据缺失） | lineage效应验证 |
| 1962 | Number Theory | (2,2,2),(2,2,3),(2,3,2),(3,2,2),(2,6,11),(2,11,6) | bare失败，tree仍失败 | **关键测试**——操作路径瓶颈 |

## 3. Arms（4组对照 × 3道题 = 12次原始运行 + 10次continue运行）

每道题跑与Phase 0相同的4组对照：

| Arm | 名称 | 内容 |
|---|---|---|
| R | problem-only | 只有题目 |
| L | lineage-only | 题目+脉络（从283号tree组提取），不给方向 |
| D | direction-only | 题目+方向提示（TellCore v0的direction hint），不给脉络 |
| LD | lineage+direction | 题目+脉络+方向提示 |

**Continue实验**：对每个hit token limit的arm，做1次continue运行（`devin -r <session_id>`恢复session后发送"请继续完成证明"）。

## 4. 原始运行结果（12次）

### 4.1 总览

| 题 | Arm | 路线层 | 证明层(thinking) | 证明层(output) | Verdict | Exit Code | Thinking长度 |
|---|---|---|---|---|---|---|---|
| 1843 | R | FAIL | FAIL | FAIL | FAILED | 1(token limit) | 127K |
| 1843 | L | **SUCCESS** | PARTIAL | FAIL | ROUTE_ONLY | 1(token limit) | 116K |
| 1843 | D | **SUCCESS** | FAIL | FAIL | ROUTE_ONLY | 1(token limit) | 114K |
| 1843 | LD | **SUCCESS** | FAIL | FAIL | ROUTE_ONLY | 1(token limit) | 109K |
| 1709 | R | **SUCCESS** | FAIL | FAIL | ROUTE_ONLY | 1(token limit) | 112K |
| 1709 | L | **SUCCESS** | **SUCCESS** | **SUCCESS** | **SUCCESS** | 0 | 135K |
| 1709 | D | **SUCCESS** | FAIL | FAIL | ROUTE_ONLY | 1(token limit) | 101K |
| 1709 | LD | **SUCCESS** | **SUCCESS** | **SUCCESS** | **SUCCESS** | 0 | 67K |
| 1962 | R | **SUCCESS** | PARTIAL | FAIL | ROUTE_ONLY | 1(token limit) | 159K |
| 1962 | L | **SUCCESS** | FAIL | FAIL | ROUTE_ONLY | 1(token limit) | 101K |
| 1962 | D | **SUCCESS** | FAIL | FAIL | ROUTE_ONLY | 1(token limit) | 195K |
| 1962 | LD | **SUCCESS** | FAIL | FAIL | ROUTE_ONLY | 1(token limit) | 116K |

### 4.2 路线层详情

**1843（mod 4分组方向）**：
- R：thinking中**未找到**mod 4分组方向（0 mentions），做多项式符号分析和case analysis
- L：thinking中**找到了**mod 4分组——"A = {k ≡ 0,1 (mod 4)}, B = {k ≡ 2,3 (mod 4)}"（6 mentions）
- D：thinking中**引用了hint**并使用mod 4分组（59 mentions）
- LD：thinking中**使用了**mod 4分组（64 mentions）

**1709（2-adic赋值方向）**：
- R：thinking中**自然使用了**v_2/2-adic分析（116 mentions）——因为t(k)本身就是关于2-adic的
- L：thinking中**使用了**v_2分析（65 mentions），并完成证明
- D：thinking中**使用了**v_2分析（124 mentions），但未完成证明
- LD：thinking中**使用了**v_2分析（17 mentions），并完成证明

**1962（2-adic+case分析方向）**：
- R：thinking中**使用了**v_2和case分析（171+69 mentions），计算找到答案(2,2,2)等但未完成证明
- L/D/LD：均**使用了**v_2和case分析，但均未完成证明

### 4.3 证明层详情

**1843**：
- L的thinking找到了答案2016和关键证明思路（mod 4分组构造 + 无实根证明 + 最优性论证），但在论证|A|=|B|的必要性时hit token limit——**thinking部分完成但未完全完成**
- D/LD的thinking虽然找到了mod 4方向，但在证明无实根的具体论证中陷入复杂分析，未完成

**1709**：
- L的thinking**完成了完整证明**——"Everything checks out. Now let me write the complete proof. The answer is a ∈ {1, 3, 5}"，输出### PROOF COMPLETE
- LD的thinking**完成了完整证明**——"All verified. Now let me write the complete proof."，输出### PROOF COMPLETE
- R/D的thinking虽然找到了v_2方向，但在处理一般a的情况时陷入复杂分析，未完成

**1962**：
- R的thinking通过计算找到了正确答案(2,2,2),(2,2,3),(2,3,2),(3,2,2),(2,6,11),(2,11,6)，并说"Now let me write a complete proof"——但hit token limit未完成证明
- L/D/LD的thinking均未完成证明，陷入2-adic赋值的复杂代数

## 5. Continue实验结果（10次）

| 题 | Arm | Continue结果 | 关键观察 |
|---|---|---|---|
| 1843 | R | **FAILED** | continue后继续做符号分析，hit token limit |
| 1843 | L | **FAILED** | continue后继续论证|A|=|B|，hit token limit |
| 1843 | D | **FAILED** | continue后继续分析，hit token limit |
| 1843 | LD | **FAILED** | continue后继续分析，hit token limit |
| 1709 | R | **FAILED** | continue后继续case analysis，hit token limit |
| 1709 | D | **FAILED** | continue后继续分析，hit token limit |
| 1962 | R | **FAILED** | continue后继续分析，hit token limit |
| 1962 | L | **FAILED** | continue后继续2-adic分析，hit token limit |
| 1962 | D | **FAILED** | continue后继续分析，hit token limit |
| 1962 | LD | **FAILED** | continue后用计算工具探索30+分钟，hit token limit 51次 |

**1709-L和1709-LD不需要continue**（原始运行已成功）。

**关键发现**：所有10次continue实验都失败了。这与Phase 0形成鲜明对比——Phase 0中L-continue立即输出了完整proof（thinking中已完成证明），但Phase 1中没有任何continue实验成功。

## 6. Contrasts

### 6.1 主contrast（每道题独立计算）

**1843**：

| Contrast | Proof Level | Route Level | 含义 |
|---|---|---|---|
| C1: LD−L | 0 | 0 | direction无增量效果（两者都未完成proof，都找到route） |
| C2: (LD−L)−(D−R) | 0 | -1 | route层面direction单独时效果更强（D从0到1，L已从0到1） |
| C3: LD−R | 0 | 1 | route层面总效果（LD找到route，R没有） |

**1709**：

| Contrast | Proof Level | Route Level | 含义 |
|---|---|---|---|
| C1: LD−L | 0 | 0 | direction无增量效果（L和LD都完成proof，都找到route） |
| C2: (LD−L)−(D−R) | 0 | 0 | 无交互效应（所有arm都找到route） |
| C3: LD−R | **1** | 0 | proof层面总效果（LD完成proof，R没有） |

**1962**：

| Contrast | Proof Level | Route Level | 含义 |
|---|---|---|---|
| C1: LD−L | 0 | 0 | direction无增量效果（都未完成proof，都找到route） |
| C2: (LD−L)−(D−R) | 0 | 0 | 无交互效应 |
| C3: LD−R | 0 | 0 | 无总效果（都未完成proof，都找到route） |

### 6.2 跨题contrast

| Contrast | 值 | 含义 |
|---|---|---|
| C4: L_continue成功率 | **0/2 = 0%** | 认知支架假说跨题成立程度——**不成立**（1843-L和1962-L的continue都失败） |
| C5: 1962 LD − 1631 LD | **-1** | TellCore v0对操作路径瓶颈题的适用边界——**1962是边界**（1631 LD成功，1962 LD失败） |

## 7. 关键发现

### 发现1：1709复现了Phase 0的"认知支架"模式

1709-L在thinking中完成了完整证明并输出PROOF COMPLETE，1709-LD也成功。这与Phase 0的1631-L模式一致——lineage提供认知支架（推理锚点），使AI在thinking中完成证明。

**但1709-L不需要continue就成功了**——与Phase 0的1631-L不同（1631-L需要continue才能输出）。1709-L在原始token预算内就完成了proof输出。

### 发现2：1843的"认知支架"部分成立但不充分

1843-L找到了正确的mod 4分组方向和答案2016，thinking中包含了关键证明思路（构造 + 无实根证明 + 最优性论证）。但thinking**未完全完成**——在论证|A|=|B|必要性时hit token limit。

continue后1843-L继续论证但仍hit token limit——**与Phase 0的1631-L不同**（1631-L的thinking完全完成了证明，continue后立即输出）。

这说明"认知支架"效应在1843上**部分成立但不充分**——lineage帮助AI找到正确方向和关键思路，但不足以让AI在thinking中完全完成证明。

### 发现3：1843上LD未成功——与Phase 0和预测都不同

Phase 0中1631-LD是唯一完成proof的arm。但Phase 1中1843-LD也hit token limit未完成。这是一个**意外结果**——预注册预测1843-LD会成功（"与1631类似，LD完成proof输出"）。

可能原因：1843的证明比1631更复杂——需要同时论证构造的正确性（无实根）和最优性（2016是最小值），两部分都需要详细的符号分析。即使有lineage+direction，token预算也不够完成两部分。

### 发现4：1962确实是TellCore v0的适用边界

1962的所有arm（R/L/D/LD）都找到了v_2和case分析方向（route层全SUCCESS），但都没有完成证明。即使1962-LD（lineage+direction）也失败，continue后用计算工具探索30+分钟仍失败。

这验证了预注册的关键预测：**1962的瓶颈不是"找不到工具"而是"不知道操作路径"**。TellCore v0的direction hint是方向性的（"用2-adic赋值"），不是操作路径性的（"分a=b, a<b<c等case，每个case用不同的分析方法"）。

C5 = -1（1962 LD失败，1631 LD成功）确认了TellCore v0的适用边界。

### 发现5：所有continue实验都失败了

Phase 0中L-continue成功是因为L的thinking已经完成了完整证明。Phase 1中：
- 1709-L不需要continue（原始运行已成功）
- 1843-L的thinking部分完成但未完全完成，continue后继续论证但仍失败
- 1962-L的thinking未完成证明，continue后继续探索但仍失败

C4 = 0% 说明"lineage使thinking完成证明"的效应**不跨题稳定**——只在某些题（如1631、1709）上成立，在其他题（如1843、1962）上不成立。

### 发现6：route finding在1709和1962上不是瓶颈

1709和1962的所有arm（包括R/bare）都找到了正确的数学方向（v_2/2-adic）。这说明对于"自然涉及2-adic"的题（t(k)本身就是关于2-adic的，powers of 2本身就是关于2-adic的），route finding不是瓶颈——AI自然会想到2-adic。

这与1843形成对比——1843的mod 4分组是非显然的技巧，R（bare）没有想到，但L（lineage）和D（direction）都想到了。

## 8. 对"认知支架"假说的修正

### 8.1 Phase 0的假说

Phase 0提出：lineage提供"认知支架"（推理锚点），使AI在thinking中完成证明。direction提供"工具提示"（route finding）。两者组合使proof completion成为可能。

### 8.2 Phase 1的修正

Phase 1揭示了"认知支架"假说的**适用范围**：

1. **认知支架不是万能的**——lineage帮助AI找到正确方向和关键思路，但不一定能让AI在thinking中完全完成证明。1843-L找到了方向和思路但未完成，1962-L连思路都没完成。

2. **认知支架的效果取决于题目难度**——1709（相对简单）上L足以完成证明，1843（中等难度）上L部分完成，1962（高难度）上L无法完成。

3. **direction的增量效果在Phase 1中消失**——Phase 0中C1(LD-L)=1（direction在lineage基础上增加proof完成），但Phase 1中三道题的C1(LD-L)都是0。direction在Phase 1中没有提供额外的proof completion效果。

4. **continue实验的失败模式不同**——Phase 0中L-continue成功（thinking已完成），Phase 1中所有continue失败（thinking未完成）。这说明"认知支架使thinking完成证明"不是稳定效应。

### 8.3 修正后的因果模型

```
Phase 0模型（cognitive scaffold）：
  lineage提供推理锚点 → AI从正确位置开始 → thinking高效完成证明
  direction提供工具提示 → AI知道用什么工具 → 但不知道从哪里开始
  lineage + direction → proof completion

Phase 1修正模型（cognitive scaffold with difficulty threshold）：
  lineage提供推理锚点 → 帮助找到正确方向和关键思路
  但thinking是否完全完成证明 → 取决于题目难度
  - 简单题（1709）：lineage足以完成证明
  - 中等题（1843）：lineage帮助找到方向和思路，但不足以完全完成
  - 难题（1962）：lineage帮助找到方向，但无法完成证明（操作路径瓶颈）
  direction的增量效果 → 在Phase 1中消失（可能因为route finding不是瓶颈）
```

## 9. 与Phase 0的对比

| 维度 | Phase 0 (1631) | Phase 1 (1843) | Phase 1 (1709) | Phase 1 (1962) |
|---|---|---|---|---|
| R route | FAIL | FAIL | SUCCESS | SUCCESS |
| L route | SUCCESS | SUCCESS | SUCCESS | SUCCESS |
| D route | SUCCESS | SUCCESS | SUCCESS | SUCCESS |
| LD route | SUCCESS | SUCCESS | SUCCESS | SUCCESS |
| R proof | FAIL | FAIL | FAIL | FAIL |
| L proof | FAIL(hit limit) | FAIL(hit limit) | **SUCCESS** | FAIL(hit limit) |
| D proof | FAIL(hit limit) | FAIL(hit limit) | FAIL(hit limit) | FAIL(hit limit) |
| LD proof | **SUCCESS** | FAIL(hit limit) | **SUCCESS** | FAIL(hit limit) |
| L thinking完成 | **YES** | PARTIAL | **YES** | NO |
| L-continue | **SUCCESS** | FAILED | (不需要) | FAILED |
| C1(LD-L) proof | 1 | 0 | 0 | 0 |
| C5 vs 1631 | — | 0 | 0 | **-1** |

## 10. 对TellCore v0的验证状态

| 验证项 | Phase 0状态 | Phase 1状态 | 修正 |
|---|---|---|---|
| TellCore v0的direction指向正确方向 | ✅ 验证 | ✅ 验证（1843-D/LD找到mod4） | — |
| TellCore v0的direction是必要的 | ⚠️ 部分修正 | ❌ 不成立（1709/1962上R也找到route） | direction对"自然涉及2-adic"的题不是必要的 |
| TellCore v0的direction+lineage组合有效 | ✅ 验证 | ⚠️ 部分成立（1709-LD成功，1843/1962-LD失败） | 组合有效性取决于题目难度 |
| TellCore v0的价值在于认知支架 | ✅ 新发现 | ⚠️ 部分成立（1709-L成功，1843-L部分成功，1962-L失败） | 认知支架有难度阈值 |
| TellCore v0的适用边界 | 未测试 | ✅ 验证（1962是边界） | 操作路径瓶颈题不在覆盖范围内 |

## 11. 混淆因素

1. **Token limit**：10/12个原始运行hit了token limit。如果token预算更大，1843-L/D/LD可能也能完成proof。但1709-L在相同预算内完成，说明题目难度差异是真实存在的。
2. **单次运行**：每个arm只跑了一次，无法估计variance。
3. **1709的lineage来源**：1709不在283号tree组中，lineage来自vms10的interference文件（从bare thinking提取）。lineage质量可能与1843/1962不同。
4. **Continue实验的session恢复**：continue实验通过`devin -r`恢复session，可能存在session状态不完整的问题。1962-LD-continue运行了30+分钟用计算工具探索，但仍未完成。

## 12. 对"中"的定位的验证

| 验证内容 | "中"的来源 | 预期结果 | 实际结果 |
|---|---|---|---|
| 分层峰值跨题成立 | 345号钟形曲线 | 1843/1709上L在route层到峰值，proof层差一点 | **部分成立**——1709上L在两层都到峰值，1843上L在route层到峰值但proof层差一点 |
| 多峰曲线可能性 | 352号"非单调峰值假设" | 1962的峰值位置可能和1631不同 | **验证**——1962的峰值在route层（所有arm都到峰值），但proof层没有峰值（所有arm都失败） |
| 三个独立指标不合成 | 352号三个指标 | 路线层/证明层/落盘层分别记录 | ✅ 遵守——三层分别记录，未合成综合效用 |
| 不用帕累托前沿 | 拒绝372号 | 3道题×4组=12次运行的规模无法估计9维帕累托前沿 | ✅ 遵守——未引入帕累托前沿 |

## 13. 下一步

1. **Step 6（Lineage分解）**：lineage中哪部分是关键锚点？是结论还是推导过程？在1709上做L1/L2/L3对照
2. **1843的深入分析**：为什么1843-LD失败而1631-LD成功？是证明复杂度还是token预算问题？
3. **1962的操作路径Tell**：1962需要操作路径Tell而非方向Tell——这是TellCore v1的设计方向（但不在当前POC范围内）
4. **多次运行**：在1709上多次运行确认L成功的稳定性

## 14. 实验文件索引

| 文件 | 路径 | 用途 |
|---|---|---|
| 预注册文档 | runs/phase1/preregistration.md | FROZEN预注册 |
| Prompt文件 | runs/phase1/prompts/{题号}_{arm}.txt | 12个prompt文件 |
| Contrast结果 | runs/phase1/contrast_results.json | 自动计算的contrast |
| Contrast脚本 | scripts/contrast_calculator_phase1.py | Phase 1 contrast计算 |
| Continue启动脚本 | scripts/launch_continue.sh | continue实验启动脚本 |
| Trajectory数据 | /data/math-agent-glm5.2-tmux-agents-trajectory/eight-p1-* | 12个原始+10个continue的trajectory |
