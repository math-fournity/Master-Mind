# 证据文档 · CC-101_bare · POC-2.6 续传机制验证

**日期**：2026-08-18
**性质**：实验证据文档——记录续传机制首次成功让裸AI完成竞赛数学题的完整过程
**题目**：CC-101 / polymath_00146——求最小正整数n，使得可以用n种颜色给每个正整数着色，且方程 w + 6x = 2y + 3z 在正整数中没有同色解
**正确答案**：n = 4
**AI 最终答案**：$\boxed{4}$ ✅

---

## 1. 实验目的

验证续传机制能否让裸AI模型（无vein/hint策略注入）完成因 completion_tokens 限制而无法单轮完成的竞赛数学推理。

**核心论断**：glm-5-2 单次API调用的 completion_tokens 上限是 25000（thinking + content + tool_calls 都算在内）。竞赛数学题的 thinking spin 可能超过此限制，导致AI在 thinking 中被截断（message=0, tool_calls=0），无法进入 working 阶段。续传机制把被截断的 reasoning_content 作为新 prompt 的上下文注入，让AI在新的 API 调用中继续思考，多轮累积完成。

## 2. 实验条件

| 项目 | 值 |
|---|---|
| 条件 | bare（只有题目，无vein/hint） |
| 模型 | glm-5-2 |
| 启动方式 | `devin -p --prompt-file ... --export ...`（非交互模式） |
| 续传脚本 | `continue_solver.py single --problem CC-101_bare --max-rounds 5` |
| 完成轮次 | 2轮（Round 1 截断 → Round 2 续传完成） |

## 3. Round 1：被截断

| 指标 | 值 | 说明 |
|---|---|---|
| agent steps | 1 | 只有一个agent step（thinking spin） |
| reasoning_content | 54,481 字符 | AI在thinking中分析了大量内容 |
| message | 0 字符 | 没有 working 产出 |
| tool_calls | 0 | 没有工具调用 |
| completion_tokens | 25,000 | 撑满上限，被截断 |
| 截断判定 | ✅ truncated | rc>0, msg=0, tc=0, comp>=24000 |

**Round 1 thinking 方向**：
- 开头：分析题目结构，考虑用 Rado 定理判定分划正则性
- 中间：检查系数子集和（{1,6,-2,-3}的所有非空子集），确认没有子集和为零，方程不是分划正则的
- 结尾：在手动验证4-着色的具体方案（检查 c(8), c(10), c(4) 等具体值的约束传播）

**关键**：AI在 Round 1 中已经找到了正确的数学方向（Rado定理 + 分划正则性判定），只是 thinking 太长被截断了。

## 4. Round 2：续传完成

续传 prompt 构造：把 Round 1 的 54,481 字符 reasoning_content 作为上下文注入，加上原始题目文本，让AI"从上次思考中断的地方继续"。

| 指标 | 值 | 说明 |
|---|---|---|
| agent steps | 19 | 19步工具调用+思考 |
| 最终 message | 586 字符 | 有 working 产出 |
| 最终 tool_calls | 0 | 最后一步无工具调用（输出答案） |
| completion_tokens | 785 | 远未达到上限 |
| 截断判定 | ❌ not truncated | 正常完成 |
| 完成判定 | ✅ completed | 有message产出 |

**Round 2 第一步（关键续传信号）**：

> 我将从上次思考中断的地方继续。我已经确定了一种有效的 4-coloring，并正在检查 3 colors 是否足够。让我编写一个计算程序来验证这一点，而不是继续进行手动分析。

AI 在续传的第一步就准确接续了 Round 1 的思考状态——它知道 Round 1 已经确定了4-着色可行，现在需要验证3色是否不够。

**Round 2 的 19 步工具调用序列**：

