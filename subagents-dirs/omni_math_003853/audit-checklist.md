# Master Agent 审计 Checklist — AoPS omni_math #3853

- **problem_id**: omni_math_003853
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，IMO Shortlist 2022 C7（2022元组操作+二次多项式尖峰构造）

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——Lucy写s个整数值2022元组在黑板上，可取任意两个操作。解答：用二次多项式1-2(i-j)²构造尖峰元组（在一个坐标处等于1，其他位置≤-1），再用max操作从尖峰元组提取标准基向量。答案：3 ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.3-0.7全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+2个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R5", tb="R4"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——二次多项式1-2(i-j)²构造尖峰元组+max操作提取标准基向量 ✅
- [x] 2c. discrete_combinatorial vs constructive_generation_with_invariant区分清晰 ✅
- [x] 2d. key_insight="用二次多项式1-2(i-j)²构造尖峰元组（一个坐标等于1，其他≤-1），再用max操作提取标准基向量"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→小尝试→比例不等式不变量→二次多项式尖峰构造→max操作→综合，合理 ✅
- [x] 2f. R5 kb=True正确（二次多项式尖峰构造是知识瓶颈），R4 tb正确（比例不等式不变量是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
