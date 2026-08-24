"""
Try to find minimal UNSAT by:
1. Testing specific subsets of shapes
2. Testing sub-grids of 7x5
"""
import z3
from itertools import combinations

def enumerate_area3_triangles_on_pts(pts):
    """All area-3 triangles among given points."""
    pidx = {p: i for i, p in enumerate(pts)}
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
    return tris

def check_pts(pts, verbose=True):
    tris = enumerate_area3_triangles_on_pts(pts)
    n = len(pts)
    if verbose:
        print(f"  {n} pts, {len(tris)} tris -> ", end="", flush=True)
    s = z3.Solver()
    color = [z3.Int(f"c_{i}") for i in range(n)]
    for c in color:
        s.add(c >= 0, c <= 2)
    for (i, j, k) in tris:
        s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
    res = s.check()
    if verbose:
        print(res)
    return str(res) == "unsat"

# Full 7x5 grid
full_pts = [(x, y) for x in range(7) for y in range(5)]
print("Full 7x5:", check_pts(full_pts))

# Try removing each point and check if still UNSAT
print("\n=== Remove one point from 7x5 ===")
for idx in range(len(full_pts)):
    subset = full_pts[:idx] + full_pts[idx+1:]
    result = check_pts(subset, verbose=False)
    if result:
        print(f"  Remove {full_pts[idx]}: still UNSAT ({len(subset)} pts)")

# Try 6x5
pts_65 = [(x, y) for x in range(6) for y in range(5)]
print(f"\n6x5: {check_pts(pts_65, verbose=False)}")

# Try 7x4
pts_74 = [(x, y) for x in range(7) for y in range(4)]
print(f"7x4: {check_pts(pts_74, verbose=False)}")

# Try specific shapes only
# Shape: (0,0),(6,0),(0,1) and translations - "wide" triangles
print("\n=== Only 'wide' triangles (span 6 in x) ===")
# These have one side of length 6 along x-axis
# (0,0),(6,0),(0,1): det=6, area 3
# (0,0),(6,0),(0,k): det=6k, area 3k. Only k=1 works.
# (0,0),(6,0),(1,1): det=6*1-1*0=6, area 3
# (0,0),(6,0),(2,1): det=6*1-2*0=6, area 3
# (0,0),(6,0),(3,1): det=6*1-3*0=6, area 3
# (0,0),(6,0),(4,1): det=6*1-4*0=6, area 3
# (0,0),(6,0),(5,1): det=6*1-5*0=6, area 3
# (0,0),(6,0),(k,1) for k=0..5: all area 3
# Also (0,0),(6,0),(k,-1) but that's same as (0,1),(6,1),(k,0) by translation
# Also (0,k),(6,0),(0,0) type - same shapes

# Let me try: only triangles with a horizontal side of length 6
# A horizontal side of length 6: (x,y),(x+6,y). Third point (x+a,y+b) with |6b|=6, so |b|=1.
# So third point at y±1, any x.
# These are: (x,y),(x+6,y),(x+a,y+1) and (x,y),(x+6,y),(x+a,y-1) for any a.
# On 7x5 grid: x in [0,6], so x and x+6 both in [0,6] means x=0.
# y in [0,4], y+1 in [0,4] means y in [0,3]. y-1 in [0,4] means y in [1,4].
# Triangles: (0,y),(6,y),(a,y+1) for y=0..3, a=0..6
#            (0,y),(6,y),(a,y-1) for y=1..4, a=0..6

wide_tris = []
for y in range(4):
    for a in range(7):
        wide_tris.append(((0,y),(6,y),(a,y+1)))
for y in range(1,5):
    for a in range(7):
        wide_tris.append(((0,y),(6,y),(a,y-1)))

# Also vertical side of length 6: but 7x5 only has height 5, so no vertical side of length 6.
# What about diagonal sides? Let's also add triangles with a side of length 6 in other directions.

# Actually, let me also consider "tall" triangles: side of length 3 in y, with appropriate x offset.
# (0,0),(0,3),(2,0): det=0*0-2*3=-6, area 3. Side (0,0)-(0,3) has length 3 in y.
# (0,0),(0,3),(a,b): det = 0*b-a*3 = -3a, so |3a|=6 means a=2. b can be anything.
# So (0,0),(0,3),(2,b) for any b. On 7x5: b in [0,4].

tall_tris = []
for x in range(5):  # x and x+2 in [0,6]
    for b in range(5):
        tall_tris.append(((x,0),(x,3),(x+2,b)))
        tall_tris.append(((x,4),(x,1),(x+2,b)))
        tall_tris.append(((x,0),(x,3),(x+2,b)))
# Actually let me be more careful. (x,y),(x,y+3),(x+2,y') for y'=any.
# y and y+3 in [0,4] means y in [0,1]. x and x+2 in [0,6] means x in [0,4].
tall_tris = []
for x in range(5):
    for y in [0, 1]:
        for yp in range(5):
            tall_tris.append(((x,y),(x,y+3),(x+2,yp)))

# Also (x,y),(x,y+3),(x-2,yp): x in [2,6], y in [0,1]
for x in range(2, 7):
    for y in [0, 1]:
        for yp in range(5):
            tall_tris.append(((x,y),(x,y+3),(x-2,yp)))

# Combine wide and tall
combined_pts = set()
for t in wide_tris + tall_tris:
    for p in t:
        combined_pts.add(p)
combined_pts = sorted(combined_pts)
print(f"\nWide+tall: {len(combined_pts)} pts, {len(wide_tris)+len(tall_tris)} tris")

# Check
all_tris = wide_tris + tall_tris
# Remove duplicates and invalid (where points coincide)
valid_tris = set()
for t in all_tris:
    if len(set(t)) == 3:
        valid_tris.add(tuple(sorted(t)))
valid_tris = list(valid_tris)
print(f"  Valid tris: {len(valid_tris)}")

pidx = {p: i for i, p in enumerate(combined_pts)}
s = z3.Solver()
color = [z3.Int(f"c_{i}") for i in range(len(combined_pts))]
for c in color:
    s.add(c >= 0, c <= 2)
for t in valid_tris:
    i, j, k = pidx[t[0]], pidx[t[1]], pidx[t[2]]
    s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
res = s.check()
print(f"  -> {res}")
