"""
Check if only axis-parallel right triangles with area 3 give UNSAT.
Right triangles: (0,0), (a,0), (0,b) with ab/2 = 3, so ab = 6.
Pairs: (1,6), (2,3), (3,2), (6,1).
Include all rotations and reflections.
"""
import z3

def get_right_triangle_tris(W, H):
    """All axis-parallel right triangles with area 3 (ab=6)."""
    tris = set()
    legs = [(1,6), (2,3), (3,2), (6,1)]
    for (a, b) in legs:
        # Triangle (x,y), (x+dx1, y), (x, y+dy1) where |dx1*dy1| = 6
        # 4 orientations: (±a, ±b), (±b, ±a)
        for (dx, dy) in [(a,b), (-a,b), (a,-b), (-a,-b), (b,a), (-b,a), (b,-a), (-b,-a)]:
            for x in range(W):
                for y in range(H):
                    p1 = (x, y)
                    p2 = (x + dx, y)  # horizontal leg
                    p3 = (x, y + dy)  # vertical leg
                    if (0 <= p2[0] < W and 0 <= p2[1] < H and
                        0 <= p3[0] < W and 0 <= p3[1] < H and
                        len({p1, p2, p3}) == 3):
                        tris.add(tuple(sorted([p1, p2, p3])))
    return tris

def check(W, H, tris_set, label=""):
    pts = [(x, y) for x in range(W) for y in range(H)]
    pidx = {p: i for i, p in enumerate(pts)}
    n = len(pts)
    tris = []
    for t in tris_set:
        if all(p in pidx for p in t):
            tris.append(tuple(pidx[p] for p in t))
    tris = list(set(tris))
    s = z3.Solver()
    color = [z3.Int(f"c_{i}") for i in range(n)]
    for c in color:
        s.add(c >= 0, c <= 2)
    for (i, j, k) in tris:
        s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
    res = s.check()
    print(f"{label} Grid {W}x{H}: {n} pts, {len(tris)} tris -> {res}")
    return str(res) == "unsat"

# Right triangles only
for W, H in [(7,5), (7,7), (9,7), (11,7), (13,7), (7,13), (9,9), (13,13)]:
    tris = get_right_triangle_tris(W, H)
    check(W, H, tris, "right")

# Also try right triangles + H6 (horizontal side 6, third vertex anywhere in adjacent row)
print("\n=== Right + H6 + V3 ===")
def get_H6_tris(W, H):
    tris = set()
    for x in range(W - 6):
        for y in range(H):
            for a in range(W):
                for dy in [1, -1]:
                    if 0 <= y + dy < H:
                        t = tuple(sorted([(x,y), (x+6,y), (a,y+dy)]))
                        if len(set(t)) == 3:
                            tris.add(t)
    return tris

def get_V3_tris(W, H):
    tris = set()
    for x in range(W):
        for y in range(H - 3):
            for b in range(H):
                for dx in [2, -2]:
                    if 0 <= x + dx < W:
                        t = tuple(sorted([(x,y), (x,y+3), (x+dx,b)]))
                        if len(set(t)) == 3:
                            tris.add(t)
    return tris

for W, H in [(7,5), (7,7), (9,7)]:
    rt = get_right_triangle_tris(W, H)
    h6 = get_H6_tris(W, H)
    v3 = get_V3_tris(W, H)
    check(W, H, rt | h6 | v3, "right+H6+V3")
