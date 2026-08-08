#!/usr/bin/env python3
"""
POC-VMS-3: 批量生成1000个Pattern实例

从基础模板 × 群参数 × 题目类型 × 挑战模板生成Pattern实例。
每个实例的Q字段来自基础模板，但trigger_conditions不同。

生成维度：
1. 基础模板（8个原始 + 12个扩展 = 20个）
2. order×type组合（13个）
3. 题目类型（6种）
4. 挑战模板（T1-T6，6类）——仅对task_type=any的模板

目标：≥1000个Pattern实例
"""

import json
import os

REPO_DIR = '~/master-mind-glm5.2-worktree'


# ============================================================
# 扩展Pattern模板（在8个原始模板基础上补充12个）
# ============================================================

EXTENDED_TEMPLATES = [
    {
        'pattern_id': 'VG-coset-computation',
        'name': '陪集计算',
        'description': '计算子群的左/右陪集，判断是否相等',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has found a subgroup but has not checked if it is normal via cosets'},
        },
        'Q': '计算子群H的左陪集和右陪集。如果左陪集=右陪集（gH=Hg对所有g），则H是正规子群。',
        'Level': 0.5,
        'non_specificity': 0.7,
        'situation_type': '操作引导',
    },
    {
        'pattern_id': 'VG-abelian-check',
        'name': '交换性判断',
        'description': '检查群是否交换（阿贝尔群）——交换群的共轭类都是单元素集，中心就是整个群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'conjugacy_class_computation', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has not yet checked if the group is abelian'},
        },
        'Q': '检查群是否交换——对乘法表中所有i,j，检查a_i*a_j = a_j*a_i。交换群的共轭类都是单元素集，中心就是整个群。',
        'Level': 0.3,
        'non_specificity': 0.8,
        'situation_type': '基础操作引导',
    },
    {
        'pattern_id': 'VG-generator-finding',
        'name': '生成元寻找',
        'description': '寻找群的生成元集合',
        'trigger_conditions': {
            'deterministic': {'task_type': 'cyclic_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has computed element orders but has not checked if any element generates the whole group'},
        },
        'Q': '寻找群的生成元——如果存在一个元素a使得<a>=G（a的阶=|G|），则G是循环群。检查是否有阶等于群阶的元素。',
        'Level': 0.4,
        'non_specificity': 0.7,
        'situation_type': '操作引导',
    },
    {
        'pattern_id': 'VG-quotient-group-construction',
        'name': '商群构造',
        'description': '构造商群G/H',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI has confirmed H is normal but has not constructed the quotient group'},
        },
        'Q': '构造商群G/H——H是正规子群时，G/H的元素是H的陪集，阶=|G|/|H|。商群的结构可以帮助理解原群的结构。',
        'Level': 0.6,
        'non_specificity': 0.6,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-homomorphism-kernel-image',
        'name': '同态核与像',
        'description': '计算同态的核和像',
        'trigger_conditions': {
            'deterministic': {'task_type': 'homomorphism_construction', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is trying to construct a homomorphism but has not considered kernel and image constraints'},
        },
        'Q': '同态φ:G→H的核ker(φ)是G的正规子群，像im(φ)是H的子群。|G|=|ker(φ)|×|im(φ)|。先确定核和像的阶，再构造映射。',
        'Level': 0.6,
        'non_specificity': 0.5,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-isomorphism-test',
        'name': '同构判定',
        'description': '判断两个群是否同构——用于群结构识别',
        'trigger_conditions': {
            'deterministic': {'task_type': 'cyclic_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has computed basic properties but has not compared with known groups'},
        },
        'Q': '判断群是否同构于已知群——比较阶、元素阶分布、交换性、循环性。同构的群有相同的元素阶分布。',
        'Level': 0.5,
        'non_specificity': 0.7,
        'situation_type': '操作引导',
    },
    {
        'pattern_id': 'VG-subgroup-lattice',
        'name': '子群格构造',
        'description': '构造子群格（所有子群的包含关系）',
        'trigger_conditions': {
            'deterministic': {'task_type': 'subgroup_enumeration', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI has found some subgroups but has not organized them into a lattice'},
        },
        'Q': '把所有子群按包含关系组织成格。子群H1⊆H2当且仅当H1的元素都是H2的元素。子群格揭示了群的结构。',
        'Level': 0.7,
        'non_specificity': 0.5,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-centralizer-computation',
        'name': '中心化子计算',
        'description': '计算元素的中心化子',
        'trigger_conditions': {
            'deterministic': {'task_type': 'conjugacy_class_computation', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is computing conjugacy classes by brute force without using centralizers'},
        },
        'Q': '元素a的中心化子C(a)={g: ga=ag}。共轭类[a]的大小=|G|/|C(a)|。先算中心化子，再用轨道-稳定化子定理确定共轭类大小。',
        'Level': 0.6,
        'non_specificity': 0.5,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-class-equation',
        'name': '类方程',
        'description': '用类方程分析群结构',
        'trigger_conditions': {
            'deterministic': {'task_type': 'conjugacy_class_computation', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI has computed conjugacy classes but has not used the class equation'},
        },
        'Q': '类方程：|G|=|Z(G)|+Σ[G:C(a_i)]，其中a_i取遍非中心共轭类的代表元。类方程可以验证共轭类计算的正确性。',
        'Level': 0.7,
        'non_specificity': 0.4,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-sylow-theorem',
        'name': 'Sylow定理应用',
        'description': '用Sylow定理分析群结构',
        'trigger_conditions': {
            'deterministic': {'task_type': 'subgroup_enumeration', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 8}},
            'non_deterministic': {'reasoning_state': 'AI is enumerating subgroups without using Sylow theorems'},
        },
        'Q': 'Sylow定理：如果|G|=p^n×m（gcd(p,m)=1），则G有阶p^n的子群（Sylow p-子群）。Sylow p-子群的个数≡1(mod p)且整除m。用Sylow定理快速定位大子群。',
        'Level': 0.8,
        'non_specificity': 0.3,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-direct-product-decomposition',
        'name': '直积分解',
        'description': '判断群是否可以分解为直积',
        'trigger_conditions': {
            'deterministic': {'task_type': 'group_structure_identification', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI has identified the group order but has not checked for direct product decomposition'},
        },
        'Q': '检查群是否可以分解为直积——如果G有正规子群H和K，使得H∩K={e}且HK=G，则G≅H×K。直积分解简化群结构分析。',
        'Level': 0.7,
        'non_specificity': 0.4,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-permutation-representation',
        'name': '置换表示',
        'description': '用置换表示分析群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'homomorphism_construction', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is constructing homomorphism without considering permutation representations'},
        },
        'Q': 'Cayley定理：每个群同构于某个置换群的子群。把群元素表示为置换，可以帮助构造同态和理解群的作用。',
        'Level': 0.8,
        'non_specificity': 0.3,
        'situation_type': '高级操作引导',
    },
    # ============================================================
    # 第二批扩展模板（20个）——用于POC-VMS-4大规模验证
    # ============================================================
    {
        'pattern_id': 'VG-order-statistics',
        'name': '阶统计',
        'description': '统计各阶元素的个数，用阶分布识别群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'cyclic_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has the multiplication table but has not computed the order distribution'},
        },
        'Q': '统计每个阶的元素个数。阶分布是群的不变量——同构的群有相同的阶分布。例如Z₄有1个阶1+1个阶2+2个阶4，V₄有1个阶1+3个阶2。',
        'Level': 0.4,
        'non_specificity': 0.8,
        'situation_type': '基础操作引导',
    },
    {
        'pattern_id': 'VG-closure-check',
        'name': '封闭性验证',
        'description': '验证子集是否在运算下封闭',
        'trigger_conditions': {
            'deterministic': {'task_type': 'subgroup_enumeration', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has found a subset but has not verified closure'},
        },
        'Q': '验证子集H的封闭性——对H中所有a,b，检查a*b是否仍在H中。封闭性是子群的必要条件。',
        'Level': 0.2,
        'non_specificity': 0.9,
        'situation_type': '基础操作引导',
    },
    {
        'pattern_id': 'VG-inverse-check',
        'name': '逆元验证',
        'description': '验证子集中每个元素是否有逆元',
        'trigger_conditions': {
            'deterministic': {'task_type': 'subgroup_enumeration', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has verified closure but not inverses'},
        },
        'Q': '验证H中每个元素a的逆元a⁻¹是否仍在H中。封闭性+逆元+单位元=子群。',
        'Level': 0.2,
        'non_specificity': 0.9,
        'situation_type': '基础操作引导',
    },
    {
        'pattern_id': 'VG-associativity-verification',
        'name': '结合律验证',
        'description': '验证运算是否满足结合律',
        'trigger_conditions': {
            'deterministic': {'task_type': 'any', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is using the multiplication table without verifying associativity'},
        },
        'Q': '验证结合律——对所有a,b,c，检查(a*b)*c = a*(b*c)。结合律是群公理之一，但给定的乘法表通常已保证。',
        'Level': 0.1,
        'non_specificity': 0.95,
        'situation_type': '基础操作引导',
    },
    {
        'pattern_id': 'VG-conjugation-action',
        'name': '共轭作用分析',
        'description': '分析群的共轭作用',
        'trigger_conditions': {
            'deterministic': {'task_type': 'conjugacy_class_computation', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is computing conjugacy classes without understanding the conjugation action'},
        },
        'Q': '共轭作用g·a=gag⁻¹定义了群在自身上的作用。共轭类是此作用的轨道。理解作用本身比逐个计算共轭更高效。',
        'Level': 0.6,
        'non_specificity': 0.5,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-normalizer-computation',
        'name': '正规化子计算',
        'description': '计算子群的正规化子',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has a subgroup but has not computed its normalizer'},
        },
        'Q': '子群H的正规化子N(H)={g: gHg⁻¹=H}。H是正规子群当且仅当N(H)=G。正规化子可以帮助判断正规性。',
        'Level': 0.7,
        'non_specificity': 0.4,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-commutator-subgroup',
        'name': '换位子群',
        'description': '计算换位子群和导群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI is checking normality by brute force without using the commutator subgroup'},
        },
        'Q': '换位子群G\'=[G,G]由所有换位子[a,b]=a⁻¹b⁻¹ab生成。G\'是正规子群，G/G\'是交换群。G是交换群当且仅当G\'={e}。',
        'Level': 0.8,
        'non_specificity': 0.3,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-center-by-definition',
        'name': '中心定义法',
        'description': '用定义直接计算中心',
        'trigger_conditions': {
            'deterministic': {'task_type': 'center_computation', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is trying to find the center without using the definition directly'},
        },
        'Q': '中心Z(G)={a: ag=ga对所有g}。逐个检查每个元素a是否与所有元素交换。与所有元素交换的元素构成中心。',
        'Level': 0.2,
        'non_specificity': 0.9,
        'situation_type': '基础操作引导',
    },
    {
        'pattern_id': 'VG-cyclic-subgroup-generation',
        'name': '循环子群生成',
        'description': '由元素生成循环子群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'subgroup_enumeration', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is enumerating subsets without generating cyclic subgroups from elements'},
        },
        'Q': '对每个元素a，<a>={e, a, a², ..., a^(ord(a)-1)}是循环子群。所有循环子群都是子群，从元素出发生成子群比枚举子集高效。',
        'Level': 0.3,
        'non_specificity': 0.8,
        'situation_type': '操作引导',
    },
    {
        'pattern_id': 'VG-maximal-subgroup',
        'name': '极大子群',
        'description': '寻找极大子群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'subgroup_enumeration', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI has found some subgroups but has not identified maximal ones'},
        },
        'Q': '极大子群是没有更大子群包含它的子群（除了G本身）。极大子群的阶是|G|/p（p是素因子）。先找极大子群，再找它们的子群。',
        'Level': 0.7,
        'non_specificity': 0.4,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-automorphism-group',
        'name': '自同构群',
        'description': '计算群的自同构群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'homomorphism_construction', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI is constructing homomorphisms without considering automorphisms'},
        },
        'Q': '自同构Aut(G)是G到自身的同构。内自同构由共轭给出：φ_g(a)=gag⁻¹。Aut(G)的结构揭示了群的对称性。',
        'Level': 0.9,
        'non_specificity': 0.2,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-group-presentation',
        'name': '群表示',
        'description': '用生成元和关系表示群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'cyclic_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has computed element orders but has not written a group presentation'},
        },
        'Q': '群表示G=<S|R>，S是生成元集合，R是关系集合。例如Z₄=<a|a⁴=e>。群表示可以帮助识别群的同构类型。',
        'Level': 0.6,
        'non_specificity': 0.5,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-element-conjugation-test',
        'name': '元素共轭判定',
        'description': '判断两个元素是否共轭',
        'trigger_conditions': {
            'deterministic': {'task_type': 'conjugacy_class_computation', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI is computing all conjugates instead of checking if two specific elements are conjugate'},
        },
        'Q': '两个元素a,b共轭当且仅当存在g使得b=gag⁻¹。逐个检查g。如果找到了，a和b在同一共轭类。',
        'Level': 0.3,
        'non_specificity': 0.8,
        'situation_type': '操作引导',
    },
    {
        'pattern_id': 'VG-power-calculation',
        'name': '幂运算',
        'description': '计算元素的幂',
        'trigger_conditions': {
            'deterministic': {'task_type': 'any', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI needs to compute powers of elements but is not using the multiplication table efficiently'},
        },
        'Q': '用乘法表计算a²=a*a, a³=a²*a, ...。幂运算是计算元素阶和生成循环子群的基础。',
        'Level': 0.1,
        'non_specificity': 0.95,
        'situation_type': '基础操作引导',
    },
    {
        'pattern_id': 'VG-index-calculation',
        'name': '指数计算',
        'description': '计算子群的指数',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has a subgroup but has not computed its index'},
        },
        'Q': '子群H在G中的指数[G:H]=|G|/|H|。指数等于陪集的个数。指数为2的子群一定是正规子群。',
        'Level': 0.4,
        'non_specificity': 0.7,
        'situation_type': '操作引导',
    },
    {
        'pattern_id': 'VG-simple-group-check',
        'name': '单群判定',
        'description': '判断群是否是单群',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 8}},
            'non_deterministic': {'reasoning_state': 'AI has found all normal subgroups but has not checked if the group is simple'},
        },
        'Q': '单群是没有非平凡正规子群的群。如果G只有{e}和G两个正规子群，则G是单群。阶为素数的群一定是单群。',
        'Level': 0.8,
        'non_specificity': 0.3,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-solvable-group-check',
        'name': '可解群判定',
        'description': '判断群是否可解',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 8}},
            'non_deterministic': {'reasoning_state': 'AI has the derived subgroup but has not checked solvability'},
        },
        'Q': '可解群有导列G▶G\'▶G\'\'▶...▶{e}有限步到达{e}。交换群可解。p-群可解。阶≤60的群除A₅外都可解。',
        'Level': 0.9,
        'non_specificity': 0.2,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-coset-multiplication',
        'name': '陪集乘法',
        'description': '定义陪集的乘法运算',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has found cosets but has not defined multiplication on cosets'},
        },
        'Q': '当H是正规子群时，陪集的乘法(gH)(g\'H)=(gg\')H是良定义的。这给出了商群G/H的运算。',
        'Level': 0.6,
        'non_specificity': 0.5,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-correspondence-theorem',
        'name': '对应定理',
        'description': '用对应定理分析子群结构',
        'trigger_conditions': {
            'deterministic': {'task_type': 'normal_subgroup_determination', 'has_multiplication_table': True, 'group_order': {'op': '>', 'value': 4}},
            'non_deterministic': {'reasoning_state': 'AI has a normal subgroup but has not used the correspondence theorem'},
        },
        'Q': '对应定理：G的包含N的子群↔G/N的子群。G的包含N的正规子群↔G/N的正规子群。用对应定理从商群结构推断原群结构。',
        'Level': 0.8,
        'non_specificity': 0.3,
        'situation_type': '高级操作引导',
    },
    {
        'pattern_id': 'VG-exponent-calculation',
        'name': '指数计算',
        'description': '计算群的指数（所有元素阶的最小公倍数）',
        'trigger_conditions': {
            'deterministic': {'task_type': 'cyclic_determination', 'has_multiplication_table': True},
            'non_deterministic': {'reasoning_state': 'AI has computed element orders but has not computed the exponent'},
        },
        'Q': '群的指数exp(G)是所有元素阶的最小公倍数。G是循环群当且仅当exp(G)=|G|。用指数快速判断循环性。',
        'Level': 0.5,
        'non_specificity': 0.6,
        'situation_type': '操作引导',
    },
]


