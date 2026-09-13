#!/usr/bin/env python3
"""Replay the finite least-totient-preimage correction for Erdős #51.

Standard library only.  This is a finite census, not an asymptotic theorem.
"""
from array import array
from math import gcd

N = 2_000_000
MAX_A = 1_000_000

phi = array('I', range(N + 1))
for p in range(2, N + 1):
    if phi[p] == p:
        for m in range(p, N + 1, p):
            phi[m] -= phi[m] // p

least = array('I', [0]) * (MAX_A + 1)
for n in range(1, N + 1):
    a = phi[n]
    if a <= MAX_A and least[a] == 0:
        least[a] = n

assert least[5760] == 5917
assert phi[15015] == 5760
assert phi[5917] == 5760

# Maximize exactly by cross multiplication.
best_a = 1
best_n = least[1]
maximizers = []
for a in range(1, MAX_A + 1):
    n = least[a]
    if not n:
        continue
    lhs = n * best_a
    rhs = best_n * a
    if lhs > rhs:
        best_a, best_n = a, n
        maximizers = [(a, n)]
    elif lhs == rhs:
        maximizers.append((a, n))

g = gcd(best_n, best_a)
reduced = (best_n // g, best_a // g)
assert reduced == (11985, 5888), reduced
assert maximizers == [(5888, 11985), (276736, 563295)], maximizers

print('PASS')
print('n_5760 =', least[5760])
print('max reduced ratio = 11985/5888')
print('maximizers =', maximizers)
