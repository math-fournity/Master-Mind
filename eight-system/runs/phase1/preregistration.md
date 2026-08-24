# Phase 1 预注册文档 — 跨题泛化验证

> **状态**：FROZEN（2026-08-15冻结，冻结于结果前）
> **实验ID前缀**：eight-p1
> **对应方案§8.5**：Step 5
> **"中"的定位**：验证345号钟形曲线跨题的峰值位置是否稳定 + 352号"多峰曲线"可能性

---

## 1. 实验目标

验证Phase 0在1631上发现的"认知支架"假说是否跨题成立。具体回答：

1. **L（lineage-only）是否在多道题上都能在thinking中完成证明？**——如果是，"认知支架"假说跨题成立
2. **LD（lineage+direction）是否在多道题上都能完成proof输出？**——如果是，direction的"工具提示"作用跨题成立
3. **1962是否是例外？**——1962在283号tree组仍失败，原方案指出1962需要操作路径Tell而非方向Tell。如果1962上L/D/LD都失败，说明TellCore v0（局部-全局表示切换）对"操作路径瓶颈"题不够

## 2. 题目（3道）

### 1843（Algebra）

- **已知证据**：bare失败；tree成功；干扰Tell失败（与1631同类的P0题）
- **预测**：与1631类似，L在thinking中完成证明，LD完成proof输出

### 1709（Number Theory）

- **已知证据**：bare失败；干扰Tell失败（P0题，但tree组数据缺失）
- **预测**：L在thinking中可能完成证明（lineage提供认知支架），但route finding可能需要更精确的direction

### 1962（Number Theory）——关键测试

- **已知证据**：bare失败；**tree仍失败**（283号——方向不够，需操作路径）
- **预测**：1962上L（lineage）可能不足以引导route finding，因为1962的瓶颈不是"找不到工具"而是"不知道操作路径"。即使LD也可能失败——因为TellCore v0的direction hint是方向性的，不是操作路径性的
- **关键意义**：如果1962的LD也失败，这是TellCore v0的**适用边界**——需要操作路径Tell的题不在TellCore v0的覆盖范围内

## 3. Arms（4组对照 × 3道题 = 12次运行）

每道题跑与Phase 0相同的4组对照：

| Arm | 名称 | 内容 |
|---|---|---|
| R | problem-only | 只有题目 |
| L | lineage-only | 题目+脉络（从283号tree组提取），不给方向 |
| D | direction-only | 题目+方向提示（TellCore v0的direction hint），不给脉络 |
| LD | lineage + direction | 题目+脉络+方向提示 |

**Continue实验**：对每个hit token limit的arm，做1次continue实验（与Phase 0 Step 4相同）。

## 4. Contrasts

### 主contrast（每道题独立计算）

| Contrast | 计算 | 含义 |
|---|---|---|
| C1: LD−L | LD成功 − L成功 | direction的增量效果 |
| C2: (LD−L)−(D−R) | C1 − (D成功 − R成功) | direction是否依赖lineage |
| C3: LD−R | LD成功 − R成功 | 总效果 |

### 跨题contrast（Phase 1新增）

| Contrast | 计算 | 含义 |
|---|---|---|
| C4: L_continue成功率（跨题） | 3道题中L_continue成功的比例 | 认知支架假说跨题成立程度 |
| C5: 1962的LD−1631的LD | 1962 LD成功 − 1631 LD成功 | TellCore v0对操作路径瓶颈题的适用边界 |

## 5. 资源契约

- 模型：devin cli默认模型（GLM-5.2 High）
- Token预算：无限制（devin cli默认）
- 工具策略：solver_harness默认（无工具）
- 每道题4组原始运行 + 若干continue运行

## 6. 成功标准（三层判定，与Phase 0一致）

| 层 | 判定 | 方法 |
|---|---|---|
| 路线层 | AI是否使用了目标方向 | 检查thinking中是否出现相关关键词 |
| 证明层 | proof是否数学正确 | 人工核验 |
| 落盘层 | proof.md是否生成 | 检查文件存在性 |

**Continue实验新增判定**：
| 层 | 判定 | 方法 |
|---|---|---|
| Thinking完成度 | thinking中是否已完成完整证明 | 检查thinking中是否包含所有关键步骤 |

## 7. 预测（冻结前写明）

| 题 | R | L（route） | L（proof） | L_continue | D（route） | D（proof） | LD（route） | LD（proof） |
|---|---|---|---|---|---|---|---|---|
| 1843 | 失败 | 高 | 低（hit limit） | **成功** | 高 | 低（hit limit） | 高 | **成功** |
| 1709 | 失败 | 中-高 | 低（hit limit） | **可能成功** | 中-高 | 低（hit limit） | 中-高 | **可能成功** |
| 1962 | 失败 | **低** | 低 | **失败** | **低** | 低 | **低** | **失败** |

**关键预测**：1962是TellCore v0的适用边界——L/D/LD都无法引导route finding，因为1962的瓶颈是操作路径不是工具方向。

## 8. "中"的定位对应

| 验证内容 | "中"的来源 | 预期结果 |
|---|---|---|
| 分层峰值跨题成立 | 345号钟形曲线 | 1843/1709上L在route层到峰值，proof层差一点 |
| 多峰曲线可能性 | 352号"非单调峰值假设" | 1962的峰值位置可能和1631不同（操作路径瓶颈） |
| 三个独立指标不合成 | 352号三个指标 | 路线层/证明层/落盘层分别记录，不合成综合效用 |
| 不用帕累托前沿 | 拒绝372号 | 3道题×4组=12次运行的规模无法估计9维帕累托前沿 |

## 9. 停止规则

- 每道题每个arm跑一次原始运行
- hit token limit的arm做1次continue运行
- 所有运行完成后计算contrast
- 不在看到结果后追加arm或修改判定标准

## 10. 实验ID

- eight-p1-1843-R/L/D/LD
- eight-p1-1709-R/L/D/LD
- eight-p1-1962-R/L/D/LD
- eight-p1-{题号}-{arm}-continue（如需要）

## 11. 前置工作

- [x] 从283号tree组提取1843/1709/1962的lineage
- [x] 构造1843/1709/1962的R/L/D/LD prompt文件
- [x] 冻结本预注册文档
