"""
Mock LLM响应：A1-A10每个的预定义JSON响应。

A7的mock响应用260号§4.2.2的完整JSON（即case_253.py的GOLD_STANDARD_A7）。
其他轮次按260号§4.1表格的解析目标编写。
"""

from .case_253 import GOLD_STANDARD_A7


# ---------------------------------------------------------------------------
# A1-A10的mock LLM响应
# ---------------------------------------------------------------------------

MOCK_RESPONSE_A1 = {
    "semantic_events": [
        {
            "type": "OBSERVATION",
            "description": "识别为渐近精细下界问题",
            "raw_text_span": "识别为渐近精细下界问题。第(1)问证极差≥√5（常数下界），第(2)问要证极差≥√5+C₂n^(-3/2)（渐近精细下界）。",
            "math_objects": [
                {
                    "name": "目标不等式",
                    "latex": "\\max a_i - \\min a_i \\ge \\sqrt{5} + C_2 n^{-3/2}",
                    "sympy_expr": "max_a - min_a - sqrt(5) - C_2*n**(-Rational(3,2))",
                    "object_type": "inequality",
                    "variables": ["max_a", "min_a", "C_2", "n"],
                    "properties": {"type": "asymptotic_lower_bound"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "observation",
            "content": "渐近精细下界问题：极差≥√5+C₂n^(-3/2)",
            "math_objects": ["目标不等式"],
            "is_frontier": True,
            "confidence": 0.9,
        }
    ],
    "trajectory_edges": [],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "渐近精细下界问题：需要证δ≥c/n^(3/2)", "status": "exploring"}
        ],
        "O_t": [
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.9,
    "parse_warnings": [],
}


MOCK_RESPONSE_A2 = {
    "semantic_events": [
        {
            "type": "CANDIDATE",
            "description": "复用第(1)问的q(x)和恒等式",
            "raw_text_span": "复用第(1)问的q(x)和恒等式",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "投影到根",
            "raw_text_span": "投影到根",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "扰动分析",
            "raw_text_span": "扰动分析",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "紧性论证",
            "raw_text_span": "紧性论证",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
    ],
    "trajectory_nodes": [
        {
            "type": "candidate",
            "content": "复用q(x)和恒等式",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "投影到根",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "扰动分析",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "紧性论证",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.8,
        },
    ],
    "trajectory_edges": [],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "渐近精细下界问题", "status": "exploring"},
            {"statement": "候选方向：复用q(x)、投影、扰动、紧性", "status": "exploring"}
        ],
        "O_t": [
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.85,
    "parse_warnings": [],
}


MOCK_RESPONSE_A3 = {
    "semantic_events": [
        {
            "type": "SUBGOAL",
            "description": "先复用q(x)和两个恒等式，然后设R=√5+δ，分析δ很小时的行为",
            "raw_text_span": "先复用q(x)和两个恒等式，然后设R=√5+δ，分析δ很小时的行为。可能描述紧性归约思路——δ≤1时所有点落在固定紧区间内。",
            "math_objects": [
                {
                    "name": "R的定义",
                    "latex": "R = \\sqrt{5} + \\delta",
                    "sympy_expr": "Eq(R, sqrt(5) + delta)",
                    "object_type": "definition",
                    "variables": ["R", "delta"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "subgoal",
            "content": "复用q(x)和恒等式，设R=√5+δ做紧性归约",
            "math_objects": ["R的定义"],
            "is_frontier": True,
            "confidence": 0.85,
        }
    ],
    "trajectory_edges": [],
    "six_tuple": {
        "V_t": [],
        "F_t": [
            {"statement": "渐近精细下界问题", "status": "exploring"}
        ],
        "O_t": [
            {"description": "复用q(x)和恒等式", "obligation_type": "prove", "status": "in_progress"},
            {"description": "做紧性归约", "obligation_type": "prove", "status": "open"},
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.85,
    "parse_warnings": [],
}


MOCK_RESPONSE_A4 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "设R=√5+δ，做紧性归约",
            "raw_text_span": "设R=√5+δ，做紧性归约",
            "math_objects": [
                {
                    "name": "R的定义",
                    "latex": "R = \\sqrt{5} + \\delta",
                    "sympy_expr": "Eq(R, sqrt(5) + delta)",
                    "object_type": "definition",
                    "variables": ["R", "delta"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "紧性归约：δ≥1时结论显然成立，只需讨论0≤δ≤1，此时所有xᵢ落在固定紧区间[r-1, s+1]",
            "raw_text_span": "δ≥1时结论显然成立，故只需讨论0≤δ≤1。此时所有xᵢ落在固定紧区间[r-1, s+1]。",
            "math_objects": [
                {
                    "name": "紧性归约结果",
                    "latex": "0 \\le \\delta \\le 1 \\Rightarrow x_i \\in [r-1, s+1]",
                    "sympy_expr": "delta",
                    "object_type": "inequality",
                    "variables": ["delta"],
                    "properties": {"compact_interval": "[r-1, s+1]"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "设R=√5+δ",
            "math_objects": ["R的定义"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "紧性归约：δ≤1时所有xᵢ落在[r-1,s+1]",
            "math_objects": ["紧性归约结果"],
            "is_frontier": True,
            "confidence": 0.9,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从R=√5+δ推出紧性归约",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4}
        ],
        "F_t": [],
        "O_t": [
            {"description": "复用q(x)和恒等式", "obligation_type": "prove", "status": "in_progress"},
            {"description": "做紧性归约", "obligation_type": "prove", "status": "solved"},
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.88,
    "parse_warnings": [],
}


MOCK_RESPONSE_A5 = {
    "semantic_events": [
        {
            "type": "OBSERVATION",
            "description": "完成了紧性归约，但还没有δ的定量下界",
            "raw_text_span": "完成了紧性归约，但还没有δ的定量下界。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "STALL",
            "description": "知道δ≥0但需要δ≥c/n^(3/2)，不知道下一步如何得到定量下界",
            "raw_text_span": "差距：知道δ≥0（第(1)问），需要δ≥c/n^(3/2)。需要更精细的分析。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "observation",
            "content": "有紧性归约但缺δ定量下界",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "stall",
            "content": "有结果但不知道下一步——需要δ≥c/n^(3/2)但只有δ≥0",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.8,
        }
    ],
    "trajectory_edges": [],
    "six_tuple": {
        "V_t": [
            {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4}
        ],
        "F_t": [],
        "O_t": [
            {"description": "复用q(x)和恒等式", "obligation_type": "prove", "status": "in_progress"},
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4}
        ],
        "E_t": [],
        "U_t": [
            {"description": "δ的定量下界", "severity": "blocking", "identified_at_round": 5}
        ],
    },
    "parse_confidence": 0.82,
    "parse_warnings": [],
}


MOCK_RESPONSE_A6 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "投影到最近根：ζᵢ∈{r,s}，定义eᵢ=xᵢ-ζᵢ",
            "raw_text_span": "投影到最近根：以中点-1/2为界，ζᵢ=r（xᵢ≤-1/2）或ζᵢ=s（xᵢ>-1/2），定义eᵢ=xᵢ-ζᵢ。",
            "math_objects": [
                {
                    "name": "投影定义",
                    "latex": "\\zeta_i \\in \\{r, s\\}, \\quad e_i = x_i - \\zeta_i",
                    "sympy_expr": "e_i",
                    "object_type": "definition",
                    "variables": ["e_i"],
                    "properties": {"zeta_set": "{r,s}"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "得到展开式q(xᵢ)=±√5·eᵢ+eᵢ²，由紧性得统一界|eᵢ|≤√5/2",
            "raw_text_span": "得到展开式q(xᵢ)=±√5·eᵢ+eᵢ²。由紧性得统一界|eᵢ|≤√5/2。",
            "math_objects": [
                {
                    "name": "展开式",
                    "latex": "q(x_i) = \\pm \\sqrt{5} \\cdot e_i + e_i^2",
                    "sympy_expr": "q_x_i - (sqrt(5)*e_i + e_i**2)",
                    "object_type": "equation",
                    "variables": ["q_x_i", "e_i"],
                    "properties": {"bound": "|e_i|<=sqrt(5)/2"},
                }
            ],
            "depends_on": [],
            "confidence": 0.88,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "投影到根：ζᵢ∈{r,s}, eᵢ=xᵢ-ζᵢ",
            "math_objects": ["投影定义"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "展开式q(xᵢ)=±√5·eᵢ+eᵢ²，|eᵢ|≤√5/2",
            "math_objects": ["展开式"],
            "is_frontier": True,
            "confidence": 0.88,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从投影定义推出展开式",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "投影：ζ_i∈{r,s}, e_i=x_i-ζ_i, q(x_i)=±√5·e_i+e_i²", "verified_by": "logic", "verified_at_round": 6}
        ],
        "F_t": [],
        "O_t": [
            {"description": "从矩条件和投影展开式导出恒等式", "obligation_type": "prove", "status": "in_progress"},
            {"description": "估计δ的定量下界", "obligation_type": "prove", "status": "open"}
        ],
        "R_t": [
            {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4},
            {"name": "投影到根", "description": "ζ_i∈{r,s}, e_i=x_i-ζ_i", "introduced_at_round": 6}
        ],
        "E_t": [],
        "U_t": [
            {"description": "δ的定量下界", "severity": "blocking", "identified_at_round": 5}
        ],
    },
    "parse_confidence": 0.87,
    "parse_warnings": [],
}


# A7使用260号§4.2.2的完整JSON
MOCK_RESPONSE_A7 = GOLD_STANDARD_A7


MOCK_RESPONSE_A8 = {
    "semantic_events": [
        {
            "type": "CLAIM",
            "description": "D=√5(pn-k)，D=0需要k/n=p，但p是无理数，所以D≠0",
            "raw_text_span": "分析D=√5(pn-k)。D=0需要k/n=p，但p是无理数，所以D≠0。",
            "math_objects": [
                {
                    "name": "D非零",
                    "latex": "D = \\sqrt{5}(pn - k) \\ne 0",
                    "sympy_expr": "D",
                    "object_type": "claim",
                    "variables": ["D"],
                    "properties": {"reason": "p is irrational, k/n rational"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "STALL",
            "description": "尝试各种估计但有困难——这是知识瓶颈",
            "raw_text_span": "但|D|至少有多大？AI尝试各种估计但有困难——这是知识瓶颈。",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.85,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "claim",
            "content": "D≠0因为p是无理数",
            "math_objects": ["D非零"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "stall",
            "content": "知识瓶颈：|D|的下界估计有困难",
            "math_objects": [],
            "is_frontier": True,
            "confidence": 0.85,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "claim",
            "target_type": "stall",
            "edge_type": "infer",
            "description": "从D≠0到|D|下界估计遇到知识瓶颈",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "投影：ζ_i∈{r,s}, e_i=x_i-ζ_i, q(x_i)=±√5·e_i+e_i²", "verified_by": "logic", "verified_at_round": 6},
            {"statement": "稳定性方程5D=3√5(B_r-B_s)+2C", "verified_by": "logic", "verified_at_round": 7},
            {"statement": "D=√5(pn-k), p=(5-√5)/10是无理数", "verified_by": "logic", "verified_at_round": 7},
            {"statement": "D≠0因为p是无理数", "verified_by": "logic", "verified_at_round": 8}
        ],
        "F_t": [
            {"statement": "稳定性方程5D=3√5(B_r-B_s)+2C", "status": "exploring"}
        ],
        "O_t": [
            {"description": "复用q(x)和恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "做紧性归约", "obligation_type": "prove", "status": "solved"},
            {"description": "从矩条件和投影展开式导出恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "估计D的下界", "obligation_type": "prove", "status": "in_progress"},
            {"description": "把D下界传递到δ下界", "obligation_type": "prove", "status": "open"},
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"},
        ],
        "R_t": [
            {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4},
            {"name": "投影到根", "description": "ζ_i∈{r,s}, e_i=x_i-ζ_i", "introduced_at_round": 6},
            {"name": "稳定性方程表示", "description": "D=√5(pn-k), A_r,A_s,B_r,B_s,C", "introduced_at_round": 7}
        ],
        "E_t": [],
        "U_t": [
            {"description": "D的下界估计——知识瓶颈：需要badly approximable性质", "severity": "blocking", "identified_at_round": 8}
        ],
    },
    "parse_confidence": 0.85,
    "parse_warnings": ["知识瓶颈识别：工作智能体缺乏badly approximable的数论知识"],
}


MOCK_RESPONSE_A9 = {
    "semantic_events": [
        {
            "type": "VERIFICATION",
            "description": "使用badly approximable性质：|p-k/n|≥c₀/n² → |pn-k|≥c₀/n → |D|≥c₁/n",
            "raw_text_span": "使用badly approximable性质：|p-k/n|≥c₀/n² → |pn-k|≥c₀/n → |D|≥c₁/n。",
            "math_objects": [
                {
                    "name": "D的下界",
                    "latex": "|D| \\ge c_1 / n",
                    "sympy_expr": "Abs(D) - c_1/n",
                    "object_type": "inequality",
                    "variables": ["D", "c_1", "n"],
                    "properties": {"method": "badly_approximable"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "由稳定性方程(3)：5|D|≤4√5·E，因此E=Σeᵢ²≥c₂/n",
            "raw_text_span": "由稳定性方程(3)：5|D|≤4√5·E，因此E=Σeᵢ²≥c₂/n。",
            "math_objects": [
                {
                    "name": "E的下界",
                    "latex": "E = \\sum e_i^2 \\ge c_2 / n",
                    "sympy_expr": "E - c_2/n",
                    "object_type": "inequality",
                    "variables": ["E", "c_2", "n"],
                    "properties": {"derived_from": "stability_equation"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        }
    ],
    "trajectory_nodes": [
        {
            "type": "resolution",
            "content": "|D|≥c₁/n（badly approximable）",
            "math_objects": ["D的下界"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "E=Σeᵢ²≥c₂/n（由稳定性方程传递）",
            "math_objects": ["E的下界"],
            "is_frontier": True,
            "confidence": 0.9,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从|D|≥c₁/n和稳定性方程推出E≥c₂/n",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "投影：ζ_i∈{r,s}, e_i=x_i-ζ_i, q(x_i)=±√5·e_i+e_i²", "verified_by": "logic", "verified_at_round": 6},
            {"statement": "稳定性方程5D=3√5(B_r-B_s)+2C", "verified_by": "logic", "verified_at_round": 7},
            {"statement": "D≠0因为p是无理数", "verified_by": "logic", "verified_at_round": 8},
            {"statement": "|D|≥c₁/n（badly approximable性质）", "verified_by": "logic", "verified_at_round": 9},
            {"statement": "E=Σeᵢ²≥c₂/n（由稳定性方程传递）", "verified_by": "logic", "verified_at_round": 9}
        ],
        "F_t": [],
        "O_t": [
            {"description": "复用q(x)和恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "做紧性归约", "obligation_type": "prove", "status": "solved"},
            {"description": "从矩条件和投影展开式导出恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "估计D的下界", "obligation_type": "prove", "status": "solved"},
            {"description": "把D下界传递到δ下界", "obligation_type": "prove", "status": "in_progress"},
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"},
        ],
        "R_t": [
            {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4},
            {"name": "投影到根", "description": "ζ_i∈{r,s}, e_i=x_i-ζ_i", "introduced_at_round": 6},
            {"name": "稳定性方程表示", "description": "D=√5(pn-k), A_r,A_s,B_r,B_s,C", "introduced_at_round": 7}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.9,
    "parse_warnings": [],
}


MOCK_RESPONSE_A10 = {
    "semantic_events": [
        {
            "type": "RESOLUTION",
            "description": "|q(xᵢ)|≥c₃|eᵢ| → Σq(xᵢ)²≥c₄/n",
            "raw_text_span": "|q(xᵢ)|≥c₃|eᵢ| → Σq(xᵢ)²≥c₄/n",
            "math_objects": [
                {
                    "name": "q平方和下界",
                    "latex": "\\sum q(x_i)^2 \\ge c_4 / n",
                    "sympy_expr": "sum_q_sq - c_4/n",
                    "object_type": "inequality",
                    "variables": ["sum_q_sq", "c_4", "n"],
                    "properties": {},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "柯西不等式：Σ|q(xᵢ)|≥√(Σq(xᵢ)²)≥c₅/√n → S≥c₆/√n",
            "raw_text_span": "柯西：Σ|q(xᵢ)|≥√(Σq(xᵢ)²)≥c₅/√n → S≥c₆/√n",
            "math_objects": [
                {
                    "name": "S的下界",
                    "latex": "S \\ge c_6 / \\sqrt{n}",
                    "sympy_expr": "S - c_6/sqrt(n)",
                    "object_type": "inequality",
                    "variables": ["S", "c_6", "n"],
                    "properties": {"method": "cauchy_schwarz"},
                }
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "q(x)在正值区总长度δ，q(x)≤c₇δ → S≤nc₇δ，合并得δ≥c₈/n^(3/2)",
            "raw_text_span": "q(x)在正值区总长度α+β=δ，q(x)≤c₇δ → S≤nc₇δ\n- 合并：nc₇δ≥c₆/√n → δ≥c₈/n^(3/2) ✓",
            "math_objects": [
                {
                    "name": "最终结论",
                    "latex": "\\delta \\ge c_8 n^{-3/2}",
                    "sympy_expr": "delta - c_8*n**(-Rational(3,2))",
                    "object_type": "inequality",
                    "variables": ["delta", "c_8", "n"],
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
            "content": "Σq(xᵢ)²≥c₄/n",
            "math_objects": ["q平方和下界"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "S≥c₆/√n（柯西不等式）",
            "math_objects": ["S的下界"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "δ≥c₈/n^(3/2) ✓ 证毕",
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
            "description": "从Σq²≥c₄/n和柯西不等式推出S≥c₆/√n",
        },
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从S≥c₆/√n和S≤nc₇δ推出δ≥c₈/n^(3/2)",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "投影：ζ_i∈{r,s}, e_i=x_i-ζ_i, q(x_i)=±√5·e_i+e_i²", "verified_by": "logic", "verified_at_round": 6},
            {"statement": "稳定性方程5D=3√5(B_r-B_s)+2C", "verified_by": "logic", "verified_at_round": 7},
            {"statement": "|D|≥c₁/n（badly approximable性质）", "verified_by": "logic", "verified_at_round": 9},
            {"statement": "E=Σeᵢ²≥c₂/n（由稳定性方程传递）", "verified_by": "logic", "verified_at_round": 9},
            {"statement": "δ≥c₈/n^(3/2)（最终结论）", "verified_by": "logic", "verified_at_round": 10}
        ],
        "F_t": [],
        "O_t": [
            {"description": "复用q(x)和恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "做紧性归约", "obligation_type": "prove", "status": "solved"},
            {"description": "从矩条件和投影展开式导出恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "估计D的下界", "obligation_type": "prove", "status": "solved"},
            {"description": "把D下界传递到δ下界", "obligation_type": "prove", "status": "solved"},
            {"description": "估计δ的定量下界", "obligation_type": "prove", "status": "solved"},
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "solved"},
        ],
        "R_t": [
            {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4},
            {"name": "投影到根", "description": "ζ_i∈{r,s}, e_i=x_i-ζ_i", "introduced_at_round": 6},
            {"name": "稳定性方程表示", "description": "D=√5(pn-k), A_r,A_s,B_r,B_s,C", "introduced_at_round": 7}
        ],
        "E_t": [],
        "U_t": [],
    },
    "parse_confidence": 0.92,
    "parse_warnings": [],
}


# ---------------------------------------------------------------------------
# 所有mock响应的列表（索引0对应A1，索引6对应A7）
# ---------------------------------------------------------------------------

MOCK_RESPONSES = [
    MOCK_RESPONSE_A1,
    MOCK_RESPONSE_A2,
    MOCK_RESPONSE_A3,
    MOCK_RESPONSE_A4,
    MOCK_RESPONSE_A5,
    MOCK_RESPONSE_A6,
    MOCK_RESPONSE_A7,
    MOCK_RESPONSE_A8,
    MOCK_RESPONSE_A9,
    MOCK_RESPONSE_A10,
]


def get_mock_response(round_index: int) -> dict:
    """
    获取指定轮次的mock LLM响应。

    Args:
        round_index: 轮次（1-10）

    Returns:
        该轮的mock LLM JSON响应
    """
    idx = round_index - 1
    if idx < 0 or idx >= len(MOCK_RESPONSES):
        raise ValueError(f"轮次{round_index}超出范围(1-10)")
    return MOCK_RESPONSES[idx]


def make_mock_provider():
    """
    创建一个mock响应提供函数，用于LLMParser。

    返回一个函数，输入ParseRequest，返回对应轮次的mock响应。
    """
    def provider(request):
        return get_mock_response(request.round_index)

    return provider
