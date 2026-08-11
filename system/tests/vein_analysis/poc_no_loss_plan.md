# 脉络分析Pipe内细化——POC验证方案

**目标**：验证三阶段架构（格化→程序枚举→综合分析）不会丢失当前完整流程架构产出的有价值内容。

**核心原则**：不能因为优化（防truncated）而丢东西。如果新架构丢东西了，要么修正新架构，要么放弃新架构。

**测试题目**：IMO 2009 P6（蚱蜢问题）——和之前V5/V7/V8/V9/V10各版本开发时用的同一道题。之前每个版本开发时都做了POC验证，数据全部留存，可以作为对比基准。

---

## 1. 之前POC留存的对比数据

之前4个版本开发时，每次都做了POC验证并留存了对比分析文档。这些是已有的对比基准：

| POC | 对比对象 | 留存文件 | 关键发现 |
|---|---|---|---|
| VMS-28c | V5 vs V7 | `vms28c_v5_v7_trace_comparison.md` | V7从V5的38个trace减到19个，去冗余有效但漏了3个有价值trace（trace_31/32/33） |
| VMS-28c | V7程序验证 | `vms28c_audit_report.json` | V7闭元素完备性100%（15/15），21个段12个特征 |
| VMS-28c | V5/V7产出 | `vms28c_subagent_output.json/md` | V5/V7的完整output |
| VMS-28d | V5 vs V8 | `vms28d_v5_v8_trace_comparison.md` | V8补回了V7漏掉的trace_31/33，adv_3被程序判定为"FCA可找出"但AI识别的是语义层面元模式 |
| VMS-28e | V5 vs V8 vs V9 | `vms28e_v5_v8_v9_trace_comparison.md` | V9元反思发现5个新trace（mrt_1~5），adv_3伪元模式问题 |

**这些留存文件的位置**：`第六代系统研发过程文档/`

**另外**，刚才4并发完整流程的产出也作为基线：
- `system/tests/vein_analysis/baseline/V{5,7,8,10}_output.json`——4版本各自的完整产出
- 基线数据摘要：93个trace并集、69个闭元素并集、21个AI优势元素并集、11个关键实体并集、2个元反思trace

---

## 2. 测试资产存放规则

```
system/tests/vein_analysis/
├── poc_no_loss_plan.md            # 本验证方案
├── poc_no_loss_report.md          # 测试报告（运行后生成）
├── run_poc_no_loss.py             # POC验证脚本
├── baseline/                      # 基线产出（当前完整流程架构）
│   ├── V5_output.json
│   ├── V5_output.md
│   ├── V7_output.json
│   ├── V7_output.md
│   ├── V8_output.json
│   ├── V8_output.md
│   ├── V10_output.json
│   └── V10_output.md
├── prior_poc/                     # 之前POC留存的对比数据（复制副本）
│   ├── vms28c_v5_v7_trace_comparison.md
│   ├── vms28c_audit_report.json
│   ├── vms28c_subagent_output.json
│   ├── vms28c_subagent_output.md
│   ├── vms28d_v5_v8_trace_comparison.md
│   └── vms28e_v5_v8_v9_trace_comparison.md
└── new_arch/                      # 新架构产出（三阶段架构）
    ├── phase1_grading/            # 阶段1：4并发格化——全部留存
    │   ├── V5_segments.json
    │   ├── V5_formal_context.json
    │   ├── V7_segments.json
    │   ├── V7_formal_context.json
    │   ├── V8_segments.json
    │   ├── V8_formal_context.json
    │   ├── V10_segments.json
    │   └── V10_formal_context.json
    ├── phase1_5_enumerate/        # 阶段1.5：程序枚举闭元素——全部留存
    │   ├── V5_closed_elements.json
    │   ├── V7_closed_elements.json
    │   ├── V8_closed_elements.json
    │   └── V10_closed_elements.json
    ├── phase2_synthesis/          # 阶段2：综合分析——全部留存
    │   ├── output.json
    │   └── output.md
    └── comparison.json            # 对比结果（自动生成）
```

**资产性质**：永久存档，不是用完就扔。每次架构改动后重跑验证。

**中间结果全部留存**：阶段1的4个格化session的segments.json和formal_context.json、阶段1.5的4个closed_elements.json、阶段2的output.json和output.md，全部存到`new_arch/`下对应的子目录，文件可查。

---

## 3. 验证方法

