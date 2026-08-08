#!/usr/bin/env python3
"""
retriever.py —— POC-VMS-2 简化版检索器

从数据基座（patterns集合）中检索与当前节点最相关的Pattern。

检索流程（对应267号§7.4）：
1. 从node的situation提取deterministic字段（task_type/group_order/group_type）
2. 用deterministic字段做粗筛——缩小候选Pattern集
3. 返回候选Pattern列表（每个Pattern的Q字段就是一个方向）

简化版说明：
- 不用RetrievalPipeline/ConstrainedPolicy——直接用deterministic字段做filter
- 不用AI精筛——POC-VMS-2阶段先验证粗筛的准确性
- 后续POC-VMS-3加入AI精筛
"""

import os
import json
from typing import Optional
from arango import ArangoClient


def get_db():
    host = os.environ.get('ARANGO_HOST', 'http://localhost:8529')
    db_name = os.environ.get('ARANGO_DB', 'xishujuzhen_math_glm52')
    user = os.environ.get('ARANGO_USER', 'root')
    password = os.environ.get('ARANGO_PASS', 'REDACTED-DB-PASSWORD')
    client = ArangoClient(hosts=host)
    return client.db(db_name, username=user, password=password)


def load_patterns_to_arango(patterns: list):
    """把基础Pattern模板加载到ArangoDB的patterns集合。

    注意：用base_patterns（8个模板），不用patterns（22个实例）。
    模板的trigger_conditions.deterministic中group_order是条件dict（如{'op': '>', 'value': 8}），
    实例的group_order是具体值（如4）。
    """
    db = get_db()
    existing = {c['name'] for c in db.collections() if not c['name'].startswith('_')}
    if 'patterns' not in existing:
        db.create_collection('patterns')
        print("  created collection: patterns")

    col = db.collection('patterns')
    col.truncate()  # 清空旧数据

    for p in patterns:
        doc = {
            '_key': p['pattern_id'],
            'base_pattern_id': p.get('base_pattern_id', p['pattern_id']),
            'name': p['name'],
            'description': p.get('description', ''),
            'domain': p.get('domain', 'virtual_group_theory'),
            'trigger_conditions': p['trigger_conditions'],
            'Q': p['Q'],
            'Level': p['Level'],
            'non_specificity': p.get('non_specificity', 0.5),
            'situation_type': p.get('situation_type', ''),
            'instance_count': p.get('instance_count', 0),
            'ai_used_count': p.get('ai_used_count', 0),
        }
        col.insert(doc)

    print(f"  loaded {len(patterns)} patterns into ArangoDB")


def retrieve_directions(db, task_type: str, group_order: int, group_type: str) -> list:
    """
    从数据基座检索与当前节点最相关的Pattern（方向Q）。

    检索逻辑（简化版）：
    1. 硬筛：task_type匹配（any匹配所有）
    2. 软筛：group_order条件检查（满足条件加分，不满足不排除）
    3. 返回所有通过硬筛的Pattern，按相关性排序

    返回：方向Q列表，每个Q是一个dict含pattern_id/Q/Level/non_specificity
    """
    aql = """
    FOR p IN patterns
      LET det = p.trigger_conditions.deterministic
      // 硬筛：task_type必须匹配
      FILTER det.task_type == 'any' OR det.task_type == @task_type

      // 软筛：group_order条件匹配度
      LET go_cond = det.group_order
      LET go_match = go_cond == null
        OR (IS_OBJECT(go_cond) AND go_cond.op == '>' AND @group_order > go_cond.value)
        OR (IS_OBJECT(go_cond) AND go_cond.op == 'in' AND @group_order IN go_cond.value)
        OR (IS_NUMBER(go_cond) AND @group_order == go_cond)

      // 软筛：group_type匹配度
      LET gt_cond = det.group_type
      LET gt_match = gt_cond == null OR gt_cond == @group_type

      // 综合评分：软筛匹配数 + Level权重
      LET score = (go_match ? 1 : 0) + (gt_match ? 1 : 0) + p.Level * 0.5

      SORT score DESC, p.Level DESC
      RETURN {
        pattern_id: p._key,
        base_pattern_id: p.base_pattern_id,
        name: p.name,
        Q: p.Q,
        Level: p.Level,
        non_specificity: p.non_specificity,
        situation_type: p.situation_type,
        trigger_deterministic: det,
        score: score,
        go_match: go_match,
        gt_match: gt_match
      }
    """

    cursor = db.aql.execute(aql, bind_vars={
        'task_type': task_type,
        'group_order': group_order,
        'group_type': group_type,
    })

    return list(cursor)


def retrieve_for_node(db, node, problem_metadata: dict) -> list:
    """
    为一个树节点检索方向。

    node: tree_nodes文档
    problem_metadata: 题目元数据（含problem_type/group_order/group_type）
    """
    task_type = problem_metadata.get('problem_type', 'unknown')
    group_order = problem_metadata.get('group_order', 0)
    group_type = problem_metadata.get('group_type', 'unknown')

    directions = retrieve_directions(db, task_type, group_order, group_type)

    return directions


# ============================================================
# 评估检索准确性
# ============================================================

