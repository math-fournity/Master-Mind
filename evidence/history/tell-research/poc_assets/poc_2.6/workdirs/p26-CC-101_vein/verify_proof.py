#!/usr/bin/env python3
"""
Verify the simplified formula and the proof logic.
c(n) = ((n/3^v3(n)) mod 3 - 1) + 2*(v3(n) mod 2)
= (d - 1) + 2*(nu mod 2) where d = leading nonzero digit in base 3, nu = trailing zeros in base 3.
"""

def v3(n):
    c = 0
    while n % 3 == 0: n //= 3; c += 1
    return c

def three_free(n):
    while n % 3 == 0: n //= 3
    return n

def color(n):
    nu = v3(n)
    n3 = three_free(n)  # 3-free part
    d = n3 % 3  # leading nonzero digit in base 3 (1 or 2)
    return (d - 1) + 2 * (nu % 2)

# Verify against backtracking
bt = [0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 2, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2, 0, 1, 3, 0, 1, 3, 0, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 0, 1, 3, 0, 1, 1, 0, 1, 2]

match = all(color(n) == bt[n-1] for n in range(1, 76))
print(f"Formula matches backtracking: {match}")

# Verify the proof key step:
# For the equation w + 6x = 2y + 3z, 
# the 3-adic valuation analysis shows that either s(w) != s(y) or s(x) != s(z)
# where s(n) = (n3 mod 3) - 1 is the low bit.

# Let's verify: for any solution, check that either s(w) != s(y) or s(x) != s(z)
# when t(w) = t(x) = t(y) = t(z) (high bits equal)

print("\n=== Verifying proof logic ===")
N = 500
violations = 0
for w in range(1, N+1):
    for x in range(1, N+1):
        val = w + 6*x
        for z in range(1, min((val - 2) // 3, N) + 1):
            rem = val - 3*z
            if rem >= 2 and rem % 2 == 0:
                y = rem // 2
                if 1 <= y <= N:
                    # Check if high bits are all equal
                    tw, tx, ty, tz = v3(w) % 2, v3(x) % 2, v3(y) % 2, v3(z) % 2
                    if tw == tx == ty == tz:
                        # Check if low bits are all equal (monochromatic)
                        sw = (three_free(w) % 3) - 1
                        sx = (three_free(x) % 3) - 1
                        sy = (three_free(y) % 3) - 1
                        sz = (three_free(z) % 3) - 1
                        if sw == sx == sy == sz:
                            violations += 1
                            print(f"  VIOLATION: ({w},{x},{y},{z}) s=({sw},{sx},{sy},{sz}) t=({tw},{tx},{ty},{tz})")

print(f"Violations (high bits equal AND low bits equal): {violations}")

# Also verify: when high bits equal, either s(w)!=s(y) or s(x)!=s(z)
print("\n=== Checking: when t(w)=t(x)=t(y)=t(z), either s(w)!=s(y) or s(x)!=s(z) ===")
counterexample = 0
for w in range(1, N+1):
    for x in range(1, N+1):
        val = w + 6*x
        for z in range(1, min((val - 2) // 3, N) + 1):
            rem = val - 3*z
            if rem >= 2 and rem % 2 == 0:
                y = rem // 2
                if 1 <= y <= N:
                    tw, tx, ty, tz = v3(w) % 2, v3(x) % 2, v3(y) % 2, v3(z) % 2
                    if tw == tx == ty == tz:
                        sw = (three_free(w) % 3) - 1
                        sx = (three_free(x) % 3) - 1
                        sy = (three_free(y) % 3) - 1
                        sz = (three_free(z) % 3) - 1
                        if sw == sy and sx == sz:
                            counterexample += 1
                            if counterexample <= 5:
                                print(f"  COUNTEREXAMPLE: ({w},{x},{y},{z}) s=({sw},{sx},{sy},{sz})")

print(f"Counterexamples: {counterexample}")

# Verify 3-color impossibility for N=12
print("\n=== Verifying 3-color impossibility for N=12 ===")
from itertools import product

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

sols12 = find_solutions(12)
print(f"Solutions in [1,12]: {len(sols12)}")

found = False
for coloring in product([0, 1, 2], repeat=12):
    c = [0] + list(coloring)
    valid = True
    for (w, x, y, z) in sols12:
        if c[w] == c[x] == c[y] == c[z]:
            valid = False
            break
    if valid:
        print(f"3-coloring found for N=12: {c[1:]}")
        found = True
        break

if not found:
    print("No 3-coloring exists for N=12 (confirmed)")
