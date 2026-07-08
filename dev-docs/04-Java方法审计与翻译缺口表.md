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

- [x] **步骤1**：更新 dev-notes/06-功能模块完整盘点.md 的过时状态标记（EvalRule 已部分研究、Calculate 升落已翻译、ChartData 命宫身宫已翻译等）
- [x] **步骤2**：Calculate.java 59 公开方法逐个标记翻译状态
- [x] **步骤3**：ChartData.java 66 公开 + 52 私有计算方法逐个标记翻译状态
- [x] **步骤4**：EvalRule.java 20 公开方法 + RuleEntry.java 24 内置函数标记翻译状态
- [x] **步骤5**：moira_s.prop 59 命理 key 列出已提取/未提取
- [x] **步骤6**：20 个未翻译功能块按重要性排序，标注依赖关系

---

## 八、20 个未翻译功能块排序+依赖（步骤6 完成）

基于步骤2-5的审计结果，按**依赖深度**和**命理重要性**排序。分层标注：
- **L1 基础层**：其他功能块的前置依赖
- **L2 核心层**：七政四余核心输出
- **L3 扩展层**：高级功能
- **L4 辅助层**：显示/工具

### 8.1 功能块排序表

| 优先级 | 功能块 | 层级 | Java 方法 | 依赖 | 被依赖 | 命理 key |
|---|---|---|---|---|---|---|
| **P1** | 神煞完整体系 | L1 | getStarSigns, addStarSign, computeYearSign | star_sky_earth_key, star_sky_qi_key, star_month_key, star_month_hour_key, star_sign_key, star_equ_map, year_sign_key, long_life_pos, long_life_start | 规则引擎, 八字, 流年 | 9个 |
| **P2** | 八字系统 | L2 | computeEightCharData, getTenGodName, getAltPoleName, getEarthGodSeq, getBirthSeason, getBeforeBirthName, parseEightChar | 神煞体系, getZodiacShift, getElementalIndex | 规则引擎, 流年 | day_pole_long_life_seq, life_master, life_helper_key |
| **P3** | 弱宫/强宫 | L1 | computeWeakHouse, getSolidHouse, getWeakHouse | 无 | 八字, 规则引擎(setBirthInfo) | 无 |
| **P4** | 流年神煞 | L2 | getYearInfo, getYearInfoKey, getYearStar, computeYearSign | 神煞体系, 八字 | 流年推演, 规则引擎 | birth_year_info, current_year_info, year_info_sep, year_star_map, year_star_range, year_star_seq, power_key, power_index, sky_key_seq, year_birth_earth_key |
| **P5** | 规则引擎符号表 | L1 | EvalRule.setBirthInfo, setBirthStarSign, setBirthSign | 神煞体系, 八字, 弱宫强宫, 流年神煞 | 规则引擎求值 | life_master, life_helper_key, birth_year_signs |
| **P6** | 规则引擎内置函数 | L1 | RuleEntry.evalFunction + 24内置函数 | 规则引擎符号表 | 规则引擎求值 | 无 |
| **P7** | 规则引擎求值器 | L2 | RuleEntry.computeRules, evalExpr, evalRel, evalFunction, evalUserFunction, evalSet, setContainment, setIter | 规则引擎符号表, 内置函数 | 格局判读 | 无 |
| **P8** | 流年推演 | L2 | computeNowData, EvalRule.setNowInfo, setNowStarSign, setNowSign | 流年神煞, 规则引擎符号表 | 流年格局 | current_year_info |
| **P9** | 大运精确起点 | L2 | getBigCycleStartGap, getBigCycleStartDate | 无 | 大限精度 | big_cycle |
| **P10** | 小限/月限完整 | L2 | getSmallLimit, getMonthLimit | 无 | 限运完整性 | small_limit, month_limit |
| **P11** | 三煞 | L2 | computeThreeDanger, findMountainSign | 神煞体系, 罗盘方位 | 八字, 规则引擎 | three_danger |
| **P12** | 地支顺逆 | L1 | Calculate.getZodiacShift | 无 | 神煞体系(star_sky_qi_key) | 无 |
| **P13** | 五行索引 | L1 | Calculate.getElementalIndex, getElementalStateIndex | 无 | 八字, 规则引擎 | 无 |
| **P14** | 相位系统 | L3 | initAspects, getAspects, Calculate.computeAspects | 无 | 格局分析 | 无 |
| **P15** | 推运系统 | L3 | computeTransitData, computePlanetTransit, computePlanetRelativeTransit, computeSpeedTransit | 无 | 流年推运 | 无 |
| **P16** | 返照系统 | L3 | computeSolarReturn, computeLunarReturn | 无 | 高级推运 | 无 |
| **P17** | 主限/次限推运 | L3 | computePrimaryDirection, computeSecondaryProgression, setOrbitData, setEquOrbitData, getPrimarySpeed, getCompressionRatio | 无 | 高级推运 | 无 |
| **P18** | 日月食 | L3 | computeEclipse, Calculate.computeSolarEclipse, computeLunarEclipse, getEclipseState | 无 | 特殊命理 | 无 |
| **P19** | 高格林区位 | L4 | computeGauquelin, getGauquelin, gauquelinPlusZone, computeOpposite | 无 | 高级占星 | 无 |
| **P20** | 恒星/方位角/罗盘 | L4 | computeStar, findStarByEquPos, computeFixstarState, computeAzimuth, getAltitude, getMountain, getMountainPos, getLATDateFromDate, getLocalJulianDayUT | 无 | 风水/择日/恒星 | 无 |

### 8.2 依赖关系图

