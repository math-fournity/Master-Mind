# 02-trace-tell-hint三步链路

**前置阅读**：01-基础概念/01-系统概述.md
**关联文件**：02-trace端/01-trace的定义与分类.md、03-hint端/01-hint字典的结构.md
**来源**：309号§4、311号§3.4、333号（tell-hint多对多关系）、第五代说明书01-02

---

## §1 三步链路的定义

trace（发现：辅助AI从thinking中识别出的结构化内容）→ tell（匹配：数据库中标准化的trace描述）→ hint（取用：与tell关联的方向提示）

---

## §2 为什么不用第五代的tell+hint二元组

tell身兼两职（既是识别结果又是库内容）的混淆；trace是AI侧的（动态的、具体的），tell是库侧的（静态的、标准化的）

---

## §3 trace的命名来源

"踪迹"，辅助AI在推理AI的思维中追踪，留下的识别结果就是trace

---

## §4 trace→tell→hint每一步的动作不同

发现（trace）、匹配（tell）、取用（hint）。原来tell→hint是两步，但tell内部混了发现和匹配，实际上是三步硬说成两步

---

## §5 trace和tell的多对多关系

一个tell可以匹配多个trace（"闭式猜测追逐"tell匹配"PSLQ闭式追逐"trace和"连分数闭式追逐"trace）；一个trace也可能匹配多个tell。

---

## §6 tell和hint的多对多关系

**tell和hint是多对多关系**（333号）：

- **一个tell可以对应多个hint**——同一个trace识别结果（tell）可以触发多个不同的方向提示（hint）。例如"同构之桥tell"可以对应"考虑椭圆曲线方向""考虑表示论方向""考虑代数几何方向"等多个hint。
- **一个hint也可能被多个tell指到**——同一个方向提示（hint）可能被不同的识别结果（tell）触发。例如"考虑椭圆曲线方向"这个hint，可能被"同构之桥tell"触发，也可能被"代数变换tell"触发。
- **这意味着tell→hint不是一对一映射，是多对多映射**。数据库schema中trace_tell_match集合和tell_hint_match集合需要支持多对多。

### §6.1 "同构之桥"的多对多关系实例

"同构之桥tell"和"同构之桥hint"两者都有意义：
- "同构之桥tell" = 识别到"AI没做跨域翻译"这个trace，匹配到"同构之桥"这个tell
- "同构之桥hint" = "考虑把问题翻译到另一个领域"这个方向提示

一个"同构之桥tell"可以对应多个"同构之桥hint"——因为跨域翻译有多个可能的目标领域（椭圆曲线、表示论、代数几何等），每个目标领域是一个独立的hint。

---

## §7 三步链路与并发Telling AI的关系

每个Telling AI产出trace，汇总AI从trace匹配tell，tell关联的hint被取出

---

## §8 待后续完善的内容

1. tell_hint_match多对多关系的具体schema
2. 多对多关系下的hint选择策略——一个tell对应多个hint时，如何选择最合适的hint？