| Step | 操作 | 说明 |
|---|---|---|
| 0 | exec: ls | 查看工作目录 |
| 1 | write: check_coloring.py | 写验证着色的脚本 |
| 2 | exec: python3 check_coloring.py | 运行验证 |
| 3 | write: forcing_chain.py | 写强制链分析脚本 |
| 4 | exec: python3 forcing_chain.py | 运行 |
| 5 | write: forcing_chain2.py | 改进强制链脚本 |
| 6 | exec: python3 forcing_chain2.py | 运行 |
| 7 | write: forcing_chain3.py | 再次改进 |
| 8 | exec: timeout 120 python3 forcing_chain3.py | 运行（带超时） |
| 9 | write: case_analysis.py | 写case分析脚本 |
| 10 | exec: python3 case_analysis.py | 运行 |
| 11 | write: trace_branches.py | 写分支追踪脚本 |
| 12 | exec: python3 trace_branches.py | 运行 |
| 13 | write: verify_solutions.py | 写解验证脚本 |
| 14 | exec: python3 verify_solutions.py | 运行 |
| 15 | exec: python3 -c ... | 快速计算验证 |
| 16 | get_output | 获取后台进程输出 |
| 17 | write: proof.md | **写出最终证明** |
| 18 | FINAL: 答案 $\boxed{4}$ | **输出最终答案** |

**AI 的工作模式**：写脚本→运行→看结果→写新脚本→运行→...→写proof.md→输出答案。这是典型的实验数学家工作方式——用计算验证猜想，逐步缩小空间，最终写出证明。

## 5. 最终证明结构

proof.md 的结构（Rado定理路线）：

1. **方程不是分划正则的**——用 Rado 定理检查系数 {1, 6, -2, -3} 的所有非空子集，没有子集和为零
2. **2-正则性**——任意2-着色都有同色解（三个解迫使 c(1), c(2), c(3) 两两不同）
3. **3-正则性**——任意3-着色都有同色解（通过约束传播证明）
4. **4-着色存在**——构造具体的4-着色方案
5. **结论**——最小色数为4

## 6. 资产清单

| 资产 | 路径 | 说明 |
|---|---|---|
| Round 1 export | `trajectories/p26-CC-101_bare/round1/exports/conversation.json` | 154KB，被截断的thinking |
| Round 2 export | `trajectories/p26-CC-101_bare/round2/exports/conversation.json` | 286KB，完整续传过程 |
| Round 2 prompt | `workdirs/p26-CC-101_bare/round2_prompt.txt` | 55KB，续传prompt（注入的reasoning_content） |
| proof.md | `workdirs/p26-CC-101_bare/proof.md` | 10KB，最终证明 |
| check_coloring.py | `workdirs/p26-CC-101_bare/check_coloring.py` | 验证着色脚本 |
| forcing_chain.py | `workdirs/p26-CC-101_bare/forcing_chain.py` | 强制链分析（v1） |
| forcing_chain2.py | `workdirs/p26-CC-101_bare/forcing_chain2.py` | 强制链分析（v2） |
| forcing_chain3.py | `workdirs/p26-CC-101_bare/forcing_chain3.py` | 强制链分析（v3） |
| case_analysis.py | `workdirs/p26-CC-101_bare/case_analysis.py` | case分析 |
| trace_branches.py | `workdirs/p26-CC-101_bare/trace_branches.py` | 分支追踪 |
| verify_solutions.py | `workdirs/p26-CC-101_bare/verify_solutions.py` | 解验证 |

## 7. 结论

**续传机制验证通过**。裸AI模型在 completion_tokens 限制下无法单轮完成的竞赛数学推理，通过续传机制完成了：

- Round 1 被截断（54K字符thinking，0产出）
- Round 2 续传后AI准确接续思考状态，19步工具调用，写出proof.md，答案 $\boxed{4}$ 正确

**这是一个独立成立的最小AI数学工程化方案**——不依赖Tell/Hint理论框架，单独可复用。任何使用thinking模型的系统，遇到长thinking spin撞上completion_tokens上限时，都可以用续传机制解决。
