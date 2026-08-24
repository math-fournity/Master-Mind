"""
Try restricting to specific triangle shapes to find a minimal UNSAT.
Axis-aligned right triangles with legs (a,b), ab=6: (1,6),(2,3),(3,2),(6,1).
"""
import z3

def check_shape(W, H, shapes, label=""):
    """shapes: list of (dx1,dy1,dx2,dy2) representing triangle (0,0),(dx1,dy1),(dx2,dy2)."""
    pts = [(x, y) for x in range(W) for y in range(H)]
    pidx = {p: i for i, p in enumerate(pts)}
    tris = set()
    for (dx1, dy1, dx2, dy2) in shapes:
        for (x, y) in pts:
            for ox, oy in [(0,0)]:
                a = (x+ox, y+oy)
                b = (x+dx1, y+dy1)
                c = (x+dx2, y+dy2)
                if a in pidx and b in pidx and c in pidx:
                    tris.add(tuple(sorted([pidx[a], pidx[b], pidx[c]])))
    tris = list(tris)
    print(f"{label} Grid {W}x{H}: {len(pts)} pts, {len(tris)} tris -> ", end="", flush=True)
    s = z3.Solver()
    color = [z3.Int(f"c_{i}") for i in range(len(pts))]
    for c in color:
        s.add(c >= 0, c <= 2)
    for (i, j, k) in tris:
        s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
    res = s.check()
    print(res)
    return str(res)

# Right triangles with legs (a,b), ab=6
# (0,0),(a,0),(0,b): area = ab/2 = 3
shapes_right = [(1,0,0,6), (6,0,0,1), (2,0,0,3), (3,0,0,2)]
# also reflections: (0,0),(a,0),(0,-b) etc - but within grid, translations cover these
# also the mirror: (0,0),(-a,0),(0,b) -> covered by translation

print("=== Only axis-aligned right triangles (legs product 6) ===")
for W, H in [(7,7), (8,8), (10,10), (13,7), (7,13)]:
    check_shape(W, H, shapes_right, "right")

# Add the "slanted" triangles too
# (0,0),(1,2),(3,0): det = 1*0-3*2 = -6, area 3
# (0,0),(2,1),(0,3): det = 2*3-0*1 = 6, area 3
# (0,0),(1,1),(6,0): det = 1*0-6*1 = -6, area 3
# (0,0),(1,3),(4,0): det = 1*0-4*3 = -12, area 6 - no
# (0,0),(1,2),(6,0): det = 1*0-6*2=-12 - no
# (0,0),(2,3),(3,0): det = 2*0-3*3=-9 - no
# (0,0),(1,2),(3,1): det = 1*1-3*2=-5 - no
# (0,0),(1,3),(3,0): det = 1*0-3*3=-9 - no
# (0,0),(2,1),(3,2): det = 2*2-3*1=1 - no
# (0,0),(1,2),(2,3): det = 1*3-2*2=-1 - no
# (0,0),(1,2),(4,1): det = 1*1-4*2=-7 - no
# (0,0),(1,2),(5,1): det = 1*1-5*2=-9 - no
# (0,0),(2,1),(4,2): det = 2*2-4*1=0 - degenerate
# (0,0),(1,2),(2,0): det = 1*0-2*2=-4 - no
# (0,0),(1,2),(4,0): det = 1*0-4*2=-8 - no
# (0,0),(1,3),(2,0): det = 1*0-2*3=-6, area 3! 
# (0,0),(2,3),(0,1): det = 2*1-0*3=2 - no
# (0,0),(3,1),(0,2): det = 3*2-0*1=6, area 3!
# (0,0),(3,2),(0,1): det = 3*1-0*2=3 - no
# (0,0),(1,3),(0,2): det = 1*2-0*3=2 - no

# Let me just enumerate all area-3 triangles with vertices in a small bounding box
print("\n=== All primitive area-3 triangles (bounding box <= 6) ===")
shapes_all = set()
for dx2 in range(-6, 7):
    for dy2 in range(-6, 7):
        for dx3 in range(-6, 7):
            for dy3 in range(-6, 7):
                det = abs(dx2*dy3 - dx3*dy2)
                if det == 6 and (dx2,dy2) != (0,0) and (dx3,dy3) != (0,0) and (dx2,dy2) != (dx3,dy3):
                    # normalize: translate so min coords are 0
                    pts_t = [(0,0),(dx2,dy2),(dx3,dy3)]
                    # canonical form
                    s = tuple(sorted(pts_t))
                    shapes_all.add(s)

# Convert to (dx1,dy1,dx2,dy2) form, normalized so first point is origin
shape_list = set()
for tri in shapes_all:
    # tri is sorted tuple of 3 points
    # try each point as origin
    for o in range(3):
        ox, oy = tri[o]
        others = [tri[i] for i in range(3) if i != o]
        d1 = (others[0][0]-ox, others[0][1]-oy)
        d2 = (others[1][0]-ox, others[1][1]-oy)
        # normalize direction
        key = tuple(sorted([d1, d2]))
        shape_list.add((d1[0], d1[1], d2[0], d2[1]))
shape_list = list(shape_list)
print(f"Total distinct shapes: {len(shape_list)}")

# Now check with ALL area-3 shapes on smaller grids
print("\n=== All area-3 shapes on various grids ===")
for W, H in [(5,5), (6,4), (6,5), (7,4), (7,5), (4,7), (5,6), (5,7)]:
    check_shape(W, H, shape_list, "all")
