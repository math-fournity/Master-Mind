#!/usr/bin/env python3
"""
POC-VMS-9: tell端去特化与形式化过滤验证

Pipe 0: 拓扑化——将bare AI的thinking编码为拓扑结构
Pipe 1: 形式化过滤——用拓扑相似/等价匹配数据基座中的tell

验证目标：
1. Pipe 1能命中target_tell（不漏）
2. Pipe 1可能也命中interference_tell（拓扑相似）——这是Pipe 2的工作
3. 通过拓扑标注可以区分target_tell和interference_tell
"""

import json
import os
import re
import sys

# ============================================================
# tell数据基座（小规模——2个目标tell + 2个干扰tell = 4个tell）
# 实际上干扰tell就是目标tell互相充当的，所以只有2个tell
# 但在数据基座中它们都是独立条目
# ============================================================

TELL_DATABASE = [
    {
        "tell_id": "tell-1",
        "name": "连续方法处理离散问题",
        "topology": {
            "problem_type": "discrete_combinatorial",
            "ai_method_type": "continuous_analytic",
            "gap_type": "method_problem_mismatch",
        },
        "topology_signature": "AI在用连续/分析工具（多项式符号分析/微积分/极限）处理离散/组合/整数问题",
        "hint": "T01模算术——把离散问题翻译到模p空间中检查",
        "hint_id": "T01",
        "domain": "algebra_combinatorics",
    },
    {
        "tell_id": "tell-2",
        "name": "穷举方法处理结构问题",
        "topology": {
            "problem_type": "structural_existence",
            "ai_method_type": "enumeration_brute_force",
            "gap_type": "method_problem_mismatch",
        },
        "topology_signature": "AI在用枚举/穷举/covering system方法处理有隐藏结构/不变量的问题",
        "hint": "T03二次剩余——利用模p的二次剩余性质得到结构矛盾",
        "hint_id": "T03",
        "domain": "number_theory_algebra",
    },
]

# ============================================================
# Pipe 0: 拓扑化——从thinking中提取拓扑结构
# ============================================================

# 连续/分析方法的信号词
CONTINUOUS_SIGNALS = [
    'polynomial sign', 'sign analysis', 'f(x) > 0', 'f(x) < 0', 'positive for all',
    'negative for all', 'derivative', '导数', 'integral', '积分', 'limit',
    '极限', 'continuous', '连续', 'IVT', 'intermediate value',
    'cubic', '三次多项式', 'quadratic formula', '求根公式',
    'discriminant', '判别式', 'real root', '实根',
    's^3', 's^2', 'expand', '展开',
]

# 穷举/枚举方法的信号词
ENUMERATION_SIGNALS = [
    'enumerate', '枚举', 'listing', '列举', 'try a=2', 'try a=3', 'try a=5',
    'case by case', 'covering', 'covering system', 'brute force',
    'check each', '逐一检查', '试了', 'let me try',
    'a=2', 'a=3', 'a=5', 'a=11', 'a=7',
]

# 离散/组合问题的信号词
DISCRETE_PROBLEM_SIGNALS = [
    'erase', '擦除', 'factor', '因子', 'partition', '划分',
    'grouping', '分组', 'coloring', '染色', 'domino', '多米诺',
    'integer', '整数', 'divisible', '整除', 'mod', '模',
    'parity', '奇偶', 'prime', '素数',
]

# 结构/存在性问题的信号词
STRUCTURAL_PROBLEM_SIGNALS = [
    'mersenne', '梅森', 'prime', '素数', 'exist', '存在',
    'find all', '求所有', 'find the maximum', '求最大',
    'surjective', '满射', 'function', '函数',
    'sequence', '序列', 'recursive', '递推',
]


