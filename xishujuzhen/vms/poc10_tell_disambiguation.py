#!/usr/bin/env python3
"""
POC-VMS-10: 拓扑相同且距离极近的tell怎么区分

验证目标：
1. Pipe 1（大概念过滤）对拓扑相同的tell给同分——无法区分
2. Pipe 2（小概念标记分辨）能区分拓扑相同但小概念不同的tell

两个tell：
- tell-A: 1631——穷举a值处理Mersenne素数结构问题，hint=T03二次剩余
- tell-B: 1709——穷举a值处理最大奇因子结构问题，hint=T05 2-adic赋值

拓扑完全相同：(structural_existence, enumeration_brute_force, method_problem_mismatch)
距离极近：都是数论题，都是穷举a值，都是结构问题
但小概念不同：穷举对象不同、需要的结构方法不同
"""

import json
import os
import re
import sys

# ============================================================
# tell数据基座——两个拓扑相同且距离极近的tell
# ============================================================

TELL_DATABASE = [
    {
        "tell_id": "tell-A",
        "name": "穷举参数处理素数存在性结构问题",
        "source_problem": 1631,
        # 大概念（拓扑结构）——与tell-B完全相同
        "topology": {
            "problem_type": "structural_existence",
            "ai_method_type": "enumeration_brute_force",
            "gap_type": "method_problem_mismatch",
        },
        # 小概念（标准化语言描述）——与tell-B不同
        "small_concepts": {
            "enumeration_object": "sequence_parameter",  # 穷举的对象是序列参数
            "problem_structure": "primality",  # 问题的结构是素数性
            "correct_method_type": "quadratic_residue",  # 正确方法是二次剩余
            "number_theory_subfield": "mersenne_primes",  # 数论子领域是Mersenne素数
        },
        "small_concept_description": "AI在枚举序列参数a的值（a=2,3,5,11...），试图用covering system覆盖所有情况，但问题是Mersenne素数的存在性，需要用二次剩余/Euler准则来发现x_3≡7(mod 8)的结构矛盾",
        "hint": "T03二次剩余——利用模p的二次剩余性质得到结构矛盾",
        "hint_id": "T03",
    },
    {
        "tell_id": "tell-B",
        "name": "穷举参数处理整除性判定结构问题",
        "source_problem": 1709,
        # 大概念（拓扑结构）——与tell-A完全相同
        "topology": {
            "problem_type": "structural_existence",
            "ai_method_type": "enumeration_brute_force",
            "gap_type": "method_problem_mismatch",
        },
        # 小概念（标准化语言描述）——与tell-A不同
        "small_concepts": {
            "enumeration_object": "difference_parameter",  # 穷举的对象是差分参数
            "problem_structure": "divisibility",  # 问题的结构是整除性
            "correct_method_type": "p_adic_valuation",  # 正确方法是p-adic赋值
            "number_theory_subfield": "largest_odd_divisor",  # 数论子领域是最大奇因子
        },
        "small_concept_description": "AI在枚举差分参数a的值（a=1,2,3,...），试图逐一验证条件，但问题是最大奇因子差的整除性判定，需要用2-adic赋值（a=2^α·d）分case分析模4行为",
        "hint": "T05 2-adic赋值——用最高2幂次分析a的奇偶性，分case证明存在i使差不被4整除",
        "hint_id": "T05",
    },
]

# ============================================================
# Pipe 0: 拓扑化（复用POC-VMS-9的逻辑）
# ============================================================

CONTINUOUS_SIGNALS = [
    'polynomial sign', 'sign analysis', 'f(x) > 0', 'f(x) < 0', 'positive for all',
    'negative for all', 'derivative', '导数', 'integral', '积分', 'limit',
    '极限', 'continuous', '连续', 'IVT', 'intermediate value',
    'cubic', '三次多项式', 'quadratic formula', '求根公式',
    'discriminant', '判别式', 'real root', '实根',
    's^3', 's^2', 'expand', '展开',
]

ENUMERATION_SIGNALS = [
    'enumerate', '枚举', 'listing', '列举', 'try a=2', 'try a=3', 'try a=5',
    'case by case', 'covering', 'covering system', 'brute force',
    'check each', '逐一检查', '试了', 'let me try',
    'a=2', 'a=3', 'a=5', 'a=11', 'a=7',
]

