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

`schema.json` 从星平会海卷一提取，含：
- **躔度歌** 307 条：28宿 × 11星曜 = 308条（轸宿缺木星条目），XPath 式 ID 如 `卷一/星曜躔度歌/轸/土-天柱`
- **交会歌** 59 条：9个星×星section，59条组合规则（木会火/木会土/.../孛会计）
- **照宫歌** 96 条：12个宫位 × 11星曜 = 132种组合中的96条有文本的规则
- **守宫歌** 3 条：宫主入命规则（身命主/闲极主/官禄主）
- 总计 **465 条**七政四余规则，XPath 式 ID 如 `卷一/交会歌/木会火`
- 提取脚本：`extract_rules_v3.py`（交会歌/照宫歌/守宫歌）+ `extract_rules.py`（躔度歌）

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
| `dev-docs/原典/星平会海/` | suanzhun.net + ctext.org | **星平会海完整10卷**，163个raw文件/1.3MB。卷1躔度歌307条+交会歌59条+照宫歌96条+守宫歌3条已提取。含兰台妙选完整版(52KB)。附 schema.json + extract_rules_v3/v4.py |
| `dev-docs/原典/星学大成/` | GitHub youngzs/xuanxue | **星学大成卷一卷二**，16个文件/67KB。卷一含星曜图例/十干变曜/星曜喜怒/干支吉煞；卷二含财禄神煞/驿马/纳音/卦气/三元/格局；另含杂诗36首 |

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
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/14-古籍研究SOP脚本化设计.md" /> | **古籍研究SOP脚本化设计：强制检查点 + 审计跟踪 + 质量门控 + 结果验证。渐进式实现，先覆盖四层考据** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/15-Master-Worker架构设计方案.md" /> | **Master-Worker架构设计：主控脚本 + Worker启动脚本 + 任务队列 + 检查点机制 + 停止门。基于MiMo模型20万token上下文限制，推荐宿级粒度** |
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/46-Devin-CLI非线性运行时改造.md" /> | **Devin CLI 非线性运行时改造：在不破坏 opencode 工作面的前提下，新增 Devin 项目配置、hooks、skills、runtime capsule、provider adapter 和 stop gate** |

### Master-Worker架构与完整性审计（2026-07-09 新增）

**架构目标**：用Master Agent控制sub-agents在tmux中执行古籍研究任务，确保内容完整性。

**核心组件**：

| 组件 | 文件 | 功能 |
|---|---|---|
| **Master Agent** | `master.py` | 主控脚本：分配任务/记录检查点/完成任务/验证完整性 |
| **Worker Agent** | `worker.sh` | 启动脚本：在tmux中启动 opencode 或 Devin CLI 执行任务 |
| **任务队列** | `tasks.json` | 任务状态管理：queued/leased/completed |
| **Path树** | `build_path_tree.py` | 构建《星平会海》完整path树（精确到每一行） |
| **完整性验证** | `verify_integrity.py` | 全量验证/行级验证/审计日志 |

**Master命令**：
```bash
# 查看系统状态
python3 master.py status

# 分配任务
python3 master.py assign --task-id 20.4 --worker-id W1

# 记录检查点
python3 master.py checkpoint --worker-id W1 --task-id 20.4 --phase <PHASE> --cursor-line <LINE> --evidence-count <COUNT> --note '<NOTE>'

# 完成任务
python3 master.py complete --task-id 20.4 --result '<RESULT>'

# 报告行级覆盖
python3 master.py report-line-coverage --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌 --start-line 1 --end-line 130 --content-hash <SHA256>

# 验证section完整性
python3 master.py verify-section --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 全量验证
python3 master.py verify-complete --document 星平会海

# 停止门检查
python3 master.py may-stop
```

**Worker启动**：
```bash
# 基本启动
./worker.sh --worker-id W1 --task-id 20.4

# 带行级参数启动
./worker.sh --worker-id W1 --task-id 20.4 --start-line 1 --end-line 130 --section-id 卷一/星曜躔度歌

# 使用 Devin CLI
./worker.sh --provider devin --worker-id W1 --task-id 20.4
```

**完整性审计结果**（2026-07-09 测试）：
- Path树：10卷 / 246节 / 79子节 / 307规则
- 卷覆盖：10/10 (100%)
- 节覆盖：246/246 (100%)
- 规则覆盖：307/307 (100%)
- 行级报告：1-130 (130行) 已验证

**审计日志位置**：`runtime/audit_logs/`

### Devin CLI 非线性运行时支撑（2026-07-10 新增）

本项目未来可以由 Devin CLI 支撑，但不能把这个迁移理解成简单替换命令行工具。MOIRA 的运行时是非线性的：系统会从 `S-n` 吸收经验包，发现新维度，提升成熟度，改变可计算性，再反过来生成新的任务和审计要求。

因此，Devin 进入本项目时必须先读取 runtime capsule，而不是只依赖上下文记忆。项目已新增 `.devin/config.json`、`.devin/hooks.v1.json`、`.devin/skills/`、`ai-runtime/protocol/`、`tools/moira_runtime.py` 和 `tools/agent_launcher.py`。Devin 的 `SessionStart` 与 `UserPromptSubmit` 会注入当前任务状态、Worker 状态、非线性维度覆盖、协议锚点和下一步动作；`Stop` hook 会在仍有 queued、leased、busy 或协议漂移时阻止过早停止。

