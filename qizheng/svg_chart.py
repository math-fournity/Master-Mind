"""七政四余命盘 SVG 图形渲染。

绘制12宫圆盘命盘，包含：
- 12宫位扇形（命宫/相貌/福德/...）
- 11颗行星位置标记
- 28宿外圈
- 行星状态颜色编码
- 神煞标注

用法:
    from qizheng.chart import build_chart
    from qizheng.svg_chart import render_svg
    chart = build_chart(1990, 5, 15, 3.5, 116.4, 39.9)
    svg = render_svg(chart)
    with open("chart.svg", "w") as f:
        f.write(svg)
"""
import math
from qizheng.core import normalize_degree, _lon_to_branch, _load_shen_sha

# 行星中文名
_PLANET_CN = {
    "sun": "日", "moon": "月", "venus": "金", "jupiter": "木",
    "mercury": "水", "mars": "火", "saturn": "土",
    "inv_true_node_jidu": "计", "true_node_rohuo": "罗",
    "mean_apog_ziqi": "炁", "mean_apog_yuebei": "孛",
}

# 行星颜色
_PLANET_COLOR = {
    "sun": "#FF6B00", "moon": "#4A90D9", "venus": "#D4AF37",
    "jupiter": "#7B8B6F", "mercury": "#5B9BD5", "mars": "#C0392B",
    "saturn": "#7F8C8D", "inv_true_node_jidu": "#8E44AD",
    "true_node_rohuo": "#E74C3C", "mean_apog_ziqi": "#2C3E50",
    "mean_apog_yuebei": "#34495E",
}

# 12宫名
_HOUSE_NAMES = [
    "命宫", "相貌", "福德", "官禄", "迁移", "疾厄",
    "夫妻", "奴仆", "男女", "田宅", "兄弟", "财帛",
]

# 12地支
_BRANCHES = ["戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥"]


