# 阶段4要求：审计+合并+AI优势+关键实体+元反思

## 你要做的

读取 `comparison.json`、`closed_element_traces.json`、`content_based_traces.json`，合并所有trace，做审计、去冗余、AI优势识别、关键实体列举、元反思，产出最终的output.json和output.md。

## 详细步骤

### 1. 合并所有trace

从3个输入文件中合并所有trace：
- `closed_element_traces.json`中的入选闭元素→local trace
- `closed_element_traces.json`中的跨闭元素元模式→cross_element_meta_pattern trace
- `content_based_traces.json`中的nonlocal trace
- `content_based_traces.json`中的cross_case_merge trace
- `content_based_traces.json`中的global trace

### 2. 审计

#### 审计项1：trace完备性自检
- 你有没有遗漏什么trace？
- 每个闭元素都有入选/排除判定吗？
- nonlocal trace（从段内容出发识别，不依赖闭元素）都识别了吗？
- 跨闭元素元模式和跨Case非相邻合并都识别了吗？
- global trace（贯穿全证明的结构性模式）都识别了吗？有没有应该标为global但被标为local的trace？

#### 审计项2：闭元素完备性（程序已做——你只做回溯检查）
- 程序枚举的闭元素是否完备？（见comparison.json中的回溯检查）
- 你有没有发现程序遗漏的闭元素？（如果有，说明形式上下文有遗漏）

#### 审计项3：trace去冗余
- 有没有两个trace描述的是同一个思维模式？如果有，合并。
- 有没有trace太具体（只适用于这道题）？如果有，考虑是否能泛化。
- **去冗余不要过度**：不同抽象层级的trace不要合并。local（来自闭元素）、nonlocal（跨段思维模式）、global（贯穿全证明的结构骨架）、cross_case_merge（跨Case相同操作）、cross_element_meta_pattern（跨闭元素元模式）是5个不同的抽象视角。同一个模式从不同抽象视角看会得到不同类型的trace——这些不要合并，它们各自有泛化价值。

#### 审计项4：trace描述质量
- 每个trace的描述是否在"具体"和"抽象"之间？
- 太具体："Case 1中用鸽巢论证找r"——只适用于这道题
- 太抽象："存在性构造"——太宽泛，匹配不到具体tell
- 合适："鸽巢论证找存在性元素：构造注入映射+计数"——具体到注入映射，抽象到可泛化

#### 审计项5：最有价值trace
- 选出最有价值的3-5个trace
- 什么算"最有价值"：可泛化性高（能匹配到很多tell）+ 揭示证明的核心策略

#### 审计项6-9：复杂情况检查
- 嵌套的结构？跨域构造？反证法+归约？构造-分析-排除？探索-诊断-修复循环？辅助函数+非负性约束？模分析无尽追逐？段之间有依赖关系？
- 如果有，确保这些复杂情况被trace捕获了

### 3. 识别AI优势元素

**AI优势元素**：程序做不了的语义判断。对每个跨闭元素元模式和跨Case非相邻合并，判断：
- FCA能做什么？（枚举出哪些闭元素/特征共现）
- AI能做什么？（识别什么语义层面的元模式，程序看不到的）
- 为什么AI能识别而程序不能？

### 4. 列举关键实体

从所有trace中提炼关键实体——贯穿多个段的变量/技巧/策略：
- 实体名称、类型（变量/技巧/策略/概念）
- 涉及哪些段
- 是否构成元模式
- 如果是元模式，描述元模式

### 5. 元反思——系统化方法的局限（必填——不允许跳过）

**注意**：伪元模式过滤和贯穿性验证已由程序自动完成，你不需要在审计中重复这两个验证。元反思聚焦于"程序无法做的判断"——回到证明本身重新审视有无遗漏。

你刚才完成了以下系统化步骤：
- 闭元素枚举（程序完成，完备）
- nonlocal trace识别（阶段3完成，从段内容出发，不依赖闭元素）
- 闭元素语义解读（阶段2完成，可能遗漏）
- 跨闭元素元模式识别（阶段2完成，靠直觉，不完备）
- 跨Case非相邻合并识别（阶段3完成，靠直觉，不完备）
- global trace识别（阶段3完成，靠直觉，不完备）

**请你再审视一遍被分析的证明内容**：

回到证明本身（不是回到你的结构化产出），重新读一遍解答。抛开你已有的段划分、闭元素、关键实体列表，用"新鲜的眼光"看这个证明：
- 这个证明的**整体策略**是什么？它是否已经被你的某个trace捕获？
- 这个证明中有没有**三个Case的递进关系**？这种递进是否已经被捕获？
- 这个证明中有没有**两种策略的对比**（如预防性避障 vs 修复性避障）？这种对比是否已经被捕获？
- 有没有某个你**没列举的关键实体**，重新审视后发现它其实贯穿了多个段？
- 有没有某个思维模式，它不属于任何已知的trace类型，但它确实有数学思维上的价值？

**如果你发现了新trace**：
- 补充到traces列表中
- 在JSON输出的`meta_reflection_traces`字段中记录
- 说明为什么前面的系统化步骤没覆盖到它

**如果你没有发现新trace**：
- 明确说明"经元反思审视，未发现系统化步骤未覆盖的有价值trace"

## 产出格式

填充 `output.json`：

```json
{
  "phase": "synthesis",
  "problem_id": "题目ID",
  "base_grading": "你选择的基础格化版本（如V10）",
  "grading_comparison": "4个版本格化对比的简述",
  "formal_context_review": {
    "is_complete": true,
    "corrections": [
      {"version": "V10", "reason": "修正原因", "change": "修正了什么"}
    ]
  },
  "closed_elements": [
    {"id": "ce_1", "extent": ["段1"], "intent": ["特征1"], "source_version": "V10", "judgment": "included", "trace_description": "trace描述", "reason": "入选理由"}
  ],
  "traces": [
    {"id": "trace_1", "type": "local/nonlocal/global/cross_case_merge/cross_element_meta_pattern", "level": "L2", "segments": ["段1"], "description": "trace描述", "generalizable": true, "is_ai_advantage": false}
  ],
  "ai_advantage_elements": [
    {"id": "adv_1", "advantage_type": "cross_case_merge/cross_element_meta_pattern", "description": "AI优势元素描述", "segments": ["段11"], "reason": "为什么FCA找不到这个但AI能识别"}
  ],
  "key_entities": [
    {"name": "x", "type": "变量", "segments": ["段2"], "is_meta_pattern": true, "meta_pattern_description": "如果是元模式，描述"}
  ],
  "meta_reflection_traces": [
    {"id": "mrt_1", "description": "元反思发现的新trace描述", "pattern_type": "递进/对比/闭环/生命周期/同构异构/其他", "reason": "为什么前面的系统化步骤没覆盖到"}
  ],
  "most_valuable_traces": ["trace_1", "trace_5", "trace_3"]
}
```

同时填充 `output.md`——人类可读的完整分析报告，包含：
1. 4个版本格化对比
2. 形式上下文回溯检查结果
3. 闭元素清单（每个闭元素的入选/排除判定）
4. trace列表（每个trace的描述和理由）
5. AI优势元素
6. 关键实体
7. 审计报告
8. 元反思结果
9. 最有价值trace

## 完成后

填充完 `output.json` 和 `output.md` 后，创建 `step4_done.md`（空文件）作为完成标记。

然后创建 `DONE.md`（空文件）作为全部完成的信号。
