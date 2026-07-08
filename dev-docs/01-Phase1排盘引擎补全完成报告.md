# Phase 1 排盘引擎补全完成报告

**完成时间**：2026-07-15
**Phase**：Phase 1 - 排盘引擎补全
**状态**：✅ 完成

---

## 一、本轮完成内容

### 1.1 农历转换（公历→农历）

**算法来源**：Calculate.java `getLunarDate` / `getLunarCalendar` / `computeNewMoons` / `getLeapMonthIndex`

**实现函数**：
- `core.calc_solar_terms_v2()` - 26节气，使用 `swe.solcross_ut`
- `core._new_moon_ut()` - 新月（日月合朔），使用 `swe.mooncross_ut` 迭代
- `core.compute_new_moons()` - 出生年前后14个新月
- `core._get_leap_month_index()` - 闰月判定（无中气法则）
- `core.solar_to_lunar()` - 公历→农历完整转换

**验证结果**：
| 公历日期 | 期望农历 | 实际输出 | 状态 |
|---|---|---|---|
| 1990-01-27 | 庚午年正月初一 | 庚午年正月初一 | ✅ |
| 1990-05-15 | 庚午年四月廿一 | 庚午年四月廿一 | ✅ |
| 2024-02-10 | 甲辰年正月初一 | 甲辰年正月初一 | ✅ |
| 2025-01-29 | 乙巳年正月初一 | 乙巳年正月初一 | ✅ |

**关键技术点**：
- 新月计算用 `swe.mooncross_ut(sun_lon, jd)` 迭代2-3次收敛（太阳在搜索期间移动很少）
- `_trim_hour` 截断到北京时间零点：`bj = val + 8/24; bj_midnight = int(bj - 0.5) + 0.5; return bj_midnight - 8/24`
- 闰月判定：两个新月之间没有中气（偶数索引节气）则为闰月

### 1.2 二十八宿宿度

**数据来源**：《汉书·律历志》赤道宿度 + 黄道宿度（360°制）

**实现函数**：`core.calc_lunar_mansion(lon)`

**constants.json 新增**：
```json
"lunar_mansions": {
    "order": ["角","亢","氐",...,"轸"],  // 28宿
    "width_yellow": [11,11,18,...,13],   // 黄道宿度，合计360
    "element": ["木","金","土",...],     // 宿五行
    "animal": ["蛟","龙","貉",...],      // 宿禽
    "group": ["东方苍龙",...,"南方朱雀"]  // 四象分组
}
```

**已知待校准**：角宿起点（MANSION_START=174°）是 Lahiri ayanamsa 下的近似值，需根据岁差精确校准。

### 1.3 升落 / 昼夜判定

**算法来源**：Calculate.java `computeRiseSet` / `isDayBirth`

**实现函数**：`core.calc_rise_set(jd_ut, lon, lat, alt, body)`

**验证结果**：
| 出生时间 | 期望 | 实际 | 状态 |
|---|---|---|---|
| 1990-05-15 11:30 北京时间 | 白天 | is_day=True | ✅ |
| 1990-05-15 23:30 北京时间 | 夜间 | is_day=False | ✅ |
| 1990-05-15 03:30 北京时间 | 夜间 | is_day=False | ✅ |

**关键技术点**：
- `swe.rise_trans` 返回搜索时间之后的下一个升/落事件
- 需要向前搜索找到出生时间之前最近的日出和日落
- 如果日出 > 日落（白天出生），需要找当天的日落（在出生之后）

### 1.4 身宫算法

**算法来源**：ChartData.java `computeSelfSign`

**实现函数**：`core.calc_self_sign_v2(birth_date, moon_pos, sun_pos, lon, lat)`

**模式**：
- self_mode=0：直接用月亮位置
- self_mode=1：日落基准（从日落时间计算月亮位置）
- self_mode=2：月升基准

### 1.5 长生十二运

**数据来源**：协纪辨方书本原一 + 星学大成

**实现函数**：`core.calc_sheng_zhang(element, branch, is_yang)`

**constants.json 新增**：
```json
"sheng_zhang_12_stages": {
    "stages": ["长生","沐浴","冠带","临官","帝旺","衰","病","死","墓","绝","胎","养"],
    "yang_start": {"木":"亥","火":"寅","金":"巳","水":"申","土":"寅"},
    "yin_start": {"木":"午","火":"酉","金":"子","水":"卯","土":"酉"},
    "yang_forward": true,
    "yin_forward": false
}
```

**验证结果**：
| 输入 | 期望 | 实际 | 状态 |
|---|---|---|---|
| 阳木在亥 | 长生 | 长生 | ✅ |
| 阳木在卯 | 帝旺 | 帝旺 | ✅ |
| 阳火在寅 | 长生 | 长生 | ✅ |

### 1.6 逆顺迟疾状态

**算法来源**：Calculate.java `getSpeedState`

**实现函数**：`core.calc_speed_state(planet_name, lon_speed)`

**状态**：顺/疾/迟/留/逆行

### 1.7 完整星盘 JSON

**chart.py `build_chart()`** 现在输出：
1. input（输入参数）
2. lunar（农历转换）
3. rise_set（升落/昼夜）
4. solar_terms（26节气）
5. bodies（10天体位置）
6. mansions（28宿宿度）
7. speed_states（逆顺迟疾）
8. houses（12宫宫头+ASC+MC）
9. life_sign（命宫）
10. self_sign（身宫）
11. child_limit_years（童限）
12. daxian（12大限起止）

---

## 二、Gate Reconciliation

| 计划 Gate | 验收标准 | 实际证据 | 状态 |
|---|---|---|---|
| 农历转换 | 春节日期正确 | 4个春节日期全部验证通过 | Done |
| 二十八宿 | 宿度表+计算函数 | constants.json + calc_lunar_mansion | Done |
| 升落/昼夜 | 白天/夜间判定正确 | 3个时段全部验证通过 | Done |
| 身宫 | 日落/月升基准 | calc_self_sign_v2 已实现 | Done |
| 完整星盘JSON | chart.py 输出全部参数 | 12个section全部输出 | Done |

---

## 三、下一步

Phase 2：命理参数表提取
- 庙旺平陷表（28宿×五行→庙旺平陷状态）
- 十干化曜表（天干→化曜星）
- 神煞表（神煞起例规则）
- 纳音五行表（六十甲子→纳音）