```
P12 地支顺逆 ─┐
P13 五行索引 ─┤
P3 弱宫/强宫 ─┤
              ├─→ P1 神煞完整体系 ─→ P2 八字系统 ─→ P5 规则引擎符号表
              │                    ─→ P4 流年神煞 ─→ P8 流年推演
              │                                    ─→ P5 规则引擎符号表
              │
              └─→ P6 规则引擎内置函数 ─→ P7 规则引擎求值器 ─→ P8 流年推演
                                        ↑
                                        └─ P5 规则引擎符号表

P11 三煞 ←─ P1 神煞体系 + P20 罗盘方位
P9 大运精确起点（独立）
P10 小限/月限（独立）
P14 相位系统（独立）
P15 推运系统（独立）
P16 返照系统（独立）
P17 主限/次限推运（独立）
P18 日月食（独立）
P19 高格林区位（独立）
P20 恒星/方位角/罗盘（独立）
```

### 8.3 推荐实施顺序

基于依赖关系，推荐按以下顺序实施：

**第一批（L1 基础层，解锁后续）**：
1. P12 地支顺逆（getZodiacShift）— 简单，神煞体系前置
2. P13 五行索引（getElementalIndex/getElementalStateIndex）— 简单，八字前置
3. P3 弱宫/强宫（computeWeakHouse）— 简单，规则引擎前置
4. P1 神煞完整体系（getStarSigns）— **核心缺口**，解锁八字/流年/规则引擎

**第二批（L2 核心层，七政四余核心输出）**：
5. P2 八字系统（computeEightCharData）— **核心缺失**
6. P4 流年神煞（getYearInfo）— **核心缺失**
7. P5 规则引擎符号表（setBirthInfo/setBirthStarSign）— 解锁规则引擎
8. P6 规则引擎内置函数（24个）— 解锁58条规则
9. P7 规则引擎求值器 — 完整格局判读
10. P8 流年推演（computeNowData）— 流年盘
11. P9 大运精确起点
12. P10 小限/月限完整
13. P11 三煞

**第三批（L3 扩展层，高级功能）**：
14. P14 相位系统
15. P15 推运系统
16. P16 返照系统
17. P17 主限/次限推运
18. P18 日月食

**第四批（L4 辅助层，按需）**：
19. P19 高格林区位
20. P20 恒星/方位角/罗盘

---

## 七、moira_s.prop 命理 key 缺口表（步骤5 完成）

moira_s.prop 共 1136 个顶级 key，其中命理相关约 59 个。当前 constants.json 仅提取 24 个 key（覆盖 6 个命理 key）。

### 7.1 已提取的命理 key（6/59）

| moira_s.prop key | constants.json 对应 | 说明 |
|---|---|---|
| star_sky_key | stem_stars | 天干神煞 |
| star_earth_key | branch_stars | 地支神煞 |
| ten_god_list_org | ten_god_transform | 十干化曜 |
| sign_status_seq | dignity_states | 庙旺平陷 |
| year_sound_key | na_yin_60 | 纳音五行 |
| long_life_signs | sheng_zhang_12_stages | 长生十二运 |

### 7.2 未提取的命理 key（53/59）

按功能分组：

#### 神煞体系（17个，最核心缺口）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| star_sky_earth_key | 天干地支合神煞 | getStarSigns | **高** |
| star_sky_qi_key | 天干气神煞 | getStarSigns | **高** |
| star_month_key | 月支神煞 | getStarSigns | **高** |
| star_month_hour_key | 月支时支神煞 | getStarSigns | **高** |
| star_sign_key | 神煞→星宿映射 | setStarSign | **高** |
| star_equ_map | 神煞等价映射 | setStarSign | **高** |
| year_sign_key | 年神→星宿映射 | setStarSign | **高** |
| year_star_map | 年星映射 | getYearStar | 中 |
| year_star_range | 年星范围 | getYearStar | 中 |
| year_star_seq | 年星序列 | getYearStar | 中 |
| year_birth_earth_key | 年命地支key | getYearInfo | 中 |
| power_key | 权力神煞key | getYearInfo | 中 |
| power_index | 权力神煞索引 | getYearInfo | 中 |
| sky_key_seq | 天干key序列 | getYearInfo | 中 |
| three_danger | 三煞表 | computeThreeDanger | 中 |
| birth_wife_sign | 妻星 | getYearInfo | 低 |
| wife_signs | 妻星序列 | getYearInfo | 低 |

#### 流年神煞（8个）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| birth_year_info | 出生流年信息模板 | getYearInfo | **高** |
| current_year_info | 当前流年信息模板 | getYearInfo | **高** |
| alt_birth_year_info | 替代出生流年信息 | getYearInfo | 中 |
| alt_current_year_info | 替代当前流年信息 | getYearInfo | 中 |
| pick_year_info | 择日流年信息 | getYearInfo | 低 |
| alt_pick_year_info | 替代择日流年信息 | getYearInfo | 低 |
| year_info_sep | 流年信息分隔符 | getYearInfo | **高** |
| year_data_plus_eight_char | 年数据+八字 | getYearInfo | 中 |

#### 八字系统（6个）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| day_pole_long_life_seq | 日柱长生序 | computeEightCharData | **高** |
| long_life_pos | 长生位置 | getStarSigns | **高** |
| long_life_start | 长生起点 | getStarSigns | **高** |
| life_helper_key | 命宫辅助key | setBirthInfo | 中 |
| alt_life_helper_key | 替代命宫辅助key | setBirthInfo | 低 |
| life_master / life_master_name | 命主/命主名 | setBirthInfo | 中 |

#### 限运系统（5个）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| big_cycle | 大运周期 | getBigCycleStartGap | **高** |
| child_limit | 童限 | getChildLimit | 中（已部分翻译） |
| small_limit | 小限 | getSmallLimit | 中 |
| month_limit | 月限 | getMonthLimit | 低 |
| fly_limit | 飞限 | getFlyLimit | 低（已部分翻译） |

