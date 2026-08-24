#!/usr/bin/env python3
"""
尝试找到更小的UNSAT配置。
1. 尝试特定的列子集（如列0,2,3,5,6）
2. 尝试从7x5中删除特定行/列
3. 提取z3 unsat core并分析
"""
from z3 import *
from itertools import combinations

def lattice_area2(p1, p2, p3):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def gen_tris(points):
    pts = list(points)
    tris = []
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            for k in range(j+1, len(pts)):
                if lattice_area2(pts[i], pts[j], pts[k]) == 6:
                    tris.append((pts[i], pts[j], pts[k]))
    return tris

def check_sat(points):
    tris = gen_tris(points)
    if not tris:
        return None, tris
    s = Solver()
    color = {p: Int(f"c_{p[0]}_{p[1]}") for p in points}
    for p in points:
        s.add(color[p] >= 0, color[p] <= 2)
    for tri in tris:
        p1, p2, p3 = tri
        s.add(Not(And(color[p1] == color[p2], color[p2] == color[p3])))
    result = s.check()
    return (result == unsat), tris

# 1. 尝试特定的列子集
print("=== 特定列子集（7x5网格的子集）===")
all_rows = range(5)
for cols in [(0,3,6), (0,2,3,6), (0,3,5,6), (0,2,4,6), (0,1,3,5,6), (0,2,3,4,6), (0,2,3,5,6), (0,1,3,4,6)]:
    points = [(x, y) for x in cols for y in all_rows]
    result, ntris = check_sat(points)
    status = "UNSAT" if result == True else ("SAT" if result == False else "NO_TRIS")
    print(f"  cols={cols}, {len(points)} pts, {ntris} tris: {status}")

# 2. 尝试特定的行子集
print("\n=== 特定行子集（7x5网格的子集）===")
all_cols = range(7)
for rows in [(0,1,2,3,4), (0,1,2,3), (0,1,3,4), (0,2,3,4), (1,2,3,4)]:
    points = [(x, y) for x in all_cols for y in rows]
    result, ntris = check_sat(points)
    status = "UNSAT" if result == True else ("SAT" if result == False else "NO_TRIS")
    print(f"  rows={rows}, {len(points)} pts, {ntris} tris: {status}")

# 3. 尝试3列x5行 + 额外点
print("\n=== 3列+额外点 ===")
base_cols = (0, 3, 6)
base_points = [(x, y) for x in base_cols for y in range(5)]
result, ntris = check_sat(base_points)
print(f"  Base (0,3,6)x5: {len(base_points)} pts, {ntris} tris: {'UNSAT' if result else 'SAT'}")

# 4. 尝试不同的列组合
print("\n=== 两列组合 ===")
for c1, c2 in [(0,6), (0,3), (3,6), (0,2), (2,6), (0,4), (4,6), (1,4), (2,5)]:
    points = [(x, y) for x in (c1, c2) for y in range(5)]
    result, ntris = check_sat(points)
    status = "UNSAT" if result == True else ("SAT" if result == False else "NO_TRIS")
    print(f"  cols=({c1},{c2}), {len(points)} pts, {ntris} tris: {status}")

# 5. 尝试更宽更矮的网格
print("\n=== 其他网格形状 ===")
for W, H in [(9, 3), (10, 3), (11, 3), (8, 4), (9, 4), (10, 4), (13, 2), (7, 5)]:
    points = [(x, y) for x in range(W) for y in range(H)]
    result, ntris = check_sat(points)
    status = "UNSAT" if result == True else ("SAT" if result == False else "NO_TRIS")
    print(f"  {W}x{H}, {len(points)} pts, {ntris} tris: {status}")

# 6. 尝试7x5删除单个点
print("\n=== 7x5删除单个点 ===")
full_points = [(x, y) for x in range(7) for y in range(5)]
for p in full_points:
    subset = [q for q in full_points if q != p]
    result, ntris = check_sat(subset)
    if result == False:  # SAT after removing this point
        print(f"  Removing {p}: SAT ({ntris} tris) — this point is critical!")
