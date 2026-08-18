#!/usr/bin/env python3
"""
检查周期为N的3-着色是否能避免面积为3的同色三角形。

关键理论：
对于周期N的着色 f(x,y) = g(x mod N, y mod N)，
面积为3的三角形存在当且仅当：
存在 a, d1, d2 使得 g(a) = g(a+d1 mod N) = g(a+d2 mod N)
且 |d1 × d2| = 6（其中 d1, d2 可以跨周期）。

对于周期N，d1 = r1 + N*k1, d2 = r2 + N*k2，
|d1 × d2| = |r1×r2 + N*(r1×k2 + k1×r2) + N²*(k1×k2)|
可达到的值模N为 r1×r2 mod N，但精确值需要更仔细分析。

简化方法：对于给定的周期N和着色g，
检查所有 a ∈ [0,N-1]² 和所有 d1, d2 ∈ [-M, M]²（M足够大）
是否满足 g(a)=g(a+d1)=g(a+d2) 且 |d1×d2|=6。
"""
import itertools
import sys

def cross(d1, d2):
    return d1[0]*d2[1] - d1[1]*d2[0]

def check_periodic_coloring(N, g, max_disp=None):
    """检查周期N的着色g是否有面积为3的同色三角形"""
    if max_disp is None:
        max_disp = max(6, N) + N  # 足够大

    # 预计算：对于每对残差类 (r1, r2)，是否存在 k1, k2 使得 |cross(r1+N*k1, r2+N*k2)| = 6
    # 简化：直接枚举 d1, d2 在 [-max_disp, max_disp] 范围内
    for a in itertools.product(range(N), repeat=2):
        ca = g[a[0]][a[1]]
        for d1 in itertools.product(range(-max_disp, max_disp+1), repeat=2):
            b = ((a[0]+d1[0]) % N, (a[1]+d1[1]) % N)
            cb = g[b[0]][b[1]]
            if cb != ca:
                continue
            if d1 == (0, 0):
                continue
            for d2 in itertools.product(range(-max_disp, max_disp+1), repeat=2):
                if d2 == (0, 0) or d2 == d1:
                    continue
                c = ((a[0]+d2[0]) % N, (a[1]+d2[1]) % N)
                cc = g[c[0]][c[1]]
                if cc != ca:
                    continue
                if abs(cross(d1, d2)) == 6:
                    return True, (a, d1, d2)
    return False, None

def check_all_period_N(N, max_disp=None):
    """检查所有周期N的3-着色"""
    total = 3 ** (N * N)
    print(f"Period {N}: {total} colorings to check")

    if total > 10**7:
        print(f"  Too many colorings, skipping.")
        return None

    found_valid = 0
    for idx, flat in enumerate(itertools.product(range(3), repeat=N*N)):
        g = [[flat[i*N + j] for j in range(N)] for i in range(N)]
        result, info = check_periodic_coloring(N, g, max_disp)
        if not result:
            found_valid += 1
            if found_valid <= 3:
                print(f"  Found valid coloring #{found_valid}: {flat}")
                for y in range(N-1, -1, -1):
                    row = " ".join(str(g[x][y]) for x in range(N))
                    print(f"    y={y}: {row}")
                if found_valid == 1:
                    return True, g  # 找到了避免面积3的着色

    if found_valid == 0:
        print(f"  NO valid coloring exists for period {N}!")
        print(f"  => Every period-{N} coloring has a mono area-3 triangle.")
        return False, None
    else:
        print(f"  Found {found_valid} valid colorings for period {N}.")
        return True, None

# 先检查 F_3^2 是否可以无单色线
def check_no_mono_line_F3():
    """检查 F_3^2 是否可以3-着色使得没有单色线"""
    print("=== 检查 F_3^2 是否可以无单色线 ===")
    # F_3^2 的所有线
    lines = []
    directions = [(1,0), (0,1), (1,1), (1,2)]
    for d in directions:
        for a in itertools.product(range(3), repeat=2):
            line = frozenset(
                tuple((a[0]+i*d[0]) % 3, (a[1]+i*d[1]) % 3) for i in range(3)
            )
            if line not in [frozenset(l) for l in lines]:
                lines.append(set(line))

    print(f"  {len(lines)} lines in F_3^2")

    count = 0
    for flat in itertools.product(range(3), repeat=9):
        count += 1
        coloring = {((i % 3, i // 3)): flat[i] for i in range(9)}
        # 检查是否有单色线
        has_mono = False
        for line in lines:
            colors = [coloring[p] for p in line]
            if colors[0] == colors[1] == colors[2]:
                has_mono = True
                break
        if not has_mono:
            print(f"  Found coloring with no monochromatic line: {flat}")
            g = [[flat[x + y*3] for y in range(3)] for x in range(3)]
            for y in range(2, -1, -1):
                row = " ".join(str(g[x][y]) for x in range(3))
                print(f"    y={y}: {row}")
            return True

    print(f"  No valid coloring exists (checked {count})")
    print(f"  => Every 3-coloring of F_3^2 has a monochromatic line")
    return False

if __name__ == "__main__":
    # 1. 检查 F_3^2 无单色线
    result = check_no_mono_line_F3()
    print()

    # 2. 检查周期2
    print("=== 检查周期2的着色 ===")
    check_all_period_N(2, max_disp=8)
    print()

    # 3. 检查周期3
    print("=== 检查周期3的着色 ===")
    check_all_period_N(3, max_disp=8)
