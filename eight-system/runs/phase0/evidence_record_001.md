# EvidenceRecord: eight-p0-1631-001

> **ID**: eight-p0-1631-001
> **日期**: 2026-08-15
> **类型**: contrast-level evidence
> **实验**: Phase 0 R/L/D/LD四组对照
> **题目**: 1631 (Mersenne型递推素数长度)
> **TellCore**: TellCore_v0_local_global_switch (局部-全局表示切换)

---

## Evidence

### Contrast结果

**Proof Level:**
- C1 (LD−L) = 1: direction在lineage基础上增加proof完成
- C2 (LD−L)−(D−R) = 1: direction依赖lineage才能完成proof（交互效应）
- C3 (LD−R) = 1: 总效果

**Route Level:**
- C1 (LD−L) = 0: direction不增加route finding（L自己找到了）
- C2 (LD−L)−(D−R) = -1: direction单独时route效果更强
- C3 (LD−R) = 1: 总效果

### 核心观察

1. **L (lineage only) 自己发现了QR/Euler方向** — thinking中8处"quadratic residue"，2处"Euler's criterion"，推导出了2^{(p-1)/2}≡1(mod p)
2. **L和D都找到了路线但hit token limit** — 只有LD在token预算内完成proof
3. **LD完成了完整证明** — 5/5关键步骤，输出### PROOF COMPLETE

## Inference

### TellCore v0的direction hint不是在提供AI不知道的信息

L从x₃≡7(mod 8)的脉络中**独立发现了**二次剩余和Euler准则的方向。AI有能力从局部条件出发找到正确的数学工具。TellCore v0的direction hint不是唯一路径。

### TellCore v0的价值在于token efficiency

- L找到路线但hit token limit（105K chars thinking，未完成proof）
- D找到路线但hit token limit（未完成proof）
- LD在token预算内完成proof（lineage节省context推导token + direction节省探索token）

TellCore v0 + lineage的组合通过提高token效率使得proof completion成为可能，而不是通过提供AI无法自己发现的信息。

### Lineage和direction在proof completion上有正向交互效应

C2 (proof level) = 1 表明direction需要lineage才能实现proof completion。Direction alone (D) 虽然找到路线，但没有lineage的预计算context，token不够完成proof。

## Validity

### 内部效度
- ✅ 预注册冻结：在看到结果前冻结了arms、contrasts、成功标准
- ✅ 资源契约一致：所有arm使用相同模型、相同token预算
- ⚠️ 单次运行：无法估计variance
- ⚠️ Token limit混淆：R/L/D都hit token limit，可能低估了L和D的潜力

### 外部效度
- ⚠️ 单题验证：只在1631题上验证
- ⚠️ TellCore v0只有一个：无法比较不同TellCore的效果

## Step 4 Continue实验补充（2026-08-15）

> **详细报告**：`experiment_report_step4.md`

### Continue实验结果

用`devin -c`恢复R/L/D的session，给额外token预算：

| Arm | Continue结果 | 关键观察 |
|---|---|---|
| R | FAILED — 仍无QR/Euler，hit token limit | continue thinking从头开始，继续case analysis |
| L | **SUCCESS** — 立即输出完整proof | thinking中已完成证明，continue直接输出 |
| D | FAILED — thinking从头开始，hit token limit | 找到QR/Euler但未完成证明，continue未利用之前推理 |

### 假说修正

**原假说（token efficiency）修正为（cognitive scaffold）**：
- L和D的thinking长度相似（105K chars），但L完成证明而D没有 → 不是token数量问题
- L从x₃≡7(mod 8)的预计算context出发，直接进入QR/Euler → lineage提供推理锚点
- D从题目出发，探索多种方向后才回到QR/Euler，token耗尽 → direction提供工具但不提供锚点
- **Lineage的核心价值是认知支架（推理锚点），不是token节省**

### Confidence更新

**High confidence:**
- LD > R in proof completion (1 vs 0)
- L found QR/Euler direction independently (8 matches in thinking)
- L completed full proof in thinking (continue immediately output it)
- D did NOT complete proof in thinking (continue started from scratch and failed)
- **Cognitive scaffold is the mechanism, not token efficiency**

**Medium confidence:**
- Lineage × direction interaction in proof completion (需要多次运行确认)
- Direction alone enables route finding but not proof completion (需要更多题目验证)

**Low confidence:**
- Generalization to other problems (需要Phase 1跨题验证)
- Which part of lineage is the key anchor (需要lineage分解实验)
