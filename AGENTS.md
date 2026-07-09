# 项目 AGENTS.md · MOIRA 七政四余排盘与星盘矫正

## 项目定位

本项目是 **AI 七政四余排盘、矫正星盘项目**，不是单纯的写代码项目。

底座是知名七政四余排盘软件 **MOIRA**（由 athomeprojects 建立，GPL 协议）的源代码。AI 需要在其基础上进行 **了解、调整、编译**，使其能辅助 AI 完成排盘、矫正、分析任务。

## 项目目标

建设一个 **"代码精确排盘 + 规则库可审计 + AI 智能判读"** 的七政四余推命系统。

让这套排盘软件可以辅助 AI 完成：

1. **七政四余排盘** —— 根据命主生辰信息排出七政四余星盘。
2. **命主星盘矫正** —— 对存疑或缺失出生时间的命主，进行星盘时间矫正。
3. **洞微大限等分析** —— 基于排盘与矫正结果，开展洞微大限等命理分析。

**终态目标与建设计划**：见 <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/00-七政四余推命系统建设计划.md" />

## AI 计算 + 经典计算 相结合

本项目的工作模式是 **AI 智能 + 经典数值计算 相结合**，二者分工明确：

| 工作类型 | 由谁完成 | 载体 |
|---|---|---|
| **数值计算**（星历、宫位、行星位置、大限起算、矫正求解等） | **代码**完成 | MOIRA Java 实现 / Swiss Ephemeris / CS41.py（ephem+scipy） |
| **命理分析**（星盘格局判读、命主推断、洞微大限推演、矫正结果取舍等） | **AI 智能**完成 | AI 在对话中直接给出 |

- **后续 AI 需要做数值计算时** → 调用本项目代码（编译运行的 MOIRA，或 CS41.py 等脚本）来完成，不靠 AI 心算。
- **需要进行命理分析时** → 由 AI 智能给出，代码只提供计算原料。
- **二者结合**：代码产出精确数值，AI 在数值之上做命理判断与解释。

## 改造理念 · 从"给人看"到"给 AI 看"

原 MOIRA 是 **给人看** 的排盘软件（GUI 星盘图，人工判读）。现在要变成 **给 AI 看** 的排盘引擎（JSON 结构化数据，AI 判读）。

改造原则：
1. **核心逻辑保留**：星历计算、宫位推算、大限起算、矫正算法等数值核心不动。
2. **接口层重构**：剥离 GUI，改出面向 AI 的接口（CLI / pipeline / 函数库）。
3. **KISS 原则**：一组职责单一、可组合的小工具，不做大而全 CLI。
4. **pipeline 化**：围绕数据库串成 pipeline。
5. **结果 JSON 化**：所有工具输出 JSON。
6. **AI 调度 + 经典计算**：AI 负责调度与命理判断，代码负责数值计算。

目标形态：
```
AI（调度 + 命理分析）
   │  JSON in/out
   ▼
┌─────────── 围绕数据库 ───────────┐
│  chart_db (命主 / 星盘 / 矫正 / 大限) │
└──────────────────────────────────┘
   ▲          ▲          ▲          ▲
   │ JSON     │ JSON     │ JSON     │ JSON
┌──┴───┐  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐
│排盘  │  │矫正  │  │大限  │  │流年  │   ← KISS 小工具，各司其职
│chart │  │rectif│  │daxian│  │liunian│
└──────┘  └──────┘  └──────┘  └──────┘
   ▼          ▼          ▼          ▼
              核心计算层（保留）
   Calculate / ChartData / Swiss Ephemeris / CS41.py
```

## 代码结构速查

### 原 MOIRA 源码（Java，给人看的旧形态）

| 目录/文件 | 角色 | 说明 |
|---|---|---|
| `moira/` | SWT GUI 层 | 主程序入口 `Moira.java`，各 Dialog 为功能界面（重构可丢弃） |
| `base/` | 核心逻辑层 | `Calculate`（星历计算）、`ChartData`（星盘数据/大限，9424 行上帝类）、`ChartMode`（模式）、`EvalRule`/`RuleParse`（命理规则引擎）、`Rule.yacc`（规则语法） |
| `swisseph/` | 星历底座 | Swiss Ephemeris 的 Java 移植，行星/恒星位置计算（已验证可独立运行） |
| `moiraApplet/` | Applet 版本 | 网页版排盘（重构可丢弃） |
| `awtext/` | AWT 控件 | 日历/位置选择等（重构可丢弃） |
| `CS41.py` | Python 辅助（旧） | 用 `ephem` + `scipy.optimize.minimize` 做星盘矫正，main() 写死 CSV 路径，待重新包装 |
| `moira_extra_files/` | 运行资源 | `ephe/` 星历数据、`*.prop` 属性文件（命理常量源）、SWT jar/DLL、地磁模型 COF |
| `src/module-info.java` | 模块声明 | 模块名 `FINANCIALASTROLOGY` |

### 重构产物（Python，给 AI 看的新形态）

| 目录/文件 | 角色 | 说明 |
|---|---|---|
| `qizheng/` | **Python 接口层（主产物）** | 七政四余排盘/矫正/分析工具集（Phase 1-12 全部完成） |
| `qizheng/core.py` | 核心计算库（~2831行） | 封装 swisseph + 命理常量 + 60+ 个七政四余算法函数 |
| `qizheng/chart.py` | 排盘主函数 | `build_chart()` 一次调用 → 22 个顶层字段的完整命盘 |
| `qizheng/render.py` | 文本渲染 + JSON 导出（~515行） | `render_chart()` 文本命盘 + `export_json()` 规范化 JSON |
| `qizheng/svg_chart.py` | SVG 图形命盘（~200行） | `render_svg()` 12宫圆盘可视化 |
| `qizheng/__main__.py` | CLI 命令行入口（~83行） | `python -m qizheng` 文本/JSON/SVG 输出 |
| `qizheng/api.py` | Web API 服务（~111行） | FastAPI 封装 5 个 RESTful 接口 |
| `qizheng/daxian.py` | 大限小工具 | 输入生辰+年龄 → 大限/小限/飞限 JSON |
| `qizheng/rectify.py` | 矫正小工具 | 输入目标黄经 → 反推时间 JSON |
| `qizheng/db.py` | SQLite 数据库 | 命主/星盘/矫正/大限 4 表，单文件 `qizheng.db` |
| `qizheng/constants.json` | 命理常量 | 28宿/长生十二运/庙旺平陷/纳音/十干化曜/天干星曜/地支神煞 |
| `qizheng/rules_library.json` | 格局规则库 | 134条规则（模板展开后295条），全部可求值 |
| `qizheng/shen_sha_complete.json` | 完整神煞数据 | 7大类神煞（年干/流年/干支/天干/地支/月/时）+ 三煞 |
| `qizheng/README.md` | 模块文档 | 环境准备/用法/算法来源 |
| `spike/` | Java spike | 验证 swisseph 可脱离 GUI 运行 |
| `ephe` | 软链 | → `moira_extra_files/ephe`，星历路径对齐 |
| `.venv/` | Python 虚拟环境 | 含 pyswisseph 2.10.3.2 |

## 关键功能定位

### 在原 MOIRA 源码中（研究参考用）

- **七政四余（恒星黄道）**：`base/Calculate.java` 的 `sidereal_mode` + `sidereal_systems`；界面 `moira/SiderealDialog.java`。
- **大限（limit）**：`base/ChartData.java` 的 `limit_seq`（12 限序列）、`limit_ring`（限环绘制）；`addYearToBirthDate` 推算限年。
- **时间矫正**：`moira/TimeDialog.java`（`dialog_time_correct`）；`CS41.py` 用 scipy 数值求解做更精细矫正。
- **宫位矫正**：`moira/HouseDialog.java`（`house_correction`）。
- **命理规则引擎**：`base/EvalRule.java` + `base/RuleParse.java` + `base/Rule.yacc`，可扩展命理判读规则。
- **赤道/黄道修正**：`base/Calculate.java` 的 `correction_key`（`fixstar_equ_adjustments`）。

### 在 Python 接口层中（实际使用入口 · 5 层）

| 层级 | 入口 | 用法 | 适用场景 |
|---|---|---|---|
| **L1 核心库** | `qizheng.core` | `from qizheng import core` | 细粒度控制单个算法步骤 |
| **L2 排盘主函数** | `qizheng.chart.build_chart()` | `from qizheng.chart import build_chart` | **AI 论命标准入口**——一次调用拿全部原料（22个顶层字段） |
| **L3 CLI** | `qizheng.__main__` | `python -m qizheng Y M D H LON LAT [--json|--svg|--quiet]` | 命令行快速排盘 |
| **L4 Web API** | `qizheng.api` | `uvicorn qizheng.api:app` → 5个RESTful接口 | Web 应用集成 |
| **L5 数据库** | `qizheng.db` | `from qizheng import db` → 4表CRUD | 命主档案管理/矫正历史/大限存档 |
| **专项 矫正** | `qizheng.rectify` | `python -m qizheng.rectify --target '{"sun":30.0}'` | 出生时间矫正 |

## 编译与运行环境

