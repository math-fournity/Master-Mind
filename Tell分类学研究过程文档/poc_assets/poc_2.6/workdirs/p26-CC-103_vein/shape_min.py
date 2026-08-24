"""
Find minimal set of area-3 triangle shapes that gives UNSAT.
Try shapes fitting in small bounding boxes.
"""
import z3
from itertools import combinations

def get_shapes_in_box(max_w, max_h):
    """All area-3 triangles with bounding box width <= max_w, height <= max_h,
    as (d1x,d1y,d2x,d2y) with origin at a vertex."""
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

# Shapes fitting in 3x4 box
shapes_34 = get_shapes_in_box(3, 4)
print(f"Shapes in 3x4 box: {len(shapes_34)}")
for s in sorted(shapes_34):
    print(f"  {s}")

# Check on various grids
print("\n=== Shapes in 3x4 box ===")
for W, H in [(7,5), (8,6), (10,7), (10,10), (15,10)]:
    check(W, H, shapes_34, "3x4box")

# Shapes fitting in 4x3 box (same by rotation, but let's be explicit)
shapes_43 = get_shapes_in_box(4, 3)
print(f"\nShapes in 4x3 box: {len(shapes_43)}")

# Shapes fitting in 2x3 box
shapes_23 = get_shapes_in_box(2, 3)
print(f"Shapes in 2x3 box: {len(shapes_23)}")
for s in sorted(shapes_23):
    print(f"  {s}")

print("\n=== Shapes in 2x3 box ===")
for W, H in [(10,10), (15,15), (20,20)]:
    check(W, H, shapes_23, "2x3box")

# Shapes fitting in 3x2 box
shapes_32 = get_shapes_in_box(3, 2)
print(f"\nShapes in 3x2 box: {len(shapes_32)}")
for s in sorted(shapes_32):
    print(f"  {s}")

print("\n=== Shapes in 3x2 box ===")
for W, H in [(10,10), (15,15), (20,20)]:
    check(W, H, shapes_32, "3x2box")

# Combined 2x3 and 3x2
shapes_23_32 = shapes_23 + shapes_32
print("\n=== Shapes in 2x3 or 3x2 box ===")
for W, H in [(7,5), (8,6), (10,7), (10,10)]:
    check(W, H, shapes_23_32, "2x3+3x2")
