#!/usr/bin/env python3
"""Check if a k-coloring of {1,...,N} exists that avoids monochromatic solutions
to w + 6x = 2y + 3z."""

from pysat.solvers import Glucose3
import sys

def var(n, i, k):
    """Variable for number n (1-indexed) having color i (0-indexed), with k colors."""
    return (n - 1) * k + i + 1

def check_coloring(N, k, verbose=False):
    """Check if a k-coloring of {1,...,N} exists avoiding monochromatic solutions."""
    # Generate solutions
    solutions = []
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                w = 2 * y + 3 * z - 6 * x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))

    if verbose:
        print(f"N={N}, k={k}: {len(solutions)} solutions")

    # Build clauses
    clauses = []

    # Exactly one color per number
    for n in range(1, N + 1):
        # At least one
        clauses.append([var(n, i, k) for i in range(k)])
        # At most one
        for i in range(k):
            for j in range(i + 1, k):
                clauses.append([-var(n, i, k), -var(n, j, k)])

    # No monochromatic solution
    for (w, x, y, z) in solutions:
        for i in range(k):
            clauses.append([-var(w, i, k), -var(x, i, k), -var(y, i, k), -var(z, i, k)])

    # Solve
    solver = Glucose3()
    for clause in clauses:
        solver.add_clause(clause)

    result = solver.solve()
    model = solver.get_model() if result else None
    solver.delete()

    if result and model and verbose:
        # Extract coloring
        coloring = {}
        for n in range(1, N + 1):
            for i in range(k):
                if model[var(n, i, k) - 1] > 0:
                    coloring[n] = i
                    break
        return True, coloring
    return result, None

if __name__ == "__main__":
    # Check 2-coloring for increasing N
    print("=== Checking 2-colorings ===")
    for N in [20, 50, 100, 150, 200, 300, 500]:
        result, coloring = check_coloring(N, 2, verbose=True)
        status = "EXISTS" if result else "DOES NOT EXIST"
        print(f"  N={N}: 2-coloring {status}")
        if not result:
            print(f"  => Equation is 2-regular (Rado number <= {N})")
            break

    print()
    print("=== Checking 3-colorings ===")
    for N in [20, 50, 100, 200, 300, 500, 1000]:
        result, coloring = check_coloring(N, 3, verbose=True)
        status = "EXISTS" if result else "DOES NOT EXIST"
        print(f"  N={N}: 3-coloring {status}")
        if not result:
            print(f"  => Equation is 3-regular (Rado number <= {N})")
            break
        if result and N <= 100:
            # Print the coloring for small N
            print(f"  Coloring: { {n: c for n, c in sorted(coloring.items()) if n <= 50} }")
