#!/usr/bin/env python3
"""
使用回溯+约束传播检查是否存在3-着色避免所有同色面积3三角形。
检查更大的网格。
"""
import sys
from itertools import combinations

def area_det(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def find_triangles(width, height, target_det):
    points = [(i, j) for i in range(width) for j in range(height)]
    point_idx = {p: i for i, p in enumerate(points)}
    triangles = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                d = area_det(points[i], points[j], points[k])
                if d == target_det:
                    triangles.append((i, j, k))
    return points, triangles

def solve(width, height, target_det, max_solutions=1):
    """回溯求解：是否存在3-着色避免所有同色target_det三角形"""
    points, triangles = find_triangles(width, height, target_det)
    n = len(points)
    print(f"Grid {width}x{height}: {n} points, {len(triangles)} triangles with |D|={target_det}")

    if len(triangles) == 0:
        print("  No target triangles.")
        return None

    # 为每个点构建相关的三角形列表
    point_tris = [[] for _ in range(n)]
    for t_idx, (i, j, k) in enumerate(triangles):
        point_tris[i].append(t_idx)
        point_tris[j].append(t_idx)
        point_tris[k].append(t_idx)

    # 着色状态
    coloring = [-1] * n
    solutions_found = []

    def is_valid(idx, color):
        """检查给点idx着color色是否违反约束"""
        for t_idx in point_tris[idx]:
            i, j, k = triangles[t_idx]
            # 检查这个三角形的三个点是否都着了相同颜色
            colors = []
            for p in (i, j, k):
                if p == idx:
                    colors.append(color)
                elif coloring[p] != -1:
                    colors.append(coloring[p])
                else:
                    colors.append(None)
            # 如果三个点都着了色且颜色相同，违反约束
            if all(c is not None for c in colors) and colors[0] == colors[1] == colors[2]:
                return False
        return True

    def backtrack(idx):
        if idx == n:
            solutions_found.append(coloring[:])
            return True  # 找到解

        for color in range(3):
            if is_valid(idx, color):
                coloring[idx] = color
                if backtrack(idx + 1):
                    return True
                coloring[idx] = -1
        return False

    result = backtrack(0)
    if result:
        print(f"  FOUND valid coloring avoiding area {target_det/2}:")
        color_map = {points[i]: solutions_found[0][i] for i in range(n)}
        for y in range(height-1, -1, -1):
            row = " ".join(str(color_map[(x, y)]) for x in range(width))
            print(f"    y={y}: {row}")
        return True
    else:
        print(f"  NO valid coloring - grid FORCES mono area-{target_det/2} triangle!")
        return False

if __name__ == "__main__":
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 6  # |D|=6 => area=3

    grids = [
        (4, 3),
        (5, 3),
        (7, 2),
        (7, 3),
        (4, 4),
        (5, 4),
        (7, 4),
        (10, 3),
        (13, 2),
    ]

    for w, h in grids:
        if w * h > 28:  # 跳过太大的
            print(f"Grid {w}x{h}: skipping (too large for backtracking)")
            continue
        result = solve(w, h, target)
        print()
        if result == False:
            print(f"*** S = {target/2} confirmed by grid {w}x{h}! ***")
            break
