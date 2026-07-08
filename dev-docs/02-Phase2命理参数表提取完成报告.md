# Phase 2 命理参数表提取完成报告

**完成时间**：2026-07-15
**Phase**：Phase 2 - 命理参数表提取
**状态**：✅ 完成

---

## 一、本轮完成内容

### 2.1 庙旺平陷表（殿/垣/庙/旺/乐/喜/怒）

**数据来源**：`moira_extra_files/moira_s.prop` 的 `星辰日/月/金/木/水/火/土/计/罗/炁/孛` 字段

**constants.json 新增**：`dignity_states`
- 11 星曜（日/月/金/木/水/火/土/计/罗/炁/孛）× 12 地支
- 7 种状态：殿 > 垣 > 庙 > 旺 > 乐 > 喜 > 怒
- 同一地支可有多个状态（如太阳在午 = 垣 + 庙 + 乐）
- 用列表格式 `[[branch, state], ...]` 存储避免 JSON 重复 key 覆盖

**实现函数**：
- `core.calc_dignity(planet_name, branch)` - 按地支查询
- `core.calc_dignity_from_lon(planet_name, lon)` - 按黄经查询（自动转地支）
- `core._lon_to_branch(lon)` - 恒星黄经→地支（戌=0°，逆序）

**验证结果**：
| 输入 | 期望 | 实际 | 状态 |
|---|---|---|---|
| 太阳在午 | 垣+庙+乐 | 垣+庙+乐 | ✅ |
| 太阳在子 | 无 | 无 | ✅ |
| 金星在寅 | 怒 | 怒 | ✅ |
| 土星黄经271°（午） | 垣+庙+乐 | 垣+庙+乐 | ✅ |
| 金星黄经348°（亥） | 旺 | 旺 | ✅ |

### 2.2 六十甲子纳音五行表

**数据来源**：`moira_s.prop` 的 `纳音甲子/乙丑/.../癸亥` 字段

**constants.json 新增**：`na_yin_60`
- 60 组干支→纳音五行（如甲子=海中金，庚午=路旁土）

**实现函数**：
- `core.calc_na_yin(gan_zhi)` - 按干支查询
- `core.calc_na_yin_from_year(year)` - 按年份查询（年命）

**验证结果**：
| 输入 | 期望 | 实际 | 状态 |
|---|---|---|---|
| 甲子 | 海中金 | 海中金 | ✅ |
| 庚午 | 路旁土 | 路旁土 | ✅ |
| 1990年 | 庚午/路旁土 | 庚午/路旁土 | ✅ |

### 2.3 十干化曜表

**数据来源**：`moira_s.prop` 的 `ten_god_list_org` / `ten_god_list_alt` / `stem_mapping`

**constants.json 新增**：`ten_god_transform`
- 10 天干→11 化曜星（天禄/天暗/天福/天耗/天荫/天贵/天嗣/天刑/天印/天囚/天权）
- 替代名：比肩/劫财/食神/伤官/偏财/正财/七杀/正官/偏印/正印

**实现函数**：`core.calc_ten_god_transform(stem)`

**验证结果**：
| 输入 | 期望 | 实际 | 状态 |
|---|---|---|---|
| 甲 | 天禄/比肩 | 天禄/比肩 | ✅ |
| 庚 | 天嗣/七杀 | 天嗣/七杀 | ✅ |

### 2.4 天干吉凶星曜表

**数据来源**：`moira_s.prop` 的 `天干甲/乙/.../癸` 字段

**constants.json 新增**：`stem_stars`
- 10 天干×12 地支→13 种吉凶星曜（禄勋/天贵/玉贵/天厨/文昌/阳刃/飞刃/国印/红艳/流霞/学堂/福贵/官贵）
- 用列表格式 `[[branch, star], ...]` 存储避免 JSON 重复 key 覆盖

**实现函数**：`core.calc_stem_stars(stem, branch)`

**验证结果**：
| 输入 | 期望 | 实际 | 状态 |
|---|---|---|---|
| 甲×寅 | 禄勋+福贵 | 禄勋+福贵 | ✅ |
| 甲×酉 | 飞刃+流霞+官贵 | 飞刃+流霞+官贵 | ✅ |
| 甲×子 | 无 | 无 | ✅ |

---

## 二、Gate Reconciliation

| 计划 Gate | 验收标准 | 实际证据 | 状态 |
|---|---|---|---|
| 庙旺平陷表 | 11星曜×12地支完整 | constants.json dignity_states + calc_dignity | Done |
| 纳音五行表 | 60甲子完整 | constants.json na_yin_60 + calc_na_yin | Done |
| 十干化曜表 | 10天干→化曜星 | constants.json ten_god_transform + calc_ten_god_transform | Done |
| 天干星曜表 | 10天干×12地支→星曜 | constants.json stem_stars + calc_stem_stars | Done |
| chart.py集成 | 星盘JSON含新参数 | na_yin + dignities 已集成 | Done |

---

## 三、技术要点

### JSON 重复 key 问题

`moira_s.prop` 中同一地支可有多个状态/星曜（如 `午:垣,午:庙,午:乐`）。直接转为 JSON dict 会覆盖重复 key。解决方案：用 `[[branch, value], ...]` 列表格式存储。

### 地支与黄经的对应关系

七政四余地支从戌开始（戌=0°），逆序排列：戌→酉→申→未→午→巳→辰→卯→寅→丑→子→亥，每30°一个地支。

---

## 四、下一步

Phase 3：格局判定规则提取
- 研究 EvalRule.java + RuleParse.java + Rule.yacc 的规则引擎结构
- 提取命理格局判定规则（如"日月同宫"、"五星环阳"、"罗计截空"等）
- 建立机器可读的规则库 JSON
