# 证据文档 · CC-101_vein · POC-2.5 vein条件策略验证

**日期**：2026-08-18
**性质**：实验证据文档——记录vein条件（参考路径注入）下AI完成竞赛数学题的完整过程
**题目**：CC-101 / polymath_00146——求最小正整数n，使得可以用n种颜色给每个正整数着色，且方程 w + 6x = 2y + 3z 在正整数中没有同色解
**正确答案**：n = 4
**AI 最终答案**：$\boxed{4}$ ✅

---

## 1. 实验目的

验证 vein 条件（注入source trace题的认知路径模板）下AI能否完成竞赛数学题，并与 bare 条件对比。

**vein 注入内容**：来自 source trace 题 CC-003/1709（t(k)最大奇因子差被4整除）的认知路径：
1. 困境识别：直接枚举无法收敛
2. 方向切换：注意到 t(k) = k / 2^{v_2(k)}，切换到2-adic赋值分析
3. 新方向操作：在2-adic赋值下建立v_2关系，推导约束
4. 提升回全局：从2-adic赋值约束推导出a必须是2的幂
5. 关键认知动作：引入p-adic赋值作为新的表示 → 在赋值下分析局部结构 → 从局部约束推导全局结论

**注意**：vein注入的p-adic赋值方向来自1709题的具体方法，不是CC-101本身的最优路径。CC-101_bare的AI自己走了Rado定理路线，更简洁。详见§7对比分析。

## 2. 实验条件

| 项目 | 值 |
|---|---|
| 条件 | vein（题目+参考路径，无Hint） |
| 模型 | glm-5-2 |
| 启动方式 | `devin -p --prompt-file ... --export ...`（非交互模式） |
| 续传脚本 | `continue_solver.py single --problem CC-101_vein --max-rounds 5` |
| 完成轮次 | 2轮（Round 1 截断 → Round 2 续传完成） |
| 总耗时 | 约45分钟（Round 1 ~17分钟 + Round 2 ~28分钟） |

## 3. Round 1：被截断

| 指标 | 值 | 说明 |
|---|---|---|
| agent steps | 1 | 只有一个agent step（thinking spin） |
| reasoning_content | 46,551 字符 | AI在thinking中分析了大量内容 |
| message | 0 字符 | 没有 working 产出 |
| tool_calls | 0 | 没有工具调用 |
| completion_tokens | 25,000 | 撑满上限，被截断 |
| 截断判定 | ✅ truncated | rc>0, msg=0, tc=0, comp>=24000 |

**Round 1 thinking 方向**（受vein引导）：
- 开头：分析题目，注意到vein提供的参考思路——"Let me think about this using the approach suggested - looking at modular arithmetic / p-adic valuations"
- 中间：切换到p-adic赋值分析，建立 c(n) = (c_0(m) + v_2(n) - v_3(n)) mod 3 的着色公式（m是n的6-free部分）
- 结尾：在分析 c_0(5t) ≠ c_0(7t) 等约束时被截断——正在推导6-free部分的着色约束

**关键**：AI被vein引导到了p-adic赋值路线，和CC-101_bare的Rado定理路线完全不同。

## 4. Round 2：续传完成

续传 prompt 构造：把 Round 1 的 46,551 字符 reasoning_content 作为上下文注入。

| 指标 | 值 | 说明 |
|---|---|---|
| agent steps | 30 | 30步工具调用+思考（比bare的19步多11步） |
| 最终 message | 700 字符 | 有 working 产出 |
| 最终 tool_calls | 0 | 最后一步无工具调用（输出答案） |
| completion_tokens | 450 | 远未达到上限 |
| 截断判定 | ❌ not truncated | 正常完成 |
| 完成判定 | ✅ completed | 有message产出 |

**Round 2 的 30 步工具调用序列**：

| Step | 操作 | 说明 |
|---|---|---|
| 0 | exec: ls | 查看工作目录 |
| 1 | write: check_coloring.py | 写验证着色的脚本 |
| 2 | exec: python3 check_coloring.py | 运行验证 |
| 3 | write: check_4colors.py | 写4色验证脚本 |
| 4 | exec: python3 check_4colors.py | 运行 |
| 5 | edit: check_4colors.py | 修改4色脚本 |
| 6 | exec: python3 check_4colors.py | 运行 |
| 7 | edit: check_4colors.py | 再次修改 |
| 8 | exec: python3 check_4colors.py | 运行 |
| 9 | get_output | 获取输出 |
| 10 | write: check_4colors_bt.py | 写回溯搜索脚本 |
| 11 | exec: python3 check_4colors_bt.py | 运行回溯搜索 |
| 12 | write: analyze_formula.py | 写公式分析脚本 |
| 13 | exec: python3 analyze_formula.py | 运行 |
| 14-15 | get_output | 获取输出（等长时间运行） |
| 16 | write: analyze_formula2.py | 改进公式分析 |
| 17 | exec: python3 analyze_formula2.py | 运行 |
| 18-19 | get_output | 获取输出（等更长时间） |
| 20 | kill_shell | 杀掉超时进程 |
| 21 | write: verify_formula.py | 写公式验证脚本 |
| 22 | exec: python3 verify_formula.py | 运行 |
| 23 | get_output | 获取输出 |
| 24 | write: verify_proof.py | 写证明验证脚本 |
| 25 | exec: python3 verify_proof.py | 运行 |
| 26 | get_output | 获取输出 |
| 27 | write: proof.md | **写出最终证明** |
| 28 | read: proof.md | 读回检查 |
| 29 | FINAL: 答案 $\boxed{4}$ | **输出最终答案** |

