#!/usr/bin/env python3
"""
Backtracking search for 4-coloring of [1,N] with no monochromatic solution
to w + 6x = 2y + 3z.
"""

def find_solutions(N):
    """Find all solutions (w,x,y,z) with w+6x=2y+3z, all in [1,N]"""
    sols = []
    for w in range(1, N+1):
        for x in range(1, N+1):
            val = w + 6*x
            for z in range(1, min((val - 2) // 3, N) + 1):
                rem = val - 3*z
                if rem >= 2 and rem % 2 == 0:
                    y = rem // 2
                    if 1 <= y <= N:
                        sols.append((w, x, y, z))
    return sols

def backtrack_color(N, k, solutions):
    """Find a k-coloring of [1,N] with no monochromatic solution using backtracking."""
    # For each number, track which solutions it's involved in
    # color[i] = color of number i (0-indexed, color[0] unused)
    color = [0] * (N + 1)
    
    # Build solution list indexed by max variable
    # When we assign color to number n, we need to check all solutions
    # where all variables are <= n and at least one variable equals n
    
    # Group solutions by their max variable
    sols_by_max = [[] for _ in range(N + 1)]
    for sol in solutions:
        mx = max(sol)
        sols_by_max[mx].append(sol)
    
    def is_valid(n):
        """Check all solutions where max variable = n and all vars assigned"""
        for (w, x, y, z) in sols_by_max[n]:
            if color[w] == color[x] == color[y] == color[z] and color[w] != -1:
                return False
        return True
    
    def solve(pos):
        if pos > N:
            return True
        for c in range(k):
            color[pos] = c
            if is_valid(pos):
                if solve(pos + 1):
                    return True
            color[pos] = -1
        return False
    
    # Initialize
    for i in range(N + 1):
        color[i] = -1
    
    if solve(1):
        return color[1:]
    return None

# Check 4 colors for increasing N
print("=== Checking 4 colors with backtracking ===")
for N in range(10, 80, 5):
    sols = find_solutions(N)
    print(f"N={N}: {len(sols)} solutions, searching...", end=" ", flush=True)
    result = backtrack_color(N, 4, sols)
    if result is not None:
        print(f"4-coloring found: {result}")
    else:
        print(f"No 4-coloring exists")
        break
