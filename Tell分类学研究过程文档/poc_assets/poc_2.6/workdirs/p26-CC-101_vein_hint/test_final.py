#!/usr/bin/env python3
"""Verify the key formula for larger N, and test 3-coloring formulas."""

def v_p(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def three_free(n):
    while n % 3 == 0:
        n //= 3
    return n

def find_solutions(N):
    solutions = []
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                w = 2 * y + 3 * z - 6 * x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))
    return solutions

def test_formula_fast(N, solutions, color_func, name):
    colors = [0] * (N + 1)
    for n in range(1, N + 1):
        colors[n] = color_func(n)
    bad = 0
    examples = []
    for (w, x, y, z) in solutions:
        if colors[w] == colors[x] == colors[y] == colors[z]:
            bad += 1
            if len(examples) < 5:
                examples.append((w, x, y, z, colors[w]))
    if bad:
        print(f"  {name}: FAILS ({bad} mono sols / {len(solutions)})")
        for s in examples:
            print(f"    {s}")
    else:
        print(f"  {name}: WORKS for N={N}!")
    return bad == 0

# The winning 4-coloring
def formula_4color(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    return 2 * (v3 % 2) + (1 if tf == 1 else 0)

# Test 3-coloring: c(n) = (v3(n) + chi3(3free(n))) % 3
def formula_3color_a(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    chi = 1 if tf == 1 else 0
    return (v3 + chi) % 3

# Test 3-coloring: c(n) = (v3(n) + 2*chi3(3free(n))) % 3
def formula_3color_b(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    chi = 1 if tf == 1 else 0
    return (v3 + 2 * chi) % 3

# Test 3-coloring: c(n) = (2*v3(n) + chi3(3free(n))) % 3
def formula_3color_c(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    chi = 1 if tf == 1 else 0
    return (2 * v3 + chi) % 3

# Test: c(n) = (v3(n) * chi3(3free(n))) % 3
def formula_3color_d(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    chi = 1 if tf == 1 else 0
    return (v3 * chi) % 3

# 3-coloring: c(n) = n mod 3
def formula_3color_mod3(n):
    return n % 3

# 3-coloring: c(n) = (v2(n) + v3(n)) % 3
def formula_3color_v2v3(n):
    return (v_p(n, 2) + v_p(n, 3)) % 3

print("=== Testing 4-coloring formula ===", flush=True)
for N in [200, 500, 1000]:
    sols = find_solutions(N)
    test_formula_fast(N, sols, formula_4color, "4color: (v3%2, chi3(3free))")
    print(flush=True)

print("\n=== Testing 3-coloring formulas (should all fail) ===", flush=True)
for N in [50, 100]:
    sols = find_solutions(N)
    print(f"N={N}:", flush=True)
    test_formula_fast(N, sols, formula_3color_a, "3color_a: (v3+chi3)%3")
    test_formula_fast(N, sols, formula_3color_b, "3color_b: (v3+2*chi3)%3")
    test_formula_fast(N, sols, formula_3color_c, "3color_c: (2*v3+chi3)%3")
    test_formula_fast(N, sols, formula_3color_mod3, "3color: n%3")
    test_formula_fast(N, sols, formula_3color_v2v3, "3color: (v2+v3)%3")
    print(flush=True)
