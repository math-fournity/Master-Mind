"""七政四余核心计算库。
封装 swisseph 星历 + 命理常量 + 七政四余算法（恒星黄道、宫位、命宫、童限、大限、小限、飞限、节气、矫正反推）。
所有算法来自对 MOIRA Calculate.java / ChartData.java 的研究，用 Python 重写。
"""
import json, os
from datetime import datetime, timedelta
import swisseph as swe

_HERE = os.path.dirname(os.path.abspath(__file__))
_CONST_PATH = os.path.join(_HERE, "constants.json")

# 天体 ID 映射（七政 + 四余）
BODIES = {
    "sun":     swe.SUN,
    "moon":    swe.MOON,
    "mercury": swe.MERCURY,
    "venus":   swe.VENUS,
    "mars":    swe.MARS,
    "jupiter": swe.JUPITER,
    "saturn":  swe.SATURN,
    "true_node_rohuo":   swe.TRUE_NODE,   # 罗睺
    "mean_apog_ziqi":    swe.MEAN_APOG,   # 紫炁
    "oscu_apog_yuebei":  swe.OSCU_APOG,   # 月孛
}
# 计都 = 罗睺对宫
INV_TRUE_NODE = "inv_true_node_jidu"

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

def calc_all_bodies(jd, sidereal=True):
    """计算七政四余所有天体。返回 dict[name] -> {lon, lat, dist, *_speed}。"""
    out = {}
    for name, pid in BODIES.items():
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
    # 计都 = 罗睺 + 180
    rn = out.get("true_node_rohuo", {})
    if "lon" in rn:
        out[INV_TRUE_NODE] = {**rn, "lon": round(normalize_degree(rn["lon"] + 180.0), 6)}
    return out

# ---------- 宫位 ----------

