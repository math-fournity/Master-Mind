# 004-v1-2026-08-05 Phase 7 representation/ 22 维度审计执行方案

## 元数据

| 字段 | 值 |
|---|---|
| 文档编号 | 004（Master repo） |
| 版本 | v1 |
| 日期 | 2026-08-05 |
| 类型 | 审计执行方案 |
| 关联文档 | 003号（Master工作审计方案）、146号v4.2、147号v1.4.1、163号（Phase7实现方案）、164-166号 |

---

## 0. 目标

对 `xishujuzhen/research_runtime/representation/` 中的 24 个 .py 文件执行 22 维度审计，发现理解偏差、设计不足、实现错漏，并产出详细改进意见。

---

## 1. 审计对象

`xishujuzhen/research_runtime/representation/` 共 24 个 .py 文件：

```
__init__.py
baseline_comparison.py
commutative_diagram.py
egraph.py
fermat_chain.py
geometry_guard.py
groupoid_check.py
hole_detector.py
hott_directions.py
hott_gate.py
local_view.py
math_label.py
mislabel_guard.py
path_equivalence.py
persistent_homology.py
phase_gate.py
representation_map.py
soundness_obligation.py
source_version.py
tda_gate.py
test_phase7.py
trajectory_alignment.py
transport_fidelity.py
transport_objects.py
```

---

## 2. 审计依据

### 2.1 母本

1. `系统探讨.md`（2288 行）——最高母本
2. `123-v1-2026-08-05-数学大师系统全景复盘与第一性原理重构计划.md`（1210 行）
3. `plan-dad3347dc4d8e542.md`（387 行，早期演进）

### 2.2 规划文档

1. `137-v1-...Phase7-CheckList.md`
2. `162-v1-...Phase7-CheckList-v4维度19-20-21预防性审计与修正报告.md`
3. `163-v1-...Phase7实现方案.md`

### 2.3 审计与测试报告

1. `164-v1-...Phase7实现21维度审计报告.md`
2. `165-v1-...Phase7三文件逐行审计与修正报告.md`
3. `166-v1-...Phase0-6-CheckList-v4.2维度22预防性审计报告.md`

### 2.4 审计方法论

1. `146-v1-...审计方法论手册v4.2.md`
2. `147-v1-...Phase实现启动SOP-v1.4.1.md`

---

## 3. 审计维度重点

### 高优先维度（Phase 7 代码审计重点）

| 维度 | 重点检查内容 |
|---|---|
| D1 | 代码是否被母本要求覆盖 |
| D14 | 实现→母本覆盖：每个函数/类/字段是否来自母本具体要求 |
| D15 | Check List→实现完整性：137号和163号要求是否全部实现 |
| D16 | 实现→Check List 完整性：代码实现是否超出或未对齐 Check List |
| D17 | 方法完整性：方法参数、返回值、异常处理是否完整 |
| D19 | 方法多来源/多字段：是否遗漏限定词或来源 |
| D20 | plan/123号逐字要求：163号中的具体实现要求是否一一对应 |
| D21 | 声明性 vs 强制性：检查是否只返回 True/对象，没有实际强制机制 |
| D22 | 母本逐字要求：系统探讨.md 中的具体例子/公式/映射是否在代码中保留 |

### 具体 F 断层类型检查

- **F12c**：多限定词遗漏（如"≥3"但漏了"未参与设计"）
- **F14**：plan/123号逐字要求未被 Check List 概括
- **F15**：声明性实现而非强制性实现（方法返回 True 但无强制）
- **F16**：母本逐字要求未被任何维度覆盖（维度 22 专门处理）

---

## 4. 审计方法

### 4.1 每个 .py 文件单独审计

对 24 个文件逐个执行以下步骤：

1. 读取文件全文
2. 提取：类、函数、方法签名、文档字符串
3. 对照 `163号` Phase7实现方案，看该文件承担哪些职责
4. 对照 `137号` Phase7 Check List，看该文件覆盖了哪些 P7-xxx 项
5. 对照 `系统探讨.md` 和 `123号` 相关章节，看是否有母本要求未被实现
6. 检查 `test_phase7.py` 中对应的测试是否覆盖该文件

### 4.2 跨文件一致性审计

1. 24 个文件之间的接口是否一致
2. 同一名称在不同文件中是否含义一致
3. 共享的数据结构/类型定义是否统一
4. 错误处理/异常类型是否统一