DISCRETE_PROBLEM_SIGNALS = [
    'erase', '擦除', 'factor', '因子', 'partition', '划分',
    'grouping', '分组', 'coloring', '染色', 'domino', '多米诺',
    'integer', '整数', 'divisible', '整除', 'mod', '模',
    'parity', '奇偶', 'prime', '素数',
]

STRUCTURAL_PROBLEM_SIGNALS = [
    'mersenne', '梅森', 'prime', '素数', 'exist', '存在',
    'find all', '求所有', 'find the maximum', '求最大',
    'surjective', '满射', 'function', '函数',
    'sequence', '序列', 'recursive', '递推',
]

# 小概念信号词——用于Pipe 2的标记分辨
# tell-A的小概念信号
TELL_A_SMALL_CONCEPT_SIGNALS = {
    "mersenne": ["mersenne", "梅森", "2^x", "2^n", "2^{x_n}", "2^{x_n}-1", "y_n"],
    "primality": ["prime", "素数", "mersenne prime", "梅森素数", "is prime", "is a prime", "primality"],
    "quadratic_residue_hint": ["euler", "legendre", "quadratic residue", "二次剩余", "euler criterion"],
    "covering_system": ["covering", "covering system", "cover all", "覆盖"],
}

# tell-B的小概念信号
TELL_B_SMALL_CONCEPT_SIGNALS = {
    "largest_odd_divisor": ["largest odd", "最大奇", "odd divisor", "奇因子", "t(k)", "t(n)", "t(a)"],
    "divisibility_4": ["divisible by 4", "被4整除", "divisible by 4", "mod 4", "模4", "\\pmod{4}"],
    "p_adic_hint": ["2-adic", "2^\\alpha", "2^s", "valuation", "赋值", "highest power of 2", "最高幂"],
    "difference_parameter": ["t(n+a)", "t(n+i)", "difference", "差", "t(n+a)-t(n)"],
}


def pipe0_topologize(thinking_text: str) -> dict:
    """Pipe 0: 将thinking编码为拓扑结构（大概念）。"""
    thinking_lower = thinking_text.lower()
    
    continuous_freq = sum(thinking_lower.count(kw.lower()) for kw in CONTINUOUS_SIGNALS)
    enumeration_freq = sum(thinking_lower.count(kw.lower()) for kw in ENUMERATION_SIGNALS)
    
    total_method = continuous_freq + enumeration_freq
    if total_method == 0:
        ai_method_type = "unknown"
    elif enumeration_freq > continuous_freq:
        ai_method_type = "enumeration_brute_force"
    elif continuous_freq > enumeration_freq:
        ai_method_type = "continuous_analytic"
    else:
        ai_method_type = "unknown"
    
    discrete_specific = sum(thinking_lower.count(kw.lower()) for kw in [
        'erase', '擦除', 'partition', '划分', 'grouping', '分组',
        'coloring', '染色', 'domino', '多米诺', 'parity', '奇偶',
    ])
    structural_specific = sum(thinking_lower.count(kw.lower()) for kw in [
        'mersenne', '梅森', 'surjective', '满射', 'sequence', '序列',
        'recursive', '递推', 'find all', '求所有', 'find the maximum', '求最大',
        'exist', '存在', 'largest odd', '最大奇', 'odd divisor', '奇因子',
    ])
    
    if discrete_specific > structural_specific:
        problem_type = "discrete_combinatorial"
    elif structural_specific > discrete_specific:
        problem_type = "structural_existence"
    else:
        problem_type = "unknown"
    
    if ai_method_type == "continuous_analytic" and problem_type == "discrete_combinatorial":
        gap_type = "method_problem_mismatch"
    elif ai_method_type == "enumeration_brute_force" and problem_type == "structural_existence":
        gap_type = "method_problem_mismatch"
    elif ai_method_type == "continuous_analytic" and problem_type == "structural_existence":
        gap_type = "method_problem_mismatch"
    elif ai_method_type == "enumeration_brute_force" and problem_type == "discrete_combinatorial":
        gap_type = "method_problem_mismatch"
    else:
        gap_type = "unknown"
    
    return {
        "problem_type": problem_type,
        "ai_method_type": ai_method_type,
        "gap_type": gap_type,
        "signal_counts": {
            "continuous": continuous_freq,
            "enumeration": enumeration_freq,
            "discrete_specific": discrete_specific,
            "structural_specific": structural_specific,
        },
    }


# ============================================================
# Pipe 1: 形式化过滤（大概念匹配）
# ============================================================