- **Java**：本机 `/opt/homebrew/opt/openjdk`（OpenJDK 25）。MOIRA 原为 Java 早期版本编写，编译时需注意 SWT 依赖与 module 兼容性。swisseph 源文件为 Latin-1 编码，编译需 `-encoding ISO-8859-1`。
- **Python**：本机 `python3`（3.14）。`CS41.py` 依赖 `ephem`、`scipy`、`pandas`、`numpy`，运行前需确认依赖已装。
- **Python venv**：`.venv/`（项目内虚拟环境），含 `pyswisseph 2.10.3.2`。Homebrew Python 不让直接装包，故用 venv。运行 qizheng 工具用 `.venv/bin/python3 -m qizheng.xxx`。
- **SWT**：`moira_extra_files/swt-win.jar` 与 DLL 为 Windows 版本；macOS 上运行 GUI 需替换为 macOS 版 SWT jar（重构后不再需要 GUI）。
- **星历数据**：项目已自带完整 Swiss Ephemeris 数据（`moira_extra_files/ephe/`），无需另行下载。已建软链 `ephe -> moira_extra_files/ephe`。

## Python 接口层实现（qizheng/）

**Phase 1-12 全部完成**。核心排盘/神煞/格局/八字/限运/流年/CLI/API/SVG 全功能已实现并通过 20/20 全量回归测试。

### 模块结构

```
qizheng/
├── core.py              # 核心计算库（~2759行，60+ 算法函数）
├── constants.json       # 命理常量（28宿/长生/庙旺/纳音/十干化曜/天干星曜/地支神煞）
├── rules_library.json   # 格局规则库（134条，模板展开后295条）
├── shen_sha_complete.json # 完整神煞数据（7大类+三煞）
├── chart.py             # 排盘主函数 build_chart() → 22个顶层字段
├── render.py            # 文本渲染 + JSON 导出（~515行）
├── svg_chart.py         # SVG 图形命盘（~200行）
├── __main__.py          # CLI 命令行入口
├── api.py               # FastAPI Web API（5个接口）
├── daxian.py            # 大限小工具
├── rectify.py           # 矫正小工具
├── db.py                # SQLite 数据库（4表）
├── spike_chart.py       # Python spike（验证用）
├── README.md            # 模块文档
└── __init__.py
```

详细文档见 <ref_file file="~/MOIRA_chinese_astrology-main/qizheng/README.md" />。

### 核心库 core.py 已实现算法

| 函数 | 对应 MOIRA 源码 | 状态 |
|---|---|---|
| `init_ephe()` | Calculate.setChartMode (Lahiri) | ✅ |
| `calc_planet()` / `calc_all_bodies()` | Calculate.compute | ✅ 四余含双模式 |
| `calc_ziqi()` | ChartData setOrbitData (紫炁自定义轨道) | ✅ 匀速线性运动，28年周期 |
| `set_four_yu_mode()` | ChartData true_as_north 开关 | ✅ 新法/旧法罗睺 + mean/oscu月孛 |
| `calc_houses()` | Calculate.computeHouses | ✅ |
| `calc_life_sign()` | ChartData.computeLifeSign | ✅ |
| `calc_self_sign_v2()` | ChartData.computeSelfSign | ✅ 日落/月升基准 |
| `calc_child_limit_years()` | ChartData.getChildLimit | ✅ |
| `calc_daxian()` / `daxian_full()` | ChartData.nowYearPosition | ✅ |
| `compute_limits()` | ChartData 限运综合 | ✅ 当前所在限+限内行运星 |
| `get_child_limit()` / `get_small_limit()` | ChartData.getChildLimit/getSmallLimit | ✅ |
| `get_month_limit()` / `get_fly_limit()` | ChartData.getMonthLimit/getFlyLimit | ✅ |
| `calc_solar_terms_v2()` | Calculate.computeSolarTerms | ✅ 使用 swe.solcross_ut |
| `compute_new_moons()` | Calculate.computeNewMoons | ✅ 使用 swe.mooncross_ut 迭代 |
| `solar_to_lunar()` | Calculate.getLunarDate | ✅ 已验证4个春节日期正确 |
| `calc_rise_set()` | Calculate.computeRiseSet | ✅ 白天/夜间判定正确 |
| `calc_lunar_mansion()` | 二十八宿宿度 | ✅ 28宿宿度表 |
| `calc_sheng_zhang()` | 长生十二运 | ✅ 五行×地支→十二运 |
| `calc_speed_state()` | Calculate.getSpeedState | ✅ 逆顺迟疾判定 |
| `calc_dignity()` / `calc_dignity_from_lon()` | moira_s.prop 星辰表 | ✅ 庙旺平陷（殿/垣/庙/旺/乐/喜/怒） |
| `calc_na_yin()` / `calc_na_yin_from_year()` | moira_s.prop 纳音表 | ✅ 六十甲子纳音五行 |
| `calc_ten_god_transform()` | moira_s.prop 十干化曜 | ✅ 天干→化曜星 |
| `calc_stem_stars()` / `calc_stem_stars_from_branch()` | moira_s.prop 天干星曜 | ✅ 天干×地支→吉凶星曜 |
| `calc_branch_stars()` / `calc_branch_stars_for_all()` | moira_s.prop 地支神煞 | ✅ 年支×地支→38神曜 |
| `calc_four_poles()` | ChartData 八字四柱 | ✅ 年月日时四柱干支（`use_solar_terms=True`节气分年月/`False`农历分年月，Phase 24修复） |
| `compute_eight_char_data()` | ChartData.computeEightCharData | ✅ 四柱/十神/长生/纳音/藏干/弱宫/季节 |
| `compute_weak_house()` | ChartData.computeWeakHouse | ✅ 弱宫/强宫 |
| `get_weak_solid_houses()` | ChartData 弱宫强宫 | ✅ |
| `get_star_signs()` | ChartData 神煞完整体系 | ✅ 12地支×神煞 + 12宫位×神煞 |
| `get_year_info()` | ChartData.getYearInfo | ✅ 流年神煞 |
| `compute_now_data()` | ChartData.computeNowData | ✅ 流年推演（年柱+四柱+神煞+年星） |
| `get_zodiac_shift()` | ChartData.getZodiacShift | ✅ 地支顺逆 |
| `get_elemental_index()` / `get_elemental_state_index()` | ChartData 五行索引 | ✅ |
| `get_earth_god_seq()` | ChartData 地支神煞序列 | ✅ |
| `get_birth_season()` | 节气季节判定 | ✅ |
| `get_long_life_name()` / `get_ten_god_name()` | 名称查表 | ✅ |
| `get_year_sound_name()` | 纳音名称查表 | ✅ |
| `load_rules_library()` | EvalRule + Rule.yacc | ✅ 加载134条格局规则 |
| `eval_rules()` | EvalRule.computeRules | ✅ 完整求值器，283条规则可求值（含sign字段，Phase24b扩充） |
| `score_rules()` | — | ✅ 格局质量评分模型v3（Phase24b：数据驱动权重+关键格局加权+组合惩罚/奖励+命格等级建议，高低命格差14.1分） |
| `find_date_at_sun_pos()` | ChartData.getDateAtSunPos | ✅ |
| `find_date_at_planet_pos()` | ChartData.getDateAtPlanetPos | ✅ |
| `jd_from_ymd_ut()` / `ymd_ut_from_jd()` | Calculate 儒略日转换 | ✅ |
| `degree_gap()` | 黄经差计算 | ✅ |

### 命理常量提取

`constants.json` 从 `moira_extra_files/moira_s.prop`（UTF-16BE）提取，含：
- `limit_seq`（洞微大限 12 限年数）
- `child_seq` / `fly_seq_yang/ying`（童限/飞限序列）
- `zodiac` / `mountain_signs`（星座/24 山）
- `house_system_char`（宫位制）
- `life_mode` / `self_mode` / `child_period`（算法模式开关）
- `lunar_mansions`（二十八宿宿度表：28宿名/黄道宿度/五行/禽名/四象分组）
- `sheng_zhang_12_stages`（长生十二运表：五行×地支→十二运状态+旺度）
- `dignity_states`（庙旺平陷表：11星曜×地支→殿/垣/庙/旺/乐/喜/怒）
- `na_yin_60`（六十甲子纳音五行表）
- `ten_god_transform`（十干化曜表：天干→天禄/天暗/.../天权）
- `stem_stars`（天干吉凶星曜表：天干×地支→禄勋/天贵/.../官贵）
- `branch_stars`（地支神煞表：12年支×地支→38神曜）

### 命理格局规则库

`rules_library.json` 从 `moira_s.prop` 提取，含：
- 134 条吉格局规则（`+` 开头），模板展开后 **295 条**，**全部可求值**（零异常）
- 每条规则含：编号、名称、优先级 `[level.rank.sub]`、条件表达式、排斥规则、注释
- 优先级分布：[1.2.0] 4条 / [2.0.x] 19条 / [2.2.0] 18条 / [2.3.0] 43条 / [2.4.0] 5条 / [3.1.0] 10条 / [3.2.0] 20条 / [4.x.0] 9条
- 规则语言支持：`@`（黄道星座）/ `%`（恒星宿度）/ `$`（字符串）/ `?`（布尔判定）/ `&|!`（逻辑运算）/ `&func()`（函数调用）
- **24 个内置函数**：if/eval/map/test/set/offset/format/prefix/suffix/intersection/union/complement/contain/iter/trim/entry/split/empty/size/import/int/round/abs
- **模板规则展开**：`{日,月,金}垣` → `&日垣`/`&月垣`/`&金垣`
- **规则引用**：`?{日月会}`（引用其他规则的求值结果）
- **算术比较**：`@变量+N=@变量`（正向+反向均已实现）
- **方位标记**：`?日东`/`?日南`/`?月西`/`?月北`（11星×4方位）
- **__sp 行星排序**：6种连珠格局（七政连环/五曜随阳/五星随月/五曜连珠/五曜环阳/四余捧月）
- **星曜变量**：`@[星名]` 变量（紫微/禄勋等，基于神煞地支）
- Python 求值器 `core.eval_rules()` 完整实现，**295/295 条可求值**

