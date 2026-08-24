#!/usr/bin/env python3
"""
Optimized verification: check constraints incrementally during DFS.
"""
import sys

def sq_mod16(x):
    return (x*x) % 16

# Precompute: for given x, y, the set of valid z = f(a+b) values
# such that x^2 + y^2 + z^2 ≡ 1 + 2xyz (mod 16)
valid_z_cache = {}
def get_valid_z(x, y):
    key = (x, y)
    if key in valid_z_cache:
        return valid_z_cache[key]
    result = []
    for z in range(16):
        if (x*x + y*y + z*z - 1 - 2*x*y*z) % 16 == 0:
            result.append(z)
    valid_z_cache[key] = result
    return result

def count_case(choices_list):
    """Count solutions where f[a] ∈ choices_list[a], with incremental checking."""
    counter = [0]
    f = [0]*16
    
    def rec(k):
        if k == 16:
            # Final check: all pairs (a,b) where a+b wraps around (a+b >= 16)
            for a in range(16):
                fa = f[a]
                for b in range(16):
                    s = a + b
                    if s < 16:
                        continue  # already checked
                    c = s - 16  # (a+b) mod 16
                    fb = f[b]
                    fc = f[c]
                    if (fa*fa + fb*fb + fc*fc - 1 - 2*fa*fb*fc) % 16 != 0:
                        return
            counter[0] += 1
            return
        
        for v in choices_list[k]:
            f[k] = v
            # Check all pairs (a, b) with a+b = k, 0 <= a,b < k
            # (these are the pairs where both values are now known)
            ok = True
            for a in range(1, k):
                b = k - a
                if b < 1 or b >= k:
                    continue
                fa, fb = f[a], f[b]
                if (fa*fa + fb*fb + v*v - 1 - 2*fa*fb*v) % 16 != 0:
                    ok = False
                    break
            if ok:
                # Also check pair (0, k): f[0]^2 + f[k]^2 + f[k]^2 ≡ 1 + 2*f[0]*f[k]^2
                f0 = f[0]
                if (f0*f0 + 2*v*v - 1 - 2*f0*v*v) % 16 != 0:
                    ok = False
            if ok:
                rec(k+1)
        f[k] = 0
    
    rec(0)
    return counter[0]

# ---- Case A: f(0)=1, all f(a) in {1,7,9,15} ----
print("=== Case A ===", flush=True)
count_A = 0
for hom in range(2):
    choices = []
    for a in range(16):
        if a == 0:
            choices.append([1])
        elif hom == 0:
            choices.append([1, 9])
        else:
            choices.append([1, 9] if a % 2 == 0 else [7, 15])
    c = count_case(choices)
    print(f"  hom={hom}: {c}", flush=True)
    count_A += c
print(f"Case A total: {count_A} (expected {2**16})", flush=True)

# ---- Case B: even -> {1,7,9,15}, odd -> {0,4,8,12} ----
print("\n=== Case B ===", flush=True)
count_B = 0
for hom in range(2):
    choices = []
    for a in range(16):
        if a == 0:
            choices.append([1])
        elif a % 2 == 0:
            if hom == 0:
                choices.append([1, 9])
            else:
                choices.append([7, 15] if a % 4 == 2 else [1, 9])
        else:
            choices.append([0, 4, 8, 12])
    c = count_case(choices)
    print(f"  hom={hom}: {c}", flush=True)
    count_B += c
print(f"Case B total: {count_B}", flush=True)
print(f"Case B\\A: {count_B - count_A} (expected {2**24})", flush=True)

# ---- Case C: even -> {1,7,9,15}, odd -> {2,6,10,14} ----
print("\n=== Case C ===", flush=True)
count_C = 0
for hom in range(2):
    choices = []
    for a in range(16):
        if a == 0:
            choices.append([1])
        elif a % 2 == 0:
            if hom == 0:
                choices.append([1, 9])
            else:
                choices.append([7, 15] if a % 4 == 2 else [1, 9])
        else:
            choices.append([2, 6, 10, 14])
    c = count_case(choices)
    print(f"  hom={hom}: {c}", flush=True)
    count_C += c
print(f"Case C total: {count_C}", flush=True)
print(f"Case C\\A: {count_C - count_A} (expected {2**24})", flush=True)

# ---- Case D: sampling ----
print("\n=== Case D: sampling ===", flush=True)
import random
random.seed(42)
sample_size = 500000
count_D = 0
for _ in range(sample_size):
    hom = random.choice([0, 1])
    f = [0]*16
    f[0] = 1
    for a in range(1, 16):
        if hom == 0:
            f[a] = random.choice([1, 5, 9, 13])
        else:
            f[a] = random.choice([1, 5, 9, 13]) if a % 2 == 0 else random.choice([3, 7, 11, 15])
    ok = True
    for a in range(16):
        for b in range(16):
            if (f[a]**2 + f[b]**2 + f[(a+b)%16]**2 - 1 - 2*f[a]*f[b]*f[(a+b)%16]) % 16 != 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        count_D += 1
print(f"Case D sample: {count_D}/{sample_size} passed", flush=True)

# ---- Summary ----
print("\n=== Summary ===", flush=True)
DnotA = 2**31 - 2**16
N1 = count_A + (count_B - count_A) + (count_C - count_A) + DnotA
print(f"N_1 = {count_A} + {count_B - count_A} + {count_C - count_A} + {DnotA}")
print(f"N_1 = {N1}")
print(f"Expected: 2^25 + 2^31 = {2**25 + 2**31}")
print(f"Match: {N1 == 2**25 + 2**31}")

N5 = 2 * 4**15
N = 2 * N1 + 2 * N5
print(f"\nN_5 = {N5}")
print(f"N = 2*N_1 + 2*N_5 = {N}")
print(f"Expected: 2^26 + 2^33 = {2**26 + 2**33}")
print(f"Match: {N == 2**26 + 2**33}")
print(f"\nN mod 2017 = {N % 2017}")
