#!/usr/bin/env python3
"""Trace the two backtracking branches in detail."""

def generate_solutions(N):
    solutions = []
    for x in range(1, N+1):
        for y in range(1, N+1):
            for z in range(1, N+1):
                w = 2*y + 3*z - 6*x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))
    return solutions

def find_forced(cd, fd, sols, num_colors=3, trace=None, indent=""):
    """Propagate constraints."""
    changed = True
    while changed:
        changed = False
        for (w, x, y, z) in sols:
            vals = [w, x, y, z]
            colors = [cd.get(v, None) for v in vals]
            unassigned = [(i, vals[i]) for i in range(4) if colors[i] is None]

            if len(unassigned) == 0:
                if colors[0] == colors[1] == colors[2] == colors[3]:
                    if trace is not None:
                        trace.append(f"{indent}CONTRADICTION: ({w},{x},{y},{z}) all color {colors[0]}")
                    return None, f"Mono ({w},{x},{y},{z}) color {colors[0]}"
            elif len(unassigned) == 1:
                assigned_colors = [c for c in colors if c is not None]
                if len(set(assigned_colors)) == 1:
                    idx, u = unassigned[0]
                    fc = assigned_colors[0]
                    if u in cd and cd[u] == fc:
                        if trace is not None:
                            trace.append(f"{indent}CONTRADICTION: c({u})={fc} but ({w},{x},{y},{z}) needs different")
                        return None, f"c({u})={fc} conflicts"
                    if u not in fd:
                        fd[u] = set()
                    if fc not in fd[u]:
                        fd[u].add(fc)
                        changed = True
                        avail = set(range(num_colors)) - fd[u]
                        if len(avail) == 0:
                            if trace is not None:
                                trace.append(f"{indent}CONTRADICTION: c({u}) no color left (forbidden {sorted(fd[u])}) from ({w},{x},{y},{z})")
                            return None, f"c({u}) no color left"
                        elif len(avail) == 1:
                            cd[u] = list(avail)[0]
                            if trace is not None:
                                trace.append(f"{indent}c({u})={cd[u]} (forced, ≠{fc} from ({w},{x},{y},{z}))")
    return cd, None

N = 12
sols = generate_solutions(N)
base = {1: 0, 2: 1, 3: 2}

def full_backtrace(cd, fd, sols, N, trace, indent=""):
    """Complete backtracking with trace."""
    # Find next unassigned
    for v in range(1, N+1):
        if v not in cd:
            avail = set(range(3)) - fd.get(v, set())
            for c in sorted(avail):
                trace.append(f"{indent}Try c({v})={c}")
                cd2 = dict(cd)
                cd2[v] = c
                fd2 = {k: set(s) for k, s in fd.items()}

                r, err = find_forced(cd2, fd2, sols, trace=trace, indent=indent+"  ")
                if err:
                    continue

                res = full_backtrace(r, fd2, sols, N, trace, indent+"  ")
                if res is not None:
                    return res
            return None
    return cd  # All assigned

# Trace branch 1: c(4)=2, c(5)=0, c(6)=0
print("=== Branch: c(4)=2, c(5)=0, c(6)=0 ===")
cd = dict(base)
cd[4] = 2; cd[5] = 0; cd[6] = 0
fd = {}
trace = []
r, err = find_forced(cd, fd, sols, trace=trace)
if err:
    for s in trace:
        print(s)
else:
    print(f"After propagation: {dict(sorted(r.items()))}")
    print(f"Forbidden: {dict(sorted((k, sorted(v)) for k, v in fd.items() if v))}")
    res = full_backtrace(r, fd, sols, N, trace)
    if res is None:
        for s in trace:
            print(s)
        print("=> IMPOSSIBLE")
    else:
        print(f"Solution found: {res}")

# Trace branch 2: c(4)=2, c(5)=1, c(6)=0
print("\n=== Branch: c(4)=2, c(5)=1, c(6)=0 ===")
cd = dict(base)
cd[4] = 2; cd[5] = 1; cd[6] = 0
fd = {}
trace = []
r, err = find_forced(cd, fd, sols, trace=trace)
if err:
    for s in trace:
        print(s)
else:
    print(f"After propagation: {dict(sorted(r.items()))}")
    print(f"Forbidden: {dict(sorted((k, sorted(v)) for k, v in fd.items() if v))}")
    res = full_backtrace(r, fd, sols, N, trace)
    if res is None:
        for s in trace:
            print(s)
        print("=> IMPOSSIBLE")
    else:
        print(f"Solution found: {res}")