默认 provider 仍是 opencode，以保护当前工作面。未来启动 Devin Worker 或 Auditor 时，使用 `--provider devin`，或设置 `MOIRA_AGENT_PROVIDER=devin`。无论 provider 是谁，Worker 仍必须输出维度、成熟度和可计算性，Auditor 仍必须把执行完成和语义通过分开。

### Devin Worker yolo 模式 + git worktree + 限流恢复（2026-07-10 新增）

**核心约束：最多 2 个 Devin Worker 实例**（算上 Master 共 3 个 Devin 进程）。超过会触发 API 限流，导致全部 Worker 白费工作。

**禁止用 subagent 派 Worker**。subagent 共享 Master 的 rate limit，10 个 subagent 同时跑会瞬间触发限流。Worker 必须用独立的 Devin CLI 进程，在独立 tmux 会话中运行。

**Worker 启动方式**：

```bash
# 方式一：用 launch_workers.sh 自动从 tasks.json 取任务并启动
./tools/launch_workers.sh                    # 启动 2 个 Worker
./tools/launch_workers.sh --max-workers 1    # 只启动 1 个

# 方式二：手动启动单个 Worker
./tools/worker_v2.sh --worker-id W1 --task-id auto.40 \
  --section-id 卷一/星曜照宫歌/兄弟宫 --start-line 302 --end-line 303
```

**worker_v2.sh 做了什么**：

1. **git worktree 隔离**：每个 Worker 在 `.worktrees/worker-<WID>/` 独立工作目录中运行，避免文件冲突。worktree 基于 main 分支创建，分支名 `worker/<WID>/<TID>`。
2. **Devin yolo 模式**：`devin --permission-mode dangerous --prompt-file <prompt> --export <transcript>`。dangerous 模式自动批准所有操作，无需人工确认。
3. **tmux 会话**：Worker 在 `tmux new-session -d -s worker-<WID>` 中运行，可 `tmux attach -t worker-<WID>` 查看。
4. **watchdog 监控**：`tools/watchdog.sh` 在后台监控 Worker tmux 会话状态。

**限流检测和自动恢复**：

watchdog 脚本（`tools/watchdog.sh`）每 30 秒检查一次 Worker tmux 会话：

| 情况 | watchdog 行为 |
|---|---|
| tmux 会话正常运行 | 继续监控 |
| tmux 会话退出 + 任务已完成 | 标记完成，watchdog 退出 |
| tmux 会话退出 + 检测到限流 | 等待 cooldown（默认 1800 秒 = 30 分钟）→ 重启 Worker 并发"继续" |
| tmux 会话退出 + 非限流错误 | re-queue 任务，watchdog 退出 |
| 超过最大重试次数（默认 5 次） | re-queue 任务，watchdog 退出 |

**限流检测方式**：检查 transcript 文件（`runtime/transcripts/*.devin.atif.json`）和 tmux pane 输出中是否包含 `rate limit` / `Reached overall message rate limit` / `limit will reset` 等关键词。

**"继续"机制**：限流恢复后，watchdog 在 worktree 目录中重新启动 devin，并发送"继续之前被限流中断的工作"提示词。Devin 会检查已有工作成果（AUDIT 文件、checkpoint），继续完成未完成的部分。

**检测间隔合理性**：

- **poll_interval = 30 秒**：tmux 会话状态检查间隔。30 秒足够及时检测到 Worker 退出，又不会过于频繁。
- **cooldown = 1800 秒（30 分钟）**：限流恢复等待时间。API 限流通常提示"28-30 分钟后重置"，30 分钟留足余量。
- **max_retries = 5 次**：最多重试 5 次限流恢复。超过则 re-queue，避免无限循环。

**关键文件**：

| 文件 | 功能 |
|---|---|
| `tools/launch_workers.sh` | 启动器：从 tasks.json 取任务，启动最多 2 个 Worker |
| `tools/worker_v2.sh` | Worker 启动脚本 v2：git worktree + Devin yolo + tmux + watchdog |
| `tools/watchdog.sh` | 监控脚本：限流检测 + cooldown + 自动重启 + "继续" |
| `.worktrees/worker-<WID>/` | Worker 独立工作目录（git worktree） |
| `runtime/prompts/` | Worker 提示词文件 |
| `runtime/transcripts/` | Devin 会话导出文件 |
| `runtime/watchdog_logs/` | watchdog 日志 |

### 系统脚本架构与调用关系（2026-07-10 补全）

**四个主控脚本的分工**：

| 脚本 | 定位 | 角色 |
|---|---|---|
| `master.py` | **手动控制接口** | 分配任务/记录检查点/完成任务/验证完整性/启动Auditor。AI（Master Agent）通过 CLI 命令直接调用 |
| `master_controller.py` | **自动化循环控制器** | 最高层。循环调用 factory.py + self_iteration.py，实现无人值守运行 |
| `factory.py` | **Worker 生命周期管理** | 从 schema.json 自动发现任务、动态创建 Worker、分配任务、检查完成 |
| `self_iteration.py` | **自我迭代引擎** | 从吸收结果中发现新任务、动态调整吸收策略、构建知识图谱 |

**调用关系图**：

