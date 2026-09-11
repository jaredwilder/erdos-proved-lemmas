# Erdős #289 — all-prime p-adic obstruction for integral reciprocal sums

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `S` be a finite set of integers at least 2 and suppose

`Σ_{n∈S} 1/n ∈ Z`.

Fix a prime `p` and define

`U_p = Σ_{n∈S, p|n} p/n`.

Then

`v_p(U_p) ≥ 1`.

### Proof

Write

`T = U_p/p + V_p`,

where every denominator occurring in `V_p` is prime to `p`. Hence `v_p(V_p)≥0`. Since `T` is an integer, `v_p(T)≥0`, so `U_p/p = T-V_p` is p-adically integral. Therefore `v_p(U_p)-1≥0`.

## Consequences

The case `p=2` recovers the classical consecutive-interval obstruction: no nontrivial finite sum

`1/a + 1/(a+1) + ... + 1/b`

with `b>a` is an integer.

A separate exact reduction for reciprocal-interval decompositions of 1 shows that if the denominator 2 occurs, its interval is forced to be `[2,3]`, leaving a tail of exactly `1/6`. A finite formal check rules out a single interval `[a,b]` with `5≤a<b≤60` summing to `1/6`.

The all-prime theorem is unconditional; the `b≤60` statement is finite and should be read at that exact range.
