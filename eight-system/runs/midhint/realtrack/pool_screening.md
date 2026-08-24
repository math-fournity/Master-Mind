# 真实题库轨道 · 选题池筛选记录（2026-08-16）

> 来源：错题分析系统 analysis_results（DIRECTION_ERROR + PARTIAL_PROGRESS）× d2=mod_p_grouping
> 筛选者：Master Agent。此记录是后续扩展选题（第2、3圈…）的直接输入。

## 两道筛选闸门（从首圈教训提炼，后续选题必须过）

1. **闸门A·真做了本题**：分析记录的 d1_explanation 必须确认 bare AI 当时在解本题（有真实探索），排除"拿到错题面/做了另一道题"的退化运行——这类题 thinking 全部无效，Phase B 无脉络可提取（首例：omni_math_004105，214KB thinking 全是另一道 k-sum 集合问题，弃）。
2. **闸门B·解答亲自核验**：题库 solution 字段的质量参差（有只给结论不给证明的 sketch，甚至有论证不成立的），实验者必须亲自读题面+解答并核验数学正确性（程序穷举小case + 手工构造证明），才可作为标准答案。

## 池子筛选结果（32 → 13）

32道 mod_p_grouping 可选题中，约**19道是退化运行**（d1_explanation 明确写"addressed an entirely different problem"），排除。**13道真实做过本题**（按thinking丰富度排序，均为 polymath 来源）：

| 题号 | 判定 | AI的真实卡点形态 |
|---|---|---|
| **polymath_00995** ✅已选 | PARTIAL_PROGRESS/high | 框架完整（7条正确结论），卡在n≡2 mod 4唯一未决类，从未尝试不可能性证明 |
| polymath_00128 | PARTIAL_PROGRESS/high | 奇偶论证的全部组件已找到但没组装 |
| polymath_00871 | PARTIAL_PROGRESS/high | 上界n≤17已证，卡在2017=3N+1素数的mod 3精化 |
| polymath_00269 | PARTIAL_PROGRESS/high | 7个最小平方和已识别，卡在闭包mod 2论证 |
| polymath_00072 | DIRECTION_ERROR/high | 构造到错误答案3600，从未考虑奇偶染色 |
| polymath_00773 | DIRECTION_ERROR/high | 穷举方向，从未考虑棋盘染色（13/12格） |
| polymath_00083 | DIRECTION_ERROR/high | Chebyshev递推框架，错失f(奇)全偶/全奇分类 |
| polymath_01187 | DIRECTION_ERROR/high | 极值刻画方向，错失答案mod 4计数 |
| polymath_02644 | DIRECTION_ERROR/medium | 染色得上界48，错失2×2块分组精化 |
| polymath_00021 | DIRECTION_ERROR/high | 2D前缀和框架，错失双带分组 |
| polymath_01089 | DIRECTION_ERROR/high | 图支配集框架，错失周期3权序列 |
| polymath_04777 | DIRECTION_ERROR/medium | 博弈论分析，错失中央4格标记 |
| polymath_00433 | PARTIAL_PROGRESS/medium | 染色已找到但只得弱界12 |
| polymath_01850 | PARTIAL_PROGRESS/medium | 奇偶分裂已做，卡在mod 2比值常数化 |

**未过闸门B的注意项**：polymath 解答字段多为sketch（首圈00995即如此，靠我另行核验）；后续选题同样必须走 verification/ 程序核验流程。

## 交叉验证发现（midhint 11道源题 vs 分析系统）

- 11道已选源题中仅 **1631、1843** 在分析池中。1631：DIRECTION_ERROR/quadratic_residue_euler/high（与关键词判定一致）。**1843：PARTIAL_PROGRESS/mod_p_grouping/high——比关键词判定的DIRECTION_ERROR更精确**：bare AI当时已证出下界2016、正在做区间符号分析、尝试了mod 2配对后停滞，从未发现mod 4块内外对分组。
- 其余9道（1678/1929/1964/2024/2040/2095/2111/2843/2921）不在分析池——选题依据仍是关键词脚本+subagent核验，是已知缺口（可请分析系统补跑，非本轨道阻塞项）。

## 与本轨道的关系

- 首圈：polymath_00995（见 `00995/` 目录全套staged资产）
- 第2圈起候选：优先 polymath_00128（组件齐未组装——与00995同为PARTIAL_PROGRESS形态，hint靶点清晰）和 polymath_00072（构造出错误答案——DIRECTION_ERROR形态，hint需把AI从构造拉向染色不变量）