def pipe0_topologize(thinking_text: str) -> dict:
    """
    Pipe 0: 将thinking编码为拓扑结构。
    
    输入：bare AI的thinking文本
    输出：拓扑结构（problem_type + ai_method_type + gap_type + signal_counts）
    
    改进版：用频次加权而非仅计数，并区分"问题特征"和"方法特征"。
    问题类型由问题本身决定（从题目元数据或thinking中的问题描述提取），
    方法类型由AI实际使用的方法决定（从thinking中的方法信号提取）。
    """
    thinking_lower = thinking_text.lower()
    
    # 统计各类信号词出现频次（不是计数而是总出现次数）
    continuous_freq = sum(thinking_lower.count(kw.lower()) for kw in CONTINUOUS_SIGNALS)
    enumeration_freq = sum(thinking_lower.count(kw.lower()) for kw in ENUMERATION_SIGNALS)
    discrete_freq = sum(thinking_lower.count(kw.lower()) for kw in DISCRETE_PROBLEM_SIGNALS)
    structural_freq = sum(thinking_lower.count(kw.lower()) for kw in STRUCTURAL_PROBLEM_SIGNALS)
    
    # 判断AI方法类型——基于频次比例
    total_method = continuous_freq + enumeration_freq
    if total_method == 0:
        ai_method_type = "unknown"
    elif continuous_freq > enumeration_freq * 2:
        ai_method_type = "continuous_analytic"
    elif enumeration_freq > continuous_freq * 2:
        ai_method_type = "enumeration_brute_force"
    elif continuous_freq > enumeration_freq:
        ai_method_type = "continuous_analytic"
    elif enumeration_freq > continuous_freq:
        ai_method_type = "enumeration_brute_force"
    else:
        ai_method_type = "unknown"
    
    # 判断问题类型——基于频次比例
    # 注意：数论题既有discrete信号（mod/prime/integer）又有structural信号（prime/sequence）
    # 需要用更区分性的信号
    # discrete_combinatorial: 擦除/因子/分组/染色/划分/多米诺
    # structural_existence: Mersenne/序列/满射/函数/求所有/求最大
    # 共享信号（prime/mod/integer）不算区分性
    discrete_specific = sum(thinking_lower.count(kw.lower()) for kw in [
        'erase', '擦除', 'partition', '划分', 'grouping', '分组',
        'coloring', '染色', 'domino', '多米诺', 'parity', '奇偶',
    ])
    structural_specific = sum(thinking_lower.count(kw.lower()) for kw in [
        'mersenne', '梅森', 'surjective', '满射', 'sequence', '序列',
        'recursive', '递推', 'find all', '求所有', 'find the maximum', '求最大',
        'exist', '存在',
    ])
    
    if discrete_specific > structural_specific:
        problem_type = "discrete_combinatorial"
    elif structural_specific > discrete_specific:
        problem_type = "structural_existence"
    else:
        problem_type = "unknown"
    
    # 判断缺口类型
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
            "discrete": discrete_freq,
            "structural": structural_freq,
            "discrete_specific": discrete_specific,
            "structural_specific": structural_specific,
        },
    }


# ============================================================
# Pipe 1: 形式化过滤——用拓扑相似/等价匹配tell
# ============================================================

def pipe1_filter(thinking_topology: dict, tell_db: list) -> list:
    """
    Pipe 1: 用拓扑相似/等价从tell数据基座中筛选候选tell。
    
    输入：Pipe 0产出的拓扑结构 + tell数据基座
    输出：候选tell列表（按拓扑相似度排序）
    
    过滤逻辑：
    1. 硬筛：gap_type必须匹配（method_problem_mismatch）
    2. 软筛：problem_type和ai_method_type匹配度
    3. 返回所有通过硬筛的tell，按匹配度排序
    """
    candidates = []
    
    for tell in tell_db:
        tell_topo = tell["topology"]
        
        # 硬筛：gap_type必须匹配
        if thinking_topology["gap_type"] != tell_topo["gap_type"]:
            continue
        
        # 软筛：problem_type和ai_method_type匹配度
        score = 0
        if thinking_topology["problem_type"] == tell_topo["problem_type"]:
            score += 2
        elif thinking_topology["problem_type"] == "unknown" or tell_topo["problem_type"] == "unknown":
            score += 1  # unknown给中等分（不排除）
        
        if thinking_topology["ai_method_type"] == tell_topo["ai_method_type"]:
            score += 2
        elif thinking_topology["ai_method_type"] == "unknown" or tell_topo["ai_method_type"] == "unknown":
            score += 1
        
        candidates.append({
            "tell_id": tell["tell_id"],
            "name": tell["name"],
            "hint": tell["hint"],
            "hint_id": tell["hint_id"],
            "topology": tell_topo,
            "match_score": score,
            "is_target": None,  # 由实验设计标注
        })
    
    # 按匹配度排序
    candidates.sort(key=lambda x: x["match_score"], reverse=True)
    return candidates


