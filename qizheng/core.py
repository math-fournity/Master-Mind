"""七政四余核心计算库。
封装 swisseph 星历 + 命理常量 + 七政四余算法（恒星黄道、宫位、命宫、童限、大限、小限、飞限、节气、矫正反推）。
所有算法来自对 MOIRA Calculate.java / ChartData.java 的研究，用 Python 重写。
"""
import json, os
from datetime import datetime, timedelta
import swisseph as swe

_HERE = os.path.dirname(os.path.abspath(__file__))
_CONST_PATH = os.path.join(_HERE, "constants.json")

# 天体 ID 映射（七政 + 罗睺 + 月孛）
# 紫炁是虚星，没有天文对应体，不能用 Swiss Ephemeris 计算，用自定义线性运动（见 calc_ziqi）
BODIES = {
    "sun":     swe.SUN,
    "moon":    swe.MOON,
    "mercury": swe.MERCURY,
    "venus":   swe.VENUS,
    "mars":    swe.MARS,
    "jupiter": swe.JUPITER,
    "saturn":  swe.SATURN,
    "true_node_rohuo":   swe.TRUE_NODE,   # 罗睺（真交点）
    "mean_apog_yuebei":  swe.MEAN_APOG,   # 月孛（平均远地点，与 Java MOIRA 一致）
}
# 计都 = 罗睺对宫
INV_TRUE_NODE = "inv_true_node_jidu"
# 紫炁 key（保持兼容，但计算方式已改为线性运动）
ZIQI_KEY = "mean_apog_ziqi"
YUEBEI_KEY = "mean_apog_yuebei"  # 新 key（mean_apog_yuebei 已废弃）

# --- 紫炁线性运动参数（匹配 Java MOIRA moira_s.prop）---
# 紫炁是虚星，约28年行一周天，匀速顺行，无天文对应体
# 基准点：1975-03-13 16:00 UT，回归黄道 230.5°
# 用《授时历》1280年数据点验证：误差约6°（694年外推，可接受）
ZIQI_PERIOD = 10227.1792       # 周期（天）≈ 28年
ZIQI_BASE_LON = 230.5          # 基准度数（回归黄道）
ZIQI_SPEED = 360.0 / ZIQI_PERIOD  # 每日行度 ≈ 0.03520034°/天

def _ziqi_base_jd():
    """紫炁基准日期的儒略日：1975-03-13 16:00 UT。"""
    return swe.julday(1975, 3, 13, 16.0)

# --- 四余计算模式开关 ---
# true_as_north: True=罗睺=升交点（新法/汤若望法，Java默认）
#                False=罗睺=降交点（旧法/传统星命家法）
# yuebei_mode: "mean"=平均远地点（Java MOIRA），"oscu"=osculating远地点
_true_as_north = True
_yuebei_mode = "mean"

def set_four_yu_mode(true_as_north=True, yuebei_mode="mean"):
    """设置四余计算模式。
    true_as_north: True=罗睺升交点(新法/Java默认)，False=罗睺降交点(旧法/传统)
    yuebei_mode: "mean"=平均远地点(Java MOIRA)，"oscu"=osculating远地点
    """
    global _true_as_north, _yuebei_mode
    _true_as_north = true_as_north
    _yuebei_mode = yuebei_mode

# 命理常量（懒加载）
_CONST = None

def load_constants(path=None):
    """加载命理常量 JSON。"""
    global _CONST
    if _CONST is None or path:
        with open(path or _CONST_PATH, encoding="utf-8") as f:
            _CONST = json.load(f)
    return _CONST

def _c():
    if _CONST is None:
        load_constants()
    return _CONST

def init_ephe(ephe_path="ephe"):
    """初始化星历路径 + Lahiri 恒星黄道。"""
    swe.set_ephe_path(ephe_path)
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)

def jd_from_ymd_ut(y, mo, d, h_ut=0.0):
    """公历日期 -> 儒略日(UT)。"""
    return swe.julday(y, mo, d, h_ut)

def ymd_ut_from_jd(jd):
    """儒略日(UT) -> (y, mo, d, h_ut)。"""
    return swe.revjul(jd)

def normalize_degree(deg):
    """归一化到 [0, 360)。"""
    return deg % 360.0

def degree_gap(a, b):
    """两角度最短间距 (-180, 180]。"""
    d = (a - b) % 360.0
    if d > 180.0:
        d -= 360.0
    return d

# ---------- 行星位置 ----------

def calc_planet(jd, pid, sidereal=True, speed=True):
    """计算行星位置。返回 (lon, lat, dist, lon_speed, lat_speed, dist_speed)。"""
    flag = swe.FLG_SWIEPH | swe.FLG_SPEED
    if sidereal:
        flag |= swe.FLG_SIDEREAL
    xx, ret = swe.calc_ut(jd, pid, flag)
    if ret < 0:
        return None
    return xx

def calc_ziqi(jd, sidereal=True):
    """计算紫炁位置（匀速线性运动，虚星无天文对应体）。

    匹配 Java MOIRA 的自定义轨道算法：
      degree = base_lon + speed * (jd - base_jd)
    sidereal 模式下减去 ayanamsa（与 Java computeOrbit 一致）。

    参数来源：moira_s.prop → purple_period / purple_base_date / purple_base_degree
    验证：用《授时历》1280年数据点（紫气在女二度）验证，误差约6°（694年外推）。
    """
    base_jd = _ziqi_base_jd()
    lon_tropical = (ZIQI_BASE_LON + ZIQI_SPEED * (jd - base_jd)) % 360.0
    if sidereal:
        ayanamsa = swe.get_ayanamsa_ut(jd)
        lon = (lon_tropical - ayanamsa) % 360.0
    else:
        lon = lon_tropical
    return {
        "lon": round(lon, 6),
        "lat": 0.0,
        "dist": 1.0,
        "lon_speed": round(ZIQI_SPEED, 6),
        "lat_speed": 0.0,
        "dist_speed": 0.0,
    }

def calc_all_bodies(jd, sidereal=True):
    """计算七政四余所有天体。返回 dict[name] -> {lon, lat, dist, *_speed}。

    四余计算方式：
    - 罗睺：Swiss Ephemeris TRUE_NODE（真交点），受 true_as_north 开关影响
    - 计都：罗睺 + 180°
    - 紫炁：匀速线性运动（虚星，无天文对应体），见 calc_ziqi
    - 月孛：Swiss Ephemeris MEAN_APOG（平均远地点，受 yuebei_mode 开关影响）
    """
    out = {}
    for name, pid in BODIES.items():
        # 月孛：根据 yuebei_mode 选择 MEAN_APOG 或 OSCU_APOG
        if name == YUEBEI_KEY and _yuebei_mode == "oscu":
            pid = swe.OSCU_APOG
        xx = calc_planet(jd, pid, sidereal=sidereal)
        if xx is None:
            out[name] = {"error": "calc failed"}
            continue
        out[name] = {
            "lon": round(xx[0], 6),
            "lat": round(xx[1], 6),
            "dist": round(xx[2], 8),
            "lon_speed": round(xx[3], 6),
            "lat_speed": round(xx[4], 6),
            "dist_speed": round(xx[5], 8),
        }
    # 紫炁：线性运动（不在 BODIES 中，单独计算）
    out[ZIQI_KEY] = calc_ziqi(jd, sidereal=sidereal)
    # 计都 = 罗睺 + 180
    rn = out.get("true_node_rohuo", {})
    if "lon" in rn:
        out[INV_TRUE_NODE] = {**rn, "lon": round(normalize_degree(rn["lon"] + 180.0), 6)}
        # 旧法（true_as_north=False）：交换罗睺和计都
        if not _true_as_north:
            out["true_node_rohuo"], out[INV_TRUE_NODE] = out[INV_TRUE_NODE], out["true_node_rohuo"]
    return out

# ---------- 宫位 ----------

def calc_houses(jd, lat, lon, house_system='P', sidereal=True):
    """计算 12 宫宫头 + ASC/MC。返回 (cusps, ascmc)。
    使用 houses_ex 支持 sidereal flag。
    极区（|lat|>66°）Placidus 失败时回退到整宫制（'W'）。
    """
    flag = swe.FLG_SIDEREAL if sidereal else 0
    try:
        cusps, ascmc = swe.houses_ex(jd, lat, lon, house_system.encode(), flag)
    except Exception:
        # 极区 Placidus 失败，回退到整宫制
        cusps, ascmc = swe.houses_ex(jd, lat, lon, b'W', flag)
    return cusps, ascmc

# ---------- 命宫 ----------