def calc_houses(jd, lat, lon, house_system='P', sidereal=True):
    """计算 12 宫宫头 + ASC/MC。返回 (cusps, ascmc)。
    pyswisseph 的 houses() 不接受 flag 参数；sidereal 通过全局 set_sid_mode 生效。
    """
    cusps, ascmc = swe.houses(jd, lat, lon, house_system.encode())
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

    return {
        "sunrise_jd": round(rise_jd, 6) if rise_jd else None,
        "sunset_jd": round(set_jd, 6) if set_jd else None,
        "is_day_birth": is_day,
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

def calc_speed_state(planet_name, lon_speed):
    """计算行星逆顺迟疾状态。算法来自 Calculate.getSpeedState。
    返回 {state, state_name}
    state: 0=顺行快, 1=顺行慢, 2=留(迟), 3=逆行
    """
    c = _c()
    thresholds = c["speed_thresholds"]

    # 行星索引映射到 speed_thresholds 数组
    # speed_thresholds 数组顺序: [水星, 金星, 火星, 木星, 土星]（5个外行星）
    planet_idx_map = {
        "mercury": 0, "venus": 1, "mars": 2, "jupiter": 3, "saturn": 4
    }
    idx = planet_idx_map.get(planet_name)
    if idx is None:
        # 日月不逆行
        if planet_name in ("sun", "moon"):
            return {"state": 0, "state_name": "顺行"}
        return {"state": 0, "state_name": "顺行"}

    slow = thresholds["slow_speed"][idx]
    fast = thresholds["fast_speed"][idx]
    gap = thresholds["stationary_gap"][idx]

    abs_speed = abs(lon_speed)
    if lon_speed < 0:
        return {"state": 3, "state_name": "逆行"}
    elif abs_speed < gap:
        return {"state": 2, "state_name": "留"}
    elif abs_speed < slow:
        return {"state": 1, "state_name": "迟"}
    elif abs_speed > fast:
        return {"state": 0, "state_name": "疾"}
    else:
        return {"state": 0, "state_name": "顺"}

# ---------- 庙旺平陷（殿/垣/庙/旺/乐/喜/怒） ----------

# 行星名映射到 dignity_states 中的 key
_PLANET_DIGNITY_MAP = {
    "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
    "mercury": "水", "mars": "火", "saturn": "土",
    "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
    "mean_apog_ziqi": "炁", "oscu_apog_yuebei": "孛",
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

def calc_four_poles(year, month, day, hour_ut, solar_cal=None):
    """计算四柱干支（翻译 ChartData.chineseCalendar 的干支部分）。
    返回 ["年柱","月柱","日柱","时柱"]。

    year/month/day: 公历
    hour_ut: UT 小数
    solar_cal: [chinese_year_num, lunar_month] 或 None（自动计算）
    """
    data = _load_shen_sha()
    year_names = data.get('birth_year_names', '').split(', ')

    # 获取农历年序号和月序号
    if solar_cal is None:
        lunar = solar_to_lunar(year, month, day, hour_ut)
        if lunar is None:
            return ["", "", "", ""]
        solar_cal = [lunar.get('chinese_year_num', 1), lunar.get('lunar_month', 1)]

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
    # 23:00 后算下一日的天干（除非 switch_day_at_11_pm=0）
    if adj_hour == 23:
        y2 = (y2 + 1) % 10
    hour_index = (adj_hour + 1) // 2  # 子时=0, 丑时=1, ...
    h1 = (hour_index + _HOUR_SKY_POLE_SHIFTS[y2]) % 10
    h2 = (hour_index + _HOUR_EARTH_POLE_SHIFT) % 12
    hour_pole = _SKY_POLE_NAMES[h1] + _EARTH_POLE_NAMES_LIST[h2]

    return [year_pole, month_pole, day_pole, hour_pole]

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
        "mean_apog_ziqi": "炁", "oscu_apog_yuebei": "孛",
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

    return sym

def _planet_element(name):
    """行星→五行"""
    m = {
        "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
        "mercury": "水", "mars": "火", "saturn": "土",
        "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
        "mean_apog_ziqi": "炁", "oscu_apog_yuebei": "孛",
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
    """从星盘数据推导高级事实（会/拱/夹等）"""
    bodies = chart_data.get("bodies", {})
    facts = {}

    planet_pairs = [
        ("sun", "moon"), ("sun", "venus"), ("sun", "jupiter"),
        ("sun", "mercury"), ("sun", "mars"), ("sun", "saturn"),
        ("sun", "inv_true_node_jidu"), ("sun", "true_node_rohuo"),
        ("sun", "mean_apog_ziqi"), ("sun", "oscu_apog_yuebei"),
        ("moon", "venus"), ("moon", "jupiter"), ("moon", "mercury"),
        ("moon", "mars"), ("moon", "saturn"),
        ("moon", "inv_true_node_jidu"), ("moon", "true_node_rohuo"),
        ("moon", "mean_apog_ziqi"), ("moon", "oscu_apog_yuebei"),
        ("venus", "jupiter"), ("venus", "mercury"), ("venus", "mars"),
        ("venus", "saturn"), ("jupiter", "mercury"), ("jupiter", "mars"),
        ("jupiter", "saturn"), ("mercury", "mars"), ("mercury", "saturn"),
        ("mars", "saturn"),
    ]

    name_map = {
        "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
        "mercury": "水", "mars": "火", "saturn": "土",
        "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
        "mean_apog_ziqi": "炁", "oscu_apog_yuebei": "孛",
    }

    # 会（同宫）
    for p1, p2 in planet_pairs:
        n1, n2 = name_map.get(p1, p1), name_map.get(p2, p2)
        if _check_conjunction(bodies, p1, p2):
            facts[f"?{n1}{n2}会"] = "t"
            facts[f"?{n2}{n1}会"] = "t"

    return facts

def eval_rules(chart_data):
    """对星盘数据执行规则库判定。
    返回 {matched: [规则], total: N, matched_count: M}
    """
    rules = load_rules_library()
    sym = _build_symbol_table(chart_data)
    derived = _build_derived_facts(chart_data)
    sym.update(derived)

    matched = []
    for rule in rules:
        # 跳过模板规则（名称含 {} 占位符的）
        if "{" in rule["name"]:
            continue
        # 简化判定：只处理不含复杂语法的规则
        cond = rule["condition"]
        if not cond:
            continue
        # 尝试简单判定
        result = _eval_simple_condition(cond, sym)
        if result:
            matched.append({
                "id": rule["id"],
                "name": rule["name"],
                "priority": rule["priority"],
                "condition": cond,
                "comment": rule["comment"],
                "excludes": rule.get("excludes", []),
            })

    return {"matched": matched, "total": len(rules), "matched_count": len(matched)}

def _eval_simple_condition(cond, sym):
    """简化版条件求值器。
    支持: ?变量, & (与), | (或), ! (非), = (等于/集合包含)
    支持: @变量[0]=地支, @变量=@变量, %变量[0]=宿名
    不支持: 算术运算、函数调用、复杂集合操作
    """
    import re
    expr = cond.strip()
    if not expr:
        return False

    # 跳过含函数调用、__sp、复杂索引的规则
    if "&(" in expr or "__sp" in expr:
        return False
    # 跳过含 + - * / 算术的规则（如 @命+6=@日）
    if re.search(r'@\w+\s*[+\-*/]', expr):
        return False
    # 跳过含 ${...} 复杂变量的规则
    if "${" in expr:
        return False
    # 跳过含 @{...} 模板变量的规则
    if "@{" in expr:
        return False
    # 跳过含 %{...} 模板变量的规则
    if "%{" in expr:
        return False

    # 替换 ?{变量名} → True/False（规则引用）
    def replace_qref(m):
        var = m.group(1)
        val = sym.get(f"?{var}", "f")
        return "True" if val == "t" else "False"
    expr = re.sub(r'\?\{(\w+)\}', replace_qref, expr)

    # 替换 ?变量 → True/False
    def replace_qvar(m):
        var = m.group(1)
        val = sym.get(f"?{var}", "f")
        return "True" if val == "t" else "False"
    expr = re.sub(r'\?(\w+)', replace_qvar, expr)

    # 替换 @变量[0]=值 → 比较
    # 模式: @name[0]=value
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

    # 如果还有未替换的 @ % $ 变量，跳过
    if "@" in expr or "%" in expr or "$" in expr:
        return False

    # 替换逻辑运算符
    expr = expr.replace("&", " and ").replace("|", " or ")
    # 替换 ! 为 not（注意不要替换 != 中的 !）
    expr = re.sub(r'!(?!=)', " not ", expr)

    try:
        return bool(eval(expr))
    except Exception:
        return False
