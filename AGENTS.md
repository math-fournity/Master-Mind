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
| `qizheng/` | **Python 接口层（主产物）** | 七政四余排盘/矫正/分析工具集 |
| `qizheng/core.py` | 核心计算库 | 封装 swisseph + 命理常量 + 11 个七政四余算法函数 |
| `qizheng/constants.json` | 命理常量 | 从 `moira_s.prop` 提取的 limit_seq/child_seq/fly_seq/zodiac 等 |
| `qizheng/chart.py` | 排盘小工具 | 输入生辰 → 星盘 JSON（10 天体 + 12 宫 + 命宫 + 童限） |
| `qizheng/daxian.py` | 大限小工具 | 输入生辰+年龄 → 大限/小限/飞限 JSON |
| `qizheng/rectify.py` | 矫正小工具 | 输入目标黄经 → 反推时间 JSON |
| `qizheng/db.py` | SQLite 数据库 | 命主/星盘/矫正/大限 4 表，单文件 `qizheng.db` |
| `qizheng/README.md` | 模块文档 | 环境准备/用法/算法来源/TODO |
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

### 在 Python 接口层中（实际使用入口）

- **排盘**：`qizheng/chart.py`（`python3 -m qizheng.chart`）
- **大限/小限/飞限**：`qizheng/daxian.py`（`python3 -m qizheng.daxian`）
- **时间矫正**：`qizheng/rectify.py`（`python3 -m qizheng.rectify`）
- **数据库读写**：`qizheng/db.py`（`from qizheng import db`）
- **核心算法库**：`qizheng/core.py`（所有算法函数，可 import 复用）

## 编译与运行环境

- **Java**：本机 `/opt/homebrew/opt/openjdk`（OpenJDK 25）。MOIRA 原为 Java 早期版本编写，编译时需注意 SWT 依赖与 module 兼容性。swisseph 源文件为 Latin-1 编码，编译需 `-encoding ISO-8859-1`。
- **Python**：本机 `python3`（3.14）。`CS41.py` 依赖 `ephem`、`scipy`、`pandas`、`numpy`，运行前需确认依赖已装。
- **Python venv**：`.venv/`（项目内虚拟环境），含 `pyswisseph 2.10.3.2`。Homebrew Python 不让直接装包，故用 venv。运行 qizheng 工具用 `.venv/bin/python3 -m qizheng.xxx`。
- **SWT**：`moira_extra_files/swt-win.jar` 与 DLL 为 Windows 版本；macOS 上运行 GUI 需替换为 macOS 版 SWT jar（重构后不再需要 GUI）。
- **星历数据**：项目已自带完整 Swiss Ephemeris 数据（`moira_extra_files/ephe/`），无需另行下载。已建软链 `ephe -> moira_extra_files/ephe`。

## Python 接口层实现（qizheng/）

**已落地**：按推荐路径完成 Python 重写，三个 KISS 小工具 + 核心库 + 数据库全部跑通。

### 模块结构

```
qizheng/
├── core.py          # 核心计算库（swisseph + 命理常量 + 七政四余算法）
├── constants.json   # 命理常量（从 moira_s.prop 提取）
├── chart.py         # 排盘小工具：生辰 → 星盘 JSON
├── daxian.py        # 大限小工具：生辰+年龄 → 大限/小限/飞限 JSON
├── rectify.py       # 矫正小工具：目标黄经 → 反推时间 JSON
├── db.py            # SQLite 数据库（命主/星盘/矫正/大限）
├── spike_chart.py   # Python spike（验证用）
├── README.md        # 模块文档
└── __init__.py
```

详细文档见 <ref_file file="~/MOIRA_chinese_astrology-main/qizheng/README.md" />。

### 核心库 core.py 已实现算法

| 函数 | 对应 MOIRA 源码 | 状态 |
|---|---|---|
| `init_ephe()` | Calculate.setChartMode (Lahiri) | ✅ |
| `calc_planet()` / `calc_all_bodies()` | Calculate.compute | ✅ |
| `calc_houses()` | Calculate.computeHouses | ✅ |
| `calc_life_sign()` | ChartData.computeLifeSign | ⚠️ 传统算法基准日简化 |
| `calc_self_sign_v2()` | ChartData.computeSelfSign | ✅ 日落/月升基准已实现 |
| `calc_child_limit_years()` | ChartData.getChildLimit | ✅ |
| `calc_daxian()` / `daxian_full()` | ChartData.nowYearPosition | ✅ |
| `small_limit()` / `child_limit_pos()` | ChartData.getSmallLimit/getChildLimit | ✅ |
| `fly_limit()` | ChartData.getFlyLimit | ⚠️ 半年切换简化 |
| `calc_solar_terms_v2()` | Calculate.computeSolarTerms | ✅ 使用 swe.solcross_ut |
| `compute_new_moons()` | Calculate.computeNewMoons | ✅ 使用 swe.mooncross_ut 迭代 |
| `solar_to_lunar()` | Calculate.getLunarDate | ✅ 已验证4个春节日期正确 |
| `calc_rise_set()` | Calculate.computeRiseSet | ✅ 白天/夜间判定正确 |
| `calc_lunar_mansion()` | 二十八宿宿度 | ✅ 新增，28宿宿度表 |
| `calc_sheng_zhang()` | 长生十二运 | ✅ 新增，五行×地支→十二运 |
| `calc_speed_state()` | Calculate.getSpeedState | ✅ 新增，逆顺迟疾判定 |
| `calc_dignity()` / `calc_dignity_from_lon()` | moira_s.prop 星辰表 | ✅ 新增，庙旺平陷（殿/垣/庙/旺/乐/喜/怒） |
| `calc_na_yin()` / `calc_na_yin_from_year()` | moira_s.prop 纳音表 | ✅ 新增，六十甲子纳音五行 |
| `calc_ten_god_transform()` | moira_s.prop 十干化曜 | ✅ 新增，天干→化曜星 |
| `calc_stem_stars()` | moira_s.prop 天干星曜 | ✅ 新增，天干×地支→吉凶星曜 |
| `calc_branch_stars()` / `calc_branch_stars_for_all()` | moira_s.prop 地支神煞 | ✅ 新增，年支×地支→38神曜 |
| `load_rules_library()` | EvalRule + Rule.yacc | ✅ 新增，加载134条格局规则 |
| `eval_rules()` | EvalRule.computeRules | ⚠️ 简化版求值器，76/134条可求值 |
| `find_date_at_sun_pos()` | ChartData.getDateAtSunPos | ✅ |
| `find_date_at_planet_pos()` | ChartData.getDateAtPlanetPos | ✅ |

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
- 134 条吉格局规则（`+` 开头）
- 每条规则含：编号、名称、优先级 `[level.rank.sub]`、条件表达式、排斥规则、注释
- 优先级分布：[1.2.0] 4条 / [2.0.x] 19条 / [2.2.0] 18条 / [2.3.0] 43条 / [2.4.0] 5条 / [3.1.0] 10条 / [3.2.0] 20条 / [4.x.0] 9条
- 规则语言支持：`@`（黄道星座）/ `%`（恒星宿度）/ `$`（字符串）/ `?`（布尔判定）/ `&|!`（逻辑运算）/ `&func()`（函数调用）
- Python 求值器 `core.eval_rules()` 当前可求值 76/134 条（29条模板规则 + 29条复杂语法跳过）

