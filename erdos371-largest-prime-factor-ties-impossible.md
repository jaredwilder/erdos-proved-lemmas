# Erdős #371 — consecutive integers cannot tie in largest prime factor

**Author:** Jared Wilder  
**Status:** exact universal child theorem; parent density/balance question remains open  
**Historical novelty:** not asserted

Let `P(n)` denote the largest prime factor of `n` for `n>=2`.

## Theorem

For every integer `n>=2`,

\[
\boxed{P(n)\ne P(n+1).}
\]

In fact the prime-factor sets of `n` and `n+1` are disjoint.

## Proof

Consecutive integers are coprime:

\[
\gcd(n,n+1)=1.
\]

If some prime `p` divided both `n` and `n+1`, then it would divide their difference

\[
(n+1)-n=1,
\]

which is impossible.

Thus no prime divides both consecutive integers. In particular their largest prime factors cannot coincide.

## Consequence for #371

Any comparison of consecutive largest prime factors has only the two strict cases

\[
P(n)<P(n+1)
\qquad\text{or}\qquad
P(n)>P(n+1).
\]

There is no tie class to account for.

The recovered #371 campaign studies the asymptotic balance/density of these two strict comparison classes. Tie-freeness is an exact structural simplification, but it does not determine that density. Later falsifier passes explicitly preserved this lemma while refusing any promotion to the parent asymptotic close.

No novelty claim is made for the elementary coprimality observation.