```
AI Master Agent（如 Devin CLI）
    │
    │ 直接调用 master.py CLI 命令
    ↓
master.py（手动控制）
    │ 读写 tasks.json, runtime/checkpoints/, runtime/audit_logs/
    │ subprocess → auditor.py, tools/agent_launcher.py, tmux
    │
    │ 或者由自动化控制器接管
    ↓
master_controller.py（自动化循环）
    │ 读写 runtime/master_state.json, tasks.json
    │ subprocess → factory.py --action run/status
    │ subprocess → self_iteration.py --action iterate/status
    ↓
factory.py（Worker 工厂）
    │ 读写 tasks.json, runtime/factory_state.json
    │ 读 dev-docs/原典/星平会海/schema.json → 自动发现 auto.* 任务
    │ subprocess → worker.sh（旧）或 tools/worker_v2.sh（新）
    ↓
self_iteration.py（自我迭代）
    │ 读写 runtime/iteration_state.json
    │ 读写 runtime/absorption_strategy.json
    │ 读写 runtime/knowledge_graph.json（尚未创建）
    │ 读写 tasks.json → 生成 explore.*/random.* 任务
```

**非线性状态文件**：

| 文件 | 写入者 | 读取者 | 内容 |
|---|---|---|---|
| `runtime/iteration_state.json` | `self_iteration.py` | `self_iteration.py`, `tools/moira_runtime.py` | 迭代次数、发现列表、生成的新任务 |
| `runtime/absorption_strategy.json` | `self_iteration.py` | `self_iteration.py`, `tools/moira_runtime.py` | 当前阶段(exploration)、6维度覆盖率、非线性权重 |
| `runtime/knowledge_graph.json` | `self_iteration.py` | `self_iteration.py`, `tools/moira_runtime.py` | 算子/集合/命题/关系/概念/发现（尚未创建，系统未进入知识积累阶段） |
| `runtime/master_state.json` | `master_controller.py` | `master_controller.py` | 主控状态、周期数、发现数 |
| `runtime/factory_state.json` | `factory.py` | `factory.py` | 工厂状态 |

**moira_runtime.py 如何使用这些文件**：`tools/moira_runtime.py` 的 `nonlinear_state()` 函数读取 `iteration_state.json`、`absorption_strategy.json`、`knowledge_graph.json`，生成 runtime capsule 中的 `nonlinear_phase`、`iteration_count`、`dimension_coverage`、`lowest_coverage_dimensions` 等字段。这就是 SessionStart/UserPromptSubmit hook 注入的"当前系统状态"的来源。

### 双账本架构：tasks.json vs dev-docs/todos.json（2026-07-10 补全）

**两个文件是平行的，没有映射关系**：

| 账本 | 文件 | 管理工具 | ID 格式 | 用途 |
|---|---|---|---|---|
| **执行账本** | `tasks.json` | `master.py`, `factory.py` | `auto.N`, `random.N`, `explore.N` | Worker 实际执行的任务队列（文献考据、探索等） |
| **规划账本** | `dev-docs/todos.json` | `todo.py` | `phase.N`（如 20.4, 13.1） | 项目建设的长期规划（Phase 1-25） |

**auto.* 任务的来源**：`factory.py` 的 `discover_tasks_from_schema()` 从 `dev-docs/原典/星平会海/schema.json` 自动生成 `auto.N` 考据任务，每个 subsection 生成一个。

**runtime-manifest.json 的定义**：`ai-runtime/protocol/runtime-manifest.json` 中明确标注了 `tasks.json` = execution_tasks，`dev-docs/todos.json` = todo_truth。

### Worker 执行流程与 AUDIT 文件（2026-07-10 补全）

**Worker 提示词**（`worker_prompt.py` 生成，约200行）：
- **核心思维力提示词**（~150行）：形式化五问、定量化意识、开放性意识、全息意识、时代性意识、PathListGate 硬门
- **动态任务信息**（~50行）：任务ID、标题、Section ID、行范围、执行步骤、汇报要求
- **不直接读取数据文件**：提示词要求 Worker 自己确认 `full_path_tree.json` 存在，而不是预加载内容

**Worker 产出物**：`dev-docs/AUDIT-auto.{N}-{section名}.md`，包含：
- PathListGate 验证（hash 比对）
- 原始文本内容（来源、文件、行号、歌诀、注释）
- 形式化五问（每条规则的算子/输入/输出/可求值性/一致性）
- 维度/成熟度/可计算性汇报（SOP 三要素）
- 跨文献对照、定量化/开放性/全息/时代性分析
- 审计判定（PASS + 理由）

**已知缺口**：AUDIT-auto.*.md 文件目前由 Worker 直接产出，**缺少 Auditor 的二次审查**。审计系统脚本已实现但未自动运行。

### 审计系统脚本架构（2026-07-10 补全）

**四个审计脚本的分工**：

| 脚本 | 定位 | 读写文件 | CLI 命令 |
|---|---|---|---|
| `auditor.py` | **Auditor Agent 主控** | 读 checkpoints/，写 auditor_prompts/ | `audit-section`, `audit-task`, `generate-report` |
| `audit.py` | **审计记录管理** | 读写 dev-notes/AUDIT-*.json，读 todos.json | `create`, `validate`, `report`, `list` |
| `sop_audit.py` | **SOP 汇报审计** | 读 checkpoints/，写 audit_logs/ | `audit-section`, `audit-task`, `report` |
| `quality_gate.py` | **质量门控** | 读 dev-notes/AUDIT-*.json, todos.json | `check`, `check-all`, `report` |

**审计流程**：

