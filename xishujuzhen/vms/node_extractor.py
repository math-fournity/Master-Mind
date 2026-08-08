#!/usr/bin/env python3
"""
node_extractor.py —— 从trajectory提取树节点

从推理AI的thinking数据中提取树节点。
每个thinking round对应一个节点——AI在这个round中做了什么操作、处于什么数学处境。

简化版（POC-VMS阶段）：
- 不要求六元组完美——先用situation_text描述处境
- 从thinking内容识别AI的思维操作（用Pattern关键词匹配）
- 从tool_calls识别AI用了什么工具
- 节点之间的边 = AI从一个思维操作转到下一个思维操作

后续升级：
- 用DevinCliParserProvider提取六元组
- 用更复杂的NLP提取situation
"""

import json
import os
import re
from typing import Optional


# ============================================================
# Thinking解析
# ============================================================

def parse_thinking_rounds(thinking_path: str) -> list[dict]:
    """解析thinking_readable.txt，提取每个round。"""
    with open(thinking_path, 'r', encoding='utf-8') as f:
        content = f.read()

    rounds = []
    # 格式：[timestamp] === Thinking Round N START ===\n<thinking>\n--- [Tool Call: xxx] ---\n\n===...END ===
    # 或：[timestamp] === Thinking Round N START ===\n<thinking>\n\n===...END === (无tool call)
    pattern = r'Thinking Round (\d+) START ===\n(.*?)(?:\n===.*?Thinking Round \1 END ===)'
    matches = re.findall(pattern, content, re.DOTALL)

    for round_num, thinking_text in matches:
        thinking_text = thinking_text.strip()
        # 去掉开头的=分隔线
        thinking_text = re.sub(r'^=+\n', '', thinking_text).strip()
        if not thinking_text:
            continue

        # 检查thinking_text中是否有tool call标记
        tool_call = None
        tc_match = re.search(r'--- \[Tool Call: (\w+)\]', thinking_text)
        if tc_match:
            tool_call = tc_match.group(1)
            # 去掉tool call标记
            thinking_text = re.sub(r'\n--- \[Tool Call:.*', '', thinking_text).strip()

        rounds.append({
            'round': int(round_num),
            'thinking': thinking_text,
            'tool_call': tool_call,
        })

    return rounds


# ============================================================
# 思维操作识别
# ============================================================

# 思维操作→Pattern ID映射
OPERATION_PATTERNS = {
    'read_problem': {
        'keywords': ['read', 'problem', '读取', '题目'],
        'pattern_id': None,  # 读题不是Pattern，是起点
        'node_type': 'root',
        'situation_template': 'AI读取了题目，准备开始解题',
    },
    'element_order': {
        'keywords': ['order', '阶', 'power', '幂', 'a²', 'a^2', 'generate', '生成元'],
        'pattern_id': 'VG-element-order-computation',
        'node_type': 'internal',
        'situation_template': 'AI在计算元素的阶',
    },
    'lagrange': {
        'keywords': ['Lagrange', 'divide', '整除', 'factor', '因子', 'subgroup order'],
        'pattern_id': 'VG-lagrange-theorem-application',
        'node_type': 'internal',
        'situation_template': 'AI在用Lagrange定理约束子群阶',
    },
    'structure_id': {
        'keywords': ['isomorphic', '同构', 'S_4', 'S₄', 'D_n', 'D₆', 'Z_n', 'Z₄', 'V_4', 'V₄', 'Klein', 'quaternion', 'Q_8', 'Q₈', 'structure', '结构'],
        'pattern_id': 'VG-group-structure-identification',
        'node_type': 'internal',
        'situation_template': 'AI在识别群的结构（同构类型）',
    },
    'cyclic_check': {
        'keywords': ['cyclic', '循环', 'generator', '生成元', 'Z_n'],
        'pattern_id': 'VG-cyclic-group-identification',
        'node_type': 'internal',
        'situation_template': 'AI在判断群是否是循环群',
    },
    'conjugacy': {
        'keywords': ['conjugacy', '共轭', 'conjugate', 'gag', 'class', '类'],
        'pattern_id': 'VG-conjugacy-class-computation',
        'node_type': 'internal',
        'situation_template': 'AI在计算共轭类',
    },
    'center': {
        'keywords': ['center', '中心', 'commute', '可交换', 'abelian', '交换', 'Z(G)'],
        'pattern_id': 'VG-center-computation',
        'node_type': 'internal',
        'situation_template': 'AI在计算群的中心',
    },
    'normal_subgroup': {
        'keywords': ['normal', '正规', 'invariant', '不变', 'gHg', 'conjugation'],
        'pattern_id': 'VG-normal-subgroup-determination',
        'node_type': 'internal',
        'situation_template': 'AI在判定正规子群',
    },
    'python_verify': {
        'keywords': ['python', 'verify', '验证', 'compute', '计算', 'enumerate', '枚举', 'brute'],
        'pattern_id': 'VG-python-verification',
        'node_type': 'internal',
        'situation_template': 'AI在用Python验证计算',
    },
    'write_answer': {
        'keywords': ['证毕', 'QED', 'boxed', '最终答案', '结论', 'final answer'],
        'pattern_id': None,
        'node_type': 'leaf_success',
        'situation_template': 'AI给出了最终答案',
    },
}


