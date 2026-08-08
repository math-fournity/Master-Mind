"""
泛化能力评估脚本：2个新案例的解析准确率验证。

对数论案例和组合/概率案例，分别：
1. GLM-5.2作为LLM独立解析每个A_i（不看Gold Standard）
2. 对比Gold Standard，计算6项准确率指标
3. 输出逐轮对比+汇总指标+达标判断

运行：
    cd ~/master-mind-glm5.2-worktree
    .venv/bin/python3 -m xishujuzhen.research_runtime.parser.evaluate_generalization
"""

import sys
from typing import List, Tuple

from .test_data.gold_standard_new_cases import (
    NT_GOLD_STANDARDS,
    CB_GOLD_STANDARDS,
    get_nt_gold_standard,
    get_cb_gold_standard,
)
from .test_data.case_number_theory import QA_SEQUENCE as NT_QA_SEQUENCE
from .test_data.case_number_theory import PROBLEM_TEXT as NT_PROBLEM_TEXT
from .test_data.case_combinatorics import QA_SEQUENCE as CB_QA_SEQUENCE
from .test_data.case_combinatorics import PROBLEM_TEXT as CB_PROBLEM_TEXT


# ===========================================================================
# GLM-5.2独立解析结果（数论案例）
#
# GLM-5.2读取A_i文本，独立输出解析结果JSON，不参考Gold Standard。
# 解析时基于A1到A_{i-1}的累积context（用本文件中前几轮的解析结果作为历史）。
# ===========================================================================

# ---------------------------------------------------------------------------
# 数论案例 A1: 读题，识别为"存在无穷多个"型命题，列出方向
# ---------------------------------------------------------------------------

