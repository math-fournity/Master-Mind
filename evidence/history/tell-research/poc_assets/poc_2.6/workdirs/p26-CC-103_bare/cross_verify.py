#!/usr/bin/env python3
"""
交叉验证7x5网格的UNSAT结果。
方法1: z3（已验证UNSAT）
方法2: 独立的回溯搜索
方法3: 验证三角形枚举的正确性
"""
from itertools import combinations, product
import random
import sys

def lattice_area2(p1, p2, p3):
    """面积的两倍（行列式绝对值）。"""
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def verify_triangle_enum():
    """验证三角形面积计算的正确性。"""
    # 已知面积-3三角形
    test_cases = [
        ((0,0), (6,0), (0,1), 6),   # 面积3, det=6
        ((0,0), (3,0), (0,2), 6),   # 面积3, det=6
        ((0,0), (2,0), (0,3), 6),   # 面积3, det=6
        ((0,0), (1,0), (0,6), 6),   # 面积3, det=6
        ((0,0), (1,0), (0,1), 1),   # 面积1/2, det=1
        ((0,0), (2,0), (0,1), 2),   # 面积1, det=2
        ((0,0), (6,0), (0,2), 12),  # 面积6, det=12
    ]
    print("=== 验证面积计算 ===")
    for p1, p2, p3, expected in test_cases:
        result = lattice_area2(p1, p2, p3)
        status = "OK" if result == expected else "FAIL"
        print(f"  {p1}, {p2}, {p3}: det={result}, expected={expected} [{status}]")

def backtracking_search(W, H, max_solutions=1, timeout_nodes=5000000):
    """纯Python回溯搜索3-着色。"""
    points = [(x, y) for x in range(W) for y in range(H)]
    tris = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if lattice_area2(points[i], points[j], points[k]) == 6:
                    tris.append((i, j, k))
    
    print(f"\n=== 回溯搜索 {W}x{H} ===")
    print(f"  {len(points)} points, {len(tris)} area-3 triangles")
    
    # 为每个点，找出它参与的所有三角形
    point_tris = {i: [] for i in range(len(points))}
    for tidx, (a, b, c) in enumerate(tris):
        point_tris[a].append(tidx)
        point_tris[b].append(tidx)
        point_tris[c].append(tidx)
    
    # 按参与的三角形数量排序（最多的先着色）
    order = sorted(range(len(points)), key=lambda i: -len(point_tris[i]))
    
    coloring = [-1] * len(points)
    nodes = [0]
    
    def is_valid(point_idx, color):
        """检查给point_idx着color色是否违反约束。"""
        nodes[0] += 1
        if nodes[0] > timeout_nodes:
            return None  # timeout
        for tidx in point_tris[point_idx]:
            a, b, c = tris[tidx]
            ca = coloring[a] if a != point_idx else color
            cb = coloring[b] if b != point_idx else color
            cc = coloring[c] if c != point_idx else color
            if ca == cb == cc and ca != -1:
                return False
        return True
    
    def backtrack(idx):
        if idx == len(order):
            return True  # 找到合法着色
        if nodes[0] > timeout_nodes:
            return None  # timeout
        
        p = order[idx]
        for c in range(3):
            result = is_valid(p, c)
            if result is None:
                return None
            if result:
                coloring[p] = c
                result = backtrack(idx + 1)
                if result is not None:
                    return result
                coloring[p] = -1
        return False
    
    result = backtrack(0)
    if result is None:
        print(f"  TIMEOUT ({timeout_nodes} nodes)")
        return None
    elif result:
        print(f"  SAT: Found valid coloring (explored {nodes[0]} nodes)")
        return coloring
    else:
        print(f"  UNSAT: No valid coloring exists (explored {nodes[0]} nodes)")
        return None

def random_search(W, H, attempts=100000):
    """随机搜索：尝试随机着色看是否能避免同色面积-3三角形。"""
    points = [(x, y) for x in range(W) for y in range(H)]
    tris = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if lattice_area2(points[i], points[j], points[k]) == 6:
                    tris.append((i, j, k))
    
    print(f"\n=== 随机搜索 {W}x{H} ({attempts} attempts) ===")
    print(f"  {len(points)} points, {len(tris)} area-3 triangles")
    
    found = 0
    for _ in range(attempts):
        coloring = [random.randint(0, 2) for _ in points]
        valid = True
        for a, b, c in tris:
            if coloring[a] == coloring[b] == coloring[c]:
                valid = False
                break
        if valid:
            found += 1
            print(f"  Found valid coloring!")
            return coloring
    
    print(f"  No valid coloring found in {attempts} attempts (expected if UNSAT)")
    return None

if __name__ == "__main__":
    verify_triangle_enum()
    
    # 交叉验证7x5
    result = backtracking_search(7, 5, timeout_nodes=10000000)
    
    # 也验证一个已知SAT的情况（6x6）
    result66 = backtracking_search(6, 6, timeout_nodes=1000000)
    
    # 随机搜索验证
    random_search(7, 5, attempts=500000)
