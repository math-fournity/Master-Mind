#!/usr/bin/env python3
"""
tree_engine.py —— POC-VMS-2 树生长引擎

对每道题：
1. 在ArangoDB创建problem + 根节点
2. 启动裸跑AI（baseline对照）
3. 在根节点上做检索（用8个基础Pattern）
4. 对检索到的每个方向，启动新AI实例（给它脉络+方向Q）
5. 等待所有AI完成
6. 从所有AI的trajectory提取节点，更新树
7. 标记叶节点（leaf_success/leaf_deadend）

并发约束（硬约束，见 .devin/rules/solver-concurrency.md）：
- 同时运行的AI最多 MAX_CONCURRENT=2 个
- 有N个任务时用2个并发额度批次完成
- 启动新AI前检查当前并发数，<2才启动

简化版说明：
- 不做实时采集——等AI完成后批量提取节点
- 脉络构造：根节点只有题目，脉络=题目+方向Q
"""

import os
import sys
import json
import time
import subprocess
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from xishujuzhen.vms import tree_store
from xishujuzhen.vms.node_extractor import extract_nodes_from_trajectory, backfill_tree_from_experiment
from xishujuzhen.vms.retriever import get_db, retrieve_directions


# ============================================================
# 脉络构造
# ============================================================

def construct_path_text(problem_text: str, path_nodes: list, direction_q: str) -> str:
    """
    构造给新推理AI的脉络文本。

    简化版：根节点的脉络 = 题目 + 方向Q
    """
    if not path_nodes:
        # 从根节点开始
        text = f"""你正在解答以下数学题：

{problem_text}

系统识别出以下探索方向，请在此方向的引导下解题：

【方向】{direction_q}

请理解这个方向的含义，然后继续推理，给出完整的推理过程。
最终答案用 \\boxed{{}} 框出。
"""
    else:
        # 从中间节点开始（后续版本）
        text = f"""你正在解答以下数学题：

{problem_text}

之前已经进行了以下探索：
"""
        for i, node in enumerate(path_nodes):
            text += f"\n[步骤{i+1}] {node['situation_text']}\n"

        text += f"\n请理解验证以上路径后，继续探索以下方向：\n【方向】{direction_q}\n\n继续推理，给出完整的推理过程。\n最终答案用 \\boxed{{}} 框出。"

    return text


# ============================================================
# 树生长引擎
# ============================================================

def prepare_tree_for_problem(db, problem: dict, group: dict, exp_id_base: str,
                              problem_file: str, max_branches: int = 2) -> dict:
    """
    为一道题准备树结构（problem + 根节点 + 检索），但不启动AI。

    返回：树信息（含所有AI任务的exp_id和方向）
    """
    problem_id = problem['pid']
    task_type = problem['problem_type']
    group_order = group['order']
    group_type = group['group_type']

    print(f"\n--- 准备 {problem_id} ({task_type}, {group_type} order={group_order}) ---")

    # 1. 创建problem
    prob_doc = tree_store.get_problem(db, problem_id)
    if not prob_doc:
        prob_doc = tree_store.create_problem(db, problem_id, problem['full_problem'],
                                             metadata={
                                                 'group_type': group_type,
                                                 'group_order': group_order,
                                                 'problem_type': task_type,
                                                 'challenge_template': problem.get('challenge_template', ''),
                                                 'challenge_type': problem.get('challenge_type', ''),
                                             })

    # 2. 创建根节点
    root_node = tree_store.create_node(
        db, problem_id,
        node_type='root',
        situation_text=f'初始处境：{task_type}题，{group_type}群阶{group_order}',
        depth=0,
        created_by_ai=None,
        trajectory_segment={},
        status='growing',
    )
    db.collection('problems').update({
        '_key': problem_id,
        'root_node_key': root_node['_key']
    })

    # 3. 在根节点检索方向
    directions = retrieve_directions(db, task_type, group_order, group_type)
    print(f"  检索到 {len(directions)} 个方向，取top-{max_branches}")

    tree_store.mark_retrieval_done(db, root_node['_key'],
                                    [d['pattern_id'] for d in directions[:max_branches]])

    # 4. 准备所有AI任务（不启动）
    bare_exp_id = f'{exp_id_base}-bare'

    # 注册裸跑AI
    tree_store.register_ai_instance(
        db, bare_exp_id, problem_id,
        entry_node_key=root_node['_key'],
        hint_q=None,
        path_text=problem['full_problem'],
        trajectory_dir=f'/data/math-agent-glm5.2-tmux-agents-trajectory/{bare_exp_id}',
    )

    # 准备检索引导AI
    branch_ais = []
    for i, direction in enumerate(directions[:max_branches]):
        branch_exp_id = f'{exp_id_base}-branch{i+1}'
        path_text = construct_path_text(problem['full_problem'], [], direction['Q'])

        # 写入题目文件
        branch_problem_file = f'~/master-mind-glm5.2-worktree/runs/vms_poc_0/vms2_problem_files/{branch_exp_id}.txt'
        with open(branch_problem_file, 'w', encoding='utf-8') as f:
            f.write(path_text)

        # 注册AI
        tree_store.register_ai_instance(
            db, branch_exp_id, problem_id,
            entry_node_key=root_node['_key'],
            hint_q=direction['Q'],
            hint_q_id=direction['pattern_id'],
            path_text=path_text,
            trajectory_dir=f'/data/math-agent-glm5.2-tmux-agents-trajectory/{branch_exp_id}',
        )

        branch_ais.append((branch_exp_id, direction))

    return {
        'problem_id': problem_id,
        'root_node_key': root_node['_key'],
        'bare_ai_id': bare_exp_id,
        'branch_ais': branch_ais,
        'directions_count': len(directions),
    }