def render_svg(chart_data, size=600):
    """渲染 SVG 命盘。
    chart_data: build_chart 返回的 dict
    size: SVG 画布尺寸（正方形）
    返回: SVG 字符串
    """
    cx, cy = size / 2, size / 2
    r_outer = size * 0.45       # 外圈（28宿）
    r_zodiac = size * 0.40      # 黄道12宫圈
    r_house = size * 0.32       # 12宫位圈
    r_inner = size * 0.15       # 内圈（中心信息）

    bodies = chart_data.get("bodies", {})
    mansions = chart_data.get("mansions", {})
    speed_states = chart_data.get("speed_states", {})
    dignities = chart_data.get("dignities", {})
    houses = chart_data.get("houses", {})
    cusps = houses.get("cusps", [])
    life_sign = chart_data.get("life_sign", 0)
    four_poles = chart_data.get("four_poles", ["", "", "", ""])
    rules = chart_data.get("rules", {})
    matched = rules.get("matched", []) if isinstance(rules, dict) else []

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">')
    parts.append(f'<rect width="{size}" height="{size}" fill="#FAFAF5"/>')

    # === 12宫位扇形 ===
    life_idx = int(normalize_degree(life_sign) / 30.0) % 12 if life_sign else 0
    for i in range(12):
        # 从命宫开始，逆时针排列
        branch_idx = (life_idx - i) % 12
        start_angle = branch_idx * 30 - 90  # 从上方开始
        end_angle = (branch_idx + 1) * 30 - 90

        # 扇形路径
        x1 = cx + r_house * math.cos(math.radians(start_angle))
        y1 = cy + r_house * math.sin(math.radians(start_angle))
        x2 = cx + r_house * math.cos(math.radians(end_angle))
        y2 = cy + r_house * math.sin(math.radians(end_angle))
        x3 = cx + r_zodiac * math.cos(math.radians(end_angle))
        y3 = cy + r_zodiac * math.sin(math.radians(end_angle))
        x4 = cx + r_zodiac * math.cos(math.radians(start_angle))
        y4 = cy + r_zodiac * math.sin(math.radians(start_angle))

        # 交替背景色
        fill = "#F0F0E8" if i % 2 == 0 else "#E8E8E0"
        parts.append(f'<path d="M {x1:.1f} {y1:.1f} A {r_house:.1f} {r_house:.1f} 0 0 1 {x2:.1f} {y2:.1f} L {x3:.1f} {y3:.1f} A {r_zodiac:.1f} {r_zodiac:.1f} 0 0 0 {x4:.1f} {y4:.1f} Z" fill="{fill}" stroke="#999" stroke-width="0.5"/>')

        # 宫位名标签
        mid_angle = (start_angle + end_angle) / 2
        label_r = (r_house + r_zodiac) / 2
        lx = cx + label_r * math.cos(math.radians(mid_angle))
        ly = cy + label_r * math.sin(math.radians(mid_angle))
        house_name = _HOUSE_NAMES[i]
        parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="11" fill="#333" font-family="serif">{house_name}</text>')

    # === 12地支圈 ===
    for i in range(12):
        angle = i * 30 - 90 + 15  # 每宫中心
        br = r_zodiac + 15
        bx = cx + br * math.cos(math.radians(angle))
        by = cy + br * math.sin(math.radians(angle))
        parts.append(f'<text x="{bx:.1f}" y="{by:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="10" fill="#666" font-family="serif">{_BRANCHES[i]}</text>')

    # === 外圈 ===
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r_outer}" fill="none" stroke="#333" stroke-width="1.5"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r_zodiac}" fill="none" stroke="#999" stroke-width="0.5"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r_house}" fill="none" stroke="#999" stroke-width="0.5"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r_inner}" fill="#FAFAF5" stroke="#333" stroke-width="1"/>')

    # === 行星位置标记 ===
    planet_order = ["sun", "moon", "mercury", "venus", "mars",
                    "jupiter", "saturn", "inv_true_node_jidu",
                    "true_node_rohuo", "mean_apog_ziqi", "mean_apog_yuebei"]

    # 按黄经分组，避免重叠
    planet_positions = []
    for name in planet_order:
        if name not in bodies or "lon" not in bodies[name]:
            continue
        lon = normalize_degree(bodies[name]["lon"])
        planet_positions.append((name, lon))

    # 排序并调整位置避免重叠
    planet_positions.sort(key=lambda x: x[1])

    for name, lon in planet_positions:
        angle = lon - 90  # 从上方开始
        pr = r_house - 20  # 行星标记半径
        px = cx + pr * math.cos(math.radians(angle))
        py = cy + pr * math.sin(math.radians(angle))

        cn = _PLANET_CN.get(name, name)
        color = _PLANET_COLOR.get(name, "#333")

        # 速度状态
        ss = speed_states.get(name, {})
        state_name = ss.get("state_name", "")
        # 逆行标记
        is_retro = state_name in ("逆", "留")

        # 行星圆圈
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="10" fill="{color}" opacity="0.8"/>')
        parts.append(f'<text x="{px:.1f}" y="{py:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="11" fill="white" font-weight="bold" font-family="serif">{cn}</text>')

        # 逆行标记
        if is_retro:
            parts.append(f'<text x="{px+12:.1f}" y="{py-8:.1f}" font-size="8" fill="#C0392B" font-family="serif">R</text>')

        # 庙旺标记
        dig = dignities.get(name, {})
        states = dig.get("states", []) if dig else []
        if states:
            state_str = "".join(states[:2])
            parts.append(f'<text x="{px:.1f}" y="{py+18:.1f}" text-anchor="middle" font-size="7" fill="#666" font-family="serif">{state_str}</text>')

    # === 28宿外圈标记 ===
    for name in planet_order:
        if name not in mansions:
            continue
        man = mansions[name]
        man_name = man.get("mansion_name", "")
        if not man_name:
            continue
        lon = normalize_degree(bodies.get(name, {}).get("lon", 0))
        angle = lon - 90
        mr = r_outer - 12
        mx = cx + mr * math.cos(math.radians(angle))
        my = cy + mr * math.sin(math.radians(angle))
        parts.append(f'<text x="{mx:.1f}" y="{my:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="7" fill="#888" font-family="serif">{man_name}</text>')

    # === 中心信息 ===
    fp_str = " ".join(four_poles) if four_poles else ""
    parts.append(f'<text x="{cx}" y="{cy-15}" text-anchor="middle" font-size="10" fill="#333" font-family="serif">{fp_str}</text>')

    # 匹配格局数
    mc = len(matched)
    parts.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" font-size="9" fill="#666" font-family="serif">格局 {mc}条</text>')

    # 命宫地支
    life_branch = _lon_to_branch(life_sign) if life_sign else ""
    parts.append(f'<text x="{cx}" y="{cy+15}" text-anchor="middle" font-size="10" fill="#C0392B" font-weight="bold" font-family="serif">命{life_branch}</text>')

    # === 命宫标记线 ===
    if life_sign:
        angle = normalize_degree(life_sign) - 90
        lx = cx + r_outer * math.cos(math.radians(angle))
        ly = cy + r_outer * math.sin(math.radians(angle))
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="#C0392B" stroke-width="1" opacity="0.3"/>')

    parts.append('</svg>')
    return "\n".join(parts)
