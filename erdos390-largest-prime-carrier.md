# Erdős #390 — largest-prime carrier bound

Author: Jared Wilder  
Public release: 2026-09-11

Let `p_*(n)` be the largest prime at most `n`. Consider a factorization

`n! = a_1 a_2 ... a_k`

with

`n < a_1 < ... < a_k = m`.

## Theorem

If `p_*(n)>n/2`, then every such factorization satisfies

`m >= 2 p_*(n)`.

Consequently, whenever the extremal function `f(n)` of Erdős #390 is defined,

`f(n) >= 2 p_*(n)`.

## Proof

Put `p=p_*(n)`. Since `p>n/2`, the exponent of `p` in `n!` is exactly one.

Therefore some factor `a_i` on the right is divisible by `p`. Every `a_i` is strictly greater than `n`, while `p<=n`. The first positive multiple of `p` above `n` is at least `2p`; under `p>n/2`, indeed `2p>n`.

Thus `a_i>=2p`, and hence the largest factor `m>=a_i>=2p`.

## Scope

This is a one-sided structural lower bound. It does not determine the asymptotic constant asked for in Erdős #390. The raw chronology contains inconsistent finite-value computations and failed asymptotic upgrades; none of those are used here.

## License

Apache-2.0.
