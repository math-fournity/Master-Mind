# qizheng · 七政四余 Python 接口层

面向 AI 的七政四余排盘/矫正/分析工具集。从 MOIRA Java 源码研究重写为 Python，保留 Swiss Ephemeris 星历精度，输出 JSON 供 AI 调度与命理分析。

## 设计原则

- **KISS**：每个小工具职责单一，可独立运行，可组合成 pipeline。
- **JSON in/out**：所有工具输入输出 JSON，AI 直接解析。
- **AI 调度 + 经典计算**：代码做数值计算，AI 做命理判断。
- **围绕数据库**：命主/星盘/矫正/大限存 SQLite 单文件。

## 模块结构

```
qizheng/
├── core.py          # 核心计算库（封装 swisseph + 命理常量 + 七政四余算法）
├── constants.json   # 命理常量（从 moira_s.prop 提取）
├── chart.py         # 排盘小工具：输入生辰 → 星盘 JSON
├── daxian.py        # 大限小工具：输入生辰+年龄 → 大限/小限/飞限 JSON
├── rectify.py       # 矫正小工具：给定目标黄经 → 反推时间 JSON
├── db.py            # SQLite 数据库（命主/星盘/矫正/大限）
├── spike_chart.py   # Python spike（验证用，对齐 Java spike）
└── __init__.py
```

## 环境准备

```bash
# venv + pyswisseph
python3 -m venv .venv
.venv/bin/pip install pyswisseph

# 星历数据软链（已建）
# ephe -> moira_extra_files/ephe
```

## 用法

### 排盘

```bash
.venv/bin/python3 -m qizheng.chart --year 1990 --month 5 --day 15 --hour 3.5 --lon 116.4 --lat 39.9
# 或 JSON 输入
.venv/bin/python3 -m qizheng.chart --json '{"year":1990,"month":5,"day":15,"hour":3.5,"lon":116.4,"lat":39.9}'
```

输出：10 天体恒星黄道位置 + 12 宫宫头 + ASC/MC + 命宫 + 童限年数。

### 洞微大限

```bash
.venv/bin/python3 -m qizheng.daxian --year 1990 --month 5 --day 15 --hour 3.5 --age 35
```

输出：当前所在限 + 全部 12 限起止年龄/度数 + 小限 + 飞限。

### 星盘矫正

```bash
.venv/bin/python3 -m qizheng.rectify --year 1990 --month 5 --day 15 --hour 3.5 --target '{"sun":30.0}'
```

输出：给定目标黄经反推的时间 + 与初始时间的差值（小时）。

### 数据库

```python
from qizheng import db
conn = db.get_db()
sid = db.add_subject(conn, '命主名', birth_ut='1990-05-15T03:30', birth_lon=116.4, birth_lat=39.9)
# 排盘结果入库
db.add_chart(conn, sid, jd, params, bodies, houses, life_sign, child_limit_years)
```

## 算法来源

所有七政四余命理算法来自对 MOIRA 源码的研究（详见项目 AGENTS.md "Calculate.java 七政四余核心算法研究" 章节）：

- 恒星黄道：`Calculate.java:239-265` → `core.init_ephe()`
- 宫位：`Calculate.java:691-723` → `core.calc_houses()`
- 行星位置：`Calculate.java:427-463` → `core.calc_planet()`
- 命宫：`ChartData.java:6689-6705` → `core.calc_life_sign()`
- 童限：`ChartData.java:4362-4372` → `core.calc_child_limit_years()`
- 洞微大限：`ChartData.java:3901` + prop → `core.calc_daxian()`
- 小限/月限/飞限：`ChartData.java:7515-7584` → `core.small_limit()` / `core.fly_limit()`
- 节气：`Calculate.java:1102-1125` → `core.calc_solar_terms()`
- 矫正反推：`ChartData.java:7961-8027` → `core.find_date_at_sun_pos()`

## 已知 TODO

- `calc_life_sign` 传统算法的 `birth_adj_date` 基准日定义需确认（当前简化为出生日本身）。
- `calc_self_sign` 身宫算法需日落/月升时间（self_mode=1/2 时）。
- `fly_limit` 童限后的半年切换逻辑简化了，需对照 `fly_seq_half_shift` 完整实现。
- `calc_solar_terms` 的 `sol_cross_ut` API 需验证 pyswisseph 版本兼容性。
