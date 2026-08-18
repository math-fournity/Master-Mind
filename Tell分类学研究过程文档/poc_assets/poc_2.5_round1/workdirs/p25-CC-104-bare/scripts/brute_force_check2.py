"""
Extended brute-force check for n=9,10,12.
Also check which alpha values give valid affine arrangements.
"""
from itertools import permutations
from math import gcd

def crosses(p1, p2, p3, p4, n):
    arc = set()
    curr = (p1 + 1) % n
    while curr != p2:
        arc.add(curr)
        curr = (curr + 1) % n
    return (p3 in arc) != (p4 in arc)

def check_arrangement(perm, n):
    pos = [0] * n
    for i in range(n):
        pos[perm[i]] = i
    for s in range(n):
        pairs = []
        for a in range(n):
            b = (s - a) % n
            if a < b:
                pairs.append((a, b))
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                a1, b1 = pairs[i]
                a2, b2 = pairs[j]
                if crosses(pos[a1], pos[b1], pos[a2], pos[b2], n):
                    return False
    return True

def count_arrangements(n):
    count = 0
    valid_perms = []
    elements = list(range(1, n))
    for perm_rest in permutations(elements):
        perm = (0,) + perm_rest
        if check_arrangement(perm, n):
            count += 1
            valid_perms.append(perm)
    return count, valid_perms

def euler_phi(n):
    return sum(1 for i in range(1, n + 1) if gcd(i, n) == 1)

def affine_perm(n, alpha, beta=0):
    """Generate affine permutation p(x) = alpha*x + beta mod n."""
    return tuple((alpha * x + beta) % n for x in range(n))

# Check n=9, 10
for n in [9, 10]:
    result, valid = count_arrangements(n)
    phi = euler_phi(n)
    print(f"n={n}: valid={result}, phi(n)={phi}, match={result==phi}")
    
    # Check that all valid arrangements are affine
    affine_set = set()
    for alpha in range(1, n):
        if gcd(alpha, n) == 1:
            perm = affine_perm(n, alpha)
            # Fix element 0 at position 0: we need perm[0]=0, so beta=0
            # But our convention: perm[i] = element at position i
            # p(x) = alpha*x means element at position x is alpha*x
            # So perm = (alpha*0, alpha*1, ..., alpha*(n-1)) mod n
            if perm[0] == 0:
                affine_set.add(perm)
    
    valid_set = set(valid)
    print(f"  Affine arrangements with beta=0: {len(affine_set)}")
    print(f"  Valid == Affine: {valid_set == affine_set}")
    if valid_set != affine_set:
        print(f"  In valid but not affine: {valid_set - affine_set}")
        print(f"  In affine but not valid: {affine_set - valid_set}")
