#!/usr/bin/env python3
"""
Check if a 3-coloring exists for the equation w + 6x = 2y + 3z
with no monochromatic solution (w,x,y,z positive integers).

Strategy:
1. First check if 2 colors work (brute force small numbers)
2. Then check if 3 colors work, using the structural constraint
   c(n) = (c_0(m) + v_2(n) - v_3(n)) % 3 where m is 6-free part
3. Enumerate constraints on c_0 and check satisfiability
"""

from itertools import product

def v2(n):
    """2-adic valuation"""
    if n == 0:
        return float('inf')
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def v3(n):
    """3-adic valuation"""
    if n == 0:
        return float('inf')
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c

def six_free_part(n):
    """Remove all factors of 2 and 3"""
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n

def is_6free(n):
    return n % 2 != 0 and n % 3 != 0

# Step 1: Brute force check for 2 colors (small range)
print("=== Checking 2 colors (brute force, N=20) ===")
N = 20

# Find all solutions (w,x,y,z) with w+6x=2y+3z, all in [1,N]
solutions = []
for w in range(1, N+1):
    for x in range(1, N+1):
        for y in range(1, N+1):
            val = w + 6*x - 2*y
            if val > 0 and val % 3 == 0:
                z = val // 3
                if 1 <= z <= N:
                    solutions.append((w, x, y, z))

print(f"Found {len(solutions)} solutions with all vars in [1,{N}]")

# Try all 2-colorings of [1,N]
found_2color = False
for coloring in product([0, 1], repeat=N):
    c = [0] + list(coloring)  # c[1..N]
    valid = True
    for (w, x, y, z) in solutions:
        if c[w] == c[x] == c[y] == c[z]:
            valid = False
            break
    if valid:
        print(f"2-coloring found: {c[1:]}")
        found_2color = True
        break

if not found_2color:
    print("No 2-coloring exists for N=20 (as expected)")

# Step 2: Check 3 colors with structural constraint
print("\n=== Checking 3 colors with structural constraint ===")
print("c(n) = (c_0(m) + v_2(n) - v_3(n)) % 3, m = 6-free part")

# For 3 colors, the constraint c(2t)!=c(t), c(3t)!=c(t), c(2t)!=c(3t)
# forces the structure c(n) = (c_0(m) + v2(n) - v3(n)) % 3

# We need to find c_0 on 6-free numbers such that no monochromatic solution exists

# Enumerate 6-free numbers up to N
N3 = 100  # check up to this bound
six_free_nums = [n for n in range(1, N3+1) if is_6free(n)]
print(f"6-free numbers up to {N3}: {six_free_nums[:20]}... ({len(six_free_nums)} total)")

