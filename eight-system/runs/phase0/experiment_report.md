# Phase 0 实验报告：TellCore v0 在1631题上的R/L/D/LD四组对照

> **日期**：2026-08-15
> **实验ID**：eight-p0-1631
> **预注册文档**：preregistration.md
> **状态**：COMPLETED
>
> **⚠️ 更新说明（2026-08-15）**：本报告记录了Phase 0原始4组对照的结果。
> §5-8中的"token efficiency"假说和"Token budget实验"作为下一步——
> 这些已被Step 4 continue实验修正。Step 4发现：
> - L在thinking中已完成完整证明（continue后立即输出），D未完成（continue后从头开始再次失败）
> - 假说从"token efficiency"修正为"cognitive scaffold"（认知支架）
> - 详见 [experiment_report_step4.md](experiment_report_step4.md) 和 [evidence_record_001.md](evidence_record_001.md)

---

## 1. 实验概述

在1631题（Mersenne型递推素数长度）上验证TellCore v0（局部-全局表示切换）的因果效应，通过R/L/D/LD四组对照隔离lineage和direction各自的因果贡献。

## 2. Arms

| Arm | 名称 | 内容 | Session |
|---|---|---|---|
| R | problem-only | 只有题目 | typical-scarf |
| L | lineage-only | 题目+脉络（推理到x₃≡7(mod 8)），不给方向 | sunrise-board |
| D | direction-only | 题目+方向提示（模p+二次剩余+Euler准则），不给脉络 | antique-copper |
| LD | lineage+direction | 题目+脉络+方向提示 | foul-cantaloupe |

## 3. 结果

| Arm | 路线层 | 证明层 | 落盘层 | Verdict | Token Limit |
|---|---|---|---|---|---|
| R | FAIL | FAIL | FAIL | FAILED | YES (hit limit) |
| L | **SUCCESS** | partial (4/5 steps) | FAIL | ROUTE_ONLY | YES (hit limit) |
| D | **SUCCESS** | partial (4/5 steps) | FAIL | ROUTE_ONLY | YES (hit limit) |
| LD | **SUCCESS** | **SUCCESS** (5/5) | **SUCCESS** | **SUCCESS** | NO (completed) |

### 路线层详情

- **R (bare)**：thinking中做case analysis（a=1,2,3,5,7,13...），未找到QR/Euler方向。thinking被token limit截断。
- **L (lineage)**：thinking中**自己发现了QR/Euler方向**！从x₃≡7(mod 8)出发，推导出"2 is a quadratic residue mod p (since (2/p) = (-1)^{(p²-1)/8} = 1 when p ≡ ±1 (mod 8))"，应用Euler准则得到2^{(p-1)/2} ≡ 1 (mod p)。8处"quadratic residue"，2处"Euler's criterion"。但hit token limit未完成最后一步（x₃ | y₂）。
- **D (direction)**：thinking中**引用了hint**："The hint mentions mod 8 and quadratic residues / Euler's criterion"，并开始用Euler准则分析。但hit token limit未完成。
- **LD (lineage+direction)**：**完成完整证明**。proof包含所有5个关键步骤：mod8分析、QR判定、Euler准则、指数关系(x₃-1)/2=x₂、整除关系x₃|y₂。输出### PROOF COMPLETE。

### 证明层详情（5个关键步骤）

| 步骤 | R | L | D | LD |
|---|---|---|---|---|
| 1. x₃≡7(mod 8) | ✓ | ✓ | ✓ | ✓ |
| 2. 2是x₃的QR | ✗ | ✓ | ✓ | ✓ |
| 3. Euler准则 | ✗ | ✓ | ✓ | ✓ |
| 4. (x₃-1)/2=x₂ | ✓ | ✓ | ✓ | ✓ |
| 5. x₃\|y₂ (矛盾) | ✗ | ✗ | ✗ | ✓ |

## 4. Contrasts

### Proof Level（完成证明）

| Contrast | 值 | 含义 |
|---|---|---|
| C1: LD−L | **1** | direction在lineage基础上增加proof完成 |
| C2: (LD−L)−(D−R) | **1** | direction依赖lineage才能完成proof |
| C3: LD−R | **1** | 总效果：完整干预包 vs bare |

### Route Level（找到目标方向）

| Contrast | 值 | 含义 |
|---|---|---|
| C1: LD−L | **0** | direction不增加route finding（L已自己找到） |
| C2: (LD−L)−(D−R) | **-1** | direction单独时route效果更强（D从0到1，L已从0到1） |
| C3: LD−R | **1** | 总效果：完整干预包 vs bare |

## 5. 关键发现

### 发现1：Lineage alone足以引导route finding

**L（只有脉络）自己发现了QR/Euler方向。** 从x₃≡7(mod 8)这个条件出发，AI独立推导出了二次剩余判定和Euler准则的应用。这说明TellCore v0的direction hint**不是在告诉AI它不知道的信息**——AI有能力从脉络中自己发现正确的数学方向。

### 发现2：Direction alone也足以引导route finding

**D（只有方向）**从hint中直接获得了QR/Euler方向，并开始应用。这验证了TellCore v0的direction hint的有效性——它确实指向了正确的数学方向。

### 发现3：Route finding ≠ Proof completion

**L和D都找到了正确路线，但都没完成证明。** 两者都hit了max output token limit。只有LD（lineage+direction）在token预算内完成了证明。

这说明TellCore v0的价值**不在于route finding（AI自己能做到），而在于token efficiency**：
- Lineage提供预计算context（省去AI重新推导x₃≡7(mod 8)等步骤的token）
- Direction提供明确方向（省去AI探索各种可能性的token）
- 两者结合提供了足够的token效率来完成proof

### 发现4：Proof-level C2=1 表明lineage和direction在proof completion上有交互效应

D alone（direction but no lineage）找到了路线但没完成proof。LD（direction + lineage）完成了proof。差异在于lineage提供的预计算context节省了token，使得AI有足够的token预算来完成proof的最后一步。

## 6. 对TellCore v0的验证状态

| 验证项 | 状态 | 证据 |
|---|---|---|
| TellCore v0的direction指向正确方向 | ✅ 验证 | D和LD都使用了QR/Euler方向 |
| TellCore v0的direction是必要的 | ⚠️ 部分修正 | L自己也能找到方向，direction不是唯一路径 |
| TellCore v0的direction+lineage组合有效 | ✅ 验证 | LD是唯一完成proof的arm |
| TellCore v0的价值在于token efficiency | ✅ 新发现 | L和D都找到路线但hit token limit，LD在预算内完成 |

## 7. 混淆因素

1. **Token limit**：R/L/D都hit了max output token limit。如果token预算更大，L和D可能也能完成proof。但LD在相同预算内完成，说明组合干预的token效率更高。
2. **单次运行**：每个arm只跑了一次，无法估计variance。需要多次运行确认结果的稳定性。
3. **单题验证**：只在1631题上验证，无法确认TellCore v0在其他题目上的效果。

## 8. 下一步

1. **Phase 0扩展**：在1631上多次运行（至少3次）确认结果稳定性
2. **Phase 1**：在3-5道不同题目上验证TellCore v0的泛化性
3. **Token budget实验**：增大token预算，测试L和D是否能完成proof（验证token efficiency假说）
4. **Selector验证**：测试Selector能否从题目特征预测TellCore v0的适用性