### SQLite 数据库

`db.py` + `qizheng.db`（单文件），4 表：
- `subject`：命主档案
- `chart`：星盘记录
- `rectification`：矫正历史
- `daxian`：大限结果

### 运行方式

```bash
# CLI — 文本命盘
.venv/bin/python3 -m qizheng 1990 5 15 3.5 116.4 39.9

# CLI — JSON 格式
.venv/bin/python3 -m qizheng 1990 5 15 3.5 116.4 39.9 --json

# CLI — SVG 图形命盘
.venv/bin/python3 -m qizheng 1990 5 15 3.5 116.4 39.9 --svg

# CLI — 只看匹配格局
.venv/bin/python3 -m qizheng 1990 5 15 3.5 116.4 39.9 --quiet

# Web API — 启动服务
.venv/bin/python3 -m qizheng.api
# 或 uvicorn qizheng.api:app --host 0.0.0.0 --port 8000

# 矫正 — 太阳位置反推
.venv/bin/python3 -m qizheng.rectify --year 1990 --month 5 --day 15 --hour 3.5 --target '{"sun":30.0}'

# Python API — AI 论命标准入口
# from qizheng.chart import build_chart
# chart = build_chart(1990, 5, 15, 3.5, 116.4, 39.9)
# → 22个顶层字段全部就绪
```

### build_chart() 输出结构（22 个顶层字段）

`build_chart(y, mo, d, h, lon, lat)` 是 AI 论命的标准入口，一次调用返回完整命盘：

| 字段 | 类型 | 内容 | 传统论命步骤 |
|---|---|---|---|
| `input` | dict | 输入参数（jd/lon/lat/ayanamsa/house_system） | — |
| `lunar` | dict | 农历（年/月/日/闰/干支年/中文年号） | Step 1 历法 |
| `na_yin` | dict | 纳音（纳音/五行/干支） | Step 8 状态 |
| `rise_set` | dict | 升落（日出/日落/昼生夜生/月升月落） | Step 1 历法 |
| `solar_terms` | list(26) | 二十四节气 UT 时间 | Step 1 历法 |
| `bodies` | dict(11) | 11天体黄经位置（日月金木水火土+罗计孛炁） | Step 2 星历 |
| `mansions` | dict(11) | 11天体所在二十八宿宿度 | Step 2 星历 |
| `speed_states` | dict(11) | 11天体逆顺迟疾状态 | Step 2 星历 |
| `dignities` | dict(11) | 11天体庙旺平陷（殿/垣/庙/旺/乐/喜/怒） | Step 8 状态 |
| `branch_stars` | dict(11) | 11天体地支神煞 | Step 6 化曜 |
| `four_poles` | list(4) | 四柱干支（年月日时） | Step 5 八字 |
| `eight_char` | dict | 八字完整数据（四柱/日主/十神/长生/纳音/藏干/弱宫/季节） | Step 5 八字 |
| `star_signs` | dict | 神煞完整表（12地支×神煞 + 12宫位×神煞 + 弱宫/强宫） | Step 7 神煞 |
| `now_data` | dict | 流年推演（年龄/年柱/四柱/神煞/年星） | Step 10 流年 |
| `limits` | dict | 限运（童限/小限/飞限） | Step 4 限运 |
| `rules` | dict | 格局（matched/total/matched_count，295条规则） | Step 9 格局 |
| `houses` | dict | 宫位（12宫头 + ASC + MC） | Step 3 宫位 |
| `life_sign` | float | 命宫黄经位置 | Step 3 宫位 |
| `self_sign` | float | 身宫黄经位置 | Step 3 宫位 |
| `child_limit_years` | int | 童限年数 | Step 4 限运 |
| `daxian` | list(12) | 洞微大限12限（每限：索引/起止年龄/年数/起止黄经） | Step 4 限运 |
| `current_daxian` | dict | 当前所在限（索引/年数/限内年龄/限内度数/起始黄经） | Step 4 限运 |
| `daxian_stars` | list | 当前限内行运星 | Step 4 限运 |

### 业务工作流入口与 SOP（从原始文献到软件落地）

**核心区分**：这里的"入口"不是 CLI/API 这种技术接口，而是 **AI 完成一次完整七政四余推命所必须走的业务工作流**。每个工作流是一个系统化作业 SOP，不是单个函数调用。

**原始文献依据**：
- 《星学大成》五层结构：宇宙观→天星系统→时空框架→推演方法→应用判断
- 《果老星宗》工作流：安命安身→定限度→推行限→论星格→断吉凶
- 学术地图 11 步 Schema（dev-notes/07）：历法→星历→宫位→命宫身宫→限运→化曜→神煞→状态→格局→限运推演→综合判读

从这些文献中提炼出 **8 个业务工作流入口**，每个对应一个 SOP：

---

#### 入口 1 · 命主档案管理

**文献依据**：果老星宗"先须生月日时"；星学大成要求完整生辰+地点。铁板神数"考刻定分"的前提是有命主档案。

**SOP**：
1. 录入命主基本信息：姓名、性别、出生公历年月日、出生时间（UT）、经度、纬度、时区
2. 记录出生时间不确定性（如"大约凌晨3点"→时间窗口±1小时）
3. 记录人生重大事件（用于矫正）：结婚、生育、升迁、大病、迁居、父母亡故等，含事件年份
4. 关联排盘记录、矫正历史、大限推演结果
5. 支持更新/删除/查询

**软件支持度**：
| SOP 步骤 | 软件支持 | 状态 |
|---|---|---|
| 录入基本信息 | `db.add_subject()` | ✅ |
| 查询命主 | `db.get_subject()` / `db.list_subjects()` | ✅ |
| 记录时间不确定性 | — | ❌ 无字段 |
| 记录人生事件 | — | ❌ 无表 |
| 更新/删除 | — | ❌ 无函数 |
| 关联矫正历史 | `db.add_rectification()` 可写入，但无查询函数 | ⚠️ 半 |
| 关联大限结果 | `db.add_daxian()` 可写入，但无查询函数 | ⚠️ 半 |

**缺口**：`db.py` 缺少 `update_subject`/`delete_subject`/`add_life_event`/`get_rectification_history`/`list_charts_for_subject`/`list_daxian_for_subject`。需要扩展 `life_event` 表和 subject 的 `time_uncertainty` 字段。

---

#### 入口 2 · 排盘（定盘）

**文献依据**：这是所有推命的基础。果老星宗"安命安身"为第一步。星学大成卷一-六覆盖完整排盘。

**SOP**：
1. 输入：出生公历年月日、出生时间（UT）、经度、纬度
2. 调用 `build_chart(y, mo, d, h, lon, lat)` → 一次返回 22 个顶层字段
3. 验证关键数据：命宫黄经、身宫黄经、昼夜判定、四柱干支
4. [可选] 持久化：`db.add_chart()`
5. [可选] 输出：`render_chart()` 文本 / `export_json()` JSON / `render_svg()` SVG

**软件支持度**：✅ **完整支持**。`build_chart()` 是 AI 论命的标准入口，22 字段一次拿齐。

---

#### 入口 3 · 出生时间矫正（考刻定分）

**文献依据**：类似铁板神数"考刻定分"——用已知人生事件反推精确出生时间。七政四余中，通过行星位置与人生事件的对应关系来校准。

**SOP**（这是一个迭代流程，不是单次调用）：
1. **起点**：用近似出生时间生成初始命盘 `build_chart(y, mo, d, h_approx, lon, lat)`
2. **收集校准事件**：从命主档案中提取可用于校准的人生事件（入口 1 的 life_event）
3. **AI 事件-星象映射**：对每个事件，AI 判断对应哪个星象变化：
   - 婚姻/感情 → 金星/月亮过宫、7宫（妻妾宫）激活
   - 事业突破 → 木星/太阳过宫、10宫（官禄宫）激活
   - 健康危机 → 火星/土星/罗睺冲照、6宫（疾厄宫）/8宫
   - 生育 → 木星/月亮、5宫（男女宫）激活
   - 父母变动 → 太阳/土星、4宫（田宅）/10宫
   - 学业/考试 → 水星/文昌/科甲星激活
4. **反推计算**：对每个校准点，用 `rectify.py` 反推：
   - `rectify --target '{"sun":<目标黄经>}'` → 反推 UT 时间
   - 或 `rectify --target '{"jupiter":<目标黄经>}'` → 用其他行星
5. **一致性检验**：AI 检查多个校准点反推出的出生时间是否一致
   - 若一致 → 确定为矫正结果
   - 若不一致 → 调整事件-星象映射假设，重新迭代
6. **存储矫正历史**：`db.add_rectification()` 记录原始时间、矫正后时间、方法、目标、结果
7. **用矫正后时间重新排盘**：回到入口 2

