#!/usr/bin/env python3
"""
Direct brute-force check for 3-coloring (no structural assumption)
and check if 4 colors work.
"""
from itertools import product

def check_k_colors(N, k, solutions):
    """Check if a k-coloring of [1,N] exists with no monochromatic solution."""
    # For small N, try all k-colorings
    if k**N > 10**8:
        return None  # too large for brute force
    
    for coloring in product(range(k), repeat=N):
        c = [0] + list(coloring)
        valid = True
        for (w, x, y, z) in solutions:
            if c[w] == c[x] == c[y] == c[z]:
                valid = False
                break
        if valid:
            return c[1:]
    return None

def find_solutions(N):
    """Find all solutions (w,x,y,z) with w+6x=2y+3z, all in [1,N]"""
    sols = []
    for w in range(1, N+1):
        for x in range(1, N+1):
            val = w + 6*x
            for z in range(1, (val - 2) // 3 + 1):
                rem = val - 3*z
                if rem >= 2 and rem % 2 == 0:
                    y = rem // 2
                    if 1 <= y <= N and 1 <= z <= N:
                        sols.append((w, x, y, z))
    return sols

# Check 3 colors directly for small N
for N in range(5, 16):
    sols = find_solutions(N)
    if 3**N > 10**7:
        print(f"N={N}: too large for brute force ({3**N} colorings)")
        continue
    result = check_k_colors(N, 3, sols)
    if result is not None:
        print(f"N={N}: 3-coloring exists: {result}")
    else:
        print(f"N={N}: No 3-coloring exists")

print()

# Let me use the structural approach but with backtracking for 4 colors
# For 4 colors, the constraint c(2t)!=c(t), c(3t)!=c(t), c(2t)!=c(3t)
# doesn't force a unique structure. So we need a different approach.

# Let's check: with 4 colors, can we find a coloring?
# Try c(n) = (v_2(n) - v_3(n)) % 4 ... but this might not work
# Let's try c(n) = (a*v_2(n) + b*v_3(n) + f(m)) % 4

# Actually, let's try a simpler approach: 
# c(n) = v_2(n) % 4 won't work (c(3)=c(1))
# c(n) = (v_2(n) + v_3(n)) % 4 - let's check

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

# Try various 4-colorings
print("=== Testing specific 4-colorings ===")

# Test c(n) = (v_2(n) - v_3(n)) % 4
def color_test1(n):
    return (v2(n) - v3(n)) % 4

# Test c(n) = (2*v_2(n) + v_3(n)) % 4
def color_test2(n):
    return (2*v2(n) + v3(n)) % 4

# Test c(n) = (v_2(n) + 2*v_3(n)) % 4
def color_test3(n):
    return (v2(n) + 2*v3(n)) % 4

# Test c(n) = (v_2(n) + v_3(n)) % 4
def color_test4(n):
    return (v2(n) + v3(n)) % 4

N_test = 200
sols_test = find_solutions(N_test)

for name, color_fn in [("v2-v3 mod 4", color_test1), 
                        ("2v2+v3 mod 4", color_test2),
                        ("v2+2v3 mod 4", color_test3),
                        ("v2+v3 mod 4", color_test4)]:
    mono_count = 0
    first_mono = None
    for (w, x, y, z) in sols_test:
        if color_fn(w) == color_fn(x) == color_fn(y) == color_fn(z):
            mono_count += 1
            if first_mono is None:
                first_mono = (w, x, y, z)
    print(f"{name}: {mono_count} monochromatic solutions, first: {first_mono}")

# Now try a more sophisticated 4-coloring
# c(n) = (v_2(n) - v_3(n) + g(m)) % 4 where g depends on 6-free part
# For 4 colors, we have more freedom

# Let's try: c(n) = (v_2(n) - v_3(n) + m % 4) % 4 where m = six_free(n)
# But that's not well-defined for large m

# Let's try: c(n) = (v_2(n) - v_3(n)) % 4 for the 2,3-part,
# combined with m mod 4 for the 6-free part
# c(n) = (v_2(n) - v_3(n) + six_free(n)) % 4

def color_test5(n):
    return (v2(n) - v3(n) + six_free(n)) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test5(w) == color_test5(x) == color_test5(y) == color_test5(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + 2*six_free(n)) % 4
def color_test6(n):
    return (v2(n) - v3(n) + 2*six_free(n)) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test6(w) == color_test6(x) == color_test6(y) == color_test6(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+2sf mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + six_free(n) % 2) % 4
# This uses the parity of the 6-free part
def color_test7(n):
    return (v2(n) - v3(n) + six_free(n) % 2) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test7(w) == color_test7(x) == color_test7(y) == color_test7(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%2 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + 2*(six_free(n) % 2)) % 4
def color_test8(n):
    return (v2(n) - v3(n) + 2*(six_free(n) % 2)) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test8(w) == color_test8(x) == color_test8(y) == color_test8(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+2(sf%2) mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + 2*(six_free(n) % 2) + (six_free(n) // 2) % 2) % 4
# This uses more bits of the 6-free part
def color_test9(n):
    m = six_free(n)
    return (v2(n) - v3(n) + 2*(m % 2) + ((m // 2) % 2)) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test9(w) == color_test9(x) == color_test9(y) == color_test9(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+bits(sf) mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 5) % 4 where m = six_free(n) mod 5
# Use Legendre-like symbol
def color_test10(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 5) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test10(w) == color_test10(x) == color_test10(y) == color_test10(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%5 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 7) % 4
def color_test11(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 7) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test11(w) == color_test11(x) == color_test11(y) == color_test11(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%7 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 11) % 4
def color_test12(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 11) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test12(w) == color_test12(x) == color_test12(y) == color_test12(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%11 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 13) % 4
def color_test13(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 13) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test13(w) == color_test13(x) == color_test13(y) == color_test13(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%13 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 17) % 4
def color_test14(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 17) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test14(w) == color_test14(x) == color_test14(y) == color_test14(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%17 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 19) % 4
def color_test15(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 19) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test15(w) == color_test15(x) == color_test15(y) == color_test15(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%19 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 23) % 4
def color_test16(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 23) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test16(w) == color_test16(x) == color_test16(y) == color_test16(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%23 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")

# Try c(n) = (v_2(n) - v_3(n) + m % 29) % 4
def color_test17(n):
    m = six_free(n)
    return (v2(n) - v3(n) + m % 29) % 4

mono_count = 0
first_mono = None
for (w, x, y, z) in sols_test:
    if color_test17(w) == color_test17(x) == color_test17(y) == color_test17(z):
        mono_count += 1
        if first_mono is None:
            first_mono = (w, x, y, z)
print(f"v2-v3+sf%29 mod 4: {mono_count} monochromatic solutions, first: {first_mono}")
