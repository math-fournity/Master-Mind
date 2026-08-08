# Pipe 0接口定义

**前置阅读**：02-tell端/03-Pipe-0-拓扑化.md、07-工程规格/01-系统架构总图.md
**关联文件**：07-工程规格/03-Pipe-1接口定义.md
**来源**：288号Pipe 0实现、poc9_tell_filter.py

---

## 1. 输入

| 字段 | 类型 | 说明 |
|---|---|---|
| thinking_text | string | 推理AI的thinking文本（从mitmproxy流式截获或sessions.db提取） |

## 2. 输出

```python
class TopologyResult:
    problem_type: str        # 问题类型，如 "discrete_combinatorial"
    ai_method_type: str      # AI方法类型，如 "continuous_analytic"
    gap_type: str            # 缺口类型，如 "method_problem_mismatch"
    signal_counts: dict      # 各信号词的频次，如 {"continuous": 92, "enumeration": 5, ...}
    confidence: float        # 拓扑化置信度，0-1
```

## 3. 接口规格

```python
def pipe0_topologize(thinking_text: str) -> TopologyResult:
    """
    Pipe 0：将thinking文本编码为拓扑结构
    
    处理流程：
    1. 统计各信号词在thinking中的出现频次
    2. 根据频次判定problem_type
    3. 根据频次判定ai_method_type
    4. 根据problem_type和ai_method_type判定gap_type
    5. 计算置信度
    
    返回：TopologyResult对象
    """
```

## 4. 信号词定义

```python
SIGNAL_WORDS = {
    "continuous": ["polynomial", "symbol", "sign", "continuous", "analytic", 
                   "derivative", "integral", "smooth", "function"],
    "enumeration": ["enumerate", "list", "cover", "check", "brute", 
                    "force", "try", "case", "all"],
    "discrete": ["group", "factor", "mod", "residue", "discrete", 
                 "combinatorial", "partition", "integer"],
    "structural": ["structure", "subgroup", "normal", "homomorphism", 
                   "quotient", "sylow", "center"],
    "discrete_specific": ["mersenne", "prime", "divisor", "gcd", 
                          "congruence", "modular"],
    "structural_specific": ["euler", "legendre", "quadratic", "residue", 
                            "p_adic", "valuation"]
}
```

## 5. 拓扑维度取值判定规则

```python
def determine_problem_type(signal_counts):
    if signal_counts["discrete"] + signal_counts["discrete_specific"] > signal_counts["structural"] + signal_counts["structural_specific"]:
        return "discrete_combinatorial"
    else:
        return "structural_existence"

def determine_ai_method_type(signal_counts):
    if signal_counts["continuous"] > signal_counts["enumeration"]:
        return "continuous_analytic"
    else:
        return "enumeration_brute_force"

def determine_gap_type(problem_type, ai_method_type):
    # 如果问题类型和AI方法类型不匹配
    if (problem_type == "discrete_combinatorial" and ai_method_type == "continuous_analytic") or \
       (problem_type == "structural_existence" and ai_method_type == "enumeration_brute_force"):
        return "method_problem_mismatch"
    else:
        return "other"
```

## 6. 错误处理

| 情况 | 处理 |
|---|---|
| thinking为空 | 返回TopologyResult(confidence=0)，Pipe 1不产生候选 |
| 信号词全部为0 | 返回TopologyResult(confidence=0.1)，Pipe 1可能产生少量候选 |
| confidence < 0.5 | 标记为低置信度结果，Pipe 2需要更谨慎地做标记分辨 |

## 7. 参考实现

`xishujuzhen/vms/poc9_tell_filter.py`中的Pipe 0实现（329行）。
