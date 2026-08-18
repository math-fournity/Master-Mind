#!/usr/bin/env python3
"""
Find the forcing chain for 3-regularity with full propagation.
When a variable has only one available color, assign it and continue propagating.
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
    sols = generate_solutions(N)

    # c(1)=0, c(2)=1, c(3)=2 (WLOG, forced by 2-regularity argument)
    color = {1: 0, 2: 1, 3: 2}
    forbidden = {}  # forbidden[n] = set of forbidden colors
    chain = []

    def add_forbidden(n, c, reason):
        """Add forbidden color c for number n. If only one color left, assign it."""
        if n in color:
            if color[n] == c:
                chain.append(f"CONTRADICTION: c({n})={c} but forbidden by {reason}")
                return True  # contradiction
            return False

        if n not in forbidden:
            forbidden[n] = set()
        if c in forbidden[n]:
            return False  # already forbidden

        forbidden[n].add(c)
        available = set(range(num_colors)) - forbidden[n]

        if len(available) == 0:
            chain.append(f"CONTRADICTION: c({n}) has no available color (forbidden: {sorted(forbidden[n])}) — {reason}")
            return True
        elif len(available) == 1:
            color[n] = list(available)[0]
            chain.append(f"c({n}) = {color[n]} (only option; {reason})")
            # Propagate: check all solutions involving n
            return propagate(n)
        else:
            chain.append(f"c({n}) ≠ {c} ({reason})")
            return False

    def propagate(n):
        """After assigning color[n], check all solutions involving n."""
        c_n = color[n]
        for (w, x, y, z) in sols:
            vals = [w, x, y, z]
            if n not in vals:
                continue

            # Get colors of all 4
            colors = []
            unassigned = []
            for v in vals:
                if v in color:
                    colors.append(color[v])
                else:
                    colors.append(None)
                    unassigned.append(v)

            if len(unassigned) == 0:
                # All assigned
                if colors[0] == colors[1] == colors[2] == colors[3]:
                    chain.append(f"CONTRADICTION: ({w},{x},{y},{z}) all color {colors[0]}")
                    return True
            elif len(unassigned) == 1:
                # 3 assigned, 1 unassigned
                assigned_colors = [c for c in colors if c is not None]
                if len(set(assigned_colors)) == 1:
                    # All 3 assigned have same color -> 4th must differ
                    u = unassigned[0]
                    sol_str = f"({w},{x},{y},{z})"
                    if add_forbidden(u, assigned_colors[0], f"3 same in {sol_str}"):
                        return True
        return False

    # Initial propagation from c(1)=0, c(2)=1, c(3)=2
    # First, the basic constraints:
    # (1,1,2,1): c(1)≠c(2) -> already satisfied
    # (3,1,3,1): c(1)≠c(3) -> already satisfied
    # (3,2,3,3): c(2)≠c(3) -> already satisfied

    # Propagate from each assigned variable
    for n in [1, 2, 3]:
        if propagate(n):
            break

    has_contradiction = any("CONTRADICTION" in s for s in chain)
    return chain, has_contradiction

print("=== Full forcing chain for 3-regularity ===")
for N in [10, 12, 14, 15, 16, 18, 20, 25, 30, 50]:
    chain, has_contradiction = find_forcing_chain(N, 3)
    print(f"\nN={N}: {'CONTRADICTION FOUND' if has_contradiction else 'No contradiction (need deeper search)'}")
    for s in chain:
        print(f"  {s}")
    if has_contradiction:
        break
