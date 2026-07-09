"""铁板神数180年日历遍历枚举引擎。

替代原 tieban_enum.py 的暴力全乘法，改用按公历日历逐日遍历：
- 180年（3元 × 60年）≈ 65,745天
- 每天12时辰 × 8刻
- 同一八字×刻同时用南派/北派/江南派计算
- 结果存入SQLite

修复原 tieban_enum.py 的bug：
1. 月干由年干推出（五虎遁元），不是固定甲
2. 时干由日干推出（五鼠遁元），不是固定甲
3. 互卦用正确六爻计算，不是简化近似
4. 三元甲子正确纳入计算
"""
import sqlite3
import json
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from collections import Counter

from .core import (
    TIAN_GAN, DI_ZHI, JIAZI_60, GAN_INDEX, ZHI_INDEX, JIAZI_INDEX,
    wuhu_month_gan, wushu_hour_gan,
    get_yuan, yuan_ganzhi_num,
    algorithm_a, algorithm_b_xiantian, algorithm_b_houtian,
    expand_48, expand_96, gender_secret, kaoke_base,
    taixuan_pillar,
)
from .schools import get_school, SCHOOLS
from .corpus.lookup import load_corpus


# ============================================================
# 日柱计算（公历→六十甲子日）
# ============================================================

# 参考基准：1900年1月1日 = 甲子日（实际需验证）
# 用 datetime 计算天数差，再 mod 60
# 注意：1900年1月1日实际是庚子日，需要正确基准
# 已验证基准：2000年1月7日 = 甲子日
_DAY基准日期 = datetime(2000, 1, 7)
_DAY基准干支 = 0  # 甲子 = JIAZI_60[0]


def day_ganzhi(dt: datetime) -> str:
    """公历日期→日柱干支。

    用已知基准日推算：2000-01-07 = 甲子日。
    """
    delta = (dt - _DAY基准日期).days
    idx = (_DAY基准干支 + delta) % 60
    return JIAZI_60[idx]


def year_ganzhi(dt: datetime) -> str:
    """公历年份→年柱干支（简化：以立春为界，此处用近似）。

    精确计算需要节气，此处用简化近似：立春≈2月4日。
    """
    # 简化：立春前算上一年
    year = dt.year
    if dt.month < 2 or (dt.month == 2 and dt.day < 4):
        year -= 1

    # 年干支：以甲子年=1984为基准（也可用其他基准）
    base_year = 1984  # 甲子年
    delta = year - base_year
    idx = delta % 60
    return JIAZI_60[idx]


def month_ganzhi(year_gz: str, dt: datetime) -> str:
    """公历日期→月柱干支（简化：以节气为界，此处用近似月份）。

    精确计算需要节气，此处用简化近似：
    - 寅月(正月)≈2月4日-3月5日
    - 卯月(二月)≈3月6日-4月4日
    - ...
    """
    # 简化：按公历月份近似对应地支月
    # 寅月=正月≈公历2月, 卯月=二月≈3月, ..., 丑月=十二月≈1月
    month_to_zhi = {
        2: '寅', 3: '卯', 4: '辰', 5: '巳', 6: '午', 7: '未',
        8: '申', 9: '酉', 10: '戌', 11: '亥', 12: '子', 1: '丑',
    }
    month_zhi = month_to_zhi.get(dt.month, '寅')
    month_gan = wuhu_month_gan(year_gz[0], month_zhi)
    return f"{month_gan}{month_zhi}"


