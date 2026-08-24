#!/usr/bin/env python3
"""Check specific 4-coloring formulas to see if they avoid monochromatic solutions."""

def v_p(n, p):
    """p-adic valuation of n."""
    if n == 0:
        return float('inf')
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def check_coloring_formula(N, color_func, name):
    """Check if a coloring formula avoids monochromatic solutions up to N."""
    solutions = []
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                w = 2 * y + 3 * z - 6 * x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))

    mono_count = 0
    mono_examples = []
    for (w, x, y, z) in solutions:
        cw, cx, cy, cz = color_func(w), color_func(x), color_func(y), color_func(z)
        if cw == cx == cy == cz:
            mono_count += 1
            if len(mono_examples) < 10:
                mono_examples.append((w, x, y, z, cw))

    print(f"  {name}: {mono_count} monochromatic solutions out of {len(solutions)}")
    if mono_examples:
        print(f"    Examples: {mono_examples}")
    return mono_count == 0

# Coloring 1: (v2+v3) mod 2, (v2+v5) mod 2
def color1(n):
    a = v_p(n, 2)
    b = v_p(n, 3)
    c = v_p(n, 5)
    return ((a + b) % 2, (a + c) % 2)

# Coloring 2: (v2+v3) mod 2, (v3+v5) mod 2
def color2(n):
    a = v_p(n, 2)
    b = v_p(n, 3)
    c = v_p(n, 5)
    return ((a + b) % 2, (b + c) % 2)

# Coloring 3: v2 mod 2, v3 mod 2 (known to fail)
def color3(n):
    return (v_p(n, 2) % 2, v_p(n, 3) % 2)

# Coloring 4: (v2+v3) mod 2, (v2+v5) mod 2, mapped to 0-3
def color4(n):
    a = v_p(n, 2)
    b = v_p(n, 3)
    c = v_p(n, 5)
    return ((a + b) % 2) * 2 + ((a + c) % 2)

# Coloring 5: v2 mod 2, v5 mod 2
def color5(n):
    return (v_p(n, 2) % 2, v_p(n, 5) % 2)

# Coloring 6: v3 mod 2, v5 mod 2
def color6(n):
    return (v_p(n, 3) % 2, v_p(n, 5) % 2)

# Coloring 7: (v2+v3+v5) mod 2, v2 mod 2
def color7(n):
    a = v_p(n, 2)
    b = v_p(n, 3)
    c = v_p(n, 5)
    return ((a + b + c) % 2, a % 2)

# Coloring 8: (v2+v3) mod 2, (v5) mod 2
def color8(n):
    a = v_p(n, 2)
    b = v_p(n, 3)
    c = v_p(n, 5)
    return ((a + b) % 2, c % 2)

N = 100
print(f"Checking coloring formulas up to N={N}:")
print()

for func, name in [
    (color1, "(v2+v3)%2, (v2+v5)%2"),
    (color2, "(v2+v3)%2, (v3+v5)%2"),
    (color3, "v2%2, v3%2 (known fail)"),
    (color5, "v2%2, v5%2"),
    (color6, "v3%2, v5%2"),
    (color7, "(v2+v3+v5)%2, v2%2"),
    (color8, "(v2+v3)%2, v5%2"),
]:
    result = check_coloring_formula(N, func, name)
    if result:
        print(f"    *** NO monochromatic solutions! ***")
    print()
