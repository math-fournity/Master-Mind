#!/usr/bin/env python3
"""Extract SAT coloring for larger N and analyze first bit pattern vs v3."""

from pysat.solvers import Glucose3

def var(n, i, k):
    return (n - 1) * k + i + 1

def get_coloring(N, k=4):
    solutions = []
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                w = 2 * y + 3 * z - 6 * x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))
    clauses = []
    for n in range(1, N + 1):
        clauses.append([var(n, i, k) for i in range(k)])
        for i in range(k):
            for j in range(i + 1, k):
                clauses.append([-var(n, i, k), -var(n, j, k)])
    for (w, x, y, z) in solutions:
        for i in range(k):
            clauses.append([-var(w, i, k), -var(x, i, k), -var(y, i, k), -var(z, i, k)])
    solver = Glucose3()
    for clause in clauses:
        solver.add_clause(clause)
    result = solver.solve()
    model = solver.get_model() if result else None
    solver.delete()
    if result and model:
        coloring = {}
        for n in range(1, N + 1):
            for i in range(k):
                if model[var(n, i, k) - 1] > 0:
                    coloring[n] = i
                    break
        return coloring
    return None

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

N = 1000
print(f"Getting SAT 4-coloring for N={N}...", flush=True)
coloring = get_coloring(N, 4)
if not coloring:
    print("No coloring found!")
    exit()
print("Done!", flush=True)

# Analyze first bit as function of (v3, 3free%3)
from collections import defaultdict

bit_map = {}  # (v3, 3free%3) -> set of first bits
for n in range(1, N+1):
    v3 = v_p(n, 3)
    tf = three_free(n) % 3
    key = (v3, tf)
    if key not in bit_map:
        bit_map[key] = set()
    bit_map[key].add(coloring[n] % 2)

print("\nFirst bit pattern (v3, 3free%3) -> first_bit:")
for v3 in range(8):
    for tf in [1, 2]:
        key = (v3, tf)
        if key in bit_map:
            bits = sorted(bit_map[key])
            chi = 1 if tf == 1 else 0
            flip = "FLIP" if bits[0] != chi else "same"
            print(f"  v3={v3}, 3free%3={tf}: first_bit={bits} ({flip}), chi={chi}")

# Also check: is first bit = chi_3(3free) XOR f(v3) for some function f?
print("\nFlip function f(v3) = first_bit XOR chi:")
for v3 in range(8):
    for tf in [1, 2]:
        key = (v3, tf)
        if key in bit_map:
            chi = 1 if tf == 1 else 0
            bits = sorted(bit_map[key])
            if len(bits) == 1:
                flip = bits[0] ^ chi
                print(f"  v3={v3}: flip={flip} (from 3free%3={tf})")
                break

# Check if second bit is still v3%2
mismatches = sum(1 for n in range(1, N+1) if coloring[n] // 2 != v_p(n, 3) % 2)
print(f"\nSecond bit = v3%2: {mismatches} mismatches out of {N}")

# Try to find a formula for the first bit
# Hypothesis: first_bit = chi_3(3free) XOR g(v3) where g is some function
print("\n--- Testing flip hypotheses ---")
for v3 in range(8):
    flips = set()
    for tf in [1, 2]:
        key = (v3, tf)
        if key in bit_map:
            chi = 1 if tf == 1 else 0
            bits = sorted(bit_map[key])
            if len(bits) == 1:
                flips.add(bits[0] ^ chi)
    if len(flips) == 1:
        print(f"  v3={v3}: flip = {flips.pop()}")
    else:
        print(f"  v3={v3}: INCONSISTENT flips = {flips}")