def pipe1_filter(thinking_topology: dict, tell_db: list) -> list:
    """Pipe 1: 用大概念（拓扑）匹配tell。拓扑相同的tell会得到同分。"""
    candidates = []
    
    for tell in tell_db:
        tell_topo = tell["topology"]
        
        if thinking_topology["gap_type"] != tell_topo["gap_type"]:
            continue
        
        score = 0
        if thinking_topology["problem_type"] == tell_topo["problem_type"]:
            score += 2
        if thinking_topology["ai_method_type"] == tell_topo["ai_method_type"]:
            score += 2
        
        candidates.append({
            "tell_id": tell["tell_id"],
            "name": tell["name"],
            "hint": tell["hint"],
            "hint_id": tell["hint_id"],
            "topology": tell_topo,
            "small_concepts": tell.get("small_concepts", {}),
            "small_concept_description": tell.get("small_concept_description", ""),
            "match_score": score,
        })
    
    candidates.sort(key=lambda x: x["match_score"], reverse=True)
    return candidates


# ============================================================
# Pipe 2: 小概念标记分辨
# ============================================================

def pipe2_small_concept_disambiguation(thinking_text: str, candidates: list) -> list:
    """
    Pipe 2: 用小概念标记分辨拓扑相同的候选tell。
    
    对每个候选tell，检查thinking中是否出现该tell的小概念信号词。
    小概念信号匹配更多的tell更可能是目标tell。
    """
    thinking_lower = thinking_text.lower()
    
    # 小概念信号定义
    small_concept_signals = {
        "tell-A": {
            "mersenne": ["mersenne", "梅森", "2^x", "2^n", "2^{x_n}", "y_n", "y_1", "y_2", "y_3"],
            "primality": ["prime", "素数", "mersenne prime", "is prime", "is a prime", "primality"],
            "quadratic_residue_context": ["euler", "legendre", "quadratic residue", "二次剩余"],
            "covering_system": ["covering", "covering system", "cover all", "覆盖"],
        },
        "tell-B": {
            "largest_odd_divisor": ["largest odd", "最大奇", "odd divisor", "奇因子", "t(k)", "t(n)", "t(a)"],
            "divisibility_4": ["divisible by 4", "被4整除", "mod 4", "模4", "pmod{4}"],
            "p_adic_context": ["2-adic", "2^\\alpha", "2^s", "valuation", "赋值", "highest power of 2"],
            "difference_parameter": ["t(n+a)", "t(n+i)", "difference", "差"],
        },
    }
    
    results = []
    for cand in candidates:
        tell_id = cand["tell_id"]
        signals = small_concept_signals.get(tell_id, {})
        
        # 统计小概念信号匹配
        small_concept_hits = {}
        total_hits = 0
        for concept_name, keywords in signals.items():
            hits = sum(thinking_lower.count(kw.lower()) for kw in keywords)
            small_concept_hits[concept_name] = hits
            total_hits += hits
        
        results.append({
            **cand,
            "small_concept_hits": small_concept_hits,
            "small_concept_total_hits": total_hits,
            "combined_score": cand["match_score"] * 10 + total_hits,  # 大概念分数为主，小概念为辅
        })
    
    # 按combined_score排序
    results.sort(key=lambda x: x["combined_score"], reverse=True)
    return results


# ============================================================
# POC验证主流程
# ============================================================

