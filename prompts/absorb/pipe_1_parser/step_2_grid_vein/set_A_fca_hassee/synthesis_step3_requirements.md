# 阶段3要求：内容trace识别（nonlocal+cross_case_merge+global）

## 你要做的

读取 `input.md`（题目和解答文本）和 `comparison.json`（获取基础格化的段划分信息），从段内容出发识别3类trace：nonlocal、cross_case_merge、global。

**这3类trace都不依赖闭元素**——它们从段内容和段间关系出发，是AI不可替代的语义判断。

## 详细步骤

### 1. 识别nonlocal trace（从段内容出发，不依赖闭元素）

**为什么需要这一步**：闭元素枚举是段集合层面的完备运算，但nonlocal trace不一定对应任何闭元素——nonlocal trace是"跨多个段的思维模式"，可能不是任何闭元素的内涵能捕获的。如果只从闭元素出发做语义解读，会漏掉这些不对应闭元素的nonlocal trace。

**怎么做**：从段的内容和段间关系出发，识别跨多个段的思维模式：

1. **论证链识别**：哪些段在思维上属于同一个"论证链"？
   - 例："定义bad index→构造注入映射→鸽巢论证得好指标r"是一个3段的论证链——这3段构成一个完整的存在性论证，但它们可能不构成闭元素（因为各自还有不同的特征）

2. **对比/呼应识别**：哪些段在思维上构成"对比"或"呼应"？
   - 例："段1 WLOG排序"和"段21一般情形归约"是首尾呼应——一个在开头把问题归约到排序情形，一个在结尾把排序情形的结果推广回一般情形
   - 例："Case 1的预防性避障"和"Case 3的修复性避障"是策略对比——两种不同的避障策略

3. **关键变量使用链识别**：哪些段共享同一个"关键变量的使用"？
   - 例：x在多个段中作为分类标准/边界量/验证依据——x的使用贯穿多个段，但这种"贯穿"不一定对应闭元素

4. **思维模式跨段复用识别**：哪些段在做本质相同的操作？
   - 例：三个Case的验证段本质都是"前缀和验证避开M"——但它们在不同Case中，特征标注可能不同，不构成闭元素

### 2. 识别cross_case_merge trace（跨Case非相邻合并）

**为什么需要这一步**：cross_case_merge是跨Case的非相邻段合并——这些段在不同Case中但本质相同，它们的合并不一定对应任何闭元素。不相邻的段如果属性不同不会被程序归为同一闭元素，但你可以在思维上识别出它们的共性。

**怎么做**：对比三个Case的段，找出"本质相同但在不同Case中"的段集合：
- Case 1的验证段、Case 2的验证段、Case 3的验证段——本质都是"前缀和验证避开M"
- Case 1的M'构造段、Case 2的M'构造段、Case 3的M'构造段——本质都是"缩减M为归纳创造条件"
- Case 1的归纳应用段、Case 2的归纳应用段、Case 3的归纳应用段——本质都是"对缩减后子问题应用归纳假设"

### 3. 识别global trace（贯穿全证明的结构性模式）

**为什么需要这一步**：global trace是"贯穿全证明的结构性模式"——它不是局部于某个Case或某几个段，而是整个证明的结构骨架。global trace和nonlocal/cross_case_merge不同：nonlocal是跨段思维模式，cross_case_merge是跨Case的相同操作，global是**贯穿全证明的统一框架或核心变量角色**。如果只识别nonlocal和cross_case_merge，会漏掉"强归纳贯穿整个证明"、"x作为核心边界量贯穿全证明"这种结构性模式。

**global trace vs local trace的区别**：local trace来自闭元素——"这几个段共享某特征"。global trace是**全证明层面的结构**——"这个策略/变量/框架贯穿了证明的绝大部分段，是证明的结构骨架"。一个trace如果涉及全证明超过一半的段，或者涉及证明的框架性决策（如归纳框架、核心变量定义），应该标为global而不是local。

**怎么做**：从全证明的视角，识别贯穿整个证明的结构性模式：

1. **框架性模式识别**：什么策略/框架贯穿了证明的始终？
   - 例："强归纳统一框架"——段1排序归约、段3归纳声明、三Case的归纳调用（段15/段23/段30），强归纳是连接整个证明的结构骨架
   - 例："以x为枢纽的三情况分析"——x的定义(段2)→情况分析框架(段4)→三Case条件(段5/段20/段28)，x的位置关系决定了整个证明的分岔结构

2. **核心变量贯穿识别**：哪个变量贯穿了证明的大部分段，扮演多种角色？
   - 例："x作为核心边界量贯穿全证明"——x是分类标准(段4/段5)、bad index基准(段6/段7)、M'缩减边界(段9/段14)、验证依据(段12/段16)，x贯穿了11个段
   - 例："aₙ贯穿定义和三Case构造验证"——aₙ在段2定义最大性，在段11/12/15/19参与构造和验证

3. **统一模式识别**：三个Case在做什么统一的事？
   - 例："三Case统一归纳模式：M'缩减+强归纳应用"——三个Case都在做"缩减M→应用归纳"
   - 例："三Case统一验证模式：验证前缀和避开M"——三个Case都以验证收尾

**注意**：global trace和cross_case_merge有重叠——"三Case统一归纳模式"既是cross_case_merge也是global。如果同一个模式既是跨Case合并又是贯穿全证明的结构骨架，标为global（global是更高的抽象层级）。不要因为已经标为cross_case_merge就不再标为global——它们是不同的抽象视角。

## 产出格式

填充 `content_based_traces.json`：

```json
{
  "phase": "synthesis_step3",
  "nonlocal_traces": [
    {
      "id": "trace_NL1",
      "type": "nonlocal",
      "description": "bad index存在性论证链",
      "segments": ["段7", "段8", "段9", "段10", "段11", "段12"],
      "level": "L3",
      "generalizable": true
    }
  ],
  "cross_case_merge_traces": [
    {
      "id": "trace_CCM1",
      "type": "cross_case_merge",
      "description": "递归调用归纳假设到缩减子问题",
      "segments": ["段15", "段23", "段30"],
      "level": "L2",
      "generalizable": true
    }
  ],
  "global_traces": [
    {
      "id": "trace_G1",
      "type": "global",
      "description": "强归纳统一框架",
      "segments": ["段1", "段3", "段15", "段23", "段30"],
      "level": "L2",
      "generalizable": true
    }
  ]
}
```

## 完成后

填充完 `content_based_traces.json` 后，创建 `step3_done.md`（空文件）作为完成标记。
