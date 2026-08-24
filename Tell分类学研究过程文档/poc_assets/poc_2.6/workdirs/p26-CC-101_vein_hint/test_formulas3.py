#!/usr/bin/env python3
"""Test candidate 4-coloring formulas - optimized."""

def v_p(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def six_free(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n

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

def test_formula(N, solutions, color_func, name):
    bad = []
    for (w, x, y, z) in solutions:
        cw, cx, cy, cz = color_func(w), color_func(x), color_func(y), color_func(z)
        if cw == cx == cy == cz:
            bad.append((w, x, y, z))
    if bad:
        print(f"  {name}: FAILS ({len(bad)} mono sols / {len(solutions)})")
        for s in bad[:3]:
            print(f"    {s}: colors = {color_func(s[0])},{color_func(s[1])},{color_func(s[2])},{color_func(s[3])}")
    else:
        print(f"  {name}: WORKS for N={N}!")
    return len(bad) == 0

# Precompute colors for speed
def test_formula_fast(N, solutions, color_func, name):
    colors = [0] * (N + 1)
    for n in range(1, N + 1):
        colors[n] = color_func(n)
    bad = 0
    examples = []
    for (w, x, y, z) in solutions:
        if colors[w] == colors[x] == colors[y] == colors[z]:
            bad += 1
            if len(examples) < 3:
                examples.append((w, x, y, z, colors[w]))
    if bad:
        print(f"  {name}: FAILS ({bad} mono sols / {len(solutions)})")
        for s in examples:
            print(f"    {s}")
    else:
        print(f"  {name}: WORKS for N={N}!")
    return bad == 0

def formula_A(n):
    a = v_p(n, 2); b = v_p(n, 3); m = six_free(n)
    return 2 * ((a + b) % 2) + (1 if m % 3 == 2 else 0)

def formula_B(n):
    a = v_p(n, 2); b = v_p(n, 3); m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    return 2 * (a % 2) + ((b + chi) % 2)

def formula_C(n):
    a = v_p(n, 2); b = v_p(n, 3); m = three_free(n)
    chi = 1 if m % 3 == 2 else 0
    return 2 * (a % 2) + ((b + chi) % 2)

def formula_D(n):
    a = v_p(n, 2); b = v_p(n, 3); m = three_free(n)
    chi = 1 if m % 3 == 2 else 0
    return 2 * ((a + chi) % 2) + (b % 2)

def formula_E(n):
    a = v_p(n, 2); b = v_p(n, 3); m = three_free(n)
    return 2 * ((a + b) % 2) + (1 if m % 3 == 2 else 0)

def formula_F(n):
    a = v_p(n, 2); b = v_p(n, 3); m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    return 2 * ((a + b + chi) % 2) + chi

def formula_G(n):
    a = v_p(n, 2); b = v_p(n, 3); m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    return 2 * ((a + chi) % 2) + ((b + chi) % 2)

def formula_H(n):
    a = v_p(n, 2); b = v_p(n, 3); m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    return 2 * ((a + b) % 2) + ((chi + a) % 2)

def formula_I(n):
    a = v_p(n, 2); b = v_p(n, 3); m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    return 2 * ((a + b) % 2) + ((chi + b) % 2)

formulas = [
    (formula_A, "A: ((v2+v3)%2, chi3(6free))"),
    (formula_B, "B: (v2%2, (v3+chi3(6free))%2)"),
    (formula_C, "C: (v2%2, (v3+chi3(3free))%2)"),
    (formula_D, "D: ((v2+chi3(3free))%2, v3%2)"),
    (formula_E, "E: ((v2+v3)%2, chi3(3free))"),
    (formula_F, "F: ((v2+v3+chi)%2, chi)"),
    (formula_G, "G: ((v2+chi)%2, (v3+chi)%2)"),
    (formula_H, "H: ((v2+v3)%2, (chi+v2)%2)"),
    (formula_I, "I: ((v2+v3)%2, (chi+v3)%2)"),
]

for N in [50, 100, 200]:
    print(f"=== N = {N} ===", flush=True)
    sols = find_solutions(N)
    print(f"  {len(sols)} solutions", flush=True)
    for func, name in formulas:
        test_formula_fast(N, sols, func, name)
    print(flush=True)
