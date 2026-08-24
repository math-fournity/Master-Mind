#!/usr/bin/env python3
"""
Verify the case analysis for Z/16Z mod 16 by directly enumerating each case.
"""

def check_all_pairs(f):
    for a in range(16):
        fa = f[a]
        fa2 = fa*fa
        for b in range(16):
            fb = f[b]
            fc = f[(a+b)%16]
            if (fa2 + fb*fb + fc*fc - 1 - 2*fa*fb*fc) % 16 != 0:
                return False
    return True

def enumerate_case(choices):
    """Given choices[a] = list of possible values for f[a], enumerate all
    and count how many satisfy the equation."""
    counter = [0]
    f = [None]*16
    def rec(idx):
        if idx == 16:
            if check_all_pairs(f):
                counter[0] += 1
            return
        for v in choices[idx]:
            f[idx] = v
            rec(idx+1)
        f[idx] = None
    rec(0)
    return counter[0]

# ---- Case A: f(0)=1, all f(a) in {1,7,9,15} ----
print("=== Case A: f(0)=1, all f(a) in {1,7,9,15} ===")
count_A = 0
for hom in range(2):
    choices = []
    for a in range(16):
        if a == 0:
            choices.append([1])
        elif hom == 0:
            choices.append([1, 9])
        else:
            if a % 2 == 0:
                choices.append([1, 9])
            else:
                choices.append([7, 15])
    c = enumerate_case(choices)
    print(f"  hom={hom}: {c}")
    count_A += c
print(f"Case A total: {count_A} (expected {2**16})")

# ---- Case B (including A): even -> {1,7,9,15}, odd -> {0,4,8,12} ----
print("\n=== Case B: even -> {1,7,9,15}, odd -> {0,4,8,12} ===")
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
                if a % 4 == 2:
                    choices.append([7, 15])
                else:
                    choices.append([1, 9])
        else:
            choices.append([0, 4, 8, 12])
    c = enumerate_case(choices)
    print(f"  hom={hom}: {c}")
    count_B += c
print(f"Case B total: {count_B}")
print(f"Case B\\A: {count_B - count_A} (expected {2**24})")

# ---- Case C: even -> {1,7,9,15}, odd -> {2,6,10,14} ----
print("\n=== Case C: even -> {1,7,9,15}, odd -> {2,6,10,14} ===")
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
                if a % 4 == 2:
                    choices.append([7, 15])
                else:
                    choices.append([1, 9])
        else:
            choices.append([2, 6, 10, 14])
    c = enumerate_case(choices)
    print(f"  hom={hom}: {c}")
    count_C += c
print(f"Case C total: {count_C}")
print(f"Case C\\A: {count_C - count_A} (expected {2**24})")

# ---- Case D: sampling (too large to enumerate) ----
print("\n=== Case D: sampling all-odd functions ===")
import random
random.seed(42)
sample_size = 200000
count_D_sample = 0
for _ in range(sample_size):
    hom = random.choice([0, 1])
    f = [0]*16
    f[0] = 1
    for a in range(1, 16):
        if hom == 0:
            f[a] = random.choice([1, 5, 9, 13])
        else:
            if a % 2 == 0:
                f[a] = random.choice([1, 5, 9, 13])
            else:
                f[a] = random.choice([3, 7, 11, 15])
    if check_all_pairs(f):
        count_D_sample += 1
print(f"Case D sample: {count_D_sample}/{sample_size} passed (expect ~{sample_size})")

# ---- Summary ----
print("\n=== Summary ===")
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
