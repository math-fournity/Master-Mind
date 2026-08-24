#!/usr/bin/env python3
"""Extract SAT 4-coloring and try to find the pattern by systematic analysis."""

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

def six_free(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n

N = 300
coloring = get_coloring(N, 4)
if not coloring:
    print("No coloring found!")
    exit()

# Analyze the first bit (color % 2) and second bit (color // 2)
print("=== Second bit (color // 2) analysis ===")
# Check if second bit = v3(n) % 2
mismatches_2 = 0
for n in range(1, N+1):
    expected = v_p(n, 3) % 2
    actual = coloring[n] // 2
    if expected != actual:
        mismatches_2 += 1
        if mismatches_2 <= 5:
            print(f"  n={n}: expected second bit {expected}, got {actual}, v3={v_p(n,3)}, color={coloring[n]}")
print(f"  Second bit = v3%2: {mismatches_2} mismatches out of {N}")

# Check if second bit = v2(n) % 2
mismatches_2b = 0
for n in range(1, N+1):
    expected = v_p(n, 2) % 2
    actual = coloring[n] // 2
    if expected != actual:
        mismatches_2b += 1
print(f"  Second bit = v2%2: {mismatches_2b} mismatches out of {N}")

# Check if second bit = (v2+v3) % 2
mismatches_2c = 0
for n in range(1, N+1):
    expected = (v_p(n, 2) + v_p(n, 3)) % 2
    actual = coloring[n] // 2
    if expected != actual:
        mismatches_2c += 1
print(f"  Second bit = (v2+v3)%2: {mismatches_2c} mismatches out of {N}")

print()
print("=== First bit (color % 2) analysis ===")
# For each combination of (v2%2, v3%2, 3free%3, 6free%5, 6free%7), check first bit
from collections import defaultdict

# Try: first bit as function of (v2, v3, 3free_mod3)
print("--- First bit vs (v3, 3free%3) ---")
bit_by_key = defaultdict(set)
for n in range(1, N+1):
    v3 = v_p(n, 3)
    tf = n
    while tf % 3 == 0:
        tf //= 3
    key = (v3, tf % 3)
    bit_by_key[key].add(coloring[n] % 2)

for key in sorted(bit_by_key.keys()):
    print(f"  v3={key[0]}, 3free%3={key[1]}: first bits = {sorted(bit_by_key[key])}")

print()
print("--- First bit vs (v3%2, 3free%3) ---")
bit_by_key2 = defaultdict(set)
for n in range(1, N+1):
    v3 = v_p(n, 3)
    tf = n
    while tf % 3 == 0:
        tf //= 3
    key = (v3 % 2, tf % 3)
    bit_by_key2[key].add(coloring[n] % 2)

for key in sorted(bit_by_key2.keys()):
    print(f"  v3%2={key[0]}, 3free%3={key[1]}: first bits = {sorted(bit_by_key2[key])}")

print()
print("--- First bit vs (v2%2, v3, 3free%3) ---")
bit_by_key3 = defaultdict(set)
for n in range(1, N+1):
    v2 = v_p(n, 2)
    v3 = v_p(n, 3)
    tf = n
    while tf % 3 == 0:
        tf //= 3
    key = (v2 % 2, v3, tf % 3)
    bit_by_key3[key].add(coloring[n] % 2)

for key in sorted(bit_by_key3.keys()):
    if len(bit_by_key3[key]) > 1:
        print(f"  v2%2={key[0]}, v3={key[1]}, 3free%3={key[2]}: first bits = {sorted(bit_by_key3[key])} *** AMBIGUOUS")
    else:
        print(f"  v2%2={key[0]}, v3={key[1]}, 3free%3={key[2]}: first bits = {sorted(bit_by_key3[key])}")

print()
print("--- First bit vs (v2, v3, 3free%3) ---")
bit_by_key4 = defaultdict(set)
for n in range(1, N+1):
    v2 = v_p(n, 2)
    v3 = v_p(n, 3)
    tf = n
    while tf % 3 == 0:
        tf //= 3
    key = (v2, v3, tf % 3)
    bit_by_key4[key].add(coloring[n] % 2)

ambiguous = 0
for key in sorted(bit_by_key4.keys()):
    if len(bit_by_key4[key]) > 1:
        ambiguous += 1
        print(f"  v2={key[0]}, v3={key[1]}, 3free%3={key[2]}: first bits = {sorted(bit_by_key4[key])} *** AMBIGUOUS")
print(f"  Total ambiguous: {ambiguous} out of {len(bit_by_key4)}")