#### 星座/星宿（5个）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| twelve_signs | 十二地支 | 多处 | **高** |
| chinese_zodiac_signs | 生肖 | getYearInfo | 中 |
| full_zodiac | 完整地支 | 多处 | **高** |
| full_stellar_signs | 完整二十八宿 | 多处 | **高** |
| stellar_signs / stellar_sign_pos | 二十八宿 | 多处 | **高** |

#### 节气/历法（4个）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| season_starts | 节气起点 | getBirthSeason | **高** |
| start_at_winter_solstice | 冬至起点 | computeNewMoons | **高** |
| signs | 星座序列 | 多处 | **高** |
| asc_influence | 上升影响 | getYearInfo | 低 |

#### 十神/模式（4个）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| ten_god_mode | 十神模式 | getYearInfoKey | 中 |
| ten_god_seq1 / ten_god_seq2 | 十神序列 | getYearInfo | 中 |
| ten_god_list_alt | 替代十神列表 | setStarSign | 低 |

#### 其他（4个）

| key | 功能 | 依赖方法 | 优先级 |
|---|---|---|---|
| sign_status_key | 星座状态key | getSignStatus | 中 |
| birth_year_signs | 出生年神煞 | setBirthInfo | 中 |
| year_sound_field | 纳音字段 | getYearInfo | 低 |
| year_data_plus_eight_char | 年数据+八字 | getYearInfo | 低 |

### 7.3 moira_s.prop 命理 key 翻译统计

| 分组 | 总数 | 已提取 | 未提取 | 覆盖率 |
|---|---|---|---|---|
| 神煞体系 | 17 | 2 | 15 | 12% |
| 流年神煞 | 8 | 0 | 8 | 0% |
| 八字系统 | 6 | 1 | 5 | 17% |
| 限运系统 | 5 | 0 | 5 | 0% |
| 星座/星宿 | 5 | 0 | 5 | 0% |
| 节气/历法 | 4 | 0 | 4 | 0% |
| 十神/模式 | 4 | 1 | 3 | 25% |
| 其他 | 4 | 0 | 4 | 0% |
| 长生十二运 | 6 | 1 | 5 | 17% |
| **合计** | **59** | **6** | **53** | **10%** |

**结论**：命理 key 缺口集中在神煞体系（15个未提取）和流年神煞（8个未提取）。这两块是规则引擎和八字系统的前置依赖。

---

## 六、EvalRule.java + RuleEntry.java 翻译状态表（步骤4 完成）

### 6.1 EvalRule.java 20 公开方法

图例：✅ 已翻译  ⚠️ 部分翻译  ❌ 未翻译  🗑️ 不需要

| # | Java 方法 | 行号 | 功能 | 状态 | Python 对应 |
|---|---|---|---|---|---|
| 1 | EvalRule(ChartData) | 47 | 构造函数 | ✅ | core.eval_rules（参数） |
| 2 | initSign(String[],String[],boolean) | 51 | 初始化星座/星宿/性别 | ❌ | **未翻译**（规则引擎需要） |
| 3 | initNow() | 74 | 初始化流年 | ❌ | **未翻译**（流年规则需要） |
| 4 | setBirthInfo(Calculate,String[],boolean,String[],double,double,double[],int[],boolean) | 79 | **设置出生信息**（四柱/季节/昼夜/命宫/身宫/弱宫强宫/农历/朔望/命主边界/身主边界/命宫度主/身宫度主/命宫临宫神煞） | ❌ | **未翻译**（规则引擎核心上下文，core._build_symbol_table 仅实现约1/3） |
| 5 | setNowInfo(Calculate,String[],int[],int,double,double[],int[],boolean) | 202 | 设置流年信息 | ❌ | **未翻译**（流年规则需要） |
| 6 | setBirthSign(Calculate,String[],double[],double[],double) | 323 | 设置出生星位置 | ❌ | **未翻译**（规则引擎需要） |
| 7 | setNowSign(Calculate,String[],double[],double[]) | 430 | 设置流年星位置 | ❌ | **未翻译**（流年规则需要） |
| 8 | setSign(Calculate,Hashtable,String,...) | 436 | 设置星位置（内部） | ❌ | **未翻译** |
| 9 | setBirthStarSign(Hashtable,Hashtable,LinkedList,String[],String[],String) | 532 | **设置出生神煞** | ❌ | **未翻译**（规则引擎核心，神煞→规则变量映射） |
| 10 | setNowStarSign(Hashtable,Hashtable,LinkedList,String[],String[],String) | 539 | 设置流年神煞 | ❌ | **未翻译**（流年规则需要） |
| 11 | setStarSign(Hashtable,Hashtable,...) | 546 | 设置神煞（内部） | ❌ | **未翻译** |
| 12 | initOptions(BaseTab) | 641 | 初始化选项 | 🗑️ | GUI |
| 13 | getYearOffsetStart() | 747 | 流年偏移起点 | ❌ | **未翻译**（流年规则需要） |
| 14 | getYearOffsetEnd() | 751 | 流年偏移终点 | ❌ | **未翻译**（流年规则需要） |
| 15 | computeStyles() | 755 | **计算格局风格** | ❌ | **未翻译**（good_styles/bad_styles） |
| 16 | ruleHeader() | 766 | 规则头部 | 🗑️ | GUI 输出 |
| 17 | ruleFooter() | 773 | 规则尾部 | 🗑️ | GUI 输出 |
| 18 | **computeRules()** | 779 | **计算规则** | ⚠️ | core.eval_rules（简化版，76/134条） |
| 19 | getGoodStyles() | 793 | 获取好格局 | ❌ | **未翻译** |
| 20 | getBadStyles() | 797 | 获取坏格局 | ❌ | **未翻译** |

### 6.2 EvalRule.java 翻译统计

| 状态 | 数量 | 占比 |
|---|---|---|
| ✅ 已翻译 | 1 | 5% |
| ⚠️ 部分翻译 | 1 | 5% |
| ❌ 未翻译 | 16 | 80% |
| 🗑️ 不需要 | 2 | 10% |
| **合计** | **20** | **100%** |

