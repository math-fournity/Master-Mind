#!/usr/bin/env python3
"""验证z3给出的6x6着色是否真的合法，并调试回溯搜索的bug。"""

def lattice_area2(p1, p2, p3):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def verify_coloring(W, H, coloring_grid):
    """验证一个着色是否合法（无同色面积-3三角形）。"""
    points = [(x, y) for x in range(W) for y in range(H)]
    # coloring_grid[y][x] = color
    violations = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if lattice_area2(points[i], points[j], points[k]) == 6:
                    p1, p2, p3 = points[i], points[j], points[k]
                    c1 = coloring_grid[p1[1]][p1[0]]
                    c2 = coloring_grid[p2[1]][p2[0]]
                    c3 = coloring_grid[p3[1]][p3[0]]
                    if c1 == c2 == c3:
                        violations.append((p1, p2, p3, c1))
    return violations

# z3给出的6x6着色（从y=5到y=0）
z3_6x6 = [
    [2, 0, 0, 2, 2, 0],  # y=5
    [0, 0, 2, 2, 0, 0],  # y=4
    [1, 1, 1, 1, 1, 1],  # y=3
    [1, 1, 2, 1, 1, 1],  # y=2
    [2, 0, 0, 2, 2, 0],  # y=1
    [0, 0, 2, 2, 0, 0],  # y=0
]

print("=== 验证z3给出的6x6着色 ===")
violations = verify_coloring(6, 6, z3_6x6)
if violations:
    print(f"  ILLEGAL: {len(violations)} monochromatic area-3 triangles found!")
    for v in violations[:10]:
        print(f"    {v}")
else:
    print(f"  LEGAL: No monochromatic area-3 triangles. z3 solution is correct!")

# 现在调试回溯搜索的bug
print("\n=== 调试回溯搜索 ===")

def backtracking_debug(W, H, timeout_nodes=10000000):
    points = [(x, y) for x in range(W) for y in range(H)]
    tris = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if lattice_area2(points[i], points[j], points[k]) == 6:
                    tris.append((i, j, k))
    
    print(f"  {W}x{H}: {len(points)} points, {len(tris)} triangles")
    
    # 按参与的三角形数量排序
    point_tris = {i: [] for i in range(len(points))}
    for tidx, (a, b, c) in enumerate(tris):
        point_tris[a].append(tidx)
        point_tris[b].append(tidx)
        point_tris[c].append(tidx)
    
    order = sorted(range(len(points)), key=lambda i: -len(point_tris[i]))
    print(f"  Order (first 10): {order[:10]}")
    print(f"  Points (first 10 in order): {[points[i] for i in order[:10]]}")
    print(f"  Triangle counts (first 10): {[len(point_tris[i]) for i in order[:10]]}")
    
    coloring = [-1] * len(points)
    nodes = [0]
    
    def is_valid(point_idx, color):
        nodes[0] += 1
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
            return True
        if nodes[0] > timeout_nodes:
            return None
        
        p = order[idx]
        for c in range(3):
            result = is_valid(p, c)
            if result:
                coloring[p] = c
                result = backtrack(idx + 1)
                if result is not None:
                    return result
                coloring[p] = -1
        return False
    
    result = backtrack(0)
    if result is None:
        print(f"  TIMEOUT")
    elif result:
        print(f"  SAT: Found valid coloring (explored {nodes[0]} nodes)")
        # Print coloring
        for y in range(H-1, -1, -1):
            row = ""
            for x in range(W):
                idx = points.index((x, y))
                row += str(coloring[idx]) + " "
            print(f"    {row}")
    else:
        print(f"  UNSAT (explored {nodes[0]} nodes)")
        # 调试：打印前几个点的着色尝试
        # 重新运行，打印决策过程
        coloring2 = [-1] * len(points)
        nodes2 = [0]
        depth = [0]
        
        def is_valid2(point_idx, color):
            for tidx in point_tris[point_idx]:
                a, b, c = tris[tidx]
                ca = coloring2[a] if a != point_idx else color
                cb = coloring2[b] if b != point_idx else color
                cc = coloring2[c] if c != point_idx else color
                if ca == cb == cc and ca != -1:
                    return False, (a, b, c)
            return True, None
        
        def backtrack2(idx, max_depth=20):
            if idx == len(order):
                return True
            if depth[0] >= max_depth:
                return None
            
            p = order[idx]
            for c in range(3):
                valid, conflict = is_valid2(p, c)
                if valid:
                    coloring2[p] = c
                    depth[0] += 1
                    if idx < 10:
                        print(f"    Try point {p} {points[p]} = color {c} (depth {depth[0]})")
                    result = backtrack2(idx + 1, max_depth)
                    if result is not None:
                        return result
                    coloring2[p] = -1
                    depth[0] -= 1
                else:
                    if idx < 10:
                        ca, cb, cc = conflict
                        print(f"    Point {p} {points[p]} = color {c} CONFLICT with tri {points[ca]},{points[cb]},{points[cc]}")
            return False
        
        backtrack2(0)

backtracking_debug(6, 6)
