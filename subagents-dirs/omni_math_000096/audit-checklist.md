# Master Agent 审计 Checklist — AoPS omni_math #96

- **problem_id**: omni_math_000096
- **审计时间**: 2025-01-24
- **来源**：AoPS omni_math，中国国家队选拔考试（函数方程）
- **备注**：subagent首次空通知，重试成功

## Phase 0: 加载审计材料 [x]

- [x] 0a. 从ArangoDB读取完整profile ✅
- [x] 0b. 读problem.lean——求所有f:Z→Z满足2f(a²+b²+c²)-2f(ab+bc+ca)=f(a-b)²+f(b-c)²+f(c-a)²。解答：令b=c=0得f(x²)=f(x)²，由f(1)=f(1)²分出f≡0和f=id两条路径，代数恒等式将方程化简为可加性验证。答案：f(x)=0或f(x)=x ✅
- [x] 0c. 读取subagent的checklist.md ✅
- [x] 0d. 数据库与profile.json一致 ✅

## Phase 1: 格式检查 [x]

- [x] 1a. situation_type：7个pair全规范 ✅
- [x] 1b. hint_level：0.4-0.8全0-1浮点数 ✅
- [x] 1c. per-pair拓扑：7+3个pair全有tell_topology和tell_small_concepts ✅
- [x] 1d. 必填字段全部完整 ✅
- [x] 1e. QA序列结构：7轮，stats完整（kb="R4", tb="R6"字符串类型）✅

## Phase 2: 数学内容审查 [x]

- [x] 2a. 题目理解准确 ✅
- [x] 2b. 解答理解准确——b=c=0代入得f(x²)=f(x)²+f(1)=f(1)²分岔+代数恒等式化简为可加性验证 ✅
- [x] 2c. characterization vs specialization_and_case_analysis区分清晰 ✅
- [x] 2d. key_insight="令b=c=0得到f(x²)=f(x)²，由f(1)=f(1)²分出f≡0和f=id两条路径，代数恒等式将方程化简为可加性验证"——准确 ✅
- [x] 2e. QA序列逐轮审查：7轮覆盖观察→列举→代入尝试→b=c=0特化→f(1)分岔→恒等式化简→综合，合理 ✅
- [x] 2f. R4 kb=True正确（b=c=0代入推导f(x²)=f(x)²是知识瓶颈），R6 tb正确（识别隐藏代数恒等式是思维瓶颈）✅
- [x] 2g-2p. 全部通过 ✅

## Phase 3-6: 全部通过 [x]

## Phase 5: 审计结论 [x]

- [x] 5a. **合格**——0个大问题，0个小问题
- [x] 5d. 记录到review-log.md

## 审计员签字

- 审计结论：✅ 合格
- 日期：2025-01-24
