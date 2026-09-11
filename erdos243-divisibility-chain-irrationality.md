# Erdős #243 — divisibility-chain irrationality criterion

**Author:** Jared Wilder  
**Recovered:** September 2026 theorem audit  
**Subject-home promotion:** 2026-09-11

Let `a_1,a_2,...` be positive integers. Suppose that eventually

`a_m | a_(m+1)`

and

`a_(m+1)/a_m -> infinity`.

Then

> **`sum_{m>=1} 1/a_m` is irrational.**

The same conclusion holds if the divisibility and growth hypotheses begin after any finite initial segment.

## Proof

Discarding finitely many initial terms changes the sum by a rational number, so work on a tail where the divisibility chain holds.

Assume the tail sum equals `u/v` with positive integers `u,v`. Choose `M` so far out that all later ratios exceed a fixed `R>2v`. Because

`a_(M0) | a_(M0+1) | ... | a_M`,

multiplying by `v a_M` makes the rational side and every term through `M` integral. Hence

`v a_M sum_{m>M} 1/a_m`

must be an integer.

It is positive. But `a_(M+j)>=R^j a_M`, so

`0 < v a_M sum_{m>M} 1/a_m <= v sum_{j>=1} R^(-j) = v/(R-1) < 1`,

impossible for an integer.

## Scope and literature

This is a restricted structural theorem relevant to Erdős #243, not the strongest known statement around the parent problem. The audit marks the mechanism as folklore-risk because it is a classical Cantor-series-style argument; no historical priority claim is made.

Original extraction: `jaredwilder/unpublished-math-papers/erdos243-divisibility-irrationality/`.
