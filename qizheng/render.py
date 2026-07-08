"""七政四余命盘文本渲染引擎。
将 build_chart 的 JSON 输出渲染为人类可读的纯文本命盘。
翻译 ChartData.showData 的文本输出部分（不依赖 GUI）。
"""
from qizheng.core import _load_shen_sha, normalize_degree, _lon_to_branch

# 行星中文名映射
_PLANET_CN = {
    "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
    "mercury": "水", "mars": "火", "saturn": "土",
    "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
    "mean_apog_ziqi": "炁", "oscu_apog_yuebei": "孛",
}

# 行星显示顺序
_PLANET_ORDER = [
    "sun", "moon", "mercury", "venus", "mars",
    "jupiter", "saturn",
    "inv_true_node_jidu", "true_node_rohuo",
    "mean_apog_ziqi", "oscu_apog_yuebei",
]

# 12宫名
_HOUSE_NAMES = [
    "命宫", "相貌", "福德", "官禄", "迁移", "疾厄",
    "夫妻", "奴仆", "男女", "田宅", "兄弟", "财帛",
]


def render_chart(chart_data, verbose=False):
    """渲染完整命盘文本。
    chart_data: build_chart 返回的 dict
    verbose: 是否显示详细信息（28宿宿度、宫位度数等）
    返回: 纯文本命盘字符串
    """
    lines = []
    data = _load_shen_sha()

    # === 基本信息 ===
    lines.append("=" * 60)
    lines.append(_center("七政四余命盘", 60))
    lines.append("=" * 60)
    lines.append("")

    # 出生信息
    input_data = chart_data.get("input", {})
    lines.append(f"出生: {input_data.get('date_ut', '?')}")
    loc = chart_data.get("input", {})
    if "lon" in loc:
        lines.append(f"经纬: {loc.get('lon', 0):.4f}, {loc.get('lat', 0):.4f}")
    lines.append("")

    # === 农历/四柱/八字 ===
    lunar = chart_data.get("lunar", {})
    four_poles = chart_data.get("four_poles", ["", "", "", ""])
    eight_char = chart_data.get("eight_char", {})
    rise_set = chart_data.get("rise_set", {})

    year_char = data.get("year_char", "年")
    month_char = data.get("month_char", "月")
    day_char = data.get("day_char", "日")
    hour_char = data.get("hour_char", "时")
    leap_char = data.get("leap", "闰")
    day_night = rise_set.get("day_night", "")

    # 阴历
    lunar_str = f"阴历: {_gan_zhi_str(four_poles[0])}{year_char} "
    if lunar.get("is_leap"):
        lunar_str += f"{leap_char}"
    lunar_str += f"{_chinese_number(lunar.get('lunar_month', 0))}{month_char} "
    lunar_str += f"{_chinese_number(lunar.get('lunar_day', 0))}{day_char} "
    if four_poles[3]:
        lunar_str += f"{four_poles[3][1]}{hour_char} ({day_night})"
    lines.append(lunar_str)

    # 干支
    sky_earths = data.get("sky_earths", "干支")
    lines.append(f"{sky_earths}: {_gan_zhi_str(four_poles[0])}{year_char} "
                 f"{_gan_zhi_str(four_poles[1])}{month_char} "
                 f"{_gan_zhi_str(four_poles[2])}{day_char} "
                 f"{_gan_zhi_str(four_poles[3])}{hour_char}")

    # 八字
    eight_chars_label = data.get("eight_characters", "八字")
    na_yin = eight_char.get("poles", [{}]*4)
    year_sound = na_yin[0].get("na_yin", "") if na_yin else ""
    lines.append(f"{eight_chars_label}: {_gan_zhi_str(four_poles[0])} "
                 f"{_gan_zhi_str(four_poles[1])} "
                 f"{_gan_zhi_str(four_poles[2])} "
                 f"{_gan_zhi_str(four_poles[3])} [{year_sound}]")

    # 弱宫/强宫
    star_signs = chart_data.get("star_signs", {})
    weak_houses = star_signs.get("weak_houses", [])
    solid_houses = star_signs.get("solid_houses", [])
    weak_label = data.get("weak", "虚")
    solid_label = data.get("solid", "实")
    house_label = data.get("zodiac_house", "宫")
    if weak_houses or solid_houses:
        wh = "".join(weak_houses[:4]) if weak_houses else ""
        sh = "".join(solid_houses[:4]) if solid_houses else ""
        lines.append(f"  {weak_label}{house_label}: {wh},  "
                     f"{solid_label}{house_label}: {sh}")

    # 出生季节
    birth_season = eight_char.get("birth_season", "")
    if birth_season:
        birth_at = data.get("birth_at", "生于")
        lines.append(f"{birth_at}: {birth_season}")

    lines.append("")

    # === 命主/身主 ===
    life_master_label = data.get("life_master", "命主")
    self_master_label = data.get("self_master", "身主")
    life_sign = chart_data.get("life_sign")
    self_sign = chart_data.get("self_sign")
    if life_sign is not None:
        lines.append(f"{life_master_label}: {_format_degree_with_mansion(life_sign, chart_data)}")
    if self_sign is not None:
        lines.append(f"{self_master_label}: {_format_degree_with_mansion(self_sign, chart_data)}")
    lines.append("")

    # === 行星位置表 ===
    lines.append("-" * 60)
    lines.append(_center("行星位置", 60))
    lines.append("-" * 60)

    bodies = chart_data.get("bodies", {})
    mansions = chart_data.get("mansions", {})
    dignities = chart_data.get("dignities", {})
    speed_states = chart_data.get("speed_states", {})

    for name in _PLANET_ORDER:
        if name not in bodies:
            continue
        body = bodies[name]
        if "lon" not in body:
            continue
        cn = _PLANET_CN.get(name, name)
        lon = body["lon"]
        branch = _lon_to_branch(lon)
        zodiac_name = _zodiac_name(lon)

        # 宿度
        man = mansions.get(name, {})
        mansion_name = man.get("mansion_name", "") if man else ""

        # 庙旺
        dig = dignities.get(name, {})
        states = dig.get("states", []) if dig else []
        state_str = "".join(states) if states else ""

        # 速度状态
        ss = speed_states.get(name, {})
        ss_name = ss.get("state_name", "") if ss else ""

        line = f"  {cn}  {_format_degree(lon)}  {zodiac_name}  "
        if mansion_name:
            line += f"{mansion_name}  "
        if state_str:
            line += f"[{state_str}]  "
        if ss_name and ss_name != "顺":
            line += f"({ss_name})"
        lines.append(line)

    lines.append("")

    # === 12宫位 ===
    lines.append("-" * 60)
    lines.append(_center("十二宫", 60))
    lines.append("-" * 60)

    houses = chart_data.get("houses", {})
    cusps = houses.get("cusps", [])
    for i, house_name in enumerate(_HOUSE_NAMES):
        if i < len(cusps):
            cusp = cusps[i]
            branch = _lon_to_branch(cusp)
            lines.append(f"  {house_name}: {_format_degree(cusp)}  {branch}宫")
    lines.append("")

    # === 神煞 ===
    if not verbose:
        # 简洁模式：只显示神煞总数
        star_table = star_signs.get("table", {})
        total_stars = sum(len(v) for v in star_table.values())
        lines.append(f"神煞: 共 {total_stars} 个")
    else:
        lines.append("-" * 60)
        lines.append(_center("神煞明细", 60))
        lines.append("-" * 60)
        star_table = star_signs.get("table", {})
        for pos in sorted(star_table.keys()):
            stars = star_table[pos]
            if stars:
                lines.append(f"  {pos}: {', '.join(stars)}")
    lines.append("")

    # === 限运 ===
    limits = chart_data.get("limits", {})
    if limits:
        lines.append("-" * 60)
        lines.append(_center("限运", 60))
        lines.append("-" * 60)
        for key, label in [("child_limit", "童限"), ("small_limit", "小限"),
                           ("fly_limit", "飞限"), ("month_limit", "月限")]:
            val = limits.get(key)
            if val:
                lines.append(f"  {label}: {val}")
        lines.append("")

    # === 流年 ===
    now_data = chart_data.get("now_data", {})
    if now_data:
        lines.append("-" * 60)
        lines.append(_center("流年", 60))
        lines.append("-" * 60)
        age = now_data.get("age", 0)
        year_pole = now_data.get("year_pole", "")
        lines.append(f"  年龄: {age}岁")
        lines.append(f"  流年: {_gan_zhi_str(year_pole)}{year_char}")
        year_stars = now_data.get("year_stars", {})
        if year_stars:
            stars_str = ", ".join(year_stars.values())
            lines.append(f"  年星: {stars_str}")
        ns_table = now_data.get("star_signs", {}).get("table", {})
        if ns_table:
            total_ns = sum(len(v) for v in ns_table.values())
            lines.append(f"  流年神煞: 共 {total_ns} 个")
        lines.append("")

    # === 规则引擎 ===
    rules_result = chart_data.get("rules", {})
    if isinstance(rules_result, dict):
        matched = rules_result.get("matched", [])
        total = rules_result.get("total", 0)
        lines.append("-" * 60)
        lines.append(_center(f"格局判定 ({len(matched)}/{total})", 60))
        lines.append("-" * 60)
        if matched:
            for r in matched:
                comment = r.get("comment", "")
                lines.append(f"  [{r['id']}] {r['name']}")
                if comment:
                    lines.append(f"        {comment}")
        else:
            lines.append("  （无匹配格局）")
        lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