```
Worker 完成任务 → 汇报 SOP（维度/成熟度/可计算性）→ 保存到 checkpoint
    ↓
Master 调用 sop_audit.py 审计 SOP 汇报 → 保存到 runtime/audit_logs/
    ↓
Master 调用 master.py launch-auditor 启动 Auditor Agent
    ↓
auditor.py 生成审计提示词 → runtime/auditor_prompts/
    ↓
Auditor Agent（tmux 中）进行语义审计 → 保存到 runtime/audit_logs/
    ↓
Master 读取审计结果 → PASS 则任务完成 / FAIL 则 Worker 重新执行
```

**`master.py launch-auditor` 已实现**（第 685-798 行），支持 `--provider opencode/devin`，在 tmux 中启动 Auditor Agent。

**审计结果存储位置**：
- `runtime/audit_logs/` — 自动化审计日志（JSON）
- `runtime/auditor_prompts/` — 审计提示词（Markdown）
- `runtime/checkpoints/` — Worker 检查点（JSON）
- `dev-notes/AUDIT-*.json` — 结构化审计记录（由 audit.py 生成）
- `dev-docs/AUDIT-*.md` — Worker 手写的详细审计报告（Markdown）

**当前状态**：审计系统脚本已实现，runtime/audit_logs/ 中有 2026-07-09 的运行记录，但目前没有 Auditor 在运行。97 个 auto.* 任务的 AUDIT 文件缺少 Auditor 二次审查。

### 全 path 列表前置门（PathListGate · 2026-07-10 新增）

任何一本原典在正文处理前，必须先完成全 path 列表。这里的“处理”包括摘要、形式化、规则抽取、考据、审计和系统吸收。没有全 path 列表时，Master 不得派 Worker 读正文，Worker 不得自行开始正文处理，Auditor 不得给正文处理结果 PASS。

全 path 列表至少要覆盖：源文件、卷、篇、章、节、子节、规则、行号范围、稳定 path ID、原文定位和可复核 hash。对当前《星平会海》，已有入口是 `dev-docs/原典/星平会海/schema.json` 和 `dev-docs/原典/星平会海/full_path_tree.json`，构建脚本是 `build_path_tree.py`。后续处理其他书时，也必须先在该书目录下建立 `full_path_tree.json` 和 path 审计记录。

PathListGate 的判定口径是 remainder=0。也就是说，Master 要先证明这本书的 path list 覆盖完整、没有断裂、没有重复、能回到原文行号和内容 hash，再进入 Worker 分包。Worker 只能处理 Master 分配的 path ID 和行号范围；发现 path list 缺失、错位或无法定位时，必须停止正文处理并回报 Master 修 path。

### 优雅停止机制（2026-07-09 新增）

**停止命令**：

| 命令 | 功能 | 参数 |
|---|---|---|
| `shutdown` | 优雅停止系统 | `--force` 强制停止 |
| `cleanup` | 清理临时文件和会话 | 无 |
| `status-report` | 生成状态报告 | 无 |

**优雅停止流程**：

```
用户请求停止
    ↓
执行停止门检查 (may-stop)
    ↓
├── STOP_ALLOWED → 执行清理流程
└── CONTINUE_REQUIRED → 提示未完成任务
    ↓
清理流程
    ├── 终止所有Worker tmux会话
    ├── 保存检查点状态
    ├── 更新任务状态
    ├── 生成停止报告
    └── 清理临时文件
    ↓
系统停止完成
```

**停止报告内容**：

```json
{
  "shutdown_time": "2026-07-09T10:30:00",
  "shutdown_type": "graceful",
  "tasks_summary": {
    "total": 3,
    "completed": 2,
    "in_progress": 1,
    "queued": 0
  },
  "workers_summary": {
    "W1": {"status": "idle", "last_task": "20.4"},
    "W2": {"status": "idle", "last_task": "30.11"}
  },
  "checkpoints_saved": 5,
  "audit_logs_generated": 3
}
```

**资源清理清单**：

| 资源类型 | 清理方式 | 命令 |
|---|---|---|
| tmux会话 | 终止所有Worker会话 | `tmux kill-session -t worker-W1` |
| 检查点文件 | 保留在`runtime/checkpoints/` | 不清理（用于恢复） |
| 任务状态 | 更新为最终状态 | `tasks.json` |
| 审计日志 | 保留在`runtime/audit_logs/` | 不清理（用于审计） |
| 临时文件 | 清理`runtime/`下的临时文件 | `rm -rf runtime/temp/*` |

**使用示例**：

```bash
# 优雅停止（等待所有任务完成）
python3 master.py shutdown

# 强制停止（立即停止所有Worker）
python3 master.py shutdown --force

# 清理临时文件和会话
python3 master.py cleanup

# 生成状态报告
python3 master.py status-report
```

### 自动化系统设计（2026-07-09 新增）

**核心问题**：如何确保系统以非线性模式吸收目标文集，而不是沦为线性模式？

**解决方案**：三个核心脚本协同工作，实现完全自动化的非线性吸收。

#### 1. 工厂脚本 (factory.py)

**功能**：管理Worker/Auditor的生命周期

**核心特性**：
- **动态Worker创建**：根据任务量自动创建Worker
- **自动任务分配**：将排队任务分配给空闲Worker
- **任务发现**：从schema.json和文本文件自动发现任务
- **完成检查**：定期检查Worker完成情况

**非线性策略**：
- **随机打乱卷顺序**：不按卷1→卷10的顺序处理
- **随机选择起始行**：在每个卷内随机选择处理区间
- **多区间处理**：每个卷处理3-5个随机区间，而不是整体处理

