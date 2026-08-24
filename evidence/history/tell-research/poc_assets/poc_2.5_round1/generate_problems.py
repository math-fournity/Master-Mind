#!/usr/bin/env python3
"""Generate all 16 problem files for POC-2.5 (4 problems × 4 conditions)."""
import os

OUT_DIR = "/tmp/poc2.5/problems"
os.makedirs(OUT_DIR, exist_ok=True)

# --- Problem statements (from casepack_v1.md) ---
PROBLEMS = {
    "CC-101": {
        "pid": "polymath_00146",
        "statement": """求最小正整数n，使得可以用n种颜色给每个正整数着色，
且方程 w + 6x = 2y + 3z 在正整数中没有同色解
（w,x,y,z不必互异）。""",
        "answer": "n=4",
    },
    "CC-103": {
        "pid": "polymath_01076",
        "statement": """用3种颜色给整数格点着色。求最小正实数S，
使得对任何3色着色，都存在同色格点A,B,C
构成面积为S的三角形。""",
        "answer": "S=3",
    },
    "CC-104": {
        "pid": "polymath_03408",
        "statement": """将{1,2,3,...,500}排列在圆周上，使得对任意四个不同数a,b,c,d
满足 a+b ≡ c+d (mod 500)，连接a,b和c,d的线段在圆内不相交。
旋转相同的排列视为同一种。求排列数。""",
        "answer": "200",
    },
    "CC-105": {
        "pid": "polymath_00083",
        "statement": """设N为满足以下条件的函数f:Z/16Z→Z/16Z的个数：
对所有a,b∈Z/16Z，
f(a)²+f(b)²+f(a+b)² ≡ 1+2f(a)f(b)f(a+b) (mod 16)。
求N除以2017的余数。""",
        "answer": "793",
    },
}

# --- Veins (extracted from source trace problems) ---
# Each vein is the cognitive path from the matched source trace problem:
# 困境识别 → 方向切换 → 新方向操作 → 提升回全局
VEINS = {
    "CC-101": {
        # CC-101 (3-adic赋值着色) ← CC-003/1709 (2-adic赋值分析t(k) mod 4)
        "source": "CC-003/1709",
        "text": """【参考思路——来自类似题目的解题脉络】

以下是一道结构相似的题目的解题过程，供参考其认知路径（不是本题的答案）：

题目背景：对每个正整数k，令t(k)为k的最大奇因子。求所有正整数a，使存在正整数n，让t(n+a)-t(n), ..., t(n+2a-1)-t(n+a-1)全部被4整除。

解题脉络：
1. 困境识别：直接枚举a和函数分析无法收敛——t(k)的结构在自然表示下不清晰，尝试了多种枚举方法都无法建立一般性证明。
2. 方向切换：注意到t(k) = k / 2^{v_2(k)}，其中v_2(k)是k的2-adic赋值（k中2的幂次）。切换到2-adic赋值分析——在局部表示（模4 / 2-adic赋值）下分析t(k)的结构。
3. 新方向操作：在2-adic赋值下，t(k) mod 4的结构变得清晰——可以建立v_2(n+i)与v_2(n+i-a)之间的关系，利用赋值的性质推导约束。
4. 提升回全局：从2-adic赋值的约束推导出a必须是2的幂——局部表示下的发现提升为全局结论。

关键认知动作：引入p-adic赋值作为新的表示 → 在赋值下分析函数的局部结构 → 从局部约束推导全局结论。""",
    },
    "CC-103": {
        # CC-103 (mod 2 + mod 3 CRT) ← CC-001/1631 (mod 8 + Euler准则)
        "source": "CC-001/1631",
        "text": """【参考思路——来自类似题目的解题脉络】

以下是一道结构相似的题目的解题过程，供参考其认知路径（不是本题的答案）：

题目背景：对正整数a，定义x₁=a，x_{n+1}=2x_n+1。令y_n=2^{x_n}-1。求最大k使存在某个a，y₁,...,y_k全素数。

解题脉络：
1. 困境识别：直接枚举奇素数a逐个验证y_n的素性，无法收敛到一般性证明——每个a需要验证多个y_n，计算量巨大且无模式。
2. 方向切换：注意到x₃ mod 8的结构——切换到模8分析。关键洞察是选择模数不是随机的，而是由"哪个数论定理能利用这个模数"决定。
3. 新方向操作：在模8下计算x₃ ≡ 7 ≡ -1 (mod 8)，应用Euler准则（二次剩余理论）得到x₃是模8的二次剩余，从而x₃ | 2^{(x₃-1)/2} - 1。
4. 提升回全局：识别(x₃-1)/2 = x₂，所以x₃ | y₂ → y₂合数 → k≤2。局部发现（模8下的整除关系）提升为全局结论。

关键认知动作：选择特定模数使得数论定理可用 → 在模数下发现隐藏的整除关系 → 将局部整除关系提升为全局结论。""",
    },
    "CC-104": {
        # CC-104 (mod 500算术级数) ← CC-002/1843 (mod 4分类)
        "source": "CC-002/1843",
        "text": """【参考思路——来自类似题目的解题脉络】

以下是一道结构相似的题目的解题过程，供参考其认知路径（不是本题的答案）：

题目背景：板上写着方程 (x-1)(x-2)…(x-2016)=(x-1)(x-2)…(x-2016)。擦去两边的一些线性因子，使每边至少剩一个因子，且结果方程无实根。求最少擦除数。

解题脉络：
1. 困境识别：2016个因子的符号分析太复杂——直接分析多项式的实根需要处理大量因子的符号组合，无法系统化。
2. 方向切换：按mod 4分类因子——k≡0,1(mod 4)的因子乘积与k≡2,3(mod 4)的因子乘积符号相反。切换到模4分析，将全局的符号问题转化为局部的模4分类问题。
3. 新方向操作：在模4下，因子按剩余类分组后，可以建立符号配对——每对因子（一个来自{0,1}类，一个来自{2,3}类）的乘积符号相反，使得方程无实根。
4. 提升回全局：通过模4分类的符号配对，确定最少擦除数=2016（每边留1008个因子，按mod 4配对）。局部发现（模4符号模式）提升为全局结论。

关键认知动作：将全局条件翻译为局部模约束 → 在模约束下发现结构模式 → 从局部模式推导全局结论。""",
    },
    "CC-105": {
        # CC-105 (mod 16奇偶case分裂) ← CC-004/1962 (v_2 case分裂)
        "source": "CC-004/1962",
        "text": """【参考思路——来自类似题目的解题脉络】

以下是一道结构相似的题目的解题过程，供参考其认知路径（不是本题的答案）：

题目背景：求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是2的幂。

解题脉络：
1. 困境识别：代数变形无法约束(a,b,c)——ab-c, bc-a, ca-b都是2的幂的条件在自然表示下太复杂，直接代数操作无法建立有效约束。
2. 方向切换：令v_2(ab-c)=u等，切换到2-adic赋值分析——在局部表示（2-adic赋值）下分析每个表达式的结构。
3. 新方向操作：按关键变量的相等/不等关系分case——a=b vs a<b<c是完全不同的分析路径。在每个case中，利用2-adic赋值的性质建立v_2方程，从赋值约束推导变量的可能值。
4. 提升回全局：从每个case的v_2约束综合出(a,b,c)的所有可能值。局部发现（每个case的赋值约束）提升为全局结论。

关键认知动作：引入p-adic赋值 → 按变量关系分case → 每个case独立分析 → 综合全局结论。""",
    },
}

