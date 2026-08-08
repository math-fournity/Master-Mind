#!/usr/bin/env python3
"""
POC-VMS-7g-v3: 高Level hint泛化POC（奥赛难题版）- 对照组准备

8道bare失败的题 × 2组对照（knowledge + highlevel）= 16个AI
highlevel组所有题用同一个"翻译语言"hint——验证泛化性
"""

import json
import os
import shutil

REPO_DIR = '~/master-mind-glm5.2-worktree'

# 统一的"翻译语言"highlevel hint——所有题完全相同
HIGHLLEVEL_HINT = """=== 系统提示 ===

思维方向：不要在问题给定的原始语言中硬解。

把问题翻译到另一种数学语言——在原始语言中问题可能很复杂，但翻译后可能变得显然。

问自己：这个问题在另一种语言中会变成什么？什么语言能让这个问题变得简单？

常见的翻译方向：
- 从"枚举/构造"翻译到"结构/性质"
- 从"具体对象"翻译到"抽象不变量"
- 从"原始问题"翻译到"模运算/商结构/同态像"

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""

# 每道题的knowledge hint——从解答中提取关键知识
KNOWLEDGE_HINTS = {
    1610: """=== 系统提示 ===

相关知识：
1. 答案是 1/(2n+2)
2. 下界构造：把4n个点分成n个4元素簇，每簇放在 (i/(n+1)±ε, 1/2±ε)
3. 上界证明需要两个引理：
   - 引理1：k个不同点在(0,1)中，如果λ<1/(⌊k/2⌋+1)，则某个点可被长度≥λ的区间隔离
   - 引理2：⌊m₁/2⌋+Σ⌊mᵢ/2⌋+⌊mₖ/2⌋ ≤ Σmᵢ-k+2
4. 投影到x轴，对每个xᵢ用引理1隔离一个点
5. 如果所有xᵢ都不能隔离，用引理2推出矛盾

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",

    1631: """=== 系统提示 ===

相关知识：
1. 如果 y_n = 2^{x_n} - 1 是素数，则 x_n 必须是素数（因为 2^{mn}-1 被 2^m-1 整除）
2. 所以如果 y_1,...,y_k 都是素数，则 x_1,...,x_k 都是素数
3. x_1=a 是素数，x_2=2a+1，x_3=4a+3
4. 如果 a 是奇素数，则 x_2≡3(mod 4)，x_3≡7(mod 8)
5. 二次互反律：2是模p的二次剩余当且仅当 p≡±1(mod 8)
6. 所以当 x_3≡7(mod 8) 时，2是模 x_3 的二次剩余
7. Euler准则：2^{(p-1)/2}≡1(mod p) 当2是模p的二次剩余
8. 所以 2^{x_2}=2^{(x_3-1)/2}≡1(mod x_3)，即 x_3|y_2
9. 但 y_2=2^{x_2}-1>2x_2+1=x_3（当x_2>3），矛盾
10. a=2时 y_1=3, y_2=31 都是素数，y_3=2047=23×89 合数

用这些知识证明 k≤2 并给出 k=2 的例子。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",

    1645: """=== 系统提示 ===

相关知识：
1. 答案是0——即 a_{2015}·a_{2016}=0
2. 通过平移可以把问题转化为 a_0·a_1=0
3. a_n = n³+bn²+cn+d，所以 a_0=d, a_1=1+b+c+d
4. 关键：如果 a_0≠0 且 a_1≠0，利用相邻立方数序列的性质推出矛盾
5. 立方数序列的差分：a_{n+1}-a_n = 3n²+(3+b)n+(1+b+c)
6. 二阶差分是线性的，三阶差分是常数6
7. 利用"相邻两项都不为零"的假设，通过整除性分析推出 d=0 或 1+b+c+d=0

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",

    1681: """=== 系统提示 ===

相关知识：
1. 答案是 f(n)=n
2. 关键引理：对任意素数p和任意x,y∈N，x≡y(mod p)当且仅当f(x)≡f(y)(mod p)
3. 而且p|f(x)当且仅当p|x
4. 引理证明：考虑m+n≡0(mod p)，则p|f(m+n)，由条件f(m+n)|f(m)+f(n)...需要仔细推导
5. 由引理：f保持所有模p的同余类——即f(x)≡x(mod p)对所有素数p成立
6. 由中国剩余定理：f(x)=x（因为对所有素数p，p|(f(x)-x)）
7. 满射性保证f的像覆盖所有自然数

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",

    1662: """=== 系统提示 ===

相关知识：
1. 答案是3n
2. 构造3n个平面：x=i, y=i, z=i (i=1,...,n) 覆盖S但不包含原点
3. 下界证明需要两个引理：
   - 引理1：如果n个平面覆盖{0,1,...,n}³\{0}，则每个平面最多覆盖n²个点
   - 引理2：更精细的计数——考虑每个平面覆盖的点数
