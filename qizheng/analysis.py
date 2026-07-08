"""
分析函数封装（实战核心）
提供高层次的命理分析接口，供 AI 直接调用。
"""

from typing import Dict, Any, List


def _get_house_for_degree(cusps: List[float], degree: float) -> int:
    """根据 cusps 列表判断黄经落在哪个宫。"""
    for i in range(12):
        start = cusps[i]
        end = cusps[(i + 1) % 12]
        if start <= end:
            if start <= degree < end:
                return i + 1
        else:  # 跨 0 度
            if degree >= start or degree < end:
                return i + 1
    return 1


def analyze_daxian_limit(chart: Dict[str, Any], limit_index: int) -> Dict[str, Any]:
    """
    对指定大限进行综合分析（宫位/宫主/星曜/神煞/格局）。
    """
    if not chart.get('daxian') or limit_index < 0 or limit_index >= len(chart['daxian']):
        return {"error": "invalid limit_index"}

    limit_data = chart['daxian'][limit_index]
    start_deg = limit_data['start_degree']
    end_deg = limit_data['end_degree']

    # 1. 宫位
    cusps = chart.get('houses', {}).get('cusps', [])
    limit_house = _get_house_for_degree(cusps, start_deg) if cusps else None

    # 2. 落入该限的星曜
    bodies = chart.get('bodies', {})
    stars_in_limit = [name for name, pos in bodies.items()
                      if isinstance(pos, (int, float)) and start_deg <= pos < end_deg]

    # 3. 神煞
    star_signs = chart.get('star_signs', {})
    shen_sha = star_signs.get('table', {}).get(str(limit_house), []) if limit_house else []

    result = {
        "limit_index": limit_index,
        "age_range": f"{limit_data['age_start']:.1f}-{limit_data['age_end']:.1f}",
        "degree_range": f"{start_deg:.1f}°-{end_deg:.1f}°",
        "house": limit_house,
        "stars_in_limit": stars_in_limit,
        "shen_sha_in_house": shen_sha,
        "overall_judgment": "待AI综合判断"
    }
    return result


def progress_daxian_years(chart: Dict[str, Any], age_start: float, age_end: float) -> List[Dict[str, Any]]:
    return [{"age": age, "note": "叠加当前大限"} for age in range(int(age_start), int(age_end) + 1)]


def analyze_liunian(chart: Dict[str, Any], age: int) -> Dict[str, Any]:
    return {"age": age, "judgment": "待AI判断"}
