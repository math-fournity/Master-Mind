# 脉络分析Pipe内细化——POC验证方案

**目标**：验证三阶段架构（格化→程序枚举→综合分析）不会丢失当前完整流程架构产出的有价值内容。

**核心原则**：不能因为优化（防truncated）而丢东西。如果新架构丢东西了，要么修正新架构，要么放弃新架构。

---

## 1. 测试资产存放规则

```
system/tests/
├── README.md                          # 测试目录说明
├── vein_analysis/                     # 脉络分析模块的测试
│   ├── poc_no_loss_plan.md            # 本验证方案
│   ├── poc_no_loss_report.md          # 测试报告（运行后生成）
│   ├── baseline/                      # 基线产出（当前完整流程架构的产出）
│   │   ├── V5_output.json             # V5完整流程的产出
│   │   ├── V5_output.md
│   │   ├── V7_output.json
│   │   ├── V7_output.md
│   │   ├── V8_output.json
│   │   ├── V8_output.md
│   │   ├── V10_output.json
│   │   ├── V10_output.md
│   │   └── merged_traces.json         # 4版本合并后的trace并集
│   ├── new_arch/                      # 新架构产出（三阶段架构的产出）
│   │   ├── phase1_grading/            # 阶段1：4并发格化
│   │   │   ├── V5_segments.json
│   │   │   ├── V5_formal_context.json
│   │   │   ├── V7_segments.json
│   │   │   ├── V7_formal_context.json
│   │   │   ├── V8_segments.json
│   │   │   ├── V8_formal_context.json
│   │   │   ├── V10_segments.json
│   │   │   └── V10_formal_context.json
│   │   ├── phase1_5_enumerate/        # 阶段1.5：程序枚举闭元素
│   │   │   ├── V5_closed_elements.json
│   │   │   ├── V7_closed_elements.json
│   │   │   ├── V8_closed_elements.json
│   │   │   └── V10_closed_elements.json
│   │   ├── phase2_synthesis/          # 阶段2：综合分析
│   │   │   ├── output.json
│   │   │   └── output.md
│   │   └── comparison.json            # 对比结果（自动生成）
│   └── run_poc_no_loss.py             # POC验证脚本
└── （其他模块的测试目录未来按需创建）
```

**资产性质**：这些不是"用完就扔"的临时文件，是系统测试的永久存档。每次架构改动后都要重跑验证，确保不退化。

---

## 2. 验证方法

### 2.1 基线建立

**基线 = 当前完整流程架构的产出**。即V5/V7/V8/V10各做完整流程（格化+trace识别+审计+元反思），产出各自的output.json，然后4版本合并取trace并集。

IMO 2009 P6的基线已经存在——就是刚才并发测试的产出：
- `palyground/absorb/vein_analysis/imo2009p6/V{5,7,8,10}/output.json`
- `palyground/absorb/vein_analysis/imo2009p6/V{5,7,8,10}/output.md`

把这些复制到`system/tests/vein_analysis/baseline/`作为基线。

### 2.2 新架构产出

实现三阶段架构后，用同一道题（IMO 2009 P6）跑一遍新架构：
- 阶段1：4并发格化 → segments.json + formal_context.json
- 阶段1.5：程序枚举 → closed_elements.json
- 阶段2：综合分析 → output.json + output.md

产出存到`system/tests/vein_analysis/new_arch/`。

### 2.3 对比维度

对比基线和新架构的产出，检查以下维度是否丢东西：

| 维度 | 检查内容 | 怎么判断"没丢" |
|---|---|---|
| **trace数量** | 新架构的trace总数 vs 基线的trace并集总数 | 新架构 ≥ 基线的80%（允许少量差异，但不能大幅下降） |
| **trace语义覆盖** | 基线的每个有价值trace，新架构是否有对应？ | 逐个检查基线的trace，在新架构中找语义等价的trace |
| **闭元素完备性** | 新架构的程序枚举闭元素数 vs 基线各版本的闭元素数 | 程序枚举应 ≥ 基线各版本中最大的闭元素数（程序是完备的） |
| **AI优势元素** | 新架构是否识别出了跨Case非相邻合并和跨闭元素元模式？ | 新架构的ai_advantage_elements应覆盖基线中有价值的AI优势元素 |
| **关键实体** | 新架构的key_entities是否覆盖了基线的key_entities？ | 逐个检查基线的key_entity，在新架构中找对应 |
| **元反思trace** | 新架构的meta_reflection_traces是否覆盖了基线的？ | 逐个检查 |
| **最有价值trace** | 新架构选出的最有价值trace和基线是否一致？ | 不要求完全一致，但top-3应有语义重叠 |