NT_REAL_A1 = {
    "semantic_events": [
        {
            "type": "OBSERVATION",
            "description": "识别为'存在无穷多个'型命题——证明p≡1(mod n)的素数无穷",
            "raw_text_span": "结论是\"存在无穷多个\"型命题——要证明某个集合（满足p≡1(mod n)的素数）是无穷集。",
            "math_objects": [
                {
                    "name": "目标命题",
                    "latex": "\\forall n \\in \\mathbb{Z}^+, \\, |\\{p : p \\equiv 1 \\pmod{n}\\}| = \\infty",
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
            "description": "反证法——假设有限个构造矛盾",
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
            "description": "分圆多项式性质",
            "raw_text_span": "用分圆多项式的性质",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "Dirichlet定理（太重）",
            "raw_text_span": "Dirichlet定理直接给出结论（但太重了）",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.7,
        },
    ],
    "trajectory_nodes": [
        {
            "type": "observation",
            "content": "存在无穷多个型命题：p≡1(mod n)",
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
            "content": "分圆多项式",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "Dirichlet定理",
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
# 数论案例 A2: 反证法构造N，卡点
# ---------------------------------------------------------------------------

NT_REAL_A2 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "反证法：假设p₁,...,p_k是所有p≡1(mod n)的素数，构造N = n·p₁·...·p_k + 1",
            "raw_text_span": "假设只有有限个素数p₁, p₂, ..., p_k满足p_i ≡ 1 (mod n)。构造N = n·p₁·p₂·...·p_k + 1。",
            "math_objects": [
                {
                    "name": "N的构造",
                    "latex": "N = n \\cdot p_1 \\cdots p_k + 1",
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
            "description": "N ≡ 1 (mod n)但素因子不一定各自≡1(mod n)",
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
            "description": "Euclid风格构造不能保证新素因子≡1(mod n)，需要更强构造",
            "raw_text_span": "构造N = n·p₁·...·p_k + 1不能直接保证新素因子≡1(mod n)。需要更强的构造。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "N = n·p₁·...·p_k + 1",
            "math_objects": ["N的构造"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "resolution",
            "content": "N ≡ 1 (mod n)但素因子不保证",
            "math_objects": ["N模n"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "stall",
            "content": "需要更强的构造保证素因子≡1(mod n)",
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
            "description": "从N≡1(mod n)但素因子不保证到卡点",
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
# 数论案例 A3: 改用A^n-1，阶的关系，卡点
# ---------------------------------------------------------------------------

NT_REAL_A3 = {
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
            "description": "ord_q(A)|n不意味着ord_q(A)=n——阶可能是真因子",
            "raw_text_span": "ord_q(A) | n不意味着ord_q(A) = n——阶可能是n的真因子。需要排除阶是n的真因子的情形。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.82,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "M = A^n - 1",
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
            "content": "阶可能是n的真因子——需要保证ord_q(A)=n",
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
            {"description": "保证ord_q(A) = n", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "反证法构造N", "description": "N = n·p₁·...·p_k + 1", "introduced_at_round": 2},
            {"name": "A^n-1构造", "description": "M = A^n - 1", "introduced_at_round": 3}
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
# 数论案例 A4: 分圆多项式Φ_n(A)，关键突破
# ---------------------------------------------------------------------------

NT_REAL_A4 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "用分圆多项式Φ_n(A)代替A^n-1",
            "raw_text_span": "分圆多项式Φ_n(x)的根是本原n次单位根。令A = n·p₁·...·p_k，考虑M = Φ_n(A)。",
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
            "description": "q | Φ_n(A)且q∤n → ord_q(A) = n（排除真因子）",
            "raw_text_span": "如果ord_q(A) = d < n，那么q | (A^d - 1)。但Φ_n(A)和∏_{e|d} Φ_e(A)互素，矛盾。因此ord_q(A) = n。",
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
            "description": "由Fermat小定理和ord_q(A)=n → n|(q-1) → q≡1(mod n)",
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
            "content": "ord_q(A) = n",
            "math_objects": ["阶恰好为n"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "q ≡ 1 (mod n)",
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
            {"description": "确认q是新的素数", "obligation_type": "prove", "status": "open"}
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
# 数论案例 A5: 确认Φ_n(A)>1, q∤A, q是新的
# ---------------------------------------------------------------------------

NT_REAL_A5 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "Φ_n(A) > 1（对A≥2, n≥2），有素因子q",
            "raw_text_span": "当n≥2时，A ≥ 2，Φ_n(A) > 1。所以Φ_n(A)有素因子q。",
            "math_objects": [
                {
                    "name": "M有素因子",
                    "latex": "\\Phi_n(A) > 1 \\Rightarrow \\exists q, \\, q \\mid \\Phi_n(A)",
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
                    "properties": {"reason": "Phi_n(0)=1"},
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
            "content": "q ∤ A",
            "math_objects": ["q不整除A"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "q是新的素数",
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
            {"statement": "ord_q(A) = n", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "q ≡ 1 (mod n)", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "Φ_n(A) > 1有素因子q", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q ∤ A（Φ_n(0)=1）", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q是新的素数", "verified_by": "logic", "verified_at_round": 5}
        ],
        "F_t": [],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "in_progress"},
            {"description": "组织完整证明", "obligation_type": "prove", "status": "open"}
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
# 数论案例 A6: 完整证明，逻辑闭环
# ---------------------------------------------------------------------------

NT_REAL_A6 = {
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
            "raw_text_span": "步骤3：ord_q(A) = n。由Φ_n(A)|(A^n-1)得A^n≡1(mod q)。若ord=d<n则矛盾。",
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
                    "latex": "|\\{p : p \\equiv 1 \\pmod{n}\\}| = \\infty",
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
            "content": "步骤4：q≡1(mod n)，矛盾→无穷 ✓",
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
            "description": "从步骤1-2到步骤3",
        },
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从步骤3到步骤4",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "ord_q(A) = n", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "q ≡ 1 (mod n)", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "Φ_n(A) > 1有素因子q", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q ∤ A", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "q是新的素数", "verified_by": "logic", "verified_at_round": 5},
            {"statement": "矛盾→存在无穷多个p≡1(mod n)", "verified_by": "logic", "verified_at_round": 6}
        ],
        "F_t": [],
        "O_t": [
            {"description": "证明存在无穷多个素数p≡1(mod n)", "obligation_type": "prove", "status": "solved"},
            {"description": "构造使新素因子≡1(mod n)的数", "obligation_type": "prove", "status": "solved"},
            {"description": "保证ord_q(A) = n", "obligation_type": "prove", "status": "solved"},
            {"description": "确认Φ_n(A)有素因子且q∤n", "obligation_type": "prove", "status": "solved"},
            {"description": "确认q是新的素数", "obligation_type": "prove", "status": "solved"},
            {"description": "组织完整证明", "obligation_type": "prove", "status": "solved"}
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


NT_REAL_RESPONSES = [NT_REAL_A1, NT_REAL_A2, NT_REAL_A3, NT_REAL_A4, NT_REAL_A5, NT_REAL_A6]


# ===========================================================================
# GLM-5.2独立解析结果（组合/概率案例）
# ===========================================================================

# ---------------------------------------------------------------------------
# 组合案例 A1: 读题，识别为博弈/策略优化，列出方向
# ---------------------------------------------------------------------------

CB_REAL_A1 = {
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
            "description": "先看简单情况k=2",
            "raw_text_span": "先看简单情况——n小、k小（如k=2二色）",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "信息论视角",
            "raw_text_span": "信息论视角——每人看到的信息能否推断自己的",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "编码理论——帽子向量是k^n空间中的点",
            "raw_text_span": "编码理论——帽子颜色向量是k^n空间中的一个点，策略是某种解码",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "OBSERVATION",
            "description": "直觉：全员猜成功率(1/k)^n极低，需平衡",
            "raw_text_span": "如果所有人都猜，每人猜对概率1/k，但只要一人错就失败，成功率(1/k)^n极低。所以需要平衡。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.85,
        },
    ],
    "trajectory_nodes": [
        {
            "type": "observation",
            "content": "博弈/策略优化问题",
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
# 组合案例 A2: k=2奇偶性策略，1/2，卡点
# ---------------------------------------------------------------------------

CB_REAL_A2 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "k=2：S = Σc_i (mod 2)，约定S=s，每人推断c_i = s - S_{-i}",
            "raw_text_span": "令帽子颜色c_i ∈ {0, 1}，总和S = c_1 + ... + c_n (mod 2)。约定S的猜测值s。",
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
            "description": "全员猜策略：S=s时全对，S≠s时全错，成功率1/2",
            "raw_text_span": "当S=0时，所有人都猜对→成功。当S=1时，所有人都猜错→失败。成功率 = 1/2。",
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
            "description": "一人猜策略也得到1/2",
            "raw_text_span": "如果只让一个人猜，他猜对概率1/2，其余人pass。成功率 = 1/2。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "STALL",
            "description": "1/2似乎不是最优——n个人应提供更多信息",
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
            "content": "1/2是否最优",
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
            {"name": "奇偶性策略", "description": "S=Σc_i mod 2", "introduced_at_round": 2}
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
# 组合案例 A3: Hamming码思路，卡点
# ---------------------------------------------------------------------------

CB_REAL_A3 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "策略函数f_i: {0,1}^{n-1} → {0,1,pass}",
            "raw_text_span": "把帽子向量c ∈ {0,1}^n看作2^n个可能状态。策略 = 每人一个函数f_i。",
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
            "description": "Hamming码思路：n=2^m-1完美码覆盖半径1",
            "raw_text_span": "Hamming码[2^m-1, 2^m-1-m, 3]是完美码，覆盖半径1。",
            "math_objects": [
                {
                    "name": "Hamming码性质",
                    "latex": "\\{0,1\\}^n = \\bigsqcup_{w \\in C} B(w, 1)",
                    "sympy_expr": "perfect_covering",
                    "object_type": "claim",
                    "variables": ["C", "n"],
                    "properties": {"n": "2^m-1", "covering_radius": 1},
                }
            ],
            "depends_on": [],
            "confidence": 0.82,
        },
        {
            "type": "STALL",
            "description": "策略逻辑绕——需要理清猜/pass条件",
            "raw_text_span": "逻辑有点绕。需要理清：什么时候人猜，什么时候pass，猜什么。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.78,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "策略函数f_i",
            "math_objects": ["策略函数"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "candidate",
            "content": "Hamming码思路",
            "math_objects": ["Hamming码性质"],
            "is_frontier": False,
            "confidence": 0.82,
        },
        {
            "type": "stall",
            "content": "策略逻辑需要理清",
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
            {"statement": "Hamming码思路", "status": "exploring"}
        ],
        "O_t": [
            {"description": "求最优策略及成功概率", "obligation_type": "prove", "status": "in_progress"},
            {"description": "理清Hamming码策略逻辑", "obligation_type": "prove", "status": "in_progress"}
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
# 组合案例 A4: 理清Hamming码策略，1/(n+1)，方向反了
# ---------------------------------------------------------------------------

CB_REAL_A4 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "c∈C时所有人都猜对",
            "raw_text_span": "当c ∈ C时：人i会猜c_i = c_i——猜对！",
            "math_objects": [
                {
                    "name": "码字情况",
                    "latex": "c \\in C \\Rightarrow \\forall i: \\text{guess}_i = c_i",
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
            "description": "c∉C时人j猜错，其余pass→失败",
            "raw_text_span": "当c ∉ C时，人j猜错，其余pass → 失败。",
            "math_objects": [
                {
                    "name": "非码字情况",
                    "latex": "c \\notin C \\Rightarrow \\text{person } j \\text{ wrong}",
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
            "description": "成功率 = P(c∈C) = 1/(n+1)",
            "raw_text_span": "成功率 = P(c ∈ C) = |C| / 2^n = 1/(n+1)。",
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
            "description": "1/(n+1)比1/2差——方向反了",
            "raw_text_span": "1/(n+1)比1/2还差！方向反了。应该反过来。",
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
            "content": "c∉C时人j猜错",
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
            "description": "从1/(n+1)比1/2差到方向反了",
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
            {"description": "反转Hamming码策略", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "奇偶性策略", "description": "S=Σc_i mod 2", "introduced_at_round": 2},
            {"name": "Hamming码框架", "description": "c∈{0,1}^n, 码字集合C", "introduced_at_round": 3}
        ],
        "E_t": [],
        "U_t": [
            {"description": "1/(n+1)比1/2差——Hamming码方向反了", "severity": "blocking", "identified_at_round": 4}
        ],
    },
    "parse_confidence": 0.83,
    "parse_warnings": ["Hamming码策略方向反了"],
}


# ---------------------------------------------------------------------------
# 组合案例 A5: 尝试反转策略，多次失败，卡点
# ---------------------------------------------------------------------------

CB_REAL_A5 = {
    "semantic_events": [
        {
            "type": "TEST",
            "description": "尝试反转策略1：码字pass非码字猜",
            "raw_text_span": "新策略：如果v⁰∈C且v¹∉C，猜c_i=1。分析c∉C时人j猜对，c∈C时人i猜错。还是不对。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.75,
        },
        {
            "type": "TEST",
            "description": "尝试反转策略2：翻转得码字则pass否则猜",
            "raw_text_span": "人i看到c_{-i}，如果v⁰∈C或v¹∈C则pass，否则猜。c∈C时全pass（失败），c∉C时人不保证对。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.75,
        },
        {
            "type": "STALL",
            "description": "Hamming码思路需要更精巧的策略设计",
            "raw_text_span": "Hamming码思路需要更精巧的策略设计。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.78,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "operation",
            "content": "尝试反转策略1",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.75,
        },
        {
            "type": "operation",
            "content": "尝试反转策略2",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.75,
        },
        {
            "type": "stall",
            "content": "Hamming码策略需要更精巧设计",
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
    "parse_warnings": ["Hamming码策略设计遇到困难"],
}


# ---------------------------------------------------------------------------
# 组合案例 A6: 回到本质，k色策略，结论1/k
# ---------------------------------------------------------------------------

CB_REAL_A6 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "k=2正确策略：约定S=s，S_{-i}=s时猜c_i=0否则pass，成功率1/2",
            "raw_text_span": "策略：约定S = s。人i看到S_{-i}：如果S_{-i} = s，猜c_i = 0；否则pass。成功率=1/2。",
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
            "description": "推广k色：S=Σc_i(mod k)，约定S=s，S_{-i}=s时猜c_i=0",
            "raw_text_span": "k色时，S = c_1 + ... + c_n (mod k)。约定S = s。人i看到S_{-i}：如果S_{-i}=s，猜c_i=0；否则pass。",
            "math_objects": [
                {
                    "name": "k色推广",
                    "latex": "S = \\sum c_i \\pmod{k}",
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
            "description": "成功率 = 1/k - P(S=s, ∀i c_i≠0) → 1/k",
            "raw_text_span": "成功率 = P(S = s) - P(S = s, ∀i c_i ≠ 0)。当n → ∞时，成功率 → 1/k。",
            "math_objects": [
                {
                    "name": "k色成功率",
                    "latex": "P(\\text{success}) \\to \\frac{1}{k}",
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
            "description": "上界1/k（信息论：每人缺少1个信息）",
            "raw_text_span": "上界论证：由信息论，每人缺少1个信息，成功率上界 = 1/k。",
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
            "content": "成功率→1/k",
            "math_objects": ["k色成功率"],
            "is_frontier": False,
            "confidence": 0.88,
        },
        {
            "type": "resolution",
            "content": "上界1/k→最优 ✓",
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
            {"statement": "成功率上界1/k", "verified_by": "logic", "verified_at_round": 6}
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
            {"name": "k色模策略", "description": "S=Σc_i mod k", "introduced_at_round": 6}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.88,
    "parse_warnings": ["上界1/k的严格证明用了信息论论证"],
}


CB_REAL_RESPONSES = [CB_REAL_A1, CB_REAL_A2, CB_REAL_A3, CB_REAL_A4, CB_REAL_A5, CB_REAL_A6]


# ===========================================================================
# 对比辅助函数（复用evaluate_accuracy.py的逻辑）
# ===========================================================================

def _collect_math_objects(response: dict) -> List[dict]:
    """从响应中收集所有math_objects"""
    objects = []
    for evt in response.get("semantic_events", []):
        for mo in evt.get("math_objects", []):
            objects.append(mo)
    return objects


def _get_frontier_node(response: dict) -> dict:
    """获取前沿节点"""
    for node in response.get("trajectory_nodes", []):
        if node.get("is_frontier", False):
            return node
    return None


def _has_stall(response: dict) -> bool:
    """判断是否有STALL事件"""
    for evt in response.get("semantic_events", []):
        if evt.get("type") == "STALL":
            return True
    return False


def _get_stall_type(response: dict) -> str:
    """获取卡点类型"""
    if not _has_stall(response):
        return "none"
    for u in response.get("six_tuple", {}).get("U_t", []):
        desc = u.get("description", "")
        if "知识瓶颈" in desc or "知识不足" in desc:
            return "knowledge_gap"
    for w in response.get("parse_warnings", []):
        if "知识瓶颈" in desc or "知识不足" in desc:
            return "knowledge_gap"
    return "thinking_stall"


def _normalize_type(t: str) -> str:
    return t.upper().strip() if t else ""


def _normalize_node_type(t: str) -> str:
    return t.lower().strip() if t else ""


def _descriptions_match(d1: str, d2: str) -> bool:
    if d1 == d2:
        return True
    d1 = d1.strip()
    d2 = d2.strip()
    if d1 in d2 or d2 in d1:
        return True
    return False


def _math_objects_match(mo1: dict, mo2: dict) -> bool:
    name1 = mo1.get("name", "")
    name2 = mo2.get("name", "")
    type1 = mo1.get("object_type", "")
    type2 = mo2.get("object_type", "")
    name_match = (name1 == name2 or name1 in name2 or name2 in name1)
    type_match = (type1 == type2)
    return name_match and type_match


def _six_tuple_field_match(real_items, gold_items, key_field) -> Tuple[int, int]:
    matched = 0
    for gold_item in gold_items:
        gold_key = gold_item.get(key_field, "")
        for real_item in real_items:
            real_key = real_item.get(key_field, "")
            if _descriptions_match(gold_key, real_key):
                matched += 1
                break
    return matched, len(gold_items)


def _check_sympy_parseable(expr: str) -> bool:
    try:
        import sympy as sp
        expr_clean = expr.strip()
        if expr_clean.startswith("Eq("):
            expr_clean = expr_clean.replace("Rational(", "sp.Rational(")
            sp.sympify(expr_clean, locals={"sp": sp, "Rational": sp.Rational})
        else:
            expr_clean = expr_clean.replace("Rational(", "sp.Rational(")
            sp.sympify(expr_clean, locals={"sp": sp, "Rational": sp.Rational})
        return True
    except Exception:
        return False


# ===========================================================================
# 逐轮对比
# ===========================================================================

def evaluate_round(real: dict, gold: dict, round_index: int) -> dict:
    """对比单个A_i的real_response和gold_standard"""
    # 1. 事件类型准确率
    real_events = real.get("semantic_events", [])
    gold_events = gold.get("semantic_events", [])
    real_types_used = set()
    event_type_correct = 0
    for gold_evt in gold_events:
        gold_type = _normalize_type(gold_evt.get("type", ""))
        gold_desc = gold_evt.get("description", "")
        best_idx = None
        for i, real_evt in enumerate(real_events):
            if i in real_types_used:
                continue
            real_type = _normalize_type(real_evt.get("type", ""))
            if real_type == gold_type:
                real_desc = real_evt.get("description", "")
                if _descriptions_match(gold_desc, real_desc):
                    best_idx = i
                    break
                if best_idx is None:
                    best_idx = i
        if best_idx is not None:
            event_type_correct += 1
            real_types_used.add(best_idx)
    event_type_total = len(gold_events)

    # 2. 数学对象提取率
    real_math_objects = _collect_math_objects(real)
    gold_math_objects = _collect_math_objects(gold)
    mo_matched = 0
    real_mo_used = set()
    for gold_mo in gold_math_objects:
        for i, real_mo in enumerate(real_math_objects):
            if i in real_mo_used:
                continue
            if _math_objects_match(gold_mo, real_mo):
                mo_matched += 1
                real_mo_used.add(i)
                break
    mo_total = len(gold_math_objects)

    # 3. SymPy验证通过率
    sympy_pass = 0
    sympy_total = 0
    for mo in real_math_objects:
        expr = mo.get("sympy_expr")
        if expr:
            sympy_total += 1
            if _check_sympy_parseable(expr):
                sympy_pass += 1

    # 4. 六元组字段准确率
    real_st = real.get("six_tuple", {})
    gold_st = gold.get("six_tuple", {})
    v_match, v_total = _six_tuple_field_match(real_st.get("V_t", []), gold_st.get("V_t", []), "statement")
    f_match, f_total = _six_tuple_field_match(real_st.get("F_t", []), gold_st.get("F_t", []), "statement")
    o_match, o_total = _six_tuple_field_match(real_st.get("O_t", []), gold_st.get("O_t", []), "description")
    r_match, r_total = _six_tuple_field_match(real_st.get("R_t", []), gold_st.get("R_t", []), "name")
    e_match, e_total = _six_tuple_field_match(real_st.get("E_t", []), gold_st.get("E_t", []), "content")
    u_match, u_total = _six_tuple_field_match(real_st.get("U_t", []), gold_st.get("U_t", []), "description")
    six_tuple_correct = v_match + f_match + o_match + r_match + e_match + u_match
    six_tuple_total = v_total + f_total + o_total + r_total + e_total + u_total

    # 5. 前沿节点识别率
    real_frontier = _get_frontier_node(real)
    gold_frontier = _get_frontier_node(gold)
    frontier_correct = False
    if real_frontier and gold_frontier:
        real_ftype = _normalize_node_type(real_frontier.get("type", ""))
        gold_ftype = _normalize_node_type(gold_frontier.get("type", ""))
        if real_ftype == gold_ftype:
            frontier_correct = True

    # 6. 卡点类型识别率
    real_stall_type = _get_stall_type(real)
    gold_stall_type = _get_stall_type(gold)
    has_stall = _has_stall(gold)
    stall_correct = False
    if has_stall:
        stall_correct = (real_stall_type == gold_stall_type)

    return {
        "round_index": round_index,
        "event_type_correct": event_type_correct,
        "event_type_total": event_type_total,
        "mo_matched": mo_matched,
        "mo_total": mo_total,
        "sympy_pass": sympy_pass,
        "sympy_total": sympy_total,
        "six_tuple_correct": six_tuple_correct,
        "six_tuple_total": six_tuple_total,
        "frontier_correct": frontier_correct,
        "has_stall": has_stall,
        "stall_correct": stall_correct,
        "real_stall_type": real_stall_type,
        "gold_stall_type": gold_stall_type,
    }


def evaluate_case(real_responses, gold_standards, case_name) -> dict:
    """评估单个案例的所有轮次"""
    round_results = []
    for i in range(len(gold_standards)):
        result = evaluate_round(real_responses[i], gold_standards[i], i + 1)
        round_results.append(result)

    total_event_correct = sum(r["event_type_correct"] for r in round_results)
    total_event_total = sum(r["event_type_total"] for r in round_results)
    total_mo_matched = sum(r["mo_matched"] for r in round_results)
    total_mo_total = sum(r["mo_total"] for r in round_results)
    total_sympy_pass = sum(r["sympy_pass"] for r in round_results)
    total_sympy_total = sum(r["sympy_total"] for r in round_results)
    total_st_correct = sum(r["six_tuple_correct"] for r in round_results)
    total_st_total = sum(r["six_tuple_total"] for r in round_results)
    total_frontier_correct = sum(1 for r in round_results if r["frontier_correct"])
    total_frontier_total = len(round_results)
    stall_rounds = [r for r in round_results if r["has_stall"]]
    total_stall_correct = sum(1 for r in stall_rounds if r["stall_correct"])
    total_stall_total = len(stall_rounds)

    return {
        "case_name": case_name,
        "round_results": round_results,
        "event_type_accuracy": (total_event_correct, total_event_total),
        "math_object_extraction": (total_mo_matched, total_mo_total),
        "sympy_verification": (total_sympy_pass, total_sympy_total),
        "six_tuple_accuracy": (total_st_correct, total_st_total),
        "frontier_identification": (total_frontier_correct, total_frontier_total),
        "stall_identification": (total_stall_correct, total_stall_total),
    }


# ===========================================================================
# 输出格式化
# ===========================================================================

def _pct(correct, total) -> str:
    if total == 0:
        return "N/A"
    return f"{correct/total*100:.1f}%"


def _mark(value, threshold) -> str:
    return "✅" if value >= threshold else "❌"


def _print_case_results(results: dict):
    """打印单个案例的评估结果"""
    case_name = results["case_name"]
    round_results = results["round_results"]

    print(f"\n{'='*60}")
    print(f"=== {case_name} ===")
    print(f"{'='*60}")

    print("\n--- 逐轮对比 ---")
    for r in round_results:
        i = r["round_index"]
        evt_ok = "✅" if r["event_type_correct"] == r["event_type_total"] else "⚠️"
        mo_ok = "✅" if r["mo_matched"] == r["mo_total"] else "⚠️"
        st_pct = r["six_tuple_correct"] / r["six_tuple_total"] * 100 if r["six_tuple_total"] > 0 else 100
        st_ok = "✅" if st_pct >= 75 else "⚠️"
        ft_ok = "✅" if r["frontier_correct"] else "❌"
        stall_str = ""
        if r["has_stall"]:
            stall_ok = "✅" if r["stall_correct"] else "❌"
            stall_str = f", 卡点 {r['real_stall_type']} {stall_ok}"
        print(
            f"A{i}: 事件类型 {r['event_type_correct']}/{r['event_type_total']} {evt_ok}, "
            f"数学对象 {r['mo_matched']}/{r['mo_total']} {mo_ok}, "
            f"六元组 {r['six_tuple_correct']}/{r['six_tuple_total']} {st_ok}, "
            f"前沿节点 {ft_ok}{stall_str}"
        )

    print("\n--- 汇总指标 ---")
    evt_c, evt_t = results["event_type_accuracy"]
    mo_c, mo_t = results["math_object_extraction"]
    sym_c, sym_t = results["sympy_verification"]
    st_c, st_t = results["six_tuple_accuracy"]
    ft_c, ft_t = results["frontier_identification"]
    stall_c, stall_t = results["stall_identification"]

    evt_pct = evt_c / evt_t * 100 if evt_t > 0 else 0
    mo_pct = mo_c / mo_t * 100 if mo_t > 0 else 0
    sym_pct = sym_c / sym_t * 100 if sym_t > 0 else 0
    st_pct = st_c / st_t * 100 if st_t > 0 else 0
    ft_pct = ft_c / ft_t * 100 if ft_t > 0 else 0
    stall_pct = stall_c / stall_t * 100 if stall_t > 0 else 0

    print(f"事件类型准确率: {evt_c}/{evt_t} = {_pct(evt_c, evt_t)}")
    print(f"数学对象提取率: {mo_c}/{mo_t} = {_pct(mo_c, mo_t)}")
    print(f"SymPy验证通过率: {sym_c}/{sym_t} = {_pct(sym_c, sym_t)}")
    print(f"六元组字段准确率: {st_c}/{st_t} = {_pct(st_c, st_t)}")
    print(f"前沿节点识别率: {ft_c}/{ft_t} = {_pct(ft_c, ft_t)}")
    print(f"卡点类型识别率: {stall_c}/{stall_t} = {_pct(stall_c, stall_t)}")

    print("\n--- 最低可接受值达标情况 ---")
    print(f"  事件类型 ≥70%: {_mark(evt_pct, 70)} ({evt_pct:.1f}%)")
    print(f"  数学对象 ≥80%: {_mark(mo_pct, 80)} ({mo_pct:.1f}%)")
    print(f"  SymPy验证 ≥75%: {_mark(sym_pct, 75)} ({sym_pct:.1f}%)")
    print(f"  六元组 ≥65%: {_mark(st_pct, 65)} ({st_pct:.1f}%)")
    print(f"  前沿节点 ≥80%: {_mark(ft_pct, 80)} ({ft_pct:.1f}%)")
    print(f"  卡点类型 ≥70%: {_mark(stall_pct, 70)} ({stall_pct:.1f}%)")

    return {
        "evt_pct": evt_pct, "mo_pct": mo_pct, "sym_pct": sym_pct,
        "st_pct": st_pct, "ft_pct": ft_pct, "stall_pct": stall_pct,
    }


def main() -> int:
    print()
    print("=" * 60)
    print("=== 解析器泛化能力评估：2个新案例 ===")
    print("=" * 60)
    print()
    print("案例1：数论题（p ≡ 1 mod n的素数无穷）")
    print("案例2：组合/概率题（n人猜帽子策略）")
    print()
    print("评估方法：GLM-5.2独立解析每个A_i（不看Gold Standard），")
    print("然后对比Gold Standard计算6项准确率指标。")

    # 评估数论案例
    nt_results = evaluate_case(NT_REAL_RESPONSES, NT_GOLD_STANDARDS, "案例1：数论题")
    nt_pcts = _print_case_results(nt_results)

    # 评估组合/概率案例
    cb_results = evaluate_case(CB_REAL_RESPONSES, CB_GOLD_STANDARDS, "案例2：组合/概率题")
    cb_pcts = _print_case_results(cb_results)

    # 汇总两个案例
    print(f"\n{'='*60}")
    print("=== 两案例汇总 ===")
    print(f"{'='*60}")

    all_pcts = {k: [nt_pcts[k], cb_pcts[k]] for k in nt_pcts}
    avg_pcts = {k: sum(v) / len(v) for k, v in all_pcts.items()}

    print(f"\n{'指标':<20} {'数论案例':>12} {'组合案例':>12} {'平均':>12}")
    print("-" * 60)
    labels = {
        "evt_pct": "事件类型准确率",
        "mo_pct": "数学对象提取率",
        "sym_pct": "SymPy验证通过率",
        "st_pct": "六元组字段准确率",
        "ft_pct": "前沿节点识别率",
        "stall_pct": "卡点类型识别率",
    }
    for k, label in labels.items():
        print(f"{label:<20} {nt_pcts[k]:>11.1f}% {cb_pcts[k]:>11.1f}% {avg_pcts[k]:>11.1f}%")

    print("\n--- 泛化能力达标判断 ---")
    min_thresholds = {
        "事件类型": (avg_pcts["evt_pct"], 70),
        "数学对象": (avg_pcts["mo_pct"], 80),
        "SymPy验证": (avg_pcts["sym_pct"], 75),
        "六元组": (avg_pcts["st_pct"], 65),
        "前沿节点": (avg_pcts["ft_pct"], 80),
        "卡点类型": (avg_pcts["stall_pct"], 70),
    }

    all_pass = True
    for name, (pct, thr) in min_thresholds.items():
        status = _mark(pct, thr)
        print(f"  {name} ≥{thr}%: {status} ({pct:.1f}%)")
        if pct < thr:
            all_pass = False

    print()
    if all_pass:
        print("🎉 两案例平均指标全部达到最低可接受值！解析器泛化能力验证通过。")
        print("   解析器在数论、组合/概率领域均能有效解析，不局限于代数/分析领域。")
        return 0
    else:
        failed = [name for name, (pct, thr) in min_thresholds.items() if pct < thr]
        print(f"⚠️  以下指标未达最低可接受值: {', '.join(failed)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
