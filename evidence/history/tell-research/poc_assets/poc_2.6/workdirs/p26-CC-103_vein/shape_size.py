"""
Find which shape sizes are needed for UNSAT on 7x5.
Try shapes with bounding box up to various sizes.
"""
import z3

def get_shapes_up_to(max_w, max_h):
    shapes = set()
    for x2 in range(0, max_w+1):
        for y2 in range(0, max_h+1):
            for x3 in range(0, max_w+1):
                for y3 in range(0, max_h+1):
                    det = abs(x2*y3 - x3*y2)
                    if det == 6 and (x2,y2) != (0,0) and (x3,y3) != (0,0) and (x2,y2) != (x3,y3):
                        shapes.add((x2,y2,x3,y3))
    return list(shapes)

def check(W, H, shapes, label=""):
    pts = [(x, y) for x in range(W) for y in range(H)]
    pidx = {p: i for i, p in enumerate(pts)}
    tris = set()
    for (dx1, dy1, dx2, dy2) in shapes:
        for (x, y) in pts:
            a = (x, y)
            b = (x+dx1, y+dy1)
            c = (x+dx2, y+dy2)
            if a in pidx and b in pidx and c in pidx:
                tris.add(tuple(sorted([pidx[a], pidx[b], pidx[c]])))
    tris = list(tris)
    s = z3.Solver()
    color = [z3.Int(f"c_{i}") for i in range(len(pts))]
    for c in color:
        s.add(c >= 0, c <= 2)
    for (i, j, k) in tris:
        s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
    res = s.check()
    print(f"{label} Grid {W}x{H}: {len(pts)} pts, {len(tris)} tris -> {res}")
    return str(res) == "unsat"

W, H = 7, 5
for mw, mh in [(3,4), (4,4), (5,4), (6,4), (7,4), (4,5), (5,5), (6,5), (7,5)]:
    shapes = get_shapes_up_to(mw, mh)
    check(W, H, shapes, f"box<{mw}x{mh}>")
