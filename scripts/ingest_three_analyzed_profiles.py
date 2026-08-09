#!/usr/bin/env python3
"""将3道Tier 1题目的分析结果入库problem_profiles集合，验证v2 Schema。"""
from arango import ArangoClient
from datetime import datetime, timezone

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
profiles = db.collection('problem_profiles')
progress = db.collection('problem_extraction_progress')

now = datetime.now(timezone.utc).isoformat()

# === 题1: IMO 1963 P5 ===
p1 = {
    '_key': 'compfiles_imo1963p5',
    'source_id': 'Imo1963P5',
    'source_dataset': 'compfiles',
    'schema_version': 2,
    'problem_text': 'Prove that cos(π/7) - cos(2π/7) + cos(3π/7) = 1/2.',
    'solution_text': 'Multiply both sides by 2sin(π/7). Using product-to-sum: 2sin(x)cos(y)=sin(x+y)-sin(y-x). The sum telescopes: sin(2π/7)-sin(0)+sin(6π/7)-sin(4π/7)+sin(4π/7)-sin(2π/7) = sin(6π/7) = sin(π/7). So 2sin(π/7)·LHS = sin(π/7), hence LHS = 1/2.',
    'solution_summary': '乘以辅助因子2sin(π/7)，用积化和差公式将余弦求和转化为正弦望远镜求和，中间项全部消去。',
    'domain': 'algebra',
    'subfield': 'trigonometric identities',
    'answer_type': 'Proof',
    'answer': 'QED (cos(π/7) - cos(2π/7) + cos(3π/7) = 1/2)',
    'problem_type': 'trigonometric identity verification',
    'solution_method_type': 'telescoping sum via auxiliary factor',
    'structure_features': '三角恒等式，角度π/7的倍数，符号模式+,-,+',
    'key_objects': ['cos(π/7)', 'cos(2π/7)', 'cos(3π/7)', '2sin(π/7)'],
    'thinking_patterns': ['auxiliary factor', 'telescoping', 'product-to-sum transformation'],
    'primary_pattern': 'auxiliary factor → telescoping',
    'knowledge_required': ['product-to-sum formula', 'sin(pi-x)=sin(x)'],
    'key_insight': '乘以2sin(π/7)把余弦求和变成正弦望远镜——中间项全消',
    'translation_from': 'direct calculation of cos values',
    'translation_to': 'structural transformation via auxiliary factor 2sin(π/7)',
    'translation_type': '计算→结构变换',
    'tell_topology': {'problem_type': 'trigonometric_identity', 'ai_method_type': 'direct_calculation', 'gap_type': 'structural_transformation'},
    'tell_small_concepts': ['cos', 'sin', 'pi/7', 'telescoping', 'product-to-sum', 'auxiliary factor'],
    'expected_ai_method': '直接计算cos(π/7)等值',
    'correct_method': '乘以2sin(π/7)做望远镜求和',
    'tell_hint_pairs': [
        {'qa_round': 1, 'tell': 'AI面对三角恒等式，尚未识别角度结构', 'hint': '描述题目结构——角度π/7的倍数，符号模式+,-,+', 'hint_level': 1.0, 'situation_type': '纯元认知观察', 'is_knowledge_bottleneck': False},
        {'qa_round': 2, 'tell': 'AI尚未列出可用方法', 'hint': '列出所有可能方向：直接计算、复数单位根、积化和差、Chebyshev', 'hint_level': 1.0, 'situation_type': '自由列举', 'is_knowledge_bottleneck': False},
        {'qa_round': 3, 'tell': 'AI试图直接计算cos(π/7)——走错路了', 'hint': '试着用φ的定义直接算——π/7不是标准角度，直接计算困难', 'hint_level': 0.9, 'situation_type': '小尝试', 'is_knowledge_bottleneck': False},
        {'qa_round': 4, 'tell': 'AI在直接计算上碰壁，需要结构变换方向', 'hint': '试试乘以2sin(π/7)，用积化和差公式', 'hint_level': 0.7, 'situation_type': '思维操作引导', 'is_knowledge_bottleneck': False},
        {'qa_round': 5, 'tell': 'AI展开了积化和差但还没看到望远镜', 'hint': '注意到了什么？中间项全部消去——望远镜求和', 'hint_level': 1.0, 'situation_type': '推进', 'is_knowledge_bottleneck': False},
        {'qa_round': 6, 'tell': 'AI看到望远镜结果sin(6π/7)=sin(π/7)但还没收尾', 'hint': '所以原式等于？2sin(π/7)·原式=sin(π/7)，原式=1/2', 'hint_level': 0.6, 'situation_type': '能量传递引导', 'is_knowledge_bottleneck': False},
    ],
    'global_tell_hint_pairs': [
        {'scope_type': 'path_feature', 'scope': 'translation_type', 'observation_point': None,
         'tell': '整条路径从"直接计算cos值"转向"乘辅助因子做结构变换"',
         'hint': '不要计算三角函数的值，而是乘以辅助因子变换表达式结构',
         'hint_level': 0.8, 'generalizability': 'high——"计算→结构变换"适用于任何涉及特殊角度的三角恒等式',
         'why_not_visible_locally': None},
        {'scope_type': 'implicit', 'scope': 'implicit_structure_vs_value', 'observation_point': 'Q3',
         'tell': 'AI在试图计算三角函数的值，但解法要求的是变换表达式的结构——AI不知道"不要算值，要变换结构"',
         'hint': '不要计算三角函数的值，而是乘以辅助因子2sin(π/7)把求和转化为望远镜',
         'hint_level': 0.9, 'generalizability': 'high——"有值要算但应该变换结构"适用于任何计算vs变换的分叉',
         'why_not_visible_locally': '在Q3时AI还在尝试直接计算（tell不可见），在Q5时AI已经在望远镜里了（tell已过时），只有在Q3看前后才能读出'},
    ],
    'bare_ai_expected': 'fail',
    'bare_ai_error_prediction': '会试图直接计算cos(π/7)的值，或用计算器近似验证，而不是想到乘辅助因子做结构变换',
    'suitable_for_poc': ['VMS-tell-detection', 'VMS-translation-hint'],
    'discriminates_levels': True,
    'qa_sequence': {
        'rounds': [
            {'round': 1, 'question': '描述题目结构', 'expected_answer': '三角恒等式，角度π/7, 2π/7, 3π/7，符号模式+,-,+', 'situation_type': '纯元认知观察', 'level': 1.0},
            {'round': 2, 'question': '列出所有可能方向', 'expected_answer': '直接计算、复数单位根、积化和差、Chebyshev多项式', 'situation_type': '自由列举', 'level': 1.0},
            {'round': 3, 'question': '试着直接算', 'expected_answer': 'π/7不是标准角度，直接计算困难', 'situation_type': '小尝试', 'level': 0.9},
            {'round': 4, 'question': '试试乘以2sin(π/7)，用积化和差公式', 'expected_answer': '2sin(x)cos(y)=sin(x+y)-sin(y-x)，展开后得到正弦项', 'situation_type': '思维操作引导', 'level': 0.7},
            {'round': 5, 'question': '注意到了什么？', 'expected_answer': '望远镜求和！中间项全部消去，只剩sin(6π/7)=sin(π/7)', 'situation_type': '推进', 'level': 1.0},
            {'round': 6, 'question': '所以原式等于？', 'expected_answer': '2sin(π/7)·原式=sin(π/7)，所以原式=1/2', 'situation_type': '能量传递引导', 'level': 0.6},
        ],
        'stats': {
            'total_rounds': 6,
            'metacognitive_rounds': 4,
            'knowledge_rounds': 2,
            'level_sum': 5.2,
            'knowledge_bottleneck': None,
            'thinking_bottleneck': 'Q4——从直接计算转向结构变换',
        }
    },
    'analysis_metadata': {
        'analyzed_by': 'master',
        'analyzed_at': now,
        'analysis_duration': '10min',
        'notes': 'Lean解答中用rw和linarith逐步化简，本质就是乘2sin(π/7)做望远镜',
    }
}