**软件支持度**：
| SOP 步骤 | 软件支持 | 状态 |
|---|---|---|
| 生成初始命盘 | `build_chart()` | ✅ |
| 收集校准事件 | — | ❌ 无 life_event 表 |
| AI 事件-星象映射 | AI 智能（无代码辅助） | ⚠️ AI 能力 |
| 反推计算（单点） | `rectify.py` / `core.find_date_at_sun_pos()` / `find_date_at_planet_pos()` | ✅ |
| 多点一致性检验 | — | ❌ 无函数 |
| 存储矫正历史 | `db.add_rectification()` | ✅ |
| 查询矫正历史 | — | ❌ 无查询函数 |

**缺口**：`rectify.py` 只做单点反推，缺少多点校准的迭代 SOP 封装。需要：`life_event` 表、`rectify_multi_point()` 函数（接受多个目标，返回一致性评分）、矫正历史查询函数。

---

#### 入口 4 · 格局分析

**文献依据**：星学大成卷十二-十七"星格"；果老星宗"星格"专章。134 条格局规则从 moira_s.prop 提取。

**SOP**：
1. 调用 `build_chart()` → `chart['rules']` 获取匹配的格局
2. AI 逐条解读匹配的格局：
   - 格局名称含义（如"日月并明"=日月同旺）
   - 涉及哪些星曜，这些星曜的庙旺平陷状态（查 `chart['dignities']`）
   - 格局是否完整（有无破格的凶星冲照）
   - 格局优先级（`[level.rank.sub]` 数字越小越重要）
3. AI 分析格局间的交互：
   - 多个吉格叠加 → 加倍吉利
   - 吉格被凶格冲破 → 减分
   - 互斥规则（规则库中有 `exclude` 字段）
4. AI 结合传统典籍解读（星学大成/果老星宗中的断语）

**软件支持度**：
| SOP 步骤 | 软件支持 | 状态 |
|---|---|---|
| 规则求值 | `core.eval_rules()` → 295/295 条 | ✅ |
| 返回匹配格局 | `chart['rules']['matched']` | ✅ |
| 格局优先级 | 规则库含 `[level.rank.sub]` | ✅ |
| 互斥规则 | 规则库含 `exclude` 字段 | ✅ |
| 庙旺状态查询 | `chart['dignities']` | ✅ |
| 格局含义解读 | AI 智能 | ⚠️ AI 能力 |
| 格局交互分析 | AI 智能 | ⚠️ AI 能力 |
| 断语秘诀库 | — | ❌ 未结构化 |

**缺口**：断语秘诀（《星学大成》卷二十-二十二、《耶律秘诀》、《碧玉真经》等）未结构化为可查询的数据库。可作为未来扩展。

---

#### 入口 5 · 洞微大限推演（系统化推运 SOP）

**文献依据**：果老星宗"洞微大限"为核心推运法；星学大成卷十八"限赋"。这不是"算一下当前在哪限"，而是**系统化地推演一生12限的吉凶走势**。

**SOP**（这是系统化作业，不是单次查询）：
1. **计算12限框架**：`chart['daxian']` → 12个限的起止年龄/年数/黄经范围
2. **逐限分析**（对12限中的每一限）：
   a. 该限落在哪个宫位？（限起始黄经 → 地支 → 十二宫）
   b. 该限宫位的宫主是谁？宫主庙旺平陷？（查 `dignities`）
   c. 原盘哪些星曜落入该限宫位？（行星黄经 vs 限黄经范围）
   d. 该限宫位有哪些神煞？（查 `star_signs.table`）
   e. 该限触发了哪些格局？（对限宫位重新求值规则）
   f. AI 判断该限总体吉凶
3. **当前限深入分析**：
   a. `chart['current_daxian']` → 当前所在限/限内年龄/限内度数
   b. `chart['daxian_stars']` → 当前限内有哪些行运星
   c. 当前限的小限/飞限是什么？（`chart['limits']`）
   d. AI 综合判断当前限运势
4. **限内逐年推演**（对当前限内的每一年）：
   a. 调用 `core.compute_now_data(birth_year, age, life_sign_pos)` → 流年四柱/神煞/年星
   b. AI 判断该年与当前限的叠加关系
5. **大限交接期分析**：
   a. 限与限交接的前后2-3年通常是运势转折点
   b. AI 识别交接期并提示注意事项

**软件支持度**：
| SOP 步骤 | 软件支持 | 状态 |
|---|---|---|
| 12限框架 | `chart['daxian']` (12项) | ✅ |
| 当前限 | `chart['current_daxian']` | ✅ |
| 当前限内行运星 | `chart['daxian_stars']` | ✅ |
| 小限/飞限 | `chart['limits']` | ✅ |
| 逐限分析（宫位/宫主/星曜/神煞） | 原料齐备，但需 AI 手动交叉查询 | ⚠️ 无封装 |
| 逐限格局触发分析 | — | ❌ 无"对限宫位求值规则"函数 |
| 限内逐年推演 | `core.compute_now_data()` 可逐年调用 | ✅ 但需循环 |
| 大限交接期识别 | — | ❌ 无函数 |

**缺口**：缺少 `analyze_daxian_limit(chart, limit_index)` 封装函数（对指定限做综合分析：宫位/宫主/星曜/神煞/格局）。缺少 `progress_daxian_years(chart, age_start, age_end)` 封装函数（对年龄区间逐年推演）。

---

#### 入口 6 · 流年推演

**文献依据**：果老星宗"流年"专章；星学大成卷十九。流年推演是"对特定年份做运势分析"，不是"算一下当前年龄"。

**SOP**：
1. **确定目标年份**：命主当前年龄 / 命主想问的特定年份
2. **流年基础计算**：`core.compute_now_data(birth_year, age, life_sign_pos)` → 流年四柱/神煞/年星
3. **流年-原盘叠加分析**：
   a. 流年太岁（年支）与原盘命宫的关系：合/冲/刑/破/害
   b. 流年神煞叠加到原盘神煞上：哪些凶煞被激活？哪些吉煞被加强？
   c. 流年年星（天禄/天暗等）与原盘化曜的关系
4. **流年-大限叠加分析**：
   a. 流年太岁与当前大限宫位的关系
   b. 流年是否激活当前大限的潜在格局
   c. 流年行运星是否经过当前大限宫位
5. **AI 综合判断该年吉凶**

**软件支持度**：
| SOP 步骤 | 软件支持 | 状态 |
|---|---|---|
| 流年基础计算 | `core.compute_now_data()` | ✅ |
| 流年四柱/神煞/年星 | 同上 | ✅ |
| 流年-原盘叠加 | 原料齐备，AI 手动交叉 | ⚠️ 无封装 |
| 流年-大限叠加 | 原料齐备，AI 手动交叉 | ⚠️ 无封装 |
| 多年连续推演 | 需循环调用 `compute_now_data()` | ⚠️ 无封装 |

**缺口**：缺少 `analyze_liunian(chart, age)` 封装函数（对流年做综合分析：太岁关系/神煞叠加/大限叠加）。缺少 `progress_liunian_years(chart, age_start, age_end)` 封装函数。

---

#### 入口 7 · 综合判读

**文献依据**：星学大成卷二十-二十二"断语秘诀"；果老星宗最终断吉凶。这是 AI 智能的核心战场——代码提供原料，AI 做命理判断。

**SOP**（AI 智能层，代码不参与判断）：
1. **汇总全部原料**（来自入口 2-6 的输出）：
   - 原盘：`bodies` / `eight_char` / `star_signs` / `dignities` / `rules`
   - 限运：`daxian` / `current_daxian` / `daxian_stars` / `limits`
   - 流年：`now_data`
2. **应用传统判读原则**（星学大成/果老星宗）：
   a. **身命二主强弱**：命宫主星（宫主）+ 命度主星（度主）的庙旺平陷
   b. **四正宫吉凶**：命宫/田宅/妻妾/官禄四宫的星曜配置
   c. **五行生克**：恩（生我）用（我生）仇（克我）难（我克）的平衡
   d. **神煞叠加**：吉煞多则吉，凶煞多则凶，吉凶交见则辨主次
   e. **格局成破**： matched 格局是否完整，有无破格因素
   f. **大限吉凶**：当前限宫主强弱 + 限内星曜 + 限内格局
   g. **流年吉凶**：太岁关系 + 流年神煞 + 与大限叠加
3. **AI 产出命理判断**：性格/六亲/事业/财运/健康/婚姻/大运走势/流年提示

**软件支持度**：✅ **原料完整**。全部 22 字段就绪，AI 可直接读取分析。此入口是 AI 智能的核心，代码的职责到此为止。

**缺口**：无代码缺口。但 AGENTS.md 应记录判读原则清单（上述 a-g），供 AI session 遵循。**本 SOP 即此清单。**

---

#### 入口 8 · 主数据维护

**文献依据**：命理常量来源于传统典籍（moira_s.prop 从星学大成/果老星宗/协纪辨方书提取）。

**SOP**：
1. **规则库扩展**（`rules_library.json`）：
   - 从《果老星宗》星格章补充新格局
   - 从《星学大成》卷十二-十七补充新格局
   - 每条规则需：编号/名称/优先级/条件表达式/排斥规则/注释
   - 规则语言：`@`黄道 / `%`宿度 / `$`字符串 / `?`布尔 / `&|!`逻辑 / `&func()`函数