**核心方法翻译率**（排除 🗑️）：2/18 = **11%**

### 6.3 RuleEntry.java 24 内置函数翻译状态

| # | 内置函数 | 参数数 | 功能 | 状态 | Python 对应 |
|---|---|---|---|---|---|
| 1 | if | 2-3+ | 条件判断 | ❌ | **未实现** |
| 2 | eval | 2-3 | 求值集合 | ❌ | **未实现** |
| 3 | map | 2-3 | 映射集合 | ❌ | **未实现** |
| 4 | test | 2-3 | 测试集合 | ❌ | **未实现** |
| 5 | set | 任意 | 构造集合 | ❌ | **未实现** |
| 6 | offset | 4 | 位置偏移 | ❌ | **未实现** |
| 7 | format | 3 | 格式化字符串 | ❌ | **未实现** |
| 8 | prefix | 3 | 前缀扩展 | ❌ | **未实现** |
| 9 | suffix | 3 | 后缀扩展 | ❌ | **未实现** |
| 10 | intersection | 2-3 | 集合交集 | ❌ | **未实现** |
| 11 | iter | 2-3 | 集合迭代 | ❌ | **未实现** |
| 12 | digit | 3 | 数字格式化 | ❌ | **未实现** |
| 13 | union | 2 | 集合并集 | ❌ | **未实现** |
| 14 | complement | 2 | 集合补集 | ❌ | **未实现** |
| 15 | contain | 2 | 包含判断 | ❌ | **未实现** |
| 16 | trim | 2 | 集合修剪 | ❌ | **未实现** |
| 17 | entry | 2 | 集合元素 | ❌ | **未实现** |
| 18 | split | 2 | 字符串分割 | ❌ | **未实现** |
| 19 | empty | 1 | 空集判断 | ❌ | **未实现** |
| 20 | size | 1 | 集合大小 | ❌ | **未实现** |
| 21 | import | 1 | 导入集合 | ❌ | **未实现** |
| 22 | int | 1 | 取整 | ❌ | **未实现** |
| 23 | round | 1 | 四舍五入 | ❌ | **未实现** |
| 24 | abs | 1 | 绝对值 | ❌ | **未实现** |

### 6.4 RuleEntry.java 核心求值方法翻译状态

| # | Java 方法 | 行号 | 功能 | 状态 | Python 对应 |
|---|---|---|---|---|---|
| 1 | evalVariable(RuleParse,char,Object,Object) | 298 | 变量求值 | ⚠️ | core._eval_var（部分，仅简单形式） |
| 2 | evalBoolean(RuleParse,Object) | 323 | 布尔求值 | ⚠️ | core._eval_cond（部分） |
| 3 | evalAlias(RuleParse,String,Object) | 376 | 别名求值 | ❌ | **未实现** |
| 4 | evalHasEntry(RuleParse,Object,boolean) | 398 | 存在判断 | ❌ | **未实现** |
| 5 | evalNot(RuleParse,Object) | 408 | 逻辑非 | ❌ | **未实现** |
| 6 | evalAnd(RuleParse,Object,Object) | 417 | 逻辑与 | ⚠️ | core._eval_cond（隐式） |
| 7 | evalOr(RuleParse,Object,Object) | 427 | 逻辑或 | ⚠️ | core._eval_cond（隐式） |
| 8 | evalAssign(RuleParse,Object,Object,boolean) | 438 | 赋值 | ⚠️ | core._eval_cond（部分） |
| 9 | evalExpr(RuleParse,Object,Object,char) | 448 | 表达式（+-*/%） | ❌ | **未实现**（算术运算） |
| 10 | evalRel(RuleParse,Object,Object,String) | 484 | 关系（><>=<===!=） | ❌ | **未实现** |
| 11 | evalFunction(RuleParse,Object,LinkedList) | 515 | **函数调用** | ❌ | **未实现**（24内置函数入口） |
| 12 | evalUserFunction(RuleParse,RuleEntry,LinkedList) | 674 | 用户函数 | ❌ | **未实现** |
| 13 | evalDefined(RuleParse,Object) | 723 | 定义判断 | ❌ | **未实现** |
| 14 | evalSet(RuleParse,Object,String,String,String) | 728 | 集合求值 | ❌ | **未实现** |
| 15 | concatString(RuleParse,Object,Object) | 761 | 字符串连接 | ❌ | **未实现** |
| 16 | indexValue(RuleParse,Object,Object) | 765 | 索引取值 | ❌ | **未实现** |
| 17 | shiftValue(RuleParse,Object,Object,boolean) | 795 | 偏移取值 | ❌ | **未实现** |
| 18 | setContainment(RuleParse,Object,Object) | 833 | 集合包含 | ❌ | **未实现** |
| 19 | setUnion(Object,Object) | 862 | 集合并集 | ❌ | **未实现** |
| 20 | setContainString(Object,String) | 979 | 字符串包含 | ❌ | **未实现** |
| 21 | setIter(RuleParse,Object,Object,Object) | 994 | 集合迭代 | ❌ | **未实现** |
| 22 | computeRules(LinkedList,LinkedList) | 1512 | **规则主循环** | ⚠️ | core.eval_rules（简化版） |
| 23 | initBirth(Hashtable,String[]) | 1449 | 初始化出生表 | ❌ | **未实现** |
| 24 | initNow(Hashtable) | 1464 | 初始化流年表 | ❌ | **未实现** |

### 6.5 规则引擎翻译统计

| 模块 | 总数 | ✅ 已翻译 | ⚠️ 部分 | ❌ 未翻译 | 覆盖率 |
|---|---|---|---|---|---|
| EvalRule 公开方法 | 20 | 1 | 1 | 18 | 10% |
| RuleEntry 内置函数 | 24 | 0 | 0 | 24 | **0%** |
| RuleEntry 求值方法 | 24 | 0 | 5 | 19 | 21%（含部分） |
| **合计** | **68** | **1** | **6** | **61** | **10%** |