def _snap_to_sign_start(date_arr):
    """把时间对齐到星座起始（2 小时粒度），模拟 ChartData.snapToSignStart。"""
    y, mo, d, h, mi = date_arr
    hour = ((h + 1) // 2) * 2 - 1
    day_off = 0
    if hour < 0:
        hour = 23
    if h < 1:
        day_off = -1
    return [y, mo, d + day_off, hour, 0]

def calc_life_sign(birth_date, sun_pos, cusps):
    """计算命宫位置(life_sign_pos)。算法来自 ChartData.computeLifeSign。
    birth_date: [y,mo,d,h,mi]
    sun_pos: 太阳恒星黄经
    cusps: 宫头数组
    """
    c = _c()
    life_mode = c["life_sign"]["life_mode"]
    if life_mode != 0 and len(cusps) > 1:
        pos = cusps[1]  # ASC
        if c["life_sign"].get("astro_snap_to_sun_pos", 0) == 0:
            return pos
    else:
        # 传统算法: 太阳每回归年退 360°
        # adj_ut = JD(snap(出生日)) - JD(snap(基准日))
        # 基准日 = 出生年1月1日? MOIRA 用 birth_adj_date, 这里取出生日 snap
        snap_birth = _snap_to_sign_start(birth_date)
        jd_birth = jd_from_ymd_ut(snap_birth[0], snap_birth[1], snap_birth[2], snap_birth[3] + (snap_birth[4]/60.0 if len(snap_birth) > 4 else 0.0))
        # 基准: 出生日 snap 本身 (adj_ut=0 时 pos=sun_pos)
        # 实际 MOIRA 用 birth_adj_date (年初), 这里简化为用出生日
        # TODO: 确认 birth_adj_date 的确切定义
        pos = normalize_degree(sun_pos)
    return (sun_pos % 30) + (int(pos) // 30) * 30

def calc_self_sign(moon_pos, birth_date, moon_rise_date=None, sun_set_date=None):
    """计算身宫。算法来自 ChartData.computeSelfSign。"""
    c = _c()
    self_mode = c["life_sign"]["self_mode"]
    if self_mode == 0:
        return moon_pos
    # self_mode 1: 日落基准, 2: 月升基准
    # 简化: backward, moon_pos + adj_ut * 360
    # TODO: 完整实现需日落/月升时间
    return moon_pos

# ---------- 童限 ----------

def calc_child_limit_years(life_sign_pos, round_to_year=True):
    """童限年数。算法来自 ChartData.getChildLimit。
    童限天数 = (9 + 命宫度数/3) * 365.25
    """
    c = _c()
    degree = life_sign_pos % 30.0
    base = 10.0 if c["life_sign"]["child_period"] != 0 else 9.0
    days = (base + degree / 3.0) * 365.25
    if round_to_year:
        return int(days / 365.25 + 0.5)
    return int(days)

# ---------- 洞微大限 ----------

def calc_daxian(life_sign_pos, age, child_limit_years=None):
    """洞微大限: 给定年龄, 返回当前所在限及限内位置。
    返回 {limit_index, limit_years, age_in_limit, degree_in_limit, limit_start_degree}
    算法来自 ChartData.nowYearPosition。
    """
    c = _c()
    limit_seq = c["limits"]["limit_seq"]
    if child_limit_years is None:
        child_limit_years = calc_child_limit_years(life_sign_pos, round_to_year=False) / 365.25

    # 年龄从 1 开始, val = age - 1 - (年内偏移)  简化: val = age - 1
    val = age - 1
    degree_offset = 0.0
    for i in range(len(limit_seq)):
        year = child_limit_years if i == 0 else limit_seq[i]
        if val < year:
            return {
                "limit_index": i,
                "limit_years": year,
                "age_in_limit": round(val, 4),
                "degree_in_limit": round(degree_offset + 30.0 * val / year, 6),
                "limit_start_degree": round(degree_offset, 6),
            }
        degree_offset += 30.0
        val -= year
    return None  # 超出 12 限

def daxian_full(life_sign_pos, child_limit_years=None):
    """列出全部 12 限的起止年龄与起始度数。"""
    c = _c()
    limit_seq = c["limits"]["limit_seq"]
    if child_limit_years is None:
        child_limit_years = calc_child_limit_years(life_sign_pos, round_to_year=False) / 365.25
    out = []
    age_start = 0.0
    for i in range(len(limit_seq)):
        year = child_limit_years if i == 0 else limit_seq[i]
        out.append({
            "limit_index": i,
            "age_start": round(age_start, 4),
            "age_end": round(age_start + year, 4),
            "years": year,
            "start_degree": round(i * 30.0, 6),
            "end_degree": round((i + 1) * 30.0, 6),
        })
        age_start += year
    return out

# ---------- 小限 / 月限 / 飞限 ----------

def small_limit(life_sign_pos, age):
    """小限: 命宫 + (age-1)*30°, 每年顺行一宫。"""
    return normalize_degree(life_sign_pos + (age - 1) * 30.0)

def child_limit_pos(life_sign_pos, age):
    """童限宫位: 命宫 + 30 * child_seq[age]。"""
    c = _c()
    seq = c["limits"]["child_seq"]
    if age < 0 or age >= len(seq):
        return None
    return normalize_degree(life_sign_pos + 30.0 * seq[age])

def fly_limit(life_sign_pos, age, child_age_limit):
    """飞限。算法来自 ChartData.getFlyLimit。"""
    c = _c()
    idx = int(life_sign_pos / 30.0)
    if age >= 0 and age < child_age_limit:
        seq = c["limits"]["fly_seq_yang1"] if idx % 2 == 0 else c["limits"]["fly_seq_ying1"]
        return normalize_degree(life_sign_pos + 30.0 * seq[age % len(seq)])
    elif age >= child_age_limit:
        a = age - child_age_limit
        seq = c["limits"]["fly_seq_yang2"] if idx % 2 == 0 else c["limits"]["fly_seq_ying2"]
        hs = c["limits"]["fly_seq_half_shift"]
        if a + 2 < len(seq):
            # 简化: 取 seq[a+1] (完整年)
            return normalize_degree(life_sign_pos + 30.0 * seq[a + 1])
    return None

# ---------- 节气 ----------

def calc_solar_terms(birth_year, ephe_path="ephe"):
    """计算出生年前后 26 节气。算法来自 Calculate.computeSolarTerms。
    每 15° 一个, 从冬至(-90°)开始。
    """
    init_ephe(ephe_path)
    date = [birth_year - 1, 12, 1, 0, 0]
    when = jd_from_ymd_ut(*date[:4])
    terms = []
    for i in range(26):
        degree = normalize_degree(15.0 * i - 90.0)
        when = swe.sol_cross_ut(degree, when) if hasattr(swe, 'sol_cross_ut') else _transit_sun(when, degree)
        if when is None:
            break
        y, mo, d, h = ymd_ut_from_jd(when)
        terms.append({"index": i, "degree": round(degree, 2), "date": f"{y:04d}-{mo:02d}-{d:02d}T{h:07.4f}"})
        when += 13.0
    return terms

def _transit_sun(start_ut, target_degree, backward=False):
    """太阳到达目标黄经的时间。用 swe.next_transit_ut 或迭代。"""
    # pyswisseph 有 sol_cross_ut / next_transit
    try:
        return swe.sol_cross_ut(target_degree, start_ut)
    except AttributeError:
        # fallback: 牛顿迭代
        jd = start_ut
        for _ in range(100):
            xx = calc_planet(jd, swe.SUN, sidereal=False, speed=True)
            if xx is None:
                return None
            cur = xx[0]
            spd = xx[3]
            delta = degree_gap(target_degree, cur)
            if abs(delta) < 0.01:
                return jd
            if abs(spd) < 1e-9:
                return None
            jd += delta / spd
        return jd

# ---------- 矫正反推 ----------

def find_date_at_sun_pos(target_degree, start_jd, backward=False, ephe_path="ephe"):
    """给定目标太阳黄经, 反推时间。算法来自 ChartData.getDateAtSunPos。"""
    init_ephe(ephe_path)
    return _transit_sun(start_jd, target_degree, backward)

def find_date_at_planet_pos(planet_id, target_degree, start_jd, backward=False, ephe_path="ephe"):
    """给定目标行星黄经, 反推时间。"""
    init_ephe(ephe_path)
    # 牛顿迭代
    jd = start_jd
    for _ in range(100):
        xx = calc_planet(jd, planet_id, sidereal=True, speed=True)
        if xx is None:
            return None
        delta = degree_gap(target_degree, xx[0])
        if abs(delta) < 0.01:
            return jd
        if abs(xx[3]) < 1e-9:
            return None
        step = delta / xx[3]
        jd += step if not backward else -abs(step)
    return jd

# ---------- 节气（修正版，使用 solcross_ut） ----------

def calc_solar_terms_v2(birth_year, ephe_path="ephe"):
    """计算出生年前后 26 节气（修正版）。算法来自 Calculate.computeSolarTerms。
    每 15° 一个, 从冬至(-90°)开始。返回 [{index, degree, jd, date}]。
    使用 swe.solcross_ut 替代旧版 _transit_sun。
    """
    init_ephe(ephe_path)
    when = jd_from_ymd_ut(birth_year - 1, 12, 1, 0.0)
    terms = []
    for i in range(26):
        degree = normalize_degree(15.0 * i - 90.0)
        try:
            when = swe.solcross_ut(degree, when, swe.FLG_SWIEPH)
        except Exception:
            when = _transit_sun(when, degree)
        if when is None:
            break
        y, mo, d, h = ymd_ut_from_jd(when)
        terms.append({
            "index": i,
            "degree": round(degree, 2),
            "jd": round(when, 6),
            "date": f"{y:04d}-{mo:02d}-{d:02d}T{h:07.4f}",
        })
        when += 13.0
    return terms

# ---------- 新月（朔日）计算 ----------

def _new_moon_ut(start_ut, backward=False):
    """计算下一个（或上一个）新月时间。新月 = 日月合朔（黄经差0°）。
    先算太阳黄经，再用 mooncross_ut 搜索月亮经过该黄经。
    迭代2-3次收敛（太阳在搜索期间移动很少）。
    """
    jd = start_ut
    for _ in range(5):
        sun = calc_planet(jd, swe.SUN, sidereal=False, speed=True)
        if sun is None:
            return None
        sun_lon = sun[0]
        try:
            jd = swe.mooncross_ut(sun_lon, jd, swe.FLG_SWIEPH)
        except Exception:
            return None
        if abs(jd - start_ut) < 0.01:
            return jd
        start_ut = jd
    return jd

def compute_new_moons(birth_year, ephe_path="ephe"):
    """计算出生年前后的新月（朔日）时间。算法来自 Calculate.computeNewMoons。
    第一个新月在上年冬至前，最后一个在本年冬至后。
    返回 [jd_ut, ...]（截断到 UT 正午）。
    """
    init_ephe(ephe_path)
    # 先算节气获取冬至
    terms = calc_solar_terms_v2(birth_year, ephe_path)
    if not terms or len(terms) < 25:
        return []
    winter_solstice_prev = terms[0]["jd"]  # 上年冬至
    winter_solstice_this = terms[24]["jd"]  # 本年冬至

    # 策略：从上年冬至前35天开始，向前搜索所有新月直到本年冬至后
    when = winter_solstice_prev - 35.0
    new_moons = []
    for _ in range(20):  # 最多20个新月（一年最多13个）
        nm = _new_moon_ut(when)
        if nm is None:
            break
        nm_trimmed = _trim_hour(nm)
        if nm_trimmed > winter_solstice_this + 35.0:
            break
        if nm_trimmed >= winter_solstice_prev - 35.0:
            new_moons.append(nm_trimmed)
        when = nm_trimmed + 25.0  # 跳到下个新月搜索区间

    new_moons.sort()
    return new_moons

def _trim_hour(val):
    """截断到北京时间零点。
    JD 的整数部分对应 UT 12:00（正午），0.5 对应 UT 00:00（午夜）。
    北京时间 = UT + 8h。北京时间零点 = UT 16:00（前一天）。
    截断逻辑：把 val 转为北京时间，截断到北京时间零点，再转回 UT。
    """
    # 北京时间 = UT + 8h
    bj = val + 8.0 / 24.0
    # 截断到北京时间零点：JD 的 .5 对应零点
    bj_midnight = float(int(bj - 0.5)) + 0.5
    return bj_midnight - 8.0 / 24.0  # 转回 UT

# ---------- 农历转换 ----------

# 地支序号 → 农历月名
_BRANCHES = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
# 天干序号
_STEMS = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]

def _get_chinese_year(year, base=1984):
    """干支年。base=1984 为甲子年（60甲子周期起点）。
    返回干支序号 1-60。
    """
    return ((year - base) % 60) + 1

def _gan_zhi_name(n):
    """干支序号(1-60) → 干支名。"""
    n = n - 1
    stem = _STEMS[n % 10]
    branch = _BRANCHES[n % 12]
    return stem + branch

def _get_leap_month_index(solar_terms_jd, new_moons_jd):
    """确定闰月索引。算法来自 Calculate.getLeapMonthIndex。
    闰月 = 两个新月之间没有中气（偶数索引节气）的月份。
    """
    if len(new_moons_jd) == 14:
        return 100  # 13个月，无闰月
    for j in range(1, len(new_moons_jd)):
        start = _trim_hour(new_moons_jd[j - 1])
        end = _trim_hour(new_moons_jd[j])
        has_mid_term = False
        # 中气 = 偶数索引节气（index 0,2,4,...）
        for i in range(0, len(solar_terms_jd), 2):
            center = solar_terms_jd[i]
            if center >= start and center < end:
                has_mid_term = True
                break
        if not has_mid_term:
            return j - 1
    return 100

def solar_to_lunar(year, month, day, hour_ut=0.0, ephe_path="ephe"):
    """公历转农历。算法来自 Calculate.getLunarDate。
    返回 {year, month, day, is_leap, gan_zhi_year, gan_zhi_month}
    注意：农历计算基于北京时间。
    """
    init_ephe(ephe_path)
    jd = jd_from_ymd_ut(year, month, day, hour_ut)

    # 计算节气和新月
    solar_terms = calc_solar_terms_v2(year, ephe_path)
    if not solar_terms:
        return None
    solar_terms_jd = [t["jd"] for t in solar_terms]

    new_moons = compute_new_moons(year, ephe_path)
    if not new_moons:
        return None

    # 找到当前日期在哪个新月周期内
    jd_trimmed = _trim_hour(jd)
    index = None
    for i in range(1, len(new_moons)):
        if jd_trimmed >= _trim_hour(new_moons[i - 1]) and jd_trimmed < _trim_hour(new_moons[i]):
            index = i
            break
    if index is None:
        return None

    # 闰月判定
    leap_index = _get_leap_month_index(solar_terms_jd, new_moons)
    is_leap = (index - 1) == leap_index

    # 农历月号
    lunar_month = index + 10 - (1 if (index - 1) >= leap_index else 0)
    lunar_year_offset = 0
    if lunar_month <= 12:
        lunar_year_offset = -1  # 去年
    else:
        lunar_month -= 12
        if lunar_month == 12:
            # 需要检查是否闰月
            next_year_terms = calc_solar_terms_v2(year + 1, ephe_path)
            next_year_moons = compute_new_moons(year + 1, ephe_path)
            if next_year_terms and next_year_moons:
                next_leap = _get_leap_month_index(
                    [t["jd"] for t in next_year_terms], next_year_moons)
                if next_leap == 1:
                    is_leap = True
                    lunar_month -= 1

    # 农历日 = 当前日 - 新月日 + 1
    lunar_day = int(jd_trimmed - _trim_hour(new_moons[index - 1])) + 1

    # 干支年
    chinese_year_num = _get_chinese_year(year + lunar_year_offset)
    gan_zhi_year = _gan_zhi_name(chinese_year_num)

    return {
        "lunar_year": year + lunar_year_offset,
        "lunar_month": lunar_month,
        "lunar_day": lunar_day,
        "is_leap": is_leap,
        "gan_zhi_year": gan_zhi_year,
        "chinese_year_num": chinese_year_num,
    }

# ---------- 升落 / 昼夜判定 ----------

def calc_rise_set(jd_ut, lon, lat, alt=0.0, body=None, ephe_path="ephe"):
    """计算天体升落时间。算法来自 Calculate.computeRiseSet。
    body=None 时默认计算太阳。
    返回 {sunrise_jd, sunset_jd, is_day_birth}。
    注意：rise_trans 返回的是 jd_ut 之后的下一个升/落时间，
    所以需要搜索前一天/前12小时来找到当天的升落。
    """
    init_ephe(ephe_path)
    if body is None:
        body = swe.SUN
    geopos = (lon, lat, alt)

    def _try_rise_trans(search_jd, calc_flag):
        try:
            ret, tret = swe.rise_trans(search_jd, body, calc_flag, geopos, 0.0, 20.0)
            return tret[0] if ret == 0 else None
        except Exception:
            # 高纬度 fallback
            try:
                ret, tret = swe.rise_trans(search_jd, body, calc_flag, (lon, 0.0, alt), 0.0, 20.0)
                return tret[0] if ret == 0 else None
            except Exception:
                return None

    # 从前一天开始搜索，确保找到当天的升落
    rise_jd = _try_rise_trans(jd_ut - 1.0, swe.CALC_RISE)
    set_jd = _try_rise_trans(jd_ut - 1.0, swe.CALC_SET)

    # 正确逻辑：
    # rise_trans 返回搜索时间之后的下一个升/落事件
    # 找到出生时间之前最近的日出和出生时间之前最近的日落
    # 如果日出 > 日落（白天出生），需要找当天的日落（在出生之后）
    # 如果日出 < 日落（夜间出生），is_day=False

    # 日出：向前搜索直到日出在出生时间之前
    while rise_jd is not None and rise_jd > jd_ut:
        rise_jd = _try_rise_trans(rise_jd - 0.5, swe.CALC_RISE)

    # 日落：向前搜索直到日落在出生时间之前
    while set_jd is not None and set_jd > jd_ut:
        set_jd = _try_rise_trans(set_jd - 0.5, swe.CALC_SET)

    # 如果日出在日落之后（白天出生），需要找到当天的日落（在出生之后）
    if rise_jd is not None and set_jd is not None and rise_jd > set_jd:
        set_jd = _try_rise_trans(jd_ut, swe.CALC_SET)

    is_day = None
    if rise_jd is not None and set_jd is not None:
        is_day = rise_jd <= jd_ut < set_jd

    # 计算月亮升落（用于昼夜辅助判断）
    moon_rise = _try_rise_trans(jd_ut - 1.0, swe.MOON | swe.CALC_RISE) if hasattr(swe, 'MOON') else None
    moon_set = _try_rise_trans(jd_ut - 1.0, swe.MOON | swe.CALC_SET) if hasattr(swe, 'MOON') else None

    # 昼夜标签
    data = _load_shen_sha()
    daytime_label = data.get('daytime', '昼')
    nighttime_label = data.get('nighttime', '夜')
    day_night_label = daytime_label if is_day else nighttime_label

    return {
        "sunrise_jd": round(rise_jd, 6) if rise_jd else None,
        "sunset_jd": round(set_jd, 6) if set_jd else None,
        "is_day_birth": is_day,
        "is_day": is_day,
        "day_night": day_night_label,
        "moonrise_jd": round(moon_rise, 6) if moon_rise else None,
        "moonset_jd": round(moon_set, 6) if moon_set else None,
    }

# ---------- 二十八宿宿度 ----------

def calc_lunar_mansion(lon, ayanamsa_offset=0.0):
    """根据恒星黄经计算所在二十八宿。
    返回 {mansion_name, mansion_index, mansion_degree, mansion_width, element, animal, group}。
    注意：二十八宿起点（角宿）的恒星黄经需要根据岁差调整。
    当前实现使用 Lahiri ayanamsa 下的近似起点。
    """
    c = _c()
    mansions = c["lunar_mansions"]
    order = mansions["order"]
    widths = mansions["width_yellow"]
    elements = mansions["element"]
    animals = mansions["animal"]
    groups = mansions["group"]

    # 角宿起点在恒星黄道中的位置
    # Lahiri ayanamsa 下，J2000 时角宿一（Spica）约在恒星黄经 180°
    # 二十八宿从角宿开始，角宿起点约在 170°-175°（恒星黄道）
    # 这里用近似值 174° 作为角宿起点
    MANSION_START = 174.0 + ayanamsa_offset

    lon_norm = normalize_degree(lon - MANSION_START)
    cumulative = 0.0
    for i, w in enumerate(widths):
        if lon_norm < cumulative + w:
            return {
                "mansion_name": order[i],
                "mansion_index": i,
                "mansion_degree": round(lon_norm - cumulative, 6),
                "mansion_width": w,
                "element": elements[i],
                "animal": animals[i],
                "group": groups[i],
            }
        cumulative += w
    # fallback（理论不会到这里，因为 widths 合计 360）
    return {
        "mansion_name": order[-1],
        "mansion_index": len(order) - 1,
        "mansion_degree": round(lon_norm - cumulative + widths[-1], 6),
        "mansion_width": widths[-1],
        "element": elements[-1],
        "animal": animals[-1],
        "group": groups[-1],
    }

# ---------- 身宫（修正版） ----------

def calc_self_sign_v2(birth_date, moon_pos, sun_pos, lon, lat, ephe_path="ephe"):
    """计算身宫。算法来自 ChartData.computeSelfSign。
    self_mode=0: 直接用月亮位置
    self_mode=1: 日落基准（从日落时间逆推月亮位置）
    self_mode=2: 月升基准
    """
    c = _c()
    self_mode = c["life_sign"]["self_mode"]
    if self_mode == 0:
        return moon_pos

    jd = jd_from_ymd_ut(birth_date[0], birth_date[1], birth_date[2],
                        birth_date[3] + (birth_date[4] / 60.0 if len(birth_date) > 4 else 0.0))

    if self_mode == 1:
        # 日落基准：找到出生日日落时间，从日落逆推月亮位置
        rs = calc_rise_set(jd, lon, lat, ephe_path=ephe_path)
        if rs["sunset_jd"] is not None:
            # 从日落时间计算月亮位置
            moon_at_sunset = calc_planet(rs["sunset_jd"], swe.MOON, sidereal=True)
            if moon_at_sunset is not None:
                return moon_at_sunset[0]
    elif self_mode == 2:
        # 月升基准：找到出生日月升时间
        rs = calc_rise_set(jd, lon, lat, body=swe.MOON, ephe_path=ephe_path)
        if rs["sunrise_jd"] is not None:  # moonrise
            moon_at_rise = calc_planet(rs["sunrise_jd"], swe.MOON, sidereal=True)
            if moon_at_rise is not None:
                return moon_at_rise[0]

    return moon_pos  # fallback

# ---------- 长生十二运 ----------

_BRANCH_ORDER = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

def calc_sheng_zhang(element, branch, is_yang=True):
    """计算长生十二运状态。
    element: 五行（木/火/金/水/土）
    branch: 地支（子/丑/.../亥）
    is_yang: 阳干 or 阴干
    返回 {stage_index, stage_name, vitality}
    vitality: 长生=10, 冠带=8, 临官=7, 帝旺=6, 衰=4, 病=3, 死=2, 墓=1, 绝=0, 胎=5, 养=6, 沐浴=9
    """
    c = _c()
    sz = c["sheng_zhang_12_stages"]
    stages = sz["stages"]

    if is_yang:
        start_branch = sz["yang_start"].get(element)
        forward = sz["yang_forward"]
    else:
        start_branch = sz["yin_start"].get(element)
        forward = sz["yin_forward"]

    if start_branch is None:
        return None

    start_idx = _BRANCH_ORDER.index(start_branch)
    branch_idx = _BRANCH_ORDER.index(branch)

    if forward:
        offset = (branch_idx - start_idx) % 12
    else:
        offset = (start_idx - branch_idx) % 12

    stage_idx = offset % 12
    # 旺度映射
    vitality_map = {0: 10, 1: 9, 2: 8, 3: 7, 4: 6, 5: 4, 6: 3, 7: 2, 8: 1, 9: 0, 10: 5, 11: 6}

    return {
        "stage_index": stage_idx,
        "stage_name": stages[stage_idx],
        "vitality": vitality_map[stage_idx],
    }

# ---------- 逆顺迟疾状态 ----------

def calc_speed_state(planet_name, lon_speed, sun_lon=None, planet_lon=None):
    """计算行星逆顺迟疾状态。算法来自 Calculate.getSpeedState。
    返回 {state, state_name}
    state: 0=顺, 1=逆, 2=蚀, 3=留, 4=伏, 5=迟, 6=速

    planet_name: 行星名
    lon_speed: 黄经速度
    sun_lon: 太阳黄经（用于计算伏/不见状态）
    planet_lon: 行星黄经（用于计算伏/不见状态）
    """
    c = _c()
    thresholds = c["speed_thresholds"]

    # 行星索引映射到 speed_thresholds 数组
    planet_idx_map = {
        "mercury": 0, "venus": 1, "mars": 2, "jupiter": 3, "saturn": 4
    }
    idx = planet_idx_map.get(planet_name)
    if idx is None:
        # 日月不逆行
        if planet_name in ("sun", "moon"):
            return {"state": 0, "state_name": "顺"}
        return {"state": 0, "state_name": "顺"}

    slow = thresholds["slow_speed"][idx]
    fast = thresholds["fast_speed"][idx]
    gap = thresholds["stationary_gap"][idx]
    invisible_gap = 3.0  # 与太阳合相3°内为伏

    abs_speed = abs(lon_speed)

    # 检查伏（与太阳合相）
    if sun_lon is not None and planet_lon is not None:
        degree_gap = abs(normalize_degree(planet_lon - sun_lon))
        if degree_gap > 180.0:
            degree_gap = 360.0 - degree_gap
        if degree_gap <= invisible_gap:
            return {"state": 4, "state_name": "伏"}

    if lon_speed < 0:
        return {"state": 1, "state_name": "逆"}
    elif abs_speed < gap:
        return {"state": 3, "state_name": "留"}
    elif abs_speed < slow:
        return {"state": 5, "state_name": "迟"}
    elif abs_speed > fast:
        return {"state": 6, "state_name": "速"}
    else:
        return {"state": 0, "state_name": "顺"}

# ---------- 庙旺平陷（殿/垣/庙/旺/乐/喜/怒） ----------

# 行星名映射到 dignity_states 中的 key
_PLANET_DIGNITY_MAP = {
    "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
    "mercury": "水", "mars": "火", "saturn": "土",
    "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
    "mean_apog_ziqi": "炁", "mean_apog_yuebei": "孛",
}

def calc_dignity(planet_name, branch):
    """计算行星在某地支的庙旺状态。
    planet_name: core.BODIES 中的 key
    branch: 地支名（子/丑/.../亥）
    返回 {states: [状态名列表], best_state, best_state_index, is_dignified}
    """
    c = _c()
    dignity = c["dignity_states"]
    planet_key = _PLANET_DIGNITY_MAP.get(planet_name)
    if planet_key is None or planet_key not in dignity["planets"]:
        return {"states": [], "best_state": None, "best_state_index": -1, "is_dignified": False}

    state_list = dignity["planets"][planet_key]
    state_order = dignity["states"]
    matched = []
    for entry in state_list:
        b, s = entry[0], entry[1]
        if b == branch:
            matched.append(s)

    if not matched:
        return {"states": [], "best_state": None, "best_state_index": -1, "is_dignified": False}

    # 找最高等级状态
    best = None
    best_idx = 999
    for s in matched:
        idx = state_order.index(s) if s in state_order else 999
        if idx < best_idx:
            best = s
            best_idx = idx

    return {
        "states": matched,
        "best_state": best,
        "best_state_index": best_idx,
        "is_dignified": best_idx <= 3,  # 殿/垣/庙/旺 为得地
    }

def calc_dignity_from_lon(planet_name, lon):
    """根据行星黄经计算庙旺状态（自动转换到地支）。"""
    branch = _lon_to_branch(lon)
    return calc_dignity(planet_name, branch)

def _lon_to_branch(lon):
    """恒星黄经 → 地支。
    七政四余地支从戌开始（戌=0°，逆序）。
    戌酉申未午巳辰卯寅丑子亥 → 每30°一个地支。
    """
    lon_norm = normalize_degree(lon)
    branch_order = ["戌","酉","申","未","午","巳","辰","卯","寅","丑","子","亥"]
    idx = int(lon_norm / 30.0) % 12
    return branch_order[idx]

def _get_stellar_sign(degree, chart_data):
    """找到黄经度数所在的28宿（翻译 Calculate.getStarSign）。
    返回28宿名（如"昴日"），包含宿名+五行属性。
    """
    data = _load_shen_sha()
    full_stellar_signs = data.get('full_stellar_signs', '').split(', ')
    if not full_stellar_signs:
        return ""
    # 28宿的起始位置需要从星盘数据中获取
    # 简化版：用 mansions 数据找到最近的28宿
    mansions = chart_data.get("mansions", {})
    # mansions 中有每个行星的 mansion 信息，但没有28宿边界
    # 使用简化算法：按等分28宿计算（实际应从 stellar_sign_pos 获取）
    lon_norm = normalize_degree(degree)
    # 28宿等分：360/28 ≈ 12.857°
    # 但28宿不等分，需要真实数据。暂时用等分近似
    idx = int(lon_norm / (360.0 / len(full_stellar_signs))) % len(full_stellar_signs)
    return full_stellar_signs[idx]

# 七政四余地支顺序（戌=0°开始逆序），与 moira_s.prop zodiac 一致
_ZODIAC_ORDER = ["戌","酉","申","未","午","巳","辰","卯","寅","丑","子","亥"]

def get_zodiac_shift(sign, degree):
    """地支顺逆偏移（翻译 Calculate.getZodiacShift）。
    计算从指定地支到当前度数所在地的偏移量（0-11）。
    用于神煞体系（star_sky_qi_key）计算天干气神煞的顺逆。
    """
    idx = int(normalize_degree(degree) / 30.0) % 12
    for i, z in enumerate(_ZODIAC_ORDER):
        if z == sign:
            gap = idx - i
            if gap < 0:
                gap += 12
            return gap
    return 0

def get_elemental_index(degree):
    """五行索引（翻译 Calculate.getElementalIndex）。
    度数→五行索引（0=火,1=金,2=水,3=月/木...按戌火酉金申水...循环）。
    用于八字系统和规则引擎。
    """
    return int(normalize_degree(degree) / 30.0) % 4

def get_elemental_state_index(degree):
    """五行状态索引（翻译 Calculate.getElementalStateIndex）。
    度数→五行状态索引（0/1/2，对应长生十二运的三组状态）。
    用于八字系统和规则引擎。
    """
    return int(normalize_degree(degree) / 30.0) % 3

# ---------- 弱宫/强宫（空亡）----------

# 60甲子列表（与 moira_s.prop birth_year_names 一致）
_60_JIAZI = [
    "甲子","乙丑","丙寅","丁卯","戊辰","己巳","庚午","辛未","壬申","癸酉",
    "甲戌","乙亥","丙子","丁丑","戊寅","己卯","庚辰","辛巳","壬午","癸未",
    "甲申","乙酉","丙戌","丁亥","戊子","己丑","庚寅","辛卯","壬辰","癸巳",
    "甲午","乙未","丙申","丁酉","戊戌","己亥","庚子","辛丑","壬寅","癸卯",
    "甲辰","乙巳","丙午","丁未","戊申","己酉","庚戌","辛亥","壬子","癸丑",
    "甲寅","乙卯","丙辰","丁巳","戊午","己未","庚申","辛酉","壬戌","癸亥",
]

# 地支名（与 earth_pole_names 一致）
_EARTH_POLES = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

def compute_weak_house(pole, both=False):
    """空亡地支（翻译 ChartData.computeWeakHouse）。
    根据干支在60甲子中的索引，计算空亡地支。
    both=True 返回两个地支，both=False 根据 i%2 返回其中一个。
    用于八字系统和规则引擎(setBirthInfo)。
    """
    for i, name in enumerate(_60_JIAZI):
        if pole == name:
            index = 10 - 2 * (i // 10)
            if both:
                return _EARTH_POLES[index] + _EARTH_POLES[index + 1]
            else:
                if i % 2 == 1:
                    index += 1
                return _EARTH_POLES[index]
    return ""

def get_weak_solid_houses(birth_poles):
    """计算四柱的弱宫（空亡）和强宫。
    birth_poles: ["甲子","丙寅","戊午","壬子"] 形式的四柱。
    返回 {"weak_houses": ["戌","午",...], "solid_houses": ["子","寅",...]}。
    """
    weak_houses = []
    solid_houses = []
    for pole in birth_poles:
        weak_houses.append(compute_weak_house(pole, False))
        solid_houses.append(pole[1] if len(pole) > 1 else "")
    return {"weak_houses": weak_houses, "solid_houses": solid_houses}

def get_weak_house_label(house, weak_houses):
    """检查地支是否在空亡列表中（翻译 ChartData.getWeakHouse）。
    返回 "虚" 或 ""。
    """
    if house in weak_houses:
        return "虚"
    return ""

def get_solid_house_label(house, solid_houses):
    """检查地支是否在强宫列表中（翻译 ChartData.getSolidHouse）。
    返回 "实" 或 ""。
    """
    if house in solid_houses:
        return "实"
    return ""

# ---------- 神煞完整体系（翻译 ChartData.getStarSigns）----------

import os as _os
_SHEN_SHA_DATA = None

def _load_shen_sha():
    """加载神煞完整数据（从 shen_sha_complete.json）。"""
    global _SHEN_SHA_DATA
    if _SHEN_SHA_DATA is None:
        _path = _os.path.join(_os.path.dirname(__file__), 'shen_sha_complete.json')
        with open(_path, 'r', encoding='utf-8') as f:
            _SHEN_SHA_DATA = json.load(f)
    return _SHEN_SHA_DATA

def _parse_star_entries(raw):
    """解析 '子:岁殿, 午:游奕' 格式 → ['子:岁殿', '午:游奕']"""
    if not raw:
        return []
    return [x.strip() for x in raw.split(',') if x.strip()]

def _add_star_sign(head, entry, prop_data):
    """翻译 ChartData.addStarSign。
    entry 格式 '子:岁殿'，如果神煞名是 prop key 则展开分组。
    """
    if len(entry) < 3:
        return
    key = entry[2:]
    prefix = entry[:2]
    head.append(entry)
    if key in prop_data:
        group_str = prop_data[key]
        for item in group_str.split(','):
            item = item.strip()
            if item.startswith('+'):
                head.append(prefix + item[1:])
            else:
                head.append(prefix + item)

def get_star_signs(poles, sign_pos=None, day_pole=False, day_birth=True,
                   life_sign_pos=0.0, birth_poles=None):
    """神煞完整体系（翻译 ChartData.getStarSigns）。
    根据四柱干支计算所有神煞，返回 {地支: [神煞名, ...]} 的表。

    poles: 四柱干支 ["甲子","丙寅","戊午","壬子"]
    sign_pos: 行星黄经位置数组（用于卦气计算）
    day_pole: True=用日柱, False=用年柱
    day_birth: True=白天出生（用太阳），False=夜间（用月亮）
    life_sign_pos: 命宫黄经位置（用于年神12宫计算）
    birth_poles: 出生四柱（用于弱宫强宫计算，如果 poles==birth_poles 则计算）

    返回 {"table": {地支: [神煞名]}, "weak_houses": [...], "solid_houses": [...]}
    """
    data = _load_shen_sha()
    YEAR_POLE, MONTH_POLE, DAY_POLE, HOUR_POLE = 0, 1, 2, 3

    main_pole = poles[DAY_POLE if day_pole else YEAR_POLE]
    head = []

    # 1. 长生十二运（根据日柱/年柱的干支查 jiazi_data，取第 long_life_start 个元素作为五行名）
    jiazi_data = data.get('jiazi_data', {})
    long_life_start = int(data.get('long_life_start', '11')) - 1
    if main_pole in jiazi_data:
        year_data = jiazi_data[main_pole].split(', ')
        if long_life_start < len(year_data):
            key = year_data[long_life_start]
            # long_life_pos 格式: "金:4, 木:10, ..."
            ll_pos = data.get('long_life_pos', '')
            twelve_signs = data.get('twelve_signs', '').split(', ')
            long_life_signs = data.get('long_life_signs', '').split(', ')
            for entry in ll_pos.split(', '):
                entry = entry.strip()
                if ':' in entry:
                    elem, n_str = entry.split(':')
                    if elem == key:
                        n = int(n_str)
                        for j in range(12):
                            m = n + j
                            if m >= 12:
                                m -= 12
                            if m < len(twelve_signs) and j < len(long_life_signs):
                                head.append(f"{twelve_signs[m]}:{long_life_signs[j]}")
                        break

    # 2. 干支神煞（60甲子，仅年柱）
    if not day_pole:
        gan_zhi_stars = data.get('gan_zhi_stars', {})
        if main_pole in gan_zhi_stars:
            for entry in _parse_star_entries(gan_zhi_stars[main_pole]):
                _add_star_sign(head, entry, data)

    # 3. 天干神煞（10天干）
    stem_stars = data.get('stem_stars_full', {})
    main_stem = main_pole[0]
    if main_stem in stem_stars:
        for entry in _parse_star_entries(stem_stars[main_stem]):
            _add_star_sign(head, entry, data)

    # 4. 卦气神煞（仅年柱，需要 sign_pos）
    if not day_pole and sign_pos is not None:
        qi_stars = data.get('qi_stars', {})
        sky_pole_names = data.get('sky_pole_names', '').split(', ')
        year_part = main_pole[0]
        qi_key = year_part
        if qi_key in qi_stars:
            qi_str = qi_stars[qi_key]
            # qi_str 格式 "亥:寅"，第一个字是地支，用于计算 shift
            degree = sign_pos[0] if day_birth else sign_pos[1]  # SUN or MOON
            shift = get_zodiac_shift(qi_str[0], degree)
            for i, name in enumerate(sky_pole_names):
                if name == year_part:
                    index = i + shift
                    while index >= len(sky_pole_names):
                        index -= len(sky_pole_names)
                    qi_key2 = sky_pole_names[index]
                    if qi_key2 in qi_stars:
                        str2 = qi_stars[qi_key2]
                        if len(str2) >= 3:
                            head.append(f"{str2[2]}:{data.get('star_sky_qi_key', '卦气')}")
                    break

    # 5. 地支神煞（12地支）
    branch_stars = data.get('branch_stars_full', {})
    main_branch = main_pole[1]
    if main_branch in branch_stars:
        for entry in _parse_star_entries(branch_stars[main_branch]):
            _add_star_sign(head, entry, data)

    # 6. 月支神煞 + 月时神煞（仅年柱）
    if not day_pole and len(poles) > HOUR_POLE and poles[MONTH_POLE]:
        month_branch_stars = data.get('month_branch_stars', {})
        mb = poles[MONTH_POLE][1]
        if mb in month_branch_stars:
            for entry in _parse_star_entries(month_branch_stars[mb]):
                _add_star_sign(head, entry, data)

        month_hour_stars = data.get('month_hour_stars', {})
        hb = poles[HOUR_POLE][1] if poles[HOUR_POLE] else ''
        mh_key = f"{mb}{hb}"
        if mh_key in month_hour_stars:
            for entry in _parse_star_entries(month_hour_stars[mh_key]):
                _add_star_sign(head, entry, data)

    # 7. 构建 table: {地支: [神煞名, ...]}
    table = {}
    for val in head:
        if len(val) >= 3:
            pos = val[0]
            field = val[2:]
            if pos not in table:
                table[pos] = []
            table[pos].append(field)

    # 8. 弱宫/强宫 + 年神12宫（仅年柱且 poles==birth_poles）
    weak_houses = []
    solid_houses = []
    if not day_pole and birth_poles is not None and poles == birth_poles:
        for i in range(min(4, len(birth_poles))):
            weak_houses.append(compute_weak_house(birth_poles[i], False))
            solid_houses.append(birth_poles[i][1] if len(birth_poles[i]) > 1 else "")
        _compute_year_sign(poles, table, life_sign_pos, weak_houses, solid_houses, data)

    return {"table": table, "weak_houses": weak_houses, "solid_houses": solid_houses}

def _compute_year_sign(poles, table, life_sign_pos, weak_houses, solid_houses, data):
    """翻译 ChartData.computeYearSign。
    计算12宫年神并加入神煞表。
    """
    year_signs = data.get('birth_year_signs', '').split(', ')
    year_sign_key = data.get('year_sign_key', '星')
    year_sign_data = data.get('year_sign_data', {})
    year_names = data.get('birth_year_names', '').split(', ')

    # 年柱在60甲子中的索引
    y_index = 0
    year_pole = poles[0]
    for i, name in enumerate(year_names):
        if name == year_pole:
            y_index = i
            break

    # 年星计算参数
    year_star_seq = data.get('year_star_seq', '').split(', ')
    year_star_map = [int(x) for x in data.get('year_star_map', '0,9,2,1,4,3,6,5,8,7').split(',')]
    year_star_range = [int(x) for x in data.get('year_star_range', '90,100').split(',')]
    ten_god_mode = int(data.get('ten_god_mode', '0'))

    for i in range(12):
        ys = year_signs[i] if i < len(year_signs) else ''
        ys_key = ys + year_sign_key
        if ys in year_sign_data:
            array = year_sign_data[ys].split(', ')
            if len(array) >= 2:
                index = int(array[0])
                if index > 0:
                    val = _get_year_star(y_index, index, year_star_seq, year_star_map,
                                         year_star_range, ten_god_mode)
                    if ten_god_mode:
                        table[val] = [array[1][1:] + "," + array[1][0]]
                    else:
                        table[val] = [array[1][0] + "," + array[1][1:]]

                    # 12宫弱宫强宫标注
                    house_deg = normalize_degree(life_sign_pos - i * 30.0)
                    house_idx = int(house_deg / 30.0) % 12
                    zodiac_order = ["戌","酉","申","未","午","巳","辰","卯","寅","丑","子","亥"]
                    house = zodiac_order[house_idx]
                    half_house = house[0]
                    weak_label = get_weak_house_label(half_house, weak_houses)
                    solid_label = get_solid_house_label(half_house, solid_houses)
                    str_val = weak_label + solid_label
                    if str_val:
                        str_val += ","
                    str_val = f"({str_val}{val}): {array[2] if len(array) > 2 else ''}"
                    table[ys] = [str_val]

                    # 添加到星宿映射
                    s_key = house[1:] if len(house) > 1 else house
                    s_key += data.get('star_sign_key', '神煞')
                    if s_key not in table:
                        table[s_key] = []
                    table[s_key].append(f"[{ys}]")

def _get_year_star(year, order, year_star_seq, year_star_map, year_star_range, ten_god_mode):
    """翻译 ChartData.getYearStar。"""
    order -= year_star_range[0]
    if ten_god_mode and (year & 1) == 1:
        order = year_star_map[order % 10]
    index = (year + order) % 10
    return year_star_seq[index] if index < len(year_star_seq) else ""

# ---------- 四柱干支计算（翻译 ChartData.chineseCalendar 的干支部分）----------

_SKY_POLE_NAMES = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
_EARTH_POLE_NAMES_LIST = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
_MONTH_SKY_POLE_SHIFTS = [2, 4, 6, 8, 0, 2, 4, 6, 8, 0]
_MONTH_EARTH_POLE_SHIFT = 2
_HOUR_SKY_POLE_SHIFTS = [0, 2, 4, 6, 8, 0, 2, 4, 6, 8]
_HOUR_EARTH_POLE_SHIFT = 0
# day_pole_base: 1971年8月7日 = 甲子日（60甲子索引0）
_DAY_POLE_BASE = [1971, 8, 7]

def _days_between(y1, m1, d1, y2, m2, d2):
    """计算两个日期之间的天数差（y2-m2-d2 减 y1-m1-d1）。"""
    import datetime
    d_start = datetime.date(y1, m1, d1)
    d_end = datetime.date(y2, m2, d2)
    return (d_end - d_start).days

def calc_four_poles(year, month, day, hour_ut, solar_cal=None, use_solar_terms=True):
    """计算四柱干支（翻译 ChartData.chineseCalendar 的干支部分）。
    返回 ["年柱","月柱","日柱","时柱"]。

    year/month/day: 公历
    hour_ut: UT 小数
    solar_cal: [chinese_year_num, lunar_month] 或 None（自动计算）
    use_solar_terms: True=节气分年月（果老星宗/传统八字），False=农历分年月（琴堂派）
    """
    data = _load_shen_sha()
    year_names = data.get('birth_year_names', '').split(', ')

    # 时辰：23:00 后算下一日的时柱天干
    hour_local = hour_ut + 8.0  # UT → 北京时间
    if hour_local >= 24:
        hour_local -= 24
        # 日期+1
        import datetime
        next_day = datetime.date(year, month, day) + datetime.timedelta(days=1)
        year, month, day = next_day.year, next_day.month, next_day.day

    adj_hour = int(hour_local)
    adj_min = int((hour_local % 1) * 60)

    if use_solar_terms:
        # 节气分年月（果老星宗/传统八字标准）
        # 节气基于回归黄道，不是恒星黄道
        import swisseph as _swe
        jd = jd_from_ymd_ut(year, month, day, hour_ut)
        # 用回归黄道计算太阳位置（节气用回归黄道）
        sun_result = _swe.calc_ut(jd, _swe.SUN, _swe.FLG_SWIEPH)
        sun_lon = sun_result[0][0]  # 回归黄道经度

        # 年柱：以立春(315°)为界
        # 立春前(小寒285°到立春315°之间)=前一年，立春后=本年
        if 270 <= sun_lon < 315:
            solar_year = year - 1
        else:
            solar_year = year

        # 月柱地支：寅=315-345, 卯=345-15, ..., 丑=285-315
        # 节气月序号：寅=0(立春), 卯=1(惊蛰), ..., 丑=11(小寒)
        month_branch_idx = int(((sun_lon - 315) % 360) / 30)
        # 月柱地支
        month_branches_solar = ["寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子", "丑"]
        month_earth = month_branches_solar[month_branch_idx]

        # 年柱：1984=甲子年(year_names[0])
        offset = (solar_year - 1984) % 60
        year_pole = year_names[offset]

        # 月柱天干：五虎遁
        year_stem = year_pole[0]
        y_idx = _SKY_POLE_NAMES.index(year_stem) if year_stem in _SKY_POLE_NAMES else 0
        # 寅月天干起于：甲己年丙寅, 乙庚年戊寅, 丙辛年庚寅, 丁壬年壬寅, 戊癸年甲寅
        # _MONTH_SKY_POLE_SHIFTS已编码此规则
        m1 = (month_branch_idx + _MONTH_SKY_POLE_SHIFTS[y_idx]) % 10
        # 月柱地支：寅=0, 卯=1, ..., 丑=11
        # 需要映射到_EARTH_POLE_NAMES_LIST的索引：子=0, 丑=1, ..., 亥=11
        earth_map = {"寅":2, "卯":3, "辰":4, "巳":5, "午":6, "未":7, "申":8, "酉":9, "戌":10, "亥":11, "子":0, "丑":1}
        m2 = earth_map[month_earth]
        month_pole = _SKY_POLE_NAMES[m1] + month_earth
    else:
        # 农历分年月（原实现，琴堂派）
        if solar_cal is None:
            lunar = solar_to_lunar(year, month, day, hour_ut)
            if lunar is None:
                return ["", "", "", ""]
            solar_cal = [lunar.get('chinese_year_num', 1), lunar.get('lunar_month', 1)]

        # 年柱
        offset = solar_cal[0] - 1
        year_pole = year_names[offset % len(year_names)]

        # 月柱
        year_stem = year_pole[0]
        y_idx = _SKY_POLE_NAMES.index(year_stem) if year_stem in _SKY_POLE_NAMES else 0
        month_index = solar_cal[1] - 1
        m1 = (month_index + _MONTH_SKY_POLE_SHIFTS[y_idx]) % 10
        m2 = (month_index + _MONTH_EARTH_POLE_SHIFT) % 12
        month_pole = _SKY_POLE_NAMES[m1] + _EARTH_POLE_NAMES_LIST[m2]

    # 日柱（基于 day_pole_base 的天数差）
    day_offset = _days_between(_DAY_POLE_BASE[0], _DAY_POLE_BASE[1], _DAY_POLE_BASE[2],
                               year, month, day)
    day_pole = year_names[day_offset % len(year_names)]

    # 时柱
    day_stem = day_pole[0]
    y2 = _SKY_POLE_NAMES.index(day_stem) if day_stem in _SKY_POLE_NAMES else 0
    # 果老星宗/传统八字用早子时：23-0时属于当日子时，不用次日天干
    # （晚子时0-1时已在上面hour_local>=24时跨日处理）
    hour_index = ((adj_hour + 1) // 2) % 12  # 子时=0, 丑时=1, ..., 亥时=11
    h1 = (hour_index + _HOUR_SKY_POLE_SHIFTS[y2]) % 10
    h2 = (hour_index + _HOUR_EARTH_POLE_SHIFT) % 12
    hour_pole = _SKY_POLE_NAMES[h1] + _EARTH_POLE_NAMES_LIST[h2]

    return [year_pole, month_pole, day_pole, hour_pole]

# ---------- 八字系统（翻译 ChartData.computeEightCharData 核心计算）----------

def get_ten_god_name(name, day_name, plus=False):
    """十神名（翻译 ChartData.getTenGodName）。
    name: 天干, day_name: 日柱天干
    返回十神名（比肩/劫财/食神/伤官/偏财/正财/七杀/正官/偏印/正印）
    """
    data = _load_shen_sha()
    sky_pole_names = data.get('sky_pole_names', '甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬, 癸').split(', ')
    ten_god_seq1 = data.get('ten_god_seq1', '比肩, 劫财, 食神, 伤官, 偏财, 正财, 七杀, 正官, 偏印, 正印').split(', ')
    ten_god_seq2 = data.get('ten_god_seq2', '劫财, 比肩, 伤官, 食神, 正财, 偏财, 正官, 七杀, 正印, 偏印').split(', ')

    i = sky_pole_names.index(name) if name in sky_pole_names else 0
    j = sky_pole_names.index(day_name) if day_name in sky_pole_names else 0
    index = i - 2 * (j // 2)
    if index < 0:
        index += 10
    if (j % 2) == 0:
        str_val = ten_god_seq1[index] if index < len(ten_god_seq1) else ""
    else:
        str_val = ten_god_seq2[index] if index < len(ten_god_seq2) else ""
    return str_val

def get_long_life_name(name, day_name):
    """长生十二运名（翻译 ChartData.getLongLifeName）。
    name: 地支, day_name: 日柱天干
    返回长生十二运阶段名（长生/养/胎/绝/墓/死/病/衰/帝旺/临官/冠带/沐浴）
    """
    data = _load_shen_sha()
    earth_pole_names = data.get('earth_pole_names', '子, 丑, 寅, 卯, 辰, 巳, 午, 未, 申, 酉, 戌, 亥').split(', ')
    sky_pole_names = data.get('sky_pole_names', '甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬, 癸').split(', ')
    long_life_signs = data.get('long_life_signs', '长生, 养, 胎, 绝, 墓, 死, 病, 衰, 帝旺, 临官, 冠带, 沐浴').split(', ')
    day_pole_long_life_seq = [int(x) for x in data.get('day_pole_long_life_seq', '11, 6, 2, 3, 2, 3, 5, 0, 8, 9').split(',')]

    i = earth_pole_names.index(name) if name in earth_pole_names else 0
    j = sky_pole_names.index(day_name) if day_name in sky_pole_names else 0
    dir_val = -1 if (j % 2) == 0 else 1
    index = day_pole_long_life_seq[j] + dir_val * i
    while index < 0:
        index += 12
    while index >= 12:
        index -= 12
    return long_life_signs[index] if index < len(long_life_signs) else ""

def get_year_sound_name(name):
    """纳音名（翻译 ChartData.getYearSoundName）。
    name: 干支（如"甲子"）
    返回纳音五行名（如"海中金"）
    """
    data = _load_shen_sha()
    na_yin = data.get('na_yin_60_detail', {})
    return na_yin.get(name, "")

def get_earth_god_seq(name):
    """地支藏干（翻译 ChartData.getEarthGodSeq）。
    name: 地支
    返回藏干字符串（如"癸辛己"）
    """
    data = _load_shen_sha()
    earth_god_seq = data.get('earth_god_seq', '').split(', ')
    for entry in earth_god_seq:
        if ':' in entry:
            branch, gods = entry.split(':', 1)
            if branch == name:
                return gods
    return ""

def get_birth_season(birth_date_arr, ephe_path="ephe"):
    """出生季节（翻译 ChartData.getBirthSeason）。
    根据出生日期判断在哪个节气区间。
    返回节气名。
    """
    y, mo, d = birth_date_arr[0], birth_date_arr[1], birth_date_arr[2]
    data = _load_shen_sha()
    season_starts = data.get('season_starts', '').split(', ')
    solar_terms = calc_solar_terms_v2(y, ephe_path=ephe_path)
    if not solar_terms:
        return ""
    jd = jd_from_ymd_ut(y, mo, d, birth_date_arr[3] if len(birth_date_arr) > 3 else 0.0)
    # 找到当前 jd 在哪个节气之后
    for i, term in enumerate(solar_terms):
        if jd < term['jd']:
            # 当前在 term[i-1] 和 term[i] 之间
            prev_idx = (i - 1 + 24) % 24
            return season_starts[prev_idx]
    return season_starts[-1] if season_starts else ""

def compute_eight_char_data(four_poles, birth_date_arr=None, ephe_path="ephe"):
    """八字数据（翻译 ChartData.computeEightCharData 核心计算部分）。
    返回四柱的完整八字信息：长生/十神/纳音/藏干/弱宫强宫。

    four_poles: ["年柱","月柱","日柱","时柱"]
    birth_date_arr: [年,月,日,时,分]（用于季节判断）
    """
    day_pole_key = four_poles[2][0]  # 日柱天干

    result = {
        "four_poles": four_poles,
        "day_master": day_pole_key,  # 日主
        "poles": [],
    }

    # 四柱各自的详细信息
    for i, pole in enumerate(four_poles):
        pole_info = {
            "gan_zhi": pole,
            "stem": pole[0],  # 天干
            "branch": pole[1],  # 地支
            "ten_god": get_ten_god_name(pole[0], day_pole_key) if i != 2 else "日主",
            "long_life": get_long_life_name(pole[1], day_pole_key),
            "na_yin": get_year_sound_name(pole),
            "hidden_stems": get_earth_god_seq(pole[1]),
        }
        result["poles"].append(pole_info)

    # 弱宫（空亡）
    weak_both = compute_weak_house(four_poles[2], True)  # 日柱空亡（两个地支）
    result["day_weak_house"] = weak_both

    # 各柱是否在空亡中
    result["weak_pole_flags"] = []
    for pole in four_poles:
        branch = pole[1]
        result["weak_pole_flags"].append(branch in weak_both)

    # 出生季节
    if birth_date_arr:
        result["birth_season"] = get_birth_season(birth_date_arr, ephe_path)

    return result

# ---------- 流年神煞（翻译 ChartData.getYearInfo 数据层）----------

def get_year_info(four_poles, life_sign_pos, use_birth=True, table=None):
    """流年神煞（翻译 ChartData.getYearInfo 数据层）。
    解析 birth_year_info/current_year_info 模板，替换占位符为年星名，
    把结果中的5字符token解析为神煞加入 table。

    four_poles: 四柱干支
    life_sign_pos: 命宫黄经
    use_birth: True=出生年, False=当前年
    table: 神煞表（会被修改）
    返回解析后的年星列表。
    """
    data = _load_shen_sha()
    year_names = data.get('birth_year_names', '').split(', ')
    jiazi_data = data.get('jiazi_data', {})

    # 选择模板
    if use_birth:
        template = data.get('birth_year_info', '')
    else:
        template = data.get('current_year_info', '')

    # 年柱在60甲子中的索引
    year_pole = four_poles[0]
    y_index = 0
    for i, name in enumerate(year_names):
        if name == year_pole:
            y_index = i
            break

    # year_data: 60甲子对应的数据
    year_data = jiazi_data.get(year_pole, '').split(', ')

    # 替换模板中的编号占位符（01-20）
    import re
    result_str = template
    for i in range(len(year_data)):
        field = f"{i+1:02d}"
        val = year_data[i] if i < len(year_data) else ""
        result_str = result_str.replace(field, val, 1)

    # 替换年星占位符（90-99）
    year_star_seq = data.get('year_star_seq', '').split(', ')
    year_star_map = [int(x) for x in data.get('year_star_map', '0,9,2,1,4,3,6,5,8,7').split(',')]
    year_star_range = [int(x) for x in data.get('year_star_range', '90,100').split(',')]
    ten_god_mode = int(data.get('ten_god_mode', '0'))

    year_stars = {}
    for i in range(year_star_range[0], year_star_range[1]):
        field = f"{i:02d}"
        val = _get_year_star(y_index, i, year_star_seq, year_star_map,
                             year_star_range, ten_god_mode)
        year_stars[field] = val
        result_str = result_str.replace(field, val)

    # 解析5字符token为神煞，加入 table
    star_sign_key = data.get('star_sign_key', '神煞')
    ten_god_list = data.get('ten_god_list_org', '比肩, 劫财, 食神, 伤官, 偏财, 正财, 七杀, 正官, 偏印, 正印').split(', ')

    parsed_stars = []
    tokens = re.split(r'[$%| ]', result_str)
    for token in tokens:
        token = token.strip()
        if len(token) == 5:
            # token 格式: "XX地支Y" → val=token[0:2], pos=token[3], star_sign_key
            val = token[:2]
            pos = token[3]
            s_key = pos + star_sign_key
            if table is not None:
                if s_key not in table:
                    table[s_key] = []
                if val not in table[s_key]:
                    if val in ten_god_list:
                        table[s_key].insert(0, val)
                    else:
                        table[s_key].append(val)
            parsed_stars.append({"value": val, "position": pos})

    return {
        "year_stars": year_stars,
        "parsed_stars": parsed_stars,
        "template_filled": result_str,
    }

# ---------- 流年推演（翻译 ChartData.computeNowData）----------

def compute_now_data(birth_year, age, birth_poles=None, life_sign_pos=0.0):
    """流年推演（翻译 ChartData.computeNowData）。
    根据出生年和当前年龄，计算流年的四柱干支和神煞。

    birth_year: 出生年份
    age: 当前年龄（虚岁）
    birth_poles: 出生四柱（用于计算弱宫强宫，可选）
    life_sign_pos: 命宫黄经位置（用于年神12宫计算）

    返回 {year_pole, four_poles, star_signs}
    """
    data = _load_shen_sha()
    year_names = data.get('birth_year_names', '').split(', ')

    # 年柱索引 = 出生年 + age - 1（虚岁）
    # 需要找到出生年对应的60甲子索引
    # 1984年=甲子年=索引0，所以 year_index = (birth_year - 1984) % 60
    birth_index = (birth_year - 1984) % 60
    now_index = (birth_index + age - 1) % 60
    year_pole = year_names[now_index] if now_index < len(year_names) else ""

    # 构建流年四柱（简化版：只有年柱，月日时柱需要完整农历计算）
    # 这里用出生四柱作为占位，实际应计算当前年的四柱
    four_poles = [year_pole, "", "", ""]
    if birth_poles:
        # 月日时柱暂时用出生的（实际应重新计算）
        four_poles = [year_pole, birth_poles[1], birth_poles[2], birth_poles[3]]

    # 计算流年神煞
    star_signs_result = get_star_signs(
        four_poles, sign_pos=None, day_pole=False,
        day_birth=True, life_sign_pos=life_sign_pos,
        birth_poles=None)  # 流年不计算弱宫强宫

    # 流年年星
    year_info = get_year_info(four_poles, life_sign_pos, use_birth=False,
                              table=star_signs_result["table"])

    return {
        "age": age,
        "year_pole": year_pole,
        "four_poles": four_poles,
        "star_signs": {
            "table": star_signs_result["table"],
            "weak_houses": star_signs_result["weak_houses"],
            "solid_houses": star_signs_result["solid_houses"],
        },
        "year_info": year_info,
    }

# ---------- 限运系统（翻译 ChartData.getChildLimit/getSmallLimit/getMonthLimit/getFlyLimit）----------

def get_child_limit(cur_age, sep=":"):
    """童限（翻译 ChartData.getChildLimit）。
    根据年龄返回童限所在宫位。
    """
    data = _load_shen_sha()
    child_seq = [int(x) for x in data.get('child_seq', '0, 1, 7, 6,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0').replace(' ', '').split(',')]
    child_limit_label = data.get('child_limit', '童限')

    cur_age = min(cur_age, len(child_seq) - 1)
    if cur_age < 0:
        return ""

    # 需要命宫位置，这里用参数传入或从全局获取
    # 简化版：返回标签+偏移量
    offset = child_seq[cur_age] if cur_age < len(child_seq) else 0
    return f"{child_limit_label}{sep}{offset}"

def get_child_limit_with_pos(cur_age, life_sign_pos, sep=":"):
    """童限（带命宫位置计算）。
    返回童限所在宫位的地支。
    """
    data = _load_shen_sha()
    child_seq = [int(x) for x in data.get('child_seq', '0, 1, 7, 6,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0').replace(' ', '').split(',')]
    child_limit_label = data.get('child_limit', '童限')

    cur_age = min(cur_age, len(child_seq) - 1)
    if cur_age < 0:
        return ""

    offset = child_seq[cur_age] if cur_age < len(child_seq) else 0
    pos = normalize_degree(life_sign_pos + 30.0 * offset)
    zodiac = _lon_to_zodiac_name(pos)
    return f"{child_limit_label}{sep}{zodiac}"

def get_small_limit(cur_age, life_sign_pos, sep=":"):
    """小限（翻译 ChartData.getSmallLimit）。
    从命宫开始，每年逆行一个宫位。
    """
    data = _load_shen_sha()
    small_limit_label = data.get('small_limit', '小限')

    pos = normalize_degree(life_sign_pos + (cur_age - 1) * 30.0)
    zodiac = _lon_to_zodiac_name(pos)
    return f"{small_limit_label}{sep}{zodiac}"

def get_month_limit(cur_age, life_sign_pos, now_lunar_month, birth_lunar_month, sep=":"):
    """月限（翻译 ChartData.getMonthLimit）。
    """
    data = _load_shen_sha()
    month_limit_label = data.get('month_limit', '月限')

    index = now_lunar_month - birth_lunar_month
    if index < 0:
        index += 12
        index += cur_age - 2  # 用去年的小限作为基础
    else:
        index += cur_age - 1

    pos = normalize_degree(life_sign_pos + index * 30.0)
    zodiac = _lon_to_zodiac_name(pos)
    return f"{month_limit_label}{sep}{zodiac}"

def get_fly_limit(cur_age, life_sign_pos, child_age_limit, sep=":"):
    """飞限（翻译 ChartData.getFlyLimit）。
    """
    data = _load_shen_sha()
    fly_limit_label = data.get('fly_limit', '飞限')
    each_half_year = data.get('each_half_year', '各半年')

    fly_seq_yang1 = [int(x) for x in data.get('fly_seq_yang1', '0, 0, 6, 6, 8, 4').replace(' ', '').split(',')]
    fly_seq_ying1 = [int(x) for x in data.get('fly_seq_ying1', '0, 0, 6, 6, 4, 8').replace(' ', '').split(',')]
    fly_seq_yang2 = [int(x) for x in data.get('fly_seq_yang2', '').replace(' ', '').split(',') if x.strip()]
    fly_seq_ying2 = [int(x) for x in data.get('fly_seq_ying2', '').replace(' ', '').split(',') if x.strip()]
    fly_seq_half_shift = [int(x) for x in data.get('fly_seq_half_shift', '66, 71, 75, 88').split(',')]

    index = int(life_sign_pos / 30.0)
    result = f"{fly_limit_label}{sep}"

    if 0 <= cur_age < child_age_limit:
        fly_seq = fly_seq_yang1 if (index % 2) == 0 else fly_seq_ying1
        pos = normalize_degree(life_sign_pos + 30.0 * fly_seq[cur_age % len(fly_seq)])
        result += _lon_to_zodiac_name(pos)
    elif cur_age >= child_age_limit:
        cur_age -= child_age_limit
        fly_seq = fly_seq_yang2 if (index % 2) == 0 else fly_seq_ying2
        if cur_age + 2 < len(fly_seq):
            last_index, cur_index = 0, 0
            if fly_seq_half_shift[0] <= cur_age < fly_seq_half_shift[1]:
                last_index = fly_seq[cur_age]
                cur_index = fly_seq[cur_age + 1]
            elif fly_seq_half_shift[2] <= cur_age < fly_seq_half_shift[3]:
                last_index = fly_seq[cur_age + 1]
                cur_index = fly_seq[cur_age + 2]
            elif cur_age >= fly_seq_half_shift[1]:
                last_index = cur_index = fly_seq[cur_age + 1]
            else:
                last_index = cur_index = fly_seq[cur_age]

            if last_index != cur_index:
                pos1 = normalize_degree(life_sign_pos + 30.0 * last_index)
                pos2 = normalize_degree(life_sign_pos + 30.0 * cur_index)
                result += _lon_to_zodiac_name(pos1) + _lon_to_zodiac_name(pos2) + each_half_year
            else:
                pos = normalize_degree(life_sign_pos + 30.0 * cur_index)
                result += _lon_to_zodiac_name(pos)
        else:
            return ""
    else:
        return ""

    return result

def _lon_to_zodiac_name(lon):
    """黄经 → 地支名（单字，如"戌"）。"""
    return _lon_to_branch(lon)

def compute_limits(life_sign_pos, age, lunar_date=None, now_lunar_month=None):
    """计算所有限运（童限/小限/月限/飞限）。
    life_sign_pos: 命宫黄经
    age: 当前虚岁
    lunar_date: [年, 月, 日] 农历日期
    now_lunar_month: 当前农历月
    """
    data = _load_shen_sha()
    child_seq = [int(x) for x in data.get('child_seq', '0, 1, 7, 6,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0').replace(' ', '').split(',')]
    child_age_limit = len(child_seq) - 1  # 童限年龄上限

    result = {
        "child_limit": get_child_limit_with_pos(age, life_sign_pos),
        "small_limit": get_small_limit(age, life_sign_pos),
        "fly_limit": get_fly_limit(age - 1, life_sign_pos, child_age_limit),
    }

    if lunar_date and now_lunar_month:
        birth_lunar_month = lunar_date[1] if len(lunar_date) > 1 else 1
        result["month_limit"] = get_month_limit(age, life_sign_pos, now_lunar_month, birth_lunar_month)

    return result

# ---------- 纳音五行 ----------

def calc_na_yin(gan_zhi):
    """根据干支（如'甲子'）查询纳音五行。
    返回 {na_yin: 纳音名, element: 五行}
    """
    c = _c()
    na_yin = c["na_yin_60"].get(gan_zhi)
    if na_yin is None:
        return {"na_yin": None, "element": None}
    # 纳音最后一个字是五行
    element = na_yin[-1] if na_yin else None
    return {"na_yin": na_yin, "element": element}

def calc_na_yin_from_year(year):
    """根据年份查询纳音五行（年命）。
    返回 {gan_zhi, na_yin, element}
    """
    chinese_year_num = _get_chinese_year(year)
    gan_zhi = _gan_zhi_name(chinese_year_num)
    result = calc_na_yin(gan_zhi)
    result["gan_zhi"] = gan_zhi
    return result

# ---------- 十干化曜 ----------

def calc_ten_god_transform(stem):
    """根据天干查询化曜星。
    stem: 天干名（甲/乙/.../癸）
    返回 {org_name: 传统名, alt_name: 替代名}
    """
    c = _c()
    tg = c["ten_god_transform"]
    org = tg["stem_mapping"].get(stem)
    if org is None:
        return {"org_name": None, "alt_name": None}
    # 找到 org_name 在 org_names 中的索引，对应 alt_names
    try:
        idx = tg["org_names"].index(org)
        alt = tg["alt_names"][idx] if idx < len(tg["alt_names"]) else None
    except ValueError:
        alt = None
    return {"org_name": org, "alt_name": alt}

# ---------- 天干吉凶星曜 ----------

def calc_stem_stars(stem, branch):
    """根据天干×地支查询吉凶星曜。
    返回 [星曜名列表]（同一地支可能有多个星曜）
    """
    c = _c()
    stem_data = c["stem_stars"].get(stem)
    if stem_data is None:
        return []
    # stem_stars 是 [[branch, star], ...] 列表格式
    matched = []
    for entry in stem_data:
        b, s = entry[0], entry[1]
        if b == branch:
            matched.append(s)
    return matched

def calc_stem_stars_from_branch(stem, branch):
    """根据天干×地支查询吉凶星曜（同 calc_stem_stars）。"""
    return calc_stem_stars(stem, branch)

# ---------- 地支神煞 ----------

def calc_branch_stars(year_branch, target_branch):
    """根据年支查询某地支上的神煞。
    year_branch: 年支（子/丑/.../亥）
    target_branch: 目标地支
    返回 [神曜名列表]
    """
    c = _c()
    branch_data = c["branch_stars"].get(year_branch)
    if branch_data is None:
        return []
    matched = []
    for entry in branch_data:
        b, star = entry[0], entry[1]
        if b == target_branch:
            matched.append(star)
    return matched

def calc_branch_stars_for_all(year_branch):
    """根据年支查询所有地支的神煞。
    返回 dict[branch] = [神曜名列表]
    """
    c = _c()
    branch_data = c["branch_stars"].get(year_branch)
    if branch_data is None:
        return {}
    result = {}
    for entry in branch_data:
        b, star = entry[0], entry[1]
        if b not in result:
            result[b] = []
        result[b].append(star)
    return result

# ---------- 命理格局规则引擎 ----------

def load_rules_library():
    """加载命理格局规则库。
    返回 [rule_dict, ...]，每条规则含 id/sign/name/priority/condition/excludes/comment
    """
    import json, os
    rules_path = os.path.join(os.path.dirname(__file__), "rules_library.json")
    with open(rules_path, encoding="utf-8") as f:
        return json.load(f)

def _build_symbol_table(chart_data):
    """从星盘 JSON 构建规则引擎符号表。
    将星盘数据转换为规则引擎可用的变量字典。
    """
    bodies = chart_data.get("bodies", {})
    houses = chart_data.get("houses", {})
    lunar = chart_data.get("lunar", {})
    rise_set = chart_data.get("rise_set", {})
    dignities = chart_data.get("dignities", {})
    mansions = chart_data.get("mansions", {})

    # 地支顺序（戌=0°开始逆序）
    branch_order = ["戌","酉","申","未","午","巳","辰","卯","寅","丑","子","亥"]
    zodiac_names = ["戌宫","酉宫","申宫","未宫","午宫","巳宫","辰宫","卯宫","寅宫","丑宫","子宫","亥宫"]

    sym = {}
    # 行星黄道星座（地支）— 同时用英文和中文名
    cn_names = {
        "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
        "mercury": "水", "mars": "火", "saturn": "土",
        "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
        "mean_apog_ziqi": "炁", "mean_apog_yuebei": "孛",
    }
    for name, data in bodies.items():
        if "lon" not in data:
            continue
        lon = data["lon"]
        branch = _lon_to_branch(lon)
        zodiac_idx = int(normalize_degree(lon) / 30.0) % 12
        zodiac_val = zodiac_names[zodiac_idx]
        elem = _planet_element(name)
        # 英文名
        sym[f"@{name}"] = zodiac_val
        sym[f"@{name}[0]"] = branch
        sym[f"@{name}[1]"] = elem
        sym[f"${name}_degree"] = str(round(lon, 2))
        # 中文名（规则库用中文名）
        cn = cn_names.get(name)
        if cn:
            sym[f"@{cn}"] = zodiac_val
            sym[f"@{cn}[0]"] = branch
            sym[f"@{cn}[1]"] = elem
            sym[f"${cn}_degree"] = str(round(lon, 2))
        # 庙旺状态
        dig = dignities.get(name, {})
        if dig.get("states"):
            for s in dig["states"]:
                sym[f"?{name}_{s}"] = "t"
                if cn:
                    sym[f"?{cn}{s}"] = "t"  # 如 ?日垣, ?月庙
        # 宿度
        man = mansions.get(name, {})
        if man.get("mansion"):
            sym[f"%{name}[0]"] = man["mansion"]
            if cn:
                sym[f"%{cn}[0]"] = man["mansion"]

    # 命宫/身宫
    life_sign = chart_data.get("life_sign")
    self_sign = chart_data.get("self_sign")
    if life_sign is not None:
        life_branch = _lon_to_branch(life_sign)
        sym["@命"] = zodiac_names[int(normalize_degree(life_sign) / 30.0) % 12]
        sym["@命[0]"] = life_branch
        sym["@命[1]"] = _planet_element_by_branch(life_branch)
        sym["@命宫"] = sym["@命"]
    if self_sign is not None:
        self_branch = _lon_to_branch(self_sign)
        sym["@身"] = zodiac_names[int(normalize_degree(self_sign) / 30.0) % 12]
        sym["@身[0]"] = self_branch
        sym["@身[1]"] = _planet_element_by_branch(self_branch)

    # 12宫位变量（@官禄/@福德等）在下方 year_signs_list 循环中统一设置

    # 昼夜
    is_day = rise_set.get("is_day_birth", True)
    sym["?昼"] = "t" if is_day else "f"
    sym["?夜"] = "f" if is_day else "t"

    # 季节（根据出生月份粗略判断）
    month = chart_data.get("input", {}).get("date_ut", "")[5:7]
    try:
        m = int(month)
    except (ValueError, TypeError):
        m = 0
    sym["?春"] = "t" if m in (2, 3, 4) else "f"
    sym["?夏"] = "t" if m in (5, 6, 7) else "f"
    sym["?秋"] = "t" if m in (8, 9, 10) else "f"
    sym["?冬"] = "t" if m in (11, 12, 1) else "f"

    # 农历
    sym["$lunar_year"] = str(lunar.get("lunar_year", ""))
    sym["$lunar_month"] = str(lunar.get("lunar_month", ""))
    sym["$lunar_day"] = str(lunar.get("lunar_day", ""))
    sym["?leap_month"] = "t" if lunar.get("is_leap") else "f"

    # === setBirthInfo 符号（翻译 EvalRule.setBirthInfo）===
    ss_data = _load_shen_sha()
    four_poles = chart_data.get("four_poles")
    star_signs = chart_data.get("star_signs", {})
    eight_char = chart_data.get("eight_char", {})

    if four_poles:
        # 四柱干支: $年柱, $月柱, $日柱, $时柱
        pole_labels = ['年','月','日','时']
        for i, label in enumerate(pole_labels):
            sym[f"${label}柱"] = four_poles[i]

        # 季节（根据月支计算）
        month_branch = four_poles[1][1]
        earth_pole_names = ss_data.get('earth_pole_names', '子, 丑, 寅, 卯, 辰, 巳, 午, 未, 申, 酉, 戌, 亥').split(', ')
        if month_branch in earth_pole_names:
            mb_idx = earth_pole_names.index(month_branch)
            season_val = (mb_idx - 2) % 12 // 3
            sym["$季节"] = str(season_val)
            four_seasons = ss_data.get('four_seasons', '春, 夏, 秋, 冬').split(', ')
            if season_val < len(four_seasons):
                sym[f"?{four_seasons[season_val]}"] = "t"

        # 昼夜
        is_day = rise_set.get("is_day_birth", True)
        daytime = ss_data.get('daytime', '昼')
        nighttime = ss_data.get('nighttime', '夜')
        sym[f"?{daytime}"] = "t" if is_day else "f"
        sym[f"?{nighttime}"] = "f" if is_day else "t"

        # 12宫年神 + 弱宫强宫
        year_signs_list = ss_data.get('birth_year_signs', '').split(', ')
        full_zodiac = ss_data.get('full_zodiac', '').split(', ')
        zodiac_house = ss_data.get('zodiac_house', '宫')
        if life_sign is not None:
            val = int(normalize_degree(life_sign) / 30.0)
            for i in range(min(12, len(year_signs_list))):
                n = val - i
                if n < 0:
                    n += 12
                if n < len(full_zodiac):
                    fz = full_zodiac[n]
                    sym[f"@{year_signs_list[i]}"] = fz
                    if len(fz) >= 2:
                        sym[f"@{year_signs_list[i]}[0]"] = fz[0]
                        sym[f"@{year_signs_list[i]}[1]"] = fz[1]
                    if len(fz) > 0:
                        sym[f"${fz[0]}{zodiac_house}"] = year_signs_list[i]

        # 弱宫/强宫标记
        weak_houses = star_signs.get("weak_houses", [])
        solid_houses = star_signs.get("solid_houses", [])
        weak_label = ss_data.get('weak', '虚')
        solid_label = ss_data.get('solid', '实')
        for i in range(min(12, len(full_zodiac))):
            key = full_zodiac[i][0] if full_zodiac else ""
            if key in weak_houses:
                sym[f"?{weak_label}{key}"] = "t"
            if key in solid_houses:
                sym[f"?{solid_label}{key}"] = "t"

        # 神煞表 → ?神煞名 标记 + @神煞名 地支变量
        star_table = star_signs.get("table", {})
        for pos, stars in star_table.items():
            for star in stars:
                if isinstance(star, str) and len(star) > 0:
                    sym[f"?{star}"] = "t"
                    # 为格局规则需要的神煞创建 @变量（地支+五行）
                    special_stars = ("紫微", "禄勋", "驿马", "岁驾", "岁殿",
                                     "斗杓", "唐符", "国印", "卦气", "长生",
                                     "帝旺", "华盖", "天贵", "玉贵", "天厨",
                                     "文昌", "天德", "红鸾", "解神", "血刃")
                    if star in special_stars and pos:
                        branch = pos[0] if len(pos) > 0 else pos
                        elem = _planet_element_by_branch(branch)
                        sym[f"@{star}"] = f"{branch}{elem}"
                        sym[f"@{star}[0]"] = branch
                        sym[f"@{star}[1]"] = elem

        # 八字十神/纳音/长生
        if eight_char.get("poles"):
            for i, pole_info in enumerate(eight_char["poles"]):
                label = pole_labels[i] if i < 4 else f"pole{i}"
                sym[f"${label}十神"] = pole_info.get("ten_god", "")
                sym[f"${label}纳音"] = pole_info.get("na_yin", "")
                sym[f"${label}长生"] = pole_info.get("long_life", "")
                sym[f"${label}藏干"] = pole_info.get("hidden_stems", "")

        # 命主/身主
        life_master = ss_data.get('life_master', '命主')
        self_master = ss_data.get('self_master', '身主')
        if life_sign is not None:
            life_master_key = life_master[0] if life_master else ""
            sym[f"@{life_master_key}"] = sym.get("@命", "")
        if self_sign is not None:
            self_master_key = self_master[0] if self_master else ""
            sym[f"@{self_master_key}"] = sym.get("@身", "")

        # 难仇恩用（life_helper_key）
        # Java: sign = cal.getStarSign(life_sign_pos, stellar_sign_pos, full_stellar_signs)
        # sign 是28宿名（如"昴日"），sign.substring(1) 取五行属性（如"日"）
        life_helper_key = ss_data.get('life_helper_key', '难仇恩用')
        life_helper_data = ss_data.get('life_helper_data', {})
        if life_sign is not None:
            # 找到命宫所在的28宿
            stellar_sign = _get_stellar_sign(life_sign, chart_data)
            if stellar_sign and len(stellar_sign) >= 2:
                star_elem = stellar_sign[1]  # 五行属性
                if star_elem in life_helper_data:
                    helpers = life_helper_data[star_elem].split(', ')
                    for i, h in enumerate(life_helper_key):
                        if i < len(helpers):
                            sym[f"${h}度"] = helpers[i]
                # 也设置宫位版本
                life_branch = _lon_to_branch(life_sign)
                if life_branch in life_helper_data:
                    helpers = life_helper_data[life_branch].split(', ')
                    for i, h in enumerate(life_helper_key):
                        if i < len(helpers):
                            sym[f"${h}宫"] = helpers[i]

        # 农历闰月
        if lunar.get("is_leap"):
            leap = ss_data.get('leap', '闰')
            month_char = ss_data.get('month_char', '月')
            sym[f"?{leap}{month_char}"] = "t"

        # 晦朔/弦望
        lunar_day = lunar.get("lunar_day", 0)
        try:
            lunar_day = int(lunar_day)
        except (ValueError, TypeError):
            lunar_day = 0
        lf1_range = [int(x) for x in ss_data.get('lunar_face_1_range', '26, 5').split(',')]
        lf2_range = [int(x) for x in ss_data.get('lunar_face_2_range', '11, 20').split(',')]
        if lf1_range[0] > lf1_range[1]:
            b_val = lunar_day >= lf1_range[0] or lunar_day <= lf1_range[1]
        else:
            b_val = lunar_day >= lf1_range[0] and lunar_day <= lf1_range[1]
        if b_val:
            sym[f"?{ss_data.get('lunar_face_1', '晦朔')}"] = "t"
        if lf2_range[0] > lf2_range[1]:
            b_val = lunar_day >= lf2_range[0] or lunar_day <= lf2_range[1]
        else:
            b_val = lunar_day >= lf2_range[0] and lunar_day <= lf2_range[1]
        if b_val:
            sym[f"?{ss_data.get('lunar_face_2', '弦望')}"] = "t"

    return sym

def _planet_element(name):
    """行星→五行"""
    m = {
        "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
        "mercury": "水", "mars": "火", "saturn": "土",
        "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
        "mean_apog_ziqi": "炁", "mean_apog_yuebei": "孛",
    }
    return m.get(name, "")

def _planet_element_by_branch(branch):
    """地支→五行（纳音五行简化版，用地支本气五行）"""
    m = {
        "子": "水", "丑": "土", "寅": "木", "卯": "木",
        "辰": "土", "巳": "火", "午": "火", "未": "土",
        "申": "金", "酉": "金", "戌": "土", "亥": "水",
    }
    return m.get(branch, "")

def _check_conjunction(bodies, p1, p2, orb=8.0):
    """检查两行星是否合相（同宫）"""
    d1 = bodies.get(p1, {})
    d2 = bodies.get(p2, {})
    if "lon" not in d1 or "lon" not in d2:
        return False
    gap = abs(normalize_degree(d1["lon"] - d2["lon"]))
    # 同宫 = 在同一30°区间
    b1 = _lon_to_branch(d1["lon"])
    b2 = _lon_to_branch(d2["lon"])
    return b1 == b2

def _build_derived_facts(chart_data):
    """从星盘数据推导高级事实（会/拱/夹/__sp行星排序等）"""
    bodies = chart_data.get("bodies", {})
    facts = {}

    planet_pairs = [
        ("sun", "moon"), ("sun", "venus"), ("sun", "jupiter"),
        ("sun", "mercury"), ("sun", "mars"), ("sun", "saturn"),
        ("sun", "inv_true_node_jidu"), ("sun", "true_node_rohuo"),
        ("sun", "mean_apog_ziqi"), ("sun", "mean_apog_yuebei"),
        ("moon", "venus"), ("moon", "jupiter"), ("moon", "mercury"),
        ("moon", "mars"), ("moon", "saturn"),
        ("moon", "inv_true_node_jidu"), ("moon", "true_node_rohuo"),
        ("moon", "mean_apog_ziqi"), ("moon", "mean_apog_yuebei"),
        ("venus", "jupiter"), ("venus", "mercury"), ("venus", "mars"),
        ("venus", "saturn"), ("jupiter", "mercury"), ("jupiter", "mars"),
        ("jupiter", "saturn"), ("mercury", "mars"), ("mercury", "saturn"),
        ("mars", "saturn"),
    ]

    name_map = {
        "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
        "mercury": "水", "mars": "火", "saturn": "土",
        "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
        "mean_apog_ziqi": "炁", "mean_apog_yuebei": "孛",
    }

    # 会（同宫）
    for p1, p2 in planet_pairs:
        n1, n2 = name_map.get(p1, p1), name_map.get(p2, p2)
        if _check_conjunction(bodies, p1, p2):
            facts[f"?{n1}{n2}会"] = "t"
            facts[f"?{n2}{n1}会"] = "t"

    # __sp 行星排序检测（翻译 EvalRule.setBirthSign 中的 __sp 逻辑）
    facts.update(_compute_sp_flags(bodies))

    # 方位标记（翻译 EvalRule.setSign 中的 directions 逻辑）
    # directions = [西, 南, 东, 北]，每3个宫位一个方位
    # 宫位从戌=0°开始逆序：戌酉申=西, 未午巳=南, 辰卯寅=东, 丑子亥=北
    directions = ["西", "南", "东", "北"]
    for name, body_data in bodies.items():
        if "lon" not in body_data:
            continue
        cn = name_map.get(name)
        if not cn:
            continue
        lon = normalize_degree(body_data["lon"])
        n = int(lon / 30.0) % 12
        direction = directions[n // 3]
        facts[f"?{cn}{direction}"] = "t"

    return facts

def _compute_sp_flags(bodies):
    """计算 __sp1~__sp6 行星排序标记。
    翻译 EvalRule.setBirthSign 中的行星连续排列检测逻辑。

    __sp1: 七政连环 — 日月金木水火土7颗按黄经顺序连续排列
    __sp2: 五曜随阳 — 金木水火土5颗连续，且日紧邻其中
    __sp3: 五星随月 — 金木水火土5颗连续，且月紧邻其中
    __sp4: 五曜连珠 — 金木水火土5颗按黄经顺序连续排列
    __sp5: 五曜环阳 — 金木水火土5颗连续，且日在其中
    __sp6: 四余捧月 — 罗计孛炁4余星+月连续排列
    """
    facts = {}

    # 行星索引（与 Java ChartData 常量一致）
    # SUN=0, MOON=1, VENUS=2, JUPITER=3, MERCURY=4, MARS=5, SATURN=6
    # TRUE_NODE=7, MEAN_APOG=8, OSCU_APOG=9 (实际索引可能不同)
    # 这里用名称映射
    SEVEN_STARS = ["sun", "moon", "venus", "jupiter", "mercury", "mars", "saturn"]
    FIVE_STARS = ["venus", "jupiter", "mercury", "mars", "saturn"]
    FOUR_YU = ["true_node_rohuo", "inv_true_node_jidu", "mean_apog_ziqi", "mean_apog_yuebei"]

    # 构建行星位置列表（按黄经排序）
    positions = []
    for name in SEVEN_STARS + FOUR_YU:
        if name in bodies and "lon" in bodies[name]:
            positions.append((name, normalize_degree(bodies[name]["lon"])))

    if len(positions) < 11:
        return facts

    # 按黄经排序
    positions.sort(key=lambda x: x[1])
    sorted_names = [p[0] for p in positions]

    # 检查五曜连珠（__sp4）: 金木水火土5颗连续
    five_star_set = set(FIVE_STARS)
    for i in range(len(sorted_names)):
        # 检查从i开始的5个位置是否都是五曜
        count = 0
        for j in range(5):
            idx = (i + j) % len(sorted_names)
            if sorted_names[idx] in five_star_set:
                count += 1
            else:
                break
        if count == 5:
            facts["?__sp4"] = "t"

            # 检查是否日紧邻（__sp2: 五曜随阳）
            prev_idx = (i - 1) % len(sorted_names)
            next_idx = (i + 5) % len(sorted_names)
            if sorted_names[prev_idx] == "sun" or sorted_names[next_idx] == "sun":
                facts["?__sp2"] = "t"

            # 检查是否月紧邻（__sp3: 五星随月）
            if sorted_names[prev_idx] == "moon" or sorted_names[next_idx] == "moon":
                facts["?__sp3"] = "t"

            # 检查是否日在其中（__sp5: 五曜环阳）
            around_sun = False
            for j in range(5):
                idx = (i + j) % len(sorted_names)
                if sorted_names[idx] == "sun":
                    around_sun = True
                    break
            if around_sun:
                facts["?__sp5"] = "t"
            break

    # 检查七政连环（__sp1）: 日月金木水火土7颗连续
    seven_star_set = set(SEVEN_STARS)
    for i in range(len(sorted_names)):
        count = 0
        for j in range(7):
            idx = (i + j) % len(sorted_names)
            if sorted_names[idx] in seven_star_set:
                count += 1
            else:
                break
        if count == 7:
            facts["?__sp1"] = "t"
            break

    # 检查四余捧月（__sp6）: 罗计孛炁+月5颗连续
    yu_moon_set = set(FOUR_YU + ["moon"])
    for i in range(len(sorted_names)):
        count = 0
        for j in range(5):
            idx = (i + j) % len(sorted_names)
            if sorted_names[idx] in yu_moon_set:
                count += 1
            else:
                break
        if count == 5:
            facts["?__sp6"] = "t"
            break

    return facts

def eval_rules(chart_data):
    """对星盘数据执行规则库判定。
    返回 {matched: [规则], total: N, matched_count: M}
    """
    rules = load_rules_library()
    sym = _build_symbol_table(chart_data)
    derived = _build_derived_facts(chart_data)
    sym.update(derived)

    # 规则引用缓存：避免重复计算 ?{规则名}
    rule_cache = {}

    # 展开模板规则
    expanded_rules = []
    for rule in rules:
        if "{" in rule["name"]:
            expanded_rules.extend(_expand_template_rule(rule))
        else:
            expanded_rules.append(rule)

    matched = []
    for rule in expanded_rules:
        cond = rule["condition"]
        if not cond:
            continue
        # 求值
        result = _eval_simple_condition(cond, sym, rule_cache)
        if result:
            matched.append({
                "id": rule["id"],
                "sign": rule.get("sign", "+"),
                "name": rule["name"],
                "priority": rule["priority"],
                "condition": cond,
                "comment": rule["comment"],
                "excludes": rule.get("excludes", []),
            })

    return {"matched": matched, "total": len(expanded_rules), "matched_count": len(matched)}

def score_rules(eval_result):
    """格局质量评分模型（v2）。
    不只数格局数量，而是：
    1. 按priority权重给每个格局打分
    2. 关键格局（日月夹命/官福夹命等）额外加权
    3. 忌格组合惩罚（多个忌格同时出现时额外减分）
    4. 喜格(sign="+")加分，忌格(sign="-")减分

    priority权重映射（果老星宗传统等级）：
    - 1.x.x（最高）：日月核心格局，权重5
    - 2.0.x（高）：入垣/殿/得地，权重3
    - 2.2.x（中高）：会合/夹拱，权重2.5
    - 2.3.x（中）：相生/同辉，权重2
    - 2.4.x（中低）：特殊组合，权重1.5
    - 3.x.x（低）：方位/季节，权重1
    - 4.x.x（最低）：其他，权重0.5
    - None/未知：权重1
    """
    priority_weights = {
        "1": 5.0,    # 最高：日月核心
        "2.0": 3.0,  # 高：入垣殿
        "2.2": 2.5,  # 中高：会合夹拱
        "2.3": 2.0,  # 中：相生同辉
        "2.4": 1.5,  # 中低：特殊组合
        "3": 1.0,    # 低：方位季节
        "4": 0.5,    # 最低：其他
    }

    # 关键格局额外加权（这些是决定命格等级的核心格局）
    KEY_GOOD_PATTERNS = {
        "日月夹命": 5.0, "日月夹夫": 3.0, "日月夹财": 3.0, "日月夹辅": 3.0,
        "官福夹命": 5.0, "田财夹命": 3.0,
        "日月拱福": 3.0, "官福拱命": 3.0,
        "七政拱命": 4.0, "众曜环拱": 3.0,
        "君臣庆会": 4.0, "天地开明": 3.0,
        "日月殿垣": 3.0, "日月居垣": 3.0,
        "孤月独明": 3.0, "木月清贵": 3.0,
        "福官会聚": 3.0, "官福居垣": 3.0,
        "身命升殿": 3.0, "身命殿垣": 3.0,
    }

    # 关键忌格（出现即严重减分）
    KEY_BAD_PATTERNS = {
        "日月失明": 5.0, "日月失躔": 4.0, "日月失位": 4.0, "日月失垣": 3.0,
        "土埋双女": 4.0, "木打宝瓶": 4.0,
        "水火交战": 3.0, "火孛交战": 3.0, "金木对克": 3.0,
        "罗犯太阳": 4.0, "计犯太阴": 4.0,
        "土月对掩": 4.0, "土月相掩": 3.0,
        "诸星怒地": 5.0, "诸星背命": 4.0,
        "孤日单行": 3.0, "炁星蔽月": 3.0,
    }

    good_score = 0.0
    bad_score = 0.0
    good_count = 0
    bad_count = 0
    key_good_matched = []
    key_bad_matched = []

    for m in eval_result["matched"]:
        sign = m.get("sign", "+")
        name = m.get("name", "")

        # 计算基础权重
        pri = str(m.get("priority", ""))
        weight = 1.0
        for prefix, w in priority_weights.items():
            if pri.startswith(prefix):
                weight = w
                break

        # 关键格局额外加权
        key_bonus = 0.0
        if sign == "+":
            for kp, bonus in KEY_GOOD_PATTERNS.items():
                if kp in name:
                    key_bonus = bonus
                    key_good_matched.append(name)
                    break
        else:
            for kp, bonus in KEY_BAD_PATTERNS.items():
                if kp in name:
                    key_bonus = bonus
                    key_bad_matched.append(name)
                    break

        total_weight = weight + key_bonus

        if sign == "+":
            good_score += total_weight
            good_count += 1
        else:
            bad_score += total_weight
            bad_count += 1

    # 忌格组合惩罚：多个关键忌格同时出现时额外减分
    if len(key_bad_matched) >= 3:
        bad_score += len(key_bad_matched) * 2.0
    elif len(key_bad_matched) >= 2:
        bad_score += len(key_bad_matched) * 1.0

    total_score = good_score - bad_score
    ratio = good_score / bad_score if bad_score > 0 else float('inf') if good_score > 0 else 1.0

    # 命格等级建议（基于总分、喜忌比、关键格局）
    key_good_count = len(key_good_matched)
    key_bad_count = len(key_bad_matched)

    if total_score >= 35 and ratio >= 2.5 and key_good_count >= 2 and key_bad_count <= 1:
        grade = "高命格（三品以上）"
    elif total_score >= 25 and ratio >= 2 and key_good_count >= 1:
        grade = "中高命格（五品至四品）"
    elif total_score >= 15 and ratio >= 1.5:
        grade = "中命格（七品至六品）"
    elif total_score >= 10 or (key_bad_count >= 2 and ratio < 2):
        grade = "中低命格（寻常至安常）"
    else:
        grade = "低命格（带疾/起倒）"

    return {
        "total_score": round(total_score, 2),
        "good_score": round(good_score, 2),
        "bad_score": round(bad_score, 2),
        "good_count": good_count,
        "bad_count": bad_count,
        "ratio": round(ratio, 2) if ratio != float('inf') else 999.0,
        "key_good_count": key_good_count,
        "key_bad_count": key_bad_count,
        "key_good_matched": key_good_matched,
        "key_bad_matched": key_bad_matched,
        "grade_suggestion": grade,
    }

def _expand_template_rule(rule):
    """展开模板规则（名称含 {} 占位符的）。
    支持两种格式：
    1. {日,月,金} → 简单枚举，{} 替换为枚举值
    2. {命=命宫,财=财帛} → 键值对，名称用键，条件用值
    """
    import re
    name = rule["name"]
    cond = rule["condition"]

    # 找到 {枚举列表} 部分
    match = re.search(r'\{([^}]+)\}', name)
    if not match:
        return [rule]

    enum_str = match.group(1)
    enum_items = [x.strip() for x in enum_str.split(',')]

    # 检查是否是键值对格式
    is_kv = any('=' in item for item in enum_items)

    expanded = []
    for item in enum_items:
        if is_kv and '=' in item:
            key, val = item.split('=', 1)
            key, val = key.strip(), val.strip()
            new_name = name.replace(match.group(0), key)
            new_cond = cond.replace("{}", val)
        else:
            new_name = name.replace(match.group(0), item)
            new_cond = cond.replace("{}", item)
        new_rule = dict(rule)
        new_rule["name"] = new_name
        new_rule["condition"] = new_cond
        expanded.append(new_rule)

    return expanded

def _eval_simple_condition(cond, sym, rule_cache=None, depth=0):
    """简化版条件求值器。
    支持: ?变量, & (与), | (或), ! (非), = (等于/集合包含)
    支持: @变量[0]=地支, @变量=@变量, %变量[0]=宿名
    支持: &函数名(参数) 形式的24个内置函数
    支持: @{变量} 模板变量, %{变量} 模板变量
    支持: ?{规则名} 规则引用
    支持: @变量+N 算术运算
    """
    import re
    expr = cond.strip()
    if not expr:
        return False

    # 防止递归过深
    if depth > 10:
        return False

    # 跳过含 __sp 的规则（需要行星位置排序，暂不支持）
    if "__sp" in expr:
        return False

    # 替换 ?{规则名} → 规则引用结果
    def replace_rule_ref(m):
        rule_name = m.group(1)
        # 1. 先检查符号表中是否有 ?规则名（如 ?日水会）
        sym_key = f"?{rule_name}"
        if sym_key in sym:
            return "True" if sym[sym_key] == "t" else "False"
        # 2. 检查规则缓存
        if rule_cache is not None and rule_name in rule_cache:
            return "True" if rule_cache[rule_name] else "False"
        # 3. 尝试从规则库查找该规则
        if rule_cache is not None:
            rules = load_rules_library()
            for r in rules:
                if r['name'] == rule_name and r['condition']:
                    result = _eval_simple_condition(r['condition'], sym, rule_cache, depth + 1)
                    rule_cache[rule_name] = result
                    return "True" if result else "False"
        return "False"
    expr = re.sub(r'\?\{([^}]+)\}', replace_rule_ref, expr)

    # 替换 @{变量} → 模板变量（先取变量值，再用该值作为新变量名）
    def replace_at_template(m):
        var = m.group(1)
        val = sym.get(f"@{var}", "")
        return val
    # 先替换 @{变量}[index] 形式
    def replace_at_template_index(m):
        var = m.group(1)
        idx = m.group(2)
        val = sym.get(f"@{var}", "")
        if val:
            return f'@{val}[{idx}]'
        return ''
    expr = re.sub(r'@\{(\w+)\}\[(\d+)\]', replace_at_template_index, expr)
    # 再替换 @{变量} 形式
    expr = re.sub(r'@\{(\w+)\}', replace_at_template, expr)

    # 替换 %{变量} → 模板变量
    def replace_pct_template_index(m):
        var = m.group(1)
        idx = m.group(2)
        val = sym.get(f"%{var}", "")
        if val:
            return f'%{val}[{idx}]'
        return ''
    expr = re.sub(r'%\{(\w+)\}\[(\d+)\]', replace_pct_template_index, expr)
    def replace_pct_template(m):
        var = m.group(1)
        val = sym.get(f"%{var}", "")
        return val
    expr = re.sub(r'%\{(\w+)\}', replace_pct_template, expr)

    # 替换 ?变量 → True/False
    def replace_qvar(m):
        var = m.group(1)
        val = sym.get(f"?{var}", "f")
        return "True" if val == "t" else "False"
    expr = re.sub(r'\?(\w+)', replace_qvar, expr)

    # 替换 &函数名(参数) → 函数调用
    expr = _replace_functions(expr, sym)

    # 替换 @变量+N=@变量 和 @变量-N=@变量 → 算术比较
    def replace_at_arith_eq(m):
        var1 = m.group(1)
        op = m.group(2)
        n = int(m.group(3))
        var2 = m.group(4)
        val1 = sym.get(f"@{var1}", "")
        val2 = sym.get(f"@{var2}", "")
        # 解析地支为索引
        branch_order = ["戌","酉","申","未","午","巳","辰","卯","寅","丑","子","亥"]
        if val1 and val2 and val1[0] in branch_order and val2[0] in branch_order:
            idx1 = branch_order.index(val1[0])
            idx2 = branch_order.index(val2[0])
            if op == '+':
                expected = (idx1 + n) % 12
            else:
                expected = (idx1 - n) % 12
            return f'({expected}=={idx2})'
        return "False"
    expr = re.sub(r'@(\w+)([+\-])(\d+)=@(\w+)', replace_at_arith_eq, expr)

    # 替换 @变量=@变量+N 和 @变量=@变量-N → 反向算术比较
    def replace_at_arith_eq_rev(m):
        var1 = m.group(1)
        var2 = m.group(2)
        op = m.group(3)
        n = int(m.group(4))
        val1 = sym.get(f"@{var1}", "")
        val2 = sym.get(f"@{var2}", "")
        branch_order = ["戌","酉","申","未","午","巳","辰","卯","寅","丑","子","亥"]
        if val1 and val2 and val1[0] in branch_order and val2[0] in branch_order:
            idx1 = branch_order.index(val1[0])
            idx2 = branch_order.index(val2[0])
            if op == '+':
                expected = (idx2 + n) % 12
            else:
                expected = (idx2 - n) % 12
            return f'({idx1}=={expected})'
        return "False"
    expr = re.sub(r'@(\w+)=@(\w+)([+\-])(\d+)', replace_at_arith_eq_rev, expr)

    # 替换 @变量[0]=值 → 比较
    def replace_at_index(m):
        var = m.group(1)
        idx = m.group(2)
        val = m.group(3)
        sym_key = f"@{var}[{idx}]"
        sym_val = sym.get(sym_key, "")
        return f'("{sym_val}"=="{val}")'
    expr = re.sub(r'@(\w+)\[(\d+)\]=(\S+)', replace_at_index, expr)

    # 替换 @变量=@变量 → 同宫比较
    def replace_at_eq(m):
        var1 = m.group(1)
        var2 = m.group(2)
        val1 = sym.get(f"@{var1}", "")
        val2 = sym.get(f"@{var2}", "")
        return f'("{val1}"=="{val2}")'
    expr = re.sub(r'@(\w+)=@(\w+)', replace_at_eq, expr)

    # 替换 %变量[0]=值 → 宿度比较
    def replace_pct_index(m):
        var = m.group(1)
        idx = m.group(2)
        val = m.group(3)
        sym_key = f"%{var}[{idx}]"
        sym_val = sym.get(sym_key, "")
        return f'("{sym_val}"=="{val}")'
    expr = re.sub(r'%(\w+)\[(\d+)\]=(\S+)', replace_pct_index, expr)

    # 替换 ${变量名} → 字符串值
    def replace_sref(m):
        var = m.group(1)
        return f'"{sym.get(f"${var}", "")}"'
    expr = re.sub(r'\$\{(\w+)\}', replace_sref, expr)

    # 替换 $变量 → 字符串值（如果不在引号内）
    def replace_svar(m):
        var = m.group(1)
        val = sym.get(f"${var}", "")
        return f'"{val}"'
    expr = re.sub(r'\$(\w+)(?![\w])', replace_svar, expr)

    # 替换 @变量 → 字符串值（如果还有未替换的）
    def replace_at_var(m):
        var = m.group(1)
        val = sym.get(f"@{var}", "")
        return f'"{val}"'
    expr = re.sub(r'@(\w+)(?![\w\[])', replace_at_var, expr)

    # 替换 %变量 → 字符串值
    def replace_pct_var(m):
        var = m.group(1)
        val = sym.get(f"%{var}", "")
        return f'"{val}"'
    expr = re.sub(r'%(\w+)(?![\w\[])', replace_pct_var, expr)

    # 替换逻辑运算符
    expr = expr.replace("&", " and ").replace("|", " or ")
    # 替换 ! 为 not（注意不要替换 != 中的 !）
    expr = re.sub(r'!(?!=)', " not ", expr)

    try:
        return bool(eval(expr))
    except Exception:
        return False

def _replace_functions(expr, sym):
    """替换 &函数名(参数) 为 Python 表达式。
    支持24个内置函数: if, eval, map, test, set, offset, format, prefix, suffix,
    intersection, iter, digit, union, complement, contain, trim, entry, split,
    empty, size, import, int, round, abs
    """
    import re

    # 递归处理嵌套函数调用
    max_iter = 10
    while max_iter > 0:
        # 查找最内层的函数调用（没有嵌套其他函数的）
        pattern = r'&(\w+)\(([^()&]*)\)'
        match = re.search(pattern, expr)
        if not match:
            break

        func_name = match.group(1)
        args_str = match.group(2)

        # 解析参数
        args = [a.strip() for a in args_str.split(',')] if args_str.strip() else []

        # 求值参数
        eval_args = []
        for arg in args:
            arg = arg.strip()
            if arg.startswith('"') and arg.endswith('"'):
                eval_args.append(arg[1:-1])
            elif arg in ('True', 'False'):
                eval_args.append('t' if arg == 'True' else 'f')
            else:
                # 尝试从符号表获取
                if arg.startswith('?'):
                    eval_args.append(sym.get(arg, 'f'))
                elif arg.startswith('@') or arg.startswith('$') or arg.startswith('%'):
                    eval_args.append(sym.get(arg, ''))
                else:
                    eval_args.append(arg)

        # 调用内置函数
        result = _call_builtin_function(func_name, eval_args, sym)
        if result is None:
            # 未知函数，替换为 False
            result_str = "False"
        elif isinstance(result, bool):
            result_str = "True" if result else "False"
        elif isinstance(result, (int, float)):
            result_str = str(result)
        else:
            result_str = f'"{result}"'

        expr = expr[:match.start()] + result_str + expr[match.end():]
        max_iter -= 1

    return expr

def _call_builtin_function(func_name, args, sym):
    """调用24个内置函数之一。"""
    name = func_name.lower()

    if name == "if":
        # if(cond, then, [else, ...])
        if len(args) >= 2:
            i = 0
            while i + 1 < len(args):
                if args[i] == "t":
                    return args[i + 1]
                i += 2
            if i < len(args):
                return args[i]
        return ""

    if name in ("eval", "map", "test"):
        # eval/set(arg, [prefix], suffix)
        if len(args) >= 1:
            prefix = args[1] if len(args) >= 3 else ""
            suffix = args[-1] if len(args) >= 2 else ""
            return _eval_set(args[0], prefix, suffix, name, sym)
        return ""

    if name == "set":
        # set(*args) → 集合
        return ",".join(args)

    if name == "offset":
        # offset(pos, base, shift, size)
        if len(args) == 4:
            try:
                pos = int(args[0])
                base = int(args[1])
                shift = int(args[2])
                size = int(args[3])
                return str((base + shift - pos) % size)
            except (ValueError, TypeError):
                return ""
        return ""

    if name == "format":
        # format(template, index, value)
        if len(args) == 3:
            try:
                idx = int(args[1])
                template = args[0]
                val = args[2]
                # 替换模板中第idx个占位符
                result = template.replace(f"{{{idx}}}", val)
                return result
            except (ValueError, TypeError):
                return ""
        return ""

    if name in ("prefix", "suffix"):
        # prefix/suffix(set, prefix/suffix, count)
        if len(args) == 3:
            try:
                count = int(args[2])
                s = args[0]
                ps = args[1]
                if name == "prefix":
                    return ps + s[:count]
                else:
                    return s[-count:] + ps if count > 0 else s
            except (ValueError, TypeError):
                return ""
        return ""

    if name == "intersection":
        # intersection(set_a, set_b, [trim])
        if len(args) >= 2:
            set_a = set(args[0].split(',')) if args[0] else set()
            set_b = set(args[1].split(',')) if args[1] else set()
            result = set_a & set_b
            if len(args) >= 3:
                # trim: 只保留指定数量的元素
                try:
                    trim = int(args[2])
                    result = set(list(result)[:trim])
                except (ValueError, TypeError):
                    pass
            return ",".join(sorted(result)) if result else ""
        return ""

    if name == "union":
        # union(set_a, set_b)
        if len(args) == 2:
            set_a = set(args[0].split(',')) if args[0] else set()
            set_b = set(args[1].split(',')) if args[1] else set()
            result = set_a | set_b
            return ",".join(sorted(result)) if result else ""
        return ""

    if name == "complement":
        # complement(set_a, set_b) → set_a - set_b
        if len(args) == 2:
            set_a = set(args[0].split(',')) if args[0] else set()
            set_b = set(args[1].split(',')) if args[1] else set()
            result = set_a - set_b
            return ",".join(sorted(result)) if result else ""
        return ""

    if name == "contain":
        # contain(set, value)
        if len(args) == 2:
            s = set(args[0].split(',')) if args[0] else set()
            return "t" if args[1] in s else "f"
        return "f"

    if name == "trim":
        # trim(set, count)
        if len(args) == 2:
            try:
                count = int(args[1])
                items = args[0].split(',') if args[0] else []
                return ",".join(items[:count])
            except (ValueError, TypeError):
                return ""
        return ""

    if name == "entry":
        # entry(set, index)
        if len(args) == 2:
            try:
                idx = int(args[1])
                items = args[0].split(',') if args[0] else []
                return items[idx] if 0 <= idx < len(items) else ""
            except (ValueError, TypeError):
                return ""
        return ""

    if name == "split":
        # split(string, separator)
        if len(args) == 2:
            sep = args[1] if args[1] else ","
            return ",".join(args[0].split(sep)) if args[0] else ""
        return ""

    if name == "empty":
        # empty(set)
        if len(args) == 1:
            s = args[0].strip()
            return "t" if not s or s == "," else "f"
        return "f"

    if name == "size":
        # size(set)
        if len(args) == 1:
            items = args[0].split(',') if args[0] else []
            return str(len([x for x in items if x.strip()]))
        return "0"

    if name == "import":
        # import(set) → 导入集合（简化版直接返回）
        if len(args) == 1:
            return args[0]
        return ""

    if name in ("int", "round", "abs"):
        # int/round/abs(value)
        if len(args) == 1:
            try:
                d = float(args[0])
                if name == "round":
                    d += 0.5
                if name == "abs":
                    return str(abs(d))
                return str(int(d))
            except (ValueError, TypeError):
                return ""
        return ""

    if name == "digit":
        # digit(value, int_digits, frac_digits)
        if len(args) == 3:
            try:
                d = float(args[0])
                int_d = int(args[1])
                frac_d = int(args[2])
                return f"{d:.{frac_d}f}".zfill(int_d + frac_d + 1)
            except (ValueError, TypeError):
                return ""
        return ""

    if name == "iter":
        # iter(set, template, [separator]) → 遍历集合
        if len(args) >= 2:
            items = args[0].split(',') if args[0] else []
            template = args[1]
            sep = args[2] if len(args) >= 3 else ","
            results = []
            for i, item in enumerate(items):
                result = template.replace("[a]", item).replace("[i]", str(i))
                results.append(result)
            return sep.join(results) if results else ""
        return ""

    return None

def _eval_set(arg, prefix, suffix, func, sym):
    """eval/map/test 函数的核心逻辑。
    对集合中的每个元素，构造 prefix+element+suffix，求值后收集结果。
    """
    items = arg.split(',') if arg else []
    results = []
    for item in items:
        key = prefix + item + suffix
        if key.startswith("?"):
            val = sym.get(key, "f")
            if func == "test":
                return val == "t"
            if val == "t":
                results.append(item)
        elif key.startswith("@") or key.startswith("$") or key.startswith("%"):
            val = sym.get(key, "")
            if val:
                results.append(val)
        else:
            # 直接求值
            if func == "test":
                return False
    if func == "test":
        return len(results) > 0
    if func == "map":
        return ",".join(results)
    # eval
    return ",".join(results) if results else ""


# ---------- Phase 25: 历史宿度加载 ----------

_MANSION_ERA = "default"

def set_mansion_era(era="default"):
    """设置宿度时代。
    era: "default"(汉代), "shoushi"(授时历), "dazong"(大统历)
    """
    global _MANSION_ERA
    available = _c()["lunar_mansions"].get("historical_widths", {}).keys()
    if era not in available:
        raise ValueError(f"未知宿度时代: {era}, 可用: {list(available)}")
    _MANSION_ERA = era


def get_mansion_widths(era=None):
    """获取指定时代的二十八宿宿度表。"""
    if era is None:
        era = _MANSION_ERA
    lm = _c()["lunar_mansions"]
    historical = lm.get("historical_widths", {})
    if era in historical:
        return historical[era]
    return lm.get("width_yellow", [])


def calc_lunar_mansion_historical(lon, era=None, ayanamsa_offset=0.0):
    """历史宿度计算：使用指定时代的宿度表。
    返回 {mansion_index, mansion_name, degree_in_mansion, mansion_width}
    """
    if era is None:
        era = _MANSION_ERA
    widths = get_mansion_widths(era)
    order = _c()["lunar_mansions"]["order"]

    # 计算角宿起点（考虑岁差）
    sid_lon = normalize_degree(lon - ayanamsa_offset)

    total = sum(widths)
    pos = sid_lon * total / 360.0  # 缩放到宿度制

    cursor = 0.0
    for i, w in enumerate(widths):
        if pos < cursor + w:
            return {
                "mansion_index": i,
                "mansion_name": order[i],
                "degree_in_mansion": round(pos - cursor, 6),
                "mansion_width": w,
                "era": era,
            }
        cursor += w

    # 超出范围（不应该发生）
    return {
        "mansion_index": 27,
        "mansion_name": order[-1],
        "degree_in_mansion": round(pos - cursor + widths[-1], 6),
        "mansion_width": widths[-1],
        "era": era,
    }


# ---------- Phase 17: 断语库 ----------

_DUANYU_LIBRARY = None

def load_duanyu_library(path=None):
    """加载断语库 JSON。"""
    global _DUANYU_LIBRARY
    if path is None:
        path = os.path.join(_HERE, "duanyu_library.json")
    if not os.path.exists(path):
        _DUANYU_LIBRARY = []
        return _DUANYU_LIBRARY
    with open(path, encoding="utf-8") as f:
        _DUANYU_LIBRARY = json.load(f)
    return _DUANYU_LIBRARY


def query_duanyu(chart_data):
    """根据星盘数据查询匹配断语。
    返回 [{id, source, text, tags, ...}] 列表。
    """
    if _DUANYU_LIBRARY is None:
        load_duanyu_library()
    if not _DUANYU_LIBRARY:
        return []

    # 构建符号表（复用规则引擎的符号系统）
    sym = _build_symbol_table(chart_data)

    matched = []
    for duanyu in _DUANYU_LIBRARY:
        cond = duanyu.get("condition", "")
        if not cond:
            # 无条件的断语总是匹配
            matched.append(duanyu)
            continue
        try:
            if _eval_simple_condition(cond, sym):
                matched.append(duanyu)
        except Exception:
            continue

    return matched


# ---------- Phase 14: 多点矫正 ----------

def rectify_multi_point(targets, start_jd, ephe_path="ephe"):
    """接受多个 {planet: degree} 目标，对每个目标反推 UT，返回所有结果 + 一致性评分。
    targets: {"sun": 30.0, "moon": 200.0, ...}
    start_jd: 搜索起始JD
    返回 {results: {planet: {jd, date_ut, delta_hours}}, consistency_score}
    """
    init_ephe(ephe_path)
    results = {}
    jds = []

    for name, deg in targets.items():
        if name == "sun":
            jd_found = find_date_at_sun_pos(deg, start_jd)
        elif name == ZIQI_KEY:
            base_jd = _ziqi_base_jd()
            jd_found = base_jd + ((deg - ZIQI_BASE_LON) / ZIQI_SPEED)
        else:
            pid = BODIES.get(name)
            if pid is None:
                results[name] = {"error": f"unknown body {name}"}
                continue
            jd_found = find_date_at_planet_pos(pid, deg, start_jd)

        if jd_found is None:
            results[name] = {"error": "no solution"}
        else:
            fy, fmo, fd, fh = ymd_ut_from_jd(jd_found)
            results[name] = {
                "jd": round(jd_found, 8),
                "date_ut": f"{fy:04d}-{fmo:02d}-{fd:02d}T{fh:07.4f}",
                "delta_hours": round((jd_found - start_jd) * 24, 4),
            }
            jds.append(jd_found)

    # 一致性评分
    score = _consistency_score(jds)

    return {
        "results": results,
        "consistency_score": score,
        "jd_count": len(jds),
    }


def _consistency_score(jds):
    """多个反推结果的标准差/极差 → 评分（0-100，越高越一致）。"""
    if not jds:
        return 0
    if len(jds) == 1:
        return 100

    import statistics
    mean_jd = statistics.mean(jds)
    stdev = statistics.stdev(jds) if len(jds) > 1 else 0
    range_jd = max(jds) - min(jds)

    # 转换为小时
    stdev_hours = stdev * 24
    range_hours = range_jd * 24

    # 评分：标准差越小越高，极差越小越高
    # 0小时差=100分, 24小时差=0分
    score_stdev = max(0, 100 - stdev_hours * 100 / 24)
    score_range = max(0, 100 - range_hours * 100 / 24)
    score = (score_stdev + score_range) / 2

    return {
        "score": round(score, 2),
        "stdev_hours": round(stdev_hours, 4),
        "range_hours": round(range_hours, 4),
        "mean_jd": round(mean_jd, 6),
    }


def iterative_rectify(birth_info, life_events, ephe_path="ephe"):
    """完整迭代矫正 SOP 封装：生成初始盘→AI 映射事件→多点反推→一致性检验→返回矫正结果+历史。
    birth_info: {year, month, day, hour, lon, lat}
    life_events: [{year, event_type, description, target_planet, target_degree}]
    返回 {original_ut, corrected_ut, method, history, consistency}
    """
    init_ephe(ephe_path)
    y, mo, d, h = birth_info["year"], birth_info["month"], birth_info["day"], birth_info["hour"]
    start_jd = jd_from_ymd_ut(y, mo, d, h)
    original_ut = f"{y:04d}-{mo:02d}-{d:02d}T{h:07.4f}"

    # 收集所有目标
    targets = {}
    for ev in life_events:
        tp = ev.get("target_planet")
        td = ev.get("target_degree")
        if tp and td is not None:
            targets[tp] = td

    if not targets:
        return {
            "original_ut": original_ut,
            "corrected_ut": original_ut,
            "method": "no_targets",
            "history": [],
            "consistency": {"score": 0, "reason": "no targets provided"},
        }

    # 多点反推
    result = rectify_multi_point(targets, start_jd, ephe_path)

    # 取一致性最高的JD作为矫正结果
    jds = [r["jd"] for r in result["results"].values() if isinstance(r, dict) and "jd" in r]
    if jds:
        import statistics
        corrected_jd = statistics.median(jds)
        cy, cm, cd, ch = ymd_ut_from_jd(corrected_jd)
        corrected_ut = f"{cy:04d}-{cm:02d}-{cd:02d}T{ch:07.4f}"
        delta_hours = round((corrected_jd - start_jd) * 24, 4)
    else:
        corrected_ut = original_ut
        delta_hours = 0

    return {
        "original_ut": original_ut,
        "corrected_ut": corrected_ut,
        "corrected_jd": round(corrected_jd, 8) if jds else None,
        "delta_hours": delta_hours,
        "method": "multi_point_median",
        "targets": targets,
        "results": result["results"],
        "consistency": result["consistency_score"],
        "history": [{
            "step": 1,
            "action": "multi_point_rectify",
            "targets_count": len(targets),
            "consistency": result["consistency_score"],
        }],
    }


# ---------- Phase 15: 大限综合分析 ----------

def find_daxian_transitions(life_sign_pos, child_limit_years=None):
    """识别12个大限的交接年龄。
    返回 [{limit_index, transition_age, limit_start_degree, limit_name}]。
    """
    limit_seq = _c()["limits"]["limit_seq"]
    if child_limit_years is None:
        child_limit_years = calc_child_limit_years(life_sign_pos, round_to_year=False) / 365.25

    transitions = []
    age_cursor = child_limit_years
    for i in range(len(limit_seq)):
        year = child_limit_years if i == 0 else limit_seq[i]
        transitions.append({
            "limit_index": i,
            "transition_age": round(age_cursor, 4),
            "limit_start_degree": round(normalize_degree(life_sign_pos + 30.0 * i), 6),
            "limit_name": _lon_to_zodiac_name(normalize_degree(life_sign_pos + 30.0 * i)),
        })
        age_cursor += year
    return transitions


def analyze_daxian_limit(chart_data, limit_index):
    """对指定大限做综合分析：宫位/宫主/宫主庙旺/限内星曜/限内神煞。
    chart_data: build_chart() 返回的完整星盘数据
    limit_index: 0-11
    返回结构化 JSON。
    """
    life_sign = chart_data.get("life_sign", 0.0)
    bodies = chart_data.get("bodies", {})
    dignities = chart_data.get("dignities", {})
    child_limit_yr = chart_data.get("child_limit_years", 10)

    limit_seq = _c()["limits"]["limit_seq"]
    if limit_index < 0 or limit_index >= len(limit_seq):
        return None

    year = child_limit_yr if limit_index == 0 else limit_seq[limit_index]
    limit_start = normalize_degree(life_sign + 30.0 * limit_index)
    limit_end = normalize_degree(limit_start + 30.0)
    limit_name = _lon_to_zodiac_name(limit_start)

    # 限内星曜
    stars_in_limit = []
    for name, body in bodies.items():
        if "lon" not in body:
            continue
        lon = normalize_degree(body["lon"])
        in_range = (limit_start <= lon < limit_end) if limit_start < limit_end else (lon >= limit_start or lon < limit_end)
        if in_range:
            stars_in_limit.append({
                "name": name,
                "lon": round(lon, 6),
                "dignity": dignities.get(name, ""),
                "speed_state": chart_data.get("speed_states", {}).get(name, ""),
            })

    # 宫主（该宫位地支的主星）
    limit_branch = _lon_to_branch(limit_start)
    house_ruler = _get_house_ruler(limit_branch)

    # 宫主庙旺
    ruler_dignity = ""
    if house_ruler:
        ruler_dignity = calc_dignity(house_ruler, limit_branch)

    # 限内神煞（基于四柱）
    star_signs = chart_data.get("star_signs", {})
    table = star_signs.get("table", {})
    limit_stars = []
    if isinstance(table, dict):
        # table 是 {地支: [神煞]} 映射
        limit_stars = table.get(limit_branch, [])
    elif isinstance(table, list) and limit_index < len(table):
        row = table[limit_index]
        if isinstance(row, list):
            limit_stars = [s for s in row if s]
        elif isinstance(row, dict):
            limit_stars = [v for v in row.values() if v]

    return {
        "limit_index": limit_index,
        "limit_name": limit_name,
        "limit_branch": limit_branch,
        "limit_years": year,
        "limit_start_degree": round(limit_start, 6),
        "limit_end_degree": round(limit_end, 6),
        "house_ruler": house_ruler,
        "ruler_dignity": ruler_dignity,
        "stars_in_limit": stars_in_limit,
        "limit_shen_sha": limit_stars,
    }


def _get_house_ruler(branch):
    """获取地支的宫主星（七政四余宫主分配）。"""
    # 十二宫主：子丑土、寅卯木、辰巳火、午未日、申酉水、戌亥火（七政四余体系）
    # 实际七政四余宫主：子土/丑土/寅木/卯木/辰火/巳火/午日/未日/申水/酉水/戌火/亥火
    # 这里用简化的地支→五行→行星映射
    rulers = {
        "子": "土", "丑": "土", "寅": "木", "卯": "木",
        "辰": "火", "巳": "火", "午": "日", "未": "日",
        "申": "水", "酉": "水", "戌": "火", "亥": "火",
    }
    return rulers.get(branch, "")


def progress_daxian_years(chart_data, age_start, age_end):
    """对年龄区间逐年调用 compute_now_data()，返回逐年流年数据列表。"""
    life_sign = chart_data.get("life_sign", 0.0)
    birth_year = chart_data.get("input", {}).get("date_ut", "1990")[:4]
    try:
        birth_year = int(birth_year)
    except (ValueError, TypeError):
        birth_year = 1990

    results = []
    for age in range(age_start, age_end + 1):
        now_data = compute_now_data(birth_year, age, chart_data.get("four_poles"), life_sign)
        daxian = calc_daxian(life_sign, age, chart_data.get("child_limit_years"))
        results.append({
            "age": age,
            "year_pole": now_data.get("year_pole", ""),
            "daxian": daxian,
            "small_limit": round(small_limit(life_sign, age), 6),
        })
    return results


def analyze_daxian_full(chart_data):
    """12限全量分析：逐限调用 analyze_daxian_limit + 交接期标注。
    返回完整大限推演报告 JSON。
    """
    life_sign = chart_data.get("life_sign", 0.0)
    child_limit_yr = chart_data.get("child_limit_years", 10)

    transitions = find_daxian_transitions(life_sign, child_limit_yr)
    limits_analysis = []
    for i in range(12):
        analysis = analyze_daxian_limit(chart_data, i)
        if analysis:
            analysis["transition_age"] = transitions[i]["transition_age"] if i < len(transitions) else None
            limits_analysis.append(analysis)

    return {
        "life_sign": round(life_sign, 6),
        "child_limit_years": child_limit_yr,
        "transitions": transitions,
        "limits": limits_analysis,
        "total_limits": len(limits_analysis),
    }


# ---------- Phase 16: 流年分析 ----------

def taishui_relation(life_sign_pos, year_branch):
    """太岁关系计算：返回合/冲/刑/破/害。
    life_sign_pos: 命宫黄经
    year_branch: 流年地支（如 "子"）
    """
    branches = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    if year_branch not in branches:
        return {"relation": "未知", "details": ""}

    year_idx = branches.index(year_branch)
    life_branch = _lon_to_branch(life_sign_pos)
    if life_branch not in branches:
        return {"relation": "未知", "details": ""}
    life_idx = branches.index(life_branch)

    diff = (year_idx - life_idx) % 12

    relations = []
    if diff == 0:
        relations.append("值太岁")
    elif diff == 6:
        relations.append("冲太岁")
    elif diff == 3 or diff == 9:
        relations.append("刑太岁")
    elif diff == 7 or diff == 5:
        relations.append("破太岁")
    elif diff == 4 or diff == 8:
        relations.append("害太岁")
    elif diff == 1 or diff == 11:
        relations.append("合太岁")

    return {
        "life_branch": life_branch,
        "year_branch": year_branch,
        "relation": "、".join(relations) if relations else "无",
        "details": f"命宫{life_branch} vs 流年{year_branch}",
    }


def analyze_liunian(chart_data, age):
    """对指定年龄做流年综合分析：太岁关系/神煞叠加/大限叠加。
    返回结构化 JSON。
    """
    life_sign = chart_data.get("life_sign", 0.0)
    birth_year = chart_data.get("input", {}).get("date_ut", "1990")[:4]
    try:
        birth_year = int(birth_year)
    except (ValueError, TypeError):
        birth_year = 1990

    # 流年数据
    now_data = compute_now_data(birth_year, age, chart_data.get("four_poles"), life_sign)

    # 流年地支
    year_pole = now_data.get("year_pole", "")
    year_branch = year_pole[1] if len(year_pole) >= 2 else ""

    # 太岁关系
    taishui = taishui_relation(life_sign, year_branch)

    # 当前大限
    current_daxian = calc_daxian(life_sign, age, chart_data.get("child_limit_years"))

    # 小限
    small = small_limit(life_sign, age)

    return {
        "age": age,
        "year_pole": year_pole,
        "year_branch": year_branch,
        "taishui": taishui,
        "current_daxian": current_daxian,
        "small_limit": round(small, 6),
        "now_data": now_data,
    }


def progress_liunian_years(chart_data, age_start, age_end):
    """对年龄区间逐年调用 analyze_liunian，返回逐年分析列表。"""
    return [analyze_liunian(chart_data, age) for age in range(age_start, age_end + 1)]


# ---------- Phase 19: 天文计算扩展 ----------

def sanfang_sizheng(house_index):
    """三方四正计算：返回三合宫+对宫。
    house_index: 0-11
    返回 {sanfang: [indices], duigong: index}
    """
    # 三合宫：index, index+4, index+8 (mod 12)
    sanfang = [(house_index + i * 4) % 12 for i in range(3)]
    # 对宫：index + 6 (mod 12)
    duigong = (house_index + 6) % 12
    return {
        "house_index": house_index,
        "sanfang": sanfang,
        "duigong": duigong,
        "all_related": sorted(set(sanfang + [duigong])),
    }


def calc_aspects(bodies, orb=8.0):
    """行星间相位计算。
    主要相位：合(0°)、冲(180°)、三合(120°)、六合(60°)、刑(90°)
    返回 [{p1, p2, aspect, orb}] 列表。
    """
    aspects_def = [
        ("合", 0.0),
        ("六合", 60.0),
        ("刑", 90.0),
        ("三合", 120.0),
        ("冲", 180.0),
    ]

    names = [n for n, d in bodies.items() if "lon" in d]
    results = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            n1, n2 = names[i], names[j]
            lon1, lon2 = bodies[n1]["lon"], bodies[n2]["lon"]
            diff = abs(normalize_degree(lon1 - lon2))
            if diff > 180.0:
                diff = 360.0 - diff
            for asp_name, asp_angle in aspects_def:
                delta = abs(diff - asp_angle)
                if delta <= orb:
                    results.append({
                        "p1": n1, "p2": n2,
                        "aspect": asp_name,
                        "exact_angle": asp_angle,
                        "actual_angle": round(diff, 6),
                        "orb": round(delta, 6),
                    })
    return results


def calc_transit(birth_jd, now_jd, body_id, ephe_path="ephe"):
    """行星过境计算：计算某行星从出生到当前的移动。"""
    init_ephe(ephe_path)
    birth_pos = calc_planet(birth_jd, body_id)
    now_pos = calc_planet(now_jd, body_id)
    # calc_planet 返回 tuple: (lon, lat, dist, lon_speed, lat_speed, dist_speed)
    birth_lon, _, _, birth_speed = birth_pos[0], birth_pos[1], birth_pos[2], birth_pos[3]
    now_lon, _, _, now_speed = now_pos[0], now_pos[1], now_pos[2], now_pos[3]
    delta = normalize_degree(now_lon - birth_lon)
    return {
        "body": body_id,
        "birth_lon": round(birth_lon, 6),
        "now_lon": round(now_lon, 6),
        "delta": round(delta, 6),
        "birth_speed": round(birth_speed, 6),
        "now_speed": round(now_speed, 6),
    }


def solar_return(birth_jd, year, ephe_path="ephe"):
    """太阳返照计算：返回太阳回到出生位置的JD。
    birth_jd: 出生JD
    year: 目标年份
    """
    init_ephe(ephe_path)
    birth_sun = calc_planet(birth_jd, swe.SUN)
    target_sun_lon = birth_sun[0]

    # 从目标年年初开始搜索
    jan1 = jd_from_ymd_ut(year, 1, 1, 0.0)
    try:
        return_jd = find_date_at_sun_pos(target_sun_lon, jan1, backward=False, ephe_path=ephe_path)
    except Exception:
        # 回退：手动迭代搜索
        return_jd = _search_sun_pos(target_sun_lon, jan1, ephe_path)
    if return_jd is None:
        return None
    return_sun = calc_planet(return_jd, swe.SUN)
    return {
        "year": year,
        "return_jd": round(return_jd, 6),
        "sun_lon": round(return_sun[0], 6),
        "birth_sun_lon": round(target_sun_lon, 6),
        "delta": round(abs(normalize_degree(return_sun[0] - target_sun_lon)), 6),
    }


def _search_sun_pos(target_lon, start_jd, ephe_path="ephe", max_days=400):
    """回退方案：手动迭代搜索太阳到达目标经度的JD。"""
    init_ephe(ephe_path)
    # 使用 Moshier 回退模式（不需要星历文件）
    flag = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL
    try:
        flag_moshier = swe.FLG_MOSEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL
    except AttributeError:
        flag_moshier = flag
    jd = start_jd
    for _ in range(max_days * 2):
        try:
            xx, ret = swe.calc_ut(jd, swe.SUN, flag_moshier)
        except Exception:
            xx, ret = swe.calc_ut(jd, swe.SUN, flag)
        lon = xx[0]
        diff = normalize_degree(target_lon - lon)
        if abs(diff) < 0.01:
            return jd
        if diff > 180:
            diff -= 360
        jd += diff  # 太阳每天约1°
    return None


def calc_eclipse(jd, ephe_path="ephe"):
    """日月食状态判定。
    返回 {type: 'solar'/'lunar'/'none', details}
    """
    init_ephe(ephe_path)
    sun = calc_planet(jd, swe.SUN)
    moon = calc_planet(jd, swe.MOON)
    sun_lon, moon_lon = sun[0], moon[0]
    diff = abs(normalize_degree(moon_lon - sun_lon))

    # 合朔（日食可能）：diff ≈ 0
    # 望（月食可能）：diff ≈ 180
    is_new_moon = diff < 3.0
    is_full_moon = abs(diff - 180.0) < 3.0

    # 检查月亮纬度（简化判断：纬度接近0才可能发生食）
    moon_lat = moon[1]
    can_eclipse = abs(moon_lat) < 1.5

    result = {"type": "none", "sun_lon": round(sun_lon, 6), "moon_lon": round(moon_lon, 6),
              "moon_lat": round(moon_lat, 6), "separation": round(diff, 6)}

    if is_new_moon and can_eclipse:
        result["type"] = "solar"
        result["details"] = "日食可能（合朔+月亮纬度<1.5°）"
    elif is_full_moon and can_eclipse:
        result["type"] = "lunar"
        result["details"] = "月食可能（望+月亮纬度<1.5°）"
    elif is_new_moon:
        result["type"] = "new_moon"
        result["details"] = "合朔（无食）"
    elif is_full_moon:
        result["type"] = "full_moon"
        result["details"] = "望（无食）"

    return result

