#!/usr/bin/env python3
"""
Check the minimum number of colors for w + 6x = 2y + 3z to have no monochromatic solution.

Strategy:
1. Generate all solutions (w,x,y,z) with 1 <= w,x,y,z <= N
2. Use backtracking/SAT to check if a c-coloring exists with no monochromatic solution
3. Try c = 2, 3, 4 for increasing N
"""

def generate_solutions(N):
    """Generate all solutions (w,x,y,z) with 1 <= w,x,y,z <= N to w + 6x = 2y + 3z."""
    solutions = []
    for x in range(1, N+1):
        for y in range(1, N+1):
            for z in range(1, N+1):
                w = 2*y + 3*z - 6*x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))
    return solutions

def check_coloring(N, num_colors, solutions=None):
    """
    Check if there exists a num_colors-coloring of {1,...,N} with no monochromatic solution.
    Uses backtracking with constraint propagation.
    """
    if solutions is None:
        solutions = generate_solutions(N)

    # Build constraint list: for each solution, all four values must NOT be the same color
    # This means: NOT(c[w] == c[x] == c[y] == c[z])
    # Equivalently: at least one pair among (w,x), (w,y), (w,z), (x,y), (x,z), (y,z) has different colors

    # For backtracking, we assign colors to 1..N one by one
    # After each assignment, check all solutions where all variables are already assigned

    color = [0] * (N + 1)  # color[0] unused

    # Group solutions by max variable for efficiency
    solutions_by_max = {}
    for sol in solutions:
        m = max(sol)
        if m not in solutions_by_max:
            solutions_by_max[m] = []
        solutions_by_max[m].append(sol)

    def backtrack(n):
        if n > N:
            return True

        for c in range(num_colors):
            color[n] = c

            # Check all solutions where max variable == n (all variables now assigned)
            valid = True
            if n in solutions_by_max:
                for (w, x, y, z) in solutions_by_max[n]:
                    if color[w] == color[x] == color[y] == color[z]:
                        valid = False
                        break

            if valid:
                if backtrack(n + 1):
                    return True

        return False

    if backtrack(1):
        return True, color[1:N+1]
    else:
        return False, None

def verify_4coloring(N):
    """Verify the 4-coloring c(n) = (v3(n) mod 2, (n/3^v3(n)) mod 3)."""
    def v3(n):
        v = 0
        while n % 3 == 0:
            n //= 3
            v += 1
        return v

    def color(n):
        v = v3(n)
        unit = n // (3 ** v)
        return (v % 2, unit % 3)

    solutions = generate_solutions(N)
    for (w, x, y, z) in solutions:
        if color(w) == color(x) == color(y) == color(z):
            return False, (w, x, y, z)
    return True, None

# Test the 4-coloring first
print("=== Verifying 4-coloring ===")
for N in [20, 50, 100, 200]:
    ok, bad = verify_4coloring(N)
    if ok:
        print(f"  N={N}: 4-coloring works (no monochromatic solution)")
    else:
        print(f"  N={N}: 4-coloring FAILS at {bad}")

print()
print("=== Checking 2-coloring ===")
for N in [10, 15, 20, 25, 30]:
    sols = generate_solutions(N)
    print(f"  N={N}: {len(sols)} solutions, checking 2-coloring...", end=" ", flush=True)
    ok, coloring = check_coloring(N, 2, sols)
    if ok:
        print(f"EXISTS: {coloring}")
    else:
        print("IMPOSSIBLE (equation is 2-regular up to N)")

print()
print("=== Checking 3-coloring ===")
for N in [10, 15, 20, 25, 30, 40, 50]:
    sols = generate_solutions(N)
    print(f"  N={N}: {len(sols)} solutions, checking 3-coloring...", end=" ", flush=True)
    ok, coloring = check_coloring(N, 3, sols)
    if ok:
        print(f"EXISTS: {coloring}")
    else:
        print("IMPOSSIBLE (equation is 3-regular up to N)")
