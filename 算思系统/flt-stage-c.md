# FLT Stage C — 前沿真测：BSD 猜想攻击策略生成（2026-09-28）

> **性质**：`flt-test-design.md` Stage C 的可执行部分——**只生成与排序，不可验证**（设计文档
> 定位：长期锚而非本轮判据）。目标选择依据：Wiles 引言自述证明联结了两大传统，其中第二大
> 传统"special values of L-functions"的旗舰问题即 BSD `[语料：wiles 引言 L9-11]`——C 关选
> 它，是对 A/B 关方法在同一条思想线上的自然延伸。
> **方法**：与 Stage B 同程序（P1 facet 生成 → P2 机械就绪清点（2026）→ P3 双目标排序）。
> 锚点=截至本日的已命名成果（年份标注）；无预注册判据，产出为排序与理由，供未来检验。

## 1. 机械就绪清点（W10，2026）

Kato Euler 系〔2004〕；Skinner–Urban 主猜想（GL₂ 普通）〔2014〕；Kolyvagin Euler 系
（秩0/1 BSD）〔1989/90〕；Gross–Zagier〔1986〕；p-parity（Nekovář/Dokchitser）〔2000s〕；
p-converse 定理族（Skinner–Urban/Zhang/Wan 等，秩1 大量情形）〔2010s〕；Heegner 点与
Bertolini–Darmon Iwasawa–Heegner〔2000s〕；Darmon 型构造点（实二次/五次）〔2000s–10s〕；
Beilinson–Flach 元素与对角循环（三重积 Gross–Zagier 型）〔2010s〕；Gross–Schoen 对角循环
〔1990s〕；subconvexity/非消失密度〔2000s–10s〕；syntomic/p 进 BSD（Coleman–Mazur 时代以降）
〔2000s–〕；Mazur 可见–不可见 Sha 纲领〔1970s–〕。

## 2. 候选域（P1 生成，10 条）

| # | 策略 | 一句话 |
|---|---|---|
| S1 | Euler 系全覆盖 | 把 Kato/Kolyvagin 推广到任意秩，Selmer 双侧夹逼 |
| S2 | Iwasawa 主猜想普适化 | 全秩 p-converse + parity 拼成 BSD 主部 |
| S3 | Heegner/Darmon 构造点 | 高秩有理点的系统构造 |
| S4 | 算术循环线 | 对角循环/Beilinson–Flach 对接 L″（秩2 BSD 几乎空白） |
| S5 | 解析非消失线 | subconvexity 给 L 值非消失密度 |
| S6 | 自守提升线 | 基变换/Asai 把 BSD 归约到更高群上的 L 恒等式 |
| S7 | Sha 结构线 | 可见–不可见 Selmer 结构学（Mazur 纲领续） |
| S8 | p 进/代数 BSD 桥线 | syntomic 上同调对接 p 进 BSD ⇒ 整数 BSD |
| S9 | 三重积线 | 三重积中心值分解给单因子二次导数信息 |
| S10 | 反例考古线 | 按网格空格（F11 成本×L2 完成性）反向搜"最便宜的可证伪域" |

## 3. 排序（P3）

- **G1 完全解决**：#1 **S1+S2 组合**（Euler 系全秩化 ⊕ 主猜想普适化——社区主流路线的算子
  表述：BSD 预期在"Iwasawa 主猜想×非消失控制"合成下倒下；W10 依据：两条传统各自已到
  秩0/1 全覆盖）。#2 S4（**唯一开垦秩2 的现役机械**——对角循环是 L″ 的构造对应物）。#3 S6。
- **G2 十年内进展**：#1 S4 秩2 特例（"下一个 Kolyvagin 时刻"）；#2 S3 Darmon 点纲领；#3 S5。
- **网格空格产出**：S10 为 OP-6 式空格发现的直接产品——(L2×F11) 胞（完成性×成本）提示
  "搜最便宜可证伪域"这一元策略，历史先例=第一类/第二类案例的早期计算筛。

## 4. 诚实声明

本关**无判据、不可验证**：排序是程序输出而非发现承诺；其价值在于（i）与未来进展的可对账性
（十年后对照 G2 排序与实际突破，即 Stage B"区分性校验"的时间延拓版）；（ii）S10 型空格策略
是网格方法论自身的产品。**结论性表述一律禁止。**
