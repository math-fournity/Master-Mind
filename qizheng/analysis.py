"""
分析函数封装（实战核心）
提供高层次的命理分析接口，供 AI 直接调用。
"""

from typing import Dict, Any, List


def analyze_daxian_limit(chart: Dict[str, Any], limit_index: int) -> Dict[str, Any]:
    """
    对指定大限进行综合分析（宫位/宫主/星曜/神煞/格局）。
    这是入口 5 逐限分析的核心函数。
    """
    if not chart.get('daxian') or limit_index < 0 or limit_index >= len(chart['daxian']):
        return {"error": "invalid limit_index"}

    limit_data = chart['daxian'][limit_index]
    start_deg = limit_data['start_degree']
    end_deg = limit_data['end_degree']

    # 1. 该限落在哪个宫位
    houses = chart.get('houses', {})
    limit_house = None
    for h in range(1, 13):
        h_start = houses.get(f'house{h}_cusp')
        if h_start is None:
            continue
        h_end = houses.get(f'house{(h % 12) + 1}_cusp') or (h_start + 30) % 360
        if (h_start <= start_deg < h_end) or (h_start > h_end and (start_deg >= h_start or start_deg < h_end)):
            limit_house = h
            break

    # 2. 落入该限的星曜
    bodies = chart.get('bodies', {})
    stars_in_limit = []
    for name, pos in bodies.items():
        if isinstance(pos, (int, float)) and start_deg <= pos < end_deg:
            stars_in_limit.append(name)

    # 3. 该限宫位的神煞
    star_signs = chart.get('star_signs', {})
    shen_sha = star_signs.get('table', {}).get(str(limit_house), []) if limit_house else []

    result = {
        "limit_index": limit_index,
        "age_range": f"{limit_data['age_start']:.1f}-{limit_data['age_end']:.1f}",
        "degree_range": f"{start_deg:.1f}°-{end_deg:.1f}°",
        "house": limit_house,
        "palace_lord": None,          # TODO: 实现宫主计算
        "dignity_of_lord": None,
        "stars_in_limit": stars_in_limit,
        "shen_sha_in_house": shen_sha,
        "triggered_rules": [],        # TODO: 对该限宫位重新 eval_rules
        "overall_judgment": "待AI综合判断（建议结合 current_daxian 和 daxian_stars）"
    }
    return result


def progress_daxian_years(chart: Dict[str, Any], age_start: float, age_end: float) -> List[Dict[str, Any]]:
    """对大限内年龄区间逐年推演。"""
    results = []
    for age in range(int(age_start), int(age_end) + 1):
        results.append({
            "age": age,
            "note": "调用 core.compute_now_data 叠加当前大限分析"
        })
    return results


def analyze_liunian(chart: Dict[str, Any], age: int) -> Dict[str, Any]:
    """对特定年龄（流年）做综合分析。"""
    return {
        "age": age,
        "taishui_relation": "待实现（年支与命宫关系）",
        "shen_sha_overlay": [],
        "daxian_overlay": [],
        "judgment": "待AI判断"
    }
