# POC-VMS-10：小概念标记分辨验证

**前置阅读**：02-tell端/05-Pipe-2-小概念标记分辨.md、04-概念树/01-大概念与小概念.md
**来源**：289号

---

## 1. 实验目标

验证比POC-VMS-9更高标准的场景：**在拓扑相同的情况下，如果两个tell的"距离"极其相近怎么办？**

具体验证：
1. Pipe 1（大概念过滤）对拓扑相同的tell给同分——大概念无法区分
2. Pipe 2（小概念标记分辨）能区分拓扑相同但小概念不同的tell
3. 交叉验证：干扰tell在错误题目上无效

## 2. 两个拓扑相同且距离极近的tell

| | tell-A | tell-B |
|---|---|---|
| 来源 | 1631题 | 1709题 |
| 大概念拓扑 | (structural_existence, enumeration_brute_force, method_problem_mismatch) | **完全相同** |
| 距离极近 | 都是数论题，都是穷举a值，都是结构问题 | 同 |
| 小概念：穷举对象 | 序列参数a | 差分参数a |
| 小概念：问题结构 | 素数性（Mersenne素数） | 整除性（被4整除） |
| 小概念：正确方法 | 二次剩余/Euler准则 | 2-adic赋值/模4分析 |
| hint | T03二次剩余 | T05 2-adic赋值 |

## 3. Pipe验证结果

### 1631题（tell-A的题目）

**Pipe 1大概念过滤**：两个tell都得score=4——大概念无法区分 ✅

**Pipe 2小概念标记分辨**：
| 候选tell | 小概念命中 | combined_score | 角色 |
|---|---|---|---|
| tell-A | mersenne=497, primality=339, covering=20, total=856 | 896 | ← 目标tell胜出 |
| tell-B | divisibility_4=12, total=12 | 52 | ← 干扰tell |

✅ Pipe 2目标tell胜出（896 vs 52）

### 1709题（tell-B的题目）

**Pipe 1大概念过滤**：两个tell都得score=4——大概念无法区分 ✅

**Pipe 2小概念标记分辨**：
| 候选tell | 小概念命中 | combined_score | 角色 |
|---|---|---|---|
| tell-B | largest_odd_divisor=14, divisibility_4=19, p_adic=2, difference=6, total=41 | 81 | ← 目标tell胜出 |
| tell-A | total=0 | 40 | ← 干扰tell |

✅ Pipe 2目标tell胜出（81 vs 40）

## 4. 交叉验证结果

| 实验 | 结果 | 详情 |
|---|---|---|
| 1709 bare | ❌ 失败 | AI用枚举+g(k)函数分析，没找到2-adic赋值 |
| 1631 interference (T05) | ❌ 失败 | AI用2-adic赋值分析Mersenne素数，2-adic不适用于素数性判定 |
| 1709 interference (T03) | ❌ 失败 | AI用Legendre符号分析最大奇因子，二次剩余不适用于整除性判定 |

## 5. 验证总结

| 验证项 | 结果 |
|---|---|
| 两个tell拓扑完全相同 | ✅ PASS |
| 两个tell距离极近 | ✅ PASS |
| Pipe 1给同分（大概念无法区分） | ✅ PASS |
| Pipe 2小概念标记分辨成功 | ✅ PASS（896 vs 52，81 vs 40） |
| 1709 bare AI做不出来 | ✅ PASS |
| 1631+T05干扰无效 | ✅ PASS |
| 1709+T03干扰无效 | ✅ PASS |
| 干扰tell不是trivial | ✅ PASS |

**全部PASS。**

## 6. 关键发现

1. **大概念无法区分拓扑相同的tell**——验证了用户的核心预判："随着tell数量积累，大概念不足以区分"
2. **小概念标记分辨成功**——验证了"定义新概念区分tell"的路径
3. **小概念信号词是tell的标准化语言描述的关键词提取**——验证了"通过标准化对tell的语言描述来应对"
4. **干扰tell即使拓扑相同也无效**——即使两个tell拓扑相同，它们的hint也是不可互换的
5. **完整三层Pipe架构验证通过**——Pipe 0→Pipe 1→Pipe 2

## 7. 局限

1. 小概念信号词仍然是手工设计的
2. 只有2个拓扑相同的tell
3. 1709+T05的正确hint没有验证（只验证了bare失败和T03干扰失败）
4. 概念树管理还没有验证
