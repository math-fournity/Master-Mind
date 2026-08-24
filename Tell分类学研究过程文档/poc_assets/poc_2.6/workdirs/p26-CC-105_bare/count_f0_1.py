#!/usr/bin/env python3
"""
Complete DFS count for f(0)=1 only, with aggressive pruning.
Uses iterative approach with precomputed constraint sets.
"""
import sys
from itertools import product

def count_f0_1():
    """Count all solutions with f(0) = 1."""
    f0 = 1
    count = 0
    
    # Precompute: for pair (x, y), the set of valid z values
    # such that x^2 + y^2 + z^2 ≡ 1 + 2xyz (mod 16)
    valid = {}
    for x in range(16):
        for y in range(16):
            valid[(x,y)] = set()
            for z in range(16):
                if (x*x + y*y + z*z - 1 - 2*x*y*z) % 16 == 0:
                    valid[(x,y)].add(z)
    
    # DFS: build f[0..15] in order
    # f[0] = 1
    # For k >= 1, constrain f[k] using pairs (a, k-a) with a < k and k-a < k
    # and pair (0, k)
    
    f = [0]*16
    f[0] = f0
    
    def dfs(k):
        nonlocal count
        if k == 16:
            # Check wrap-around pairs: (a, b) with a+b >= 16
            for a in range(16):
                fa = f[a]
                for b in range(16-a, 16):
                    c = a + b - 16
                    if (fa*fa + f[b]*f[b] + f[c]*f[c] - 1 - 2*fa*f[b]*f[c]) % 16 != 0:
                        return
            count += 1
            return
        
        # Compute candidates for f[k]
        cands = set(range(16))
        
        # Pairs (a, k-a) with 1 <= a <= k-1
        for a in range(1, k):
            b = k - a
            if b < 1 or b >= k:
                continue
            cands &= valid[(f[a], f[b])]
            if not cands:
                return
        
        # Pair (0, k): f[0]^2 + f[k]^2 + f[k]^2 ≡ 1 + 2*f[0]*f[k]^2
        # For f0=1: 1 + 2*f[k]^2 ≡ 1 + 2*f[k]^2, always true. No constraint.
        # (Already handled by the fact that valid[(1, z)] includes all z
        #  where 1 + z^2 + z^2 ≡ 1 + 2*z^2, i.e., 2*z^2 ≡ 2*z^2, always true)
        
        for v in cands:
            f[k] = v
            dfs(k+1)
    
    dfs(1)
    return count

print("Counting solutions for f(0)=1...", flush=True)
n1 = count_f0_1()
print(f"N_1 = {n1}", flush=True)
print(f"Expected: 2^25 + 2^31 = {2**25 + 2**31}", flush=True)
print(f"Match: {n1 == 2**25 + 2**31}", flush=True)
