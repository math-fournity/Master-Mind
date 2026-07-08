## Calculate.java 七政四余核心算法研究


### 1. 恒星黄道（sidereal）模式

**位置**：`base/Calculate.java:239-265` `setChartMode()`

七政四余用恒星黄道（非回归黄道）。MOIRA 支持 17 种 ayanamsa：

```
sidereal_systems = { FAGAN_BRADLEY, LAHIRI, YUKTESHWAR, RAMAN, JN_BHASIN,
  DELUCE, USHASHASHI, KRISHNAMURTI, DJWHAL_KHUL, YUKTESHWAR, HIPPARCHOS,
  SASSANIAN, BABYL_KUGLER1/2/3, BABYL_ETPSC, BABYL_HUBER }
```

模式选择逻辑：
- `ASTRO_MODE + astro_system_mode!=0` → 用 `sidereal_systems[astro_sidereal_index]`
- `SIDEREAL_MODE` 或 `PICK_MODE+pick_sidereal_mode` → 支持自定义 ayanamsha base（`SE_SIDM_USER` + `ayanamsha_base_degree` + `ayanamsha_base_date`），否则默认 `FAGAN_BRADLEY`
- 其他 → 回归黄道

**七政四余传统用 Lahiri**（spike 已验证）。但 MOIRA 的 SIDEREAL_MODE 默认是 FAGAN_BRADLEY——这是个需要注意的点：七政四余模式可能走的是 ASTRO_MODE 分支或自定义 base，不是 SIDEREAL_MODE 默认。

`getAyanamsha()` (267-280) 返回当前 ayanamsa 偏移量。

### 2. 宫位（house）算法

**位置**：`base/Calculate.java:691-723`

```java
computeHouses(cusps, ut):
  i_flag = ephe_flag | (sidereal_mode ? SEFLG_SIDEREAL : 0)
  swe_houses(ut, i_flag, lat, lon, house_system_char[house_system_index], cusps, ascmc)
  // cusps[0..12] = 12 宫宫头, ascmc[0]=ASC, ascmc[1]=MC
```

- `house_system_char` 从 prop 加载，是宫位制字符（Placidus 'P', Koch 'K', Equal 'A', Whole 'W' 等）。
- `computeHousesFromMidHeaven(cusps, midheaven)` (707-723)：迭代法调整 UT 让 MC 等于指定值——**这是矫正/择日的底层能力**。
- sidereal 模式时宫位也用恒星黄道。

### 3. 行星位置计算

**位置**：`base/Calculate.java:427-463` `compute(int body)`

```java
compute(body):
  if SE_START..SE_END → computeSpecial (ASC/MC/Fortune)
  if body < 0 → computeOrbit
  else → swe_calc_ut(jd_ut, body, ephe_flag|SEFLG_SPEED|sidereal, computation, error)
  // computation[0]=黄经, [1]=黄纬, [2]=距离, [3-5]=三速度
  // 有星历文件缺失自动加载逻辑 (loadEphIndex)
```

- `computeSpecial`：ASC=`ascmc[0]`, MC=`ascmc[1]`, Fortune=`ASC + (moon-sun)`（日生顺推，夜生逆推）。
- 返回 `computation[0]`（黄经），但 6 元数组完整保留。

### 4. 命宫（life_sign_pos）—— 七政四余核心

**位置**：`base/ChartData.java:6689-6705` `computeLifeSign()`

命宫是所有大限/小限/飞限的基准。算法：

```
sun_pos = computePlanet(SUN)
if life_mode != 0:  # 用第一宫宫头
    pos = cusp[1]  (即 ASC)
    if astro_snap_to_sun_pos == 0: return pos
else:  # 传统算法 (life_mode=0, prop 默认)
    adj_ut = JD(snapToSignStart(出生日)) - JD(snapToSignStart(基准日))
    pos = normalize(sun_pos - adj_ut * 360)  # forward，太阳每回归年退 360°
return (sun_pos % 30) + ((int)pos / 30) * 30
# = 太阳在星座内度数 + pos 所在星座起始度数
```

- `snapToSignStart`：把时间对齐到星座起始（2 小时粒度）。
- 传统算法本质：从出生日逆推到"命宫月份"的太阳位置，取其星座 + 太阳在星座内的精确度数。
- `life_mode=0`（prop 默认）→ 传统算法。

**身宫** `computeSelfSign` (6707-6727)：类似但用月亮，backward，`self_mode` 控制（日落/月升基准）。

### 5. 童限（起限年龄）

**位置**：`base/ChartData.java:4362-4372` `getChildLimit(boolean)`

```
degree = life_sign_pos % 30  # 命宫在星座内度数
base = (child_period != 0) ? 10.0 : 9.0  # prop 默认 child_period=0 → 9 年
day = (base + degree/3) * 365.25
# 童限天数 = (9 + 命宫度数/3) 年
# 命宫度数越大，起限越晚
```

- `child_period=0`（prop 默认）→ 9 年起。
- 童限宫位 `getChildLimit(cur_age, sep)` (7501-7513)：`life_sign_pos + 30 * child_seq[cur_age]`，`child_seq=0,1,7,6,10,9,8,7,6,5,4,3,2,1,0`。

### 6. 洞微大限（limit_seq）

**位置**：`base/ChartData.java:221,514,3901` + prop

```
limit_seq = 11.0, 10.0, 11.0, 15.0, 8.0, 7.0, 11.0, 4.5, 4.5, 4.5, 5.0, 5.0
# 12 限，每限年数，从命宫起逆数
```