def _center(text, width):
    """居中文本（中文按2宽度计算）。"""
    text_width = sum(2 if ord(c) > 127 else 1 for c in text)
    padding = max(0, (width - text_width) // 2)
    return " " * padding + text


def _gan_zhi_str(pole):
    """干支字符串，如"甲子"。"""
    if not pole or len(pole) < 2:
        return pole or ""
    return pole[:2]


def _chinese_number(n):
    """数字转中文（1-30）。"""
    if n == 0:
        return "初"
    cn_nums = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
               "十一", "十二", "十三", "十四", "十五", "十六", "十七",
               "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四",
               "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]
    if 1 <= n <= 30:
        return cn_nums[n - 1]
    return str(n)


def _format_degree(lon):
    """格式化黄经度数为 度分秒。"""
    lon = normalize_degree(lon)
    deg = int(lon)
    min_val = int((lon - deg) * 60)
    sec = int(((lon - deg) * 60 - min_val) * 60)
    return f"{deg:3d}°{min_val:02d}'{sec:02d}\""


def _format_degree_with_mansion(lon, chart_data):
    """格式化度数带28宿。"""
    lon = normalize_degree(lon)
    branch = _lon_to_branch(lon)
    zodiac = _zodiac_name(lon)
    return f"{_format_degree(lon)} {zodiac}"


def _zodiac_name(lon):
    """黄经 → 宫位名（如"戌火"）。"""
    data = _load_shen_sha()
    full_zodiac = data.get("full_zodiac", "").split(", ")
    idx = int(normalize_degree(lon) / 30.0) % 12
    if idx < len(full_zodiac):
        return full_zodiac[idx]
    return ""


# ---------- JSON 导出格式化 ----------

def export_json(chart_data, pretty=True):
    """导出格式化的 JSON 字符串。
    整理字段命名，增加中文字段注释，确保结构清晰。

    chart_data: build_chart 返回的 dict
    pretty: 是否美化输出（缩进）
    返回: JSON 字符串
    """
    import json

    # 构建规范化的输出结构
    output = {
        "meta": {
            "system": "七政四余推命系统",
            "version": "1.0",
            "generated_at": _now_str(),
        },
        "birth_info": _format_birth_info(chart_data),
        "lunar": _format_lunar(chart_data),
        "four_pillars": _format_four_pillars(chart_data),
        "eight_characters": _format_eight_characters(chart_data),
        "planets": _format_planets(chart_data),
        "houses": _format_houses(chart_data),
        "shen_sha": _format_shen_sha(chart_data),
        "limits": _format_limits_json(chart_data),
        "now_year": _format_now_year(chart_data),
        "patterns": _format_patterns(chart_data),
    }

    indent = 2 if pretty else None
    return json.dumps(output, ensure_ascii=False, indent=indent)


def _now_str():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _format_birth_info(chart_data):
    input_data = chart_data.get("input", {})
    rise_set = chart_data.get("rise_set", {})
    return {
        "date_ut": input_data.get("date_ut", ""),
        "jd": input_data.get("jd", 0),
        "longitude": input_data.get("lon", 0),
        "latitude": input_data.get("lat", 0),
        "altitude": input_data.get("alt", 0),
        "timezone": input_data.get("tz", ""),
        "is_day_birth": rise_set.get("is_day_birth"),
        "day_night": rise_set.get("day_night", ""),
        "sunrise_jd": rise_set.get("sunrise_jd"),
        "sunset_jd": rise_set.get("sunset_jd"),
    }


def _format_lunar(chart_data):
    lunar = chart_data.get("lunar", {})
    return {
        "lunar_year": lunar.get("lunar_year", ""),
        "lunar_month": lunar.get("lunar_month", 0),
        "lunar_day": lunar.get("lunar_day", 0),
        "is_leap": lunar.get("is_leap", False),
        "gan_zhi_year": lunar.get("gan_zhi_year", ""),
    }


def _format_four_pillars(chart_data):
    four_poles = chart_data.get("four_poles", ["", "", "", ""])
    labels = ["year", "month", "day", "hour"]
    cn_labels = ["年柱", "月柱", "日柱", "时柱"]
    result = {}
    for i, label in enumerate(labels):
        result[label] = {
            "name": cn_labels[i],
            "gan_zhi": four_poles[i] if i < len(four_poles) else "",
            "stem": four_poles[i][0] if i < len(four_poles) and four_poles[i] else "",
            "branch": four_poles[i][1] if i < len(four_poles) and len(four_poles[i]) > 1 else "",
        }
    return result


def _format_eight_characters(chart_data):
    eight_char = chart_data.get("eight_char", {})
    poles = eight_char.get("poles", [])
    result = {
        "day_master": eight_char.get("day_master", ""),
        "day_weak_house": eight_char.get("day_weak_house", ""),
        "birth_season": eight_char.get("birth_season", ""),
        "poles": [],
    }
    labels = ["year", "month", "day", "hour"]
    cn_labels = ["年柱", "月柱", "日柱", "时柱"]
    for i, pole_info in enumerate(poles):
        label = labels[i] if i < 4 else f"pole{i}"
        result["poles"].append({
            "name": cn_labels[i] if i < 4 else f"pole{i}",
            "ten_god": pole_info.get("ten_god", ""),
            "na_yin": pole_info.get("na_yin", ""),
            "long_life": pole_info.get("long_life", ""),
            "hidden_stems": pole_info.get("hidden_stems", ""),
        })
    return result


def _format_planets(chart_data):
    bodies = chart_data.get("bodies", {})
    mansions = chart_data.get("mansions", {})
    dignities = chart_data.get("dignities", {})
    speed_states = chart_data.get("speed_states", {})

    result = {}
    for name in _PLANET_ORDER:
        if name not in bodies:
            continue
        body = bodies[name]
        if "lon" not in body:
            continue
        cn = _PLANET_CN.get(name, name)
        man = mansions.get(name, {})
        dig = dignities.get(name, {})
        ss = speed_states.get(name, {})

        result[name] = {
            "chinese_name": cn,
            "longitude": round(body.get("lon", 0), 6),
            "latitude": round(body.get("lat", 0), 6),
            "distance": round(body.get("dist", 0), 6),
            "lon_speed": round(body.get("lon_speed", 0), 6),
            "zodiac": _zodiac_name(body.get("lon", 0)),
            "branch": _lon_to_branch(body.get("lon", 0)),
            "mansion": man.get("mansion_name", "") if man else "",
            "mansion_degree": round(man.get("mansion_degree", 0), 2) if man else 0,
            "dignity_states": dig.get("states", []) if dig else [],
            "speed_state": ss.get("state_name", "") if ss else "",
            "speed_state_code": ss.get("state", 0) if ss else 0,
        }
    return result


def _format_houses(chart_data):
    houses = chart_data.get("houses", {})
    cusps = houses.get("cusps", [])
    result = {
        "asc": round(houses.get("asc", 0), 6),
        "mc": round(houses.get("mc", 0), 6),
        "cusps": [],
    }
    for i, cusp in enumerate(cusps):
        if i < len(_HOUSE_NAMES):
            result["cusps"].append({
                "name": _HOUSE_NAMES[i],
                "longitude": round(cusp, 6),
                "branch": _lon_to_branch(cusp),
            })
    return result


def _format_shen_sha(chart_data):
    star_signs = chart_data.get("star_signs", {})
    table = star_signs.get("table", {})
    total = sum(len(v) for v in table.values())
    return {
        "total_count": total,
        "weak_houses": star_signs.get("weak_houses", []),
        "solid_houses": star_signs.get("solid_houses", []),
        "table": table,
    }


def _format_limits_json(chart_data):
    return chart_data.get("limits", {})


def _format_now_year(chart_data):
    now_data = chart_data.get("now_data", {})
    if not now_data:
        return {}
    ns_table = now_data.get("star_signs", {}).get("table", {})
    total_ns = sum(len(v) for v in ns_table.values())
    return {
        "age": now_data.get("age", 0),
        "year_pole": now_data.get("year_pole", ""),
        "four_poles": now_data.get("four_poles", []),
        "year_stars": now_data.get("year_stars", {}),
        "shen_sha_count": total_ns,
    }


def _format_patterns(chart_data):
    rules_result = chart_data.get("rules", {})
    if not isinstance(rules_result, dict):
        return {"matched_count": 0, "total": 0, "matched": []}
    matched = rules_result.get("matched", [])
    return {
        "matched_count": rules_result.get("matched_count", 0),
        "total": rules_result.get("total", 0),
        "matched": [
            {
                "id": r.get("id", ""),
                "name": r.get("name", ""),
                "comment": r.get("comment", ""),
            }
            for r in matched
        ],
    }
