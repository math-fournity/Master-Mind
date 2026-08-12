# 343号 · trace去特化后长什么样——去特化产出是Tell，不是高Level Tell

**日期**：2026-08-11
**触发原因**：用户提问"一个trace去特化之后长什么样子呢？难道是一个高Level的Tell？"
**上下文**：入题侧脉络分析1.0完成后，讨论下一个Pipe（trace去特化→(tell,hint)→按分类学存储）

---

## 核心结论

**trace去特化之后就是一个Tell——一个可泛化的、按分类学四层定位的Tell。不是"高Level Tell"，就是普通Tell。**

"高Level"是tell分类学中的层（domain→trace_type→segment_pattern→specific_concept四层中的高层），不是去特化后tell的特殊形态。去特化产出的就是一个标准的Tell，有完整的四成分+四层分类位置。

---

## trace和tell的区别

**trace**（脉络分析产出）是Level 0的、和当前题目绑定的：
- 只有pattern_description（模式描述）
- 例：trace_8 "swap避障技巧——通过交换排列中元素位置跳过障碍"（IMO 2009 P6特化）

**tell**（去特化后的产物）是可泛化的、标准化的：
- 有完整的四个组成成分（000号文档定义）：
  1. branch_signal：分叉信号——可以分叉但AI没分叉的位置
  2. branch_type：分叉类型——翻译类型/操作路径类型/...
  3. unexplored_diagnosis：未探索诊断——AI为什么没走这条路
  4. direction_matching：方向匹配——从诊断到翻译方向的映射
- 有分类学四层位置（313号§4.1定义）：
  - domain：数论/代数/组合/...
  - trace_type：local/non_local/global
  - segment_pattern：段结构模式
  - specific_concept：具体概念

---

## 去特化的具体例子

来自VMS-28c验证结果（第六代系统研发过程文档/vms28c_subagent_output.md）：

### 能匹配到已有tell类型的trace

| trace | 去特化后的tell类型 | 预期匹配 |
|---|---|---|
| trace_3 | 鸽巢论证找存在性元素 | 高——鸽巢论证是经典tell类型 |
| trace_9 | 分类+注入映射+鸽巢论证找存在性元素 | 中——三步组合可能匹配"存在性证明策略"类型 |
| trace_13 | 强归纳作为统一框架 | 高——强归纳是经典tell类型 |
| trace_15 | 定义辅助变量简化归纳结构 | 高——辅助变量简化是经典tell类型 |
| trace_16 | 强归纳+情况分析+鸽巢计数的组合策略 | 中——组合策略可能匹配"归纳证明整体策略"类型 |

### 可能匹配不到（新类型tell）的trace

| trace | 去特化后的tell类型 | 说明 |
|---|---|---|
| trace_8 | swap避障技巧——通过交换排列中元素位置跳过障碍 | **新类型tell**——swap修复排列是本题特有的技巧 |
| trace_17 | 四步元模式（定义→归纳→构造→验证）跨Case复用 | **新类型tell**——元模式识别是高阶tell |
| trace_18 | 避障技巧的双重策略——预防性vs修复性 | **新类型tell**——避障策略分类是新的tell类型 |
| trace_19 | 简单Case是复杂Case的简化版——结构平行递进 | **新类型tell**——Case间关系识别是新的tell类型 |

### 去特化需要把握的度

- **太宽泛**：trace_11"排列构造跨Case复用"去特化为"构造对象完成证明"——匹配太多不相关的tell。需要收窄为"构造排列+验证避障"。
- **太狭窄**：trace_5"定义z=max(M)和M'后应用归纳"——"定义z=max(M)"太具体。需要拓宽为"定义辅助变量缩小问题规模后应用归纳"。
- **恰好**：trace_3"鸽巢论证找存在性元素"——既可泛化又不失指导性。

---

## 去特化的定义（来自287号）

**去特化**：把tell从Level 0（题目特化）提升到可泛化的Level，使tell可以被穷举。

**穷举是降低tell识别难度的手段**——tell需要被穷举成一组可枚举的模式，就像hint端的24个翻译方向是从"翻译语言"这个高Level方向展开的一样。

**去特化后的tell规模会很大**——10万级别是一个虚数，意思是不能假设全部tell可以放入辅助AI的上下文中，需要用分类学+检索Pipe降低到合理量级。

---

## 入题侧vs解题侧的区别

**入题侧（解答吸收）**：
- 输入是已验证的正确解答
- traces来自正确解答，可以直接去特化成为新(tell, hint)
- 不需要Telling AI匹配已有tell库——因为目的是增长tell库，不是检索
- 1.0版本可以暂时不考虑和解题侧积累的trace发生关系

**解题侧（解题引导）**：
- 输入是探索中的AI的thinking
- traces可能走对了也可能走错了
- 需要Telling AI匹配已有tell库验证
- 匹配到tell → 取hint填引导树
- 没匹配到 → 孤悬trace存档→启发解答吸收

---

## 入题侧下一个Pipe的工作

**把traces去特化成Tells，关联Hints，按分类学四层存储到运行时。**

这个Pipe需要AI来做——因为"去特化"是语义判断，不是程序能做的：
- 判断trace去特化到什么程度恰好（不过宽不过窄）
- 补全Tell的四个组成成分（branch_signal/branch_type/unexplored_diagnosis/direction_matching）
- 确定分类学四层位置（domain/trace_type/segment_pattern/specific_concept）
- 关联hint（一个tell可以对应多个hint）

---

## 来源文档

| 文档 | 内容 |
|---|---|
| 287号 | tell端的去特化与规模检索——系统成败的关键 |
| 312号 | 第六代系统的两个核心问题——Trace识别与Trace→Tell匹配 |
| 000号 | 引导树闭环-识别端结构定义——tell的四个组成成分 |
| 313号§4.1 | Tell分类学——分类维度四层 |
| vms28c_subagent_output.md | VMS-28c验证结果——trace去特化后的tell类型实例 |
