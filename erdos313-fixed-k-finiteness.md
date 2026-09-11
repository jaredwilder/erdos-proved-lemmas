# Erdős #313 — fixed-k finiteness for reciprocal-prime solutions

Author: Jared Wilder. Public release: 2026-09-11.

Fix a positive integer `k`. Consider solutions in distinct primes

`p_1 < ... < p_k`

and a positive integer `m` of

`Σ_i 1/p_i = 1 - 1/m`.

## Theorem

For every fixed `k`, there are only finitely many such solutions. Consequently, any infinite family of solutions must have unbounded `k`.

### Step 1: the denominator is forced

Let `P=Π_i p_i`. Clearing denominators in

`Σ_i 1/p_i + 1/m = 1`

gives

`m Σ_i P/p_i + P = mP`.

Reducing modulo `p_i` shows `p_i|m` for every `i`, hence `P|m`. The same identity also gives

`P = m(P-Σ_i P/p_i)`,

so `m|P`. Therefore

`m=P`.

### Step 2: finite branching

The equation becomes

`Σ_i 1/p_i + 1/P = 1`.

After fixing `p_1,...,p_j`, let

`R_j = 1 - Σ_{i=1}^j 1/p_i > 0`.

Since the remaining primes are at least `p_{j+1}`,

`R_j ≤ (k-j+1)/p_{j+1}`,

so

`p_{j+1} ≤ (k-j+1)/R_j`.

Thus only finitely many next primes are possible at each level, and the recursion has fixed depth `k`.

This is a complete fixed-`k` finiteness theorem. Historical novelty remains a separate literature question.
