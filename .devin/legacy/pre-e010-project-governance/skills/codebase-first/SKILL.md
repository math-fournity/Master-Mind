---
name: codebase-first
description: >
  代码为中心铁律的skill——积累"Think with the codebase, work with the codebase"的
  经验和反模式。当AI发现自己或用户偏离代码中心时加载此skill查阅经验。
  WHEN to use: 回答用户提问前、设计方案前、讨论概念时——检查自己是否从代码出发。
  WHEN NOT to use: 纯文档编辑任务（如格式化文档）、纯git操作。
triggers:
  - model
---

# codebase-first

代码为中心铁律的skill——积累经验和反模式。

## 1. 铁律

AI必须永远以代码为中心，从代码出发考虑如何回答和响应用户的提问。

**Think with the codebase, work with the codebase.**

代码是第六代系统的"晾衣架"——代码中每个元素（dataclass/函数/参数）都通过`six/references.py`索引到研发文档。代码不是实现的附属品，代码是系统的骨架和认知锚点。

## 2. 正确模式（积累经验）

每次AI正确地从代码出发回答/设计/讨论时，在此积累经验。

### 经验1：用户提到"trace"时

**正确做法**：先查`six/types.py`→`Trace`的dataclass定义和docstring，从代码出发回答。

```python
# six/types.py → class Trace
@dataclass
class Trace:
    trace_id: str
    level: int                          # 来自哪个Level视图（0=最细, N=最粗）
    trace_type: Literal["local", "non_local", "global"]
    pattern_description: str            # 模式描述
    source_segment_ids: list[str]       # 涉及的段ID
    is_branch_position: bool = False    # 是否是分叉位置本身的trace（仅过程A）
```

从代码出发回答："trace是Parser AI的产出，Telling AI的输入。trace有level（来自哪个Level视图）、trace_type（局部/非局部/全局）、pattern_description（模式描述）、source_segment_ids（涉及的段ID）。过程A还有is_branch_position字段。"

**来源**：2026-08-10建立

### 经验2：用户提到"格化"时

**正确做法**：先查`six/pipes.py`→`pipe_1_parser()`的子pipe `step_2_grid_vein()`的docstring，从代码出发回答。

**来源**：2026-08-10建立

### 经验3：设计新POC时

**正确做法**：先看代码中已有的Pipe函数签名和数据结构，从代码出发设计POC的验证对象和代码指向。如VMS-28的代码指向是`pipe_1_parser()/step_2_grid_vein()`，数据结构指向是`Vein/VeinSegment/LevelView/Trace`。

**来源**：2026-08-10建立（329号POC方案）

## 3. 反模式（积累教训）

每次AI偏离代码中心时，在此积累教训。

### 反模式1：从抽象想法出发回答

**错误做法**：用户问"trace是什么"，不查代码就凭记忆回答——可能遗漏字段、定义不准确。

**正确做法**：查`types.py`→`Trace`的dataclass定义和docstring，从代码出发回答。

**来源**：2026-08-10建立

### 反模式2：设计方案时不看代码

**错误做法**：设计新功能时不看已有的函数签名和数据结构，凭空设计——可能和代码中已有的元素不一致。

**正确做法**：先看代码中已有的dataclass/函数签名/docstring，从代码出发设计方案。

**来源**：2026-08-10建立

### 反模式3：讨论概念时不指向代码

**错误做法**：讨论"格化"时不给出`pipes.py`→`step_2_grid_vein()`的位置——用户无法直接去看代码。

**正确做法**：给出代码位置，让用户可以直接去看。

**来源**：2026-08-10建立

### 反模式4：新增概念时不落盘到代码

**错误做法**：用户提出新概念/新认知时，只在文档中记录，不在`six/types.py`或`six/references.py`中添加对应的代码元素——概念没有代码锚点。

**正确做法**：考虑是否应该在代码中添加对应的dataclass/字段/映射——让概念有代码锚点，不只是文档中的文字。

**来源**：2026-08-10建立

## 4. 检查清单

回答/设计/讨论前，自检：

- [ ] 我看了`six/types.py`中相关的dataclass吗？
- [ ] 我看了`six/pipes.py`中相关的函数签名和docstring吗？
- [ ] 我看了`six/references.py`中相关的映射吗？
- [ ] 我给出了代码位置吗？
- [ ] 如果用户提出新概念，我考虑了落盘到代码吗？

## 5. 积累规则

- 每次发现自己正确地从代码出发时，在§2积累经验
- 每次发现自己偏离代码中心时，在§3积累反模式
- 积累时记录来源（日期/触发场景）
