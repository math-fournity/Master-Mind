#!/usr/bin/env python3
"""
Verify the case analysis for f: Z/16Z -> Z/16Z satisfying
  f(a)^2 + f(b)^2 + f(a+b)^2 ≡ 1 + 2 f(a) f(b) f(a+b)  (mod 16)

Case analysis for f(0)=1:
  Case A: g(a)=0 for all a (f(a)^2 ≡ 1, f(a) ∈ {1,7,9,15})
  Case B\A: g(a) ∈ {0,15}, B=even (f^2≡1), A=odd (f^2≡0, f∈{0,4,8,12})
  Case C\A: g(a) ∈ {0,3}, B=even (f^2≡1), A=odd (f^2≡4, f∈{2,6,10,14})
  Case D\A: g(a) ∈ {0,8}, all odd, not all f^2≡1

Expected:
  |A| = 2^16
  |B\A| = 2^24
  |C\A| = 2^24
  |D\A| = 2^31 - 2^16
  N_1 = 2^25 + 2^31

For f(0)=5 (and 13): all odd, 2*4^15 = 2^31
For f(0)=9 (and 1): same as f(0)=1

N = 2*N_1 + 2*N_5 = 2*(2^25+2^31) + 2*2^31 = 2^26 + 2^33
"""

# First, let's verify by brute force on a smaller group: Z/8Z mod 8
# to validate the approach

def count_solutions_mod8():
    """Brute force count for Z/8Z mod 8."""
    N = 0
    # f: Z/8Z -> Z/8Z, 8^8 = 16M configurations
    # Too many for brute force, use DFS
    
    def check_all(f, mod):
        for a in range(mod):
            for b in range(mod):
                x, y, z = f[a], f[b], f[(a+b)%mod]
                if (x*x + y*y + z*z - 1 - 2*x*y*z) % mod != 0:
                    return False
        return True
    
    # For mod 8, f(0) in {1, 5}
    total = 0
    for f0 in [1, 5]:
        for f1 in range(8):
            f = [None]*8
            f[0] = f0
            f[1] = f1
            count = [0]
            
            def dfs(k):
                if k == 8:
                    if check_all(f, 8):
                        count[0] += 1
                    return
                for v in range(8):
                    f[k] = v
                    # Quick check: all pairs (a,b) with a+b=k mod 8, a,b < k
                    ok = True
                    for a in range(k):
                        b = (k - a) % 8
                        if b >= k:
                            continue
                        x, y, z = f[a], f[b], f[k]
                        if (x*x + y*y + z*z - 1 - 2*x*y*z) % 8 != 0:
                            ok = False
                            break
                    if ok:
                        dfs(k+1)
                    f[k] = None
            
            dfs(2)
            total += count[0]
            print(f"  mod 8, f(0)={f0}, f(1)={f1}: {count[0]} solutions")
    
    return total

# Actually, even mod 8 with DFS might be slow. Let me try mod 4 first.

def count_solutions_mod4():
    """Brute force count for Z/4Z mod 4."""
    total = 0
    for f0 in range(4):
        for f1 in range(4):
            for f2 in range(4):
                for f3 in range(4):
                    f = [f0, f1, f2, f3]
                    ok = True
                    for a in range(4):
                        for b in range(4):
                            x, y, z = f[a], f[b], f[(a+b)%4]
                            if (x*x + y*y + z*z - 1 - 2*x*y*z) % 4 != 0:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        total += 1
    return total

print("=== Mod 4 ===")
n4 = count_solutions_mod4()
print(f"Total solutions mod 4: {n4}")

# Now let's do mod 8 with DFS
print("\n=== Mod 8 ===")
n8 = count_solutions_mod8()
print(f"Total solutions mod 8: {n8}")
