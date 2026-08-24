# 阶段2要求：闭元素解读+跨闭元素元模式

## 你要做的

读取 `closed_elements/`目录下的闭元素清单和 `comparison.json`（获取基础格化选择），对每个闭元素做入选/排除判定，识别跨闭元素元模式。

## 详细步骤

### 1. 对每个闭元素做入选/排除判定

程序枚举出的闭元素是段集合+共同特征集。但"这个闭元素代表什么思维模式？"是AI才能回答的。

**对每个闭元素做入选/排除判定**：
- **入选trace**：这个闭元素对应一个有数学思维价值的trace，给出trace描述和理由
- **排除**：这个闭元素虽然是闭元素，但trace太具体/不可泛化/已被更高Level的trace覆盖

**你不需要验证A''=A——程序已经验证过了。** 你做的是语义判断：这个闭元素有没有数学思维价值？

**POC-VMS-28d的实证发现（重要）**：程序枚举出的闭元素{段10,段14,段17}，程序看到的是"这三个段有共同特征，构成闭元素"。但AI识别出的是"aₙ在这三个段中扮演'跳过障碍'的统一角色"——这是语义层面的元模式，程序看不到。**即使程序枚举出了这个闭元素，你仍然需要做语义解读——程序的枚举不替代你的语义判断。**

### 2. 识别跨闭元素元模式

**跨闭元素元模式**：某个变量、技巧或策略贯穿多个闭元素，不对应任何单一闭元素，但你在思维上能识别出它的统一角色。

例："关键变量x贯穿整个证明"——x用作分类标准(段4)、bad index基准(段6)、M'缩减边界(段9)，这些角色分散在不同闭元素中，没有任何单一闭元素的内涵能捕获"x的多功能角色"。但你能识别出x是连接所有Case的结构骨架。

例："最大元素aₙ作为跳过障碍的工具"——aₙ在三个Case中扮演不同角色（Case 1放最后跳过、Case 2放最后扩展、Case 3放中间跳过z），这些角色分散在不同闭元素中，但你能识别出aₙ的统一"跳过障碍"功能。

**参考V10的key_entities.json**——V10列举了关键实体，你可以从中发现跨闭元素元模式。但不要局限于V10列举的实体——你可能发现V10没列举的跨闭元素元模式。

## 产出格式

填充 `closed_element_traces.json`：

```json
{
  "phase": "synthesis_step2",
  "closed_element_judgments": [
    {
      "id": "ce_V10_3",
      "extent": ["段19", "段27"],
      "intent": ["s:最终和验证", "验证"],
      "source_version": "V10",
      "judgment": "included",
      "trace_description": "终点验证s∉M",
      "trace_type": "local",
      "reason": "Case 1和Case 2都以验证s∉M收尾"
    },
    {
      "id": "ce_V10_0",
      "extent": [],
      "intent": ["所有特征"],
      "source_version": "V10",
      "judgment": "excluded",
      "reason": "平凡闭元素（空外延）"
    }
  ],
  "cross_element_meta_patterns": [
    {
      "id": "trace_CEM1",
      "type": "cross_element_meta_pattern",
      "description": "x的多功能角色元模式",
      "segments": ["段2", "段4", "段7", "段13", "段17", "段22", "段26"],
      "level": "L3",
      "generalizable": true,
      "reason": "x的角色分散在不同闭元素中，没有单一闭元素能捕获"
    }
  ]
}
```

## 完成后

填充完 `closed_element_traces.json` 后，创建 `step2_done.md`（空文件）作为完成标记。
