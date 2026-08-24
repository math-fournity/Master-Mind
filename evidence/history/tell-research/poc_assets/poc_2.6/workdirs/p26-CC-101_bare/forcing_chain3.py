#!/usr/bin/env python3
"""
Find the forcing chain for 3-regularity using branching (DPLL-style).
Record the decision tree that leads to contradiction.
"""

def generate_solutions(N):
    solutions = []
    for x in range(1, N+1):
        for y in range(1, N+1):
            for z in range(1, N+1):
                w = 2*y + 3*z - 6*x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))
    return solutions

def solve_with_trace(N, num_colors=3):
    sols = generate_solutions(N)

    # Group solutions by max element
    sols_by_max = {}
    for sol in sols:
        m = max(sol)
        sols_by_max.setdefault(m, []).append(sol)

    # Also build: for each variable, which solutions involve it
    sols_with_var = {}
    for sol in sols:
        for v in set(sol):
            sols_with_var.setdefault(v, []).append(sol)

    color = [None] * (N + 1)
    forbidden = [set() for _ in range(N + 1)]
    trace = []

    # Force c(1)=0, c(2)=1, c(3)=2 (WLOG)
    # From (1,1,2,1): c(1)≠c(2)
    # From (3,1,3,1): c(1)≠c(3)
    # From (3,2,3,3): c(2)≠c(3)
    # With 3 colors, they must be all different

    def propagate(assigned_list):
        """Propagate constraints after assigning colors to assigned_list."""
        queue = list(assigned_list)
        while queue:
            n = queue.pop(0)
            for (w, x, y, z) in sols_with_var.get(n, []):
                vals = [w, x, y, z]
                colors = [color[v] for v in vals]
                unassigned_idx = [i for i, c in enumerate(colors) if c is None]

                if len(unassigned_idx) == 0:
                    if colors[0] == colors[1] == colors[2] == colors[3]:
                        return f"Mono solution ({w},{x},{y},{z}) all color {colors[0]}"
                elif len(unassigned_idx) == 1:
                    assigned_colors = [c for i, c in enumerate(colors) if i != unassigned_idx[0]]
                    if len(set(assigned_colors)) == 1:
                        u = vals[unassigned_idx[0]]
                        fc = assigned_colors[0]
                        if color[u] == fc:
                            return f"c({u})={fc} conflicts with ({w},{x},{y},{z})"
                        if fc not in forbidden[u]:
                            forbidden[u].add(fc)
                            available = set(range(num_colors)) - forbidden[u]
                            if len(available) == 0:
                                return f"c({u}) no color available (forbidden {sorted(forbidden[u])}) from ({w},{x},{y},{z})"
                            elif len(available) == 1:
                                color[u] = list(available)[0]
                                trace.append(f"  c({u})={color[u]} (forced)")
                                queue.append(u)
        return None

    # Set initial assignments
    color[1] = 0
    color[2] = 1
    color[3] = 2
    trace.append("c(1)=0, c(2)=1, c(3)=2 (WLOG, forced by 2-regularity)")

    err = propagate([1, 2, 3])
    if err:
        trace.append(f"CONTRADICTION: {err}")
        return trace, True

    def backtrack(n):
        if n > N:
            return True

        # Check if already forced
        if color[n] is not None:
            return backtrack(n + 1)

        available = set(range(num_colors)) - forbidden[n]

        for c in sorted(available):
            # Save state
            saved_color = color[n]
            saved_forbidden = [set(f) for f in forbidden]
            saved_trace_len = len(trace)

            color[n] = c
            trace.append(f"Try c({n})={c}")

            err = propagate([n])
            if err:
                trace.append(f"  Fail: {err}")
                # Restore
                color[n] = saved_color
                for i in range(len(forbidden)):
                    forbidden[i] = saved_forbidden[i]
                del trace[saved_trace_len:]
                continue

            if backtrack(n + 1):
                return True

            # Restore
            color[n] = saved_color
            for i in range(len(forbidden)):
                forbidden[i] = saved_forbidden[i]
            del trace[saved_trace_len:]

        return False

    result = backtrack(1)
    if not result:
        trace.append("CONTRADICTION: No valid 3-coloring exists")
        return trace, True
    else:
        return trace, False

# Find the minimum N where 3-coloring fails
print("=== Finding minimum N for 3-regularity ===")
for N in range(10, 20):
    trace, has_contradiction = solve_with_trace(N, 3)
    if has_contradiction:
        print(f"\nN={N}: 3-coloring IMPOSSIBLE")
        print("Trace:")
        for s in trace:
            print(f"  {s}")
        break
    else:
        print(f"N={N}: 3-coloring possible")
