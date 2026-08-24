#!/usr/bin/env python3
"""
在7x5网格UNSAT的基础上，寻找最小UNSAT子集和unsat core。
"""
from itertools import combinations
from z3 import *
import sys

def lattice_area2(p1, p2, p3):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def generate_area3_triangles(points):
    pts = list(points)
    tris = []
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            for k in range(j+1, len(pts)):
                if lattice_area2(pts[i], pts[j], pts[k]) == 6:
                    tris.append((pts[i], pts[j], pts[k]))
    return tris

def check_subset(points):
    tris = generate_area3_triangles(points)
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

def get_unsat_core(W, H):
    """获取unsat core——关键约束集合。"""
    points = [(x, y) for x in range(W) for y in range(H)]
    tris = generate_area3_triangles(points)
    print(f"Grid {W}x{H}: {len(points)} points, {len(tris)} triangles")

    s = Solver()
    color = {p: Int(f"c_{p[0]}_{p[1]}") for p in points}
    for p in points:
        s.add(color[p] >= 0, color[p] <= 2)
    
    # 为每个三角形约束命名，用于unsat core
    constraints = []
    for idx, tri in enumerate(tris):
        p1, p2, p3 = tri
        c = Bool(f"tri_{idx}")
        s.assert_and_track(Not(And(color[p1] == color[p2], color[p2] == color[p3])), f"tri_{idx}")
        constraints.append((idx, tri))
    
    result = s.check()
    if result == unsat:
        core = s.unsat_core()
        core_tris = []
        for c in core:
            name = str(c)
            idx = int(name.split("_")[1])
            core_tris.append(tris[idx])
        print(f"Unsat core: {len(core)} constraints (out of {len(tris)})")
        return core_tris
    return None

def find_minimal_subgrid():
    """尝试各种小网格，找最小UNSAT。"""
    # 尝试7x5的各种子网格
    configs = [
        (7, 5), (5, 7),
        (7, 5),  # 已知UNSAT
    ]
    
    # 尝试更小的
    for W, H in [(7, 5), (6, 5), (5, 6), (7, 4), (4, 7), (6, 4), (4, 6), (5, 5), (5, 4), (4, 5)]:
        points = [(x, y) for x in range(W) for y in range(H)]
        result, ntris = check_subset(points)
        status = "UNSAT" if result == True else ("SAT" if result == False else "NO_TRIS")
        print(f"  {W}x{H} ({len(points)} pts, {ntris} tris): {status}")

def find_minimal_point_subset(W, H, target_size=None):
    """从7x5网格中尝试删除点，找到仍UNSAT的最小子集。"""
    all_points = [(x, y) for x in range(W) for y in range(H)]
    is_unsat, tris = check_subset(all_points)
    if not is_unsat:
        print(f"  {W}x{H} is not UNSAT, can't reduce.")
        return
    
    print(f"\n从 {W}x{H} ({len(all_points)} points) 开始删点...")
    
    # 贪心删除：尝试删除每个点，如果仍UNSAT则删除
    current = set(all_points)
    changed = True
    while changed:
        changed = False
        for p in list(current):
            trial = current - {p}
            result, _ = check_subset(list(trial))
            if result == True:  # still UNSAT
                current = trial
                changed = True
                # print(f"  Removed {p}, now {len(current)} points, still UNSAT")
    
    print(f"  最小UNSAT子集: {len(current)} points")
    # 打印子集
    pts = sorted(current)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    print(f"  x range: {min(xs)}-{max(xs)}, y range: {min(ys)}-{max(ys)}")
    
    # 打印网格
    for y in range(max(ys), min(ys)-1, -1):
        row = ""
        for x in range(min(xs), max(xs)+1):
            if (x, y) in current:
                row += "X "
            else:
                row += ". "
        print(f"    {row}")
    
    # 统计这个子集中的面积-3三角形
    sub_tris = generate_area3_triangles(list(current))
    print(f"  Area-3 triangles in subset: {len(sub_tris)}")
    
    return current, sub_tris

if __name__ == "__main__":
    print("=== 最小网格搜索 ===")
    find_minimal_subgrid()
    
    print("\n=== 7x5 Unsat Core ===")
    core = get_unsat_core(7, 5)
    if core:
        # 统计core涉及的点
        core_points = set()
        for tri in core:
            core_points.update(tri)
        print(f"Core involves {len(core_points)} points")
        xs = [p[0] for p in core_points]
        ys = [p[1] for p in core_points]
        print(f"  x: {min(xs)}-{max(xs)}, y: {min(ys)}-{max(ys)}")
    
    print("\n=== 贪心删点（7x5）===")
    find_minimal_point_subset(7, 5)
