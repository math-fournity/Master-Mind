# Java 方法审计与翻译缺口表

**状态**：⏳ TODO（占位，待执行）
**创建时间**：2026-07-15
**触发原因**：Phase 1-3 收口后，用户提问"你对原来 repo 代码中的所有内容都翻译了吗？所有功能都充分暴露给自己了吗？"，诚实审计后发现翻译覆盖率约 30%，且 AGENTS.md 未记录完整未翻译清单，下一个 session 会误判进度。

---

## 一、任务目标

对 MOIRA Java 原代码做一次**完整方法级审计**，产出：

1. **Java 方法全清单**：Calculate.java（59公开）+ ChartData.java（66公开+52私有计算）+ EvalRule.java（20公开）+ RuleEntry.java（30+公开+24内置函数）+ 其他 base/ 文件
2. **翻译状态表**：每个方法标记 ✅已翻译 / ⚠️部分翻译 / ❌未翻译 / 🗑️GUI不需要
3. **moira_s.prop key 全清单**：1136 个顶级 key，命理相关 59 个，已提取 6 个，列出未提取的 53 个命理 key
4. **未翻译功能块清单**：按重要性排序的 20 个重大未翻译功能块
5. **AGENTS.md 回写**：把缺口表摘要回写到 AGENTS.md，让下一个 session 看到真实进度

## 二、执行步骤

- [ ] **步骤1**：更新 dev-notes/06-功能模块完整盘点.md 的过时状态标记（EvalRule 已部分研究、Calculate 升落已翻译、ChartData 命宫身宫已翻译等）
- [ ] **步骤2**：Calculate.java 59 公开方法逐个标记翻译状态
- [ ] **步骤3**：ChartData.java 66 公开 + 52 私有计算方法逐个标记翻译状态
- [ ] **步骤4**：EvalRule.java 20 公开方法 + RuleEntry.java 24 内置函数标记翻译状态
- [ ] **步骤5**：moira_s.prop 59 命理 key 列出已提取/未提取
- [ ] **步骤6**：20 个未翻译功能块按重要性排序，标注依赖关系
- [ ] **步骤7**：缺口表摘要回写 AGENTS.md 的"已知 TODO"和"核心库对照表"
- [ ] **步骤8**：更新 dev-docs/00-七政四余推命系统建设计划.md 的 Phase 4+ 规划

## 三、初步发现（待审计确认）

基于本轮已做的快速审计：

| 模块 | 原代码规模 | 已翻译 | 覆盖率 |
|---|---|---|---|
| Calculate.java | 2340行, 59公开方法 | ~20方法 | ~50% |
| ChartData.java | 9424行, 52私有计算方法 | ~8方法 | ~22% |
| EvalRule.java | 800行, 20公开方法 | 1方法（简化版） | ~33% |
| RuleEntry.java | 1697行, 24内置函数 | 0函数 | 0% |
| RuleParse.java | 1019行（解析器） | 0 | 0% |
| moira_s.prop 命理key | 59个 | 6个 | ~10% |
| moira_s.prop 全部key | 1136个 | 24个 | ~2% |

**20 个重大未翻译功能块**（初步识别，待审计确认）：

1. 八字系统（computeEightCharData）- 长生/十神/纳音/弱宫/强宫
2. 神煞完整体系（getStarSigns）- 天乙/玉堂/紫微/禄勋/驿马/华盖/斗杓/岁驾...
3. 流年神煞（getYearInfo/getYearStar）- 年神/天官/地官/水官
4. 流年推演（computeNowData）- 流年盘
5. 推运系统（computeTransitData）- 流年推运/相位/过宫
6. 返照系统（computeSolarReturn/computeLunarReturn）
7. 主限/次限推运（computePrimaryDirection/computeSecondaryProgression）
8. 日月食计算（computeEclipse）
9. 三煞（computeThreeDanger）
10. 太岁/年神（computeYearSign）
11. 大运/小限/月限/飞限完整实现
12. 高格林区位（computeGauquelin）
13. 恒星计算（computeStar/findStarByEquPos）
14. 方位角/高度角（computeAzimuth/getAltitude）
15. 罗盘方位（getMountain/getMountainPos）
16. 相位系统（initAspects/getAspects）
17. 规则引擎 24 个内置函数（if/eval/map/set/union/intersection/contain/iter/...）
18. 规则引擎 58 条复杂规则（模板/函数调用/算术）
19. 地方视太阳时（getLATDateFromDate）
20. 地支顺逆（getZodiacShift）

## 四、关联文档

- <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/06-功能模块完整盘点.md" /> — 已有的功能盘点（状态标记待更新）
- <ref_file file="~/MOIRA_chinese_astrology-main/AGENTS.md" /> — 项目状态，TODO 部分将索引本文档
- <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/00-七政四余推命系统建设计划.md" /> — 建设计划，Phase 4+ 规划将更新
