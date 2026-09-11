# Erdős #1210 — endpoint constraint on a uniform additive constant

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

Erdős #1210 asks whether there is a uniform bounded additive term in the inequality

`sum_{a in A} 1/(n-a) <= sum_{p<n, p prime} 1/p + O(1)`

for sets `A subset [1,n)` whose distinct elements are pairwise coprime.

If this is written with one explicit uniform constant `C` as

`sum_{a in A} 1/(n-a) <= sum_{p<n} 1/p + C`,

then necessarily

> **`C >= 1`.**

Indeed take `n=2` and `A={1}`. The left side is `1`, while there are no primes below 2, so the prime-reciprocal sum is `0`.

## Scope

This is only a sharp endpoint constraint on any proposed uniform explicit constant. It does **not** prove that such a bounded constant exists and does not resolve Erdős #1210.

## Provenance

Recovered in the September 2026 Pass-3 estate audit as `P3-G016`.