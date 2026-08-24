#!/usr/bin/env python3
"""Find minimum N for 3-coloring UNSAT and extract proof structure."""

from pysat.solvers import Glucose3

def var(n, i, k):
    return (n - 1) * k + i + 1

def check_coloring(N, k):
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
    return result, model, solutions

# Find minimum N for 3-coloring UNSAT
print("Finding minimum N for 3-coloring UNSAT:", flush=True)
for N in range(5, 30):
    result, model, sols = check_coloring(N, 3)
    status = "SAT" if result else "UNSAT"
    print(f"  N={N}: {status} ({len(sols)} solutions)", flush=True)
    if not result:
        print(f"  => Minimum N for 3-coloring UNSAT is {N}", flush=True)
        break

# For the minimum N, list all solutions
print(f"\nAll solutions for N={N}:", flush=True)
result, model, sols = check_coloring(N, 3)
for s in sols:
    w, x, y, z = s
    print(f"  ({w}, {x}, {y}, {z}): {w}+{6*x}={w+6*x}, {2*y}+{3*z}={2*y+3*z}", flush=True)
