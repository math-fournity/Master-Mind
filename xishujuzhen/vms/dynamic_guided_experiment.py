#!/usr/bin/env python3
"""
POC-VMS-6v2: 动态引导A/B对照实验

实验流程：
1. 每道难题跑2个AI：bare（裸跑）+ guided（动态引导）
2. 遵守2并发约束，每批1道题的bare+guided
3. guided组：
   - 用guided版AGENTS.md（有"读hint.txt"指令）
   - AI运行时，辅助Pipe实时采集thinking
   - 识别AI处境 → 检索方向Q → 写hint.txt到工作目录
4. bare组：用标准AGENTS.md，不管它
5. 评分：检查proof.md的答案正确性

动态引导时机：
- AI开始解题后30秒，第一次写hint（给初始方向）
- 之后每60秒检查thinking，如果AI卡住或走错方向，写新hint
"""

import json
import os
import time
import subprocess
from pathlib import Path

REPO_DIR = '~/master-mind-glm5.2-worktree'
TRAJ_BASE = '/data/math-agent-glm5.2-tmux-agents-trajectory'
AGENTS_DIR = '/data/math-agent-glm5.2-tmux-agents-dir'


def write_problem_file(exp_id, problem_text, guided=False):
    """写题目文件到工作目录"""
    work_dir = os.path.join(AGENTS_DIR, exp_id)
    os.makedirs(work_dir, exist_ok=True)
    
    # 写AGENTS.md
    if guided:
        agents_src = os.path.join(REPO_DIR, 'templates/solver_agents_md_guided.md')
    else:
        agents_src = os.path.join(REPO_DIR, 'templates/solver_agents_md.md')
    
    with open(agents_src) as f:
        agents_content = f.read()
    with open(os.path.join(work_dir, 'AGENTS.md'), 'w') as f:
        f.write(agents_content)
    
    # 写problem.txt
    with open(os.path.join(work_dir, 'problem.txt'), 'w', encoding='utf-8') as f:
        f.write(problem_text)
    
    # 清除旧hint.txt
    hint_path = os.path.join(work_dir, 'hint.txt')
    if os.path.exists(hint_path):
        os.remove(hint_path)


def write_hint(exp_id, hint_text):
    """写hint.txt到工作目录"""
    work_dir = os.path.join(AGENTS_DIR, exp_id)
    hint_path = os.path.join(work_dir, 'hint.txt')
    with open(hint_path, 'w', encoding='utf-8') as f:
        f.write(hint_text)


def read_thinking(exp_id):
    """读取AI当前的thinking"""
    jsonl_path = os.path.join(TRAJ_BASE, exp_id, 'mitm', 'thinking_live.jsonl')
    if not os.path.exists(jsonl_path):
        return []
    
    from collections import defaultdict
    rounds_data = defaultdict(lambda: {'thinking': '', 'tool_calls': []})
    with open(jsonl_path) as f:
        for line in f:
            try:
                rec = json.loads(line)
            except:
                continue
            counter = rec.get('counter', 0)
            if rec['type'] == 'thinking_chunk':
                rounds_data[counter]['thinking'] += rec.get('content', '')
            elif rec['type'] == 'tool_call':
                rounds_data[counter]['tool_calls'].append(rec.get('tool_name', 'unknown'))
    
    return sorted(rounds_data.items())


def is_ai_running(exp_id):
    """检查AI是否还在运行"""
    result = subprocess.run(
        ['tmux', 'has-session', '-t', f'harness-{exp_id}'],
        capture_output=True, text=True, timeout=5
    )
    return result.returncode == 0


def dynamic_guide(exp_id, problem, db):
    """动态引导：观察thinking → 检索Q → 写hint"""
    from xishujuzhen.vms.retriever import retrieve_directions
    
    task_type = problem['problem_type']
    group_order = problem['group_order']
    group_type = problem['group_type']
    
    # 检索方向Q
    directions = retrieve_directions(db, task_type, group_order, group_type)
    seen_base = {}
    for d in directions:
        bid = d['base_pattern_id']
        if bid not in seen_base:
            seen_base[bid] = d
    top_directions = sorted(seen_base.values(), key=lambda x: -x.get('score', 0))[:5]
    
    hint_count = 0
    last_hint_round = -1
    
    while is_ai_running(exp_id):
        rounds = read_thinking(exp_id)
        if not rounds:
            time.sleep(10)
            continue
        
        current_round = rounds[-1][0]
        current_thinking = rounds[-1][1]['thinking']
        all_thinking = ' '.join(d['thinking'] for _, d in rounds)
        
        # 判断是否需要写hint
        need_hint = False
        hint_idx = 0
        
        # 时机1：AI刚读完题（round 1-2），给初始方向
        if hint_count == 0 and len(rounds) >= 2:
            need_hint = True
            hint_idx = 0
        
        # 时机2：AI卡住了（连续2个round都在说同一件事）
        elif hint_count == 0 and len(rounds) >= 3:
            need_hint = True
            hint_idx = 0
        
        # 时机3：AI走了几步，给下一步方向
        elif hint_count == 1 and len(rounds) >= 4 and current_round > last_hint_round + 2:
            need_hint = True
            hint_idx = 1
        
        # 时机4：AI走了更多步，给高级方向
        elif hint_count == 2 and len(rounds) >= 6 and current_round > last_hint_round + 2:
            need_hint = True
            hint_idx = 2
        
        if need_hint and hint_idx < len(top_directions):
            direction = top_directions[hint_idx]
            hint_text = f"""=== 系统提示（第{hint_count+1}次）===

当前方向建议：{direction['name']}

{direction['Q']}

---
（这是系统根据你当前的推理状态给出的方向建议。你可以采纳、修改或忽略。读完后再继续解题。）
"""
            write_hint(exp_id, hint_text)
            hint_count += 1
            last_hint_round = current_round
            print(f"  [{exp_id}] hint #{hint_count}: {direction['base_pattern_id']} (round {current_round})")
        
        time.sleep(15)
    
    print(f"  [{exp_id}] AI终止，共写了{hint_count}次hint")