### 3.1 基线

**基线 = 当前完整流程架构的产出**，有两个来源：

1. **4并发完整流程的产出**（`baseline/V{5,7,8,10}_output.json`）——V5/V7/V8/V10各做完整流程的产出
2. **之前POC留存的对比数据**（`prior_poc/`）——VMS-28c/d/e的对比分析文档

两个来源互相补充：基线产出提供完整的JSON数据用于程序化对比，之前POC数据提供人工分析的对比结论用于语义层面验证。

### 3.2 新架构产出

实现三阶段架构后，用同一道题（IMO 2009 P6）跑一遍新架构：
- 阶段1：4并发格化 → segments.json + formal_context.json（4版本各一套）
- 阶段1.5：程序枚举 → closed_elements.json（4版本各一套）
- 阶段2：综合分析 → output.json + output.md

**所有中间结果全部存到`new_arch/`下，文件可查**。

### 3.3 对比维度——从哪些维度考察

对比基线和新架构的产出，从以下维度检查是否丢东西：

#### 维度1：trace数量

| 检查内容 | 怎么判断"没丢" |
|---|---|
| 新架构trace总数 vs 基线4版本trace并集总数（93） | 新架构 ≥ 基线的80% |
| 新架构trace总数 vs 之前POC各版本trace数（V5:38, V7:19, V8:18, V9:23, V10:26） | 新架构应在V9/V10的23-26个量级，不应降到V7/V8的18-19个 |

#### 维度2：trace语义覆盖——逐个检查基线的有价值trace

**基线中有价值trace清单**（来自之前POC留存数据）：

| trace | 描述 | 来源版本 | 之前POC的判定 | 新架构必须覆盖 |
|---|---|---|---|---|
| trace_33 | 关键变量x贯穿整个证明 | V5 | V7漏掉，V8补回（最有价值第2名），V9保留 | ✅ 必须 |
| trace_31 | 最大元素aₙ作为跳过障碍的工具 | V5 | V7漏掉，V8补回（最有价值第1名），V9伪元模式争议 | ✅ 必须（语义层面） |
| trace_32 | 归纳递降的三种方式 | V5 | V7部分漏掉，V8部分补回，V9保留 | ⚠️ 至少部分覆盖 |
| mrt_1 | Case复杂度阶梯递进 | V9元反思 | V5有对应（trace_19），V9更完整 | ✅ 必须 |
| mrt_2 | 预防性避障vs修复性避障 | V9元反思 | V5部分对应（trace_30），V9更完整 | ✅ 必须 |
| mrt_3 | WLOG排序闭环 | V9元反思 | V5没有——V9新发现 | ✅ 必须 |
| mrt_4 | 好index r的完整生命周期 | V9元反思 | V5没有——V9新发现 | ✅ 必须 |
| mrt_5 | 三Case同构框架与异构处理 | V9元反思 | V5部分对应（trace_29），V9更完整 | ✅ 必须 |

**判定标准**：上表中标"✅ 必须"的trace，新架构必须有语义等价trace。标"⚠️ 至少部分覆盖"的trace，新架构至少有部分语义覆盖。

#### 维度3：闭元素完备性

| 检查内容 | 怎么判断"没丢" |
|---|---|
| 新架构程序枚举闭元素数 vs 基线各版本闭元素数 | 程序枚举应 ≥ 基线各版本中最大的闭元素数 |
| 新架构程序枚举闭元素数 vs VMS-28c审计报告的15个闭元素 | 程序枚举应 ≥ 15（VMS-28c的V7有15个闭元素，完备性100%） |
| 形式上下文的段数和特征数 vs VMS-28c审计报告（21段12特征） | 段数应在20-22范围，特征数应在10-14范围 |

#### 维度4：AI优势元素——跨Case非相邻合并和跨闭元素元模式

**基线中有价值的AI优势元素清单**（来自之前POC留存数据）：

| AI优势元素 | 类型 | 来源版本 | 之前POC的判定 | 新架构必须覆盖 |
|---|---|---|---|---|
| swap技巧跨Case复用 | 跨Case非相邻合并 | V7/V8 | V7的adv_1，V8保留 | ✅ 必须 |
| 四步元模式跨Case复用 | 跨Case非相邻合并 | V7/V8 | V7的adv_2，V8保留 | ✅ 必须 |
| 关键变量x贯穿整个证明 | 跨闭元素元模式 | V8 | V8的adv_1（trace_16），最有价值第2名 | ✅ 必须 |
| aₙ作为跳过障碍工具 | 跨闭元素元模式 | V8 | V8的adv_2（trace_17），最有价值第1名，adv_3伪元模式争议 | ✅ 必须（语义层面） |
| 强归纳作为结构骨架 | 跨闭元素元模式 | V8/V9 | V8的adv_4，V9保留 | ✅ 必须 |

