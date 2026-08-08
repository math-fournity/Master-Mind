#!/usr/bin/env python3
"""
POC-VMS-7g: 高Level hint泛化POC

2道题 × 3组对照 = 6个AI
- 题1（群论）：A₄没有6阶子群
- 题2（数论）：x²+y²=3无整数解

C组（翻译语言hint）的hint文本完全相同——验证泛化性
"""

import json
import os

REPO_DIR = '~/master-mind-glm5.2-worktree'


PROBLEMS = [
    {
        'pid': 'GEN_001_group_A4_no_order6',
        'domain': 'group_theory',
        'full_problem': """证明：交错群 A₄ 没有 6 阶子群。

注意：|A₄| = 12，而 6 | 12，所以 Lagrange 定理不排除 6 阶子群的存在。你需要用更精细的论证。

要求：给出完整的证明，写入 proof.md 文件。""",
        'expected_answer': '反证法：假设H是A₄的6阶子群，则[A₄:H]=2，指数2子群必正规。但A₄的正规子群只有{e},V₄,A₄，没有6阶的。矛盾。',
        'knowledge_hint': """=== 系统提示 ===

相关知识：
1. A₄的正规子群只有{e}, V₄={e,(12)(34),(13)(24),(14)(23)}, A₄本身
2. 指数2的子群必然正规（因为左陪集=右陪集，只有两个陪集）
3. 6阶子群在12阶群中的指数是2

用这些知识证明A₄没有6阶子群。

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
        'pid': 'GEN_002_number_theory_x2y2eq3',
        'domain': 'number_theory',
        'full_problem': """证明：方程 x² + y² = 3 没有整数解。

要求：给出完整的证明，写入 proof.md 文件。""",
        'expected_answer': '考虑模4。对任意整数n，n²≡0或1(mod 4)。所以x²+y²≡0,1,2(mod 4)。但3≡3(mod 4)。所以x²+y²≡3(mod 4)不可能，即x²+y²=3无整数解。',
        'knowledge_hint': """=== 系统提示 ===

相关知识：
1. 对任意整数n，n² mod 4只能是0或1
   - n偶数：n=2k, n²=4k²≡0(mod 4)
   - n奇数：n=2k+1, n²=4k²+4k+1≡1(mod 4)
2. 所以x²+y² mod 4只能是0, 1, 或2
3. 但3 mod 4 = 3

用这些知识证明x²+y²=3无整数解。

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
    print("=== POC-VMS-7g: 高Level hint泛化POC ===\n")
    
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms7g_problems.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(PROBLEMS, f, ensure_ascii=False, indent=2)
    print(f"保存 {len(PROBLEMS)} 道题\n")
    
    # 验证C组hint完全相同
    assert PROBLEMS[0]['highlevel_hint'] == PROBLEMS[1]['highlevel_hint'], "C组hint必须完全相同！"
    print("✅ C组（翻译语言hint）两道题的hint文本完全相同——泛化性验证前提成立\n")
    
    for p in PROBLEMS:
        print(f"  {p['pid']} ({p['domain']})")
        print(f"    题目: {p['full_problem'][:60]}...")
        print()


if __name__ == '__main__':
    main()
