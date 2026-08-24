#!/usr/bin/env python3
"""
Find minimal subconfiguration of 7x5 grid that forces monochromatic area-3 triangle.
Also check various grid sizes to find the minimal one.
"""
from z3 import *
import itertools

def twice_area(p1, p2, p3):
    return abs((p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1]))

def find_triangles_in_set(point_set):
    """Find all area-3 triangles among a given set of points."""
    points = list(point_set)
    triangles = []
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if twice_area(points[i], points[j], points[k]) == 6:
                    triangles.append((i, j, k))
    return points, triangles

def check_point_set(point_set, timeout_ms=30000):
    """Check if a valid 3-coloring exists for the given point set."""
    points, triangles = find_triangles_in_set(point_set)
    s = Solver()
    s.set("timeout", timeout_ms)
    c = [Int(f'c_{i}') for i in range(len(points))]
    for i in range(len(points)):
        s.add(c[i] >= 0, c[i] <= 2)
    for (i, j, k) in triangles:
        s.add(Not(And(c[i] == c[j], c[j] == c[k])))
    result = s.check()
    if result == sat:
        return True, None
    elif result == unsat:
        return False, None
    else:
        return None, None

# Check various grid sizes
print("=== Checking grid sizes ===")
for (N, M) in [(6,5), (7,5), (8,5), (6,6), (7,6), (8,6), (5,7), (6,7), (7,7)]:
    pts = set((x,y) for x in range(N) for y in range(M))
    result, _ = check_point_set(pts, timeout_ms=60000)
    status = "SAT" if result else ("UNSAT" if result is False else "TIMEOUT")
    print(f"  Grid {N}x{M}: {status}")

# Try to find minimal subconfiguration of 7x5
print("\n=== Finding minimal subconfiguration of 7x5 ===")
full_pts = set((x,y) for x in range(7) for y in range(5))
result, _ = check_point_set(full_pts)
print(f"  Full 7x5: {'UNSAT' if not result else 'SAT'}")

# Try removing one point at a time
print("\n=== Try removing single points from 7x5 ===")
minimal_found = False
for pt in sorted(full_pts):
    subset = full_pts - {pt}
    result, _ = check_point_set(subset, timeout_ms=30000)
    status = "SAT" if result else ("UNSAT" if result is False else "TIMEOUT")
    if not result:  # Still UNSAT after removing this point
        print(f"  Remove {pt}: {status} (point not needed)")
    else:
        print(f"  Remove {pt}: {status} (point IS needed)")

# Check if only right triangles suffice
print("\n=== Check if only axis-aligned right triangles of area 3 suffice ===")
# Right triangles: (x,y), (x+a,y), (x,y+b) with a*b=6
# Types: (1,6), (2,3), (3,2), (6,1)
def find_right_triangles(N, M):
    points = [(x,y) for x in range(N) for y in range(M)]
    pt_set = set(points)
    triangles = []
    for (a,b) in [(1,6),(2,3),(3,2),(6,1)]:
        for (x,y) in points:
            if (x+a,y) in pt_set and (x,y+b) in pt_set:
                i = points.index((x,y))
                j = points.index((x+a,y))
                k = points.index((x,y+b))
                triangles.append((i,j,k))
    return points, triangles

for (N,M) in [(7,7),(8,7),(7,8),(10,10),(12,12)]:
    points, triangles = find_right_triangles(N,M)
    s = Solver()
    s.set("timeout", 60000)
    c = [Int(f'c_{i}') for i in range(len(points))]
    for i in range(len(points)):
        s.add(c[i] >= 0, c[i] <= 2)
    for (i,j,k) in triangles:
        s.add(Not(And(c[i]==c[j], c[j]==c[k])))
    result = s.check()
    status = "SAT" if result == sat else ("UNSAT" if result == unsat else "TIMEOUT")
    print(f"  Right triangles only, grid {N}x{M} ({len(triangles)} triangles): {status}")
