"""
Try to find a minimal unsat core using z3's core minimization.
Also try reducing the point set.
"""
import z3

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

def minimize_core(W, H):
    pts, tris = enumerate_area3_triangles(W, H)
    n = len(pts)
    print(f"Grid {W}x{H}: {n} pts, {len(tris)} tris")

    s = z3.Solver()
    s.set("core.minimize", True)  # Try to minimize core

    color = [z3.Int(f"c_{i}") for i in range(n)]
    for c in color:
        s.add(c >= 0, c <= 2)

    for idx, (i, j, k) in enumerate(tris):
        s.assert_and_track(
            z3.Not(z3.And(color[i] == color[j], color[j] == color[k])),
            f"t_{idx}"
        )

    res = s.check()
    print(f"  -> {res}")
    if res == z3.unsat:
        core = s.unsat_core()
        core_indices = set()
        for item in core:
            name = str(item)
            idx = int(name.split("_")[1])
            core_indices.add(idx)

        core_pts = set()
        for idx in core_indices:
            i, j, k = tris[idx]
            core_pts.add(pts[i])
            core_pts.add(pts[j])
            core_pts.add(pts[k])

        print(f"  Minimized core: {len(core_indices)} tris, {len(core_pts)} pts")

        # Try to further minimize by removing points
        # Check if any point can be removed
        all_core_pts = sorted(core_pts)
        minimal_pts = list(all_core_pts)
        for p in all_core_pts:
            subset = [q for q in minimal_pts if q != p]
            if has_mono_area3_forced(subset):
                minimal_pts = subset
                print(f"    Removed {p}, still UNSAT ({len(minimal_pts)} pts)")

        print(f"  Minimal point set: {len(minimal_pts)} pts")
        print(f"  Points: {minimal_pts}")

        # Count triangles in minimal set
        pidx = {p: i for i, p in enumerate(minimal_pts)}
        count = 0
        for i in range(len(minimal_pts)):
            x1, y1 = minimal_pts[i]
            for j in range(i+1, len(minimal_pts)):
                x2, y2 = minimal_pts[j]
                for k in range(j+1, len(minimal_pts)):
                    x3, y3 = minimal_pts[k]
                    det = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    if det == 6:
                        count += 1
        print(f"  Triangles in minimal set: {count}")

        return minimal_pts

def has_mono_area3_forced(pts):
    """Check if every 3-coloring of pts has a mono area-3 triangle."""
    n = len(pts)
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
    color = [z3.Int(f"c_{i}") for i in range(n)]
    for c in color:
        s.add(c >= 0, c <= 2)
    for (i, j, k) in tris:
        s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
    res = s.check()
    return str(res) == "unsat"

if __name__ == "__main__":
    minimal = minimize_core(7, 5)