**结论**：规则引擎是当前最大的缺口。24 个内置函数全部未实现，导致 58/134 条规则无法求值。EvalRule 的 setBirthInfo/setBirthStarSign 未翻译，导致规则引擎的符号表严重不完整（缺四柱/季节/昼夜/弱宫强宫/农历/朔望/命主边界/身主边界/命宫度主/身宫度主/命宫临宫神煞）。

---

## 五、ChartData.java 方法翻译状态表（步骤3 完成）

ChartData.java 是 9424 行的上帝类，177 个方法（68 公开 + 109 私有）。本表聚焦**核心计算方法**（排除 GUI 绘制 showDesc*/draw*/page* 等 60+ 个纯显示方法）。

图例：✅ 已翻译  ⚠️ 部分翻译  ❌ 未翻译  🗑️ GUI/不需要

### 5.1 核心计算方法（私有）

| # | Java 方法 | 行号 | 功能 | 状态 | Python 对应 |
|---|---|---|---|---|---|
| 1 | initSign() | 555 | 初始化星座 | ✅ | core.init_ephe |
| 2 | loadMasterTable() | 638 | 加载主星表 | ❌ | **未翻译**（规则引擎需要） |
| 3 | getYearNameIndex(int) | 2398 | 年名索引 | ❌ | **未翻译**（流年需要） |
| 4 | getLimitTip(int,int,int) | 2408 | 限运提示 | 🗑️ | GUI 显示 |
| 5 | getBirthRiseSetDesc() | 3458 | 出生升落描述 | 🗑️ | GUI 显示 |
| 6 | getBirthDesc() | 3474 | 出生描述 | 🗑️ | GUI 显示 |
| 7 | getNowDesc() | 3525 | 当前描述 | 🗑️ | GUI 显示 |
| 8 | getYearInfoKey(boolean) | 3551 | 流年信息key | ❌ | **未翻译**（流年神煞） |
| 9 | getYearInfo(String[],String[],String,Hashtable,boolean) | 3563 | **流年神煞** | ❌ | **未翻译**（年神/天官/地官/水官/天乙/玉堂/紫微/禄勋/斗杓） |
| 10 | getYear(Date) | 3858 | 从Date获取年 | ❌ | **未翻译**（流年需要） |
| 11 | getFraction(Date,Date,Date) | 3874 | 分数计算 | ❌ | **未翻译**（限运需要） |
| 12 | nowYearPosition(int) | 3885 | **大限位置** | ✅ | core.calc_daxian |
| 13 | snapToSignStart(int[]) | 3926 | 对齐星座起点 | ❌ | **未翻译**（推运需要） |
| 14 | computeCenterPos(double[]) | 3941 | 中心位置 | ❌ | **未翻译**（显示） |
| 15 | initSignShift(int,int,String[],...) | 3955 | 初始化星宿偏移 | ❌ | **未翻译**（显示） |
| 16 | computeSignShift(DrawAWT,...) | 3974 | 星宿偏移 | 🗑️ | GUI 绘制 |
| 17 | computeSignPosition(DrawAWT,...) | 4031 | 星宿位置 | 🗑️ | GUI 绘制 |
| 18 | **computeData()** | 4402 | **排盘主入口** | ⚠️ | core.calc_all_bodies + chart.build_chart（部分，缺八字/神煞/流年/推运） |
| 19 | **computeRules()** | 5027 | **格局规则** | ⚠️ | core.eval_rules（简化版，76/134条） |
| 20 | **computeNowData(int[],String[],int)** | 5101 | **流年推演** | ❌ | **未翻译**（流年盘核心） |
| 21 | getSeasonIndex(int[]) | 6057 | 季节索引 | ❌ | **未翻译**（规则引擎需要） |
| 22 | getAdjustDate(String,double,int[],...) | 6168 | 调整日期 | ❌ | **未翻译**（时区矫正） |
| 23 | initSignDisplay() | 6262 | 初始化显示 | 🗑️ | GUI |
| 24 | findMountainSign() | 6317 | 罗盘方位 | ❌ | **未翻译**（风水/三煞需要） |
| 25 | **computeEightCharData()** | 6328 | **八字数据** | ❌ | **未翻译**（长生/十神/纳音/弱宫/强宫，核心缺失） |
| 26 | **computeLifeSign(int[],double[])** | 6689 | **命宫** | ✅ | core.calc_life_sign |
| 27 | **computeSelfSign(int[],int[])** | 6707 | **身宫** | ✅ | core.calc_self_sign_v2 |
| 28 | computePlanet(int) | 6729 | 行星计算 | ✅ | core.calc_planet |
| 29 | computeGauquelin(int,double[],...) | 6761 | 高格林区位 | ❌ | **未翻译**（高格林） |
| 30 | computeOpposite(int,double[]) | 6774 | 对相 | ❌ | **未翻译**（高格林） |
| 31 | getSpeedState(int) | 6782 | 速度状态 | ✅ | core.calc_speed_state |
| 32 | getGauquelin(int) | 6808 | 高格林名 | ❌ | **未翻译** |
| 33 | gauquelinPlusZone(int) | 6820 | 高格林分区 | ❌ | **未翻译** |
| 34 | computeAzimuth(int,double[],...) | 6826 | 方位角 | ❌ | **未翻译**（罗盘） |
| 35 | computePheno(int) | 6836 | 视直径 | ❌ | **未翻译** |
| 36 | computeAzimuth(double,double[],boolean) | 6846 | 方位角(度) | ❌ | **未翻译**（罗盘） |
| 37 | computeAltitude(int) | 6861 | 高度角 | ❌ | **未翻译** |
| 38 | computeFixstarState(double,double) | 6867 | 恒星状态 | ❌ | **未翻译**（恒星） |
| 39 | **computeEclipse()** | 6894 | **日月食** | ❌ | **未翻译**（日月食） |
| 40 | getAspects(String,int,boolean) | 6911 | 相位 | ❌ | **未翻译**（相位） |
| 41 | **computeWeakHouse(String,boolean)** | 7097 | **弱宫** | ❌ | **未翻译**（八字/规则引擎需要） |
| 42 | expandStarList(LinkedList,Hashtable,...) | 7116 | 展开星曜列表 | ❌ | **未翻译**（神煞需要） |
| 43 | getSignStatus(String,double,String[],...) | 7179 | 星座状态 | ❌ | **未翻译**（庙旺） |
| 44 | **chineseCalendar(int[],String[],...)** | 7210 | **农历日历** | ✅ | core.solar_to_lunar |
| 45 | **getStarSigns(String[],double[],boolean)** | 7296 | **神煞完整体系** | ❌ | **未翻译**（天乙/玉堂/紫微/禄勋/驿马/华盖/斗杓/岁驾，核心缺失） |
| 46 | addStarSign(LinkedList,String) | 7399 | 添加神煞 | ❌ | **未翻译**（神煞需要） |
| 47 | inTable(Hashtable,String,boolean) | 7423 | 表查询 | ❌ | **未翻译**（规则引擎需要） |
| 48 | **computeYearSign(String[],Hashtable)** | 7441 | **太岁/年神** | ❌ | **未翻译**（流年神煞） |
| 49 | **getYearStar(int,int)** | 7492 | **年星** | ❌ | **未翻译**（流年神曜） |
| 50 | getBeforeBirthName(String) | 7590 | 胎元名 | ❌ | **未翻译**（八字） |
| 51 | getYearSoundName(String) | 7598 | 纳音名 | ✅ | constants.na_yin_60 |
| 52 | getTenGodName(String,String,boolean) | 7603 | 十神名 | ❌ | **未翻译**（八字核心） |
| 53 | getAltPoleName(String,String) | 7616 | 替代柱名 | ❌ | **未翻译**（八字） |
| 54 | getLongLifeName(String,String,int) | 7624 | 长生名 | ✅ | core.calc_sheng_zhang |
| 55 | getEarthGodSeq(String) | 7640 | 地神序 | ❌ | **未翻译**（八字） |
| 56 | printSolarTerms(boolean) | 7649 | 打印节气 | 🗑️ | GUI 显示 |
| 57 | printNewMoons() | 7676 | 打印朔日 | 🗑️ | GUI 显示 |
| 58 | getBirthSeason(int[]) | 7700 | 出生季节 | ❌ | **未翻译**（八字需要） |
| 59 | **getBigCycleStartGap(int[],int)** | 7723 | **大运起点间隔** | ❌ | **未翻译**（大运精确起点） |
| 60 | **getBigCycleStartDate(int[],double)** | 7750 | **大运起日** | ❌ | **未翻译**（大运精确起日） |
| 61 | getBirthName() | 7758 | 命主名 | 🗑️ | db.py |
| 62 | getBirthSex() | 7781 | 命主性别 | 🗑️ | db.py |
| 63 | getCuspOverride() | 7820 | 宫位覆写 | ❌ | **未翻译**（宫位矫正） |
| 64 | getPosOverride() | 7834 | 位置覆写 | ❌ | **未翻译**（位置矫正） |
| 65 | setCuspOverride(String) | 7884 | 设置宫位覆写 | ❌ | **未翻译** |
| 66 | setBirthPosOverride(String) | 7896 | 设置位置覆写 | ❌ | **未翻译** |
| 67 | computePlanetTransit(int,double,...) | 8029 | 行星推运 | ⚠️ | core.find_date_at_planet_pos（部分） |
| 68 | initSunComputation() | 8048 | 初始化太阳计算 | ❌ | **未翻译**（推运） |
| 69 | setOrbitData(int) | 8060 | 设置轨道数据 | ❌ | **未翻译**（主限推运） |
| 70 | getCompressionRatio() | 8136 | 压缩比 | ❌ | **未翻译**（次限推运） |
| 71 | getPrimarySpeed() | 8144 | 主限速度 | ❌ | **未翻译**（主限推运） |
| 72 | computeBirthSignPos(DataEntry) | 8152 | 计算出生星位置 | ❌ | **未翻译**（推运） |
| 73 | **computeTransitData(LinkedList,DataEntry,...)** | 8197 | **推运数据** | ❌ | **未翻译**（流年推运/相位/过宫） |
| 74 | genTransitHTML(Transit[],...) | 8276 | 推运HTML | 🗑️ | GUI 输出 |
| 75 | parseEightChar(String) | 8915 | 解析八字 | ❌ | **未翻译**（八字） |
| 76 | genPoleDateHTML(LinkedList,...) | 8952 | 柱日期HTML | 🗑️ | GUI 输出 |
| 77 | **searchPoleDates(int,String[])** | 9008 | **搜索柱日期** | ❌ | **未翻译**（八字反推） |
| 78 | genSearchResultHTML(LinkedList,...) | 9269 | 搜索结果HTML | 🗑️ | GUI 输出 |

