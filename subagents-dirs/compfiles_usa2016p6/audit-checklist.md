# Master Agent 审计 Checklist — USA 2016 P6

- **problem_id**: compfiles_usa2016p6
- **审计时间**: 2025-01-24

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读Lean文件（1028行）——n≥k≥2，2n张卡片（每标签i两张），巫师排列后玩家每次选k张翻开，匹配则赢，否则巫师重排选中的k张。求哪些(n,k)可赢。答案：k<n。可赢方向：滑动窗口策略——查询连续k个位置的窗口滑过整行，通过相邻窗口的标签集合差推断2n-k个位置的标签，因2n-k>n用鸽巢原理找到匹配对。不可赢方向：巫师维持排列在下一次查询集上单射的不变量，利用查询集和补集都双射到所有标签的性质，总能找到合适置换。Lean中Arrangement定义排列，Valid验证每标签两次 ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.4-0.8全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+3个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R6", tb="R4"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——可赢(k<n)：滑动窗口+相邻窗口标签集合差+推断2n-k>n个位置+鸽巢找匹配；不可赢(k=n)：巫师置换不变量+查询集和补集双射到所有标签+总能找到合适置换 ✅
- [x] 2c. characterization vs case_analysis区分清晰 ✅
- [x] 2d. key_insight="k<n时滑动k位置窗口揭示足够信息推断2n-k>n个位置标签，鸽巢迫使匹配；k=n时巫师维持查询集上单射不变量总能重排"——准确，Lean中Arrangement和Valid验证 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→尝试→重叠窗口揭示标签→滑动窗口策略→巫师置换不变量→双向结论，合理 ✅
- [x] 2f. R3 kb=True正确（滑动窗口策略是知识瓶颈），R6 kb=True正确（形式化巫师置换不变量是知识瓶颈），R4 tb正确（重叠窗口揭示标签的洞察是思维瓶颈）✅
- [x] 2g. 全局tell/hint质量：3个全局pair（1 path_feature+2 implicit），why_not_visible_locally都填写 ✅
- [x] 2h-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
