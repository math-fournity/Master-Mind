#!/usr/bin/env python3
"""
POC-VMS-8: 高Level Hint系统化Low Level化的Power验证

四组对照：A(bare) / B(抽象hint) / C(字典遍历) / D(字典匹配)
6道奥赛题 × 4组 = 24个AI

字典：runs/vms_poc_0/vms8_translation_dictionary.json（已冻结）
"""

import json
import os
import shutil

REPO_DIR = '~/master-mind-glm5.2-worktree'

# 加载冻结的字典
with open(f'{REPO_DIR}/runs/vms_poc_0/vms8_translation_dictionary.json') as f:
    DICTIONARY = json.load(f)

# 字典文本（给C组用）
def make_dictionary_text():
    lines = ["=== 翻译方向字典 ===", ""]
    lines.append("以下是一个数学翻译方向的完整字典。每个条目描述了一种把问题从原始语言翻译到另一种数学语言的方法。")
    lines.append("请遍历这些翻译方向，逐一尝试：你的问题在哪种翻译下会变得可解？")
    lines.append("")
    for t in DICTIONARY['translations']:
        lines.append(f"[{t['id']}] {t['form']}")
        lines.append(f"  源领域: {t['source_domain']}")
        lines.append(f"  目标领域: {t['target_domain']}")
        lines.append(f"  描述: {t['description']}")
        lines.append(f"  信号: {t['typical_signal']}")
        lines.append(f"  威力: {t['power']}")
        lines.append("")
    lines.append("---")
    lines.append("（遍历上述翻译方向，找到能让你的问题变得可解的那个。然后在该方向下解题。最终答案必须写入proof.md文件。）")
    return "\n".join(lines)

DICTIONARY_TEXT = make_dictionary_text()

# 抽象hint（B组——和7g-v3一样）
ABSTRACT_HINT = """=== 系统提示 ===

思维方向：不要在问题给定的原始语言中硬解。

把问题翻译到另一种数学语言——在原始语言中问题可能很复杂，但翻译后可能变得显然。

问自己：这个问题在另一种语言中会变成什么？什么语言能让这个问题变得简单？

常见的翻译方向：
- 从"枚举/构造"翻译到"结构/性质"
- 从"具体对象"翻译到"抽象不变量"
- 从"原始问题"翻译到"模运算/商结构/同态像"

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""

# 每道题的匹配翻译（D组用——从字典中人工匹配正确的翻译方向）
MATCHED_HINTS = {
    1843: {
        # 代数方程→模4分类：把"擦除因子使无实根"翻译到"按模4分组"
        "translation_id": "T01",
        "hint": """=== 系统提示 ===

匹配的翻译方向：[T01] 翻译到模算术

把整数方程/不等式/存在性问题转化为模p（或模n）的同余问题。

