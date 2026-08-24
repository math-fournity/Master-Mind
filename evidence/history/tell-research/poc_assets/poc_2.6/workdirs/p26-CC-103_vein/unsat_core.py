"""
Extract unsat core from 7x5 grid to find essential triangles.
Also try restricting to specific triangle shapes to find a minimal proof.
"""
import z3
from itertools import product

def enumerate_area3_triangles(W, H):
    pts = [(x, y) for x in range(W) for y in range(H)]
    tris = []
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i+1, n):
            x2, y2 = pts[j]
            for k in range(j+1, n):
                x3, y3 = pts[k]
                det = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                if det == 6:
                    tris.append((i, j, k))
    return pts, tris

def solve_with_core(W, H):
    pts, tris = enumerate_area3_triangles(W, H)
    print(f"Grid {W}x{H}: {len(pts)} points, {len(tris)} area-3 triangles")

    s = z3.Solver()
    color = [z3.Int(f"c_{i}") for i in range(len(pts))]
    for c in color:
        s.add(c >= 0, c <= 2)

    # Use assertions with tracking
    for idx, (i, j, k) in enumerate(tris):
        same01 = color[i] == color[j]
        same12 = color[j] == color[k]
        s.assert_and_track(z3.Not(z3.And(same01, same12)), f"t_{idx}")

    res = s.check()
    print(f"  -> {res}")
    if res == z3.unsat:
        core = s.unsat_core()
        print(f"  Unsat core size: {len(core)}")
        # Map back to triangles
        core_tris = []
        for c in core:
            name = str(c)
            idx = int(name.split("_")[1])
            i, j, k = tris[idx]
            core_tris.append((pts[i], pts[j], pts[k]))
        # Find points involved
        core_pts = set()
        for a, b, c in core_tris:
            core_pts.add(a); core_pts.add(b); core_pts.add(c)
        print(f"  Core points: {sorted(core_pts)}")
        print(f"  Core points count: {len(core_pts)}")
        print(f"  Core triangles count: {len(core_tris)}")
        return core_tris, core_pts
    return None, None

if __name__ == "__main__":
    core_tris, core_pts = solve_with_core(7, 5)
    if core_tris:
        print("\nCore triangles:")
        for t in core_tris:
            print(f"  {t}")
