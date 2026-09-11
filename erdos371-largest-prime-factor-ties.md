# Erdős #371 — consecutive integers have different largest prime factors

Author: Jared Wilder. Public release: 2026-09-11.

Let `P(n)` be the largest prime factor of `n>=2`.

## Theorem

For every `n>=2`,

`P(n) != P(n+1)`.

## Proof

If `P(n)=P(n+1)=p`, then the prime `p` divides both consecutive integers, so

`p | gcd(n,n+1)=1`,

impossible.

This excludes ties. Questions about the sign or density of `P(n+1)-P(n)` are separate.
