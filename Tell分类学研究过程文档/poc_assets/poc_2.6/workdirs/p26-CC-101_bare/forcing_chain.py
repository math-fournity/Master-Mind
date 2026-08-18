#!/usr/bin/env python3
"""
Find the forcing chain for 3-regularity.
Track which constraints force which color assignments, and find the contradiction.
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

def find_forcing_chain(N, num_colors=3):
    """
    Given that c(1)=0, c(2)=1, c(3)=2 (WLOG),
    find the forcing chain that leads to contradiction.

    A solution (w,x,y,z) forces a constraint when 3 of the 4 variables
    already have the same color, forcing the 4th to be different.
    Or when all 4 would be the same color, giving a contradiction.
    """
    sols = generate_solutions(N)

    # Start with c(1)=0, c(2)=1, c(3)=2
    color = {1: 0, 2: 1, 3: 2}
    forbidden = {1: set(), 2: set(), 3: set()}  # forbidden colors for each number

    # Initially, from the basic constraints:
    # (1,1,2,1): c(1)≠c(2) -> already have
    # (3,1,3,1): c(1)≠c(3) -> already have
    # (3,2,3,3): c(2)≠c(3) -> already have

    chain = []

    changed = True
    while changed:
        changed = False
        for (w, x, y, z) in sols:
            vals = [w, x, y, z]
            colors = [color.get(v, None) for v in vals]

            # Count how many are assigned
            assigned = [(v, c) for v, c in zip(vals, colors) if c is not None]
            unassigned = [v for v, c in zip(vals, colors) if c is None]

            if len(unassigned) == 0:
                # All assigned - check if monochromatic
                if colors[0] == colors[1] == colors[2] == colors[3]:
                    chain.append(f"CONTRADICTION: ({w},{x},{y},{z}) all color {colors[0]}")
                    return chain
            elif len(unassigned) == 1:
                # 3 assigned, 1 unassigned
                # Check if the 3 assigned are all the same color
                assigned_colors = [c for v, c in assigned]
                unassigned_val = unassigned[0]

                if len(set(assigned_colors)) == 1:
                    # All 3 assigned have same color -> 4th must be different
                    c_forbidden = assigned_colors[0]
                    if c_forbidden not in forbidden.get(unassigned_val, set()):
                        forbidden.setdefault(unassigned_val, set()).add(c_forbidden)
                        chain.append(f"({w},{x},{y},{z}): c({unassigned_val}) ≠ {c_forbidden} (forced by 3 same)")
                        changed = True

                        # Check if this forces a unique color
                        available = set(range(num_colors)) - forbidden[unassigned_val]
                        if len(available) == 1:
                            color[unassigned_val] = list(available)[0]
                            chain.append(f"  => c({unassigned_val}) = {color[unassigned_val]} (only option left)")
                        elif len(available) == 0:
                            chain.append(f"  => CONTRADICTION: no color available for {unassigned_val}")
                            return chain

    # If we reach here, no contradiction found with this simple propagation
    # Try deeper search
    chain.append(f"No contradiction found with simple propagation up to N={N}")
    chain.append(f"Assigned: {dict(sorted(color.items()))}")
    chain.append(f"Forbidden: {dict(sorted((k, sorted(v)) for k, v in forbidden.items() if v))}")
    return chain

# Also find the exact N where 3-coloring becomes impossible
def check_3coloring_with_propagation(N):
    """Full backtracking with propagation for 3 colors."""
    sols = generate_solutions(N)

    color = [0] * (N + 1)
    forbidden = [set() for _ in range(N + 1)]

    # Precompute solutions grouped by max element
    sols_by_max = {}
    for sol in sols:
        m = max(sol)
        sols_by_max.setdefault(m, []).append(sol)

    # Also precompute solutions where exactly one variable is the max
    # for propagation

    def propagate(n):
        """After assigning color[n], propagate constraints."""
        queue = [n]
        while queue:
            v = queue.pop(0)
            # Find solutions where v appears and 3 others are assigned same color
            for (w, x, y, z) in sols:
                vals = [w, x, y, z]
                if v not in vals:
                    continue
                colors = [color[v2] if v2 <= n or v2 in assigned else None for v2 in vals]
                # This is getting complex, skip for now
                pass

    # Simple backtracking
    def backtrack(n):
        if n > N:
            return True

        for c in range(3):
            if c in forbidden[n]:
                continue
            color[n] = c

            # Check solutions where max == n
            valid = True
            if n in sols_by_max:
                for (w, x, y, z) in sols_by_max[n]:
                    if color[w] == color[x] == color[y] == color[z]:
                        valid = False
                        break

            if valid:
                if backtrack(n + 1):
                    return True

        return False

    return backtrack(1)

print("=== Forcing chain for 3-regularity ===")
for N in [10, 12, 14, 15, 16, 20]:
    chain = find_forcing_chain(N, 3)
    has_contradiction = any("CONTRADICTION" in s for s in chain)
    print(f"\nN={N}: {'CONTRADICTION FOUND' if has_contradiction else 'No contradiction'}")
    for s in chain:
        print(f"  {s}")
