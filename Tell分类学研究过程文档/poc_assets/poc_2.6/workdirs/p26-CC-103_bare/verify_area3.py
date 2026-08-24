#!/usr/bin/env python3
"""
验证：在有限网格上，是否存在3-着色避免所有同色面积-3三角形。
如果不存在（UNSAT），则计算验证 A(3) = 3。
"""
from itertools import combinations
from z3 import *
import sys

def lattice_area(p1, p2, p3):
    """计算格点三角形面积的两倍（行列式绝对值）。"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def generate_area3_triangles(points):
    """枚举所有面积为3的三角形（|det|=6）。"""
    point_set = set(points)
    triangles = []
    pts = list(points)
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            for k in range(j+1, len(pts)):
                if lattice_area(pts[i], pts[j], pts[k]) == 6:
                    triangles.append((pts[i], pts[j], pts[k]))
    return triangles

def check_coloring(W, H):
    """检查 W×H 网格上是否存在3-着色避免同色面积-3三角形。"""
    points = [(x, y) for x in range(W) for y in range(H)]
    triangles = generate_area3_triangles(points)
    print(f"Grid {W}x{H}: {len(points)} points, {len(triangles)} area-3 triangles")

    if not triangles:
        print("  No area-3 triangles in this grid, skipping.")
        return None

    # z3 变量：每个点的颜色 (0, 1, 2)
    color = {}
    for p in points:
        color[p] = Int(f"c_{p[0]}_{p[1]}")

    s = Solver()
    # 每个点颜色在 {0,1,2}
    for p in points:
        s.add(color[p] >= 0, color[p] <= 2)

    # 约束：每个面积-3三角形不能三同色
    for tri in triangles:
        p1, p2, p3 = tri
        s.add(Not(And(color[p1] == color[p2], color[p2] == color[p3])))

    result = s.check()
    if result == sat:
        m = s.model()
        coloring = {}
        for p in points:
            coloring[p] = m[color[p]].as_long()
        print(f"  SAT: Found a valid 3-coloring avoiding monochromatic area-3 triangles!")
        return coloring
    else:
        print(f"  UNSAT: No valid 3-coloring exists. Every 3-coloring has a monochromatic area-3 triangle.")
        return None

def extract_config(W, H):
    """UNSAT时，尝试提取unsat core或关键子集。"""
    points = [(x, y) for x in range(W) for y in range(H)]
    triangles = generate_area3_triangles(points)

    # 尝试找到最小的点子集仍然UNSAT
    # 先尝试去掉边缘的点
    print(f"\n尝试寻找最小UNSAT子集...")

    # 尝试逐步缩小网格
    for w in range(W, 0, -1):
        for h in range(H, 0, -1):
            if w > W or h > H:
                continue
            sub_points = [(x, y) for x in range(w) for y in range(h)]
            sub_tris = generate_area3_triangles(sub_points)
            if not sub_tris:
                continue
            s = Solver()
            color = {}
            for p in sub_points:
                color[p] = Int(f"c_{p[0]}_{p[1]}")
                s.add(color[p] >= 0, color[p] <= 2)
            for tri in sub_tris:
                p1, p2, p3 = tri
                s.add(Not(And(color[p1] == color[p2], color[p2] == color[p3])))
            if s.check() == unsat:
                print(f"  {w}x{h} grid ({len(sub_points)} points, {len(sub_tris)} triangles): UNSAT")
                return w, h, sub_points, sub_tris
            # else continue
    return None

if __name__ == "__main__":
    # 从小到大尝试不同网格
    for W, H in [(7, 7), (7, 5), (5, 7), (6, 6), (7, 4), (4, 7), (8, 3), (3, 8), (7, 3), (3, 7)]:
        result = check_coloring(W, H)
        if result is not None:
            print(f"  Coloring found for {W}x{H}, printing:")
            for y in range(H-1, -1, -1):
                row = ""
                for x in range(W):
                    row += str(result[(x, y)]) + " "
                print(f"    {row}")
            print()
        else:
            print()