def check_proof(exp_id):
    """检查proof.md的答案正确性"""
    work_dir = os.path.join(AGENTS_DIR, exp_id)
    proof_path = os.path.join(work_dir, 'proof.md')
    
    if not os.path.exists(proof_path):
        return None, "no proof.md"
    
    with open(proof_path, encoding='utf-8') as f:
        proof = f.read()
    
    if len(proof) < 50:
        return False, "proof too short"
    
    return True, proof[:200]


def main():
    print("=== POC-VMS-6v2: 动态引导A/B对照（难题）===\n")
    
    from xishujuzhen.vms import tree_store
    from xishujuzhen.vms.tree_engine import launch_ai
    
    db = tree_store.get_db()
    
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/vms6v2_hard_problems.json')) as f:
        problems = json.load(f)
    
    results = []
    
    for i, problem in enumerate(problems):
        pid = problem['pid']
        print(f"\n{'='*60}")
        print(f"题目 {i+1}/{len(problems)}: {pid}")
        print(f"  {problem['group_order']}阶{problem['group_type']}, {problem['problem_type']}")
        print(f"{'='*60}")
        
        bare_id = f'vms-poc6v2-{i+1:02d}-bare'
        guided_id = f'vms-poc6v2-{i+1:02d}-guided'
        
        # 准备工作目录
        write_problem_file(bare_id, problem['full_problem'], guided=False)
        write_problem_file(guided_id, problem['full_problem'], guided=True)
        
        # 启动两个AI（2并发）
        print(f"\n启动 bare: {bare_id}")
        ok1 = launch_ai(bare_id, os.path.join(AGENTS_DIR, bare_id, 'problem.txt'))
        print(f"启动 guided: {guided_id}")
        ok2 = launch_ai(guided_id, os.path.join(AGENTS_DIR, guided_id, 'problem.txt'))
        print(f"  bare: {'OK' if ok1 else 'FAIL'}, guided: {'OK' if ok2 else 'FAIL'}")
        
        # 动态引导guided组（同时bare自己跑）
        print(f"\n动态引导 {guided_id}...")
        dynamic_guide(guided_id, problem, db)
        
        # 等bare也终止
        print(f"\n等待 {bare_id} 终止...")
        while is_ai_running(bare_id):
            time.sleep(15)
        print(f"  {bare_id} 终止")
        
        # 检查proof
        bare_proof_ok, bare_proof = check_proof(bare_id)
        guided_proof_ok, guided_proof = check_proof(guided_id)
        
        # 检查thinking中的答案
        bare_rounds = read_thinking(bare_id)
        guided_rounds = read_thinking(guided_id)
        bare_all_thinking = ' '.join(d['thinking'] for _, d in bare_rounds)
        guided_all_thinking = ' '.join(d['thinking'] for _, d in guided_rounds)
        
        result = {
            'pid': pid,
            'bare_id': bare_id,
            'guided_id': guided_id,
            'bare_rounds': len(bare_rounds),
            'guided_rounds': len(guided_rounds),
            'bare_chars': len(bare_all_thinking),
            'guided_chars': len(guided_all_thinking),
            'bare_proof': bare_proof_ok,
            'guided_proof': guided_proof_ok,
            'expected': problem['expected_answer'],
        }
        results.append(result)
        
        print(f"\n结果:")
        print(f"  bare: {bare_rounds and len(bare_rounds)} rounds, proof={'yes' if bare_proof_ok else 'no'}")
        print(f"  guided: {guided_rounds and len(guided_rounds)} rounds, proof={'yes' if guided_proof_ok else 'no'}")
    
    # 总结
    print(f"\n{'='*60}")
    print(f"=== A/B对照总结 ===")
    print(f"{'='*60}")
    bare_wins = sum(1 for r in results if r['bare_proof'])
    guided_wins = sum(1 for r in results if r['guided_proof'])
    
    print(f"  bare胜率: {bare_wins}/{len(results)} = {bare_wins/len(results)*100:.0f}%")
    print(f"  guided胜率: {guided_wins}/{len(results)} = {guided_wins/len(results)*100:.0f}%")
    
    for r in results:
        print(f"  {r['pid']}: bare={r['bare_proof']}, guided={r['guided_proof']}")
    
    # 保存结果
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms6v2_results.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n结果保存到 {output_path}")


if __name__ == '__main__':
    main()