def evaluate_retrieval_accuracy(db, test_problems: list, group_by_gid: dict):
    """
    评估检索准确性——对每道测试题，检查检索到的Pattern是否包含正确的操作。

    正确操作定义：题目类型对应的Pattern应该被检索到。
    例如，subgroup_enumeration题应该检索到VG-lagrange-theorem-application。
    """
    results = []

    # 题目类型→期望的base_pattern_id映射
    expected_patterns = {
        'subgroup_enumeration': ['VG-lagrange-theorem-application', 'VG-element-order-computation',
                                  'VG-python-verification', 'VG-group-structure-identification'],
        'normal_subgroup_determination': ['VG-normal-subgroup-determination', 'VG-element-order-computation',
                                          'VG-python-verification', 'VG-group-structure-identification'],
        'cyclic_determination': ['VG-cyclic-group-identification', 'VG-element-order-computation',
                                  'VG-python-verification', 'VG-group-structure-identification'],
        'conjugacy_class_computation': ['VG-conjugacy-class-computation', 'VG-element-order-computation',
                                         'VG-python-verification', 'VG-group-structure-identification'],
        'center_computation': ['VG-center-computation', 'VG-element-order-computation',
                               'VG-python-verification', 'VG-group-structure-identification'],
        'homomorphism_construction': ['VG-group-structure-identification', 'VG-element-order-computation',
                                       'VG-python-verification'],
    }

    for i, problem in enumerate(test_problems):
        group = group_by_gid[problem['group_gid']]
        task_type = problem['problem_type']
        group_order = group['order']
        group_type = group['group_type']

        # 检索
        directions = retrieve_directions(db, task_type, group_order, group_type)

        # 检查是否包含期望的Pattern
        expected = expected_patterns.get(task_type, [])
        retrieved_base_ids = [d['base_pattern_id'] for d in directions]
        hits = [bid for bid in expected if bid in retrieved_base_ids]
        misses = [bid for bid in expected if bid not in retrieved_base_ids]

        # 检查是否有不相关的Pattern（false positive）
        all_base_ids = set(d['base_pattern_id'] for d in directions)
        irrelevant = all_base_ids - set(expected)

        result = {
            'pid': problem['pid'],
            'task_type': task_type,
            'group_order': group_order,
            'group_type': group_type,
            'retrieved_count': len(directions),
            'retrieved_base_ids': retrieved_base_ids,
            'expected_hits': hits,
            'expected_misses': misses,
            'irrelevant': list(irrelevant),
            'precision': len(hits) / max(len(directions), 1),
            'recall': len(hits) / max(len(expected), 1),
        }
        results.append(result)

        hit_str = ','.join(h.split('-')[1] if '-' in h else h for h in hits)
        miss_str = ','.join(m.split('-')[1] if '-' in m else m for m in misses)
        print(f"  {problem['pid']}: retrieved={len(directions)} hits={len(hits)}/{len(expected)} "
              f"precision={result['precision']:.2f} recall={result['recall']:.2f}")

    # 总体统计
    avg_precision = sum(r['precision'] for r in results) / len(results)
    avg_recall = sum(r['recall'] for r in results) / len(results)
    avg_retrieved = sum(r['retrieved_count'] for r in results) / len(results)

    print(f"\n=== 检索准确性 ===")
    print(f"  平均precision: {avg_precision:.2f}")
    print(f"  平均recall: {avg_recall:.2f}")
    print(f"  平均检索数: {avg_retrieved:.1f}")

    return results


# ============================================================
# 主函数
# ============================================================

def main():
    print("=== POC-VMS-2: 检索器 ===\n")

    REPO_DIR = '~/master-mind-glm5.2-worktree'

    # 1. 加载基础Pattern模板到ArangoDB（用原始模板条件，不是实例化的值）
    print("1. 加载基础Pattern模板到ArangoDB")
    from xishujuzhen.vms.pattern_extractor import PATTERN_TEMPLATES
    # 从模板构造base_patterns——保留原始条件dict
    base_patterns = []
    for t in PATTERN_TEMPLATES:
        bp = {
            'pattern_id': t['pattern_id'],
            'name': t['name'],
            'description': t['description'],
            'domain': 'virtual_group_theory',
            'trigger_conditions': {
                'deterministic': t['trigger_deterministic'],
                'non_deterministic': t['trigger_nondeterministic'],
            },
            'Q': t['Q'],
            'Level': t['Level'],
            'non_specificity': t['non_specificity'],
            'situation_type': t['situation_type'],
            'instance_count': 0,
            'ai_used_count': 0,
        }
        base_patterns.append(bp)

    # 从base_patterns.json补充统计信息
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/base_patterns.json')) as f:
        saved_bps = json.load(f)
    for bp in base_patterns:
        for sbp in saved_bps:
            if sbp['pattern_id'] == bp['pattern_id']:
                bp['instance_count'] = sbp.get('instance_count', 0)
                bp['ai_used_count'] = sbp.get('ai_used_count', 0)
                break

    load_patterns_to_arango(base_patterns)

    # 2. 加载测试题
    print("\n2. 加载测试题")
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/vms2_test_10.json')) as f:
        test_problems = json.load(f)
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/virtual_groups.json')) as f:
        groups = json.load(f)
    group_by_gid = {g['gid']: g for g in groups}

    # 3. 评估检索准确性
    print("\n3. 评估检索准确性")
    db = get_db()
    results = evaluate_retrieval_accuracy(db, test_problems, group_by_gid)

    # 4. 保存结果
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms2_retrieval_results.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n结果已保存到 {output_path}")

    # 5. 展示一个检索示例
    print("\n4. 检索示例")
    sample = test_problems[0]
    sample_group = group_by_gid[sample['group_gid']]
    directions = retrieve_directions(db, sample['problem_type'], sample_group['order'], sample_group['group_type'])
    print(f"  题目: {sample['pid']} ({sample['problem_type']}, {sample_group['group_type']} order={sample_group['order']})")
    print(f"  检索到 {len(directions)} 个方向:")
    for d in directions:
        print(f"    [{d['base_pattern_id']}] Level={d['Level']} | {d['Q'][:80]}")


if __name__ == '__main__':
    main()
