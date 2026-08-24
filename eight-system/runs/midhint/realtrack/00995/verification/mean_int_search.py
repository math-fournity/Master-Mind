"""Verify mean-integer classification via residue placement search (fixed)."""
import sys

def search(n, node_limit=30_000_000):
    remaining = [n]*n
    nodes = [0]

    def row_options(rem):
        opts = []
        cur = []
        def rec(r, need):
            if r == n:
                if need % n == 0 and len(cur) == n:
                    opts.append(tuple(cur))
                return
            maxc = min(rem[r], n - len(cur))
            for c in range(maxc, -1, -1):
                cur.extend([r]*c)
                rec(r+1, (need - r*c) % n)
                for _ in range(c): cur.pop()
        rec(0, 0)
        return opts

    def bt(rows_left, rem, colsum):
        nodes[0] += 1
        if nodes[0] > node_limit:
            raise TimeoutError
        if rows_left == 0:
            return all(c % n == 0 for c in colsum)
        for opt in row_options(rem):
            rem2 = list(rem)
            for r in opt: rem2[r] -= 1
            cs2 = list(colsum)
            for j, r in enumerate(opt):
                cs2[j] = (cs2[j] + r) % n
            bt.cache = None
            if bt(rows_left-1, rem2, cs2):
                return True
        return False
    try:
        return bt(n, remaining, [0]*n), nodes[0]
    except TimeoutError:
        return None, nodes[0]

for n in [2, 3, 4, 5]:
    found, nodes = search(n)
    verdict = 'POSSIBLE' if found else ('IMPOSSIBLE' if found is False else 'TIMEOUT')
    print(f"n={n}: {verdict} ({nodes} nodes)")
