#!/usr/bin/env python3
"""Brute-force count of functions f: Z/16Z -> Z/16Z satisfying
   f(a)^2 + f(b)^2 + f(a+b)^2 ≡ 1 + 2*f(a)*f(b)*f(a+b) (mod 16) for all a,b."""

def check(x, y, z):
    return (x*x + y*y + z*z - 1 - 2*x*y*z) % 16 == 0

def backtrack(f, k):
    if k == 16:
        # verify ALL constraints including a+b >= 16
        for a in range(16):
            for b in range(a, 16):
                if not check(f[a], f[b], f[(a+b) % 16]):
                    return 0
        return 1
    count = 0
    for fk in range(16):
        f[k] = fk
        ok = True
        for a in range(k // 2 + 1):
            b = k - a
            if b > k:
                continue
            if a == 0:  # (0, k): f[0], f[k], f[k]
                if not check(f[0], f[k], f[k]):
                    ok = False; break
            elif a == b:  # (a,a) with 2a=k
                if not check(f[a], f[a], f[k]):
                    ok = False; break
            else:  # (a, b) with a < b < k
                if not check(f[a], f[b], f[k]):
                    ok = False; break
        if ok:
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