**判定标准**：上表中所有AI优势元素，新架构必须有语义等价识别。

#### 维度5：关键实体

| 检查内容 | 怎么判断"没丢" |
|---|---|
| 新架构key_entities vs 基线4版本key_entities并集（11个） | 遗漏 ≤ 20%（最多漏2个） |
| 新架构key_entities vs V9的13个关键实体 | 新架构应覆盖V9的关键实体（x、aₙ、强归纳、r、M'、bad index等） |

#### 维度6：元反思trace

| 检查内容 | 怎么判断"没丢" |
|---|---|
| 新架构meta_reflection_traces vs V9的5个元反思trace（mrt_1~5） | 新架构应覆盖V9的5个元反思trace——这些是V9元反思步骤发现的新trace，新架构的元反思步骤也应该能发现 |
| 新架构是否有元反思步骤 | 必须有——如果新架构没有元反思步骤，说明审计项10被丢了 |

#### 维度7：adv_3语义层面元模式（关键中的关键）

**POC-VMS-28d的实证发现**：V8的adv_3（"aₙ作为跳过障碍工具"）被程序验证判定为"FCA可找出"——因为段{段10,段14,段17}恰好构成闭元素。但AI识别的是语义层面的元模式（aₙ的统一"跳过障碍"角色），不是段集合层面的闭包运算。

**新架构中的检查**：
1. 程序枚举会枚举出{段10,段14,段17}这个闭元素（段集合层面）
2. 综合分析Agent是否识别出了"aₙ的跳过障碍功能"这个语义层面的元模式？
3. 如果综合分析Agent因为程序已经枚举出了这个闭元素，反而不做语义解读了——这就是"优化丢东西"

**判定标准**：新架构必须在语义层面识别出"aₙ的跳过障碍功能"，不能只停留在段集合层面。

#### 维度8：最有价值trace

| 检查内容 | 怎么判断"没丢" |
|---|---|
| 新架构选出的最有价值trace vs 基线各版本的最有价值trace | top-3应有语义重叠 |
| 新架构最有价值trace vs V8的top-2（aₙ跳过障碍第1名、x贯穿第2名） | 新架构的top-2应包含这两个语义 |

#### 维度9：阶段间信息传递完整性

**这是新架构特有的维度**——检查三阶段之间的信息传递是否完整：

| 检查内容 | 怎么判断"没丢" |
|---|---|
| 阶段1的段划分信息是否完整传递到阶段2 | 阶段2的output.json中的段划分应和阶段1的segments.json一致 |
| 阶段1.5的闭元素枚举是否完整传递到阶段2 | 阶段2的output.json中的闭元素应和阶段1.5的closed_elements.json一致 |
| 阶段2是否做了形式上下文回溯检查（§2.4.1） | 阶段2的output.json中应有回溯检查记录 |
| 阶段2是否做了闭元素语义解读（§2.4.2） | 阶段2的output.json中每个闭元素应有语义解读，不只是入选/排除 |

---

## 4. POC验证脚本设计

`run_poc_no_loss.py`做以下事情：

```python
# 1. 加载基线产出
baseline = load_baseline("system/tests/vein_analysis/baseline/")

# 2. 加载之前POC留存数据
prior_poc = load_prior_poc("system/tests/vein_analysis/prior_poc/")

# 3. 加载新架构产出（包括中间结果）
new_arch = load_new_arch("system/tests/vein_analysis/new_arch/")

# 4. 逐维度对比（9个维度）
report = {
    "trace_count": compare_trace_count(baseline, new_arch),
    "trace_coverage": compare_trace_coverage(baseline, prior_poc, new_arch),
    "closed_elements": compare_closed_elements(baseline, prior_poc, new_arch),
    "ai_advantage": compare_ai_advantage(baseline, prior_poc, new_arch),
    "key_entities": compare_key_entities(baseline, new_arch),
    "meta_reflection": compare_meta_reflection(baseline, prior_poc, new_arch),
    "adv3_check": check_adv3_semantic_pattern(baseline, prior_poc, new_arch),
    "most_valuable": compare_most_valuable(baseline, new_arch),
    "phase_transfer": check_phase_transfer_integrity(new_arch),
}

# 5. 生成测试报告
write_report(report, "system/tests/vein_analysis/poc_no_loss_report.md")

# 6. 判定
if all_dimensions_pass(report):
    print("✅ POC验证通过——新架构没有丢东西")
else:
    print("❌ POC验证失败——新架构丢了以下东西：")
    for dim in report["failed_dimensions"]:
        print(f"  - {dim}")
```