2. **常量表扩展**（`constants.json`）：
   - `dignity_states`：补充"殿"状态数据（当前无数据）
   - `lunar_mansions`：角宿起点需根据岁差校准
3. **神煞表扩展**（`shen_sha_complete.json`）：
   - 从《协纪辨方书》补充择吉神煞
   - 从《星学大成》补充天干/地支神煞
4. **验证**：扩展后运行 `core.eval_rules()` 确认零异常

**软件支持度**：
| SOP 步骤 | 软件支持 | 状态 |
|---|---|---|
| 编辑 JSON 文件 | 直接编辑 | ✅ |
| 代码自动加载 | `core.load_*()` 自动读取 | ✅ |
| 规则验证 | `core.eval_rules()` 可验证 | ✅ |
| 扩展文档 | — | ❌ 无扩展指南 |

**缺口**：缺少主数据扩展指南文档（规则语法说明/常量格式说明/神煞格式说明）。

---

### 业务工作流支持度总览

| 入口 | 工作流 | 软件支持度 | 关键缺口 |
|---|---|---|---|
| 1 | 命主档案管理 | ⚠️ 半（缺 CRUD + 事件表） | update/delete/life_event |
| 2 | 排盘（定盘） | ✅ 完整 | — |
| 3 | 出生时间矫正 | ⚠️ 半（单点可用，缺迭代SOP） | 多点校准/一致性检验 |
| 4 | 格局分析 | ✅ 完整（断语库可选扩展） | 断语秘诀库 |
| 5 | 洞微大限推演 | ⚠️ 半（原料齐备，缺封装函数） | analyze_daxian_limit/progress |
| 6 | 流年推演 | ⚠️ 半（原料齐备，缺封装函数） | analyze_liunian/progress |
| 7 | 综合判读 | ✅ 原料完整（AI 智能层） | — |
| 8 | 主数据维护 | ⚠️ 半（可编辑，缺扩展指南） | 扩展文档 |

### 已知缺口（2026-07-16 更新，经代码验证）

**缺口分两类**：函数级缺口（影响工作流封装）和工作流级缺口（影响 AI 可用性）。

#### 函数级缺口（低优先级，不影响核心论命）

| 缺口 | 严重程度 | 说明 |
|---|---|---|
| 三方四正独立函数 | 低 | 规则引擎已隐含处理宫位关系 |
| 相位计算 | 低 | Java 有 `computeAspects()`，规则引擎用黄经差替代 |
| 推运系统（transit/返照/主限/次限/太阳弧） | 中 | Java 有完整推运系统，流年推演已覆盖部分需求 |
| 日月食计算 | 低 | Java 有 `getEclipseState()` |
| 高格林区位 | 低 | 非七政四余核心功能 |
| 恒星/方位角/罗盘 | 低 | 非七政四余核心功能 |
| 飞限半年切换精确化 | 低 | 简化实现可用 |

#### 工作流级缺口（高优先级，影响 AI 系统化使用）

| 缺口 | 影响入口 | 严重程度 | 需要什么 |
|---|---|---|---|
| `db.py` 缺少 update/delete/事件表 | 入口 1 | 高 | `update_subject`/`delete_subject`/`life_event` 表 |
| 矫正缺少多点迭代 SOP 封装 | 入口 3 | 高 | `rectify_multi_point()` + 一致性评分 |
| 矫正历史/大限/星盘查询函数缺失 | 入口 1/3/5 | 中 | `get_rectification_history`/`list_charts`/`list_daxian` |
| 大限逐限分析封装缺失 | 入口 5 | 中 | `analyze_daxian_limit(chart, idx)` |
| 大限逐年推演封装缺失 | 入口 5 | 中 | `progress_daxian_years(chart, age_start, age_end)` |
| 流年综合分析封装缺失 | 入口 6 | 中 | `analyze_liunian(chart, age)` |
| 流年多年推演封装缺失 | 入口 6 | 中 | `progress_liunian_years(chart, age_start, age_end)` |
| 断语秘诀库未结构化 | 入口 4/7 | 中 | 从典籍提取断语为可查询 JSON |
| 主数据扩展指南缺失 | 入口 8 | 低 | 规则语法/常量格式/神煞格式文档 |
| ~~格局引擎忌格完全缺失~~ | ~~入口 4/7~~ | ~~**高**~~ | **已解决(Phase24b)**：新增48条忌格规则，忌格覆盖率从0%→66.7% |
| ~~格局引擎喜格覆盖不足~~ | ~~入口 4/7~~ | ~~**高**~~ | **已解决(Phase24b)**：新增74条喜格规则，喜格覆盖率从23.3%→92.2% |
| ~~命格等级判断模型缺失~~ | ~~入口 4/7~~ | ~~中~~ | **已解决(Phase24b)**：新增`score_rules()`评分模型，三层评分(priority权重+关键格局加权+忌格组合惩罚)，高命格vs低命格总分和喜忌比均正相关 |
| 评分模型差值较小 | 入口 4/7 | ~~中~~ | **已解决(v3)**：数据驱动权重调优后，高低命格总分差14.1/喜忌比差1.49 |
| 31种星格未覆盖 | 入口 4/7 | ~~中~~ | **已解决(v3)**：补充第二批规则后，喜格99.0%/忌格94.2%，仅剩4种需宿度数据 |
| 4种星格未覆盖 | 入口 4/7 | 低 | 1种喜格+3种忌格(土躔奎度/斗木等)需精确宿度数据，当前宿度变量未填充 |

**历史审计文档**（翻译缺口表，已被本节取代）：<ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/04-Java方法审计与翻译缺口表.md" />

## 研究资料索引（dev-notes/）

以下研究性内容已从 AGENTS.md 推出到 `dev-notes/` 目录，按需查阅：

| 文件 | 内容 | 何时查阅 |
|---|---|---|
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/01-星历数据调查结果.md" /> | Swiss Ephemeris 数据位置/覆盖范围/加载机制/路径对齐 | 确认星历数据时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/02-代码耦合分析.md" /> | 重构前摸底：GUI 耦合分层、ChartData 上帝类、Resource 全局状态、CS41.py 现状 | 理解重构难点时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/03-重构决策.md" /> | 重构路径决策（先 spike 再决定）+ SQLite 单文件决策 | 理解为什么选 Python 重写时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/04-Spike验证结果.md" /> | Java spike 验证：swisseph 可脱离 GUI 运行，输出 JSON 行星位置 | 理解 spike 验证过程时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/05-Calculate核心算法研究.md" /> | Calculate.java 9 大算法详解：恒星黄道/宫位/行星/命宫/童限/大限/小限/节气/矫正 | 理解七政四余算法实现时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/06-功能模块完整盘点.md" /> | 全 repo 功能模块盘点：base/27 文件 + Calculate 92 方法 + ChartData 80 方法 + moira/40 Dialog + CS41.py | 确认未研究功能时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/07-七政四余学术地图.md" /> | 七政四余 11 步完整 Schema：历法→星历→宫位→命宫→限运→化曜→神煞→状态→格局→限运→判读 | 理解学科全貌时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/08-repo与学术地图对应分析.md" /> | repo 功能 vs 学术地图 11 步的覆盖度分析 + 15 项未来需求 | 确认功能缺口时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/09-星学大成Schema对照.md" /> | 《星学大成》22KB Schema 的 5 项关键补充：星曜性情/长生十二运/庙旺平陷/神煞/断语秘诀 | 理解星学大成理论体系时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/10-果老星宗与星学大成目录对照.md" /> | 两部典籍的完整卷章目录 + 9 个共享模块 + 8+5 个独有模块 | 理典籍结构时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/11-协纪辨方书目录对照.md" /> | 《钦定协纪辨方书》36 卷目录 + 与七政四余的 10 个交叉点 + 择吉需求 | 理解择吉体系时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-03.md" /> | **A3 审计：十干化曜**。发现庚辛壬癸四干化曜错位（天嗣被误当作独立化曜）。已修复。 | 理解十干化曜数据修复时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-02.md" /> | **A2 审计：四余定义**。发现紫炁错误使用 MEAN_APOG（改为线性运动）、月孛错误使用 OSCU_APOG（改为 MEAN_APOG）。已修复。 | 理解四余计算修复时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/12-四余文献考据资料汇编.md" /> | **四余文献考据资料汇编**：罗睺/计都/紫炁/月孛的历史演变、天文定义、计算方法、典籍出处、学术论文链接、基准点对照。A2 审计期间搜索整理。 | 研究四余相关文献时 |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/20-Layer-A审计SOP.md" /> | **Layer A审计SOP**：5步标准流程 + 考据记录统一模板 + 压缩边界恢复协议 | 审计工作开始前 |

### 原典文本（dev-docs/原典/）

Phase 20 原典收集成果，用于 Layer A 审计和 Phase 24 验证：

