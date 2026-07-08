# qizheng · 七政四余 Python 推命系统

从 MOIRA Java 源码完整重写为 Python，保留 Swiss Ephemeris 星历精度，提供排盘/神煞/格局/八字/限运/流年全功能。

## 设计原则

- **KISS**：每个模块职责单一，可独立运行，可组合成 pipeline。
- **JSON in/out**：所有工具输入输出 JSON，AI 直接解析。
- **AI 调度 + 经典计算**：代码做数值计算，AI 做命理判断。
- **与 Java 原版对齐**：行星位置精度 < 0.001°。

## 模块结构

```
qizheng/
├── __main__.py       # CLI 主入口：python -m qizheng
├── core.py           # 核心计算库（swisseph + 命理常量 + 七政四余算法）
├── chart.py          # 排盘主函数：build_chart()
├── render.py         # 文本渲染 + JSON 导出
├── daxian.py         # 大限小工具（独立运行）
├── rectify.py        # 星盘矫正小工具
├── db.py             # SQLite 数据库（命主/星盘/矫正/大限）
├── spike_chart.py    # Python spike（验证用，对齐 Java spike）
├── constants.json    # 命理常量（从 moira_s.prop 提取）
├── shen_sha_complete.json  # 神煞完整数据（126个key）
├── rules_library.json     # 格局规则库（134条→展开295条）
└── __init__.py
```

## 环境准备

```bash
python3 -m venv .venv
.venv/bin/pip install pyswisseph

# 星历数据软链（已建）
# ephe -> moira_extra_files/ephe
```

## 快速开始

### CLI 命令行

```bash
# 文本命盘
python -m qizheng 1990 5 15 3.5 116.4 39.9

# JSON 格式
python -m qizheng 1990 5 15 3.5 116.4 39.9 --json

# 神煞明细
python -m qizheng 1990 5 15 3.5 116.4 39.9 --verbose

# 只看匹配格局
python -m qizheng 1990 5 15 3.5 116.4 39.9 --quiet

# 输出到文件
python -m qizheng 1990 5 15 3.5 116.4 39.9 --json -o chart.json
```

参数：`year month day hour_ut longitude latitude`
- `hour_ut`: UT 小时（如 3.5 = 3:30 UT）
- `longitude/latitude`: 地理经纬度（东经北纬为正）

### Python API

```python
from qizheng.chart import build_chart
from qizheng.render import render_chart, export_json

# 构建命盘
chart = build_chart(1990, 5, 15, 3.5, 116.4, 39.9)

# 文本渲染
print(render_chart(chart))

# JSON 导出
json_str = export_json(chart)
```

## 输出结构

### build_chart 返回的 dict 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `input` | dict | 输入参数（日期/经纬度/JD） |
| `lunar` | dict | 农历信息（年月日/闰月/干支年） |
| `na_yin` | dict | 纳音五行（年命） |
| `rise_set` | dict | 升落/昼夜（日出日落JD/昼夜标签/月升月落） |
| `solar_terms` | list | 节气表（26个） |
| `bodies` | dict | 11颗星位置（黄经/纬度/距离/速度） |
| `mansions` | dict | 28宿宿度 |
| `speed_states` | dict | 行星状态（顺/逆/蚀/留/伏/迟/速） |
| `dignities` | dict | 庙旺平陷（殿/垣/庙/旺/乐/喜/怒） |
| `branch_stars` | dict | 地支神煞 |
| `four_poles` | list | 四柱干支 [年柱, 月柱, 日柱, 时柱] |
| `eight_char` | dict | 八字数据（十神/纳音/长生/藏干/空亡/季节） |
| `star_signs` | dict | 神煞系统（table/weak_houses/solid_houses） |
| `now_data` | dict | 流年推演（年龄/年柱/年星/流年神煞） |
| `limits` | dict | 限运（童限/小限/飞限/月限） |
| `rules` | dict | 格局判定（matched/total/matched_count） |
| `houses` | dict | 12宫位（宫头/ASC/MC） |
| `life_sign` | float | 命宫黄经 |
| `self_sign` | float | 身宫黄经 |
| `daxian` | list | 洞微大限（12限） |

### export_json 输出的 JSON 结构

