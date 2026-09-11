# Erdős #891 — semantic scope correction: `ω`, not `Ω`

**Author:** Jared Wilder  
**Release-day audit:** 2026-09-11  
**Status:** correction / negative audit of a historical false close

## Canonical statement

Let

\[
P_k=p_1p_2\cdots p_k
\]

be the product of the first `k` primes. Erdős #891 asks whether, for every `k>=2` and all sufficiently large `n`, the interval

\[
[n,n+P_k)
\]

contains an integer having **more than `k` distinct prime divisors**.

Write `ω(m)` for the number of distinct prime divisors and `Ω(m)` for the number counted with multiplicity.

The canonical problem is the `ω` problem.

## The archived false-close route

Several historical campaign records silently used `Ω`. Under that altered statement the problem becomes immediate.

For `n>P_k`, put

\[
t=\left\lceil\frac n{P_k}\right\rceil,
\qquad m=P_k t.
\]

Then

\[
n\le m<n+P_k,
\]

and `t>=2`, so

\[
\Omega(m)=\Omega(P_k)+\Omega(t)=k+\Omega(t)\ge k+1.
\]

This is a correct theorem about **prime factors counted with multiplicity**. It does **not** solve #891.

The inference fails for distinct prime factors because multiplying `P_k` by a number supported on the same first `k` primes need not increase `ω`. For example, a multiple such as `2P_k` still has only the same `k` distinct prime divisors.

## Why this is decisively a semantic mismatch

The current formal statement uses Mathlib's arithmetic function `ω`, and the historical/source interpretation is distinct prime divisors. The public problem record also says the question is unknown even for `k=2`: whether every sufficiently late interval of six consecutive integers contains a number with at least three distinct prime divisors. That would be trivial under the `Ω` interpretation, which is an immediate sanity check.

Therefore every archived route whose closure step is

> “a primorial-length interval contains a multiple of `P_k`, hence it has >k prime factors”

is reclassified as an **`Ω`-variant theorem only**, not a close of Erdős #891.

## Surviving mathematical asset

The following statement remains correct and is worth preserving:

> For every `k>=2` and every `n>P_k`, `[n,n+P_k)` contains an integer `m` with `Ω(m)>=k+1`.

It has the one-line least-multiple proof above. This is elementary and not presented as novel.

## Release consequence

- Erdős #891 remains **OPEN**.
- Historical `TARGET_CLOSED` / branch-close labels produced under the `Ω` reading are superseded.
- Finite computations that explicitly used `ω` remain finite evidence and are not affected by this correction.
- No novelty credit is assigned to the `Ω` variant.

This correction is public so that later mining cannot accidentally promote a notation drift into a theorem claim.