`nowYearPosition(age)` (3885-3924)：遍历 limit_seq 找当前年龄在哪一限，算度数偏移：
```
for i in 0..11:
    year = (i==0) ? childLimit/365.25 : limit_seq[i]
    if val < year: degree = degree_offset + 30 * val / year; break
    degree_offset += 30; val -= year
# 限内位置 = 限起始 + 30° * (已过年龄/该限年数)
```

- 第 0 限用童限年数，后续用 limit_seq。
- 每限 30°，12 限共 360°。

### 7. 小限 / 月限 / 飞限

- **小限** `getSmallLimit` (7515-7522)：`life_sign_pos + (age-1)*30°`，每年顺行一宫。
- **月限** `getMonthLimit` (7524-7538)：`life_sign_pos + index*30°`，index 基于农历月份差。
- **飞限** `getFlyLimit` (7540-7584)：分童限前/后，阴阳命宫用不同序列：
  - `fly_seq_yang1=0,0,6,6,8,4` / `fly_seq_ying1=0,0,6,6,4,8`（童限前）
  - `fly_seq_yang2/ying2`（童限后，长序列，含半年切换 `fly_seq_half_shift`）

### 8. 节气（矫正用）

**位置**：`base/Calculate.java:1102-1125` `computeSolarTerms()`

```
26 节气，每 15° 一个，从 -90°(冬至)开始
when = JD(出生前一年12月1日)
for i in 0..25:
    degree = 15*i - 90
    when = computeTransit(SE_SUN, when, degree)  # 太阳到达指定黄经的时间
    solar_terms[i] = BeijingTime(when)
    when += 13
```

- 用太阳 transit 到指定黄经度数定节气时间——**这是定月份边界、矫正出生农历月份的关键**。

### 9. 星盘矫正底层（getDateAtSunPos / getDateAtPlanetPos）

**位置**：`base/ChartData.java:7961-8027`

```
getDateAtSunPos(degree, ..., backward):
    jd_ut = computePlanetTransit(SUN, start_ut, degree, backward)
    # 给定目标黄经，反推太阳到达该位置的时间
getDateAtPlanetPos(planet_no, degree, ..., backward):
    jd_ut = computePlanetTransit(planet_no, start_ut, degree, backward)
    # 任意行星反推
```

- **这是星盘矫正的核心能力**：已知某天体"应该"在某个位置，反求出生时间。
- `computePlanetTransit` 底层调 `eph.getNextTransitUT`（swisseph 的 transit 搜索）。

### 算法依赖的命理常量（从 prop 提取）

这些常量是算法的"参数"，重构时需提取成 JSON/Python dict：

| 常量 | 值（moira_s.prop） | 用途 |
|---|---|---|
| `limit_seq` | `11,10,11,15,8,7,11,4.5,4.5,4.5,5,5` | 洞微大限 12 限年数 |
| `child_seq` | `0,1,7,6,10,9,8,7,6,5,4,3,2,1,0` | 童限宫位序列 |
| `fly_seq_yang1/ying1` | `0,0,6,6,8,4` / `0,0,6,6,4,8` | 飞限童限前序列 |
| `fly_seq_yang2/ying2` | （长序列，见 prop） | 飞限童限后序列 |
| `fly_seq_half_shift` | （见 prop） | 飞限半年切换点 |
| `child_period` | `0` | 童限 9 年起 |
| `life_mode` | `0` | 命宫传统算法 |
| `self_mode` | `0` | 身宫月亮算法 |
| `mountain_signs` | 24 山 | 24 方位 |
| `zodiac` / `full_zodiac` | 12 星座 | 黄道标识 |
| `house_system_char` | 宫位制字符 | P/K/A/W 等 |

### 研究结论 · 对"搬还是重写"的判断

| 算法 | 位置 | GUI 耦合 | 重写难度 | 建议 |
|---|---|---|---|---|
| 恒星黄道模式 | Calculate | 仅 Resource 读 pref | 低 | **Python 重写**（调 pyswisseph 的 swe_set_sid_mode） |
| 宫位 | Calculate | 仅 Resource 读 char | 低 | **Python 重写**（调 swe_houses） |
| 行星位置 | Calculate | 仅 Resource + 星历加载 | 低 | **Python 重写**（调 swe_calc_ut） |
| 命宫 | ChartData | 仅 Resource 读 life_mode | 中 | **Python 重写**（算法已搞懂，纯数学） |
| 童限 | ChartData | 仅 Resource 读 child_period | 低 | **Python 重写**（公式简单） |
| 洞微大限 | ChartData | 仅 Resource 读 limit_seq | 低 | **Python 重写**（遍历 + 算术） |
| 小限/月限/飞限 | ChartData | 仅 Resource 读序列 | 中 | **Python 重写**（序列已提取） |
| 节气 | Calculate | 无 | 低 | **Python 重写**（transit 搜索） |
| 矫正反推 | ChartData | 仅 Resource | 低 | **Python 重写**（transit 搜索） |

**核心判断**：所有七政四余命理算法的本质都是 **"swisseph 星历计算 + 命理常量参数 + 简单算术"**。算法逻辑已完全搞懂，命理常量已提取。GUI 耦合仅在于通过 Resource 读常量——把常量改成 JSON/dict 后，**全部可以用 Python + pyswisseph 重写，不需要搬 Java 代码**。

**推荐路径：Python 重写接口层**。理由：
1. 算法已彻底搞懂，重写无黑盒风险。
2. 命理常量已提取成结构化数据。
3. Python + pyswisseph 对 AI/JSON/pipeline 最友好，KISS。
4. 避免拖入 ChartData 9424 行上帝类和 Resource 全局状态的泥潭。
5. CS41.py 的评分/优化函数库可直接复用，同语言栈。