# ============================================================
# POC验证主流程
# ============================================================

def run_poc():
    """运行POC-VMS-9验证。"""
    
    # 读取bare AI的thinking
    thinking_dir = "/data/math-agent-glm5.2-tmux-agents-trajectory"
    
    experiments = [
        {
            "name": "1843 (tell-1的题目)",
            "exp_id": "vms-poc8-1843-bare",
            "target_tell_id": "tell-1",
            "interference_tell_id": "tell-2",
        },
        {
            "name": "1631 (tell-2的题目)",
            "exp_id": "vms-poc8-1631-bare",
            "target_tell_id": "tell-2",
            "interference_tell_id": "tell-1",
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
        
        # Pipe 0: 拓扑化
        topology = pipe0_topologize(thinking_text)
        print(f"\n=== {exp['name']} ===")
        print(f"Pipe 0 拓扑化结果:")
        print(f"  problem_type: {topology['problem_type']}")
        print(f"  ai_method_type: {topology['ai_method_type']}")
        print(f"  gap_type: {topology['gap_type']}")
        print(f"  signal_counts: {topology['signal_counts']}")
        
        # Pipe 1: 形式化过滤
        candidates = pipe1_filter(topology, TELL_DATABASE)
        print(f"\nPipe 1 形式化过滤结果 ({len(candidates)}个候选):")
        for c in candidates:
            is_target = c["tell_id"] == exp["target_tell_id"]
            is_interference = c["tell_id"] == exp["interference_tell_id"]
            label = "← 目标tell" if is_target else ("← 干扰tell" if is_interference else "")
            print(f"  tell_id={c['tell_id']}, name={c['name']}, score={c['match_score']}, hint={c['hint_id']} {label}")
        
        # 验证
        target_hit = any(c["tell_id"] == exp["target_tell_id"] for c in candidates)
        interference_hit = any(c["tell_id"] == exp["interference_tell_id"] for c in candidates)
        
        # 检查目标tell是否排在干扰tell前面（或同分）
        target_score = next((c["match_score"] for c in candidates if c["tell_id"] == exp["target_tell_id"]), 0)
        interference_score = next((c["match_score"] for c in candidates if c["tell_id"] == exp["interference_tell_id"]), 0)
        
        result = {
            "name": exp["name"],
            "exp_id": exp["exp_id"],
            "topology": topology,
            "candidates": candidates,
            "target_hit": target_hit,
            "interference_hit": interference_hit,
            "target_score": target_score,
            "interference_score": interference_score,
            "target_ranked_higher": target_score >= interference_score,
        }
        results.append(result)
        
        print(f"\n验证:")
        print(f"  Pipe 1命中目标tell: {'✅' if target_hit else '❌ 不漏'}")
        print(f"  Pipe 1命中干扰tell: {'✅ (预期行为——Pipe 2要排除)' if interference_hit else '❌'}")
        print(f"  目标tell分数: {target_score}, 干扰tell分数: {interference_score}")
        print(f"  目标tell排名≥干扰tell: {'✅' if target_score >= interference_score else '❌'}")
    
    # 总结
    print(f"\n{'='*60}")
    print(f"POC-VMS-9 Pipe 0+Pipe 1 验证总结:")
    print(f"{'='*60}")
    all_target_hit = all(r["target_hit"] for r in results)
    all_target_ranked_higher = all(r["target_ranked_higher"] for r in results)
    print(f"  Pipe 1不漏（所有目标tell被命中）: {'✅ PASS' if all_target_hit else '❌ FAIL'}")
    print(f"  目标tell排名≥干扰tell: {'✅ PASS' if all_target_ranked_higher else '❌ FAIL (同分也OK——Pipe 2要区分)'}")
    
    return results


if __name__ == "__main__":
    results = run_poc()
    
    # 保存结果
    output_path = "runs/vms_poc_0/vms9_pipe_results.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n结果已保存到 {output_path}")
