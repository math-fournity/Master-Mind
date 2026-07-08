#!/usr/bin/env python3
"""排盘小工具: 输入生辰 -> 输出完整七政四余星盘 JSON。
用法:
  chart.py --year 1990 --month 5 --day 15 --hour 3.5 --lon 116.4 --lat 39.9
  chart.py --json '{"year":1990,"month":5,"day":15,"hour":3.5,"lon":116.4,"lat":39.9}'
"""
import sys, json, argparse
from . import core
import swisseph as swe

def build_chart(y, mo, d, h, lon, lat, house="P", ephe="ephe", alt=0.0):
    """构建完整七政四余星盘。返回 dict。"""
    core.init_ephe(ephe)
    jd = core.jd_from_ymd_ut(y, mo, d, h)
    birth_date = [y, mo, d, int(h), int((h % 1) * 60)]

    # 1. 行星位置
    bodies = core.calc_all_bodies(jd)

    # 2. 宫位
    cusps, ascmc = core.calc_houses(jd, lat, lon, house)

    # 3. 升落 / 昼夜
    rise_set = core.calc_rise_set(jd, lon, lat, alt=alt, ephe_path=ephe)

    # 4. 农历
    lunar = core.solar_to_lunar(y, mo, d, h, ephe_path=ephe)

    # 5. 节气
    solar_terms = core.calc_solar_terms_v2(y, ephe_path=ephe)

    # 6. 命宫 / 身宫
    sun_pos = bodies["sun"]["lon"]
    moon_pos = bodies["moon"]["lon"]
    life_sign = core.calc_life_sign(birth_date, sun_pos, cusps)
    self_sign = core.calc_self_sign_v2(birth_date, moon_pos, sun_pos, lon, lat, ephe_path=ephe)

    # 7. 童限 / 大限
    child_limit_yr = core.calc_child_limit_years(life_sign)
    daxian_list = core.daxian_full(life_sign, child_limit_yr)

    # 当前所在大限（基于流年年龄）
    from datetime import datetime
    current_year = datetime.now().year
    age = current_year - y + 1  # 虚岁
    current_daxian = core.calc_daxian(life_sign, age, child_limit_yr)

    # 8. 二十八宿 / 速度状态 / 庙旺平陷
    mansions = {}
    speed_states = {}
    # 获取太阳黄经（用于伏/不见状态计算）
    sun_lon = bodies.get("sun", {}).get("lon")

    dignities = {}
    for name, data in bodies.items():
        if "lon" not in data:
            continue
        mansions[name] = core.calc_lunar_mansion(data["lon"])
        if "lon_speed" in data:
            speed_states[name] = core.calc_speed_state(
                name, data["lon_speed"], sun_lon=sun_lon, planet_lon=data["lon"])
        dignities[name] = core.calc_dignity_from_lon(name, data["lon"])

    # 9. 纳音五行（年命）+ 地支神煞
    na_yin = core.calc_na_yin_from_year(y)
    year_branch = na_yin["gan_zhi"][1]  # 干支第二个字是地支
    branch_stars_all = core.calc_branch_stars_for_all(year_branch)

    # 10. 各行星所在地的神煞
    branch_stars_for_bodies = {}
    for name, data in bodies.items():
        if "lon" not in data:
            continue
        body_branch = core._lon_to_branch(data["lon"])
        stars = core.calc_branch_stars(year_branch, body_branch)
        if stars:
            branch_stars_for_bodies[name] = {"branch": body_branch, "stars": stars}

    # 10b. 四柱干支 + 神煞完整体系 + 八字
    four_poles = core.calc_four_poles(y, mo, d, h)
    # sign_pos: [太阳黄经, 月亮黄经] 用于卦气计算
    sign_pos = None
    if "sun" in bodies and "lon" in bodies["sun"] and "moon" in bodies and "lon" in bodies["moon"]:
        sign_pos = [bodies["sun"]["lon"], bodies["moon"]["lon"]]
    day_birth = rise_set.get("is_day", True) if rise_set else True
    star_signs_result = core.get_star_signs(
        four_poles, sign_pos=sign_pos, day_pole=False,
        day_birth=day_birth, life_sign_pos=life_sign,
        birth_poles=four_poles)
    # 八字数据
    birth_date_arr = [y, mo, d, int(h), int((h % 1) * 60)]
    eight_char = core.compute_eight_char_data(four_poles, birth_date_arr)

    # 10c. 流年推演（当前年）
    from datetime import datetime
    current_year = datetime.now().year
    age = current_year - y + 1  # 虚岁
    now_data = core.compute_now_data(y, age, four_poles, life_sign)

    # 10d. 限运系统（童限/小限/飞限）
    limits = core.compute_limits(life_sign, age)

    # 11. 规则引擎判定
    chart_for_rules = {
        "bodies": bodies, "houses": {"cusps": cusps, "asc": ascmc[0], "mc": ascmc[1]},
        "lunar": lunar, "rise_set": rise_set, "dignities": dignities,
        "mansions": mansions, "life_sign": life_sign, "self_sign": self_sign,
        "input": {"date_ut": f"{y:04d}-{mo:02d}-{d:02d}T{h:07.4f}"},
    }
    rule_result = core.eval_rules(chart_for_rules)

    # 12. 组装输出
    out = {
        "input": {
            "date_ut": f"{y:04d}-{mo:02d}-{d:02d}T{h:07.4f}",
            "jd": round(jd, 6),
            "lon": lon, "lat": lat, "alt": alt,
            "ayanamsa": "Lahiri",
            "frame": "sidereal",
            "house_system": house,
        },
        "lunar": lunar,
        "na_yin": na_yin,
        "rise_set": rise_set,
        "solar_terms": solar_terms,
        "bodies": bodies,
        "mansions": mansions,
        "speed_states": speed_states,
        "dignities": dignities,
        "branch_stars": branch_stars_for_bodies,
        "four_poles": four_poles,
        "eight_char": eight_char,
        "star_signs": {
            "table": star_signs_result["table"],
            "weak_houses": star_signs_result["weak_houses"],
            "solid_houses": star_signs_result["solid_houses"],
        },
        "now_data": {
            "age": now_data["age"],
            "year_pole": now_data["year_pole"],
            "four_poles": now_data["four_poles"],
            "star_signs": now_data["star_signs"],
            "year_stars": now_data["year_info"]["year_stars"],
        },
        "limits": limits,
        "rules": rule_result,
        "houses": {
            "cusps": [round(c, 6) for c in cusps],
            "asc": round(ascmc[0], 6),
            "mc": round(ascmc[1], 6),
        },
        "life_sign": round(life_sign, 6),
        "self_sign": round(self_sign, 6),
        "child_limit_years": child_limit_yr,
        "daxian": daxian_list,
        "current_daxian": current_daxian,
        "daxian_stars": _compute_daxian_stars(current_daxian, life_sign, bodies),
    }
    return out


