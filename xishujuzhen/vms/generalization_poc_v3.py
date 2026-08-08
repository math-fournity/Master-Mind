#!/usr/bin/env python3
"""
POC-VMS-7g-v3: 高Level hint泛化POC（奥赛难题版）

2道奥赛题 × 3组对照 = 6个AI
- 题1（数论）：1+2^x+2^{2x+1}=y²——翻译到因式分解+2-adic赋值
- 题2（代数）：Mersenne序列最大k——翻译到二次剩余

C组（翻译语言hint）的hint文本完全相同——验证泛化性
题目难度：奥赛级，bare AI预期会失败
"""

import json
import os

REPO_DIR = '~/master-mind-glm5.2-worktree'


PROBLEMS = [
    {
        'pid': 'GEN_005_nt_equation_2x_y2',
        'domain': 'number_theory',
        'source': 'OlympiadBench id=1766',
        'full_problem': """Determine all pairs $(x, y)$ of integers satisfying the equation

$$1 + 2^x + 2^{2x+1} = y^2$$

要求：给出完整的解答，写入 proof.md 文件。""",
        'expected_answer': '(0,±2), (4,±23)',
        'knowledge_hint': """=== 系统提示 ===

相关知识：
1. 将方程重写为 $2^x(1 + 2^{x+1}) = (y-1)(y+1)$
2. $y-1$ 和 $y+1$ 的差是2，所以它们的gcd整除2
3. 当 $x > 0$ 时，两边是偶数，所以 $y$ 是奇数，$y-1$ 和 $y+1$ 都是偶数
4. 恰好其中一个被4整除，所以 $x \geq 3$
5. 其中一个因子被 $2^{x-1}$ 整除但不被 $2^x$ 整除
6. 设 $y = 2^{x-1}m + \epsilon$，$m$ 奇，$\epsilon = \pm 1$
7. 代入原方程得到 $1 - \epsilon m = 2^{x-2}(m^2 - 8)$

用这些知识分 $\epsilon = 1$ 和 $\epsilon = -1$ 讨论。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",
        'highlevel_hint': """=== 系统提示 ===

思维方向：不要在问题给定的原始语言中硬解。

把问题翻译到另一种数学语言——在原始语言中问题可能很复杂，但翻译后可能变得显然。

问自己：这个问题在另一种语言中会变成什么？什么语言能让这个问题变得简单？

常见的翻译方向：
- 从"枚举/构造"翻译到"结构/性质"
- 从"具体对象"翻译到"抽象不变量"
- 从"原始问题"翻译到"模运算/商结构/同态像"

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",
    },
    {
        'pid': 'GEN_006_alg_mersenne_sequence',
        'domain': 'algebra',
        'source': 'OlympiadBench id=1631',
        'full_problem': """For a positive integer $a$, define a sequence of integers $x_1, x_2, \\ldots$ by letting $x_1 = a$ and $x_{n+1} = 2x_n + 1$ for $n \\geq 1$. Let $y_n = 2^{x_n} - 1$. Determine the largest possible $k$ such that, for some positive integer $a$, the numbers $y_1, y_2, \\ldots, y_k$ are all prime.

要求：给出完整的解答，写入 proof.md 文件。""",
        'expected_answer': 'k=2 (a=2: y1=3, y2=31 are prime, y3=2047=23×89 is composite)',
        'knowledge_hint': """=== 系统提示 ===

相关知识：
1. 如果 $y_n = 2^{x_n} - 1$ 是素数，则 $x_n$ 必须是素数（因为 $2^{mn} - 1$ 被 $2^m - 1$ 整除）
2. 所以如果 $y_1, \ldots, y_k$ 都是素数，则 $x_1, \ldots, x_k$ 都是素数
3. $x_1 = a$ 是素数，$x_2 = 2a+1$，$x_3 = 4a+3$
4. 如果 $a$ 是奇素数，则 $x_2 \equiv 3 \pmod{4}$，$x_3 \equiv 7 \pmod{8}$
5. 二次互反律：2是模p的二次剩余当且仅当 $p \equiv \pm 1 \pmod{8}$
6. 所以当 $x_3 \equiv 7 \pmod{8}$ 时，2是模 $x_3$ 的二次剩余
7. Euler准则：$2^{(p-1)/2} \equiv 1 \pmod{p}$ 当2是模p的二次剩余
8. 所以 $2^{x_2} = 2^{(x_3-1)/2} \equiv 1 \pmod{x_3}$，即 $x_3 | y_2$
9. 但 $y_2 = 2^{x_2} - 1 > 2x_2 + 1 = x_3$（当 $x_2 > 3$），矛盾

用这些知识证明 $k \leq 2$，并给出 $k = 2$ 的例子。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",
        'highlevel_hint': """=== 系统提示 ===

思维方向：不要在问题给定的原始语言中硬解。

把问题翻译到另一种数学语言——在原始语言中问题可能很复杂，但翻译后可能变得显然。

问自己：这个问题在另一种语言中会变成什么？什么语言能让这个问题变得简单？

常见的翻译方向：
- 从"枚举/构造"翻译到"结构/性质"
- 从"具体对象"翻译到"抽象不变量"
- 从"原始问题"翻译到"模运算/商结构/同态像"

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",
    },
]


def main():
    print("=== POC-VMS-7g-v3: 高Level hint泛化POC（奥赛难题版）===\n")
    
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms7gv3_problems.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(PROBLEMS, f, ensure_ascii=False, indent=2)
    print(f"保存 {len(PROBLEMS)} 道题\n")
    
    # 验证C组hint完全相同
    assert PROBLEMS[0]['highlevel_hint'] == PROBLEMS[1]['highlevel_hint'], "C组hint必须完全相同！"
    print("✅ C组（翻译语言hint）两道题的hint文本完全相同\n")
    
    for p in PROBLEMS:
        print(f"  {p['pid']} ({p['domain']}, {p['source']})")
        print(f"    题目: {p['full_problem'][:80]}...")
        print(f"    预期答案: {p['expected_answer']}")
        print()


if __name__ == '__main__':
    main()
