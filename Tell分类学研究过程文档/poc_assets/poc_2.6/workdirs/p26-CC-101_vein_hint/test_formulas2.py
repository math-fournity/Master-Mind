#!/usr/bin/env python3
"""Test candidate 4-coloring formulas for w + 6x = 2y + 3z."""

def v_p(n, p):
    if n == 0:
        return float('inf')
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

def two_free(n):
    while n % 2 == 0:
        n //= 2
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

def test_formula(N, color_func, name):
    solutions = find_solutions(N)
    bad = []
    for (w, x, y, z) in solutions:
        cw, cx, cy, cz = color_func(w), color_func(x), color_func(y), color_func(z)
        if cw == cx == cy == cz:
            bad.append((w, x, y, z))
            if len(bad) <= 5:
                pass
    if bad:
        print(f"  {name}: FAILS ({len(bad)} monochromatic solutions out of {len(solutions)})")
        if len(bad) <= 5:
            for s in bad:
                print(f"    {s}: colors = {color_func(s[0])},{color_func(s[1])},{color_func(s[2])},{color_func(s[3])}")
        else:
            for s in bad[:3]:
                print(f"    {s}: colors = {color_func(s[0])},{color_func(s[1])},{color_func(s[2])},{color_func(s[3])}")
    else:
        print(f"  {name}: WORKS for N={N}!")
    return len(bad) == 0

# Candidate formulas
def formula_A(n):
    """c(n) = ((v2+v3) mod 2, chi3(6-free part))"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = six_free(n)
    bit1 = (a + b) % 2
    bit2 = 1 if m % 3 == 2 else 0
    return 2 * bit1 + bit2

def formula_B(n):
    """c(n) = (v2 mod 2, (v3 + chi3(6free)) mod 2)"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    bit1 = a % 2
    bit2 = (b + chi) % 2
    return 2 * bit1 + bit2

def formula_C(n):
    """c(n) = (v2 mod 2, (v3 + chi3(3free)) mod 2)"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = three_free(n)  # 3-free part
    chi = 1 if m % 3 == 2 else 0
    bit1 = a % 2
    bit2 = (b + chi) % 2
    return 2 * bit1 + bit2

def formula_D(n):
    """c(n) = ((v2 + chi3(3free)) mod 2, v3 mod 2)"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = three_free(n)
    chi = 1 if m % 3 == 2 else 0
    bit1 = (a + chi) % 2
    bit2 = b % 2
    return 2 * bit1 + bit2

def formula_E(n):
    """c(n) = ((v2 + v3) mod 2, chi3(3free part))"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = three_free(n)
    bit1 = (a + b) % 2
    bit2 = 1 if m % 3 == 2 else 0
    return 2 * bit1 + bit2

def formula_F(n):
    """c(n) = ((v2 + v3 + chi3(6free)) mod 2, chi3(6free))"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    bit1 = (a + b + chi) % 2
    bit2 = chi
    return 2 * bit1 + bit2

def formula_G(n):
    """c(n) = ((v2 + chi3(6free)) mod 2, (v3 + chi3(6free)) mod 2)"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    bit1 = (a + chi) % 2
    bit2 = (b + chi) % 2
    return 2 * bit1 + bit2

def formula_H(n):
    """c(n) = ((v2 + v3) mod 2, (chi3(6free) + v2) mod 2)"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    bit1 = (a + b) % 2
    bit2 = (chi + a) % 2
    return 2 * bit1 + bit2

def formula_I(n):
    """c(n) = ((v2 + v3) mod 2, (chi3(6free) + v3) mod 2)"""
    a = v_p(n, 2)
    b = v_p(n, 3)
    m = six_free(n)
    chi = 1 if m % 3 == 2 else 0
    bit1 = (a + b) % 2
    bit2 = (chi + b) % 2
    return 2 * bit1 + bit2

formulas = [
    (formula_A, "A: ((v2+v3)%2, chi3(6free))"),
    (formula_B, "B: (v2%2, (v3+chi3(6free))%2)"),
    (formula_C, "C: (v2%2, (v3+chi3(3free))%2)"),
    (formula_D, "D: ((v2+chi3(3free))%2, v3%2)"),
    (formula_E, "E: ((v2+v3)%2, chi3(3free))"),
    (formula_F, "F: ((v2+v3+chi3(6free))%2, chi3(6free))"),
    (formula_G, "G: ((v2+chi3(6free))%2, (v3+chi3(6free))%2)"),
    (formula_H, "H: ((v2+v3)%2, (chi3(6free)+v2)%2)"),
    (formula_I, "I: ((v2+v3)%2, (chi3(6free)+v3)%2)"),
]

for N in [50, 100, 200, 500]:
    print(f"\n=== N = {N} ===")
    for func, name in formulas:
        test_formula(N, func, name)