**使用方式**：
```bash
# 自动发现任务
python3 factory.py --action discover

# 创建Worker
python3 factory.py --action spawn-worker

# 运行工厂
python3 factory.py --action run --max-cycles 100
```

#### 2. 自我迭代引擎 (self_iteration.py)

**功能**：实现系统的自我迭代机制

**核心特性**：
- **知识图谱构建**：记录已吸收的内容和发现的新概念
- **吸收策略调整**：动态调整吸收方式（探索→深化→整合）
- **新任务生成**：从吸收过程中发现新任务
- **跨体系关联**：发现七政四余与其他体系的关联

**非线性策略**：
- **探索新维度**：优先探索覆盖率低的维度
- **深化未完成内容**：研究未完成的算子和未知概念
- **随机探索**：随机选择新内容进行探索
- **跨体系关联**：发现不同体系之间的关联

**使用方式**：
```bash
# 运行迭代
python3 self_iteration.py --action iterate

# 查看状态
python3 self_iteration.py --action status

# 发现新任务
python3 self_iteration.py --action discover --count 5
```

#### 3. 主控脚本 (master_controller.py)

**功能**：实现系统的完全自动化运行

**核心特性**：
- **周期运行**：定期运行迭代和工厂
- **优雅停止**：支持SIGINT/SIGTERM信号处理
- **状态监控**：实时监控系统状态
- **统计更新**：更新系统统计信息

**使用方式**：
```bash
# 运行主控
python3 master_controller.py --action run --max-cycles 100

# 查看状态
python3 master_controller.py --action status

# 优雅停止
python3 master_controller.py --action shutdown
```

### 非线性吸收策略

**核心思想**：不按线性顺序处理，而是根据多维度优先级和随机性动态选择处理内容。

**策略实现**：

1. **维度优先级**：
   - 算子维度（优先级1）
   - 集合维度（优先级2）
   - 命题维度（优先级3）
   - 状态维度（优先级4）
   - 时间维度（优先级5）
   - 体系维度（优先级6）

2. **吸收阶段**：
   - **探索阶段**：优先发现新维度和新概念
   - **深化阶段**：深化已发现但未完成的内容
   - **整合阶段**：整合各维度内容，构建完整体系

3. **非线性权重**：
   - **随机性**（0.3）：引入随机因素，避免线性处理
   - **优先级**（0.4）：根据维度优先级选择内容
   - **覆盖率**（0.3）：优先选择覆盖率低的维度

**自检机制**：

每次迭代后，系统必须自检：
1. **是否发现了新维度？**（新算子/新集合/新命题）
2. **各维度覆盖率是否提升？**（不是简单的数量增加）
3. **是否构建了新的可计算模型？**（形式/定量/推演）
4. **是否发现了跨体系关联？**（七政四余与八字/紫微/周易）
5. **是否发现了新问题？**（开放性，不预设终点）

### 使用流程

**1. 启动系统**：
```bash
# 方式1：使用主控脚本（推荐）
python3 master_controller.py --action run --max-cycles 100

# 方式2：手动启动各组件
python3 factory.py --action run --max-cycles 100 &
python3 self_iteration.py --action iterate
```

**2. 监控系统**：
```bash
# 查看主控状态
python3 master_controller.py --action status

# 查看工厂状态
python3 factory.py --action status

# 查看迭代状态
python3 self_iteration.py --action status
```

**3. 停止系统**：
```bash
# 优雅停止
python3 master_controller.py --action shutdown

# 或使用Ctrl+C
```

### SOP汇报审计（2026-07-09 新增）

**审计目标**：确保Worker按照SOP要求汇报了维度/成熟度/可计算性三要素。

**SOP汇报要求**：

Worker在检查点中必须包含`sop_report`字段：

```json
{
  "dimensions": ["算子维度", "集合维度", "命题维度", "状态维度", "时间维度", "体系维度"],
  "maturity": {
    "coverage": "已提升",
    "consistency": "已验证",
    "evaluability": "已实现",
    "explanatory": "待建设",
    "quantitative": "待建设",
    "cross_system": "待建设",
    "verifiability": "已验证"
  },
  "computability": {
    "formal": "已实现",
    "quantitative": "待建设",
    "deductive": "待建设"
  }
}
```

**审计命令**：

```bash
# 审计单个section的SOP汇报
python3 master.py sop-audit --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 审计整个任务的SOP汇报
python3 master.py sop-audit --worker-id W1 --task-id 20.4
```

**审计维度**：

| 维度类型 | 说明 | 例子 |
|---|---|---|
| 算子维度 | 新发现的算子 | 躔/照/会/守/冲/合/拱/夹/刑 |
| 集合维度 | 新发现的集合 | Star/Mansion/Palace/Dignity |
| 命题维度 | 新发现的命题类型 | 躔度命题/照宫命题/交会命题 |
| 状态维度 | 新发现的状态 | 吉凶/强弱/旺衰/多少 |
| 时间维度 | 新发现的时间切片 | 原盘/大限/流年/小限 |
| 体系维度 | 新发现的体系 | 七政四余/八字/紫微/周易 |

**审计成熟度指标**：

| 指标 | 说明 |
|---|---|
| 覆盖率 | 系统能描述的现象范围 |
| 一致性 | 规则之间是否矛盾 |
| 可求值性 | 规则能否判定真假 |
| 解释力 | 能否说"为什么" |
| 定量化 | 能否给出数值结果 |
| 跨体系 | 能否与其他体系对接 |
| 可验证性 | 能否用命例验证 |

