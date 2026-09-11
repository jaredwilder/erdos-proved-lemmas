# Erdős #313 — fixed-`k` finiteness and the exact `k=3` solution

Author: Jared Wilder. Public release: 2026-09-11.

Fix a positive integer `k`. Consider solutions in distinct primes

`p_1 < ... < p_k`

and a positive integer `m` of

`sum_i 1/p_i = 1 - 1/m`.

## Theorem 1 — the denominator is forced

Let

`P=prod_i p_i`.

Then every solution satisfies

`m=P`.

### Proof

Clearing denominators gives

`m sum_i P/p_i + P = mP`.

Reducing modulo `p_i` shows `p_i|m` for every `i`, hence `P|m`. Rearranging the same identity gives

`P = m(P-sum_i P/p_i)`,

so `m|P`. Therefore `m=P`.

The equation is thus equivalent to

`sum_i 1/p_i + 1/P = 1`.

## Theorem 2 — fixed-`k` finiteness

For every fixed `k`, there are only finitely many solutions.

After fixing `p_1,...,p_j`, put

`R_j=1-sum_{i=1}^j 1/p_i > 0`.

Since the remaining `k-j` prime reciprocals and the positive `1/P` term are each bounded above by the scale `1/p_(j+1)`, one obtains a finite upper bound for `p_(j+1)` depending on the fixed prefix and `k`. Thus the search tree has finite branching and fixed depth.

Consequently any infinite family of solutions must have unbounded `k`.

## Theorem 3 — the `k=3` case is unique

For three distinct primes, the unique solution is

`(p_1,p_2,p_3)=(2,3,7)`,

with

`m=42`.

### Proof

If `p_1>=3`, then the left side is at most

`1/3+1/5+1/7+1/(3*5*7)=72/105<1`,

so `p_1=2`.

If then `p_2>=5`, the left side is at most

`1/2+1/5+1/7+1/(2*5*7)=60/70<1`,

so `p_2=3`.

The equation becomes

`1/2+1/3+1/p+1/(6p)=1`.

Multiplying by `6p` gives

`5p+7=6p`,

hence `p=7`.

Finally

`1/2+1/3+1/7+1/42=1`,

so the solution exists and `m=2*3*7=42`.

## Scope

The fixed-`k` finiteness theorem is general; the explicit classification above is only for `k=3`. Historical novelty remains a separate literature question.