"""铁板神数 + 七政四余并行推演框架。

对同一出生时间同时运行铁板推演和七政排盘，对比两套系统的产出。
"""
import json
from datetime import datetime
from typing import Dict, Optional, List

from .core import (
    TIAN_GAN, DI_ZHI, JIAZI_60, GAN_INDEX, ZHI_INDEX,
    get_yuan, yuan_ganzhi_num,
    wuhu_month_gan, wushu_hour_gan,
    taixuan_pillar, algorithm_a, algorithm_b_xiantian, algorithm_b_houtian,
    expand_48, expand_96, gender_secret,
    GUA_WUXING, GAN_WUXING, ZHI_WUXING,
)
from .schools import get_school
from .corpus.lookup import get_entries_by_ids, get_entries_by_ids_text
from .enum_engine import year_ganzhi, month_ganzhi, day_ganzhi, hour_ganzhi


def parallel_deduction(
    year: int, month: int, day: int, hour: float,
    longitude: float, latitude: float,
    gender: str = '男',
    schools: List[str] = None,
    father_zhi: str = None,
    mother_zhi: str = None,
) -> Dict:
    """对同一出生时间同时运行铁板推演和七政排盘。

    Args:
        year, month, day: 公历出生日期
        hour: 出生时间（小数，如 3.5 = 凌晨3:30）
        longitude, latitude: 出生地经纬度
        gender: '男'/'女'
        schools: 铁板学派列表（默认 ['nanpai', 'beipai']）
        father_zhi: 父亲生肖（可选）
        mother_zhi: 母亲生肖（可选）

    Returns:
        {
            'input': 输入参数,
            'datetime': 出生时间,
            'four_poles': 四柱干支,
            'yuan': 三元甲子,
            'tieban': {school: 铁板推演结果},
            'qizheng': 七政命盘（build_chart输出）,
            'correspondence': 两套系统对应关系分析,
        }
    """
    if schools is None:
        schools = ['nanpai', 'beipai']

    # 构建datetime对象
    dt = datetime(year, month, day, int(hour), int((hour % 1) * 60))

    # 计算四柱
    year_gz = year_ganzhi(dt)
    month_gz = month_ganzhi(year_gz, dt)
    day_gz = day_ganzhi(dt)
    hour_gz = hour_ganzhi(day_gz, int(hour))

    # 三元甲子
    yuan = get_yuan(year)

    # === 铁板推演 ===
    tieban_results = {}
    for school_name in schools:
        school = get_school(school_name)
        result = school.deduce(
            year_gz, month_gz, day_gz, hour_gz,
            gender, yuan,
            father_zhi=father_zhi, mother_zhi=mother_zhi
        )
        tieban_results[school_name] = result

    # === 七政排盘 ===
    try:
        from qizheng.chart import build_chart
        qizheng_chart = build_chart(year, month, day, hour, longitude, latitude)
    except ImportError:
        qizheng_chart = {'error': 'qizheng.chart 不可用（需要 swisseph + .venv 环境）'}
    except Exception as e:
        qizheng_chart = {'error': str(e)}

    # === 对应关系分析 ===
    correspondence = _analyze_correspondence(tieban_results, qizheng_chart, gender)

    return {
        'input': {
            'year': year, 'month': month, 'day': day, 'hour': hour,
            'longitude': longitude, 'latitude': latitude,
            'gender': gender,
        },
        'datetime': dt.isoformat(),
        'four_poles': {
            'year': year_gz, 'month': month_gz,
            'day': day_gz, 'hour': hour_gz,
        },
        'yuan': yuan,
        'tieban': tieban_results,
        'qizheng': qizheng_chart,
        'correspondence': correspondence,
    }