| 目录 | 来源 | 内容 |
|---|---|---|
| `dev-docs/原典/星命溯源/` | 维基文库四库全书本 | **果老星宗鼻祖**，5卷完整：卷1通玄遗书/五星论/四时论/玉衡经，卷2果橙问答，卷3元妙经解(郑希诚注)，卷4观星要诀，卷5观星心传口诀补遗 |
| `dev-docs/原典/郑氏星案/` | tianyugong.com | **郑氏星案40例完整文本**，每例含四柱干支+性别+命格等级+所喜星格+所忌星格+命理分析。用于Phase 24端到端验证 |
| `dev-docs/原典/协纪辨方书-kanripo/` | kanripo/GitHub KR3g0051 | **协纪辨方书完整36卷**，卷1-6历法核心(本原/公规/年表/月表)，卷23-36义例(神煞体系) |
| `dev-docs/原典/果老星宗-IA/` | Internet Archive扫描本 | 1593年大文堂本10卷djvu.txt，OCR质量较差(古籍)，含完整卷次结构 |
| `dev-docs/原典/星平会海/` | suanzhun.net | **星平会海完整10卷**，卷1-10含星曜歌诀/入门看法/十二宫论断/赋文/合婚/八字基础/格局等，附 schema.json 结构索引 |

### 典籍目录文件（项目根目录）

| 文件 | 内容 |
|---|---|
| <ref_file file="~/MOIRA_chinese_astrology-main/星学典籍目录对照.md" /> | 《图解果老星宗》与《图解星学大成》完整目录对照（241 行） |
| <ref_file file="~/MOIRA_chinese_astrology-main/协纪辨方书目录对照.md" /> | 《钦定协纪辨方书》完整目录与内容对照（241 行） |
| `20250927T110252Z__《星学大成》理论体系Schema.md` | 《星学大成》理论体系 Schema（22KB，AI 生成） |

## 建设计划索引（dev-docs/）

| 文件 | 内容 |
|---|---|
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/00-七政四余推命系统建设计划.md" /> | **终态目标 + 7 个 Phase + 60+ 细化 TODO + 优先级与依赖关系** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/01-Phase1排盘引擎补全完成报告.md" /> | **Phase 1 完成报告：农历/二十八宿/升落/身宫/长生十二运/逆顺迟疾 + 验证结果** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/02-Phase2命理参数表提取完成报告.md" /> | **Phase 2 完成报告：庙旺平陷/纳音五行/十干化曜/天干星曜 + 验证结果** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/03-Phase3格局规则引擎完成报告.md" /> | **Phase 3 完成报告：134条格局规则提取 + Python求值器 + 76/134条可求值** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/04-Java方法审计与翻译缺口表.md" /> | Java 方法审计 + 翻译缺口表（历史文档，缺口已被 AGENTS.md "已知缺口"节取代） |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/05-七政四余推命系统建设完成报告.md" /> | **Phase 1-12 最终完成报告：全功能实现 + 20/20回归测试 + 精度验证** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/06-业务工作流SOP与后续建设规划.md" /> | **8 个业务工作流入口 SOP + Phase 13-19 后续建设规划 + Phase 20-21 两层审计框架 + 细化 TODO List** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/07-文献考据总体规划.md" /> | **四层考据方法论：文献广度普查 + 逐句原文考据 + 历史命例验证 + 历史星空重建。Phase 22-25** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/09-Phase24郑氏星案端到端验证报告.md" /> | **Phase 24 完成报告：郑氏星案40例端到端验证 40/40 全部匹配 + calc_four_poles 4个bug修复（节气分年月/年柱基准/时柱hour_index/早子时）** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/10-Phase24b命格判断验证报告.md" /> | **Phase 24b v3完成报告：规则库扩充134→283条(喜格99.0%/忌格94.2%) + score_rules()v3数据驱动评分模型(高低命格总分差14.1/喜忌比差1.49)** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/13-七政四余形式化体系.md" /> | **七政四余形式化体系：算子(躔/照/会/守/冲/合) + 集合(星/宿/宫) + 命题(X→Y) + 与 rules_library.json 的对应关系** |

## Layer A 考据审计日志

Phase 20 Layer A 审计逐项对照原文核对数据表和算法。已完成的审计项：

| 审计项 | 日期 | 结果 | commit | 考据记录 |
|---|---|---|---|---|
| **A3 十干化曜** | 2026-07-16 | ❌→✅ 发现庚辛壬癸四干化曜错位（天嗣被误当作独立化曜）。已修复。 | `ae1d865` | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-03.md" /> |
| **A2 四余定义** | 2026-07-16 | ❌→✅ 发现两个严重错误：(1) 紫炁错误使用 MEAN_APOG，改为28年线性运动；(2) 月孛错误使用 OSCU_APOG，改为 MEAN_APOG。另添加 true_as_north 开关。 | `3da1f20` | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-02.md" /> |
|| **A27-A29 拦驾经/倒限详论/一寸金总诀** | 2026-07-08 | ✅ PASS（搜索+对照+决策完成；不直接实现代码，作为AI判读参考） | 待本次commit | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-27-29.md" /> |
|| **A30 星曜入宫/躔宿/照宫/交会吉凶表** | 2026-07-08 | ✅ PASS（搜索+对照+决策完成；部分覆盖，不完整提取三辰通载表） | 待本次commit | <ref_file file="~/MOIRA_chinese_astrology-main/dev-notes/AUDIT-LAYER-A-30.md" /> |

### Phase 21 天文验证 + Phase 24 端到端验证（2026-07-08）

| 验证项 | 结果 | 说明 |
|---|---|---|
| **B7 节气UT** | ✅ PASS | 调整UTC→CST 8小时偏移后，误差<分钟级 |
| **B8 农历转换** | ✅ PASS | 11/11测试用例全部通过 |
| **B9 朔日** | ✅ PASS | 2024年14个朔日全部正确 |
| **B4-B5 ASC/MC** | ✅ PASS | 修复calc_houses恒星黄道bug后，与Java MOIRA差异<0.0001° |
| **B19 四柱干支** | ✅ PASS | 修复calc_four_poles 4个bug后，郑氏星案40/40全部匹配 |
| **Phase 24 端到端** | ✅ PASS | 郑氏星案40例四柱→公历→排盘，40/40全部匹配（100%） |

**calc_four_poles 修复的4个bug**（Phase 24验证期间发现）：
1. **节气分年月模式**：新增`use_solar_terms=True`，用回归黄道太阳位置判断节气月（节气基于回归黄道，不是恒星黄道，ayanamsa≈23.7°）
2. **年柱基准**：用1984=甲子作为基准（原代码用公元4年，错误）
3. **时柱hour_index**：`((adj_hour+1)//2)%12`（原缺少%12，23时算成12而非0）
4. **早子时规则**：23时后不跨日（果老星宗用早子时，23-0时属于当日子时）

**审计教训**：A3 和 A2 都暴露了 Phase 1-4 翻译的方法理缺陷——"只对比输出，不审计计算机制"。A2 尤为严重：紫炁在 Java 中是自定义线性轨道（`sign_computation_type=1`），翻译时直接套用了 `swe.MEAN_APOG`，导致所有涉及紫炁的排盘结果错误。Phase 24 进一步证明：四柱计算需要区分节气分年月（果老星宗/传统八字）和农历分年月（琴堂派），节气必须用回归黄道。

## 工作原则

- 代码改动服务于上述排盘 / 矫正 / 分析目标，不是为写代码而写代码。
- 涉及命理算法、星历计算、矫正逻辑时，先理解七政四余理论与现有实现，再动手。
- 数值计算交给代码，命理判断交给 AI，二者不混用。
- 改动前先定位相关模块（见上方"关键功能定位"），避免盲改。
- 编译/运行前先确认依赖（SWT 平台版本、Python 库、星历数据路径）。
- **项目代码知识落盘规则**：项目的代码知识（结构、机制、定位、踩坑、调查结论等）被发现后，应及时记录到 dev-notes 或本文件，不只活在当前 session 的上下文里。
- **研究性内容落盘规则**：详细的算法研究、代码耦合分析、典籍目录对照等长内容，放到 `dev-notes/` 目录，AGENTS.md 只保留索引指针。
- **Java 翻译纪律**：从 Java 源码翻译到 Python 时，不能只对比输出。必须逐行审计 Java 的计算机制——特别是 `sign_computation_type`（自定义轨道 vs Swiss Ephemeris）、`true_as_north`（新旧法开关）等配置项。A2 审计证明：只对比输出会漏掉计算机制层面的错误（紫炁被错误当作 MEAN_APOG，实际是 28 年线性运动）。
- **Java 不一定是 ground truth**：Java MOIRA 的数据选择有历史依据但不唯一。对于有争议的定义（如紫炁周期、罗睺升/降交点），必须保留双模式，默认与 Java 一致，留待 Phase 24（历史命例验证）做最终判定。

### 形式化思维规则（AI 必须遵循）

**这是 AI 思考本项目工作的元规则。** 不是具体操作步骤，而是思维方式本身。

**核心命题**：七政四余（以及所有术数体系）的本质是一个**形式系统**——它有集合（星/宿/宫）、算子（躔/照/会）、命题（X→Y）、推理规则（逻辑组合）。我们的一切工作，都是在构建、验证、完备这个形式系统。这不是一个封闭系统——我们不知道所有的算子、集合和命题，而是通过阅读古籍、验证命例、跨体系比较来不断扩展它的边界。

**为什么必须形式化**：