# Find all solutions with all vars in [1, N3]
all_solutions = []
for w in range(1, N3+1):
    for x in range(1, N3+1):
        val = w + 6*x
        # val = 2y + 3z, need y >= 1, z >= 1
        # 2y = val - 3z, y = (val - 3z)/2
        for z in range(1, (val - 2) // 3 + 1):
            rem = val - 3*z
            if rem >= 2 and rem % 2 == 0:
                y = rem // 2
                if 1 <= y <= N3:
                    all_solutions.append((w, x, y, z))

print(f"Found {len(all_solutions)} solutions with all vars in [1,{N3}]")

# For each solution, compute the color constraint on c_0
# c(w) = (c_0(sf(w)) + v2(w) - v3(w)) % 3
# Monochromatic: c(w) = c(x) = c(y) = c(z)
# This means: c_0(sf(w)) + d_w = c_0(sf(x)) + d_x = c_0(sf(y)) + d_y = c_0(sf(z)) + d_z (mod 3)
# where d_i = v2(i) - v3(i)

# For each solution, the constraint is:
# NOT(c_0(sf(w)) + d_w ≡ c_0(sf(x)) + d_x ≡ c_0(sf(y)) + d_y ≡ c_0(sf(z)) + d_z (mod 3))

# Build constraints: each constraint involves the 6-free parts and shifts
constraints = []
for (w, x, y, z) in all_solutions:
    sf_w, sf_x, sf_y, sf_z = six_free_part(w), six_free_part(x), six_free_part(y), six_free_part(z)
    d_w, d_x, d_y, d_z = v2(w) - v3(w), v2(x) - v3(x), v2(y) - v3(y), v2(z) - v3(z)
    # Monochromatic condition: c_0(sf_w) + d_w = c_0(sf_x) + d_x = c_0(sf_y) + d_y = c_0(sf_z) + d_z (mod 3)
    # This means:
    # c_0(sf_w) = c_0(sf_x) + (d_x - d_w) = c_0(sf_y) + (d_y - d_w) = c_0(sf_z) + (d_z - d_w) (mod 3)
    shifts = [(sf_w, 0), (sf_x, (d_x - d_w) % 3), (sf_y, (d_y - d_w) % 3), (sf_z, (d_z - d_w) % 3)]
    constraints.append(shifts)

# Now we need to assign c_0 values to 6-free numbers (0, 1, or 2) such that
# for each constraint, NOT all four values are equal.
# A constraint (sf, shift) means the effective value is (c_0(sf) + shift) % 3.
# Monochromatic means all four effective values are equal.

# Get unique 6-free numbers involved
involved = set()
for c in constraints:
    for (sf, s) in c:
        involved.add(sf)
involved = sorted(involved)
print(f"6-free numbers involved: {involved[:20]}... ({len(involved)} total)")

# Try all 3-colorings of involved 6-free numbers
# (Only feasible if not too many)
if len(involved) <= 16:
    print(f"Trying all 3^{len(involved)} = {3**len(involved)} colorings...")
    idx = {sf: i for i, sf in enumerate(involved)}
    
    found = False
    count = 0
    for coloring in product([0, 1, 2], repeat=len(involved)):
        count += 1
        c0 = {sf: coloring[idx[sf]] for sf in involved}
        valid = True
        for c in constraints:
            vals = [(c0[sf] + s) % 3 for (sf, s) in c]
            if vals[0] == vals[1] == vals[2] == vals[3]:
                valid = False
                break
        if valid:
            print(f"3-coloring found! c_0 = {c0}")
            found = True
            # Verify with actual coloring
            def color(n):
                m = six_free_part(n)
                return (c0.get(m, 0) + v2(n) - v3(n)) % 3
            # Check all solutions
            all_ok = True
            for (w, x, y, z) in all_solutions:
                if color(w) == color(x) == color(y) == color(z):
                    print(f"  FAIL: ({w},{x},{y},{z}) all color {color(w)}")
                    all_ok = False
                    break
            if all_ok:
                print("  All solutions verified non-monochromatic!")
            break
    
    if not found:
        print("No 3-coloring exists for N=100!")
        print("Answer is at least 4")
else:
    print(f"Too many 6-free numbers ({len(involved)}), need smarter approach")
    # Use constraint propagation / backtracking
    print("Using backtracking search...")
    
    idx = {sf: i for i, sf in enumerate(involved)}
    
    # Build constraint list in terms of indices
    indexed_constraints = []
    for c in constraints:
        indexed = [(idx[sf], s) for (sf, s) in c]
        indexed_constraints.append(indexed)
    
    # Backtracking
    assignment = {}
    
    def check_partial(constraint):
        """Check if a constraint is already violated or could be satisfied"""
        vals = []
        for (i, s) in constraint:
            if i in assignment:
                vals.append((assignment[i] + s) % 3)
            else:
                return None  # can't determine yet
        if len(vals) == 4 and vals[0] == vals[1] == vals[2] == vals[3]:
            return False  # violated
        return True
    
    def backtrack(pos):
        if pos == len(involved):
            # Check all constraints
            for c in indexed_constraints:
                vals = [(assignment[ci] + s) % 3 for (ci, s) in c]
                if vals[0] == vals[1] == vals[2] == vals[3]:
                    return False
            return True
        
        sf = involved[pos]
        for color in range(3):
            assignment[pos] = color
            # Check constraints that are fully determined
            ok = True
            for c in indexed_constraints:
                vals = []
                determined = True
                for (ci, s) in c:
                    if ci in assignment:
                        vals.append((assignment[ci] + s) % 3)
                    else:
                        determined = False
                        break
                if determined and vals[0] == vals[1] == vals[2] == vals[3]:
                    ok = False
                    break
            if ok:
                if backtrack(pos + 1):
                    return True
            del assignment[pos]
        return False
    
    if backtrack(0):
        c0 = {involved[i]: assignment[i] for i in range(len(involved))}
        print(f"3-coloring found! c_0 = {c0}")
        # Print first few values
        def color(n):
            m = six_free_part(n)
            return (c0.get(m, 0) + v2(n) - v3(n)) % 3
        print("Colors for 1..30:", [color(n) for n in range(1, 31)])
        # Verify
        all_ok = True
        for (w, x, y, z) in all_solutions:
            if color(w) == color(x) == color(y) == color(z):
                print(f"  FAIL: ({w},{x},{y},{z}) all color {color(w)}")
                all_ok = False
        if all_ok:
            print("All solutions verified non-monochromatic!")
    else:
        print("No 3-coloring exists for N=100!")
        print("Answer is at least 4")