### 4.3 测试审计

1. 运行 `test_phase7.py`，记录通过/失败
2. 检查测试覆盖率：是否每个主要函数都有测试
3. 检查测试断言的严格性：是否有"声明性"断言（只检查返回值类型，不检查内容）
4. 检查是否有 164号 提到的"假 PASS"问题

---

## 5. 审计步骤（Check List）

### 步骤 1：准备

- [ ] 确认 ArangoDB 已启动
- [ ] `source .env` 确认 `ARANGO_DB=xishujuzhen_math_glm52`
- [ ] 阅读 146号v4.2 第 8 章（实现前自检）和第 9 章（实现后审计）
- [ ] 阅读 163号 Phase7实现方案
- [ ] 阅读 165号 三文件逐行审计报告（学习已发现的 F16 问题模式）

### 步骤 2：逐文件审计

- [ ] `representation_map.py`
- [ ] `soundness_obligation.py`
- [ ] `transport_fidelity.py`
- [ ] `fermat_chain.py`
- [ ] `source_version.py`
- [ ] `groupoid_check.py`
- [ ] `path_equivalence.py`
- [ ] `commutative_diagram.py`
- [ ] `transport_objects.py`
- [ ] `local_view.py`
- [ ] `hole_detector.py`
- [ ] `egraph.py`
- [ ] `trajectory_alignment.py`
- [ ] `geometry_guard.py`
- [ ] `tda_gate.py`
- [ ] `persistent_homology.py`
- [ ] `hott_gate.py`
- [ ] `hott_directions.py`
- [ ] `baseline_comparison.py`
- [ ] `math_label.py`
- [ ] `phase_gate.py`
- [ ] `mislabel_guard.py`
- [ ] `__init__.py`
- [ ] `test_phase7.py`

### 步骤 3：跨文件一致性检查

- [ ] 检查 `__init__.py` 中的模块描述与实际文件是否一致
- [ ] 检查错误/异常类命名和使用
- [ ] 检查共享类型/常量定义
- [ ] 检查 docstring 风格一致性

### 步骤 4：测试审计

- [ ] 运行 `test_phase7.py` 并记录结果
- [ ] 统计每个 .py 文件的测试覆盖
- [ ] 标记"声明性"断言和"假 PASS"风险

### 步骤 5：产出审计报告

- [ ] 按 F12c/F14/F15/F16 分类问题
- [ ] 每条问题给出：位置、证据、母本出处、改进意见、验证方法
- [ ] 按 P0/P1/P2 排优先级
- [ ] 写入 `dev-docs/005-v1-Phase7-representation-22维度审计报告.md`

---

## 6. 改进意见格式示例

```
问题编号：P7-REP-001
文件：xishujuzhen/research_runtime/representation/fermat_chain.py
函数：FermatChain.some_method
问题类型：F16（母本逐字要求遗漏）
严重程度：P0

证据：
- 163号§3.2 明确列出"费马案例完整链条包括 4 环节 + 3 层阶梯 + 6 条大师启发"
- 当前实现只有 3 环节，缺少"反例验证"环节

母本出处：
- 163号§3.2："...4 环节..."
- 系统探讨.md §8.2："..."

改进意见：
在 FermatChain 中新增 _validate_counterexample 方法，补充第 4 环节。
```python
def _validate_counterexample(self, candidate: int) -> bool:
    """验证候选不是反例"""
    ...
```

验证方法：
1. test_phase7.py 中新增测试用例验证 4 环节完整
2. 运行 `pytest xishujuzhen/research_runtime/representation/test_phase7.py::test_fermat_chain`
```

---

## 7. 与 Supervisor 的交互点

1. Master 完成本方案后，commit 到 `glm5.2`
2. Supervisor 审阅本方案是否覆盖 22 维度的全部要点
3. Master 执行审计，产出报告
4. Supervisor 审阅审计报告，检查是否有 F16 遗漏、假 PASS 未识别、改进意见不够具体
5. Master 根据 Supervisor 反馈修正或执行改进

---

## 8. 风险

1. **审计范围过大**：24 个文件 + 22 维度可能产生大量输出。建议先重点审计 5-8 个核心文件，再扩展。
2. **165号已做部分工作**：避免重复 165号的发现，但可以从 22 维度视角补充它没覆盖的部分。
3. **改进意见过多导致无法执行**：按 P0/P1/P2 分类，先让低级别 AI 改 P0。
