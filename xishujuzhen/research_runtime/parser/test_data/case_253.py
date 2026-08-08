"""
253号案例数据：矩条件极差题第二问。

从253号文档§2.1-§2.3提取：
- PROBLEM_TEXT: 题目原文
- QA_SEQUENCE: Q1-Q10和A1-A10的完整文本
- GOLD_STANDARD_A7: A7的人工标注gold standard（按260号§4.2的LLM输出作为gold standard）
"""

# ---------------------------------------------------------------------------
# 题目原文（253号§2.1）
# ---------------------------------------------------------------------------

PROBLEM_TEXT = """已知 a_1, a_2, ..., a_n 为实数，满足：

sum_{i=1}^n a_i = n,  sum_{i=1}^n a_i^2 = 2n,  sum_{i=1}^n a_i^3 = 3n

(2) 证明存在常数 C_2 > 0，使得对所有 n >= 4，

max a_i - min a_i >= sqrt(5) + C_2 * n^(-3/2)"""


# ---------------------------------------------------------------------------
# Q1-Q10和A1-A10的完整文本（253号§2.3）
# ---------------------------------------------------------------------------

QA_SEQUENCE = [
    {
        "round": 1,
        "q_text": "请读取problem.txt。不要解题。描述这道题的结构形状：结论是什么类型？和第(1)问有什么区别？条件和结论之间的'距离'有多远？",
        "q_level": 1.0,
        "q_non_specificity": 0.1,
        "a_text": "识别为渐近精细下界问题。第(1)问证极差≥√5（常数下界），第(2)问要证极差≥√5+C₂n^(-3/2)（渐近精细下界）。差距：需要定量分析δ=R-√5的量级，证明δ≥c/n^(3/2)。",
    },
    {
        "round": 2,
        "q_text": "列出你能想到的所有可能方向——不要求正确，不要求完整，只要列出你脑中浮现的任何方向。",
        "q_level": 1.0,
        "q_non_specificity": 0.0,
        "a_text": "列出方向：复用第(1)问的q(x)和恒等式、在极差接近√5时做更精细分析、投影到根、扰动分析、数值实验观察δ量级、极值构型分析、紧性论证...",
    },
    {
        "round": 3,
        "q_text": "对你觉得最有希望的方向，描述第一步会做什么。不要求真的做，只描述。",
        "q_level": 1.0,
        "q_non_specificity": 0.0,
        "a_text": "描述：先复用q(x)和两个恒等式，然后设R=√5+δ，分析δ很小时的行为。可能描述紧性归约思路——δ≤1时所有点落在固定紧区间内。",
    },
    {
        "round": 4,
        "q_text": "选一个方向，试着做第一步。做多少算多少，做不出来也没关系。",
        "q_level": 1.0,
        "q_non_specificity": 0.0,
        "a_text": "设R=√5+δ，做紧性归约：δ≥1时结论显然成立，故只需讨论0≤δ≤1。此时所有xᵢ落在固定紧区间[r-1, s+1]。",
    },
    {
        "round": 5,
        "q_text": "你得到了什么？这个结果和你要证明的结论之间还有什么差距？下一步你想怎么走？",
        "q_level": 1.0,
        "q_non_specificity": 0.0,
        "a_text": "完成了紧性归约，但还没有δ的定量下界。差距：知道δ≥0（第(1)问），需要δ≥c/n^(3/2)。需要更精细的分析。",
    },
    {
        "round": 6,
        "q_text": "在极值构型附近，把每个点分解成'离它最近的关键点'加上'偏差'。",
        "q_level": 0.7,
        "q_non_specificity": 0.6,
        "a_text": "投影到最近根：以中点-1/2为界，ζᵢ=r（xᵢ≤-1/2）或ζᵢ=s（xᵢ>-1/2），定义eᵢ=xᵢ-ζᵢ。得到展开式q(xᵢ)=±√5·eᵢ+eᵢ²。由紧性得统一界|eᵢ|≤√5/2。",
    },
    {
        "round": 7,
        "q_text": "把你的三个矩条件和偏差展开式做组合——求和、相乘、线性组合——看看能产生哪些'免费的恒等式'。",
        "q_level": 0.8,
        "q_non_specificity": 0.4,
        "a_text": "导出稳定性方程：\n- 由Σxᵢ=0 → A_r+A_s=-D ... (1)\n- 由Σq(xᵢ)=0 → -√5·A_r+√5·A_s+B_r+B_s=0 ... (2)\n- 由Σxᵢq(xᵢ)=0 → 5D = 3√5(B_r-B_s) + 2C ... (3)\n\n其中D=Σζᵢ=kr+(n-k)s=√5(pn-k)，p=(5-√5)/10。",
    },
    {
        "round": 8,
        "q_text": "你的稳定性方程里有一个量D，它取决于k和n的关系。D能等于0吗？如果D不能等于0，它至少有多大？",
        "q_level": 0.5,
        "q_non_specificity": 0.7,
        "a_text": "分析D=√5(pn-k)。D=0需要k/n=p，但p是无理数，所以D≠0。但|D|至少有多大？AI尝试各种估计但有困难——这是知识瓶颈。",
    },
    {
        "round": 9,
        "q_text": "p=(5-√5)/10是二次无理数。数论中有一个标准事实：二次无理数的连分数部分商有界，因此它是badly approximable——存在常数c₀>0使得对任意整数k,n，|p-k/n|≥c₀/n²。你能用这个事实推出|D|的下界吗？",
        "q_level": 0.2,
        "q_non_specificity": 0.9,
        "a_text": "使用badly approximable性质：|p-k/n|≥c₀/n² → |pn-k|≥c₀/n → |D|≥c₁/n。由稳定性方程(3)：5|D|≤4√5·E，因此E=Σeᵢ²≥c₂/n。",
    },
    {
        "round": 10,
        "q_text": "你现在知道了偏差能量的下界Σe²≥c/n。你需要把这个下界传递到极差的下界δ。想想q(x)在根附近的行为，以及柯西不等式。",
        "q_level": 0.6,
        "q_non_specificity": 0.7,
        "a_text": "完成最后步骤：\n- |q(xᵢ)|≥c₃|eᵢ| → Σq(xᵢ)²≥c₄/n\n- 令S=Σ_{q>0}q(xᵢ)，由Σq(xᵢ)=0知2S=Σ|q(xᵢ)|\n- 柯西：Σ|q(xᵢ)|≥√(Σq(xᵢ)²)≥c₅/√n → S≥c₆/√n\n- q(x)在正值区总长度α+β=δ，q(x)≤c₇δ → S≤nc₇δ\n- 合并：nc₇δ≥c₆/√n → δ≥c₈/n^(3/2) ✓",
    },
]


