#!/usr/bin/env python3
"""
Count functions f: Z/16Z -> Z/16Z satisfying
  f(a)^2 + f(b)^2 + f(a+b)^2 ≡ 1 + 2 f(a) f(b) f(a+b)  (mod 16)
for all a,b.

Strategy: DFS building f[0..15], using constraints from pairs (a,b) with
a+b = k (mod 16) where both f[a], f[b] already known, plus the (0,k) constraint.
At the end, verify all 256 pairs (including wrap-around).
"""

import sys

def qr_mod16():
    """Return set of quadratic residues mod 16 and the preimage map."""
    sq = {}
    for w in range(16):
        r = (w*w) % 16
        sq.setdefault(r, []).append(w)
    return sq

SQ = qr_mod16()

def candidates_from_pair(x, y):
    """Given f[a]=x, f[b]=y, return set of possible f[a+b] values."""
    h = ((x*x - 1) * (y*y - 1)) % 16
    if h not in SQ:
        return set()
    result = set()
    for w in SQ[h]:
        result.add((x*y + w) % 16)
    return result

def constraint_0k(f0, fk_candidates):
    """Apply constraint from pair (0,k) given f[0]=f0."""
    # (f[k] - f[0]*f[k])^2 = (f[0]^2-1)(f[k]^2-1) mod 16
    # Simplified: for f0=1 or 9 -> no constraint; for f0=5 or 13 -> f[k] odd
    if f0 == 5 or f0 == 13:
        return {z for z in fk_candidates if z % 2 == 1}
    return fk_candidates

def count_for_f0(f0):
    """Count solutions with f[0] = f0."""
    total = [0]
    
    for f1 in range(16):
        f = [None]*16
        f[0] = f0
        f[1] = f1
        
        def dfs(k):
            if k == 16:
                # verify all 256 pairs
                for a in range(16):
                    fa = f[a]
                    fa2 = fa*fa
                    for b in range(16):
                        fb = f[b]
                        fc = f[(a+b)%16]
                        lhs = (fa2 + fb*fb + fc*fc) % 16
                        rhs = (1 + 2*fa*fb*fc) % 16
                        if lhs != rhs:
                            return
                total[0] += 1
                return
            
            # candidates from pairs (a, k-a) with 1 <= a <= k-1, both < k
            cands = None
            for a in range(1, k):
                b = k - a
                if b < 1 or b >= k:
                    continue
                cs = candidates_from_pair(f[a], f[b])
                if cands is None:
                    cands = cs
                else:
                    cands = cands & cs
                if not cands:
                    return
            
            if cands is None:
                cands = set(range(16))
            
            # constraint from (0, k)
            cands = constraint_0k(f0, cands)
            if not cands:
                return
            
            for z in sorted(cands):
                f[k] = z
                dfs(k+1)
                f[k] = None
        
        dfs(2)
    
    return total[0]

def main():
    results = {}
    for f0 in [1, 5, 9, 13]:
        n = count_for_f0(f0)
        results[f0] = n
        print(f"f(0)={f0}: N={n}", flush=True)
    
    N = sum(results.values())
    print(f"\nTotal N = {N}")
    print(f"N mod 2017 = {N % 2017}")
    
    # Also print the breakdown
    print(f"\nBreakdown:")
    print(f"  N_1 (f0=1) = {results[1]}")
    print(f"  N_9 (f0=9) = {results[9]}")
    print(f"  N_5 (f0=5) = {results[5]}")
    print(f"  N_13 (f0=13) = {results[13]}")

if __name__ == '__main__':
    main()