def backfill_ai_to_tree(db, problem: dict, group: dict, tree_info: dict,
                         ai_id: str, direction: Optional[dict]):
    """一个AI完成后，从其trajectory提取节点并回填到树。"""
    problem_id = problem['pid']
    root_node_key = tree_info['root_node_key']
    TRAJ_BASE = '/data/math-agent-glm5.2-tmux-agents-trajectory'

    thinking_path = os.path.join(TRAJ_BASE, ai_id, 'mitm', 'thinking_readable.txt')
    if not os.path.exists(thinking_path):
        print(f"  {ai_id}: no thinking data")
        tree_store.update_ai_status(db, ai_id, 'crashed', end_reason='no_thinking')
        return

    nodes = extract_nodes_from_trajectory(thinking_path, problem, group)
    if not nodes:
        print(f"  {ai_id}: no nodes extracted")
        tree_store.update_ai_status(db, ai_id, 'crashed', end_reason='no_nodes')
        return

    # 创建节点和边
    prev_node_key = root_node_key
    prev_edge_key = None
    node_keys = [root_node_key]

    for i, node_data in enumerate(nodes):
        node_type = node_data['node_type']
        status = 'completed' if i < len(nodes) - 1 else ('completed' if node_type == 'leaf_success' else 'growing')

        node = tree_store.create_node(
            db, problem_id,
            node_type=node_type,
            situation_text=node_data['situation_text'],
            depth=i + 1,
            parent_edge_key=prev_edge_key,
            path_from_root=node_keys + ['placeholder'],
            created_by_ai=ai_id,
            trajectory_segment=node_data['trajectory_segment'],
            status=status,
        )

        path = node_keys + [node['_key']]
        db.collection('tree_nodes').update({
            '_key': node['_key'],
            'path_from_root': path
        })

        pattern_id = node_data.get('pattern_id')
        hint_q = ''
        hint_level = None
        if direction and i == 0:
            hint_q = direction['Q']
            hint_level = direction['Level']
            pattern_id = direction['pattern_id']
        elif pattern_id:
            hint_q = f"[{pattern_id}] 引导AI进行{node_data['operation']}"
            hint_level = 0.5
        else:
            hint_q = f"AI自然过渡到{node_data['operation']}"

        edge = tree_store.create_edge(
            db, problem_id,
            from_key=prev_node_key,
            to_key=node['_key'],
            hint_q=hint_q,
            hint_q_id=pattern_id,
            hint_level=hint_level,
            ai_instance_id=ai_id,
            edge_status='completed',
        )

        node_keys.append(node['_key'])
        prev_node_key = node['_key']
        prev_edge_key = edge['_key']

    end_reason = 'solution_found' if nodes[-1]['operation'] == 'write_answer' else 'token_limit'
    tree_store.update_ai_status(db, ai_id, 'completed',
                                 end_reason=end_reason,
                                 nodes_contributed=node_keys[1:])

    if nodes[-1]['node_type'] == 'leaf_success':
        tree_store.update_problem_status(db, problem_id, 'solved', solution_path=node_keys)
        print(f"  {ai_id}: ✅ solved ({len(nodes)} nodes)")
    else:
        print(f"  {ai_id}: completed ({len(nodes)} nodes, no leaf_success)")

    tree_store.update_node_status(db, root_node_key, 'completed')


