#!/usr/bin/env python3
"""
检查在给定网格中，是否存在3-着色使得没有同色面积为3/2的三角形。
如果不存在这样的着色（即所有3-着色都强制存在同色面积3/2三角形），
则证明了 S=3/2 对该网格成立，从而对整个 Z^2 成立。
"""
import itertools
import sys

def area_det(p1, p2, p3):
    """计算行列式 D = x1(y2-y3) + x2(y3-y1) + x3(y1-y2) 的绝对值"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def find_area_triangles(width, height, target_det):
    """找到网格 {0,...,width-1} x {0,...,height-1} 中行列式绝对值=target_det 的所有三角形"""
    points = [(i, j) for i in range(width) for j in range(height)]
    triangles = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                d = area_det(points[i], points[j], points[k])
                if d == target_det:
                    triangles.append((i, j, k))
    return points, triangles

def check_grid(width, height, target_det=3):
    """检查是否存在3-着色避免所有同色目标面积三角形"""
    points, triangles = find_area_triangles(width, height, target_det)
    n = len(points)
    print(f"Grid {width}x{height}: {n} points, {len(triangles)} triangles with |D|={target_det}")

    if len(triangles) == 0:
        print("  No target triangles found, skipping.")
        return True, None

    # 暴力枚举所有3^coloring
    # 对于小网格直接枚举
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
                print(f"  Found valid coloring #{count}: {coloring}")
                # 打印着色方案
                color_map = {points[idx]: coloring[idx] for idx in range(n)}
                for y in range(height-1, -1, -1):
                    row = ""
                    for x in range(width):
                        row += str(color_map[(x, y)]) + " "
                    print(f"    y={y}: {row}")
                return True, coloring

        print(f"  No valid coloring exists (checked {count} colorings)")
        return False, None
    else:
        print(f"  Grid too large for brute force ({n} points, 3^{n} colorings)")
        return None, None

if __name__ == "__main__":
    # 检查不同大小的网格
    grids = [
        (4, 2, 3),   # 4x2, 8 points
        (4, 3, 3),   # 4x3, 12 points
        (4, 4, 3),   # 4x4, 16 points
        (7, 2, 3),   # 7x2, 14 points
        (3, 3, 3),   # 3x3, 9 points
        (5, 3, 3),   # 5x3, 15 points
    ]

    for w, h, d in grids:
        result, coloring = check_grid(w, h, d)
        if result == False:
            print(f"  => Grid {w}x{h} FORCES a monochromatic area-{d/2} triangle!")
        elif result == True:
            print(f"  => Grid {w}x{h} admits a coloring avoiding monochromatic area-{d/2} triangles.")
        else:
            print(f"  => Grid {w}x{h} too large to check.")
        print()
