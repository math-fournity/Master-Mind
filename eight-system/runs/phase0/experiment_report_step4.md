# Phase 0 Step 4 实验报告：Continue实验与Token Efficiency假说的修正

> **日期**：2026-08-15
> **实验ID**：eight-p0-1631-step4
> **基础**：Phase 0 (eight-p0-1631-001) 的后续验证
> **状态**：COMPLETED

---

## 1. 实验动机

Phase 0发现L和D都找到了QR/Euler路线但hit token limit，只有LD完成proof。初步假说：TellCore v0的价值在于token efficiency。

**验证方法**：用`devin -c`（continue）恢复L/D/R的session，给它们额外的token预算来完成proof。如果L在continue后立即输出proof（因为thinking中已完成），则验证token efficiency假说。

## 2. Continue实验结果

| Arm | 原始thinking | Continue结果 | Continue输出 |
|---|---|---|---|
| R (bare) | 无QR/Euler，case analysis（53K chars） | **FAILED** — 仍无QR/Euler，继续case analysis，hit token limit | 无 |
| L (lineage) | **QR/Euler found，proof completed in thinking**（105K chars） | **SUCCESS** — 立即输出了完整proof | 完整proof + ### PROOF COMPLETE |
| D (direction) | QR/Euler found，proof NOT completed（105K chars） | **FAILED** — thinking从头开始，hit token limit | 无 |
| LD (lineage+direction) | QR/Euler found，proof completed（一次成功） | （不需要continue） | 完整proof + ### PROOF COMPLETE |

## 3. 关键发现

### 发现1：L在thinking中已完成完整证明

L的thinking（105K chars）末尾包含了完整的证明：
- x₃≡7(mod 8) → 2是x₃的QR → Euler准则 → ord_{x₃}(2) | (x₃-1)/2 = x₂ → x₃ | y₂（矛盾）
- 甚至额外处理了a≡0/1/2 mod 3的所有子情形（比LD更完整）

continue后L**立即输出了完整proof**，没有重新推理。这证明L的thinking已经完成了证明，只是原始token预算不足以输出。

### 发现2：D在thinking中未完成证明

D的thinking（105K chars）虽然找到了QR/Euler方向，但**没有完成证明**。thinking末尾在探索Z[√2]范数和递推关系，偏离了QR/Euler路线。

continue后D的thinking**从头开始**（"Let me solve this problem carefully"），没有利用之前的推理，再次hit token limit。

### 发现3：R在continue后仍未找到正确方向

R的continue thinking（53K chars）仍然没有QR/Euler（0 mentions），继续做case analysis，hit token limit。

### 发现4：Lineage提供的是认知支架，不仅仅是token节省

**原假说修正**：TellCore v0 + lineage的价值不是"token efficiency"（节省token），而是"**认知支架**"（cognitive scaffold）。

证据：
- L和D的thinking长度相似（105K chars），但L完成了证明而D没有。如果是token efficiency，两者应该都完成或都不完成。
- L从x₃≡7(mod 8)的预计算context出发，直接进入QR/Euler分析；D从题目出发，需要自己推导到x₃≡7(mod 8)再进入QR/Euler，中间消耗了大量token在探索其他方向。
- Lineage提供的不仅是"省去的计算步骤"，更是"**推理的锚点**"——AI知道从哪里开始，不需要探索。

### 发现5：Direction alone不足以引导proof completion

D有direction hint（明确提到mod 8 + QR + Euler准则），找到了正确路线，但**没有完成证明**。原因：
- Direction告诉AI"用什么工具"，但不告诉AI"从哪里开始"
- D在thinking中先探索了多种其他方法（Z[√2]范数、递推关系、Mersenne素数列表），最后才回到QR/Euler，但token已耗尽
- Direction需要lineage的锚点才能有效转化为proof completion

## 4. 修正后的因果模型

```
原假说（token efficiency）：
  lineage节省token + direction节省token → proof completion

修正假说（cognitive scaffold）：
  lineage提供推理锚点 → AI从正确位置开始 → thinking高效完成证明
  direction提供工具提示 → AI知道用什么工具 → 但不知道从哪里开始
  lineage + direction → AI从正确位置开始 + 知道用什么工具 → proof completion
```

## 5. 对TellCore v0的修正理解

| 维度 | 原理解 | 修正后理解 |
|---|---|---|
| Direction hint的作用 | 告诉AI它不知道的信息 | 提供工具提示（AI可能自己发现） |
| Lineage的作用 | 节省token（预计算context） | **提供认知支架**（推理锚点） |
| TellCore v0的核心价值 | 信息传递 | **认知支架 + 工具提示的组合** |
| Proof completion的机制 | token efficiency | **从正确位置开始 + 用正确工具** |

## 6. Contrast修正

### 原Phase 0 contrast（proof level）