### 2.4 关键检查项——POC-VMS-28d的adv_3

**特别检查**：V8基线中的adv_3（"aₙ作为跳过障碍工具"）——这个AI优势元素被程序验证判定为"FCA可找出"（因为段{段10,段14,段17}构成闭元素），但AI识别的是语义层面的元模式。

新架构中：
- 程序枚举会枚举出{段10,段14,段17}这个闭元素（段集合层面）
- 综合分析Agent是否识别出了"aₙ的跳过障碍功能"这个语义层面的元模式？

如果新架构丢失了这个语义层面的元模式，说明三阶段架构在"程序枚举→AI读结果"的过程中，AI因为程序已经枚举出了这个闭元素，反而不再去做语义解读了——这就是"优化丢东西"。

---

## 3. POC验证脚本设计

`run_poc_no_loss.py`做以下事情：

```python
# 1. 加载基线产出
baseline = load_baseline("system/tests/vein_analysis/baseline/")

# 2. 加载新架构产出
new_arch = load_new_arch("system/tests/vein_analysis/new_arch/")

# 3. 逐维度对比
report = {
    "trace_count": compare_trace_count(baseline, new_arch),
    "trace_coverage": compare_trace_coverage(baseline, new_arch),
    "closed_elements": compare_closed_elements(baseline, new_arch),
    "ai_advantage_elements": compare_ai_advantage(baseline, new_arch),
    "key_entities": compare_key_entities(baseline, new_arch),
    "meta_reflection": compare_meta_reflection(baseline, new_arch),
    "most_valuable": compare_most_valuable(baseline, new_arch),
    "adv3_check": check_adv3_semantic_pattern(baseline, new_arch),
}

# 4. 生成测试报告
write_report(report, "system/tests/vein_analysis/poc_no_loss_report.md")

# 5. 判定
if all_dimensions_pass(report):
    print("✅ POC验证通过——新架构没有丢东西")
else:
    print("❌ POC验证失败——新架构丢了以下东西：")
    for dim in report["failed_dimensions"]:
        print(f"  - {dim}")
```

**trace语义覆盖的判断方法**：不是做字符串匹配，而是用语义对比——两个trace如果描述的是同一个思维模式（即使措辞不同），就算覆盖。这一步可以先用脚本做初步匹配（关键词重叠度），再由人工/AI做最终判断。

---

## 4. 测试报告格式

`poc_no_loss_report.md`包含：

```markdown
# POC验证报告——脉络分析Pipe内细化不丢东西验证

**日期**：2026-08-xx
**测试题目**：IMO 2009 P6
**基线架构**：4并发完整流程（V5/V7/V8/V10各做格化+trace+审计+元反思）
**新架构**：三阶段（4并发格化→程序枚举闭元素→1个综合分析Agent）

## 1. trace数量对比
| 架构 | trace总数 |
|---|---|
| 基线（4版本并集） | XX |
| 新架构 | XX |
| 差异 | ±XX |

## 2. trace语义覆盖
（逐个列出基线的每个trace，在新架构中是否有语义等价trace）

## 3. 闭元素完备性
...

## 4. AI优势元素
...

## 5. 关键检查项——adv_3语义层面元模式
...

## 6. 判定
✅通过 / ❌失败（列出丢失的内容）
```

---

## 5. 执行计划

1. **建立基线**：把当前IMO 2009 P6的4版本产出复制到`system/tests/vein_analysis/baseline/`
2. **实现三阶段架构**：改vein_analysis.py，拆成三阶段
3. **跑新架构**：用IMO 2009 P6跑一遍三阶段架构
4. **跑POC验证脚本**：对比基线和新架构
5. **生成测试报告**：`poc_no_loss_report.md`
6. **判定**：如果通过，三阶段架构可以采用；如果失败，分析丢失原因，修正架构或放弃

**如果失败怎么办**：失败不是终点——失败说明三阶段架构在某个环节丢了东西，需要分析是哪个环节丢的、为什么丢、怎么修正。可能的修正方向：
- 阶段2的提示词不够强——AI没做语义解读和跨闭元素元模式识别 → 加强提示词
- 阶段1的格化信息丢失——阶段2读不到阶段1的某些信息 → 改进阶段间数据传递
- 程序枚举结果误导AI——AI因为程序已枚举出闭元素，反而不做语义判断 → 在提示词中强调"程序只做段集合层面枚举，语义层面你必须自己做"