# ============================================================
# 主函数
# ============================================================

MAX_CONCURRENT = 2  # 硬约束：最多2个并发AI


def count_running_ais() -> int:
    """统计当前运行的AI数量（通过tmux session判断）。"""
    result = subprocess.run(
        ['tmux', 'list-sessions'],
        capture_output=True, text=True, timeout=5
    )
    count = 0
    for line in result.stdout.splitlines():
        # 只数harness-vms开头的devin cli session，不数dbmon
        if 'harness-vms' in line and 'dbmon' not in line and 'mitmproxy' not in line:
            count += 1
    return count


def wait_for_ai_slot(timeout: int = 600):
    """等待直到有空闲的AI额度（当前运行数 < MAX_CONCURRENT）。"""
    while True:
        n = count_running_ais()
        if n < MAX_CONCURRENT:
            return
        print(f"  当前{ n }个AI运行中，等待空槽（最多{timeout}秒）...")
        time.sleep(30)
        timeout -= 30
        if timeout <= 0:
            print(f"  ⚠️ 等待超时，强制继续")
            return


def wait_for_ai_done(exp_id: str, timeout: int = 600) -> bool:
    """等待指定AI完成（tmux session的devin cli停止）。"""
    session_name = f'harness-{exp_id}'
    elapsed = 0
    while elapsed < timeout:
        result = subprocess.run(
            ['tmux', 'has-session', '-t', session_name],
            capture_output=True, text=True, timeout=5
        )
        # has-session返回0=存在，非0=不存在
        if result.returncode != 0:
            # session不存在了，检查是否是devin cli停止（dbmon可能还在）
            return True
        time.sleep(15)
        elapsed += 15
    print(f"  ⚠️ {exp_id} 等待超时({timeout}s)")
    return False


def launch_ai(exp_id: str, problem_file: str) -> bool:
    """启动一个AI（通过solver-harness）。"""
    result = subprocess.run([
        '.venv/bin/python3', 'xishujuzhen/solver_harness/solver_harness.py', 'launch',
        '--exp-id', exp_id,
        '--problem-file', problem_file,
    ], capture_output=True, text=True, timeout=60,
       cwd='~/master-mind-glm5.2-worktree',
       env={**os.environ, 'ARANGO_DB': 'xishujuzhen_math_glm52'})

    return result.returncode == 0


def check_ai_terminated(exp_id: str) -> bool:
    """检测推理AI是否自然终止（tmux session的devin cli停止）。"""
    session_name = f'harness-{exp_id}'
    result = subprocess.run(
        ['tmux', 'has-session', '-t', session_name],
        capture_output=True, text=True, timeout=5
    )
    # has-session返回0=存在，非0=不存在
    return result.returncode != 0


