#!/usr/bin/env python3
"""Optimized count of functions f: Z/16Z -> Z/16Z satisfying
   f(a)^2 + f(b)^2 + f(a+b)^2 ≡ 1 + 2*f(a)*f(b)*f(a+b) (mod 16) for all a,b."""

# Precompute: for each (x, y), the set of z with x^2+y^2+z^2 ≡ 1+2xyz (mod 16)
valid_z = [[set() for _ in range(16)] for _ in range(16)]
for x in range(16):
    for y in range(16):
        for z in range(16):
            if (x*x + y*y + z*z - 1 - 2*x*y*z) % 16 == 0:
                valid_z[x][y].add(z)

def backtrack(f, k):
    if k == 16:
        # verify ALL constraints including a+b >= 16
        for a in range(16):
            for b in range(a, 16):
                if f[(a+b) % 16] not in valid_z[f[a]][f[b]]:
                    return 0
        return 1
    # Compute candidate set for f[k] from all constraints (a, b) with a+b=k, a<=b, a,b<=k
    candidates = set(range(16))
    for a in range(k // 2 + 1):
        b = k - a
        if b > k:
            continue
        if a == 0:  # (0, k): x=f[0], y=f[k], z=f[k] => f[k] in valid_z[f[0]][f[k]]
            # f[k]^2 + f[0]^2 + f[k]^2 ≡ 1 + 2*f[0]*f[k]^2
            # i.e., f[k] is a valid z for (x=f[0], y=f[k])... but f[k] is unknown
            # Actually: check(f[0], f[k], f[k]) means f[k] in valid_z[f[0]][f[k]]
            # This is self-referential. Let's handle it differently.
            # The constraint is: 2*f[k]^2*(1-f[0]) ≡ 1-f[0]^2 (mod 16)
            # Precompute which fk values satisfy this
            cands = set()
            for fk in candidates:
                if (f[0]*f[0] + fk*fk + fk*fk - 1 - 2*f[0]*fk*fk) % 16 == 0:
                    cands.add(fk)
            candidates = cands
        elif a == b:  # (a, a) with 2a=k: x=f[a], y=f[a], z=f[k]
            candidates &= valid_z[f[a]][f[a]]
        else:  # (a, b) with a < b < k
            candidates &= valid_z[f[a]][f[b]]
        if not candidates:
            return 0
    count = 0
    for fk in candidates:
        f[k] = fk
        count += backtrack(f, k + 1)
    f[k] = None
    return count

total = 0
for f0 in [1, 5, 9, 13]:
    for f1 in range(16):
        f = [None]*16
        f[0] = f0
        f[1] = f1
        c = backtrack(f, 2)
        if c > 0:
            print(f"f0={f0}, f1={f1}: {c} functions")
        total += c

print(f"\nTotal N = {total}")
print(f"N mod 2017 = {total % 2017}")
