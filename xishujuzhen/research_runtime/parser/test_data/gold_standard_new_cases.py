"""
2个新案例的Gold Standard（人工标注的正确解析结果）。

案例1：数论题（p ≡ 1 mod n的素数无穷）
案例2：组合/概率题（n人猜帽子策略）

每个A_i的Gold Standard是A_i之后的完整状态（含累积的六元组），
格式同gold_standard.py。
"""

# ===========================================================================
# 案例1：数论题 Gold Standard
# ===========================================================================

# ---------------------------------------------------------------------------
# A1: 读题，识别为"存在无穷多个"型命题，列出方向
# 主要事件类型: OBSERVATION + CANDIDATE(多个)
# 前沿节点类型: candidate
# 六元组关键变化: F_t: {"存在无穷多个型命题", "候选方向"}
# ---------------------------------------------------------------------------

NT_GOLD_STANDARD_A1 = {
    "semantic_events": [
        {
            "type": "OBSERVATION",
            "description": "识别为'存在无穷多个'型命题——证明满足p≡1(mod n)的素数集合是无穷集",
            "raw_text_span": "结论是\"存在无穷多个\"型命题——要证明某个集合（满足p≡1(mod n)的素数）是无穷集。",
            "math_objects": [
                {
                    "name": "目标命题",
                    "latex": "\\forall n \\in \\mathbb{Z}^+, \\, |\\{p \\text{ prime} : p \\equiv 1 \\pmod{n}\\}| = \\infty",
                    "sympy_expr": "p_mod_n_infinite",
                    "object_type": "claim",
                    "variables": ["n", "p"],
                    "properties": {"type": "infinitude_claim"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "CANDIDATE",
            "description": "反证法——假设只有有限个，构造矛盾",
            "raw_text_span": "反证法——假设只有有限个，构造矛盾",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "构造法——直接构造无穷序列",
            "raw_text_span": "构造法——直接构造无穷序列",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "用分圆多项式的性质",
            "raw_text_span": "用分圆多项式的性质",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "Dirichlet定理直接给出结论（但太重）",
            "raw_text_span": "Dirichlet定理直接给出结论（但太重了）",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.7,
        },
    ],
    "trajectory_nodes": [
        {
            "type": "observation",
            "content": "存在无穷多个型命题：p≡1(mod n)的素数无穷",
            "math_objects": ["目标命题"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "candidate",
            "content": "反证法",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "构造法",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "分圆多项式性质",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "Dirichlet定理（太重）",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.7,
        },
    ],
    "trajectory_edges": [],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "存在无穷多个型命题：p≡1(mod n)的素数无穷", "status": "exploring"},
            {"statement": "候选方向：反证法、构造法、分圆多项式、Dirichlet定理", "status": "exploring"}
        ],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.88,
    "parse_warnings": [],
}


# ---------------------------------------------------------------------------
# A2: 尝试反证法，构造N = n·p₁·...·p_k + 1，遇到卡点
# 主要事件类型: REPRESENTATION + STALL
# 前沿节点类型: stall
# 六元组关键变化: R_t: {"反证法构造N"}; U_t: {"N的素因子不一定≡1(mod n)"}
# ---------------------------------------------------------------------------

NT_GOLD_STANDARD_A2 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "反证法：假设p₁,...,p_k是所有p≡1(mod n)的素数，构造N = n·p₁·...·p_k + 1",
            "raw_text_span": "假设只有有限个素数p₁, p₂, ..., p_k满足p_i ≡ 1 (mod n)。构造N = n·p₁·p₂·...·p_k + 1。",
            "math_objects": [
                {
                    "name": "N的构造",
                    "latex": "N = n \\cdot p_1 \\cdot p_2 \\cdots p_k + 1",
                    "sympy_expr": "N_val - n*p - 1",
                    "object_type": "definition",
                    "variables": ["N", "n", "p_1", "p_k"],
                    "properties": {"method": "euclid_style"},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "RESOLUTION",
            "description": "N ≡ 1 (mod n)，但N的素因子不一定各自≡1(mod n)",
            "raw_text_span": "N ≡ 1 (mod n)只说明N作为整体模n余1，但N的素因子可能各自模n余别的值。",
            "math_objects": [
                {
                    "name": "N模n",
                    "latex": "N \\equiv 1 \\pmod{n}",
                    "sympy_expr": "N_val % n - 1",
                    "object_type": "equation",
                    "variables": ["N", "n"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "STALL",
            "description": "构造N = n·p₁·...·p_k + 1不能直接保证新素因子≡1(mod n)",
            "raw_text_span": "构造N = n·p₁·...·p_k + 1不能直接保证新素因子≡1(mod n)。需要更强的构造。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "N = n·p₁·...·p_k + 1（Euclid风格构造）",
            "math_objects": ["N的构造"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "resolution",
            "content": "N ≡ 1 (mod n)但素因子不一定≡1(mod n)",
            "math_objects": ["N模n"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "stall",
            "content": "Euclid风格构造不够强——需要保证素因子≡1(mod n)",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.8,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从N的构造推出N≡1(mod n)",
        },
        {
            "source_type": "resolution",
            "target_type": "stall",
            "edge_type": "infer",
            "description": "从N≡1(mod n)但素因子不保证≡1(mod n)到卡点",
        }
    ],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "存在无穷多个型命题", "status": "exploring"}
        ],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "in_progress"},
            {"description": "构造使新素因子≡1(mod n)的数", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "反证法构造N", "description": "N = n·p₁·...·p_k + 1", "introduced_at_round": 2}
        ],
        "E_t": [],
        "U_t": [
            {"description": "N的素因子不一定≡1(mod n)——需要更强的构造", "severity": "blocking", "identified_at_round": 2}
        ],
    },
    "parse_confidence": 0.85,
    "parse_warnings": ["Euclid风格构造对mod n条件不够强"],
}


# ---------------------------------------------------------------------------
# A3: 改用M = A^n - 1，用阶的关系，遇到卡点（阶可能是真因子）
# 主要事件类型: REPRESENTATION + RESOLUTION + STALL
# 前沿节点类型: stall
# 六元组关键变化: R_t: {"A^n-1构造"}; U_t: {"阶可能是n的真因子"}
# ---------------------------------------------------------------------------

NT_GOLD_STANDARD_A3 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "构造M = A^n - 1，其中A = n·p₁·...·p_k",
            "raw_text_span": "考虑M = (n·p₁·p₂·...·p_k)^n - 1。令A = n·p₁·...·p_k，则M = A^n - 1。",
            "math_objects": [
                {
                    "name": "M的构造",
                    "latex": "M = A^n - 1, \\quad A = n \\cdot p_1 \\cdots p_k",
                    "sympy_expr": "M - A**n + 1",
                    "object_type": "definition",
                    "variables": ["M", "A", "n"],
                    "properties": {"method": "order_based"},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        },
        {
            "type": "RESOLUTION",
            "description": "q | M意味着A^n ≡ 1 (mod q)，即ord_q(A) | n",
            "raw_text_span": "如果q | M，即q | (A^n - 1)，那么A^n ≡ 1 (mod q)。这说明A在模q下的阶ord_q(A)整除n。",
            "math_objects": [
                {
                    "name": "阶整除关系",
                    "latex": "\\text{ord}_q(A) \\mid n",
                    "sympy_expr": "Mod(n, ord_q_A)",
                    "object_type": "equation",
                    "variables": ["ord_q_A", "n"],
                    "properties": {"derived_from": "A^n ≡ 1 mod q"},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        },
        {
            "type": "STALL",
            "description": "ord_q(A) | n不意味着ord_q(A) = n——阶可能是n的真因子",
            "raw_text_span": "ord_q(A) | n不意味着ord_q(A) = n——阶可能是n的真因子。需要排除阶是n的真因子的情形。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.82,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "M = A^n - 1，A = n·p₁·...·p_k",
            "math_objects": ["M的构造"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "resolution",
            "content": "q | M → ord_q(A) | n",
            "math_objects": ["阶整除关系"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "stall",
            "content": "阶可能是n的真因子——需要保证ord_q(A) = n",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.82,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从M = A^n - 1和q|M推出ord_q(A)|n",
        },
        {
            "source_type": "resolution",
            "target_type": "stall",
            "edge_type": "infer",
            "description": "从ord_q(A)|n到阶可能是真因子的卡点",
        }
    ],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "存在无穷多个型命题", "status": "exploring"}
        ],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "in_progress"},
            {"description": "构造使新素因子≡1(mod n)的数", "obligation_type": "prove", "status": "in_progress"},
            {"description": "保证ord_q(A) = n（排除真因子）", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "反证法构造N", "description": "N = n·p₁·...·p_k + 1", "introduced_at_round": 2},
            {"name": "A^n-1构造", "description": "M = A^n - 1, A = n·p₁·...·p_k", "introduced_at_round": 3}
        ],
        "E_t": [],
        "U_t": [
            {"description": "阶可能是n的真因子——需要保证ord_q(A)恰好为n", "severity": "blocking", "identified_at_round": 3}
        ],
    },
    "parse_confidence": 0.86,
    "parse_warnings": ["A^n-1构造的阶不保证恰好为n"],
}


