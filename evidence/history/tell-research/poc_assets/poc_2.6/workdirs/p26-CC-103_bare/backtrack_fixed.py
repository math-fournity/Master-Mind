#!/usr/bin/env python3
"""修复后的回溯搜索，交叉验证z3的7x5 UNSAT结果。"""

def lattice_area2(p1, p2, p3):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def backtracking_fixed(W, H, timeout_nodes=50000000):
    points = [(x, y) for x in range(W) for y in range(H)]
    tris = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if lattice_area2(points[i], points[j], points[k]) == 6:
                    tris.append((i, j, k))
    
    print(f"  {W}x{H}: {len(points)} points, {len(tris)} triangles")
    
    point_tris = {i: [] for i in range(len(points))}
    for tidx, (a, b, c) in enumerate(tris):
        point_tris[a].append(tidx)
        point_tris[b].append(tidx)
        point_tris[c].append(tidx)
    
    order = sorted(range(len(points)), key=lambda i: -len(point_tris[i]))
    coloring = [-1] * len(points)
    nodes = [0]
    
    def is_valid(point_idx, color):
        nodes[0] += 1
        if nodes[0] > timeout_nodes:
            return None
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
            valid = is_valid(p, c)
            if valid is None:
                return None
            if valid:
                coloring[p] = c
                result = backtrack(idx + 1)
                if result is True:
                    return True
                elif result is None:
                    return None
                # result is False: continue to next color
                coloring[p] = -1
        return False
    
    result = backtrack(0)
    if result is None:
        print(f"  TIMEOUT ({nodes[0]} nodes)")
        return None
    elif result:
        print(f"  SAT: Found valid coloring ({nodes[0]} nodes)")
        for y in range(H-1, -1, -1):
            row = ""
            for x in range(W):
                idx = points.index((x, y))
                row += str(coloring[idx]) + " "
            print(f"    {row}")
        return coloring
    else:
        print(f"  UNSAT: No valid coloring ({nodes[0]} nodes)")
        return None

print("=== 修复后的回溯搜索 ===")
print("\n7x5:")
backtracking_fixed(7, 5)

print("\n6x6 (应该SAT):")
backtracking_fixed(6, 6)

print("\n5x7:")
backtracking_fixed(5, 7)
