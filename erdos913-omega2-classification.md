# Erdős #913 — exact classification when omega(n(n+1))=2 and the two exponents are distinct

Author: Jared Wilder. Public release: 2026-09-11.

Let `omega(m)` denote the number of distinct prime factors of `m`.

## Theorem

Suppose

`omega(n(n+1))=2`,

and write the two coprime consecutive factors as prime powers

`n=p^a`, `n+1=q^b`,

with distinct positive exponents `a!=b`.

Then exactly one of the following occurs:

1. `n=8`;
2. `n=2^a` and `2^a+1` is prime — a Fermat-prime predecessor branch;
3. `n=2^b-1` is prime and `n+1=2^b` — a Mersenne-prime branch.

## Proof

Because `gcd(n,n+1)=1` and the product has exactly two distinct prime factors, each of `n` and `n+1` must be a power of a single prime.

If both exponents satisfy `a,b>=2`, then `q^b-p^a=1` is an equation between consecutive nontrivial perfect powers. Catalan-Mihailescu gives the unique solution

`3^2-2^3=1`,

so `n=8`.

Otherwise one exponent is 1. Since one of two consecutive integers is even, the other prime-power factor must then be a power of 2.

If `n=2^a`, the exponent on `n+1` is 1, so `n+1=2^a+1` is prime.

If `n+1=2^b`, the exponent on `n` is 1, so `n=2^b-1` is prime.

These are exactly the stated Fermat-predecessor and Mersenne branches.

## Scope

This classifies the stated `omega=2`, distinct-exponent stratum. It does not classify cases with more distinct prime factors or with equal exponents.

Historical novelty is not claimed.