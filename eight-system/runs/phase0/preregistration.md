# Phase 0 预注册文档

> **冻结时间**：2026-08-15 04:00
> **状态**：FROZEN（看到任何结果前冻结）
> **实验ID前缀**：eight-p0-1631
>
> **实验结果**：[experiment_report.md](experiment_report.md) + [experiment_report_step4.md](experiment_report_step4.md) + [evidence_record_001.md](evidence_record_001.md)

---

## 1. 实验目标

验证TellCore v0（局部-全局表示切换）在1631题上的因果效应，通过R/L/D/LD四组对照隔离lineage和direction各自的因果贡献。

## 2. 题目

1631题（Mersenne型递推素数长度）：
- 对正整数a，定义x₁=a，x_{n+1}=2x_n+1。令y_n=2^{x_n}-1。
- 求最大k使存在某个a，y₁,...,y_k全素数。
- 答案：k=2

**已知证据**：
- bare失败（VMS-7g-v3、VMS-8、VMS-9三次确认）
- tree成功（VMS-8 tree组，AI用了模8+二次剩余+Euler准则）
- 干扰Tell失败（VMS-9，给T01模算术方向在1631上无效——实际上1631需要的是二次剩余不是模算术）

## 3. Arms（4组对照）

| Arm | 名称 | Prompt文件 | 内容 |
|---|---|---|---|
| R | problem-only restart | 1631_R_bare.txt | 只有题目 |
| L | lineage-only | 1631_L_lineage.txt | 题目+脉络（推理到x₃≡7(mod 8)），不给方向 |
| D | direction-only | 1631_D_direction.txt | 题目+方向提示（模p+二次剩余+Euler准则），不给脉络 |
| LD | lineage + direction | 1631_LD_lineage_direction.txt | 题目+脉络+方向提示 |

## 4. Contrasts（3个因果对比）

| Contrast | 计算 | 含义 |
|---|---|---|
| C1: LD−L | LD成功 − L成功 | direction的增量效果（在lineage基础上） |
| C2: (LD−L)−(D−R) | C1 − (D成功 − R成功) | direction是否依赖lineage（>0=依赖，≈0=独立） |
| C3: LD−R | LD成功 − R成功 | 总效果（完整干预包 vs bare） |

## 5. 资源契约（所有arm相同）

- 模型：devin cli默认模型（GLM-5.2 High）
- Token预算：无限制（devin cli默认）
- 时间预算：无限制（devin cli默认）
- 工具策略：solver_harness默认（无工具）
- 启动间隔：3秒（站点下限）

## 6. 成功标准（每个arm的三层判定）

| 层 | 判定 | 方法 |
|---|---|---|
| 路线层 | AI是否使用了目标方向（模p分析/二次剩余/Euler准则） | 检查thinking中是否出现相关关键词 |
| 证明层 | proof.md是否存在且数学正确 | 人工核验proof.md |
| 落盘层 | proof.md文件是否生成 | 检查文件存在性 |

**成功定义**：proof.md存在 + 数学正确 + proof中使用了目标方向

## 7. 停止规则

- 每个arm跑一次（不重复）
- 所有4个arm完成后计算contrast
- 不在看到结果后追加arm或修改判定标准

## 8. 预注册的排除规则

- 如果Solver因基础设施原因失败（tmux崩溃、DB连接失败等），记录为infrastructure_invalid，不纳入contrast计算
- 如果proof.md不存在但thinking中显示了正确路线，记录为output_failure（落盘失败），路线层仍可判定

## 9. 实验ID

- eight-p0-1631-R
- eight-p0-1631-L
- eight-p0-1631-D
- eight-p0-1631-LD