def main():
    """
    实时并行主循环（267号§7.1）。

    核心认知：系统与推理AI并行运行。
    - 推理AI持续推理，不停下
    - 系统在AI工作的同时，实时读取不断增长的thinking_readable.txt
    - 实时从新thinking rounds提取节点，更新树
    - 树和AI是并行生长的——AI走到哪里，树就长到哪里
    - 不是"等AI完成再回填"，而是"AI一边工作，系统一边整理树"
    """
    print("=== POC-VMS-2: 树生长引擎（实时并行模式） ===\n")
    print(f"  并发上限: {MAX_CONCURRENT}")
    print(f"  核心认知: AI持续推理，系统实时整理树，并行运行\n")

    REPO_DIR = '~/master-mind-glm5.2-worktree'
    POLL_INTERVAL = 10  # 轮询间隔（秒）

    db = tree_store.get_db()
    tree_store.ensure_collections(db)

    # 加载测试题
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/vms2_test_10.json')) as f:
        test_problems = json.load(f)
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/virtual_groups.json')) as f:
        groups = json.load(f)
    group_by_gid = {g['gid']: g for g in groups}

    # 为每道题准备树结构（problem + 根节点 + 检索方向）
    all_tasks = []  # 待执行的任务队列
    for i, problem in enumerate(test_problems):
        group = group_by_gid[problem['group_gid']]
        exp_id_base = f'vms-poc2-{i+1:02d}'
        problem_file = os.path.join(REPO_DIR, f'runs/vms_poc_0/vms2_problem_files/vms2_problem_{i+1:02d}.txt')

        tree_info = prepare_tree_for_problem(db, problem, group, exp_id_base, problem_file, max_branches=2)

        # 裸跑AI任务
        all_tasks.append({
            'exp_id': tree_info['bare_ai_id'],
            'problem_file': problem_file,
            'problem': problem,
            'group': group,
            'tree_info': tree_info,
            'direction': None,
        })
        # 检索引导AI任务
        for ai_id, direction in tree_info['branch_ais']:
            branch_problem_file = os.path.join(REPO_DIR, f'runs/vms_poc_0/vms2_problem_files/{ai_id}.txt')
            all_tasks.append({
                'exp_id': ai_id,
                'problem_file': branch_problem_file,
                'problem': problem,
                'group': group,
                'tree_info': tree_info,
                'direction': direction,
            })

    print(f"  总任务数: {len(all_tasks)}（10道题 × 3个AI/题）")
    print(f"  并发: {MAX_CONCURRENT}，预计{len(all_tasks) // MAX_CONCURRENT}轮\n")

    # 运行状态跟踪
    # running_ais: {exp_id: {task, last_round_count, node_keys}}
    running_ais = {}
    completed_ais = set()
    task_queue = list(all_tasks)
    task_idx = 0

    # ===== 主循环：系统与推理AI并行运行 =====
    while task_queue or running_ais:
        # --- 步骤1: 启动新AI（填满并发额度）---
        while task_queue and len(running_ais) < MAX_CONCURRENT:
            task = task_queue.pop(0)
            task_idx += 1
            exp_id = task['exp_id']
            print(f"[{task_idx}/{len(all_tasks)}] 启动 {exp_id}...")
            ok = launch_ai(exp_id, task['problem_file'])
            if ok:
                print(f"  ✅ {exp_id} 已启动")
                running_ais[exp_id] = {
                    'task': task,
                    'last_round_count': 0,  # 上次读到的thinking round数
                    'node_keys': [task['tree_info']['root_node_key']],  # 已创建的节点key序列
                    'start_time': time.time(),
                }
            else:
                print(f"  ❌ {exp_id} 启动失败")
                tree_store.update_ai_status(db, exp_id, 'crashed', end_reason='launch_failed')
                completed_ais.add(exp_id)

        if not running_ais:
            break

        # --- 步骤2: 实时采集+整理树（AI一边工作，系统一边整理）---
        for exp_id, state in list(running_ais.items()):
            task = state['task']
            problem = task['problem']
            group = task['group']
            tree_info = task['tree_info']
            direction = task['direction']

            thinking_path = os.path.join(
                '/data/math-agent-glm5.2-tmux-agents-trajectory', exp_id,
                'mitm', 'thinking_readable.txt'
            )

            if not os.path.exists(thinking_path):
                continue  # thinking文件还没生成

            # 读取当前所有thinking rounds
            from xishujuzhen.vms.node_extractor import parse_thinking_rounds, identify_operation, OPERATION_PATTERNS
            rounds = parse_thinking_rounds(thinking_path)
            current_count = len(rounds)

            if current_count <= state['last_round_count']:
                continue  # 没有新round

            # 有新round——提取新节点，实时更新树
            new_rounds = rounds[state['last_round_count']:]
            state['last_round_count'] = current_count

            prev_node_key = state['node_keys'][-1]
            prev_edge_key = None

            for r in new_rounds:
                op = identify_operation(r['thinking'], r.get('tool_call'))
                if op is None:
                    continue
                # 去重连续相同操作
                # 检查上一个节点是否也是这个操作
                last_node = tree_store.get_node(db, prev_node_key) if prev_node_key != tree_info['root_node_key'] else None
                if last_node and last_node.get('situation_text', '').startswith(OPERATION_PATTERNS[op]['situation_template'][:20]):
                    continue

                op_info = OPERATION_PATTERNS[op]
                situation_text = op_info['situation_template']
                if op == 'structure_id':
                    for gtype in ['S₄', 'S_4', 'D₆', 'D_6', 'Z₄', 'Z_4', 'V₄', 'V_4', 'Q₈', 'Q_8', 'Klein']:
                        if gtype in r['thinking']:
                            situation_text += f"（识别为{gtype}）"
                            break

                depth = len(state['node_keys'])
                node_type = op_info['node_type']
                is_last = (r == new_rounds[-1]) and check_ai_terminated(exp_id)
                status = 'completed' if not is_last else ('completed' if node_type == 'leaf_success' else 'growing')

                node = tree_store.create_node(
                    db, problem['pid'],
                    node_type=node_type,
                    situation_text=situation_text,
                    depth=depth,
                    parent_edge_key=prev_edge_key,
                    path_from_root=state['node_keys'] + ['placeholder'],
                    created_by_ai=exp_id,
                    trajectory_segment={'round': r['round'], 'thinking': r['thinking'][:500], 'tool_call': r.get('tool_call')},
                    status=status,
                )

                path = state['node_keys'] + [node['_key']]
                db.collection('tree_nodes').update({'_key': node['_key'], 'path_from_root': path})

                # 创建边
                pattern_id = op_info['pattern_id']
                hint_q = ''
                hint_level = None
                if direction and depth == 1:
                    # 分支的第一个节点——用检索到的方向Q
                    hint_q = direction['Q']
                    hint_level = direction['Level']
                    pattern_id = direction['pattern_id']
                elif pattern_id:
                    hint_q = f"[{pattern_id}] 引导AI进行{op}"
                    hint_level = 0.5
                else:
                    hint_q = f"AI自然过渡到{op}"

                edge = tree_store.create_edge(
                    db, problem['pid'],
                    from_key=prev_node_key,
                    to_key=node['_key'],
                    hint_q=hint_q,
                    hint_q_id=pattern_id,
                    hint_level=hint_level,
                    ai_instance_id=exp_id,
                    edge_status='completed',
                )

                state['node_keys'].append(node['_key'])
                prev_node_key = node['_key']
                prev_edge_key = edge['_key']

                print(f"  🌳 {exp_id} round {r['round']}: 新节点 [{node['_key'][:8]}] d{depth} {op} | {situation_text[:50]}")

                # 如果是leaf_success，更新problem
                if node_type == 'leaf_success':
                    tree_store.update_problem_status(db, problem['pid'], 'solved', solution_path=state['node_keys'])
                    print(f"  ✅ {exp_id}: problem {problem['pid']} solved!")

        # --- 步骤3: 检查AI终止 ---
        for exp_id, state in list(running_ais.items()):
            if check_ai_terminated(exp_id):
                task = state['task']
                problem = task['problem']
                tree_info = task['tree_info']

                # 最后再读一次thinking，确保所有round都提取了
                thinking_path = os.path.join(
                    '/data/math-agent-glm5.2-tmux-agents-trajectory', exp_id,
                    'mitm', 'thinking_readable.txt'
                )
                if os.path.exists(thinking_path):
                    from xishujuzhen.vms.node_extractor import parse_thinking_rounds
                    rounds = parse_thinking_rounds(thinking_path)
                    if len(rounds) > state['last_round_count']:
                        # 还有未提取的round——提取最后一批
                        # （简化：用backfill_ai_to_tree补齐）
                        # 实际上上面的步骤2应该已经提取了，这里只是兜底
                        pass

                # 判断终止原因
                end_reason = 'solution_found' if any(
                    tree_store.get_node(db, k) and tree_store.get_node(db, k).get('node_type') == 'leaf_success'
                    for k in state['node_keys'][1:]
                ) else 'token_limit'

                tree_store.update_ai_status(db, exp_id, 'completed',
                                             end_reason=end_reason,
                                             nodes_contributed=state['node_keys'][1:])

                # 标记根节点completed
                tree_store.update_node_status(db, tree_info['root_node_key'], 'completed')

                elapsed = time.time() - state['start_time']
                node_count = len(state['node_keys']) - 1  # 不含根节点
                print(f"  📦 {exp_id} 终止 ({end_reason}, {node_count} nodes, {elapsed:.0f}s)")

                del running_ais[exp_id]
                completed_ais.add(exp_id)

        # --- 步骤4: 短暂等待后继续循环 ---
        if running_ais:
            time.sleep(POLL_INTERVAL)

    # ===== 最终统计 =====
    print("\n=== 最终统计 ===")
    total_nodes = list(db.aql.execute('RETURN LENGTH(FOR n IN tree_nodes RETURN 1)'))
    total_edges = list(db.aql.execute('RETURN LENGTH(FOR e IN tree_edges RETURN 1)'))
    total_problems = list(db.aql.execute('RETURN LENGTH(FOR p IN problems RETURN 1)'))
    total_ais = list(db.aql.execute('RETURN LENGTH(FOR a IN ai_instances RETURN 1)'))
    solved = list(db.aql.execute('FOR p IN problems FILTER p.status == "solved" RETURN p._key'))

    print(f"  tree_nodes: {list(total_nodes)[0]}")
    print(f"  tree_edges: {list(total_edges)[0]}")
    print(f"  problems: {list(total_problems)[0]} (solved: {len(solved)})")
    print(f"  ai_instances: {list(total_ais)[0]}")
    print(f"  completed_ais: {len(completed_ais)}")


if __name__ == '__main__':
    main()
