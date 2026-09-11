# Erdős #156 — repaired maximal-Sidon N^(1/3) barrier

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

Let `A⊆[N]` be a maximal Sidon set and put `m=|A|`.

## Theorem

\[
\boxed{N\le m+m^3+m^2.}
\]

Hence `m=Omega(N^(1/3))`.

## Proof

For every `x∈[N]\A`, maximality says that `A∪{x}` is not Sidon. Since all pair sums internal to `A` were already distinct, a new collision must involve `x`. There are two essential forms:

1. `x+a=b+c` for `a,b,c∈A`;
2. `2x=a+b` for `a,b∈A`.

The first form gives at most `m^3` possible excluded values `x`; the second gives at most `m^2`. Adding the `m` elements already in `A` gives

\[
N\le m+m^3+m^2.
\]

## Correction record

The raw campaign proof used only `(A+A)-A` and silently omitted the second blocker `2x=a+b`. The bound survives after adding that missing case; the broken proof does not.

## Scope

This is a universal lower barrier for the size of a maximal Sidon subset of `[N]`, not a close of the parent problem. Historical novelty is not claimed; folklore risk is substantial.

The original extraction remains archived in `unpublished-math-papers/erdos156-maximal-sidon-barrier/`.
