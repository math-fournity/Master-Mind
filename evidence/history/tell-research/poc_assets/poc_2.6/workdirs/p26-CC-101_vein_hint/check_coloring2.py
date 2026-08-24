#!/usr/bin/env python3
"""Check if a k-coloring of {1,...,N} exists that avoids monochromatic solutions
to w + 6x = 2y + 3z. Check higher k values."""

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

if __name__ == "__main__":
    for k in range(2, 10):
        print(f"=== Checking {k}-colorings ===")
        found_regular = False
        for N in [10, 15, 20, 30, 50, 100, 200, 500]:
            result, coloring = check_coloring(N, k, verbose=True)
            status = "EXISTS" if result else "DOES NOT EXIST"
            print(f"  N={N}: {k}-coloring {status}")
            if not result:
                print(f"  => Equation is {k}-regular (Rado number <= {N})")
                found_regular = True
                break
            if result and N <= 50:
                # Print coloring for small N
                print(f"  Coloring (1-30): { {n: c for n, c in sorted(coloring.items()) if n <= 30} }")
        if not found_regular:
            print(f"  => {k}-coloring exists for all tested N, equation is NOT {k}-regular")
            # Print the coloring for the largest N
            result, coloring = check_coloring(100, k, verbose=False)
            if coloring:
                print(f"  Coloring (1-50): { {n: c for n, c in sorted(coloring.items()) if n <= 50} }")
            break
        print()
