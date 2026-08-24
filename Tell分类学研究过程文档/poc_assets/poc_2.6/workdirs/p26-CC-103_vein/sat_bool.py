"""
Efficient SAT encoding using boolean variables.
Each point has 3 booleans: r (is color 0), g (is color 1), b (is color 2).
Exactly one is true.
For each area-3 triangle, forbid all three same color.
"""
import z3
from itertools import combinations

def solve_bool(W, H, return_core=False, core_tris=None):
    pts = [(x, y) for x in range(W) for y in range(H)]
    pidx = {p: i for i, p in enumerate(pts)}
    n = len(pts)

    # Enumerate area-3 triangles
    tris = []
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i+1, n):
            x2, y2 = pts[j]
            for k in range(j+1, n):
                x3, y3 = pts[k]
                det = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                if det == 6:
                    tris.append((i, j, k))

    s = z3.Solver()
    # Boolean variables: c[i][col] = True means point i has color col
    c = [[z3.Bool(f"c_{i}_{col}") for col in range(3)] for i in range(n)]

    # Exactly one color per point
    for i in range(n):
        s.add(z3.Or(c[i][0], c[i][1], c[i][2]))
        s.add(z3.Not(z3.And(c[i][0], c[i][1])))
        s.add(z3.Not(z3.And(c[i][0], c[i][1])))
        s.add(z3.Not(z3.And(c[i][0], c[i][2])))
        s.add(z3.Not(z3.And(c[i][1], c[i][2])))

    # For each area-3 triangle, forbid monochromatic
    for idx, (i, j, k) in enumerate(tris):
        for col in range(3):
            constraint = z3.Not(z3.And(c[i][col], c[j][col], c[k][col]))
            if return_core:
                s.assert_and_track(constraint, f"t_{idx}_{col}")
            else:
                s.add(constraint)

    res = s.check()
    print(f"Grid {W}x{H}: {n} pts, {len(tris)} tris -> {res}")

    if res == z3.unsat and return_core:
        core = s.unsat_core()
        print(f"  Core size: {len(core)}")
        # Extract unique triangles from core
        core_tri_indices = set()
        for item in core:
            name = str(item)
            parts = name.split("_")
            idx = int(parts[1])
            core_tri_indices.add(idx)
        print(f"  Core triangles: {len(core_tri_indices)}")
        core_tri_pts = set()
        for idx in core_tri_indices:
            i, j, k = tris[idx]
            core_tri_pts.add(pts[i])
            core_tri_pts.add(pts[j])
            core_tri_pts.add(pts[k])
        print(f"  Core points: {len(core_tri_pts)}")
        return core_tri_indices, tris, pts
    return None, tris, pts

if __name__ == "__main__":
    # Verify 7x5
    solve_bool(7, 5)

    # Get unsat core
    print("\n=== Unsat core ===")
    core_idx, tris, pts = solve_bool(7, 5, return_core=True)

    if core_idx:
        # Print core triangles
        print("\nCore triangles:")
        for idx in sorted(core_idx):
            i, j, k = tris[idx]
            print(f"  {pts[i]} {pts[j]} {pts[k]}")