```json
{
  "meta": { "system", "version", "generated_at" },
  "birth_info": { "date_ut", "jd", "longitude", "latitude", "is_day_birth", "day_night", ... },
  "lunar": { "lunar_year", "lunar_month", "lunar_day", "is_leap", "gan_zhi_year" },
  "four_pillars": { "year", "month", "day", "hour" },
  "eight_characters": { "day_master", "birth_season", "poles": [...] },
  "planets": { "sun": { "chinese_name", "longitude", "zodiac", "mansion", "dignity_states", "speed_state", ... }, ... },
  "houses": { "asc", "mc", "cusps": [...] },
  "shen_sha": { "total_count", "weak_houses", "solid_houses", "table" },
  "limits": { "child_limit", "small_limit", "fly_limit" },
  "now_year": { "age", "year_pole", "year_stars", "shen_sha_count" },
  "patterns": { "matched_count", "total", "matched": [...] }
}
```

## 功能清单

### 排盘引擎
- 11颗星位置（日月金木水火土 + 罗计孛炁四余）
- 恒星黄道（Lahiri ayanamsa）
- 12宫位（整宫制）
- 28宿宿度
- 命宫/身宫计算
- 升落/昼夜判断

### 八字系统
- 四柱干支计算
- 十神（比肩/劫财/食神/伤官/偏财/正财/七杀/正官/偏印/正印）
- 纳音五行（60甲子纳音）
- 长生十二运
- 地支藏干
- 空亡
- 出生季节（节气判断）

### 神煞系统
- 110个神煞（天干神煞/地支神煞/月神煞/时神煞）
- 30个年星（天禄/科名/天马/生官/天暗/...）
- 弱宫/强宫标记
- 流年神煞

### 格局规则引擎
- 134条规则（展开后295条）
- 24个内置函数（if/eval/map/test/set/offset/format/...）
- 模板规则展开（{日,月,金}垣 → &日垣/&月垣/&金垣）
- 规则引用（?{日月会}）
- 算术比较（@变量+6=@变量）
- 方位标记（?日东/?日南/?月西/?月北）
- __sp 行星排序（七政连环/五曜连珠/四余捧月）

### 限运系统
- 童限（child_seq 序列）
- 小限（每年逆行一宫）
- 月限（农历月计算）
- 飞限（fly_seq_yang/ying + half_shift）

### 流年推演
- 流年年柱计算
- 流年神煞
- 流年年星

### 行星状态
- 7种状态：顺/逆/蚀/留/伏/迟/速
- 庙旺平陷：殿/垣/庙/旺/乐/喜/怒

## 算法来源

所有七政四余命理算法来自对 MOIRA 源码的研究：

| 功能 | Java 源码 | Python 实现 |
|------|-----------|-------------|
| 恒星黄道 | `Calculate.java:239-265` | `core.init_ephe()` |
| 宫位 | `Calculate.java:691-723` | `core.calc_houses()` |
| 行星位置 | `Calculate.java:427-463` | `core.calc_planet()` |
| 命宫 | `ChartData.java:6689-6705` | `core.calc_life_sign()` |
| 童限 | `ChartData.java:4362-4372` | `core.calc_child_limit_years()` |
| 洞微大限 | `ChartData.java:3901` | `core.calc_daxian()` |
| 小限/飞限 | `ChartData.java:7515-7584` | `core.get_small_limit()` / `core.get_fly_limit()` |
| 节气 | `Calculate.java:1102-1125` | `core.calc_solar_terms()` |
| 矫正反推 | `ChartData.java:7961-8027` | `core.find_date_at_sun_pos()` |
| 四柱干支 | `ChartData.java:chineseCalendar` | `core.calc_four_poles()` |
| 神煞 | `ChartData.java:getStarSigns` | `core.get_star_signs()` |
| 八字 | `ChartData.java:getTenGodName` 等 | `core.compute_eight_char_data()` |
| 规则引擎 | `EvalRule.java` | `core.eval_rules()` / `core._eval_simple_condition()` |
| 限运 | `ChartData.java:getChildLimit` 等 | `core.compute_limits()` |
| 流年 | `ChartData.java:computeNowData` | `core.compute_now_data()` |

## 精度验证

与 Java 原版 SpikeChart 对比，5个测试用例行星黄经最大差值 0.000171°（约0.6角秒），全部 PASS。

```
测试1: 1990-05-15 — 最大差值 0.000171° PASS
测试2: 1985-11-22 — 最大差值 0.000043° PASS
测试3: 2000-01-01 — 最大差值 0.000043° PASS
测试4: 1978-08-08 — 最大差值 0.000043° PASS
测试5: 1995-06-18 — 最大差值 0.000043° PASS
```
