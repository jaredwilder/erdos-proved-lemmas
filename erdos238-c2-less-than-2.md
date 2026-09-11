# Erdős #238 — the full `0<c_2<2` slice

Author: Jared Wilder. Public release: 2026-09-11.

## Canonical question

Given constants `c_1,c_2>0`, must every sufficiently large `x` contain more than `c_1 log x` consecutive primes, all at most `x`, such that the difference between any two of them is greater than `c_2`?

## Theorem

For every fixed `c_1>0` and every

`0<c_2<2`,

the answer is yes for all sufficiently large `x`.

## Proof

Every two distinct odd primes differ by an even positive integer, hence by at least `2`.

Therefore when `c_2<2`, every block of distinct odd primes automatically satisfies the required pairwise separation.

It remains only to ensure that there are more than `c_1 log x` odd primes at most `x`. Standard prime-counting growth gives

`pi(x) ~ x/log x`,

and in particular

`pi(x)-1 > c_1 log x`

for all sufficiently large `x`.

Taking any block of more than `c_1 log x` consecutive odd primes below `x` proves the claim.

## Scope / literature boundary

This resolves the entire easy separation range `0<c_2<2`. It does not address `c_2>=2`, where actual large-gap structure becomes load-bearing. The maintained Erdős Problems page still lists the general problem as open and records stronger classical partial results in other parameter regimes.

Historical novelty is not claimed.