# === 题2: IMO 1963 P6 ===
p2 = {
    '_key': 'compfiles_imo1963p6',
    'source_id': 'Imo1963P6',
    'source_dataset': 'compfiles',
    'schema_version': 2,
    'problem_text': 'Five students A,B,C,D,E were placed 1 to 5 in a contest with no ties. One prediction was A,B,C,D,E. But no student finished in the position predicted, and no two students predicted to finish consecutively did so. Another prediction was D,A,E,C,B. Exactly two students finished in the places predicted, and two disjoint pairs of students predicted to finish consecutively did so. Determine the outcome.',
    'solution_text': 'There are only 5!=120 possible outcomes. Check all 120 permutations against all constraints: (1) no student in predicted position from first prediction, (2) no consecutive pair from first prediction, (3) exactly 2 students in predicted positions from second prediction, (4) two disjoint consecutive pairs from second prediction. The unique solution is: A=3rd, B=5th, C=4th, D=2nd, E=1st (i.e., permutation [2,4,3,1,0]).',
    'solution_summary': '穷举120种排列，逐一检查所有约束条件，唯一解为E,D,A,C,B（位置1-5）。',
    'domain': 'combinatorics',
    'subfield': 'constraint satisfaction',
    'answer_type': 'Numerical',
    'answer': 'A=3rd, B=5th, C=4th, D=2nd, E=1st',
    'problem_type': 'constraint satisfaction with unique solution',
    'solution_method_type': 'exhaustive enumeration with constraint filtering',
    'structure_features': '5个学生5个名次，两个预测给出4组约束，求唯一排列',
    'key_objects': ['permutation of 5', 'first prediction A,B,C,D,E', 'second prediction D,A,E,C,B'],
    'thinking_patterns': ['exhaustive enumeration', 'constraint filtering', 'search space size estimation'],
    'primary_pattern': 'exhaustive enumeration',
    'knowledge_required': ['permutation', 'derangement condition'],
    'key_insight': '5!=120是可穷举的——直接枚举比逻辑推导更可靠',
    'translation_from': 'logical deduction of constraints',
    'translation_to': 'exhaustive enumeration of 120 permutations',
    'translation_type': '逻辑推导→穷举枚举',
    'tell_topology': {'problem_type': 'constraint_satisfaction', 'ai_method_type': 'logical_deduction', 'gap_type': 'search_space_estimation'},
    'tell_small_concepts': ['permutation', 'prediction', 'consecutive', 'derangement', 'enumeration', 'constraint'],
    'expected_ai_method': '试图用逻辑推理逐步排除可能性',
    'correct_method': '穷举120种排列逐一检查约束',
    'tell_hint_pairs': [
        {'qa_round': 1, 'tell': 'AI面对约束满足问题，尚未识别搜索空间大小', 'hint': '描述题目结构——约束满足问题，5个学生5个名次', 'hint_level': 1.0, 'situation_type': '纯元认知观察', 'is_knowledge_bottleneck': False},
        {'qa_round': 2, 'tell': 'AI尚未评估搜索空间大小', 'hint': '列出所有可能方向：穷举枚举、逻辑推导、约束传播', 'hint_level': 1.0, 'situation_type': '自由列举', 'is_knowledge_bottleneck': False},
        {'qa_round': 3, 'tell': 'AI不知道搜索空间是否可穷举', 'hint': '有多少种可能？5!=120种排列，可以穷举', 'hint_level': 0.9, 'situation_type': '小尝试', 'is_knowledge_bottleneck': False},
        {'qa_round': 4, 'tell': 'AI知道可以穷举但还没系统化', 'hint': '系统地应用所有约束过滤', 'hint_level': 0.7, 'situation_type': '思维操作引导', 'is_knowledge_bottleneck': False},
        {'qa_round': 5, 'tell': 'AI在枚举过滤中', 'hint': '枚举过滤后剩多少？唯一解', 'hint_level': 0.8, 'situation_type': '推进', 'is_knowledge_bottleneck': False},
    ],
    'global_tell_hint_pairs': [
        {'scope_type': 'path_feature', 'scope': 'translation_type', 'observation_point': None,
         'tell': '整条路径从"逻辑推导"转向"穷举枚举"',
         'hint': '评估搜索空间大小——如果可穷举，直接枚举比逻辑推导更可靠',
         'hint_level': 0.8, 'generalizability': 'high——"逻辑推导→穷举枚举"适用于任何小规模约束满足问题',
         'why_not_visible_locally': None},
        {'scope_type': 'implicit', 'scope': 'implicit_search_space', 'observation_point': 'Q2',
         'tell': 'AI列出了多个方向但不知道穷举枚举在这个问题上是最直接的——AI不知道"120种可能性是可穷举的"',
         'hint': '评估搜索空间大小——5!=120是可穷举的，直接枚举比逻辑推导更可靠',
         'hint_level': 0.9, 'generalizability': 'high——"有多个方法但不知道哪个最直接"适用于任何有多个解法的问题',
         'why_not_visible_locally': '在Q2时AI还没评估搜索空间（tell不可见），在Q3时AI已经在穷举了（tell已过时），只有在Q2看前后才能读出'},
    ],
    'bare_ai_expected': 'marginal',
    'bare_ai_error_prediction': '可能试图用逻辑推理逐步排除，但在管理多个约束时容易出错；也可能不知道120种是可穷举的而放弃枚举',
    'suitable_for_poc': ['VMS-search-space-estimation'],
    'discriminates_levels': True,
    'qa_sequence': {
        'rounds': [
            {'round': 1, 'question': '描述题目结构', 'expected_answer': '约束满足问题，5个学生5个名次，两个预测给出约束', 'situation_type': '纯元认知观察', 'level': 1.0},
            {'round': 2, 'question': '列出所有可能方向', 'expected_answer': '穷举枚举、逻辑推导、约束传播', 'situation_type': '自由列举', 'level': 1.0},
            {'round': 3, 'question': '有多少种可能？', 'expected_answer': '5!=120种排列，可以穷举', 'situation_type': '小尝试', 'level': 0.9},
            {'round': 4, 'question': '系统地应用所有约束过滤', 'expected_answer': '逐一检查120种排列，应用所有约束', 'situation_type': '思维操作引导', 'level': 0.7},
            {'round': 5, 'question': '枚举过滤后剩多少？', 'expected_answer': '唯一解：A=3rd,B=5th,C=4th,D=2nd,E=1st', 'situation_type': '推进', 'level': 0.8},
        ],
        'stats': {
            'total_rounds': 5,
            'metacognitive_rounds': 3,
            'knowledge_rounds': 2,
            'level_sum': 4.4,
            'knowledge_bottleneck': None,
            'thinking_bottleneck': 'Q3——评估搜索空间大小决定用枚举',
        }
    },
    'analysis_metadata': {
        'analyzed_by': 'master',
        'analyzed_at': now,
        'analysis_duration': '8min',
        'notes': 'Lean解答用decide tactic做穷举验证，本质就是枚举120种排列',
    }
}