**AI的工作模式**：和bare类似（写脚本→运行→看结果→写新脚本），但多了"公式不匹配"后的反复尝试——AI在analyze_formula阶段试图找到显式的4-着色公式，多次尝试后才转向构造性验证。

**关键中间发现**（从tmux pane观察）：
- "3种颜色在 N=12 时失败"——通过计算验证3色不够
- "4种颜色适用于所有测试的 N（最大到 75）"——通过回溯搜索验证4色可行
- "公式不匹配。让我更仔细地分析一下回溯着色"——试图找显式公式但失败
- 最终放弃找显式公式，改用构造性验证（基于3-adic赋值的着色方案）

## 5. 最终证明结构

proof.md 的结构（p-adic赋值路线）：

1. **3种颜色不够**——通过关键解族 (2t,t,t,2t), (3t,t,3t,t), (3t,2t,3t,3t) 推出 c(t), c(2t), c(3t) 必须两两不同，再结合其他解族约束，对 {1,...,12} 穷举验证确认无3-着色可行
2. **4种颜色足够**——构造基于3-adic赋值的着色（将n写成3进制，ν为末尾0的个数）
3. **结论**——最小色数为4

## 6. 资产清单

| 资产 | 路径 | 说明 |
|---|---|---|
| Round 1 export | `trajectories/p26-CC-101_vein/round1/exports/conversation.json` | 148KB，被截断的thinking（p-adic方向） |
| Round 2 export | `trajectories/p26-CC-101_vein/round2/exports/conversation.json` | 344KB，完整续传过程 |
| Round 2 prompt | `workdirs/p26-CC-101_vein/round2_prompt.txt` | 49KB，续传prompt |
| proof.md | `workdirs/p26-CC-101_vein/proof.md` | 7KB，最终证明 |
| check_coloring.py | `workdirs/p26-CC-101_vein/check_coloring.py` | 验证着色脚本 |
| check_4colors.py | `workdirs/p26-CC-101_vein/check_4colors.py` | 4色验证脚本（被多次edit） |
| check_4colors_bt.py | `workdirs/p26-CC-101_vein/check_4colors_bt.py` | 回溯搜索脚本 |
| analyze_formula.py | `workdirs/p26-CC-101_vein/analyze_formula.py` | 公式分析（v1） |
| analyze_formula2.py | `workdirs/p26-CC-101_vein/analyze_formula2.py` | 公式分析（v2） |
| verify_formula.py | `workdirs/p26-CC-101_vein/verify_formula.py` | 公式验证 |
| verify_proof.py | `workdirs/p26-CC-101_vein/verify_proof.py` | 证明验证 |

## 7. 与 CC-101_bare 的对比分析

| 维度 | CC-101_bare | CC-101_vein |
|---|---|---|
| **Round 1 thinking 方向** | Rado定理→分划正则性→子集和检查 | p-adic赋值（vein引导）→v_2/v_3分析→6-free部分 |
| **Round 2 agent steps** | 19步 | 30步（多11步） |
| **Round 2 总耗时** | ~13分钟 | ~28分钟 |
| **证明路线** | Rado定理判定+约束传播+4-着色构造 | 解族分析+3-adic赋值着色构造 |
| **proof.md 结构** | 4步（非分划正则→2-正则→3-正则→4-着色存在） | 2部分（3色不够→4色足够） |
| **是否找显式公式** | 否（直接用Rado定理避免找公式） | 是（尝试找4-着色公式，多次失败后转向构造性验证） |
| **最终答案** | $\boxed{4}$ ✅ | $\boxed{4}$ ✅ |
| **completion_tokens（Round 2最后一步）** | 785 | 450 |

**关键发现**：

1. **vein引导的方向不是最优路径**：CC-101用Rado定理直接判定分划正则性是最简洁的路线（bare的AI自己找到了这条路），vein引导的p-adic赋值路线更复杂、需要更多步骤。

2. **vein没有导致失败，但增加了成本**：vein条件的AI最终也成功了，但花了更多步骤（30 vs 19）和更多时间（28分钟 vs 13分钟）。vein注入的p-adic方向虽然不是最优，但AI在这个方向上通过计算验证最终也完成了证明。

3. **vein的"误导"是部分的而非完全的**：vein注入的p-adic赋值方向对CC-101不是最优，但也不是完全错误——3-adic赋值确实可以用来构造4-着色方案（vein的AI最终用这个方法完成了证明的第二部分）。vein的问题在于它让AI走了弯路（试图找显式公式），而不是直接走向最简洁的Rado定理路线。

4. **这印证了398号§2.5的分析**：vein在展开非特化策略时混入了source trace题的具体方法特化（p-adic赋值），这个特化方法对CC-101不是最优路径。hint的一句话"切换到局部表示Z/pZ"不指定具体方法，可能反而更好——因为它让AI自己选择适合本题的局部表示（bare的AI选择了Rado定理，也是一种"局部表示"思路）。

## 8. 结论

**vein条件下AI成功完成了竞赛数学题**，答案 $\boxed{4}$ 正确。但相比bare条件：
- 花了更多步骤（30 vs 19）
- 花了更多时间（28分钟 vs 13分钟）
- 走了更复杂的路线（p-adic赋值 vs Rado定理）

**对POC-2.5因果效应分析的启示**：CC-101的vein条件没有比bare更好——反而更慢更复杂。但这只是单题观察，不能作为因果效应的结论。需要等全部16个run完成后按398号§5.3判定逻辑做完整分析。CC-101的对比提示了一个重要问题：vein的特化方法引导可能是双刃剑——对某些题有帮助，对另一些题反而增加成本。