def _analyze_correspondence(tieban_results: Dict, qizheng_chart: Dict, gender: str) -> Dict:
    """分析铁板条文与七政星盘的对应关系。"""
    analysis = {
        'summary': {},
        'details': [],
    }

    if 'error' in qizheng_chart:
        analysis['summary']['qizheng_error'] = qizheng_chart['error']
        return analysis

    # 提取七政关键信息
    try:
        qizheng_bodies = qizheng_chart.get('bodies', {})
        qizheng_houses = qizheng_chart.get('houses', {})
        qizheng_dignities = qizheng_chart.get('dignities', {})
        qizheng_rules = qizheng_chart.get('rules', {})
        qizheng_star_signs = qizheng_chart.get('star_signs', {})

        # 关键宫位
        life_sign = qizheng_chart.get('life_sign', 0)  # 命宫
        self_sign = qizheng_chart.get('self_sign', 0)  # 身宫

        analysis['summary']['qizheng_life_sign'] = life_sign
        analysis['summary']['qizheng_self_sign'] = self_sign
        analysis['summary']['matched_rules'] = len(qizheng_rules.get('matched', []))
    except Exception:
        analysis['summary']['qizheng_parse_error'] = '无法解析七政命盘'

    # 铁板条文覆盖分析
    for school_name, tb_result in tieban_results.items():
        base_num = tb_result['base']['base_num']
        expanded = tb_result['expanded']

        # 查找对应条文
        entries = get_entries_by_ids(expanded)
        entry_texts = [e['text'][:30] + ('...' if len(e['text']) > 30 else '') for e in entries[:5]]

        analysis['summary'][f'{school_name}_base_num'] = base_num
        analysis['summary'][f'{school_name}_expanded_count'] = len(expanded)
        analysis['summary'][f'{school_name}_sample_entries'] = entry_texts

    return analysis


def parallel_batch(
    birth_times: List[Dict],
    schools: List[str] = None,
) -> List[Dict]:
    """批量并行推演。

    Args:
        birth_times: [{year, month, day, hour, longitude, latitude, gender}, ...]
        schools: 铁板学派列表

    Returns:
        推演结果列表
    """
    results = []
    for bt in birth_times:
        result = parallel_deduction(
            year=bt['year'], month=bt['month'], day=bt['day'],
            hour=bt['hour'], longitude=bt['longitude'], latitude=bt['latitude'],
            gender=bt.get('gender', '男'), schools=schools,
            father_zhi=bt.get('father_zhi'), mother_zhi=bt.get('mother_zhi'),
        )
        results.append(result)
    return results


def format_report(result: Dict) -> str:
    """格式化并行推演报告为可读文本。"""
    lines = []
    lines.append("=" * 60)
    lines.append("铁板+七政并行推演报告")
    lines.append("=" * 60)

    inp = result['input']
    lines.append(f"\n出生时间: {inp['year']}-{inp['month']:02d}-{inp['day']:02d} {inp['hour']}")
    lines.append(f"出生地: 经度{inp['longitude']}, 纬度{inp['latitude']}")
    lines.append(f"性别: {inp['gender']}")

    fp = result['four_poles']
    lines.append(f"\n四柱: {fp['year']} {fp['month']} {fp['day']} {fp['hour']}")
    lines.append(f"三元: {result['yuan']}")

    # 铁板推演
    lines.append("\n--- 铁板神数 ---")
    for school_name, tb in result['tieban'].items():
        base_num = tb['base']['base_num']
        expanded = tb['expanded']
        entries = get_entries_by_ids(expanded)
        lines.append(f"\n【{school_name}】基本数: {base_num}")
        lines.append(f"  展开数序: {expanded}")
        lines.append(f"  对应条文:")
        for e in entries:
            age_str = f"（虚岁{'、'.join(str(a) for a in e['ages'])}）" if e['ages'] else ""
            lines.append(f"    {e['id']}：{age_str}{e['text']}")

    # 七政命盘
    lines.append("\n--- 七政四余 ---")
    qizheng = result['qizheng']
    if 'error' in qizheng:
        lines.append(f"  错误: {qizheng['error']}")
    else:
        bodies = qizheng.get('bodies', {})
        lines.append(f"  命宫黄经: {qizheng.get('life_sign', 'N/A')}")
        lines.append(f"  身宫黄经: {qizheng.get('self_sign', 'N/A')}")
        lines.append(f"  天体位置:")
        for name, data in bodies.items():
            if isinstance(data, dict):
                lines.append(f"    {name}: {data.get('lon', 0):.2f}°")
            else:
                lines.append(f"    {name}: {data}")

        rules = qizheng.get('rules', {})
        matched = rules.get('matched', [])
        lines.append(f"  匹配格局: {len(matched)}条")
        for rule in matched[:5]:
            if isinstance(rule, dict):
                lines.append(f"    [{rule.get('priority', '')}] {rule.get('name', '')}")
            else:
                lines.append(f"    {rule}")

    # 对应关系
    corr = result['correspondence']
    lines.append("\n--- 对应关系 ---")
    for k, v in corr.get('summary', {}).items():
        if isinstance(v, list):
            lines.append(f"  {k}:")
            for item in v:
                lines.append(f"    - {item}")
        else:
            lines.append(f"  {k}: {v}")

    return '\n'.join(lines)