**trace语义覆盖的判断方法**：不是做字符串匹配，而是用语义对比——两个trace如果描述的是同一个思维模式（即使措辞不同），就算覆盖。这一步先用脚本做初步匹配（关键词重叠度），再由人工/AI做最终判断。

**之前POC数据的用法**：prior_poc中的对比分析文档（vms28c/d/e）提供了人工分析的对比结论——哪些trace是有价值的、哪些是V7漏掉的、哪些是V8补回的、哪些是V9元反思新发现的。这些结论用于验证新架构是否覆盖了之前POC确认的有价值内容。

---

## 5. 测试报告格式

`poc_no_loss_report.md`包含：

```markdown
# POC验证报告——脉络分析Pipe内细化不丢东西验证

**日期**：YYYY-MM-DD HH:MM
**测试题目**：IMO 2009 P6（蚱蜢问题）
**基线架构**：4并发完整流程（V5/V7/V8/V10各做格化+trace+审计+元反思）
**新架构**：三阶段（4并发格化→程序枚举闭元素→1个综合分析Agent）
**之前POC基准**：VMS-28c（V5 vs V7）、VMS-28d（V5 vs V8）、VMS-28e（V5 vs V8 vs V9）

## 总判定
✅通过 / ❌失败（列出失败的维度）

## 1. trace数量对比
（新架构 vs 基线4版本并集 vs 之前POC各版本）

## 2. trace语义覆盖
（逐个列出基线中有价值trace在新架构中的覆盖情况，参照之前POC的对比结论）

## 3. 闭元素完备性
（新架构程序枚举 vs 基线各版本 vs VMS-28c审计报告）

## 4. AI优势元素
（新架构 vs 基线中有价值的AI优势元素清单）

## 5. 关键实体
（新架构 vs 基线 vs V9的13个关键实体）

## 6. 元反思trace
（新架构 vs V9的5个元反思trace mrt_1~5）

## 7. adv_3语义层面元模式（关键中的关键）
（新架构是否在语义层面识别出"aₙ跳过障碍"）

## 8. 最有价值trace
（新架构top-3 vs 基线各版本top-3）

## 9. 阶段间信息传递完整性
（阶段1→阶段1.5→阶段2的信息传递是否完整）

## 10. 判定
✅通过 / ❌失败（列出丢失的内容和可能原因）
```

---

## 6. 执行计划

1. ✅ **基线已建立**——4版本产出已复制到`baseline/`
2. **复制之前POC数据**——把vms28c/d/e的对比分析文档复制到`prior_poc/`
3. **实现三阶段架构**——改vein_analysis.py，拆成三阶段
4. **跑新架构**——用IMO 2009 P6跑一遍三阶段架构，**所有中间结果存到`new_arch/`**
5. **跑POC验证脚本**——`python3 system/tests/vein_analysis/run_poc_no_loss.py`
6. **检查测试报告**——`poc_no_loss_report.md`的判定结果
7. **如果失败**——分析丢失原因，修正架构，重跑验证

**如果失败怎么办**：失败不是终点——失败说明三阶段架构在某个环节丢了东西，需要分析是哪个环节丢的、为什么丢、怎么修正。可能的修正方向：
- 阶段2的提示词不够强——AI没做语义解读和跨闭元素元模式识别 → 加强提示词
- 阶段1的格化信息丢失——阶段2读不到阶段1的某些信息 → 改进阶段间数据传递
- 程序枚举结果误导AI——AI因为程序已枚举出闭元素，反而不做语义判断 → 在提示词中强调"程序只做段集合层面枚举，语义层面你必须自己做"
- 元反思步骤丢失——阶段2的提示词中没有审计项10 → 补上元反思步骤
