"""
Brute-force check: count valid circular arrangements of Z/nZ
such that for every sum s, the matching {a, s-a} is non-crossing.
Fix element 0 at position 0 (quotient by rotation).
"""
from itertools import permutations
from math import gcd

def crosses(p1, p2, p3, p4, n):
    """Check if chord {p1,p2} crosses chord {p3,p4} on circle of n points."""
    # Arc from p1 to p2 (going forward, exclusive of endpoints)
    arc = set()
    curr = (p1 + 1) % n
    while curr != p2:
        arc.add(curr)
        curr = (curr + 1) % n
    in1 = p3 in arc
    in2 = p4 in arc
    return in1 != in2

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
    elements = list(range(1, n))
    for perm_rest in permutations(elements):
        perm = (0,) + perm_rest
        if check_arrangement(perm, n):
            count += 1
    return count

def euler_phi(n):
    return sum(1 for i in range(1, n + 1) if gcd(i, n) == 1)

for n in [4, 5, 6, 7, 8]:
    result = count_arrangements(n)
    phi = euler_phi(n)
    print(f"n={n}: valid={result}, phi(n)={phi}, match={result==phi}")
