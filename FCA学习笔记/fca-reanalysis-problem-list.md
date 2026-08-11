# FCA再分析题目清单（抽样验证第一批）

> 从455个profile中按domain分布抽样12题，覆盖6个归一化domain（每个2题）。
> 逐个处理，不并发。分类学修正由主agent亲自执行。

## 题目列表（按处理顺序）

| 序号 | problem_id | 归一化domain | 局部tell数 | 全局tell数 | 题目摘要 | profile.json |
|---|---|---|---|---|---|---|
| 1 | compfiles_imo1985p6 | analysis | 8 | 2 | For every real number x_1, construct the sequence... | Y |
| 2 | compfiles_imo1979p6 | combinatorics | 7 | 3 | Let A and E be opposite vertices of an octagon. A frog... | Y |
| 3 | compfiles_imo2014p5 | combinatorics | 7 | 3 | For every positive integer n, the Bank of Cape Town issues... | Y |
| 4 | compfiles_imo1993p6 | general | 8 | 3 | There are n > 1 lamps L_0, L_1, ..., L_{n-1} in a circle... | Y |
| 5 | compfiles_imo1996p6 | general | 8 | 3 | Let p, q, n be three positive integers with p + q < n... | Y |
| 6 | compfiles_imo1991p5 | geometry | 7 | 2 | Let ABC be a triangle and P be an interior point of ABC... | Y |
| 7 | omni_math_004181 | geometry | 8 | 3 | Let S=KA∩Ω, and let T be the antipode of K on Ω... | Y |
| 8 | fate_000255 | algebra | 7 | 3 | Prove that if #G = 396 then G is not simple. | Y |
| 9 | compfiles_imo1976p6 | algebra | 7 | 3 | The sequence u_0, u_1, u_2, ... is defined by: u_0... | Y |
| 10 | fate_000268 | number_theory | 8 | 3 | Let α = √((2+√2)(3+√3)) and consider the extension E = ... | Y |
| 11 | compfiles_imo1992p6 | number_theory | 7 | 3 | For each positive integer n, S(n) is defined to be... | Y |
| 12 | compfiles_imo2020p5 | number_theory | 7 | 3 | A deck of n > 1 cards is given. A positive integer... | Y |

## 处理规则

1. **逐个处理，不并发**——每道题完成并验证后再启动下一道
2. **分类学修正由主agent亲自执行**——subagent只负责分析和报告，不修正分类学
3. **每道题的处理流程**：
   - 主agent从check list模板建立TODO List
   - 主agent从prompt模板构造subagent prompt（填入problem_id和产出路径）
   - 主agent启动subagent（profile选subagent_general）
   - subagent按10步SOP执行FCA再分析
   - subagent返回执行摘要
   - 主agent用产出验证check list验证产出
   - 如果发现分类学问题 → 主agent亲自执行修正流程（7条铁律）
   - 主agent git commit
4. **产出路径**：`FCA学习笔记/10-{problem_id}-FCA再分析.md`（从第10号文件开始，09号是IMO 2024 P5对比）

## 进度跟踪

| 序号 | problem_id | 状态 | 产出文件 | 分类学问题 | 完成时间 |
|---|---|---|---|---|---|
| 1 | compfiles_imo1985p6 | 待处理 | - | - | - |
| 2 | compfiles_imo1979p6 | 待处理 | - | - | - |
| 3 | compfiles_imo2014p5 | 待处理 | - | - | - |
| 4 | compfiles_imo1993p6 | 待处理 | - | - | - |
| 5 | compfiles_imo1996p6 | 待处理 | - | - | - |
| 6 | compfiles_imo1991p5 | 待处理 | - | - | - |
| 7 | omni_math_004181 | 待处理 | - | - | - |
| 8 | fate_000255 | 待处理 | - | - | - |
| 9 | compfiles_imo1976p6 | 待处理 | - | - | - |
| 10 | fate_000268 | 待处理 | - | - | - |
| 11 | compfiles_imo1992p6 | 待处理 | - | - | - |
| 12 | compfiles_imo2020p5 | 待处理 | - | - | - |
