# Pipe 2接口定义

**前置阅读**：02-tell端/05-Pipe-2-小概念标记分辨.md、07-工程规格/03-Pipe-1接口定义.md
**关联文件**：04-概念树/02-概念文件格式.md
**来源**：289号Pipe 2实现、poc10_tell_disambiguation.py

---

## 1. 输入

| 字段 | 类型 | 说明 |
|---|---|---|
| candidates | List[TellCandidate] | Pipe 1的候选tell列表 |
| thinking_text | string | 推理AI的thinking文本 |
| concept_file | ConceptFile | 概念文件（包含大概念下的所有小概念） |

## 2. 输出

```python
class TellResult:
    tell_id: str                # tell的唯一标识
    combined_score: float       # 大概念分数 + 小概念命中次数加权
    small_concept_hits: dict    # 各小概念信号词的命中次数
    selected: bool              # 是否被选为目标tell
```

返回：`List[TellResult]`——精准识别的tell列表，selected=True的是目标tell。

## 3. 接口规格

```python
def pipe2_disambiguate(
    candidates: List[TellCandidate], 
    thinking_text: str, 
    concept_file: ConceptFile
) -> List[TellResult]:
    """
    Pipe 2：在Pipe 1的候选中用小概念标记分辨精准识别
    
    处理流程：
    1. 从概念文件加载小概念信号词
    2. 对每个候选tell，统计其小概念信号词在thinking中的命中次数
    3. 计算combined_score = 大概念分数 + 小概念命中次数加权
    4. 按combined_score排序
    5. 选最高分的为selected=True
    
    前提条件：
    - Pipe 1已经缩小了候选范围
    - 概念文件已加载（包含该大概念下的所有小概念）
    """
```

## 4. combined_score计算

```python
def calculate_combined_score(candidate, thinking_text):
    # 大概念分数（来自Pipe 1）
    big_concept_score = candidate.match_score  # 如4
    
    # 小概念命中次数
    small_concept_hits = {}
    total_hits = 0
    for marker in candidate.small_concept_markers:
        count = thinking_text.lower().count(marker.lower())
        if count > 0:
            small_concept_hits[marker] = count
            total_hits += count
    
    # combined_score = 大概念分数 + 小概念命中次数
    combined_score = big_concept_score + total_hits
    
    return combined_score, small_concept_hits
```

## 5. 参考实现

`xishujuzhen/vms/poc10_tell_disambiguation.py`中的Pipe 2实现（386行）。
