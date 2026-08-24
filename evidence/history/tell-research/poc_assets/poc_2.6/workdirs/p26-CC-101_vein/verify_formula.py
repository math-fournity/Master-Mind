#!/usr/bin/env python3
"""
Verify the 4-coloring formula efficiently.
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

# Formula: c(n) = ((v2(n) + base(m)) % 2) + 2*(v3(n) % 2)
# where base(m) = (m%3) - 1, m = 6-free part
def color(n):
    m = six_free(n)
    base = (m % 3) - 1
    return ((v2(n) + base) % 2) + 2 * (v3(n) % 2)

# Verify against backtracking
bt = [0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 2, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 3, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2]

match = all(color(n) == bt[n-1] for n in range(1, 76))
print(f"Formula matches backtracking for n=1..75: {match}")

# Check for monochromatic solutions efficiently
# Instead of enumerating all solutions, use the formula structure
print("\n=== Checking for monochromatic solutions ===")

for N in [100, 200, 500, 1000]:
    mono_count = 0
    first_mono = None
    for w in range(1, N+1):
        cw = color(w)
        for x in range(1, N+1):
            cx = color(x)
            if cw != cx:
                continue
            val = w + 6*x
            # 2y + 3z = val, y >= 1, z >= 1
            for z in range(1, min((val - 2) // 3, N) + 1):
                rem = val - 3*z
                if rem >= 2 and rem % 2 == 0:
                    y = rem // 2
                    if 1 <= y <= N:
                        cy = color(y)
                        if cy != cw:
                            continue
                        cz = color(z)
                        if cz == cw:
                            mono_count += 1
                            if first_mono is None:
                                first_mono = (w, x, y, z)
    print(f"N={N}: {mono_count} monochromatic solutions, first: {first_mono}")
    if mono_count > 0:
        break