| Contrast | 值 | 原解释 | 修正解释 |
|---|---|---|---|
| C1 (LD−L) | 1 | direction增加proof完成 | direction在lineage基础上提供工具提示，使proof在原始预算内完成 |
| C2 (LD−L)−(D−R) | 1 | direction依赖lineage | direction需要lineage的锚点才能转化为proof completion |
| C3 (LD−R) | 1 | 总效果 | lineage+direction的组合效果 |

### 新增Step 4 contrast（continue后）

| Contrast | 值 | 含义 |
|---|---|---|
| L_continue − D_continue | 1 | lineage的continue效果远超direction（L完成，D失败） |
| L_continue − R_continue | 1 | lineage的continue效果远超bare（L完成，R失败） |
| L_original_thinking_completed | 1 | L在原始thinking中已完成证明（continue立即输出） |
| D_original_thinking_completed | 0 | D在原始thinking中未完成证明（continue从头开始） |

## 7. 对钟形曲线理论的实证补充

> **关联方案章节**：§2.3-2.6（去特化产出是Tell、Tell族的钟形曲线、三步法找峰值、Tell的三种形态）

### 7.1 原有理论回顾

钟形曲线（§2.4）描述的是：同一条trace被不同去特化程度（Level）处理后，得到的Tell族中每个Tell对AI的**指导力**随Level变化的规律。

- Level 0（不去特化）：指导力低——太具体，只对原题有用
- Level ∞（过度去特化）：指导力也低——太抽象，AI不知道怎么用（280号实验已验证）
- **中间某处**：指导力最高——既保留可操作的关系结构，又剥离表面特征

§2.6已有一个修正：钟形曲线不是一条固定曲线，而是**曲线族**——同一Level的Tell，提示词形态不同，指导力不同。

### 7.2 Phase 0的实证发现：指导力需要分层测量

Phase 0的4组对照结果给钟形曲线增加了一个新的维度——**指导力不是单一标量，需要分层测量**：

| 层次 | R (Level 0) | L (中间) | D (中间) | LD (中间) |
|---|---|---|---|---|
| Route finding（找到正确方向） | 低 | **高** | **高** | **高** |
| Proof completion（完成证明输出） | 低 | 低（hit limit） | 低（hit limit） | **高** |

**关键观察**：L和D在route finding层面已经接近峰值，但在proof completion层面还差一点。只有LD在两个层面都到了峰值。

这说明钟形曲线的"峰值"不是一个点，而是**取决于你测量什么**：
- 在route finding层面，L和D都已经接近峰值
- 在proof completion层面，只有LD在峰值

### 7.3 Step 4的进一步发现：认知峰值 vs 执行峰值

Step 4 continue实验进一步发现：L在thinking中**已经完成了完整证明**（105K chars thinking，包含所有5个关键步骤），只是没能输出（hit token limit）。continue后L立即输出了完整proof。

这意味着L的指导力在**认知层面**其实已经到了峰值（AI想到了完整证明），但在**执行层面**（token预算内完成输出）还差一点。Direction提供的工具提示补上了这最后一点——不是补在"想到什么"上，而是补在"多快想到"上，从而节省了token用于输出。

### 7.4 对钟形曲线理论的修正

**修正1：钟形曲线的峰值取决于测量维度**

原理论隐含假设"指导力"是单一标量。Phase 0实证表明指导力至少有两个维度：
- **认知指导力**（route finding + thinking中完成证明的能力）
- **执行指导力**（在有限token预算内完成proof输出的能力）

同一Tell在这两个维度上的峰值可能出现在不同Level。L在认知维度已到峰值，但在执行维度还差一点；LD在两个维度都到了峰值。

**修正2：与§2.6曲线族修正的一致性**

这个发现与§2.6的"曲线族"修正一致：钟形曲线的形状取决于你测量指导力的哪个维度。§2.6说"同一Level的Tell，提示词形态不同，指导力不同"——Phase 0补充说"同一Level的Tell，测量维度不同，峰值位置不同"。

**修正3：三步法找峰值需要指定测量维度**

§2.5的三步法找峰值需要补充：在步骤3"检查可操作性"时，必须指定测量维度——是route finding的可操作性，还是proof completion的可操作性？不同维度的峰值可能需要不同的Tell设计。

### 7.5 对下一步实验的启示

1. **Phase 1跨题验证**：需要同时测量route finding和proof completion两个维度，不能只看proof completion
2. **Lineage分解实验**：lineage的哪部分影响route finding的峰值？哪部分影响proof completion的峰值？
3. **Direction精度实验**：更精确的direction能否提高proof completion维度的峰值（即使不提高route finding维度的峰值）？

## 8. 下一步

1. **Phase 1**：在1843/1709/1962上验证"认知支架"假说——预测lineage的锚点效应跨题成立
2. **Lineage分解实验**：lineage中哪部分是关键锚点？是x₃≡7(mod 8)这个结论，还是推导到这个结论的过程？
3. **Direction精度实验**：如果direction更精确（直接说"从x₃≡7(mod 8)出发用Euler准则"），D能否完成proof？
