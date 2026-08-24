#!/usr/bin/env python3
"""
Analyze the 4-coloring pattern found by backtracking and verify a formula.
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
bt_coloring = [0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 2, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 3, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2]

# Proposed formula: c(n) = ((m mod 3) - 1 + (v2(n) mod 2) + 2*(v3(n) mod 2)) % 4
# where m = six_free(n)
def color_formula(n):
    m = six_free(n)
    return ((m % 3) - 1 + (v2(n) % 2) + 2 * (v3(n) % 2)) % 4

# Verify formula matches backtracking
print("=== Verifying formula against backtracking ===")
match = True
for n in range(1, 76):
    formula_val = color_formula(n)
    bt_val = bt_coloring[n-1]
    if formula_val != bt_val:
        print(f"  MISMATCH at n={n}: formula={formula_val}, bt={bt_val}")
        match = False
if match:
    print("Formula matches backtracking for all n=1..75!")

# Print the formula values
print("\nFormula values for n=1..30:")
print([color_formula(n) for n in range(1, 31)])

# Now check the formula for large N
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

for N in [100, 200, 500, 1000]:
    sols = find_solutions(N)
    mono_count = 0
    first_mono = None
    for (w, x, y, z) in sols:
        if color_formula(w) == color_formula(x) == color_formula(y) == color_formula(z):
            mono_count += 1
            if first_mono is None:
                first_mono = (w, x, y, z)
    print(f"N={N}: {len(sols)} solutions, {mono_count} monochromatic, first: {first_mono}")

# Also try some variations of the formula
print("\n=== Testing formula variations ===")

# Variation 1: c(n) = ((m mod 3) - 1 + (v2(n) mod 2) + 2*(v3(n) mod 2)) % 4
# This is the original formula

# Variation 2: swap the roles - use (m mod 4) or something
def color_v2(n):
    m = six_free(n)
    return ((m % 3) + (v2(n) % 2) + 2*(v3(n) % 2)) % 4

# Variation 3: use m mod 5
def color_v3(n):
    m = six_free(n)
    return ((m % 5) + (v2(n) % 2) + 2*(v3(n) % 2)) % 4

N_test = 500
sols_test = find_solutions(N_test)

for name, fn in [("original", color_formula), 
                  ("m%3 (no -1)", color_v2),
                  ("m%5", color_v3)]:
    mono = sum(1 for (w,x,y,z) in sols_test if fn(w)==fn(x)==fn(y)==fn(z))
    print(f"  {name}: {mono} monochromatic solutions for N={N_test}")

# Let me also understand the formula better
print("\n=== Understanding the formula ===")
print("c(n) = ((m%3 - 1) + (v2(n)%2) + 2*(v3(n)%2)) % 4")
print("where m = 6-free part of n")
print()
print("For 6-free m: m%3 ∈ {1,2}, so m%3-1 ∈ {0,1}")
print("This is the 'base color' depending on m mod 3")
print("(v2%2, v3%2) gives 4 possibilities: (0,0)->0, (1,0)->1, (0,1)->2, (1,1)->3")
print()

# Verify key constraints
print("=== Verifying key constraints ===")
# c(2t) != c(t)
ok = all(color_formula(2*t) != color_formula(t) for t in range(1, 500))
print(f"c(2t) != c(t) for all t in [1,499]: {ok}")

# c(3t) != c(t)
ok = all(color_formula(3*t) != color_formula(t) for t in range(1, 500))
print(f"c(3t) != c(t) for all t in [1,499]: {ok}")

# c(2t) != c(3t)
ok = all(color_formula(2*t) != color_formula(3*t) for t in range(1, 500))
print(f"c(2t) != c(3t) for all t in [1,499]: {ok}")

# c(5t) != c(7t)
ok = all(color_formula(5*t) != color_formula(7*t) for t in range(1, 500))
print(f"c(5t) != c(7t) for all t in [1,499]: {ok}")

# c(3t) != c(5t)
ok = all(color_formula(3*t) != color_formula(5*t) for t in range(1, 500))
print(f"c(3t) != c(5t) for all t in [1,499]: {ok}")
