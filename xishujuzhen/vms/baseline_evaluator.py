#!/usr/bin/env python3
"""
Baseline评估器 —— 提取AI答案并判分
"""

import json
import os
import re

BASELINE_DIR = '/data/math-agent-glm5.2-tmux-agents-trajectory'
SOLVER_DIR = '/data/math-agent-glm5.2-tmux-agents-dir'
REPO_DIR = '~/master-mind-glm5.2-worktree'


def extract_ai_answer(tmux_log_path: str) -> str:
    """从tmux_pipe.log提取AI的最终回答。"""
    with open(tmux_log_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 找最后一个boxed{...}（处理嵌套大括号）
    # 简单方法：找所有boxed出现位置，从最后一个开始匹配大括号
    last_boxed_idx = content.rfind('\\boxed{')
    if last_boxed_idx >= 0:
        # 从boxed{后开始匹配大括号
        start = last_boxed_idx + len('\\boxed{')
        depth = 1
        end = start
        while end < len(content) and depth > 0:
            if content[end] == '{':
                depth += 1
            elif content[end] == '}':
                depth -= 1
            end += 1
        return content[start:end-1].strip()
    # fallback：找"证毕"或"QED"标记
    if '证毕' in content or 'QED' in content:
        marker = '证毕' if '证毕' in content else 'QED'
        idx = content.rfind(marker)
        return content[max(0, idx-500):idx].strip()
    # fallback：返回最后1000字符
    return content[-1000:].strip()


def load_correct_answer(exp_id: str) -> dict:
    """从baseline_10_problems.json加载正确答案。"""
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/baseline_10_problems.json')) as f:
        probs = json.load(f)
    # exp_id格式：vms-poc0-baseline-XX
    idx = int(exp_id.split('-')[-1]) - 1
    return probs[idx]


def evaluate_one(exp_id: str) -> dict:
    """评估一道题。"""
    traj_dir = os.path.join(BASELINE_DIR, exp_id)
    tmux_log = os.path.join(traj_dir, 'tmux', 'tmux_pipe.log')

    correct = load_correct_answer(exp_id)

    if not os.path.exists(tmux_log):
        return {
            'exp_id': exp_id,
            'pid': correct['pid'],
            'challenge_template': correct['challenge_template'],
            'status': 'no_log',
            'ai_answer': '',
            'correct_answer': correct['answer_description'],
            'correct': False,
        }

    ai_answer = extract_ai_answer(tmux_log)

    # 读取完整log用于判断
    with open(tmux_log, 'r', encoding='utf-8') as f:
        full_log = f.read()

    # 简单判分逻辑：根据题目类型检查AI答案
    prob_type = correct['problem_type']
    is_correct = False

    # 元素符号归一化：将Unicode下标转为LaTeX格式（x₁→x_1）
    def normalize(s):
        import unicodedata
        subs = '₀₁₂₃₄₅₆₇₈₉'
        for i, c in enumerate(subs):
            s = s.replace(c, f'_{i}')
        return s

    full_log_norm = normalize(full_log)
    ai_answer_norm = normalize(ai_answer)

    if prob_type == 'subgroup_enumeration':
        # 检查AI是否列出了正确数量的子群
        correct_subs = correct['answer']
        correct_count = len(correct_subs)
        if '证毕' in full_log or 'QED' in full_log:
            # 检查AI答案中是否包含所有正确子群的元素（归一化后比较）
            all_found = True
            for sub in correct_subs:
                for elem in sub:
                    elem_norm = normalize(elem)
                    if elem_norm not in full_log_norm and elem not in full_log:
                        all_found = False
                        break
            if all_found:
                is_correct = True

    elif prob_type == 'normal_subgroup_determination':
        correct_answer = correct['answer_formatted']
        if '是' in correct_answer:
            is_correct = '是' in ai_answer or 'yes' in ai_answer.lower() or 'true' in ai_answer.lower()
        else:
            is_correct = '否' in ai_answer or 'no' in ai_answer.lower() or 'false' in ai_answer.lower()

    elif prob_type == 'cyclic_determination':
        is_cyclic = correct['answer']
        if is_cyclic:
            is_correct = '是' in ai_answer and '循环' in full_log
        else:
            is_correct = ('不是' in ai_answer or '否' in ai_answer) and '循环' in full_log

    elif prob_type == 'conjugacy_class_computation':
        correct_count = len(correct['answer'])
        # 在答案中找共轭类的数量
        if str(correct_count) in ai_answer or str(correct_count) in full_log[-2000:]:
            is_correct = True

    elif prob_type == 'center_computation':
        correct_center = set(correct['answer'])
        if '证毕' in full_log or 'QED' in full_log:
            all_found = True
            for elem in correct_center:
                elem_norm = normalize(elem)
                if elem_norm not in full_log_norm and elem not in full_log:
                    all_found = False
                    break
            if all_found:
                is_correct = True

    elif prob_type == 'homomorphism_construction':
        exists = correct['answer']
        if exists:
            is_correct = '存在' in ai_answer or 'exist' in ai_answer.lower()
        else:
            is_correct = '不存在' in ai_answer or 'not exist' in ai_answer.lower()

    return {
        'exp_id': exp_id,
        'pid': correct['pid'],
        'challenge_template': correct['challenge_template'],
        'challenge_type': correct['challenge_type'],
        'problem_type': prob_type,
        'status': 'evaluated',
        'ai_answer': ai_answer[:500],
        'correct_answer': correct['answer_description'],
        'correct': is_correct,
    }


def main():
    print("=== POC-VMS-0 Baseline 评估 ===\n")

    results = []
    for i in range(1, 11):
        exp_id = f'vms-poc0-baseline-{i:02d}'
        result = evaluate_one(exp_id)
        results.append(result)
        status = '✅' if result['correct'] else '❌'
        print(f"{status} {exp_id} | {result['challenge_template']} {result['challenge_type']}")
        print(f"   正确答案: {result['correct_answer']}")
        print(f"   AI答案: {result['ai_answer'][:200]}")
        print()

    # 统计
    correct_count = sum(1 for r in results if r['correct'])
    print(f"\n=== 总计: {correct_count}/10 正确 ===")

    # 按挑战模板统计
    template_stats = {}
    for r in results:
        t = r['challenge_template']
        if t not in template_stats:
            template_stats[t] = {'correct': 0, 'total': 0}
        template_stats[t]['total'] += 1
        if r['correct']:
            template_stats[t]['correct'] += 1

    print("\n按挑战模板:")
    for t in sorted(template_stats.keys()):
        s = template_stats[t]
        print(f"  {t}: {s['correct']}/{s['total']}")

    # 保存结果
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/baseline_results.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n结果已保存到 {output_path}")


if __name__ == '__main__':
    main()
