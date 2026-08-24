#!/usr/bin/env python3
"""Test coloring based on v5 and Legendre symbol mod 5."""

def v_p(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def five_free(n):
    while n % 5 == 0:
        n //= 5
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

# Legendre symbol mod 5: QR(1,4)->0, QNR(2,3)->1
def chi5(m):
    r = m % 5
    if r in (1, 4):
        return 0
    elif r in (2, 3):
        return 1
    else:
        raise ValueError(f"m={m} divisible by 5")

# Formula: c(n) = (v5(n) mod 2, chi5(5-free part))
def formula_v5_chi5(n):
    a = v_p(n, 5)
    m = five_free(n)
    return 2 * (a % 2) + chi5(m)

# Also try with v5 on second bit
def formula_chi5_v5(n):
    a = v_p(n, 5)
    m = five_free(n)
    return 2 * chi5(m) + (a % 2)

# Try combining v5 with v2+v3
def formula_v5sum_chi5(n):
    a = v_p(n, 2) + v_p(n, 3) + v_p(n, 5)
    m = five_free(n)
    return 2 * (a % 2) + chi5(m)

# Try: first bit = (v2+v3+v5) mod 2, second bit = chi5(5free)
def formula_sumall_chi5(n):
    a = v_p(n, 2) + v_p(n, 3) + v_p(n, 5)
    m = five_free(n)
    return 2 * (a % 2) + chi5(m)

# Try: first bit = (v2+v5) mod 2, second bit = chi5(5free)  
def formula_v2v5_chi5(n):
    a = v_p(n, 2) + v_p(n, 5)
    m = five_free(n)
    return 2 * (a % 2) + chi5(m)

# Try: first bit = (v3+v5) mod 2, second bit = chi5(5free)
def formula_v3v5_chi5(n):
    a = v_p(n, 3) + v_p(n, 5)
    m = five_free(n)
    return 2 * (a % 2) + chi5(m)

# Try: first bit = v5 mod 2, second bit = chi5(5free) XOR (v2+v3) mod 2
def formula_v5_chi5xorsum(n):
    a = v_p(n, 5)
    m = five_free(n)
    s = (v_p(n, 2) + v_p(n, 3)) % 2
    return 2 * (a % 2) + (chi5(m) ^ s)

# Try: first bit = v5 mod 2, second bit = chi5(5free) XOR v2 mod 2
def formula_v5_chi5xorv2(n):
    a = v_p(n, 5)
    m = five_free(n)
    s = v_p(n, 2) % 2
    return 2 * (a % 2) + (chi5(m) ^ s)

# Try: first bit = v5 mod 2, second bit = chi5(5free) XOR v3 mod 2
def formula_v5_chi5xorv3(n):
    a = v_p(n, 5)
    m = five_free(n)
    s = v_p(n, 3) % 2
    return 2 * (a % 2) + (chi5(m) ^ s)

formulas = [
    (formula_v5_chi5, "v5%2, chi5(5free)"),
    (formula_chi5_v5, "chi5(5free), v5%2"),
    (formula_v5sum_chi5, "(v2+v3+v5)%2, chi5(5free)"),
    (formula_v2v5_chi5, "(v2+v5)%2, chi5(5free)"),
    (formula_v3v5_chi5, "(v3+v5)%2, chi5(5free)"),
    (formula_v5_chi5xorsum, "v5%2, chi5^((v2+v3)%2)"),
    (formula_v5_chi5xorv2, "v5%2, chi5^(v2%2)"),
    (formula_v5_chi5xorv3, "v5%2, chi5^(v3%2)"),
]

for N in [50, 100, 200, 500]:
    print(f"=== N = {N} ===", flush=True)
    sols = find_solutions(N)
    print(f"  {len(sols)} solutions", flush=True)
    for func, name in formulas:
        test_formula_fast(N, sols, func, name)
    print(flush=True)