def identify_operation(thinking: str, tool_call: str = None) -> Optional[str]:
    """从thinking内容识别AI的思维操作。"""
    thinking_lower = thinking.lower()

    # 最高优先级：write_answer（含"final answer"/"证毕"/"QED"/"present"/"confirms"等）
    write_keywords = ['证毕', 'QED', 'boxed', '最终答案', '结论', 'final answer', 'present the', 'let me present',
                      'write up', 'confirms my analysis', 'the answer is', 'is cyclic', 'is not cyclic',
                      'is a normal', 'is not a normal', 'the subgroups are', 'the center is',
                      'the conjugacy classes', 'there exists', 'there does not exist']
    if any(kw.lower() in thinking_lower for kw in write_keywords):
        # 但要排除还在分析中的情况
        if not any(kw in thinking_lower for kw in ['let me check', 'let me verify', 'need to', 'should']):
            return 'write_answer'

    # 次高优先级：read_problem（短thinking+read关键词）
    if any(kw.lower() in thinking_lower for kw in ['read', '读取', 'problem.txt', '题目']):
        if len(thinking) < 200:  # 短thinking+read关键词=读题
            return 'read_problem'

    # 按优先级检查具体操作
    priority = ['lagrange', 'conjugacy', 'center', 'normal_subgroup',
                'cyclic_check', 'structure_id', 'element_order', 'python_verify']

    for op in priority:
        keywords = OPERATION_PATTERNS[op]['keywords']
        for kw in keywords:
            if kw.lower() in thinking_lower:
                return op

    # 如果有tool_call=exec，且thinking中有计算相关词
    if tool_call == 'exec':
        return 'python_verify'

    return None


# ============================================================
# 节点提取
# ============================================================

