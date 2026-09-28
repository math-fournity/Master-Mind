# Distance Report — Anthropic FLT 机器证明与本项目三关的"距离"（六轴终局报告，2026-09-28）

> **执行者**：设立闭包的原 Session（用户令"亲自来做做试试，广度优先"）。全部按 `distance-sop.md`
> 执行；**对象仓全程只读**（仅读 PROOF-PATH 全文、README、ATTRIBUTION 头部、文件名级统计、
> 3 个定理文件头），未运行任何构建/验证脚本。
> **锚点体例**：`ART-*`/`OUR-*`/`EXT-*` 引用 objects.tsv；对象仓内文件按仓内相对路径；
> 外部材料标注 URL 与检索日 2026-09-28。

## U-D1 路线轴：蓝图来源已裁定

- **EXT-004 补锚**：[Anthropic 官方研究文](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
  （2026-09 检索）——"Claude 的证明遵循 Darmon、Diamond、Taylor 对 Wiles 证明的简化版"；
  任务图"closely follows Wiles's original proof"；人类数学输入仅限 Tianyi Peng 的高层指令
  （如"Jacobian as a scheme sounds high priority"）。→ **R-0011 的"待查"升级为 high 置信**：
  路线=人类给定（DDT 蓝图），蜂群=执行引擎；协调机制=Prove2Me 平台（DAG+陈述/证明分文件+
  自然语言描述记忆外化）。
- **U-D1-a 判定**：蓝图=人类；执行=蜂群；**无混合路线选择**的证据。
- **U-D1-b**：同构精化表见 §D1 同构表；差异项三条（§4.3）。

### D1 同构表（PROOF-PATH 六步 ↔ Stage A 五环）

| PROOF-PATH | Stage A 环 | 算子 | 差异 |
|---|---|---|---|
| 1 归约到素数 p≥5（Mathlib of_odd_primes+指数4特例） | 链条外沿 | W4 的前置分解 | A 关未单列（进位到第 0 环） |
| 2 Frey package + no_frey_package 终点 | Frey 环 | W1→W3→W2 | 完全同构；A 关"X₀(2) 亏格 0"论证在机内为 S₂(Γ₀(2))=0 定理 |
| 3 不可约性（Mazur，含 a≡3 mod 8 的素数 2 分案） | （Wiles 环内） | W5 前半 | A 关未单列 |
| 4 模性提升（R=T by TW patching；3/5 切换 threeFiveSwitchCurve） | Wiles 环 | W5 后半+W6+W7+W8 | 完全同构；threeFiveSwitch 与共 ρ₅ 曲线族逐字对应 |
| 5 level lowering（Ribet/Mazur-Ribet，Čerednik-Drinfeld） | Ribet 环 | W4 | 完全同构 |
| 6 S₂(Γ₀(2))=0 | （Frey 环终点） | W2 | A 关并入第 2 环 |
| （无） | 修复环（1993–95） | W9 | **机内无对应**：一次成证 |

**同构度结论**：执行路线 = A 关路线的**逐环超集**（差仅"修复环"——机器一次成证无修复史）。

## U-D2 算子轴：映射表（10/10 落位，7 落实 3 特化）

| 算子 | 对象仓对应物 | 关系 | 置信 |
|---|---|---|---|
| W1 | Def_FLTPrelim_FreyPackage.lean + FreyPackage.of_counterexample | 对应 | high |
| W2 | FreyPackage.no_frey_package + S₂(Γ₀(2))=0 | 对应 | high |
| W3 | GaloisRepIsIrreducible 群 + Def_FLTPrelim_GaloisRep.lean | 对应 | high |
| W4 | level_lowering_to_two 族 + Čerednik-Drinfeld | 对应 | high |
| W5 | threeFiveSwitchCurve + RubinSilverberg 显式族 + modularityLiftingAtConductor_threeFive 族 | 对应 | high |
| W6 | DeformationRingData/CuspForm.HeckeGaloisRepDatum（Deformation 120 文件主题） | 对应 | med（主题级） |
| W7 | （R=T 后不再需要独立计数判据——被 patching 定理吸收） | 特化吸收 | med |
| W8 | Algebra.PatchingDatum + exists_surjective_algHom_of_heckeGaloisRepDatum | 对应 | high |
| W9 | **仓内空缺**（一次成证）→ 外部：失败尝试贡献约 7% 非样板代码 | 外部证据 | high |
| W10 | ATTRIBUTION 106+23 文件 + Mathlib 挂接 + Prove2Me NL 描述复用 | 对应 | high |

## U-D3 粒度轴：分解剖面的量化

- **29,511 定理陈述与证明严格一一对应**（Theorems/ 29,511 文件 = P2M/Sol/ 29,511 文件）；
- 主题分布（文件名前缀统计）：**WeierstrassCurve 1,003 / CuspForm 697 / Valuation 343 /
  GaloisRep 262 / Hecke 183 / ModularForm 170 / Deformation 120 / FreyPackage 59**……
  主题浓度与 DDT 路线的机械重心完全一致；
- 粒度两级显形：**数学级定理**（PROOF-PATH 六步指名者）+ **实例/类型类支撑件**（如 Thm_
  fermat_last_theorem.lean 头部的巨型 attribute 负实例块——不是数学内容，是 Lean 类型类
  冲突的机械消解）。**29,511 中真正承载策略层的只有 PROOF-PATH 指名的几十个**；
- 分解来源（外部证据）：DAG 由 Prove2Me 平台维护，代理据图领任务；人类定蓝图与优先级；
  首次尝试（无共享蓝图）**失败**——"agents quickly lost track of the project's state"。
  → **与 OP 程序的结构同构**：units.tsv 预注册+状态列调度 ≈ Prove2Me 的 DAG+领任务；
  我们的"禁止无单元漫游"≈ 蜂群加蓝图后才成功的教训。**306 号"粒度规范"在 6 万文件尺度
  获得实证**：粒度不是品味问题，是可并行性与可恢复性的先决条件。

## U-D4 仲裁轴

"Lean as the arbiter"（机器三公理+无 sorry+comparator 15h kernel 重放）与 OP-7"机器可检查
骨架"**收敛于同一判据形态**——差一层：其=语句级全自动（编译器即裁判），OP-7=策略级需人工
读骨架。距离≈"粒度差一层"，非本质冲突；且官方文承认"formalized proof 不应替代人类可读
阐述"——与我们"人话文档"要求**同构**。

## U-D5 货架轴

- 2026 货架剖面（ATTRIBUTION）：Imperial FLT 106 文件（Frey package/Galois rep/形变/patching/
  Kummer 挠性等）、flt-regular（Kummer 定理）、Mathlib 全库（5 倍于此证规模）、Prove2Me
  平台；23 文件复现 Mathlib 引理（兼容层）。
- **1983→2026 决定性增量**（U-D5-b 对比结论）：① Wiles 当年**亲手做的全部形变论/patching
  机械已成人类货架预制品**（Imperial FLT）；② Lean/Mathlib+comparator=验证机械的商品化；
  ③ Prove2Me=协作记忆外化平台。B 关 1983 清点里的"货架空缺"（主猜想未证）在 2026 已被
  Mazur–Wiles 等填上——**货架轴的距离 = 43 年数学商品化的全部差距**。

## U-D6 意义轴：对三关的反身裁决

1. **B 关结论加固而非修正**：路线被证实为人类给定（D1）——蜂群项目**未覆盖路线生成能力**；
   我们 B 关测的正是该项目没有测的东西，互补关系坐实。对抗重放仍值得做（其外部材料还给出
   了意外的第三裁判来源：Prove2Me 的 DAG 结构与失败史）。
2. **C 关升级意见**：排序应加"可执行性权重"——2026 货架已把"形变/patching 级"机械商品化，
   S1/S2 类策略的可执行成本被历史性压低；S4（算术循环线）的货架尚空，权重应相应调低其
   短期优先级。（不改 C 关排序原文，作为附录意见登记。）
3. **方法自反验证**：OP 程序的 units 调度 ≈ Prove2Me DAG 调度；"禁止漫游"≈ 蓝图教训；
   W9 障碍账本 ≈ "7% 代码来自失败尝试"——**三条独立同构**，本框架对蜂群式协作有直接
   描述力。
4. **"距离"的最终一句话**：我们与蜂群之间隔着**一层执行**——同一张路线图（D1 同构表），
   他们向下走到了 6 万个可编译模块，我们向上守住了"路线从哪来、为什么选这条"；两层各自
   完整，互不覆盖；**接缝恰好落在货架轴**——货架越厚，执行层越自动，策略层越稀缺。

## 7. 交付物与边界

- 交付：本报告 + `plain/06-Anthropic距离-人话.md` + 矩阵更新（relations 升级与新增行）+
  MEMORY/README 索引。
- 边界：对象仓只读了文件名级+3 个文件头（29,511 定理正文 0 读——广度优先纪律下足够 D1–D5
  裁决，但个别主题级对应[W6]置信仅 med）；ATTRIBUTION 表格未逐行量化（留 U-D5-a 精化余量）；
  外部材料仅官方文一手，Nature/Xena 报道未单独核验。
