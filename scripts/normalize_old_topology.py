#!/usr/bin/env python3
"""
归一化老profile的非标准拓扑值到标准值。
"""
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
profiles = db.collection('problem_profiles')

# 归一化映射
PT_MAP = {
    'trigonometric identity verification': 'characterization',
    'constraint satisfaction with unique solution': 'constraint_satisfaction',
    'system of equations with absolute values': 'constraint_satisfaction',
    'word_problem_with_diophantine_constraint': 'constraint_satisfaction',
    'infinite_sum_evaluation_with_floor': 'characterization',
    'functional_equation_periodicity_proof_and_construction': 'characterization',
    'inequality_proof_with_equality_conditions': 'inequality_proof',
}

AM_MAP = {
    'brute_force_simulation_or_simultaneous_equations': 'enumeration_brute_force',
    'direct_evaluation_or_small_cases_only': 'direct_calculation',
    'constructive_induction': 'case_by_case',
}

GT_MAP = {
    'global_sorting': 'structural_transformation',
    'recurrence_solving_and_number_theoretic_argument': 'knowledge_gap',
    'knowledge_bottleneck_on_floor_identity': 'knowledge_gap',
    'strategic_algebraic_identity': 'structural_transformation',
    'method_selection_and_hidden_structure_recognition': 'method_problem_mismatch',
}

# per-pair也需要归一化
PER_PAIR_PT_MAP = {
    'absolute_value_system': 'constraint_satisfaction',
    'functional_equation_periodicity': 'characterization',
    'infinite_sum_evaluation_with_floor': 'characterization',
    'trigonometric_identity': 'characterization',
    'word_problem_with_diophantine_constraint': 'constraint_satisfaction',
}

PER_PAIR_AM_MAP = {
    'avoidance_argument': 'logical_deduction',
    'brute_force_simulation_or_simultaneous_equations': 'enumeration_brute_force',
    'direct_construction': 'direct_calculation',
    'direct_evaluation_or_small_cases_only': 'direct_calculation',
    'finiteness_argument': 'logical_deduction',
    'isometry_argument': 'structural_transformation',
    'constructive_induction': 'case_by_case',
}

PER_PAIR_GT_MAP = {
    'direct_manipulation': 'method_problem_mismatch',
    'global_sorting': 'structural_transformation',
    'knowledge_bottleneck_on_floor_identity': 'knowledge_gap',
    'method_selection_and_hidden_structure_recognition': 'method_problem_mismatch',
    'recurrence_solving_and_number_theoretic_argument': 'knowledge_gap',
    'strategic_algebraic_identity': 'structural_transformation',
}

# 需要修正的profile keys
target_keys = [
    'compfiles_imo1963p5', 'compfiles_imo1963p6', 'compfiles_imo1966p5',
    'compfiles_imo1967p6', 'compfiles_imo1968p6', 'compfiles_imo1968p5',
    'compfiles_imo1969p6', 'compfiles_imo1971p5'
]

fixed_count = 0
for key in target_keys:
    p = profiles.get(key)
    if not p:
        print(f'  {key}: NOT FOUND')
        continue
    
    changes = []
    
    # profile级
    if p['problem_type'] in PT_MAP:
        old = p['problem_type']
        p['problem_type'] = PT_MAP[old]
        changes.append(f'pt: {old}→{p["problem_type"]}')
    
    tt = p.get('tell_topology', {})
    if tt.get('ai_method_type') in AM_MAP:
        old = tt['ai_method_type']
        tt['ai_method_type'] = AM_MAP[old]
        changes.append(f'am: {old}→{tt["ai_method_type"]}')
    
    if tt.get('gap_type') in GT_MAP:
        old = tt['gap_type']
        tt['gap_type'] = GT_MAP[old]
        changes.append(f'gt: {old}→{tt["gap_type"]}')
    
    # per-pair
    for pair in p.get('tell_hint_pairs', []):
        ptt = pair.get('tell_topology', {})
        if ptt.get('problem_type') in PER_PAIR_PT_MAP:
            old = ptt['problem_type']
            ptt['problem_type'] = PER_PAIR_PT_MAP[old]
            changes.append(f'  pair R{pair.get("qa_round","?")}: pt {old}→{ptt["problem_type"]}')
        if ptt.get('ai_method_type') in PER_PAIR_AM_MAP:
            old = ptt['ai_method_type']
            ptt['ai_method_type'] = PER_PAIR_AM_MAP[old]
            changes.append(f'  pair R{pair.get("qa_round","?")}: am {old}→{ptt["ai_method_type"]}')
        if ptt.get('gap_type') in PER_PAIR_GT_MAP:
            old = ptt['gap_type']
            ptt['gap_type'] = PER_PAIR_GT_MAP[old]
            changes.append(f'  pair R{pair.get("qa_round","?")}: gt {old}→{ptt["gap_type"]}')
    
    # global pairs
    for g in p.get('global_tell_hint_pairs', []):
        gtt = g.get('tell_topology', {})
        if gtt.get('problem_type') in PER_PAIR_PT_MAP:
            gtt['problem_type'] = PER_PAIR_PT_MAP[gtt['problem_type']]
        if gtt.get('ai_method_type') in PER_PAIR_AM_MAP:
            gtt['ai_method_type'] = PER_PAIR_AM_MAP[gtt['ai_method_type']]
        if gtt.get('gap_type') in PER_PAIR_GT_MAP:
            gtt['gap_type'] = PER_PAIR_GT_MAP[gtt['gap_type']]
    
    profiles.update(p)
    fixed_count += 1
    print(f'  {key}: {len(changes)} changes')
    for c in changes:
        print(f'    {c}')

print(f'\n完成，修正了{fixed_count}个profile')
