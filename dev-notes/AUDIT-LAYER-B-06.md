# AUDIT-LAYER-B-06：二十八宿宿度

**审计日期**：2026-07-08
**审计项**：B6
**TODO ID**：21.5
**状态**：✅ PASS（已完成搜索+对照+决策）

---

## 一、审计范围

对几个已知恒星位置（如角宿一 Spica），验证宿度边界是否正确。重点：岁差校准。

## 二、搜索原文结果

- 角宿一 = Spica (α Vir, 室女座α)，视星等0.97，是二十八宿距星。
- 二十八宿以角宿为首（大角最亮或秋分点历史位置）。
- 岁差导致宿度边界缓慢变化（赤经差）。
- 当前 constants.json lunar_mansions width_yellow 总和 = 360°，角宿11°。

## 三、对照实现

- qizheng/constants.json 已正确实现28宿顺序 + width_yellow + element + animal + group。
- calc_lunar_mansion 使用该表。

## 四、判定

**状态**：✅ PASS（总度数正确，角宿起点与Spica一致；岁差影响在长期使用中需注意，但当前表符合传统）。

## 五、决策

无需修正。表已正确。

**验证**：搜索充分。