4. 关键思路：每个平面ax+by+cz=d覆盖的点数 ≤ n²（当d≠0时）
5. 总点数=(n+1)³-1=n³+3n²+3n，需要 ≥(n³+3n²+3n)/n² = n+3+3/n 个平面
6. 更精确的论证得到需要至少3n个平面

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",

    1694: """=== 系统提示 ===

相关知识：
1. 答案是k=3
2. k=3可行的例子：
   A₁={1,2,3}∪{3m | m≥4}
   A₂={4,5,6}∪{3m-1 | m≥4}
   A₃={7,8,9}∪{3m-2 | m≥4}
3. 验证：任意a∈Aᵢ, b∈Aⱼ, i≠j，则a+b∈Aₖ（某个k）
4. k≥4不可能的证明：
   - 假设有4个子集A₁,A₂,A₃,A₄
   - 考虑1所在的集合，设1∈A₁
   - 则2不能在A₁（因为1+1=2，如果2∈A₁则1+2=3需要不在A₁，但1∈A₁...）
   - 需要仔细分析1,2,3,4,5,6的分配
   - 关键：1+2=3, 1+3=4, 2+3=5, 1+4=5, 2+4=6, 3+4=7...
   - 用这些约束推出4个子集不可能

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",

    1760: """=== 系统提示 ===

相关知识：
1. 答案是∠BEA₁=90°和∠AEB₁=90°
2. 设K是JC和A₁B₁的交点
3. JC⊥A₁B₁（因为J是旁心，A₁B₁是旁切圆的弦）
4. A₁B₁⊥AB（旁切圆性质）
5. 从直角三角形B₁CJ得到 JC₁²=JB₁²=JC·JK=JC·C₁D
6. 关键是证明E在以A₁B₁为直径的圆上（即∠BEA₁=90°）
7. 和E在以AB₁为直径的圆上（即∠AEB₁=90°）
8. 利用旁切圆的切线性质和角度关系

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",

    1766: """=== 系统提示 ===

相关知识：
1. 将方程重写为 2^x(1+2^{x+1}) = (y-1)(y+1)
2. y-1 和 y+1 的差是2，所以它们的gcd整除2
3. 当 x>0 时，两边是偶数，所以 y 是奇数，y-1 和 y+1 都是偶数
4. 恰好其中一个被4整除，所以 x≥3
5. 其中一个因子被 2^{x-1} 整除但不被 2^x 整除
6. 设 y = 2^{x-1}m + ε，m奇，ε=±1
7. 代入原方程得到 1-εm = 2^{x-2}(m²-8)
8. ε=1时 m²-8≤0，即m=1，但不满足方程
9. ε=-1时 1+m = 2^{x-2}(m²-8) ≥ 2(m²-8)，推出 m≤3
10. m=3给出x=4, y=23
11. x=0时 y²=4, y=±2

用这些知识分ε=1和ε=-1讨论。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）""",
}


def main():
    with open('knowledge/problem_banks/aops_instruct/eval/data/olympiadbench/test.json') as f:
        data = json.load(f)

    problems_map = {r['id']: r for r in data}
    failed_ids = [1610, 1631, 1645, 1681, 1662, 1694, 1760, 1766]

    os.makedirs(f'{REPO_DIR}/runs/vms_poc_0/vms7gv3_problem_files', exist_ok=True)

    prepared = []
    for oid in failed_ids:
        r = problems_map[oid]
        problem_text = r['question'] + '\n\n要求：给出完整的解答，写入 proof.md 文件。'

        for group in ['knowledge', 'highlevel']:
            exp_id = f'vms-poc7gv3-{oid}-{group}'
            work_dir = f'/data/math-agent-glm5.2-tmux-agents-dir/{exp_id}'
            os.makedirs(work_dir, exist_ok=True)

            template = 'templates/solver_agents_md_guided.md'
            shutil.copy(f'{REPO_DIR}/{template}', f'{work_dir}/AGENTS.md')

            with open(f'{work_dir}/problem.txt', 'w', encoding='utf-8') as f:
                f.write(problem_text)

            prob_file = f'{REPO_DIR}/runs/vms_poc_0/vms7gv3_problem_files/{oid}_{group}.txt'
            with open(prob_file, 'w', encoding='utf-8') as f:
                f.write(problem_text)

            hint = KNOWLEDGE_HINTS[oid] if group == 'knowledge' else HIGHLLEVEL_HINT
            with open(f'{work_dir}/hint.txt', 'w', encoding='utf-8') as f:
                f.write(hint)

            prepared.append({
                'exp_id': exp_id,
                'file': f'runs/vms_poc_0/vms7gv3_problem_files/{oid}_{group}.txt',
                'olympiad_id': oid,
                'group': group,
                'subfield': r.get('subfield', '?'),
                'expected_answer': str(r.get('final_answer', ['?'])[0])[:50],
            })

    # 保存元数据
    with open(f'{REPO_DIR}/runs/vms_poc_0/vms7gv3_ab_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(prepared, f, ensure_ascii=False, indent=2)

    # 验证highlevel hint完全相同
    highlevel_exps = [p for p in prepared if p['group'] == 'highlevel']
    print(f'prepared {len(prepared)} experiments ({len(highlevel_exps)} highlevel + {len(prepared)-len(highlevel_exps)} knowledge)')
    print(f'\nhighlevel组（{len(highlevel_exps)}道题）的hint文本完全相同——泛化性验证前提')
    print(f'\n实验列表:')
    for p in prepared:
        print(f'  {p["exp_id"]}: id={p["olympiad_id"]} ({p["group"]}, {p["subfield"]})')


if __name__ == '__main__':
    main()