def extract_nodes_from_trajectory(thinking_path: str, problem: dict, group: dict) -> list[dict]:
    """
    从一道题的trajectory提取树节点序列。

    返回：节点列表，每个节点含：
    - operation: 思维操作类型
    - situation_text: 处境描述
    - node_type: root/internal/leaf_success
    - pattern_id: 对应的Pattern ID（如有）
    - thinking_snippet: thinking片段（前200字）
    - trajectory_segment: 完整thinking+tool_call
    """
    if not os.path.exists(thinking_path):
        return []

    rounds = parse_thinking_rounds(thinking_path)
    if not rounds:
        return []

    nodes = []
    seen_operations = set()

    for i, r in enumerate(rounds):
        op = identify_operation(r['thinking'], r.get('tool_call'))
        if op is None:
            # 无法识别的round，跳过
            continue

        # 去重连续相同操作
        if nodes and nodes[-1]['operation'] == op:
            # 合并到上一个节点
            nodes[-1]['thinking_snippet'] += '\n---\n' + r['thinking'][:200]
            continue

        op_info = OPERATION_PATTERNS[op]
        situation_text = op_info['situation_template']

        # 如果是python_verify，补充具体信息
        if op == 'python_verify':
            situation_text += f"（群阶={group['order']}）"

        # 如果是structure_id，补充识别结果
        if op == 'structure_id':
            # 从thinking中提取识别出的群类型
            for gtype in ['S₄', 'S_4', 'D₆', 'D_6', 'Z₄', 'Z_4', 'V₄', 'V_4', 'Q₈', 'Q_8', 'Klein']:
                if gtype in r['thinking']:
                    situation_text += f"（识别为{gtype}）"
                    break

        node = {
            'operation': op,
            'situation_text': situation_text,
            'node_type': op_info['node_type'],
            'pattern_id': op_info['pattern_id'],
            'thinking_snippet': r['thinking'][:200],
            'trajectory_segment': {
                'round': r['round'],
                'thinking': r['thinking'],
                'tool_call': r.get('tool_call'),
            },
            'depth': len(nodes),  # 线性链中depth=序号
        }
        nodes.append(node)

    return nodes


# ============================================================
# 主函数：从实验回填树
# ============================================================

def backfill_tree_from_experiment(db, exp_id: str, problem: dict, group: dict,
                                   thinking_path: str, ai_id: str = None):
    """
    从一个实验的trajectory回填一棵树到ArangoDB。

    对于baseline实验（裸跑），这棵树是一条线性链。
    对于有检索介入的实验，树会有分叉。
    """
    from xishujuzhen.vms import tree_store

    problem_id = problem['pid']

    # 1. 创建problem（如果不存在）
    prob_doc = tree_store.get_problem(db, problem_id)
    if not prob_doc:
        prob_doc = tree_store.create_problem(db, problem_id, problem['full_problem'],
                                             metadata={
                                                 'group_type': group['group_type'],
                                                 'group_order': group['order'],
                                                 'problem_type': problem['problem_type'],
                                                 'challenge_template': problem.get('challenge_template', ''),
                                                 'challenge_type': problem.get('challenge_type', ''),
                                             })

    # 2. 提取节点
    nodes = extract_nodes_from_trajectory(thinking_path, problem, group)
    if not nodes:
        print(f"  {exp_id}: no nodes extracted")
        return None

    # 3. 注册AI实例
    ai_id = ai_id or exp_id
    root_node = None

    # 4. 创建节点和边（线性链）
    prev_node_key = None
    prev_edge_key = None
    node_keys = []

    for i, node_data in enumerate(nodes):
        # 创建节点
        if i == 0:
            # 根节点
            node = tree_store.create_node(
                db, problem_id,
                node_type='root',
                situation_text=node_data['situation_text'],
                depth=0,
                created_by_ai=ai_id,
                trajectory_segment=node_data['trajectory_segment'],
                status='completed' if i < len(nodes) - 1 else 'growing',
            )
            # 回填root_node_key到problem
            db.collection('problems').update({
                '_key': problem_id,
                'root_node_key': node['_key']
            })
        else:
            # 内部节点或叶节点
            node_type = node_data['node_type']
            status = 'completed' if i < len(nodes) - 1 else ('completed' if node_type == 'leaf_success' else 'growing')
            node = tree_store.create_node(
                db, problem_id,
                node_type=node_type,
                situation_text=node_data['situation_text'],
                depth=i,
                parent_edge_key=prev_edge_key,
                path_from_root=node_keys + [None],  # 先占位，创建后更新
                created_by_ai=ai_id,
                trajectory_segment=node_data['trajectory_segment'],
                status=status,
            )
            # 更新path_from_root
            path = node_keys + [node['_key']]
            db.collection('tree_nodes').update({
                '_key': node['_key'],
                'path_from_root': path
            })

            # 创建边（从上一个节点到本节点）
            pattern_id = node_data.get('pattern_id')
            hint_q = ''
            hint_level = None
            if pattern_id:
                # 从Pattern库找Q
                hint_q = f"[{pattern_id}] 引导AI进行{node_data['operation']}"
                hint_level = 0.5  # 默认值，后续从Pattern库查
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
            prev_edge_key = edge['_key']

        node_keys.append(node['_key'])
        prev_node_key = node['_key']

    # 5. 注册AI实例
    tree_store.register_ai_instance(
        db, ai_id, problem_id,
        entry_node_key=node_keys[0],
        tmux_session=f'harness-{exp_id}',
        trajectory_dir=f'/data/math-agent-glm5.2-tmux-agents-trajectory/{exp_id}',
    )

    # 6. 更新AI状态为completed
    tree_store.update_ai_status(
        db, ai_id, 'completed',
        end_reason='solution_found' if nodes[-1]['operation'] == 'write_answer' else 'token_limit',
        nodes_contributed=node_keys,
    )

    # 7. 如果最后一个节点是leaf_success，更新problem状态
    if nodes[-1]['node_type'] == 'leaf_success':
        tree_store.update_problem_status(db, problem_id, 'solved', solution_path=node_keys)

    return node_keys


