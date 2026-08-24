#!/usr/bin/env python3
"""
Complete enumeration of Case B (even -> {1,7,9,15}, odd -> {0,4,8,12})
and Case C (even -> {1,7,9,15}, odd -> {2,6,10,14}).
These have 2^8 * 4^8 = 2^24 ≈ 16M paths each, feasible to enumerate.
"""
import sys
import time

def check_all_pairs(f):
    for a in range(16):
        fa2 = f[a]**2
        for b in range(16):
            c = (a+b) % 16
            if (fa2 + f[b]**2 + f[c]**2 - 1 - 2*f[a]*f[b]*f[c]) % 16 != 0:
                return False
    return True

def count_case_complete(even_choices_per_hom, odd_choices):
    """Count solutions by enumerating all even and odd combinations."""
    total = 0
    f = [0]*16
    f[0] = 1  # fixed
    
    for hom in range(2):
        even_vals = even_choices_per_hom[hom]
        # Enumerate all combinations of even elements (2,4,6,8,10,12,14)
        even_indices = [2, 4, 6, 8, 10, 12, 14]
        odd_indices = [1, 3, 5, 7, 9, 11, 13, 15]
        
        count_this_hom = 0
        
        for even_combo in product(*[even_vals[a] for a in even_indices]):
            for i, a in enumerate(even_indices):
                f[a] = even_combo[i]
            
            # Now enumerate all odd combinations
            for odd_combo in product(*[odd_choices for _ in odd_indices]):
                for i, a in enumerate(odd_indices):
                    f[a] = odd_combo[i]
                
                if check_all_pairs(f):
                    count_this_hom += 1
        
        print(f"  hom={hom}: {count_this_hom}", flush=True)
        total += count_this_hom
    
    return total

# Case B: even -> {1,9} or {7,15} (hom), odd -> {0,4,8,12}
print("=== Case B: complete enumeration ===", flush=True)
t0 = time.time()

even_choices_B = [
    {2: [1,9], 4: [1,9], 6: [1,9], 8: [1,9], 10: [1,9], 12: [1,9], 14: [1,9]},  # hom=0
    {2: [7,15], 4: [1,9], 6: [7,15], 8: [1,9], 10: [7,15], 12: [1,9], 14: [7,15]},  # hom=1
]

# This is 2^7 * 4^8 = 128 * 65536 = 8,388,608 per hom, ~16M total
# Each requires 256 pair checks = ~4 billion ops. Too slow in Python.
# Let me optimize: only check wrap-around pairs, since non-wrap pairs are
# automatically satisfied by construction.

def check_wrap_only(f):
    """Only check pairs (a,b) where a+b >= 16 (wrap-around)."""
    for a in range(16):
        fa2 = f[a]**2
        fa = f[a]
        for b in range(16-a, 16):
            c = a + b - 16
            if (fa2 + f[b]**2 + f[c]**2 - 1 - 2*fa*f[b]*f[c]) % 16 != 0:
                return False
    return True

def count_case_fast(even_choices_per_hom, odd_choices):
    """Count using incremental DFS with pruning on wrap-around pairs."""
    total = 0
    f = [0]*16
    f[0] = 1
    
    for hom in range(2):
        even_vals = even_choices_per_hom[hom]
        even_indices = [2, 4, 6, 8, 10, 12, 14]
        odd_indices = [1, 3, 5, 7, 9, 11, 13, 15]
        
        count_h = [0]
        
        def rec_even(idx):
            if idx == len(even_indices):
                rec_odd(0)
                return
            a = even_indices[idx]
            for v in even_vals[a]:
                f[a] = v
                # Check pairs (a2, b2) with a2+b2 = a, both already set
                ok = True
                for a2 in range(1, a):
                    b2 = a - a2
                    if b2 < 1 or b2 >= a:
                        continue
                    if b2 in even_indices[:idx] or b2 == 0:
                        if (f[a2]**2 + f[b2]**2 + v**2 - 1 - 2*f[a2]*f[b2]*v) % 16 != 0:
                            ok = False
                            break
                if ok:
                    rec_even(idx+1)
            f[a] = 0
        
        def rec_odd(idx):
            if idx == len(odd_indices):
                # Check all wrap-around pairs
                if check_wrap_only(f):
                    count_h[0] += 1
                return
            a = odd_indices[idx]
            for v in odd_choices:
                f[a] = v
                # Check pairs (a2, b2) with a2+b2 = a, both already set
                ok = True
                for a2 in range(1, a):
                    b2 = a - a2
                    if b2 < 1 or b2 >= a:
                        continue
                    if (f[a2]**2 + f[b2]**2 + v**2 - 1 - 2*f[a2]*f[b2]*v) % 16 != 0:
                        ok = False
                        break
                if ok:
                    rec_odd(idx+1)
            f[a] = 0
        
        rec_even(0)
        print(f"  hom={hom}: {count_h[0]}", flush=True)
        total += count_h[0]
    
    return total

print("Case B:", flush=True)
count_B = count_case_fast(even_choices_B, [0, 4, 8, 12])
print(f"Case B total: {count_B}", flush=True)
print(f"Time: {time.time()-t0:.1f}s", flush=True)

# Case C: even -> same, odd -> {2,6,10,14}
print("\nCase C:", flush=True)
t0 = time.time()
even_choices_C = even_choices_B  # same even choices
count_C = count_case_fast(even_choices_C, [2, 6, 10, 14])
print(f"Case C total: {count_C}", flush=True)
print(f"Time: {time.time()-t0:.1f}s", flush=True)

# Case A: all in {1,7,9,15}
print("\nCase A:", flush=True)
t0 = time.time()
even_choices_A = [
    {2: [1,9], 4: [1,9], 6: [1,9], 8: [1,9], 10: [1,9], 12: [1,9], 14: [1,9]},
    {2: [7,15], 4: [1,9], 6: [7,15], 8: [1,9], 10: [7,15], 12: [1,9], 14: [7,15]},
]
count_A = count_case_fast(even_choices_A, [1, 7, 9, 15])
print(f"Case A total: {count_A} (expected {2**16})", flush=True)
print(f"Time: {time.time()-t0:.1f}s", flush=True)

print(f"\n=== Summary ===")
print(f"Case A: {count_A}")
print(f"Case B\\A: {count_B - count_A} (expected {2**24})")
print(f"Case C\\A: {count_C - count_A} (expected {2**24})")
print(f"Case D\\A: {2**31 - 2**16} (analytical)")
print(f"N_1 = {count_A + (count_B - count_A) + (count_C - count_A) + (2**31 - 2**16)}")
print(f"Expected: {2**25 + 2**31}")
