#!/usr/bin/env python3
"""
POC-VMS-7g-v2: 高Level hint泛化POC（难题版）

2道题 × 3组对照 = 6个AI
- 题1（群论）：36阶群有非平凡正规子群——需要翻译到"群作用+置换表示"
- 题2（数论）：p≡3(mod 4)时x²≡-1(mod p)无解——需要翻译到"群论（Z_p*元素阶）"

C组（翻译语言hint）的hint文本完全相同——验证泛化性
题目难度：bare AI预期会token_limit失败
"""

import json
import os

REPO_DIR = '~/master-mind-glm5.2-worktree'


PROBLEMS = [
    {
        'pid': 'GEN_003_group_order36_normal',
        'domain': 'group_theory',
        'full_problem': """证明：如果 G 是 36 阶群，则 G 有非平凡正规子群。

（即：存在 N ⊴ G，N ≠ {e}，N ≠ G。）

要求：给出完整的证明，写入 proof.md 文件。""",
        'expected_answer': '36=2²×3²。n₃∈{1,4}。若n₃=1则Sylow 3-子群正规。若n₃=4，G作用在4个Sylow 3-子群上给出同态φ:G→S₄。kerφ⊴G。若kerφ非平凡则完成。若kerφ平凡则G嵌入S₄，但|G|=36>24=|S₄|，矛盾。所以kerφ非平凡。',
        'knowledge_hint': """=== 系统提示 ===

相关知识：
1. 36 = 2² × 3²
2. Sylow定理：n₃ ≡ 1(mod 3) 且 n₃ | 4，所以 n₃ ∈ {1, 4}
3. 如果 n₃ = 1，则唯一的 Sylow 3-子群是正规的
4. 如果 n₃ = 4，考虑 G 在 4 个 Sylow 3-子群上的共轭作用
5. 共轭作用给出同态 φ: G → S₄
6. ker(φ) 是 G 的正规子群
7. |S₄| = 24

用这些知识：分 n₃=1 和 n₃=4 两种情况讨论。

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
        'pid': 'GEN_004_number_theory_minus1_nonsquare',
        'domain': 'number_theory',
        'full_problem': """证明：如果 p 是素数且 p ≡ 3 (mod 4)，则同余方程

    x² ≡ -1 (mod p)

没有解。

要求：给出完整的证明，写入 proof.md 文件。""",
        'expected_answer': '反证法：设x²≡-1(mod p)有解。则x⁴≡1(mod p)且x²≢1(mod p)（因为-1≢1(mod p)当p>2）。所以x在Z_p*中的阶恰好是4。但Z_p*是p-1阶群，由Lagrange定理4|(p-1)。而p≡3(mod 4)意味着p-1≡2(mod 4)，4不整除p-1。矛盾。',
        'knowledge_hint': """=== 系统提示 ===

相关知识：
1. Z_p* = {1, 2, ..., p-1} 是 p-1 阶乘法群
2. Z_p* 是循环群（p 是素数时）
3. Lagrange定理：群中元素的阶整除群的阶
4. 如果 x² ≡ -1 (mod p)，则 x⁴ ≡ 1 (mod p)
5. 当 p > 2 时，-1 ≢ 1 (mod p)，所以 x² ≢ 1 (mod p)
6. 因此 x 在 Z_p* 中的阶恰好是 4
7. 由 Lagrange 定理，4 | (p-1)
8. 但 p ≡ 3 (mod 4) 意味着 p-1 ≡ 2 (mod 4)，4 不整除 p-1

用这些知识推出矛盾。

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
    print("=== POC-VMS-7g-v2: 高Level hint泛化POC（难题版）===\n")
    
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms7gv2_problems.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(PROBLEMS, f, ensure_ascii=False, indent=2)
    print(f"保存 {len(PROBLEMS)} 道题\n")
    
    # 验证C组hint完全相同
    assert PROBLEMS[0]['highlevel_hint'] == PROBLEMS[1]['highlevel_hint'], "C组hint必须完全相同！"
    print("✅ C组（翻译语言hint）两道题的hint文本完全相同\n")
    
    for p in PROBLEMS:
        print(f"  {p['pid']} ({p['domain']})")
        print(f"    题目: {p['full_problem'][:80]}...")
        print(f"    预期bare: 失败（需要翻译思维，bare会卡在原始语言中）")
        print()


if __name__ == '__main__':
    main()
