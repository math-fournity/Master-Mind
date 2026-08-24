#!/usr/bin/env python3
"""
Carefully analyze the backtracking 4-coloring and find the correct formula.
"""

def v2(n):
    c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c

def v3(n):
    c = 0
    while n % 3 == 0: n //= 3; c += 1
    return c

def six_free(n):
    while n % 2 == 0: n //= 2
    while n % 3 == 0: n //= 3
    return n

# The backtracking coloring for N=75
bt = [0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 2, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 3, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2]

# Analyze by 6-free part
from collections import defaultdict

groups = defaultdict(list)  # m -> list of (n, a, b, c)
for n in range(1, 76):
    m = six_free(n)
    a = v2(n)
    b = v3(n)
    c = bt[n-1]
    groups[m].append((n, a, b, c))

# For each 6-free part, show the pattern
print("=== Pattern by 6-free part ===")
for m in sorted(groups.keys())[:15]:
    entries = groups[m]
    print(f"\nm={m} (m%3={m%3}):")
    for (n, a, b, c) in sorted(entries, key=lambda x: (x[1], x[2])):
        print(f"  n={n:3d} (a={a}, b={b}) -> c={c}")

# Try formula: c = ((v2 + base) % 2) + 2*(v3 % 2)
# where base = 0 if m%3==1, base = 1 if m%3==2
def color_formula(n):
    m = six_free(n)
    base = (m % 3) - 1  # 0 if m%3==1, 1 if m%3==2
    return ((v2(n) + base) % 2) + 2 * (v3(n) % 2)

# Verify
print("\n=== Verifying formula ===")
match = True
for n in range(1, 76):
    if color_formula(n) != bt[n-1]:
        print(f"  MISMATCH at n={n}: formula={color_formula(n)}, bt={bt[n-1]}")
        match = False
if match:
    print("Formula matches backtracking for all n=1..75!")

# Check for large N
print("\n=== Checking formula for large N ===")
def find_solutions(N):
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

for N in [100, 500, 1000, 2000]:
    sols = find_solutions(N)
    mono = 0
    first = None
    for (w, x, y, z) in sols:
        if color_formula(w) == color_formula(x) == color_formula(y) == color_formula(z):
            mono += 1
            if first is None:
                first = (w, x, y, z)
    print(f"N={N}: {len(sols)} solutions, {mono} monochromatic, first: {first}")
    if mono > 0:
        break