**审计可计算性层次**：

| 层次 | 问题 |
|---|---|
| 形式可计算 | 给定输入，能否算法化地得到输出？ |
| 定量可计算 | 能否给出数值结果？ |
| 推演可计算 | 能否从已知推出未知？ |

**审计结果示例**：

```json
{
  "status": "incomplete",
  "worker_id": "W1",
  "task_id": "20.4",
  "section_id": "卷一/星曜躔度歌",
  "dimension_audit": {
    "reported": false,
    "count": 0,
    "types": [],
    "missing": ["operator", "set", "proposition", "state", "time", "system"]
  },
  "maturity_audit": {
    "reported": false,
    "metrics": {},
    "missing": ["coverage", "consistency", "evaluability", "explanatory", "quantitative", "cross_system", "verifiability"]
  },
  "computability_audit": {
    "reported": false,
    "levels": {},
    "missing": ["formal", "quantitative", "deductive"]
  },
  "all_reported": false
}
```

### Auditor Agent（语义审计）

**架构目标**：实现职责分离，Master负责调度，Auditor负责语义审计。

**核心组件**：

| 组件 | 文件 | 功能 |
|---|---|---|
| **Auditor Agent** | `auditor.py` | 语义审计脚本：生成审计提示词/启动审计 |
| **审计提示词** | `runtime/auditor_prompts/` | 审计任务的详细提示词 |
| **审计结果** | `runtime/audit_logs/` | 审计结果和报告 |

**Auditor命令**：

```bash
# 审计单个section
python3 auditor.py audit-section --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 审计整个任务
python3 auditor.py audit-task --worker-id W1 --task-id 20.4

# 生成审计报告
python3 auditor.py generate-report
```

**Master启动Auditor**：

```bash
# 启动Auditor Agent进行语义审计
python3 master.py launch-auditor --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌
```

**语义审计标准**：

| 审计维度 | 审计标准 | 评分标准 |
|---|---|---|
| **维度审计** | 维度类型是否正确分类？每个维度是否有具体例子？ | 0-10分 |
| **成熟度审计** | 每个指标是否有具体说明？指标之间是否有逻辑关系？ | 0-10分 |
| **可计算性审计** | 每个层次是否有具体说明？是否有可执行的算法？ | 0-10分 |

**审计流程**：

```
Worker完成任务
    ↓
Worker汇报SOP（维度/成熟度/可计算性）
    ↓
Master生成审计提示词
    ↓
Master启动Auditor Agent
    ↓
Auditor Agent进行语义审计
    ↓
Auditor生成审计结果
    ↓
Master读取审计结果
    ↓
审计通过 → 任务完成
审计不通过 → Worker重新执行
```

**使用示例**：

```bash
# 1. Worker完成任务并汇报SOP
python3 master.py checkpoint --worker-id W1 --task-id 20.4 --phase "考据完成" --cursor-line 130 --evidence-count 10 --note "已完成角宿11条规则的考据"

# 2. Master启动Auditor进行语义审计
python3 master.py launch-auditor --worker-id W1 --task-id 20.4 --section-id 卷一/星曜躔度歌

# 3. 查看审计结果
tmux attach -t auditor-W1-20.4

# 4. 审计通过后，完成任务
python3 master.py complete --task-id 20.4 --result "PASS"
```

### Worker提示词设计（思维力内化）

**核心问题**：如何确保Worker真正具备了AGENTS.md中的思维力要求？

**解决方案**：将思维力要求内化到Worker提示词中，而不仅仅是告诉Worker执行步骤。

**提示词生成器**：`worker_prompt.py`

```bash
# 生成Worker提示词
python3 worker_prompt.py --task-id 20.4 --task-title "审计A4：天干神煞" --section-id 卷一/星曜躔度歌/角 --start-line 1 --end-line 130
```

**思维力内化要求**：

| 思维力 | 内化方式 | 质量标准 |
|---|---|---|
| **形式化思维** | 每遇到命理规则，自动进行形式化五问 | 每条规则必须有明确的算子/输入/输出，必须可求值，必须与已有规则一致 |
| **定量化意识** | 每遇到程度描述，自动思考量化可能性 | 每个程度描述必须思考量化可能性，能量化必须给出公式，不能能量化必须说明原因 |
| **开放性意识** | 每遇到新概念，自动记录为"待发现" | 每个新概念必须记录为"待发现"，每个新算子/新工具必须保持敏感 |
| **全息意识** | 每遇到跨体系描述，自动思考同构关系 | 每个跨体系描述必须思考同构关系，每个同构关系必须记录并验证 |
| **时代性意识** | 每遇到具体事件，自动思考时代背景 | 每个具体事件结论必须思考时代背景，每个能量单位必须思考兑现方式 |

**汇报要求**：

Worker汇报SOP时，不仅仅是字段填充，而是**思维过程的外化**：

```json
{
  "dimensions": [
    {
      "type": "operator",
      "found": "拱",
      "input": "两颗星",
      "output": "拱格",
      "semantic": "两颗星形成特定角度关系"
    }
  ],
  "maturity": {
    "coverage": "从只能描述躔/照/会，到能描述躔/照/会/拱",
    "consistency": "验证了拱与躔/照/会不矛盾",
    "evaluability": "拱格现在可以判定真假"
  },
  "computability": {
    "formal": "给定两颗星的黄经，可以算法化判定是否形成拱格",
    "quantitative": "拱的紧密程度可以用角度差量化",
    "deductive": "从原盘可以推演出大限/流年是否激活拱格"
  }
}
```

