#!/usr/bin/env python3
"""Check if specific partial colorings of {1..12} have monochromatic solutions."""

def find_solutions(N):
    solutions = []
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                w = 2 * y + 3 * z - 6 * x
                if 1 <= w <= N:
                    solutions.append((w, x, y, z))
    return solutions

sols = find_solutions(12)

# Case I: c(1)=A=0, c(2)=B=1, c(3)=C=2
# Derived: c(4)=C=2, c(5)=B=1, c(6)=A=0, c(7)=A=0, c(8)=B=1, c(9)=B=1, c(12)=A=0
# c(10) in {A=0, C=2}, c(11) in {B=1, C=2}, NOT(c(10)=2 and c(11)=2)

# Try all valid combinations of c(10), c(11)
for c10 in [0, 2]:
    for c11 in [1, 2]:
        if c10 == 2 and c11 == 2:
            continue  # excluded
        coloring = {1:0, 2:1, 3:2, 4:2, 5:1, 6:0, 7:0, 8:1, 9:1, 10:c10, 11:c11, 12:0}
        bad = []
        for (w, x, y, z) in sols:
            if coloring[w] == coloring[x] == coloring[y] == coloring[z]:
                bad.append((w, x, y, z, coloring[w]))
        if bad:
            print(f"c(10)={c10}, c(11)={c11}: {len(bad)} mono solutions")
            for s in bad:
                print(f"  {s}")
        else:
            print(f"c(10)={c10}, c(11)={c11}: NO mono solutions (valid!)")

print()
# Also check Sub-case I-b: c(7)=B, c(5)=A
print("=== Sub-case I-b: c(7)=B=1, c(5)=A=0 ===")
for c10 in [0, 2]:
    for c11 in [1, 2]:
        if c10 == 2 and c11 == 2:
            continue
        # Need to re-derive constraints for this sub-case
        # c(1)=0, c(2)=1, c(3)=2, c(4)=2, c(5)=0, c(6)=0, c(7)=1, c(8)=?, c(9)=1, c(12)=0
        # From (8,2,7,2): c(8)≠B or c(7)≠B. c(7)=B=1, so c(8)≠1. c(8)∈{0,2} but c(8)≠C=2, so c(8)=0.
        # Wait, c(8)≠C from earlier. c(8)∈{A=0,B=1}. c(8)≠B=1. So c(8)=0.
        # From (8,7,7,12): c(8)=c(7)=c(7)=c(12). c(7)=1, c(12)=0. 1≠0. ✓
        # Actually let me re-derive c(8) for this sub-case.
        # From (8,4,4,8): c(8)≠c(4)=C=2. So c(8)∈{0,1}.
        # From (8,2,7,2): c(8)≠B=1 or c(7)≠B=1. c(7)=1, so c(8)≠1. c(8)=0.
        # From (8,7,7,12): c(8)=0, c(7)=1, c(12)=0. c(8)=c(12)=0, c(7)=1. Not all same. ✓
        coloring = {1:0, 2:1, 3:2, 4:2, 5:0, 6:0, 7:1, 8:0, 9:1, 10:c10, 11:c11, 12:0}
        bad = []
        for (w, x, y, z) in sols:
            if coloring[w] == coloring[x] == coloring[y] == coloring[z]:
                bad.append((w, x, y, z, coloring[w]))
        if bad:
            print(f"c(10)={c10}, c(11)={c11}: {len(bad)} mono solutions")
            for s in bad:
                print(f"  {s}")
        else:
            print(f"c(10)={c10}, c(11)={c11}: NO mono solutions (valid!)")

print()
# Case II: c(1)=A=0, c(2)=B=1, c(3)=B=1
print("=== Case II: c(1)=0, c(2)=1, c(3)=1 ===")
# From (4,2,2,4): c(4)≠B=1. c(4)∈{0,2}
# From (6,3,3,6): c(6)≠B=1. c(6)∈{0,2}
# From (8,4,4,8): c(8)≠c(4)
# From (9,3,3,9)? Not a solution. (9,1,3,3): c(9)=c(1)=c(3). c(1)=0, c(3)=1. ✓
# From (3,3,3,5): c(3)=c(3)=c(3)=c(5). c(3)=1. Need c(5)≠1. c(5)∈{0,2}
# From (6,2,6,2): c(6)=c(2)=c(6)=c(2). c(2)=1. Need c(6)≠1. Already have.
# From (6,4,6,6): c(6)=c(4)=c(6)=c(6). Need c(6)≠c(4).

# Let me try all possible colorings for c(4), c(5), c(6), c(7), c(8), c(9), c(10), c(11), c(12)
# with c(1)=0, c(2)=1, c(3)=1, c(4)∈{0,2}, c(5)∈{0,2}, c(6)∈{0,2}, c(6)≠c(4)
# This is too many. Let me use SAT or brute force.

from itertools import product

count = 0
found_valid = False
for c4, c5, c6, c7, c8, c9, c10, c11, c12 in product([0,1,2], repeat=9):
    coloring = {1:0, 2:1, 3:1, 4:c4, 5:c5, 6:c6, 7:c7, 8:c8, 9:c9, 10:c10, 11:c11, 12:c12}
    bad = False
    for (w, x, y, z) in sols:
        if coloring[w] == coloring[x] == coloring[y] == coloring[z]:
            bad = True
            break
    if not bad:
        print(f"  Valid coloring found: {coloring}")
        found_valid = True
        count += 1
        if count >= 3:
            break

if not found_valid:
    print("  No valid coloring exists (UNSAT confirmed for Case II)")
