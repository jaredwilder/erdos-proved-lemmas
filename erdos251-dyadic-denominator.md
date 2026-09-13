# Erdős #251 — exact dyadic denominator of finite partial sums

**Author:** Jared Wilder  
**Release:** 2026-09-11

## Theorem

For the finite partial sums used in the #251 campaign, the reduced denominator is exactly

\[
\boxed{2^{N-1}}
\]

for every `N>=2`; `N=1` is the exceptional initial case.

The campaign proof is the standard common-denominator parity argument: put the finite sum over the common denominator `2^(N-1)`. After normalization, exactly one numerator contribution is odd while all remaining contributions are even. Hence the numerator is odd and no factor 2 cancels. Therefore the reduced denominator retains the full factor `2^(N-1)`.

## Scope boundary

This is an exact **finite-partial-sum invariant**. It does not by itself prove irrationality of the infinite series: a separate tail-denominator separation theorem would be needed to pass from exact finite denominators to the infinite limit.

The recovered estate classifies the theorem as `DIRECT PROOF IN ARCHIVE`; a formalization mission (`exact_power_two_denominator`) was also queued but is not represented here as kernel-checked.

## Novelty boundary

No historical novelty claim is made. The purpose of this release is to prevent a proved finite invariant from remaining buried merely because it was insufficient for the parent close.

## Explicit indexing and companion statement

Write `p_1=2,p_2=3,...` for the primes. In the origin-0 convention used here,

`T_N = sum_{j=0}^{N-1} p_{j+1}/2^j`.

The [origin-1 statement and proof](https://github.com/jaredwilder/erdos-findings-ledger/blob/main/theorems/ERDOS-251-DYADIC-PREFIX-DENOMINATOR.md) instead uses `S_N=sum_{n=1}^N p_n/2^n`. Since `T_N=2S_N`, the reduced denominators for `N≥2` are `2^(N−1)` and `2^N`, respectively. For `N=1`, both reduced denominators are 1. These are equivalent finite invariants with different indexing conventions.
