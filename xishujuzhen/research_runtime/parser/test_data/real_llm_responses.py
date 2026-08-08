"""
真实LLM解析结果：GLM-5.2作为LLM，对253号案例A1-A10的解析输出。

这是真实LLM的解析结果——GLM-5.2直接读A_i的文本，按260号§3.1.2的
prompt格式输出解析结果JSON。

关键：这是独立解析，不参考Gold Standard。GLM-5.2先读A_i文本，
独立输出解析结果，然后再跟Gold Standard对比。

渐进解析：A_i的解析使用A1到A_{i-1}的历史和上一轮的六元组。
用GLM-5.2自己的解析结果作为历史（不是Gold Standard）。

解析过程说明：
- GLM-5.2读取253号文档§2.3中A1-A10的完整文本
- 对每个A_i，按260号§3.1.2的system prompt和user prompt格式输出解析结果
- A_i的解析基于A1到A_{i-1}的累积context（用本文件中前几轮的解析结果作为历史）
- A7的解析是独立做的，不参考260号§4.2.2的示例JSON
"""

from .case_253 import PROBLEM_TEXT, QA_SEQUENCE


# ---------------------------------------------------------------------------
# A1: 识别为渐近精细下界问题
#
# A1文本："识别为渐近精细下界问题。第(1)问证极差≥√5（常数下界），
# 第(2)问要证极差≥√5+C₂n^(-3/2)（渐近精细下界）。差距：需要定量分析
# δ=R-√5的量级，证明δ≥c/n^(3/2)。"
#
# GLM-5.2解析：这是一个OBSERVATION事件——从题面注意到结论类型。
# 前沿节点是observation类型。
# 六元组：V_t空，F_t加入渐近精细下界问题，O_t加入证明目标。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A1 = {
    "semantic_events": [
        {
            "type": "OBSERVATION",
            "description": "识别为渐近精细下界问题：第(1)问证常数下界，第(2)问证渐近精细下界",
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


# ---------------------------------------------------------------------------
# A2: 列出所有可能方向
#
# A2文本："列出方向：复用第(1)问的q(x)和恒等式、在极差接近√5时做更精细
# 分析、投影到根、扰动分析、数值实验观察δ量级、极值构型分析、紧性论证..."
#
# GLM-5.2解析：多个CANDIDATE事件——每个方向是一个候选。
# 前沿节点是candidate类型（多个，最后一个为前沿）。
# 六元组：F_t加入候选方向。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A2 = {
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
            "description": "在极差接近√5时做更精细分析",
            "raw_text_span": "在极差接近√5时做更精细分析",
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
            "description": "数值实验观察δ量级",
            "raw_text_span": "数值实验观察δ量级",
            "math_objects": [],
            "depends_on": [],
            "confidence": 0.8,
        },
        {
            "type": "CANDIDATE",
            "description": "极值构型分析",
            "raw_text_span": "极值构型分析",
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
            "content": "极差接近√5时更精细分析",
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
            "content": "数值实验观察δ量级",
            "math_objects": [],
            "is_frontier": False,
            "confidence": 0.8,
        },
        {
            "type": "candidate",
            "content": "极值构型分析",
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
            {"statement": "候选方向：复用q(x)、精细分析、投影、扰动、数值实验、极值构型、紧性", "status": "exploring"}
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


# ---------------------------------------------------------------------------
# A3: 描述最有希望方向的第一步
#
# A3文本："描述：先复用q(x)和两个恒等式，然后设R=√5+δ，分析δ很小时的行为。
# 可能描述紧性归约思路——δ≤1时所有点落在固定紧区间内。"
#
# GLM-5.2解析：SUBGOAL事件——描述要做的子目标。
# 前沿节点是subgoal类型。
# 六元组：O_t加入"复用q(x)和恒等式"和"做紧性归约"。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A3 = {
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


# ---------------------------------------------------------------------------
# A4: 设R=√5+δ，做紧性归约
#
# A4文本："设R=√5+δ，做紧性归约：δ≥1时结论显然成立，故只需讨论0≤δ≤1。
# 此时所有xᵢ落在固定紧区间[r-1, s+1]。"
#
# GLM-5.2解析：REPRESENTATION（设R=√5+δ）+ RESOLUTION（紧性归约结果）。
# 前沿节点是resolution类型（紧性归约结果）。
# 六元组：V_t加入紧性归约结果，R_t加入"紧性归约"。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A4 = {
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


# ---------------------------------------------------------------------------
# A5: 完成紧性归约，指出差距
#
# A5文本："完成了紧性归约，但还没有δ的定量下界。差距：知道δ≥0（第(1)问），
# 需要δ≥c/n^(3/2)。需要更精细的分析。"
#
# GLM-5.2解析：OBSERVATION（完成了紧性归约但缺下界）+ STALL（不知道下一步）。
# 前沿节点是stall类型。
# 六元组：U_t加入"δ的定量下界"（blocking）。
# 卡点类型："有结果但不知道下一步"。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A5 = {
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


# ---------------------------------------------------------------------------
# A6: 投影到最近根，展开式
#
# A6文本："投影到最近根：以中点-1/2为界，ζᵢ=r（xᵢ≤-1/2）或ζᵢ=s（xᵢ>-1/2），
# 定义eᵢ=xᵢ-ζᵢ。得到展开式q(xᵢ)=±√5·eᵢ+eᵢ²。由紧性得统一界|eᵢ|≤√5/2。"
#
# GLM-5.2解析：REPRESENTATION（投影定义）+ RESOLUTION（展开式和界）。
# 前沿节点是resolution类型。
# 六元组：V_t加入投影结果，R_t加入"投影到根"。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A6 = {
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


# ---------------------------------------------------------------------------
# A7: 导出稳定性方程
#
# A7文本："导出稳定性方程：
# - 由Σxᵢ=0 → A_r+A_s=-D ... (1)
# - 由Σq(xᵢ)=0 → -√5·A_r+√5·A_s+B_r+B_s=0 ... (2)
# - 由Σxᵢq(xᵢ)=0 → 5D = 3√5(B_r-B_s) + 2C ... (3)
# 其中D=Σζᵢ=kr+(n-k)s=√5(pn-k)，p=(5-√5)/10。"
#
# GLM-5.2独立解析（不参考260号§4.2.2示例）：
# - REPRESENTATION：引入D、p、A_r、A_s、B_r、B_s、C等新记号
# - RESOLUTION×3：三个方程分别由三个矩条件导出
# 前沿节点是resolution类型（稳定性方程(3)）。
# 六元组：F_t加入稳定性方程和D的定义，U_t加入"D的量级问题"。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A7 = {
    "semantic_events": [
        {
            "type": "REPRESENTATION",
            "description": "引入量D=Σζᵢ=kr+(n-k)s=√5(pn-k)和新记号A_r,A_s,B_r,B_s,C",
            "raw_text_span": "其中D=Σζᵢ=kr+(n-k)s=√5(pn-k)，p=(5-√5)/10。",
            "math_objects": [
                {
                    "name": "D的定义",
                    "latex": "D = \\sum \\zeta_i = kr + (n-k)s = \\sqrt{5}(pn - k)",
                    "sympy_expr": "Eq(D, k*r + (n-k)*s)",
                    "object_type": "definition",
                    "variables": ["D", "k", "r", "s", "n"],
                    "properties": {
                        "also_equals": "sqrt(5)*(p*n - k)",
                        "p_definition": "(5-sqrt(5))/10",
                    },
                },
                {
                    "name": "p的定义",
                    "latex": "p = \\frac{5 - \\sqrt{5}}{10}",
                    "sympy_expr": "Eq(p, (5 - sqrt(5))/10)",
                    "object_type": "definition",
                    "variables": ["p"],
                    "properties": {"is_irrational": "true"},
                },
            ],
            "depends_on": [],
            "confidence": 0.9,
        },
        {
            "type": "RESOLUTION",
            "description": "由Σxᵢ=0导出方程(1): A_r+A_s=-D",
            "raw_text_span": "由Σxᵢ=0 → A_r+A_s=-D ... (1)",
            "math_objects": [
                {
                    "name": "方程(1)",
                    "latex": "A_r + A_s = -D",
                    "sympy_expr": "Eq(A_r + A_s, -D)",
                    "object_type": "equation",
                    "variables": ["A_r", "A_s", "D"],
                    "properties": {"derived_from": "Σx_i=0"},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "RESOLUTION",
            "description": "由Σq(xᵢ)=0导出方程(2): -√5·A_r+√5·A_s+B_r+B_s=0",
            "raw_text_span": "由Σq(xᵢ)=0 → -√5·A_r+√5·A_s+B_r+B_s=0 ... (2)",
            "math_objects": [
                {
                    "name": "方程(2)",
                    "latex": "-\\sqrt{5} A_r + \\sqrt{5} A_s + B_r + B_s = 0",
                    "sympy_expr": "Eq(-sqrt(5)*A_r + sqrt(5)*A_s + B_r + B_s, 0)",
                    "object_type": "equation",
                    "variables": ["A_r", "A_s", "B_r", "B_s"],
                    "properties": {"derived_from": "Σq(x_i)=0"},
                }
            ],
            "depends_on": [],
            "confidence": 0.85,
        },
        {
            "type": "RESOLUTION",
            "description": "由Σxᵢq(xᵢ)=0导出稳定性方程(3): 5D = 3√5(B_r-B_s) + 2C",
            "raw_text_span": "由Σxᵢq(xᵢ)=0 → 5D = 3√5(B_r-B_s) + 2C ... (3)",
            "math_objects": [
                {
                    "name": "稳定性方程",
                    "latex": "5D = 3\\sqrt{5}(B_r - B_s) + 2C",
                    "sympy_expr": "Eq(5*D, 3*sqrt(5)*(B_r - B_s) + 2*C)",
                    "object_type": "equation",
                    "variables": ["D", "B_r", "B_s", "C"],
                    "properties": {
                        "derived_from": "Σx_i*q(x_i)=0",
                        "is_stability_equation": "true",
                    },
                }
            ],
            "depends_on": ["event_7_1", "event_7_2"],
            "confidence": 0.9,
        },
    ],
    "trajectory_nodes": [
        {
            "type": "representation",
            "content": "引入D=√5(pn-k), p=(5-√5)/10, A_r, A_s, B_r, B_s, C",
            "math_objects": ["D的定义", "p的定义"],
            "is_frontier": False,
            "confidence": 0.9,
        },
        {
            "type": "resolution",
            "content": "方程(1): A_r+A_s=-D",
            "math_objects": ["方程(1)"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "resolution",
            "content": "方程(2): -√5·A_r+√5·A_s+B_r+B_s=0",
            "math_objects": ["方程(2)"],
            "is_frontier": False,
            "confidence": 0.85,
        },
        {
            "type": "resolution",
            "content": "稳定性方程(3): 5D=3√5(B_r-B_s)+2C",
            "math_objects": ["稳定性方程"],
            "is_frontier": True,
            "confidence": 0.9,
        }
    ],
    "trajectory_edges": [
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从D的定义和Σx_i=0推出方程(1)",
        },
        {
            "source_type": "representation",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从D的定义和Σq(x_i)=0推出方程(2)",
        },
        {
            "source_type": "resolution",
            "target_type": "resolution",
            "edge_type": "infer",
            "description": "从方程(1)(2)和Σx_i*q(x_i)=0推出稳定性方程(3)",
        }
    ],
    "six_tuple": {
        "V_t": [
            {"statement": "中心化：x_i=a_i-1, Σx_i=0, Σx_i²=n, Σx_i³=-n", "verified_by": "logic", "verified_at_round": 1},
            {"statement": "q(x)=x²+x-1, 根r,s, s-r=√5", "verified_by": "logic", "verified_at_round": 2},
            {"statement": "两个恒等式：Σq(x_i)=0, Σx_i·q(x_i)=0", "verified_by": "logic", "verified_at_round": 3},
            {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4},
            {"statement": "投影：ζ_i∈{r,s}, e_i=x_i-ζ_i, q(x_i)=±√5·e_i+e_i²", "verified_by": "logic", "verified_at_round": 6},
        ],
        "F_t": [
            {"statement": "稳定性方程5D=3√5(B_r-B_s)+2C", "status": "exploring"},
            {"statement": "D=√5(pn-k), p=(5-√5)/10", "status": "exploring"},
        ],
        "O_t": [
            {"description": "复用q(x)和恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "做紧性归约", "obligation_type": "prove", "status": "solved"},
            {"description": "从矩条件和投影展开式导出恒等式", "obligation_type": "prove", "status": "solved"},
            {"description": "估计D的下界", "obligation_type": "prove", "status": "open"},
            {"description": "把D下界传递到δ下界", "obligation_type": "prove", "status": "open"},
            {"description": "证明极差≥√5+C₂n^(-3/2)", "obligation_type": "prove", "status": "open"},
        ],
        "R_t": [
            {"name": "中心化", "description": "x_i=a_i-1", "introduced_at_round": 1},
            {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4},
            {"name": "投影到根", "description": "ζ_i∈{r,s}, e_i=x_i-ζ_i", "introduced_at_round": 6},
            {"name": "稳定性方程表示", "description": "D=√5(pn-k), A_r,A_s,B_r,B_s,C", "introduced_at_round": 7},
        ],
        "E_t": [],
        "U_t": [
            {"description": "D的量级问题——D=√5(pn-k)取决于整数k和n的关系，需要估计|D|的下界", "severity": "blocking", "identified_at_round": 7},
        ],
    },
    "parse_confidence": 0.87,
    "parse_warnings": [
        "D的SymPy表达式使用了k*r+(n-k)*s形式，未直接展开为√5(pn-k)，需要确认等价性"
    ],
}


# ---------------------------------------------------------------------------
# A8: 分析D=√5(pn-k)，遇到困难
#
# A8文本："分析D=√5(pn-k)。D=0需要k/n=p，但p是无理数，所以D≠0。
# 但|D|至少有多大？AI尝试各种估计但有困难——这是知识瓶颈。"
#
# GLM-5.2解析：CLAIM（D≠0）+ STALL（知识瓶颈）。
# 前沿节点是stall类型。
# 六元组：U_t更新为"D的下界估计——知识瓶颈"。
# 卡点类型："知识不足"（knowledge_gap）。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A8 = {
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


# ---------------------------------------------------------------------------
# A9: 使用badly approximable性质
#
# A9文本："使用badly approximable性质：|p-k/n|≥c₀/n² → |pn-k|≥c₀/n → |D|≥c₁/n。
# 由稳定性方程(3)：5|D|≤4√5·E，因此E=Σeᵢ²≥c₂/n。"
#
# GLM-5.2解析：VERIFICATION（badly approximable验证|D|下界）+ RESOLUTION（E的下界）。
# 前沿节点是resolution类型。
# 六元组：V_t加入|D|≥c₁/n和E≥c₂/n，U_t移除"D的下界"（已解决）。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A9 = {
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


# ---------------------------------------------------------------------------
# A10: 完成最后步骤，证毕
#
# A10文本："完成最后步骤：
# - |q(xᵢ)|≥c₃|eᵢ| → Σq(xᵢ)²≥c₄/n
# - 令S=Σ_{q>0}q(xᵢ)，由Σq(xᵢ)=0知2S=Σ|q(xᵢ)|
# - 柯西：Σ|q(xᵢ)|≥√(Σq(xᵢ)²)≥c₅/√n → S≥c₆/√n
# - q(x)在正值区总长度α+β=δ，q(x)≤c₇δ → S≤nc₇δ
# - 合并：nc₇δ≥c₆/√n → δ≥c₈/n^(3/2) ✓"
#
# GLM-5.2解析：RESOLUTION×3（q平方和下界、柯西S下界、最终结论δ≥c₈/n^(3/2)）。
# 前沿节点是resolution类型（最终结论）。
# 六元组：V_t加入δ≥c₈/n^(3/2)，O_t全部solved。
# ---------------------------------------------------------------------------

REAL_RESPONSE_A10 = {
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
# 所有真实LLM响应的列表（索引0对应A1，索引6对应A7）
# ---------------------------------------------------------------------------

REAL_RESPONSES = [
    REAL_RESPONSE_A1,
    REAL_RESPONSE_A2,
    REAL_RESPONSE_A3,
    REAL_RESPONSE_A4,
    REAL_RESPONSE_A5,
    REAL_RESPONSE_A6,
    REAL_RESPONSE_A7,
    REAL_RESPONSE_A8,
    REAL_RESPONSE_A9,
    REAL_RESPONSE_A10,
]


def get_real_response(round_index: int) -> dict:
    """
    获取指定轮次的真实LLM响应。

    Args:
        round_index: 轮次（1-10）

    Returns:
        该轮的真实LLM JSON响应
    """
    idx = round_index - 1
    if idx < 0 or idx >= len(REAL_RESPONSES):
        raise ValueError(f"轮次{round_index}超出范围(1-10)")
    return REAL_RESPONSES[idx]


def make_real_provider():
    """
    创建一个真实LLM响应提供函数，用于LLMParser。

    返回一个函数，输入ParseRequest，返回对应轮次的真实LLM响应。
    用于端到端测试，替代mock_llm_responses.make_mock_provider。
    """
    def provider(request):
        return get_real_response(request.round_index)

    return provider
