# Phase 2 预注册文档 — Selector验证

> **状态**：DRAFT（待冻结）
> **实验ID前缀**：eight-p2
> **对应方案§8.5**：Step 7
> **"中"的定位**：验证352号的三个独立指标中的"误触发率"——Tell用在不该用的题上会跑偏

---

## 1. 实验目标

验证Selector能否从题目特征预测TellCore v0的适用性。具体回答：

1. **false_friend题**：TellCore v0的trigger_boundary会误触发吗？——如果误触发，AI拿到不匹配的Tell会跑偏（误触发率>0）
2. **boundary题**：TellCore v0的negative_boundary能正确拒绝边界题吗？——如果不能拒绝，AI拿到部分匹配的Tell可能走错误方向
3. **Selector的预测准确率**：Selector从题目特征预测的"适用/不适用"和实际运行结果一致吗？

## 2. 题目类型（3类）

### 2.1 true_positive题（应触发且应成功）

使用Phase 0/1中LD成功的题（如1631、1843）：
- 预测：Selector判定"适用" → LD成功

### 2.2 false_friend题（应拒绝但可能误触发）

构造与true_positive题表面相似但结构不同的题：
- **构造原则**：题目表面特征（如"递推""素数""模运算"）与true_positive相似，但解题需要的思维方向不同
- **候选**：CC-013结构（但数学解答必须正确——需要独立数学核验）
- **预测**：Selector应判定"不适用" → 如果Selector误判"适用"，LD会跑偏

### 2.3 boundary题（边界情况，应标为boundary）

构造true_positive题的变体，使TellCore v0部分匹配：
- **构造原则**：修改true_positive题的某个关键条件，使TellCore v0的direction hint部分适用但不完全
- **候选**：1962变体（如CC-018：1962的"2的幂"改为"素数"）
- **预测**：Selector应判定"boundary" → LD可能部分成功或失败

## 3. Arms

### 3.1 false_friend实验

| Arm | 名称 | 内容 |
|---|---|---|
| R_ff | bare | 只有false_friend题 |
| LD_ff | lineage+direction | false_friend题+true_positive题的lineage+direction（故意不匹配） |

### 3.2 boundary实验

| Arm | 名称 | 内容 |
|---|---|---|
| R_b | bare | 只有boundary题 |
| LD_b | lineage+direction | boundary题+原题的lineage+direction（部分匹配） |

### 3.3 Selector验证

对每道题（true_positive + false_friend + boundary），运行Selector预测，记录：
- Selector判定（适用/不适用/boundary）
- 判定依据（trigger_boundary和negative_boundary的匹配结果）

## 4. Contrasts

| Contrast | 计算 | 含义 |
|---|---|---|
| C1: LD_ff − R_ff | LD_ff跑偏率 − R_ff跑偏率 | 不匹配Tell是否导致跑偏（误触发率） |
| C2: LD_b − R_b | LD_b成功率 − R_b成功率 | 部分匹配Tell是否有增量或有害 |
| C3: Selector准确率 | 预测正确数 / 总题数 | Selector的预测准确率 |

## 5. 资源契约

- 模型：devin cli默认模型（GLM-5.2 High）
- Token预算：无限制
- 工具策略：solver_harness默认（无工具）
- 每道题每组1次运行

## 6. 成功标准

### false_friend判定

| 层 | 判定 | 方法 |
|---|---|---|
| 跑偏 | AI是否走了错误方向（因不匹配Tell误导） | 检查thinking是否被Tell的方向带偏 |
| 证明 | proof是否数学正确 | 人工核验 |

**误触发定义**：LD_ff走了Tell指示的错误方向（而非自己找到正确方向）

### boundary判定

| 层 | 判定 | 方法 |
|---|---|---|
| 部分成功 | proof是否部分正确或完全正确 | 人工核验 |
| 跑偏 | AI是否被部分匹配的Tell带偏 | 检查thinking |

### Selector准确率

| 预测 | 实际 | 判定 |
|---|---|---|
| 适用 | LD成功 | ✅ 正确 |
| 适用 | LD失败 | ❌ 误判 |
| 不适用 | LD失败 | ✅ 正确 |
| 不适用 | LD成功 | ❌ 漏判 |
| boundary | LD部分成功 | ✅ 正确 |

## 7. 预测

| 题型 | Selector预测 | LD实际 | 预期结果 |
|---|---|---|---|
| true_positive（1631/1843） | 适用 | 成功 | ✅ 正确 |
| false_friend | 不适用 | 跑偏或失败 | ✅ 正确（如果Selector正确拒绝） |
| boundary | boundary | 部分成功或失败 | ✅ 正确（如果Selector正确标为boundary） |

**关键预测**：
1. false_friend题上，如果Selector正确拒绝（判定"不适用"），不运行LD——但如果运行LD（故意不匹配），LD会跑偏（误触发率>0）
2. boundary题上，LD可能部分成功——TellCore v0的direction部分适用，但lineage不匹配可能导致AI在关键步骤走错

## 8. "中"的定位对应

| 验证内容 | "中"的来源 | 预期结果 |
|---|---|---|
| 误触发率 | 352号三个独立指标之一 | false_friend题上误触发率>0（不匹配Tell有害） |
| 不合成综合效用 | 352号"不引入综合效用函数" | 跑偏率/成功率/部分成功率分别记录，不合成 |
| 不用帕累托前沿 | 拒绝372号 | 不估计9维帕累托前沿，只看3类题的3个独立指标 |

## 9. 停止规则

- 每道题每个arm跑一次
- 所有运行完成后计算contrast和Selector准确率
- 不在看到结果后追加arm或修改判定标准

## 10. 实验ID

- eight-p2-tp-{题号}-R/LD（true_positive验证）
- eight-p2-ff-{题号}-R/LD（false_friend验证）
- eight-p2-b-{题号}-R/LD（boundary验证）

## 11. 前置工作

- [ ] 构造1-2道数学正确的false_friend题（需独立数学核验）
- [ ] 构造1道boundary题（1962变体）
- [ ] 实现Selector（从题目特征匹配trigger_boundary和negative_boundary）
- [ ] 冻结本预注册文档

## 12. 依赖

- Phase 1完成（需要true_positive题的LD成功确认）
- TellCore v0的trigger_boundary和negative_boundary已定义（在local_global_switch.yaml中）
