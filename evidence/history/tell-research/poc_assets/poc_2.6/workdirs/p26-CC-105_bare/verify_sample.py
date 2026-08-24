#!/usr/bin/env python3
"""
Efficient verification: verify the key claims by sampling.
"""
import random
random.seed(12345)

def check_all_pairs(f):
    for a in range(16):
        fa2 = f[a]**2
        for b in range(16):
            c = (a+b) % 16
            if (fa2 + f[b]**2 + f[c]**2 - 1 - 2*f[a]*f[b]*f[c]) % 16 != 0:
                return False
    return True

# ---- Verify Case A: 2^16 = 65536 ----
# Already verified above. Skip.

# ---- Verify Case B: key claim is that odd elements are free ----
# Fix hom=0, even elements all = 1 (simplest case), vary odd elements
print("=== Case B: odd elements free? ===")
f_base = [1]*16  # all 1's (hom=0, all even = 1)
# This is in Case A. Let's use a non-Case-A config.
# hom=0: even elements all in {1,9}. Let's set f[2]=9 (non-trivial).
# odd elements in {0,4,8,12}

fail_count = 0
sample_size = 100000
for _ in range(sample_size):
    f = [0]*16
    f[0] = 1
    # even elements: hom=0, all in {1,9}
    f[2] = random.choice([1, 9])
    f[4] = random.choice([1, 9])
    f[6] = random.choice([1, 9])
    f[8] = random.choice([1, 9])
    f[10] = random.choice([1, 9])
    f[12] = random.choice([1, 9])
    f[14] = random.choice([1, 9])
    # odd elements: free in {0,4,8,12}
    for a in [1, 3, 5, 7, 9, 11, 13, 15]:
        f[a] = random.choice([0, 4, 8, 12])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"hom=0: {fail_count}/{sample_size} failures")

# hom=1: even elements with homomorphism
fail_count = 0
for _ in range(sample_size):
    f = [0]*16
    f[0] = 1
    # hom=1 on Z/8Z (even elements): a=2,6,10,14 -> {7,15}, a=4,8,12 -> {1,9}
    f[2] = random.choice([7, 15])
    f[4] = random.choice([1, 9])
    f[6] = random.choice([7, 15])
    f[8] = random.choice([1, 9])
    f[10] = random.choice([7, 15])
    f[12] = random.choice([1, 9])
    f[14] = random.choice([7, 15])
    for a in [1, 3, 5, 7, 9, 11, 13, 15]:
        f[a] = random.choice([0, 4, 8, 12])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"hom=1: {fail_count}/{sample_size} failures")

# ---- Verify Case C: odd elements free in {2,6,10,14} ----
print("\n=== Case C: odd elements free? ===")
fail_count = 0
for _ in range(sample_size):
    f = [0]*16
    f[0] = 1
    f[2] = random.choice([1, 9])
    f[4] = random.choice([1, 9])
    f[6] = random.choice([1, 9])
    f[8] = random.choice([1, 9])
    f[10] = random.choice([1, 9])
    f[12] = random.choice([1, 9])
    f[14] = random.choice([1, 9])
    for a in [1, 3, 5, 7, 9, 11, 13, 15]:
        f[a] = random.choice([2, 6, 10, 14])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"hom=0: {fail_count}/{sample_size} failures")

fail_count = 0
for _ in range(sample_size):
    f = [0]*16
    f[0] = 1
    f[2] = random.choice([7, 15])
    f[4] = random.choice([1, 9])
    f[6] = random.choice([7, 15])
    f[8] = random.choice([1, 9])
    f[10] = random.choice([7, 15])
    f[12] = random.choice([1, 9])
    f[14] = random.choice([7, 15])
    for a in [1, 3, 5, 7, 9, 11, 13, 15]:
        f[a] = random.choice([2, 6, 10, 14])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"hom=1: {fail_count}/{sample_size} failures")

# ---- Verify Case D: all odd, homomorphism mod 4 ----
print("\n=== Case D: all odd, homomorphism mod 4? ===")
fail_count = 0
for _ in range(sample_size):
    hom = random.choice([0, 1])
    f = [0]*16
    f[0] = 1
    for a in range(1, 16):
        if hom == 0:
            f[a] = random.choice([1, 5, 9, 13])
        else:
            f[a] = random.choice([1, 5, 9, 13]) if a % 2 == 0 else random.choice([3, 7, 11, 15])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"Case D: {fail_count}/{sample_size} failures")

