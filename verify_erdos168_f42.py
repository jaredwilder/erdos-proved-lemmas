#!/usr/bin/env python3
"""Exact verifier for the released Erdős #168 finite value F(42)=34.

F(n) is the largest subset of [1,n] containing no triple {k,2k,3k}.
The complement of an avoiding set is a hitting set for all such triples, so
F(n)=n-tau where tau is the exact minimum hitting-set size.

Standard library only. Exit 0 means all checks reproduced.
"""


def F(n):
    triples = [(k, 2*k, 3*k) for k in range(1, n//3 + 1)]

    def first_uncovered(chosen):
        for t in triples:
            if not any(v in chosen for v in t):
                return t
        return None

    def search(chosen, best):
        t = first_uncovered(chosen)
        if t is None:
            return min(best, len(chosen))
        if len(chosen) + 1 >= best:
            return best
        for v in t:
            best = min(best, search(chosen | {v}, best))
        return best

    return n - search(frozenset(), n)


def brute_F(n):
    triples = [(k, 2*k, 3*k) for k in range(1, n//3 + 1)]
    best = 0
    for mask in range(1 << n):
        S = {i + 1 for i in range(n) if (mask >> i) & 1}
        if len(S) <= best:
            continue
        if not any(all(v in S for v in t) for t in triples):
            best = len(S)
    return best


def main():
    for n in (6, 9, 12, 15, 18):
        a, b = F(n), brute_F(n)
        assert a == b, (n, a, b)
    expected = {10: 8, 20: 16, 30: 24, 42: 34}
    for n, want in expected.items():
        got = F(n)
        print(f"F({n})={got}")
        assert got == want, (n, got, want)
    print("PASS: exact branch-and-bound gives F(42)=34")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