# ============================================================
# 批量回填
# ============================================================

def backfill_all_experiments():
    """回填所有POC-VMS-0/1的实验到ArangoDB。"""
    from xishujuzhen.vms import tree_store

    REPO_DIR = '~/master-mind-glm5.2-worktree'
    TRAJ_BASE = '/data/math-agent-glm5.2-tmux-agents-trajectory'

    db = tree_store.get_db()
    tree_store.ensure_collections(db)

    # 加载虚拟群和题目
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/virtual_groups.json')) as f:
        groups = json.load(f)
    group_by_gid = {g['gid']: g for g in groups}

    # 加载所有题目
    all_problems = []
    for fname in ['baseline_10_problems.json', 'hard_baseline_10.json']:
        path = os.path.join(REPO_DIR, 'runs/vms_poc_0', fname)
        with open(path) as f:
            all_problems.extend(json.load(f))

    print(f"=== 回填 {len(all_problems)} 个实验到ArangoDB ===\n")

    for i, problem in enumerate(all_problems):
        if i < 10:
            exp_id = f'vms-poc0-baseline-{i+1:02d}'
        else:
            exp_id = f'vms-poc0-hard-{i-9:02d}'

        group = group_by_gid.get(problem['group_gid'])
        if not group:
            continue

        thinking_path = os.path.join(TRAJ_BASE, exp_id, 'mitm', 'thinking_readable.txt')
        if not os.path.exists(thinking_path):
            print(f"  {exp_id}: no thinking data, skip")
            continue

        node_keys = backfill_tree_from_experiment(db, exp_id, problem, group, thinking_path)
        if node_keys:
            print(f"  {exp_id} ({problem['pid']}): {len(node_keys)} nodes")

    # 统计
    print(f"\n=== 回填完成 ===")
    total_nodes = db.aql.execute("RETURN LENGTH(FOR n IN tree_nodes RETURN 1)")
    total_edges = db.aql.execute("RETURN LENGTH(FOR e IN tree_edges RETURN 1)")
    total_problems = db.aql.execute("RETURN LENGTH(FOR p IN problems RETURN 1)")
    total_ais = db.aql.execute("RETURN LENGTH(FOR a IN ai_instances RETURN 1)")
    print(f"  tree_nodes: {list(total_nodes)[0]}")
    print(f"  tree_edges: {list(total_edges)[0]}")
    print(f"  problems: {list(total_problems)[0]}")
    print(f"  ai_instances: {list(total_ais)[0]}")


if __name__ == '__main__':
    backfill_all_experiments()