def hour_ganzhi(day_gz: str, hour: int) -> str:
    """小时数→时柱干支。

    hour: 0-23的小时数
    时辰：23-1=子, 1-3=丑, 3-5=寅, ..., 21-23=亥
    """
    # 小时→时支
    # 23:00-00:59=子(0), 01:00-02:59=丑(1), ..., 21:00-22:59=亥(11)
    zhi_idx = ((hour + 1) // 2) % 12
    hour_zhi = DI_ZHI[zhi_idx]

    # 时干由日干推出（五鼠遁元）
    hour_gan = wushu_hour_gan(day_gz[0], hour_zhi)
    return f"{hour_gan}{hour_zhi}"


def hour_zhi_name(hour: int) -> str:
    """小时数→时支名。"""
    zhi_idx = ((hour + 1) // 2) % 12
    return DI_ZHI[zhi_idx]


# ============================================================
# SQLite 持久化
# ============================================================

_SCHEMA = """
CREATE TABLE IF NOT EXISTS enum_result (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    year_gz TEXT NOT NULL,
    month_gz TEXT NOT NULL,
    day_gz TEXT NOT NULL,
    hour_gz TEXT NOT NULL,
    ke INTEGER NOT NULL,
    gender TEXT NOT NULL,
    yuan TEXT NOT NULL,
    school TEXT NOT NULL,
    base_num INTEGER,
    expanded_ids TEXT,
    detail TEXT
);

CREATE INDEX IF NOT EXISTS idx_enum_date ON enum_result(date);
CREATE INDEX IF NOT EXISTS idx_enum_year_gz ON enum_result(year_gz);
CREATE INDEX IF NOT EXISTS idx_enum_day_gz ON enum_result(day_gz);
CREATE INDEX IF NOT EXISTS idx_enum_school ON enum_result(school);
CREATE INDEX IF NOT EXISTS idx_enum_base_num ON enum_result(base_num);
"""


def init_db(db_path: str) -> sqlite3.Connection:
    """初始化SQLite数据库。"""
    conn = sqlite3.connect(db_path)
    conn.executescript(_SCHEMA)
    return conn


def save_result(conn: sqlite3.Connection, row: Dict):
    """保存单条枚举结果到数据库。"""
    conn.execute(
        """INSERT INTO enum_result
           (date, year_gz, month_gz, day_gz, hour_gz, ke, gender, yuan, school, base_num, expanded_ids, detail)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            row['date'], row['year_gz'], row['month_gz'], row['day_gz'], row['hour_gz'],
            row['ke'], row['gender'], row['yuan'], row['school'],
            row['base_num'], json.dumps(row['expanded_ids']), json.dumps(row['detail']),
        )
    )


# ============================================================
# 枚举主循环
# ============================================================

def enumerate_range(
    start_date: datetime,
    end_date: datetime,
    schools: List[str] = None,
    db_path: str = None,
    max_days: int = 0,
    verbose: bool = True,
) -> Dict:
    """按公历日历遍历指定日期范围，对每个八字×刻组合运行多学派推演。

    Args:
        start_date: 起始日期
        end_date: 结束日期
        schools: 学派列表（默认 ['nanpai', 'beipai']）
        db_path: SQLite数据库路径（None则不持久化）
        max_days: 最大天数限制（0=不限）
        verbose: 是否输出进度

    Returns:
        统计信息
    """
    if schools is None:
        schools = ['nanpai', 'beipai']

    school_instances = [get_school(s) for s in schools]
    school_names = [s.name() for s in school_instances]

    conn = None
    if db_path:
        conn = init_db(db_path)

    stats = {
        'total_configs': 0,
        'total_days': 0,
        'school_stats': {name: {'count': 0, 'base_nums': Counter()} for name in school_names},
        'yuan_stats': Counter(),
    }

    current = start_date
    day_count = 0
    t0 = time.time()

    while current <= end_date:
        if max_days > 0 and day_count >= max_days:
            break

        # 计算该日四柱
        year_gz_str = year_ganzhi(current)
        month_gz_str = month_ganzhi(year_gz_str, current)
        day_gz_str = day_ganzhi(current)

        # 三元甲子
        yuan = get_yuan(current.year)

        # 遍历12个时辰
        for hour in range(24):
            # 时辰只取12个（每2小时一个）
            if hour % 2 != 1 and hour != 23:
                continue

            hour_gz_str = hour_ganzhi(day_gz_str, hour)

            # 遍历8个刻
            for ke in range(1, 9):
                # 对每个学派计算
                for school_inst in school_instances:
                    school_name = school_inst.name()

                    # 男女各算一次
                    for gender in ['男', '女']:
                        # 调用学派推演
                        result = school_inst.deduce(
                            year_gz_str, month_gz_str, day_gz_str, hour_gz_str,
                            gender, yuan, ke
                        )

                        base_num = result['base']['base_num']
                        expanded = result['expanded']

                        # 保存到数据库
                        if conn:
                            save_result(conn, {
                                'date': current.strftime('%Y-%m-%d'),
                                'year_gz': year_gz_str,
                                'month_gz': month_gz_str,
                                'day_gz': day_gz_str,
                                'hour_gz': hour_gz_str,
                                'ke': ke,
                                'gender': gender,
                                'yuan': yuan,
                                'school': school_name,
                                'base_num': base_num,
                                'expanded_ids': expanded,
                                'detail': result['base'].get('detail', {}),
                            })

                        # 更新统计
                        stats['total_configs'] += 1
                        stats['school_stats'][school_name]['count'] += 1
                        stats['school_stats'][school_name]['base_nums'][base_num] += 1
                        stats['yuan_stats'][yuan] += 1

        day_count += 1
        stats['total_days'] = day_count

        # 进度输出
        if verbose and day_count % 1000 == 0:
            elapsed = time.time() - t0
            rate = day_count / elapsed if elapsed > 0 else 0
            print(f"  ... {day_count} 天 | {stats['total_configs']:,} 配置 | {rate:.1f} 天/秒 | {yuan}", file=sys.stderr)

        current += timedelta(days=1)

    if conn:
        conn.commit()
        conn.close()

    stats['elapsed_seconds'] = time.time() - t0
    return stats


def enumerate_180year(
    schools: List[str] = None,
    db_path: str = None,
    verbose: bool = True,
) -> Dict:
    """枚举完整180年周期（3元 × 60年）。

    默认范围：1864-01-01 至 2043-12-31
    """
    start = datetime(1864, 1, 1)
    end = datetime(2043, 12, 31)
    return enumerate_range(start, end, schools, db_path, verbose=verbose)


# ============================================================
# 查询函数
# ============================================================

def query_by_base_num(db_path: str, base_num: int, school: str = None) -> List[Dict]:
    """按基本数查询枚举结果。"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    if school:
        rows = conn.execute(
            "SELECT * FROM enum_result WHERE base_num=? AND school=?",
            (base_num, school)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM enum_result WHERE base_num=?",
            (base_num,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def query_by_date(db_path: str, date: str) -> List[Dict]:
    """按日期查询枚举结果。"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT * FROM enum_result WHERE date=?", (date,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def db_stats(db_path: str) -> Dict:
    """数据库统计信息。"""
    conn = sqlite3.connect(db_path)
    total = conn.execute("SELECT COUNT(*) FROM enum_result").fetchone()[0]
    schools = conn.execute(
        "SELECT school, COUNT(*) as cnt FROM enum_result GROUP BY school"
    ).fetchall()
    yuans = conn.execute(
        "SELECT yuan, COUNT(*) as cnt FROM enum_result GROUP BY yuan"
    ).fetchall()
    base_range = conn.execute(
        "SELECT MIN(base_num), MAX(base_num) FROM enum_result"
    ).fetchone()
    conn.close()
    return {
        'total': total,
        'by_school': {r[0]: r[1] for r in schools},
        'by_yuan': {r[0]: r[1] for r in yuans},
        'base_num_range': (base_range[0], base_range[1]),
    }


# ============================================================
# CLI 入口
# ============================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description='铁板神数180年日历遍历枚举引擎')
    parser.add_argument('--start', type=str, default='1864-01-01', help='起始日期')
    parser.add_argument('--end', type=str, default='2043-12-31', help='结束日期')
    parser.add_argument('--schools', nargs='+', default=['nanpai', 'beipai'],
                        help='学派列表（默认 nanpai beipai）')
    parser.add_argument('--db', type=str, default='dev-docs/tieban_enum.db', help='SQLite数据库路径')
    parser.add_argument('--max-days', type=int, default=0, help='最大天数限制（0=不限）')
    parser.add_argument('--query', type=str, help='查询模式：base_num=数字 或 date=YYYY-MM-DD')
    args = parser.parse_args()

    if args.query:
        # 查询模式
        if args.query.startswith('base_num='):
            num = int(args.query.split('=')[1])
            results = query_by_base_num(args.db, num)
        elif args.query.startswith('date='):
            date = args.query.split('=')[1]
            results = query_by_date(args.db, date)
        else:
            print("查询格式：base_num=数字 或 date=YYYY-MM-DD")
            return

        for r in results[:20]:
            print(f"  {r['date']} {r['year_gz']}{r['month_gz']}{r['day_gz']}{r['hour_gz']} 刻{r['ke']} "
                  f"{r['gender']} {r['yuan']} {r['school']}: 基本数={r['base_num']}")
        print(f"共 {len(results)} 条结果")
        return

    # 枚举模式
    start = datetime.strptime(args.start, '%Y-%m-%d')
    end = datetime.strptime(args.end, '%Y-%m-%d')

    print(f"=== 铁板神数枚举引擎 ===")
    print(f"日期范围: {args.start} ~ {args.end}")
    print(f"学派: {args.schools}")
    print(f"数据库: {args.db}")
    if args.max_days > 0:
        print(f"最大天数: {args.max_days}")
    print()

    stats = enumerate_range(start, end, args.schools, args.db, args.max_days)

    print(f"\n=== 枚举完成 ===")
    print(f"总天数: {stats['total_days']:,}")
    print(f"总配置数: {stats['total_configs']:,}")
    print(f"耗时: {stats['elapsed_seconds']:.1f}秒")
    for name, s in stats['school_stats'].items():
        print(f"  {name}: {s['count']:,} 配置")
    print(f"三元分布: {dict(stats['yuan_stats'])}")

    # 数据库统计
    if Path(args.db).exists():
        db_s = db_stats(args.db)
        print(f"\n数据库统计:")
        print(f"  总记录: {db_s['total']:,}")
        print(f"  基本数范围: {db_s['base_num_range']}")


if __name__ == '__main__':
    main()
