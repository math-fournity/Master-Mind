#!/usr/bin/env python3
"""
分析两个关键着色的面积集合交集，并检查是否能避免面积3。
"""
import itertools

def area_det(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

# 着色1: f(x,y) = (x+y) mod 3
# D ≡ 0 (mod 3), 面积 = |D|/2 是 3/2 的倍数
# 面积集合: {3/2, 3, 9/2, 6, 15/2, 9, ...}

# 着色2: f(x,y) = x mod 2  (2-着色，也是合法3-着色)
# D ≡ 0 (mod 2), 面积 = |D|/2 是整数
# 面积集合: {1, 2, 3, 4, 5, 6, ...}

# 交集: {3, 6, 9, 12, ...} = 3的正整数倍
# 所以 S >= 3

print("=== 面积集合分析 ===")
print("x+y mod 3 着色: 面积 ∈ {3k/2 : k >= 1} = {3/2, 3, 9/2, 6, ...}")
print("x mod 2 着色:   面积 ∈ {k : k >= 1} = {1, 2, 3, 4, 5, 6, ...}")
print("交集: {3, 6, 9, 12, ...} = 3的正整数倍")
print("所以 S >= 3")
print()

# 现在检查: 是否存在3-着色避免面积3?
# 即检查有限网格是否能强制存在同色面积3三角形

def find_triangles(width, height, target_det):
    points = [(i, j) for i in range(width) for j in range(height)]
    triangles = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                d = area_det(points[i], points[j], points[k])
                if d == target_det:
                    triangles.append((i, j, k))
    return points, triangles

def check_grid_avoid(width, height, target_det):
    """检查是否存在3-着色避免所有同色target_det三角形"""
    points, triangles = find_triangles(width, height, target_det)
    n = len(points)
    print(f"Grid {width}x{height}: {n} points, {len(triangles)} triangles with |D|={target_det} (area={target_det/2})")

    if len(triangles) == 0:
        print("  No target triangles found.")
        return None, None

    if n <= 16:
        count = 0
        for coloring in itertools.product(range(3), repeat=n):
            count += 1
            valid = True
            for (i, j, k) in triangles:
                if coloring[i] == coloring[j] == coloring[k]:
                    valid = False
                    break
            if valid:
                print(f"  Found valid coloring (#{count}): avoids all mono area-{target_det/2} triangles")
                color_map = {points[idx]: coloring[idx] for idx in range(n)}
                for y in range(height-1, -1, -1):
                    row = " ".join(str(color_map[(x, y)]) for x in range(width))
                    print(f"    y={y}: {row}")
                return True, coloring

        print(f"  NO valid coloring exists! (checked {count} colorings)")
        print(f"  => Grid {width}x{height} FORCES mono area-{target_det/2} triangle")
        return False, None
    else:
        print(f"  Too large for brute force ({n} points)")
        return None, None

print("=== 检查是否能避免面积3 (|D|=6) ===")
print()

grids = [
    (4, 3, 6),   # 4x3, 12 points
    (4, 4, 6),   # 4x4, 16 points
    (7, 2, 6),   # 7x2, 14 points
    (3, 3, 6),   # 3x3, 9 points
    (5, 3, 6),   # 5x3, 15 points
    (6, 3, 6),   # 6x3, 18 points - too large for brute force
]

for w, h, d in grids:
    result, coloring = check_grid_avoid(w, h, d)
    if result == False:
        print(f"  => S = {d/2} is forced by grid {w}x{h}!")
    elif result == True:
        print(f"  => Grid {w}x{h} can avoid area {d/2}")
    else:
        print(f"  => Could not determine for grid {w}x{h}")
    print()
