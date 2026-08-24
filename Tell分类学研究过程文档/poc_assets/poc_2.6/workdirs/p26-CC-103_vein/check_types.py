"""
Check various combinations of triangle types.
H6: horizontal base 6, height 1
V3: vertical base 3, height 2
H3: horizontal base 3, height 2
H2: horizontal base 2, height 3
V2: vertical base 2, height 3
"""
import z3

def get_tris_H6(W, H):
    """(x,y), (x+6,y), (x+a, y±1) for any a."""
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

def get_tris_V3(W, H):
    """(x,y), (x,y+3), (x±2, b) for any b."""
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

def get_tris_H3(W, H):
    """(x,y), (x+3,y), (x+a, y±2) for any a."""
    tris = set()
    for x in range(W - 3):
        for y in range(H):
            for a in range(W):
                for dy in [2, -2]:
                    if 0 <= y + dy < H:
                        t = tuple(sorted([(x,y), (x+3,y), (a,y+dy)]))
                        if len(set(t)) == 3:
                            tris.add(t)
    return tris

def get_tris_H2(W, H):
    """(x,y), (x+2,y), (x+a, y±3) for any a."""
    tris = set()
    for x in range(W - 2):
        for y in range(H):
            for a in range(W):
                for dy in [3, -3]:
                    if 0 <= y + dy < H:
                        t = tuple(sorted([(x,y), (x+2,y), (a,y+dy)]))
                        if len(set(t)) == 3:
                            tris.add(t)
    return tris

def get_tris_V2(W, H):
    """(x,y), (x,y+2), (x±3, b) for any b."""
    tris = set()
    for x in range(W):
        for y in range(H - 2):
            for b in range(H):
                for dx in [3, -3]:
                    if 0 <= x + dx < W:
                        t = tuple(sorted([(x,y), (x,y+2), (x+dx,b)]))
                        if len(set(t)) == 3:
                            tris.add(t)
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

W, H = 7, 5
H6 = get_tris_H6(W, H)
V3 = get_tris_V3(W, H)
H3 = get_tris_H3(W, H)
H2 = get_tris_H2(W, H)
V2 = get_tris_V2(W, H)

print(f"H6: {len(H6)}, V3: {len(V3)}, H3: {len(H3)}, H2: {len(H2)}, V2: {len(V2)}")

combos = [
    ("H6+V3", H6 | V3),
    ("H6+V3+H3", H6 | V3 | H3),
    ("H6+V3+H2", H6 | V3 | H2),
    ("H6+V3+V2", H6 | V3 | V2),
    ("H6+V3+H3+H2", H6 | V3 | H3 | H2),
    ("H6+V3+H3+V2", H6 | V3 | H3 | V2),
    ("H6+V3+H2+V2", H6 | V3 | H2 | V2),
    ("H6+V3+H3+H2+V2", H6 | V3 | H3 | H2 | V2),
    ("H3+H2+V3+V2", H3 | H2 | V3 | V2),
    ("H3+H2+V2", H3 | H2 | V2),
    ("H3+V3", H3 | V3),
    ("H2+V2", H2 | V2),
    ("H3+H2", H3 | H2),
    ("V3+V2", V3 | V2),
]

for label, tris_set in combos:
    check(W, H, tris_set, label)
