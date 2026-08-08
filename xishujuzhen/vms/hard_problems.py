#!/usr/bin/env python3
"""
POC-VMS-6v2: 真正的动态引导A/B对照——用裸跑AI会失败的难题

难题设计原则：
1. 24阶以上群或需要非显然定理的题
2. 需要多步构造性证明
3. GLM-5.2裸跑大概率会失败或给出不完整答案
"""

import json
import os

REPO_DIR = '~/master-mind-glm5.2-worktree'


HARD_PROBLEMS = [
    {
        'pid': 'HARD_001_sylow_S4',
        'problem_type': 'subgroup_enumeration',
        'group_order': 24,
        'group_type': 'symmetric',
        'full_problem': """给定对称群 S₄（4次对称群，24阶），其元素为所有4个元素的置换。

S₄的元素按cycle type分为5类：
- 恒等：e（1个）
- 对换 (ij)：6个
- 三轮换 (ijk)：8个
- 四轮换 (ijkl)：6个
- 双对换 (ij)(kl)：3个

问题：用Sylow定理确定S₄的Sylow p-子群的结构和个数（对每个素因子p），并证明你的结论。""",
        'expected_answer': 'Sylow 2-子群：阶8，同构于D₄，个数n₂≡1(mod2)且n₂|3，n₂=3。Sylow 3-子群：阶3，同构于Z₃，个数n₃≡1(mod3)且n₃|8，n₃=4。',
        'difficulty': 'hard',
    },
    {
        'pid': 'HARD_002_semidirect_A4',
        'problem_type': 'group_structure_identification',
        'group_order': 12,
        'group_type': 'alternating',
        'full_problem': """给定交错群 A₄（4次交错群，12阶）。

已知：
- A₄有正规子群V₄={e, (12)(34), (13)(24), (14)(23)}（Klein四元群）
- A₄/V₄ ≅ Z₃

问题：证明 A₄ ≅ V₄ ⋊ Z₃（半直积），并明确构造这个半直积的同态φ: Z₃ → Aut(V₄)。

提示：Aut(V₄) ≅ S₃（V₄的自同构群同构于S₃）。""",
        'expected_answer': 'A₄ ≅ V₄ ⋊φ Z₃，其中φ: Z₃ → Aut(V₄)≅S₃把Z₃的生成元映到S₃的一个3阶元素（即V₄上的一个3轮换自同构）。',
        'difficulty': 'hard',
    },
    {
        'pid': 'HARD_003_class_equation_D6',
        'problem_type': 'conjugacy_class_computation',
        'group_order': 12,
        'group_type': 'dihedral',
        'full_problem': """给定二面体群 D₆（正六边形的对称群，12阶），其元素为 {e, r, r², r³, r⁴, r⁵, s, sr, sr², sr³, sr⁴, sr⁵}，
其中 r 是60度旋转（r⁶=e），s 是反射（s²=e, sr=r⁵s）。

问题：
1. 求D₆的所有共轭类
2. 用类方程验证你的结果：|D₆| = |Z(D₆)| + Σ[D₆:C(aᵢ)]
3. 求D₆的中心Z(D₆)""",
        'expected_answer': '共轭类：{e}, {r³}, {r,r⁵}, {r²,r⁴}, {s,sr²,sr⁴}, {sr,sr³,sr⁵}。中心Z(D₆)={e,r³}。类方程：12=2+1+2+2+3+3。',
        'difficulty': 'hard',
    },
    {
        'pid': 'HARD_004_homomorphism_S3_to_Z2',
        'problem_type': 'homomorphism_construction',
        'group_order': 6,
        'group_type': 'symmetric',
        'full_problem': """给定对称群 S₃ = {e, (12), (13), (23), (123), (132)}（6阶）和循环群 Z₂ = {0, 1}（2阶，模2加法）。

问题：
1. 求所有从S₃到Z₂的群同态φ: S₃ → Z₂
2. 对每个同态，确定其核ker(φ)和像im(φ)
3. 验证|S₃| = |ker(φ)| × |im(φ)|

要求：给出完整的构造和证明，不能只列答案。""",
        'expected_answer': '2个同态：平凡同态φ(g)=0（ker=S₃, im={0}）和符号同态φ(g)=sgn(g) mod 2（ker=A₃={e,(123),(132)}, im=Z₂）。验证：6=6×1和6=3×2。',
        'difficulty': 'hard',
    },
    {
        'pid': 'HARD_005_normal_series_S4',
        'problem_type': 'normal_subgroup_determination',
        'group_order': 24,
        'group_type': 'symmetric',
        'full_problem': """给定对称群 S₄（24阶）。

问题：
1. 求S₄的所有正规子群
2. 构造S₄的一个合成列（composition series）
3. 验证Jordan-Hölder定理：合成列的因子在同构意义下唯一

注意：S₄的正规子群不只是{e}和S₄——还有A₄和V₄。你需要证明这些是全部的正规子群。""",
        'expected_answer': '正规子群：{e}, V₄, A₄, S₄。合成列：S₄ ▷ A₄ ▷ V₄ ▷ {e}，因子为Z₂, Z₃, V₄≅Z₂×Z₂。',
        'difficulty': 'hard',
    },
    {
        'pid': 'HARD_006_quaternion_not_dihedral',
        'problem_type': 'group_structure_identification',
        'group_order': 8,
        'group_type': 'quaternion',
        'full_problem': """给定两个8阶群：
- Q₈ = {±1, ±i, ±j, ±k}（四元数群）
- D₄ = {e, r, r², r³, s, sr, sr², sr³}（二面体群）

问题：证明Q₈和D₄不同构。

要求：至少给出3个不同的证明方法（即3个不同的群不变量来区分它们）。""",
        'expected_answer': '3种方法：1) 元素阶分布不同（Q8有6个4阶元素，D4只有2个）；2) 子群结构不同（Q8的每个子群都正规，D4有非正规子群）；3) 阶2元素个数不同（Q8只有1个阶2元素-1，D4有5个阶2元素）',
        'difficulty': 'hard',
    },
]


def main():
    print("=== POC-VMS-6v2: 动态引导A/B对照（难题）===\n")
    
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms6v2_hard_problems.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(HARD_PROBLEMS, f, ensure_ascii=False, indent=2)
    print(f"保存 {len(HARD_PROBLEMS)} 道难题\n")
    
    for p in HARD_PROBLEMS:
        print(f"  {p['pid']}: {p['group_order']}阶{p['group_type']}, 难度={p['difficulty']}")
        print(f"    {p['full_problem'][:80]}...")
        print()


if __name__ == '__main__':
    main()