# === 题3: IMO 1966 P5 ===
p3 = {
    '_key': 'compfiles_imo1966p5',
    'source_id': 'Imo1966P5',
    'source_dataset': 'compfiles',
    'schema_version': 2,
    'problem_text': 'Solve the system: |a1-a2|x2 + |a1-a3|x3 + |a1-a4|x4 = 1, |a2-a1|x1 + |a2-a3|x3 + |a2-a4|x4 = 1, |a3-a1|x1 + |a3-a2|x2 + |a3-a4|x4 = 1, |a4-a1|x1 + |a4-a2|x2 + |a4-a3|x3 = 1, where a1,a2,a3,a4 are four different real numbers.',
    'solution_text': 'WLOG assume a1<a2<a3<a4 (by symmetry). Then all absolute values become known differences. Take differences of consecutive equations: eq(i+1)-eq(i) gives telescoping relations. This shows x2=x3=0. Using first and last equations: (a4-a1)(x1+x4)=1, and by symmetry x1=x4=1/(a4-a1). Generalized to n variables in the Lean proof.',
    'solution_summary': 'WLOG排序a_i消除所有绝对值，取相邻方程差得到望远镜消元，中间变量全为零，首尾变量相等。',
    'domain': 'algebra',
    'subfield': 'systems of equations with absolute values',
    'answer_type': 'Expression',
    'answer': 'x1=x4=1/(a4-a1), x2=x3=0 (WLOG a1<a2<a3<a4)',
    'problem_type': 'system of equations with absolute values',
    'solution_method_type': 'WLOG sorting + telescoping elimination',
    'structure_features': '4×4方程组，系数含绝对值|a_i-a_j|，a_i互不相同',
    'key_objects': ['absolute value |a_i-a_j|', 'system of 4 equations', 'four distinct reals a_i'],
    'thinking_patterns': ['WLOG sorting', 'telescoping elimination', 'symmetry exploitation'],
    'primary_pattern': 'WLOG sorting → telescoping',
    'knowledge_required': ['absolute value properties', 'WLOG argument', 'telescoping sums'],
    'key_insight': 'WLOG排序a_i后所有绝对值自动确定，取相邻方程差做望远镜消元',
    'translation_from': 'case-by-case absolute value discussion',
    'translation_to': 'WLOG sorting to eliminate all absolute values at once',
    'translation_type': '分情况讨论→排序消除',
    'tell_topology': {'problem_type': 'absolute_value_system', 'ai_method_type': 'case_by_case', 'gap_type': 'global_sorting'},
    'tell_small_concepts': ['absolute value', 'WLOG', 'sorting', 'telescoping', 'system of equations', 'distinct reals'],
    'expected_ai_method': '分情况讨论每个绝对值的符号（2^12=4096种情况）',
    'correct_method': 'WLOG排序a_i一次性消除所有绝对值',
    'tell_hint_pairs': [
        {'qa_round': 1, 'tell': 'AI面对含绝对值的方程组，尚未识别排序策略', 'hint': '描述题目结构——4×4方程组含绝对值', 'hint_level': 1.0, 'situation_type': '纯元认知观察', 'is_knowledge_bottleneck': False},
        {'qa_round': 2, 'tell': 'AI尚未评估各方向的可行性', 'hint': '列出所有可能方向：分情况讨论、排序a_i、代数消元', 'hint_level': 1.0, 'situation_type': '自由列举', 'is_knowledge_bottleneck': False},
        {'qa_round': 3, 'tell': 'AI试图分情况讨论绝对值——走错路了', 'hint': '试着分情况讨论——12个绝对值2^12=4096种情况太多', 'hint_level': 0.9, 'situation_type': '小尝试', 'is_knowledge_bottleneck': False},
        {'qa_round': 4, 'tell': 'AI在分情况讨论上碰壁，需要全局策略', 'hint': 'WLOG排序a_i——设a1<a2<a3<a4', 'hint_level': 0.7, 'situation_type': '思维操作引导', 'is_knowledge_bottleneck': False},
        {'qa_round': 5, 'tell': 'AI排序后还没看到消元路径', 'hint': '取相邻方程的差——望远镜消元', 'hint_level': 0.7, 'situation_type': '思维操作引导', 'is_knowledge_bottleneck': False},
        {'qa_round': 6, 'tell': 'AI看到消元结果但还没解出变量', 'hint': '望远镜给出了什么？x2=x3=0', 'hint_level': 0.8, 'situation_type': '推进', 'is_knowledge_bottleneck': False},
        {'qa_round': 7, 'tell': 'AI知道中间变量为零但还没解首尾', 'hint': '解x1和x4——用首末方程', 'hint_level': 0.6, 'situation_type': '能量传递引导', 'is_knowledge_bottleneck': False},
    ],
    'global_tell_hint_pairs': [
        {'scope_type': 'path_feature', 'scope': 'translation_type', 'observation_point': None,
         'tell': '整条路径从"分情况讨论绝对值符号"转向"WLOG排序消除绝对值"',
         'hint': '用WLOG排序替代逐个分情况讨论——排序后绝对值自动确定',
         'hint_level': 0.8, 'generalizability': 'high——"分情况→排序消除"适用于任何含绝对值且具有对称性的问题',
         'why_not_visible_locally': None},
        {'scope_type': 'implicit', 'scope': 'implicit_sorting_vs_cases', 'observation_point': 'Q3',
         'tell': 'AI在试图分情况讨论绝对值符号，但解法要求的是通过排序一次性消除所有绝对值——AI不知道"排序可以替代分情况讨论"',
         'hint': '用WLOG排序替代逐个分情况讨论——排序后绝对值自动确定',
         'hint_level': 0.9, 'generalizability': 'high——"有分情况但应该排序"适用于任何含绝对值的对称问题',
         'why_not_visible_locally': '在Q3时AI还在尝试分情况（tell不可见），在Q4时AI已经在排序了（tell已过时），只有在Q3看前后才能读出'},
    ],
    'bare_ai_expected': 'fail',
    'bare_ai_error_prediction': '会试图分情况讨论每个绝对值的符号，面对2^12种情况无法处理；不会想到WLOG排序可以一次性消除所有绝对值',
    'suitable_for_poc': ['VMS-tell-detection', 'VMS-translation-hint', 'VMS-wlog-strategy'],
    'discriminates_levels': True,
    'qa_sequence': {
        'rounds': [
            {'round': 1, 'question': '描述题目结构', 'expected_answer': '4×4方程组含绝对值|a_i-a_j|，a_i互不相同', 'situation_type': '纯元认知观察', 'level': 1.0},
            {'round': 2, 'question': '列出所有可能方向', 'expected_answer': '分情况讨论、排序a_i、代数消元', 'situation_type': '自由列举', 'level': 1.0},
            {'round': 3, 'question': '试着分情况讨论绝对值', 'expected_answer': '12个绝对值2^12=4096种情况太多', 'situation_type': '小尝试', 'level': 0.9},
            {'round': 4, 'question': 'WLOG排序a_i', 'expected_answer': '排序后所有绝对值变成已知差值', 'situation_type': '思维操作引导', 'level': 0.7},
            {'round': 5, 'question': '取相邻方程的差', 'expected_answer': '望远镜关系，大量项消去', 'situation_type': '思维操作引导', 'level': 0.7},
            {'round': 6, 'question': '望远镜给出了什么？', 'expected_answer': 'x2=x3=0，只有x1和x4非零', 'situation_type': '推进', 'level': 0.8},
            {'round': 7, 'question': '解x1和x4', 'expected_answer': 'x1=x4=1/(a4-a1)', 'situation_type': '能量传递引导', 'level': 0.6},
        ],
        'stats': {
            'total_rounds': 7,
            'metacognitive_rounds': 4,
            'knowledge_rounds': 3,
            'level_sum': 5.7,
            'knowledge_bottleneck': None,
            'thinking_bottleneck': 'Q4——从分情况讨论转向WLOG排序',
        }
    },
    'analysis_metadata': {
        'analyzed_by': 'master',
        'analyzed_at': now,
        'analysis_duration': '12min',
        'notes': 'Lean解答很长(334行)，包含n维推广。QA序列只覆盖4维特例的核心思路。',
    }
}

# 入库
for p in [p1, p2, p3]:
    # 保存profile
    profiles.insert(p, overwrite=True)
    # 查找progress中的_key
    docs = list(db.aql.execute(f'FOR p IN problem_extraction_progress FILTER p.problem_id == "{p["_key"]}" RETURN p._key'))
    if docs:
        progress_key = docs[0]
        db.collection('problem_extraction_progress').update({
            '_key': progress_key,
            'extraction_status': 'completed',
            'schema_version': 2,
            'extracted_at': now,
            'profile_doc_id': f"problem_profiles/{p['_key']}",
            'extracted_by': 'master',
        })
    print(f"入库: {p['_key']} ({p['solution_method_type']})")

# 验证
count = list(db.aql.execute('RETURN COUNT(FOR p IN problem_profiles RETURN 1)'))
completed = list(db.aql.execute('RETURN COUNT(FOR p IN problem_extraction_progress FILTER p.extraction_status == "completed" RETURN 1)'))
print(f"\nproblem_profiles总数: {count[0]}")
print(f"completed总数: {completed[0]}")
