## repo 与学术地图的对应分析


### 覆盖度总览

| 学术 Schema 步骤 | repo 覆盖 | Python 重构 | 状态 |
|---|---|---|---|
| Step 1 历法转换 | ❌ Calculate 有农历方法但未研究 | ❌ | **缺失** |
| Step 2 星历计算 | ✅ Calculate + swisseph | ✅ core.py | **完成** |
| Step 3 宫位系统 | ✅ Calculate.computeHouses | ✅ core.calc_houses | **完成** |
| Step 4 命宫/身宫 | ⚠️ 命宫已研究，身宫未完成 | ⚠️ core.calc_life_sign | **部分** |
| Step 5 童限/大限 | ✅ ChartData 大限系列 | ✅ core.calc_daxian | **完成** |
| Step 6 化曜/十神 | ❌ 未研究 | ❌ | **缺失** |
| Step 7 神煞系统 | ❌ 未研究（可能在 RuleEntry?） | ❌ | **缺失** |
| Step 8 星曜状态 | ⚠️ getSpeedState 部分研究 | ❌ | **部分** |
| Step 9 格局分析 | ⚠️ computeAspects 未研究，EvalRule 未研究 | ❌ | **缺失** |
| Step 10 限运推演 | ⚠️ 大限已研究，流年/流月未研究 | ⚠️ | **部分** |
| Step 11 综合判读 | ❌ EvalRule 规则引擎未研究 | ❌ | **缺失** |

### 详细对应表

| 学术概念 | repo 位置 | 研究状态 | Python 状态 | 缺口 |
|---|---|---|---|---|
| **公历→农历** | Calculate.computeNewMoons/getLunarCalendar/getLunarDate/getDateFromLunarDate/isLeapMonth/getChineseYear | ❌ | ❌ | **需研究 + 实现** |
| **节气** | Calculate.computeSolarTerms | ✅ | ⚠️ API 待验证 | 小缺口 |
| **十一曜位置** | Calculate.compute | ✅ | ✅ | 完成 |
| **二十八宿宿度** | ❌ repo 中未见独立宿度计算 | ❌ | ❌ | **需研究：repo 是否有宿度？还是只有黄道度？** |
| **十二宫宫头** | Calculate.computeHouses | ✅ | ✅ | 完成 |
| **宫主** | ❌ 未见独立方法 | ❌ | ❌ | **需确认：宫主是查表还是计算？** |
| **命宫** | ChartData.computeLifeSign | ✅ | ⚠️ 基准日简化 | 小缺口 |
| **身宫** | ChartData.computeSelfSign | ⚠️ 未完成 | ❌ | **需研究** |
| **命度主/身度主** | ❌ 未见 | ❌ | ❌ | **需确认：是否在 EvalRule?** |
| **昼生/夜生** | Calculate.isDayBirth/computeRiseSet | ❌ | ❌ | **需研究** |
| **童限** | ChartData.getChildLimit | ✅ | ✅ | 完成 |
| **洞微大限** | ChartData.nowYearPosition + limit_seq | ✅ | ✅ | 完成 |
| **大限行度诀** | ❌ 未见独立实现 | ❌ | ❌ | **需确认：是否在 limit_seq 之外？** |
| **小限** | ChartData.getSmallLimit | ✅ | ✅ | 完成 |
| **月限** | ChartData.getMonthLimit | ✅ | ⚠️ 简化 | 小缺口 |
| **飞限** | ChartData.getFlyLimit | ✅ | ⚠️ 半年切换简化 | 小缺口 |
| **十干化曜** | ❌ 未见 | ❌ | ❌ | **需确认：是否在 RuleEntry/EvalRule?** |
| **神煞** | ❌ 未见独立模块 | ❌ | ❌ | **需确认：是否在 RuleEntry/EvalRule?** |
| **庙旺利陷** | ❌ 未见独立方法 | ❌ | ❌ | **需确认：是否在 prop/EvalRule?** |
| **入垣/升殿** | ❌ 未见 | ❌ | ❌ | **需确认** |
| **逆顺迟疾** | Calculate.getSpeedState | ⚠️ | ❌ | **需研究** |
| **三方四正** | ❌ 未见独立方法 | ❌ | ❌ | **需确认：是否在 EvalRule?** |
| **相位/夹拱** | Calculate.computeAspects + ChartData.initAspects | ❌ | ❌ | **需研究** |
| **星格** | ❌ 未见独立模块 | ❌ | ❌ | **需确认：是否在 EvalRule 规则?** |
| **流年太岁** | ❌ 未见 | ❌ | ❌ | **需确认** |
| **限运推演** | ChartData.getTransitData | ❌ | ❌ | **需研究** |
| **命理规则引擎** | EvalRule + RuleParse + RuleEntry + Rule.yacc | ❌ | ❌ | **需研究（核心缺口）** |

### 关键发现

1. **repo 覆盖了 Step 2-5 的核心计算**（星历/宫位/命宫/大限），这是"排盘"部分。
2. **repo 的 Step 6-11（化曜/神煞/状态/格局/限运/判读）大概率在 EvalRule 规则引擎中**——这是 3500+ 行未研究的代码，可能是 repo 最有价值的命理判读核心。
3. **二十八宿宿度**是七政四余区别于西方占星的核心特征，但 repo 未见独立宿度计算——需确认 repo 是否只算黄道度，还是宿度藏在某处。
4. **农历转换**是排盘的前置步骤，repo 有方法但未研究——这是必须补的缺口。
5. **十干化曜 + 神煞**是七政四余的"参数层"，repo 未见独立模块——大概率在 prop 文件或 RuleEntry 中以规则形式存在。

### 下一步研究优先级（按学术地图重新排序）

1. **EvalRule 规则引擎**（Step 6-11 的核心）——搞清楚 repo 的命理判读规则系统，确认化曜/神煞/格局/判读是否在此。
2. **二十八宿宿度**——确认 repo 是否有宿度计算，这是七政四余的核心坐标。
3. **农历转换**（Step 1）——排盘前置，必须补。
4. **升落/日夜**（Step 4 子步骤）——命宫/身宫/命度主需要。
5. **相位/格局**（Step 9）——星盘分析需要。
6. **流年/限运**（Step 10）——动态运势推演。
7. **CS41.py 评分体系**——AI 辅助推命的评分算法。

