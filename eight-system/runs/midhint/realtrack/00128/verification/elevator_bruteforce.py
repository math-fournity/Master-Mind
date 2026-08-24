"""Gate-B verification for polymath_00128 (elevator).
Enumerate all stop orders s1..s10 (permutation of floors 1..10).
Distance = |s1-0| + sum |s_{i+1}-s_i|. Constraint: consecutive stops alternate parity.
Both readings tested: (a) alternation only between stops; (b) also from start floor 0."""
from itertools import permutations

def dist(seq):
    total = abs(seq[0] - 0)
    for i in range(len(seq)-1):
        total += abs(seq[i+1] - seq[i])
    return total

def parity_alt(seq, strict_from_start):
    prev = 0 if strict_from_start else None
    for s in seq:
        if prev is not None and (s % 2) == (prev % 2):
            return False
        prev = s
    return True

for strict in (False, True):
    best = -1; best_seq = None
    for seq in permutations(range(1, 11)):
        if parity_alt(seq, strict):
            d = dist(seq)
            if d > best:
                best = d; best_seq = seq
    print(f"strict_from_start={strict}: max_floors={best} ({best*4}m) via {best_seq}")
# also verify the published constructions
for name, seq in [("sol1", (7,2,9,4,5,10,3,8,1,6)), ("sol2", (9,2,7,4,5,10,1,8,3,6))]:
    print(f"{name}: dist={dist(seq)} floors, parity_alt={parity_alt(seq, True)}")
# and the unconstrained max (original F.2280 check)
best = -1
for seq in permutations(range(1, 11)):
    d = dist(seq)
    if d > best: best = d
print(f"unconstrained max = {best} floors (solution cites 55)")
