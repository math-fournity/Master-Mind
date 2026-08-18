---
description: >
  完整工作流对照原则。设计或修改任何Pipe的衔接关系时。
  WHEN to use: 设计或修改任何Pipe的衔接关系时。
  WHEN NOT to use: 不涉及Pipe衔接关系的操作。
trigger: model_decision
---

# 完整工作流对照原则

**触发条件**：设计或修改任何Pipe的衔接关系时。
**来源文档**：315号（完整工作流）、`six/loops.py`

## 规则

设计或修改任何Pipe的衔接关系时，必须对照315号的完整工作流——从推理AI探索到引导树填充的6步完整流程。

确认衔接关系没有断裂：

```
Pipe 0（Solver）→ Pipe 1（Parser）→ Pipe 2（Telling）→ 步骤5分叉 → Pipe 3（Guide）→ 回到Pipe 0
```

如果修改导致衔接关系变化，在315号文档中更新工作流描述，在`six/loops.py`中更新流程函数。