1. **知识整理的需要**：古籍中的命理规则散落在歌诀、赋文、注释中，格式不统一、结构隐含、依赖上下文。形式化把"隐性知识"变成"显性结构"——每条规则有明确的算子、输入、输出、判定，不再依赖"悟"。
2. **可计算性的需要**：AI 要做命理判读，前提是能"算"。形式化之后，"躔(木,角)→天贵"就变成了一个可查表、可推理、可验证的计算步骤，而不是一段需要"理解"的文字。
3. **多体系研究的需要**：七政四余、八字、紫微斗数、铁板神数——这些体系的底层逻辑不同，但都可以用"集合+算子+命题"的框架来描述。形式化之后，跨体系的比较、融合、验证才有基础。
4. **大数据研究的需要**：当规则库达到数千条、命例达到数万条时，只有形式化的结构才能支撑批量验证、统计分析、模式发现。自然语言的规则库做不到这一点。

**形式化的工作方式**：

- **每条规则必须可定位**：用 XPath 式的 ID（如 `卷一/星曜躔度歌/轸/土-天柱`）精确定位到每条规则，不接受"大概在某个文件的某个位置"。
- **每个算子必须有形式定义**：躔、照、会、守、冲、合等算子，必须定义输入类型、输出类型、语义。不接受"躔就是缠上去"这种解释。
- **命题必须可求值**：给定一个星盘实例，每条命题必须能判定为真/假/不确定。不可求值的命题是未完成的形式化。
- **规则库必须可审计**：新增规则必须检查与已有规则的一致性（是否矛盾？是否重复？是否归并？）。规则库不是堆数量，而是构建一个自洽的系统。
- **形式化是一个开放过程**：我们不是在"定义一套封闭的形式系统"，而是在"持续地发现和记录"。古籍中的算子、集合、命题，有些是我们已经识别的（躔/照/会），有些还在文本中等待发现（如"拱"/"夹"/"刑"/"穿"/"害"等）。我们不预设"形式系统长什么样"，而是让文本告诉我们它长什么样。每次深入阅读一部典籍，都可能发现新的算子、新的集合元素、新的命题结构。形式化的边界是随着研究推进而不断扩展的，不是预先划定的。

**形式化与现有代码的关系**：

- `rules_library.json` 已经是形式化的产物（134条格局规则，每条有条件表达式和求值器）
- `core.eval_rules()` 已经是形式化的实现（295条规则可求值）
- `schema.json` 是形式化的索引（XPath 式定位）
- 本文档（`13-七政四余形式化体系.md`）是形式化的语法定义

**AI 执行此规则的方式**：

当处理任何命理规则时，AI 必须问自己：
1. 这条规则的**算子**是什么？（躔/照/会/守/冲/合/...）
2. 这条规则的**输入**是什么？（哪颗星、哪个宿/宫）
3. 这条规则的**输出**是什么？（什么名称、什么判定）
4. 这条规则是否**可求值**？（给定星盘实例，能否判定真/假）
5. 这条规则与已有规则库是否**一致**？

如果任何一个问题答不上来，说明形式化尚未完成，需要继续工作。

### 形式化的灵魂：解释框架

**形式系统本身只是语法，没有灵魂。** 一个只有算子、命题、规则库的形式系统，就像一本只有语法规则没有语义的字典——它能告诉你"这个句子合不合语法"，但不能告诉你"这个句子是什么意思"。形式系统的灵魂来自**解释框架**：它把形式表达映射到经验现象上，让"躔(木,角)→天贵"不只是一个可求值的命题，而是一个**有意义的判断**。

**四种可能的解释立场**：

| 立场 | 说什么 | 优点 | 缺点 |
|---|---|---|---|
| **因果论**（物理主义） | 星曜有磁场/引力/辐射，直接影响人体 | 最符合现代科学直觉 | 无实证；无法解释为什么火星距地球最近时仍是"凶星" |
| **相关论**（统计主义） | 星曜位置与人生事件统计相关，但非因果 | 能做大数据验证 | 只能描述"是什么"，不能解释"为什么" |
| **符号论**（语义主义） | 星曜是符号，表意不致因；天人同构，同一模式在不同层面显现 | 能解释"为什么"；与传统典籍一致 | 难以证伪 |
| **全息论**（同构主义） | 宇宙与人生是全息对应的——星象是"宇宙-人生剧本"的索引，周易卦象是另一个索引，同一套底层模式在不同维度上展开 | 能解释跨体系的一致性；与"天人感应"传统完全吻合 | 目前缺乏形式化定义 |

**本项目的立场：全息论为主，因果论为辅。**

- **全息论（主）**：星曜是"宇宙-人生剧本"的全息索引。即便我们找不到物理层面的"场"或"作用力"，星象与人生之间仍然存在同构关系——宇宙的模式在人生中重现，人生是宇宙的微缩。这与周易占卜的卦象有相似性：卦象是另一套索引系统，指向同一套底层模式。躔(木,角)→天贵，意思是"当木星落在角宿时，这个宇宙配置与'贵'这个人生模式全息对应"。传统典籍说"天人感应"、"天人合一"，正是这个意思。周易说"仰则观象于天，俯则观法于地"，也是这个意思。
- **符号论**：作为全息论的补充——当全息对应关系暂时无法形式化时，先用符号-语义的方式描述。
- **因果论（辅）**：物理层面的关联可以作为辅助解释。比如月球引力对潮汐的影响——但这是物理层面的因果，不是命理层面的因果。

**为什么这个立场重要**：

1. **避免伪科学陷阱**：如果坚持因果论，就必须证明"木星磁场如何导致人富贵"——这在目前是不可能的。全息论绕开了这个陷阱。
2. **与传统典籍一致**：《果老星宗》说"天地虽大，万物虽多，要之一理"——强调的是"理"（pattern/meaning），不是"力"（force/energy）。
3. **解释跨体系一致性**：七政四余、八字、紫微斗数、周易占卜——这些体系的底层模式相同，只是索引方式不同。全息论能解释为什么不同体系的判读常常指向相似的结论。
4. **保留扩展空间**：未来如果发现了物理层面的因果机制，全息论不排斥它——它只是说，在没有因果证据时，先用全息同构解释，不强行声称因果。
5. **形式化不受阻塞**：不管采用哪种解释立场，形式化工作（提取规则、构建命题、验证一致性）都可以正常进行。解释框架是形式化的"灵魂"，但不是形式化的"前提"。

**形式系统的三层结构**：

```
┌─────────────────────────────────────────┐
│  Layer 3: 解释框架（灵魂）                │
│  "躔(木,角)→天贵" 意味着什么？             │
│  全息论 / 符号论 / 因果论 / 相关论          │
├─────────────────────────────────────────┤
│  Layer 2: 形式系统（骨架）                │
│  集合 + 算子 + 命题 + 推理规则             │
│  "躔(木,角)→天贵" 是一个可求值的命题        │
├─────────────────────────────────────────┤
│  Layer 1: 经验现象（血肉）                │
│  古籍中的命理规则、历史命例、人生经验         │
│  "木缠角宿号天贵，诗礼传家居职位"           │
└─────────────────────────────────────────┘
```

形式化的工作是**构建 Layer 2**（骨架）。解释框架是**赋予 Layer 3**（灵魂）。但 Layer 1（经验现象）是根基——如果形式系统不能描述经验现象，或者解释框架不能回应经验现象，那么整个结构就是空转。

**AI 执行此规则的方式**：

当处理任何命理规则时，除了问"算子/输入/输出/可求值/一致性"（形式化五问），还要问：
6. 这条规则的**解释框架**是什么？（全息/符号/因果/相关）
7. 如果是全息论/符号论：这个符号的**语义**是什么？（"天贵"意味着什么？）
8. 如果是因果论：这个因果的**机制**是什么？（目前能证明吗？）
9. 这条规则与周易/八字/紫微斗数等其他体系是否有**同构关系**？（全息论视角）

如果第 7 题答不上来，说明解释框架尚未完成。如果第 8 题答不上来但声称是因果论，说明解释框架有误。

### 定性与定量：铁板神数的时代性

本项目的终态目标之一，是将**定性的七政四余**与**定量的铁板神数**进行并行分析——基于铁板神数 180 年全时刻的出生星盘和推运盘，做定性+定量的双重判读。

**但必须警惕：铁板神数的"定量"不是绝对结论的定量，而是"能量单位"的定量。**

铁板神数给出的数序（如"3子"、"财帛三万"）是对人生能量的**度量**，不是对人生事件的**预言**。同一个"3子"的能量，在不同时代有不同的实现方式：

| 时代背景 | "3子"的实际含义 |
|---|---|
| 英雄妈妈年代（1950-60s） | 生育不受限制，"3子"可能对应 6-7 个孩子 |
| 计划生育年代（1980-2010s） | 政策限制，"3子"可能只有 1 个孩子 |
| 持票供应的大锅饭时代 | "财帛三万"——再富也富不到哪去 |
| 市场经济时代 | "财帛三万"——能量单位可以充分兑现 |

**这意味着**：铁板神数的定量刻画有两层含义：
1. **能量刻度**（跨时代稳定）：星盘配置决定了"子嗣能量=3"这个刻度值
2. **时代解码**（因时而变）：这个刻度值在具体时代背景下如何兑现，取决于社会结构、政策环境、经济条件

**本项目的工作方向**：
- **七政四余**提供定性判读：星曜配置的整体格局、喜忌、方向
- **铁板神数**提供定量刻度：能量的度量值
- **时代背景**作为解码器：把能量刻度翻译为具体的人生事件
- 三者结合，才是完整的判读