**使用流程**：

```bash
# 1. 启动Worker（使用新的提示词）
./worker.sh --worker-id W1 --task-id 20.4 --start-line 1 --end-line 130 --section-id 卷一/星曜躔度歌/角

# 2. Worker执行任务时会自动进行思维力内化
#    - 形式化思维：每遇到命理规则，自动进行形式化五问
#    - 定量化意识：每遇到程度描述，自动思考量化可能性
#    - 开放性意识：每遇到新概念，自动记录为"待发现"
#    - 全息意识：每遇到跨体系描述，自动思考同构关系
#    - 时代性意识：每遇到具体事件，自动思考时代背景

# 3. Worker汇报SOP时会外化思维过程
#    - 不是简单列出"算子维度"，而是具体说明发现了什么新算子
#    - 不是简单说"已提升"，而是具体说明提升了什么
#    - 不是简单说"已实现"，而是具体说明实现了什么
```

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
- `schema.json` 是形式化的索引（XPath 式定位），含465条七政四余规则（躔度歌307+交会歌59+照宫歌96+守宫歌3）
- 本文档（`13-七政四余形式化体系.md`）是形式化的语法定义

**AI 执行此规则的方式**：

当处理任何命理规则时，AI 必须问自己：
1. 这条规则的**算子**是什么？（躔/照/会/守/冲/合/...）
2. 这条规则的**输入**是什么？（哪颗星、哪个宿/宫）
3. 这条规则的**输出**是什么？（什么名称、什么判定）
4. 这条规则是否**可求值**？（给定星盘实例，能否判定真/假）
5. 这条规则与已有规则库是否**一致**？

如果任何一个问题答不上来，说明形式化尚未完成，需要继续工作。

**关于数学工具的选择**：当需要将定性规则转化为定量表达时，同时持有多种数学工具（向量点积/平行四边形法则/RGB混色/频率谐波/多维空间），不预设哪一种"最好"。具体问题用具体工具，在行进过程中对比考量，最终可能各有适用场景。

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

**可能用到的数学工具**（不限于此）：

| 工具 | 命理应用 | 说明 |
|---|---|---|
| **向量点积** | 能量在特定方向的投影 | 星曜可视为方向向量，点积衡量其在命格方向上的分量 |
| **平行四边形法则** | 能量向量的合成 | 两颗星曜同时作用时，用牛顿的向量合成法获得合力的大小和方向 |
| **RGB 混色模型** | 能量的混合效果 | 如同三原色混合产生万千色彩，不同星曜能量混合产生复合效应（木火通明、金白水清等） |
| **频率/谐波** | 周期性共振 | 行星周期之间的谐波关系可能产生能量共振或相消 |
| **多维空间** | 多参数联合建模 | 当参数超过3个时，需要在高维空间中定义能量的度量和距离 |

这些数学工具不是强行套用，而是从命理问题本身出发：当我们说"木火通明"时，"通明"的强度如何度量？当我们说"众星拱北"时，"拱"的紧密程度如何量化？数学工具是回答这些问题的手段。

**数学工具的选择也是开放的**。我们不是在众多工具中"选择一个"，而是**同时持有多个工具**，在行进过程中不断对比考量。甚至最终都不是非此即彼的，而是**各有适用的场景**：向量点积适合度量方向性能量，RGB 混色适合描述能量混合的质变，频率谐波适合分析周期性共振。具体问题用具体工具，不预设哪一种"最好"。

**根本问题**：我们对星学到底能理解和把握到多么深刻的程度？这个问题没有预设答案——答案在 T-0、T-1、T-2……被持续吸收的过程中逐渐浮现。每一次吸收经验包，都可能发现我们之前想不到的概念、关系、规律。

这是本项目的研究态度：**不预设终点，但追求深度。** 形式化框架是脚手架，经验包是砖石，二者交替推进，系统才会长大。

### 工作协议：系统自我成长的 SOP

每一次扫描古籍、吸收经验包、推演计算，都不是孤立的任务，而是系统自我成长的一个节律。以下是必须同时开启的意识层面。

**进入任何工作单元前，必须先确认**：

1. **当前系统状态**：我现在处于 S-几？当前系统有哪些算子、集合、命题、数学工具？
2. **经验包边界**：我要吸收的这一段文本，属于哪个算子类型？是否涉及新算子？
3. **解释框架**：这段文本背后的立场是全息论、符号论、还是因果论？它如何映射到我的三层结构？

**在吸收过程中，必须同时开启五重意识**：

| 意识 | 触发条件 | 做什么 |
|---|---|---|
| **形式化意识** | 遇到任何命理规则 | 识别算子/输入/输出，判断是否可求值，检查与已有规则库的一致性 |
| **定量化意识** | 遇到"强弱""多少""轻重"等程度描述 | 思考：这个程度能否用数学工具表达？用向量点积？平行四边形？RGB混色？ |
| **开放性意识** | 遇到现有算子/工具无法描述的规则 | 不强行套用现有框架，记录为"待发现"，保持对新算子/新工具的敏感 |
| **全息意识** | 遇到跨体系的相似描述 | 追问：这个模式在八字/紫微/周易中有没有同构？全息对应关系是什么？ |
| **时代性意识** | 遇到涉及具体人生事件的结论 | 追问：这个结论的"能量单位"在不同时代背景下如何兑现？事在人为的边界在哪里？ |