def run_poc():
    """运行POC-VMS-10验证。"""
    
    thinking_dir = "/data/math-agent-glm5.2-tmux-agents-trajectory"
    
    experiments = [
        {
            "name": "1631 (tell-A的题目)",
            "exp_id": "vms-poc8-1631-bare",
            "target_tell_id": "tell-A",
            "interference_tell_id": "tell-B",
        },
        {
            "name": "1709 (tell-B的题目)",
            "exp_id": "vms-poc10-1709-bare",
            "target_tell_id": "tell-B",
            "interference_tell_id": "tell-A",
        },
    ]
    
    results = []
    
    for exp in experiments:
        thinking_path = f"{thinking_dir}/{exp['exp_id']}/mitm/thinking_readable.txt"
        if not os.path.exists(thinking_path):
            print(f"❌ {exp['name']}: thinking文件不存在 {thinking_path}")
            continue
        
        with open(thinking_path, 'r', encoding='utf-8') as f:
            thinking_text = f.read()
        
        print(f"\n{'='*60}")
        print(f"=== {exp['name']} ===")
        print(f"{'='*60}")
        
        # Pipe 0: 拓扑化
        topology = pipe0_topologize(thinking_text)
        print(f"\nPipe 0 拓扑化结果:")
        print(f"  problem_type: {topology['problem_type']}")
        print(f"  ai_method_type: {topology['ai_method_type']}")
        print(f"  gap_type: {topology['gap_type']}")
        print(f"  signal_counts: {topology['signal_counts']}")
        
        # Pipe 1: 大概念过滤
        candidates = pipe1_filter(topology, TELL_DATABASE)
        print(f"\nPipe 1 大概念过滤结果 ({len(candidates)}个候选):")
        for c in candidates:
            is_target = c["tell_id"] == exp["target_tell_id"]
            is_interference = c["tell_id"] == exp["interference_tell_id"]
            label = "← 目标tell" if is_target else ("← 干扰tell" if is_interference else "")
            print(f"  tell_id={c['tell_id']}, name={c['name']}, score={c['match_score']} {label}")
        
        # 检查Pipe 1是否给同分（大概念无法区分）
        if len(candidates) >= 2:
            scores = [c["match_score"] for c in candidates]
            pipe1_tied = len(set(scores)) == 1
            print(f"\n  Pipe 1是否给同分（大概念无法区分）: {'✅ 是——需要Pipe 2' if pipe1_tied else '❌ 否——Pipe 1已能区分'}")
        else:
            pipe1_tied = False
        
        # Pipe 2: 小概念标记分辨
        print(f"\nPipe 2 小概念标记分辨:")
        disambiguated = pipe2_small_concept_disambiguation(thinking_text, candidates)
        for d in disambiguated:
            is_target = d["tell_id"] == exp["target_tell_id"]
            is_interference = d["tell_id"] == exp["interference_tell_id"]
            label = "← 目标tell" if is_target else ("← 干扰tell" if is_interference else "")
            print(f"  tell_id={d['tell_id']}, small_concept_hits={d['small_concept_hits']}, total={d['small_concept_total_hits']}, combined={d['combined_score']} {label}")
        
        # 验证
        target = next((d for d in disambiguated if d["tell_id"] == exp["target_tell_id"]), None)
        interference = next((d for d in disambiguated if d["tell_id"] == exp["interference_tell_id"]), None)
        
        pipe1_target_hit = target is not None
        pipe1_tied_with_interference = (target and interference and target["match_score"] == interference["match_score"])
        pipe2_target_wins = (target and interference and target["combined_score"] > interference["combined_score"])
        
        result = {
            "name": exp["name"],
            "exp_id": exp["exp_id"],
            "topology": topology,
            "pipe1_candidates": [{"tell_id": c["tell_id"], "score": c["match_score"]} for c in candidates],
            "pipe1_tied": pipe1_tied_with_interference,
            "pipe2_results": [{"tell_id": d["tell_id"], "small_concept_hits": d["small_concept_hits"], "total": d["small_concept_total_hits"], "combined": d["combined_score"]} for d in disambiguated],
            "pipe2_target_wins": pipe2_target_wins,
        }
        results.append(result)
        
        print(f"\n验证:")
        print(f"  Pipe 1命中目标tell: {'✅' if pipe1_target_hit else '❌'}")
        print(f"  Pipe 1给同分（大概念无法区分）: {'✅ 是' if pipe1_tied_with_interference else '❌ 否'}")
        print(f"  Pipe 2目标tell胜出（小概念能区分）: {'✅' if pipe2_target_wins else '❌'}")
    
    # 总结
    print(f"\n{'='*60}")
    print(f"POC-VMS-10 验证总结:")
    print(f"{'='*60}")
    all_pipe1_tied = all(r["pipe1_tied"] for r in results)
    all_pipe2_wins = all(r["pipe2_target_wins"] for r in results)
    print(f"  Pipe 1对拓扑相同的tell给同分（验证了大概念无法区分）: {'✅ PASS' if all_pipe1_tied else '❌ FAIL'}")
    print(f"  Pipe 2小概念标记分辨成功（目标tell胜出）: {'✅ PASS' if all_pipe2_wins else '❌ FAIL'}")
    
    return results


if __name__ == "__main__":
    results = run_poc()
    
    output_path = "runs/vms_poc_0/vms10_pipe_results.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n结果已保存到 {output_path}")
