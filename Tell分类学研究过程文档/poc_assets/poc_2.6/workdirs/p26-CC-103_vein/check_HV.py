"""
Check if only H-triangles (horizontal side length 6) and V-triangles (vertical side length 3)
are sufficient for UNSAT on 7x5.

H-triangle: (x,y), (x+6,y), (x+a,y+1) or (x,y), (x+6,y), (x+a,y-1) for any a.
  Area = 6*1/2 = 3.
V-triangle: (x,y), (x,y+3), (x+2,b) or (x,y), (x,y+3), (x-2,b) for any b.
  Area = 3*2/2 = 3.
"""
import z3

def check_HV(W, H, use_H=True, use_V=True, label=""):
    pts = [(x, y) for x in range(W) for y in range(H)]
    pidx = {p: i for i, p in enumerate(pts)}
    n = len(pts)
    tris = set()

    if use_H:
        # H-triangles: (x,y), (x+6,y), (x+a,y+1) and (x,y), (x+6,y), (x+a,y-1)
        for x in range(W - 6):
            for y in range(H):
                for a in range(W):
                    for dy in [1, -1]:
                        if 0 <= y + dy < H and 0 <= a < W:
                            t = tuple(sorted([pidx[(x,y)], pidx[(x+6,y)], pidx[(a,y+dy)]]))
                            if len(set(t)) == 3:
                                tris.add(t)

    if use_V:
        # V-triangles: (x,y), (x,y+3), (x+2,b) and (x,y), (x,y+3), (x-2,b)
        for x in range(W):
            for y in range(H - 3):
                for b in range(H):
                    for dx in [2, -2]:
                        if 0 <= x + dx < W:
                            t = tuple(sorted([pidx[(x,y)], pidx[(x,y+3)], pidx[(x+dx,b)]]))
                            if len(set(t)) == 3:
                                tris.add(t)

    tris = list(tris)
    s = z3.Solver()
    color = [z3.Int(f"c_{i}") for i in range(n)]
    for c in color:
        s.add(c >= 0, c <= 2)
    for (i, j, k) in tris:
        s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
    res = s.check()
    print(f"{label} Grid {W}x{H}: {n} pts, {len(tris)} tris -> {res}")
    return str(res) == "unsat"

# Check H only, V only, H+V
print("=== 7x5 ===")
check_HV(7, 5, use_H=True, use_V=False, label="H only")
check_HV(7, 5, use_H=False, use_V=True, label="V only")
check_HV(7, 5, use_H=True, use_V=True, label="H+V")

# Also try on larger grids with H only
print("\n=== H only on larger grids ===")
for W, H in [(7, 7), (7, 10), (7, 15), (13, 5), (13, 7)]:
    check_HV(W, H, use_H=True, use_V=False, label="H only")

# V only on larger grids
print("\n=== V only on larger grids ===")
for W, H in [(7, 5), (9, 5), (11, 5), (15, 5), (7, 7), (9, 7), (11, 7)]:
    check_HV(W, H, use_H=False, use_V=True, label="V only")

# H+V on larger grids
print("\n=== H+V on larger grids ===")
for W, H in [(7, 5), (7, 7), (9, 5), (7, 8), (9, 7)]:
    check_HV(W, H, use_H=True, use_V=True, label="H+V")
