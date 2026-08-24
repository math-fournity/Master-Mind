"""
Find a minimal set of area-3 triangles that makes 7x5 UNSAT.
Use iterative deletion: try removing each triangle, keep if still UNSAT.
"""
import z3
import random

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

def is_unsat(pts, tris):
    n = len(pts)
    s = z3.Solver()
    color = [z3.Int(f"c_{i}") for i in range(n)]
    for c in color:
        s.add(c >= 0, c <= 2)
    for (i, j, k) in tris:
        s.add(z3.Not(z3.And(color[i] == color[j], color[j] == color[k])))
    return str(s.check()) == "unsat"

def minimize_triangles(pts, tris, max_iter=100):
    """Greedy minimization: try removing each triangle."""
    current = list(tris)
    changed = True
    iteration = 0
    while changed and iteration < max_iter:
        changed = False
        iteration += 1
        # Try removing each triangle
        random.shuffle(current)
        for idx in range(len(current)):
            subset = current[:idx] + current[idx+1:]
            if is_unsat(pts, subset):
                current = subset
                changed = True
                print(f"  Iter {iteration}: removed triangle {idx}, now {len(current)} tris")
                break
    return current

W, H = 7, 5
pts, tris = enumerate_area3_triangles(W, H)
print(f"Initial: {len(tris)} triangles")

# First verify UNSAT
assert is_unsat(pts, tris), "Should be UNSAT!"
print("Verified UNSAT")

# Minimize
minimal_tris = minimize_triangles(pts, tris)
print(f"\nMinimal set: {len(minimal_tris)} triangles")

# Print the minimal triangles
print("\nMinimal triangles:")
for (i, j, k) in minimal_tris:
    print(f"  {pts[i]} {pts[j]} {pts[k]}")

# Count points involved
pts_used = set()
for (i, j, k) in minimal_tris:
    pts_used.add(pts[i])
    pts_used.add(pts[j])
    pts_used.add(pts[k])
print(f"\nPoints used: {len(pts_used)}")
print(f"Points: {sorted(pts_used)}")