### SQLite 数据库

`db.py` + `qizheng.db`（单文件），4 表：
- `subject`：命主档案
- `chart`：星盘记录
- `rectification`：矫正历史
- `daxian`：大限结果

### 运行方式

```bash
.venv/bin/python3 -m qizheng.chart --year 1990 --month 5 --day 15 --hour 3.5 --lon 116.4 --lat 39.9
.venv/bin/python3 -m qizheng.daxian --year 1990 --month 5 --day 15 --hour 3.5 --age 35
.venv/bin/python3 -m qizheng.rectify --year 1990 --month 5 --day 15 --hour 3.5 --target '{"sun":30.0}'
```

### 已知 TODO

#### ⏳ 高优先级：Java 方法审计与翻译缺口表

**任务**：对 MOIRA Java 原代码做完整方法级审计，产出翻译状态表 + 未翻译功能块清单 + moira_s.prop key 缺口表，回写本 AGENTS.md。

**触发原因**：Phase 1-3 收口后诚实审计发现翻译覆盖率约 30%（Calculate 50% / ChartData 22% / EvalRule 33% / RuleEntry 0% / moira_s.prop 命理key 10%），且本 AGENTS.md 未记录完整未翻译清单，下一个 session 会误判进度。

**执行文档**：<ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/04-Java方法审计与翻译缺口表.md" />（含 8 个执行步骤，边做边勾选）

**初步识别的 20 个未翻译功能块**（待审计确认，详见 dev-docs/04）：
1. 八字系统（computeEightCharData）2. 神煞完整体系（getStarSigns）3. 流年神煞（getYearInfo）4. 流年推演（computeNowData）5. 推运系统（computeTransitData）6. 返照系统 7. 主限/次限推运 8. 日月食 9. 三煞 10. 太岁/年神 11. 大运/小限/月限/飞限完整实现 12. 高格林区位 13. 恒星计算 14. 方位角/高度角 15. 罗盘方位 16. 相位系统 17. 规则引擎24内置函数 18. 规则引擎58条复杂规则 19. 地方视太阳时 20. 地支顺逆

#### 既有遗留问题

- `calc_life_sign` 传统算法的 `birth_adj_date` 基准日定义需确认。
- `fly_limit` 童限后半年切换逻辑需完整实现。
- `calc_lunar_mansion` 角宿起点（MANSION_START=174°）需根据岁差精确校准。
- `dignity_states` 中"殿"状态目前无数据（moira_s.prop 中未找到殿表）。
- `eval_rules()` 简化版求值器当前 76/134 条可求值，需增量支持：
  - 模板规则展开（29条 `{}` 占位符规则）
  - 月柱变量 `${月柱}` （影响7条规则）
  - 算术运算 `@命+6=@日`（影响1条规则）
  - 函数调用 `&func()`（影响7条规则）
- Phase 4+：流年推演待实现（依赖审计完成后的功能块排序）。
- Phase 5+：完整 Rule.yacc 语法求值器（如果需要 100% 规则覆盖）。

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
| <ref_file file="~/MOIRA_chinese_astrology-main/dev-docs/04-Java方法审计与翻译缺口表.md" /> | **⏳ TODO：Java 方法完整审计 + 翻译缺口表（翻译覆盖率约30%，20个未翻译功能块）** |

## 工作原则

- 代码改动服务于上述排盘 / 矫正 / 分析目标，不是为写代码而写代码。
- 涉及命理算法、星历计算、矫正逻辑时，先理解七政四余理论与现有实现，再动手。
- 数值计算交给代码，命理判断交给 AI，二者不混用。
- 改动前先定位相关模块（见上方"关键功能定位"），避免盲改。
- 编译/运行前先确认依赖（SWT 平台版本、Python 库、星历数据路径）。
- **项目代码知识落盘规则**：项目的代码知识（结构、机制、定位、踩坑、调查结论等）被发现后，应及时记录到 dev-notes 或本文件，不只活在当前 session 的上下文里。
- **研究性内容落盘规则**：详细的算法研究、代码耦合分析、典籍目录对照等长内容，放到 `dev-notes/` 目录，AGENTS.md 只保留索引指针。
