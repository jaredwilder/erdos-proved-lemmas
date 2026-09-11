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