def load_base_patterns():
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/base_patterns.json')) as f:
        return json.load(f)


def load_virtual_groups():
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/virtual_groups.json')) as f:
        return json.load(f)


def generate_pattern_instances(base_patterns, groups):
    """从基础模板+扩展模板 × 群参数 × 题目类型 × 挑战模板生成Pattern实例。"""
    
    # 合并原始模板和扩展模板
    all_templates = base_patterns + EXTENDED_TEMPLATES
    
    # 6种题目类型
    task_types = [
        'subgroup_enumeration',
        'normal_subgroup_determination', 
        'cyclic_determination',
        'conjugacy_class_computation',
        'center_computation',
        'homomorphism_construction',
    ]
    
    # 6类挑战模板（T1-T6）
    challenge_templates = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
    
    # 获取唯一的(order, group_type)组合
    order_type_combos = sorted(set((g['order'], g['group_type']) for g in groups))
    
    instances = []
    seen_ids = set()
    
    for template in all_templates:
        pid_base = template['pattern_id']
        tt_cond = template.get('trigger_conditions', {}).get('deterministic', {}).get('task_type', 'any')
        go_cond = template.get('trigger_conditions', {}).get('deterministic', {}).get('group_order')
        
        for order, gtype in order_type_combos:
            # 检查group_order条件
            if go_cond and isinstance(go_cond, dict):
                op = go_cond.get('op')
                val = go_cond.get('value')
                if op == '>' and not (order > val):
                    continue
                if op == 'in' and order not in val:
                    continue
            
            # 确定适用的task_type
            if tt_cond == 'any':
                applicable_tasks = task_types
            else:
                applicable_tasks = [tt_cond]
            
            for task_type in applicable_tasks:
                # 对task_type=any的模板，加入challenge_template维度
                if tt_cond == 'any':
                    challenge_combos = challenge_templates
                else:
                    challenge_combos = ['']  # 特定task_type的模板不加challenge维度
                
                for ct in challenge_combos:
                    # 生成Pattern实例
                    ct_suffix = f'-{ct}' if ct else ''
                    instance_id = f"{pid_base}-o{order}-{gtype}-{task_type}{ct_suffix}"
                    if instance_id in seen_ids:
                        continue
                    seen_ids.add(instance_id)
                    
                    # 构造trigger_conditions
                    det = {
                        'task_type': task_type,
                        'has_multiplication_table': True,
                        'group_order': order,
                        'group_type': gtype,
                    }
                    if ct:
                        det['challenge_template'] = ct
                    
                    instance = {
                        'pattern_id': instance_id,
                        'base_pattern_id': pid_base,
                        'name': template.get('name', ''),
                        'description': template.get('description', ''),
                        'domain': 'virtual_group_theory',
                        'trigger_conditions': {
                            'deterministic': det,
                            'non_deterministic': template.get('trigger_conditions', {}).get('non_deterministic', {}),
                        },
                        'Q': template.get('Q', ''),
                        'Level': template.get('Level', 0.5),
                        'non_specificity': template.get('non_specificity', 0.5),
                        'situation_type': template.get('situation_type', ''),
                        'source': f'batch_generated_o{order}_{gtype}_{task_type}_{ct or "none"}',
                        'ai_used_this_pattern': False,
                        'challenge_template': ct,
                        'challenge_type': '',
                    }
                    instances.append(instance)
    
    return instances


def main():
    print("=== POC-VMS-3: 批量生成Pattern实例 ===\n")
    
    base_patterns = load_base_patterns()
    groups = load_virtual_groups()
    
    print(f"基础模板: {len(base_patterns)}")
    print(f"虚拟群: {len(groups)}")
    
    order_type_combos = sorted(set((g['order'], g['group_type']) for g in groups))
    print(f"order×type组合: {len(order_type_combos)}")
    
    instances = generate_pattern_instances(base_patterns, groups)
    print(f"\n生成Pattern实例: {len(instances)}")
    
    # 按base_pattern_id统计
    from collections import Counter
    by_base = Counter(i['base_pattern_id'] for i in instances)
    print("\n按基础模板统计:")
    for bid, count in sorted(by_base.items()):
        print(f"  {bid}: {count}")
    
    # 写入文件
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms3_patterns_1000.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(instances, f, ensure_ascii=False, indent=2)
    print(f"\n写入: {output_path}")
    
    # 验证唯一性
    ids = [i['pattern_id'] for i in instances]
    print(f"唯一pattern_id: {len(set(ids))}/{len(ids)}")


if __name__ == '__main__':
    main()
