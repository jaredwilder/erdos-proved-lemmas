#!/usr/bin/env python3
"""Verify the bounded Erdős #137 consecutive-powerful census through 300,000."""

LIMIT = 300_000

spf = list(range(LIMIT + 2))
for p in range(2, int((LIMIT + 1) ** 0.5) + 1):
    if spf[p] == p:
        for m in range(p * p, LIMIT + 2, p):
            if spf[m] == m:
                spf[m] = p


def powerful(n: int) -> bool:
    if n == 1:
        return True
    x = n
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e < 2:
            return False
    return True

starts = [n for n in range(2, LIMIT) if powerful(n) and powerful(n + 1)]
expected = [8, 288, 675, 9800, 12167, 235224]
assert starts == expected, (starts, expected)

triples = [n for n in range(2, LIMIT - 1)
           if powerful(n) and powerful(n + 1) and powerful(n + 2)]
assert triples == [], triples

print('PASS')
print('pair starts:', starts)
print('triple starts:', triples)