# --- Hint-L3 (中等非特化程度, from POC-3.5-Asset-1) ---
HINT_L3 = "当问题在自然表示下陷入困境时，切换到局部表示Z/pZ。"

# --- Conditions ---
CONDITIONS = ["bare", "vein", "vein_hint", "hint"]

def generate_problem_file(cc_id, condition):
    """Generate a problem file for a given problem and condition."""
    prob = PROBLEMS[cc_id]
    lines = []
    lines.append("你是数学大师。请解答以下数学题。")
    lines.append("")
    lines.append(f"题目（{cc_id} / {prob['pid']}）：")
    lines.append(prob["statement"])
    lines.append("")

    if condition in ("vein", "vein_hint"):
        vein = VEINS[cc_id]
        lines.append(vein["text"])
        lines.append("")

    if condition in ("vein_hint", "hint"):
        lines.append("【解题策略提示】")
        lines.append(HINT_L3)
        lines.append("")

    lines.append("要求：")
    lines.append("1. 给出完整的解答过程")
    lines.append("2. 最终答案用 \\boxed{答案} 格式给出")
    lines.append("3. 数学公式用LaTeX")
    lines.append("4. 把证明写到proof.md文件中，不要在对话里输出完整证明")
    lines.append("")

    return "\n".join(lines)

# Generate all 16 files
generated = []
for cc_id in PROBLEMS:
    for cond in CONDITIONS:
        content = generate_problem_file(cc_id, cond)
        fname = f"{cc_id}_{cond}.txt"
        fpath = os.path.join(OUT_DIR, fname)
        with open(fpath, "w") as f:
            f.write(content)
        generated.append(fname)
        print(f"Generated: {fname} ({len(content)} chars)")

print(f"\nTotal: {len(generated)} files generated in {OUT_DIR}")