### 5.2 ChartData.java 翻译统计

| 状态 | 数量 | 占比 |
|---|---|---|
| ✅ 已翻译 | 10 | 13% |
| ⚠️ 部分翻译 | 3 | 4% |
| ❌ 未翻译 | 49 | 63% |
| 🗑️ GUI/不需要 | 16 | 20% |
| **合计** | **78** | **100%** |

**核心计算方法翻译率**（排除 🗑️）：13/62 = **21%**

### 5.3 公开方法（68个）翻译状态摘要

大部分公开方法是 getter/setter，已被 chart.py 的参数传递替代。核心公开方法：

| 公开方法 | 状态 | 说明 |
|---|---|---|
| compute() | ✅ | chart.build_chart |
| computeData() | ⚠️ | 部分翻译（缺八字/神煞/流年/推运） |
| reset() | 🗑️ | 不需要 |
| getChildLimit() | ✅ | core.calc_child_limit_years |
| getChildLimit(age) | ✅ | core.calc_daxian |
| getSmallLimit() | ❌ | **未翻译** |
| getMonthLimit() | ❌ | **未翻译** |
| getFlyLimit() | ⚠️ | core.calc_fly_limit（部分） |
| getDateAtSunPos() | ✅ | core.find_date_at_sun_pos |
| getDateAtPlanetPos() | ✅ | core.find_date_at_planet_pos |
| getPlanetOffset() | ✅ | core |
| getTransitData() | ❌ | **未翻译** |
| canComputeTransit() | ❌ | **未翻译** |
| initAspects() | ❌ | **未翻译** |
| getAspectSignArray() | ❌ | **未翻译** |
| getEclipseData() | ❌ | **未翻译** |
| setEclipseData() | ❌ | **未翻译** |
| getEightCharOverride() | ❌ | **未翻译** |
| setEightCharOverride() | ❌ | **未翻译** |
| getYearInfo(boolean,Hashtable) | ❌ | **未翻译**（流年神煞） |
| inMasterTable(String,boolean) | ❌ | **未翻译**（规则引擎需要） |
| getDisplayTable() | 🗑️ | GUI |
| getSignArray() | 🗑️ | GUI |
| 其余 40+ getter/setter | 🗑️ | GUI/db.py 替代 |
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