# ---- Verify f(0)=5: all odd, homomorphism mod 4 ----
print("\n=== f(0)=5: all odd, homomorphism mod 4? ===")
fail_count = 0
for _ in range(sample_size):
    hom = random.choice([0, 1])
    f = [0]*16
    f[0] = 5
    for a in range(1, 16):
        if hom == 0:
            f[a] = random.choice([1, 5, 9, 13])
        else:
            f[a] = random.choice([1, 5, 9, 13]) if a % 2 == 0 else random.choice([3, 7, 11, 15])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"f(0)=5: {fail_count}/{sample_size} failures")

# ---- Verify f(0)=9: same as f(0)=1 ----
print("\n=== f(0)=9: same equations as f(0)=1? ===")
fail_count = 0
for _ in range(sample_size):
    # Random all-odd function with f(0)=9
    hom = random.choice([0, 1])
    f = [0]*16
    f[0] = 9
    for a in range(1, 16):
        if hom == 0:
            f[a] = random.choice([1, 5, 9, 13])
        else:
            f[a] = random.choice([1, 5, 9, 13]) if a % 2 == 0 else random.choice([3, 7, 11, 15])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"f(0)=9 (Case D): {fail_count}/{sample_size} failures")

# Also test f(0)=9 with Case B structure
fail_count = 0
for _ in range(sample_size):
    f = [0]*16
    f[0] = 9
    f[2] = random.choice([1, 9])
    f[4] = random.choice([1, 9])
    f[6] = random.choice([1, 9])
    f[8] = random.choice([1, 9])
    f[10] = random.choice([1, 9])
    f[12] = random.choice([1, 9])
    f[14] = random.choice([1, 9])
    for a in [1, 3, 5, 7, 9, 11, 13, 15]:
        f[a] = random.choice([0, 4, 8, 12])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"f(0)=9 (Case B): {fail_count}/{sample_size} failures")

# ---- Verify f(0)=13: same as f(0)=5 ----
print("\n=== f(0)=13: same equations as f(0)=5? ===")
fail_count = 0
for _ in range(sample_size):
    hom = random.choice([0, 1])
    f = [0]*16
    f[0] = 13
    for a in range(1, 16):
        if hom == 0:
            f[a] = random.choice([1, 5, 9, 13])
        else:
            f[a] = random.choice([1, 5, 9, 13]) if a % 2 == 0 else random.choice([3, 7, 11, 15])
    if not check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  FAIL: f={f}")
print(f"f(0)=13 (Case D): {fail_count}/{sample_size} failures")

# ---- Also verify: non-homomorphism all-odd functions FAIL ----
print("\n=== Negative test: non-homomorphism all-odd should FAIL ===")
fail_count = 0  # count of passes (should be 0 or very few)
for _ in range(sample_size):
    f = [0]*16
    f[0] = 1
    for a in range(1, 16):
        f[a] = random.choice([1, 3, 5, 7, 9, 11, 13, 15])  # all odd, no homomorphism constraint
    if check_all_pairs(f):
        fail_count += 1
        if fail_count <= 5:
            print(f"  PASS (unexpected): f={f}")
            # Check if it's actually a homomorphism
            is_hom = all(f[a] % 4 == (1 if a % 2 == 0 else 3) for a in range(16)) or \
                     all(f[a] % 4 == 1 for a in range(16))
            print(f"  Is homomorphism? {is_hom}")
print(f"Non-hom all-odd: {fail_count}/{sample_size} passed (expect ~0)")

# ---- Final computation ----
print("\n=== Final Answer ===")
N1 = 2**25 + 2**31
N5 = 2 * 4**15
N = 2 * N1 + 2 * N5
print(f"N_1 = 2^25 + 2^31 = {N1}")
print(f"N_5 = 2*4^15 = {N5}")
print(f"N = 2*N_1 + 2*N_5 = {N}")
print(f"N = 2^26 + 2^33 = {2**26 + 2**33}")
print(f"N mod 2017 = {N % 2017}")

# Verify 2^26 mod 2017 and 2^33 mod 2017
p = 1
for i in range(33):
    p = (p * 2) % 2017
    if i+1 in [26, 33]:
        print(f"2^{i+1} mod 2017 = {p}")
