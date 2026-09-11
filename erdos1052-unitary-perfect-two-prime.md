# Erdős #1052 — unitary-perfect integers with at most two prime factors

Author: Jared Wilder. Public release: 2026-09-11.

For `n=∏p_i^{a_i}`, let

`sigma*(n)=∏(p_i^{a_i}+1)`.

A unitary-perfect integer satisfies `sigma*(n)=2n`.

## Theorem

1. No odd unitary-perfect integer exceeds 1.
2. Among unitary-perfect integers with at most two distinct prime factors, the only one is `6`.

## Proof

If `n>1` is odd with at least two distinct prime factors, every factor `p_i^{a_i}+1` is even, so `sigma*(n)` is divisible by 4 while `2n` has 2-adic valuation 1. If `n=p^a` is an odd prime power, `p^a+1=2p^a` would force `p^a=1`.

Now write a two-prime example as `n=2^a q^b` with `q` odd. Then

`(2^a+1)(q^b+1)=2^(a+1)q^b`

rearranges to

`q^b(2^a-1)=2^a+1`.

Hence `2^a-1` divides 2. Being positive and odd, it equals 1, so `a=1`; then `q^b=3`, giving `n=6`. Directly, `sigma*(6)=12=2*6`.

This classifies the at-most-two-distinct-prime-factor stratum exactly.
