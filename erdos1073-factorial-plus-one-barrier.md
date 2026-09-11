# Erdős #1073 — factorial-plus-one divisor barrier

Author: Jared Wilder  
Public release: 2026-09-11

Erdős #1073 studies composite integers `u` that divide `n!+1` for some `n`.

## Theorem

If

`u>1` and `u | n!+1`,

then every prime factor `p` of `u` satisfies

`p>n`.

Consequently, if `u` is composite then

`u>n^2`.

Equivalently, every composite witness `u<x` can only arise from an index

`n<sqrt(x)`.

## Proof

Let `p` be any prime divisor of `u`. Since `u|n!+1`,

`n! ≡ -1 (mod p)`.

If `p<=n`, then `p|n!`, so the same congruence would give

`0 ≡ -1 (mod p)`,

a contradiction. Hence every prime factor of `u` exceeds `n`.

If `u` is composite, it contains at least two prime factors counted with multiplicity. Each exceeds `n`, so

`u>n^2`.

## Scope

This is a structural reduction, not the canonical `A(x)<=x^{o(1)}` bound. Summing crude divisor estimates over `n<sqrt(x)` only reaches approximately an `x^{1/2+o(1)}` scale; the subpolynomial target requires substantially more arithmetic information about divisors of `n!+1`.

A historical raw route tried to obtain a polynomial-size counterexample family from a Wilson-type assertion for odd prime powers. That close was separately rejected; none of it is used here.

## License

Apache-2.0.
