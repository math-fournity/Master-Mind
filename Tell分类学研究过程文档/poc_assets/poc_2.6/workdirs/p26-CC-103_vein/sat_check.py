"""
z3 SAT check: does there exist a 3-coloring of a W x H grid
that avoids all monochromatic lattice triangles of area 3?

Area-3 triangle <=> |shoelace determinant| = 6.
"""
import z3
from itertools import product

def enumerate_area3_triangles(W, H):
    """All unordered triples of distinct lattice points in [0,W)x[0,H)
    with |det| = 6 (area = 3)."""
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

def solve(W, H, verbose=True):
    pts, tris = enumerate_area3_triangles(W, H)
    if verbose:
        print(f"Grid {W}x{H}: {len(pts)} points, {len(tris)} area-3 triangles")

    s = z3.Solver()
    # color[p] in {0,1,2}
    color = [z3.Int(f"c_{i}") for i in range(len(pts))]
    for c in color:
        s.add(c >= 0, c <= 2)

    # For each area-3 triangle, NOT all same color
    for (i, j, k) in tris:
        # forbid c_i == c_j == c_k
        same01 = color[i] == color[j]
        same12 = color[j] == color[k]
        s.add(z3.Not(z3.And(same01, same12)))

    res = s.check()
    if verbose:
        print(f"  -> {res}")
    if res == z3.sat:
        m = s.model()
        coloring = [m[color[i]].as_long() if m[color[i]] is not None else 0
                    for i in range(len(pts))]
        return True, coloring, pts, tris
    return False, None, pts, tris

if __name__ == "__main__":
    import sys
    W = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    H = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    sat, coloring, pts, tris = solve(W, H)
    if sat:
        print("SAT - found a coloring avoiding all mono area-3 triangles:")
        # print grid
        grid = {}
        for (x, y), c in zip(pts, coloring):
            grid[(x, y)] = c
        for y in range(H):
            row = ""
            for x in range(W):
                row += str(grid[(x, y)]) + " "
            print(row)
    else:
        print("UNSAT - every 3-coloring has a mono area-3 triangle")