具体到本题：把因子按模4分类——擦除左边k≡2,3(mod 4)的因子，擦除右边m≡0,1(mod 4)的因子。然后证明剩下的方程无实根。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""
    },
    1738: {
        # 多项式平方和→模8的整数平方和约束
        "translation_id": "T01",
        "hint": """=== 系统提示 ===

匹配的翻译方向：[T01] 翻译到模算术

把整数方程/不等式/存在性问题转化为模p（或模n）的同余问题。

具体到本题：把有理系数多项式平方和的问题，通分后转化为整数平方和的模8约束。利用"整数平方模8只能是0,1,4"这一性质推出矛盾。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""
    },
    1962: {
        # ab-c是2的幂→2-adic赋值
        "translation_id": "T02",
        "hint": """=== 系统提示 ===

匹配的翻译方向：[T02] 翻译到p-adic赋值

把整除/幂次/因子分解问题转化为p-adic赋值分析。v_p(x)表示x中p的幂次，把乘法关系转化为加法关系。

具体到本题：ab-c, bc-a, ca-b都是2的幂。用2-adic赋值分析a,b,c的结构——它们的奇偶性、2的幂次如何分配。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""
    },
    1766: {
        # y²-1=(y-1)(y+1)→2-adic赋值分析因子结构
        "translation_id": "T02",
        "hint": """=== 系统提示 ===

匹配的翻译方向：[T02] 翻译到p-adic赋值

把整除/幂次/因子分解问题转化为p-adic赋值分析。v_p(x)表示x中p的幂次，把乘法关系转化为加法关系。

具体到本题：把方程重写为2^x(1+2^{x+1})=(y-1)(y+1)，用2-adic赋值分析y-1和y+1中2的幂次分配。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""
    },
    1631: {
        # Mersenne素数→二次剩余（Euler准则）
        "translation_id": "T03",
        "hint": """=== 系统提示 ===

匹配的翻译方向：[T03] 翻译到二次剩余/Legendre符号

把'某数是否为平方'、'方程是否有解'的问题转化为二次剩余判定。用Legendre符号/Euler准则计算2^{(p-1)/2} mod p。

具体到本题：需要证明y_3=2^{x_3}-1是合数。用Euler准则——当x_3≡7(mod 8)时，2是模x_3的二次剩余，所以2^{(x_3-1)/2}≡1(mod x_3)，即x_3|y_2。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""
    },
    1974: {
        # 组合→模算术（棋盘rook配置→模ℓ分组）
        "translation_id": "T01",
        "hint": """=== 系统提示 ===

匹配的翻译方向：[T01] 翻译到模算术

把整数方程/不等式/存在性问题转化为模p（或模n）的同余问题。

具体到本题：把棋盘rook配置问题中的列按模ℓ分组。如果n>ℓ²，用鸽巢原理证明存在空ℓ×ℓ方格。

---
（读完后再继续解题。最终答案必须写入proof.md文件。）"""
    },
}

SELECTED_IDS = [1843, 1738, 1962, 1766, 1631, 1974]


def main():
    with open(f'{REPO_DIR}/knowledge/problem_banks/aops_instruct/eval/data/olympiadbench/test.json') as f:
        data = json.load(f)
    problems_map = {r['id']: r for r in data}

    os.makedirs(f'{REPO_DIR}/runs/vms_poc_0/vms8_problem_files', exist_ok=True)

    experiments = []
    for oid in SELECTED_IDS:
        r = problems_map[oid]
        problem_text = r['question'] + '\n\n要求：给出完整的解答，写入 proof.md 文件。'

        for group, template, hint in [
            ('bare', 'templates/solver_agents_md.md', None),
            ('abstract', 'templates/solver_agents_md_guided.md', ABSTRACT_HINT),
            ('dictionary', 'templates/solver_agents_md_guided.md', DICTIONARY_TEXT),
            ('matched', 'templates/solver_agents_md_guided.md', MATCHED_HINTS[oid]['hint']),
        ]:
            exp_id = f'vms-poc8-{oid}-{group}'
            work_dir = f'/data/math-agent-glm5.2-tmux-agents-dir/{exp_id}'
            os.makedirs(work_dir, exist_ok=True)
            shutil.copy(f'{REPO_DIR}/{template}', f'{work_dir}/AGENTS.md')
            with open(f'{work_dir}/problem.txt', 'w', encoding='utf-8') as f:
                f.write(problem_text)

            prob_file = f'runs/vms_poc_0/vms8_problem_files/{oid}_{group}.txt'
            with open(f'{REPO_DIR}/{prob_file}', 'w', encoding='utf-8') as f:
                f.write(problem_text)

            if hint:
                with open(f'{work_dir}/hint.txt', 'w', encoding='utf-8') as f:
                    f.write(hint)

            experiments.append({
                'exp_id': exp_id,
                'file': prob_file,
                'olympiad_id': oid,
                'group': group,
                'subfield': r.get('subfield', '?'),
                'expected_answer': str(r.get('final_answer', ['?'])[0])[:50],
            })

    with open(f'{REPO_DIR}/runs/vms_poc_0/vms8_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(experiments, f, ensure_ascii=False, indent=2)

    print(f'prepared {len(experiments)} experiments ({len(SELECTED_IDS)} problems × 4 groups)')
    print(f'\n字典: {len(DICTIONARY["translations"])} 个翻译方向')
    print(f'\n实验列表:')
    for e in experiments:
        print(f'  {e["exp_id"]}: id={e["olympiad_id"]} ({e["group"]}, {e["subfield"]})')


if __name__ == '__main__':
    main()
