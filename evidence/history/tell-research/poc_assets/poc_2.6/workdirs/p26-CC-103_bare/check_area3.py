#!/usr/bin/env python3
"""
Check if a 3-coloring of a finite grid can avoid all monochromatic
triangles of area 3. If UNSAT for a large enough grid, then A(3) = 3.
"""
from z3 import *
import sys

def twice_area(p1, p2, p3):
    """Twice the signed area (absolute value)."""
    return abs((p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1]))

def find_triangles(N, M=None):
    """Find all triangles of area 3 (twice_area = 6) in an N x M grid."""
    if M is None:
        M = N
    points = [(x, y) for x in range(N) for y in range(M)]
    triangles = []
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if twice_area(points[i], points[j], points[k]) == 6:
                    triangles.append((i, j, k))
    return points, triangles

def check_grid(N, M=None, verbose=True):
    """Check if a valid 3-coloring exists for the grid."""
    if M is None:
        M = N
    points, triangles = find_triangles(N, M)
    if verbose:
        print(f"Grid {N}x{M}: {len(points)} points, {len(triangles)} area-3 triangles", flush=True)

    s = Solver()
    s.set("timeout", 120000)  # 2 minute timeout
    c = [Int(f'c_{i}') for i in range(len(points))]
    for i in range(len(points)):
        s.add(c[i] >= 0, c[i] <= 2)
    for (i, j, k) in triangles:
        s.add(Not(And(c[i] == c[j], c[j] == c[k])))

    result = s.check()
    if result == sat:
        if verbose:
            print(f"  SAT: Valid coloring exists (A(3) > 3 for this grid)")
        m = s.model()
        coloring = {}
        for i in range(len(points)):
            val = m[c[i]]
            coloring[points[i]] = val.as_long() if val is not None else 0
        if verbose:
            for y in range(M-1, -1, -1):
                row = ""
                for x in range(N):
                    row += str(coloring[(x,y)])
                print(f"  y={y}: {row}")
        return True, coloring
    elif result == unsat:
        if verbose:
            print(f"  UNSAT: No valid coloring exists => A(3) = 3!")
        return False, None
    else:
        if verbose:
            print(f"  {result}: timeout or unknown")
        return None, None

if __name__ == "__main__":
    # Check rectangular grids
    for (N, M) in [(4, 3), (5, 3), (4, 4), (5, 4), (6, 4), (5, 5), (7, 3), (7, 4), (7, 5), (7, 7)]:
        result, _ = check_grid(N, M)
        if result is False:
            print(f"\n*** A(3) = 3 confirmed at grid {N}x{M} ***")
            break
        print()
