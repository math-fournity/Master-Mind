# 阶段1要求：对比+回溯检查

## 你要做的

读取 `grading/`目录下的4版本格化结果和 `closed_elements/`目录下的闭元素清单，综合对比4版本，选择基础格化，做形式上下文回溯检查。

## 详细步骤

### 1. 综合对比4个版本的格化

读4个版本的segments.json和formal_context.json，对比：
- 4个版本的段划分有什么不同？（段数、段边界、段特征标注）
- 4个版本的形式上下文有什么不同？（特征数、特征名称、特征粒度）
- 这些不同反映了什么"看法差异"？

### 2. 选择基础格化

以哪个版本的格化为基础做trace识别？还是合并多个版本的格化？这是你的认知判断。

选择理由需要记录——为什么选这个版本？它的段划分/特征标注有什么优势？

**可以补充其他版本的特征**——如果选择V10为基础，但V8有某些V10缺少的角色特征，可以补充。

### 3. 形式上下文回溯检查

程序枚举闭元素是给定(G,M,I)的确定性运算——给定形式上下文，Next Closure算法枚举所有满足A''=A的子集A，一个不漏。这个运算是完备的。

**但(G,M,I)本身可能不完美**——阶段1的AI在做段划分和特征标注时可能遗漏：
- 段的特征标注不够准确——某个段应该有"构造性证明"特征，但AI漏标了
- 特征粒度不合适——太粗导致闭元素太少；太细导致闭元素太多
- 同一思维特征用了不同名称——"鸽巢论证"有时写"鸽巢原理"有时写"抽屉原理"

**回溯检查**：
1. **完备性检查**：有没有"在思维上属于同一层的段集合"没有被程序枚举到？
   - 如果有：说明形式上下文的特征标注有遗漏 → 诊断遗漏原因 → 记录修正建议
   - 如果没有：形式上下文完备，继续
2. **多版本交叉验证**：对比4个版本的闭元素清单，如果某个版本枚举出了其他版本没有的闭元素，检查其他版本的特征标注是否遗漏

## 产出格式

填充 `comparison.json`：

```json
{
  "phase": "synthesis_step1",
  "base_grading": "V10",
  "version_comparison": {
    "V5": {"segments": 26, "features": "描述性，无形式上下文", "closed_elements": null, "characteristic": "自由直觉段划分"},
    "V7": {"segments": 21, "features": 15, "closed_elements": 23, "characteristic": "结构化约束"},
    "V8": {"segments": 22, "features": 40, "closed_elements": 39, "characteristic": "跨闭元素元模式引导"},
    "V10": {"segments": 35, "features": 26, "closed_elements": 52, "characteristic": "显式元模式编码"}
  },
  "viewpoint_differences": [
    "V5→V7: ...",
    "V7→V8: ...",
    "V8→V10: ..."
  ],
  "base_grading_rationale": "选择V10的理由...",
  "supplementary_features": "需要从其他版本补充的特征...",
  "formal_context_review": {
    "is_complete": true,
    "issues": [
      {"issue": "段10标注错误", "correction": "应改为s的代数角色", "version": "V10"},
      {"issue": "验证特征过粗", "correction": "应拆分为前缀和验证+终点验证", "version": "V10"}
    ]
  }
}
```

## 完成后

填充完 `comparison.json` 后，创建 `step1_done.md`（空文件）作为完成标记。
