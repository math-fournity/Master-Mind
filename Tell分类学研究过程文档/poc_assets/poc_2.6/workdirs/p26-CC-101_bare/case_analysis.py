#!/usr/bin/env python3
"""
Exhaustive case analysis for 3-regularity.
Show that every 3-coloring of {1,...,12} with c(1)=0, c(2)=1, c(3)=2 fails.
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

def check_partial(color_dict, sols):
    """Check if a partial coloring (dict) has any monochromatic solution."""
    for (w, x, y, z) in sols:
        if all(v in color_dict for v in [w, x, y, z]):
            if color_dict[w] == color_dict[x] == color_dict[y] == color_dict[z]:
                return (w, x, y, z)
    return None

def find_forced(color_dict, forbidden_dict, sols, num_colors=3):
    """Find variables forced to a single color or with contradictions."""
    changed = True
    while changed:
        changed = False
        for (w, x, y, z) in sols:
            vals = [w, x, y, z]
            colors = [color_dict.get(v, None) for v in vals]
            unassigned = [(i, vals[i]) for i in range(4) if colors[i] is None]

            if len(unassigned) == 0:
                if colors[0] == colors[1] == colors[2] == colors[3]:
                    return None, f"Mono ({w},{x},{y},{z}) color {colors[0]}"
            elif len(unassigned) == 1:
                assigned_colors = [c for c in colors if c is not None]
                if len(set(assigned_colors)) == 1:
                    idx, u = unassigned[0]
                    fc = assigned_colors[0]
                    if u in color_dict and color_dict[u] == fc:
                        return None, f"c({u})={fc} conflicts with ({w},{x},{y},{z})"
                    if u not in forbidden_dict:
                        forbidden_dict[u] = set()
                    if fc not in forbidden_dict[u]:
                        forbidden_dict[u].add(fc)
                        changed = True
                        avail = set(range(num_colors)) - forbidden_dict[u]
                        if len(avail) == 0:
                            return None, f"c({u}) no color left (forbidden {sorted(forbidden_dict[u])}) from ({w},{x},{y},{z})"
                        elif len(avail) == 1:
                            color_dict[u] = list(avail)[0]

    return color_dict, None

N = 12
sols = generate_solutions(N)

# Base: c(1)=0, c(2)=1, c(3)=2
base = {1: 0, 2: 1, 3: 2}
base_forbidden = {}

# First propagate from base
result, err = find_forced(dict(base), dict(base_forbidden), sols)
if err:
    print(f"Base propagation fails: {err}")
else:
    print(f"After base propagation:")
    print(f"  Assigned: {dict(sorted(result.items()))}")
    print(f"  Forbidden: {dict(sorted((k, sorted(v)) for k, v in base_forbidden.items() if v))}")

    # Now try all combinations for unassigned variables 4..N
    # The forbidden sets tell us:
    # c(4) ∈ {0, 2} (≠ 1)
    # c(5) ∈ {0, 1} (≠ 2)
    # c(6) ∈ {0, 1} (≠ 2)

    # Let's do case analysis on c(4), c(5), c(6)
    from itertools import product

    c4_options = [0, 2]
    c5_options = [0, 1]
    c6_options = [0, 1]

    print(f"\nCase analysis on c(4)∈{c4_options}, c(5)∈{c5_options}, c(6)∈{c6_options}:")
    print(f"Total branches: {len(c4_options)*len(c5_options)*len(c6_options)}")

    all_fail = True
    for c4, c5, c6 in product(c4_options, c5_options, c6_options):
        cd = dict(base)
        cd[4] = c4
        cd[5] = c5
        cd[6] = c6

        fd = {}
        # Re-derive forbidden from base
        for (w, x, y, z) in sols:
            vals = [w, x, y, z]
            colors = [cd.get(v, None) for v in vals]
            unassigned = [(i, vals[i]) for i in range(4) if colors[i] is None]
            if len(unassigned) == 1:
                assigned_colors = [c for c in colors if c is not None]
                if len(set(assigned_colors)) == 1:
                    u = unassigned[0][1]
                    fc = assigned_colors[0]
                    if u not in fd:
                        fd[u] = set()
                    fd[u].add(fc)

        result, err = find_forced(cd, fd, sols)
        if err:
            print(f"  c(4)={c4}, c(5)={c5}, c(6)={c6}: FAIL - {err}")
        else:
            # Need to continue assigning
            unassigned_vars = [v for v in range(1, N+1) if v not in result]
            if not unassigned_vars:
                print(f"  c(4)={c4}, c(5)={c5}, c(6)={c6}: SUCCESS - {result}")
                all_fail = False
            else:
                # Try to complete with backtracking
                def bt(vars_left, cd, fd):
                    if not vars_left:
                        return cd
                    v = vars_left[0]
                    avail = set(range(3)) - fd.get(v, set())
                    for c in sorted(avail):
                        cd2 = dict(cd)
                        cd2[v] = c
                        fd2 = {k: set(s) for k, s in fd.items()}
                        r, e = find_forced(cd2, fd2, sols)
                        if e:
                            continue
                        remaining = [x for x in vars_left[1:] if x not in r]
                        res = bt(remaining, r, fd2)
                        if res:
                            return res
                    return None

                res = bt(unassigned_vars, result, fd)
                if res:
                    print(f"  c(4)={c4}, c(5)={c5}, c(6)={c6}: SUCCESS - {dict(sorted(res.items()))}")
                    all_fail = False
                else:
                    print(f"  c(4)={c4}, c(5)={c5}, c(6)={c6}: FAIL (backtracking)")

    if all_fail:
        print(f"\nAll branches fail => 3-coloring impossible for N={N}")