def _compute_daxian_stars(current_daxian, life_sign, bodies):
    """计算当前大限宫位内的行星。
    current_daxian: calc_daxian 返回的 dict
    life_sign: 命宫黄经
    bodies: 行星位置 dict
    返回: [行星名, ...] 在当前大限宫位内的行星列表
    """
    if not current_daxian:
        return []
    from qizheng.core import normalize_degree, _lon_to_branch
    # 当前大限的起始度数（相对于命宫）
    limit_start = current_daxian.get("limit_start_degree", 0)
    # 大限宫位绝对黄经 = 命宫 + 限内偏移
    limit_abs_start = normalize_degree(life_sign + limit_start)
    limit_abs_end = normalize_degree(limit_abs_start + 30.0)
    # 找出在该宫位范围内的行星
    stars = []
    for name, body in bodies.items():
        if "lon" not in body:
            continue
        lon = normalize_degree(body["lon"])
        # 检查是否在大限宫位范围内
        if limit_abs_start < limit_abs_end:
            if limit_abs_start <= lon < limit_abs_end:
                stars.append(name)
        else:  # 跨0°
            if lon >= limit_abs_start or lon < limit_abs_end:
                stars.append(name)
    return stars


def main():
    ap = argparse.ArgumentParser(description="七政四余排盘")
    ap.add_argument("--json", help="JSON 输入")
    ap.add_argument("--year", type=int)
    ap.add_argument("--month", type=int)
    ap.add_argument("--day", type=int)
    ap.add_argument("--hour", type=float, help="UT 小数")
    ap.add_argument("--lon", type=float, default=116.4)
    ap.add_argument("--lat", type=float, default=39.9)
    ap.add_argument("--alt", type=float, default=0.0)
    ap.add_argument("--house", default="P", help="宫位制 P/K/A/W 等")
    ap.add_argument("--ephe", default="ephe")
    args = ap.parse_args()

    if args.json:
        inp = json.loads(args.json)
    else:
        inp = {k: getattr(args, k) for k in ["year","month","day","hour","lon","lat","alt"]}
    y, mo, d, h = inp["year"], inp["month"], inp["day"], inp["hour"]
    lon = inp.get("lon", 116.4)
    lat = inp.get("lat", 39.9)
    alt = inp.get("alt", 0.0)

    out = build_chart(y, mo, d, h, lon, lat, args.house, args.ephe, alt)
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