**为什么这件事重要**：如果把铁板神数的数序当成绝对预言，就会闹笑话——在计划生育时代说人"3子"，结果只有 1 个孩子，就说铁板不准。其实铁板的"3"是能量单位，不是绝对数量。搞清楚这一点，才能正确使用铁板神数。

**泛化警示：能量再大，也怕结扎。**

这句话有两层含义：
1. **具体含义**：铁板神数说"3子"，但计划生育政策让你只能生1个——星象的能量刻度是真实的，但兑现路径可以被人间制度截断。
2. **泛化含义**：无论星盘配置多么强大、格局多么好、能量加持多么充分，**事在人为**仍然是最终的决定因素。星象给出的是"可能性空间"，不是"必然性结论"。一个人可以选择顺着星象走，也可以选择逆着星象走，甚至可以选择完全无视星象。命理系统描述的是"如果...那么..."的条件关系，不是"因为...所以..."的因果必然。

这是本项目解释框架的核心前提之一：**星象不是宿命，而是条件；不是枷锁，而是地图。** 地图告诉你前面有路，但走不走、怎么走，是你自己的事。铁板神数的能量刻度再精确，也敌不过一个人的自主选择。

### 系统演化：经验包的迭代吸收

我们以形式化框架来系统化吸收现有星学文献，这个过程不是简单的"文本整理成数据库"，而是**系统的自我迭代**。

**迭代结构**：

```
S-0 → [T-0] → S-1 → [T-1] → S-2 → [T-2] → S-3 → ...
       ↑           ↑           ↑
     经验包0      经验包1      经验包2
```

- **S-0**：初始系统（七政四余的基本算子和集合）
- **T-0**：第一批经验包（如《星平会海》卷一的星曜躔度歌 308 条规则）
- **S-1**：吸收 T-0 后的新系统（算子更精确，集合更完备，规则库更丰富）
- **T-1**：第二批经验包（如《星学大成》的格局规则、《果老星宗》的限运理论）
- **S-2**：吸收 T-1 后的更深系统
- ……

**关键原则：不是吸收，是深化**。

不应该直接把 T-1 塞进 S-1（那是数据库录入），而是在 S-1 的视角下审视 T-1，问：
1. T-1 中有哪些 S-1 无法描述的规则？→ 这意味着 S-1 需要新的算子或集合
2. T-1 中有哪些规则与 S-1 矛盾？→ 这意味着 S-1 需要修正
3. T-1 中有哪些规则能统一 S-1 中零散的规则？→ 这意味着 S-1 需要更高层的抽象

**深化出来什么？——定性+定量的认知**。

随着 T-0、T-1、T-2……被持续吸收，系统持续发现和定义新的概念。但从一开始就清楚：我们要构建的是**定性+定量**的认知。

- **定性**：星曜配置的格局、喜忌、方向（七政四余的强项）
- **定量**：能量的度量值（铁板神数的强项）

定量化的难点在于：很多概念（如"福气"、"贵气"）没有现成的度量单位。可能需要：
- 多参数化：一个"福气"由多个星曜参数共同决定
- 代数方程：星曜间的几何关系（光学关系）越紧密，能量越强
- 能量单位：建立自己的度量体系，类似铁板神数的数序

**根本问题**：我们对星学到底能理解和把握到多么深刻的程度？这个问题没有预设答案——答案在 T-0、T-1、T-2……被持续吸收的过程中逐渐浮现。每一次吸收经验包，都可能发现我们之前想不到的概念、关系、规律。

这是本项目的研究态度：**不预设终点，但追求深度。** 形式化框架是脚手架，经验包是砖石，二者交替推进，系统才会长大。

## TODO 管理（JSON 化 + 脚本化）

**禁止用 grep 查 TODO 状态。** TODO 的唯一真理源是 `dev-docs/todos.json`，用 `todo.py` 脚本管理。

### 文件

| 文件 | 用途 |
|---|---|
| `dev-docs/todos.json` | TODO 数据库（唯一真理源，115 个 TODO） |
| `todo.py` | 管理脚本：查询/更新/统计/添加 |
| `dev-docs/generate_todos.py` | 初始化脚本：从 dev-docs/06 和 07 的 Markdown 表格生成 todos.json（只需运行一次） |

### 常用命令

```bash
# 查询
python3 todo.py list                          # 列出所有 TODO
python3 todo.py list --phase 13               # 按 Phase 过滤
python3 todo.py list --status pending         # 按状态过滤
python3 todo.py list --search-preset 先搜索     # 按搜索预置过滤
python3 todo.py show 13.1                     # 查看单个 TODO

# 更新状态（开始做某个 TODO 时）
python3 todo.py update 13.1 --status in_progress
python3 todo.py update 20.4 --status completed --result "PASS" --commit abc123

# 统计
python3 todo.py stats                         # 总览
python3 todo.py stats --by-phase              # 按 Phase 统计
python3 todo.py stats --by-search-preset      # 按搜索预置统计

# 找下一个可做的事
python3 todo.py next                          # pending + 依赖满足的 TODO

# 搜索预置
python3 todo.py search-preset                 # 列出所有需要搜索的 TODO
python3 todo.py search-preset --only 先搜索     # 只看"先搜索"级

# 添加新 TODO
python3 todo.py add --phase 99 --id 99.1 --title "新任务" --search-preset 先搜索
```

### 搜索预置三级

每个 TODO 都有 `search_preset` 字段，决定动手前是否需要搜索：

| 级别 | 含义 | 数量 |
|---|---|---|
| 🔍 **先搜索** | 必须先搜索外部信息源（原文/参考数据/API文档）才能动手。不搜索 = 必然幻觉或用错数据 | 57 项 |
| 🔄 **边做边搜索** | 主体是工程任务，过程中有特定细节需要核对 | 8 项 |
| ⚙️ **不需要** | 纯工程任务，不需要搜索 | 47 项 |

**执行 🔍 先搜索 的 TODO 前，必须完成：web_search → webfetch → 记录考据 → 确认充分 → 才能动手。**

详见 <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/07-文献考据总体规划.md" /> §9。

### 执行纪律：同步更新 TODO + keep git clean

执行任何计划的过程中，必须遵守以下纪律：

1. **同步更新 TODO List**：
   - 开始做某个 TODO 时：`python3 todo.py update <id> --status in_progress`
   - 完成时：`python3 todo.py update <id> --status completed --result "..." --commit <hash>`
   - 被阻塞时：`python3 todo.py update <id> --status blocked --note "阻塞原因"`
   - **禁止只做不更新**——TODO 状态必须实时反映真实进度

2. **keep git clean**：
   - 完成一个逻辑工作单元后，立即 commit
   - commit 后确认 `git status` 回到 clean 状态
   - 禁止积压多个未提交的改动
   - 禁止在 dirty 状态下开始下一个 TODO

## 术语备忘

- **"紫气" = 紫炁**：四余之一（紫炁 qì，木之余）。用户输入法打不出"炁"字，日常用"紫气"指代。代码中统一用"炁"（如 `mean_apog_ziqi`、`shen_sha_complete.json` 中的 `qi_stars`），AI 读到用户说"紫气"时应理解为"紫炁"。同理"气"在七政四余语境下通常也指"炁"。

---

## TODO List 工作协议（正式项目纪律）

**目的**：确保所有后续工作（尤其是进入实战后的持续演进）不只活在聊天记录或个人记忆中，而是**必须先落实到一份集中式、可读的 TODO List**，并形成可传承的工作意识。

**核心文件**：
- `dev-docs/26-后续TODO-List.md`：高层次、面向人的**主 TODO List**（活文档）。
- `dev-docs/todos.json` + `todo.py`：颗粒度执行层（已有的 JSON 化管理）。

**协议内容**：

1. **落盘纪律**（强制）
   - 任何新发现的 TODO（包括实战中踩到的坑、用户反馈、新需求），必须在 24 小时内补充到 `dev-docs/26-后续TODO-List.md`。
   - 重大或跨阶段的 TODO，必须同步更新 AGENTS.md 中的“已知缺口”或本协议相关段落。
   - 禁止只在聊天中讨论而不落盘。

2. **更新时机**（必须执行）
   - 每完成一个大阶段（Phase 或一批实战命例）后，立即 review 并更新主 TODO List。
   - 进入新阶段（例如从审计进入实战）前，必须把该阶段所有准备工作写入主 TODO List。
   - 每季度进行一次全面审查（优先级调整、依赖清理、已完成归档）。

3. **主列表与执行层的关系**
   - `dev-docs/26-后续TODO-List.md` 记录“为什么要做”“影响哪个入口”“优先级与依赖”。
   - `todos.json` 记录“具体怎么做”“当前状态”“搜索预置”。
   - 所有待执行的 TODO 最终都要通过 `todo.py` 管理执行，但高层次可见性必须保留在主列表。

4. **实战特别要求**
   - 在开始任何真实命例前，必须确认 `dev-docs/26-后续TODO-List.md` 中的“实战前必须完成的准备工作”已全部完成或有明确计划。
   - 实战过程中发现的新缺口，必须立即补充到主列表，并标记“实战中发现”。

5. **审查与传承**
   - 本协议本身是项目级工作纪律，任何新加入的开发者或 AI session 都必须先阅读本节。
   - 维护主 TODO List 的意识，是本项目“从给人看 → 给 AI 看”之后，进一步“给未来自己看”的核心文化。

**最后更新**：2026-07-08（本协议正式确立）。
