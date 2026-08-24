#!/usr/bin/env python3
"""Extract 4-coloring from SAT solver and analyze the pattern."""

from pysat.solvers import Glucose3

def var(n, i, k):
    return (n - 1) * k + i + 1

def check_coloring(N, k, verbose=False):
    solutions = []
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                w = 2 * y + 3 * z - 6 * x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))

    if verbose:
        print(f"N={N}, k={k}: {len(solutions)} solutions, {N*k} variables")

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
        return True, coloring
    return result, None


def v_p(n, p):
    """p-adic valuation of n."""
    if n == 0:
        return float('inf')
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def six_free_part(n):
    """n with all factors of 2 and 3 removed."""
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n


if __name__ == "__main__":
    N = 200
    result, coloring = check_coloring(N, 4, verbose=True)
    if not result:
        print("No 4-coloring found!")
        exit()

    print(f"\n4-coloring for N={N}:")
    print(f"  Colors 1-60: {[coloring[n] for n in range(1, 61)]}")
    print()

    # Analyze: for each n, show (n, color, v2, v3, v5, six_free_part, n%5, n%7)
    print("n  color  v2  v3  v5  6free  n%5  n%7  n%11")
    for n in range(1, 121):
        c = coloring[n]
        a = v_p(n, 2)
        b = v_p(n, 3)
        d = v_p(n, 5)
        m = six_free_part(n)
        print(f"{n:4d}  {c}  {a}  {b}  {d}  {m:4d}  {n%5}  {n%7}  {n%11}")

    # Check if color correlates with (v2 mod 2, v3 mod 2)
    print("\n--- Check correlation with (v2%2, v3%2) ---")
    from collections import Counter
    for n in range(1, N+1):
        key = (v_p(n,2)%2, v_p(n,3)%2)
        # We'll see if each key maps to a unique color
    key_to_colors = {}
    for n in range(1, N+1):
        key = (v_p(n,2)%2, v_p(n,3)%2)
        if key not in key_to_colors:
            key_to_colors[key] = set()
        key_to_colors[key].add(coloring[n])
    for key, colors in sorted(key_to_colors.items()):
        print(f"  (v2%2={key[0]}, v3%2={key[1]}): colors = {sorted(colors)}")

    # Check correlation with 6-free part mod something
    print("\n--- Check 6-free part mod 5 vs color (for 6-free numbers) ---")
    for n in range(1, N+1):
        if v_p(n,2) == 0 and v_p(n,3) == 0:  # 6-free
            m = n
            print(f"  n={n:4d} (6-free), color={coloring[n]}, n%5={n%5}, n%7={n%7}, n%11={n%11}, n%13={n%13}")
            if n > 80:
                break
