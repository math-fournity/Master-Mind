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
        if nm_trimmed > winter_solstice_this + 5.0:
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