---

## 四、Calculate.java 59 公开方法翻译状态表（步骤2 完成）

图例：✅ 已翻译  ⚠️ 部分翻译  ❌ 未翻译  🗑️ 不需要翻译（GUI/IO/资源管理）

| # | Java 方法 | 行号 | 功能 | 状态 | Python 对应 |
|---|---|---|---|---|---|
| 1 | loadResource() | 195 | 加载资源 | 🗑️ | constants.json 替代 |
| 2 | setEphMode(boolean) | 213 | 设置星历模式 | ✅ | core.init_ephe |
| 3 | getEphMode() | 221 | 获取星历模式 | ✅ | core.init_ephe |
| 4 | setTopocentricMode(boolean,boolean) | 226 | 设置地心模式 | ✅ | core.calc_planet（geocentric） |
| 5 | setChartMode() | 239 | 设置图表模式 | 🗑️ | CLI 不需要 |
| 6 | getAyanamsha() | 267 | 获取岁差 | ✅ | core.calc_all_bodies（ayanamsa） |
| 7 | setJulianDay(int[]) | 282 | 从日期设置JD | ✅ | core.jd_from_ymd_ut |
| 8 | setJulianDay(double) | 290 | 从UT设置JD | ✅ | core.jd_from_ymd_ut |
| 9 | getLATDateFromDate(int[]) | 336 | 地方视太阳时 | ❌ | **未翻译**（择日/风水用） |
| 10 | getJulianDayUT() | 372 | 获取JD UT | ✅ | core.jd_from_ymd_ut |
| 11 | getJulianDay() | 377 | 获取JD | ✅ | core.jd_from_ymd_ut |
| 12 | setLocation(double[]) | 382 | 设置位置 | ✅ | core.calc_planet（参数） |
| 13 | setLocation(double,double) | 389 | 设置经纬度 | ✅ | core.calc_planet（参数） |
| 14 | getLocation(double[]) | 396 | 获取位置 | ✅ | chart.py 参数 |
| 15 | getLongitude() | 402 | 获取经度 | ✅ | chart.py 参数 |
| 16 | getLatitude() | 407 | 获取纬度 | ✅ | chart.py 参数 |
| 17 | getDifferenceInDays(int[],int[]) | 412 | 两日期相差天数 | ❌ | **未翻译**（推运需要） |
| 18 | compute(double,int) | 418 | 计算行星位置(JD) | ✅ | core.calc_planet |
| 19 | compute(int) | 427 | 计算行星位置(当前JD) | ✅ | core.calc_planet |
| 20 | computeGauquelin(int) | 465 | 高格林区位 | ❌ | **未翻译**（高格林分区） |
| 21 | computePheno(int) | 500 | 视直径/相位 | ❌ | **未翻译**（视直径） |
| 22 | setOrbitData(double,double,double) | 532 | 设置轨道数据 | ❌ | **未翻译**（主限推运） |
| 23 | setEquOrbitData(int,double,double,double,double) | 541 | 设置赤道轨道数据 | ❌ | **未翻译**（主限推运） |
| 24 | getEclipseState(boolean) | 592 | 食相状态 | ❌ | **未翻译**（日月食） |
| 25 | getSpeedState(int,int) | 609 | 速度状态(行星,索引) | ✅ | core.calc_speed_state |
| 26 | getSpeedState() | 666 | 速度状态(当前) | ✅ | core.calc_speed_state |
| 27 | getSpeedStateName(int,String) | 676 | 速度状态名 | ✅ | core.calc_speed_state（name字段） |
| 28 | setHouseSystemIndex(int) | 686 | 设置宫位制 | ✅ | core.calc_houses（参数） |
| 29 | computeHouses(double[]) | 691 | 计算宫位 | ✅ | core.calc_houses |
| 30 | computeHouses(double[],double) | 696 | 计算宫位(JD) | ✅ | core.calc_houses |
| 31 | computeHousesFromMidHeaven(double[],double) | 707 | 从中天计算宫位 | ❌ | **未翻译**（宫位矫正） |
| 32 | initSpecial(double,double,boolean) | 747 | 初始化特殊点(ASC/MC/Fortune) | ⚠️ | core.calc_all_bodies 含 ASC/MC，Fortune ❌ |
| 33 | computeAzimuth(double) | 780 | 方位角(磁偏) | ❌ | **未翻译**（罗盘方位） |
| 34 | computeAzimuth(double,double,double) | 794 | 方位角(度,宫位,磁偏) | ❌ | **未翻译**（罗盘方位） |
| 35 | getAltitude() | 830 | 高度角 | ❌ | **未翻译**（地平坐标） |
| 36 | computePlanetAzimuthTransit(int,double,...) | 839 | 行星方位角推运 | ❌ | **未翻译**（推运） |
| 37 | computePlanetAzimuth(int,double,...) | 931 | 行星方位角 | ❌ | **未翻译**（罗盘） |
| 38 | computePlanetAzimuthSpeed(int,double,...) | 947 | 行星方位角速度 | ❌ | **未翻译**（罗盘） |
| 39 | getLocalJulianDayUT(String,boolean) | 962 | 本地时区JD | ❌ | **未翻译**（时区转换） |
| 40 | computeRiseSet(String,int,double[]) | 977 | 升落计算 | ✅ | core.calc_rise_set |
| 41 | isDayBirth(double[]) | 1011 | 昼夜判定 | ✅ | core.calc_rise_set（is_day_birth） |
| 42 | isDayBirthByZone(int,int,int) | 1017 | 按时区昼夜判定 | ❌ | **未翻译**（非北京时区用） |
| 43 | computeStar(StringBuffer,String) | 1033 | 恒星计算 | ❌ | **未翻译**（恒星） |
| 44 | computeSpeedTransit(int,double,double,...) | 1174 | 速度推运 | ❌ | **未翻译**（推运） |
| 45 | computePlanetTransit(int,double,double,boolean) | 1183 | 行星推运 | ⚠️ | core.find_date_at_planet_pos（部分） |
| 46 | computePlanetRelativeTransit(int,int,double,...) | 1204 | 行星相对推运 | ❌ | **未翻译**（推运） |
| 47 | findStarByEquPos(double[]) | 1335 | 按赤道位置找恒星 | ❌ | **未翻译**（恒星） |
| 48 | computePlanetAzimuth(int,double,...) | 1399 | 行星方位角(列表) | ❌ | **未翻译**（罗盘） |
| 49 | computeSolarEclipseLocation(double,double[]) | 1442 | 日食位置 | ❌ | **未翻译**（日月食） |
| 50 | computeSolarEclipse(double,double,...) | 1449 | 日食计算 | ❌ | **未翻译**（日月食） |
| 51 | computeLunarEclipse(double,double,...) | 1484 | 月食计算 | ❌ | **未翻译**（日月食） |
| 52 | isLeapMonth() | 1810 | 闰月判定 | ✅ | core.solar_to_lunar（is_leap） |
| 53 | getChineseYear(int) | 1897 | 干支年 | ✅ | core._get_chinese_year |
| 54 | getStarSign(double,double[],String[]) | 1937 | 星宿名 | ⚠️ | core.calc_lunar_mansion（部分） |
| 55 | getZodiac(double,boolean) | 1957 | 地支/星座名 | ✅ | core._lon_to_branch |
| 56 | getZodiacShift(String,double) | 1963 | 地支顺逆 | ❌ | **未翻译**（神煞需要） |
| 57 | getMountain(double) | 1977 | 罗盘方位 | ❌ | **未翻译**（风水） |
| 58 | getElementalIndex(double) | 1987 | 五行索引 | ❌ | **未翻译**（五行判定） |
| 59 | getElementalStateIndex(double) | 1992 | 五行状态索引 | ❌ | **未翻译**（庙旺） |
| 60 | setMountainOffset(double) | 1997 | 设置罗盘偏移 | ❌ | **未翻译**（风水） |
| 61 | formatDegree(double,boolean,...) | 2002 | 度数格式化(4个重载) | ❌ | **未翻译**（显示） |
| 62 | getSignIndex(double,double[],int) | 2027 | 星座索引 | ❌ | **未翻译**（显示） |
| 63 | dispose() | 2194 | 释放资源 | 🗑️ | Python GC |
| 64 | dumpPlanetData(String,int,int,...) | 2199 | 导出行星数据 | ❌ | **未翻译**（数据导出） |
| 65 | compareTo(Object) | 2336 | 比较 | 🗑️ | 不需要 |