# ---------------------------------------------------------------------------
# A4: 用分圆多项式Φ_n(A)，关键突破——ord_q(A) = n
# 主要事件类型: REPRESENTATION + RESOLUTION(多个) + VERIFICATION
# 前沿节点类型: resolution
# 六元组关键变化: V_t: {"ord_q(A)=n", "q≡1(mod n)"}; R_t: {"分圆多项式Φ_n"}
# ---------------------------------------------------------------------------

NT_GOLD_STANDARD_A4 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "用分圆多项式Φ_n(A)代替A^n-1",
            "raw_text_span": "好提示！分圆多项式Φ_n(x)的根是本原n次单位根。令A = n·p₁·p₂·...·p_k，考虑M = Φ_n(A)。",
            "math_objects": [
                {
                    "name": "分圆多项式构造",
                    "latex": "M = \\Phi_n(A), \\quad A = n \\cdot p_1 \\cdots p_k",
                    "sympy_expr": "Phi_n_A",
                    "object_type": "definition",
                    "variables": ["M", "Phi_n", "A", "n"],
                    "properties": {"cyclotomic": "true"},
                },
                {
                    "name": "分圆多项式性质",
                    "latex": "x^n - 1 = \\prod_{d \\mid n} \\Phi_d(x)",
                    "sympy_expr": "x**n - 1",
                    "object_type": "identity",
                    "variables": ["x", "n"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "q | Φ_n(A)且q∤n → ord_q(A) = n（排除真因子情形）",
            "raw_text_span": "如果ord_q(A) = d < n，那么q | (A^d - 1)。但Φ_n(A)和∏_{e|d} Φ_e(A)互素（q∤n时），矛盾。因此ord_q(A) = n。",
            "math_objects": [
                {
                    "name": "阶恰好为n",
                    "latex": "\\text{ord}_q(A) = n",
                    "sympy_expr": "ord_q_A - n",
                    "object_type": "equation",
                    "variables": ["ord_q_A", "n"],
                    "properties": {"key_breakthrough": "true"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "VERIFICATION",
            "description": "由Fermat小定理A^{q-1}≡1(mod q)和ord_q(A)=n → n | (q-1) → q ≡ 1 (mod n)",
            "raw_text_span": "由Fermat小定理，A^{q-1} ≡ 1 (mod q)，所以ord_q(A) | (q-1)，即n | (q-1)，即q ≡ 1 (mod n)。",
            "math_objects": [
                {
                    "name": "q模n",
                    "latex": "q \\equiv 1 \\pmod{n}",
                    "sympy_expr": "Mod(q, n) - 1",
                    "object_type": "equation",
                    "variables": ["q", "n"],
                    "properties": {"derived_from": "Fermat + ord"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "M = Φ_n(A)，分圆多项式构造",
            "math_objects": ["分圆多项式构造", "分圆多项式性质"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "ord_q(A) = n（分圆多项式排除真因子）",
            "math_objects": ["阶恰好为n"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "q ≡ 1 (mod n)（Fermat小定理 + 阶）",
            "math_objects": ["q模n"],
            "is_frontier": True,
            "confidence": 0.9,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从Φ_n(A)构造推出ord_q(A)=n",
        },
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从ord_q(A)=n和Fermat推出q≡1(mod n)",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "ord_q(A) = n（分圆多项式排除真因子）", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "q ≡ 1 (mod n)（Fermat小定理 + 阶）", "verified_by": "logic", "verified_at_round": 4}
        ],
        "F_t": [],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "in_progress"},
            {"description": "确认Φ_n(A)有素因子且q∤n", "obligation_type": "prove", "status": "open"},
            {"description": "确认q是新的素数（不在p₁,...,p_k中）", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "反证法构造N", "description": "N = n·p₁·...·p_k + 1", "introduced_at_round": 2},
            {"name": "A^n-1构造", "description": "M = A^n - 1", "introduced_at_round": 3},
            {"name": "分圆多项式Φ_n", "description": "M = Φ_n(A)", "introduced_at_round": 4}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.9,
    "parse_warnings": [],
}


# ---------------------------------------------------------------------------
# A5: 确认Φ_n(A) > 1有素因子，q∤n，q是新的
# 主要事件类型: RESOLUTION(多个) + VERIFICATION
# 前沿节点类型: resolution
# 六元组关键变化: V_t: 加入"Φ_n(A)>1有素因子", "q∤A", "q是新的"
# ---------------------------------------------------------------------------

NT_GOLD_STANDARD_A5 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "Φ_n(A) > 1（对A≥2, n≥2），所以有素因子q",
            "raw_text_span": "当n≥2时，A ≥ 2，Φ_n(A) ≥ Φ_n(2) > 1。所以Φ_n(A) > 1，有素因子q。",
            "math_objects": [
                {
                    "name": "M有素因子",
                    "latex": "\\Phi_n(A) > 1 \\Rightarrow \\exists q \\text{ prime}, \\, q \\mid \\Phi_n(A)",
                    "sympy_expr": "Phi_n_A - 1",
                    "object_type": "inequality",
                    "variables": ["Phi_n_A", "q"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        },
        {
            "type": "RESOLUTION",
            "description": "q ∤ A：若q|A则Φ_n(A)≡Φ_n(0)=1(mod q)，矛盾",
            "raw_text_span": "若q | A，则Φ_n(A) ≡ Φ_n(0) (mod q)。对n ≥ 2，Φ_n(0) = 1，矛盾。因此q ∤ A。",
            "math_objects": [
                {
                    "name": "q不整除A",
                    "latex": "q \\nmid A",
                    "sympy_expr": "Mod(A, q)",
                    "object_type": "claim",
                    "variables": ["q", "A"],
                    "properties": {"reason": "Phi_n(0)=1 for n>=2"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "VERIFICATION",
            "description": "q是新的素数：q≠p_i因为q∤A而p_i|A",
            "raw_text_span": "如果q = p_i，那么q | A。但q ∤ A，所以q ≠ p_i，q是新的。",
            "math_objects": [
                {
                    "name": "q是新的素数",
                    "latex": "q \\notin \\{p_1, \\ldots, p_k\\}",
                    "sympy_expr": "q_not_in_p_list",
                    "object_type": "claim",
                    "variables": ["q", "p_1", "p_k"],
                    "properties": {"reason": "q∤A but p_i|A"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "resolution",
            "content": "Φ_n(A) > 1有素因子q",
            "math_objects": ["M有素因子"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "resolution",
            "content": "q ∤ A（Φ_n(0)=1）",
            "math_objects": ["q不整除A"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "q是新的素数（q∤A, p_i|A）",
            "math_objects": ["q是新的素数"],
            "is_frontier": True,
            "confidence": 0.9,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从q∤A推出q是新的素数",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "ord_q(A) = n（分圆多项式排除真因子）", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "q ≡ 1 (mod n)（Fermat小定理 + 阶）", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "Φ_n(A) > 1有素因子q", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q ∤ A（Φ_n(0)=1）", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q是新的素数（q∤A, p_i|A）", "verified_by": "logic", "verified_at_round": 5}
        ],
        "F_t": [],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "in_progress"},
            {"description": "组织完整证明确认逻辑闭环", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "反证法构造N", "description": "N = n·p₁·...·p_k + 1", "introduced_at_round": 2},
            {"name": "A^n-1构造", "description": "M = A^n - 1", "introduced_at_round": 3},
            {"name": "分圆多项式Φ_n", "description": "M = Φ_n(A)", "introduced_at_round": 4}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.9,
    "parse_warnings": [],
}


# ---------------------------------------------------------------------------
# A6: 完整证明，逻辑闭环
# 主要事件类型: RESOLUTION(多个)
# 前沿节点类型: resolution
# 六元组关键变化: V_t: 加入"矛盾→无穷"; O_t: 全部solved
# ---------------------------------------------------------------------------

NT_GOLD_STANDARD_A6 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "n=1时由Euclid定理直接成立",
            "raw_text_span": "n = 1时，所有素数都满足p ≡ 1 (mod 1)，由Euclid定理素数无穷，结论成立。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.95,
        },
        {
            "type": "RESOLUTION",
            "description": "步骤1-2：M=Φ_n(A)>1有素因子q，q∤A",
            "raw_text_span": "步骤1：M > 1。步骤2：q ∤ A（Φ_n(0)=1）。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "步骤3：ord_q(A)=n（分圆多项式排除真因子）",
            "raw_text_span": "步骤3：ord_q(A) = n。由Φ_n(A)|(A^n-1)得A^n≡1(mod q)。若ord=d<n则q|(A^d-1)与Φ_n(A)互素矛盾。",
            "math_objects": [
                {
                    "name": "阶恰好为n（完整）",
                    "latex": "\\text{ord}_q(A) = n",
                    "sympy_expr": "ord_q_A - n",
                    "object_type": "equation",
                    "variables": ["ord_q_A", "n"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "步骤4：n|(q-1) → q≡1(mod n)，矛盾→无穷",
            "raw_text_span": "步骤4：n | (q-1)，所以q ≡ 1 (mod n)。矛盾：q是新的满足q≡1(mod n)的素数。",
            "math_objects": [
                {
                    "name": "最终结论",
                    "latex": "|\\{p \\text{ prime} : p \\equiv 1 \\pmod{n}\\}| = \\infty",
                    "sympy_expr": "infinite_primes",
                    "object_type": "claim",
                    "variables": ["n", "p"],
                    "properties": {"is_final_result": "true"},
                }
            ],
            "depends_on": [],
            "confidence": 0.95,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "resolution",
            "content": "n=1平凡情况",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.95,
        },
        {
            "type": "resolution",
            "content": "步骤1-2：M有素因子q，q∤A",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "步骤3：ord_q(A)=n",
            "math_objects": ["阶恰好为n（完整）"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "步骤4：q≡1(mod n)，矛盾→无穷 ✓ 证毕",
            "math_objects": ["最终结论"],
            "is_frontier": True,
            "confidence": 0.95,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从步骤1-2到步骤3（ord_q(A)=n）",
        },
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从步骤3到步骤4（q≡1(mod n)→矛盾）",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "ord_q(A) = n（分圆多项式排除真因子）", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "q ≡ 1 (mod n)（Fermat小定理 + 阶）", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "Φ_n(A) > 1有素因子q", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q ∤ A（Φ_n(0)=1）", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q是新的素数（q∤A, p_i|A）", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "矛盾→存在无穷多个p≡1(mod n)", "verified_by": "logic", "verified_at_round": 6}
        ],
        "F_t": [],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "solved"},
            {"description": "构造使新素因子≡1(mod n)的数", "obligation_type": "prove", "status": "solved"},
            {"description": "保证ord_q(A) = n", "obligation_type": "prove", "status": "solved"},
            {"description": "确认Φ_n(A)有素因子且q∤n", "obligation_type": "prove", "status": "solved"},
            {"description": "确认q是新的素数", "obligation_type": "prove", "status": "solved"},
            {"description": "组织完整证明确认逻辑闭环", "obligation_type": "prove", "status": "solved"}
        ],
        "R_t": [
            {"name": "反证法构造N", "description": "N = n·p₁·...·p_k + 1", "introduced_at_round": 2},
            {"name": "A^n-1构造", "description": "M = A^n - 1", "introduced_at_round": 3},
            {"name": "分圆多项式Φ_n", "description": "M = Φ_n(A)", "introduced_at_round": 4}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.93,
    "parse_warnings": [],
}


NT_GOLD_STANDARDS = [
    NT_GOLD_STANDARD_A1,
    NT_GOLD_STANDARD_A2,
    NT_GOLD_STANDARD_A3,
    NT_GOLD_STANDARD_A4,
    NT_GOLD_STANDARD_A5,
    NT_GOLD_STANDARD_A6,
]


# ===========================================================================
# 案例2：组合/概率题 Gold Standard
# ===========================================================================

# ---------------------------------------------------------------------------
# A1: 读题，识别为博弈/策略优化问题，列出方向
# 主要事件类型: OBSERVATION + CANDIDATE(多个)
# 前沿节点类型: candidate
# 六元组关键变化: F_t: {"博弈/策略优化问题", "候选方向"}
# ---------------------------------------------------------------------------

CB_GOLD_STANDARD_A1 = {
    "semantic_events": [
        {
            "type": "OBSERVATION",
            "description": "识别为博弈/策略优化问题——设计策略最大化成功概率",
            "raw_text_span": "这是一个博弈/策略优化问题——设计策略最大化某个概率事件。",
            "math_objects": [
                {
                    "name": "成功条件",
                    "latex": "\\text{success} \\iff (\\exists i: \\text{guess}_i = c_i) \\wedge (\\forall i: \\text{guess}_i \\neq \\bar{c}_i)",
                    "sympy_expr": "success_condition",
                    "object_type": "definition",
                    "variables": ["c_i", "guess_i"],
                    "properties": {"type": "strategy_optimization"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "CANDIDATE",
            "description": "先看简单情况——n小、k小（如k=2二色）",
            "raw_text_span": "先看简单情况——n小、k小（如k=2二色）",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "信息论视角——每人看到的信息能否推断自己的",
            "raw_text_span": "信息论视角——每人看到的信息能否推断出自己的",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "编码理论——帽子向量是k^n空间中的点，策略是解码",
            "raw_text_span": "编码理论——帽子颜色向量是k^n空间中的一个点，策略是某种\"解码\"",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "OBSERVATION",
            "description": "直觉：全员猜成功率(1/k)^n极低，需平衡——少数猜多数pass",
            "raw_text_span": "如果所有人都猜，每人猜对概率1/k，但只要一人错就失败，成功率(1/k)^n极低。所以需要平衡。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.85,
        },
    ],
    "trajectory_nodes": [
        {
            "type": "observation",
            "content": "博弈/策略优化问题：最大化成功概率",
            "math_objects": ["成功条件"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "candidate",
            "content": "简单情况k=2",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "信息论视角",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "编码理论视角",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "observation",
            "content": "直觉：少数猜多数pass",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.85,
        },
    ],
    "trajectory_edges": [],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "博弈/策略优化问题：最大化成功概率", "status": "exploring"},
            {"statement": "候选方向：简单情况、信息论、编码理论", "status": "exploring"}
        ],
        "O_t": [
            {"description": "求最优策略及成功概率", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.88,
    "parse_warnings": [],
}


# ---------------------------------------------------------------------------
# A2: k=2分析，约定S的奇偶性，得到1/2，卡点
# 主要事件类型: REPRESENTATION + RESOLUTION + STALL
# 前沿节点类型: stall
# 六元组关键变化: R_t: {"奇偶性策略"}; U_t: {"1/2是否最优"}
# ---------------------------------------------------------------------------

CB_GOLD_STANDARD_A2 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "k=2：令S = c_1+...+c_n (mod 2)，约定S=s，每人推断c_i = s - S_{-i}",
            "raw_text_span": "令帽子颜色c_i ∈ {0, 1}，总和S = c_1 + ... + c_n (mod 2)。约定S的猜测值s。第i个人能算出S_{-i}，如果知道S就能推断c_i = S - S_{-i}。",
            "math_objects": [
                {
                    "name": "奇偶性定义",
                    "latex": "S = \\sum_{i=1}^n c_i \\pmod{2}",
                    "sympy_expr": "S_val % 2",
                    "object_type": "definition",
                    "variables": ["S", "c_i", "n"],
                    "properties": {"modulus": 2},
                },
                {
                    "name": "推断公式",
                    "latex": "c_i = s - S_{-i} \\pmod{2}",
                    "sympy_expr": "Mod(s - S_minus_i, 2)",
                    "object_type": "equation",
                    "variables": ["c_i", "s", "S_minus_i"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        },
        {
            "type": "RESOLUTION",
            "description": "全员猜策略：S=s时全对（成功），S≠s时全错（失败），成功率1/2",
            "raw_text_span": "当S确实=0时，所有人都猜对 → 成功。当S=1时，所有人都猜错 → 失败。成功率 = P(S=0) = 1/2。",
            "math_objects": [
                {
                    "name": "成功率1/2",
                    "latex": "P(\\text{success}) = \\frac{1}{2}",
                    "sympy_expr": "Rational(1,2)",
                    "object_type": "equation",
                    "variables": [],
                    "properties": {"strategy": "all_guess"},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        },
        {
            "type": "RESOLUTION",
            "description": "一人猜策略：也得到成功率1/2",
            "raw_text_span": "如果只让一个人猜（假设S=0），他猜对概率1/2，其余人pass。成功率 = 1/2。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "STALL",
            "description": "1/2似乎不是最优——n个人应该提供更多信息",
            "raw_text_span": "1/2似乎不是最优。能否更好？n个人应该提供更多信息。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "S = Σc_i (mod 2)，约定S=s",
            "math_objects": ["奇偶性定义", "推断公式"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "resolution",
            "content": "全员猜策略成功率1/2",
            "math_objects": ["成功率1/2"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "resolution",
            "content": "一人猜策略也1/2",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "stall",
            "content": "1/2是否最优——n个人应提供更多信息",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.8,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从奇偶性策略推出成功率1/2",
        }
    ],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "博弈/策略优化问题", "status": "exploring"}
        ],
        "O_t": [
            {"description": "求最优策略及成功概率", "obligation_type": "prove", "status": "in_progress"},
            {"description": "k=2时能否超过1/2", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "奇偶性策略", "description": "S=Σc_i mod 2, 约定S=s", "introduced_at_round": 2}
        ],
        "E_t": [],
        "U_t": [
            {"description": "1/2是否最优——n个人应提供更多信息", "severity": "blocking", "identified_at_round": 2}
        ],
    },
    "parse_confidence": 0.85,
    "parse_warnings": [],
}


# ---------------------------------------------------------------------------
# A3: Hamming码思路，n=2^m-1，卡点（逻辑绕）
# 主要事件类型: REPRESENTATION + CANDIDATE + STALL
# 前沿节点类型: stall
# 六元组关键变化: R_t: {"Hamming码框架"}; U_t: {"策略逻辑需要理清"}
# ---------------------------------------------------------------------------

CB_GOLD_STANDARD_A3 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "把帽子向量c∈{0,1}^n看作2^n个状态，策略=每人函数f_i:{0,1}^{n-1}→{0,1,pass}",
            "raw_text_span": "把帽子向量c = (c_1,...,c_n) ∈ {0,1}^n看作k^n = 2^n个可能状态之一。策略 = 每人一个函数f_i: {0,1}^{n-1} → {0,1,pass}。",
            "math_objects": [
                {
                    "name": "策略函数",
                    "latex": "f_i: \\{0,1\\}^{n-1} \\to \\{0, 1, \\text{pass}\\}",
                    "sympy_expr": "f_i",
                    "object_type": "definition",
                    "variables": ["f_i", "c"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "CANDIDATE",
            "description": "Hamming码思路：n=2^m-1时完美码，覆盖半径1",
            "raw_text_span": "Hamming码[2^m-1, 2^m-1-m, 3]是完美码，覆盖半径1。{0,1}^n可以被划分为2^m个球，每球以码字为中心，半径1。",
            "math_objects": [
                {
                    "name": "Hamming码性质",
                    "latex": "\\{0,1\\}^n = \\bigsqcup_{w \\in C} B(w, 1)",
                    "sympy_expr": "perfect_covering",
                    "object_type": "claim",
                    "variables": ["C", "n"],
                    "properties": {"n": "2^m - 1", "covering_radius": 1},
                }
            ],
            "depends_on": [],
            "confidence": 0.82,
        },
        {
            "type": "STALL",
            "description": "策略逻辑绕——需要理清什么时候人猜、什么时候pass、猜什么",
            "raw_text_span": "逻辑有点绕。需要理清：什么时候人猜，什么时候pass，猜什么。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.78,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "策略函数f_i: {0,1}^{n-1} → {0,1,pass}",
            "math_objects": ["策略函数"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "candidate",
            "content": "Hamming码思路（n=2^m-1完美码）",
            "math_objects": ["Hamming码性质"],
            "is_frontier": False,
            "confidence": 0.82,
        },
        {
            "type": "stall",
            "content": "策略逻辑需要理清——猜/pass条件不明确",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.78,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "candidate",
            "edge_type": "infer",
            "description": "从策略函数框架到Hamming码候选",
        }
    ],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "博弈/策略优化问题", "status": "exploring"},
            {"statement": "Hamming码思路：n=2^m-1完美码", "status": "exploring"}
        ],
        "O_t": [
            {"description": "求最优策略及成功概率", "obligation_type": "prove", "status": "in_progress"},
            {"description": "理清Hamming码策略的猜/pass逻辑", "obligation_type": "prove", "status": "in_progress"}
        ],
        "R_t": [
            {"name": "奇偶性策略", "description": "S=Σc_i mod 2", "introduced_at_round": 2},
            {"name": "Hamming码框架", "description": "c∈{0,1}^n, 码字集合C", "introduced_at_round": 3}
        ],
        "E_t": [],
        "U_t": [
            {"description": "Hamming码策略逻辑需要理清", "severity": "blocking", "identified_at_round": 3}
        ],
    },
    "parse_confidence": 0.82,
    "parse_warnings": ["Hamming码策略逻辑尚未理清"],
}


# ---------------------------------------------------------------------------
# A4: 理清Hamming码策略，得到1/(n+1)，发现方向反了
# 主要事件类型: RESOLUTION(多个) + STALL
# 前沿节点类型: stall
# 六元组关键变化: V_t: {"码字时全猜对/非码字时一人猜错"}; U_t: {"1/(n+1)比1/2差，方向反了"}
# ---------------------------------------------------------------------------

CB_GOLD_STANDARD_A4 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "c∈C时所有人都猜且猜对（每人翻转自己得非码字，猜真实值）",
            "raw_text_span": "当c ∈ C时：v^{c_i} = c ∈ C（猜对方向），v^{1-c_i} = c' ∉ C。所以人i会猜c_i = c_i——猜对！",
            "math_objects": [
                {
                    "name": "码字情况",
                    "latex": "c \\in C \\Rightarrow \\forall i: \\text{guess}_i = c_i \\text{ (correct)}",
                    "sympy_expr": "c_in_C_all_correct",
                    "object_type": "claim",
                    "variables": ["c", "C"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "RESOLUTION",
            "description": "c∉C时人j猜错（差异位），其余pass → 失败",
            "raw_text_span": "当c ∉ C时，c与码字w距离1，差异位j。人j猜错，其余pass → 失败。",
            "math_objects": [
                {
                    "name": "非码字情况",
                    "latex": "c \\notin C \\Rightarrow \\text{person } j \\text{ guesses wrong}",
                    "sympy_expr": "c_not_in_C_j_wrong",
                    "object_type": "claim",
                    "variables": ["c", "C", "j"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "RESOLUTION",
            "description": "成功率 = P(c∈C) = |C|/2^n = 1/(n+1)",
            "raw_text_span": "成功率 = P(c ∈ C) = |C| / 2^n = 2^{n-m} / 2^n = 1/2^m = 1/(n+1)。",
            "math_objects": [
                {
                    "name": "成功率1/(n+1)",
                    "latex": "P(\\text{success}) = \\frac{1}{n+1}",
                    "sympy_expr": "1/(n+1)",
                    "object_type": "equation",
                    "variables": ["n"],
                    "properties": {"strategy": "hamming_wrong_direction"},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "STALL",
            "description": "1/(n+1)比1/2还差——方向反了，应该让码字情况pass",
            "raw_text_span": "1/(n+1)比1/2还差！方向反了。应该反过来——让码字情况pass，非码字情况猜。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.82,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "resolution",
            "content": "c∈C时全猜对",
            "math_objects": ["码字情况"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "resolution",
            "content": "c∉C时人j猜错→失败",
            "math_objects": ["非码字情况"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "resolution",
            "content": "成功率1/(n+1)",
            "math_objects": ["成功率1/(n+1)"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "stall",
            "content": "1/(n+1)比1/2差——方向反了",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.82,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从码字/非码字情况推出成功率1/(n+1)",
        },
        {
            "source_type": "resolution",
            "target_type": "stall",
            "edge_type": "infer",
            "description": "从1/(n+1)比1/2差到方向反了的卡点",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "c∈C时全猜对，c∉C时人j猜错", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "Hamming码策略成功率1/(n+1)", "verified_by": "logic", "verified_at_round": 4}
        ],
        "F_t": [],
        "O_t": [
            {"description": "求最优策略及成功概率", "obligation_type": "prove", "status": "in_progress"},
            {"description": "反转Hamming码策略——码字pass非码字猜", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "奇偶性策略", "description": "S=Σc_i mod 2", "introduced_at_round": 2},
            {"name": "Hamming码框架", "description": "c∈{0,1}^n, 码字集合C", "introduced_at_round": 3}
        ],
        "E_t": [],
        "U_t": [
            {"description": "1/(n+1)比1/2差——Hamming码方向反了，需要反转策略", "severity": "blocking", "identified_at_round": 4}
        ],
    },
    "parse_confidence": 0.83,
    "parse_warnings": ["Hamming码策略方向反了"],
}


# ---------------------------------------------------------------------------
# A5: 尝试反转策略，多次尝试逻辑仍绕，卡点
# 主要事件类型: TEST(多个) + STALL
# 前沿节点类型: stall
# 六元组关键变化: U_t: {"Hamming码策略需要更精巧设计"}
# ---------------------------------------------------------------------------

CB_GOLD_STANDARD_A5 = {
    "semantic_events": [
        {
            "type": "TEST",
            "description": "尝试反转策略1：码字时pass，非码字时猜真实值",
            "raw_text_span": "新策略（每人i）：如果v⁰∈C且v¹∉C，猜c_i=1。分析c∉C时人j猜对，c∈C时人i猜错。还是不对。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.75,
        },
        {
            "type": "TEST",
            "description": "尝试反转策略2：翻转自己得码字时pass，否则猜",
            "raw_text_span": "人i看到c_{-i}，如果v⁰∈C或v¹∈C则pass，否则猜。分析c∈C时全pass（失败），c∉C时人i≠j猜但不保证对。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.75,
        },
        {
            "type": "STALL",
            "description": "Hamming码思路需要更精巧的策略设计——多次尝试未成功",
            "raw_text_span": "Hamming码思路需要更精巧的策略设计。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.78,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "operation",
            "content": "尝试反转策略1：码字pass非码字猜",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.75,
        },
        {
            "type": "operation",
            "content": "尝试反转策略2：翻转得码字则pass",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.75,
        },
        {
            "type": "stall",
            "content": "Hamming码策略需要更精巧设计——多次尝试未成功",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.78,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "operation",
            "target_type": "operation",
            "edge_type": "infer",
            "description": "从反转策略1失败到尝试反转策略2",
        },
        {
            "source_type": "operation",
            "target_type": "stall",
            "edge_type": "infer",
            "description": "从反转策略2失败到卡点",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "c∈C时全猜对，c∉C时人j猜错", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "Hamming码策略成功率1/(n+1)", "verified_by": "logic", "verified_at_round": 4}
        ],
        "F_t": [],
        "O_t": [
            {"description": "求最优策略及成功概率", "obligation_type": "prove", "status": "in_progress"},
            {"description": "设计正确的Hamming码策略", "obligation_type": "prove", "status": "in_progress"}
        ],
        "R_t": [
            {"name": "奇偶性策略", "description": "S=Σc_i mod 2", "introduced_at_round": 2},
            {"name": "Hamming码框架", "description": "c∈{0,1}^n, 码字集合C", "introduced_at_round": 3}
        ],
        "E_t": [],
        "U_t": [
            {"description": "Hamming码策略需要更精巧设计——多次尝试未成功", "severity": "blocking", "identified_at_round": 5}
        ],
    },
    "parse_confidence": 0.78,
    "parse_warnings": ["Hamming码策略设计遇到困难，需要回到本质"],
}


# ---------------------------------------------------------------------------
# A6: 回到本质，奇偶性策略+部分pass，推广k色，结论1/k
# 主要事件类型: RESOLUTION(多个) + VERIFICATION
# 前沿节点类型: resolution
# 六元组关键变化: V_t: 加入"成功率1/k", "上界1/k"; O_t: 全部solved
# ---------------------------------------------------------------------------

CB_GOLD_STANDARD_A6 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "k=2正确策略：约定S=s，S_{-i}=s时猜c_i=0否则pass，成功率1/2",
            "raw_text_span": "策略：约定S = s。人i看到S_{-i}：如果S_{-i} = s，猜c_i = 0；否则pass。S=s时c_i=0的人猜对，c_i=1的人pass→成功。S≠s时c_i=1的人猜错→失败。成功率=1/2。",
            "math_objects": [
                {
                    "name": "k=2最优策略",
                    "latex": "P(\\text{success}) = \\frac{1}{2}",
                    "sympy_expr": "Rational(1,2)",
                    "object_type": "equation",
                    "variables": [],
                    "properties": {"strategy": "partial_pass"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "推广k色：S=Σc_i(mod k)，约定S=s，S_{-i}=s时猜c_i=0否则pass",
            "raw_text_span": "k色时，S = c_1 + ... + c_n (mod k)。约定S = s。人i看到S_{-i}：如果s - S_{-i} ≡ 0 (mod k)即S_{-i}=s，猜c_i=0；否则pass。",
            "math_objects": [
                {
                    "name": "k色推广",
                    "latex": "S = \\sum c_i \\pmod{k}, \\quad \\text{guess } c_i = 0 \\text{ if } S_{-i} = s",
                    "sympy_expr": "S_val % k",
                    "object_type": "definition",
                    "variables": ["S", "c_i", "k", "s"],
                    "properties": {"modulus": "k"},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        },
        {
            "type": "RESOLUTION",
            "description": "成功率 = P(S=s) - P(S=s, ∀i c_i≠0) → 1/k（n→∞）",
            "raw_text_span": "成功率 = P(S = s) - P(S = s, ∀i c_i ≠ 0)。P(S = s) = 1/k。当n → ∞时，P(∀i c_i≠0) → 0，成功率 → 1/k。",
            "math_objects": [
                {
                    "name": "k色成功率",
                    "latex": "P(\\text{success}) = \\frac{1}{k} - P(S=s, \\forall i: c_i \\ne 0) \\to \\frac{1}{k}",
                    "sympy_expr": "1/k",
                    "object_type": "equation",
                    "variables": ["k", "n"],
                    "properties": {"asymptotic": "true"},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        },
        {
            "type": "VERIFICATION",
            "description": "上界论证：由信息论，每人缺少1个信息，成功率上界=1/k",
            "raw_text_span": "上界论证：对任意策略，由对称性和信息论论证（每人只看到n-1个帽子，缺少1个信息），成功率上界 = 1/k。",
            "math_objects": [
                {
                    "name": "成功率上界",
                    "latex": "P(\\text{success}) \\le \\frac{1}{k}",
                    "sympy_expr": "1/k",
                    "object_type": "inequality",
                    "variables": ["k"],
                    "properties": {"method": "information_theory"},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "resolution",
            "content": "k=2最优策略成功率1/2",
            "math_objects": ["k=2最优策略"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "推广k色：S mod k策略",
            "math_objects": ["k色推广"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "resolution",
            "content": "成功率→1/k（渐近）",
            "math_objects": ["k色成功率"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "resolution",
            "content": "上界1/k（信息论）→最优 ✓ 证毕",
            "math_objects": ["成功率上界"],
            "is_frontier": True,
            "confidence": 0.85,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从k=2策略推广到k色",
        },
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从k色成功率和上界推出最优",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "c∈C时全猜对，c∉C时人j猜错", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "Hamming码策略成功率1/(n+1)", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "k=2最优策略成功率1/2", "verified_by": "logic", "verified_at_round": 6},
            {"statement": "k色策略成功率→1/k", "verified_by": "logic", "verified_at_round": 6},
            {"statement": "成功率上界1/k（信息论）", "verified_by": "logic", "verified_at_round": 6}
        ],
        "F_t": [],
        "O_t": [
            {"description": "求最优策略及成功概率", "obligation_type": "prove", "status": "solved"},
            {"description": "k=2时能否超过1/2", "obligation_type": "prove", "status": "solved"},
            {"description": "设计正确的策略", "obligation_type": "prove", "status": "solved"},
            {"description": "推广到k色", "obligation_type": "prove", "status": "solved"},
            {"description": "证明最优性（上界）", "obligation_type": "prove", "status": "solved"}
        ],
        "R_t": [
            {"name": "奇偶性策略", "description": "S=Σc_i mod 2", "introduced_at_round": 2},
            {"name": "Hamming码框架", "description": "c∈{0,1}^n, 码字集合C", "introduced_at_round": 3},
            {"name": "k色模策略", "description": "S=Σc_i mod k, 约定S=s", "introduced_at_round": 6}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.88,
    "parse_warnings": ["上界1/k的严格证明用了信息论论证，细节略简"],
}


CB_GOLD_STANDARDS = [
    CB_GOLD_STANDARD_A1,
    CB_GOLD_STANDARD_A2,
    CB_GOLD_STANDARD_A3,
    CB_GOLD_STANDARD_A4,
    CB_GOLD_STANDARD_A5,
    CB_GOLD_STANDARD_A6,
]


# ===========================================================================
# 接口函数
# ===========================================================================

def get_nt_gold_standard(round_index: int) -> dict:
    """获取数论案例指定轮次的Gold Standard（1-6）"""
    idx = round_index - 1
    if idx < 0 or idx >= len(NT_GOLD_STANDARDS):
        raise ValueError(f"数论案例轮次{round_index}超出范围(1-{len(NT_GOLD_STANDARDS)})")
    return NT_GOLD_STANDARDS[idx]


def get_cb_gold_standard(round_index: int) -> dict:
    """获取组合/概率案例指定轮次的Gold Standard（1-6）"""
    idx = round_index - 1
    if idx < 0 or idx >= len(CB_GOLD_STANDARDS):
        raise ValueError(f"组合案例轮次{round_index}超出范围(1-{len(CB_GOLD_STANDARDS)})")
    return CB_GOLD_STANDARDS[idx]