**完成一个工作单元后，必须做三件事**：

1. **系统更新**：这次吸收让系统从 S-n 演进到 S-n+1 了吗？如果是，更新形式化文档（`13-七政四余形式化体系.md`）和 AGENTS.md。
2. **一致性验证**：新吸收的内容与已有规则库是否一致？用 `core.eval_rules()` 验证。
3. **向下传递**：这次发现的新算子/新集合/新工具，是否会影响后续工作？更新 TODO List。

**这不是线性过程**。系统在不断演进，新的内容会参与到对后续将要吸收的内容的计算和推演中。S-2 的视角与 S-0 不同，对同一个经验包的理解深度也不同。这意味着：**之前看不懂的文本，在系统成长后可能突然看懂了**——这是正常的，也是预期的。

**完成每个 path 叶子节点后，必须汇报三个问题**：

1. **我们新得到了什么系统的新维度？**（新算子？新集合？新命题类型？新状态维度？新时间维度？新体系维度？）
2. **在不同的维度上，我们获得了哪些让系统更成熟的内容？**（覆盖率提升？一致性提升？可求值性提升？解释力提升？定量化提升？跨体系提升？可验证性提升？）
3. **这些新的内容，在未来具备什么样的可计算性？**（形式可计算？定量可计算？推演可计算？还是暂时不可计算？）

**三个元概念的定义**（AI 必须逐条对照执行）：

**维度：系统描述现象的轴线。**

每发现一个新算子、新集合、新命题类型，就增加了一个维度。维度越多，系统的描述力越强。维度的细分类型：

| 维度类型 | 例子 | 说明 |
|---|---|---|
| **算子维度** | 躔/照/会/守/冲/合 | 每个算子是一条独立的描述轴线 |
| **集合维度** | Star/Mansion/Palace/Dignity/Element/Name | 每个集合是一个可被描述的对象类别 |
| **命题维度** | 躔度命题/照宫命题/交会命题/组合命题 | 不同的命题结构描述不同层面的关系 |
| **状态维度** | 吉凶/强弱/旺衰/多少 | 命题输出的丰富程度 |
| **时间维度** | 原盘/大限/流年/小限 | 同一个系统在不同时间切片上的展开 |
| **体系维度** | 七政四余/八字/紫微/周易 | 不同体系对同一现象的不同描述 |

新维度的发现方式：遇到一个现有算子无法描述的关系（如"拱"/"夹"/"刑"）→ 新算子维度；遇到一个现有集合无法容纳的对象（如新的神煞类型）→ 新集合维度。

**成熟度：系统在多个维度上同时发展的程度。**

不是"规则数量"，而是系统的整体完备性。成熟度的细分指标：

| 成熟度指标 | 低成熟度 | 高成熟度 |
|---|---|---|
| **覆盖率** | 只能描述少数星曜配置 | 能描述绝大多数星曜配置 |
| **一致性** | 规则之间有矛盾 | 规则之间自洽 |
| **可求值性** | 很多规则无法判定真假 | 绝大多数规则可求值 |
| **解释力** | 只能说"是什么" | 能说"为什么"（有解释框架） |
| **定量化** | 只有定性判断 | 有定量度量 |
| **跨体系** | 只在一个体系内工作 | 能与其他体系对接 |
| **可验证性** | 无法用命例验证 | 能用历史命例端到端验证 |

成熟度的提升方式：不是线性地"加规则"，而是多维度同时推进。发现新算子 → 算子维度提升；用数学工具量化"福气" → 定量化维度提升；用郑氏星案验证规则 → 可验证性维度提升。

**可计算性：系统从"能描述"到"能算"的跃迁。**

三个层次：

| 层次 | 问题 | 例子 |
|---|---|---|
| **形式可计算** | 给定输入，能否算法化地得到输出？ | 给定星盘，能否算出所有匹配的格局？（已有：`eval_rules()`） |
| **定量可计算** | 能否给出数值结果？ | 能否算出"贵气"的强度值？（待建：能量度量模型） |
| **推演可计算** | 能否从已知推出未知？ | 给定原盘，能否推演出大限/流年的运势变化？（部分已有：`compute_now_data()`） |

可计算性的意义：验证（可计算的规则可以被批量验证）；发现（可计算的系统可以发现人类难以发现的模式）；融合（可计算的系统可以与其他可计算系统对接）。

**三者的关系：正反馈循环**。

```
维度 ←─── 成熟度 ←─── 可计算性
 │         │           │
 └─────────┴───────────┘
      相互促进
```

- 更多维度 → 系统能描述更多现象 → 成熟度提升
- 更高成熟度 → 更多规则可求值 → 可计算性提升
- 更强可计算性 → 能验证更多规则 → 发现新维度

**AI 执行此汇报的方式**：

每完成一个 path 叶子节点，AI 必须输出一份结构化汇报，逐条回答：
1. 本次发现了哪些新维度？（逐条列出维度类型和具体内容）
2. 本次在哪些成熟度指标上有提升？（逐条列出指标和提升程度）
3. 本次发现的内容中，哪些是形式可计算的？哪些是定量可计算的？哪些是推演可计算的？哪些暂时不可计算？

禁止笼统回答"提升了系统能力"——必须具体到维度类型、成熟度指标、可计算性层次。

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