### Calculate.java 翻译统计

| 状态 | 数量 | 占比 |
|---|---|---|
| ✅ 已翻译 | 22 | 34% |
| ⚠️ 部分翻译 | 3 | 5% |
| ❌ 未翻译 | 33 | 51% |
| 🗑️ 不需要 | 7 | 11% |
| **合计** | **65** | **100%** |

**核心计算方法翻译率**（排除 🗑️）：25/58 = **43%**

**未翻译的重要方法**（按依赖排序）：
- **getZodiacShift**（地支顺逆）→ 神煞体系需要
- **getElementalIndex/getElementalStateIndex**（五行索引）→ 八字/规则引擎需要
- **getLATDateFromDate**（地方视太阳时）→ 择日需要
- **getLocalJulianDayUT**（时区JD）→ 非北京时区需要
- **computeStar/findStarByEquPos**（恒星）→ 恒星功能
- **computeAzimuth/getAltitude**（方位角/高度角）→ 罗盘/风水
- **computeGauquelin/computePheno**（高格林/视直径）→ 高级占星
- **computeSolarEclipse/computeLunarEclipse/getEclipseState**（日月食）→ 特殊命理
- **computePlanetTransit 系列**（推运）→ 流年推运
- **computeHousesFromMidHeaven**（从中天算宫位）→ 宫位矫正

## 四、关联文档

- <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/06-功能模块完整盘点.md" /> — 已有的功能盘点（状态标记待更新）
- <ref_file file="~/MOIRA_chinese_astrology-main/AGENTS.md" /> — 项目状态，TODO 部分将索引本文档
- <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/00-七政四余推命系统建设计划.md" /> — 建设计划，Phase 4+ 规划将更新