# ---------------------------------------------------------------------------
# A7的人工标注gold standard（按260号§4.2.2的LLM输出作为gold standard）
# ---------------------------------------------------------------------------

GOLD_STANDARD_A7 = {
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
        },
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
        },
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
# A6之后的六元组（A7的previous_six_tuple，260号§4.2.1）
# ---------------------------------------------------------------------------

PREVIOUS_SIX_TUPLE_A6 = {
    "V_t": [
        {"statement": "中心化：x_i=a_i-1, Σx_i=0, Σx_i²=n, Σx_i³=-n", "verified_by": "logic", "verified_at_round": 1},
        {"statement": "q(x)=x²+x-1, 根r=(-1-√5)/2, s=(-1+√5)/2, s-r=√5", "verified_by": "logic", "verified_at_round": 2},
        {"statement": "两个恒等式：Σq(x_i)=0, Σx_i·q(x_i)=0", "verified_by": "logic", "verified_at_round": 3},
        {"statement": "紧性归约：δ≤1时所有x_i落在[r-1,s+1]", "verified_by": "logic", "verified_at_round": 4},
        {"statement": "投影：ζ_i∈{r,s}, e_i=x_i-ζ_i, q(x_i)=±√5·e_i+e_i²", "verified_by": "logic", "verified_at_round": 6},
    ],
    "F_t": [],
    "O_t": [
        {"description": "从矩条件和投影展开式导出恒等式", "status": "in_progress", "obligation_type": "prove"},
        {"description": "估计δ的定量下界", "status": "open", "obligation_type": "prove"},
    ],
    "R_t": [
        {"name": "中心化", "description": "x_i=a_i-1", "introduced_at_round": 1},
        {"name": "紧性归约", "description": "R=√5+δ, δ≤1", "introduced_at_round": 4},
        {"name": "投影到根", "description": "ζ_i∈{r,s}, e_i=x_i-ζ_i", "introduced_at_round": 6},
    ],
    "E_t": [],
    "U_t": [
        {"description": "δ的定量下界", "severity": "blocking", "identified_at_round": 5},
    ],
}
