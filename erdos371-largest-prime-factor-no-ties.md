# Erdős #371 — consecutive integers cannot have the same largest prime factor

Author: Jared Wilder. Public release: 2026-09-11.

Let `P(n)` denote the largest prime factor of `n` for `n>=2`.

## Theorem

For every `n>=2`,

`P(n) != P(n+1)`.

## Proof

If `P(n)=P(n+1)=p`, then the same prime `p` divides both `n` and `n+1`. Hence

`p | gcd(n,n+1)=1`,

impossible.

## Scope

This is a universal local obstruction. It does not settle any density statement about inequalities such as `P(n)<P(n+1)` versus `P(n)>P(n+1)`.

Historical novelty is not claimed.