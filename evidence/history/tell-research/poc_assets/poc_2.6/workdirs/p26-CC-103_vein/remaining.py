"""
Find the remaining triangles (not in H6, V3, H3, H2, V2).
"""
import z3
from itertools import combinations

def enumerate_all_area3(W, H):
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
                    tris.append((pts[i], pts[j], pts[k]))
    return tris

def get_tris_H6(W, H):
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

W, H = 7, 5
all_tris = set(enumerate_all_area3(W, H))
covered = get_tris_H6(W, H) | get_tris_V3(W, H) | get_tris_H3(W, H) | get_tris_H2(W, H) | get_tris_V2(W, H)

remaining = all_tris - covered
print(f"Total: {len(all_tris)}, Covered: {len(covered)}, Remaining: {len(remaining)}")

# Analyze remaining triangles
print("\nRemaining triangles:")
for t in sorted(remaining):
    # Check if any side is axis-parallel
    p1, p2, p3 = t
    sides = [(p1,p2), (p1,p3), (p2,p3)]
    axis_parallel = []
    for (a, b) in sides:
        if a[0] == b[0] or a[1] == b[1]:
            axis_parallel.append((a,b))
    ap_str = "AXIS" if axis_parallel else "SLANTED"
    # Compute side vectors
    print(f"  {t} {ap_str}")
