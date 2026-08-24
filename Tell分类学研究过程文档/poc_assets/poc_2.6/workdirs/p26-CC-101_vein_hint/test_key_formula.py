#!/usr/bin/env python3
"""Test the key formula: c(n) = (v3(n)%2, chi3(3free(n)))"""

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
            if len(examples) < 10:
                examples.append((w, x, y, z, colors[w]))
    if bad:
        print(f"  {name}: FAILS ({bad} mono sols / {len(solutions)})")
        for s in examples:
            w,x,y,z,c = s
            print(f"    ({w},{x},{y},{z}) color={c}: v3={v_p(w,3)},{v_p(x,3)},{v_p(y,3)},{v_p(z,3)} 3free%3={three_free(w)%3},{three_free(x)%3},{three_free(y)%3},{three_free(z)%3}")
    else:
        print(f"  {name}: WORKS for N={N}!")
    return bad == 0

# Formula: c(n) = (v3(n)%2, chi3(3free(n)))  where chi3 = 1 if 3free≡1 mod 3, 0 if ≡2
def formula_simple(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    return 2 * (v3 % 2) + (1 if tf == 1 else 0)

# Formula with flip: flip(v3) = 0 for v3 in {0,1,2}, 1 for v3=3, 0 for v3=4, 1 for v3=5
# flip = floor(v3/3) % 2 when v3%3 != 1, 0 when v3%3 == 1
def flip_func(v3):
    if v3 % 3 == 1:
        return 0
    return (v3 // 3) % 2

def formula_with_flip(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    chi = 1 if tf == 1 else 0
    return 2 * (v3 % 2) + (chi ^ flip_func(v3))

# Also try: flip = (v3 >= 3) and (v3 % 2 == 1), i.e., flip for odd v3 >= 3
def flip_func2(v3):
    if v3 >= 3 and v3 % 2 == 1:
        return 1
    return 0

def formula_with_flip2(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    chi = 1 if tf == 1 else 0
    return 2 * (v3 % 2) + (chi ^ flip_func2(v3))

# Try: flip = floor(v3/3) % 2 (simple, no condition on v3%3)
def flip_func3(v3):
    return (v3 // 3) % 2

def formula_with_flip3(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    chi = 1 if tf == 1 else 0
    return 2 * (v3 % 2) + (chi ^ flip_func3(v3))

# Try: no flip at all (pure chi3)
def formula_noflip(n):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    return 2 * (v3 % 2) + (1 if tf == 1 else 0)

formulas = [
    (formula_simple, "simple: (v3%2, chi3(3free))"),
    (formula_noflip, "noflip: same as simple"),
    (formula_with_flip, "flip1: floor(v3/3)%2 if v3%3!=1, else 0"),
    (formula_with_flip2, "flip2: v3>=3 and v3 odd"),
    (formula_with_flip3, "flip3: floor(v3/3)%2 (unconditional)"),
]

for N in [50, 100, 200, 500]:
    print(f"=== N = {N} ===", flush=True)
    sols = find_solutions(N)
    print(f"  {len(sols)} solutions", flush=True)
    for func, name in formulas:
        test_formula_fast(N, sols, func, name)
    print(flush=True)
